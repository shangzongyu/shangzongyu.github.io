---
title: '拥抱 Conventional Commits：让你的代码提交信息更有价值'
description: '写更有价值的 Git Commit 信息'
slug: conventional-commits
date: 2025-09-13 07:31:11+0000
tags:
    - git-tips
weight: 1
---

在日常的编码过程中，版本控制软件是我们不可或缺的伙伴。每一次的代码提交，都像是为项目留下一个重要的 “时间戳”，记录着我们在上线或其他关键操作时所做的修改。然而，当项目团队不断壮大，或者项目本身变得日益庞大复杂时，随意编写的 Commit 信息，哪怕在自己看来清晰明了，也可能给团队协作带来不便。

为了解决这一痛点，我接触到了一个非常有价值的规范——**Conventional Commits (约定式提交)**。它提供了一套清晰、简洁的指引，旨在将每一次提交转化为有意义、结构化的信息单元，从而显著提升 Commit Log 的价值和可利用性。

## Conventional Commits 规范详解

Conventional Commits 规范为每次提交定义了如下的标准结构：

```sh
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

这个结构包含了几个关键要素：

- `Type` (类型)**：**必须遵循的指引**，表明提交的性质。规范定义了以下基础类型：
	- `fix`：修复 Bug (对应 SemVer 的 PATCH 版本更新)。
    - `feat`：引入新功能 (对应 SemVer 的 MINOR 版本更新)。
    - **鼓励扩展**：团队可以根据需要定义其他类型，如 `build`、`chore` (用于标记常规维护工作，如更新依赖项)、`ci`、`docs`、`style`、`refactor`、`perf`、`test` 等，以适应具体的工作流。这些扩展类型本身通常不直接影响版本号 (除非包含破坏性变更)。
- `Scope` (范围)：**可选但推荐的指引**，用于明确提交影响的代码区域或模块，用括号包裹，如 `feat(api):` 或 `fix(tools):`。这极大地增强了信息的可定位性。
- `Description` (描述)：**必须遵循的指引**，紧跟在冒号和空格之后，用简洁的语言 (推荐使用祈使句的现在时态) 概括本次提交的核心变更内容。这是提交信息的 “标题”。
- `Body` (正文)：**可选指引**，当简短描述不足以说明时，提供更详细的上下文、动机和实现细节。与 Description 之间需要空一行。
- `Footer(s)` (脚注)：**可选指引**，提供元数据，如关联的 `Issue` (例如 `Refs: #123`)。特别重要的两个脚注指引：
  - `BREAKING CHANGE`：明确标示**不兼容的 API 变更** (对应 SemVer 的 MAJOR 版本更新)。
  - `INITIAL STABLE RELEASE`：标记项目从 `0.y.z` 版本进入 `1.0.0` 稳定版。

> **强调重要变更的简化指引：**规范还提供了 `!` (紧跟 type 或 scope 之后) 和 `!!` 作为标记 `BREAKING CHANGE` 和 `INITIAL STABLE RELEASE` 的快捷方式，进一步简化了实践。

## 示例展示

以下是一些遵循 Conventional Commits 规范的提交示例：

- **修复简单的 BUG**：

    ```
    fix: correct username validation logic
    ```

- **带有范围的新功能**：

    ```
    feat(api): add user profile endpoint
    ```

- **使用 `!` 标记破坏性变更**：

    ```
    refactor!(auth): remove deprecated JWT authentication
    ```

- **包含详细正文和脚注的提交**：

    ```
    perf(api): improve user query performance significantly

    Implemented a new indexing strategy for the users table and optimized
    the SQL query execution plan. Initial tests show a 50% reduction
    in average query latency under heavy load.

    Reviewed-by: Alice <alice@example.com>
    Refs: #456, #478
    ```

- **使用 `!!` 标记首次稳定版发布**：

    ```
    chore(release)!!: prepare for 1.0.0 stable release
    
    Finalized documentation, updated dependencies, and ran comprehensive
    end-to-end tests to ensure stability for the first major release.
    
    BREAKING CHANGE: The project is now considered stable for production use.
    ```

通过遵循上述规范，你的 Commit 信息将转化为清晰、信息丰富的记录。

## 遵循 Conventional Commits 的收益

采纳 Conventional Commits 规范，对日常开发和团队协作能带来诸多好处：

- **提升可读性与理解性**：`Type` 和 `Scope` 能够让你快速筛选和定位信息，清晰的 `Description` 和 `Body` 阐述了变更的 “什么” 和 “为什么”。
- **增强团队沟通与协作**：统一的格式减少了误解，提高了代码审查和协作效率，让每一次提交都成为清晰的沟通。
- **简化历史追溯与问题排查**：结构化的日志便于查找特定功能引入、Bug 修复或破坏性变更的源头。
- **驱动自动化流程**：有意义的提交日志是自动化工具的理想输入，能够驱动自动化生成 `CHANGELOG`、自动判断 SemVer 版本，以及基于提交类型触发不同的 CI/CD 流程。

## Conventional Commits 的最佳实践与洞察

- **原子化提交**：鼓励将复杂的变更分解为多个逻辑上独立的、遵循单一 `type` 的提交。这是良好的 Git 实践，Conventional Commits 进一步强化了这一点。
- **选择最合适的 `Type`**：当一次提交包含多种类型的变更时 (应尽量避免)，选择最能代表其核心意图的 `type`，并在 `Body` 中详述其他变更。
- **使用祈使句现在时**：推荐使用如 “Add feature”、“Fix bug” 的风格撰写 `Description`，简洁、直接，如同给代码库下达指令。
- **善用工具辅助**：社区提供了丰富的工具 (如 [Commitizen](https://commitizen-tools.github.io/commitizen/)，[commitlint](https://commitlint.js.org/) 等) 来帮助开发者遵循规范格式，并在提交前进行校验，降低遵循规范的门槛。
- **团队共识与逐步采纳**：引入规范需要团队达成共识。可以通过分享、讨论和使用工具逐步推广。

## 强大的工具支持

有了 Conventional Commits 规范，以下工具可以极大地提升开发效率：

- **Commitizen**：一款交互式命令行工具，引导用户创建符合规范的提交信息。
- **Commitlint**：用于校验提交信息是否符合规范，通常与 Git Hooks (如 husky) 集成。
- **IDE 插件**：主流 IDE (如 VS Code，JetBrains IDEs 等) 均有插件提供模板、补全和校验支持。
- **自动化版本与 Changelog 工具**：如 [semantic-release](https://github.com/semantic-release/semantic-release)，[goreleaser/chglog](https://github.com/goreleaser/chglog) 等，它们能够消费符合规范的提交历史，实现自动化版本发布和 Changelog 生成。

> **AI 赋能 Commit 信息生成**：近年来，AI 的飞速发展也为 Commit 信息生成带来了新的可能。不少编辑器和工具已经集成了 AI 功能，能够根据你的代码修改生成建议的 Commit 信息，这在我的使用体验中也相当不错。

## 参考资料

- [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/#specification)

## 补充说明

上面的文章是我写的之后，AI 帮助我进行了润色。
