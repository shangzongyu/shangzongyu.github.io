---
title: 'GLM 4.5 配置全攻略：Claude Code 与 Codex 实战指南'
description: '智谱最新推出的 **GLM 4.5** 是一款面向编程和智能应用的通用大模型，相比前一代在**代码生成、复杂推理、对话体验**等方面有了显著提升。'
slug: glm-45-claude-code-codex
date: 2025-09-27 08:22:56+0000
tags:
    - ai
    - tools
weight: 1
---


## 简介

智谱最新推出的 **GLM 4.5** 是一款面向编程和智能应用的通用大模型，相比前一代在**代码生成、复杂推理、对话体验**等方面有了显著提升。
它不仅支持在交互式编程中作为助手使用，还可以集成到 **Claude Code** 和 **Codex** 工具中，帮助开发者更高效地完成编码、调试和文档处理等任务。

本文将介绍 GLM 4.5 在 **Claude Code** 和 **Codex** 中的配置方法，帮助你快速上手。
目前智谱还推出了一个 **“编程套餐” GLM Coding Plan**，有限时优惠，基础版本 3 个月仅需 60 元，我也入手体验了一下。

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2025/upgit_20250927_GLM4.5-Coding-Plan.png)

在使用 Claude Code 和 Codex 前，需要先安装 **Node.js**。

```sh
# 安装 Node.js
brew install node@22
```

---

## Claude Code

官网文档地址：[https://docs.bigmodel.cn/cn/coding-plan/tool/claude](https://docs.bigmodel.cn/cn/coding-plan/tool/claude)

### 安装

```sh
npm install -g @anthropic-ai/claude-code
```

### 配置

通过环境变量进行配置：

```sh
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/coding/paas/v4"
export ANTHROPIC_AUTH_TOKEN="your Zhipu API key"
```

> API Key 可在[这里](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys)获取。
> 注意：`ANTHROPIC_BASE_URL` 必须设置为 [`https://open.bigmodel.cn/api/coding/paas/v4`，这是智谱专门为编程提供的端点。](https://open.bigmodel.cn/api/coding/paas/v4，这是智谱专门为编程提供的端点。)

配置完成后即可使用：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2025/upgit_20250927_GLM4.5-Claude-Code.png)

### FAQ

#### 1、错误处理 `API Error`

若出现类似 **“API Error 401 ”** 的报错，只需删除旧的 API Key，重新生成一个新的即可解决。

错误如下图：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2025/upgit_20250927_SCR-20250922-orcl.png)

#### 2、模型选择

Claude Code 内置了两个模型环境变量：

* `ANTHROPIC_MODEL`：使用 `GLM-4.5` (适用于对话、规划、代码编写、复杂推理等场景)。

* `ANTHROPIC_SMALL_FAST_MODEL`：使用 `GLM-4.5-Air` (适用于文件搜索、语法检查等辅助场景)。


该组合在性能与速度之间取得了较好的平衡，也是官方推荐的默认方案。
目前不支持其他模型 (如 `GLM-4.5-X`、`GLM-4.5-AirX`、`GLM-4.5-Flash`)。

---

## Codex

> 在撰写本文时，智谱官方尚未提供 Codex 的完整配置方案。

### 安装

```sh
npm install -g @openai/codex@latest
```

### 配置

```sh
# 设置环境变量
export GLM_API_KEY="your Zhipu API key"

# 编辑配置文件 ~/.codex/config.toml（若不存在则新建），内容如下：
model_provider = "glm"
model = "glm-4.5"

[model_providers.glm]
name = "zai"
base_url = "https://open.bigmodel.cn/api/coding/paas/v4"
env_key = "GLM_API_KEY"
```

> **提示**：`env_key` 必须与之前设置的环境变量 `GLM_API_KEY` 一致。

配置完成后即可使用：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2025/upgit_20250927_GLM4.5-Codex.png)

---

## 总结

GLM 4.5 在**编程辅助**、**复杂推理**和**高效交互**等方面展现了强大的能力。通过结合 **Claude Code** 与 **Codex**，开发者可以快速将其集成到工作流中，提升开发效率和体验。

随着 GLM 在更多工具和生态中的支持不断完善，它将不仅是一个**编程助手**，更可能成为未来**智能开发环境**的核心组成部分。

---

## 后记

本文由我原创撰写，并通过 AI 辅助进行了语言润色与排版优化，以提升可读性和表达效果。核心内容与观点均为本人所有。
