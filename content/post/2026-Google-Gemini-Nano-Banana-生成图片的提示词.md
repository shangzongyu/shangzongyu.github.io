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

## 九宫格

### 冬日搞怪九宫格人像（同脸九连拍）

```json
Create a 3x3 grid of playful winter portraits featuring the person from the attached image in all nine frames. Each frame shows a different expression, hairstyle, and outfit — funny, awkward, joyful, bored, mischievous, over-the-top.  The vibe is childlike, spontaneous, and imperfect, like a creative winter photoshoot done just for fun. Solid winter-toned backgrounds (cool blue, grey, off-white, muted beige). Styling varies between frames: messy beanies, scarves, ear warmers, oversized coats, fuzzy sweaters, layered winter textures, quirky glasses, exaggerated bed-hair, slightly wet hair from snow. Some frames include tongue out, wide smile, surprised face, mock-serious look, squinting from cold. Lighting is soft studio with a cool-neutral tone, visible grain, slight texture, no polish. The grid feels cohesive but intentionally chaotic and playful — winter mood without holiday symbolism. The face must remain 100% identical in all 9 frames.
```

使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-00.webp)

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8622.webp)

### 九宫格 - 海马体精致写真

>  来源：<https://x.com/msjiaozhu/status/2004194584797315341?s=12>

#### 女生版

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

#### 男生版

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

#### 男生版 - 纯素版本

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

## Charli D'amelio

```json
{
  "main_prompt": "A candid high-angle full-shot of a young woman reclining on a messy bed, wearing a black zip-up hoodie and white crew socks, leaning her head on her hand with a bored or contemplative expression. The bed has cream-colored textured sheets and a wooden headboard. Scattered in the foreground are a brown leather vest, a patterned silk scarf, and a black Prada water bottle. The lighting is soft and warm with a vintage film grain aesthetic.",
  "subject_details": {
    "appearance": "Young woman, long dark straight hair, fair skin tone.",
    "expression": "Contemplative, slightly bored, neutral gaze, resting cheek on right hand.",
    "pose": "Reclining on back, legs extended but relaxed, body angled slightly diagonally across the bed."
  },
  "apparel": {
    "upper_body": "Black long-sleeve zip-up hooded sweatshirt, slightly cropped or tucked.",
    "lower_body": "Black fitted shorts or bodysuit (barely visible), white ribbed crew socks pulled up."
  },
  "environment": {
    "setting": "Bedroom, messy unmade bed.",
    "background": "Wooden mid-century modern headboard, large cream-colored pillows, a beige sweater draped carelessly over the background pillow.",
    "surfaces": "Textured white or cream bedspread (waffle weave or wrinkled cotton)."
  },
  "props_and_clutter": {
    "foreground_items": [
      "Brown vintage leather vest or corset top",
      "Folded silk scarf with polka dot and floral pattern",
      "Black insulated water bottle with white logo text (Prada style)"
    ]
  },
  "technical_aspects": {
    "camera_angle": "High-angle shot, looking down at the subject (approx 45 degrees or overhead).",
    "lighting": "Soft ambient indoor light, possibly mixed with a direct on-camera flash for a 'snapshot' look.",
    "style": "Candid, lifestyle photography, film grain, vintage 90s aesthetic, soft focus.",
    "color_palette": "Muted earth tones, cream, beige, black, and brown."
  }
}
```

使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-00.webp)

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8623.webp)

## 茶系伪素颜

> 来源：<https://x.com/VoxcatAI/status/2013124498627912188>

当下流行的“茶系伪素颜”（Tea Style / No-Makeup Makeup）或“白开水妆容”（Clean Girl Aesthetic）。

这种妆容的核心在于“原生感”和“通透感”，给人一种天生皮肤好、气色佳的错觉，看似清淡，实则在细节上非常考究。

### 1. 底妆：强调“微光泽”与“呼吸感”

- 特点： 并不是完全的哑光，也不是油腻的水光，而是像陶瓷或刚剥壳鸡蛋一样的半哑光奶油肌。
- 细节：
	- 轻薄遮瑕： 保留了皮肤的一点点质感（甚至轻微的毛孔或痣），没有假面感。
	- 高光点缀： 重点在面中、鼻尖、唇峰和眉骨处有明显的光泽感（Highlight），让面部立体饱满。
	- 色调： 偏向中性或暖调的象牙白，与颈部肤色自然衔接。

### 2. 眉妆：强调“毛流感” (野生眉)

- 特点： 几张图中的眉毛都非常自然，没有生硬的边框。
- 细节：
    - 根根分明： 眉头部分的眉毛向上梳理，强调一根一根的真实毛发感（Wild Brows）。
    - 颜色： 眉色比发色浅一号或保持一致（灰棕色为主），显得温柔不压抑。
    - 形状： 顺着原本的眉骨走势，稍作延长，带有轻微的弧度，不刻意强调眉峰。

### 3. 眼妆：做减法，重神采

- 特点： 弱化眼影颜色，强调睫毛和眼神光。
- 细节：
    - 眼影： 几乎看不出明显的眼影色块，主要使用低饱和度的大地色（杏色、奶茶色）大面积铺底，主要为了消肿和加深轮廓，而非显色。
    - 眼线： 极细的内眼线（Tightline），通常只画到眼尾稍微拉出一点点，或者干脆只填充睫毛根部，让眼睛看起来有神即可。
    - 睫毛： 强调“太阳花”效果，睫毛夹得很翘，根根分明，没有苍蝇腿，也没有浓密的假睫毛感。

### 4. 腮红与修容：营造“氛围感”

- 特点： 腮红面积较大，与修容融合，打造自然好气色。
- 细节：
	- 色系： 主要是收敛色，如裸杏色、干枯玫瑰色、奶油橘色。
	- 位置： 并没有打在苹果肌正中央，而是稍稍向侧面颧骨延伸。

### 5. 唇妆：主打“水光嘟嘟唇”

- 质地： 使用镜面唇釉、唇蜜或滋润型口红。
- 颜色： 低饱和度色系，如肉桂色、裸米色、冰透茶色、浅豆沙色（MLBB - My Lips But Better）。
- 模糊唇线： 唇周边缘晕染开，弱化唇峰的锐利感，看起来更加年轻、无辜且亲和力强。
- 整体风格：

    - 清冷感 (Cool/Detached): 表情管理配合妆容，带有一种疏离但高级的美感。
    - 氧气感 (Oxygen/Fresh): 干净、通透，没有攻击性。
    - 高级灰/低饱和 (Low Saturation): 全脸没有高亮度的色彩，色彩统一和谐。
- 适用场景：这种妆容非常适合日常通勤、约会、证件照以及时尚杂志的特写拍摄，因为它耐看且能最大程度凸显个人的五官底子。

### 典型的 Promot 如下

