---
title: '工具推荐：markitdown - 转换文件为 Markdown'
description: '一个 Python 工具转换文件为 Markdown，方便自己使用 Markdown 成为的笔记。'
slug: markitdown-markdown
date: 2024-12-21 06:56:21+0000
tags:
  - tools
weight: 1
---

> 一个 Python 工具转换文件为 Markdown，方便自己使用 Markdown 成为的笔记。

<!--more-->

## 介绍

一个 Python 工具转换文件为 Markdown，方便自己使用 Markdown 成为的笔记。

支持的文件格式如下：

* PDF
* PowerPoint
* Word
* Excel
* Images (EXIF metadata and OCR)
* Audio (EXIF metadata and speech transcription)
* HTML
* Text-based formats (CSV，JSON，XML)
* ZIP files (iterates over contents)
  
> Github：<https://github.com/microsoft/markitdown>

## 使用

> 工具支持多种使用方式：命令行，Python API 以及 Docker 等，下面以命令行为主介绍。

```sh
# 安装
pip install markitdown

# 转换 pdf
markitdown path-to-file.pdf > document.md
markitdown path-to-file.pdf -o document.md
```
