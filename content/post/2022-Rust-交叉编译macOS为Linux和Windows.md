---
title: Rust 交叉编译 macOS 为 Linux 和 Windows
description: 
slug: rust-macos-linux-windows
date: 2022-05-15 06:23:27+0000
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_2022-Rust-交叉编译macOS为Linux和Windows.webp
tags:
  - linux
  - rust
  - macos
weight: 1
---

> Rust 支持交叉编译，可以 macOS 平台编译出 Linux 或者 Windows 可运行的程序，或者在 Linux 平台编译 macOS 或者 Windows 可运行的程序。
>
> 这篇文章主要讲解 Mac 平台编译为其他平台的二进制程序。

<!--more-->

想要实现跨平台编译并且可运行的程序，那么我们就需要静态链接，这样生成程序才不会因为动态链接库的原因运行失败。

在默认情况下，Rust 静态连接所有 Rust 代码。如果程序中使用了标准库，Rust 会连接到系统的 `libc` 实现。

## 环境

- macOS：
  - OS：`macOS 12.3.1 21E258 x86_64`
  - rustc：`rustc 1.60.0 (7737e0b5c 2022-04-04)`
  - rustup：`rustup 1.24.3 (ce5817a94 2021-05-31)`
- Linux：
  - OS：`EndeavourOS Linux x86_64`
  - kernel：`5.17.1-arch1-1`
  - rustc：`rustc 1.60.0 (7737e0b5c 2022-04-04)`
  - rustup：`rustup 1.24.3 (ce5817a94 2021-05-31)`

> 首先需要安装 Rust，这个这里就不要说了。

## 示例准备

使用 `Cargo` 新建二进制项目：

```sh
cargo new --bin hello
```

文件 `main.rs`：

```rs
fn main() {
  println!("Hello World!\n");
}
```

## macOS 编译为 Linux 和 Windows 可用二进制程序

### 编译为 Linux 平台

> 要实现 Linux 平台可以运行的程序，那么需要使用 [musl] 来替代 `glibc`，[musl][musl] 实现了 `Linux libc`。

[musl] 在 macOS 上使用 musl-cross，musl-cross 是用来专门编译到 Linux 的工具链，下面进行安装：

```sh
brew install FiloSottile/musl-cross/musl-cross
```

还需要创建 `musl-gcc`：

```sh
ln -s /usr/local/bin/x86_64-linux-musl-gcc /usr/local/bin/musl-gcc
```

添加对应的 Target，只需要执行一次就可以了：

```sh
rustup target add x86_64-unknown-linux-musl
```

修改配置文件 `~/.cargo/config` (如果没有可以新建)，添加如下内容：

```ini
[target.x86_64-unknown-linux-musl]
linker = "x86_64-linux-musl-gcc"
```

> 也可在项目根目录下创建 `.cargo/config` 文件，只对当前项目生效

编译：

```sh
# 使用
cargo build --release --target x86_64-unknown-linux-musl
```

结果：

```sh
$ tree -L 2 target/x86_64-unknown-linux-musl
target/x86_64-unknown-linux-musl
├── CACHEDIR.TAG
└── debug
    ├── build
    ├── deps
    ├── examples
    ├── hello
    ├── hello.d
    └── incremental

5 directories, 3 files
$ file target/x86_64-unknown-linux-musl/debug/hello
target/x86_64-unknown-linux-musl/debug/hello: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), static-pie linked, with debug_info, not stripped
```

### 编译为 Windows 平台

`mingw-w64` 是用来编译到 Windows 的工具链，使用如下命令进行安装：

```sh
brew install mingw-w64
```

接下来添加 `mingw-64` 对应的 Target，只需要执行一次就可以了：

```sh
rustup target add x86_64-pc-windows-gnu
```

修改配置文件 `~/.cargo/config` (如果没有可以新建)，设置 Linker，添加如下内容：

```sh
[target.x86_64-pc-windows-gnu]
linker = "x86_64-w64-mingw32-gcc"
ar = "x86_64-w64-mingw32-gcc-ar"
```

编译：

```sh
# 使用
$ cargo build --release --target x86_64-unknown-linux-musl
```

结果：