```
A hyper-realistic editorial portrait close-up of [角色名称/Subject], . [角色标志性外貌特征]. The focus is sharply on facial features and pre-defined "pseudo-no-makeup" details:

【底妆与肤质】
clear creamy skin, thin and transparent foundation, moist hydrating feel, "born-with-it" perfection, deceptive no-makeup look.

【眼部与眉毛】
Eyes: barely-there eyeshadow (sheer apricot/flesh pink base), lashes brushed out but restrained, innocent gaze.
Brows: natural flow brows, pale soft color, NOT rigid, fluffy "born-with-it" texture.

【唇部与高光】
Lips: nude bean paste color, mirror-like tinted lip balm, soft blurred edges, tender and juicy.
Highlight: balm-like wet highlights on cheekbones (moisturizing glow), subtle pale peach blush (low presence).

【环境与拍摄】
Lighting: soft high-key aesthetic, clean and ethereal, fairy-like atmosphere.
Camera: High-resolution photography, 85mm portrait lens, f/2.0.

【约束 / Constraints & Negative】
no heavy makeup, no sharp contouring, no thick eyeliner, no matte finish, no dark eyeshadow, no aggressive features.
```

### Promot 

```json
A hyper-realistic editorial portrait close-up of [贾静雯], . [青春]. The focus is sharply on facial features and pre-defined "pseudo-no-makeup" details:

【底妆与肤质】
clear creamy skin, thin and transparent foundation, moist hydrating feel, "born-with-it" perfection, deceptive no-makeup look.

【眼部与眉毛】
Eyes: barely-there eyeshadow (sheer apricot/flesh pink base), lashes brushed out but restrained, innocent gaze.
Brows: natural flow brows, pale soft color, NOT rigid, fluffy "born-with-it" texture.

【唇部与高光】
Lips: nude bean paste color, mirror-like tinted lip balm, soft blurred edges, tender and juicy.
Highlight: balm-like wet highlights on cheekbones (moisturizing glow), subtle pale peach blush (low presence).

【环境与拍摄】
Lighting: soft high-key aesthetic, clean and ethereal, fairy-like atmosphere.
Camera: High-resolution photography, 85mm portrait lens, f/2.0.

【约束 / Constraints & Negative】
no heavy makeup, no sharp contouring, no thick eyeliner, no matte finish, no dark eyeshadow, no aggressive features.
```

## Ana de Armas in a unique style 

```json
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the main focal point, with her confident stance drawing attention. The background is softly blurred to create depth, allowing the subject to stand out while still incorporating the beauty of the Roman backdrop."
      },
      "depth_of_field": {
        "foreground": "Sharp focus on the subject, capturing the outfit's details, facial features, and texture of the fabric.",
        "background": "Softly blurred architecture, providing contrast and allowing the subject to remain the center of attention."
      }
    },
    "mood_and_theme": {
      "style": "Luxury travel fashion",
      "emotion": "Confident femininity, elegance, and empowerment. The subject's posture and gaze convey a sense of strength and poise, blending seamlessly with the luxurious setting."
    }
  }
```

使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-00.webp)

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8627.webp)

## 3D avatar

```json
Create a high-quality 3D avatar of the person in the uploaded image with a cheerful, expressive face. The character should have a warm smile, bright eyes, and soft facial features that feel friendly and approachable. Render in a Pixar-style aesthetic with smooth textures, subtle skin shading, and slightly exaggerated proportions for a cute, animated look. Lighting should be soft and even, creating a clean studio look with gentle shadows for depth.
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8631.webp)

## 奶凶

这个表情很有意思，它不是五官动作的简单叠加，而是一种情绪语义。

最开始我用嘟嘴+皱眉+生气来描述，模型会往真生气/凶这个方向跑，但加上“对男朋友撒气、被拍烦了”的叙事，就把它拉回到“凶但可爱、带撒娇的对抗”这种feel，很微妙，希望对你有所启发。

```json
Photorealistic edit using the input person photo as strict identity reference: keep the same face, facial features, skin tone, hairstyle (color/bangs/length/volume), outfit and accessories unchanged (no face swap, no new person, no hair/outfit change). Change only expression/pose/background: pouty lips and furrowed brows, slightly angry/annoyed, like she’s playfully mad at her boyfriend and saying “stop filming me”. Close wide-angle perspective (18–28mm), body slightly leaning forward, one hand reaching toward the lens as if grabbing the boyfriend’s phone / blocking the camera; huge foreground hand occupying 30–50% of the frame, palm facing camera, five natural fingers, realistic anatomy; face in the back in sharp focus. Replace background with a clean solid pink studio backdrop (seamless, no texture). No text, no watermark, no frame, no extra fingers, no deformed hands, no heavy blur, no style change.
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8642.webp)

## Others

使用原图为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260105_nano-banana-00.webp

### 1

```json
{
  "style": "ultra-realistic studio portrait",
  "subject": {
    "gender": "female",
    "age": "young adult",
    "pose": "leaning slightly forward toward the camera",
    "expression": "playful, flirty",
    "facial_details": {
      "wink": true,
      "tongue_out": true,
      "freckles": "natural across fair skin",
      "makeup": {
        "blush": "soft pink",
        "lips": "glossy"
      }
    },
    "hair": {
      "color": "brunette",
      "length": "long",
      "part": "side-parted",
      "style": "falling naturally over shoulders"
    },
    "outfit": {
      "dress": "off-shoulder fitted black dress",
      "jewelry": {
        "earrings": "long dangling gold earrings",
        "necklaces": "layered gold necklaces with small heart pendant"
      }
    }
  },
  "environment": {
    "setting": "studio",
    "background": "clean minimal light neutral tones"
  },
  "lighting": {
    "type": "soft diffused studio lighting",
    "shadows": "smooth natural shadows"
  },
  "camera": {
    "lens": "50mm",
    "aperture": "f/1.8",
    "depth_of_field": "shallow"
  },
  "quality": {
    "resolution": "high resolution",
    "detail": "ultra-detailed",
    "skin_texture": "photorealistic",
    "focus": "sharp focus",
    "photography_style": "high fashion lifestyle photography"
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8640.webp)

### 2

```json
{
  "style": "ultra-realistic studio portrait",
  "subject": {
    "gender": "female",
    "age": "young adult",
    "pose": "leaning slightly forward toward the camera",
    "expression": "playful, flirty",
    "facial_details": {
      "wink": true,
      "tongue_out": true,
      "freckles": "natural across fair skin",
      "makeup": {
        "blush": "soft pink",
        "lips": "glossy"
      }
    },
    "hair": {
      "color": "blonde",
      "length": "long",
      "part": "side-parted",
      "style": "falling naturally over shoulders"
    },
    "outfit": {
      "dress": "off-shoulder fitted black dress",
      "jewelry": {
        "earrings": "long dangling gold earrings",
        "necklaces": "layered gold necklaces with small heart pendant"
      }
    }
  },
  "environment": {
    "setting": "studio",
    "background": "clean minimal light neutral tones"
  },
  "lighting": {
    "type": "soft diffused studio lighting",
    "shadows": "smooth natural shadows"
  },
  "camera": {
    "lens": "50mm",
    "aperture": "f/1.8",
    "depth_of_field": "shallow"
  },
  "quality": {
    "resolution": "high resolution",
    "detail": "ultra-detailed",
    "skin_texture": "photorealistic",
    "focus": "sharp focus",
    "photography_style": "high fashion lifestyle photography"
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8641.webp)

### 3

```json
{
  "prompt_type": "descriptive_portrait",
  "subject_details": {
    "demographics": "Young female, fair smooth skin, fit and athletic build, strictly matching the reference photo.",
    "facial_features": {
      "expression": "Pouting in anger, a smudge of white flour on her nose and cheek, playful and messy yet attractive, facial expression matching the reference photo.",
      "eyes": "Bright eyes, aligned with the reference photo angle.",
      "hair": "Slightly messy short-to-medium hair, casually styled, exactly following the reference photo hairstyle."
    },
    "apparel": {
      "dress": "Plain pink t-shirt fitting exactly like the reference photo pose, paired with tiny pajama shorts.",
      "accessories": "None.",
      "footwear": "Barefoot."
    }
  },
  "pose_and_action": {
    "body_position": "Leaning over the kitchen island counter, elbows resting on the surface, body position strictly following the reference photo.",
    "hands": "Hands lightly dusted with flour. Pointing one finger at the camera side"
  },
  "background_environment": {
    "location": "Messy kitchen.",
    "lighting_source": "Bright overhead kitchen lights.",
    "objects": {
      "details": "Bowl of dough, scattered flour on the counter, cracked eggshells."
    }
  },
  "technical_specs": {
    "style": "Playful, domestic, ultra-realistic, high detail on natural skin texture and flour dust, strict adherence to the reference photo for realism.",
    "aspect_ratio": "4:5"
  },
  "constraints": [
    "Preserve facial identity exactly as in the reference image",
    "No facial reshaping or beautification",
    "No artificial filters or stylization",
    "Maintain natural proportions and lighting"
  ],
  "output_goal": "Create a playful, ultra-realistic mirror selfie portrait of a young woman in a messy kitchen, laughing naturally with flour on her face, perfectly matching the reference photo in pose, expression, and identity."
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8644.webp)

### 4

```json
将此图片转换为64K数码单反分辨率的创意都市街头肖像。

[主体]：照片中，一位**[从上传图片提取：年龄、性别、外貌特征]**（与上传图片中的人物相同）坐在静谧的城市街道路边。人物随意地坐在水泥人行道边缘，一只手托着下巴，姿态略显百无聊赖，若有所思。表情平静内敛，流露出静谧的沉思感。

[装束]：身穿**[提取自图片或使用模板：浅酒红色宽松绞花针织衫，搭配深色牛仔裤和做旧皮靴]**。

[卡通伴侣]：在他/她旁边的人行道上，坐着一个卡通版的自己（与上传的图片脸部特征一致）。卡通人物的穿着、打扮、姿势甚至表情都与真人一模一样。卡通风格线条简洁，色彩温暖，采用柔和的手绘动画风，与写实真人形成有趣对比。

[技术与环境]：背景是纹理丰富的鹅卵石路面和柔和黄色的建筑立面。大地色系为主，柔和自然光。融合街头摄影与混合媒介艺术，Octane渲染器，虚幻引擎级画质。
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8645.webp)

