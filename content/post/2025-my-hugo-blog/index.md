---
title: "My Hugo Blog"
description:
date: 2025-11-11T18:23:41+08:00
image:
math:
license:
hidden: false
comments: true
draft: true
---

## 写作工作

- Typora
- MiaoYan
-  Obsidian

## 工具

每次提交的时候需要执行 `zhlint` 格式化。

使用 `pre-commit` 作为钩子工具。

```sh
pip install pre-commit
```

另一个常用且更灵活的方法是使用 pre-commit 这个第三方工具管理钩子：

安装 pre-commit (Python 工具)，pip install pre-commit。

在项目根目录创建。pre-commit-config.yaml，配置类似如下：

```yaml
repos:
  - repo: local
    hooks:
      - id: zhlint-fix
        name: Fix markdown with zhlint
        entry: zhlint --fix
        language: system
        types: [markdown]
```

运行 pre-commit install 安装钩子到。git/hooks/pre-commit。

当执行 git commit 时，zhlint --fix 会自动运行在所有被提交的 Markdown 文件上。

这种方式配置简单且易于维护，也支持多个钩子、条件控制等。

总结来说，最推荐使用 pre-commit 工具来管理执行命令脚本，若不需额外依赖也可通过。git/hooks/pre-commit 脚本自定义实现。脚本逻辑中需要获取所有待提交的 Markdown 文件，运行 zhlint --fix 命令，再将修复后的文件重新添加到缓存区以保证提交的是修复后的内容。
