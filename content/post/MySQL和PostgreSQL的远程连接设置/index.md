---
title: MySQL 和 PostgreSQL 的远程连接设置
description: 本文介绍 MySQL 和 PostgreSQL 数据库如何设置远程连接。
slug: mysql-postgresql
date: 2024-12-02 02:41:53+0000
image:
tags:
  - postgresql
  - mysql
weight: 1
---
本文介绍 MySQL 和 PostgreSQL 数据库如何设置远程连接。

我的环境如下：

- OS：Ubuntu 22.04
- DB：
  - MySQL 8.0.37
  - PostgreSQL 14.12

## MySQL

MySQL 想要远程从外部连接，需要做一些设置，修改配置文件中的绑定端口，允许远不端口访问，具体步骤如下：

1. 打开 MySQL 的配置文件 `/etc/mysql/mysql.conf.d/mysqld.cnf`
2. 修改 `bind-address` 为 `0.0.0.0` (如果没有，在 `[mysqld]` 下新添加 `bind-address = 0.0.0.0`)
3. 保存配置文件，并且重启数据库
4. 确保防火墙开放了 MySQL 默认端口 3306

> `mysqld.cnf` 通常位于 `/etc/mysql/mysql.conf.d/mysqld.cnf` 或者 `/etc/my.cnf`。

为远程连接新建一个用户：

```sql
-- 创建用户(username)并设置密码(password)，`%` 表示允许任何主机连接:
CREATE USER 'username'@'%' IDENTIFIED BY 'password';

-- 授权
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%';

-- MySQL 8.0 之前的版本需要刷新权限，8.0 之后的版本 GRANT 语句会自动刷新权限
-- FLUSH PRIVILEGES;
```

> 注意：MySQL 8.0 及以后的版本使用 GRANT 语句会自动刷新权限，不需要手动执行 FLUSH PRIVILEGES。只有在使用 INSERT、UPDATE 或 DELETE 直接修改授权表时，才需要执行 FLUSH PRIVILEGES。

## PostgreSQL

PostgreSQL 允许外部连接，需要做一些设置：

1. 打开配置 `/etc/postgresql/14/main/postgresql.conf`
2. 修改 `listen_addresses` 为 `0.0.0.0`
3. 保存配置文件，并且重启数据库
4. 确保防火墙开放了 PostgreSQL 默认端口 5432

> `postgresql.conf` 通常位于 `/etc/postgresql/<version>/main/postgresql.conf`，我使用的版本是 14，因此文件路径为 `/etc/postgresql/14/main/postgresql.conf`。

除了上面的操作外还需要修改 `pg_hba.conf` 在文件下添加：

```ini
host    all             all             192.168.0.0/16      md5
```

> 192.168.0.0/16 允许访问的 IP 网段。

为远程连接新建一个用户：

```sql
-- 新建用户
CREATE ROLE username WITH LOGIN PASSWORD 'password';

-- 授权数据库连接权限
GRANT CONNECT ON DATABASE database_name TO username;

-- 授权用户操作数据库
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;

-- 切换到目标数据库后授权 schema 权限
\c database_name
GRANT ALL ON ALL TABLES IN SCHEMA public TO username;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO username;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO username;
```

## 防火墙配置

Ubuntu 默认使用 UFW (Uncomplicated Firewall) 作为防火墙。需要开放数据库端口：

```bash
# MySQL (3306 端口)
sudo ufw allow 3306/tcp

# PostgreSQL (5432 端口)
sudo ufw allow 5432/tcp

# 查看防火墙状态
sudo ufw status
```

## 验证连接

MySQL 连接验证：

```bash
# 命令行连接
mysql -h <服务器IP> -u username -p

# 或使用完整 URL
mysql mysql://username:password@<服务器IP>:3306/database_name
```

PostgreSQL 连接验证：

```bash
# 命令行连接
psql -h <服务器IP> -U username -d database_name

# 或使用完整 URL
psql postgresql://username:password@<服务器IP>:5432/database_name
```

## 常见问题排查

1. 连接被拒绝
   - 检查数据库服务是否运行：`systemctl status mysql` 或 `systemctl status postgresql`
   - 检查防火墙配置：`sudo ufw status`
   - 确认配置文件修改正确并已重启服务
   - 检查服务器 IP 是否正确

2. 认证失败
   - MySQL：检查用户名和主机设置是否匹配
   - PostgreSQL：检查 `pg_hba.conf` 中的认证方法和允许的 IP 范围

3. 数据库服务无法启动
   - 检查错误日志：
     - MySQL：`/var/log/mysql/error.log`
     - PostgreSQL：`/var/log/postgresql/postgresql-14-main.log`
   - 确认配置文件语法正确
