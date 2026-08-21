---
title: "Markdown 语法与工具"
description: 介绍学习 Markdown 的原因以及 macOS 平台下的 Markdown 写作工具
slug: markdown-macos-writing-tools
date: 2026-04-18T00:00:00+08:00
draft: true
tags:
  - Markdown
  - 写作工具
  - macOS
categories:
  - 工具推荐
weight: 1
---

介绍下为什么要学习 Markdown，以及 MacOS 写 Markdown 的工具。

<!--more-->

<https://x.com/PandaTalk8/status/2036277542802629107>

## Markdown 基本语法

- <https://www.markdownguide.org/>


### 标题

```md
# 一级标题
## 二级标题 
### 三级标题
```

### 列表

顺序列表

```md
1. 序号
2. 序号
3. 序号
...
```

没顺序列表：

```md
- 序号
- 序号
- 序号
```

### 强调

```md
**粗体**
*斜体*
~~删除线~~
```

### 引用

```md
> 这是一段引用
> 可以换行继续写
>
> 也可以使用多个段落
```

### 代码

行内代码使用反引号包裹：`code`，代码块使用三个反引号，并可以标注语言：

````md
```python
print("Hello, World!")
```
````

### 链接

```md
[Markdown 指南](https://www.markdownguide.org/)
[带标题的链接](https://www.markdownguide.org/ "访问 Markdown 指南")
```

### 图片

```md
![替代文本](https://example.com/image.png)
```

图片和链接语法类似，区别是图片以 `!` 开头。

### 表格

```md
| 语法 | 说明 |
| ---- | ---- |
| 标题 | 使用 # 表示 |
| 列表 | 使用 - 或数字 |
```

### 任务列表

```md
- [x] 已完成
- [ ] 未完成
```

### 分割线

```md
---
```

用三个或更多 `-`、`*`、`_` 都可以生成分割线，常用于分隔文章段落。

## Miaoyan

https://raw.githubusercontent.com/tw93/static/main/miaoyan/miaoyan.gif

- GitHub: <https://github.com/tw93/MiaoYan>
- 官网：<https://miaoyan.app/>

轻量级 Markdown 笔记应用，专为 macOS 设计。

**主要特点**：

- 本地优先，支持 iCloud Drive
- 无账号、无追踪、无数据收集
- 三栏布局，编辑器和预览区并排显示
- 实时渲染，60fps 双向滚动同步
- 支持 LaTeX 数学公式、Mermaid 图表
- 演示模式：将 Markdown 转换为幻灯片
- Swift 6 原生开发，性能优异
