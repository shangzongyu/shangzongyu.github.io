---
title: 工具推荐：Telegram 相关
description: '主要收集 Telegram 相关的一些工具。'
slug: telegram
date: 2025-07-08 03:52:56+0000
image: cover.jpg
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

- Github：<https://github.com/AyuGram/AyuGramDesktop>
- 平台：macOS/Linux/Winodws
- 开源

特点：



### Swiftgram

- 官网：<https://swiftgram.app/>
- 开源，但是有付费功能

特点：

- 快速格式化
- 
