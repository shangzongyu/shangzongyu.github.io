---
title: 'Tips:查询 Linux 系统安装时间'
description: 'Linux 系统安装之后，`root` 路径的创建时间是不会变更，因此可以通过做个特性来查找。'
slug: tips-linux
date: 2024-01-14 03:20:54+0000
tags:
    - linux
    - tips
weight: 1
---


## 通用方法

Linux 系统安装之后，`root` 路径的创建时间是不会变更，因此可以通过做个特性来查找。

```sh
$ stat / | awk '/Birth: /{print $2 " " substr($3,1,5)}'
2023-07-28 11:19
```

> 可以看到我的系统是：2023-07-28 11:19 时间安装的。

这样方法有些麻烦，仔细看这串代码，其实就是使用 `stat` 命令获取时间，然后使用 `awk` 和 `substr` 进行选取 `Birth` 字段，其实可以直接使用 `stat /` 查看：

```sh
$ stat /
 File: /
  Size: 230       	Blocks: 0          IO Block: 4096   directory
Device: 22h/34d	Inode: 210115      Links: 1
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-07-28 05:52:36.000000000 +0800
Modify: 2024-01-14 10:23:24.184641738 +0800
Change: 2024-01-14 10:23:24.184641738 +0800
Birth: 2023-07-28 11:19:08.063247240 +0800
```

> `stat` 的 [man page](https://man7.org/linux/man-pages/man1/stat.1.html)。

还有一个通用的方法如下：

```sh
$ tune2fs: Bad magic number in super-block while trying to open /dev/vdb1
```

> PS：有可能报错，推荐第一种方法。

## Debian 系列

> 包括：Debian/Ubuntu/Mint 等。

```sh
$ sudo head -n1 /var/log/installer/syslog
```

> PS：虚拟机或者容器安装有可能会报错：没有 syslog 文件。

## RHEL 系列

> 包括：CentOS/Fedora/Rocky 等。

```sh
$ sudo rpm -qi basesystem | grep -i "install date"
Install Date: Sat 13 Jan 2024 10:09:22 AM CST
```

## Arch 系列

> 包括：Manjaro/EndeavourOS 等

```sh
$ head -n1 /var/log/pacman.log
[2023-12-11T04:18:36+0000] [PACMAN] Running 'pacman -Sy --needed --noconfirm archlinux-keyring'
```

## 参考资料

* [Linux Installation Date：How to Discover Your System’s Age](https://linuxiac.com/how-to-find-linux-os-installation-date/)