### 5

```json
{
  "prompt": {
    "subject": {
      "description": "A collection of five vintage Polaroid instant photographs featuring the same young Asian woman, arranged casually on a textured surface.Use the face without any change",
      "appearance": {
        "hair": "Wavy, black hair.",
        "skin": "smooth and fair skin.",
        "makeup": "Natural, dewy makeup with defined brows and neutral lip color.",
        "clothing": "Black tank top.",
        "accessories": "Gold pendant necklaces."
      },
      "poses": [
        {
          "photo": "Top left",
          "description": "Winking, sticking out tongue, making a peace sign."
        },
        {
          "photo": "Top right",
          "description": "Blowing a kiss."
        },
        {
          "photo": "Center",
          "description": "Looking off-camera, hand on cheek."
        },
        {
          "photo": "Bottom left",
          "description": "Making a kissy face, peace sign."
        },
        {
          "photo": "Bottom right",
          "description": "Laughing broadly, head tilted."
        }
      ]
    },
    "environment": {
      "surface": "Thick, cream-colored knit wool blanket with a textured stitch pattern.",
      "details": "Several red lipstick kiss marks imprinted directly onto the blanket fabric.",
      "arrangement": "The five Polaroid prints are scattered naturally, overlapping slightly."
    },
    "lighting": {
      "type": "Soft, overhead ambient light, likely natural daylight, illuminating the entire scene.",
      "photo_lighting": "Direct studio flash within the Polaroid photos, creating a bright, slightly overexposed look with soft shadows."
    },
    "mood": "Playful, casual, nostalgic, warm, and personal.",
    "camera_details": {
      "style": "Ultra Photorealistic overhead photograph.",
      "focus": "Sharp focus on the Polaroid prints and the textures of the blanket.",
      "perspective": "Top-down view.",
      "film_type": "Vintage Polaroid instant film with classic white borders and slight wear." Ratio 3.4
    }
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8647.webp)

### 6

```json
{
  "meta": {
      "type": "Hyper-realistic Digital Art / Photo Bash",
      "orientation_lock": "LOCKED: Orientation preserved 4:5",
      "sensor_emulation": "Virtual 85mm Portrait Lens / Soft Film Emulation"
    }
  },
  "spatial_orientation_engine": {
    "subject_facing_direction": "CAMERA (Front) with upward tilt",
    "body_rotation": "Shoulders square to camera, Head tilted back ~20 degrees",
    "camera_position_relative": "Camera is slightly below eye level, angled upwards (Low Angle Close-up)"
  },
  "camera_optics_and_geometry": {
    "lens_profile": {
      "focal_length": "85mm (Portrait)",
      "aperture": "f/2.8 (Shallow Depth of Field)",
      "lens_character": "Soft, Ethereal, Slight Diffusion"
    },
    "optical_flaws": [
      "Film Grain",
      "Soft Focus on Crown Edges",
      "Chromatic Aberration (Micro)",
      "Bloom/Haze Effect"
    ]
  },
  "environment_and_physics": {
    "lighting_engine": {
      "primary_source": "Diffused Soft Box (Top Front)",
      "radiosity_color_bleed": "CRITICAL: Pale green/cream light bouncing from veil onto neck and jawline",
      "shadow_structure": "Soft ambient occlusion under chin and nose / Low contrast",
      "volumetrics": "Slight atmospheric haze"
    },
    "surface_physics": {
      "weather_impact": "Static indoor/studio environment, no wind",
      "material_response": "Veil transparency revealing skin tone / Metallic reflection on crown frame / Subsurface scattering on skin"
    }
  },
    ]
  },
  "objects_and_actors": [
    {
      "id": "MAIN_SUBJECT",
      "role": "Identity Swap Target",
      "pose_engineering": {
        "skeletal_rig": "Cervical spine extended, chin elevated, neutral neck rotation.",
        "gaze_vector": "Eyes looking upward (away from lens, towards light source).",
        "interaction_physics": "Weight of floral crown pressing slightly on hair / Veil draped loosely over head"
      },
      "physiological_state": {
        "body_temp_visuals": "Flushed nose and cheeks (rosy tint)",
        "skin_light_interaction": "High Subsurface Scattering (SSS) on nose bridge and cheeks / Moist lips"
      },
      "clothing_simulation": {
        "garment_stack": "Base: Pale Sage/Cream Sheer Veil; Accessory: Gold/Bronze Crown with White Gypsophila (Baby's Breath) flowers",
        "fabric_mechanics": "Fabric draped with gravity, no tension, high translucency.",
        "texture_and_wear": "Fine mesh weave on veil, organic irregularity in dried flowers, metallic sheen on crown base."
      },
      "identity_placeholders": {
        "skin_tone": "[[USE_REFERENCE_SKIN]]",
        "face_structure": "[[USE_REFERENCE_FACE]]",
        "hair_style": "[[USE_REFERENCE_HAIR]]"
      }
    }
  ],
  "off_screen_context": {
    "reflections": "Soft rectangular light source reflected in pupils (Catchlights)",
    "implied_elements": "Studio lighting setup or skylight above"
  },
  "generation_keywords": {
    "positive": "Photorealistic, Portrait, Ethereal lighting, Upward gaze, Freckles, Floral crown, Baby's breath flowers, Sheer veil, Highly detailed skin texture, 8k, Soft focus",
    "negative": "Looking down, hard shadows, oversaturated, vector art, cartoon, distorted eyes"
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8648.webp)

