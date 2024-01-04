---
title: "使用 Hugo 搭建自己的 Blog"
date: 2024-01-04T20:22:19+08:00
draft: true
---

## 安装

以 macOS 为例进行实例。

```sh
# install
brew install hugo

# 测试安装
hugo version
```

新建一个网站：

```sh
hugo new site my_website
```

## 主题

下载主题：

```sh
cd my_website
git clone https://github.com/dillonzq/LoveIt.git themes/LoveIt
```

把主题作为子模块：

```sh
git submodule add https://github.com/dillonzq/LoveIt.git themes/LoveIt
```

更新主题：

```sh
git submodule update --rebase --remote
```

## 简单使用

```sh
hugo new posts/first_post.md
```

> 运行 hugo serve 时, 当文件内容更改时, 页面会随着更改自动刷新.

```sh
hugo -D
```

这会生成一个 public 目录, 其中包含你网站的所有静态内容和资源. 现在可以将其部署在任何 Web 服务器上。

确认无误后就要把它发到公网上了，这里采用 GitHub pages 进行部署（当然，也有很多种方法也能达成这一目的）

## Github Pages 部署

```sh
cd public
git init
git remote add origin https://github.com/yourname/yourname.github.io.git

# 此URL可在你的 repo 中找到
git add .
git commit -m "update %date%,%time%"
git push origin master
```

## Github Actions 实现自动化部署

```sh
# 使用脚本进行部署
#!/usr/bin/env bash

hugo -D
cd public
git add .
git commit -m "update %date%,%time%"
git push origin master
```

使用 Github Action

在 repo 目录下新建 `.github/workflow` 目录，在 `workflow` 下以 yml 形式配置 Github Action。

配置 GitHub Actions

在 GitHub 打开源码仓库，点击 Actions → New workflow 中选择 -> Pages -> Hugo 作为基础实用的版本，并且提交。

修改：

- external_repository：设置成页面仓库 username.github.io 的地址。
- publish_branch：设置成页面仓库的主分支，比如 master 或者 main。
- cname：设置成网站的域名。如果使用 .github.io 域名就不需要这一行。

## 参考

<https://gohugo.io/hosting-and-deployment/hosting-on-github/>
