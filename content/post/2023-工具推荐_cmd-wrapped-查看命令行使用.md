---
title: 工具推荐：cmd-wrapped - 查看 Shell 历史记录
description: 
slug: cmd-wrapped
date: 2023-12-20 16:00:00+0000
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_2023-工具推荐_cmd-wrapped--查看命令行使用.webp
tags:
  - tools
  - command—line
weight: 1
---

## 介绍

使用 Rust 实现的用户查看自己命令行的使用。

## 安装

Github： <https://github.com/YiNNx/cmd-wrapped>

```sh
# 使用 cargo
cargo install cmd-wrapped

# ArchLinux
yay -S cmd-wrapped

# 自己编译使用
git clone git@github.com:YiNNx/cmd-wrapped.git
cd cmd-wrapped
## 生成 2023年
cargo run -- 2023
## 或者
./target/debug/cmd-wrapped 2023
```

## cmd-wrapped 查看自己 2023 年命令使用

我的运行结果如下图。

![cmd-wrapped-00](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20240106_cmd-wrapped-00.png)

![cmd-wrapped-01](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20240106_cmd-wrapped-01.png)

![cmd-wrapped-02](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20240106_cmd-wrapped-02.png)

## cmd-wrapped 查看自己 2024 年命令使用

![cmd-wrapped-2024](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20241221_cmd-wrapped-2024.png)

![cmd-wrapped-2024-01](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20241221_cmd-wrapped-2024-01.png )

![cmd-wrapped-2024-02](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20241221_cmd-wrapped-2024-02.png)
