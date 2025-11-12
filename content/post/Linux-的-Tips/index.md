---
title: 'Linux 的 Tips'
description: 'Linux 使用过程中的一些技巧整理。'
slug: linux-tips
date: 2022-05-16 05:46:47+0000
image: cover.jpg
tags:
    - linux
    - tips
weight: 1
---


> Linux 使用过程中的一些技巧整理。
> 
> 持续更新中...

## 关闭终端下 `Tab` 键的蜂鸣提示

修改配置文件：

```sh
sudo vim /etc/inputrc
```

将 `set bell-style none` 前的注释去掉
