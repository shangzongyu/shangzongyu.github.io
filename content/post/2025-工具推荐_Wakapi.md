---
title: 工具推荐：Wakapi
description: ''
slug: wakapi
date: 2025-08-30 08:44:46+0000
tags:
  - tools
weight: 1
---

> 之前使用 [Wakatime](https://wakatime.com/) 记录自己日常编程时间消耗，支持各种不同的编辑器，包括 VSCode 系列、Vim、Emacs 以及 JetBrains 系列。

![wakatime](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_wakatime.webp)

> 有些不好的点是：
>
> 1. 数据存储在别人的服务器；
> 2. 虽然可以免费使用，但是一些功能需要付费。
>
> 最后找到了一个兼容 [Wakatime](https://wakatime.com/) 的工具 Wakapi。

## 介绍

Wakapi 是一个完全开源、自我托管的 WakaTime 兼容后端服务，它可以统计和展示开发者的编程活动。

![Wakapi](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_wakapi.webp)

官网：<https://wakapi.dev/>

## 服务端

安装 Wakapi 服务端相对较简单。启动的时候需要选择一个数据库，Wakapi 支持以下数据库：

- SQLite (默认，易于设置)
- MySQL (推荐，因为经过最广泛的测试)
- MariaDB (开源，MySQL 的一个分支)
- PostgreSQL (开源)
- CockroachDB (云原生、分布式、PostgreSQL 兼容 API)

虽然 Wakapi 支持多种数据库，但是 SQLite 是最简单的一种，我更喜欢使用 SQLite + Wakapi (二进制) 单体部署，因为方便，迁移更容易。

```sh
# 安装二进制
curl -L https://wakapi.dev/get | bash

# 通过配置文件指定
./wakapi --config config.yml
```

## 客户端

Wakapi 支持所有 WakaTime 支持的客户端。可以在以下地址找到所有支持的客户端：

<https://wakatime.com/plugins>

配置客户端很简单。在机器上，打开 `~/.wakatime.cfg` 文件，并添加以下内容：

```ini
[settings]
# Your Wakapi server URL or '<https://wakapi.dev/api>' when using the cloud server
api_url = <http://localhost:3000/api>
# Your Wakapi API key (get it from the web interface after having created an account)
api_key = 406fe41f-6d69-4183-a4cc-121e0c524c2b
```
