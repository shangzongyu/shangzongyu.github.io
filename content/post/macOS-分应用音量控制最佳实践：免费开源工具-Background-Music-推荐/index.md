---
title: 'macOS 分应用音量控制最佳实践：免费开源工具 Background Music 推荐'
description: 'Mac 用户常常遇到这样的问题：不同 App 的音量需求差异很大，有的需要放大，有的希望静音，但 macOS 并没有原生多应用音量控制功能。这一需求，可以通过开源工具 background-music 轻松解决。[1]'
slug: macos-background-music
date: 2025-10-06 04:31:13+0000
tags:
    - tools
    - macos
weight: 1
---


Mac 用户常常遇到这样的问题：不同 App 的音量需求差异很大，有的需要放大，有的希望静音，但 macOS 并没有原生多应用音量控制功能。这一需求，可以通过开源工具 background-music 轻松解决。[1]

### 工具介绍

![](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2025/upgit_20251006_tools-backgroud-music.png)

background-music 是一款 macOS 下的开源音频控制工具，它支持为每个应用单独设置音量，还能自动在有新音频播放时暂停当前音乐播放器，并在音频结束时继续播放，非常贴合多任务的场景需求。除了分应用音量调节，background-music 还提供系统音频录制等功能，基本覆盖了日常对音频控制的要求。[1]

### 安装方式

在终端输入以下命令即可安装，无需重启系统，非常方便：

```sh
brew install background-music
```

安装后，直接运行 Background Music.app 即可，在“系统设置 > 声音”中会自动切换为默认输出设备。[1]

### 相似工具推荐

除了 background-music，还有一些功能更丰富或界面更专业的付费选择——

| 工具名称      | 主要功能特点                                                                     | 是否付费      |
| ------------- | -------------------------------------------------------------------------------- | ------------- |
| Sound Control | 分应用音量控制、均衡器调节、可自定义输出设备、快捷键支持，界面简洁               | 是（付费）[1] |
| SoundSource   | 专业级音频控制，可针对每个 App 单独调节音量/音质、均衡器、多设备输出，菜单栏便捷 | 是（付费）[1] |

如果只是需要最基础的分应用音量调节，background-music 足够满足日常需求，而且完全免费、开源，很适合 macOS 用户作为轻量级解决方案。[1]

### 结语

macOS 缺失的“多应用音量管理”功能，通过 background-music 这款免费小工具，可以轻松补齐。如果有更高阶需求，则可选择 Sound Control 或 SoundSource 这类专业软件辅助。[1]

[1](https://github.com/kyleneideck/BackgroundMusic)

## FAQ

使用这个工具后有个问题就是，Airpod 耳机的在电脑和手机之间自动切换的功能就用不了了。

---

**特别感谢**  
本文由作者与 AI 协同创作完成，内容融合了真实应用体验和前沿工具解读，希望为大家带来实用且高效的 Mac 使用参考。