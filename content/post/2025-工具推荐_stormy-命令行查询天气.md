---
title: "工具推荐：stormy 命令行查询天气"
description:
date: 2025-11-17T14:28:42+08:00
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251117_stormy-cover.webp
tags:
  - weather
  - command-line
  - tools
weight: 1
---

之前介绍过一个通过命令找查询天气的工具[工具推荐：wttr-命令行查询天气。]({{< relref "post/2022-工具推荐_wttr-命令行查询天气.md" >}})，这次主要介绍另外一款命令行查询工具 [stormy](https://github.com/ashish0kumar/stormy)。

我自己感觉这个项目的好处就是给一个二进制的命令行执行进行查询，缺点就是只支持英文。

## 安装

```sh
go install github.com/ashish0kumar/stormy@latest
```

## 基本使用

```sh
# Basic usage
stormy

# Specify city via command line
stormy --city "New York"

# Use imperial units
stormy --units imperial

# Use compact display mode
stormy --compact

# Show version
stormy --version

# Show help
stormy --help
```

## 实际使用

在第一次执行的时候会新建配置文件：

![stormy-first](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251117_stormy-01.webp)

然后接着使用：

![stormy](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251117_stormy.webp)

使用的时候发现问题，如果使用 “Shen Zhen” 这样查询不可以，但是查询其他非中文的类似 “New York” 的可以，中文使用类似这样的 “ShenZhen”。

我们还可以通过配置某一个城市，这样之后字节查询配置城市的，我的配置如下：

```ini
provider = "OpenMeteo"
api_key = ""
city = "ShenZhen"
units = "metric"
showcityname = true
use_colors = true
live_mode = false
compact = false
```

> PS: OpenMeteo 这个不用设置 API key，provider 还支持 [OpenWeatherMap](https://openweathermap.org/api) ，不过这个需要添加 API Key。

## Wttr.in 和 Stormy 的比较

wttr.in 和 stormy 都是命令行天气查询工具，但它们在功能、数据来源、定制性和实现语言等方面有显著差异。

### 功能对比

| 项目      | wttr.in                                            | stormy                                                      |
| --------- | -------------------------------------------------- | ----------------------------------------------------------- |
| 数据来源  | 自有 API（聚合多源），支持机场编码、特殊地名等查询 | OpenMeteo（默认、免 API Key）、OpenWeatherMap（需 API Key） |
| 输出格式  | ANSI、纯文本、HTML、PNG、JSON、Prometheus、地图等  | 纯文本、ASCII 艺术、Neofetch 风格                           |
| 展示内容  | 当前天气、预测、多地查询、月相、地图、天文信息     | 当前天气（温度、风速、湿度、降水）、ASCII 图标展示          |
| 国际化    | 多语言支持（54种）、自动选择单位/语言              | 主要基于英文，单位可选                                      |
| 集成方式  | shell、tmux、conky、IRC、Web、小组件等             | 本地 CLI，配置文件管理                                      |
| 定制/扩展 | 支持参数自定义格式、单位、显示内容                 | 可选数据源、城市、单位、展示格式，支持 config 文件          |
| 技术实现  | Python、Go 等                                      | Go                                                          |
| 用户基数  | 日查询量 2200万~2700万，用户约18万~21万            | 社区较小，约130星（2025.7），轻量个人项目                   |

### 核心差异解析

#### 数据源与配置灵活性

- wttr.in 集成多种数据源且无需配置 API Key，支持机场代码与特殊地名，适合需要高自由度和多样化查询场景。[1]
- stormy 则强调本地化 (默认 OpenMeteo 免费、OpenWeatherMap 需 key)，配置灵活，适合希望自定义数据源、格式和信息展示的用户。[2]

#### 输出样式和集成方式

- wttr.in 提供多种展示风格 (终端彩色、网页、图片、JSON、Prometheus)，并易于嵌入系统状态栏、tmux、网页小组件、IRC 等，适合自动化和多平台集成。[1]
- stormy 灵感来源于 Neofetch，聚焦本地 CLI、简洁美观的终端 ASCII 图形，主要面向视觉美学和个性化定制。[2]

#### 国际化与扩展性

- wttr.in 支持 54 种语言，地名输入高度兼容 Unicode，用法极其灵活。[1]
- stormy 目前主要英文说明，国际化支持有限，但配置较为简洁直接。[2]

#### 技术架构与社区

- wttr.in 基于 Python 主体并集成 Go、Shell 等，稳定成熟，社区巨大、贡献者众多。[1]
- stormy 纯 Go 实现，更轻量、代码简洁、适合快速自定义和二次开发，但社区较小。[2]

### 适用建议

- 需要多端集成、丰富格式、国际化支持，或对自动化脚本/网页嵌入有需求，可优先考虑 wttr.in。[1]
- 倾向本地纯 CLI、视觉美观、配置简单、可选天气源并对 Go 生态有偏好者可选 stormy。[2]

以上对比涵盖两个项目的核心特性与定位区别。[2][1]

[1](https://github.com/chubin/wttr.in)
[2](https://github.com/ashish0kumar/stormy)

