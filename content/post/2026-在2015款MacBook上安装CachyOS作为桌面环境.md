---
title: "在 2015 款 MacBook Pro 上安装 CachyOS 作为桌面环境"
description: 在旧 MacBook 上安装 Linux 桌面环境，配置常用工具和软件
date: 2026-04-18T20:00:00+08:00
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_作为自己的桌面环境_CachyOS.webp
tags:
  - OS
  - Linux
  - MacBook
categories: ["折腾"]
draft: false
---

## 硬件信息

- **硬件**: MacBook Pro 2015 款 (8GB RAM + 512GB SSD)
- **操作系统**: CachyOS

## 安装经历

尝试了多个 Linux 发行版，最终选择了 CachyOS：

1. **Omarchy Linux** - 安装过程顺利，但重启后无法输入密码，放弃
2. **CachyOS** - 安装时无法连接 WiFi，虽然可解决但选择放弃
3. **EndeavourOS** - 对硬件支持良好，支持离线安装，重启后，无法连接 WiFi
4. PopOS - 硬件支持最好，还是 无法连接 WiFi

最终决定还是使用 CachyOS，因为 CachyOS 的性能最好，然后通过连接网线就有网络了，不用折腾 Wifi 了。

## 系统初始化

### 修复 WiFi 连接

2015 款 MacBook Pro 使用 Broadcom BCM4360/BCM43602 无线网卡，需要额外的驱动支持。如果安装时使用网线连接，安装完成后可以按照以下步骤修复 WiFi：

#### 检查无线网卡

```sh
# 查看 PCI 设备信息
lspci | grep -i network

# 查看内核模块
lsmod | grep brcm
```

#### 方法 1：安装 Broadcom 驱动（推荐）

```sh
# 更新系统
sudo pacman -Syu

# 安装 linux-firmware（包含 Broadcom 固件）
sudo pacman -S linux-firmware

# 安装 Broadcom 专有驱动
sudo pacman -S broadcom-wl

# 移除可能冲突的开源驱动
sudo rmmod b43 b43legacy bcma brcm80211 brcmfmac brcmsmac ssb wl

# 加载专有驱动
sudo modprobe wl

# 验证驱动加载
lsmod | grep wl
```

如果上述方法无效，可以尝试使用 DKMS 版本的驱动：

```sh
# 安装 DKMS 版本（需要内核头文件）
sudo pacman -S linux-headers dkms broadcom-wl-dkms

# 重新加载驱动
sudo rmmod wl
sudo modprobe wl
```

#### 方法 2：使用 brcmfmac 驱动

```sh
# 安装相关固件
sudo pacman -S linux-firmware

# 确保 brcmfmac 模块已加载
sudo modprobe brcmfmac

# 检查无线接口
ip link show
```

#### 配置 NetworkManager

```sh
# 确保 NetworkManager 已安装
sudo pacman -S networkmanager

# 启动 NetworkManager 服务
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager

# 使用 nmcli 连接 WiFi
nmcli device wifi list
nmcli device wifi connect "你的WiFi名称" password "你的密码"
```

#### 自动启动 WiFi 驱动

为了确保驱动在每次启动时自动加载，创建配置文件：

```sh
# 创建驱动加载配置
echo "wl" | sudo tee /etc/modules-load.d/wifi.conf

# 禁用可能冲突的开源驱动
echo "blacklist b43" | sudo tee /etc/modprobe.d/blacklist-b43.conf
echo "blacklist b43legacy" | sudo tee /etc/modprobe.d/blacklist-b43legacy.conf
echo "blacklist bcma" | sudo tee /etc/modprobe.d/blacklist-bcma.conf
echo "blacklist brcm80211" | sudo tee /etc/modprobe.d/blacklist-brcm80211.conf
echo "blacklist brcmfmac" | sudo tee /etc/modprobe.d/blacklist-brcmfmac.conf
echo "blacklist brcmsmac" | sudo tee /etc/modprobe.d/blacklist-brcmsmac.conf
echo "blacklist ssb" | sudo tee /etc/modprobe.d/blacklist-ssb.conf
```

