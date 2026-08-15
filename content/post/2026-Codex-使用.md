---
title: "Codex 使用"
date: 2026-01-01T00:00:00+08:00
draft: true
categories: ["未分类"]
tags: []
weight: 1
---

2026-Codex 使用

## oh-my-codex（OMX）

不跟 Codex 抢饭碗，而是在 Codex 之上补齐一整套标准化流程 + 技能系统：把 AI 编程从 “会写代码” 推进到 “能交付结果”，从需求澄清一路顺滑到落地。

它的主线流程很清晰：

1. `$deep-interview`：需求一团雾？先做深度访谈，把边界、目标、约束问透
2. `$ralplan`：把确认后的需求翻译成可执行的架构与实现计划
3. `$ralph` / `$team`：
   - 选 `ralph`：一个持久化 agent 循环推进，直到完成交付
   - 选 `team`：多个 agent 并行协作，把活拆开一起干

底层做的关键增强也很实用：

- 常用角色封装成可复用关键词，少配配置，多干活
- 内置标准技能库 (`deep-interview / ralplan / team / ralph` 等)，开箱即用
- 用 `.omx/` 持久化计划、日志、记忆与运行状态，上下文不再动不动丢失
- 支持用 `AGENTS.md` 给项目 “划范围、立规矩”，避免越界发挥
- 集成 `tmux` 做持久化运行时，多 agent 协作更稳、更可控

团队模式尤其值得玩：

- `omx team 3:executor "修复失败的测试并验证"`
- `omx team status <team-name>`
- `omx team resume <team-name>`

支持同时启动多个 executor 并行干活，进度状态随时可查；会话可恢复，任务不断档。

更多实用工具一并带上：
- omx explore：只读检索代码库，可注入 wiki 上下文优先搜索
- omx sparkshell：原生 shell 的检查与有界验证
- omx wiki：本地 markdown 知识库，主打搜索优先而非向量检索
- omx doctor：安装/运行异常的诊断工具

安装也很省事：
npm install -g @openai/codex oh-my-codex
omx setup
omx --madmax --high

GitHub：https://github.com/Yeachan-Heo/oh-my-codex

官网：https://yeachan-heo.github.io/oh-my-codex-website/

推荐组合：macOS/Linux + Codex CLI (Windows 原生支持仍在完善中)。适合已经在用 Codex、想把工作流做得更系统，并把运行时状态管理做扎实的开发者。

## RKT

rtk (Rust Token Killer) 专门帮开发者省 token。

<https://github.com/rtk-ai/rtk>

当你用 Claude Code、Codex、Cursor 等 AI 编码工具时，这些工具经常要执行 `git status`、`cargo test`、`npm install`、`docker ps` 等命令，结果输出一大堆废话 (重复行、日志、进度条、路径等)，全塞进 AI 的上下文窗口里，白白浪费 token。

rtk 就干这件事：

- 自动拦截这些命令
- 智能过滤、压缩、去重、截断输出
- 只把 “关键信息” 传给 AI，既节省了 token，又提升了效果

它支持 100+ 常见开发者命令 (git、cargo、npm、docker、aws 等)，还有专门针对测试框架、linter、包管理器、云工具的优化。

单文件 Rust 二进制，无任何依赖，体积小、速度快 (<10ms 开销)

## Claude Codex 的插件
