---
title: Tips：Linux 下给 ManPage 添加颜色
description: Linux 下使用 `man` 命令的时候没有一些颜色，看起来不输入，因此可以添加一些颜色。
slug: linux-manpage
date: 2023-10-14 11:51:30+0000
image:
tags:
  - linux
  - tips
weight: 1
---


> Linux 下使用 `man` 命令的时候没有一些颜色，看起来不输入，因此可以添加一些颜色。

## oh-my-zsh

如果使用的是 `on-my-zhs`，可以通过添加插件 `colored-man-pages` 就可实现 man page 带有颜色。

## bash

如果使用 bash 在 `.bashrc` 中添加如下设置：

```sh
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_so=$'\e[01;33m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'
```

上面的配置的颜色：

- **31** -- red
- **32** -- green
- **33** -- yellow

上面的使用的 `escape codes` 的含义：

- **0** -- reset/normal
- **1** -- bold
- **4** -- underlined

## 更加通的解决方法

使用 [most][1] 是一个分页应用程序。

特点：

- 跨平台，支持 Unix，VMS，MSDOS 以及 win32 systems
- 支持多窗口
- 只是方向键
- 使用空格进行向下滚动

安装：

```sh
# Debian/Ubuntu
sudo apt install most   

# macOS
brew install most
```

配置：

然后在 `.bashrc` 或者 `.zshrc` 添加如下配置：

```sh
export PAGER="most"
```

> PS：自己认为不好用，应为 `most` 的操作方式和之前的操作方式不同，有种使用割裂感觉，不好用。

[1]: http://www.jedsoft.org/most/
