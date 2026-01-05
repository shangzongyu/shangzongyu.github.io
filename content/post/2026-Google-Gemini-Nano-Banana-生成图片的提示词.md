---
title: "Google Gemini Nano Banana 生成图片的提示词"
description: 
date: 2026-01-05T09:42:57+08:00
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_2026-Google-Gemini-Nano-Banana-%E7%94%9F%E6%88%90%E5%9B%BE%E7%89%87%E7%9A%84%E6%8F%90%E7%A4%BA%E8%AF%8D-cover.webp
math: 
license: 
hidden: false
comments: true
tags:
  - AI
  - Prompt
weight: 1
---

>  主要收集一些生成图片的 Prompt。

## 九宫格 - 海马体精致写真

>  来源：<https://x.com/msjiaozhu/status/2004194584797315341?s=12>

### 女生版

```json
{
  "project_settings": {
    "task_type": "Single_Image_Contact_Sheet (9-Grid)",
    "aspect_ratio": "3:4",
    "resolution_mode": "High / Upscale (Crucial for face details in grids)",
    "batch_size": 1
  },
  "reference_config": {
    "usage": "Upload Reference Image -> Set Strength to 0.5-0.7",
    "purpose": "Define the 3x3 grid structure and character identity"
  },
  "prompt_payload": {
    "structure_trigger": "A single contact sheet image containing a 3x3 photo grid matrix",
    "grid_logic": "9 distinct panels separated by thin white borders",
    "subject_consistency": "Same young asian woman in all 9 panels, identical outfit, identical hairstyle",
    "expression_variation": "9 different facial expressions (winking, tongue out, surprised, laughing, serious, etc.)",
    "camera_angles": "Varied angles in each panel (high angle, low angle, straight on)",
    "visual_style": "Photorealistic, Studio lighting, Light grey background, K-pop idol photocard style"
  },
  "negative_prompt": [
    "One single portrait",
    "merged bodies",
    "distorted grid lines",
    "missing panels",
    "cartoon",
    "illustration",
    "different clothes"
  ]
}
```

使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-00.webp)

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_Gemini_Generated_Image_a0d80la0d80la0d8.webp)

### 男生版

```json
{
  "project_settings": {
    "task_type": "Single_Image_Contact_Sheet (9-Grid)",
    "aspect_ratio": "3:4",
    "resolution_mode": "High / Upscale (Crucial for face details in grids)",
    "batch_size": 1
  },
  "reference_config": {
    "usage": "Upload Reference Image -> Set Strength to 0.5-0.7",
    "purpose": "Define the 3x3 grid structure and character identity"
  },
  "prompt_payload": {
    "structure_trigger": "A single contact sheet image containing a 3x3 photo grid matrix",
    "grid_logic": "9 distinct panels separated by thin white borders",
    "subject_consistency": "Same young asian woman in all 9 panels, identical outfit, identical hairstyle",
    "expression_variation": "9 different facial expressions (winking, tongue out, surprised, laughing, serious, etc.)",
    "camera_angles": "Varied angles in each panel (high angle, low angle, straight on)",
    "visual_style": "Photorealistic, Studio lighting, Light grey background, K-pop idol photocard style"
  },
  "negative_prompt": [
    "One single portrait",
    "merged bodies",
    "distorted grid lines",
    "missing panels",
    "cartoon",
    "illustration",
    "different clothes"
  ]
}
```



使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-01.webp)

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_Gemini_Generated_Image_kdwlodkdwlodkdwl.webp)

> PS: 生成图片不是分享有可能因为我给的图片分辨率不高。

### 男生版 - 纯素版本

```json
{
  "project_type": "9-Grid High-Fidelity Portrait Contact Sheet",
  "aspect_ratio": "3:4",
  "visual_style": {
    "background": "Textured light gray wall, Concrete studio background, Minimalist, High-end grey tone",
    "lighting": [
      "Cinematic studio lighting",
      "Soft butterfly light",
      "High-key photography (bright but not washed out)",
      "Dimensional shadows"
    ],
    "mood": "Celebrity editorial, Cool, Atmospheric, High-fashion, Charismatic"
  },
  "subject_description": {
    "identity_consistency": "Strictly preserve original facial features and hairstyle (Identity First)",
    "styling": "Keep original styling or simple high-end black t-shirt/turtleneck",
    "hair": "Same hairstyle as reference photo (to ensure maximum face consistency)",
    "variations": [
      "Subtle micro-expressions",
      "Slight head tilt left/right",
      "Eyebrow raise",
      "Confident smirk",
      "Cold serious stare",
      "Looking down arrogantly",
      "Looking sideways",
      "Winking",
      "Laughing naturally"
    ]
  },
  "composition": {
    "layout": "3 columns x 4 rows (12 panels), Contact sheet format, Neat arrangement",
    "framing": "Uniform headshots, Shoulder level"
  },
  "technical_specs": {
    "camera": "Hasselblad X1D",
    "film_look": "Black and white, Fine grain, Sharp details"
  },
  "negative_prompt": [
    "Changing hairstyle",
    "Different person",
    "Distorted features",
    "Messy layout",
    "Dark black background",
    "Pure white background"
  ]
}
```

使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-01.webp)

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_Gemini_Generated_Image_9vukjs9vukjs9vuk.webp)