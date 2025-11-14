---
title: 'Redis 的 FAQ'
description: ''
slug: redis-error-err-debug-command-not-allowed
date: 2023-07-26 10:24:40+0000
image: https://raw.githubusercontent.com/shangzongyu/blog-image/main/2025/piclist_20251114_redis.webp
tags:
  - redis
  - FAQ
weight: 1
---

## Redis Error: "ERR DEBUG command not allowed.

Redis 安装之后，默认不允许使用 DEBUG 这个命令，我们只需要修改一些配置文件就可以了。

修改配置文件 `/etc/redis/redis.conf`，修改 `enable-debug-command no`，修改为 `enable-debug-command yes`，并且解开注释，然后重启。

![redis-config](https://raw.githubusercontent.com/shangzongyu/blog-image/main/hashnode/2023/upgit_20230726_redis-faq-0000.png)

重启服务：

```sh
sudo systemctl restart redis-server
```
