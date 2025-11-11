---
title: 常用字体设置
description: '> 在常用的软件中设置自己常用的字体。'
slug: 5bi455so5a2x5l2t6k6572u
date: 2024-01-07 10:33:52+0000
tags:
    - fonts
    - tips
weight: 1
---


> 在常用的软件中设置自己常用的字体。

- 中文使用[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)，很好看的中文字体题。
- 英文使用 [FiraCode](https://github.com/tonsky/FiraCode)

## VS Code 设置

打开 VSCode 的配置，修改配置：

```json
 "editor.fontFamily": "'FiraCode Nerd Font Mono', 'LXGW WenKai Mono'"
```

## Logseq 设置

在 `Settings-> General -> Custom theme -> Edit custom.css` 添加如下内容

```
@font-face {
  font-family: "FiraCode Nerd Font Mono";
  font-weight: 200 900;
  font-style: normal;
  font-stretch: normal;
  src: url("https://letui-game-res.oss-cn-shenzhen.aliyuncs.com/tmp/RobotoMono.ttf");
}

@font-face {
  font-family: "LXGW WenKai Mono";
  font-weight: 200 900;
  font-style: normal;
  font-stretch: normal;
  src: url("https://letui-game-res.oss-cn-shenzhen.aliyuncs.com/tmp/LXGWWenKaiMono-Regular.ttf");
}

:root {
  --ct-text-size: 20px;
  --ct-line-height: 1.6;
  --ls-font-family: FiraCode Nerd Font Mono, "Only Emoji", "LXGW WenKai Mono";
  --ct-page-title-font-family: var(--ls-font-family);
  --ct-code-font-family: FiraCode Nerd Font Mono,"LXGW WenKai Mono", monospace;
}
.CodeMirror {
  font-family: FiraCode Nerd Font Mono,"LXGW WenKai Mono", monospace;
}
:not(pre)>code {
  font-family: FiraCode Nerd Font Mono,"LXGW WenKai Mono", monospace;
}
```

为了统一性，统一使用 `src` 设置字体路径。

> 上面设置的配置在手机上会正常展示。

## iTerm2

打开配置 `Preferences -> Profiles -> Default -> Font`：

- `Font` 设置为 `Fira Code Nerd Font`
- `Non-ASCIIFont` 设置为 `LXGW WenKai Mono`

## Typroa

在 Typora 的主题文件夹下，创建 `base.user.css`，里面写上如下内容：

```json
body {
    font-family: 'FiraCode Nerd Font Mono', "LXGW WenKai Mono";
    --monospace: 'FiraCode Nerd Font Mono', "LXGW WenKai Mono"; 
}
```

然后重启 Typora 就可以看到字体修改成功了。