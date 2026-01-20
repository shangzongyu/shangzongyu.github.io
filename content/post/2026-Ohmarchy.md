---
title: "Ohmarchy"
description: "Ohmarchy Linux Software"
date: 2026-01-20T10:30:25+08:00
image: 
math: 
license: 
hidden: false
comments: true
draft: true
---

> Will List My Use software On Ohmarchy Linux.

## Editor

- Visual Studio Code
- Antigravity
- NeoVim

## Broswer

- Chrominum
- Google Chrome

## DataBase

### MySQL

> Use Docker to install.
> Why Use Docker, because install too complext, can't use pacman to install.
> Instead of mariadb, but i only want to use MySQL.

```sh
docker run --name mysql-server \
  -e MYSQL_ROOT_PASSWORD=my-secret-pw \
  -p 3306:3306 \
  -d mysql:8.0
```

Breakdown of the flags:

- --name mysql-server: Gives your container a friendly name.
- -e MYSQL_ROOT_PASSWORD=...: Sets your root password immediately.
- -p 3306:3306: Maps your physical machine's port 3306 to the container's port 3306.
- -d: Runs the container in the background (detached).

> mysql:8.0: Specifies the exact version. (Use mysql:5.7 if you want the older version).

#### 1. Persisting Your Data

By default, if you delete the container, your data is gone. To keep your databases safe on your Arch filesystem, use a Volume:

```sh
docker run --name mysql-server \
  -v /my/own/datadir:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=my-secret-pw \
  -p 3306:3306 \
  -d mysql:8.0
```

> Replace /my/own/datadir with a folder path on your computer.)

#### Managing the Database

| Action | Command |
|--------|---------|
| Check if running | docker ps |
| Enter MySQL Shell | docker exec -it mysql-server mysql -p | | Stop MySQL | docker stop mysql-server |
| Start MySQL again | docker start mysql-server |
| View Logs | docker logs mysql-server |

### Install MySQL Client

```sh
paru -S mysql-clients80

# command lint
paru -S mycli

```

### PostgreSQL

> Use pacman

#### 1. Install

Update your system and install the PostgreSQL package from the official repositories:

```sh
sudo pacman -Syu postgresql
```

#### 2. Iitialize the Database Cluster

Before starting the service, you must initialize the data directory. Switch to the postgres user to run the initdb command:

```sh
sudo -u postgres initdb -D /var/lib/postgres/data
```

> Note: You can add --locale $LANG -E UTF8 if you want to ensure specific locale settings.

### 3. Start and Enable the Service

Use systemctl to start the database server immediately and enable it to run at every system boot:

```sh
sudo systemctl enable --now postgresql
```

To verify it is running correctly, use: `sudo systemctl status postgresql`.

#### 4. Initial Configuration (Optional)

By default, there is no password for the postgres user. You can set one by entering the PostgreSQL shell:

1. Access the shell: `sudo -u postgres psql`
2. Set password: `\password postgres`
3. Exit: `\q`

#### 5. Create a New User and Database

It is best practice to create a separate user and database for your applications rather than using the default admin account:

1. Create User: `sudo -u postgres createuser --interactive`
2. Create Database: `sudo -u postgres createdb my_database`

> For more advanced configuration, refer to the [PostgreSQL ArchWiki page](https://wiki.archlinux.org/title/PostgreSQL).
