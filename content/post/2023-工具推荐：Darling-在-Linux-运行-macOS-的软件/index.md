---
title: '工具推荐: Darling - 在 Linux 运行 macOS 的软件'
description: '可以帮助用户在非 mac 平台运行 mac 平台的软件。'
slug: darling-linux-macos
date: 2023-07-28 10:43:11+0000
image: cover.jpg
tags:
    - macos
weight: 1
---


## 介绍

可以帮助用户在非 mac 平台运行 mac 平台的软件。

> 当然这个也是有限制的。

## 安装

不同的平台需要安装的软件不同，这里以 Ubuntu 22.04 为例子进行介绍。

> 其他的 Linux 的发行版参考[这个](https://docs.darlinghq.org/build-instructions.html)。

### 下载需要库

```sh
sudo apt install cmake clang bison flex libfuse-dev libudev-dev pkg-config libc6-dev-i386 \
gcc-multilib libcairo2-dev libgl1-mesa-dev libglu1-mesa-dev libtiff5-dev \
libfreetype6-dev git git-lfs libelf-dev libxml2-dev libegl1-mesa-dev libfontconfig1-dev \
libbsd-dev libxrandr-dev libxcursor-dev libgif-dev libavutil-dev libpulse-dev \
libavformat-dev libavcodec-dev libswresample-dev libdbus-1-dev libxkbfile-dev \
libssl-dev python2
```

### 2。clone darling 项目

```sh
# clone 项目
git clone --recursive https://github.com/darlinghq/darling.git
```

### 构建和安装

```sh
# 进入刚才 clone 的目录
cd darling

# 删除已经安装的 darling
sudo ./tools/uninstall

# 创建构建目录
mkdir build && cd build

# 执行 cmake 进行构建
cmake ..

# 构建
make

# 安装
make install
```

## 使用

darling 不止可以直接运行 Mac 平台的软件，还可以安装 Mac 平台的 DMG 格式的软件，不过我没有这个需要，这里主要介绍在 Linux 平台运行 Mac 平台的命令行软件。

```sh
# 在 Linux 下启动一个 macOS 的环境
$ darling shell
Setting up a new Darling prefix at /home/tomshine/.darling
Bootstrapping the container with launchd...

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.

# 查看内核版本
$ uname -a
Darwin ubuntu22.04 20.6.0 Darwin Kernel Version 20.6.0 x86_64
```

## 实例

首先我们使用 go 写一个程序，然后进行测试，内容如下：

需要准备三个文件：

- main.go
- main_linux.go
- main_darwin.go

然后进行编译，进行测试。

`main.go` 内容如下：

````go
package main

func main() {
  PrintOS()
}
```ma c

`main_linux.go` 内容如下：

```go
//go:build linux

package main

import (
	"fmt"
	"runtime"
)

func PrintOS() {
	fmt.Println("OS is", runtime.GOOS)
}
````

`main_darwin.go` 内容如下：

```go
//go:build darwin

package main

import (
	"fmt"
	"runtime"
)

func PrintOS() {
	fmt.Println("OS is", runtime.GOOS)
}
```

编译：

```sh
$ GOOS=linux go build -o darling-linux
$ GOOS=darwin go build -o darling-darwin
```

查看二进制的类型：

```sh
$ file darling-linux
darling-linux: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=BrvHsgIjrBhSTFuvkyEm/m5-a3TFICalPz-oYNNpy/Nnl87_vvwB9rds54GOyM/JgRfd1wJbYrRhG83TWrq, with debug_info, not stripped
$ file darling-darwin
darling-darwin: Mach-O 64-bit x86_64 executable
```

运行：

```sh
$ ./darling-darwin
Cannot mmap segment __LINKEDIT at 0x1173000: File exists

# TODO 出错了，但是不知道什么原因，等待解决。
```

## 资料

- Github：<https://github.com/darlinghq/darling-docs>
- 文档：<https://docs.darlinghq.org/darling-shell.html>