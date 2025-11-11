import os
import re
import sys
import asyncio
import aiohttp
from datetime import datetime

def safe_dirname(name):
    # 用 - 替换空格，去掉特殊字符
    name = name.replace(' ', '-')
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    return name

def parse_front_matter(fm_raw):
    result = {}
    lines = fm_raw.splitlines()
    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)
            value = value.strip().strip('"').strip("'")
            result[key] = value
    return result

def convert_date(date_str):
    fmts = [
        "%a %b %d %Y %H:%M:%S GMT%z (%Z)",
        "%a %b %d %Y %H:%M:%S GMT%z",
        "%a %b %d %Y %H:%M:%S %z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S"
    ]
    date_str = re.sub(r"\s*\(.*\)$", "", date_str).strip()
    for fmt in fmts:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d %H:%M:%S%z")
        except Exception:
            continue
    return date_str

def quote_single_if_space(val):
    if ' ' in val and not (val.startswith("'") and val.endswith("'")):
        return f"'{val}'"
    return val

def make_yaml_front_matter(opts):
    fm_lines = ["---"]
    fm_lines.append(f"title: {quote_single_if_space(opts['title'])}")
    if opts.get('description'):
        fm_lines.append(f"description: {quote_single_if_space(opts['description'])}")
    if opts.get('slug'):
        fm_lines.append(f"slug: {opts['slug']}")
    fm_lines.append(f"date: {opts['date']}")
    if opts.get('image'):
        fm_lines.append(f"image: {opts['image']}")
    if opts.get('categories'):
        fm_lines.append("categories:")
        for cate in opts['categories']:
            fm_lines.append(f"    - {cate}")
    if opts.get('tags'):
        fm_lines.append("tags:")
        for tag in opts['tags']:
            fm_lines.append(f"    - {tag}")
    fm_lines.append("weight: 1")
    fm_lines.append("---")
    return '\n'.join(fm_lines)

def extract_description(body):
    ps = [line.strip() for line in body.splitlines() if line.strip() and not line.startswith('#')]
    if ps:
        desc = ps[0]
        desc = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', desc)
        return desc[:120]
    return ""

async def download_image(session, url, dest_path):
    try:
        async with session.get(url, timeout=10) as resp:
            if resp.status == 200:
                content = await resp.read()
                with open(dest_path, 'wb') as f:
                    f.write(content)
                print(f"下载封面成功: {dest_path}")
                return True
            else:
                print(f"下载失败 {url}，状态码: {resp.status}")
                return False
    except Exception as e:
        print(f"下载封面失败: {url} ({e})")
        return False

async def process_file(file_path, output_dir_root, session):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^-{3,}\n(.+?)\n-{3,}\n(.*)", content, re.DOTALL)
    if not match:
        print(f"{file_path}：无法解析 front matter")
        return
    fm_raw, body = match.groups()
    fm = parse_front_matter(fm_raw)
    title_val = fm.get('title', 'untitled')
    dirname = safe_dirname(title_val)
    output_dir = os.path.join(output_dir_root, dirname)
    os.makedirs(output_dir, exist_ok=True)
    slug_val = fm.get('slug', dirname)
    date_val = convert_date(fm.get('datePublished', fm.get('date', "")))
    tags_raw = fm.get('tags', '')
    tags_list = [t.strip() for t in re.split(r'[;,]', tags_raw) if t.strip()]
    cats_raw = fm.get('categories', '')
    cats_list = [c.strip() for c in re.split(r'[;,]', cats_raw) if c.strip()]
    cover_url = fm.get('cover', '')
    cover_filename = 'cover.jpg'
    image_field = ''
    if cover_url and (cover_url.startswith('http://') or cover_url.startswith('https://')):
        cover_path = os.path.join(output_dir, cover_filename)
        if await download_image(session, cover_url, cover_path):
            image_field = cover_filename
    desc_val = extract_description(body)
    header_opts = dict(
        title=title_val,
        slug=slug_val,
        date=date_val,
        image=image_field if image_field else None,
        tags=tags_list if tags_list else None,
        categories=cats_list if cats_list else None,
        description=desc_val
    )
    yaml_fm = make_yaml_front_matter(header_opts)
    out_md_path = os.path.join(output_dir, 'index.md')
    with open(out_md_path, 'w', encoding='utf-8') as out:
        out.write(yaml_fm + '\n\n' + body)
    print(f"{file_path} -> {out_md_path}")

async def main():
    if len(sys.argv) != 3:
        print("用法: python3 convert.py <输入目录> <输出目录>")
        sys.exit(1)
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    files = [os.path.join(input_dir, fn) for fn in os.listdir(input_dir) if fn.endswith('.md')]
    async with aiohttp.ClientSession() as session:
        tasks = [process_file(f, output_dir, session) for f in files]
        await asyncio.gather(*tasks)
    print(f"全部转换完成，输出目录：{output_dir}")

if __name__ == '__main__':
    asyncio.run(main())
