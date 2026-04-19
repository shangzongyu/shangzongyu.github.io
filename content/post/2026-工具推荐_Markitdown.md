---
title: "工具推荐：Markitdown 使用笔记"
description: Microsoft MarkItDown 工具的基础使用记录
date: 2026-04-18T00:00:00+08:00
draft: true
tags:
  - Markdown
  - Python
  - 工具
categories: ["工具推荐"]
weight: 1
---

- GitHub: [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)
- PyPI: [https://pypi.org/project/markitdown/](https://pypi.org/project/markitdown/)

> Python tool for converting files and office documents to Markdown.

MarkItDown 是一个轻量级的 Python 工具，用于将各种文件转换为 Markdown 格式，主要用于 LLM 和文本分析管道。它专注于保留重要的文档结构和内容（包括标题、列表、表格、链接等）。

## 支持的文件格式

- PDF
- PowerPoint (.pptx)
- Word (.docx)
- Excel (.xlsx, .xls)
- 图片（EXIF 元数据和 OCR）
- 音频（EXIF 元数据和语音转录）
- HTML
- 基于文本的格式（CSV, JSON, XML）
- ZIP 文件（遍历内容）
- YouTube URL
- EPubs
- ...以及更多！

## 安装

### 基本安装

```bash
pip install 'markitdown[all]'
```

### 选择性安装

如果你只需要支持特定格式，可以选择安装对应依赖：

```bash
# 只安装 PDF、DOCX 和 PPTX 支持
pip install 'markitdown[pdf, docx, pptx]'

# 可选依赖组
# [all] - 安装所有可选依赖
# [pptx] - PowerPoint 文件
# [docx] - Word 文件
# [xlsx] - Excel 文件
# [xls] - 旧版 Excel 文件
# [pdf] - PDF 文件
# [outlook] - Outlook 邮件
# [az-doc-intel] - Azure Document Intelligence
# [audio-transcription] - 音频转录（wav, mp3）
# [youtube-transcription] - YouTube 视频转录
```

### 系统要求

- Python 3.10 或更高版本
- 建议使用虚拟环境以避免依赖冲突

## 命令行使用

### 基本用法

```bash
# 转换文件到标准输出
markitdown path-to-file.pdf

# 指定输出文件
markitdown path-to-file.pdf -o document.md

# 使用管道
cat path-to-file.pdf | markitdown
```

### 列出已安装的插件

```bash
mark markitdown --list-plugins
```

### 启用插件

```bash
markitdown --use-plugins path-to-file.pdf
```

### 使用 Azure Document Intelligence

```bash
markitdown path-to-file.pdf -o document.md -d -e "<document_intelligence_endpoint>"
```

## Python API 使用

### 基本用法

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert("test.xlsx")
print(result.text_content)
```

### 启用插件

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True)
result = md.convert("document.pdf")
print(result.text_content)
```

### 使用 Azure Document Intelligence

```python
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert("test.pdf")
print(result.text_content)
```

### 使用 LLM 生成图片描述

目前支持 PPTX 和图片文件：

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(
    llm_client=client,
    llm_model="gpt-4o",
    llm_prompt="请用中文描述这张图片的内容"
)
result = md.convert("example.jpg")
print(result.text_content)
```

## 使用 OCR 插件

`markitdown-ocr` 插件为 PDF、DOCX、PPTX 和 XLSX 转换器添加 OCR 支持，使用 LLM Vision 从嵌入的图片中提取文本。

### 安装 OCR 插件

```bash
pip install markitdown-ocr
pip install openai  # 或任何兼容 OpenAI 的客户端
```

### 使用 OCR 插件

```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
result = md.convert("document_with_images.pdf")
print(result.text_content)
```

## 实用示例

### 批量转换文件

```python
import os
from markitdown import MarkItDown

md = MarkItDown()
input_dir = "documents"
output_dir = "markdown"

for filename in os.listdir(input_dir):
    if filename.endswith(('.pdf', '.docx', '.pptx')):
        input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.md")
    
    result = md.convert(input_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result.text_content)
    
    print(f"已转换: {filename}")
```

### 处理 YouTube 视频

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("https://www.youtube.com/watch?v=VIDEO_ID")
print(result.text_content)
```

### 处理 ZIP 文件

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("archive.zip")
print(result.text_content)  # 将包含 ZIP 中所有文件的内容
```

## MCP 服务器支持

MarkItDown 现在提供 MCP（Model Context Protocol）服务器，用于与 Claude Desktop 等 LLM 应用集成。

更多信息请查看：[markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)

## 为什么选择 Markdown？

Markdown 接近纯文本，具有最小的标记或格式，但仍提供表示重要文档结构的方法。主流 LLM（如 OpenAI 的 GPT-4o）原生"理解"Markdown，并且通常在提示时会自然地结合 Markdown。这表明它们接受了大量 Markdown 格式文本的训练，并且理解得很好。作为额外的好处，Markdown 约定也具有很高的令牌效率。

## 相关资源

- [官方文档](https://github.com/microsoft/markitdown)
- [MarkItDown MCP 服务器](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)
- [OCR 插件文档](https://github.com/microsoft/markitdown/blob/main/packages/markitdown-ocr/README.md)
- [示例插件](https://github.com/microsoft/markitdown/blob/main/packages/markitdown-sample-plugin)
- [贡献指南](https://github.com/microsoft/markitdown/blob/main/CONTRIBUTING.md)

---

**注意**：MarkItDown 的输出通常适合文本分析工具使用，但可能不是高保真文档转换以供人类阅读的最佳选择。如果需要完美的文档格式保留，建议使用专门的文档转换工具。
