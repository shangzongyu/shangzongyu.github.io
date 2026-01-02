---
title: 工具推荐：Telegram 相关
description: 主要收集 Telegram 相关的一些工具。
slug: telegram
date: 2025-07-08 03:52:56+0000
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_2025-工具推荐_Telegram-相关.webp
weight: 1
---

> 主要收集 Telegram 相关的一些工具。

## Telegram Search

> 介绍：一个功能强大的 Telegram 聊天记录搜索工具，支持向量搜索和语义匹配。基于 OpenAI 的语义向量技术，让你的 Telegram 消息检索更智能、更精准。

- Github：<https://github.com/groupultra/telegram-search>

### 使用

> 使用 Docker/Podman 启动这样更简单一些，不用自己额外装软件，对小白友好。

```sh
# 克隆仓库
git clone https://github.com/GramSearch/telegram-search.git
cd telegram-search

# 复制配置文件
cp config/config.example.yaml config/config.yaml

# 启动

## 1. Docker 启动
docker compose up -d

## 2. Podman 启动
## 如果是 macOS，需要启动 podman machine，使用命令：podman machine start
podman-compose up -d
```

启动后就可以在 `http://localhost:3333` 看到界面。

> PS：需要修改配置文件 `config.yml`
> 1。`database.host` 的值为数据库容器的服务名称 “pgvector”
> 2。修改 `api.telegram.apiKey` 为自己的 Open API Key。

## 第三方客户端

### AyuGram

AyuGram 是一个基于 Telegram 的第三方开源客户端，提供 Android 和桌面版本，主打做官方客户端做不到的「增强功能」。 对重度聊天 / 社群用户来说，它更像是一个带很多隐藏功能的「Telegram Pro」。

- Github: <https://github.com/AyuGram/AyuGramDesktop>

**核心特性**: 

- **Ghost 模式**：可以隐藏已读、隐藏在线、隐藏输入状态，还支持通过延迟发送实现“上线不暴露”的发送方式，Android 和桌面端都支持。
- **消息历史 & 防撤回**：保存更完整的聊天记录，即使清理缓存也保留，并可以查看被删除 / 撤回的消息。
- 消**息过滤与 Premium 外观**：支持过滤广告 / 黑名单用户消息、从受限频道转发（AyuForward）、本地解锁类似 Premium 的 UI 和一些额外 UI 定制。

**开源与平台**:

- Android 端 AyuGram4A、桌面端 AyuGramDesktop 都托管在 GitHub，采用 GPLv3 协议，社区可以自行编译或审计代码。
- 桌面端支持 Windows / Linux / macOS，有字体定制、Streamer 模式、消息截图 Shot 等桌面特化功能。

> 总结：AyuGram 更适合：在 PC / Android 上重度用 Telegram、对隐私控制、防撤回、消息存档和 UI/行为高度可配置有需求的用户。

### Swiftgram

Swiftgram 是一款面向 iOS 的 Telegram mod 客户端，强调隐私、无广告和无使用限制，同时保持接近官方的操作体验。 它集成了 Telegram 最新功能，并在账号管理和通知体验上做了明显增强。

- 官网: <https://swiftgram.app/>
![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_2025-工具推荐_Telegram-相关-Swiftgram-00.webp)

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_2025-工具推荐_Telegram-相关-Swiftgram-01.webp)

**核心特性**:

- **无限账号 + 账号备份**：号称支持无限数量账号，并提供账号备份功能，可以在不重新收验证码的情况下快速恢复登录，非常适合多号场景。
- **隐私与无广告**：官方简介明确强调全无广告、无追踪，聚焦隐私；同时兼容 Telegram 的更新，不会因功能落后影响使用。
- **iOS 生态增强**：支持更灵活的聊天标签 / 文件夹管理、通知细粒度控制，一些版本还提到 Stories 隐身浏览等增强功能。

**平台与开源声明**:

- 通过 App Store 分发，描述中称完全开源，需要到官方站点或仓库进一步查看源码位置。
- 社区评价里经常被当作 iOS 上「原版替代品」，很多人因为无限账号等特性直接用它替换官方客户端。

> 总结：Swiftgram 更适合：主力用 iPhone（加 Apple Watch）聊天、账号多、希望在原版基础上小幅增强但又不想被广告和追踪打扰的用户。

### 简要对比

| 维度 | AyuGram | Swiftgram |
| ---- | ------- | --------- |
| 平台 |	Android + 桌面（Win/Linux/macOS）| iOS（并兼容 Telegram 最新特性）|
| 核心卖点|	Ghost 模式、防撤回、消息历史、深度定制、本地 Premium 外观  | 无限账号、账号备份、隐私优先、无广告、通知/聊天管理增强 |
| 开源与形态	| GitHub 开源，GPLv3，适合想自己审计或编译的用户；更偏「功能密集」的高级客户端 | App Store 分发，宣称 100% 开源、无追踪，更接近官方体验但加上多账号和隐私增强 |

总结：

- PC/Android 重度用户、在意防撤回 + Ghost 模式，优先选 AyuGram
- 主力在 iOS、账号多、想要「无广告原版升级」，则更偏向 Swiftgram。
