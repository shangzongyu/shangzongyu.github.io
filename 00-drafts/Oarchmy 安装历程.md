- Omarchy
  - SSD 确实快太多了
  - Lang
    - Python
    - NodeJS
    - Go
  - subverison
  - tree
  - meld - GUI 比较
  - clash verge rev
    - https://www.clashverge.dev/install.html#__tabbed_2_3

## 软件的删除

简短结论：在 Arch/Manjaro 等使用 pacman 的系统中，删除软件通常使用 pacman -R 来卸载软件包，结合选项控制依赖和配置文件的处理；若要更彻底地清理缓存或孤儿依赖，需要配合其他命令如 paccache 或 pacman -Qdt 等来清理。

下面分解为实用要点和常用命令示例。

### 基本卸载软件

- 只卸载目标软件，不移除其依赖的情况
  - 命令：`pacman -R 软件包名`
  - 说明：删除指定包，但不会自动删除被它依赖的其他包。
- 同时删除该软件及其未被其它软件使用的依赖
  - 命令：`pacman -Rs` 软件包名
  - 说明：会移除该包以及它的孤儿依赖，前提条件是这些依赖不再被其他软件需要。
- 删除软件、依赖及全局配置文件
  - 命令：`pacman -Rns 软件包名`
  - 说明：连同配置文件一起删除，较为彻底。
- 同时删除软件、依赖以及可能的未被使用的配置/缓存等
  - 参考用法通常是 `-Rns` 的组合，确保清理残留。
- 删除后查看系统中仍有的被显式安装的软件包
  - 命令：`pacman -Qe`
  - 说明：列出“显式安装”的包，便于后续清理时定位。

### 清理缓存和孤儿包

- 清理缓存中的未安装包（保留最近版本可选）
  - 命令：`pacman -Sc`
  - 说明：清理缓存中的未安装软件包，保留已安装包的最近若干版本通常更安全。
- 更强力的缓存清理（清空缓存）
  - 命令：`pacman -Scc`
  - 说明：两次执行清空缓存，谨慎使用，可能导致重新安装软件时需要重新下载。
- 找出并删除孤儿包（不再被任何已安装包所依赖）
  - 命令之一：`pacman -Qdt`
  - 说明：列出孤儿包。要删除：`pacman -R $(pacman -Qdtq)`
- 结合清理孤儿与缓存的综合步骤
  - 典型流程：
    - 先查找孤儿包：`pacman -Qdt`
    - 删除孤儿包：`pacman -R $(pacman -Qdtq)`
    - 清理缓存：`pacman -Sc 或 pacman -Scc`

### 实用的小贴士

- 在执行大规模清理前，先执行 `pacman -Syu` 更新系统，确保包数据库与仓库信息是最新的。
- 使用 `pacman -Rns` 这样的组合在生产环境中较为稳妥，因为会清理不再被需要的字段与配置，减少残留。
- 对于服务器或关键系统，建议在清理前备份并确保有可回滚的包镜像或安装介质。

## Git 配置代理

Git 使用代理一般分为 HTTP(S)代理和 socks5 代理两种方式，配置方法主要通过 git config 命令设置。

### 设置 HTTP(S)代理：

```sh
#全局配置：
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890

# 针对特定域名（例如只对GitHub）设置代理：
 git config --global http.https://github.com.proxy http://127.0.0.1:7890
 git config --global https.https://github.com.proxy http://127.0.0.1:7890
```

### 设置 SOCKS5 代理：

```sh
#假设 SOCKS5 代理地址为 127.0.0.1 端口 7890，命令如下：
git config --global http.https://github.com.proxy socks5://127.0.0.1:7890
git config --global https.https://github.com.proxy socks5://127.0.0.1:7890
```

### 取消代理设置：

```sh
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### 查看已设置的代理配置：

```sh
git config --global -l
```

### 注意

- 以上设置对通过 HTTP/HTTPS 协议访问的 Git 仓库有效，对于通过 SSH 协议访问（如`git@github.com`）无效。
- 对于有些使用代理环境下遇到的证书问题，可以考虑关闭 SSL 验证或者配置信任的 CA 证书，但这涉及安全风险，要谨慎处理。

总的来说，设置 Git 代理主要是通过上述命令，根据你的代理类型和需求选择合适的命令进行配置即可。

### `git@github.com` 设置代理

给使用 SSH 协议的 Git 连接（如 [git@github.com]）设置代理，不能直接通过 git config 的 http.proxy 或 https.proxy 来配置，因为这些是针对 HTTP/HTTPS 协议的代理设置。

要为 SSH 协议设置代理，可以采用以下两种方法：

#### 使用环境变量和代理工具

> 如 proxychains

使用工具 proxychains、proxychains-ng 或类似的，使得 SSH 连接通过 SOCKS 或 HTTP 代理。

- 例如，运行命令：
  text
  `proxychains git clone git@github.com:user/repo.git`
- 这要求你已经配置好 proxychains 让它指向你的代理服务器。

## 修改 SSH 配置文件使用代理命令

在 `~/.ssh/config` 文件中为 GitHub 主机配置代理，通过 ProxyCommand 使用代理工具（如 nc/netcat 或 corkscrew）连接代理服务器。

示例（使用 SOCKS5 代理，例如代理在 127.0.0.1 端口 1080）：

text

`Host github.com Hostname ssh.github.com Port 443 ProxyCommand nc -x 127.0.0.1:1080 %h %p`

或者使用 corkscrew 工具配置 HTTP 代理：

text

`Host github.com Hostname ssh.github.com Port 443 ProxyCommand corkscrew 127.0.0.1 8080 %h %p`

注意：

- GitHub 的 SSH 可以使用端口 443（HTTPS 端口）绕过防火墙限制。
- 需要安装并配置好 nc (netcat) 或 corkscrew。
- 这种方法是最常见为 ssh 连接设置代理的方式。

这样配置后，所有通过 SSH 协议访问 github.com 的 Git 命令都会通过代理服务器转发，实现代理访问。

如果需要更具体的工具或命令配置，可进一步说明。