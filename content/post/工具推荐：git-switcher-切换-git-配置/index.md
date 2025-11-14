---
title: '工具推荐s: git-switcher - 切换 git 配置'
description: '切换不同的 Git 配置'
slug: tips-git-switcher-git
date: 2024-01-06 09:54:08+0000
image: git-switcher.png
tags:
  - tools
  - git
weight: 1
---

## 为什么推荐这个工具？

我在公司使用自己的电脑，因此使用 git 提交代码的时候经常使用自己的个人的 Git 信息提交代码，我在想要是有个可以切换 Git 配置的工具好了，现在这个工具找到了。

[git-switcher](https://github.com/TheYkk/git-switcher) 这个工具很简单，就是帮助我们切换 git 的配置。

## 安装

```sh
brew install theykk/tap/git-switcher
```

## 使用

使用起来很简单：

```sh
# 切换
git-switcher

# 新建
git-switcher create

# 删除
git-switcher delete

# 重命名
git-switcher rename
```

## 配置

使用这个工具之后，它只是帮助我们修改 `user.name` 这个变量，但是我们提交代码的时候还有一个关联的变量 `user.email` 这个需要我们自己修改，这个需要注意。

不过我们也可以通过配置文件进行修改，配置文件在 `~/.config/gitconfigs`。
