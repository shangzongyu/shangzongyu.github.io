---
title: "工具推荐：CC Switch - AI 编码助手统一管理器"
description: 统一管理 Claude Code、Codex、Gemini CLI、OpenCode 和 OpenClaw 的桌面应用
date: 2026-04-18T21:09:23+08:00
image:
math:
license:
hidden: false
comments: true
categories: ["工具推荐"]
tags: ["AI工具", "开源", "Rust"]
weight: 1
---

CC Switch 是一个跨平台桌面应用，用于统一管理多个 AI 编码 CLI 工具，包括 Claude Code、Codex、Gemini CLI、OpenCode 和 OpenClaw。

## 为什么需要 CC Switch？

现代 AI 编程依赖于多个 CLI 工具，每个工具都有自己的配置格式。切换 API 提供商意味着手动编辑 JSON、TOML 或 `.env` 文件，并且没有统一的方式来管理多个工具的 MCP 和 Skills。

**CC Switch** 提供了一个单一桌面应用来管理所有五个 CLI 工具。你可以：

- 一键导入和切换 API 提供商
- 使用 50+ 内置预设
- 统一管理 MCP 和 Skills
- 快速系统托盘切换
- 可靠的 SQLite 数据库保护配置

## 支持的工具

- **Claude Code** - Anthropic 的 AI 编码助手
- **Codex** - OpenAI 的编码工具
- **Gemini CLI** - Google 的 Gemini 工具
- **OpenCode** - 编码助手
- **OpenClaw** - AI 编码工具

## 主要功能

### 统一管理

- **单一界面**：一个应用管理所有五个 CLI 工具
- **不再手动编辑**：50+ 提供商预设，包括 AWS Bedrock、NVIDIA NIM 等
- **快速切换**：即时切换不同提供商和模型

### MCP 管理

- 统一的 MCP 服务器管理
- 跨应用 MCP 同步
- 一键安装和配置

### Skills 管理

- Skills 一键安装
- 支持 GitHub 仓库和 ZIP 文件
- 自定义仓库管理
- 符号链接和文件复制支持

### 系统托盘

- 快速切换功能
- 最小化到托盘
- 方便的快捷操作

## 安装

### macOS (Homebrew)

```bash
brew tap farion1231/ccswitch
brew install --cask cc-switch
```

### 更新

```bash
brew upgrade --cask cc-switch
```

### 其他平台

访问 [GitHub Releases](https://github.com/farion1231/cc-switch/releases) 下载对应平台的安装包：

- Windows: `.msi` 安装程序或 `.zip` 便携版
- Linux: `.AppImage` 或 `.deb`
- macOS: `.dmg`

## 使用

### 基本工作流程

1. **启动 CC Switch**：打开应用
2. **添加提供商**：点击导入按钮，选择预设或手动配置
3. **配置 MCP**：在 MCP 标签页管理服务器
4. **安装 Skills**：浏览 GitHub 仓库一键安装
5. **开始使用**：配置完成后直接使用 CLI 工具

### 配置文件

CC Switch 使用 SQLite 数据库存储配置，确保：

- 原子写入保护配置
- 快速检索和切换
- 备份和恢复功能

## 技术栈

- **前端**：TypeScript + Vue 3
- **后端**：Rust + Tauri
- **数据库**：SQLite
- **跨平台**：支持 Windows、macOS、Linux

## GitHub

- **仓库**：[https://github.com/farion1231/cc-switch](https://github.com/farion1231/cc-switch)
- **Star 数**：34.3k+
- **许可**：MIT License

## 常见问题

### 哪个 AI CLI 工具最好？
CC Switch 支持五个工具，每个都有专门的提供商配置。根据你的需求选择：
- **Claude Code**：适合需要高级推理的场景
- **Codex**：适合 OpenAI 生态
- **Gemini CLI**：适合 Google 服务
- **OpenCode/OpenClaw**：轻量级选择

### 为什么不能删除当前活动的提供商？
CC Switch 遵循"最小干扰"设计原则，确保至少有一个提供商可用。

### 配置文件在哪？
- **macOS**：`~/Library/Application Support/cc-switch/`
- **Windows**：`%APPDATA%/cc-switch/`
- **Linux**：`~/.config/cc-switch/`

---

CC Switch 是管理多个 AI 编码工具的绝佳选择，特别是当你需要在不同的提供商和工具之间频繁切换时。
