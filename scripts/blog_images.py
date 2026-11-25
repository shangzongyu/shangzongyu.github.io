"""上传独立 Markdown 文章的本地配图。"""

import hashlib
import html
import os
import re
import stat
import subprocess
from collections.abc import Iterator
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from urllib.parse import unquote

IMAGE_OWNER = "shangzongyu"
IMAGE_REPO = "blog-image"
IMAGE_BRANCH = "main"
RAW_URL = f"https://raw.githubusercontent.com/{IMAGE_OWNER}/{IMAGE_REPO}/{IMAGE_BRANCH}"

FRONTMATTER = re.compile(
    r"\A\ufeff?---[ \t]*\r?\n(.*?)(?:^---[ \t]*\r?(?:\n|\Z))", re.MULTILINE | re.DOTALL
)
COVER_FIELD = re.compile(
    r"""^featuredImage(?:Preview)?:[ \t]*(?:"(?P<double>[^"\r\n]*)"|'(?P<single>[^'\r\n]*)'|"""
    r"""(?P<plain>[^\r\n]*?))(?=[ \t]*(?:[ \t]#[^\r\n]*)?\r?$)""",
    re.MULTILINE,
)
BODY_IMAGE = re.compile(
    # 先跳过代码块、注释和行内代码，再查找图片链接。
    r"^[ \t]{0,3}(?P<fence>(?P<marker>[`~])(?P=marker){2,})(?!(?P=marker))[^\r\n]*\r?\n.*?"
    r"(?:^[ \t]{0,3}(?P=fence)(?P=marker)*[ \t]*\r?(?:\n|\Z)|\Z)"
    r"|<!--.*?(?:-->|\Z)"
    r"|(?<!`)(?P<ticks>`+)(?!`)(?:(?!\r?\n[ \t]*\r?\n).)*?(?<!`)(?P=ticks)(?!`)"
    r"|\\[!`<\\]"
    r"|!\[(?:\\.|\[[^\]\r\n]*\]|[^\]\\[\r\n])*\]\(\s*"
    r"(?:<(?P<angle>[^<>\r\n]+)>|(?P<inline>(?:\\.|[^\s()<>\\]|\([^()\r\n]*\))+))"
    r"""(?:\s+(?:"[^"\r\n]*"|'[^'\r\n]*'|\([^()\r\n]*\)))?\s*\)"""
    r"""|(?P<tag><img(?=\s)(?:[^"'<>]|"[^"]*"|'[^']*')*>)""",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)
HTML_ATTR = re.compile(
    r"""(?P<name>[^\s=<>/'"]+)(?:\s*=\s*(?:"(?P<double>[^"]*)"|"""
    r"""\'(?P<single>[^']*)\'|(?P<plain>[^\s<>"'=`]+)))?"""
)
MARKDOWN_ESCAPE = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])")


def image_destinations(text: str) -> Iterator[tuple[int, int, str]]:
    """返回可替换的链接在源码中的区间和链接内容。"""
    frontmatter = FRONTMATTER.match(text)
    body_start = 0
    if frontmatter:
        body_start = frontmatter.end()
        for field in COVER_FIELD.finditer(
            text, frontmatter.start(1), frontmatter.end(1)
        ):
            group = field.lastgroup
            yield *field.span(group), field[group]

    for match in BODY_IMAGE.finditer(text, body_start):
        group = match.lastgroup
        if group in {"angle", "inline"}:
            yield (
                *match.span(group),
                MARKDOWN_ESCAPE.sub(r"\1", html.unescape(match[group])),
            )
        elif group == "tag":
            for attr in HTML_ATTR.finditer(
                text, match.start() + len("<img"), match.end() - 1
            ):
                if attr["name"].lower() == "src" and attr.lastgroup != "name":
                    yield (
                        *attr.span(attr.lastgroup),
                        html.unescape(attr[attr.lastgroup]),
                    )
                    break


