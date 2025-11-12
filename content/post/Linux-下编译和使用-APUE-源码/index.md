---
title: 'Linux 下编译和使用 APUE 源码'
description: '介绍如何在 Linux 下 Linux 下编译和使用 APUE 源码。'
slug: linux-config-apue
date: 2022-05-02 16:00:00+0000
tags:
    - linux
weight: 1
---


> 介绍如何在 Linux 下 Linux 下编译和使用 APUE 源码。

![apue-cover-v3] (https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230726_apue-cover-v3.png align=“center”)

## 环境

- APUE 版本：第三版
- Linux 发行版：[EndeavourOS](https://endeavouros.com/)
- Gcc 版本：11.2.0
- GNU Make 版本：4.3

> [EndeavourOS](https://endeavouros.com/) 是基于 Arch Linux 的发行版，默认已经安装 `make`、`gcc` 以及 `libbsd`。

## 开始

一共分为两步：

1. 下载源码
2. 编译源码

> 最重要的是编译这一步，编译其实很简单，只是会报错，我们一步一步解决即可。

### 1。下载源码

到[官网](http://www.apuebook.com/code2e.html)下载 APUE 的源码或者使用命令 `wget` 进行下载

> 这里使用 `wget` 命令下载。

```sh
# 下载
$ wget http://www.apuebook.com/src.3e.tar.gz

# 解压
$ tar -zxvf src.3e.tar.gz
```

### 2。编译

```sh
# 进入 apue 源码目录
$ cd apue.3e

# 编译
$ make
...
...
...
```

当然没有那么容易编程成功，果不其然出错了，我们一个一个来，我遇到的问题有如下几个。

#### 错误

##### 错误 1：编译 db 的时候报错 `/usr/bin/ld: Error: unable to disambiguate: -dylib (did you mean --dylib ?)`

详细的如下：

```sh
$ make
...
making db
make[1]: Entering directory '/home/shine/Code/apue.3e/db'
gcc -fPIC -ansi -I../include -Wall -DLINUX -D_GNU_SOURCE  -c db.c
gcc -shared -Wl,-dylib -o libapue_db.so.1 -L../lib -lapue -lc db.o
/usr/bin/ld: Error: unable to disambiguate: -dylib (did you mean --dylib ?)
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:32: libapue_db.so.1] Error 1
make[1]: Leaving directory '/home/shine/Code/apue.3e/db'
make: *** [Makefile:6: all] Error 1
```

**解决方法**：修改 `db/Makefile` 文件第 12 行，修改为 `LDCMD=$(CC) -shared -o libapue_db.so.1 -L$(ROOT)/lib -lapue -lc db.o`

修改成功后，再次执行 `make` 命令。

##### 错误 2：编译 `devrdev.c` 出错，`devrdev.c:(.text+0xc7): undefined reference to` minor ‘\`

详细的如下：

```sh
$ make
...
devrdev.c: In function ‘main’:
devrdev.c:19:39: warning: implicit declaration of function ‘major’ [-Wimplicit-function-declaration]
   19 |                 printf("dev = %d/%d", major(buf.st_dev),  minor(buf.st_dev));
      |                                       ^~~~~
devrdev.c:19:59: warning: implicit declaration of function ‘minor’ [-Wimplicit-function-declaration]
   19 |                 printf("dev = %d/%d", major(buf.st_dev),  minor(buf.st_dev));
      |                                                           ^~~~~
/usr/bin/ld: /tmp/ccZ80s7o.o: in function `main':
devrdev.c:(.text+0xc7): undefined reference to `minor'
/usr/bin/ld: devrdev.c:(.text+0xdd): undefined reference to `major'
/usr/bin/ld: devrdev.c:(.text+0x12d): undefined reference to `minor'
/usr/bin/ld: devrdev.c:(.text+0x143): undefined reference to `major'
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:18: devrdev] Error 1
make[1]: Leaving directory '/home/shine/Code/apue.3e/filedir'
make: *** [Makefile:6: all] Error 1
```

解决办法：`filedir/devrdev.c`，添加头文件 `#include <sys/sysmacros.h>`。

修改成功后，再次执行 `make` 命令。

##### 错误 3：编译 `stdio` 目录出错

```sh
$ make
...
making stdio
make[1]: Entering directory '/home/shine/Code/apue.3e/stdio'
gcc -ansi -I../include -Wall -DLINUX -D_GNU_SOURCE  buf.c -o buf  -L../lib -lapue
buf.c: In function ‘is_unbuffered’:
buf.c:90:15: error: ‘FILE’ has no member named ‘__pad’; did you mean ‘__pad5’?
   90 | #define _flag __pad[4]
      |               ^~~~~
buf.c:98:20: note: in expansion of macro ‘_flag’
   98 |         return(fp->_flag & _IONBF);
      |                    ^~~~~
buf.c: In function ‘is_linebuffered’:
buf.c:90:15: error: ‘FILE’ has no member named ‘__pad’; did you mean ‘__pad5’?
   90 | #define _flag __pad[4]
      |               ^~~~~
buf.c:104:20: note: in expansion of macro ‘_flag’
  104 |         return(fp->_flag & _IOLBF);
      |                    ^~~~~
buf.c: In function ‘buffer_size’:
buf.c:92:15: error: ‘FILE’ has no member named ‘__pad’; did you mean ‘__pad5’?
   92 | #define _base __pad[2]
      |               ^~~~~
buf.c:111:20: note: in expansion of macro ‘_base’
  111 |         return(fp->_base - fp->_ptr);
      |                    ^~~~~
buf.c:91:14: error: ‘FILE’ has no member named ‘__pad’; did you mean ‘__pad5’?
   91 | #define _ptr __pad[1]
      |              ^~~~~
buf.c:111:32: note: in expansion of macro ‘_ptr’
  111 |         return(fp->_base - fp->_ptr);
      |                                ^~~~
buf.c: In function ‘is_unbuffered’:
buf.c:99:1: warning: control reaches end of non-void function [-Wreturn-type]
   99 | }
      | ^
buf.c: In function ‘is_linebuffered’:
buf.c:105:1: warning: control reaches end of non-void function [-Wreturn-type]
  105 | }
      | ^
buf.c: In function ‘buffer_size’:
buf.c:115:1: warning: control reaches end of non-void function [-Wreturn-type]
  115 | }
      | ^
make[1]: *** [Makefile:16: buf] Error 1
make[1]: Leaving directory '/home/shine/Code/apue.3e/stdio'
make: *** [Makefile:6: all] Error 1
```

**解决方法**：

- 修改 `buf.c` 98 行和 104 行的 `_flag` 修改为 `_flags`
- 修改 `buf.c` 111 行 `return(fp->_base - fp->_ptr);` 修改为 `return(fp->_IO_buf_end - fp->_IO_buf_base);`

#### 测试

把上述错误修改完成后，我们再次执行 `make`。

```sh
$ cd apue.3e/intro
$ ./hello
hello world from process ID 3380
```

成功运行。

## 使用 APUE 源码

那么如何使用 APUE 源码，很简单只需要指定它的头文件 `apue.h` 和静态库 `libapue.a`。

新建文件 `hello_process.c` 内容如下：

```c
#include "apue.h"

int main(void)
{
  printf("hello world from process ID %ld\n", (long)getpid());
  exit(0);
}
```

### 直接使用 Gcc 编译

编译：

```sh
$ gcc hello_process.c -o hello_process -I../apue.3e/include -L../apue.3e/lib
```

每次都这样指定头文件和相应的库比较麻烦，APUE 源码编译成功后，会在 `apue.3e/lib` 目录下生成静态库 `libapue.a`，为了方便我们把相应的静态 `libapue.a` 和头文件放到系统相关的目录中，如下：

```sh
sudo cp include/apue.h /usr/include/
sudo cp lib/error.c /usr/include/
sudo cp lib/libapue.a /usr/lib
```

如果不使用了，通过如下命令清理：

```sh
sudo rm /usr/include/apue.h
sudo rm /usr/include/error.c
sudo rm /usr/lib/libapue.a
```

### 使用 CMake

新建 `CMakefile.txt` 如下：

```bash
cmake_minimum_required(VERSION 2.8)
project(apue)

set(SOURCE_FILES hello_process.c)
add_executable(main ${SOURCE_FILES})

include_directories(/usr/include)
target_link_libraries(hello_process /usr/lib/libapue.a)
```

为了防止 CMake 执行过程中污染源码，在同级目录新建 `build` 具体步骤如下：

```sh
$ mkdir build
$ cd build
# 执行 cmake，生成 makefile
$ cmake .
# 运行 makefile
$ make
# 运行
$ ./hello_process
```

### 其他

如果使用 `err_sys` 等函数在编译时找不到的问题：在 `apue.h` 文件里添加 `#include "error.c"` 即可。
