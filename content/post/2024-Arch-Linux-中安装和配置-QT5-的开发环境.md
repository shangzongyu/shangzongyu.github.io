---
title: Arch Linux 中安装和配置 QT5 的开发环境
description: 环境如下：
slug: arch-linux-qt5
date: 2024-11-09 08:43:09+0000
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_2024-Arch-Linux-中安装和配置-QT5-的开发环境.webp
tags:
  - development
weight: 1
---
环境如下：

- OS：EndeavourOS x86_64
- QT 版本：QT5

```sh
# 更新系统
sudo pacman -Syu

# 安装基本 QT 基本包
sudo pacman -S qt5-base

# 安装 QT 开发工具，包含：Qt Assistant/Qt Linguist/Qt Designer 等 
sudo pacman -S qt5-tools

# 安装 Qt 的编辑器 qtcreator
sudo pacman -S qtcreator
```

安装好之后，就可以打开 qtcreator 进行开发了。

在 Linux 上安装比 macOS 上方便一些。
