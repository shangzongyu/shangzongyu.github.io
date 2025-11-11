---
title: 'Tips: Cursor 免费试用重置'
description: '* Github: https://github.com/yuaotian/go-cursor-help'
slug: tips-cursor
date: 2024-12-21 06:43:20+0000
tags:
    - tips
weight: 1
---


## 介绍

* Github：[https://github.com/yuaotian/go-cursor-help](https://github.com/yuaotian/go-cursor-help)
    

解决 Cursor 免费订阅期间出现出现下面的问题：

```plaintext
Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake.
```

## 安装和使用

我的环境：macOS 15.2

### 安装

```sh
# 下载
wget https://github.com/yuaotian/go-cursor-help/releases/download/v0.0.6/cursor_id_modifier_0.0.6_darwin_amd64

# 添加可执行权限
chmod a+x cursor_id_modifier_0.0.6_darwin_amd64

# 运行
./cursor_id_modifier_0.0.6_darwin_amd64
```

安装脚本会自动执行如下操作：

* 需要 Sudo 权限
    
* 关闭所有的 Cusor 实例
    
* 备份存在的配置文件
    
* 安装工具
    
* 把工具添加到 PATH 路径
    
* 清理临时文件