```sh
$ tree -L 2 target/x86_64-pc-windows-gnu
target/x86_64-pc-windows-gnu
├── CACHEDIR.TAG
└── debug
    ├── build
    ├── deps
    ├── examples
    ├── hello.d
    ├── hello.exe
    └── incremental

5 directories, 3 files
$ file target/x86_64-pc-windows-gnu/debug/hello.exe
target/x86_64-pc-windows-gnu/debug/hello.exe: PE32+ executable (console) x86-64, for MS Windows
```

## 在 Linux 编译为 macOS 和 Windows

### 编译为 macOS 平台

在 Linux 编译 macOS 平台使用 [osxcross][osxcross]。[osxcross][osxcross] 可以在 Linux/FreeBSD/OpenBSD 以及 Android (Termux) 交叉编译 macOS 平台的工具。

我看了下 [osxcross][osxcross] 编译为 macOS 平台真的还是挺麻烦的，我决定不编译为 macOS 版本，何必为难自己呢，何况自己有 Mac 电脑呢 😂。

### 编译为 Windows 平台

`mingw-w64` 是用来编译到 Windows 的工具链，Arch 对应的包为 [mingw-w64-gcc](https://archlinux.org/packages/community/x86_64/mingw-w64-gcc/)，接下来进行安装：

```sh
sudo pacman -S mingw-w64-gcc
```

接下来就容易了，和 “macOS 编译为 Linux 和 Windows” 一样了，就是添加 Target，修改配置文件，然后编译就可以了。

## FAQ

### `x86_64-unknown-freebsd` target may not be installed

自己在 Mac 平台的时候，把上述所有的操作都做了，但是还是包如下错误：

```sh
error[E0463]: can't find crate for `std`
  |
  = note: the `x86_64-unknown-freebsd` target may not be installed
  = help: consider downloading the target with `rustup target add x86_64-unknown-freebsd`

error: requires `sized` lang_item
```

那么怎么解决的呢，我发现自己之前使用 [Homebrew][homebrew] 安装过 `rust`，而且还使用官方命令 `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` 再次进行安装，导致 rust 工具链对不上，只需要做如下操作就可以了：

1. 先完全卸载

```sh
brew uninstall rust
rustup self uninstall
```

1. 重新安装：

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### error：linking with `cc` failed：exit status：1

配置 `~/.cargo/config` 或者在项目内 `.cargo/config` 文件就可以解决这个问题。

## 总结

介绍了在 macOS 编译为 Linux/Windows 以及 Linux 平台编译为 macOS/Windows，其实就两个三个步骤：

1. 添加相应的 Target
2. 安装对应的 Linker
3. 修改配置文件

从 macOS 编译其他的平台，其实是比较容易的，从其他平台编译为 macOS 平台却不那么简单，最终自己放弃了。

## Reference

- [MUSL 支持完全静态二进制文件](https://rustwiki.org/zh-CN/edition-guide/rust-2018/platform-and-target-support/musl-support-for-fully-static-binaries.html#musl-%E6%94%AF%E6%8C%81%E5%AE%8C%E5%85%A8%E9%9D%99%E6%80%81%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)
- [Rust on Lambda](https://rendered-obsolete.github.io/2019/03/19/rust_lambda.html)
- [Cross-compiling a simple Rust web app](https://www.andrew-thorburn.com/cross-compiling-a-simple-rust-web-app/)
- [How to Cross-Compile from Mac to Linux on Rust](https://stackoverflow.com/questions/57797695/how-to-cross-compile-from-mac-to-linux-on-rust)
- [MUSL support for fully static binaries](https://doc.rust-lang.org/edition-guide/rust-2018/platform-and-target-support/musl-support-for-fully-static-binaries.html)
- [Cross-compile and link a static binary on macOS for Linux with cargo and rust](https://chr4.org/blog/2017/03/15/cross-compile-and-link-a-static-binary-on-macos-for-linux-with-cargo-and-rust/)
- [Everything you need to know about cross compiling Rust programs](https://rustrepo.com/repo/japaric-rust-cross-rust-embedded#cross-compiling-with-rustc)
- [Cross-compiling Rust from ARM to x86-64](https://burgers.io/cross-compile-rust-from-arm-to-x86-64)
- [Cross compiling Rust from Linux to macOS](https://wapl.es/rust/2019/02/17/rust-cross-compile-linux-to-macos.html)

---

[musl]: https://musl.libc.org/
[homebrew]: https://brew.sh/
[osxcross]: https://github.com/tpoechtrager/osxcross
