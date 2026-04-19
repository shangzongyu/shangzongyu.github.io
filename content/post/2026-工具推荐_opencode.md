---
title: "工具推荐：OpenCode 及 Oh My OpenCode 插件"
description: OpenCode 编码助手及其强大的插件系统
date: 2026-04-18T21:10:59+08:00
image:
math:
license:
hidden: false
comments: true
categories: ["工具推荐"]
tags: ["AI工具", "编码助手", "开源"]
weight: 1
---

## OpenCode

OpenCode 是一个强大的 AI 编码助手 CLI 工具，提供智能代码补全、分析和优化功能。

## Oh My OpenCode (Omo) - OpenCode 的全能插件

Oh My OpenCode (也称为 Omo) 是 OpenCode 的最强大插件，为 OpenCode 增加了丰富的功能，包括多个 AI 提供商、专业子代理、MCP 集成等。

### 主要特性

#### 多 AI 提供商支持

- **Anthropic**：Claude 系列模型
- **OpenAI**：GPT 系列模型
- **本地模型**：Ollama、LM Studio 等
- **其他**：支持自定义 OpenAI 兼容端点
- **轻松切换**：无需修改代码即可切换提供商

#### 专业子代理系统

- **Oracle**：问答和解释代理
- **Explore**：代码导航和发现代理
- **Librarian**：文档和代码探索代理
- **Sisyphus**：默认规划和执行代理

#### MCP 集成

- **grep.app**：超快速代码搜索（默认启用）
- **Context7**：最新的文档查询（默认启用）
- **其他 MCP**：支持所有 MCP 兼容服务器

#### LSP 支持

完整的语言服务器协议支持，包括：
- 代码补全和导航
- 重构工具（重命名、代码操作）
- 代码分析和类型检查

#### 工作流自动化

- **20+ 内置 Hook**：目录注入、README 注入、规则注入等
- **自定义工作流**：可配置自动执行的命令和操作
- **输出管理**：grep 输出截断、工具输出处理

### 安装

#### 使用包管理器

```bash
# 使用 bun
bunx oh-my-opencode install

# 或者使用 npm
npm install -g oh-my-opencode
```

#### 手动安装

```bash
curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md | bash
```

### 配置

#### 基本配置

创建 `~/.config/opencode/oh-my-opencode.json`：

```json
{
  "agents": {
    "sisyphus": {
      "model": "claude-opus-4-6"
    },
    "explore": {
      "model": "github-copilot/grok-code-fast-1"
    }
  },
  "categories": {
    "quick": {
      "model": "opencode/gpt-5-nano"
    }
  }
}
```

#### 提供商别名

支持模型别名，方便切换：

```json
{
  "model_aliases": {
    "claude": "anthropic|github-copilot",
    "gpt4": "openai|github-copilot",
    "kimi": "kimi-for-coding/k2p5"
  }
}
```

### 使用技巧

#### 快速开始

```bash
# 安装完成后直接使用
ultrawork  # 开始工作
```

#### 检查配置

```bash
bunx oh-my-opencode doctor  # 诊断配置问题
opencode models  # 列出可用模型
```

#### 管理代理

```bash
# 查看已配置的代理
oh-my-opencode list agents

# 测试特定代理
oh-my-opencode test oracle
```

### 开发者功能

#### Hook 系统

创建自定义 Hook 来自动化工作流：

```json
{
  "hooks": {
    "pre-write": [
      "custom-hook-command"
    ]
  }
}
```

#### 自定义 MCP

添加自定义 MCP 服务器：

```json
{
  "mcps": {
    "my-custom-mcp": {
      "command": "my-mcp-server",
      "args": ["--port", "8080"]
    }
  }
}
```

### GitHub

- **仓库**：[https://github.com/code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)
- **Star 数**：52k+
- **许可**：MIT License
- **更新频率**：频繁更新（最新版本 v3.17.4）

### 重要说明

⚠️ **安全警告**：
- 不要使用第三方站点下载安装包
- 只使用官方 GitHub releases
- 验证下载文件的完整性

✅ **官方来源**：
- GitHub Releases：https://github.com/code-yeongyu/oh-my-openagent/releases
- 官方文档：https://ohmyopencode.com/

## OpenCode CLI 命令参考

### 常用命令

```bash
opencode              # 启动交互式会话
opencode models        # 列出可用模型
opencode providers     # 列出可用的提供商
opencode config         # 显示配置
opencode doctor        # 诊断问题
```

### 项目级配置

在项目目录创建 `.opencode/oh-my-opencode.json`：

```json
{
  "model": "claude-opus-4-6",
  "context_files": [
    "README.md",
    "ARCHITECTURE.md"
  ]
}
```

## 社区和资源

- **文档**：[https://ohmyopencode.com/documentation](https://ohmyopencode.com/documentation)
- **GitHub Discussions**：报告问题和讨论
- **贡献指南**：欢迎社区贡献

## 使用场景

### 个人开发

- 日常编码辅助
- 代码审查和优化
- 学习新技术栈
- 快速原型开发

### 团队协作

- 统一的代理配置
- 共享最佳实践
- 团队知识库
- 代码质量保证

### 研究和学习

- 探索代码库
- 理解复杂系统
- 生成文档
- 实验新想法

---

Oh My OpenCode 将 OpenCode 提升到了一个全新的水平，提供了专业级 AI 编码助手的能力。无论你是个人开发者还是团队成员，这个插件都能显著提高你的编程效率。