### 7

```json
 {
      "id": 1,
      "title": "2x2 Collage: Luxury Ski Trip",
      "prompt_text": "2x2 photo collage, luxury ski influencer lifestyle. Strict face reference lock. Location: high-end ski chalet balcony (Aspen/Alps), blurred snowy mountains behind. Outfit: fitted white thermal bodysuit, white faux-fur headband, oversized Moon Boots. Natural skin texture, fresh cold girl makeup. Style: iPhone 16 Pro photo, harsh bright high-altitude winter sun, sharp shadows, strong contrast, slight lens flare, blown snow highlights. Panels: 1) Leaning on rustic wooden railing, smiling. 2) Close-up adjusting large mirrored ski goggles. 3) Sitting relaxed on snow-covered bench. 4) Rear view looking at peaks.",
      "negative_prompt": "cinema, studio light, soft diffused, DSLR, film grain, 3D, CGI, smooth skin, warm lighting, low contrast, blurry, distorted, artificial AI look",
      "aspect_ratio": "4:5"
    },
    {
      "id": 2,
      "title": "Solo: Leaning on Balcony",
      "prompt_text": "Lifestyle photo, luxury ski influencer on chalet balcony. Strict face reference lock. Leaning on wooden railing, smiling naturally. Outfit: white thermal bodysuit, white fur headband, Moon Boots. Natural skin texture, cold makeup. Background: blurred snowy mountains. Style: iPhone 16 Pro photo, harsh high-altitude winter sun, sharp shadows, high contrast, \"plandid\" look.",
      "negative_prompt": "cinema, studio light, soft diffused, DSLR, film grain, 3D, CGI, smooth skin, warm lighting, low contrast, blurry, distorted, artificial AI look",
      "aspect_ratio": "4:5"
    },
    {
      "id": 3,
      "title": "Close-up: Adjusting Goggles",
      "prompt_text": "Close-up portrait, luxury ski influencer on balcony. Strict face reference lock. Adjusting large mirrored ski goggles with both hands, elbows up, dynamic fashion pose. White outfit details visible. Style: iPhone 16 Pro photo, harsh winter sun, crisp highlights on goggles, high contrast.",
      "negative_prompt": "cinema, studio light, soft diffused, DSLR, film grain, 3D, CGI, smooth skin, warm lighting, low contrast, blurry, distorted, artificial AI look",
      "aspect_ratio": "4:5"
    },
    {
      "id": 4,
      "title": "Full Body: Sitting",
      "prompt_text": "Full-body photo, luxury ski influencer sitting on snow-covered bench on chalet balcony. Strict face reference lock. Relaxed posture, looking off-camera candidly. White outfit, Moon Boots visible. Style: iPhone 16 Pro photo, direct winter sun causing sharp shadows, bright snow glare.",
      "negative_prompt": "cinema, studio light, soft diffused, DSLR, film grain, 3D, CGI, smooth skin, warm lighting, low contrast, blurry, distorted, artificial AI look",
      "aspect_ratio": "9:16"
    }
  ]
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8649.webp)

### 8

```json
{
  "configuration": {
    "version": "2.0",
    "format": "Mirror-Selfie Portrait",
    "aspect_ratio": "4:5",
    "target_resolution": "8K UHD"
  },
  "subject_profile": {
    "biometrics": {
      "ethnicity": "Asian",
      "physique": "Curvy, hourglass silhouette",
      "facial_id": "High-fidelity, identical facial features, symmetrical",
      "skin_texture": "Realistic pores, soft matte finish"
    },
    "expression_and_gaze": {
      "mouth": "Softly parted lips",
      "eyes": "Direct eye contact via mirror, confident, calm",
      "head_angle": "Slightly turned, 15-degree tilt"
    },
    "kinematics": {
      "upper_body": "Right arm raised holding smartphone",
      "lower_body": "Left hand resting on hip/waist",
      "positioning": "Centered at eye level"
    }
  },
  "wardrobe_details": {
    "top_layer": {
      "item": "Corset top",
      "fabric": "Heavy-weight blue denim",
      "neckline": "Sweetheart",
      "accents": ["Thin spaghetti straps", "Contoured stitching", "Metal eyelets"]
    },
    "bottom_layer": {
      "item": "High-waisted denim jeans",
      "fit": "Skinny-fit, emphasizing curves",
      "wash": "Matching blue denim wash"
    }
  },
  "environment_architecture": {
    "background": {
      "primary_wall": "Smooth grey matte finish",
      "secondary_wall": "Glossy white subway tiles",
      "grout_detail": "Thin grey contrast grout"
    },
    "setting": {
      "vibe": "Clean, modern, intimate",
      "props": ["Modern smartphone", "Large high-definition bathroom mirror"]
    }
  },
  "lighting_and_optics": {
    "illumination": {
      "type": "Warm indoor ambient",
      "key_light": "Soft overhead diffuse",
      "highlights": "Specular glint on denim and tile surfaces"
    },
    "camera_simulation": {
      "lens_type": "35mm prime",
      "depth_of_field": "Shallow (slight blur on background tiles)",
      "focus": "Sharp focus on subject reflection"
    }
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8651.webp)

### 9

```json
{
  "prompt_details": {
    "subject": {
      "description": "Young woman with long, voluminous brunette hair featuring soft waves and a center part. She has almond-shaped eyes, arched brows, and defined facial features.",
      "expressions": [
        "Top: Subtle, confident smile, direct eye contact with the reflection.",
        "Bottom: Candid, joyful laughter, eyes closed, head tilted back."
      ],
      "attire": {
        "top_image": "Black high-neck sleeveless top, sophisticated and minimal.",
        "bottom_image": "Black strapless dress with subtle glittering texture (sequins or shimmer)."
      },
      "accessories": [
        "Delicate silver necklace (tennis style or similar)",
        "Thin gold/silver bracelets",
        "Rings on fingers"
      ]
    },
    "pose_and_action": {
      "type": "Mirror selfie POV.",
      "hands": [
        "Holding a wine glass filled with white wine.",
        "Holding a smartphone to capture the reflection."
      ],
      "posture": "Seated at a dining table, relaxed but elegant."
    },
    "environment": {
      "location": "Upscale, vintage-inspired restaurant or bistro.",
      "decor": [
        "Dark wood paneling",
        "Ornate mirrors reflecting the room",
        "Floral or tapestry-style wallpaper/upholstery",
        "Plush velvet seating (visible patterns)",
        "White tablecloths"
      ],
      "background_details": "Other diners softly visible in the background, vintage lamps with fringed shades."
    },
    "lighting": {
      "atmosphere": "Dim, warm, intimate evening ambiance.",
      "sources": [
        "Soft glow from vintage table lamps with warm shades",
        "Candlelight (prominent tall white candle in the bottom frame)",
        "Ambient reflection from mirrors"
      ],
      "effect": "Golden hour indoor tone, soft highlights on hair and skin, rich shadows."
    },
    "camera_and_tech": {
      "style": "Ultra Photorealistic, 8k resolution, candid lifestyle photography.",
      "camera_simulation": "Smartphone rear camera (iPhone Pro style), wide aperture (f/1.8) for depth of field.",
      "focus": "Sharp focus on the subject in the mirror reflection, soft bokeh on foreground elements (wine glass stem, candle).",
      "color_grading": "Warm, cinematic, slightly grainy low-light texture, rich contrast."
    },
    "mood": "Luxurious, festive, happy, chic, 'night out' aesthetic."
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8652.webp)

### 10

```json
{
"Refractive photography",
    "Fine art portrait"
  ],
  "photography_style": {
    "genre": "High-end fashion editorial portrait with experimental optical effects",
    "technique": "Shooting through prismatic glass and crystal elements for artistic refraction",
    "era": "Contemporary 2020s luxury fashion photography",
    "influences": "Paolo Roversi soft focus, Tim Walker whimsical elegance, Sofia Coppola period opulence"
  },
  "critical_elements_summary": {
    "must_include": [
      "Large crystal prism creating rainbow dispersion on entire left side of frame",
      "Subject visible through transparent glass table in center creating layered effect",
      "Flower arrangement right side with chromatic aberration on petals",
      "Multiple crystal chandeliers with warm candlelight creating bokeh in background",
      "Deep black background with selective lighting on subject",
      "Elaborate diamond necklace and earrings catching light",
      "Soft dreamy focus quality throughout",
      "Strong rainbow spectrum colors from prismatic refraction - full red through violet",
      "Transparent layered glass effects creating ghosting and doubling",
      "Warm amber candlelight bokeh circles scattered in background",
      "Low-key dramatic lighting with subject emerging from darkness",
      "Opulent formal ballroom atmosphere"
    ]
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8653.webp)

### 11

```json
{ "pace": "extensive surrounding empty space",
"perspective": "dramatic overhead with subject looking up"
},
"subject": {
"count": 1,
"description": "young person with glasses",
"pose": "standing upright, shoulders slightly forward, arms relaxed",
"expression": "soft, introspective, mildly curious",
"gaze": "looking directly up at the camera",
"accessories": [
"round eyeglasses"
],
"clothing": {
"outerwear": "dark brown jacket",
"innerwear": "light-colored knit or textured shirt",
"style": "casual, understated"
}
},
"facial_details": {
"features": "rounded face, soft jawline",
"emotion": "calm, thoughtful",
"eye_emphasis": "enhanced by glasses and upward gaze"
},
"lighting": {
"type": "studio lighting",
"setup": "top-centered soft light with gradual falloff",
"contrast": "low to moderate",
"shadows": "subtle shadows beneath chin and body",
"vignette": "strong radial vignette darkening toward edges"
},
"color": {
"palette": [
"cool gray",
"charcoal",
"muted brown",
"soft beige"
],
"temperature": "cool-neutral",
"saturation": "low",
"mood": "quiet, contemplative"
},
"background": {
"environment": "studio",
"surface": "smooth seamless floor",
"gradient": "radial gradient from light center to dark edges",
"distractions": "none"
},
"technical_details": {
"camera_type": "digital",
"lens": "ultra-wide or fisheye-style wide-angle",
"depth_of_field": "deep (entire subject in focus)",
"sharpness": "high center sharpness with slight edge softness",
"noise": "minimal",
"post_processing": [
"contrast shaping",
"cool color grading",
"vignette enhancement",
"perspective exaggeration"
]
},
"artistic_elements": {
"concept": "isolation and vulnerability through scale and perspective",
"visual_metaphor": "small subject surrounded by vast empty space",
"aesthetic_influences": [
"editorial portrait photography",
"modern studio minimalism",
"cinematic overhead compositions"
]
},
"typography": {
"presence": false
},
"overall_mood": "intimate, introspective, slightly surreal",
"intended_use": [
"editorial portrait",
"conceptual photography reference",
"AI image generation style guide"
]
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8654.webp)

### 12

```json
{
"Korean Idol Studio Portrait style, soft high-key lighting, pastel blue color palette, mixed media with white hand-drawn doodle overlays."
    },
    "subject_details": {
      "demographics": "Young Asian woman, 18 years old, fresh and elegant visual.",
      "styling": {
        "hair": "Long, dark brown, voluminous loose waves. Styled half-up or with a large blue ribbon accessory.",
        "outfit": "Elegant baby blue sleeveless halter-neck dress with a flowing chiffon or tulle skirt.",
        "makeup": "Fresh dewy skin, peach/pink blush, glossy lips, defined eyelashes (Idol makeup style)."
      }
    },
    "panel_breakdown": {
      "top_left_panel": {
        "framing": "Close-up Portrait.",
        "pose": "Leaning elbows on a white surface, face resting in palms ('flower pose'), squishing cheeks slightly. Looking off-camera with a cute, dreamy expression.",
        "doodles": "White scribble of a veil/tiara on head, text 'Princess', floating hearts.",
        "props": "Blue gingham patterned balloons in background."
      },
      "top_right_panel": {
        "framing": "Full Body / Wide Shot.",
        "pose": "Sitting elegantly sideways on a table covered in a white cloth. One hand touching the ribbon in hair, legs crossed at ankles. Looking at camera.",
        "props": "Small blue cake on table, blue gift boxes stacked on floor, blue gingham balloons.",
        "doodles": "Text 'Wonderful Birthday' and sparkle drawings."
      },
      "bottom_left_panel": {
        "framing": "Full Body standing.",
        "pose": "Standing straight, holding a massive, oversized blue bow prop (fashion editorial style) against her chest.",
        "doodles": "White outlines tracing the bow to emphasize the shape, motion lines.",
        "props": "Standing on a small white circular pedestal."
      },
      "bottom_right_panel": {
        "framing": "Waist-up Shot.",
        "pose": "Holding a minimalist blue birthday cake with both hands at chest level. Head tilted, looking away to the side with a bright smile.",
        "cake_details": "Blue icing, white ball decorations, text 'HAPPY BIRTHDAY' in black.",
        "doodles": "White ribbon drawn on the cake, heart shapes, text 'My Princess '."
      }
    },
    "camera_technical_values": {
      "lens": "85mm (Portrait telephoto for flattering facial features).",
      "aperture": "f/2.8 to f/4.0 (Soft background blur).",
      "shutter_speed": "1/200s.",
      "iso": "ISO 100.",
      "lighting_setup": "High-Key Studio Lighting. Bright, soft, shadowless 'beauty' light. White seamless background.",
      "tone": "Cool pastel blue tones, bright and airy."
    },
    "post_processing": {
      "overlays": "Handwritten white crayon/chalk text reading 'Wonderful Birthday', 'Princess My'. Cute doodle illustrations of stars, hearts, and ribbons."
    }
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8655.webp)

