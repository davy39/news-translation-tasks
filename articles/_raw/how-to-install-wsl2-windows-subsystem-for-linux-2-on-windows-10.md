---
title: How to Install WSL2 (Windows Subsystem for Linux 2) on Windows 10
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-16T17:30:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/install-WSL2--2-.png
tags:
- name: Linux
  slug: linux
- name: Windows
  slug: windows
seo_title: null
seo_desc: "Linux is a widely used operating system and is quite important for developers.\
  \ \nThere are times when you might need to have both operating systems – Windows\
  \ and Linux – either for work, study, or even just experimentation. \nLuckily, Windows\
  \ provides ..."
---

Linux is a widely used operating system and is quite important for developers. 

There are times when you might need to have both operating systems – Windows and Linux – either for work, study, or even just experimentation. 

Luckily, Windows provides a convenient utility for using Linux along side Windows. This utility is called WSL (Windows Subsystem for Linux). Its recent version is WSL2 and in this guide we'll discuss it in detail. 

We will cover:

* What is WSL2 and what are its advantages?
* How to install WSL2 on Windows 10 with default settings.
* How to install WSL2 with a specific Linux distro.

## What is WSL2?

Windows Subsystem for Linux provides a compatibility layer that lets you run Linux binary executables natively on Windows. 

**WSL2 (Windows Subsystem for Linux version 2)** is the latest version of WSL. WSL2 architecture replaces WSL's architecture by using a lightweight virtual machine. In the new version, you can run an actual Linux kernel which improves overall performance.

### Advantages of using WSL

There are some advantages of WSL over a traditional VM setup:

* The setup for WSL is simple and not time consuming.
* It is light weight compared to VMs where you have to allocate resources from the host machine.
* You don't need to install any ISO or virtual disc image for Linux machines which tend to be heavy files.
* You can use Windows and Linux side by side.

## How to Install WSL2

First, enable the `windows subsystem for Linux` option in settings. 

* Go to Start. Search for "Turn Windows features on or off."
* Check the option Windows Subsystem for Linux.	

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-42.png)
_Turn Windows features on or off._

Next, open your command prompt and provide the installation commands.

* Open Command Prompt as an administrator.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-47.png)

* Run the command below:

```bash
wsl --install
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-31.png)

Note: By default, **Ubuntu** will be installed. But you can install any distro of your choice. We'll see later how.

Once installation is complete, you'll need to reboot your Windows machine. So, restart your Windows machine.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-32.png)

After restarting, you might see a window like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-43.png)

Once installation of Ubuntu is complete, you'll be prompted to enter your username and password.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-35.png)

And, that's it! You are ready to use Ubuntu.

Launch Ubuntu by searching from the start menu.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-44.png)

And here we have our Ubuntu instance launched.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-46.png)
_Ubuntu launched via WSL2_

## How to Install a Specific Linux Distro

If you use the default method as shown above, Ubuntu will be installed. You can find the available list of distros by running the below command on the Windows command prompt:

```bash
wsl --list --online
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-33.png)
_List the online available Linux distros_

To install a specific distro, use the command below:

```bash
wsl --install -d DISTRO-NAME
```

For example, to install Debian, the command would be modified as follows:

```bash
wsl --install -d Debian
```

Follow the prompts and the specific distribution will be installed.

**Tip**: You can also look for updates as shown below:

```bash
wsl --update
```

Check the status by launching Windows PowerShell.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-37.png)
_Check status of WSL_

## Wrapping up

WSL is a great utility to use Linux on a native Windows machine. It gives room for learning specially to those who are just starting out. I hope you found this article helpful.

Let's connect on [Twitter](https://twitter.com/hira_zaira)!

Read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Let's [chat on Discord.](https://discordapp.com/users/Zaira_H#2603)

