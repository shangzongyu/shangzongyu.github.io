---
title: "Tips: Obsidian 中图片分列显示"
description: Obsidian 默认的情况下一行显示一张，如果想要照片排列成类似九宫格的样式，需要做一些额外的处理。具体的做法就是使用自定义 CSS 代码片段。
slug: tips-obsidian
date: 2023-03-13 06:34:23+0000
image:
tags:
  - obsidian
weight: 1
---
Obsidian 默认的情况下一行显示一张，如果想要照片排列成类似九宫格的样式，需要做一些额外的处理。具体的做法就是使用自定义 CSS 代码片段。

实现方式如下。

## 新建 CSS 文件

在 `.obsidian/snapptes` 目录下新建文件 `img-grid.css`，内容如下：

```css
/* For Obsidian 0.9.22 and up */
.img-grid .markdown-preview-section img:not([width]),
.img-grid .markdown-preview-section video {
   width:100%;
}
.img-grid .markdown-preview-section > div {
   display:flex;
}
.img-grid .markdown-preview-section > div > .internal-embed {
   flex:1;
   margin-left:-0.5rem;
   padding:0 0.5rem 0.5rem 0.5rem;
}
.img-grid .markdown-preview-section > div > *:not(div) {
   margin-block-start: 0rem;
   margin-block-end: 1rem;
}
.img-grid .markdown-preview-section > div hr {
   width:100%;
}
/* These lines make every image the same height */
.img-grid .markdown-preview-section > div > .internal-embed img:not(:active) {
   object-fit:cover;
   height:100%;
}
```

在需要的文档头部 `front-matter` 添加配置写上 `cssclass: img-grid`，如下：

```yaml
---
cssclass: img-grid
---
```

> 用换行控制图片是否在同一行，图片间没有换行的话，图片默认在同一行。

## 安装主题 Minimal Theme

- 安装主题 `Minimal Theme`
- 在 `Minimal Theme Settings` 中开启 `Image grids` 选项
    
## 最终效果如下

![obsidian-css-grid] (https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230726_obsidian-css-grid.png align=“center”)

## 参考

- [Display side by side image grid](https://forum.obsidian.md/t/display-side-by-side-image-grid/9359)
