---
title: "Tips: ssh 客户端超时处理"
description: "''"
slug: ssh
date: 2023-10-14 10:47:46+0000
image: cover.jpg
tags:
  - tips
  - ssh
  - faq
weight: 1
---

> SSH 客户端连接 SSH 服务器，如果长时间不操作，那么 SSH 就会自动断线，在日常开发中遇到这种情况让人很抓狂。这篇文章就是为了解决这个问题，如果使用 ZOC 这种图形化工具，比较容易解决做个简单的配置就可以，Mac/Linux 需要做其他的处理。

## Windows

在 Windows 上有主要是图形化工具。

1. WinSCP

可以找到主机的连接超时时间设置更改，打开 keepalive 选项，每隔一段时间给连接发送一个 SSH 空包或哑命令以保持连接不断开，keepalive 的间隔秒数要设置少于超时等待的时候，如设置成 10 秒，确认重新连接即可。设置项如图：

![winscp-ssh-timeout](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230922_winscp-ssh-timeout.png)

### ZOC

在顶部 `Options -> Edtion session Profile -> Terminal -> Idle time` 设置**时长**就可以了。

![zoc-ssh-timeout-00](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230922_zoc-ssh-timeout-00.png)

![zoc-ssh-timeout-01](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230922_zoc-ssh-timeout-01.png)

## Mac/Linux

> 在 Mac/Linux 可以通过修改 SSH 客户端的配置达到这个目的。

SSH Client 会从以下途径获取配置参数：

* SSH 命令行参数
* 用户配置文件 `~/.ssh/config`
* 系统配置文件 `/etc/ssh/ssh_config`

### 命令行参数

> 使用命令行连接的时候设置参数

```sh
ssh -o ServerAliveInterval=60 \
    -o ServerAliveCountMax=30 \
    root@10.0.1.25 -p 22
```

### 修改用户配置文件

在 `~/.ssh/config` 添加如下内容：

```bash
Host *
  ServerAliveInterval 60
  ServerAliveCountMax 30
```

### 修改系统配置文件

在 `Host *` 下面添加：

```bash
Host *
  SendEnv LANG LC_*
  ServerAliveInterval 60
  ServerAliveCountMax 30
```

### 总结

这样设置后 SSH Client 每隔 60s 向 Server 端发送 \`keep-alive\`\` 包，如果发送 30 次，Server 端还无回应则断开连接。

如果以上都设置了，那么顺序是：**命令** -&gt; **用户配置** -&gt; **系统配置**。

## 服务端设置

我们也可以通过修改 SSH Server 端口的配置，但是不建议这样做。

修改配置文件 `/etc/ssh/sshd_config`，然后找到下面两项，去掉注释：

```bash
ClientAliveInterval 60
ClientAliveCountMax 30
```

说明：

* `ClientAliveInterval`：SSH Server 与 SSH Client 的心跳超时时间，也就是说，如果客户端没有发送任何指令，SSH Server 间隔 `ClientAliveInterval` 秒后，会发送一个空包来和客户都安保持心跳。
* `ClientAliveCountMax`：表示重试的最大次数，我们设置为 30，也就是说，如果 Server 像 Client 发送了每隔 `ClientAliveInterval` 秒后，发送了 `ClientAliveCountMax` 次后，都失败了，那么就会断开这个来连接。

更多参考 [man ssh\_config](https://linux.die.net/man/5/ssh_config)：

```bash
ServerAliveCountMax Sets the number of server alive messages (see below) which may be sent without ssh(1) receiving any messages back from the server. If this threshold is reached while server alive messages are being sent, ssh will disconnect from the server, terminating the session. It is important to note that the use of server alive messages is very different from TCPKeepAlive (below). The server alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by TCPKeepAlive is spoofable. The server alive mechanism is valuable when the client or server depend on knowing when a connection has become inactive.

The default value is 3. If, for example, ServerAliveInterval (see below) is set to 15 and ServerAliveCountMax is left at the default, if the server becomes unresponsive, ssh will disconnect after approximately 45 seconds. This option applies to protocol version 2 only; in protocol version 1 there is no mechanism to request a response from the server to the server alive messages, so disconnection is the responsibility of the TCP stack.

ServerAliveInterval Sets a timeout interval in seconds after which if no data has been received from the server, ssh(1) will send a message through the encrypted channel to request a response from the server. The default is 0, indicating that these messages will not be sent to the server, or 300 if the BatchMode option is set. This option applies to protocol version 2 only. ProtocolKeepAlives and SetupTimeOut are Debian-specific compatibility aliases for this option.
```
