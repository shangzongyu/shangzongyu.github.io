## 介绍

Vaultwarden 是一个用于本地搭建 [Bitwarden](https://bitwarden.com/) 服务器的第三方 Docker 项目。仅在部署的时候使用 Vaultwarden 镜像，桌面端、移动端、浏览器扩展等客户端均使用官方 Bitwarden 客户端。

- Github: <https://github.com/dani-garcia/vaultwarden/wiki>
- Wiki 中文：<https://rs.ppgg.in/>

### Vaultwarden 与 Bitwarden 的区别

- 除不支持 Bitwarden 官方企业版的部分功能（详情见[这里](https://rs.ppgg.in/home#missing-features)）外，其他大部分功能均 **免费**支持，亲并且跟随官方版本保持及时更新。
- Vaultwarden 比 Bitwarden 官方版更轻量。
  - 官方版使用 .Net 开发，使用 MSSQL 数据库，要求至少 2GB 内存。
  - Vaultwarden 使用 Rust 编写，改用 SQLite 数据库（现在也支持 MySQL 和 PostgreSQL），运行时只需要 10M 内存，可以说对硬件基本没有要求。

## 客户端

- 下载地址 <https://bitwarden.com/download/>，Bitwarden](https://bitwarden.com/) 跨平台，支持 macOS/Linux/Windows/iOS/Android 以及各个浏览器的插件。
- 手机端
  - iOS：<https://apps.apple.com/us/app/bitwarden-password-manager/id1137397744>

## 导入 KeePass

> 我之前在使用 KeePass，macOS 端使用 [KeePassXC](https://keepassxc.org/), 手机端使用 [FantasyPass](https://apps.apple.com/us/app/fantasypass/id1357961740)。

把 KeePass 迁移到 Vaultwarden，推荐使用 [KP2BW - KeePass 2.x 到 Bitwarden 转换器](https://github.com/jampe/kp2bw)执行导入，该转换器支持更多的 Keepass 功能，如文件附件，引用等等！

## 使用感受

iOS 端使用体验还可以，但是 macOS 端的软件体验有些不是很好，软件不是好用。