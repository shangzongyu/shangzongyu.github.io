#!/bin/bash

# 检查参数数量
if [ $# -lt 1 ]; then
  echo "用法：$0 <目录>"
  exit 1
fi

dir="$1"

# 判断目录是否存在
if [ ! -d "$dir" ]; then
  echo "目录不存在: $dir"
  exit 2
fi

# 遍历目录下所有 Markdown 文件并执行命令
for file in "$dir"/*.md; do
  if [ -f "$file" ]; then
    echo "处理文件: $file"
    zhlint --fix "$file"
  fi
done
