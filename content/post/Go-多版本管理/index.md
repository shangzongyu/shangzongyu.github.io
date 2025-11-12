---
title: 'Go 多版本管理'
description: '日常在开发的过程中，会用到不同的 Go 的版本，对它进行管理有些麻烦，因此自己找到下面几个工具帮助自己。'
slug: go
date: 2023-07-28 09:55:20+0000
image: cover.jpg
tags:
    - go
weight: 1
---


> 日常在开发的过程中，会用到不同的 Go 的版本，对它进行管理有些麻烦，因此自己找到下面几个工具帮助自己。

## gvm

### 介绍

[gvm](https://github.com/moovweb/gvm) Go 版本管理。

> 这个项目最后一次的 commit 信息是 20200217，也就意味着三年没有更新了。

gvm 很多功能，不过我只使用其中的一个功能，就是管理 Go 版本。


### 安装

```sh
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

### 使用

```sh
$ gvm install --help
Invalid version: --help
Usage: gvm install [version] [options]
    -s,  --source=SOURCE      Install Go from specified source.
    -n,  --name=NAME          Override the default name for this version.
    -pb, --with-protobuf      Install Go protocol buffers.
    -b,  --with-build-tools   Install package build tools.
    -B,  --binary             Only install from binary.
         --prefer-binary      Attempt a binary install, falling back to source.
    -h,  --help               Display this message.
```

```sh
# 列出所有可安装的 Go 版本
$ gvm listall

gvm gos (available)

   go1
   ...
   go1.19.11
   go1.20
    ...
   release.r56
   release.r57
   release.r58
   release.r59
   release.r60
   release.r57.1
   release.r57.2
   release.r58.1
   release.r58.2
   release.r60.1
   release.r60.2
   release.r60.3

# 安装某个版本 1.19.11
$ gvm install go1.19.11
gvm install go1.19.11
Downloading Go source...
Installing go1.19.11...
 * Compiling...
go1.19.11 successfully installed!

# 列举出安装的 Go 的版本
$ gvm list

gvm gos (installed)

   go1.19.11
   system

# 使用版本
$ gvm use go1.19.11
Now using version go1.19.11
```

## g

### 介绍 g

[g](https://github.com/voidint/g) 是一个 Linux、macOS、Windows 下的命令行工具，可以提供一个便捷的多版本 go 环境的管理和切换。

特性：

- 支持列出可供安装的 go 版本号
- 支持列出已安装的 go 版本号
- 支持在本地安装多个 go 版本
- 支持卸载已安装的 go 版本
- 支持在已安装的 go 版本之间自由切换
- 支持清空安装包文件缓存
- 支持软件自我更新 (>= 1.5.0)
- 支持软件绿色卸载 (>= 1.5.0)

### 安装 g

自己主要使用在 Linux 和 macOS 上使用，因此只介绍这两个平台的安装。

自己环境：

- 系统：Linux/macOS
- Shell：zsh

```sh
# 建议安装前清空 GOROOT、GOBIN 等环境变量
$ unset GOROOT && unset GOBIN

# 安装
$ curl -sSL https://raw.githubusercontent.com/voidint/g/master/install.sh | bash

# 可选：若其他程序（如'git'）使用了'g'作为别名
$ echo "unalias g" >> ~/.zshrc

# 加载环境变量
$ source "$HOME/.g/env"
```

> 其他的平台安装参考[这个](https://github.com/voidint/g)。

### 使用 g

```sh
# 显示当前可供安装的 stable 状态的 Go
$ g ls-remote stable
  1.19.11
  1.20.6

# 查看可供安装的所有 Go 的版本
$ g ls-remote
  1
  1.2.2
  ...
  1.3
  ...
  1.4
  ...
  1.5
  ...
  1.6
 ...
  1.7
  ...
  1.8
  ...
  1.9
  ...
  1.10
  ...
  1.11
  ...
  1.12
  ...
  1.13
  ...
  1.14
  ...
  1.15
  ...
  1.17
  ...
  1.19
  1.19.9
  1.19.10
* 1.19.11
  ...
  1.20
  1.20.1
  1.20.2
  1.20.3
  1.20.4
  1.20.5
* 1.20.6
  1.21rc2
  1.21rc3

# 安装 go1.19.10
$ g install go1.19.10

# 查询已安装的 go 版本
$ g ls
* 1.19.11

# 切换到另外一个安装的版本
$ g use 1.20.6
go version go1.20.6 darwin/amd64

# 清空 Go 安装包文件缓存
$ g clean
Remove g1.5.0.darwin-amd64.tar.gz
Remove go1.19.11.darwin-amd64.tar.gz
Remove go1.20.6.darwin-amd64.tar.gz

# 查看 g 版本信息
$ g --version
g version 1.5.0
build: 2023-01-01T21:01:51+08:00
branch: master
commit: cec84a3f4f927adb05018731a6f60063fd2fa216

# 更新 g 软件本身
$ g self update
You are up to date! g v1.5.0 is the latest version.

# 卸载 g 软件本身
$ g self uninstall
...
```

### 关于 go 安装的目录

g 安装的 go 版本在 `~/.g` 目录下：

```sh
$ tree -L 1
.
├── bin
├── downloads
├── env
├── go -> /Users/jojo/.g/versions/1.20.6
└── versions

5 directories, 1 file
```
