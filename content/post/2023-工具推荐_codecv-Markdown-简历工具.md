---
title: "工具推荐: codecv - Markdown 简历工具"
description: ''
slug: codecv-markdown
date: 2023-07-28 03:00:09+0000
image:
tags:
  - markdown
  - resume
weight: 1
---

## 介绍

自己很喜欢 Markdown 这个文本格式，因此写简历的时候就想到 Markdown 了，自己就去找符合自己需求的工具，当然最后还是需要把 Markdown 转换为 PDF，因为使用的时候需要打印出来。

自己需求为：

1. 支持 Markdown
2. 可以自己搭建
3. 可以导出 PDF

最后找到符合自己的工具 [codecv](https://github.com/acmenlei/markdown-resume-to-pdf)，这个工具有一个在线的版本，用户可以在本地自己搭建。

这个工具有很多模板，可以自己选择。

## 前置条件

```sh
# 安装 node，node 的版本需要 `^16 || ^18 || ^19`
$ brew install node

$ node --version
v20.5.0
```

## 使用

```sh
# Clone 项目
git clone https://github.com/acmenlei/markdown-resume-to-pdf.git

# 进去 markdown-resume-to-pdf
cd  markdown-resume-to-pdf

# 安装依赖
npm install

# 运行
npm run dev
```

运行后，可以在 <http://localhost:5173/> 写自己的简历。

## 写在最后

这个工具支持的模板有些少，还有就是有些自己定义的语言，这样写的东西就不能直接迁移到其他的工具中。