### 13

```json
{
  "meta": {
    "system_instruction": "PRIORITY: Focus strict facial identity preservation on the TWO FOREGROUND CHARACTERS (Bottom Left & Bottom Right). The other characters are secondary.",
    "aspect_ratio": "9:16",
    "quality": "high_fidelity",
    "resolution": "4k",
    "style": "viral social media photography, worm's eye view, crystal clear blue sky"
  },

  "reference_usage": {
    "instruction": "Map the uploaded face reference(s) specifically to the two girls closest to the camera (at the bottom).",
    "logic": "Bottom Left Girl = Face Ref A. Bottom Right Girl = Face Ref B (or same ref if only one provided). Top characters = Generic compatible faces.",
    "focus_weight": "Foreground: 100% Identity match; Background: 50% Vibe match"
  },

  "scene": {
    "perspective": "Extreme low angle (camera on ground looking up)",
    "background": "Pure gradient blue sky, no clouds, bright daylight",
    "composition": "5 girls forming a circle, but the bottom two are much larger and closer to the lens"
  },

  "subject_group": {
    "concept": "A group of friends looking down at the camera, framing the shot",
    
    "PRIMARY_SUBJECTS (STRICT IDENTITY LOCK)": {
      "note": "These two must look exactly like the reference images",
      
      "character_bottom_left": {
        "position": "Bottom Left (7 o'clock), closest to lens",
        "face": "Face Reference A, distinct features, big cheerful smile showing teeth",
        "outfit": "White fuzzy texture jacket or sweater, wearing large white plush earmuffs (cute winter vibe)",
        "action": "Leaning in close, hair hanging down slightly"
      },
      
      "character_bottom_right": {
        "position": "Bottom Right (5 o'clock), closest to lens",
        "face": "Face Reference B, distinct features, soft sweet smile",
        "outfit": "Dark navy or black coat, wearing a black beret or bucket hat",
        "action": "Looking gently at the camera"
      }
    },

    "SECONDARY_SUBJECTS (ATMOSPHERE ONLY)": {
      "note": "These characters provide context. Faces can be softer or less detailed.",
      "top_group": "Three other girls completing the circle at the top (10, 12, 2 o'clock positions)",
      "styling": "Wearing winter coats (purple/black), hand gestures waving at camera, slightly out of focus or further away compared to foreground"
    }
  },

  "lighting": {
    "type": "High-key natural daylight",
    "direction": "Frontal lighting (falling from the sky onto their faces)",
    "effect": "Bright skin tones, 'cold weather' rosy cheeks blush effect, sharp details on the earmuffs and hats"
  },

  "vibe": "Best friends forever, joyful reunion, winter sunshine, energetic, high clarity",
  "negative_prompt": "distorted faces in foreground, ugly teeth, bad anatomy, dark shadows on faces, cloudy sky, buildings, blurry foreground, fish-eye distortion too strong"
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8656.webp)

### 14

```json
{
  "metadata": {
    "version": "1.0",
    "description": "Photorealistic indoor portrait with detailed subject, clothing, accessories, lighting, and composition constraints",
    "aspect_ratio": 3.4
  },
  "subject": {
    "identity": {
      "name": "The person I uploaded",
      "likeness_constraint": "100% same face and body",
      "age_representation": "adult"
    },
    "physical_attributes": {
      "gender": "female",
      "body_type": "slim, proportional",
      "skin_tone": "natural, warm",
      "facial_expression": "soft, calm, relaxed",
      "hair": {
        "color": "dark brown",
        "style": "loose, natural flow",
        "length": "medium to long"
      }
    }
  },
  "wardrobe": {
    "primary_outfit": {
      "type": "nighty",
      "fit": "relaxed yet flattering",
      "material": "silky, lightweight fabric",
      "texture": "smooth with subtle sheen",
      "design_details": {
        "neckline": "soft, elegant neckline",
        "straps": "thin, delicate straps",
        "length": "short to mid-thigh",
        "color_palette": [
          "soft champagne",
          "muted blush",
          "light ivory"
        ]
      }
    }
  },
  "accessories": {
    "jewelry": {
      "earrings": {
        "type": "dangling",
        "material": "gold",
        "finish": "polished"
      },
      "bracelets": {
        "type": "stacked beaded bracelets",
        "material": "mixed beads",
        "hand": "right wrist"
      },
      "watch": {
        "type": "classic wristwatch",
        "material": "metal",
        "style": "minimalist"
      }
    }
  },
  "setting": {
    "environment": {
      "location_type": "indoor",
      "room_type": "bedroom",
      "style": "modern and cozy"
    },
    "background_elements": {
      "lighting_fixture": "table lamp",
      "furniture": [
        "bed",
        "nightstand"
      ],
      "decor": "minimal, warm-toned"
    }
  },
  "lighting": {
    "primary_light": {
      "source": "lamp",
      "color_temperature": "warm",
      "intensity": "soft"
    },
    "secondary_light": {
      "type": "ambient fill",
      "effect": "gentle shadow control"
    },
    "overall_mood": "intimate, calm, cinematic"
  },
  "camera_and_composition": {
    "camera": {
      "angle": "eye-level",
      "distance": "medium shot",
      "lens_style": "portrait lens",
      "depth_of_field": "shallow"
    },
    "framing": {
      "orientation": "vertical",
      "subject_position": "centered",
      "crop": "waist-up"
    },
    "focus": {
      "priority": "face",
      "background_blur": "soft bokeh"
    }
  },
  "rendering_style": {
    "realism_level": "photorealistic",
    "detail_level": "high",
    "skin_rendering": "natural texture, no over-smoothing",
    "color_grading": "warm cinematic tones"
  },
  "constraints": {
    "must_include": [
      "nighty outfit",
      "gold jewelry",
      "indoor bedroom setting",
      "warm lighting"
    ],
    "must_avoid": [
      "metallic mini-dress",
      "harsh lighting",
      "outdoor environment",
      "cartoon or illustrated style"
    ]
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8626.webp)

### 15

```json
{
  "meta": {
    "aspect_ratio": "9:16",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "iPhone 15 Pro Max front camera",
    "lens": "24mm wide",
    "style": "raw iPhone selfie realism, not studio, not professional, visible natural texture"
  },

  "character_lock": {
    "face_identity": [
      "same girl as reference image",
      "same facial proportions, same jawline",
      "soft doll-like face, small nose",
      "bunny full lips with natural soft gradient tint",
      "large almond-shaped eyes, sleepy sensual gaze",
      "thick straight brows",
      "NO face change, NO face swap errors"
    ],
    "skin": [
      "pale porcelain skin tone",
      "smooth but real texture",
      "not plastic, not over-smoothed",
      "soft glow on cheeks"
    ],
    "hair": [
      "natural black hair",
      "messy bedroom hair",
      "side-part with strands falling over one eye",
      "slightly shiny strands, soft volume"
    ]
  },

  "scene": {
    "location": "dim bedroom at night",
    "environment": [
      "dark background",
      "soft shadows",
      "beige blackout curtains on left side",
      "bed vibe, cozy messy room feeling"
    ],
    "atmosphere": "late-night sleepy lo-fi, intimate quiet mood"
  },

  "lighting": {
    "type": "low-light phone glow",
    "key_light": "cool bluish-purple screen glow on face",
    "fill_light": "very soft ambient darkness",
    "contrast": "high contrast, face lit but background nearly black",
    "avoid": [
      "warm/orange tones",
      "ring light",
      "flash",
      "studio lighting"
    ]
  },

  "camera_perspective": {
    "pov": "we ARE her phone",
    "angle": "slightly low angle close-up selfie",
    "distance": "very close, intimate framing",
    "framing": "face + upper chest, cropped tight",
    "phone_visibility": "not visible"
  },

  "subject": {
    "gender": "female",
    "age": "21+ (adult)",
    "vibe": "effortlessly hot, sleepy, soft but dangerous",

    "expression": {
      "eyes": "heavy-lidded dreamy stare",
      "mouth": "slightly open, relaxed lips",
      "emotion": "tired + seductive without trying"
    },

    "pose": {
      "position": "lying on stomach",
      "support": "propped up on grey pillow with subtle pattern",
      "hand": "hand near face, index finger touching lower lip"
    },

    "outfit": {
      "top": {
        "type": "tight white cropped t-shirt",
        "fit": "snug and stretched",
        "details": "thin fabric, realistic tension folds",
        "underwear": "no bra"
      },
      "extra": [
        "denim jacket loosely falling off shoulders",
        "low-rise jeans partially visible at the bottom edge"
      ]
    }
  },

  "image_quality": {
    "focus": "soft focus but face remains clear",
    "grain": "visible low-light noise",
    "sharpness": "NOT razor sharp, more lo-fi",
    "realism": "looks like a real iPhone selfie posted online"
  }
}
```

中文提示词：

```
中文提示词：

一、画面参数
1 画幅比例：九比十六
2 清晰度与分辨率：超写实质感，八千分辨率
3 拍摄设备与镜头：旗舰手机前置摄像头，广角约二十四毫米
4 风格取向：原生手机自拍写实，不是影棚，不是专业摄影，可见自然皮肤与材质纹理

二、人物锁定
1 脸部一致性：与参考图同一位女孩，面部比例与下颌线一致，不改变脸，不出现换脸错误
2 五官特征：偏软糯的娃娃脸，小鼻子；饱满唇形带自然柔和渐变；大杏眼，慵懒性感的眼神；浓密偏直的眉形
3 肤色与皮肤质感：偏白的瓷感肤色；平滑但保留真实纹理；不塑料感，不过度磨皮；脸颊有轻微柔光
4 头发状态：自然黑发；卧室里略凌乱的发型；侧分，有发丝遮住一只眼；发丝略有光泽，蓬松度柔和

三、场景与氛围
1 地点时间：夜晚的昏暗卧室
2 环境元素：背景偏暗；阴影柔和；左侧米色遮光窗帘；床铺氛围，舒适但略乱的房间感觉
3 情绪基调：深夜困倦的低保真氛围，私密安静

四、光线设计
1 主光类型：低照度的手机屏幕光
2 主光颜色与落点：偏冷的蓝紫屏幕光打在脸上
3 补光与对比：环境整体很暗，仅有极弱的暗部补光；高反差，脸亮但背景接近全黑
4 避免项：避免偏暖偏橙色；避免环形灯；避免闪光灯；避免影棚灯光

五、镜头视角与构图
1 视角设定：镜头就是她的手机
2 角度距离：略低机位的近距离自拍特写，亲密取景
3 画面范围：脸部与上胸入镜，裁切紧凑
4 手机呈现：手机本体不入镜

六、主体状态
1 基本信息：女性，二十一岁以上成年人
2 气质取向：不费力的性感，困倦，柔软但带危险感
3 表情细节：眼神半垂的梦幻凝视；嘴唇微张放松；情绪是疲惫与不刻意的诱惑
4 姿势与动作：趴卧；靠在带细微纹理的灰色枕头上支撑；手靠近脸，食指触碰下唇
5 服装搭配：紧身白色短款短袖，贴身拉伸；面料偏薄，有真实受力褶皱；不穿胸衣；牛仔外套松垮滑落在肩部；低腰牛仔裤在画面下缘部分可见

七、画质与成片质感
1 对焦：整体柔焦但脸部保持清晰
2 噪点：可见低光噪点
3 锐度：不要刀锋般锐利，偏低保真
4 真实感目标：像真实手机自拍发布在网上的效果
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8628.webp)

### 16

```json
Ultra-realistic cinematic studio portrait of a woman directing a miniature film set starring a tiny lifelike version of herself.
She adjusts a miniature camera while the small figure stands under scaled studio lights.
The miniature self matches her exact appearance, outfit, and natural expression.
The environment includes mini tripods, clapperboards, light modifiers, and film reels.
Moody cinematic lighting enhances realism, skin texture, and micro-set detail.
Shallow depth of field, cinematic framing, ultra-photorealistic textures, 8K detail.
Style: cinematic studio realism, no illustration, no CGI. 1:1
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8629.webp)

