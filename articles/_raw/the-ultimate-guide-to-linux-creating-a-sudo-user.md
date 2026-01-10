---
title: The Ultimate Guide to Linux - Creating a Sudo User
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-18T17:05:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-linux-creating-a-sudo-user
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fe6740569d1a4ca4564.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: sudo stands for either "superuser do" or "switch user do", and sudo users
  can execute commands with root/administrative permissions, even malicious ones.
  Be careful who you grant sudo permissions to – you are quite literally handing them
  the key your...
---

`sudo` stands for either "superuser do" or "switch user do", and `sudo` users can execute commands with root/administrative permissions, even malicious ones. Be careful who you grant `sudo` permissions to – you are quite literally handing them the key your house.

Before creating a new `sudo` user, you must first create a new user.

## How to Create a New User

### Use `adduser` or `useradd` to add a new user

```text
sudo adduser username
```

Be sure to replace `username` with the user that you want to create. Also, note that to create a new user, you must also be a `sudo` user yourself.

### Use `passwd` to update the new user's password

```text
sudo passwd username
```

A strong password is highly recommended!

## Give the New User Sudo Permissions

After creating a new user, add them to the appropriate group using the `usermod` command.

### On Debian systems (Ubuntu / Linux Mint / ElementryOS), add users to the `sudo` group

```text
sudo usermod -aG sudo username
```

### On RHEL based systems (Fedora / CentOS), add users to the `wheel` group

```text
sudo usermod -aG wheel username
```

## How to Delete a User

To delete a user, use the following commands.

### Debian based systems (Ubuntu / Linux Mint / ElementryOS)

```text
sudo deluser username
```

### RHEL based systems (Fedora / CentOS)

```text
sudo userdel username
```

That's all you need to know about creating a new `sudo` user in Linux. And remember, "With great power comes great responsibility."