def referenced_images(article: Path, text: str) -> list[tuple[int, int, Path]]:
    assets = article.parent.resolve() / f"{article.stem}.assets"
    references = []
    for start, end, link in image_destinations(text):
        relative = Path(unquote(link))
        if not relative.parts or relative.parts[0] != assets.name:
            continue
        path = (assets.parent / relative).resolve()
        if not path.is_relative_to(assets) or not path.is_file():
            raise ValueError(f"配图不存在或不在文章的配图目录中：{relative}")
        references.append((start, end, path))
    return references


def upload_files(staged: list[Path], target: str, work_dir: Path) -> dict[Path, str]:
    expected = [f"{RAW_URL}/{target}/{path.name}" for path in staged]
    try:
        output = subprocess.run(
            [
                "upgit",
                "--uploader",
                "github",
                "--raw",
                "--format",
                "url",
                "--no-log",
                "--application-path",
                str(work_dir),
                "--target-dir",
                target,
                *map(str, staged),
            ],
            env={
                **os.environ,
                "UPGIT_USERNAME": IMAGE_OWNER,
                "UPGIT_REPO": IMAGE_REPO,
                "UPGIT_BRANCH": IMAGE_BRANCH,
            },
            capture_output=True,
            text=True,
            check=True,
            timeout=300,
        )
    except FileNotFoundError as error:
        raise ValueError("找不到 upgit，请使用 mise run blog:image。") from error
    except subprocess.CalledProcessError as error:
        # 配置解析错误可能带有 TOML 原文，只显示首行摘要。
        summary, _, _ = error.stderr.strip().partition("\n")
        raise ValueError(
            f"upgit 上传失败：{summary or f'退出码 {error.returncode}'}"
        ) from error
    except subprocess.TimeoutExpired as error:
        raise ValueError("upgit 上传超时，可重新运行命令。") from error

    if output.stdout.split() != expected:
        raise ValueError("upgit 返回的链接与预期的 GitHub 图床路径不一致。")
    return dict(zip(staged, expected, strict=True))


def upload_article_images(article: Path, posts: Path) -> int:
    original = article.read_bytes()
    text = original.decode("utf-8")
    references = referenced_images(article, text)
    if not references:
        return 0

    # 固定远端目录和文件名，重试时同一份内容仍对应原来的 URL。
    article_key = hashlib.sha256(
        article.relative_to(posts).as_posix().encode()
    ).hexdigest()[:20]
    with TemporaryDirectory(prefix="blog-images-") as tmp:
        work_dir = Path(tmp)
        images = {}
        staged = []
        for path in dict.fromkeys(path for _, _, path in references):
            content = path.read_bytes()
            suffix = path.suffix.lower()
            if not re.fullmatch(r"\.[a-z0-9]+", suffix):
                raise ValueError(f"配图需要有有效的文件扩展名：{path.name}")
            staged_path = work_dir / f"{hashlib.sha256(content).hexdigest()}{suffix}"
            images[path] = staged_path
            if not staged_path.exists():
                staged_path.write_bytes(content)
                staged.append(staged_path)
        urls = upload_files(staged, f"posts/{article_key}", work_dir)

    for start, end, path in reversed(references):
        text = text[:start] + urls[images[path]] + text[end:]

    # 上传全部成功后才替换文章，并检查编辑器是否在上传期间保存了新内容。
    with NamedTemporaryFile(dir=article.parent, delete=False) as tmp_file:
        replacement = Path(tmp_file.name)
        try:
            tmp_file.write(text.encode("utf-8"))
            tmp_file.close()
            replacement.chmod(stat.S_IMODE(article.stat().st_mode))
            if article.read_bytes() != original:
                raise ValueError("文章在上传期间已修改，请保存后重新运行命令。")
            replacement.replace(article)
        finally:
            replacement.unlink(missing_ok=True)
    return len(staged)
