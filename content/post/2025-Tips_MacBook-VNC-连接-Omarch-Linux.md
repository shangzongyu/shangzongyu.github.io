---
title: "Tips：MacBook VNC 连接 Omarchy Linux"
description: 
date: 2025-11-18T19:17:00+08:00
image: 
math: 
license: 
tags:
  - tips
  - Linux
  - VNC
hidden: false
comments: true
---

## 前言

换了一个新的办公环境，新的办公桌比之前小不少，导致我的两个显示器放不下（两个显示器一个被 Omarhcy 使用，一个被 MacBook 使用），MacBook 是我的主力机，因此就能把 Linux 的显示器去掉，Linux 我平常使用 SSH 直接连接的，但是偶尔使用 GUI，我想折腾下。

!<!--more-->

最初就是找到 [Tiger VNC](https://tigervnc.org/) ，使用 VNC Server 搭建一个服务器，然后通过 Mac 的 VNC Client 连接，但是执行过程有关问题：

TigerVNC 主要是基于 X11 的 VNC 服务器，但是 Omarchy Linux 使用的 Hyprland 是基于 Wayland 的窗口管理器，Wayland 与传统 X11 不兼容。这就很难搞了，就算配置了也有各种问题。

就需要换一个兼容 Wayland 的 VNC Server, 通过询问 AI 找到了 [wayvnc](https://github.com/any1/wayvnc)，WayVNC 专为无窗口管理器依赖的 Wayland 环境设计，刚好符合我们的场景。

## 安装

```sh
sudo pacman -S wayvnc
```

## 启动

在启动之前需要简单配置下：

配置文件在 `~/.config/wayvnc/config`：

```ini
address=0.0.0.0
```

配置之后就可以通过：`wayvnc -C ~/.config/wayvnc/config` 来启动了，不过每次都要手动启动很麻烦，而且 `wayvnc` 不支持 daemon 模式，非常不方便，因此使用 `systemd` 进行管理。

新建 wayvnc 的 service 文件  `~/.config/systemd/user/wayvnc.service` 内容如下：

```ini
text
[Unit]
Description=WayVNC Server
After=graphical-session.target

[Service]
# 替换 with your username 路径
ExecStart=/usr/bin/wayvnc -C /home/shine/.config/wayvnc/config
Restart=always
Environment=WAYLAND_DISPLAY=wayland-0
Environment=XDG_RUNTIME_DIR=/run/user/$(id -u)

[Install]
WantedBy=default.target
```

> 注意：`ExecStart` 配置命令的的时候需要指定绝对路径。

之后就可以：

```sh
systemctl --user daemon-reload # 每次修改玩 serive 文件重新加载
systemctl --user enable --now wayvnc.service # 设置开机自启动
systemctl --user start wayvnc.service # 启动
systemctl --user stop wayvnc.service # 关闭
systemctl --user status wayvnc.service # 查看状态
```

## 配置

wayvnc 的基本配置主要通过配置文件 `~/.config/wayvnc/config` ，关键配置项包括：

- `address`：监听地址，默认是 `127.0.0.1`。设置为 `0.0.0.0` 允许所有网络接口远程连接。
- `port`：监听的端口，默认是 `5900`。
- `enable_auth`：是否启用身份认证（密码验证），默认 `false`。
- `username`：用于登录的用户名（如果启用认证）。
- `password`：认证密码（需要使用 `vncpasswd` 工具生成）。
- `private_key_file` 和 `certificate_file`：用于启用 TLS 加密的私钥和证书文件路径。
- `session`：指定 Wayland 显示输出，如 `HEADLESS-1`，多显示器环境可用。
- `always_shared`：是否允许多个客户端共享同一会话。
- `idle_autokill`：空闲自动关闭时间（秒），避免长时间闲置浪费资源。
- `clipboard`：是否启用剪贴板同步。
- `verbose`：开启详细日志。

示例配置文件内容：

```ini
address=0.0.0.0
port=5900
enable_auth=true
username=jojo
password=your_vnc_password_file_path
private_key_file=/path/to/private.pem
certificate_file=/path/to/cert.pem
session=HEADLESS-1
always_shared=true
idle_autokill=600
clipboard=true
verbose=false
```

这些配置允许你控制监听接口、安全认证、加密、会话管理等主要远程桌面参数。

## 连接 VNC Server 的客户端

> 我主要使用 MacBook 连接，因此选择支持 MacOS 的。

### TigerVNC

![tiger-vnc](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251119_tiger-vnc.webp)

[TigerVNC Viewer](https://tigervnc.org/) 

- 优点： 支持多平台，性能好
- 缺点：界面比较丑(自认为的缺点)

### Screens

![screens](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251119_screens.webp)

[Screens](https://edovia.com/en/screens) - 一款跨苹果生态（iPhone、iPad、Mac、Vision Pro）远程桌面客户端应用，

**特点包括**：

- 提供流畅、直观的远控体验，支持多个连接和多显示器切换。
- 支持强加密和内置 SSH 隧道，确保连接安全，适合对安全要求高的使用场景。
- 支持苹果设备的硬件键盘、触控板、鼠标操作，交互自然顺畅。
- 独特的 Curtain Mode（屏幕遮蔽模式）保护远程会话的隐私。
- 支持文件拖拽传输，方便管理远程文件。
- 兼容多平台，包括控制 Mac、Linux、Raspberry Pi 和 Windows 电脑。
- 通过 Screens Connect 服务实现跨网络无复杂配置的远程连接。

**缺点**:

- 主要定位苹果设备生态，Windows 等 PC 端作为远程控制端支持有限。
- 远程 Windows/Linux 设备只能发送/接收文本和 URL，不支持声音传输。
- 需要远程设备安装并运行支持的 VNC Server（如 UltraVNC、TightVNC）。

## FAQ

使用 `wayvnc 0.0.0.0` 报错如下：

```sh
ERROR: ../wayvnc/src/main.c: 540: WAYLAND_DISPLAY is not set in the environment
ERROR: ../wayvnc/src/main.c: 2069: Failed to initialise wayland`
```

原因：因为 SSH 会话没有继承到图形用户会话的 Wayland 环境变量，wayvnc 需要连接正在运行的 Wayland 会话才能工作，而 SSH 默认没有 Wayland 图形会话上下文。
解决：登录图形终端然后执行 `wayvnc 0.0.0.0`