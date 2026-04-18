#!/bin/bash

# 修改 Markdown 文件中的 date 字段
# 使用方法:
#   ./update_date.sh <文件路径> [新日期]
#   ./update_date.sh content/post/2026-diff-tools.md "2026-04-18T10:30:00+08:00"
#   ./update_date.sh content/post/2026-diff-tools.md  # 使用当前时间
#   ./update_date.sh content/post/*.md                # 批量更新多个文件为当前时间

# 检查参数
if [ $# -lt 1 ]; then
    echo "使用方法: $0 <文件路径> [新日期]"
    echo ""
    echo "示例:"
    echo "  $0 content/post/2026-diff-tools.md '2026-04-18T10:30:00+08:00'"
    echo "  $0 content/post/2026-diff-tools.md  # 使用当前时间"
    echo "  $0 content/post/*.md                # 批量更新所有文件为当前时间"
    exit 1
fi

# 获取文件路径
FILES=("$@")

# 如果提供了两个参数，第二个是日期
if [ $# -eq 2 ]; then
    NEW_DATE="$2"
    FILES=("$1")
else
    # 使用当前时间
    NEW_DATE=$(date +"%Y-%m-%dT%H:%M:%S+08:00")
fi

echo "使用日期: $NEW_DATE"
echo ""

# 遍历所有文件
for file in "${FILES[@]}"; do
    # 检查文件是否存在
    if [ ! -f "$file" ]; then
        echo "❌ 文件不存在: $file"
        continue
    fi

    # 检查是否是 Markdown 文件
    if [[ ! "$file" =~ \.md$ ]]; then
        echo "❌ 跳过非 Markdown 文件: $file"
        continue
    fi

    # 检查文件是否包含 frontmatter (以 --- 开头)
    if ! grep -q "^---" "$file"; then
        echo "❌ 文件不包含 frontmatter: $file"
        continue
    fi

    # 检查是否已经有 date 字段
    if grep -q "^date:" "$file"; then
        # 更新现有的 date 字段
        sed -i '' "s/^date:.*/date: $NEW_DATE/" "$file"
        echo "✅ 已更新: $file"
    else
        # 在 title 字段后添加 date 字段
        sed -i '' "/^title:/a\\
date: $NEW_DATE
" "$file"
        echo "✅ 已添加: $file"
    fi
done

echo ""
echo "完成！"
