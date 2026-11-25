# 脚本工具说明

## blog.py - 博客日常命令工具

博客日常操作使用 `mise run blog:<子命令>`。`blog:fix` 和 `blog:update-date` 的示例使用相对于项目根目录的路径，zhlint 只接受不含 `..` 的相对路径。

项目工具统一由根目录的 `mise.toml` 管理，首次使用先运行 `mise trust` 和 `mise install`。脚本使用 Python 3.12+，`rich` 依赖由 uv 自动管理。需要直接调用脚本时，可使用 `mise exec -- ./scripts/blog.py <子命令>`。

### blog:serve - 启动本地服务

```bash
mise run blog:serve                # 含草稿、过期和未来文章
mise run blog:serve --port 8080    # 指定端口
```

### blog:new - 新建文章

```bash
mise run blog:new "文章标题"                    # 交互式选择分类
mise run blog:new "文章标题" -c 工具推荐          # 直接指定分类
mise run blog:new "文章标题" -c Tips -p          # 创建为已发布（draft: false）
mise run blog:new "文章标题" --no-open           # 创建后不打开 Typora
```

- 走 `archetypes/post.md` 模板生成骨架，`date` 自动填当前时间，`draft` 默认 `true`
- 文件名自动生成 `YYYY-类别_标题.md`，中文保留、空格转 `-`，自动查重
- 标题直接写入 frontmatter 的 `title` 字段 (不经过文件名派生)
- 分类从现有文章 frontmatter 自动提取 (兼容单行与列表格式)，交互式选择或直接输入新分类
- 创建后默认用 Typora 打开 (`--no-open` 关闭)

### blog:image - 上传文章配图

写草稿时，在文章旁建立同名的 `.assets` 目录。例如 `2026-工具推荐_T3-Code.md` 的图片放在 `2026-工具推荐_T3-Code.assets/`，正文用 `![配图](2026-工具推荐_T3-Code.assets/screenshot.png)` 引用，封面在 `featuredImage` 中填写同样的相对路径。Markdown 图片链接里的路径如果有空格，可用尖括号包住路径或将空格写成 `%20`。

```bash
mise run blog:image 2026-工具推荐_T3-Code.md
```

首次使用时，在本机的 `~/.config/upgit/config.toml` 的 `[uploaders.github]` 中设置 `pat`，也可以通过环境变量 `UPGIT_TOKEN` 提供。令牌需要 `shangzongyu/blog-image` 仓库的 `Contents` 读写权限。mise 会为此任务安装所需的 `upgit` 版本。

命令会上传文章引用的 `.assets` 图片，再统一更新正文中的行内 Markdown 图片、HTML `<img src>` 和封面字段中的链接。上传失败时可重试，同一份图片内容会使用同一个远端路径。草稿状态和 Git 提交由作者控制，本地原图保留在 Git 忽略的配图目录中。

### blog:fix - 修复 Markdown 格式 (zhlint --fix)

```bash
mise run blog:fix content/posts               # 递归并行处理（默认）
mise run blog:fix content/posts --top-only    # 仅处理目录顶层文件
mise run blog:fix content/posts content/page  # 多个目录
mise run blog:fix content/posts -j 8          # 指定并行线程数（默认 4）
```

原 fix_zhlint.sh 依赖 GNU parallel，本脚本改用标准库线程池实现，无外部依赖。

### blog:update-date - 修改文章 date 字段

```bash
mise run blog:update-date content/posts/2026-xxx.md "2026-04-18T10:30:00+08:00"  # 指定日期
mise run blog:update-date content/posts/2026-xxx.md  # 使用当前时间
mise run blog:update-date content/posts/*.md         # 批量更新多个文件为当前时间
```

规则：已有 `date` 字段则替换，没有则在 `title` 字段后添加；第二个参数以 `YYYY-MM-DD` 开头才视为指定日期，否则视为文件 (避免批量更新两个文件时误判)。
