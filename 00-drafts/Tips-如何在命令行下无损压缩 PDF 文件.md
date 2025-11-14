- 系统：macOS
- 工具：ghostscript

## 工具介绍

- **核心功能 ​**​：通过调整参数实现 PDF 压缩，支持多种压缩级别，兼容性好。
- ​**​ 无损压缩方法 ​**​：  
  使用`-dPDFSETTINGS=/printer`或`/prepress`参数，保留高分辨率图像和字体嵌入，避免降低文本清晰度
- ​**​ 优势 ​**​：开源免费，支持跨平台（Windows/Linux/Mac），可批量处理

> ​**​ 注意 ​**​：需安装 Ghostscript 工具，压缩率较低但质量无损。

## 安装

```sh
# 安装工具
brew install ghostscript
```

## 使用

```sh
# 基本使用
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

## 封装脚本

```sh
#!/bin/bash

# 功能：基于Ghostscript实现PDF无损压缩，输入输出文件通过参数传递
# 用法：./compress_pdf.sh input.pdf output.pdf
# 作者：根据需求修改
# 日期：2025年5月6日

# 参数校验
if [ $# -lt 2 ]; then
    echo "错误：参数不足！"
    echo "正确用法：$0 <输入文件> <输出文件>"
    exit 1
fi

# 输入文件存在性检查
if [ ! -f "$1" ]; then
    echo "错误：输入文件 $1 不存在！"
    exit 1
fi

# 核心压缩命令[1,2](@ref)
gs -sDEVICE=pdfwrite \
   -dCompatibilityLevel=1.4 \
   -dPDFSETTINGS=/printer \
   -dNOPAUSE \
   -dQUIET \
   -dBATCH \
   -sOutputFile="$2" \
   "$1"

# 执行结果验证
if [ $? -eq 0 ]; then
    echo "压缩完成：输出文件已保存为 $2"
else
    echo "错误：压缩过程中断，请检查输入文件格式和权限"
fi
```

### **核心功能解析 ​**​

​**​ 参数传递机制 ​**​

- `$0`：脚本自身名称（如`compress_pdf.sh`）
- `$1`：第一个参数（输入文件路径）
- `$2`：第二个参数（输出文件路径）
- `$#`：参数总数校验（必须 ≥2）

### **Ghostscript 参数说明 ​**​

| 参数                       | 功能描述                               |
| -------------------------- | -------------------------------------- |
| `-sDEVICE=pdfwrite`        | 指定输出为 PDF 格式                    |
| `-dCompatibilityLevel=1.4` | 兼容 Adobe Acrobat 5.0 及以上版本      |
| `-dPDFSETTINGS=/printer`   | 打印机优化预设（保留 300dpi 图像质量） |
| `-dNOPAUSE -dBATCH`        | 非交互式批处理模式                     |
| `-dQUIET`                  | 抑制控制台输出                         |

### **增强功能建议 ​**​

1. ​**​ 批量处理扩展 ​**​

   ```sh
       # 遍历目录下所有PDF
   for file in *.pdf; do
       ./compress_pdf.sh "$file" "compressed_${file}"
   done
   ```

```

2. ​**​日志记录功能​**​


```

exec > >(tee -a compress.log) 2>&1 # 重定向输出到日志文件

```

3. ​**​进度提示（需安装pv工具）​**​

```

gs [参数列表] | pv -petr > "$2"

```

```