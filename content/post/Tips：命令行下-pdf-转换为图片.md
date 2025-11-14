---
title: 'Tips: 命令行下 pdf 转换为图片'
description: '使用工具 poppler 把 PDF 文档转换为图片，'
slug: pdf
date: 2023-07-26 08:03:08+0000
image: 
weight: 1
---

使用工具 [poppler](https://poppler.freedesktop.org)，它是基于 [xpdf-3.0](http://www.foolabs.com/xpdf/)，可以把 PDF 文档转换为图片，除此之外还可以指定分辨率、缩放以及裁剪。

## 安装

```bash
# macOS
brew install poppler
# Debian/Ubuntu
sudo apt install poppler-utils

# Arch
sudo pacman -S poppler
```

安装成功后，会有一个可用的命令为 `pdftoppm`。

## 使用

```bash
# 语法
pdftoppm [options] PDF-file PPM-root
```

使用实例如下。

### 转换整个文件

```bash
pdftoppm -<image_format> <pdf_filename> <image_name>
```

加入转换的文件名为：`xxx.pdf`，转换的图片格式为 `png`。

```bash
pdftoppm -png xxx.pdf xxx
```

### 只转换部分 PDF

```bash
pdftoppm -<image_format> -f N -l N <pdf_filename> <image_name>
```

参数解释：

* `-f N`：PDF 的起始页码
* `-l N`：PDF 的结束码
    
比如我们需要把第 2 页到第 5 页转为图片：

```bash
pdftoppm -png -f 2 -l 5 xxx.pdf xxx
```

### 调整图片的质量

`pdftoppm` 默认的 DPI 为 150。

```bash
pdftoppm -png -rx 300 -ry 300 xxx.pdf xxx
```

### 更多使用方法

```bash
pdftoppm --help  
man pdftoppm
```
