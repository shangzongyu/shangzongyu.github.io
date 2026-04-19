---
title: "工具推荐：Gitea - 自托管 Git 平台"
description: 轻量级、功能完善的自托管 Git 平台
date: 2026-04-18T21:10:14+08:00
image:
math:
license:
hidden: false
comments: true
categories: ["工具推荐"]
tags: ["Git", "自托管", "开源"]
weight: 1
---

Gitea 是一个轻量级、功能完善的自托管 Git 平台，提供与 GitHub 类似的用户体验。

## 什么是 Gitea？

Gitea 是一个用 Go 语言编写的社区托管的轻量级 Git 服务，旨在提供最简单、最快、最无痛的自托管 Git 服务方式。它支持在 Go 支持的所有平台上独立运行，包括 Linux、macOS 和 Windows。

### 主要特点

- **轻量高效**：可在 Raspberry Pi 等低配置硬件上运行
- **功能全面**：提供完整的 Git 托管功能
- **开源免费**：MIT 许可证
- **易于部署**：单一二进制文件或 Docker 容器
- **低资源消耗**：约 80MB RAM 即可运行

## 核心功能

### 代码托管

- 创建和管理仓库
- 代码浏览和提交历史
- 代码审查和合并请求
- 分支和标签管理
- 协作者管理

### CI/CD - Gitea Actions

- GitHub Actions 兼容的工作流
- YAML 格式配置
- 自托管 Runner
- 支持多种触发器

### Issue 和项目管理

- Issue 跟踪
- 项目看板（Kanban）
- 里程碑和时间线
- 标签和分类

### 包注册表

支持 20+ 种软件包管理：

- Container (Docker)
- npm
- Maven
- NuGet
- PyPI
- RubyGems
- Cargo
- Helm
- Composer
- Conan

### Wiki 和文档

- Markdown 支持
- 版本控制
- 协作编辑

## 系统要求

### 最低配置

- **CPU**：1 核心
- **内存**：256MB（推荐 512MB）
- **存储**：根据仓库大小
- **操作系统**：Linux、macOS、Windows

### 推荐配置

- **CPU**：2+ 核心
- **内存**：1GB+
- **存储**：SSD 推荐

## 安装方式

### Docker（推荐）

```yaml
version: "3"

services:
  server:
    image: gitea/gitea:latest
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    volumes:
      - ./data:/data
    ports:
      - "3000:3000"
      - "222:22"
```

### 二进制安装

从 [GitHub Releases](https://github.com/go-gitea/gitea/releases) 下载对应平台的二进制文件。

### Homebrew

```bash
brew install gitea
```

## Gitea 生态系统

### 第三方集成

- **Awesome Gitea**：社区贡献的集成和工具列表
- **Gitea Actions Runner**：自托管 CI/CD
- **迁移工具**：从 GitHub、GitLab、Bitbucket 导入

### 社区插件

- Webhook 集成
- OAuth 提供商
- 存储后端
- 主题定制

## 与其他平台比较

| 特性 | Gitea | GitLab CE | Forgejo | GitHub |
| ------ | ------- | ---------- | ------- | ------ |
| 资源消耗 | ~80MB RAM | 4GB+ RAM | ~80MB RAM | SaaS |
| CI/CD | Actions | 内置 | Actions | 内置 |
| 包注册表 | 20+ 类型 | 内置 | 20+ 类型 | 内置 |
| 开源 | ✅ MIT | ✅ MIT | ✅ GPL | ❌ |
| 部署难度 | 简单 | 复杂 | 简单 | N/A |
| 社区治理 | 商业化 | 企业化 | 社区驱动 | 商业化 |

### Gitea vs GitHub

**Gitea 优势：**
- 完全掌控数据
- 无成本限制
- 隐私可控
- 离线可用
- 自定义扩展

**GitHub 优势：**
- 无需维护
- 大社区
- 丰富集成
- 专业托管

### Gitea vs GitLab

**Gitea 优势：**
- 资源占用极低
- 部署简单
- 学习曲线平缓

**GitLab 优势：**
- 功能更全面
- 企业级功能
- 内置安全扫描
- 成熟的生态系统

## 使用场景

### 个人开发者

- 个人项目托管
- 作品集展示
- 学习 Git 操作
- 轻量级 CI/CD

### 小团队

- 团队协作
- 代码审查
- 项目管理
- 内网部署

### 企业环境

- 内网代码托管
- 合规性要求
- 数据主权
- 成本控制

## 迁移

### 从 GitHub 迁移

Gitea 提供从 GitHub 迁移的工具：

1. 在 Gitea 中创建组织
2. 使用迁移功能导入仓库
3. 迁移 Issues、Pull Requests、Wiki
4. 更新远程 URL

### 从 GitLab 迁移

类似 GitHub 迁移，Gitea 支持 GitLab 格式的导入。

## 安全特性

- **双因素认证**：支持 TOTP 和 U2F
- **LDAP/OAuth**：企业身份集成
- **权限控制**：细粒度的访问控制
- **审计日志**：操作记录和追踪
- **内容过滤**：垃圾内容和恶意代码检测

## 常见问题

### Gitea 适合谁？

- 需要自托管 Git 服务的小到中型团队
- 资源受限的环境
- 需要数据主权的企业
- 想学习 Git 托管的个人开发者

### Gitea 和 Forgejo 如何选择？

- **Gitea**：已有部署，需要稳定支持
- **Forgejo**：新部署，偏好社区治理

### 如何升级 Gitea？

使用 Docker 可以轻松升级，只需拉取新镜像并重启容器。

## 资源

- **官方网站**：[https://gitea.io](https://gitea.io)
- **文档**：[https://docs.gitea.io](https://docs.gitea.io)
- **GitHub**：[https://github.com/go-gitea/gitea](https://github.com/go-gitea/gitea)

---

Gitea 是自托管 Git 平台的优秀选择，特别适合需要轻量级、功能完善的 Git 托管解决方案的用户。
