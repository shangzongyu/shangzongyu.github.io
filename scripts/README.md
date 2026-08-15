# 脚本工具说明

## blog.py - 博客日常命令工具

博客日常操作统一入口（Python 3.12+，仅标准库，无第三方依赖）。`fix`、`update-date` 需从项目根目录运行，目录/文件参数使用项目内相对路径（zhlint 只接受不含 `..` 的相对路径）。

### serve - 启动本地服务

```bash
./scripts/blog.py serve                # 等价于 start.sh（含草稿/过期/未来文章）
./scripts/blog.py serve --port 8080    # 指定端口
```

### new - 新建文章

```bash
./scripts/blog.py new "文章标题"                    # 交互式选择分类
./scripts/blog.py new "文章标题" -c 工具推荐          # 直接指定分类
./scripts/blog.py new "文章标题" -c Tips -p          # 创建为已发布（draft: false）
./scripts/blog.py new "文章标题" --no-open           # 创建后不打开 Typora
```

- 走 `archetypes/post.md` 模板生成骨架，`date` 自动填当前时间，`draft` 默认 `true`
- 文件名自动生成 `YYYY-类别_标题.md`，中文保留、空格转 `-`，自动查重
- 标题直接写入 frontmatter 的 `title` 字段（不经过文件名派生）
- 分类从现有文章 frontmatter 自动提取（兼容单行与列表格式），交互式选择或直接输入新分类
- 创建后默认用 Typora 打开（`--no-open` 关闭）

### fix - 修复 Markdown 格式（zhlint --fix）

```bash
./scripts/blog.py fix content/post               # 递归并行处理（默认）
./scripts/blog.py fix content/post --top-only    # 仅处理目录顶层文件
./scripts/blog.py fix content/post content/page  # 多个目录
./scripts/blog.py fix content/post -j 8          # 指定并行线程数（默认 4）
```

原 fix_zhlint.sh 依赖 GNU parallel，本脚本改用标准库线程池实现，无外部依赖。

### update-date - 修改文章 date 字段

```bash
./scripts/blog.py update-date content/post/2026-xxx.md "2026-04-18T10:30:00+08:00"  # 指定日期
./scripts/blog.py update-date content/post/2026-xxx.md  # 使用当前时间
./scripts/blog.py update-date content/post/*.md         # 批量更新多个文件为当前时间
```

规则：已有 `date` 字段则替换，没有则在 `title` 字段后添加；第二个参数以 `YYYY-MM-DD` 开头才视为指定日期，否则视为文件（避免批量更新两个文件时误判）。

***

# Hashnode Markdown 批量转换 Hugo 文件夹结构工具

本工具可将 Hashnode 导出的 Markdown 博客批量转换为 Hugo 兼容的内容目录结构，主要特性包括：

- 每个 Markdown 文件输出为单独目录，目录名称为原文 front matter 中 title 字段（空格变为“-”）。
- 文章内容输出为 `index.md`，封面图片自动下载为 `cover.jpg`。
- 支持自动规范化 front matter，字段及格式详见示例。
- 支持异步批量下载所有封面图像（基于 aiohttp，速度极快）。
- 支持大部分 Hashnode 导出常见 front matter 格式，自动转换日期、标签等，title/description 包含空格自动用单引号包裹。

***

## 快速开始

### 1. 环境准备

- Python 3.7+
- 安装 aiohttp：

  ```bash
  pip install aiohttp
  ```

### 2. 用法

1. 将 Hashnode 导出的所有 `.md` 文件放入如 `input_md/` 目录。
2. 执行如下命令：

   ```bash
   python3 convert.py input_md output_md
   ```

3. 程序会自动在 `output_md/` 目录下为每篇文章建立一个以标题为名的文件夹，并生成 `index.md` 和（如有）`cover.jpg`。

### 3. 输出文件结构示例

```
output_md/
├── macOS-分应用音量控制最佳实践：免费开源工具-Background-Music-推荐/
│   ├── index.md
│   └── cover.jpg
├── 工具推荐：Xpipe/
│   ├── index.md
│   └── cover.jpg
...（每个原 Markdown 生成独立目录）
```

### 4. 生成的 index.md front matter 示例

```yaml
---
title: '工具推荐：Xpipe'
description: 'Xpipe 是一款现代化 SSH 多主机管理工具...'
slug: gongju-tuijian-xpipe
date: 2025-11-10 21:53:13+0800
image: cover.jpg
categories:
    - 工具
tags:
    - 生产力
    - SSH
weight: 1
---
```

***

## English Instructions

### What it does

- Converts all Hashnode-exported Markdown files in a directory to Hugo posts folder structure.
- Each file becomes a directory named after its title (`title` field in front matter, spaces replaced by hyphens).
- Downloads the cover image (if present) as `cover.jpg` in that folder.
- Outputs an `index.md` with well-formatted YAML front matter (title/description with spaces wrapped in single quotes, auto-converted dates/tags/categories).

### Usage

1. Place all input Markdown files into an input folder, e.g., `input_md/`.
2. Ensure you have Python 3.7+ and run
   ```bash
   pip install aiohttp
   ```
3. Then run:
   ```bash
   python3 convert.py input_md output_md
   ```
4. Outputs will appear in `output_md/` as described above.

***

## 注意事项 / Notes

- 保证每篇文章 `title` 唯一，可避免目录名冲突。
- 标题如含特殊符号会自动清理（仅保留中英文、数字、横线）。
- 如缺 title，默认目录名为 `untitled`。
- 封面字段须为 cover，如果无则不下载图片。
- 请根据自身需求修改脚本以适应特殊 front matter 或附加字段。
