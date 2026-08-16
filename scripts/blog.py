#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["rich>=13.9.0"]
# ///
"""blog.py - 博客日常命令工具（Hugo）

用法:
  ./scripts/blog.py serve [--port 1313]      启动本地服务（含草稿/过期/未来文章）
  ./scripts/blog.py new "标题" [选项]         新建文章
  ./scripts/blog.py fix <目录>... [选项]      修复 Markdown 格式（zhlint --fix）
  ./scripts/blog.py update-date <文件>...     修改文章 date 字段

new 选项:
  -c, --category <分类>   直接指定分类（默认交互式选择）
  -p, --publish           创建为已发布文章（draft: false）
      --no-open           创建后不自动打开 Typora

fix 选项:
      --top-only          仅处理目录顶层文件（默认递归）
  -j, --jobs N            并行线程数（默认 4）

依赖由 uv 内联脚本元数据自动管理。zhlint 需已安装。
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.prompt import Prompt
from rich.table import Table

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / "content" / "posts"

# 东八区（博客日期固定 +08:00 格式）
TZ_CST = datetime.timezone(datetime.timedelta(hours=8))

console = Console()
err_console = Console(stderr=True)


def info(msg: str) -> None:
    console.print(f"[cyan]ℹ  {msg}[/]")


def ok(msg: str) -> None:
    console.print(f"[green]✔ {msg}[/]")


def warn(msg: str) -> None:
    console.print(f"[yellow]⚠ {msg}[/]")


def fail(msg: str) -> None:
    console.print(f"[red]✖ {msg}[/]")
    sys.exit(1)


def banner(title: str) -> None:
    """命令横幅"""
    console.print()
    console.print(Panel.fit(f"[bold cyan]{title}[/]", border_style="cyan", padding=(0, 1)))
    console.print()


def card(rows: list[tuple[str, str]]) -> None:
    """键值信息卡片"""
    table = Table(show_header=False, box=box.ROUNDED, pad_edge=False, padding=(0, 1))
    table.add_column(style="bold cyan", no_wrap=True)
    table.add_column(style="bold white", no_wrap=False)
    for k, v in rows:
        table.add_row(k, v)
    console.print(table)


# ---------- serve: 启动本地服务 ----------
def cmd_serve(args: argparse.Namespace) -> None:
    cmd = ["hugo", "server", "-D", "-E", "-F"]
    if args.port:
        cmd += ["--port", str(args.port)]
    banner("serve · 本地服务")
    info(f"启动 Hugo 服务（含草稿/过期/未来文章），端口 {args.port or 1313}")
    console.print("[dim]按 Ctrl+C 停止[/]")
    # 用 exec 替换进程，信号处理与直接运行 hugo 一致
    os.chdir(ROOT_DIR)
    os.execvp("hugo", cmd)


# ---------- fix: zhlint 修复 ----------
def to_cwd_relative(f: Path) -> str:
    """转为相对当前工作目录的路径（zhlint 只接受不含 .. 的相对路径）

    请从项目根目录运行本脚本，并使用项目内相对路径（如 content/posts）。
    """
    try:
        return f.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        fail(f"文件不在当前工作目录下（zhlint 不支持），请从项目根目录运行并使用相对路径: {f}")


def zhlint_fix(rel_path: str) -> bool:
    """运行 zhlint --fix，返回该文件是否被修改（zhlint 无论成败都以 0 退出）"""
    result = subprocess.run(["zhlint", "--fix", rel_path], capture_output=True, text=True, check=False)
    return "[fixed]" in result.stdout


def cmd_fix(args: argparse.Namespace) -> None:
    files: list[Path] = []
    for d in args.dirs:
        p = Path(d)
        if not p.is_dir():
            warn(f"目录不存在，跳过: {d}")
            continue
        files.extend(f for f in (p.glob("*.md") if args.top_only else p.rglob("*.md")) if f.is_file())

    if not files:
        warn("没有找到任何 Markdown 文件。")
        return

    # 主线程统一校验相对路径，fail() 才能正常终止程序（线程内 sys.exit 无效）
    rels = [to_cwd_relative(f) for f in files]

    mode = "顶层" if args.top_only else "递归"
    banner("fix · 修复 Markdown")
    info(f"{mode}扫描，共 {len(files)} 个文件，{args.jobs} 线程并行")

    fixed = 0
    with Progress(
        TextColumn("[bold cyan]修复 Markdown"),
        BarColumn(bar_width=28),
        TextColumn("[cyan]{task.completed}/{task.total}"),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("修复", total=len(files))
        with ThreadPoolExecutor(max_workers=args.jobs) as executor:
            futures = [executor.submit(zhlint_fix, r) for r in rels]
            for fut in as_completed(futures):
                if fut.result():
                    fixed += 1
                progress.advance(task)
    ok(f"修复完成：{fixed} 个被修改，{len(files) - fixed} 个无需处理")


# ---------- update-date: 修改 date 字段 ----------
def now_date() -> str:
    return datetime.datetime.now(tz=TZ_CST).strftime("%Y-%m-%dT%H:%M:%S+08:00")


def update_date(filepath: str, new_date: str) -> bool:
    p = Path(filepath)
    if not p.is_file():
        warn(f"文件不存在，跳过: {filepath}")
        return False
    if p.suffix != ".md":
        warn(f"跳过非 Markdown 文件: {filepath}")
        return False

    text = p.read_text(encoding="utf-8")
    # 仅匹配开头的 frontmatter 块，避免误改正文中 date:/title: 开头的行
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        warn(f"文件不包含合法 frontmatter: {filepath}")
        return False
    fm = m.group(1)

    if re.search(r"(?m)^date:", fm):
        # 更新现有的 date 字段
        fm = re.sub(r"(?m)^date:.*", f"date: {new_date}", fm, count=1)
        ok(f"已更新  {filepath}")
    else:
        # 在 title 字段后添加 date 字段
        if not re.search(r"(?m)^title:", fm):
            warn(f"未找到 title 字段，无法插入 date: {filepath}")
            return False
        fm = re.sub(r"(?m)^(title:.*)$", rf"\1\ndate: {new_date}", fm, count=1)
        ok(f"已添加  {filepath}")

    p.write_text("---\n" + fm + "\n---" + text[m.end():], encoding="utf-8")
    return True


def cmd_update_date(args: argparse.Namespace) -> None:
    # 兼容原脚本语义：第二个参数若是日期（YYYY-MM-DD 开头）则视为指定日期；
    # 否则全部视为文件（使用当前时间），支持批量更新多个文件
    files = args.files
    new_date: str | None = None
    if len(files) == 2 and re.match(r"^\d{4}-\d{2}-\d{2}", files[1]):
        new_date = files[1]
        files = [files[0]]

    if new_date is None:
        new_date = now_date()

    banner("update-date · 修改日期")
    card([("日期", new_date), ("文件", f"{len(files)} 个")])

    ok_count = 0
    for f in files:
        if update_date(f, new_date):
            ok_count += 1
    console.print()
    ok(f"完成：成功 {ok_count}，失败 {len(files) - ok_count}")


# ---------- 分类相关 ----------
def extract_categories() -> list[str]:
    """提取现有文章 frontmatter 中的分类（兼容单行 ["a","b"] 与列表 - a 两种格式）"""
    cats: set[str] = set()
    for md in CONTENT_DIR.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        fm = m.group(1)
        # 单行格式: categories: ["a", "b"]
        m2 = re.search(r"^categories:\s*\[(.*?)\]", fm, re.MULTILINE)
        if m2:
            for item in re.findall(r'"([^"]*)"|\'([^\']*)\'', m2.group(1)):
                val = (item[0] or item[1]).strip()
                if val:
                    cats.add(val)
            continue
        # 列表格式: categories:\n  - a
        m3 = re.search(r"^categories:\s*$", fm, re.MULTILINE)
        if m3:
            rest = fm[m3.end():]
            for line in rest.splitlines():
                if re.match(r"^\s+-\s+", line):
                    val = re.sub(r"^\s+-\s+", "", line).strip().strip('"').strip("'")
                    if val:
                        cats.add(val)
    return sorted(cats)


def select_category() -> str:
    """交互式选择分类：列出已有分类，支持编号选择或输入新分类"""
    cats = extract_categories() or ["未分类"]
    cats.append("（自定义输入）")

    err_console.print()
    err_console.print("[bold cyan]已有分类：[/]")
    for i, c in enumerate(cats, 1):
        err_console.print(f"  [cyan]{i:>2}[/]  {c}")
    err_console.print()

    while True:
        try:
            choice = Prompt.ask("请选择分类编号，或输入新分类").strip()
        except EOFError:
            sys.exit(1)
        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(cats):
                picked = cats[n - 1]
                if picked == "（自定义输入）":
                    new_cat = Prompt.ask("输入新分类名称").strip()
                    if new_cat:
                        return new_cat
                    warn("分类不能为空，请重试")
                else:
                    return picked
            else:
                warn(f"编号 {n} 超出范围（1-{len(cats)}），请重试")
        elif choice:
            return choice


# ---------- 工具函数 ----------
def slugify(title: str) -> str:
    """标题转 slug：保留中文/字母/数字/下划线，空格与特殊字符转连字符"""
    s = re.sub(r"\s+", "-", title.strip())
    s = re.sub(r"[^\w]+", "-", s)  # \w 在 Unicode 模式下包含中文
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def fix_frontmatter(filepath: Path, title: str, category: str, publish: bool) -> None:
    """修正 frontmatter：title 用用户输入（archetype 默认从文件名派生）、categories、draft"""
    text = filepath.read_text(encoding="utf-8")
    escaped_title = title.replace("\\", "\\\\").replace('"', '\\"')
    # 用 lambda 作为替换，避免 re.sub 对替换串中的反斜杠做二次转义（否则 \\ 会被还原成 \）
    text = re.sub(r"(?m)^title:.*$", lambda m: f'title: "{escaped_title}"', text, count=1)
    text = re.sub(r"(?m)^categories:.*$", f'categories: ["{category}"]', text, count=1)
    if publish:
        text = re.sub(r"(?m)^draft: true$", "draft: false", text, count=1)
    filepath.write_text(text, encoding="utf-8")


def open_in_editor(filepath: Path) -> None:
    """默认用 Typora 打开（仅 macOS）"""
    if sys.platform == "darwin":
        result = subprocess.run(["open", "-a", "Typora", str(filepath)], capture_output=True, check=False)
        if result.returncode == 0:
            ok("已用 Typora 打开")
        else:
            warn(f"未找到 Typora，请手动打开: {filepath}")
    else:
        info(f"文件路径: {filepath}")


# ---------- new: 新建文章 ----------
def cmd_new(args: argparse.Namespace) -> None:
    banner("new · 新建文章")

    title = (args.title or "").strip()
    if not title:
        try:
            title = Prompt.ask("请输入文章标题").strip()
        except EOFError:
            fail("标题不能为空")
        if not title:
            fail("标题不能为空")

    category = (args.category or "").strip()
    if not category:
        category = select_category()

    year = datetime.datetime.now(tz=TZ_CST).strftime("%Y")
    slug = slugify(title)
    if not slug:
        fail("标题无法转换为文件名，请换一个标题")

    filename = f"{year}-{category}_{slug}.md"
    filepath = CONTENT_DIR / filename
    if filepath.exists():
        fail(f"文件已存在: {filename}（换个标题或分类）")

    # 用 archetype 生成骨架（date 自动填当前时间），随后修正 frontmatter
    info(f"生成文章: content/posts/{filename}")
    try:
        subprocess.run(["hugo", "new", f"content/posts/{filename}"], cwd=ROOT_DIR, check=True)
    except subprocess.CalledProcessError as e:
        # hugo new 失败（如现有文章有语法错误导致站点组装失败），清理可能残留的半成品
        filepath.unlink(missing_ok=True)
        fail(
            f"hugo new 失败（退出码 {e.returncode}），已清理残留文件。\n"
            "可能是现有文章有语法错误导致站点组装失败，可先运行 ./scripts/blog.py fix 或检查文章。"
        )

    fix_frontmatter(filepath, title, category, args.publish)
    ok(f"已创建: content/posts/{filename}")
    console.print()
    card(
        [
            ("标题", title),
            ("分类", category),
            ("状态", "已发布" if args.publish else "草稿"),
            ("文件", f"content/posts/{filename}"),
        ]
    )
    console.print()

    if args.no_open:
        info(f"文件路径: {filepath.relative_to(ROOT_DIR)}")
    else:
        open_in_editor(filepath)


# ---------- 主入口 ----------
def main() -> None:
    parser = argparse.ArgumentParser(
        prog="blog.py",
        description="博客日常命令工具（Hugo）",
        epilog="示例: ./scripts/blog.py new \"cmux 使用心得\" -c 工具推荐 -p",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", metavar="命令")

    p_serve = sub.add_parser("serve", aliases=["s"], help="启动本地服务（含草稿/过期/未来文章）")
    p_serve.add_argument("--port", type=int, metavar="端口", help="指定端口（默认 1313）")
    p_serve.set_defaults(func=cmd_serve)

    p_new = sub.add_parser("new", aliases=["n"], help="新建文章")
    p_new.add_argument("title", nargs="?", help="文章标题（不提供则交互输入）")
    p_new.add_argument("-c", "--category", help="直接指定分类（默认交互式选择）")
    p_new.add_argument("-p", "--publish", action="store_true", help="创建为已发布文章（draft: false）")
    p_new.add_argument("--no-open", action="store_true", help="创建后不自动打开 Typora")
    p_new.set_defaults(func=cmd_new)

    p_fix = sub.add_parser("fix", help="修复 Markdown 格式（zhlint --fix）")
    p_fix.add_argument("dirs", nargs="+", metavar="目录", help="要处理的目录（项目内相对路径，可多个）")
    p_fix.add_argument("--top-only", action="store_true", help="仅处理目录顶层文件（默认递归）")
    p_fix.add_argument("-j", "--jobs", type=int, default=4, metavar="N", help="并行线程数（默认 4）")
    p_fix.set_defaults(func=cmd_fix)

    p_date = sub.add_parser("update-date", aliases=["date"], help="修改文章 date 字段")
    p_date.add_argument("files", nargs="+", metavar="文件", help="文件路径（可多个，第二个参数若是日期则视为指定日期）")
    p_date.set_defaults(func=cmd_update_date)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
