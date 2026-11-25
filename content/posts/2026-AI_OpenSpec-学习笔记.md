---
title: "OpenSpec 的学习笔记"
description: "记录 OpenSpec 的核心概念、工作流、文件结构和适用场景。"
slug: openspec-notes
date: 2026-09-09T00:00:00+08:00
draft: true
categories:
  - AI
tags:
  - OpenSpec
  - AI 编程
  - 规格驱动开发
featuredImage: ""
weight: 1
---

OpenSpec 是一个面向 AI 编程助手的规格驱动开发工具。它想解决的问题很直接：不要把需求只留在聊天记录里，而是先把 “为什么做、要做到什么程度、准备怎么做” 写成可审查的文件，再让 AI 去实现。

<!--more-->

官网：<https://openspec.dev/>

GitHub：<https://github.com/Fission-AI/OpenSpec>

## 它解决什么问题

我理解 OpenSpec 的核心价值不是 “多写几份文档”，而是给 AI 编程加一个明确的停顿点。

平时直接让 AI 写代码，容易遇到几个问题：

- 需求边界藏在对话里，过几轮之后就开始漂移
- AI 很快进入实现状态，但我们还没确认 “做成什么样才算完成”
- 代码改完之后，很难反推当时的决策依据
- 多人协作时，聊天记录不是一个稳定的交接物

OpenSpec 的做法是把这些东西落到仓库里的 `openspec/` 目录。需求、规格、设计和任务清单都变成普通 Markdown 文件，可以 review、修改、提交，也可以让下一个 AI 会话继续读取。

## 核心流程

OpenSpec 默认工作流可以概括成五步：

1. Explore：先和 AI 一起把想法想清楚，不写代码，也不写文件
2. Propose：生成一个可审查的 change 目录
3. Review：人工检查 proposal、specs、tasks 是否合理
4. Apply：AI 按 `tasks.md` 一项项实现，并勾选进度
5. Archive：完成后把变更归档，并把规格合并到主规格里

官方 Quickstart 里把这个循环描述为：

```text
Explore -> Propose -> Review -> Apply -> Archive
```

这个顺序对我最大的提醒是：AI 编程不一定要从 “写代码” 开始。越是不确定的需求，越应该先停在 Explore 和 Propose 阶段。

## 文件结构

初始化之后，项目里会出现一个 `openspec/` 目录。一次变更大概长这样：

```text
openspec/
  changes/
    add-rate-limiting/
      proposal.md
      design.md
      tasks.md
      specs/
        api/
          spec.md
```

几个文件的职责：

- `proposal.md`：说明为什么需要这个变更，以及大致会改什么
- `specs/<capability>/spec.md`：描述行为层面的要求，也就是 “完成标准”
- `design.md`：记录实现方案、技术取舍和风险；简单改动可以不需要
- `tasks.md`：拆成可执行的任务清单，Apply 阶段主要按它推进

这里的重点是 `specs`。它不是普通的 PRD，而是更接近可验证的行为要求。比如 “未登录用户请求受限接口时返回 401” 就比 “完善登录校验” 更适合放进 spec。

## 安装和初始化

OpenSpec 是 Node.js CLI，官方文档要求 Node.js `20.19.0` 或更新版本。

常规安装：

```bash
npm install -g @fission-ai/openspec@latest
```

检查安装：

```bash
openspec --version
```

在项目里初始化：

```bash
cd your-project
openspec init
```

初始化时它会为支持的 AI 工具生成对应的 skills 或 commands。比如在支持 slash command 的工具里，可能会使用 `/opsx:propose` 这类命令；在支持 skills 的工具里，也可以通过 `openspec-propose` 这样的技能触发。

## 常用命令

一些需要记住的 CLI 命令：

```bash
openspec list
openspec list --specs
openspec show <change-or-spec>
openspec validate
openspec view
openspec archive <change-name> -y
```

我自己的理解：

- `list` 用来看当前有哪些未完成变更
- `show` 适合快速查看某个 change 或 spec
- `validate` 用来检查结构是否符合 OpenSpec 规则
- `archive` 是收尾动作，不只是移动文件，还会把变更规格合并回主规格

## 和 AI 对话时怎么用

如果需求还不清楚，可以先这样问：

```text
/opsx:explore 我想给这个项目增加限流，但还不确定应该按用户、IP 还是接口维度做
```

Explore 阶段的价值是让 AI 先读代码、问问题、列选项，而不是马上动手。

如果需求已经比较明确，可以直接 propose：

```text
/opsx:propose add rate limiting for public API
```

这一步会生成 change 目录。生成之后，真正应该认真看的不是 `tasks.md`，而是 `specs/`：

- 有没有漏掉异常场景
- 行为要求是否足够具体
- 是否把实现细节误写成了需求
- 有没有把一次变更做得太大

确认没问题之后再 apply：

```text
/opsx:apply add-rate-limiting
```

完成后归档：

```text
/opsx:archive add-rate-limiting
```

## 我觉得适合的场景

OpenSpec 更适合这些场景：

- 需求有一定复杂度，不适合直接一句话让 AI 改
- 需要多人 review AI 生成的计划
- 一个功能会影响多个模块
- 希望保留 “为什么这么改” 的上下文
- 项目长期维护，不能只靠临时聊天记录推进

不太适合的场景：

- 很小的 typo 或样式微调
- 明确的一行配置修改
- 一次性脚本或临时实验
- 需求还没准备进入工程实现，只是在随便想想

当然，最后一个也不绝对。OpenSpec 的 Explore 阶段其实就挺适合 “随便想想”，只是不一定要马上进入 Propose。

## 我会怎么用

如果在自己的项目里使用，我大概会遵循这个节奏：

1. 小改动直接做，不引入 OpenSpec
2. 中等以上改动先 Explore，把问题边界问清楚
3. Propose 之后先只 review `proposal.md` 和 `specs/`
4. `tasks.md` 不追求很长，只要能稳定推进即可
5. Apply 阶段每完成一块就跑对应测试
6. 合并前再 validate 和 archive

也可以在 `openspec/config.yaml` 里加项目级规则，比如：

```yaml
context: |
  所有规格和任务都使用中文。
  这是一个 Hugo 博客项目，避免修改无关配置。

rules:
  tasks:
    - 每个任务都应该能在一次会话中完成。
    - 涉及前端页面时，需要包含截图或浏览器验证。
```

这里要注意，`config.yaml` 不是项目 README。它应该只放会影响每次计划的规则，不要塞一堆 AI 自己能从代码里读出来的信息。

## 小结

OpenSpec 的思路可以浓缩成一句话：先把意图固定下来，再让 AI 写代码。

它并不是要把开发变成厚重流程，而是给 AI 编程补上一个轻量的 “规格层”。对个人项目来说，它能减少上下文漂移；对团队项目来说，它能把 AI 的计划变成可 review、可追踪、可归档的工程资产。

我现在的判断是：OpenSpec 不需要覆盖所有改动，但非常适合那些 “直接改会有点心虚” 的功能。只要心里出现这个信号，就应该先写 spec。

## 参考资料

- <https://openspec.dev/docs/quickstart>
- <https://openspec.dev/docs/installation>
- <https://openspec.dev/docs/cli>
- <https://openspec.dev/docs/schemas/spec-driven>
- <https://openspec.dev/docs/configuration>
- <https://github.com/Fission-AI/OpenSpec>
