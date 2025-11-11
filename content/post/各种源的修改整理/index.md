---
title: 各种源的修改整理
description: '> 由于国内网络众所周知的原导导致下载国外的包时，网络会很慢或者更本就下载不了，因此我们需要切换相应的源。'
slug: 5zce56en5rqq55qe5lu5ps55pw055cg
date: 2022-08-01 06:38:13+0000
image: cover.jpg
tags:
    - developer
    - tips
weight: 1
---


> 由于国内网络众所周知的原导导致下载国外的包时，网络会很慢或者更本就下载不了，因此我们需要切换相应的源。

> 这个会持续更。

## 操作系统

### Ubuntu

> 使用 USTC 的源，Ubuntu 的地址为：[https://mirrors.ustc.edu.cn/help/ubuntu.html](https://mirrors.ustc.edu.cn/help/ubuntu.html)

```sh
# 备份
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# 替换源
sudo sed -i 's/us.archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# 更新索引以生效
sudo apt update
```

也可以使用别人 snullp 大叔开发的 [配置生成器](https://mirrors.ustc.edu.cn/repogen) 。

### FreeBSD

FreeBSD `pkg` 包管理器官方源配置是 `/etc/pkg/FreeBSD.conf` 。

其中的 `url` 参数配置了官方仓库的地址，我们需要把它替换为镜像站的地址。该配置文件是 FreeBSD 系统的一部分，请不要直接创建，而是创建 `/usr/local/etc/pkg/repos/FreeBSD.conf` 覆盖配置，文件内容如下：

```sh
mkdir -p /usr/local/etc/pkg/repos/
touch /usr/local/etc/pkg/repos/FreeBSD.conf
```

```ini
# 新增如下内容
FreeBSD: {
  url: "pkg+http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly"
}
```

如果要使用滚动更新的 `latest` 仓库，把 `url` 配置最后的 `quarterly` 换成 `latest` 即可。

修改配置后，运行 `pkg update -f` 更新索引。

> 小技巧: 使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安 `security/ca_root_nss` 软件包。 参考这个 [https://mirrors.ustc.edu.cn/help/freebsd-pkg.html](https://mirrors.ustc.edu.cn/help/freebsd-pkg.html)

## 编程语言

### Python

> 更换 pip 源，使用 阿里云 提供的镜像，创建 `$HOME/.pip/pip.conf` ，写入如下内容：

```ini
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

### Go

> 只需要设置 GOPROXY 即可。

> PS：使用 [https://goproxy.cn](https://goproxy.cn) 为国内用户服务的 GOPROXY。

在 `$HOME/.bashrc` 或者 `$HOME/.zshrc` 添加如下内容：

```sh
export GOPROXY=https://goproxy.cn,direct
```

其他可用的 GOPROXY：[https://goproxy.io/zh](https://goproxy.io/zh) 一个全球代理 为 Go 模块而生。

### Rust

`.bashrc` 或者 `.zshrc` 中添加如下内容。

> 中科大的源

#### 配置 Rust 基础环境变量

```sh
# 用于更新 toolchain
export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static

# 更新 rustup
export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
```

> 参考：[Rust Toolchain 反向代理使用帮助](https://mirrors.ustc.edu.cn/help/rust-static.html)

#### 配置 cargo 环境变量

在 `$HOME/.cargo/config` 中添加如下内容：

```ini
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
```

如果所处的环境中不允许使用 git 协议，可以把上述地址改为：

```makefile
registry = "https://mirrors.ustc.edu.cn/crates.io-index"
```

> 参考：[Rust Crates 源使用帮助](https://mirrors.ustc.edu.cn/help/crates.io-index.html)

## 其他

### Homebrew

> 使用清华大学的源。

```sh
# 设置环境变量
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
```

> 参考：https://mirror.tuna.tsinghua.edu.cn/help/homebrew/