### 更新系统

```sh
sudo pacman -Syu
```

### 安装常用软件

#### 文本编辑器 Neovim

```sh
# 安装 Neovim
sudo pacman -S neovim

# 设置为默认编辑器（可选）
sudo ln -s /usr/bin/nvim /usr/bin/vi

# 配置 Neovim（创建基础配置）
mkdir -p ~/.config/nvim
cat > ~/.config/nvim/init.vim << 'EOF'
" 基础配置
set number           " 显示行号
set relativenumber   " 显示相对行号
set autoindent       " 自动缩进
set smartindent      " 智能缩进
set tabstop=4        " tab 宽度
set shiftwidth=4      " 缩进宽度
set expandtab        " 使用空格代替 tab
set cursorline       " 高亮当前行
set mouse=a          " 启用鼠标
set encoding=utf-8   " 编码

" 语法高亮
syntax on

" 插件管理（可选）
" call plug#begin('~/.config/nvim/plugged')
" Plug 'preservim/nerdtree'
" call plug#end()
EOF
```

#### SSH 服务

```sh
# 安装 OpenSSH
sudo pacman -S openssh

# 启动 SSH 服务
sudo systemctl start sshd

# 设置开机自启动
sudo systemctl enable sshd

# 检查服务状态
sudo systemctl status sshd

# 配置 SSH（可选）
sudo vim /etc/ssh/sshd_config

# 常用配置选项：
# PermitRootLogin no  # 禁止 root 登录
# PasswordAuthentication yes  # 启用密码认证
```

#### 基本开发工具

```sh
# 安装基础开发工具链
sudo pacman -S base-devel

# 安装常用开发工具
sudo pacman -S git gcc make cmake pkgconf python python-pip

# 安装版本控制系统
sudo pacman -S git subversion

# 安装调试工具
sudo pacman -S gdb valgrind strace ltrace

# 安装网络工具
sudo pacman -S curl wget net-tools nmap

# 安装文本处理工具
sudo pacman -S grep sed awk ripgrep fzf jq

# 安装压缩解压工具
sudo pacman -S zip unzip tar bzip2 gzip p7zip

# 安装系统监控工具
sudo pacman -S htop btop neofetch tree
```

#### 配置 Git

```sh
# 配置用户信息
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 配置默认分支名

git config --global init.defaultBranch main

# 配置凭证存储
git config --global credential.helper store

# 查看配置
git config --list
```

#### 配置 Python 开发环境

```sh
# 升级 pip
python -m pip install --upgrade pip

# 安装常用 Python 库
pip install --user pipenv virtualenv black pylint mypy

# 配置国内镜像源（可选）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 安装 Pamac 包管理器

[EndeavourOS](https://endeavouros.com/) 是基于 Arch Linux 的发行版，使用 Pacman 作为包管理器。[Pamac](https://wiki.manjaro.org/index.php/Pamac) 是 Manjaro 一款基于 [libalpm](https://man.archlinux.org/man/libalpm.3.en) 的 GUI 包管理工具，支持 AppStream、[AUR](https://aur.archlinux.org/)、[Flatpak](http://flatpak.org/) 以及 [Snaps](https://snapcraft.io/)，可以很方便帮助我们安装和卸载软件。

### 安装方法

有两种安装方法：

#### 方法 1：从 AUR 仓库中安装

```sh
# 如果没有安装 yay
sudo pacman -S yay

