---
title: "工具推荐：LocalSend"
description: 跨平台文件传输工具 LocalSend
date: 2026-04-18T20:07:13+08:00
draft: true
tags:
  - 工具
  - 文件传输
categories: ["工具推荐"]
weight: 1
---

## LocalSend

- GitHub: <https://github.com/localsend/localsend>
- 官网: <https://localsend.org/>

我自认为最好的本地传输工具。Blip 需要注册和登录，这个我很不喜欢。

### 特点

- 开源、免费
- 跨平台：Windows, macOS, Linux, Android, iOS, Fire OS
- 不需要登录
- 使用 HTTPS 加密传输
- 局域网内点对点传输
- 端口：TCP/UDP 53317
- 支持文件和文本片段

### 安装

```bash
# macOS
brew install --cask localsend

# Linux
flatpak install flathub org.localsend.localsend_app

# Windows
winget install LocalSend
```

### 使用

- 自动发现局域网内的设备
- 选择目标设备发送文件
- 支持拖拽发送

## Blip

- 官网: <https://blip.net/>
- App Store: [Blip: Send Files in a Click](https://apps.apple.com/us/app/blip-send-files-in-a-click/id6463305181)

需要邮箱登录，这个很不好。

### 特点

- 免费（个人使用）
- 跨平台：Windows, macOS, Android, iOS（Linux 计划中）
- 需要邮箱登录注册
- 支持局域网和互联网传输
- 无文件大小限制
- 端到端加密
- 客户端有通知，点开直接接收
- Mac 状态栏方便，文件直接拖入发送
- 界面友好，速度飞快

### 安装

从官网下载或应用商店安装。

### 使用

- 注册登录后才能使用
- 支持远程传输（通过 Blip 服务器）
- 接收方会收到通知推送

## 对比

| 特性 | LocalSend | Blip |
|------|-----------|------|
| 开源 | ✅ | ❌ |
| 无需登录 | ✅ | ❌ |
| 局域网传输 | ✅ | ✅ |
| 互联网传输 | ❌ | ✅ |
| 文件大小限制 | ❌ | ❌ |
| 通知推送 | ⚠️ | ✅ |
| 状态栏集成 | ✅ | ✅ |
| 加密 | ✅ | ✅ |

## 总结

- **LocalSend**：更推荐，无需登录，完全本地传输，开源
- **Blip**：使用更方便，有通知推送，支持远程传输，但需要登录
