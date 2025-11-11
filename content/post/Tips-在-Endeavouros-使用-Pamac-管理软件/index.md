---
title: 'Tips: 在 Endeavouros 使用 Pamac 管理软件'
description: '[Pamac][Pamac] 是 Manjaro 一款基于 [libalpm][libalpm] 的 GUI 包管理工具，[libalpm][libalpm] 支持 AppStream、[AUR][AUR]、[Flatpak][Flatpa'
slug: endeavouros-pamac
date: 2022-12-12 03:10:05+0000
image: cover.jpg
tags:
    - package-manager
weight: 1
---


## 介绍

[Pamac][Pamac] 是 Manjaro 一款基于 [libalpm][libalpm] 的 GUI 包管理工具，[libalpm][libalpm] 支持 AppStream、[AUR][AUR]、[Flatpak][Flatpak] 以及 [Snaps][Snaps]，可以很方便帮助我们安装和卸载软件。

## 安装

可以通过如下两种方法进行安装。

1. 从 AUR 仓库中安装
2. 从 [Chaotic-AUR][Chaotic-AUR] 安装，(推荐)

### 从 AUR 仓库中安装

```sh
# 如果没有安装 yay
sudo pacman -S yay

# 使用 yay 安装
yay -S pamac-aur
```

### 从 Chaotic-AUR 安装

[Chaotic-AUR][Chaotic-AUR] 是一个由开发者 [Garuda Linux](http://garudalinux.org/) 维护的仓库，仓库的包都是签名和可信任的，可以通过 Pacman 直接安装。

```sh
# 添加仓库，以下命令会安装 keyring 和 mirrorlist
sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key FBA220DFC880C036
sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
```

除了使用上面命令我们还可以手动编辑 `/etc/pacman.conf`，添加如下配置：

```sh
[chaotic-aur]
Include = /etc/pacman.d/chaotic-mirrorlist
```

最后安装 `pamac-aur`：

```sh
sudo pacman -Syu pamac-aur
```

### 检测安装成果

```sh
$ pamac                                                                           130 ↵ ──(一,12月12)─┘
Available actions:
  pamac --version
  pamac --help, -h     [action]
  pamac search         [options] <package(s)>
  pamac list           [options] <package(s)>
  pamac info           [options] <package(s)>
  pamac install        [options] <package(s)>
  pamac reinstall      [options] <package(s)>
  pamac remove         [options] [package(s)]
  pamac checkupdates   [options]
  pamac update,upgrade [options]
  pamac clone          [options] <package(s)>
  pamac build          [options] [package(s)]
  pamac clean          [options]
```

> 安装成功。

## 卸载 pamac

```sh
# 卸载很简单
sudo pacman -Rns pamac-aur
```

[Pamac]: https://wiki.manjaro.org/index.php/Pamac
[libalpm]: https://man.archlinux.org/man/libalpm.3.en
[AUR]: https://aur.archlinux.org/
[Flatpak]: http://flatpak.org/
[Snaps]: https://snapcraft.io/
[Chaotic-AUR]: https://aur.chaotic.cx/
