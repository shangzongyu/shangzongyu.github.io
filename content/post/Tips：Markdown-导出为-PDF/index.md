---
title: 'Tips: Markdown 导出为 PDF'
description: '我现在写文档使用 Markdown 进行编写，有时候需要文档发送给其他人，如果对方是程序员还好，如果不是他们不懂 Markdown，如果文档里面包含图片，对他们就相当于用不了。'
slug: markdown-pdf
date: 2024-01-08 10:07:22+0000
image: cover.jpg
tags:
    - markdown
    - pdf
weight: 1
---


我现在写文档使用 Markdown 进行编写，有时候需要文档发送给其他人，如果对方是程序员还好，如果不是他们不懂 Markdown，如果文档里面包含图片，对他们就相当于用不了。

## 使用编辑器

最简单的方式就是使用 Typora、VSCode 可以使用插件 [Markdown PDF](https://open-vsx.org/vscode/item?itemName=yzane.markdown-pdf) 这种编辑器直接进行导出就可了，当然还要有另外一种方法，使用命令行 `pandoc` 进行转换。

## 使用 pandoc

Pandoc 是一个进行文档转换的工具，可以转换很多种文档，当然也包括把 Markdown 转为 PDF，使用如下命令就可以把 Markdown 文档转换为 PDF 文档：

```sh
pandoc -o output.pdf input.md
```

> PS：前提是已经安装了 Pandoc，如果没有安装使用 `brew install pandoc` 进行安装

这样导出如果是英文没有任何问题，如果有中文则会报错，类似的报错内容如下：

```
Error producing PDF.
! LaTeX Error: Unicode character 转 (U+8F6C)
               not set up for use with LaTeX.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.97 Pdf}
```

### 分析问题

Pandoc 把 Markdown 转为 PDF 文件，实际有两步：

1. 把 Markdown 文件转换为 Latex 文件
2. 调用系统的 `pdflatex`，`xelatex` 或者其他 TeX 命令，将 `.tex` 文件转换为最终的 PDF 文件

Pandoc 默认使用的 `pdflatex` 命令无法处理 Unicode 字符，如果要把包含中文、引用、表格或者其他比较复杂的格式的 Markdown 文件转为 PDF，在生成 PDF 的过程中会报错。

### 解决问题

使用 `xelatex` 来处理中文，而且还需要使用 `CJKmainfont` 指定支持中文的字体。

可以使用以下的命令生成 PDF 文件：

```sh
pandoc --pdf-engine=xelatex -V CJKmainfont="LXGW WenKai Mono" test.md -o test1.pdf
```

如果直接执行上面的命令会报错，因为 `xelatex` 没有安装，接下来我们来安装 `xelatex`。

`xelatex` 可以用各种 latex 集成包来安装使用，例如 texlive 等。这里使用 [tinytex](https://yihui.org/tinytex/) 这个包，这个包简单小巧。

> 如果之前有安装过 textlive 相关的包，需要删除，不然会有冲突。

安装：

```sh
curl -sL "https://yihui.name/gh/tinytex/tools/install-unx.sh" | sh
```

安装成功后，我们还需要安一些扩展，执行如下命令：

```sh
tlmgr install unicode-math filehook xecjk xltxtra realscripts fancyhdr lastpage ctex ms cjk ulem environ trimspaces zhnumber collection-fontsrecommended bookmark
```

扩展安装成功后，执行命令就可以把 Markdown 文档转换为 PDF 文档了。

### 技巧

介绍一些小技巧。

### 如何批量转换

介绍两个方法：

1. 使用 Shell 脚本
2. 使用 Python 脚本

#### Shell 脚本

```sh
#!/usr/bin/env bash

DIR="."
if [[ $# == 1 ]]; then
  DIR=$1
fi

echo "Your Process Dir is: ${DIR}"

FILES=$(ls "${DIR}")

for FILE in $FILES; do
  FILENAME=$(basename -- "$FILE")
  EXT="${FILENAME##*.}"
  FILENAME="${FILENAME%.*}"
  if [[ ${EXT} == "md" ]]; then
    echo "${DIR}/${FILENAME}"
    pandoc --pdf-engine=xelatex -V mainfont='LXGW WenKai Mono' "${DIR}/${FILENAME}".md -o "${DIR}/${FILENAME}".pdf
  fi
done
```

#### Python 脚本

```py
from pathlib import Path
import os

work_dir = Path.cwd()

export_pdf_dir = work_dir
if not export_pdf_dir.exists():
    export_pdf_dir.mkdir()

for md_file in list(work_dir.glob("*.md")):
    md_file_name = md_file.name
    pdf_file_name = md_file_name.replace(".md", ".pdf")
    pdf_file = export_pdf_dir / pdf_file_name
    cmd = "pandoc '{}' -o '{}' --pdf-engine=xelatex -V mainfont='LXGW WenKai Mono'".format(
        md_file, pdf_file
    )
    os.system(cmd)
```

### 文档添加标题、作者等信息

Pandoc 支持 [YAML](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block) 格式的 Header，在文件的最前面添加 YAML 格式内容，如下：

```yaml
---
title: 我的中文文档
author: shine
date: 2024-01-08
---
```

### block quote、table 以及 list 没有正确渲染

Pandoc 渲染 block quote、table 以及 list 的时候，需要在它之前添加一个空行。

如果 block quote 中每一行渲染成 PDF 未能正确换行，所有行的文字都跑到了一行，可以通过强制在原 block quote 的每一行后面加上空格来解决这个。

### block code 添加 highlight

Pandoc 支持给 block code 加上背景高亮，并提供了不同的主题，而且支持了非常多的语言。要列出 Pandoc 提供的高亮方案，使用下面命令，

```sh
# 列出 Pandoc 提供的高亮方案
pandoc --list-highlight-styles

# 要列出所有支持的语言
pandoc --list-highlight-languages
```

要使用语法高亮，Markdown 文件中的 block code 必须指定语言，同时在命令行使用 `--highlight-style` 选项，例如：

```sh
pandoc --pdf-engine=xelatex --highlight-style zenburn test.md -o test.pdf
```

### 给 section 添加编号以及整个文档添加目录

默认情况下，生成的 PDF 不含目录，同时各级标题不含编号，仅仅字体大小有变化。

- `-N` 给各个 section 加上编号
- `--toc` 加上目录

```sh
pandoc --pdf-engine=xelatex --toc -N -o test.pdf test.md
```

## FAQ

### 中文字体选择

`CJKmainfont` 后面跟的是支持中文的字体名称。如何找到支持中文的字体呢，

- 首先，需要知道所使用的语言的 `language code`，例如，中文 (即 Chinese) 的 `language code` 是 zh
- 然后使用 `fc-list` 命令查看支持系统安装的中文字体

    ```sh
    fc-list :lang=zh # zh 是中文的 「language code」
    ```

### ``! LaTeX Error: File ` bookmark.sty' not found.`

完整错误如下：

```
Error producing PDF.
! LaTeX Error: File `bookmark.sty' not found.

Type X to quit or <RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
<read *> 
         
l.94 \IfFileExists
```

使用 `tlmr` 安装缺失的 bookstyle，如下：

``````
lmgr install bookmark
``````

### 如果使用 Pandoc 的版本小于 2.0

在 Pandoc 2.0 版本之后，原有的 `--pdf-engine` 被 `--latex-engine` 取代了，因此要使用如下命令：

```sh
pandoc --latex-engine=xelatex -V mainfont='LXGW WenKai Mono' test.md -o test.pdf
```

## 参考文档

- [纯文本做笔记 --- 使用 Pandoc 把 Markdown 转为 PDF 文件](https://jdhao.github.io/2017/12/10/pandoc-markdown-with-chinese/)
- <https://blog.kelu.org/tech/2022/03/09/pandoc-md-to-pdf-with-chinese-charator.html>
- [如何把 Markdown 文件批量转换为 PDF](https://sspai.com/post/47110)
