---
title: "2026 工具推荐: 妙言"
description: 轻量级 Markdown 笔记应用
date: 2026-04-18T00:00:00+08:00
draft: true
tags:
  - macOS
  - Markdown
  - 编辑器
  - 工具
categories: ["工具推荐"]
weight: 1
---

- 官网: <https://miaoyan.app/>
- GitHub: <https://github.com/tw93/MiaoYan>
- App Store: [MiaoYan](https://apps.apple.com/cn/app/miaoyan/id6759252269)

轻量级 Markdown 笔记应用，专为 macOS 设计。

## 主要特点

- 本地优先：数据保存在本地，支持 iCloud Drive
- 无账号、无追踪、无数据收集
- 三栏布局：编辑器和预览区并排显示
- 实时渲染：60fps 双向滚动同步
- 支持暗黑模式
- 支持 LaTeX 数学公式、Mermaid 图表
- 演示模式：将 Markdown 转换为幻灯片
- Swift 6 原生开发，性能优异

## 安装

### App Store

在 Mac App Store 搜索 "MiaoYan"。

### Homebrew

```bash
brew install --cask miaoyan
```

### GitHub

从 GitHub Releases 下载 DMG 安装包。

## 使用

### 基础使用

1. 创建 `MiaoYan` 文件夹（可以在 iCloud Drive 或本地）
2. 在设置中选择笔记文件夹
3. 创建新笔记开始写作

### 分屏模式

左侧编辑，右侧预览，实时同步滚动。

### 演示模式

使用 `---` 分隔符创建幻灯片，可在预览、演示、PPT 模式间切换。

## CLI

```bash
# 安装 CLI
curl -fsSL https://raw.githubusercontent.com/tw93/MiaoYan/main/scripts/install.sh | bash

# 使用
miao open <title|path>    # 打开笔记
miao new <title> [text]   # 创建新笔记
miao cat <title|path>     # 打印笔记内容
miao update               # 更新 CLI
```

## 适用场景

- 需要 Markdown 写作的 Mac 用户
- 重视隐私和数据安全的用户
- 需要本地笔记管理的用户
- 需要演示功能的用户