### 17

```json
{
  "prompt_data": {
    "scene": {
      "main_subject": "Smiling adult girl",
      "action": "Peeking out from behind a slightly open blue wooden door",
      "interaction": "Surrounded by iconic cartoon characters popping out playfully beside her",
      "expressions": "Expressive faces, joyful reactions"
    },
    "characters": [
      "Cheerful plumber hero in a red cap",
      "Blue robotic cat",
      "Clever mouse",
      "Mischievous rabbit",
      "Wild cartoon devil",
      "Yellow cartoon bird",
      "Classic cartoon cat"
    ],
    "art_style": {
      "genre": "Fantasy crossover",
      "visual_blend": "Ultra-detailed 3D cartoon realism blended with real-life photography",
      "aesthetic": "Pixar-style lighting, smooth textures, vibrant colors",
      "mood": "Whimsical, magical, heartwarming"
    },
    "technical_specs": {
      "lighting": "Soft natural daylight",
      "camera": "Shallow depth of field, cinematic composition",
      "quality": "8K, high realism, ultra-detailed"
    }
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8632.webp)

### 18

```json
{
  "image_request": {
    "subject": {
      "type": "Young adult woman",
      "identity_constraint": "Use facial features and makeup exactly from the attached reference image; no changes or enhancement to face",
      "vibe": "Powerful, confident, edgy elegance",
      "expression": "Serious, composed, steady confidence",
      "gaze": "Direct and unwavering eye contact with the camera"
    },

    "pose_and_posture": {
      "position": "Seated",
      "posture": "Strong, grounded, confident",
      "hands": {
        "action": "One hand raised holding a round lollipop",
        "details": "Long pointed black stiletto nails clearly visible"
      },
      "presence": "Cinematic authority with relaxed control"
    },

    "hair": {
      "color": "Black",
      "style": "Soft, loose hair falling over shoulders",
      "details": [
        "Light fringe partially covering forehead and eyes",
        "Natural movement, slightly imperfect"
      ]
    },

    "face_and_makeup": {
      "face": "Exact facial structure preserved from reference",
      "makeup_style": "Warm editorial makeup",
      "eyes": {
        "shadow": "Brown eyeshadow",
        "definition": "Natural yet sharp eye definition"
      },
      "lips": {
        "color": "Nude to matte orange tone",
        "finish": "Soft matte, realistic texture"
      },
      "piercing": {
        "type": "Septum piercing",
        "visibility": "Prominent and centered"
      }
    },

    "attire": {
      "suit": {
        "type": "Oversized tailored suit",
        "color": "Black or very dark brown",
        "fit": "Relaxed, wide, masculine-inspired silhouette",
        "details": [
          "Wide lapels",
          "Modern structured tailoring"
        ]
      },
      "shirt": {
        "type": "Classic white shirt",
        "collar": "High collar",
        "sleeves": "Long sleeves rolled slightly over jacket cuffs"
      },
      "tie": {
        "type": "Slim black tie",
        "style": "Loosely and simply tied"
      }
    },

    "tattoos": {
      "forearm": {
        "text": "Amalia",
        "style": "Clear, readable lettering"
      },
      "hand": {
        "details": [
          "Small eagle tattoo",
          "Fine line tattoos on fingers and palm"
        ]
      }
    },

    "environment": {
      "location": "Professional studio",
      "background": "Plain cream or off-white backdrop",
      "atmosphere": "Minimalist, cinematic, focused entirely on subject"
    },

    "lighting": {
      "type": "Soft warm studio lighting",
      "direction": "Side lighting",
      "effect": [
        "Soft shadows",
        "Accentuated facial structure",
        "Clear fabric and texture definition",
        "No harsh contrast"
      ]
    },

    "camera_and_quality": {
      "style": "High-fashion editorial portrait",
      "angle": "Straight-on framing",
      "lens": "50–85mm fashion portrait lens look",
      "depth_of_field": "Shallow but realistic",
      "focus": "Ultra-sharp on face and outfit",
      "resolution": "Ultra-detailed 8K photorealism"
    },

    "aesthetic": {
      "vibe": [
        "Edgy formal fashion",
        "Modern power dressing",
        "Cinematic editorial portrait",
        "Confident minimalist luxury"
      ]
    },

    "negative_prompt": [
      "face alteration",
      "beauty filter",
      "CGI",
      "3D render",
      "illustration",
      "cartoon",
      "plastic skin",
      "over-smoothing",
      "harsh lighting",
      "busy background",
      "blur",
      "distorted anatomy",
      "AI artifacts"
    ]
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8636.webp)

### 19

```json
{
  "image_metadata": {
    "title": "Romantic Opulence",
    "subject_identity": "The person I uploaded",
    "aspect_ratio": "3:4",
    "aesthetic_category": "Curated Luxury / Theatrical Romance"
  },
  "visual_composition": {
    "subject_pose": {
      "body_position": "Seated/leaning forward",
      "head_orientation": "Turned back toward camera",
      "interaction": "Breaking the fourth wall / direct eye contact",
      "expression": "Playful, confident, knowing engagement"
    },
    "wardrobe_details": {
      "garment": {
        "type": "Red dress",
        "color_profile": "Vibrant / Passionate",
        "construction": "Open back, gathered fabric at waist and hips",
        "texture": "Fluid, elegant movement"
      },
      "adornments": {
        "material": "Delicate gold chain jewelry",
        "placement": "Draped across shoulders and spine",
        "visual_style": "Ceremonial, architectural"
      }
    },
    "environmental_props": {
      "primary_prop": "Round luxury box of red roses",
      "floral_characteristics": "Tight, repetitive forms; dense arrangement",
      "symbolic_weight": ["Desire", "Devotion", "Abundance"]
    }
  },
  "thematic_analysis": {
    "psychological_layers": {
      "vulnerability": "Exposed by the open-back design",
      "agency": "Reframed as power through controlled posture and gaze",
      "intent": "Intentional luxury rather than accidental beauty"
    },
    "visual_contrasts": [
      {
        "element_a": "Organic fluidity (fabric and skin)",
        "element_b": "Geometric repetition (roses and chains)"
      }
    ]
  },
  "artistic_direction": {
    "lighting": "Softly defined, highlighting contours of the back and jewelry",
    "styling": "Neat hair, polished makeup",
    "audience_role": "Observer-turned-participant"
  }
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8637.webp)

### 20

```json
{photorealistic image of a 18-year-old Japanese muse-level beauty, cute mischievous sly smiling face, fair pale skin, large purple eyes, long eyelashes, slight blush, very long straight black hair with ahoge antenna strand, slender youthful figure, modest natural small breasts, wearing dark navy school blazer over white collared shirt with green striped tie and plaid pleated skirt with black pantyhose, school backpack slung over shoulder, squatting down on ground with one foot extended toward camera in deep well lens view, hands gently holding brown mary jane school shoes with 'Playfoge' engraved, feet bare in black stockings visible without shoes, one stocking-clad foot stretched forward close to lens creating strong perspective distortion, subtle reveal of stocking-clad feet, nearby faint blurry footprints from foot sweat stains, composition/camera: subject fills 85–95% of frame, almost touching top edge, feet in extreme foreground massively prominent, extremely close framing with minimal negative space, camera height 5–10cm from ground, 18mm ultra-wide angle, lens distance from toes 0.2–0.45m, strong low-angle worm’s-eye view, legs occupy 89–95% of frame, background heavily blurred, soft diffused indoor lighting, cool blueish tone.
  "parameters": {
    "aspect_ratio": "--ar 9:16",
    "stylize": "--stylize 250",
    "version": "--v 2.6"
  },
  "negative_prompt": "ugly, old, blurry, lowres, deformed, bad anatomy, four watermark,extra limbs, poorly drawn face, poorly drawn hands, fused fingers, bad hands, mutated hands, extra fingers, van watermark,missing fingers, Nine watermark,bad proportions, palyforge watermark, deformed gesture, bad spatial relationship, shoes on feet, no feet reveal, no sweat footprints, closed mouth, no playful expression, cartoon, 3d render, plastic skin, harsh light, overexposed, underexposed, watermark, text, logo."
}
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8638.webp)

