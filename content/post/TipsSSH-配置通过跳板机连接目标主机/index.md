---
title: 'Tips:SSH 配置通过跳板机连接目标主机'
description: '- 跳板机'
slug: tipsssh
date: 2024-12-11 12:06:52+0000
image: cover.jpg
weight: 1
---


## 前言

- 跳板机
    - private key：jumper-server.pem
    - ip：8.217.228.125
- 目的主机
    - private key：target-server.pem
    - ip：192.168.2.9

## 使用 SSH Config

```
Host jumper-server
    HostName 8.217.228.125
    User ecs-user
    IdentityFile ~/.ssh/jumper-server.pem
    IdentitiesOnly yes

Host target-server
    HostName 192.168.2.9
    User root
    ProxyJump jumper-server
    IdentityFile ~/.ssh/target-server.pem
    IdentitiesOnly yes
```

配置后：

```sh
ssh target-server
```

> 这样就可以直接登录 target-server 了。

## 使用命令行

> 除了使用 SSH Config，我想是否可以使用命令行配置，命令行如下。

```sh
ssh -i ~/.ssh/jumper-server.pem -J ecs-user@8.217.228.125 -o IdentityFile=~/.ssh/target-server.pem -o IdentitiesOnly=yes root@192.168.2.9
```

> 理论上可以，但是连接不上，我问了 ChatGPT 大概的错误是： -i 和 -o 同时指定会相互影响，-i 优先级比较高，导致 -o 这个用不上，就这样。

想要使用命令行连接可以通过 SSH 的 ProxyCommand 选项来实现：

```sh
ssh -i ~/.ssh/target-server.pem -o ProxyCommand="ssh -i ~/.ssh/jumper-server.pem -W %h:%p ecs-user@8.217.228.125" root@192.168.2.9
```

- `-i ~/.ssh/target-server.pem`：指定连接目标机时使用的 PEM 文件。
- `-o ProxyCommand="ssh -i ~/.ssh/jumper-server.pem -W %h:%p ecs-user@8.217.228.125"`：使用 ProxyCommand 来通过跳板机连接到目标机。此时，跳板机使用 `jumper-server.pem` 文件。
- `root@192.168.2.219`：目标服务器的地址。
- 关键点：`-W %h:%p` 告诉 SSH 将目标主机地址 (`%h`) 和端口 (`%p`) 转发给跳板机。

> 通过这种方式，你可以在一条命令中同时指定两个不同的 PEM 文件，一个用于跳板机，一个用于目标机。

BingGo 解决了。

## FAQ

### pem 的文件权限 too open

```sh
chmod 600 ~/.ssh/jumper-server.pem
chmod 600 ~/.ssh/target-server.pem
```
