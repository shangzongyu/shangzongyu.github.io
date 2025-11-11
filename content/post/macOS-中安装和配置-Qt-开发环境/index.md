---
title: 'macOS 中安装和配置 Qt 开发环境'
description: '> 介绍如何在 macOS 下使用 Qt Creator + Qt 进行开发。'
slug: macos-config-qt
date: 2022-05-02 06:37:50+0000
image: cover.jpg
tags:
    - macos
    - qt
weight: 1
---


> 介绍如何在 macOS 下使用 Qt Creator + Qt 进行开发。

## 环境

- macOS 版本: macOS 12.3.1
- Qt 版本：Qt 5
- Shell 版本：Zsh

## 安装相应工具

```sh
# 安装 Qt Creator
brew install --cask qt-creator

# 这里安装 Qt5，如果想要安装最新版本的 Qt 使用 qt 替换 qt@5
brew install qt@5
```

## 配置 Zsh

在 `~/.zshrc` 中添加如下配置：

```sh
export PATH="/usr/local/opt/qt@5/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/qt@5/lib"
export CPPFLAGS="-I/usr/local/opt/qt@5/include"
export PKG_CONFIG_PATH="/usr/local/opt/qt@5/lib/pkgconfig"
```

> 如果使用的是 Bash，那么把上述配置写入到 `~/.bashrc` 文件中。

## 配置 Qt Version

在 `Qt Creator -> Preferences -> Kits -> Qt Versions -> Add` 添加 `qmake` 的位置，可以通过搜索 `qmake` 的位置。

> PS：这个吐槽下 Qt Creator 的设计， 不能让用户自己直接通过 Add 输入路径，非要通过搜索才可以。

![macos-config-qt-00](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230726_macos-config-qt-00.png align="center")

配置完 Qt Versions 后，在 `Qt Creator -> Preferences -> Kits -> Kits` 配置 Qt 的版本，如下图：

![macos-config-qt-01](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230726_macos-config-qt-01.png align="center")

## 总结

macOS 需要安装 [Qt](https://www.qt.io/) 和 [Qt Creator](https://www.qt.io/product/development-tools):

- Qt - 提供相应的 GUI 框架。
- Qt Creator - 一个跨平台的 IDE 而已，理论上可以使用其他任意 IDE，但是为了方便还是使用这个。