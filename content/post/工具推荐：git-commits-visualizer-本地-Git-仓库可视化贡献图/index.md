---
title: '工具推荐: git-commits-visualizer -  本地 Git 仓库可视化贡献图'
description: 'git-commits-visualizer 可以帮助用户通过图形化查看仓库的贡献度。'
slug: git-commits-visualizer-git
date: 2023-07-28 02:25:18+0000
image: cover.jpg
tags:
    - tools
    - git
weight: 1
---


[git-commits-visualizer](https://github.com/abdullah-alaadine/git-commits-visualizer) 可以帮助用户通过图形化查看仓库的贡献度。

特点：

- 扫描本地仓库，并且生成一个贡献图
- 支持 Github 以及 Gitlab 服务
- 离线工作，哪怕链接不上远程服务不影响使用

# 安装

```sh
go install github.com/abdullah-alaadine/git-commits-visualizer@latest
```

> PS：`go install` 会把二进制安装到 `go env` 中 `GO_BIN` 指定的目录中。

## 使用

> git-commits-visualizer 支持两种显示模式：表和图。

以我自己的一个项目来看看，如下图：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230728_git-commits-visualizer.png)
