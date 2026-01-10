---
title: How to Use Linux on a Windows Machine – 5 Different Approaches
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-06-09T15:03:52.000Z'
originalURL: https://freecodecamp.org/news/5-ways-to-use-linux-on-a-windows-machine
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/5-ways-to-use-Linux-on-a-Windows-machine.png
tags:
- name: Linux
  slug: linux
- name: Windows
  slug: windows
- name: WSL
  slug: wsl
seo_title: null
seo_desc: "As a developer, you might need to run both Linux and Windows side by side.\
  \ Luckily, there are a number of ways you can get the best of both worlds without\
  \ getting different computers for each operating system. \nIn this article, we'll\
  \ explore a few wa..."
---

As a developer, you might need to run both Linux and Windows side by side. Luckily, there are a number of ways you can get the best of both worlds without getting different computers for each operating system. 

In this article, we'll explore a few ways to use Linux on a Windows machine. Some of them are browser-based or cloud-based that do not need any installation prior to using them.

Here are the methods we'll be discussing:

* Dual boot
* Windows Subsystem for Linux (WSL)
* Virtual Machines (VM)
* Browser-based solutions
* Cloud-based solutions

## Option 1: "Dual-boot" Linux + Windows 

With dual boot, you can install Linux alongside Windows on your computer, allowing you to choose which operating system to use at startup. 

This requires partitioning your hard drive and installing Linux on a separate partition. With this approach, you can only use one operating system at a time.

If this sounds like the way you want to go, [here is a useful tutorial](https://www.freecodecamp.org/news/how-to-dual-boot-windows-10-and-ubuntu-linux-dual-booting-tutorial/) on setting up dual boot on Windows 10.

## Option 2: Use Windows Subsystem for Linux (WSL)

Windows Subsystem for Linux provides a compatibility layer that lets you run Linux binary executables natively on Windows.

Using WSL has some advantages:

* The setup for WSL is simple and not time consuming.
* It is lightweight compared to VMs where you have to allocate resources from the host machine.
* You don't need to install any ISO or virtual disc image for Linux machines which tend to be heavy files.
* You can use Windows and Linux side by side.

If this sounds like the right option for you, [here is a detailed guide](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) on how to install and use WSL.

## Option 3: Use a Virtual Machine (VM)

A virtual machine (VM) is a software emulation of a physical computer system. It allows you to run multiple operating systems and applications on a single physical machine simultaneously. Here's a detailed explanation of VMs:

You can use virtualization software such as Oracle VirtualBox or VMware to create a virtual machine running Linux within your Windows environment. This allows you to run Linux as a guest operating system alongside Windows.

VM software provides options to allocate and manage hardware resources for each VM, including CPU cores, memory, disk space, and network bandwidth. You can adjust these allocations based on the requirements of the guest operating systems and applications.

Here are some of the options available for virtualization:

* [Oracle virtual box](https://www.virtualbox.org/)
* [Multipass](https://multipass.run/)
* [VMware workstation player](https://www.vmware.com/content/vmware/vmware-published-sites/us/products/workstation-player.html.html)

## Option 4: Use a Browser-based Solution

Browser based solutions are particularly useful for quick testing, learning, or accessing Linux environments from devices that don't have Linux installed.

You can either use online code editors or web based terminals to access Linux. Note that you usually don't have full administration privileges in these cases. 

### Online code editors

Online code editors offer editors with built-in Linux terminals. While their primary purpose is coding, you can also utilize the Linux terminal to execute commands and perform tasks.

[Replit](https://replit.com/) is an example of an online code editor, where you can write your code and access the Linux shell at the same time.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/replit.gif)
_Replit provides a code editor and a Linux shell._

### Web-based Linux terminals

Online Linux terminals allow you to access a Linux command-line interface directly from your browser. These terminals provide a web-based interface to a Linux shell, enabling you to execute commands and work with Linux utilities. 

One such example is [JSLinux](https://jslinux.org/). The screenshot below shows a ready to use Linux environment:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/jslinux.gif)
_Accessing Linux via JSLinux_

## Option 5: Use a Cloud-based Solution

Instead of running Linux directly on your Windows machine, you can consider using cloud-based Linux environments or virtual private servers (VPS) to access and work with Linux remotely. 

Services like Amazon EC2, Microsoft Azure, or DigitalOcean provide Linux instances that you can connect to from your Windows computer. Note that some of these services offer free tiers, but they are not usually free in the long run.

## How to Choose the Correct Method

The choice is totally dependent on your use case. But there are some factors that may help you decide which option works the best for you. Let's discuss them:

* Access level/elevated privilege: If you require full administrative privileges, it is better to skip the browser-based solutions. WSL, dual booting, VMs, and cloud-based solutions provide you with full administrative control.
* Cost: Cloud-based solutions offer services against a subscription fee. This cost varies depending on the choice of operating system, hardware specs of the machine, traffic, and so on. If you are on a tight budget, cloud-based solutions might not be the best.
* Scalability: If you are just starting, but plan to do resource exhaustive development in the future, you can always scale up the physical specs of your machine. Some options that support upgrading are cloud-based solutions and VMs. You can add more processors or increase the RAM as per your needs.
* Current system's hardware specs: If your current system has lower RAM and storage, running VMs can make the system heavy. It would be better to opt for cloud-based or browser based solutions.
* Switching: If you don't plan to use Windows and Linux side by side, dual-boot can be a really good option. It offers a complete and focused Linux experience.

## My Setup

I am using Ubuntu VM installed through VMWare workstation player. It is doing a great job as I can frequently switch between two operating systems. It was also simple to setup and I can enjoy the admin privileges as well!

![Image](https://www.freecodecamp.org/news/content/images/2023/06/my-set.gif)

## Wrapping Up

I hope you found this article helpful. What’s your favorite thing you learned from this tutorial? I would love to connect with you on any of these [platforms](https://zaira_.bio.link/). 📧

See you in the next tutorial, happy coding 😁

