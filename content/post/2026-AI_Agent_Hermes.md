---
title: "工具推荐：Hermes Agent - 自我进化的 AI 代理"
description: 持久记忆、自主学习的 AI 代理框架
date: 2026-04-18T21:35:45+08:00
image:
math:
license:
hidden: false
comments: true
categories: ["工具推荐"]
tags: ["AI", "AI代理", "开源"]
weight: 1
---

## 什么是 Hermes Agent？

Hermes Agent 是一个由 Nous Research 构建的自我改进 AI 代理，是唯一具有内置学习循环的代理。它能够：

- 从经验中创建技能
- 在使用过程中改进技能
- 促使自己持久化知识
- 搜索自己的过去对话
- 构建跨会话不断深化的用户模型

### 核心特点

#### 学习循环

- **代理管理的记忆**：周期性推动
- **自主技能创建**：复杂任务后创建技能
- **技能自我改进**：使用中学习
- **FTS5 会话搜索**：跨会话回溯
- **Honcho 方言学**：用户建模

#### 多平台支持

- **终端界面**：完整的 TUI
- **消息平台**：Telegram、Discord、Slack、WhatsApp、Signal 等
- **本地运行**：可在 $5 VPS、GPU 集群运行
- **Serverless**：支持 Daytona、Modal 等无服务器平台

#### 模型提供商

- **Nous Portal**：官方模型
- **OpenRouter**：200+ 模型支持
- **NVIDIA NIM**：Nemotron 模型
- **小米 MiMo**：kimi 系列
- **z.ai/GLM**：智谱 AI
- **Kimi/Moonshot**：月之暗面
- **MiniMax**：多模态模型
- **Hugging Face**：开源模型
- **OpenAI**：GPT 系列
- **自定义端点**：支持任何 OpenAI 兼容端点

## 安装

### 快速安装

```bash
# 一行安装
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 手动安装

```bash
# 克隆仓库
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# 安装依赖
pip install -r requirements.txt
```

## 配置

### 基本设置

```bash
# 运行设置向导
hermes setup

# 或手动配置
hermes config set anthropic.api_key YOUR_KEY
hermes config set openai.api_key YOUR_KEY
```

### 模型选择

```bash
# 列出可用模型
hermes models

# 选择模型
hermes model claude-opus-4-20250514
```

## 使用

### CLI 交互

```bash
# 启动交互式终端
hermes

# 开始对话，享受完整的 TUI 体验
```

### 消息网关

```bash
# 启动消息网关
hermes gateway

# 现在可以从 Telegram、Discord 等平台与 Hermes 对话
```

### 批量处理

```bash
# 批量运行任务
hermes batch --input tasks.json

# 轨迹生成（用于 RL 训练）
hermes trajectory --config config.yaml
```

## 高级功能

### 技能系统

#### 内置技能

- **代码生成**：自动编程任务
- **文档编写**：技术文档生成
- **调试助手**：问题诊断和解决
- **测试生成**：自动化测试用例

#### 自定义技能

```bash
# 创建新技能
hermes skill create my-skill

# 安装社区技能
hermes skill install agentskills.io/skill-name
```

### 定时任务

```bash
# 添加定时任务
hermes cron add --schedule "0 9 * * *" --command "run daily report"

# 列出任务
hermes cron list
```

### 记忆系统

#### 三层记忆架构

- **身份记忆**：代理是谁
- **结构记忆**：主题组织的知识
- **程序记忆**：具体执行细节

#### 记忆管理

```bash
# 查看记忆
hermes memory show

# 编辑记忆
hermes memory edit

# 导出记忆
hermes memory export --format json
```

### 工具调用

```bash
# 查看可用工具
hermes tools list

# 配置工具
hermes tool enable web-search
hermes tool enable browser-automation
```

## 研究就绪功能

### 批量轨迹生成

```bash
# 生成训练数据
hermes batch --output trajectories/

