---
title: "工具推荐: upgit - 把博客的照片备份到 Github"
description:
slug: upgit-github
date: 2023-07-26 10:39:57+0000
image: cover.jpg
tags:
  - blogging
  - github
  - tools
weight: 1
---
## 介绍

- Github：<https://github.com/pluveto/upgit>

upgit 可以快捷地将文件上传到 Github 仓库并得到其直链。简洁跨平台，不常驻内存。

**特点**：

- 支持多平台，包括 Linux、Windows 和 macOS
- 支持多种上传器
- 不限制文件类型
- 支持从剪贴板上传
- 自定义自动重命名规则 (包括路径)
- 可通过替换规则实现 CDN 加速
- 可通过环境变量配置
- 将 URL 输出到标准输出/剪贴板，支持 Markdown 格式

**支持平台**：

- Github
- Gitee
- 七牛云 Kodo
- 又拍云
- ...

## 安装

从[这里](https://github.com/pluveto/upgit/releases)下载系统对应的二进制版本，这里以 macOS 为例。

```sh
# 新建目录
mkdir ~/.local/bin/upgit
cd ~/.local/bin/ssupgit

# 下载 v0.2.18 版本
wget --output-document upgit https://github.com/pluveto/upgit/releases/download/v0.2.18/upgit_macos_amd64

# 添加可执行权限
chmod a+x ./upgit

# 添加到 PATH 中
## bash
echo 'export PATH="${PATH}:${HOME}/.local/bin/upgit"' >> ~/.bashrc"
## zsh
echo 'export PATH="${PATH}:${HOME}/.local/bin/upgit"' >> ~/.zshrc"

# 新建配置文件
touch config.toml
```

> 配置文件 `config.toml` 在程序的同目录下，配置参考[这里](https://github.com/pluveto/upgit/blob/main/config.sample.zh-CN.toml)。

## 实例

```sh
$ upgit ~/poe.png
https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20231102_poe.png
```

## 和 Typora 集成

配置很简单，只需要指定 `upgit` 所在的目录即可。

![upgit-typora](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20231102_upgit-typora.png)

参考 [https://support.typora.io/Upload-Image/#image-uploaders](https://support.typora.io/Upload-Image/#image-uploaders)
