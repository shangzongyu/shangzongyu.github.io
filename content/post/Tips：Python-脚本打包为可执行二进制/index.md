---
title: 'Tips: Python 脚本打包为可执行二进制'
description: '前言：最近需要使用 Python 写一个脚本，但是我不想在所在机器安装 Python 环境，因此就在想有没有可以把 Python 脚本打包为可执行的二进制程序，找到了 Nuitka，一个强大的 Python 编译器，可以将 Python'
slug: tips-python
date: 2025-05-27 09:32:08+0000
image: cover.jpg
tags:
    - tips
    - python3
weight: 1
---

> 前言：最近需要使用 Python 写一个脚本，但是我不想在所在机器安装 Python 环境，因此就在想有没有可以把 Python 脚本打包为可执行的二进制程序，找到了 Nuitka，一个强大的 Python 编译器，可以将 Python 代码编译为 C 代码，并生成高效的可执行文件。除了之外还有其他的，选择 Nuitka 是因为它的性能比较好。

## 环境

OS：Ubuntu 24.04 LTS

需要装安装包：

```sh
sudo apt-get install build-essential python3

pip install nuitka
```

## 实践

### Hello World

先来一个比较简单的程序，文件名为 `hello_world.py`，主要内容如下：

```py
import sys


def main():
    print("Hello from Nuitka on MacBook!")
    print("Arguments:", sys.argv)


if __name__ == "__main__":
    main()
```

写完后，然后进行打包为二进制程序，使用如下命令：

```sh
python -m nuitka --standalone --onefile --follow-imports --show-progress --output-dir=dist hello_world.py

# 执行成功后，会在 dist 目录下生成 hello_world.bin，这个就是可执行文件
./file hello_world.bin 
hello_world.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=56ba24bccfa917e6ce9009223e4e83924f616d46, for GNU/Linux 3.2.0, stripped
```

参数说明：

- `--standalone`：生成包含所有依赖的独立目录。
- `--onefile`：将结果打包为单个可执行文件。
- `--follow-imports`：自动包含所有导入的模块。
- `--show-progress`：显示编译进度。
- `--output-dir=dist`：指定输出目录。

### 一个更加复杂的示例：FastAPI 提供简单的 WebServer

```py
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
import logging

app = FastAPI(
    title="Simple Inventory API", description="A simple CRUD API with in-memory storage"
)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建物品
@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    pass

# 读取单个物品
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    pass


# 获取物品列表（支持分页）
@app.get("/items/", response_model=List[Item])
async def list_items(
    pass

# 更新物品
@app.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, item: Item):
    pass


# 删除物品
@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    pass

# 启动应用
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
```

> 生成二进制文件和上面那个类似，不过有一点需要注意的是，在打包之前需要把需要的包装好了，然后才能打包。

> 完整的示例参考：<https://raw.githubusercontent.com/shangzongyu/experiments/refs/heads/master/python-nuitka/fastapi_example.py>

## FAQ

### `apt/dnf/yum install patchelf' first.`

> 详细错误如下：
>  python -m nuitka --standalone --onefile --follow-imports --show-progress --output-dir=dist hello_world.py
Nuitka-Options：Used command line options：
Nuitka-Options：   --standalone --onefile --follow-imports --show-progress --output-dir=dist hello_world.py
FATAL：Error，standalone mode on Linux requires ‘patchelf’ to be installed。Use ‘apt/dnf/yum install patchelf’ first。

解决方法如下：

```sh
sudo apt install patchelf
```
