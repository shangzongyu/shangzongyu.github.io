---
title: "Siftly：让 Twitter 书签变身智能知识库"
slug: "siftly让-twitter-书签变身智能知识库"
date: 2026-08-06T18:02:42+08:00
draft: true
categories:
  - 未分类
tags: []
weight: 1
---
还在为 Twitter/X 书签管理发愁吗？[Siftly](https://github.com/viperrcrypto/Siftly) 是一个本地自托管的书签管理工具，用 AI 自动分类，还能生成思维导图。

<!--more-->

## 核心功能

### 1。AI 智能分类

自动运行 4 阶段管道：
- **实体提取** — 提取标签、链接、提及
- **视觉分析** — 识别图片内容 (文字、物体、场景)
- **语义标记** — 生成 25-35 个可搜索标签
- **自动分类** — 分配 1-3 个类别

### 2。自然语言搜索

不只是关键词搜索，试试：
- “有趣的加密货币崩盘梗图”
- “React hooks 教程”
- “最好的 AI 编程工具”

### 3。思维导图可视化

交互式思维导图展示所有书签，按类别自动组织，点击节点即可跳转原文。

### 4。零云服务

所有数据保存在本地 SQLite，只有 AI 调用才需要联网。无需账号，无需订阅。

## 快速上手

### 一键启动

```bash
git clone https://github.com/viperrcrypto/Siftly.git
cd Siftly
./start.sh
```

自动安装依赖、设置数据库、打开浏览器，访问 http://localhost:3000

### 导入书签

无需浏览器插件：

1. 打开 Siftly 的导入页面
2. 将 “Export X Bookmarks” 链接拖到书签栏
3. 访问 x.com/i/bookmarks 并点击书签栏按钮
4. 点击 “Auto-scroll” 自动抓取所有书签
5. 导出 JSON 文件并在 Siftly 中上传

AI 分类会在导入后自动开始。

## AI 配置

如果你有 [Claude Code CLI](https://claude.ai/code)，直接使用现有订阅，无需配置 API key。

否则：
1. 访问 console.anthropic.com 创建 API key
2. 在 Siftly 设置页面粘贴

新账户有 5 美元免费额度，足够处理几千条书签。

## 其他功能

- **多视图浏览** — 网格或列表视图，按类别、媒体类型过滤
- **导出功能** — CSV、JSON 或 ZIP 格式
- **命令面板** — 按 Cmd+K 全局搜索

## 技术栈

- Next.js 16 + TypeScript
- SQLite + Prisma
- Tailwind CSS
- Anthropic AI API

## 总结

Siftly 特别适合经常在 Twitter 上收藏内容的开发者或研究者。本地运行保证隐私，AI 分类让书签真正变成可搜索的知识库。

项目地址：https://github.com/viperrcrypto/Siftly
