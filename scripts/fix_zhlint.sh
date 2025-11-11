#!/bin/bash

# 目录列表，传入多个目录作为参数
DIRS=("$@")

# 并行函数，递归处理指定目录下所有 Markdown 文件
fix_in_dir() {
  local dir="$1"
  find "$dir" -type f -name "*.md" | while read -r file; do
    echo "Fixing $file ..."
    zhlint --fix "$file"
  done
  echo "Finished processing $dir"
}

export -f fix_in_dir

# 使用 parallel 并行处理多个目录
printf "%s\n" "${DIRS[@]}" | parallel -j 4 fix_in_dir {}

echo "所有目录并行修复完成。"
