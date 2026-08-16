# 脚本工具说明

## blog.py - 博客日常命令工具

博客日常操作统一入口（Python 3.12+）。脚本头部声明 uv 内联脚本依赖（`rich`），直接 `./scripts/blog.py` 即可运行，无需手动安装。`fix`、`update-date` 需从项目根目录运行，目录/文件参数使用项目内相对路径（zhlint 只接受不含 `..` 的相对路径）。

### serve - 启动本地服务

```bash
./scripts/blog.py serve                # 等价于 start.sh（含草稿/过期/未来文章）
./scripts/blog.py serve --port 8080    # 指定端口
```

### new - 新建文章

```bash
./scripts/blog.py new "文章标题"                    # 交互式选择分类
./scripts/blog.py new "文章标题" -c 工具推荐          # 直接指定分类
./scripts/blog.py new "文章标题" -c Tips -p          # 创建为已发布（draft: false）
./scripts/blog.py new "文章标题" --no-open           # 创建后不打开 Typora
```

- 走 `archetypes/post.md` 模板生成骨架，`date` 自动填当前时间，`draft` 默认 `true`
- 文件名自动生成 `YYYY-类别_标题.md`，中文保留、空格转 `-`，自动查重
- 标题直接写入 frontmatter 的 `title` 字段（不经过文件名派生）
- 分类从现有文章 frontmatter 自动提取（兼容单行与列表格式），交互式选择或直接输入新分类
- 创建后默认用 Typora 打开（`--no-open` 关闭）

### fix - 修复 Markdown 格式（zhlint --fix）

```bash
./scripts/blog.py fix content/posts               # 递归并行处理（默认）
./scripts/blog.py fix content/posts --top-only    # 仅处理目录顶层文件
./scripts/blog.py fix content/posts content/page  # 多个目录
./scripts/blog.py fix content/posts -j 8          # 指定并行线程数（默认 4）
```

原 fix_zhlint.sh 依赖 GNU parallel，本脚本改用标准库线程池实现，无外部依赖。

### update-date - 修改文章 date 字段

```bash
./scripts/blog.py update-date content/posts/2026-xxx.md "2026-04-18T10:30:00+08:00"  # 指定日期
./scripts/blog.py update-date content/posts/2026-xxx.md  # 使用当前时间
./scripts/blog.py update-date content/posts/*.md         # 批量更新多个文件为当前时间
```

规则：已有 `date` 字段则替换，没有则在 `title` 字段后添加；第二个参数以 `YYYY-MM-DD` 开头才视为指定日期，否则视为文件（避免批量更新两个文件时误判）。