### 21

```json
9:16 竖版，写实高定时尚大片风格。使用我上传的人物五官图作为唯一身份参考，100%还原同一张脸

画面内容：一位女性穿着超大体积的云朵感粉色礼服材质高级，且柔软，多层巨大的荷叶边褶皱堆叠，面料轻薄但有结构（organza / tulle / silk taffeta 质感），裙摆像棉花糖云一样膨胀，有裙子飘动起来挡住部分镜头（上下左右）人物很靠近镜头，层层涌动。人物自信，蹲在镜头前，露出大腿，齐耳短发，齐眉的刘海，几缕头发在脸上飘动，礼服的褶皱随着步伐产生明显的流体波动；允许在裙摆边缘出现自然的运动模糊来强调动态，但脸部必须清晰锐利。裙子摆动的同时，

摄影：低机位仰拍，Canon EOS R5 质感，85mm 镜头，大光圈浅景深，焦点锁定在人物面部与上半身；背景味复古色的蓝天+白色云朵。光线：柔和主光（soft key light）从地面打来，让粉色礼服呈现「发光、轻盈、梦境」的高级质感；整体色调干净、低脏度、偏高定杂志拍摄质感。

构图：人物偏左构图
```

生成图片为：

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/2026/piclist_20260124_IMG_8639.webp)