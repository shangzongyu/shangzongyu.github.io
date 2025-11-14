---
title: 'KVM 使用介绍'
description: '自己在公司中有一台 Linux 主机，以及一台 Mac 电脑，两个电脑系统不同，使用起来需要我来回在不同的设备上进行切换，有些麻烦，因此就找到 KVM Switch 这个方案。'
slug: KVM
date: 2024-11-05 06:49:19+0000
image: cover.jpg
tags:
    - tools
weight: 1
---

## 为什么要使用 KVM

自己在公司中有一台 Linux 主机，以及一台 Mac 电脑，两个电脑系统不同，使用起来需要我来回在不同的设备上进行切换，有些麻烦，因此就找到 KVM Switch 这个方案。

## KVM 介绍

根据维基百科的介绍如下：

> KVM 切换器 (英语：KVM switch)，一般简称 KVM，又名多电脑切换器，是一种计算机硬件设备，可以使用户透过一组键盘、屏幕和鼠标控制多台电脑。KVM，即键盘、显示器、鼠标的英文首字母缩写 (**K**eyboard、**V**ideo、**M**ouse)。

总结下就是使用一套特殊设备访问多个不同过的电脑。

KVM 主要是硬件设备，当然也有软件实现的，我知道有下面几个：

- [synergy](https://symless.com/synergy) - 付费
- [deskflow](https://github.com/deskflow/deskflow) - 开源
- [input-leap](https://github.com/input-leap/input-leap) - 付费

## 使用介绍

自己本来想买一个 KVM 硬件设备的，但是感觉有些占用地方，因此就找一些软件替代，虽然功能不那么全，但是够自己基本使用就行了。

[synergy](https://symless.com/synergy)、[deskflow](https://github.com/deskflow/deskflow) 和 [input-leap](https://github.com/input-leap/input-leap) 这个我都有使用。体验最好的是 [synergy](https://symless.com/synergy)，我之前也买过，但是 [synergy](https://symless.com/synergy) 升级之后就使用不了，然后就寻找开源的替代品，之后就找到了 [deskflow](https://github.com/deskflow/deskflow) 和 [input-leap](https://github.com/input-leap/input-leap)。

- [deskflow](https://github.com/deskflow/deskflow) 延迟严重，使用起来感觉就是卡卡的
- [input-leap](https://github.com/input-leap/input-leap) 有一丝丝的延迟，轻度使用没有任何问题。