# 使用 yay 安装
yay -S pamac-aur
```

#### 方法 2：从 Chaotic-AUR 安装（推荐）

[Chaotic-AUR](https://aur.chaotic.cx/) 是一个由 [Garuda Linux](http://garudalinux.org/) 维护的仓库，仓库的包都是签名和可信任的，可以通过 Pacman 直接安装。

```sh
# 添加仓库，以下命令会安装 keyring 和 mirrorlist
sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key FBA220DFC880C036
sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
```

或者手动编辑 `/etc/pacman.conf`，添加如下配置：

```sh
[chaotic-aur]
Include = /etc/pacman.d/chaotic-mirrorlist
```

最后安装 `pamac-aur`：

```sh
sudo pacman -Syu pamac-aur
```

### 验证安装

```sh
$ pamac
Available actions:
  pamac --version
  pamac --help, -h     [action]
  pamac search         [options] <package(s)>
  pamac list           [options] <package(s)>
  pamac info           [options] <package(s)>
  pamac install        [options] <package(s)>
  pamac reinstall      [options] <package(s)>
  pamac remove         [options] [package(s)>
  pamac checkupdates   [options]
  pamac update,upgrade [options]
  pamac clone          [options] <package(s)>
  pamac build          [options] [package(s)]
  pamac clean          [options]
```

### 卸载 Pamac

```sh
sudo pacman -Rns pamac-aur
```

## 使用技巧

### 关闭终端下 `Tab` 键的蜂鸣提示

修改配置文件：

```sh
sudo vim /etc/inputrc
```

将 `set bell-style none` 前的注释去掉。

### Tailscale VPN

```sh
# 安装命令行版本
sudo pacman -S tailscale
# 启动服务
sudo systemctl start tailscaled
sudo systemctl enable tailscaled
# 登录
sudo tailscale up
```

## 桌面环境安装与配置

CachyOS 提供了丰富的桌面环境选择，从功能完整的桌面环境到轻量级的窗口管理器应有尽有。在 2015 款 MacBook Pro 上，推荐根据内存和使用习惯选择合适的桌面环境。

### CachyOS 支持的桌面环境

- **KDE Plasma** - 功能丰富，界面美观，适合需要高度定制的用户
- **GNOME** - 现代化，易用性高，类似 macOS 的用户体验
- **XFCE** - 轻量级，稳定可靠，适合旧硬件
- **LXQt/LXDE** - 极其轻量，资源占用最少
- **i3/Sway** - 平铺式窗口管理器，高效但学习曲线陡峭
- **Hyprland** - 现代化的平铺式 Wayland 合成器
- **Budgie/Cinnamon** - 传统桌面环境，简单易用

### KDE Plasma 安装与配置

KDE Plasma 是 CachyOS 的默认桌面环境，功能强大且高度可定制。

#### 安装

```sh
# 安装完整的 KDE Plasma 桌面环境
sudo pacman -S plasma-desktop kde-applications

# 安装基础组件（更轻量）
sudo pacman -S plasma-desktop plasma-nm plasma-pa plasma-systemmonitor konsole dolphin

# 安装显示管理器 SDDM
sudo pacman -S sddm sddm-kcm
```

#### 启动和配置

```sh
# 启用 SDDM 显示管理器
sudo systemctl enable sddm

# 重启进入桌面环境
reboot
```

#### 性能优化

对于 2015 款 MacBook，可以进行以下优化：

```sh
# 安装性能监控工具
sudo pacman -S ksysguard

# 减少动画效果
# 系统设置 → 工作区行为 → 桌面效果 → 取消"动画"选项

# 禁用桌面搜索索引（节省资源）
# 系统设置 → 搜索 → Plasma Search → 关闭索引
```

#### 推荐主题和美化

```sh
# 安装主题引擎
sudo pacman -S breeze breeze-gtk kvantum

# 安装 CachyOS Nord 主题
sudo pacman -S kvantum-theme-nord

# 配置应用
sudo pacman -S latte-dock
```

### GNOME 安装与配置

GNOME 提供现代化的用户体验，界面简洁，适合从 macOS 转过来的用户。

#### 安装

```sh
# 安装完整的 GNOME 桌面环境
sudo pacman -S gnome gnome-extra

# 安装显示管理器 GDM
sudo pacman -S gdm
```

#### 启动和配置

```sh
# 禁用 SDDM（如果已安装）
sudo systemctl disable sddm

# 启用 GDM
sudo systemctl enable gdm

# 重启进入桌面环境
reboot
```

#### 推荐扩展和优化

```sh
# 安装 GNOME 扩展管理器和常用扩展
sudo pacman -S gnome-shell-extensions gnome-tweaks

# 从 AUR 安装常用扩展
yay -S gnome-shell-extension-appindicator
yay -S gnome-shell-extension-blur-my-shell
```

#### 性能优化

```sh
# 减少动画效果
gsettings set org.gnome.desktop.interface enable-animations false

# 减少扩展数量，保持桌面清爽
# 安装 → 扩展 → 只启用必要的扩展
```

### XFCE 轻量级桌面环境

XFCE 非常适合旧硬件，资源占用低但功能完整。

#### 安装

```sh
# 安装 XFCE 桌面环境
sudo pacman -S xfce4 xfce4-goodies

# 安装轻量级显示管理器 LightDM
sudo pacman -S lightdm lightdm-gtk-greeter
```

#### 启动和配置

```sh
# 禁用其他显示管理器
sudo systemctl disable sddm
sudo systemctl disable gdm

# 启用 LightDM
sudo systemctl enable lightdm

# 重启
reboot
```

#### 优化配置

```sh
# 安装 Compton 实现窗口特效（可选）
sudo pacman -S picom

# 配置自动启动
# 设置 → 会话和启动 → 应用程序自启动 → 添加 picom
```

### 轻量级窗口管理器

#### i3-gaps 安装

```sh
# 安装 i3-gaps 窗口管理器
sudo pacman -S i3-wm i3blocks i3status dmenu rofi

# 安装终端和文件管理器
sudo pacman -S alacritty thunar

# 配置 i3 作为登录会话
# 在显示管理器中选择 i3 会话
```

#### Hyprland 安装（Wayland 平铺）

```sh
# 从 AUR 安装 Hyprland
yay -S hyprland

# 安装必要的 Wayland 组件
sudo pacman -S waybar wlogout

# 配置文件位置
# ~/.config/hyprland/hyprland.conf
```

### 显示管理器切换

如果需要切换不同的桌面环境和显示管理器：

```sh
# 列出已安装的显示管理器
ls /usr/lib/systemd/system/*dm.service

# 禁用当前显示管理器
sudo systemctl disable sddm
sudo systemctl disable gdm
sudo systemctl disable lightdm

# 启用新的显示管理器
sudo systemctl enable gdm

# 重启
reboot
```

### 桌面环境切换注意事项

1. **备份重要数据**：在切换桌面环境前务必备份配置文件
2. **分步操作**：先安装新环境，确认正常运行后再卸载旧环境
3. **依赖清理**：移除桌面环境时使用 `-Rns` 清理不需要的依赖
4. **测试驱动**：如果是 NVIDIA 显卡，注意不同桌面环境可能需要不同的驱动配置

```sh
# 卸载 KDE Plasma
sudo pacman -Rns plasma plasma-desktop kde-applications

# 卸载 GNOME
sudo pacman -Rns gnome gnome-extra

# 清理缓存
sudo pacman -Sc
```

## 总结

CachyOS 作为基于 Arch Linux 的发行版，在 2015 款 MacBook Pro 上运行良好，对硬件的支持非常好。通过安装 Pamac 包管理器，可以方便地管理各种软件包，包括 AUR、Flatpak 和 Snap 仓库中的软件。

CachyOS 提供了多种桌面环境选择，从功能完整的 KDE Plasma 和 GNOME，到轻量级的 XFCE 和窗口管理器。对于 8GB 内存的 MacBook Pro，推荐使用 XFCE 或配置优化的 KDE Plasma，在性能和用户体验之间取得平衡。
