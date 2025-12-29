---
title: "2025 Fresh 终端编辑器新选择"
description: 
date: 2025-12-26T17:38:01+08:00
image: 
math: 
license: 
hidden: false
comments: true
draft: true
---

Github：https://github.com/sinelaw/fresh
文档： https://sinelaw.github.io/fresh/

## 介绍

Fresh 是一个用 Rust 编写的现代终端文本编辑器，专为追求熟悉 GUI 体验的后端开发者设计。不同于 Vim/Helix 的模态编辑，Fresh 提供非模态、多光标、鼠标支持，能高效处理多 GB 大文件（2GB 文件仅需 36MB 内存，加载 600ms）。

## 安装

```sh
# macOS
brew tap sinelaw/fresh
brew install fresh-editor

# Arch Liux
yay -S fresh-editor
```

核心导航：

Cmd+P / Ctrl+P：命令面板（搜索命令、文件）
Cmd+T：文件查找（模糊搜索，Git 集成）
Cmd+S：保存
Cmd+/：切换注释
鼠标：全支持（选择、滚轮、中键粘贴）


## 基础编辑操作

Fresh 默认非模态，直接像 VSCode 一样编辑：

| 操作	| 快捷键	| 说明 |
|----|-----|-----|
| 多光标	| Option+Click / Ctrl+D	| 选中相同词语 |
| 块选择	| Shift+Option+拖动	| 列编辑 |
| 撤销/重做| 	Cmd+Z / Cmd+Shift+Z	| 多级历史 |
| 查找替换	| Cmd+F / Cmd+Option+F| 	正则支持，选区替换 |
| 跳转定义	| Cmd+Click（LSP）| 	Go/Python/TS 自动 |

大文件优势：编辑 Kafka 日志、PostgreSQL 导出、MongoDB JSON 无延迟

## 高级功能

### Git 集成

- `Cmd+Shift+G`：Git 状态（分支、变更）

文件浏览器显示 Git 图标（M/A/D）

### 插件系统

TypeScript + Deno 沙箱，官方插件已内置文件浏览器、LSP、Git。

# 开发插件
deno run --allow-all plugin.ts
