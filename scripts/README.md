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

