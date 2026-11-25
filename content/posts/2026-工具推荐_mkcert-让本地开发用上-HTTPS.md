---
title: "工具推荐：mkcert，让本地开发用上 HTTPS"
description: "用 mkcert 生成本地受信任的证书，从证书签发到启动 HTTPS 服务。"
slug: ""
date: 2026-10-05T11:51:27+08:00
draft: true
categories:
  - 工具推荐
tags:
  - mkcert
  - HTTPS
  - 本地开发
featuredImage: ""
weight: 1
---

本地开发需要 HTTPS 时，麻烦的往往不是启动服务，而是让浏览器信任证书。手动生成一张自签名证书，虽然能加密连接，访问时却仍可能看到证书警告。

[mkcert](https://github.com/FiloSottile/mkcert) 把这件事简化成两步：安装一个本地证书颁发机构，再为开发服务生成证书。之后，把证书配置到服务器中，就可以使用受信任的本地 HTTPS 连接。

<!--more-->

## mkcert 是怎么工作的

浏览器是否信任证书，取决于能否沿着证书链找到受信任的证书颁发机构，也就是 CA。

mkcert 会创建一个本地 CA，并通过 `mkcert -install` 将其根证书加入系统或支持的浏览器信任库。随后生成的服务器证书由这个 CA 签发，因此在信任该 CA 的客户端上，域名匹配且证书有效时，就能通过证书校验。[官方说明](https://github.com/FiloSottile/mkcert#mkcert)

可以把这个过程理解为：

```text
客户端信任本地 CA
        ↓
本地 CA 为 localhost 签发证书
        ↓
开发服务器使用该证书提供 HTTPS
        ↓
客户端校验证书并建立连接
```

这里的 “受信任” 有范围：只对安装并信任了这个 CA 的客户端生效。把服务器证书发给别人，并不会让对方的设备自动信任它。

## 在 macOS 上安装

以下步骤需要已经安装 Homebrew。在终端执行：

```bash
brew install mkcert
```

如果使用 Firefox，还需要安装 NSS 工具，以便 mkcert 管理它的证书信任库：

```bash
brew install nss
```

然后创建并安装本地 CA：

```bash
mkcert -install
```

安装过程可能要求管理员授权。完成后，如果浏览器没有识别到新的信任配置，重启浏览器再试。其他系统的安装方式可查看[官方安装说明](https://github.com/FiloSottile/mkcert#installation)。

## 为本地服务生成证书

在一个独立的示例目录里执行：

```bash
mkdir mkcert-demo
cd mkcert-demo

mkcert -cert-file localhost.pem \
  -key-file localhost-key.pem \
  localhost 127.0.0.1 ::1
```

这条命令生成两个文件：

| 文件 | 用途 |
| --- | --- |
| `localhost.pem` | 服务器证书 |
| `localhost-key.pem` | 与服务器证书配套的私钥 |

末尾的 `localhost`、`127.0.0.1` 和 `::1` 是证书覆盖的主机名与 IP 地址，不需要写协议或端口。同一张证书可以用于不同端口上的服务，但访问地址必须在证书覆盖范围内。

mkcert 负责生成证书，服务器仍需要自己配置。下面用一个简单的 Node.js 服务演示整个流程。

## 启动一个 HTTPS 服务

以下示例使用 Node.js 24，仅依赖内置模块，无需安装 npm 包。把这段代码保存为示例目录下的 `server.mjs`，与刚才生成的证书放在一起：

```javascript
import { createServer } from 'node:https';
import { readFileSync } from 'node:fs';

// 按脚本所在目录读取证书，避免工作目录变化导致找不到文件。
const server = createServer(
  {
    cert: readFileSync(new URL('./localhost.pem', import.meta.url)),
    key: readFileSync(new URL('./localhost-key.pem', import.meta.url)),
  },
  (_req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('本地 HTTPS 已启动。\n');
  },
);

// 仅监听本机 IPv4 回环地址。
server.listen(8443, '127.0.0.1', () => {
  console.log('访问 https://127.0.0.1:8443');
});
```

启动服务：

```bash
node server.mjs
```

用浏览器访问 `https://127.0.0.1:8443`。如果 CA 已成功加入浏览器使用的信任库，就能看到 “本地 HTTPS 已启动。” 且没有证书信任报错。

代码通过 `https.createServer()` 的 `cert` 和 `key` 选项加载证书与私钥，具体接口见 [Node.js 官方文档](https://nodejs.org/api/https.html#httpscreateserveroptions-requestlistener)。使用其他开发服务器时，同样需要找到它的 HTTPS 配置项并传入这两个文件。

## 使用自定义域名

如果希望通过 `app.test` 访问本地服务，需要分别解决域名解析和证书匹配。

先在 macOS 的 `/etc/hosts` 中加入以下记录，修改该文件需要管理员权限：

```text
127.0.0.1 app.test
```

然后停止示例服务，为新域名重新生成证书：

```bash
mkcert -cert-file localhost.pem \
  -key-file localhost-key.pem \
  app.test localhost 127.0.0.1 ::1

node server.mjs
```

现在可以访问 `https://app.test:8443`。hosts 记录负责把域名指向本机，证书负责证明服务器可以使用这个域名，两者都需要配置。

## 换一台设备访问时

在电脑上安装了本地 CA，不代表手机也会信任它。如果要通过局域网访问开发服务，需要同时满足三个条件：

1. 服务监听局域网可访问的地址；上面的示例只允许本机访问，需要调整。
2. 服务器证书包含手机实际访问的域名或局域网 IP 地址。
3. 手机安装并信任签发该证书的本地 CA。

用下面的命令查看 CA 文件所在目录：

```bash
mkcert -CAROOT
```

其中 `rootCA.pem` 是可以导入其他设备的根证书。iOS 安装描述文件后，还需要启用该根证书的完全信任；Android 应用是否接受用户安装的 CA，则取决于应用的信任配置，开发版本可能需要额外设置。具体步骤见[官方移动设备说明](https://github.com/FiloSottile/mkcert#mobile-devices)。

## 几个容易混淆的地方

**根证书和根私钥用途不同。**`rootCA.pem` 用于建立信任，`rootCA-key.pem` 用于签发证书。后者一旦泄露，别人就能签发被你的设备信任的证书，因此不要分享，也不要提交到 Git 仓库。示例中生成的服务器私钥也应留在本地。[官方安全提示](https://github.com/FiloSottile/mkcert#installation)

**浏览器信任，不代表所有程序都会自动信任。**如果 Node.js 作为客户端请求 mkcert 签发证书的服务时仍然报错，可以在启动客户端进程前，显式指定附加根证书：

```bash
export NODE_EXTRA_CA_CERTS="$(mkcert -CAROOT)/rootCA.pem"
```

这个设置用于客户端校验证书，和服务器加载 `cert`、`key` 是两件事。不同 Node.js 版本和启动选项对系统信任库的支持可能不同，显式指定附加 CA 的方式见 [mkcert 官方说明](https://github.com/FiloSottile/mkcert#using-the-root-with-nodejs)。

**本地 CA 不适合给公网用户使用。**mkcert 面向开发环境，公网生产站点应使用公开受信任的 CA 证书，避免要求访问者手动安装根证书。

需要清理本机的 CA 信任配置时，可以执行：

```bash
mkcert -uninstall
```

这会移除 mkcert 管理的本地 CA 信任配置，不会删除 CA 文件，也不会清理已经生成的服务器证书。[命令源码](https://github.com/FiloSottile/mkcert/blob/master/main.go)
