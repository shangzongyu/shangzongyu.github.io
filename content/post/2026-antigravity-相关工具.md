---
title: "2026 Antigravity 相关工具"
description: 
date: 2026-01-08T09:49:45+08:00
image: 
math: 
license: 
hidden: false
---

> 主要介绍使用 Antigravity 相关的工具。

Antigravity 是 Google 的 Editor。

- 官网: <https://antigravity.google/>

## Antigravity Tools

- Github: <https://github.com/lbjlaq/Antigravity-Manager>

介绍：您的个人高性能 AI 调度网关，不仅仅是账号管理，更是打破 API 调用壁垒的终极解决方案。

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260110_antigravity-tools-00.webp)

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260110_antigravity-tools-00.webp)

### 深度功能解析 (Detailed Features)

#### 1.  智能账号仪表盘 (Smart Dashboard)

- **全局实时监控**: 一眼洞察所有账号的健康状况，包括 Gemini Pro、Gemini Flash、Claude 以及 Gemini 绘图的 **平均剩余配额**。
- **最佳账号推荐 (Smart Recommendation)**: 系统会根据当前所有账号的配额冗余度，实时算法筛选并推荐“最佳账号”，支持 **一键切换**。
- **活跃账号快照**: 直观显示当前活跃账号的具体配额百分比及最后同步时间。

#### 2. 强大的账号管家 (Account Management)

- **OAuth 2.0 授权（自动/手动）**: 添加账号时会提前生成可复制的授权链接，支持在任意浏览器完成授权；回调成功后应用会自动完成并保存（必要时可点击“我已授权，继续”手动收尾）。
- **多维度导入**: 支持单条 Token 录入、JSON 批量导入（如来自其他工具的备份），以及从 V1 旧版本数据库自动热迁移。
- **网关级视图**: 支持“列表”与“网格”双视图切换。提供 403 封禁检测，自动标注并跳过权限异常的账号。

#### 3. 协议转换与中继 (API Proxy)

- **全协议适配 (Multi-Sink)**:
  - **OpenAI 格式**: 提供 `/v1/chat/completions` 端点，兼容 99% 的现有 AI 应用。
  - **Anthropic 格式**: 提供原生 `/v1/messages` 接口，支持 **Claude Code CLI** 的全功能（如思思维链、系统提示词）。
  - **Gemini 格式**: 支持 Google 官方 SDK 直接调用。
- **智能状态自愈**: 当请求遇到 `429 (Too Many Requests)` 或 `401 (Expire)` 时，后端会毫秒级触发 **自动重试与静默轮换**，确保业务不中断。

#### 4. 模型路由中心 (Model Router)

- **系列化映射**: 您可以将复杂的原始模型 ID 归类到“规格家族”（如将所有 GPT-4 请求统一路由到 `gemini-3-pro-high`）。
- **专家级重定向**: 支持自定义正则表达式级模型映射，精准控制每一个请求的落地模型。
- **智能分级路由 (Tiered Routing)**: [新] 系统根据账号类型（Ultra/Pro/Free）和配额重置频率自动优先级排序，优先消耗高速重置账号，确保高频调用下的服务稳定性。
- **后台任务静默降级**: [新] 自动识别 Claude CLI 等工具生成的后台请求（如标题生成），智能重定向至 Flash 模型，保护高级模型配额不被浪费。

#### 5.  多模态与 Imagen 3 支持

- **高级画质控制**: 支持通过 OpenAI `size` (如 `1024x1024`, `16:9`) 参数自动映射到 Imagen 3 的相应规格。
- **超强 Body 支持**: 后端支持高达 **100MB** 的 Payload，处理 4K 高清图识别绰绰有余。

## OpenCode 中使用 antigravity

- Github: <https://github.com/NoeFabris/opencode-antigravity-auth>

最简单的，把下面的文字复制到 LLM Agent (Claude Code, OpenCode, Cursor, etc.)：

```sh
Install the opencode-antigravity-auth plugin and add the Antigravity model definitions to ~/.config/opencode/opencode.json by following: https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/dev/README.md
```



通过  `opencode auth login` 登录多个 Google 账号，插件会自动切换账号，当一个账号的被 limit 后。