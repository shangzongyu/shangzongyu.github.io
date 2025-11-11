---
title: '工具推荐: goji - 使用 Emoji 提交 Commit 信息'
description: '- Github：<https://github.com/muandane/goji>'
slug: goji-emoji-commit
date: 2024-11-14 10:32:19+0000
image: cover.jpg
tags:
    - tools
    - git
weight: 1
---


## 介绍

- Github：<https://github.com/muandane/goji>

使用 Emoji 提交 Commit 信息。

## 安装

```sh
# macOS
brew install muandane/tap/goji
```

```sh
# Linux
VERSION=$(curl --silent "https://api.github.com/repos/muandane/goji/releases/latest" | jq .tag_name -r)
curl -Lso goji.tar.gz https://github.com/muandane/goji/releases/download/$VERSION/goji_${VERSION}_Linux_x86_64.tar.gz
tar -xvzf goji.tar.gz
chmod +x ./goji
# optionnal
sudo mv ./goji /usr/local/bin/
```

## 使用

简单运行  `goji` 就可以开始交付模式：

官方示例：![](https://raw.githubusercontent.com/muandane/goji/refs/heads/main/public/goji-demo.gif)

goji 可以通过配置文件做一些配置：

```sh
# 在特定 repo 中指定配置，下面命令会在当前目录下生成 .goji 文件
goji init --repo

# 全局的配置，下面命令会在 $HOME 下生成 .goji 文件
goji init --global
```

> 配置文件的详细配置参考 [官方文档](https://github.com/muandane/goji)。