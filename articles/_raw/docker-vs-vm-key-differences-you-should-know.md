---
title: Docker vs Virtual Machine (VM) – Key Differences You Should Know
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2022-10-04T16:48:57.000Z'
originalURL: https://freecodecamp.org/news/docker-vs-vm-key-differences-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/docker-vs-vm-diff.png
tags:
- name: container
  slug: container
- name: containerization
  slug: containerization
- name: Docker
  slug: docker
- name: virtual machine
  slug: virtual-machine
seo_title: null
seo_desc: 'In this guide, you''ll learn the differences between a virtual machine
  and a Docker container.

  Both virtual machines and containers help replicate the development environment,
  and manage dependencies and configurations better. But there are certain di...'
---

In this guide, you'll learn the differences between a **virtual machine** and a **Docker** container.

Both virtual machines and containers help replicate the development environment, and manage dependencies and configurations better. But there are certain differences you should be aware of that will help you choose a VM or a Docker container depending on the application.

Over the next few minutes, we'll go over how virtual machines and Docker containers work, and then summarize the key differences between the two.

Let's begin!

## Challenges in Application Development and Deployment

When you work as part of a development team, each application requires installation of multiple third-party software and packages. In order to collaborate and work together, every developer on the team should configure their local development environment.

However, setting up the development environment is a tedious process. The installation steps can be potentially different depending on the operating system and system configuration. Even during deployment, you have to configure the same environment on the server.

Different applications also require multiple versions of a specific software, say, PostgreSQL. In such cases, managing dependencies across applications becomes difficult.

To address the above challenges, it really helps if the applications run in isolated environments that you can replicate easily—independent of the system configuration. Both Virtual Machines (VMs) and Docker containers help you achieve this. Let's learn how!

## How Does a Virtual Machine Work?

A **Virtual Machine** or **VM** is the emulation of a physical computer inside a host machine. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/1.png)
_How a VM works (image by the author)_

Running on top of the host operating system is a piece of software called a hypervisor that controls the VM instances. Each VM instance has its own guest operating system. The applications run inside this isolated environment. 

You can have multiple VMs, each running a different application on a different operating system.

## How Does a Docker Container Work?

Recently, container technology has revolutionized the software development process and the way development and operation teams work together. With time, Docker has become the go-to choice for containerizing applications.

Dockers containers are analogous to physical containers that you can use to store, package, and transport goods. But instead of tangible goods, they’re containers for software applications. 🙂

A docker container is a portable unit of software—that has the application—along with the associated dependency and configuration. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/2.png)
_How containers work (image by the author)_

Unlike a VM, Docker containers _do not_ boot up their own guest OS. Rather, they run on top of the host operating system. This is facilitated by a container engine.

## Docker vs VM – A Comprehensive Comparison

### 1️⃣ Virtualization

From our understanding thus far, both virtual machines and Docker containers provide isolated environments to run applications. The key difference between the two is in _how_ they facilitate this isolation.

Recall that a VM boots up its own guest OS. Therefore, it virtualizes both the operating system kernel and the application layer. 

A Docker container virtualizes _only_ the application layer, and runs on top of the host operating system.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/3.png)
_Container vs VM (image by the author)_

### 2️⃣ Compatibility

A virtual machine uses its own operating system and is _independent_ of the host operating system that it’s running on.  Therefore, a VM is compatible with all operating systems. 

A Docker container, on the other hand, is compatible with _any_ Linux distribution. You may run into some problems running Docker on a Windows machine or an older Mac.

### 3️⃣ Size

A Docker image is lightweight and is typically in the order of kilobytes. 

**💡 Note**: A Docker image denotes the artifact containing the application, its associated dependencies, and configuration. A running instance of the Docker image is called a container.

A VM instance can be as large as a few gigabytes or even terabytes.

### 4️⃣ Performance

In terms of performance, Docker containers provide near-native performance. Because they are lightweight, you can start them in a few milliseconds. 

Starting a VM is equivalent to setting up a standalone machine inside your computer. It can take as long as a few minutes to start a VM instance.

### 5️⃣ Security

Docker containers run on top of the host operating system. Therefore, if the host OS is susceptible to security vulnerabilities, so are the Docker containers.

Virtual machines, on the other hand, boot up their own operating system, and are more secure. Recall: each virtual machine is a fully blown machine running inside another. If you have stringent security constraints to be met for sensitive applications, you should consider using a virtual machine instead.

### 6️⃣ Replicability

The next factor we'll consider is the ease with which you can replicate the isolated environments provided by VMs and containers. We can infer the ease of replicability from our earlier discussions on **size** and **performance**. 

When there are multiple applications, each of which should run on a VM instance, using VMs can be **inefficient** and **resource intensive**. Docker containers, by virtue of being lightweight and performant, are preferred when you need to run multiple applications. ✅

## Summing Up

I hope this tutorial helped you understand how Docker containers and VMs work, and the key differences between the two. 

Here's a summary of what you've learned:

|Feature|Docker| Virtual Machine (VM)|
|------|---------|------------|
|Compatibility| Works best with Linux distributions|All operating systems|
|Size| Light in weight|Substantially larger – of the order of Gigabytes or more|
|Virtualization|Only the applications layer |Both the OS kernel and applications layers|
|Performance|Easy to start containers (typically takes milliseconds)|Takes longer to start a VM instance|
|Security|Less secure|Relatively more secure|
|Replicability|Easy to replicate. You can pull Docker images corresponding to the various applications|Difficult to replicate, especially with increasing number of VM instances|


Thank you for reading this far. See you all soon in another tutorial! 😄

