# 个人博客

基于 Hugo 和 LoveIt 主题的中文博客，使用 Typora 编辑，`upgit` / `piclist` 上传图片，GitHub Pages 托管。

## 开发环境

使用 [mise](https://mise.jdx.dev/getting-started.html) 管理工具版本和常用任务。先安装 mise，再在项目根目录执行：

```bash
mise trust
mise install
mise run hooks:install
```

[mise.toml](mise.toml) 固定 Hugo Extended、Go、Node.js、Python、uv、zhlint 和 pre-commit 的版本。Python 脚本依赖仍由 uv 管理。

## 常用命令

```bash
# 本地预览（含草稿、过期和未来文章）
mise run dev

# 指定预览端口
mise run dev --port 8080

# 新建文章
mise run blog:new "文章标题" -c 工具推荐

# 检查或修复文章格式
mise run lint
mise run fix

# 构建静态网站
mise run build
```

其他博客操作见[脚本工具说明](scripts/README.md)。任务参数会传递给对应命令；也可以用 `mise exec -- <命令>` 运行项目工具，无需激活 shell。

## 部署

推送 `master` 后，GitHub Actions 自动构建并部署到 `gh-pages`。CI 通过 [mise-action](https://github.com/jdx/mise-action) 安装 `mise.toml` 中指定的 Hugo Extended 和 Go，使本地与 CI 使用相同版本。
