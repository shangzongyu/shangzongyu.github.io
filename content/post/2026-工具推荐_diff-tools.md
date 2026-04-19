---
title: "工具推荐: Diff Tools"
description: 文件对比和 Git diff 美化工具
date: 2026-04-18T20:07:20+08:00
image:
math:
license:
tags: ["工具", "diff", "Git"]
categories: ["工具推荐"]
hidden: false
comments: true
weight: 1
---

## Vim Diff

```bash
# 命令行启动
vim -d file1 file2
nvim -d file1 file2

# 水平分割
vim -d -o file1 file2

# 比较多个文件
vim -d file1 file2 file3
```

**快捷键**：
- `]c` - 跳到下一个差异
- `[c` - 跳到上一个差异
- `do` / `:diffget` - 从另一个窗口获取修改
- `dp` / `:diffput` - 将修改放到另一个窗口
- `:diffupdate` - 更新差异
- `:diffoff` - 关闭 diff 模式

### Git

```bash
git config --global diff.tool vimdiff
git config --global difftool.prompt false
git difftool
```

### SVN

创建脚本 `svnvimdiff`：

```bash
#!/bin/bash
vimdiff "$6" "$7"
```

配置：

```bash
# ~/.subversion/config
[helpers]
diff-cmd = /path/to/svnvimdiff

# 或临时使用
svn diff --diff-cmd vimdiff
```

## diff-so-fancy

- GitHub: <https://github.com/so-fancy/diff-so-fancy>

### 安装

```bash
# macOS
brew install diff-so-fancy

# Ubuntu/Debian
sudo apt install diff-so-fancy
```

### Git

```bash
git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"
git config --global interactive.diffFilter "diff-so-fancy --patch"
git diff
```

### SVN

```bash
# ~/.subversion/config
[helpers]
diff-cmd = diff-so-fancy

# 或临时使用
svn diff --diff-cmd diff-so-fancy
```

## git-delta

- GitHub: <https://github.com/dandavison/delta>

### 安装

```bash
# macOS
brew install git-delta
```

### Git

```bash
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
git config --global delta.side-by-side true
git config --global delta.line-numbers true
git diff
```

### SVN

创建脚本 `svndelta`：

```bash
#!/bin/bash
diff -u "$6" "$7" | delta
```

配置：

```bash
# ~/.subversion/config
[helpers]
diff-cmd = /path/to/svndelta
```

## icdiff

- GitHub: <https://github.com/jeffkaufman/icdiff>

### 安装

```bash
# macOS
brew install icdiff

# pip
pip install icdiff
```

### Git

```bash
git config --global icdiff.options '--highlight --line-numbers'
git difftool --extcmd icdiff
```

### SVN

```bash
svn diff --diff-cmd icdiff
```

## colordiff

### 安装

```bash
# Ubuntu/Debian
sudo apt install colordiff

# macOS
brew install colordiff
```

### Git

```bash
git config --global alias.dic "diff --color"
git dic
```

### SVN

```bash
# ~/.subversion/config
[helpers]
diff-cmd = colordiff

# 或临时使用
svn diff --diff-cmd colordiff
```

## ydiff

- GitHub: <https://github.com/ymattw/ydiff>

### 安装

```bash
pip install ydiff
```

### Git

```bash
ydiff -s    # 代替 git diff
ydiff -ls  # 代替 git log
```

### SVN

```bash
svn diff | ydiff -s
```

## difftastic

- GitHub: <https://github.com/Wilfred/difftastic>

基于语法树的 diff 工具，语法感知。

### 安装

```bash
# macOS
brew install difftastic

# 其他系统
# 从 GitHub releases 下载
```

### Git

```bash
git config --global core.pager difftastic
git config --global diff.external difftastic
git diff
```

### SVN

创建脚本 `svndifft`：

```bash
#!/bin/bash
difft "$6" "$7"
```

配置：

```bash
# ~/.subversion/config
[helpers]
diff-cmd = /path/to/svndifft
```

## Kaleidoscope

macOS 专业的 diff 和 merge 工具。

### 安装

从官网下载：https://kaleidoscope.app/

### Git

在 Kaleidoscope 菜单中选择 "Integration…"，选择设为默认工具。

或手动配置：

```bash
git config --global difftool.Kaleidoscope.cmd "ksdiff --partial-changeset --relative-path \"$MERGED\" -- \"$LOCAL\" \"$REMOTE\""
git config --global difftool.prompt false
git config --global diff.tool Kaleidoscope
git difftool
```

### SVN

```bash
# ~/.subversion/config
[helpers]
diff-cmd = /Applications/Kaleidoscope.app/Contents/Utilities/ksdiff

# macOS 路径
diff-cmd = /Applications/Kaleidoscope.app/Contents/MacOS/ksdiff
```

## Beyond Compare

跨平台的 diff 和 merge 工具。

### 安装

从官网下载：https://www.scootersoftware.com/

### Git

```bash
# macOS
git config --global diff.tool bcomp
git config --global difftool.bcomp.cmd "/usr/local/bin/bcomp \"$LOCAL\" \"$REMOTE\""
git config --global difftool.prompt false

# Windows
git config --global diff.tool bc
git config --global difftool.bc.path "C:/Program Files/Beyond Compare 5/bcomp.exe"

git difftool
```

### SVN

创建脚本 `bcompare_svn`：

```bash
#!/bin/bash
/usr/local/bin/bcompare "$6" "$7" &
exit 0
```

配置：

```bash
# ~/.subversion/config
[helpers]
diff-cmd = /path/to/bcompare_svn
```

## Meld

开源的跨平台 diff 工具。

### 安装

```bash
# macOS
brew install meld

# Ubuntu/Debian
sudo apt install meld
```

### Git

```bash
git config --global diff.tool meld
git config --global difftool.meld.cmd "meld \"$LOCAL\" \"$REMOTE\""
git difftool
```

### SVN

```bash
# ~/.subversion/config
[helpers]
diff-cmd = meld

# 或临时使用
svn diff --diff-cmd meld
```

## VS Code

### 安装

下载：https://code.visualstudio.com/

### Git

安装扩展 "Meld Diff" 或其他 diff 扩展。

### SVN

安装扩展后使用扩展的 SVN 集成。

## Others

### diffs.com

- <https://diffs.com>

专门来渲染 diffs 的界面，语法高亮基于 Shiki，而且可定制性很强，我觉得非常漂亮，如果大家有类似需求，比如渲染一些 diffs 界面就可以用这个。

### diff-highlight

Git 自带的 diff 高亮工具。

```bash
git config --global core.pager "diff-highlight | less"
```
