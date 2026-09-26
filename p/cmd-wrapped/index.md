# 工具推荐：cmd-wrapped - 查看 Shell 历史记录


查看 Shell 历史记录。

<!--more-->

## 介绍

使用 Rust 实现的用户查看自己命令行的使用。

## 安装

Github：<https://github.com/YiNNx/cmd-wrapped>

```sh
# 使用 cargo
cargo install cmd-wrapped

# Arch Linux
yay -S cmd-wrapped

# 自己编译使用
git clone git@github.com:YiNNx/cmd-wrapped.git
cd cmd-wrapped

## 生成 2023年
cargo run -- 2023
## 或者
./target/debug/cmd-wrapped 2023
```

## 查看自己 2023 年命令使用

我的运行结果如下图。

![cmd-wrapped-00](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20240106_cmd-wrapped-00.png)

![cmd-wrapped-01](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20240106_cmd-wrapped-01.png)

![cmd-wrapped-02](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2024/upgit_20240106_cmd-wrapped-02.png)