# 压缩轨迹
hermes compress --input trajectories/ --output compressed/
```

### RL 环境

- **Atropos**：强化学习环境
- **轨迹导出**：标准格式
- **评估指标**：自动化性能评估

## 系统架构

### 后端支持

- **本地**：直接在本地运行
- **Docker**：容器化部署
- **SSH**：远程服务器
- **Daytona**：无服务器平台
- **Singularity**：HPC 环境
- **Modal**：Serverless 计算

### 消息平台

- **Telegram**：完整的交互支持
- **Discord**：服务器集成
- **Slack**：工作流集成
- **WhatsApp**：移动支持
- **Signal**：隐私优先
- **Email**：异步交互
- **CLI**：终端界面

## 使用场景

### 个人助手

```bash
# 作为个人 AI 助手
hermes --profile personal

# 自动学习你的偏好和习惯
```

### 开发代理

```bash
# 为特定项目配置
hermes --project my-project

# 自动学习项目上下文
```

### 研究工具

```bash
# 研究模式
hermes --mode research

# 自动收集和分析数据
```

### 自动化工作流

```bash
# 设置自动化任务
hermes cron add --script backup-daily.sh

# 无需人工干预执行
```

## 配置文件

### 主配置

```yaml
# ~/.hermes/config.yaml
providers:
  anthropic:
    api_key: ${ANTHROPIC_API_KEY}
  openai:
    api_key: ${OPENAI_API_KEY}

model:
  default: claude-opus-4-20250514

memory:
  enabled: true
  compression: true

skills:
  auto_install: true
  self_improve: true
```

### 项目配置

```yaml
# .hermes/project.yaml
project:
  name: "My Project"
  description: "Project description"

context_files:
  - README.md
  - ARCHITECTURE.md
  - docs/api.md

tools:
  - web-search
  - code-analysis
  - git-operations
```

## 故障排除

### 常见问题

```bash
# 诊断问题
hermes doctor

# 检查配置
hermes config validate

# 清除缓存
hermes cache clear
```

### 日志调试

```bash
# 启用调试模式
hermes --log-level debug

# 查看日志
hermes logs --tail 100
```

## 性能优化

### 记忆优化

```bash
# 压缩记忆
hermes memory compress

# 清除旧记忆
hermes memory prune --days 30
```

### 缓存管理

```bash
# 查看缓存大小
和其他cache stats

# 清除缓存
hermes cache clear
```

## 社区和资源

- **官方网站**：[https://hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com)
- **文档**：[https://hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)
- **GitHub**：[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Discord 社区**：实时讨论和支持
- **更新日志**：[https://hermes-agent.nousresearch.com/changelog](https://hermes-agent.nousresearch.com/changelog)

## 与其他代理的比较

| 特性 | Hermes | AutoGPT | CrewAI | Letta |
| ---- | ------ | ------- | ------ | ------ |
| 学习循环 | ✅ 内置 | ❌ | ❌ | 部分 |
| 持久记忆 | ✅ 三层架构 | 会话内 | 会话内 | 分页 |
| 生命周期管理 | ✅ Cron 驱动 | 手动 | 手动 | 部分 |
| 自我改进 | ✅ 主动 | ❌ | ❌ | ❌ |
| 研究就绪 | ✅ 完整 | 部分 | ❌ | ❌ |
| 多平台 | ✅ 15+ | CLI | CLI | CLI |

## 最佳实践

### 初次使用

1. **安装配置**：运行 `hermes setup`
2. **选择模型**：选择适合的模型提供商
3. **开始对话**：从简单任务开始
4. **观察学习**：让代理学习你的需求

### 团队使用

1. **共享配置**：版本控制配置文件
2. **标准化技能**：创建团队共享技能
3. **记忆管理**：定期清理和优化
4. **监控性能**：跟踪代理效率

### 研究项目

1. **轨迹收集**：使用 `hermes batch`
2. **数据压缩**：优化存储和传输
3. **环境训练**：使用 Atropos 框架
4. **评估迭代**：持续改进性能

---

Hermes Agent 是一个革命性的 AI 代理系统，它不仅仅回答问题，而是在使用中不断学习和进化。无论是个人使用、团队协作还是研究项目，Hermes 都能提供持续增值的 AI 体验。
