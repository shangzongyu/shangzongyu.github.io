# AI Agents Configuration

本项目的 AI 辅助配置，定义了各 AI Agent 的行为和职责边界。

## 项目概述

- **类型**: Hugo 个人博客
- **主题**: LoveIt v0.3.1（通过 Go Modules 引入，见 `go.mod`；项目 `layouts/` 下有兼容性覆盖模板）
- **内容语言**: 中文（zh-cn）
- **主分支**: `master`（注意不是 main）
- **部署**: GitHub Actions 自动部署到 `gh-pages` 分支
- **主要编辑器**:  Typora
- **图片托管**: GitHub (upgit/piclist)
- **代码规范**: pre-commit 集成 zhlint 检查中文 Markdown 格式

## 核心原则

1. **中文优先**: 所有文章和文档应使用中文
2. **Markdown 规范**: 遵循 Hugo 博客的 Markdown 格式
3. **简洁实用**: 内容应简洁、实用、有价值
4. **技术准确**: 技术性内容需要准确验证
5. **提交前检查**: 每次 git 提交文件之前，必须先运行 `zhlint` 检查中文 Markdown 格式，发现问题先修复再提交

## Agent 行为指南

### 写作和内容创建

- **语言**: 必须使用中文
- **格式**: 使用 Markdown，遵循 Hugo frontmatter 规范
- **结构**: 建议包含标题、摘要、正文
- **链接**: 使用相对路径，便于 GitHub Pages 部署
- **图片**: 使用 GitHub 作为图床，确保链接可访问
- **文章 URL**: permalink 格式为 `/p/:slug/`，slug 取自文件名

### 代码示例

- **语言**: 根据内容选择合适的编程语言
- **注释**: 代码应有必要的中文注释
- **可运行**: 提供的代码示例应可运行或有明确说明
- **格式化**: 遵循各语言的代码风格规范

### 技术验证

- **命令行示例**: 验证命令的正确性
- **配置文件**: 确保配置文件格式正确
- **安装步骤**: 验证安装步骤的可行性
- **依赖说明**: 明确说明依赖和版本要求

### 文档引用

- **官方文档**: 优先引用官方文档
- **时效性**: 引用最新的文档和版本
- **中文文档**: 优先使用中文文档，如无则使用英文文档
- **链接稳定性**: 确保引用的链接可访问

## 禁止行为

- ❌ 不要生成英文内容（除非是代码或命令）
- ❌ 不要创建不必要的文件
- ❌ 不要修改配置文件（除非明确要求）
- ❌ 不要创建 PR 或提交代码（除非明确要求）
- ❌ 不要运行构建或部署命令（除非明确要求）

## 文件组织

### 文章位置

- 博客文章: `content/posts/`
- 页面: `content/page/`（links）
- 分类: `content/categories/`
- 配置: `config/_default/`
- CI 流水线: `.github/workflows/`
- 主题配置: `config/_default/module.toml`（Go Modules 引入）

### 命名规范

- 文章: `YYYY-类别_标题.md`，如 `2024-工具推荐_markitdown-转换文件为-Markdown.md`
- 类别示例: `工具推荐`、`Tips`、`我使用的工具` 等
- 使用连字符 `-` 或下划线 `_` 分隔
- 避免使用特殊字符

### 新建文章

优先使用 Hugo archetype 模板（`archetypes/post.md`）生成初始 frontmatter，默认包含：

```yaml
---
title: "文章标题"
date: {{ .Date }}
draft: true
categories: ["未分类"]
tags: []
weight: 1
---
```

发布前需将 `draft` 改为 `false`，并把 `categories` 从「未分类」改为实际分类。

## 常用命令

### 本地开发

```bash
# 启动本地服务器（含草稿，start.sh 等价于此命令）
hugo server -D -E -F

# 构建静态网站
hugo

# 仅本地构建预览，不负责部署
./start.sh
```

### 提交检查

每次 git 提交文件之前，必须先运行 zhlint 检查中文 Markdown 格式：

```bash
# 检查所有 Markdown 文件
zhlint "content/**/*.md"

# 发现问题时自动修复
zhlint "content/**/*.md" --fix
```

zhlint 会检查全角/半角标点、中英文之间空格等规范，发现问题先修复再提交。另外，pre-commit 钩子也会在提交时自动运行 zhlint 作为兜底。

### 部署

- 推送 `master` 分支后，GitHub Actions 自动构建并部署到 `gh-pages` 分支
- 无需本地执行部署命令

### 内容管理

- 在 `content/posts/` 下创建新文章
- 使用 Obsidian 或 Typora 编辑
- Obsidian 配置位于 `content/posts/.obsidian/`，已加入 .gitignore 不入库

## 与 AI 交互

### 提问方式

- 清晰描述需求
- 指明文件位置（如有）
- 说明期望的输出格式
- 提供上下文（如相关文章或主题）

### 期望输出

- 中文内容
- Markdown 格式
- 代码高亮
- 必要的说明和注释

---

**最后更新**: 2025-08-06
