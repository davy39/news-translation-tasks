---
title: Introduction to Linux
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-02-23T13:49:13.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/linux.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'If you''re new to Linux, this course is for you.

  In this comprehensive course, you''ll learn many of the tools used every day by
  both Linux SysAdmins and the millions of people running Linux distributions like
  Ubuntu on their PCs. This course will teac...'
---

If you're new to Linux, this course is for you.

In this comprehensive course, you'll learn many of the tools used every day by both Linux SysAdmins and the millions of people running Linux distributions like Ubuntu on their PCs. This course will teach you how to navigate Linux's Graphical User Interfaces and powerful command line tool ecosystem.

This content of this course was developed by the Linux Foundation (They call it LFS101x). I've taken their primarily text-based course and turned it into a video-based course.

You can either read the text version of the course right here or you can watch the video version of the course on the freeCodeCamp.org YouTube channel (6-hour watch).

%[https://www.youtube.com/watch?v=sWbUDq4S6Y8]

This tutorial falls under the [Creative Commons BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

So if you want the text version of the course, read on!

## **Chapter 1**

By the end of this chapter, you should be able to:

* Describe the software environment required for this course.
* And describe the three major Linux distribution families.

### Course Requirements

In order to fully benefit from this course, you will need to have at least one Linux distribution installed (if you are not already familiar with the term distribution, as it relates to Linux, you soon will be!).

You are about to learn some more details about the many available Linux distributions. Because there are literally hundreds of distributions, I'm not covering them all in this course. Instead, I will focus on the three major distribution families.

The families and representative distributions this course will focus on are:

* **Red Hat Family Systems** (including **CentOS** and **Fedora**)
* **SUSE Family Systems** (including **openSUSE**)
* **Debian Family Systems** (including **Ubuntu** and **Linux Mint**).

![Three screenshots showing Ubuntu, CentOS, and OpenSUSE desktops](https://courses.edx.org/assets/courseware/v1/fe27a9c47f2e272c238dc227cb749528/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnomedts.png)
_Ubuntu, CentOS, and openSUSE Desktops_

# 

### Focus on Three Major Linux Distribution Families  


I'm about to tell you more about Red Hat, SUSE, and Debian. While this course focuses on these three major Linux distribution families, as long as there are talented contributors, the families of distributions and the distributions within these families will continue to change and grow. People see a need, and develop special configurations and utilities to respond to that need. Sometimes that effort creates a whole new distribution of Linux. Sometimes, that effort will leverage an existing distribution to expand the members of an existing family.

![The Linux Kernel Distribution Families and Individual Distributions](https://courses.edx.org/assets/courseware/v1/1d8c97abd237dcd44a5fe5464f6521ac/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_The_Linux_Kernel_Distribution_Families_and_Individual_Distributions.png)
_The Linux Kernel Distribution Families and Individual Distributions_

### The Red Hat Family

Red Hat Enterprise Linux (or RHEL [pronounced "rel"]) heads the family that includes CentOS, CentOS Stream, Fedora and Oracle Linux.

Fedora has a close relationship with RHEL and contains significantly more software than Red Hat's enterprise version. One reason for this is that a diverse community is involved in building Fedora, with many contributors who do not work for Red Hat. Furthermore, it is used as a testing platform for future RHEL releases.

![The Red Hat Family](https://courses.edx.org/assets/courseware/v1/8463dfd1fc8eb8ba7ff06731abc38382/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_The_Red_Hat_Family.png)
_The Red Hat Family_

In this course, we'll mainly use CentOS Stream from the Red Hat family.

The basic version of CentOS is also virtually identical to RHEL, the most popular Linux distribution in enterprise environments. However, CentOS 8 has no more scheduled updates. The replacement is CentOS 8 Stream. 

### Key Facts About the Red Hat Family

Some of the key facts about the Red Hat distribution family are:

* Fedora serves as an upstream testing platform for RHEL.
* CentOS is a close clone of RHEL, while Oracle Linux is mostly a copy with some changes.
* It supports hardware platforms such as Intel x86, Arm, Itanium, PowerPC, and IBM System z.
* It uses the yum and dnf RPM-based yum package managers (discussed more later) to install, update, and remove packages in the system.
* RHEL is widely used by enterprises which host their own systems.

### The SUSE Family

The relationship between SUSE  (SUSE Linux Enterprise Server, or SLES) and openSUSE is similar to the one described between RHEL, CentOS, and Fedora.

![The SUSE Family](https://courses.edx.org/assets/courseware/v1/ffd8ff6c0d84899812026c2e65efb0e1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_screen19.jpg)
_The SUSE Family_

We use openSUSE as the reference distribution for the SUSE family, as it is available to end users at no cost. Because the two products are extremely similar, the material that covers openSUSE can typically be applied to SLES with few problems.

### Key Facts About the SUSE Family

Some of the key facts about the SUSE family are listed below:

* SUSE Linux Enterprise Server (SLES) is upstream for openSUSE.
* It uses the RPM-based zypper package manager (we cover it in detail later) to install, update, and remove packages in the system.
* It includes the YaST (Yet Another Setup Tool) application for system administration purposes.
* SLES is widely used in retail and many other sectors.

### The Debian Family

The Debian distribution is upstream for several other distributions, including Ubuntu. In turn, Ubuntu is upstream for Linux Mint and a number of other distributions. It is commonly used on both servers and desktop computers. Debian is a pure open source community project (not owned by any corporation) and has a strong focus on stability.

Debian provides by far the largest and most complete software repository to its users of any Linux distribution.

![The Debian Family](https://courses.edx.org/assets/courseware/v1/223d3c300d6cdd86ae66e8c2b9faa265/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_screen20.jpg)
_The Debian Family_

Ubuntu aims at providing a good compromise between long term stability and ease of use. Since Ubuntu gets most of its packages from Debian’s stable branch, it also has access to a very large software repository. For those reasons, we will use Ubuntu LTS (Long Term Support) as the reference to Debian family distributions for this course.

### Key Facts About the Debian Family

Some key facts about the Debian family are listed below:

* The Debian family is upstream for Ubuntu, and Ubuntu is upstream for Linux Mint and others.
* It uses the DPKG-based APT package manager (using apt, apt-get, apt-cache, etc., which we cover in detail later) to install, update, and remove packages in the system.
* Ubuntu has been widely used for cloud deployments.
* While Ubuntu is built on top of Debian and is GNOME-based under the hood, it differs visually from the interface on standard Debian, as well as other distributions.

### Chapter Summary

* There are three major distribution families within Linux: **Red Hat,** **SUSE** and **Debian**. In this course, we will work with representative members of all of these families throughout.

## **Chapter 2: Linux Philosophy and Concepts**

### Learning Objectives

By the end of this chapter, you should be able to:

* Define the common terms associated with Linux.
* Discuss the components of a Linux distribution.

### The Power of Linux

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V010000_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Introduction

In order for you to get the most out of this course, we recommend that you have Linux installed on a machine that you can use throughout this course. You can use this brief installation guide "_[Preparing Your Computer for Linux Training](https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2020+type@asset+block@Preparing_Your_Computer_for_Linux_Training.pdf)_". It will help you to select a Linux distribution to install, decide on whether you want to do a stand-alone pure Linux machine or a dual-boot one, whether to do a physical or virtual install, etc. And then it guides through the steps. I'll also cover installation soon.

We have not covered everything in great detail, but keep in mind that most of the documentation in Linux is actually already on your system in the form of man pages, which we will discuss in great detail later. Whenever you do not understand something or want to know more about a command, program, topic, or utility, you can just type **man <topic>** at the command line. We will assume you are thinking this way and not constantly repeat "For more information, look at the man page for **<topic>**".

On a related note, throughout the course we use a shorthand that is common in the open source community. When referring to cases where the user has to make a choice of what to enter (e.g. name of a program or file), we use the short hand '**foo**' to represent **<insert file name here>**. So beware, we are not actually suggesting that you manipulate files or install services called '**foo**'!

Best way to learn Linux is by doing it. So make sure to try things out yourself as you follow along.

You'll need to have a Linux system up and running that can either be a native Linux system on your hardware, one running through a live USB stick or CD or virtual machine running through a hypervisor.

We’ll show you all these methods, so let’s get going.

### Video: Linux Terminology

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V006600_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Linux Distributions 

Suppose you have been assigned to a project building a product for a Linux platform. Project requirements include making sure the project works properly on the most widely used Linux distributions. To accomplish this, you need to learn about the different components, services, and configurations associated with each distribution. We are about to look at how you would go about doing exactly that.

So, what is a Linux distribution and how does it relate to the Linux kernel?

The Linux kernel is the core of the operating system. A full Linux distribution consists of the kernel plus a number of other software tools for file-related operations, user management, and software package management. Each of these tools provides a part of the complete system. Each tool is often its own separate project, with its own developers working to perfect that piece of the system.

While the most recent Linux kernel (and earlier versions) can always be found in [The Linux Kernel Archives](https://www.kernel.org/), Linux distributions may be based on different kernel versions. For example, the very popular RHEL 8 distribution is based on the 4.18 kernel, which is not new, but is extremely stable. Other distributions may move more quickly in adopting the latest kernel releases. It is important to note that the kernel is not an all or nothing proposition, for example, RHEL/CentOS have incorporated many of the more recent kernel improvements into their older versions, as have Ubuntu, openSUSE, SLES, etc.

Examples of other essential tools and ingredients provided by distributions include the C/C++ and Clang compilers, the gdb debugger, the core system libraries applications need to link with in order to run, the low-level interface for drawing graphics on the screen, as well as the higher-level desktop environment, and the system for installing and updating the various components, including the kernel itself. And all distributions come with a rather complete suite of applications already installed.

![Distribution roles](https://courses.edx.org/assets/courseware/v1/be89578552325fd81fb6a9a6b613afe9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/distroroles.png)
_Distribution Roles_

### Services Associated with Distributions

The vast variety of Linux distributions are designed to cater to many different audiences and organizations, according to their specific needs and tastes. However, large organizations, such as companies and governmental institutions and other entities, tend to choose the major commercially-supported distributions from Red Hat, SUSE, and Canonical (Ubuntu).

CentOS and CentOS Stream are popular free (as in no cost) alternatives to Red Hat Enterprise Linux (RHEL) and are often used by organizations that are comfortable operating without paid technical support. Ubuntu and Fedora are widely used by developers and are also popular in the educational realm. Scientific Linux is favored by the scientific research community for its compatibility with scientific and mathematical software packages. Both CentOS variants are binary-compatible with RHEL; i.e. in most cases, binary software packages will install properly across the distributions.

Note that CentOS is planned to disappear at the end of 2021 in favor of CentOS Stream. However, there are at least two new RHEL-derived substitutes: Alma Linux and Rocky Linux which are establishing a foothold.

Many commercial distributors, including Red Hat, Ubuntu, SUSE, and Oracle, provide long term fee-based support for their distributions, as well as hardware and software certification. All major distributors provide update services for keeping your system primed with the latest security and bug fixes, and performance enhancements, as well as provide online support resources.

![Image](https://courses.edx.org/assets/courseware/v1/85a0445af315a7fb90444a2d3cd0e608/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch02_screen_24.jpg)
_Services Associated with Distributions_



### Chapter 2 Summary

You have completed Chapter 2. Let’s summarize the key concepts covered:

* Linux borrows heavily from the UNIX operating system, with which its creators were well-versed.
* Linux accesses many features and services through files and file-like objects.
* Linux is a fully multi-tasking, multi-user operating system, with built-in networking and service processes known as daemons.
* Linux is developed by a loose confederation of developers from all over the world, collaborating over the Internet, with Linus Torvalds at the head. Technical skill and a desire to contribute are the only qualifications for participating.
* The Linux community is a far reaching ecosystem of developers, vendors, and users that supports and advances the Linux operating system.
* Some of the common terms used in Linux are: **kernel**, **distribution**, **boot loader**, **service**, **filesystem**, **X Window system**, **desktop  environment**, and **command line**.
* A full Linux distribution consists of the kernel plus a number of other software tools for file-related operations, user management, and software package management.

## **Chapter 3: Linux Basics and System Startup**

By the end of this chapter, you should be able to:

* Identify Linux filesystems.
* Identify the differences between partitions and filesystems.
* Describe the boot process.
* Install Linux on a computer.

## The Boot Process

The Linux boot process is the procedure for initializing the system. It consists of everything that happens from when the computer power is first switched on until the user interface is fully operational.

Having a good understanding of the steps in the boot process may help you with troubleshooting problems, as well as with tailoring the computer's performance to your needs.

On the other hand, the boot process can be rather technical, and you can start using Linux without knowing all the details.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-373.png)
_The boot process._

### BIOS - The First Step

Starting an x86-based Linux system involves a number of steps. When the computer is powered on, the **B**asic **I**nput/**O**utput **S**ystem (**BIOS**) initializes the hardware, including the screen and keyboard, and tests the main memory. This process is also called **POST** (**P**ower **O**n **S**elf **T**est).

![BIOS](https://courses.edx.org/assets/courseware/v1/f02a193180acffca543bf8f69870cc79/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen16.jpg)
_BIOS_

  
The BIOS software is stored on a ROM chip on the motherboard. After this, the remainder of the boot process is controlled by the operating system (OS).

### Master Boot Record (MBR) and Boot Loader

Once the POST is completed, the system control passes from the BIOS to the **boot** **loader**. The boot loader is usually stored on one of the hard disks in the system, either in the boot sector (for traditional BIOS/MBR systems) or the **EFI** partition (for more recent (Unified) **E**xtensible **F**irmware **I**nterface or **EFI/UEFI** systems). Up to this stage, the machine does not access any mass storage media. Thereafter, information on date, time, and the most important peripherals are loaded from the CMOS values (after a technology used for the battery-powered memory store which allows the system to keep track of the date and time even when it is powered off).

A number of boot loaders exist for Linux; the most common ones are **GRUB** (for **GR**and **U**nified **B**oot loader), **ISOLINUX** (for booting from removable media), and **DAS U-Boot** (for booting on embedded devices/appliances). Most Linux boot loaders can present a user interface for choosing alternative options for booting Linux, and even other operating systems that might be installed. When booting Linux, the boot loader is responsible for loading the kernel image and the initial RAM disk or filesystem (which contains some critical files and device drivers needed to start the system) into memory.

![Master Boot Record](https://courses.edx.org/assets/courseware/v1/b053b7b69e99a0c06ef0da7fd84236d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen20.jpg)
_Master Boot Record_

### Boot Loader in Action

The boot loader has two distinct stages:

For systems using the BIOS/MBR method, the boot loader resides at the first sector of the hard disk, also known as the **M**aster **B**oot **R**ecord (**MBR**). The size of the MBR is just 512 bytes. In this stage, the boot loader examines the **partition table** and finds a bootable partition. Once it finds a bootable partition, it then searches for the second stage boot loader, for example GRUB, and loads it into RAM (Random Access Memory). For systems using the EFI/UEFI method, UEFI firmware reads its Boot Manager data to determine which UEFI application is to be launched and from where (i.e. from which disk and partition the EFI partition can be found). The firmware then launches the UEFI application, for example GRUB, as defined in the boot entry in the firmware's boot manager. This procedure is more complicated, but more versatile than the older MBR methods.

![Boot loader in action](https://courses.edx.org/assets/courseware/v1/abd1fcc0cc9a6fe48d886efdd98711ef/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen18.jpg)

The second stage boot loader resides under **/boot**. A splash screen is displayed, which allows us to choose which operating system (OS) to boot. After choosing the OS, the boot loader loads the kernel of the selected operating system into RAM and passes control to it. Kernels are almost always compressed, so its first job is to uncompress itself. After this, it will check and analyze the system hardware and initialize any hardware device drivers built into the kernel.

### Initial RAM Disk

The **initramfs** filesystem image contains programs and binary files that perform all actions needed to mount the proper root filesystem, like providing kernel functionality for the needed filesystem and device drivers for mass storage controllers with a facility called **udev** (for **u**ser **dev**ice), which is responsible for figuring out which devices are present, locating the device drivers they need to operate properly, and loading them. After the root filesystem has been found, it is checked for errors and mounted.

The **mount** program instructs the operating system that a filesystem is ready for use, and associates it with a particular point in the overall hierarchy of the filesystem (the **mount point**). If this is successful, the initramfs is cleared from RAM and the init program on the root filesystem (**/sbin/init**) is executed.

**init** handles the mounting and pivoting over to the final real root filesystem. If special hardware drivers are needed before the mass storage can be accessed, they must be in the initramfs image.

![The initial RAM disk](https://courses.edx.org/assets/courseware/v1/13f8548b13ebe15a19aa1a6c3964fceb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen22.jpg)
_The Initial RAM Disk_

### Text-Mode Login

Near the end of the boot process, **init** starts a number of text-mode login prompts. These enable you to type your username, followed by your password, and to eventually get a command shell. However, if you are running a system with a graphical login interface, you will not see these at first.

As you will learn in _Chapter 7: Command Line Operations_, the terminals which run the command shells can be accessed using the **ALT** key plus a **function** key. Most distributions start six text terminals and one graphics terminal starting with **F1** or **F2**. Within a graphical environment, switching to a text console requires pressing **CTRL-ALT** + the appropriate function key (with **F7** or **F1** leading to the GUI).

![Text-Mode Login](https://courses.edx.org/assets/courseware/v1/e35bea5a8c6b9a41453a0e01c5ca3077/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen26.jpg)
_Text-Mode Logins_

Usually, the default command shell is **bash** (the **GNU** **B**ourne **A**gain **Sh**ell), but there are a number of other advanced command shells available. The shell prints a text prompt, indicating it is ready to accept commands; after the user types the command and presses **Enter**, the command is executed, and another prompt is displayed after the command is done.

### The Linux Kernel

The boot loader loads both the **kernel** and an initial RAM–based file system (initramfs) into memory, so it can be used directly by the kernel.

![The Linux kernel](https://courses.edx.org/assets/courseware/v1/b953394cd3145a1bd239673dc5c5a5b7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen21.jpg)
_The Linux Kernel_

When the kernel is loaded in RAM, it immediately initializes and configures the computer’s memory and also configures all the hardware attached to the system. This includes all processors, I/O subsystems, storage devices, etc. The kernel also loads some necessary user space applications.

### /sbin/init and Services

Once the kernel has set up all its hardware and mounted the root filesystem, the kernel runs **/sbin/init**. This then becomes the initial process, which then starts other processes to get the system running. Most other processes on the system trace their origin ultimately to **init**; exceptions include the so-called kernel processes. These are started by the kernel directly, and their job is to manage internal operating system details.

Besides starting the system, **init** is responsible for keeping the system running and for shutting it down cleanly. One of its responsibilities is to act when necessary as a manager for all non-kernel processes; it cleans up after them upon completion, and restarts user login services as needed when users log in and out, and does the same for other background system services.

![/sbin/init and Services](https://courses.edx.org/assets/courseware/v1/640a31713f9fded06718cb06c468f685/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen24.jpg)
_/sbin/init and Services_

Traditionally, this process startup was done using conventions that date back to the 1980s and the System V variety of UNIX. This serial process had the system passing through a sequence of **runlevels** containing collections of scripts that start and stop services. Each runlevel supported a different mode of running the system. Within each runlevel, individual services could be set to run, or to be shut down if running.

However, all major distributions have moved away from this sequential runlevel method of system initialization, although they usually emulate many System V utilities for compatibility purposes. Next, we discuss the new methods, of which **systemd** has become dominant.

### Startup Alternatives

**SysVinit** viewed things as a serial process, divided into a series of sequential stages. Each stage required completion before the next could proceed. Thus, startup did not easily take advantage of the _parallel processing_ that could be done on multiple processors or cores.

Furthermore, shutdown and reboot was seen as a relatively rare event; exactly how long it took was not considered important. This is no longer true, especially with mobile devices and embedded Linux systems. Some modern methods, such as the use of **containers**, can require almost instantaneous startup times. Thus, systems now require methods with faster and enhanced capabilities. Finally, the older methods required rather complicated startup scripts, which were difficult to keep universal across distribution versions, kernel versions, architectures, and types of systems. The two main alternatives developed were:

**Upstart**

* Developed by Ubuntu and first included in 2006
* Adopted in Fedora 9 (in 2008) and in RHEL 6 and its clones

**systemd**

* Adopted by Fedora first (in 2011)
* Adopted by RHEL 7 and SUSE
* Replaced Upstart in Ubuntu 16.04

While the migration to **systemd** was rather controversial, it has been adopted by all major distributions, and so we will not discuss the older System V method or Upstart, which has become a dead end. Regardless of how one feels about the controversies or the technical methods of **systemd**, almost universal adoption has made learning how to work on Linux systems simpler, as there are fewer differences among distributions. We enumerate **systemd** features next.

### systemd Features

Systems with **systemd** start up faster than those with earlier **init** methods. This is largely because it replaces a serialized set of steps with aggressive parallelization techniques, which permits multiple services to be initiated simultaneously.

Complicated startup shell scripts are replaced with simpler configuration files, which enumerate what has to be done before a service is started, how to execute service startup, and what conditions the service should indicate have been accomplished when startup is finished. One thing to note is that **/sbin/init** now just points to **/lib/systemd/systemd**; i.e. **systemd** takes over the **init** process.

One **systemd** command (**systemctl**) is used for most basic tasks. While we have not yet talked about working at the command line, here is a brief listing of its use:

* Starting, stopping, restarting a service (using **httpd**, the Apache web server, as an example) on a currently running system:  
**$ sudo systemctl start|stop|restart httpd.service**
* Enabling or disabling a system service from starting up at system boot:  
**$ sudo systemctl enable|disable httpd.service**

In most cases, the **.service** can be omitted. There are many technical differences with older methods that lie beyond the scope of our discussion.

![systemd Logo](https://courses.edx.org/assets/courseware/v1/2a63469f639dfeaf697c55ca137ac1d9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/systemd.png)

## Linux Filesystems Basics

Think of a refrigerator that has multiple shelves that can be used for storing various items. These shelves help you organize the grocery items by shape, size, type, etc. The same concept applies to a filesystem, which is the embodiment of a method of storing and organizing arbitrary collections of data in a human-usable form.

Different types of filesystems supported by Linux:

* Conventional disk filesystems: **ext3**, **ext4**, **XFS**, **Btrfs**, **JFS**, **NTFS**, **vfat**, **exfat**, etc.
* Flash storage filesystems: **ubifs**, **jffs2**, **yaffs**, etc.
* Database filesystems
* Special purpose filesystems: **procfs**, **sysfs**, **tmpfs**, **squashfs**, **debugfs**, **fuse**, etc.

This section will describe the standard filesystem layout shared by most Linux distributions.

### Partitions and Filesystems

A **partition** is a physically contiguous section of a disk, or what appears to be so in some advanced setups.

A **filesystem** is a method of storing/finding files on a hard disk (usually in a partition).

One can think of a partition as a container in which a filesystem resides, although in some circumstances, a filesystem can span more than one partition if one uses symbolic links, which we will discuss much later.

A comparison between filesystems in Windows and Linux is given in the accompanying table:

<table border="0" width="100%" height="200" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 750px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 14px;">&nbsp;</td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Windows</strong></span></td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Linux</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Partition</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Disk1</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">/dev/sda1</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Filesystem Type</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">NTFS/VFAT</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">EXT3/EXT4/XFS/BTRFS...</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Mounting Parameters</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">DriveLetter</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">MountPoint</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Base Folder (where OS is stored)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">C:\</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">/</td></tr></tbody></table>

### The Filesystem Hierarchy Standard

Linux systems store their important files according to a standard layout called the **F**ilesystem **H**ierarchy **S**tandard (**FHS**), which has long been maintained by the Linux Foundation. For more information, take a look at the following document: _"[Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf)"_ created by LSB Workgroup. Having a standard is designed to ensure that users, administrators, and developers can move between distributions without having to re-learn how the system is organized.

Linux uses the ‘**/**’ character to separate paths (unlike Windows, which uses ‘**\**’), and does not have drive letters. Multiple drives and/or partitions are mounted as directories in the single filesystem. Removable media such as USB drives and CDs and DVDs will show up as mounted at **/run/media/yourusername/disklabel** for recent Linux systems, or under **/media** for older distributions. For example, if your username is **student** a USB pen drive labeled FEDORA might end up being found at **/run/media/student/FEDORA**, and a file **README.txt** on that disc would be at **/run/media/student/FEDORA/README.txt**.

Click the image to view an enlarged version.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-374.png)
_The Filesystem Hierarchy Standard_

All Linux filesystem names are case-sensitive, so **/boot**, **/Boot**, and **/BOOT** represent three different directories (or folders). Many distributions distinguish between core utilities needed for proper system operation and other programs, and place the latter in directories under **/usr** (think user). To get a sense for how the other programs are organized, find the **/usr** directory in the diagram from the previous page and compare the subdirectories with those that exist directly under the system root directory (**/**).

![fs tree](https://courses.edx.org/assets/courseware/v1/65256a6c88506b6e45744b97b8875775/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/fstree1.png)

### Video: Viewing the Filesystem Hierarchy from the Graphical Interface in Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V004800_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: Viewing the Filesystem Hierarchy from the Graphical Interface in openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V002000_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

## Linux Distribution Installation

Suppose you intend to buy a new car. What factors do you need to consider to make a proper choice? Requirements which need to be taken into account include the size needed to fit your family in the vehicle, the type of engine and gas economy, your expected budget and available financing options, reliability record and after-sales services, etc.

Similarly, determining which distribution to deploy also requires planning. The figure shows some, but not all choices. Note that many embedded Linux systems use custom crafted contents, rather than Android or Yocto.

![Choosing a Linux Distribution](https://courses.edx.org/assets/courseware/v1/6eafa3b1170a0c208335ea46ac16945d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/distros.png)

### Questions to Ask When Choosing a Distribution

Some questions worth thinking about before deciding on a distribution include:

* What is the main function of the system (server or desktop)?
* What types of packages are important to the organization? For example, web server, word processing, etc.
* How much hard disk space is required and how much is available? For example, when installing Linux on an embedded device, space is usually constrained.
* How often are packages updated?
* How long is the support cycle for each release? For example, **LTS** releases have long-term support.
* Do you need kernel customization from the vendor or a third party?
* What hardware are you running on? For example, it might be **X86**, **ARM**, **PPC**, etc.
* Do you need long-term stability? Can you accept (or need) a more volatile cutting edge system running the latest software?

### Linux Installation: Planning

The partition layout needs to be decided at the time of installation; it can be difficult to change later. While Linux systems handle multiple partitions by mounting them at specific points in the filesystem, and you can always modify the design later, it is always easier to try and get it right to begin with.

![Partitions in the Linux hard disk](https://courses.edx.org/assets/courseware/v1/ae8955c30e5b10b2fd1cab2c79673555/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen_34.jpg)
_Partitions in the Linux Hard Disk_

Nearly all installers provide a reasonable default layout, with either all space dedicated to normal files on one big partition and a smaller swap partition, or with separate partitions for some space-sensitive areas like **/home** and **/var**. You may need to override the defaults and do something different if you have special needs, or if you want to use more than one disk.

### Linux Installation: Software Choices

All installations include the bare minimum software for running a Linux distribution.

Most installers also provide options for adding categories of software. Common applications (such as the Firefox web browser and LibreOffice office suite), developer tools (like the **vi** and **emacs** text editors, which we will explore later in this course), and other popular services, (such as the Apache web server tools or MySQL database) are usually included. In addition, for any system with a graphical desktop, a chosen desktop (such as **GNOME** or **KDE**) is installed by default.

All installers set up some initial security features on the new system. One basic step consists of setting the password for the superuser (root) and setting up an initial user. In some cases (such as Ubuntu), only an initial user is set up; direct root login is not configured and root access requires logging in first as a normal user and then using **sudo**, as we will describe later. Some distributions will also install more advanced security frameworks, such as SELinux or AppArmor. For example, all Red Hat-based systems including Fedora and CentOS always use SELinux by default, and Ubuntu comes with AppArmor up and running.

![Linux Installation Software Choices](https://courses.edx.org/assets/courseware/v1/10f3cbf30f540761b32e02764de07e5c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen_35.jpg)
_Linux Installation Software Choices_

### Linux Installation: Install Source

Like other operating systems, Linux distributions are provided on removable media such as USB drives and CDs or DVDs. Most Linux distributions also support booting a small image and downloading the rest of the system over the network. These small images are usable on media, or as network boot images, in which case it is possible to perform an install without using any local media.

Many installers can do an installation completely automatically, using a configuration file to specify installation options. This file is called a Kickstart file for Red Hat-based systems, an AutoYAST profile for SUSE-based systems, and a Preseed file for Debian-based systems.

Each distribution provides its own documentation and tools for creating and managing these files.

![Three pictures: one showing a cell phone, computer and laptop connected to the cloud; another one showing disk drive with a CD inserted; and the last one showing pen drive](https://courses.edx.org/assets/courseware/v1/1129ddea1e2fb579c9f309c8e9846b2c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen_36.jpg)

### Linux Installation: The Process

The actual installation process is pretty similar for all distributions.

After booting from the installation media, the installer starts and asks questions about how the system should be set up. These questions are skipped if an automatic installation file is provided. Then, the installation is performed.

Finally, the computer reboots into the newly-installed system. On some distributions, additional questions are asked after the system reboots.

Most installers have the option of downloading and installing updates as part of the installation process; this requires Internet access. Otherwise, the system uses its normal update mechanism to retrieve those updates after the installation is done.

### Linux Installation: The Warning

The demonstrations show how to install Linux directly on your machine, **erasing everything that was there**. While the demonstrations will not alter your computer, following these procedures in real life will erase all current data.

The Linux Foundation has a document: _"Preparing Your Computer for Linux Training"_ that describes alternate methods of installing Linux without over-writing existing data. You may want to consult it, if you need to preserve the information on your hard disk.

These alternate methods are:

1. Re-partitioning your hard disk to free up enough room to permit dual boot (side-by-side) installation of Linux, along with your present operating system.
2. Using a host machine hypervisor program (such as VMWare's products or Oracle Virtual Box) to install a client Linux Virtual Machine.
3. Booting off of and using a Live CD or USB stick and not writing to the hard disk at all.

The first method is sometimes complicated and should be done when your confidence is high and you understand the steps involved. The second and third methods are quite safe and make it difficult to damage your system.

### Video: Steps to Install Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000300_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: Steps to Install CentOS

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000500_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: Steps to Install openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000500_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

## Chapter 3 Summary

You have completed Chapter 3. Let’s summarize the key concepts covered:

* A **partition** is a logical part of the disk.
* A **filesystem** is a method of storing/finding files on a hard disk.
* By dividing the hard disk into partitions, data can be grouped and separated as needed. When a failure or mistake occurs, only the data in the affected partition will be damaged, while the data on the other partitions will likely survive.
* The boot process has multiple steps, starting with BIOS, which triggers the boot loader to start up the Linux kernel. From there, the initramfs filesystem is invoked, which triggers the init program to complete the startup process.
* Determining the appropriate distribution to deploy requires that you match your specific system needs to the capabilities of the different distributions.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## **Chapter 4: Graphical Interface**

### Learning Objectives

By the end of this chapter, you should be able to:

* Manage graphical interface sessions.
* Perform basic operations using the graphical interface.
* Change the graphical desktop to suit your needs.

## Graphical Desktop

You can use either a **C**ommand **L**ine **I**nterface (**CLI**) or a **G**raphical **U**ser **I**nterface (**GUI**) when using Linux. To work at the CLI, you have to remember which programs and commands are used to perform tasks, and how to quickly and accurately obtain more information about their use and options. On the other hand, using the GUI is often quick and easy. It allows you to interact with your system through graphical icons and screens. For repetitive tasks, the CLI is often more efficient, while the GUI is easier to navigate if you do not remember all the details or do something only rarely.

We will learn how to manage sessions using the GUI for the three Linux distribution families that we cover the most in this course: Red Hat (CentOS, Fedora), SUSE (openSUSE), and Debian (Ubuntu, Mint). Since we are using the GNOME-based variant of openSUSE rather than the KDE-based one, all are actually quite similar. If you are using KDE (or other Linux desktops such as XFCE), your experience will vary somewhat from what is shown, but not in any intrinsically difficult way, as user interfaces have converged to certain well-known behaviors on modern operating systems. In subsequent sections of this course we will concentrate in great detail on the command line interface, which is pretty much the same on all distributions.

![Three screenshots showing Ubuntu, CentOS, and OpenSUSE desktops](https://courses.edx.org/assets/courseware/v1/fe27a9c47f2e272c238dc227cb749528/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnomedts.png)
_Ubuntu, CentOS, and openSUSE Desktops_

### X Window System

Generally, in a Linux desktop system, the X Window System is loaded as one of the final steps in the boot process. It is often just called X.

A service called the **Display Manager** keeps track of the displays being provided and loads the X server (so-called, because it provides graphical services to applications, sometimes called X clients). The display manager also handles graphical logins and starts the appropriate desktop environment after a user logs in.

X is rather old software; it dates back to the mid 1980s and, as such, has certain deficiencies on modern systems (for example, with security), as it has been stretched rather far from its original purposes. A newer system, known as [Wayland](https://wayland.freedesktop.org/), is gradually superseding it and is the default display system for Fedora, RHEL 8, and other recent distributions.  For the most part, it looks just like X to the user, although under the hood it is quite different.

![Display manager](https://courses.edx.org/assets/courseware/v1/44717c86868ff7e9edc71c5747bb84ab/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen28.jpg)
_Display Manager_

A desktop environment consists of a session manager, which starts and maintains the components of the graphical session, and the window manager, which controls the placement and movement of windows, window title-bars, and controls.

Although these can be mixed, generally a set of utilities, session manager, and window manager are used together as a unit, and together provide a seamless desktop environment.

If the display manager is not started by default in the default runlevel, you can start the graphical desktop different way, after logging on to a text-mode console, by running **startx** from the command line. Or, you can start the display manager (**gdm**, **lightdm**, **kdm**, **xdm**, etc.) manually from the command line. This differs from running **startx** as the display managers will project a sign in screen. We discuss them next.

![Desktop environment](https://courses.edx.org/assets/courseware/v1/c4a2925d0a2d22c238c9f1d91f71635b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen29.jpg)

### GUI Startup

When you install a desktop environment, the X display manager starts at the end of the boot process. It is responsible for starting the graphics system, logging in the user, and starting the user’s desktop environment. You can often select from a choice of desktop environments when logging in to the system.

![Hand clicking Login button](https://courses.edx.org/assets/courseware/v1/b2b0c2d435bf94d2b9f10dab925967e5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen05.jpg)

The default display manager for GNOME is called **gdm**. Other popular display managers include **lightdm** (used on Ubuntu before version 18.04 LTS) and **kdm** (associated with KDE).

### GNOME Desktop Environment

GNOME is a popular desktop environment with an easy-to-use graphical user interface. It is bundled as the default desktop environment for most Linux distributions, including Red Hat Enterprise Linux (RHEL), Fedora, CentOS, SUSE Linux Enterprise, Ubuntu and Debian. GNOME has menu-based navigation and is sometimes an easy transition to accomplish for Windows users. However, as you will see, the look and feel can be quite different across distributions, even if they are all using GNOME.

![GNOME logo](https://courses.edx.org/assets/courseware/v1/70a3215567cf5bf6d84f1affb3ab0dfc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Ch4_Sec1_Gnome_logo.jpg)

Another common desktop environment very important in the history of Linux and also widely used is KDE, which has often been used in conjunction with SUSE and openSUSE. Other alternatives for a desktop environment include Unity (present on older Ubuntu, but still based on GNOME), XFCE and LXDE. As previously mentioned, most desktop environments follow a similar structure to GNOME, and we will restrict ourselves mostly to it to keep things less complex.

### Video: System Startup and Logging In and Out

<video controls width="100%" preload="none">

<source src="https://edx-video.net/521d4479-5b72-4a6f-b5ce-423a416fcf6a-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Graphical Desktop Background

Each Linux distribution comes with its own set of desktop backgrounds. You can change the default by choosing a new wallpaper or selecting a custom picture to be set as the desktop background. If you do not want to use an image as the background, you can select a color to be displayed on the desktop instead.

![Desktop computer, keyboard, and mouse](https://courses.edx.org/assets/courseware/v1/88ef9ed386547375f0aa50738e1f5af3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen63.jpg)

In addition, you can also change the desktop theme, which changes the look and feel of the Linux system. The theme also defines the appearance of application windows.

We will learn how to change the desktop background and theme.

### Customizing the Desktop Background

To change the background, you can right click anywhere on the desktop and choose **Change Background**.

![Screenshot showing how to customize the desktop background](https://courses.edx.org/assets/courseware/v1/5e5585d25c7c44efc58a7c5d7c5e6f2f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntubg.png)

### Video: How to Change the Desktop Background

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000600_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### gnome-tweaks

Most common settings, both personal and system-wide, are to be found by clicking in the upper right-hand corner, on either a gear or other obvious icon, depending on your Linux distribution.

However, there are many settings which many users would like to modify which are not thereby accessible; the default settings utility is unfortunately rather limited in modern GNOME-based distributions. Unfortunately, the quest for simplicity has actually made it difficult to adapt your system to your tastes and needs.

Fortunately, there is a standard utility, **gnome-tweaks**, which exposes many more setting options. It also permits you to easily install extensions by external parties. Not all Linux distributions install this tool by default, but it is always available (older distributions used the name **gnome-tweak-tool**). You may have to run it by hitting **Alt-F2** and then typing in the name. You may want to add it to your **Favorites** list as we shall discuss.

As discussed in the next chapter, some recent distributions have taken most of the functionality out of this tool and placed it in a new one, called **gnome-extensions-app**.

In the screenshot below, the keyboard mapping is being adjusted so the useless **CapsLock** key can be used as an additional **Ctrl** key; this saves users who use **Ctrl** a lot (such as **emacs** aficionados) from getting physically damaged by pinkie strain.

![gnome-tweaks](https://courses.edx.org/assets/courseware/v1/b9aeb9e063eda9567443ab77501286d3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnometweaktool.png)
_gnome-tweaks_

### Changing the Theme

The visual appearance of applications (the buttons, scroll bars, widgets, and other graphical components) are controlled by a **theme**. GNOME comes with a set of different themes which can change the way your applications look.

The exact method for changing your theme may depend on your distribution. For older GNOME-based distributions, you can simply run **gnome-tweaks**, as shown in the screenshot from Ubuntu. However, as mentioned earlier, if you don't find it there, you will need to look at **gnome-extensions-app**, which can now configure themes. This requires installing even more software and going to external websites, so it is unlikely to be seen as an improvement by many users.

There are other options to get additional themes beyond the default selection. You can download and install themes from the [GNOME's Wiki](https://wiki.gnome.org/Personalization) website.

![Screenshot showing how to change the theme](https://courses.edx.org/assets/courseware/v1/3b96462047b8da666c50589c7d570824/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/themesuse.png)
_Changing the Theme_

## Session Management

### Logging In and Out

The next screen shows a demonstration for logging in and out on the major Linux distribution families we concentrate on in this course. Note that evolution has brought us to a stage where it little matters which distribution you choose, as they are all rather similar.

![Login and logout buttons](https://courses.edx.org/assets/courseware/v1/11ec196634ac41509995f108392b568f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen06.jpg)

### Video: Logging In and Logging Out Using the GUI in Ubuntu, openSUSE and CentOS

<video controls width="100%" preload="none">

<source src="https://edx-video.net/a80a237c-bd71-4521-ac74-d85271da8103-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Locking the Screen

It is often a good idea to lock your screen to prevent other people from accessing your session while you are away from your computer.

_**NOTE**_: This does not suspend the computer; all your applications and processes continue to run while the screen is locked.

There are two ways to lock your screen:

* Using the graphical interface  
Clicking in the upper-right corner of the desktop, and then clicking on the lock icon.
* Using the keyboard shortcut SUPER-L   
(The **SUPER** key is also known as the **Windows** key).

The keyboard shortcut for locking the screen can be modified by altering keyboard settings, the exact prescription varying by distribution, but not hard to ascertain.

To re-enter the desktop session you just need to provide your password again.

The screenshot below shows how to lock the screen for Ubuntu. The details vary little in modern distributions.

![Screenshot showing how to lock the screen for Ubuntu](https://courses.edx.org/assets/courseware/v1/d6ee89ab27aa5ff6a458210c8cba91b8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lockubuntu.png)

### Video: Locking and Unlocking the Screen in More Detail

<video controls width="100%" preload="none">

<source src="https://edx-video.net/fe32cdd9-570c-4bfa-a631-ab2ced0ed7cf-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Switching Users

Linux is a true multi-user operating system, which allows more than one user to be simultaneously logged in. If more than one person uses the system, it is best for each person to have their own user account and password. This allows for individualized settings, home directories, and other files. Users can take turns using the machine, while keeping everyone's sessions alive, or even be logged in simultaneously through the network.

![Two cartoon busts connected with arrows](https://courses.edx.org/assets/courseware/v1/b68bf37dafb8f7d7e82e7143197620ef/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen18.jpg)

###   
Video: Switching Users in Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000800_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Shutting Down and Restarting

Besides normal daily starting and stopping of the computer, a system restart may be required as part of certain major system updates, generally only those involving installing a new Linux kernel.

![Turn On Button](https://courses.edx.org/assets/courseware/v1/6eea345b1964582af01d9f9d8923a608/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen26.jpg)

Initiating the shutdown process from the graphical desktop is rather trivial on all current Linux distributions, with very little variation. We will discuss later how to do this from the command line, using the **shutdown** command.

In all cases, you click on either a settings (gear) or a power icon and follow the prompts.

### Shutting Down and Restarting on GNOME

To shut down the computer in any recent GNOME-based Linux distribution, perform the following steps:

1. Click either the **Power** or the **Gear** icon in the upper-right corner of the screen.
2. Click on **Power Off**, **Restart**, or **Cancel**_._ If you do nothing, the system will shutdown in 60 seconds.

Shutdown, reboot, and logout operations will ask for confirmation before going ahead. This is because many applications will not save their data properly when terminated this way.

Always save your documents and data before restarting, shutting down, or logging out.

![Screenshot showing shutting down and restarting in Ubuntu](https://courses.edx.org/assets/courseware/v1/d7aec4ecc99a643b6970ce88e4c7e7c5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/centos8shutdown.png)
_Shutting Down and Restarting_

### Suspending

  
All modern computers support **Suspend** (or **Sleep**) **Mode** when you want to stop using your computer for a while. _Suspend Mode_ saves the current system state and allows you to resume your session more quickly while remaining on, but uses very little power in the sleeping state. It works by keeping your system’s applications, desktop, and so on, in system RAM, but turning off all of the other hardware. This shortens the time for a full system start-up as well as conserves battery power. One should note that modern Linux distributions actually boot so fast that the amount of time saved is often minor.

To suspend the system, the procedure starts the same as that for shutdown or locking the screen.

The method is quite simple and universal in most recent GNOME-based distributions. If you click on the **Power** icon and hold for a short time and release, you will get the double line icon displayed below, which you then click to suspend the system. Some distributions, including Ubuntu, may still show a separate Suspend icon instead of using the above method.

![Suspending Ubuntu system](https://courses.edx.org/assets/courseware/v1/8bc873843331e65aa45bd8e71847d96f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/suspend.png)
_Suspending the System_

## Basic Operations

Even experienced users can forget the precise command that launches an application, or exactly what options and arguments it requires. Fortunately, Linux allows you to quickly open applications using the graphical interface.

Applications are found at different places in Linux (and within GNOME):

* From the **Applications** menu in the upper-left corner.
* From the **Activities** menu in the upper-left corner.
* In some **Ubuntu** versions, from the **Dash** button in the upper-left corner.
* For **KDE**, and some other environments, applications can be opened from the button in the lower-left corner.

On the following pages you will learn how to perform basic operations in Linux using the graphical interface.

### Locating Applications

Unlike other operating systems, the initial install of Linux usually comes with a wide range of applications and software archives that contain thousands of programs that enable you to accomplish a wide variety of tasks with your computer. For most key tasks, a default application is usually already installed. However, you can always install more applications and try different options.

For example, Firefox is popular as the default browser in many Linux distributions, while Epiphany, Konqueror, and Chromium (the open source base for Google Chrome) are usually available for install from software repositories. Proprietary web browsers, such as Opera and Chrome, are also available.

Locating applications from the GNOME and KDE menus is easy, as they are neatly organized in functional submenus.

![Locating Applications](https://courses.edx.org/assets/courseware/v1/b24b746b71f7af714d6b07bf9074af87/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntu1910aps.png)
_Locating Applications_

### Default Applications

Multiple applications are available to accomplish various tasks and to open a file of a given type. For example, you can click on a web address while reading an email and launch a browser such as Firefox or Chrome.

To set default applications, enter the **Settings** menu (on all recent Linux distributions) and then click on either **Default Applications** or **Details > Default Applications**. The exact list will vary from what is shown here in the Ubuntu screenshot according to what is actually installed and available on your system

![Default Applications](https://courses.edx.org/assets/courseware/v1/2c777f97912b2abd2ae65425ee717e2f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/defappsubuntu.png)
_Default Applications_



### Video: Setting Default Applications

<video controls width="100%" preload="none">

<source src="https://edx-video.net/614af67b-a489-498e-939d-a8ca6b7f4a69-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### File Manager

Each distribution implements the **Nautilus** (**File** **Manager**) utility, which is used to navigate the file system. It can locate files and, when a file is clicked upon, either it will run if it is a program, or an associated application will be launched using the file as data. This behavior is completely familiar to anyone who has used other operating systems.

To start the file manager you will have to click on its icon (a file cabinet) which is easily found, usually under **Favorites** or **Accessories**. It will have the name **Files**.

This will open a window with your **Home** directory displayed. The left panel of the File Manager window holds a list of commonly used directories, such as **Desktop**, **Documents**, **Downloads** and **Pictures**.

You can click the _Magnifying Glass_ icon on the top-right to search for files or directories (folders).

![File manager](https://courses.edx.org/assets/courseware/v1/b3549f989a4dba1ca5720eaa3254bd15/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homefilesubuntu.png)
_File Manager_

### Home Directories

The File Manager lets you access different locations on your computer and the network, including the **Home** directory, **Desktop**, **Documents**, **Pictures**, and other **Other Locations**.

Every user with an account on the system will have a home directory, usually created under **/home**, and usually named according to the user, such as **/home/student**.

By default, files the user saves will be placed in a directory tree starting there. Account creation, whether during system installation or at a later time, when a new user is added, also induces default directories to be created under the user's home directory, such as **Documents**, **Desktop**, and **Downloads**.

In the screenshot shown for Ubuntu, we have chosen the list format and are also showing _hidden files_ (those starting with a period). See if you can do the same on your distribution.

![Home Directories](https://courses.edx.org/assets/courseware/v1/2a56d63772e3aff037135e2624dd9a37/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homefilesu1910.png)
_Home Directories_



![Other Locations](https://courses.edx.org/assets/courseware/v1/6c854e3e52c67c75ffa29d8bdfcf8f77/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/otherfilesu1910.png)
_Other Locations_

### Viewing Files

The File Manager allows you to view files and directories in more than one way.

You can switch between the Icons and List formats, either by clicking the familiar icons in the top bar, or you can press **CTRL-1** or **CTRL-2** respectively.

In addition, you can also arrange the files and directories by name, size, type, or modification date for further sorting. To do so, click **View** and select **Arrange Items**.

Another useful option is to show _hidden files_ (sometimes imprecisely called system files), which are usually configuration files that are hidden by default and whose name starts with a dot. To show hidden files, select **Show Hidden Files** from the menu or press **CTRL-H**.

The file browser provides multiple ways to customize your window view to facilitate easy drag and drop file operations. You can also alter the size of the icons by selecting **Zoom In** and **Zoom Out** under the _View_ menu.

![Viewing files in openSUSE](https://courses.edx.org/assets/courseware/v1/59b49f03cf57ecaf483df8f2f06f32b9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homefilessuse.png)

### Searching for Files

The File Manager includes a great search tool inside the file browser window.

1. Click **Search** in the toolbar (to bring up a text box).
2. Enter the keyword in the text box. This causes the system to perform a recursive search from the current directory for any file or directory which contains a part of this keyword.

To open the _File Manager_ from the command line, on most systems simply type **nautilus**.

![Magnifying glass](https://courses.edx.org/assets/courseware/v1/2ba30c1757235e33a807500b1af9da42/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen48.jpg)

The shortcut key to get to the search text box is **CTRL-F**. You can exit the search text box view by clicking the _Search_ button or **CTRL-F** again.

Another quick way to access a specific directory is to press **CTRL-L**, which will give you a **Location** text box to type in a path to a directory.

### More About Searching for Files

You can refine your search beyond the initial keyword by providing dropdown menus to further filter the search.

1. Based on **Location** or **File Type**, select additional criteria from the dropdown.
2. To regenerate the search, click the **Reload** button.
3. To add multiple search criteria, click the **+** button and select _Additional Search Criteria_.

For example, if you want to find a PDF file containing the word **Linux** in your home directory, navigate to your **home** directory and search for the word “Linux”. You should see that the default search criterion limits the search to your **home** directory already. To finish the job, click the **+** button to add another search criterion, select **File Type** for the type of criterion, and select **PDF** under the **File Type** dropdown.

![Screenshot showing how to search for files based on different criteria](https://courses.edx.org/assets/courseware/v1/92b46e00f94ca300fff886db41b6d2d3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/searchubuntu.png)
_Searching for Files_

### Editing a File

Editing any text file through the graphical interface is easy in the GNOME desktop environment. Simply double-click the file on the desktop or in the Nautilus file browser window to open the file with the default text editor.

![gedit icon](https://courses.edx.org/assets/courseware/v1/e47912c6805c7126aef11b9e4c5b8713/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen50.jpg)

The default text editor in GNOME is **gedit**. It is simple yet powerful, ideal for editing documents, making quick notes, and programming. Although **gedit** is designed as a general purpose text editor, it offers additional features for spell checking, highlighting, file listings and statistics.

You will learn much more about using text editors in a later chapter.

### Removing a File

Deleting a file in Nautilus will automatically move the deleted files to the **.local/share/Trash/files/** directory (a trash can of sorts) under the user's home directory. There are several ways to delete files and directories using Nautilus.

1. Select all the files and directories that you want to delete.
2. Press **CTRL-Delete** on your keyboard, or right-click the file.
3. Select **Move to Trash**.

Note that you may have a **Delete Permanently** option which bypasses the trash folder, and that this option may be visible all the time or only in list (rather than) icon mode.

![Trash can](https://courses.edx.org/assets/courseware/v1/7384e7b0992fc01be5544b2d30992425/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen52.jpg)

To _permanently_ delete a file:

1. On the left panel inside a Nautilus file browser window, right-click on the **Trash** directory.
2. Select _Empty Trash_.

Alternatively, select the file or directory you want to permanently delete and press **Shift-Delete**.

As a precaution, you should never delete your _Home_ directory, as doing so will most likely erase all your GNOME configuration files and possibly prevent you from logging in. Many personal system and program configurations are stored under your home directory.

### Video: Locating and Setting Default Applications, and Exploring Filesystems in openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001000_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

## Chapter 4 Summary

You have completed Chapter 4. Let's summarize the key concepts covered:

* **GNOME** is a popular desktop environment and graphical user interface that runs on top of the Linux operating system.
* The default display manager for GNOME is called **gdm**.
* The gdm display manager presents the user with the login screen, which prompts for the login username and password.
* Logging out through the desktop environment kills all processes in your current **X** session and returns to the display manager login screen.
* Linux enables users to switch between logged-in sessions.
* Suspending puts the computer into sleep mode.
* For each key task, there is generally a default application installed.
* Every user created in the system will have a **home** directory.
* The _Places_ menu contains entries that allow you to access different parts of the computer and the network.
* **Nautilus** gives three formats to view files.
* Most text editors are located in the _Accessories_ submenu.
* Each Linux distribution comes with its own set of desktop backgrounds.
* GNOME comes with a set of different themes which can change the way your applications look.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

# 

## **Chapter 5: System Configuration from the Graphical Interface**

### Learning Objectives

By the end of this chapter, you should be able to:

* Apply system, display, and date and time settings using the _System Settings_ panel.
* Track the network settings and manage connections using _Network Manager_ in Linux.
* Install and update software in Linux from a graphical interface.

_**NOTE**_: We will revisit all these tasks later, when we discuss how to accomplish them from the command line interface.

## System, Display, Date and Time Settings

The **System Settings** panel allows you to control most of the basic configuration options and desktop settings, such as specifying the screen resolution, managing network connections, or changing the date and time of the system.

For the GNOME Desktop Manager, one clicks on the upper right-hand corner and then selects the tools image (screwdriver crossed with a wrench or a gear). Depending on your distribution, you may find other ways to get into the settings configuration as well. You will also find variation in the menu layout between Linux distributions and versions, so you may have to hunt for the settings you need to examine or modify.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-410.png)
_System Settings Panel_

### System Settings Menus  


To get deeper into configuration, one can click on the _Devices_ on the previous menu in order to configure items like the display, the keyboard, the printers, etc.

![Configuring Applications on Ubuntu](https://courses.edx.org/assets/courseware/v1/37875055d2d8368b6c8b2edd1af73ace/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntusetapps.png)
_Configuring Applications on Ubuntu_

One can also click on the _Users_ icon (which may be under _Details_) to set values for system users, such as their login picture, password, etc.

![Configuring the User Attributes](https://courses.edx.org/assets/courseware/v1/9f2a5b8ed015a7d39f6b15df59b78c98/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntuuserconfig.png)
_Configuring the User Attributes_

### gnome-tweaks

A lot of personalized configuration settings do not appear on the settings menus. Instead, you have to launch a tool called either **gnome-tweaks** (or **gnome-tweak-tool** on older Linux distributions). We have not really discussed working at the command line yet, but you can always launch a program such as this by doing **Alt-F2** and typing in the command. Some distributions have a link to the tweaks menus in the settings, but for some mysterious reason, many obscure this tool's existence, and it becomes hard to discover how to modify even rather basic desktop attributes and behavior.

Important things you can do with this tool include selecting a **theme**, configuring **extensions** which you can get from your distribution or download from the Internet, control fonts, modify the keyboard layout, and set which programs start when you login.

The most recent GNOME versions have removed a lot of the functionality of **gnome-tweaks**; extensions now have to be configured using a new app called **gnome-extensions-app**. The reasoning for this is obscure.

The screenshot here is from a Red Hat system with quite a few extensions installed, but not all being used.

![Extensions installed on RHEL](https://courses.edx.org/assets/courseware/v1/206249c2dbef56d193c9a2e4a7a97b2f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnometweaks.png)
_Extensions Installed on RHEL_

### Display Settings

Clicking on **Settings > Displays** (or **Settings > Devices > Displays**) will expose the most common settings for changing  the desktop appearance. These settings function independently of the specific display drivers you are running. The exact appearance will depend enormously on how many monitors you have and other factors, such as Linux distribution and particular version.

If your system uses a proprietary video card driver (usually from **nVidia** or **AMD**), you will probably have a separate configuration program for that driver. This program may give more configuration options, but may also be more complicated, and might require sysadmin (root) access. If possible, you should configure the settings in the **Displays** panel rather than with the proprietary program.

The X server, which actually provides the GUI, uses **/etc/X11/xorg.conf** as its configuration file _if it exists_; In modern Linux distributions, this file is usually present only in unusual circumstances, such as when certain less common graphic drivers are in use. Changing this configuration file directly is usually for more advanced users.

![Display Settings on an Older and Newer Ubuntu Systems](https://courses.edx.org/assets/courseware/v1/c2af77e8b90d9b4213a8ec8218838999/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Display_Settings_on_an_Older_and_Newer_Ubuntu_Systems.png)
_Display Settings on an Older and Newer Ubuntu Systems_

### Setting Resolution and Configuring Multiple Screens

While your system will usually figure out the best resolution for your screen automatically, it may get this wrong in some cases, or you might want to change the resolution to meet your needs.

You can accomplish this using the _Displays_ panel. The switch to the new resolution will be effective when you click _Apply_, and then confirm that the resolution is working. In case the selected resolution fails to work or you are just not happy with the appearance, the system will switch back to the original resolution after a short timeout. Once again, the exact appearance of the configuration screen will vary a lot between distributions and versions, but usually is rather intuitive and easy, once you find the configuration menus.

In most cases, the configuration for multiple displays is set up automatically as one big screen spanning all monitors, using a reasonable guess for screen layout. If the screen layout is not as desired, a check box can turn on mirrored mode, where the same display is seen on all monitors. Clicking on a particular monitor image lets you configure the resolution of each one, and whether they make one big screen, or mirror the same video, etc.

![Setting the Resolution and Configuring Multiple Screens](https://courses.edx.org/assets/courseware/v1/c9815d9b551a9d4bc8f71530471ae097/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/multidisplayrhel8.png)
_Setting the Resolution and Configuring Multiple Screens_

### Video: Configuring Display Settings

<video controls width="100%" preload="none">

<source src="https://edx-video.net/9adfb9c8-07d7-4910-92ce-b3168692e082-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Date and Time Settings

By default, Linux always uses Coordinated Universal Time (UTC) for its own internal timekeeping. Displayed or stored time values rely on the system time zone setting to get the proper time. UTC is similar to, but more accurate than, Greenwich Mean Time (GMT).

If you click on the time displayed on the top panel, you can adjust the format with which the date and time is shown; on some distributions, you can also alter the values.

The more detailed date and time settings can be selected from the **Date & Time** window in the System Settings Menu.

![ Screenshot showing Date and Time Settings in Ubuntu](https://courses.edx.org/assets/courseware/v1/fafa9bab5da6a86410f8a8ad98278e34/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntudate.png)
_Date and Time Settings_

The "automatic" settings are referring to the use of Network Time Protocol (NTP), which we discuss next.

### Network Time Protocol

The **N**etwork **T**ime **P**rotocol (**NTP**) is the most popular and reliable protocol for setting the local time by consulting established Internet servers. Linux distributions always come with a working NTP setup, which refers to specific time servers run or relied on by the distribution. This means that no setup, beyond "on" or "off", is generally required for network time synchronization.

![Picture showing different types of watches](https://courses.edx.org/assets/courseware/v1/6559d606ae7043ce2a92fc4b5b17cdf9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen11.jpg)

### Network Configuration

All Linux distributions have network configuration files, but file formats and locations can differ from one distribution to another. Hand editing of these files can handle quite complicated setups, but is not very dynamic or easy to learn and use. **Network Manager** was developed to make things easier and more uniform across distributions. It can list all available networks (both wired and wireless), allow the choice of a wired, wireless, or mobile broadband network, handle passwords, and set up Virtual Private Networks (VPNs). Except for unusual situations, it is generally best to let Network Manager establish your connections and keep track of your settings.

![Network Configuration](https://courses.edx.org/assets/courseware/v1/427ccf47dacf228ee1d15672b07d0ad2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen18.jpg)
_Network Configuration_

In this section, you will learn how to manage network connections, including wired and wireless connections, and mobile broadband and VPN connections.

### Wired and Wireless Connections

Wired connections usually do not require complicated or manual configuration. The hardware interface and signal presence are automatically detected, and then Network Manager sets the actual network settings via **D**ynamic **H**ost **C**onfiguration **P**rotocol (DHCP).

For **static** configurations that do not use DHCP, manual setup can also be done easily through Network Manager. You can also change the Ethernet **M**edia **A**ccess **C**ontrol (MAC) address if your hardware supports it. The MAC address is a unique hexadecimal number of your network card.

![Wired and Wireless Connections](https://courses.edx.org/assets/courseware/v1/34c61d5ecb1a4f58b5729603e08b9995/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen19.jpg)

Wireless networks are usually not connected by default. You can view the list of available wireless networks and see which one (if any) you are currently connected to by using Network Manager. You can then add, edit, or remove known wireless networks, and also specify which ones you want connected by default when present.

### Configuring Wireless Connections

To configure a wireless network in any recent GNOME-based distribution:

Click on the upper-right corner of the top panel, which brings up a settings and/or network window. While the exact appearance will depend on Linux distribution and version, it will always be possible to click on a **Wi-Fi** submenu, as long as the hardware is present. Here is an example from a RHEL 8 system:

![Configuring Wireless Connections](https://courses.edx.org/assets/courseware/v1/8f9f84c03fd872a5c510fb1370ea0933/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wifi1.png)
_Configuring Wireless Connections_

Select the wireless network you wish to connect to. If it is a secure network, the first time it will request that you enter the appropriate password. By default, the password will be saved for subsequent connections.

![Selecting a Network](https://courses.edx.org/assets/courseware/v1/ab20057497c4be2af101ade999d0bd52/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wifi2.png)
_Selecting a Network_

If you click on **Wi-Fi Settings**, you will bring up the third screenshot. If you click on the **Gear** icon for any connection, you can configure it in more detail.

![Configuring the Network of Your Choice](https://courses.edx.org/assets/courseware/v1/bd0d58ae53ee5b9cc0705679b7e4cf9c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wifi3.png)
_Configuring the Network of Your Choice_

Older and other Linux distributions may look quite a bit different in detail, but the steps and choices are essentially identical, as they are all running Network Manager with perhaps somewhat different clothing.

### Video: Managing Network Settings

<video controls width="100%" preload="none">

<source src="https://edx-video.net/704c77f7-c31b-4aab-996f-cafbd84e72a7-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Mobile Broadband and VPN Connections

You can set up a mobile broadband connection with Network Manager, which will launch a wizard to set up the connection details for each connection.

Once the configuration is done, the network is configured automatically each time the broadband network is attached.

![Picture showing laptops, tablets and cell phones connected with lines](https://courses.edx.org/assets/courseware/v1/c747395ba6d725293f45c70acc201e93/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen26.jpg)

Network Manager can also manage your VPN connections.

It supports many VPN technologies, such as native IPSec, Cisco OpenConnect (via either the Cisco client or a native open source client), Microsoft PPTP, and OpenVPN.

You might get support for VPN as a separate package from your distributor. You need to install this package if your preferred VPN is not supported.

### Installing and Updating Software

Each package in a Linux distribution provides one piece of the system, such as the Linux kernel, the **C** compiler, utilities for manipulating text or configuring the network, or for your favorite web browsers and email clients.

Packages often depend on each other. For example, because your email client can communicate using SSL/TLS, it will depend on a package which provides the ability to encrypt and decrypt SSL and TLS communication, and will not install unless that package is also installed at the same time.

![Cartoon pinguin carrying books](https://courses.edx.org/assets/courseware/v1/277740a799bbd78d92f99ef9acc4e8db/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen33.jpg)

All systems have a lower-level utility which handles the details of unpacking a package and putting the pieces in the right places. Most of the time, you will be working with a higher-level utility which knows how to download packages from the Internet and can manage dependencies and groups for you.

In this section, you will learn how to install and update software in Linux using the Debian packaging system (used by systems such as Ubuntu as well) and RPM packaging systems (which is used by both Red Hat and SUSE family systems). These are the main ones in use although there are others which work well for other distributions which are less used.

### Debian Packaging

Let’s look at the Package Management for the Debian family system.

**dpkg** is the underlying package manager for these systems. It can install, remove, and build packages. Unlike higher-level package management systems, it does not automatically download and install packages and satisfy their dependencies.

![Package Management in the Debian family system](https://courses.edx.org/assets/courseware/v1/c3ddb34d7f243624f888143c74665a94/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen34.jpg)
_Package Management in the Debian Family System_

For Debian-based systems, the higher-level package management system is the **A**dvanced **P**ackage **T**ool (APT) system of utilities. Generally, while each distribution within the Debian family uses APT, it creates its own user interface on top of it (for example, apt and apt-get, synaptic, gnome-software, Ubuntu Software Center, etc). Although apt repositories are generally compatible with each other, the software they contain generally is not. Therefore, most repositories target a particular distribution (like Ubuntu), and often software distributors ship with multiple repositories to support multiple distributions. Demonstrations are shown later in this section.

### Red Hat Package Manager (RPM)

Red Hat Package Manager (RPM) is the other package management system popular on Linux distributions. It was developed by Red Hat, and adopted by a number of other distributions, including SUSE/openSUSE, Mageia, CentOS, Oracle Linux, and others.

![Red Hat Package Manager](https://courses.edx.org/assets/courseware/v1/d803cf81ee0659af701365b16aebcb3a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen35.jpg)
_Red Hat Package Manager_

The higher-level package manager differs between distributions. Red Hat family distributions historically use RHEL/CentOS and Fedora uses dnf, while retaining good backwards compatibility with the older yum program. SUSE family distributions such as openSUSE also use RPM, but use the zypper interface.

### openSUSE’s YaST Software Management

The **Y**et **a**nother **S**etup **T**ool (YaST) software manager is similar to other graphical package managers. It is an RPM-based application. You can add, remove, or update packages using this application very easily. To access the YaST software manager:

1. Click **Activities**
2. In the **Search** box, type **YaST**
3. Click the **YaST** icon
4. Click **Software Management**

You can also find YaST by clicking on **Applications > Other-YaST**, which is a strange place to put it.

![openSUSE's software management](https://courses.edx.org/assets/courseware/v1/3daba44866ca7ac7880f9eb6e74bc467/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen36.jpg)
_openSUSE's Software Management_

openSUSE’s YaST software management application is similar to the graphical package managers in other distributions. A demonstration of the YaST software manager is shown later in this section.

### Video: Installing and Updating Software in openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001400_DTH.mp4"
        type="video/mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: Installing and Updating Software in Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/0f1c4770-518a-416f-87ef-c1d515e4023f-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

## Chapter 5 Summary

You have completed Chapter 5. Let's summarize the key concepts covered:

* You can control basic configuration options and desktop settings through the _System Settings_ panel.
* Linux always uses Coordinated Universal Time (UTC) for its own internal time-keeping. You can set the date and time settings from the _System Settings_ window.
* The Network Time Protocol is the most popular and reliable protocol for setting the local time via Internet servers.
* The _Displays_ panel allows you to change the resolution of your display and configure multiple screens.
* Network Manager can present available wireless networks, allow the choice of a wireless or mobile broadband network, handle passwords, and set up VPNs.
* **dpkg** and **RPM** are the most popular package management systems used on Linux distributions.
* Debian distributions use **dpkg** and **apt**-based utilities for package management.
* RPM was developed by Red Hat, and adopted by a number of other distributions, including the openSUSE, Mandriva, CentOS, Oracle Linux, and others.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## **Chapter 6: Common Applications**

By the end of this chapter, you should be familiar with common Linux applications, including:

* Internet applications such as browsers and email programs.
* Office Productivity Suites such as LibreOffice.
* Developer tools, such as compilers, debuggers, etc.
* Multimedia applications, such as those for audio and video.
* Graphics editors such as the GIMP and other graphics utilities.

## Internet Applications

The Internet is a global network that allows users around the world to perform multiple tasks, such as searching for data, communicating through emails and online shopping. Obviously, you need to use network-aware applications to take advantage of the Internet. These include:

* Web browsers
* Email clients
* Streaming media applications
* Internet Relay Chats
* Conferencing software

![Internet applications](https://courses.edx.org/assets/courseware/v1/9ab13d93d41e76edae95a90f12c96dd3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch17_screen03.jpg)
_Internet Applications_

### Web Browsers

As discussed in the _Graphical Interface_ chapter, Linux offers a wide variety of web browsers, both graphical and text-based, including:

* Firefox
* Google Chrome
* Chromium
* Epiphany (renamed web)
* Konqueror
* linx, lynx, w3m
* Opera  


![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-31.png)

###   
Email Applications

Email applications allow for sending, receiving, and reading messages over the Internet. Linux systems offer a wide number of email clients, both graphical and text-based. In addition, many users simply use their browsers to access their email accounts.

Most email clients use the Internet Message Access Protocol (IMAP) or the older Post Office Protocol (POP) to access emails stored on a remote mail server. Most email applications also display HTML (HyperText Markup Language) formatted emails that display objects, such as pictures and hyperlinks. The features of advanced email applications include the ability of importing address books/contact lists, configuration information, and emails from other email applications.

Linux supports the following types of email applications:

* Graphical email clients, such as Thunderbird, Evolution, and Claws Mail.
* Text mode email clients, such as Mutt and mail.
* All web browser-based clients, such as Gmail, Yahoo Mail, and Office 365.

![Email applications](https://courses.edx.org/assets/courseware/v1/7ea5bcb37db44af78b8e56e6f351fc00/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch17_screen05.jpg)
_Email Applications_

### Other Internet Applications

Linux systems provide many other applications for performing Internet-related tasks. These include:

<table align="left" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Application</strong></span></td><td align="center" bgcolor="#003f60" width="85%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Use</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">FileZilla</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Intuitive graphical FTP client that supports FTP, Secure File Transfer Protocol (SFTP), and FTP Secured (FTPS).<span>&nbsp;</span>Used to transfer files to/from (FTP) servers.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Pidgin</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To access GTalk, AIM, ICQ, MSN, IRC and other messaging networks.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Ekiga</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To connect to Voice over Internet Protocol (VoIP) networks.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Hexchat</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To access Internet Relay<span>&nbsp;</span>Chat (IRC) networks.</td></tr></tbody></table>

![FileZilla logo](https://courses.edx.org/assets/courseware/v1/f9dff170755a23939c284386a7ceed60/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/save-website-ftp-login-credentials-filezilla.png)

![Pidgin logo](https://courses.edx.org/assets/courseware/v1/fc25e3da569679a9515327f5fe570f00/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Pidgin-Chat-App-logo.png)

![xChat logo](https://courses.edx.org/assets/courseware/v1/bf94cb9811a89ffa464df7c9d963df57/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Xchat_mongol.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-32.png)

### Office Applications

Most day-to-day computer systems have productivity applications (sometimes called office suites) available or installed. Each suite is a collection of closely coupled programs used to create and edit different kinds of files such as:

* Text (articles, books, reports, etc.)
* Spreadsheets
* Presentations
* Graphical objects.

Most Linux distributions offer LibreOffice, an open source office suite that started in 2010 and has evolved from OpenOffice. While other office suites are available as we have listed, LibreOffice is the most mature, widely used and intensely developed.

In addition, Linux users have full access to Internet-based office suites such as Google Docs and Microsoft Office 365.

![LibreOffice logo](https://courses.edx.org/assets/courseware/v1/6f2b4af8b24fd4702c5b9a48e5310cd2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LibreOffice_external_logo_600px.png)

### LibreOffice Components

The component applications included in LibreOffice are:

* Writer: Word Processing
* Calc: Spreadsheets
* Impress: Presentations
* Draw: Create and edit graphics and diagrams.

The LibreOffice applications can read and write non-native document formats, such as those used by Microsoft Office. Usually, fidelity is maintained quite well, but complicated documents might have some imperfect conversions.

![Screenshot of the LibreOffice office suite](https://courses.edx.org/assets/courseware/v1/208b36f99828ebe377c49dbbde60e4bc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/libreoffice.png)
_LibreOffice Applications_

### Development Applications

Linux distributions come with a complete set of applications and tools that are needed by those developing or maintaining both user applications and the kernel itself.

These tools are tightly integrated and include:

* Advanced editors customized for programmers' needs, such as vi and emacs.
* Compilers (such as gcc and clang for programs in C and C++) for every computer language that has ever existed, including very popular new ones such as Golang and Rust.
* Debuggers such as gdb and various graphical front ends to it and many other debugging tools (such as Valgrind).
* Performance measuring and monitoring programs, some with easy to use graphical interfaces, others more arcane and meant to be used only by serious experienced development engineers.
* Complete Integrated Development Environments (IDE's) such as Eclipse and Visual Studio Code that put all these tools together.

On other operating systems, these tools have to be obtained and installed separately, often at a high cost, while on Linux they are all available at no cost through standard package installation systems.

![gcc logo](https://courses.edx.org/assets/courseware/v1/563456f06696ec4ab148bdd5ac68c9f0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gccegg-65.png)

![gdb logo](https://courses.edx.org/assets/courseware/v1/2694164dcff3b59bee56c60eab76e8d4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gdb-logo.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-33.png)

### Sound Players

Multimedia applications are used to listen to music, watch videos, etc., as well as to present and view text and graphics. Linux systems offer a number of sound player applications, including:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto 20px 0px; font-size: 16px; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Application</strong></span></td><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Use</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Amarok</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Mature MP3 player with a graphical interface, that plays audio and video files, and streams (online audio files). It allows you to create a playlist that contains a group of songs, and uses a database to store information about the music collection.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Audacity</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to record and edit sounds. It can be quickly installed through a package manager. Audacity has a simple interface to get you started.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Rhythmbox</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supports a large variety of digital music sources, including streaming Internet audio and podcasts. The application also enables search of particular audio in a library. It supports<span>&nbsp;</span><em style="line-height: 1.4em; font-style: italic;">smart playlists</em>&nbsp;with an<span>&nbsp;</span><em style="line-height: 1.4em; font-style: italic;">automatic update</em><span>&nbsp;</span>feature, which can revise playlists based on specified selection criteria.</td></tr></tbody></table>

Of course, Linux systems can also connect with commercial online music streaming services, such as Pandora and Spotify through web browsers.

![Amarok logo](https://courses.edx.org/assets/courseware/v1/edb81f83b69bdd2a5c0ba95600449381/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Amarok_logo.jpeg)

![Audacity Logo](https://courses.edx.org/assets/courseware/v1/d03d86902ba54f1d44c23541d2b8c096/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Screen_Shot_2018-07-01_at_1.48.44_PM.png)

![Rhythmbox logo](https://courses.edx.org/assets/courseware/v1/687be8b4d50a2fef213ec5ffd0a1dfd8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/2000px-Rhythmbox_logo_256px.svg.png)

###   
Movie Players

Movie (video) players can portray input from many different sources, either local to the machine or on the Internet.

![Picture showing logos of VLC, MPlayer, Xine and Totem](https://courses.edx.org/assets/courseware/v1/30a387dca706a3a2e03403c3918c0a3a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch17_screen13.jpg)

Linux systems offer a number of movie players, including:

* VLC
* MPlayer
* Xine
* Totem

### Movie Editors

Movie editors are used to edit videos or movies. Linux systems offer a number of movie editors, including:

<table border="0" align="left" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto; font-size: 16px; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Application</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Use</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Cinepaint</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Frame-by-frame retouching. Cinepaint is used for editing images in a video.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Blender</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Create 3D animation and design. Blender is a professional tool that uses modeling as a starting point. There are complex and powerful tools for camera capture, recording, editing, enhancing and creating video, each having its own focus.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Cinelerra</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Capture, compose, and edit audio/video.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">FFmpeg</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Record, convert, and stream audio/video. FFmpeg is a format converter, among other things, and has other tools such as<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">ffplay</strong><span>&nbsp;</span>and<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">ffserver</strong>.</td></tr></tbody></table>

![Cinepaint logo](https://courses.edx.org/assets/courseware/v1/95c74e658654dc7a2e470cf4c4a44fe0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lp_cinepaint.png)

![Blender logo](https://courses.edx.org/assets/courseware/v1/c39a5cff9c78cfea1ad459acdbe4fb0f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/blenderlogosocket.png)

![Cinelerra logo](https://courses.edx.org/assets/courseware/v1/3b627fb386a21a6e955331d2522f2d8c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cinelerra-logo.png)

![FFmpeg logo](https://courses.edx.org/assets/courseware/v1/74a177f8982742c68c666dfe2d11c18a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/2000px-FFmpeg_Logo_new.svg.png)

###   
GIMP (GNU Image Manipulation Program)

Graphic editors allow you to create, edit, view, and organize images of various formats, like Joint Photographic Experts Group (JPEG or JPG), Portable Network Graphics (PNG), Graphics Interchange Format (GIF), and Tagged Image File Format (TIFF).

The GNU Image Manipulation Program (GIMP) is a feature-rich image retouching and editing tool similar to Adobe Photoshop and is available on all Linux distributions. Some features of the GIMP are:

* It can handle any image file format.
* It has many special purpose plugins and filters.
* It provides extensive information about the image, such as layers, channels, and histograms.

![Screenshot of the GIMP editor](https://courses.edx.org/assets/courseware/v1/eb5482ce7f196048de0070d3a517dd8c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gimpsuse.png)
_GIMP Editor_

### Graphics Utilities

In addition to GIMP, there are other graphics utilities that help perform various image-related tasks, including:

<table border="0" align="left" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Graphic Utility</strong></span></td><td align="center" bgcolor="#003f60" width="57%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Use</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">eog</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Eye of Gnome (eog) is an image viewer that provides slide show capability and a few image editing tools, such as rotate and resize. It can also step through the images in a directory with just a click.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Inkscape</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Inkscape is an image editor with lots of editing features. It works with layers and transformations of the image. It is sometimes compared to Adobe Illustrator.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">convert</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">convert is a command line tool (part of the ImageMagick set of applications) that can modify image files in many ways. The options include file format conversion and numerous image modification options, such as blur, resize, despeckle, etc.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Scribus</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Scribus is used for creating documents used for publishing and providing a<span>&nbsp;</span><em style="line-height: 1.4em; font-style: italic;">What You See Is What You Get (WYSIWYG)</em><span>&nbsp;</span>environment. It also provides numerous editing tools.</td></tr></tbody></table>

![eog Logo](https://courses.edx.org/assets/courseware/v1/51f5d22403673922faa621eeaf5ec6f3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/eog.jpeg)

![Inkscape Logo](https://courses.edx.org/assets/courseware/v1/d3c6cef446815cb7744a5d3c02ceb78f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/inkscape-logo.png)

![Image Magic Logo](https://courses.edx.org/assets/courseware/v1/7dfca43de79c0839c4b3f676f6c60988/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/logo_liquid-60.gif)

## Chapter Summary

You have completed Chapter 6. Let’s summarize the key concepts covered:

* Linux offers a wide variety of Internet applications, such as web browsers, email clients, online media applications, and others.
* Web browsers supported by Linux can be either graphical or text-based, such as Firefox, Google Chrome, Epiphany, w3m, lynx, and others.
* Linux supports graphical email clients, such as Thunderbird, Evolution, and Claws Mail, and text mode email clients, such as Mutt and mail.
* Linux systems provide many other applications for performing Internet-related tasks, such as Filezilla, XChat, Pidgin, and others.
* Most Linux distributions offer LibreOffice to create and edit different kinds of documents.
* Linux systems offer entire suites of development applications and tools, including compilers and debuggers.
* Linux systems offer a number of sound players including Amarok, Audacity, and Rhythmbox.
* Linux systems offer a number of movie players, including VLC, MPlayer, Xine, and Totem.
* Linux systems offer a number of movie editors, including Kino, Cinepaint, Blender among others.
* The GIMP (GNU Image Manipulation Program) utility is a feature-rich image retouching and editing tool available on all Linux distributions.
* Other graphics utilities that help perform various image-related tasks are eog, Inkscape, convert, and Scribus.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 7: Command Line Operations

### Learning Objectives

By the end of this chapter, you should be able to:

* Use the command line to perform operations in Linux.
* Search for files.
* Create and manage files.
* Install and update software.

### Introduction to the Command Line

Linux system administrators spend a significant amount of their time at a command line prompt. They often automate and troubleshoot tasks in this text environment. There is a saying, _"graphical user interfaces make easy tasks easier, while command line interfaces make difficult tasks possible"_. Linux relies heavily on the abundance of command line tools. The command line interface provides the following advantages:

* No GUI overhead is incurred.
* Virtually any and every task can be accomplished while sitting at the command line.
* You can implement scripts for often-used (or easy-to-forget) tasks and series of procedures.
* You can sign into remote machines anywhere on the Internet.
* You can initiate graphical applications directly from the command line instead of hunting through menus.
* While graphical tools may vary among Linux distributions, the command line interface does not.

![Command line](https://courses.edx.org/assets/courseware/v1/aff4954e12f4f2a299a3c763a1679773/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cmdline.png)

### Using a Text Terminal on the Graphical Desktop

A **terminal emulator** program emulates (simulates) a standalone terminal within a window on the desktop. By this, we mean it behaves essentially as if you were logging into the machine at a pure text terminal with no running graphical interface. Most terminal emulator programs support multiple terminal sessions by opening additional tabs or windows.

By default, on GNOME desktop environments, the **gnome-terminal** application is used to emulate a text-mode terminal in a window. Other available terminal programs include:

* **xterm**
* **konsole** (default on KDE)
* **terminator**

![Using $ ls -a command on Ubuntu, openSUSE, Gentoo, and CentOS](https://courses.edx.org/assets/courseware/v1/38f9208d04f151d5d360416b21a00db7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/terminalall.png)
_$ ls -a_

### Launching Terminal Windows



To open a terminal on any system using a recent GNOME desktop click on **Applications > System Tools > Terminal** or **Applications > Utilities > Terminal**. If you do not have the **Applications** menu, you will have to install the appropriate **gnome-shell-extension** package and turn on with **gnome-tweaks**.

On any but some of the most recent GNOME-based distributions, you can always open a terminal by right-clicking anywhere on the desktop background and selecting **Open in Terminal**. If this does not work you will once again need to install and activate the appropriate **gnome-shell-extension** package.

You can also hit **Alt-F2** and type in either **gnome-terminal** or **konsole**, whichever is appropriate.

Because distributions have had a history of burying opening up a command line terminal, and the place in menus may vary in the desktop GUI, It is a good idea to figure out how to "pin" the terminal icon to the panel, which might mean adding it to the Favorites grouping on GNOME systems.

![Screenshot showing how to open a terminal on any system using GNOME desktop](https://courses.edx.org/assets/courseware/v1/8f3255532efb831d557e3fd804d6b6a9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/applications.png)
_Opening a Terminal Using GNOME Desktop_

### Some Basic Utilities

There are some basic command line utilities that are used constantly, and it would be impossible to proceed further without using some of them in simple form before we discuss them in more detail. A short list has to include:

* **cat**: used to type out a file (or combine files).
* **head**: used to show the first few lines of a file.
* **tail**: used to show the last few lines of a file.
* **man**: used to view documentation.

The screenshot shows elementary uses of these programs. Note the use of the pipe symbol (**|**) used to have one program take as input the output of another.

For the most part, we will only use these utilities in screenshots displaying various activities, before we discuss them in detail.

![Screenshot showing basic command line utilities](https://courses.edx.org/assets/courseware/v1/4a2d0c574b1aca9a21e03764634688c7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cmdutils.png)
_Basic Command Line Utilities_

### The Command Line

Most input lines entered at the shell prompt have three basic elements:

* Command
* Options
* Arguments

The command is the name of the program you are executing. It may be followed by one or more options (or switches) that modify what the command may do. Options usually start with one or two dashes, for example, **-p** or **--print**, in order to differentiate them from arguments, which represent what the command operates on.

However, plenty of commands have no options, no arguments, or neither. In addition, other elements (such as setting environment variables) can also appear on the command line when launching a task.

### sudo

All the demonstrations created have a user configured with **sudo** capabilities to provide the user with administrative (admin) privileges when required. **sudo** allows users to run programs using the security privileges of another user, generally root (superuser).

On your own systems, you may need to set up and enable **sudo** to work correctly. To do this, you need to follow some steps that we will not explain in much detail now, but you will learn about later in this course. When running on Ubuntu and some other recent distributions, **sudo** is already always set up for you during installation. On other Linux distributions, you will likely need to set up **sudo** to work properly for you after the initial installation.

Next, you will learn the steps to set up and run **sudo** on your system.

![sudo ls -la /root](https://courses.edx.org/assets/courseware/v1/a33e740a25f053b970a27e7ebb0055b6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sudosuse.png)
_sudo ls -la /root_

### Steps for Setting Up and Running sudo

If your system does not already have **sudo** set up and enabled, you need to do the following steps:

1. You will need to make modifications as the administrative, or superuser, root. While **sudo** will become the preferred method of doing this, we do not have it set up yet, so we will use **su** (which we will discuss later in detail) instead. At the command line prompt, type **su** and press **Enter**. You will then be prompted for the root password, so enter it and press **Enter**. You will notice that nothing is printed; this is so others cannot see the password on the screen. You should end up with a different looking prompt, often ending with ‘**#**’. For example:  
**$ su** **Password:**  
**#**
2. Now, you need to create a configuration file to enable your user account to use sudo. Typically, this file is created in the **/etc/sudoers.d/** directory with the name of the file the same as your username. For example, for this demo, let’s say your username is **student**. After doing step 1, you would then create the configuration file for **student** by doing this:  
**# echo "student ALL=(ALL) ALL" > /etc/sudoers.d/student**
3. Finally, some Linux distributions will complain if you do not also change permissions on the file by doing:  
**# chmod 440 /etc/sudoers.d/student**

That should be it. For the rest of this course, if you use **sudo** you should be properly set up. When using **sudo**, by default you will be prompted to give a password (your own user password) at least the first time you do it within a specified time interval. It is possible (though very insecure) to configure **sudo** to not require a password or change the time window in which the password does not have to be repeated with every **sudo** command.

![Image](https://courses.edx.org/assets/courseware/v1/5e50e3c0ee4bb967610271e4e43862c3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sandwich.png)

**Sandwich**  
(Retrieved from [XKCD](https://xkcd.com/149/), provided under a [Creative Commons Attribution-NonCommercial 2.5 License](https://creativecommons.org/licenses/by-nc/2.5/))

### Switching Between the GUI and the Command Line

The customizable nature of Linux allows you to drop the graphical interface (temporarily or permanently) or to start it up after the system has been running.

Most Linux distributions give an option during installation (or have more than one version of the install media) to choose between desktop (with a graphical desktop) and server (usually without one).

Linux production servers are usually installed without the GUI, and even if it is installed, usually do not launch it during system startup. Removing the graphical interface from a production server can be very helpful in maintaining a lean system, which can be easier to support and keep secure.

![Switching Between the GUI and the Command Line](https://courses.edx.org/assets/courseware/v1/117f4f89c2400d3fb8cb296a7dc13c65/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/debianterminal.png)
_Switching between the GUI and the Command Line_

### Virtual Terminals

**Virtual Terminals** (**VT**) are console sessions that use the entire display and keyboard outside of a graphical environment. Such terminals are considered "virtual" because, although there can be multiple active terminals, only one terminal remains visible at a time. A VT is not quite the same as a command line terminal window; you can have many of those visible at once on a graphical desktop.

One virtual terminal (usually number one or seven) is reserved for the graphical environment, and text logins are enabled on the unused VTs. Ubuntu uses VT 7, but CentOS/RHEL and openSUSE use VT 1 for the graphical display.

An example of a situation where using VTs is helpful is when you run into problems with the graphical desktop. In this situation, you can switch to one of the text VTs and troubleshoot.

To switch between VTs, press **CTRL-ALT-function** key for the VT. For example, press **CTRL-ALT-F6** for VT 6. Actually, you only have to press the **ALT-F6** key combination if you are in a VT and want to switch to another VT.

![Switching between virtual terminals](https://courses.edx.org/assets/courseware/v1/cce9159be8b08390567dc02f1043cf92/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen07.jpg)
_Switching between Virtual Terminals_

### Turning Off the Graphical Desktop

Linux distributions can start and stop the graphical desktop in various ways. The exact method differs from distribution and among distribution versions. For the newer systemd-based distributions, the display manager is run as a service, you can stop the GUI desktop with the systemctl utility and most distributions will also work with the **telinit** command, as in:

**$ sudo systemctl stop gdm** (or **sudo telinit 3**)

and restart it (after logging into the console) with:

**$ sudo systemctl start gdm** (or **sudo telinit 5**)

On Ubuntu versions before 18.04 LTS, substitute **lightdm** for **gdm**.

![Turning Off the Graphical Desktop](https://courses.edx.org/assets/courseware/v1/7d39cf055c684fe05168b1f42819daf1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/console.png)

## Basic Operations

In this section, we will discuss how to accomplish basic operations from the command line. These include how to log in and log out from the system, restart or shut down the system, locate applications, access directories, identify absolute and relative paths, and explore the filesystem.

![Basic operations: cd, cat, echo, ls, rmdir, man, exit, login, mkdir](https://courses.edx.org/assets/courseware/v1/678d889dcb1112024ef10815f9210a07/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen11.jpg)
_Basic Operations_

### Logging In and Out

An available text terminal will prompt for a username (with the string **login:**) and password. When typing your password, nothing is displayed on the terminal (not even a ***** to indicate that you typed in something), to prevent others from seeing your password. After you have logged into the system, you can perform basic operations.

Once your session is started (either by logging into a text terminal or via a graphical terminal program), you can also connect and log into remote systems by using Secure SHell (SSH). For example, by typing **ssh student@remote-server.com**, SSH would connect securely to the remote machine (**remote-server.com**) and give **student** a command line terminal window, using either a password (as with regular logins) or cryptographic key to sign in without providing a password to verify the identity.

![Logging In and Out](https://courses.edx.org/assets/courseware/v1/e0941aff295156471c049248a7d21464/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntulogin.png)

### Rebooting and Shutting Down

The preferred method to shut down or reboot the system is to use the **shutdown** command. This sends a warning message, and then prevents further users from logging in. The init process will then control shutting down or rebooting the system. It is important to always shut down properly; failure to do so can result in damage to the system and/or loss of data.

The **halt** and **poweroff** commands issue **shutdown -h** to halt the system; **reboot** issues **shutdown -r** and causes the machine to reboot instead of just shutting down. Both rebooting and shutting down from the command line requires superuser (root) access.

When administering a multi-user system, you have the option of notifying all users prior to shutdown, as in:

**$ sudo shutdown -h 10:00 "Shutting down for scheduled maintenance."**

_**NOTE**_: On recent Wayland**-**based Linux distributions, broadcast messages do not appear on terminal emulation sessions running on the desktop; they appear only on the VT console displays.

![Rebooting and Shutting Down: $ sudo shutdown -h](https://courses.edx.org/assets/courseware/v1/fcfc77b8338d21c5b242707a434d0f0a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntushutdown.png)
_Rebooting and Shutting Down_

### Locating Applications

Depending on the specifics of your particular distribution's policy, programs and software packages can be installed in various directories. In general, executable programs and scripts should live in the **/bin**, **/usr/bin**, **/sbin**, **/usr/sbin** directories, or somewhere under **/opt**. They can also appear in **/usr/local/bin** and **/usr/local/sbin**, or in a directory in a user's account space, such as **/home/student/bin**.

One way to locate programs is to employ the which utility. For example, to find out exactly where the diff program resides on the filesystem:

**$ which diff**  
**/usr/bin/diff**

If **which** does not find the program, **whereis** is a good alternative because it looks for packages in a broader range of system directories:

**$ whereis diff**  
**diff: /usr/bin/diff /usr/share/man/man1/diff.1.gz /usr/share/man/man1p/diff.1p.gz**

as well as locating source and **man** files packaged with the program.

![which and whereis Utilities](https://courses.edx.org/assets/courseware/v1/716532f91059bd5a66899f8ef6e07c31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/whereis.png)
_`which` and `whereis` Utilities_

### Accessing Directories

When you first log into a system or open a terminal, the default directory should be your home directory. You can print the exact path of this by typing **echo $HOME**. Many Linux distributions actually open new graphical terminals in **$HOME/Desktop**. The following commands are useful for directory navigation:

<table height="280" align="center" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 603.047px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="25%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="75%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Result</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Displays the present working directory</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd ~</span></strong></span><span>&nbsp;</span>or<span>&nbsp;</span><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd</span></strong></span></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Change to your home directory (shortcut name is<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">~</span></strong><span>&nbsp;</span>(tilde))</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd ..</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Change to parent directory (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">..</span></strong>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">cd -</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Change to previous directory (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">- (minus)</span></strong>)</td></tr></tbody></table>

Video: Accessing Directories

<video controls width="100%" preload="none">

<source src="https://edx-video.net/41e9ceca-8aa4-4b08-8afc-8162da7ce91d-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Understanding Absolute and Relative Paths

There are two ways to identify paths:

* **Absolute pathname**  
An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file. Absolute paths always start with **/**.
* **Relative pathname**  
A relative pathname starts from the present working directory. Relative paths never start with **/**.

Multiple slashes (**/**) between directories and files are allowed, but all but one slash between elements in the pathname is ignored by the system. **////usr//bin** is valid, but seen as **/usr/bin** by the system.

Most of the time, it is most convenient to use relative paths, which require less typing. Usually, you take advantage of the shortcuts provided by: **.** (present directory), **..** (parent directory) and **~** (your home directory).

For example, suppose you are currently working in your home directory and wish to move to the **/usr/bin** directory. The following two ways will bring you to the same directory from your home directory:

* Absolute pathname method  
**$ cd /usr/bin**
* Relative pathname method  
**$ cd ../../usr/bin**

In this case, the absolute pathname method requires less typing.

![Understanding Absolute and Relative Paths](https://courses.edx.org/assets/courseware/v1/c9a79bc0bfc23d476b1c89380ca90aad/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen19.jpg)
_Understanding Absolute and Relative Paths_

### Exploring the Filesystem

Traversing up and down the filesystem tree can get tedious. The **tree** command is a good way to get a bird’s-eye view of the filesystem tree. Use **tree -d** to view just the directories and to suppress listing file names.

![Exploring the Filesystem: tree -d](https://courses.edx.org/assets/courseware/v1/1bfb9dae7fe271d3ab73c66d983aadff/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tree-d.png)
_Exploring the Filesystem_



The following commands can help in exploring the filesystem:

<table border="0" align="left" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 877px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="75%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd /</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Changes your current directory to the root (/) directory (or path you supply)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ls</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">List the contents of the present working directory</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ls –a</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">List all files, including hidden files and directories (those whose name start with . )</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tree</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Displays a tree view of the filesystem</td></tr></tbody></table>

Video: Exploring the Filesystem

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V006100_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Hard Links

The **ln** utility is used to create hard links and (with the **-s** option) soft links, also known as symbolic links or symlinks. These two kinds of links are very useful in UNIX-based operating systems.

Suppose that **file1** already exists. A hard link, called **file2**, is created with the command:

**$ ln file1 file2**

Note that two files now appear to exist. However, a closer inspection of the file listing shows that this is not quite true.

**$ ls -li file1 file2**

The **-i** option to **ls** prints out in the first column the inode number, which is a unique quantity for each file object. This field is the same for both of these files; what is really going on here is that it is only one file, but it has more than one name associated with it, as is indicated by the **2** that appears in the **ls** output. Thus, there was already another object linked to **file1** before the command was executed.

Hard links are very useful and they save space, but you have to be careful with their use, sometimes in subtle ways. For one thing, if you remove either **file1** or **file2** in the example, the inode object (and the remaining file name) will remain, which might be undesirable, as it may lead to subtle errors later if you recreate a file of that name.

If you edit one of the files, exactly what happens depends on your editor; most editors, including **vi** and **gedit**, will retain the link _by default_, but it is possible that modifying one of the names may break the link and result in the creation of two objects.

![Hard Links: $ touch file1, $ ln file1 file2, $ ls -li file?](https://courses.edx.org/assets/courseware/v1/aefe6c7fa6a198680e110ceae5c95c11/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lnubuntu.png)

### Soft (Symbolic) Links

Soft (or Symbolic) links are created with the **-s** option, as in:

**$ ln -s file1 file3**  
**$ ls -li file1 file3**

Notice **file3** no longer appears to be a regular file, and it clearly points to **file1** and has a different inode number.

Symbolic links take no extra space on the filesystem (unless their names are very long). They are extremely convenient, as they can easily be modified to point to different places. An easy way to create a shortcut from your **home** directory to long pathnames is to create a symbolic link.

Unlike hard links, soft links can point to objects even on different filesystems, partitions, and/or disks and other media, which may or may not be currently available or even exist. In the case where the link does not point to a currently available or existing object, you obtain a dangling link.

![Soft (Symbolic) Links: $ ln -s file1 file3, $ ls -li file?](https://courses.edx.org/assets/courseware/v1/cea407ef8cfd36b34ede2a154959a98f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lnsubuntu.png)
_Soft (Symbolic) Links_

### Navigating the Directory History

The **cd** command remembers where you were last, and lets you get back there with **cd -**. For remembering more than just the last directory visited, use **pushd** to change the directory instead of **cd**; this pushes your starting directory onto a list. Using **popd** will then send you back to those directories, walking in reverse order (the most recent directory will be the first one retrieved with **popd**). The list of directories is displayed with the **dirs** command.

![Navigating Through Directory History: $mkdir /tmp/dirl /tmp/dir2](https://courses.edx.org/assets/courseware/v1/319814cbd06ee587a78854e88478c5b0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pushdfedora.png)
_Navigating Through Directory History_

Video: Navigating the Directory History

<video controls width="100%" preload="none">

<source src="https://edx-video.net/89eb42ec-3c89-4dec-8b73-c9b890c88d9f-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Working with Files

Linux provides many commands that help you with viewing the contents of a file, creating a new file or an empty file, changing the timestamp of a file, and moving, removing and renaming a file or directory. These commands help you in managing your data and files and in ensuring that the correct data is available at the correct location.

![Yellow folders with papers](https://courses.edx.org/assets/courseware/v1/08e475796103299f4fcfac22b2c67fd7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen47A.jpg)

In this section, you will learn how to manage files.

### Viewing Files

You can use the following command line utilities to view files:

<table align="left" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 861.5px; margin: 20px auto 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Command</span></strong></td><td align="center" bgcolor="#003f60" width="85%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Usage</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">cat</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used for viewing files that are not very long; it does not provide any scroll-back.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">tac</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to look at a file backwards, starting with the last line.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">less</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to view larger files because it is a paging program. It pauses at each screen full of text, provides scroll-back capabilities, and lets you search and navigate within the file.<br style="line-height: 1.4em;"><br style="line-height: 1.4em;"><em style="line-height: 1.4em; font-style: italic;"><strong style="font-weight: bold; line-height: 1.4em;">NOTE</strong>: Use&nbsp;<span style="color: inherit; font-style: italic; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">/</strong></span>&nbsp;to search for a pattern in the forward direction and&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: italic; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">?</span></strong>&nbsp;for a pattern in the backward direction. An older program named&nbsp;more&nbsp;is still used, but has fewer capabilities: "less&nbsp;is&nbsp;more".</em></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">tail</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to print the last 10 lines of a file by default. You can change the number of lines by doing&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-n 15</span></strong><span>&nbsp;</span>or just<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">-15</strong></span><span>&nbsp;</span>if you wanted to look at the last 15 lines instead of the default.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">head</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">The opposite of&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tail</span></strong><span style="color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;">; by default, it prints the first 10 lines of a file.</span></td></tr></tbody></table>

Video: More on Viewing Files

<video controls width="100%" preload="none">

<source src="https://edx-video.net/6244a0ed-8260-4df0-bbee-553dae259d64-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### touch

**touch** is often used to set or update the access, change, and modify times of files. By default, it resets a file's timestamp to match the current time.

However, you can also create an empty file using **touch**:

**$ touch <filename>**

This is normally done to create an empty file as a placeholder for a later purpose.

**touch** provides several useful options. For example, the **-t** option allows you to set the date and timestamp of the file to a specific value, as in:

**$ touch -t 12091600 myfile**

This sets the **myfile** file's timestamp to 4 p.m., December 9th (12 09 1600).

![touch](https://courses.edx.org/assets/courseware/v1/d29a554d4187aae729d4ed40e42a0146/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/touch.png)
_touch_

### mkdir and rmdir

**mkdir** is used to create a directory:

* **mkdir sampdir**   
It creates a sample directory named **sampdir** under the current directory.
* **mkdir /usr/sampdir**   
It creates a sample directory called **sampdir** under **/usr**.

Removing a directory is done with **rmdir**. The directory must be empty or the command will fail. To remove a directory and all of its contents you have to do **rm -rf**.

![mkdir ](https://courses.edx.org/assets/courseware/v1/72f578cd278d2bd6bd48d63efbfe589e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/mkdir.png)
_mkdir_

### Moving, Renaming or Removing a File

Note that **mv** does double duty, in that it can:

* Simply rename a file
* Move a file to another location, while possibly changing its name at the same time.

If you are not certain about removing files that match a pattern you supply, it is always good to run **rm** interactively (**rm –i**) to prompt before every removal.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 516.898px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Command</span></strong></td><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Usage</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mv</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Rename a file&nbsp;</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Remove a file&nbsp;</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm –f</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Forcefully remove a file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm –i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Int</span>eractively remove a file</td></tr></tbody></table>

### Renaming or Removing a Directory

**rmdir** works only on empty directories; otherwise you get an error.

While typing **rm –rf** is a fast and easy way to remove a whole filesystem tree recursively, it is extremely dangerous and should be used with the utmost care, especially when used by root (recall that recursive means drilling down through all sub-directories, all the way down a tree).

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 516.898px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mv</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Rename a directory</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rmdir</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Remove an empty directory</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm -rf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Forcefully remove a directory recursively</td></tr></tbody></table>

### Modifying the Command Line Prompt

The **PS1** variable is the character string that is displayed as the prompt on the command line. Most distributions set **PS1** to a known default value, which is suitable in most cases. However, users may want custom information to show on the command line. For example, some system administrators require the user and the host system name to show up on the command line as in:

**student@c8 $**

This could prove useful if you are working in multiple roles and want to be always reminded of who you are and what machine you are on. The prompt above could be implemented by setting the **PS1** variable to: **\u@\h \$**.

For example:

**$ echo $PS1**  
**\$**  
**$ PS1="\u@\h \$ "**  
**student@c8 $ echo $PS1**  
**\u@\h \$**  
**student@c8 $**  


By convention, most systems are set up so that the root user has a pound sign (**#**) as their prompt.

![Thought bubble displaying Have an idea for a prompt? question](https://courses.edx.org/assets/courseware/v1/999a9aca943e61f41473186765960c14/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/prompt.png)

Video: Working With Files and Directories at the Command Prompt

<video controls width="100%" preload="none">

<source src="https://edx-video.net/0a2c05cb-7749-4c31-b351-8c1cc7791859-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Standard File Streams

When commands are executed, by default there are three standard file streams (or descriptors) always open for use: standard input (standard in or **stdin**), standard output (standard out or **stdout**) and standard error (or **stderr**).

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 689.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Name</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Symbolic Name</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Value</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Example</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">standard input</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">stdin</strong></code></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">keyboard</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">standard output</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">stdout</strong></code></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">terminal</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">standard error</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">stderr</strong></code></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">2</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">log file</td></tr></tbody></table>

Usually, **stdin** is your keyboard, and **stdout** and **stderr** are printed on your terminal. **stderr** is often redirected to an error logging file, while **stdin** is supplied by directing input to come from a file or from the output of a previous command through a pipe. **stdout** is also often redirected into a file. Since **stderr** is where error messages are written, usually nothing will go there.

In Linux, all open files are represented internally by what are called file descriptors. Simply put, these are represented by numbers starting at zero. **stdin** is file descriptor 0, **stdout** is file descriptor 1, and **stderr** is file descriptor 2. Typically, if other files are opened in addition to these three, which are opened by default, they will start at file descriptor 3 and increase from there.

On the next page and in the chapters ahead, you will see examples which alter where a running command gets its input, where it writes its output, or where it prints diagnostic (error) messages.

### I/O Redirection

Through the command shell**,** we can redirect the three standard file streams so that we can get input from either a file or another command, instead of from our keyboard, and we can write output and errors to files or use them to provide input for subsequent commands.

For example, if we have a program called **do_something** that reads from **stdin** and writes to **stdout** and **stderr**, we can change its input source by using the less-than sign (**<**) followed by the name of the file to be consumed for input data:

**$ do_something < input-file**

If you want to send the output to a file, use the greater-than sign (**>**) as in:  
  
**$ do_something > output-file**

Because **stderr** is not the same as **stdout**, error messages will still be seen on the terminal windows in the above example.

If you want to redirect **stderr** to a separate file, you use **stderr**’s file descriptor number (2), the greater-than sign (**>**), followed by the name of the file you want to hold everything the running command writes to **stderr**:  
  
**$ do_something 2> error-file**

_**NOTE:** By the same logic, **do_something 1> output-file** is the same as **do_something > output-file**._

A special shorthand notation can send anything written to file descriptor **2** (**stderr**) to the same place as file descriptor **1** (**stdout**): **2>&1**.

**$ do_something > all-output-file 2>&1**

bash permits an easier syntax for the above:

**$ do_something >& all-output-file**

### Pipes

The UNIX/Linux philosophy is to have many simple and short programs (or commands) cooperate together to produce quite complex results, rather than have one complex program with many possible options and modes of operation. In order to accomplish this, extensive use of pipes is made. You can pipe the output of one command or program into another as its input.

In order to do this, we use the vertical-bar, pipe symbol (**|**), between commands as in:  
   
**$ command1 | command2 | command3**

The above represents what we often call a pipeline, and allows Linux to combine the actions of several commands into one. This is extraordinarily efficient because **command2** and **command3** do not have to wait for the previous pipeline commands to complete before they can begin hacking at the data in their input streams; on multiple CPU or core systems, the available computing power is much better utilized and things get done quicker.

Furthermore, there is no need to save output in (temporary) files between the stages in the pipeline, which saves disk space and reduces reading and writing from disk, which is often the slowest bottleneck in getting something done.

![Pipeline](https://courses.edx.org/assets/courseware/v1/50bdd18ba2e7d4343c184f5e0e3e058a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pipeline.png)
_Pipeline_

### Searching for Files

Being able to quickly find the files you are looking for will save you time and enhance productivity. You can search for files in both your home directory space, or in any other directory or location on the system.

![File cabinets](https://courses.edx.org/assets/courseware/v1/4495f95739476edc371e3a69b29f8fc2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen32a.jpg)

The main tools for doing this are the **locate** and **find** utilities. We will also show how to use wildcards in **bash**, in order to specify any file which matches a given generalized request.

### locate

The **locate** utility program performs a search taking advantage of a previously constructed database of files and directories on your system, matching all entries that contain a specified character string. This can sometimes result in a very long list.

To get a shorter (and possibly more relevant) list, we can use the **grep** program as a filter. **grep** will print only the lines that contain one or more specified strings, as in:

**$ locate zip | grep bin**

which will list all the files and directories with both **zip** and **bin** in their name. We will cover **grep** in much more detail later. Notice the use of **|** to pipe the two commands together.

**locate** utilizes a database created by a related utility, **updatedb**. Most Linux systems run this automatically once a day. However, you can update it at any time by just running **updatedb** from the command line as the root user.

![locate](https://courses.edx.org/assets/courseware/v1/db04248c7965e78a927a0fa8a42fc703/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/locatesuse.png)
_locate_

Video: Locating Files

<video controls width="100%" preload="none">

<source src="https://edx-video.net/d9de7136-78d9-4cf5-9549-1b61e2f31d4e-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Wildcards and Matching File Names

You can search for a filename containing specific characters using wildcards.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 710.797px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Wildcard</strong></span></td><td align="center" bgcolor="#003f60" width="75%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Result</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">?</span></strong>&nbsp;</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Matches any single character</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">*</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Matches any string of characters</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[set]</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Matches any character in the set of characters, for example<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[adf]</span></strong><span>&nbsp;</span>will match any occurrence of<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">a</strong></span>,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">d</span></strong>, or<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">f</strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">[!set]</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Matches any character not in the set of characters</span></td></tr></tbody></table>

To search for files using the **?** wildcard, replace each unknown character with **?**. For example, if you know only the first two letters are 'ba' of a three-letter filename with an extension of **.out**, type **ls ba?.out**.

To search for files using the ***** wildcard, replace the unknown string with *****. For example, if you remember only that the extension was **.out**, type **ls *.out**.

Video: Using Wildcards to Search for Files

<video controls width="100%" preload="none">

<source src="https://edx-video.net/162ffd59-cf5b-4896-aade-b99a16aa95fa-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### The find Program

**find** is an extremely useful and often-used utility program in the daily life of a Linux system administrator. It recurses down the filesystem tree from any particular directory (or set of directories) and locates files that match specified conditions. The default pathname is always the present working directory.

For example, administrators sometimes scan for potentially large core files (which contain diagnostic information after a program fails) that are more than several weeks old in order to remove them.

It is also common to remove files in inessential or outdated files in **/tmp** (and other volatile directories, such as those containing cached files) that have not been accessed recently. Many Linux distributions use shell scripts that run periodically (through **cron** usually) to perform such house cleaning.

![find](https://courses.edx.org/assets/courseware/v1/102046563ac484a6047300c801886837/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findubuntu.png)
_find_

### Using find

When no arguments are given, **find** lists all files in the current directory and all of its subdirectories. Commonly used options to shorten the list include **-name** (only list files with a certain pattern in their name), **-iname** (also ignore the case of file names), and **-type** (which will restrict the results to files of a certain specified type, such as **d** for directory, **l** for symbolic link, or **f** for a regular file, etc.).

Searching for files and directories named **gcc**:  
  
**$ find /usr -name gcc**

Searching only for directories named **gcc**:  
  
**$ find /usr -type d -name gcc**

Searching only for regular files named **gcc**:  
  
**$ find /usr -type f -name gcc**

![Using the find command](https://courses.edx.org/assets/courseware/v1/ea8161eed2e8b061792778df2dec70d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findrhel7.png)
_Using find_

### Using Advanced find Options

Another good use of **find** is being able to run commands on the files that match your search criteria. The **-exec** option is used for this purpose.

To find and remove all files that end with **.swp**:

**$ find -name "*.swp" -exec rm {} ’;’**

The **{}** (squiggly brackets) is a placeholder that will be filled with all the file names that result from the find expression, and the preceding command will be run on each one individually.

Please note that you have to end the command with either ‘**;**’ (including the single-quotes) or "**\;**". Both forms are fine.

One can also use the **-ok** option, which behaves the same as **-exec**, except that **find** will prompt you for permission before executing the command. This makes it a good way to test your results before blindly executing any potentially dangerous commands.

![Finding and Removing Files that Ends with .swp](https://courses.edx.org/assets/courseware/v1/cbdf6dc606a39eace7d669077837e628/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen41.jpg)
_Finding and Removing Files that End with .swp_

### Finding Files Based on Time and Size

It is sometimes the case that you wish to find files according to attributes, such as when they were created, last used, etc., or based on their size. It is easy to perform such searches.

To find files based on time:  
  
**$ find / -ctime 3**

Here, **-ctime** is when the inode metadata (i.e. file ownership, permissions, etc.) last changed; it is often, but not necessarily, when the file was first created. You can also search for accessed/last read (**-atime**) or modified/last written (**-mtime**) times. The number is the number of days and can be expressed as either a number (**n**) that means exactly that value, **+n**, which means greater than that number, or **-n**, which means less than that number. There are similar options for times in minutes (as in **-cmin**, **-amin**, and **-mmin**).

To find files based on sizes:

**$ find / -size 0**

Note the size here is in 512-byte blocks, by default; you can also specify bytes (c), kilobytes (k), megabytes (M), gigabytes (G), etc. As with the time numbers above, file sizes can also be exact numbers (**n**), **+n** or **-n**. For details, consult the man page for find.

For example, to find files greater than 10 MB in size and running a command on those files:  
  
**$ find / -size +10M -exec command {} ’;’**

![Finding Files Based on Time and Size](https://courses.edx.org/assets/courseware/v1/007f36e6f54ef7e1547682492e8a9b93/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findsizerhel7.png)
_Finding Files Based on Time and Size_

Video: Finding Files In a Directory

<video controls width="100%" preload="none">

<source src="https://edx-video.net/467b3768-bf4b-4ba1-9899-87ef71310722-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Package Management Systems on Linux

The core parts of a Linux distribution and most of its add-on software are installed via the **Package Management System**. Each package contains the files and other instructions needed to make one software component work well and cooperate with the other components that comprise the entire system. Packages can depend on each other. For example, a package for a web-based application written in PHP can depend on the PHP package.

![Box filled with various objects](https://courses.edx.org/assets/courseware/v1/5bb5d9653cc975c21a23103c015b1483/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen59a.jpg)

There are two broad families of package managers: those based on Debian and those which use RPM as their low-level package manager. The two systems are incompatible, but broadly speaking, provide the same features and satisfy the same needs. There are some other systems used by more specialized Linux distributions.

In this section, you will learn how to install, remove, or search for packages from the command line using these two package management systems.

### Package Managers: Two Levels

Both package management systems operate on two distinct levels: a low-level tool (such as **dpkg** or **rpm**) takes care of the details of unpacking individual packages, running scripts, getting the software installed correctly, while a high-level tool (such as **apt-get**, **dnf, yum**_,_ or **zypper**) works with groups of packages, downloads packages from the vendor, and figures out dependencies.

Most of the time users need to work only with the high-level tool, which will take care of calling the low-level tool as needed. Dependency resolution is a particularly important feature of the high-level tool, as it handles the details of finding and installing each dependency for you. Be careful, however, as installing a single package could result in many dozens or even hundreds of dependent packages being installed.

![Package Managers: Two Levels](https://courses.edx.org/assets/courseware/v1/b2cfd35138881e077bfc97915aed86b8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Package_Managers.png)
_Package Managers: Two Levels_

### Working With Different Package Management Systems

The Advanced Packaging Tool (**apt**) is the underlying package management system that manages software on Debian-based systems. While it forms the backend for graphical package managers, such as the Ubuntu Software Center and synaptic, its native user interface is at the command line, with programs that include **apt** (or **apt-get**) and **apt-cache**.

**dnf** is the open source command-line package-management utility for the RPM-compatible Linux systems that belongs to the Red Hat family. **dnf** has both command line and graphical user interfaces. Fedora and RHEL 8 replaced the older **yum** utility with **dnf**, thereby eliminating a lot of historical baggage, as well as introducing many nice new capabilities. **dnf** is pretty much backwards-compatible with **yum** for day-to-day commands.

![Working with Different Package Management Systems](https://courses.edx.org/assets/courseware/v1/272cd4906572ff37d0352281abe81dbe/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Different_Package_Mmanagement_Tools.png)

**zypper** is the package management system for the SUSE/openSUSE family and is also based on RPM. **zypper** also allows you to manage repositories from the command line. **zypper** is fairly straightforward to use and resembles **dnf**/**yum** quite closely.

To learn the basic packaging commands, take a look at these basic packaging commands:

<table height="395" align="center" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 800px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="padding-left" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p align="padding-left" style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Operation</strong></span></p></td><td width="30%" align="padding-left" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p align="padding-left" style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">rpm</strong></span></p></td><td width="30%" align="padding-left" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p align="padding-left" style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">deb</strong></span></p></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Install package</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rpm -i foo.rpm</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --install foo.deb</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Install package, dependencies</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;install foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get install foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Remove package</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -e foo.rpm</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --remove foo.deb</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Remove package, dependencies</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;remove foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get autoremove foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Update package</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -U foo.rpm</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --install foo.deb</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Update package, dependencies</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;update foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get install foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Update entire system</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;update</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get dist-upgrade</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Show all installed packages</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -qa</strong></span><span>&nbsp;</span>or&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf list installed</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --list</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Get information on package</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -qil foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --listfiles foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Show packages named<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">foo</strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;list "foo"</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-cache search foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Show all available packages</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;list</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-cache dumpavail foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">What package is<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">file</strong></span><span>&nbsp;</span>part of?</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -qf file</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --search file</strong></span></td></tr></tbody></table>

### Video: Low-Level Debian Package Management with dpkg

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001500_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: Low-Level RPM Package Management with rpm

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001600_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: High-Level Package Management with dnf

<video controls width="100%" preload="none">

<source src="https://edx-video.net/825ce6b8-4cc5-4680-ae8d-a31efd12b83a-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: High-Level Package Management with zypper on openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002400_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: High-Level Package Management with apt on Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001800_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Chapter Summary

You have completed Chapter 7. Let’s summarize the key concepts we covered:

* Virtual terminals (VT) in Linux are consoles, or command line terminals that use the connected monitor and keyboard.
* Different Linux distributions start and stop the graphical desktop in different ways.
* A terminal emulator program on the graphical desktop works by emulating a terminal within a window on the desktop.
* The Linux system allows you to either log in via text terminal or remotely via the console.
* When typing your password, nothing is printed to the terminal, not even a generic symbol to indicate that you typed.
* The preferred method to shut down or reboot the system is to use the **shutdown** command.
* There are two types of pathnames**:** absolute and relative.
* An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file.
* A relative pathname starts from the present working directory.
* Using hard and soft (symbolic) links is extremely useful in Linux.
* **cd** remembers where you were last, and lets you get back there with **cd -**.
* **locate** performs a database search to find all file names that match a given pattern.
* **find** locates files recursively from a given directory or set of directories.
* **find** is able to run commands on the files that it lists, when used with the **-exec** option.
* **touch** is used to set the access, change, and edit times of files, as well as to create empty files.
* The Advanced Packaging Tool (**apt**) package management system is used to manage installed software on Debian-based systems.
* You can use the **dnf** command-line package management utility for the RPM-based Red Hat Family Linux distributions.
* The **zypper** package management system is based on RPM and used for openSUSE.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 8: Finding Linux Documentation

### Learning Objectives

By the end of this chapter, you should be able to:

* Use different sources of documentation.
* Use the man pages.
* Access the GNU Info System.
* Use the **help** command and **--help** option.
* Use other documentation sources.

### Linux Documentation Sources

Whether you are an inexperienced user or a veteran, you will not always know (or remember) the proper use of various Linux programs and utilities: what is the command to type, what options does it take, etc. You will need to consult help documentation regularly. Because Linux-based systems draw from a large variety of sources, there are numerous reservoirs of documentation and ways of getting help. Distributors consolidate this material and present it in a comprehensive and easy-to-use manner.

![Linux Documentation Sources](https://courses.edx.org/assets/courseware/v1/cf55b1fe48a37f0ae2fed5fee049c262/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch07_screen03.jpg)

**Linux Documentation Sources**

Important Linux documentation sources include:

* The **man** pages (short for manual pages)
* GNU Info
* The **help** command and **--help** option
* Other documentation sources, e.g. [Gentoo Handbook](https://www.gentoo.org/support/documentation/) or [Ubuntu Documentation](https://help.ubuntu.com/community/CommunityHelpWiki).

### The man pages

The man pages are the most often-used source of Linux documentation. They provide in-depth documentation about many programs and utilities, as well as other topics, including configuration files, and programming APIs for system calls, library routines, and the kernel. They are present on all Linux distributions and are always at your fingertips.

The man pages infrastructure was first introduced in the early UNIX versions, at the beginning of the 1970s. The name man is just an abbreviation for manual.

![Book](https://courses.edx.org/assets/courseware/v1/be369a4b31dfa8c5655024c337b9c1b8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch07_screen05.jpg)

Typing man with a topic name as an argument retrieves the information stored in the topic's man pages.

man pages are often converted to other formats, such as PDF documents and web pages. To learn more, take a look at [Linux man pages online](http://man7.org/linux/man-pages/). Many web pages have a graphical interface for help items, which may include man pages.

Other sources of documentation include published books and many Internet sites.

### man

The **man** program searches, formats, and displays the information contained in the man page system. Because many topics have copious amounts of relevant information, output is piped through a pager program (such as **less**) to be viewed one page at a time. At the same time, the information is formatted for a good visual display.

A given topic may have multiple pages associated with it and there is a default order determining which one is displayed when no options or section number is specified. To list all pages on the topic, use the **-f** option. To list all pages that discuss a specific topic (even if the specified subject is not present in the name), use the **–k** option.

* **man –f** generates the same result as typing **whatis**.
* **man –k** generates the same result as typing **apropos**.

The default order is specified in **/etc/man_db.conf** and is roughly (but not exactly) in ascending numerical order by section.

![man -f sysctl](https://courses.edx.org/assets/courseware/v1/c164a9474ac7ecb00e78799f2cfd602c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/man1.png)
_man_

### Manual Chapters

The man pages are divided into chapters numbered 1 through 9. In some cases, a letter is appended to the chapter number to identify a specific topic. For example, many pages describing part of the X Window API are in chapter **3X**.

The chapter number can be used to force man to display the page from a particular chapter. It is common to have multiple pages across multiple chapters with the same name, especially for names of library functions or system calls.

With the **-a** parameter, man will display all pages with the given name in all chapters, one after the other, as in:

**$ man -a socket**

![Manual Chapters: $ man -a socket](https://courses.edx.org/assets/courseware/v1/83583dd77505523938107d8480bea1d4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/manchap.png)
_Manual Chapters_

### Video: Using man

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002300_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### The GNU Info System

The next source of Linux documentation is the GNU Info System.

This is the GNU project's standard documentation format, which it prefers as an alternative to **man**. The Info System is basically free-form, and supports linked subsections.

![GNU Project logo](https://courses.edx.org/assets/courseware/v1/6f9aed0e12194cfc5c52cf50664c3bdd/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/GNU_Project_logo.jpg)

Functionally, **info** resembles man in many ways. However, topics are connected using links (even though its design predates the World Wide Web). Information can be viewed through either a command line interface, a graphical help utility, printed or viewed online.

### Using info from the Command Line

Typing **info** with no arguments in a terminal window displays an index of available topics. You can browse through the topic list using the regular movement keys: arrows, **Page Up**, and **Page Down**.

You can view help for a particular topic by typing **info <topic name>**. The  system then searches for the topic in all available **info** files.

Some useful keys are: **q** to quit, **h** for help, and **Enter** to select a menu item.

![info](https://courses.edx.org/assets/courseware/v1/d7c774dd6b4b262495a16a57aed417a5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/infoubuntu.png)
_info_

### info Page Structure

The topic which you view in an info page is called a **node**. The table lists the basic keystrokes for moving between nodes.

Nodes are essentially sections and subsections in the documentation. You can move between nodes or view each node sequentially. Each node may contain menus and linked subtopics, or items.

Items function like browser links and are identified by an asterisk (*****) at the beginning of the item name. Named items (outside a menu) are identified with double-colons (**::**) at the end of the item name. Items can refer to other nodes within the file or to other files.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 344.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key&nbsp;</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Function</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" :="" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px; font-family: &quot;Courier New&quot;;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">n</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Go to the next node</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">p</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Go to the previous node</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">u</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move one node up in the index</td></tr></tbody></table>

### Video: Using info

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002200_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### The --help Option

Another important source of Linux documentation is use of the **--help** option.

Most commands have an available short description which can be viewed using the **--help** or the **-h** option along with the command or application. For example, to learn more about the **man** command, you can type:

**$ man --help**

The **--help** option is useful as a quick reference and it displays information faster than the **man** or **info** pages.

![The --help Option](https://courses.edx.org/assets/courseware/v1/f9d86b387589f5e13d24cc7e88272e61/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/manhelp.png)
_The --help Option_

### The help Command

When run within a **bash** command shell, some popular commands (such as **echo** and **cd**) actually run especially built-in **bash** versions of the commands rather than the usual binaries found on the file system, say under **/bin** or **/usr/bin**. It is more efficient to do so as execution is faster because fewer resources are used (we will discuss command shells later). One should note that there can be some (usually small) differences in the two versions of the command.

To view a synopsis of these built-in commands, you can simply type **help** as shown in the screenshot.

For these built-in commands, **help** performs the same basic function as the **-h** and **--help** arguments perform for standalone programs.

![The help Command](https://courses.edx.org/assets/courseware/v1/79040611925a7890d2337fb896445e08/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/helpbash.png)
_The help Command_

### Other Documentation Sources

In addition to the man pages, the GNU Info System, and the **help** command, there are other sources of Linux documentation, some examples of which include:

* Desktop help system
* Package documentation
* Online resources.

![Other Documentation Sources](https://courses.edx.org/assets/courseware/v1/d4be6c97491354162222dd6068f4ba04/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch07_screen23.jpg)
_Other Documentation Sources_

### Graphical Help Systems

All Linux desktop systems have a graphical help application. This application is usually displayed as a question-mark icon or an image of a ship’s life-preserver, and can also always be found within the menu system. These programs usually contain custom help for the desktop itself and some of its applications, and will sometimes also include graphically-rendered **info** and **man** pages.

If you do not want to spend time hunting for the right icon or menu item to launch the help application, you can also start the graphical help system from a terminal window or command prompt by using one of the following utility programs:

* GNOME: **gnome-help** or **yelp**
* KDE: **khelpcenter**

![GNOME Help](https://courses.edx.org/assets/courseware/v1/c782c9043e9c07ee0e290aaff8503432/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnome-help.png)
_GNOME Help_



![KDE Help Center](https://courses.edx.org/assets/courseware/v1/d7496895a50216347fcd26f479adb0b9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/khelpcenter.png)
_KDE Help_

### Package Documentation

Linux documentation is also available as part of the package management system. Usually, this documentation is directly pulled from the upstream source code, but it can also contain information about how the distribution packaged and set up the software.

Such information is placed under the **/usr/share/doc** directory, grouped in subdirectories named after each package, perhaps including the version number in the name.

![Package Documentation](https://courses.edx.org/assets/courseware/v1/dcab137a19a95616557b1c49f0754419/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/usrsharedoc.png)
_Package Documentation_

### Online Resources

There are many places to access online Linux documentation, and a little bit of searching will get you buried in it.

The following book has been well-reviewed by other users of this course. It is a free, downloadable command line compendium under a Creative Commons license: _"[The Linux Command Line](http://linuxcommand.org/tlcl.php)"_ by William Shotts.

You can also find very helpful documentation for each distribution. Each distribution has its own user-generated forums and wiki sections. Here are just a few links to such sources:

* [Ubuntu Documentation](https://help.ubuntu.com/)
* [CentoS Documentation](https://wiki.centos.org/Documentation)
* [openSUSE Documentation](https://doc.opensuse.org/)
* [Gentoo Documentation](https://www.gentoo.org/support/documentation/)
* [Fedora Documentation](https://docs.fedoraproject.org/).

Moreover, you can use online search sites to locate helpful resources from all over the Internet, including blog posts, forum and mailing list posts, news articles, and so on.

### Chapter Summary

You have completed Chapter 8. Let’s summarize the key concepts covered:

* The main sources of Linux documentation are the man pages, GNU info, the **help** options and command, and a rich variety of online documentation sources.
* The **man** utility searches, formats, and displays man pages.
* The man pages provide in-depth documentation about programs and other topics about the system, including configuration files, system calls, library routines, and the kernel.
* The GNU Info System was created by the GNU project as its standard documentation. It is robust and is accessible via command line, web, and graphical tools using **info**.
* Short descriptions for commands are usually displayed with the **-h** or **--help** argument.
* You can type **help** at the command line to display a synopsis of built-in commands.
* There are many other help resources both on your system and on the Internet.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 9: Processes

### Learning Objectives

By the end of this chapter, you should be able to:

* Describe what a process is and distinguish between types of processes.
* Enumerate process attributes.
* Manage processes using **ps** and **top**.
* Understand the use of load averages and other process metrics.
* Manipulate processes by putting them in background and restoring them to foreground.
* Use **at**, **cron**, and **sleep** to schedule processes in the future or pause them.

### What Is a Process?

A **process** is simply an instance of one or more related tasks (threads) executing on your computer. It is not the same as a **program** or a **command**. A single command may actually start several processes simultaneously. Some processes are independent of each other and others are related. A failure of one process may or may not affect the others running on the system.

![Processes](https://courses.edx.org/assets/courseware/v1/219d348bf46fa4b3b8c83b3dbdf3fb31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen03.jpg)
_Processes_

Processes use many system resources, such as memory, CPU (central processing unit) cycles, and peripheral devices, such as network cards, hard drives, printers and displays. The operating system (especially the kernel) is responsible for allocating a proper share of these resources to each process and ensuring overall optimized system utilization.

### Process Types

A terminal window (one kind of command shell) is a process that runs as long as needed. It allows users to execute programs and access resources in an interactive environment. You can also run programs in the background, which means they become detached from the shell.

Processes can be of different types according to the task being performed. Here are some different process types, along with their descriptions and examples:

<table width="80%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 861.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Process Type</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td><td width="25%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Example</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Interactive Processes</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Need to be started by a user, either at a command line or through a graphical interface such as an icon or a menu selection.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">bash, firefox, top</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Batch Processes</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Automatic processes which are scheduled from and then disconnected from the terminal. These tasks are queued and work on a&nbsp;<strong style="font-weight: bold; line-height: 1.4em;">FIFO</strong><span>&nbsp;</span>(<strong style="font-weight: bold; line-height: 1.4em;">F</strong>irst-<strong style="font-weight: bold; line-height: 1.4em;">I</strong>n,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">F</strong>irst-<strong style="font-weight: bold; line-height: 1.4em;">O</strong>ut) basis.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">updatedb, ldconfig</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Daemons</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Server processes that run continuously. Many are launched during system startup and then wait for a user or system request indicating that their service is required.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">httpd, sshd, libvirtd</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Threads</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Lightweight processes. These are tasks&nbsp;that run under the umbrella of a main process, sharing memory and other resources, but are scheduled and run by the system on an individual basis. An individual thread can end without terminating the whole process and a process can create new threads at any time. Many non-trivial programs are&nbsp;multi-threaded.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">firefox, gnome-terminal-server</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Kernel Threads</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Kernel tasks that users neither start nor terminate and have little control over. These may perform actions like moving a thread from one CPU to another, or making sure input/output operations to disk are completed.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">kthreadd, migration, ksoftirqd</strong></td></tr></tbody></table>

### Process Scheduling and States

A critical kernel function called the **scheduler** constantly shifts processes on and off the CPU, sharing time according to relative priority, how much time is needed and how much has already been granted to a task.

When a process is in a so-called **running** state, it means it is either currently executing instructions on a CPU, or is waiting to be granted a share of time (a time slice) so it can execute. All processes in this state reside on what is called a run queue and on a computer with multiple CPUs, or cores, there is a run queue on each.

![Process Scheduling and States](https://courses.edx.org/assets/courseware/v1/49178932e74cb80a82c62db4fff8ce2a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen05.jpg)
_Process Scheduling and States_

However, sometimes processes go into what is called a **sleep** state, generally when they are waiting for something to happen before they can resume, perhaps for the user to type something. In this condition, a process is said to be sitting in a wait queue.

There are some other less frequent process states, especially when a process is terminating. Sometimes, a child process completes, but its parent process has not asked about its state. Amusingly, such a process is said to be in a zombie state; it is not really alive, but still shows up in the system's list of processes.

### Process and Thread IDs

At any given time, there are always multiple processes being executed. The operating system keeps track of them by assigning each a unique process ID (**PID**) number. The PID is used to track process state, CPU usage, memory use, precisely where resources are located in memory, and other characteristics.

New PIDs are usually assigned in ascending order as processes are born. Thus, PID 1 denotes the **init** process (initialization process), and succeeding processes are gradually assigned higher numbers.

The table explains the PID types and their descriptions:

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 861.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">ID Type</strong></span></td><td align="center" bgcolor="#003f60" width="70%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Process ID (PID)</td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Unique Process ID number</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Parent Process ID (PPID)</td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Process (Parent) that started this process. If the parent dies, the PPID will refer to an adoptive parent; on recent kernels, this is kthreadd which has PPID=2.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Thread ID (TID)</td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Thread ID number. This is the same as the PID for single-threaded processes. For a multi-threaded process, each thread shares the same PID, but has a unique TID.</td></tr></tbody></table>

### Terminating a Process

At some point, one of your applications may stop working properly. How do you eliminate it?

To terminate a process, you can type **kill -SIGKILL <pid>** or **kill -9 <pid>**.

Note, however, you can only kill your own processes; those belonging to another user are off limits, unless you are root.

![Terminating a Process](https://courses.edx.org/assets/courseware/v1/6a71bd8d47df4eaf7e430d8089c632a5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/rhelkill.png)
_Terminating a Process_

### User and Group IDs

Many users can access a system simultaneously, and each user can run multiple processes. The operating system identifies the user who starts the process by the Real User ID (RUID) assigned to the user.

The user who determines the access rights for the users is identified by the Effective UID (EUID). The EUID may or may not be the same as the RUID.

![User and Group IDs](https://courses.edx.org/assets/courseware/v1/fbe122ffd13edf336ad978cddb953a7f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen07.jpg)
_User and Group IDs_

Users can be categorized into various groups. Each group is identified by the Real Group ID (RGID). The access rights of the group are determined by the Effective Group ID (EGID). Each user can be a member of one or more groups.

Most of the time we ignore these details and just talk about the User ID (UID) and Group ID (GID).

### More About Priorities

At any given time, many processes are running (i.e. in the run queue) on the system. However, a CPU can actually accommodate only one task at a time, just like a car can have only one driver at a time. Some processes are more important than others, so Linux allows you to set and manipulate process priority. Higher priority processes get preferential access to the CPU.

The priority for a process can be set by specifying a **nice value**, or niceness, for the process. The lower the nice value, the higher the priority. Low values are assigned to important processes, while high values are assigned to processes that can wait longer. A process with a high nice value simply allows other processes to be executed first. In Linux, a nice value of **-20** represents the highest priority and **+19** represents the lowest. While this may sound backwards, this convention (the nicer the process, the lower the priority) goes back to the earliest days of UNIX.

![nice output](https://courses.edx.org/assets/courseware/v1/d929bb0d3a611c780e2dcb6dd00cddd5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/niceout.png)
_nice Output_

You can also assign a so-called **real-time priority** to time-sensitive tasks, such as controlling machines through a computer or collecting incoming data. This is just a very high priority and is not to be confused with what is called hard real-time which is conceptually different, and has more to do with making sure a job gets completed within a very well-defined time window.

![Nice Values](https://courses.edx.org/assets/courseware/v1/fcc61556971b7cdefbafabf3d7abab22/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen08.jpg)
_Nice Values_

### Video: Using renice to Set Priorities

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000100_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Load Averages

The **load average** is the average of the load number for a given period of time. It takes into account processes that are:

* Actively running on a CPU.
* Considered runnable, but waiting for a CPU to become available.
* Sleeping: i.e. waiting for some kind of resource (typically, I/O) to become available.

_**NOTE**_: Linux differs from other UNIX-like operating systems in that it includes the sleeping processes. Furthermore, it only includes so-called **uninterruptible** sleepers, those which cannot be awakened easily.

The load average can be viewed by running **w**, **top** or **uptime**. We will explain the numbers on the next page.

![Load Averages: w](https://courses.edx.org/assets/courseware/v1/ca05a14d78d8e3bb26b519fe65047a66/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wuptimesuse.png)
_Load Averages_

### Interpreting Load Averages

The load average is displayed using three numbers (**0.45**, **0.17**, and **0.12**) in the below screenshot. Assuming our system is a single-CPU system, the three load average numbers are interpreted as follows:

* **0.45**: For the last minute the system has been 45% utilized on average.
* **0.17**: For the last 5 minutes utilization has been 17%.
* **0.12**: For the last 15 minutes utilization has been 12%.

If we saw a value of **1.00** in the second position, that would imply that the single-CPU system was 100% utilized, on average, over the past 5 minutes; this is good if we want to fully use a system. A value over **1.00** for a single-CPU system implies that the system was over-utilized: there were more processes needing CPU than CPU was available.

If we had more than one CPU, say a quad-CPU system, we would divide the load average numbers by the number of CPUs. In this case, for example, seeing a 1 minute load average of **4.00** implies that the system as a whole was 100% (4.00/4) utilized during the last minute.

Short-term increases are usually not a problem. A high peak you see is likely a burst of activity, not a new level. For example, at start up, many processes start and then activity settles down. If a high peak is seen in the 5 and 15 minute load averages, it may be cause for concern.

![Interpreting Load Averages](https://courses.edx.org/assets/courseware/v1/5ad78e82ed03efc7777fad630abed5dd/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/woutputrhel.png)
_Interpreting Load Averages_

### Background and Foreground Processes

Linux supports background and foreground job processing. A job in this context is just a command launched from a terminal window. Foreground jobs run directly from the shell, and when one foreground job is running, other jobs need to wait for shell access (at least in that terminal window if using the GUI) until it is completed. This is fine when jobs complete quickly. But this can have an adverse effect if the current job is going to take a long time (even several hours) to complete.

In such cases, you can run the job in the background and free the shell for other tasks. The background job will be executed at lower priority, which, in turn, will allow smooth execution of the interactive tasks, and you can type other commands in the terminal window while the background job is running. By default, all jobs are executed in the foreground. You can put a job in the background by suffixing **&** to the command, for example: **updatedb &**.

You can either use **CTRL-Z** to suspend a foreground job or **CTRL-C** to terminate a foreground job and can always use the **bg** and **fg** commands to run a process in the background and foreground, respectively.

![Background and Foreground Processes](https://courses.edx.org/assets/courseware/v1/3ff2741d99789599c91efda5c5028150/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bgfgrhel.png)
_Background and Foreground Processes_

### Managing Jobs

The **jobs** utility displays all jobs running in background. The display shows the job ID, state, and command name, as shown here.

**jobs -l** provides the same information as **jobs**, and adds the PID of the background jobs.

The background jobs are connected to the terminal window, so, if you log off, the **jobs** utility will not show the ones started from that window.

![Managing Jobs](https://courses.edx.org/assets/courseware/v1/8dcff92dcec85e717944d972b96d6fcc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/jobsrhel.png)
_Managing Jobs_

### The ps Command (System V Style)

**ps** provides information about currently running processes keyed by PID. If you want a repetitive update of this status, you can use **top** or other commonly installed variants (such as **htop** or **atop**) from the command line, or invoke your distribution's graphical system monitor application.

**ps** has many options for specifying exactly which tasks to examine, what information to display about them, and precisely what output format should be used.

Without options, **ps** will display all processes running under the current shell. You can use the **-u** option to display information of processes for a specified username. The command **ps -ef** displays all the processes in the system in full detail. The command **ps -eLf** goes one step further and displays one line of information for every thread (remember, a process can contain multiple threads).

![The ps Command (System V Style)](https://courses.edx.org/assets/courseware/v1/a910c16bb6f18c4d38e9ff123a6f5e02/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntupsef.png)
_The ps Command (System V Style)_

### The ps Command (BSD Style)

**ps** has another style of option specification, which stems from the BSD variety of UNIX, where options are specified without preceding dashes. For example, the command **ps aux** displays all processes of all users. The command **ps axo** allows you to specify which attributes you want to view.

The screenshot shows a sample output of **ps** with the **aux** and **axo** qualifiers.

![The ps Command (BSD Style)](https://courses.edx.org/assets/courseware/v1/8cca52331523da587fab092df4bc7dba/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/psbsdrhel.png)
_The ps Command (BSD Style)_

### Video: Using ps

<video controls width="100%" preload="none">

<source src="https://edx-video.net/322cee4c-fb31-4b26-98c0-0fcb3da2b7aa-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### The Process Tree

**pstree** displays the processes running on the system in the form of a tree diagram showing the relationship between a process and its parent process and any other processes that it created. Repeated entries of a process are not displayed, and threads are displayed in curly braces.

![The Process Tree](https://courses.edx.org/assets/courseware/v1/bce96558c9c9be5c152a567a0c63d392/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntupstree.png)
_The Process Tree_

### top

While a static view of what the system is doing is useful, monitoring the system performance live over time is also valuable. One option would be to run **ps** at regular intervals, say, every few seconds. A better alternative is to use **top** to get constant real-time updates (every two seconds by default), until you exit by typing **q.top** clearly highlights which processes are consuming the most CPU cycles and memory (using appropriate commands from within **top**).

![top](https://courses.edx.org/assets/courseware/v1/9eaf15c635ff33e0dbd318a36f295925/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhel.png)
_top_

### First Line of the top Output

The first line of the **top** output displays a quick summary of what is happening in the system, including:

* How long the system has been up
* How many users are logged on
* What is the load average

The load average determines how busy the system is. A load average of 1.00 per CPU indicates a fully subscribed, but not overloaded, system. If the load average goes above this value, it indicates that processes are competing for CPU time. If the load average is very high, it might indicate that the system is having a problem, such as a runaway process (a process in a non-responding state).

![First Line of the the top Output](https://courses.edx.org/assets/courseware/v1/f70432d89645e43f5d72008706908bbc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline1.png)
_First Line of the top Output_

### Second Line of the top Output

The second line of the **top** output displays the total number of processes, the number of running, sleeping, stopped, and zombie processes. Comparing the number of running processes with the load average helps determine if the system has reached its capacity or perhaps a particular user is running too many processes. The stopped processes should be examined to see if everything is running correctly.

![Second Line of the top Output](https://courses.edx.org/assets/courseware/v1/486c9e55bf24f2dca9f628f0a3362bcf/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline2.png)
_Second Line of the top Output_

### Third Line of the top Output

The third line of the **top** output indicates how the CPU time is being divided between the users (**us**) and the kernel (**sy**) by displaying the percentage of CPU time used for each.

The percentage of user jobs running at a lower priority (**niceness - ni**) is then listed. Idle mode (**id**) should be low if the load average is high, and vice versa. The percentage of jobs waiting (**wa**) for I/O is listed. Interrupts include the percentage of hardware (**hi**) vs. software interrupts (**si**). Steal time (**st**) is generally used with virtual machines, which has some of its idle CPU time taken for other uses.

![Third Line of the top Output](https://courses.edx.org/assets/courseware/v1/49e0cb9bbb88ccb9cc6ff9c4f32bc243/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline3.png)
_Third Line of the top Output_

### Fourth and Fifth Lines of the top Output

The fourth and fifth lines of the **top** output indicate memory usage, which is divided in two categories:

* Physical memory (RAM) – displayed on line 4.
* Swap space – displayed on line 5.

Both categories display total memory, used memory, and free space.

You need to monitor memory usage very carefully to ensure good system performance. Once the physical memory is exhausted, the system starts using swap space (temporary storage space on the hard drive) as an extended memory pool, and since accessing disk is much slower than accessing memory, this will negatively affect system performance.

If the system starts using swap often, you can add more swap space. However, adding more physical memory should also be considered.

![Fourth and Fifth Lines of the top Output](https://courses.edx.org/assets/courseware/v1/8ec74d523983230af0d3c4d4f1556dfb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline4-5.png)
_Fourth and Fifth Lines of the top Output_

### Process List of the top Output

Each line in the process list of the **top** output displays information about a process. By default, processes are ordered by highest CPU usage. The following information about each process is displayed:

* Process Identification Number (**PID**)
* Process owner (**USER**)
* Priority (**PR**) and nice values (**NI**)
* Virtual (**VIRT**), physical (**RES**), and shared memory (**SHR**)
* Status (**S**)
* Percentage of CPU (**%CPU**) and memory (**%MEM**) used
* Execution time (**TIME+**)
* Command (**COMMAND**).

![Process List of the top Output](https://courses.edx.org/assets/courseware/v1/9eaf15c635ff33e0dbd318a36f295925/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhel.png)
_Process List of the top Output_

### Interactive Keys with top

Besides reporting information, **top** can be utilized interactively for monitoring and controlling processes. While **top** is running in a terminal window, you can enter single-letter commands to change its behavior. For example, you can view the top-ranked processes based on CPU or memory usage. If needed, you can alter the priorities of running processes or you can stop/kill a process.

The table lists what happens when pressing various keys when running **top**:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 689.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Output</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">t</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Display or hide summary information (rows 2 and 3)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">m</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Display or hide memory information (rows 4 and 5)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">A</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Sort the process list by top resource consumers</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">r</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Renice (change the priority of) a specific processes</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">k</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Kill a specific process</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">f</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Enter the<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">top</span></strong><span>&nbsp;</span>configuration screen</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">o</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Interactively select a new sort order in the process list</td></tr></tbody></table>

### Video: Using top

<video controls width="100%" preload="none">

<source src="https://edx-video.net/da3272c6-9559-41ac-a8b2-1168df22670c-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Video: Using System Monitoring

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000200_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Scheduling Future Processes Using at

Suppose you need to perform a task on a specific day sometime in the future. However, you know you will be away from the machine on that day. How will you perform the task? You can use the **at** utility program to execute any non-interactive command at a specified time, as illustrated in the screenshot below:

![Output of at command](https://courses.edx.org/assets/courseware/v1/ec37c00269266c49e55f7a52aab93f9a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/atout.png)
_Scheduling Future Processes Using at_

### cron

**cron** is a time-based scheduling utility program. It can launch routine background jobs at specific times and/or days on an on-going basis. **cron** is driven by a configuration file called **/etc/crontab** (cron table), which contains the various shell commands that need to be run at the properly scheduled times. There are both system-wide **crontab** files and individual user-based ones. Each line of a **crontab** file represents a job, and is composed of a so-called **CRON** expression, followed by a shell command to execute.

Typing **crontab -e** will open the crontab editor to edit existing jobs or to create new jobs. Each line of the **crontab** file will contain 6 fields:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 689.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="26%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Field</strong></span></td><td width="26%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td><td width="28%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Values</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">MIN</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Minutes</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0 to 59</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">HOUR</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Hour field</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0 to 23</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">DOM</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Day of Month</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1-31</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">MON</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Month field</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1-12</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">DOW</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Day Of Week</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0-6 (0 = Sunday)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CMD</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Command</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Any command to be executed</td></tr></tbody></table>

**Examples:**

* The entry *** * * * * /usr/local/bin/execute/this/script.sh** will schedule a job to execute **script.sh** every minute of every hour of every day of the month, and every month and every day in the week.
* The entry **30 08 10 06 * /home/sysadmin/full-backup** will schedule a full-backup at 8.30 a.m., 10-June, irrespective of the day of the week.

### sleep

Sometimes, a command or job must be delayed or suspended. Suppose, for example, an application has read and processed the contents of a data file and then needs to save a report on a backup system. If the backup system is currently busy or not available, the application can be made to sleep (wait) until it can complete its work. Such a delay might be to mount the backup device and prepare it for writing.

**sleep** suspends execution for at least the specified period of time, which can be given as the number of seconds (the default), minutes, hours, or days. After that time has passed (or an interrupting signal has been received), execution will resume.

The syntax is:  
  
**sleep NUMBER[SUFFIX]...**  
  
where **SUFFIX** may be:

* **s** for seconds (the default)
* **m** for minutes
* **h** for hours
* **d** for days.

**sleep** and **at** are quite different; **sleep** delays execution for a specific period, while **at** starts execution at a later time.

![sleep](https://courses.edx.org/assets/courseware/v1/b9444a7d9db9ee97c557d2373530b24d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sleepsuse.png)
_sleep_

## Chapter Summary

You have completed Chapter 9. Let’s summarize the key concepts covered:

* Processes are used to perform various tasks on the system.
* Processes can be single-threaded or multi-threaded.
* Processes can be of different types, such as interactive and non-interactive.
* Every process has a unique identifier (PID) to enable the operating system to keep track of it.
* The nice value, or niceness, can be used to set priority.
* **ps** provides information about the currently running processes.
* You can use **top** to get constant real-time updates about overall system performance, as well as information about the processes running on the system.
* Load average indicates the amount of utilization the system is under at particular times.
* Linux supports background and foreground processing for a job.
* **at** executes any non-interactive command at a specified time.
* **cron** is used to schedule tasks that need to be performed at regular intervals.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 10: File Operations

### Learning Objectives

By the end of this chapter, you should be able to:

* Explore the filesystem and its hierarchy.
* Explain the filesystem architecture.
* Compare files and identify different file types.
* Back up and compress data.

### Introduction to Filesystems

In Linux (and all UNIX-like operating systems) it is often said “Everything is a file”, or at least it is treated as such. This means whether you are dealing with normal data files and documents, or with devices such as sound cards and printers, you interact with them through the same kind of Input/Output (I/O) operations. This simplifies things: you open a “file” and perform normal operations like reading the file and writing on it (which is one reason why text editors, which you will learn about in an upcoming section, are so important).

On many systems (including Linux), the filesystem is structured like a tree. The tree is usually portrayed as inverted, and starts at what is most often called the **root directory**, which marks the beginning of the hierarchical filesystem and is also sometimes referred to as the trunk, or simply denoted by **/**. The root directory is _not_ the same as the root user. The hierarchical filesystem also contains other elements in the path (directory names), which are separated by forward slashes (**/**), as in **/usr/bin/emacs**, where the last element is the actual file name.

In this section, you will learn about some basic concepts, including the filesystem hierarchy, as well as about disk partitions.

![Filesystems](https://courses.edx.org/assets/courseware/v1/6c6a76e5e83450a2f75777a86ba8e790/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen_03.jpg)
_Filesystems_

### Filesystem Varieties

Linux supports a number of native filesystem types, expressly created by Linux developers, such as:

* ext3
* ext4
* squashfs
* btrfs

It also offers implementations of filesystems used on other alien operating systems, such as those from:

* Windows (ntfs, vfat)
* SGI (xfs)
* IBM (jfs)
* MacOS (hfs, hfs+)

Many older, legacy filesystems, such as FAT, are also supported.

It is often the case that more than one filesystem type is used on a machine, based on considerations such as the size of files, how often they are modified, what kind of hardware they sit on and what kind of access speed is needed, etc. The most advanced filesystem types in common use are the **journaling** varieties: ext4, xfs, btrfs, and jfs. These have many state-of-the-art features and high performance, and are very hard to corrupt accidentally.

### Linux Partitions

Each filesystem on a Linux system occupies a disk **partition**. Partitions help to organize the contents of disks according to the kind and use of the data contained. For example, important programs required to run the system are often kept on a separate partition (known as **root** or **/**) than the one that contains files owned by regular users of that system (**/home**). In addition, temporary files created and destroyed during the normal operation of Linux may be located on dedicated partitions. One advantage of this kind of isolation by type and variability is that when all available space on a particular partition is exhausted, the system may still operate normally.

The picture shows the use of the **gparted** utility, which displays the partition layout on a system which has four operating systems on it: RHEL 8, CentOS 7, Ubuntu and Windows.

![Linux Partitions: gparted](https://courses.edx.org/assets/courseware/v1/6b82906abb49600a3143f0f3fd8208de/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gparted.png)
_Linux Partitions: gparted_

### Mount Points

Before you can start using a filesystem, you need to **mount** it on the filesystem tree at a mount point. This is simply a directory (which may or may not be empty) where the filesystem is to be grafted on. Sometimes, you may need to create the directory if it does not already exist.

![Mount Points](https://courses.edx.org/assets/courseware/v1/90eea9eba0b63783a8bcf2b85ae8a9e3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen06.jpg)
_Mount Points_

**_WARNING_**_: If you mount a filesystem on a non-empty directory, the former contents of that directory are covered-up and not accessible until the filesystem is unmounted. Thus, mount points are usually empty directories._

### Mounting and Unmounting

The **mount** command is used to attach a filesystem (which can be local to the computer or on a network) somewhere within the filesystem tree. The basic arguments are the **device node** and mount point. For example,

**$ sudo mount /dev/sda5 /home**

will attach the filesystem contained in the disk partition associated with the **/dev/sda5** device node into the filesystem tree at the **/home** mount point. There are other ways to specify the partition other than the device node, such as using the disk label or UUID.

To unmount the partition, the command would be:

**$ sudo umount /home**

Note the command is **umount**, not unmount! Only a root user (logged in as root, or using **sudo**) has the privilege to run these commands, unless the system has been otherwise configured.

If you want it to be automatically available every time the system starts up, you need to edit **/etc/fstab** accordingly (the name is short for filesystem table). Looking at this file will show you the configuration of all pre-configured filesystems. **man fstab** will display how this file is used and how to configure it.

Executing **mount** without any arguments will show all presently mounted filesystems.

The command **df -Th** (disk-free) will display information about mounted filesystems, including the filesystem type, and usage statistics about currently used and available space.

![Mounting and Unmounting](https://courses.edx.org/assets/courseware/v1/18cd65d8ee6e189efd405e7e3c890f2d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/dfmountdebian.png)
_Mounting and Unmounting_

### NFS and Network Filesystems

It is often necessary to share data across physical systems which may be either in the same location or anywhere that can be reached by the Internet. A network (also sometimes called distributed) filesystem may have all its data on one machine or have it spread out on more than one network node. A variety of different filesystems can be used locally on the individual machines; a network filesystem can be thought of as a grouping of lower level filesystems of varying types.

![NFS client-server architecture](https://courses.edx.org/assets/courseware/v1/312ecb4a904d47191a99c6b1443f8b32/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/NFS_LFS101.png)
_****The Client-Server Architecture of NFS****<span class="-mobiledoc-kit__atom">‌‌</span>(based on the original from [www.ibm.com](https://www.ibm.com/developerworks/library/l-network-filesystems/))_



Many system administrators mount remote users' home directories on a server in order to give them access to the same files and configuration files across multiple client systems. This allows the users to log in to different computers, yet still have access to the same files and resources.

The most common such filesystem is named simply **NFS** (the **N**etwork **F**ile**s**ystem). It has a very long history and was first developed by Sun Microsystems**.** Another common implementation is **CIFS** (also termed **SAMBA**), which has Microsoft roots. We will restrict our attention in what follows to NFS.

### NFS on the Server

We will now look in detail at how to use NFS on the server.

On the server machine, NFS uses **daemons** (built-in networking and service processes in Linux) and other system servers are started at the command line by typing:

**$ sudo systemctl start nfs**

_**NOTE**_: On RHEL/CentOS 8**,** the service is called **nfs-server**, not **nfs**.

The text file **/etc/exports** contains the directories and permissions that a host is willing to share with other systems over NFS. A very simple entry in this file may look like the following:

**/projects *.example.com(rw)**

This entry allows the directory **/projects** to be mounted using NFS with read and write (**rw**) permissions and shared with other hosts in the **example.com** domain. As we will detail in the next chapter, every file in Linux has three possible permissions: read (**r**), write (**w**) and execute (**x**).

After modifying the **/etc/exports** file, you can type **exportfs -av** to notify Linux about the directories you are allowing to be remotely mounted using NFS. You can also restart NFS with **sudo systemctl restart nfs**, but this is heavier, as it halts NFS for a short while before starting it up again. To make sure the NFS service starts whenever the system is booted, issue **sudo systemctl enable nfs**.

![NFS on the Server](https://courses.edx.org/assets/courseware/v1/c9d06cf0b5114c7ff0553aae608e96bd/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/exportsnfs.png)
_NFS on the Server_

### NFS on the Client

On the client machine, if it is desired to have the remote filesystem mounted automatically upon system boot, **/etc/fstab** is modified to accomplish this. For example, an entry in the client's **/etc/fstab** might look like the following:

**servername:/projects /mnt/nfs/projects nfs defaults 0 0**

You can also mount the remote filesystem without a reboot or as a one-time mount by directly using the **mount** command:

**$ sudo mount servername:/projects /mnt/nfs/projects**

Remember, if **/etc/fstab** is not modified, this remote mount will not be present the next time the system is restarted. Furthermore, you may want to use the **nofail** option in **fstab** in case the NFS server is not live at boot.

![NFS on the Client](https://courses.edx.org/assets/courseware/v1/80a14e19e05a9cfdc8b19f09d20e8e07/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/nfsclientubuntu.png)
_NFS on the Client_

### Overview of User Home Directories

In this section, you will learn to identify and differentiate between the most important directories found in Linux. We start with ordinary users' home directory space.

Each user has a home directory, usually placed under **/home**. The **/root** ("slash-root") directory on modern Linux systems is no more than the home directory of the root user (or superuser, or system administrator account).

On multi-user systems, the **/home** directory infrastructure is often mounted as a separate filesystem on its own partition, or even exported (shared) remotely on a network through NFS.

Sometimes, you may group users based on their department or function. You can then create subdirectories under the **/home** directory for each of these groups. For example, a school may organize **/home** with something like the following:

**/home/faculty/**  
**/home/staff/**  
**/home/students/**

![home directories](https://courses.edx.org/assets/courseware/v1/9817790ba352d4047027eb1d61516db5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Home_directories.png)
_Home Directories_

### The /bin and /sbin Directories

The **/bin** directory contains executable binaries, essential commands used to boot the system or in single-user mode, and essential commands required by all system users, such as **cat**, **cp**, **ls**, **mv**, **ps**, and **rm**.

![/bin directory](https://courses.edx.org/assets/courseware/v1/0f4cc85473fc7a961b3bc98b87d33a24/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsbin.png)
_/bin Directory_

Likewise, the **/sbin** directory is intended for essential binaries related to system administration, such as **fsck** and **ip**. To view a list of these programs, type:

**$ ls /bin /sbin**

![/sbin Directory](https://courses.edx.org/assets/courseware/v1/f60523278764a748d479ef923f75b0d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lssbin.png)
_/sbin Directory_

Commands that are not essential (theoretically) for the system to boot or operate in single-user mode are placed in the **/usr/bin** and **/usr/sbin** directories. Historically, this was done so **/usr** could be mounted as a separate filesystem that could be mounted at a later stage of system startup or even over a network. However, nowadays most find this distinction is obsolete. In fact, many distributions have been discovered to be unable to boot with this separation, as this modality had not been used or tested for a long time.

Thus, on some of the newest Linux distributions **/usr/bin** and **/bin** are actually just symbolically linked together, as are **/usr/sbin** and **/sbin**.

### The /proc Filesystem

Certain filesystems, like the one mounted at **/proc**, are called **pseudo-filesystems** because they have no permanent presence anywhere on the disk.

The **/proc** filesystem contains virtual files (files that exist only in memory) that permit viewing constantly changing kernel data. **/proc** contains files and directories that mimic kernel structures and configuration information. It does not contain real files, but runtime system information, e.g. system memory, devices mounted, hardware configuration, etc. Some important entries in **/proc** are:

**/proc/cpuinfo**  
**/proc/interrupts**  
**/proc/meminfo**  
**/proc/mounts**  
**/proc/partitions**  
**/proc/version**

**/proc** has subdirectories as well, including:

**/proc/<Process-ID-#>**  
**/proc/sys**

The first example shows there is a directory for every process running on the system, which contains vital information about it. The second example shows a virtual directory that contains a lot of information about the entire system, in particular its hardware and configuration. The **/proc** filesystem is very useful because the information it reports is gathered only as needed and never needs storage on the disk.

![The proc Filesystem](https://courses.edx.org/assets/courseware/v1/5851a953799d1db46c17d156b1cd23bc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsproc.png)
_The /proc Filesystem_

### The /dev Directory

The **/dev** directory contains **device nodes**, a type of pseudo-file used by most hardware and software devices, except for network devices. This directory is:

* Empty on the disk partition when it is not mounted
* Contains entries which are created by the **udev** system, which creates and manages device nodes on Linux, creating them dynamically when devices are found. The **/dev** directory contains items such as:

1. **/dev/sda1** (first partition on the first hard disk)
2. **/dev/lp1** (second printer)
3. **/dev/random** (a source of random numbers).

![The /dev Directory](https://courses.edx.org/assets/courseware/v1/ee00318b4e056829ec5580f3f8c6ca10/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsdev.png)
_The /dev Directory_

### The /var Directory

The **/var** directory contains files that are expected to change in size and content as the system is running (var stands for variable), such as the entries in the following directories:

* System log files: **/var/log**
* Packages and database files: **/var/lib**
* Print queues: **/var/spool**
* Temporary files: **/var/tmp**.

![The /var Directory](https://courses.edx.org/assets/courseware/v1/2d840d9232739d72bb6a2af07308a46d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsvar.png)
_The /var Directory_

The **/var** directory may be put on its own filesystem so that growth of the files can be accommodated and any exploding file sizes do not fatally affect the system. Network services directories such as **/var/ftp** (the FTP service) and **/var/www** (the HTTP web service) are also found under **/var**.

![The /var Directory](https://courses.edx.org/assets/courseware/v1/948dafcdc47f674bd2c0b5c1560ebb7c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varfolders.png)
_The /var Directory_

### The /etc Directory

The **/etc** directory is the home for system configuration files. It contains no binary programs, although there are some executable scripts. For example, **/etc/resolv.conf** tells the system where to go on the network to obtain host name to IP address mappings (DNS). Files like **passwd**, **shadow** and **group** for managing user accounts are found in the **/etc** directory. While some distributions have historically had their own extensive infrastructure under **/etc** (for example, Red Hat and SUSE have used **/etc/sysconfig**), with the advent of **systemd** there is much more uniformity among distributions today.

Note that **/etc** is for system-wide configuration files and only the superuser can modify files there. User-specific configuration files are always found under their home directory.

![The /etc Directory](https://courses.edx.org/assets/courseware/v1/4e485f3695bdc1468b81a286f3538f57/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/debianetc.png)
_The /etc Directory_

### The /boot Directory

The **/boot** directory contains the few essential files needed to boot the system. For every alternative kernel installed on the system there are four files:

1. **vmlinuz**  
The compressed Linux kernel, required for booting.
2. **initramfs**  
The initial ram filesystem, required for booting, sometimes called initrd, not initramfs.
3. **config**  
The kernel configuration file, only used for debugging and bookkeeping.
4. **System.map**  
Kernel symbol table, only used for debugging.

Each of these files has a kernel version appended to its name.

The Grand Unified Bootloader (GRUB) files such as **/boot/grub/grub.conf** or **/boot/grub2/grub2.cfg** are also found under the **/boot** directory.

![The /boot Directory](https://courses.edx.org/assets/courseware/v1/cc0ea7111ab46e927a9a6f2b5bfeddab/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bootdir.png)
_The /boot Directory_

The screenshot shows an example listing of the **/boot** directory, taken from a RHEL system that has multiple installed kernels, including both distribution-supplied and custom-compiled ones. Names will vary and things will tend to look somewhat different on a different distribution.

### The /lib and /lib64 Directories

**/lib** contains libraries (common code shared by applications and needed for them to run) for the essential programs in **/bin** and **/sbin**. These library filenames either start with **ld** or **lib**. For example, **/lib/libncurses.so.5.9**.

Most of these are what is known as dynamically loaded libraries (also known as shared libraries or Shared Objects (SO)). On some Linux distributions there exists a **/lib64** directory containing 64-bit libraries, while **/lib** contains 32-bit versions.

On recent Linux distributions, one finds:

![The /lib and /lib64 Directories](https://courses.edx.org/assets/courseware/v1/a8ab641d68e711bfc4892c0e33b5033b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lslib.png)
_The /lib and /lib64 Directories_

i.e., just like for **/bin** and **/sbin**, the directories just point to those under **/usr**.

Kernel modules (kernel code, often device drivers, that can be loaded and unloaded without re-starting the system) are located in **/lib/modules/<kernel-version-number>**.

![/lib/modules contents](https://courses.edx.org/assets/courseware/v1/43a3b062df788fc58b09fca237179261/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/libmodules.png)
_/lib/modules Contents_

### Removable media: the /media, /run and /mnt Directories

One often uses removable media, such as USB drives, CDs and DVDs. To make the material accessible through the regular filesystem, it has to be mounted at a convenient location. Most Linux systems are configured so any removable media are automatically mounted when the system notices something has been plugged in.

While historically this was done under the **/media** directory, modern Linux distributions place these mount points under the **/run** directory. For example, a USB pen drive with a label **myusbdrive** for a user named **student** would be mounted at **/run/media/student/myusbdrive**.

![Picture showing CDs, floppy disks, cassettes, USBs and memory cards](https://courses.edx.org/assets/courseware/v1/02712e7fe9b99bf10e71a429cf756904/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Forty_years_of_Removable_Storage.jpg)

The **/mnt** directory has been used since the early days of UNIX for temporarily mounting filesystems. These can be those on removable media, but more often might be network filesystems, which are not normally mounted. Or these can be temporary partitions, or so-called **loopback** filesystems, which are files which pretend to be partitions.

![The /run Directory](https://courses.edx.org/assets/courseware/v1/42f91969ba3ca6077991a47dc1348f00/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsrun.png)
_The /run Directory_

### Additional Directories Under /

There are some additional directories to be found under the root directory:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 826.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Directory Name<br style="line-height: 1.4em;"></strong></span></td><td align="center" bgcolor="#003f60" width="80%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/opt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Optional application software packages</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/sys</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Virtual pseudo-filesystem giving information about the system and the hardware<br style="line-height: 1.4em;">Can be used to alter system parameters and for debugging purposes</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/srv</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Site-specific data served up by the system<br style="line-height: 1.4em;">Seldom used</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/tmp</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Temporary files; on some distributions erased across a reboot and/or may actually be a ramdisk in memory</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Multi-user applications, utilities and data</span></td></tr></tbody></table>

### The /usr Directory Tree

The **/usr** directory tree contains theoretically non-essential programs and scripts (in the sense that they should not be needed to initially boot the system) and has at least the following sub-directories:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 826.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Directory Name<br style="line-height: 1.4em;"></strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/include</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Header files used to compile applications</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/lib</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Libraries for programs in<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/bin</span></strong></span><span>&nbsp;</span>and<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/sbin</span></strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/lib64</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">64-bit libraries for 64-bit programs in<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/bin</span></strong></span><span>&nbsp;</span>and<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/usr/sbin</span></strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/sbin</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Non-essential system binaries, such as system daemons</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/share</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Shared data used by applications, generally architecture-independent</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/src</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Source code, usually for the Linux kernel</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/local</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Data and programs specific to the local machine; subdirectories include&nbsp;<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">bin</strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">sbin</span></strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">lib</span></strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">share</span></strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">include</span></strong></span>, etc.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/bin</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">This is the primary directory of executable commands on the system</span></td></tr></tbody></table>

### Comparing Files with diff

Now that you know about the filesystem and its structure, let’s learn how to manage files and directories.

**diff** is used to compare files and directories. This often-used utility program has many useful options (see: **man diff**) including:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 826.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">diff Option</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-c</span></strong><br style="line-height: 1.4em;"></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Provides a listing of differences that include&nbsp;three&nbsp;lines of context before and after the lines differing in content</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-r</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Used to recursively&nbsp;compare subdirectories, as well as the current directory</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ignore the case of letters</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ignore differences in spaces and tabs (white space)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-q</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Be quiet: only report if files are different without listing the differences</span></td></tr></tbody></table>

To compare two files, at the command prompt, type **diff [options] <filename1> <filename2>**. **diff** is meant to be used for text files; for binary files, one can use **cmp**.

In this section, you will learn additional methods for comparing files and how to apply patches to files.

### Using diff3 and patch

You can compare three files at once using **diff3**, which uses one file as the reference basis for the other two. For example, suppose you and a co-worker both have made modifications to the same file working at the same time independently. **diff3** can show the differences based on the common file you both started with. The syntax for **diff3** is as follows:

**$ diff3 MY-FILE COMMON-FILE YOUR-FILE**

The graphic shows the use of **diff3**.

![Using diff3](https://courses.edx.org/assets/courseware/v1/33d173c484df38d28dcb85d2a49a010e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/diff3centos.png)
_Using diff3_

Many modifications to source code and configuration files are distributed utilizing patches, which are applied, not surprisingly, with the **patch** program. A patch file contains the deltas (changes) required to update an older version of a file to the new one. The patch files are actually produced by running **diff** with the correct options, as in:

**$ diff -Nur originalfile newfile > patchfile**

Distributing just the patch is more concise and efficient than distributing the entire file. For example, if only one line needs to change in a file that contains 1000 lines, the patch file will be just a few lines long.

![Using patch](https://courses.edx.org/assets/courseware/v1/6bb8e04e57d74c83cd0de7335128892d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/patchrhel.png)
_Using patch_

To apply a patch, you can just do either of the two methods below:

**$ patch -p1 < patchfile**  
**$ patch originalfile patchfile**

The first usage is more common, as it is often used to apply changes to an entire directory tree, rather than just one file, as in the second example. To understand the use of the **-p1** option and many others, see the man page for **patch**.

### Using the file Utility

In Linux, a file's extension often does not categorize it the way it might in other operating systems. One cannot assume that a file named **file.txt** is a text file and not an executable program. In Linux, a filename is generally more meaningful to the user of the system than the system itself. In fact, most applications directly examine a file's contents to see what kind of object it is rather than relying on an extension. This is very different from the way Windows handles filenames, where a filename ending with **.exe**, for example, represents an executable binary file.

The real nature of a file can be ascertained by using the **file** utility. For the file names given as arguments, it examines the contents and certain characteristics to determine whether the files are plain text, shared libraries, executable programs, scripts, or something else.

![Using file Utility](https://courses.edx.org/assets/courseware/v1/6bc751d9dafe1a200e66f2eb4479db0e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/fileu1910.png)
_Using the file Utility_

## Backing Up Data

There are many ways you can back up data or even your entire system. Basic ways to do so include the use of simple copying with **cp** and use of the more robust **rsync**.

Both can be used to synchronize entire directory trees. However, **rsync** is more efficient, because it checks if the file being copied already exists. If the file exists and there is no change in size or modification time, **rsync** will avoid an unnecessary copy and save time. Furthermore, because **rsync** copies only the parts of files that have actually changed, it can be very fast.

![Computers connected to a cloud using lines with arrows on both ends. Inside the cloud it says Backup](https://courses.edx.org/assets/courseware/v1/415a756cb43f614a31ef953a88377396/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen34.jpg)

**cp** can only copy files to and from destinations on the local machine (unless you are copying to or from a filesystem mounted using NFS), but **rsync** can also be used to copy files from one machine to another. Locations are designated in the **target:path** form, where **target** can be in the form of **someone@host**. The **someone@** part is optional and used if the remote user is different from the local user.

**rsync** is very efficient when recursively copying one directory tree to another, because only the differences are transmitted over the network. One often synchronizes the destination directory tree with the origin, using the -r option to recursively walk down the directory tree copying all files and directories below the one listed as the source.

### Using rsync

**rsync** is a very powerful utility. For example, a very useful way to back up a project directory might be to use the following command:

**$ rsync -r project-X archive-machine:archives/project-X**

Note that **rsync** can be very destructive! Accidental misuse can do a lot of harm to data and programs, by inadvertently copying changes to where they are not wanted. Take care to specify the correct options and paths. It is highly recommended that you first test your **rsync** command using the **-dry-run** option to ensure that it provides the results that you want.

![Keyboard key saying Backup](https://courses.edx.org/assets/courseware/v1/b466cf17ce5d978de488e7f13989c686/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen35.jpg)

To use **rsync** at the command prompt, type **rsync sourcefile destinationfile**, where either file can be on the local machine or on a networked machine; The contents of **sourcefile** will be copied to **destinationfile**.

A good combination of options is shown in:

**$ rsync --progress -avrxH  --delete sourcedir destdir**

File data is often compressed to save disk space and reduce the time it takes to transmit files over networks.

Linux uses a number of methods to perform this compression, including:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">The most frequently used Linux compression utility</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bzip2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Produces files significantly smaller than those produced by<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">gzip</strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">The most space-efficient compression utility used in Linux</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">zip</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Is often required to examine and decompress archives from other operating systems</td></tr></tbody></table>

These techniques vary in the efficiency of the compression (how much space is saved) and in how long they take to compress; generally, the more efficient techniques take longer. Decompression time does not vary as much across different methods.

In addition, the **tar** utility is often used to group files in an archive and then compress the whole archive at once.

### Compressing Data Using gzip

**gzip** is the most often used Linux compression utility. It compresses very well and is very fast. The following table provides some usage examples:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip *</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Compresses all files in the current directory; each file is compressed and renamed with a<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">.gz</span></strong></span><span>&nbsp;</span>extension</span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">gzip -r projectX</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresses all files in the&nbsp;<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">projectX</span></strong></span><span>&nbsp;</span>directory, along with all files in all of the directories under<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">projectX</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gunzip foo</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">De-compresses<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">foo</span></strong></span><span>&nbsp;</span>found in the file<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">foo.gz</span></strong></span>. Under the hood, the&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gunzip</span></strong><span>&nbsp;</span>command is actually the same as<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip –d</span></strong></span>.</td></tr></tbody></table>

### Compressing Data Using xz

**xz** is the most space efficient compression utility used in Linux and is used to [store archives of the Linux kernel](https://www.kernel.org/). Once again, it trades a slower compression speed for an even higher compression ratio.

Some usage examples:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="55%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz *</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresses all of the files in the current directory and replaces each file with one with a<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">.xz</strong></span><span>&nbsp;</span>extension.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz foo</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresses&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">foo</span></strong><span>&nbsp;</span>into<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">foo.xz</strong></span><span>&nbsp;</span>using the default compression level (-6), and removes<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">foo</span></strong></span><span>&nbsp;</span>if compression succeeds.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz -dk bar.xz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Decompresses<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bar.xz</span></strong></span><span>&nbsp;</span>into&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bar</span></strong>&nbsp;and does not remove<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bar.xz</span></strong></span><span>&nbsp;</span>even if decompression is successful.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz -dcf a.txt b.txt.xz &gt; abcd.txt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Decompresses a mix of compressed and uncompressed files to standard output, using a single command.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">xz -d *.xz</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Decompresses the files compressed using<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz</span></strong>.</td></tr></tbody></table>

Compressed files are stored with a **.xz** extension.

### Handling Files Using zip

The **zip** program is not often used to compress files in Linux, but is often required to examine and decompress archives from other operating systems. It is only used in Linux when you get a zipped file from a Windows user. It is a legacy program.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="25%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">zip backup *</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresses all files in the current directory and places them in the<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">backup.zip</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">zip -r backup.zip ~</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Archives your login directory (<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">~</span></strong></span>) and all files and directories under it in<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">backup.zip</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">unzip backup.zip</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Extracts all files in&nbsp;<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">backup.zip</span></strong><span>&nbsp;</span></span>and places them in the current directory.</td></tr></tbody></table>

### Archiving and Compressing Data Using tar

Historically, **tar** stood for "**t**ape **ar**chive" and was used to archive files to a magnetic tape. It allows you to create or extract files from an archive file, often called a **tarball**. At the same time, you can optionally compress while creating the archive, and decompress while extracting its contents.

Here are some examples of the use of **tar**:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tar xvf mydir.tar</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Extract all the files in<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir.tar</span></strong><span>&nbsp;</span>into the<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir</span></strong></span><span>&nbsp;</span>directory.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">tar zcvf mydir.tar.gz mydir</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Create the archive and compress with<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">tar jcvf mydir.tar.bz2 mydir</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Create the archive and compress with<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bz2</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tar Jcvf mydir.tar.xz mydir</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Create the archive and compress with<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tar xvf mydir.tar.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Extract all the files in<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir.tar.gz</span></strong></span><span>&nbsp;</span>into the<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir</span></strong></span><span>&nbsp;</span>directory.<br style="line-height: 1.4em;"><em style="line-height: 1.4em; font-style: italic;"><strong style="font-weight: bold; line-height: 1.4em;">NOTE</strong>: You do<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">not</strong><span>&nbsp;</span>have to tell<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">tar</strong><span>&nbsp;</span>it is in<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: italic; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip</span></strong><span>&nbsp;</span>format.</em></td></tr></tbody></table>

You can separate out the archiving and compression stages, as in:

**$ tar cvf mydir.tar mydir ; gzip mydir.tar**  
**$ gunzip mydir.tar.gz ; tar xvf mydir.tar**

but this is slower and wastes space by creating an unneeded intermediary **.tar** file.

### Relative Compression Times and Sizes

To demonstrate the relative efficiency of **gzip**, **bzip2**, and **xz**, the following screenshot shows the results of compressing a purely text file directory tree (the **include** directory from the kernel source) using the three methods.

![Relative Compression Times and Sizes](https://courses.edx.org/assets/courseware/v1/72c55fb093021786337d84cd0a081993/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tartimes.png)
_Relative Compression Times and Sizes_

This shows that as compression factors go up, CPU time does as well (i.e. producing smaller archives takes longer).

### Disk-to-Disk Copying (dd)

The **dd** program is very useful for making copies of raw disk space. For example, to back up your Master Boot Record (MBR) (the first 512-byte sector on the disk that contains a table describing the partitions on that disk), you might type:

**dd if=/dev/sda of=sda.mbr bs=512 count=1**

**WARNING!**

Typing:

**dd if=/dev/sda of=/dev/sdb**

to make a copy of one disk onto another, will delete everything that previously existed on the second disk.

An exact copy of the first disk device is created on the second disk device.

**Do not experiment with this command as written above, as it can erase a hard disk!**

Exactly what the name **dd** stands for is an often-argued item. The words data definition is the most popular theory and has roots in early IBM history. Often, people joke that it means disk destroyer and other variants such as delete data!

![Disk-to-Disk Copying (dd)](https://courses.edx.org/assets/courseware/v1/6ed7efb57f544c1bbac9baf55f75e535/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen_41.jpg)
_Disk-to-Disk Copying (dd)_

### Chapter Summary

You have completed Chapter 10. Let’s summarize the key concepts covered:

* The filesystem tree starts at what is often called the root directory (or trunk, or **/**).
* The  Filesystem Hierarchy Standard (FHS) provides Linux developers and system administrators a standard directory structure for the filesystem.
* Partitions help to segregate files according to usage, ownership, and type.
* Filesystems can be mounted anywhere on the main filesystem tree at a mount point. Automatic filesystem mounting can be set up by editing **/etc/fstab**.
* NFS (Network File System) is a useful method for sharing files and data through the network systems.
* Filesystems like **/proc** are called pseudo filesystems because they exist only in memory.
* **/root** (slash-root) is the home directory for the root user.
* **/var** may be put in its own filesystem so that growth can be contained and not fatally affect the system.
* **/boot** contains the basic files needed to boot the system.
* **patch** is a very useful tool in Linux. Many modifications to source code and configuration files are distributed with patch files, as they contain the deltas or changes to go from an old version of a file to the new version of a file.
* File extensions in Linux do not necessarily mean that a file is of a certain type.
* **cp** is used to copy files on the local machine, while **rsync** can also be used to copy files from one machine to another, as well as synchronize contents.
* **gzip**, **bzip2**, **xz** and **zip** are used to compress files.
* **tar** allows you to create or extract files from an archive file, often called a tarball. You can optionally compress while creating the archive, and decompress while extracting its contents.
* **dd** can be used to make large exact copies, even of entire disk partitions, efficiently.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)



## Chapter 11: Text Editors

### Learning Objectives

By the end of this chapter, you should be familiar with:

* How to create and edit files using the available Linux text editors.
* nano, a simple text-based editor.
* gedit, a simple graphical editor.
* vi and emacs, two advanced editors with both text-based and graphical interfaces.

### Overview of Text Editors in Linux

At some point, you will need to manually edit text files. You might be composing an email off-line, writing a script to be used for **bash** or other command interpreters, altering a system or application configuration file, or developing source code for a programming language such as C, Python or Java.

Linux administrators may sidestep using a text editor, instead employing graphical utilities for creating and modifying system configuration files. However, this can be more laborious than directly using a text editor, and be more limited in capability. Note that word processing applications (including those that are part of common office application suites) are not really basic text editors; they add a lot of extra (usually invisible) formatting information that will probably render system administration configuration files unusable for their intended purpose. So, knowing how to confidently use one or more text editors is really an essential skill to have for Linux.

By now, you have certainly realized Linux is packed with choices; when it comes to text editors, there are many choices, ranging from quite simple to very complex, including:

* nano
* gedit
* vi
* emacs

In this section, we learn first about the nano and gedit editors, which are relatively simple and easy to learn, and then later the more complicated choices, vi and emacs. Before we start, let us take a look at some cases where an editor is not needed.

![Text Editors in Linux](https://courses.edx.org/assets/courseware/v1/57bd3f905d0a25d34771843b351ff71a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch10_screen03.jpg)
_Text Editors in Linux_

### Creating Files Without Using an Editor

Sometimes, you may want to create a short file and don't want to bother invoking a full text editor. In addition, doing so can be quite useful when used from within scripts, even when creating longer files. You will no doubt find yourself using this method when you start on the later chapters that cover shell scripting!

If you want to create a file without using an editor, there are two standard ways to create one from the command line and fill it with content.

The first is to use **echo** repeatedly:  
  
**$ echo line one > myfile**  
**$ echo line two >> myfile**  
**$ echo line three >> myfile**

Note that while a single greater-than sign (**>**) will send the output of a command to a file, two of them (**>>**) will append the new output to an existing file.

The second way is to use **cat** combined with redirection:

**$ cat << EOF > myfile**  
**> line one**  
**> line two**  
**> line three**  
**> EOF**  
**$**

Both techniques produce a file with the following lines in it:  
  
**line one**  
**line two**  
**line three**

and are extremely useful when employed by scripts.

![Creating Files Without Using an Editor](https://courses.edx.org/assets/courseware/v1/b04d6912d3a68cd8702829b69b260051/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/echocatubuntu.png)
_Creating Files Without Using an Editor_

### nano and gedit

There are some text editors that are pretty obvious; they require no particular experience to learn and are actually quite capable, even robust. A particularly easy to use one is the text terminal-based editor nano. Just invoke nano by giving a file name as an argument. All the help you need is displayed at the bottom of the screen, and you should be able to proceed without any problem.

![Computer](https://courses.edx.org/assets/courseware/v1/b3c8f733d43ceaff56f586b7c8f8708b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch10_screen04.jpg)

As a graphical editor, gedit is part of the GNOME desktop system (kwrite is associated with KDE). The gedit and kwrite editors are very easy to use and are extremely capable. They are also very configurable. They look a lot like Notepad in Windows. Other variants such as kate are also supported by KDE.

### nano

nano is easy to use, and requires very little effort to learn. To open a file, type **nano <filename>** and press **Enter**. If the file does not exist, it will be created.

nano provides a two line shortcut bar at the bottom of the screen that lists the available commands. Some of these commands are:

* **CTRL-G**  
Display the help screen.
* **CTRL-O**  
Write to a file.
* **CTRL-X**  
Exit a file.
* **CTRL-R**  
Insert contents from another file to the current buffer.
* **CTRL-C**  
Show cursor position.

![nano](https://courses.edx.org/assets/courseware/v1/c0d7acca187acbb8d82288dee538658d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/nano.png)
_nano_

### gedit

gedit (pronounced 'g-edit') is a simple-to-use graphical editor that can only be run within a Graphical Desktop environment. It is visually quite similar to the Notepad text editor in Windows, but is actually far more capable and very configurable and has a wealth of plugins available to extend its capabilities further.

To open a new file find the program in your desktop's menu system, or from the command line type **gedit <filename>**. If the file does not exist, it will be created.

Using gedit is pretty straightforward and does not require much training. Its interface is composed of quite familiar elements.

![gedit](https://courses.edx.org/assets/courseware/v1/739df8236f04571d52f8e387f0dfd50b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gedit.png)

### vi and emacs

Developers and administrators experienced in working on UNIX-like systems almost always use one of the two venerable editing options: vi and emacs. Both are present or easily available on all distributions and are completely compatible with the versions available on other operating systems.

Both vi and emacs have a basic purely text-based form that can run in a non-graphical environment. They also have one or more graphical interface forms with extended capabilities; these may be friendlier for a less experienced user. While vi and emacs can have significantly steep learning curves for new users, they are extremely efficient when one has learned how to use them.

You need to be aware that fights among seasoned users over which editor is better can be quite intense and are often described as a holy war.

![Linux Text editors: basic editors are nano and gedit and advanced editors are vi and emacs](https://courses.edx.org/assets/courseware/v1/c1242e5076d40142646d5f7d0cbb6e31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch10_screen08.jpg)
_Linux Text Editors_

### Introduction to vi

Usually, the actual program installed on your system is vim, which stands for Vi IMproved, and is aliased to the name vi. The name is pronounced as “vee-eye”.

Even if you do not want to use vi, it is good to gain some familiarity with it: it is a standard tool installed on virtually all Linux distributions. Indeed, there may be times where there is no other editor available on the system.

GNOME extends vi with a very graphical interface known as gvim and KDE offers kvim. Either of these may be easier to use at first.

When using vi, all commands are entered through the keyboard. You do not need to keep moving your hands to use a pointer device such as a mouse or touchpad, unless you want to do so when using one of the graphical versions of the editor.

![Introduction to vi](https://courses.edx.org/assets/courseware/v1/4421947fff5812630286c32046082020/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/vimubuntu.png)

### vimtutor

Typing **vimtutor** launches a short but very comprehensive tutorial for those who want to learn their first vi commands. Even though it provides only an introduction and just seven lessons, it has enough material to make you a very proficient vi user, because it covers a large number of commands. After learning these basic ones, you can look up new tricks to incorporate into your list of vi commands because there are always more optimal ways to do things in vi with less typing.

![vim tutor](https://courses.edx.org/assets/courseware/v1/b1e67aea3546804f69588aab52e97fcb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/vimtutorubuntu.png)

### Modes in vi

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Mode</strong></span></td><td align="center" bgcolor="#003f60" width="80%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Feature</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px 0px 0px 1em; margin: 1em 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc;"><li style="line-height: 1.4em; margin-bottom: 0.70788em;">By default,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">vi</strong>&nbsp;starts in<strong style="font-weight: bold; line-height: 1.4em;">&nbsp;</strong>Command mode.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Each key is an editor command.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Keyboard strokes are interpreted as commands that can modify file contents.</li></ul></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Insert</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px 0px 0px 1em; margin: 1em 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc;"><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Type<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">i</span></strong></span><span>&nbsp;</span>to switch to&nbsp;Insert mode from&nbsp;Command mode.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Insert mode is used to enter (insert) text into a file.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Insert mode is indicated by an “<code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">? INSERT ?</strong></code>” indicator at the bottom of the screen.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Press<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Esc</span></code></span></strong></span><span>&nbsp;</span>to exit Insert mode and return to Command mode.</li></ul></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Line</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px 0px 0px 1em; margin: 1em 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc;"><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Type&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:</span></strong></span><span>&nbsp;</span>to switch to the Line mode from Command mode.&nbsp;Each key is an external command, including operations such as writing the file contents to disk or exiting.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Uses line editing commands inherited from older line editors. Most of these commands are actually no longer used. Some line editing commands are very powerful.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Press<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Esc</span></strong></span><span>&nbsp;</span>to exit Line mode and return to Command mode.</li></ul></td></tr></tbody></table>

vi provides three modes, as described in the table below. It is vital to not lose track of which mode you are in. Many keystrokes and commands behave quite differently in different modes.

### Working with Files in vi

The table describes the most important commands used to start, exit, read, and write files in vi. The **ENTER** key needs to be pressed after all of these commands.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">vi myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Start the editor and edit<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">vi -r myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Start and edit<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong><span>&nbsp;</span>in recovery mode from a system crash</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:r file2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Read in<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file2</span></strong><span>&nbsp;</span>and insert at current position</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Write to the file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:w myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Write out to<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:w! file2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Overwrite<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file2</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:x or :wq</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Exit and write out modified file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:q</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Quit<strong style="font-weight: bold; line-height: 1.4em;"></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:q!</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Quit even though modifications have not been saved</span></td></tr></tbody></table>

### Changing Cursor Positions in vi

The table describes the most important keystrokes used when changing cursor position in vi. Line mode commands (those following colon **:** ) require the **ENTER** key to be pressed after the command is typed.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="25%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td width="35%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">arrow keys</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move up, down, left and right</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">j</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&lt;ret&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move one line down</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">k</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move one line up</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">h</span></strong><span>&nbsp;</span>or Backspace</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move one character left</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">l</span></strong><span>&nbsp;</span>or Space</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move one character right</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">0</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move to beginning of line</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move to end of line</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move to beginning of next word</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:0</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1G</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move to beginning of file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:n</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">nG</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move to line n</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:$</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">G</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move to last line in file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-F</span></strong></span><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Down</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move forward one page</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-B</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Up</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To move backward one page</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">^l</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">To refresh and center screen</span></td></tr></tbody></table>

### Video: Using Modes and Cursor Movements in vi

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V001700_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Searching for Text in vi

The table describes the most important _commands_ used when searching for text in vi. The **ENTER** key should be pressed after typing the search pattern.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/pattern</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Search forward for pattern</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">?pattern</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Search backward for pattern</span></td></tr></tbody></table>

The table describes the most important _keystrokes_ used when searching for text in vi.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">n</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Move to next occurrence of search pattern</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">N</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Move to previous occurrence of search pattern</span></td></tr></tbody></table>

### Working with Text in vi

The table describes the most important keystrokes used when changing, adding, and deleting text in vi.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td width="65%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">a</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Append text after cursor; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">A</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Append text at end of current line; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Insert text before cursor; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">I</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Insert text at beginning of current line; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">o</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Start a new line below current line, insert text there; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">O</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Start a new line above current line, insert text there; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">r</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Replace character at current position</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">R</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Replace text starting with current position; stop upon<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Escape</span></strong><span>&nbsp;</span>key</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">x</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Delete character at current position</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Nx</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Delete N characters, starting at current position</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dw</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Delete the word at the current position</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">D</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Delete the rest of the current line</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Delete the current line</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Ndd</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dNd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Delete N lines</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">u</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Undo the previous operation</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">yy</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Yank (copy) the current line and put it in buffer</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Nyy</span></strong></span><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">yNy</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Yank (copy) N lines and put it in buffer</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">p</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Paste at the current position the yanked line or lines from the buffer</span></td></tr></tbody></table>

**[Here is a consolidated PDF with commands for vi.](https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block@Commands_for_vi.pdf)**

### Using External Commands in vi

Typing **sh** command opens an external command shell. When you exit the shell, you will resume your editing session.

Typing **!** executes a command from within vi. The command follows the exclamation point. This technique is best suited for non-interactive commands, such as **: ! wc %**. Typing this will run the **wc** (word count) command on the file; the character **%** represents the file currently being edited.

![vi command](https://courses.edx.org/assets/courseware/v1/1b96ee76e521a7f91666d8df989960d6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/vicommand.png)

### Video: Using External Commands, Saving, and Closing in the vi Editor

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V002700_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Introduction to emacs

The emacs editor is a popular competitor for vi. Unlike vi, it does not work with modes. emacs is highly customizable and includes a large number of features. It was initially designed for use on a console, but was soon adapted to work with a GUI as well. emacs has many other capabilities other than simple text editing. For example, it can be used for email, debugging, etc.

Rather than having different modes for command and insert, like vi, emacs uses the **CTRL** and Meta (**Alt** or **Esc**) keys for special commands.

![emacs](https://courses.edx.org/assets/courseware/v1/ce4dcc838b6cc24da8199d352dd4181c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/emacsc8.png)

### Working with emacs

The table lists some of the most important key combinations that are used when starting, exiting, reading, and writing files in emacs.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 802.398px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">emacs myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Start emacs and edit<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Insert prompted for file at current position</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x s</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Save all files</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x CTRL-w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Write to the file giving a new name when prompted</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x&nbsp;CTRL-s</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Saves the current file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x&nbsp;CTRL-c</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Exit after being prompted to save&nbsp;any modified files</td></tr></tbody></table>

The emacs tutorial is a good place to start learning basic commands. It is available any time when in emacs by simply typing **CTRL-h** (for help) and then the letter **t** for tutorial.

### Changing Cursor Positions in emacs

The table lists some of the keys and key combinations that are used for changing cursor positions in emacs.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="27%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td width="53%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">arrow keys</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Use the arrow keys for up, down, left and right</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-n</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">One line down</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-p</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">One line up</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-f</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">One character forward/right</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-b</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">One character back/left</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-a</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move to beginning of line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-e</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move to end of line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-f</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move to beginning of next word</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-b</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move back to beginning of preceding word</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-&lt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move to beginning of file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-g-g-n</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move to line n (can also use '<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Esc-x Goto-line n</span></strong>')</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-&gt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move to end of file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-v</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Down</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move forward one page</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-v</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Up</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Move backward one page</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-l</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Refresh and center screen</td></tr></tbody></table>

### Searching for Text in emacs

The table lists the key combinations that are used for searching for text in emacs.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-s</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Search forward for prompted pattern, or for next pattern</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-r</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Search backwards for prompted pattern, or for next pattern</td></tr></tbody></table>

### Working with Text in emacs

The table lists some of the key combinations used for changing, adding, and deleting text in emacs**:**

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-o</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Insert a blank line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-d</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Delete character at current position</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-k</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Delete the rest of the current line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-_</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Undo the previous operation</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-</span></strong><span>&nbsp;</span>(space or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-@</span></strong>)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Mark the beginning of the selected region. The end will be at the cursor position</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-w</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Delete the current marked text and write it to the buffer</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-y</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Insert at current cursor location whatever was most recently deleted</td></tr></tbody></table>

[**Here is a consolidated PDF file with commands for emacs.**](https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block@Commands_for_emacs.pdf)

### Video: emacs Operations

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001900_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Chapter Summary

You have completed Chapter 11. Let’s summarize the key concepts covered:

* Text editors (rather than word processing programs) are used quite often in Linux, for tasks such as creating or modifying system configuration files, writing scripts, developing source code, etc.
* nano is an easy-to-use text-based editor that utilizes on-screen prompts.
* gedit is a graphical editor, very similar to Notepad in Windows.
* The vi editor is available on all Linux systems and is very widely used. Graphical extension versions of vi are widely available as well.
* emacs is available on all Linux systems as a popular alternative to vi. emacs can support both a graphical user interface and a text mode interface.
* To access the vi tutorial, type **vimtutor** at a command line window.
* To access the emacs tutorial type **Ctl-h** and then **t** from within emacs**.**
* vi has three modes: _Command_, _Insert_, and _Line_. emacs has only one, but requires use of special keys, such as **Control** and **Escape**.
* Both editors use various combinations of keystrokes to accomplish tasks. The learning curve to master these can be long, but once mastered using either editor is extremely efficient.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 12: User Environment

### Learning Objectives

By the end of this chapter, you should be able to:

* Use and configure user accounts and user groups.
* Use and set environment variables.
* Use the previous shell command history.
* Use keyboard shortcuts.
* Use and define aliases.
* Use and set file permissions and ownership.

### Identifying the Current User

As you know, Linux is a multi-user operating system, meaning more than one user can log on at the same time.

* To identify the current user, type **whoami**.
* To list the currently logged-on users, type **who**.

Giving **who** the **-a** option will give more detailed information.

![Using who and whoami](https://courses.edx.org/assets/courseware/v1/b90c91f7776e3f55a5e63eb343e10b99/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/whoubuntu.png)
_Identifying the Current User_

### User Startup Files

In Linux, the command shell program (generally **bash**) uses one or more startup files to configure the user environment. Files in the **/etc** directory define global settings for all users, while initialization files in the user's home directory can include and/or override the global settings.

![User Startup Files](https://courses.edx.org/assets/courseware/v1/a61fd2656f3894d6f93397e755157b4b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch09_screen07.jpg)
_User Startup Files_

The startup files can do anything the user would like to do in every command shell, such as:

* Customizing the prompt
* Defining command line shortcuts and aliases
* Setting the default text editor
* Setting the path for where to find executable programs

### Order of the Startup Files

The standard prescription is that when you first login to Linux, **/etc/profile** is read and evaluated, after which the following files are searched (if they exist) in the listed order:

1. **~/.bash_profile**
2. **~/.bash_login**
3. **~/.profile**

where **~/.** denotes the user's home directory. The Linux login shell evaluates whatever startup file that it comes across first and ignores the rest. This means that if it finds **~/.bash_profile**, it ignores **~/.bash_login** and **~/.profile**. Different distributions may use different startup files.

However, every time you create a new shell, or terminal window, etc., you do not perform a full system login; only a file named **~/.bashrc** file is read and evaluated. Although this file is not read and evaluated along with the login shell, most distributions and/or users include the **~/.bashrc** file from within one of the three user-owned startup files.

Most commonly, users only fiddle with **~/.bashrc**, as it is invoked every time a new command line shell initiates, or another program is launched from a terminal window, while the other files are read and executed only when the user first logs onto the system.

Recent distributions sometimes do not even have **.bash_profile** and/or **.bash_login**, and some just do little more than include **.bashrc**.

![Order of the Startup Files](https://courses.edx.org/assets/courseware/v1/618e42fc4814cce9ff91eceac55438b9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bashinit.png)
_Order of the Startup Files_

### Creating Aliases

You can create customized commands or modify the behavior of already existing ones by creating **aliases**. Most often, these aliases are placed in your **~/.bashrc** file so they are available to any command shells you create. **unalias** removes an alias.

Typing **alias** with no arguments will list currently defined aliases.

Please note there should not be any spaces on either side of the equal sign and the alias definition needs to be placed within either single or double quotes if it contains any spaces.

![Creating Aliases](https://courses.edx.org/assets/courseware/v1/97491d062822787b87a74f33ea868847/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/aliassuse.png)
_Creating Aliases_

### Basics of Users and Groups

All Linux users are assigned a unique user ID (**uid**), which is just an integer; normal users start with a uid of 1000 or greater.

Linux uses **groups** for organizing users. Groups are collections of accounts with certain shared permissions. Control of group membership is administered through the **/etc/group** file, which shows a list of groups and their members. By default, every user belongs to a default or primary group. When a user logs in, the group membership is set for their primary group and all the members enjoy the same level of access and privilege. Permissions on various files and directories can be modified at the group level.

Users also have one or more group IDs (**gid**), including a default one which is the same as the user ID. These numbers are associated with names through the files **/etc/passwd** and **/etc/group**. Groups are used to establish a set of users who have common interests for the purposes of access rights, privileges, and security considerations. Access rights to files (and devices) are granted on the basis of the user and the group they belong to.

For example, **/etc/passwd** might contain **george:x:1002:1002:George Metesky:/home/george:/bin/bash** and **/etc/group** might contain **george:x:1002**.

![Basics of Users and Groups](https://courses.edx.org/assets/courseware/v1/03549a0189644137de64f426a69442c3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/etc_group_passwd.png)
_Basics of Users and Groups_

### Adding and Removing Users

Distributions have straightforward graphical interfaces for creating and removing users and groups and manipulating group membership. However, it is often useful to do it from the command line or from within shell scripts. Only the root user can add and remove users and groups.

Adding a new user is done with **useradd** and removing an existing user is done with **userdel**. In the simplest form, an account for the new user **bjmoose** would be done with:

**$ sudo useradd bjmoose**

which, by default, sets the home directory to **/home/bjmoose**, populates it with some basic files (copied from **/etc/skel**) and adds a line to **/etc/passwd** such as:

**bjmoose:x:1002:1002::/home/bjmoose:/bin/bash**

and sets the default shell to **/bin/bash**. Removing a user account is as easy as typing **userdel bjmoose**. However, this will leave the **/home/bjmoose** directory intact. This might be useful if it is a temporary inactivation. To remove the home directory while removing the account one needs to use the **-r** option to **userdel**.

Typing **id** with no argument gives information about the current user, as in:

**$ id**  
**uid=1002(bjmoose) gid=1002(bjmoose) groups=106(fuse),1002(bjmoose)**

If given the name of another user as an argument, **id** will report information about that other user.

![Adding and Removing Users](https://courses.edx.org/assets/courseware/v1/1387735f26c0ae0b377390c4c9dd9e7a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/useradd.png)

### Video: Using User Accounts

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000300_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Adding and Removing Groups

Adding a new group is done with **groupadd**:

**$ sudo /usr/sbin/groupadd anewgroup**

The group can be removed with:

**$ sudo /usr/sbin/groupdel anewgroup**

Adding a user to an already existing group is done with **usermod**. For example, you would first look at what groups the user already belongs to:

**$ groups rjsquirrel**  
**rjsquirrel : rjsquirrel**

and then add the new group:

**$ sudo /usr/sbin/usermod -a -G anewgroup rjsquirrel**

**$ groups rjsquirrel**  
**rjsquirrel: rjsquirrel anewgroup**

These utilities update **/etc/group** as necessary. Make sure to use the **-a** option, for append, so as to avoid removing already existing groups. **groupmod** can be used to change group properties, such as the Group ID (gid) with the **-g** option or its name with then **-n** option.

Removing a user from the group is somewhat trickier. The **-G** option to usermod must give a complete list of groups. Thus, if you do:

**$ sudo /usr/sbin/usermod -G rjsquirrel rjsquirrel**

**$ groups rjsquirrel**  
**rjsquirrel : rjsquirrel**

only the **rjsquirrel** group will be left.

![Adding and Removing Groups](https://courses.edx.org/assets/courseware/v1/388d78b23f2b6d93f8f39cbecf6194b1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/newgroupsuse.png)
_Adding and Removing Groups_

### The root Account

The root account is very powerful and has full access to the system. Other operating systems often call this the administrator account; in Linux, it is often called the superuser account. You must be extremely cautious before granting full root access to a user; it is rarely, if ever, justified. External attacks often consist of tricks used to elevate to the root account.

![Tux the Penguin and black square with hash sign and colon](https://courses.edx.org/assets/courseware/v1/5ec1a18add0a1780ef903912e0b5f6ba/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch09_screen04a.jpg)

However, you can use **sudo** to assign more limited privileges to user accounts:

* Only on a temporary basis
* Only for a specific subset of commands.

### su and sudo

When assigning elevated privileges, you can use the command **su** (switch or substitute user) to launch a new shell running as another user (you must type the password of the user you are becoming). Most often, this other user is root, and the new shell allows the use of elevated privileges until it is exited. It is almost always a bad (dangerous for both security and stability) practice to use **su** to become root. Resulting errors can include deletion of vital files from the system and security breaches.

Granting privileges using **sudo** is less dangerous and is preferred. By default, **sudo** must be enabled on a per-user basis. However, some distributions (such as Ubuntu) enable it by default for at least one main user, or give this as an installation option.

In the _Local Security Principles_ chapter we will describe and compare **su** and **sudo** in detail.

### Elevating to root Account

To temporarily become the superuser for a series of commands, you can type **su** and then be prompted for the root password.

To execute just one command with root privilege type **sudo <command>**. When the command is complete, you will return to being a normal unprivileged user.

**sudo** configuration files are stored in the **/etc/sudoers** file and in the **/etc/sudoers.d/** directory. By default, the **sudoers.d** directory is empty.

![Elevating to root Account](https://courses.edx.org/assets/courseware/v1/7dd106f332e911d309ccdedc9823d9c7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sudo.png)
_Elevating to root Account_

### Environment Variables

**Environment variables** are quantities that have specific values which may be utilized by the command shell, such as **bash**, or other utilities and applications. Some environment variables are given preset values by the system (which can usually be overridden), while others are set directly by the user, either at the command line or within startup and other scripts.

An environment variable is actually just a character string that contains information used by one or more applications. There are a number of ways to view the values of currently set environment variables; one can type **set**, **env**, or **export**. Depending on the state of your system, **set** may print out many more lines than the other two methods.

![Environment Variables](https://courses.edx.org/assets/courseware/v1/1604db32728f9bb80765461155886f79/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/envsetexport.png)
_Environment Variables_

### Setting Environment Variables

By default, variables created within a script are only available to the current shell; child processes (sub-shells) will not have access to values that have been set or modified. Allowing child processes to see the values requires use of the **export** command.

<table height="258" width="90%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Task</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Show the value of a specific variable</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo $SHELL</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Export a new variable value</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">export VARIABLE=value</strong></span>&nbsp;(or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">VARIABLE=value; export VARIABLE</span></strong>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Add a variable permanently</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Edit<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">~/.bashrc</strong></span>&nbsp;and add the line<span>&nbsp;</span><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">export VARIABLE=value</span></strong></span></p><p style="color: rgb(69, 69, 69); margin: 20px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Type&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">source ~/.bashrc</span></strong>&nbsp;or just&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">. ~/.bashrc</span></strong><span>&nbsp;</span>(<em style="line-height: 1.4em; font-style: italic;">dot</em><span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">~/.bashrc</span></strong>);&nbsp;or just start a new shell by typing<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bash</span></strong></p></td></tr></tbody></table>

You can also set environment variables to be fed as a one shot to a command as in:

**$ SDIRS=s_0* KROOT=/lib/modules/$(uname -r)/build make modules_install**

which feeds the values of the **SDIRS** and **KROOT** environment variables to the command **make modules_install**.

### The HOME Variable

**HOME** is an environment variable that represents the home (or login) directory of the user. **cd** without arguments will change the current working directory to the value of **HOME**. Note the tilde character (**~**) is often used as an abbreviation for **$HOME**. Thus, **cd $HOME** and **cd ~** are completely equivalent statements.

<table width="80%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="45%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Explanation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ echo $HOME</span><br style="line-height: 1.4em;"><span style="color: rgb(106, 191, 75); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/home/me</span><br style="line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ cd /bin</span></span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Show the value of the<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">HOME</span></strong><span>&nbsp;</span>environment variable, then change directory (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd</span></strong>) to<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/bin</span></strong></span></span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ pwd</span><br style="line-height: 1.4em;"><span style="color: rgb(106, 191, 75); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/bin</span></span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Where are we? Use print (or present) working directory (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pwd</span></strong>) to find out. As expected,<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/bin</span></strong></span></span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ cd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Change directory without an argument...</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ pwd</span><br style="line-height: 1.4em;"><span style="color: rgb(106, 191, 75); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/home/me</span></span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">...takes us back to<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">HOME</span></strong>,&nbsp;as you can now see.</td></tr></tbody></table>

The screenshot demonstrates this.

![The HOME Variable](https://courses.edx.org/assets/courseware/v1/946d3c6728f797c4ce929d2730915273/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homeubuntu.png)
_The HOME Variable_

### The PATH Variable

**PATH** is an ordered list of directories (the path) which is scanned when a command is given to find the appropriate program or script to run. Each directory in the path is separated by colons (**:**). A null (empty) directory name (or **./**) indicates the current directory at any given time.

* **:path1:path2**
* **path1::path2**

In the example **:path1:path2**, there is a null directory before the first colon (**:**). Similarly, for **path1::path2** there is a null directory between **path1** and **path2**.

To prefix a private **bin** directory to your path:

**$ export PATH=$HOME/bin:$PATH**  
**$ echo $PATH**  
**/home/student/bin:/usr/local/bin:/usr/bin:/bin/usr**

![The PATH Variable](https://courses.edx.org/assets/courseware/v1/b955fc762a2b63221bc0a46e1fb9b419/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/setpath.png)
_The PATH Variable_

### The SHELL Variable

The environment variable **SHELL** points to the user's default command shell (the program that is handling whatever you type in a command window, usually bash) and contains the full pathname to the shell:

**$ echo $SHELL**  
**/bin/bash**  
**$**

![Shell](https://courses.edx.org/assets/courseware/v1/411c5576bf37caded5284030bbd8cb0e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/seashell.png)

### The PS1 Variable and the Command Line Prompt

Prompt Statement (**PS**) is used to customize your prompt string in your terminal windows to display the information you want.

**PS1** is the primary prompt variable which controls what your command line prompt looks like. The following special characters can be included in **PS1**:

**\u** - User name  
**\h** - Host name  
**\w** - Current working directory  
**\!** - History number of this command  
**\d** - Date

They must be surrounded in single quotes when they are used, as in the following example:

**$ echo $PS1**  
**$**  
**$ export PS1='\u@\h:\w$ '**  
**student@example.com:~$ # new prompt**

To revert the changes:

**student@example.com:~$ export PS1='$ '**  
**$**

An even better practice would be to save the old prompt first and then restore, as in:

**$ OLD_PS1=$PS1**

change the prompt, and eventually change it back with:

**$ PS1=$OLD_PS1**  
**$**

![The PS1 Variable and the Command Line Prompt](https://courses.edx.org/assets/courseware/v1/0e41f5477fe686acda77ec04fe717d3d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ps1.png)

### Recalling Previous Commands

bash keeps track of previously entered commands and statements in a history buffer. You can recall previously used commands simply by using the **Up** and **Down** cursor keys. To view the list of previously executed commands, you can just type **history** at the command line.

The list of commands is displayed with the most recent command appearing last in the list. This information is stored in **~/.bash_history**. If you have multiple terminals open, the commands typed in each session are not saved until the session terminates.

![Recalling Previous Commands](https://courses.edx.org/assets/courseware/v1/0dc7d17f95a156ae24e9ee8a22d98b69/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/debianhistory.png)
_Recalling Previous Commands_

### Using History Environment Variables

Several associated environment variables can be used to get information about the `**history**` file.

* **HISTFILE**  
The location of the history file.
* **HISTFILESIZE**  
The maximum number of lines in the history file (default 500).
* **HISTSIZE**  
The maximum number of commands in the history file.
* **HISTCONTROL**  
How commands are stored.
* **HISTIGNORE**  
Which command lines can be unsaved.

For a complete description of the use of these environment variables, see **man bash**.

![Using History Environment Variables](https://courses.edx.org/assets/courseware/v1/529cf8bca6c3fff74ad538be6dbab7f2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/history.png)
_Using History Environment Variables_

### Finding and Using Previous Commands

Specific keys to perform various tasks:

<table border="0" width="100%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Key</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;">Up</strong></span>/<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;">Down</strong></span><span>&nbsp;</span>arrow keys</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Browse through the list of commands previously executed</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!!</span></strong></span><span>&nbsp;</span>(Pronounced as bang-bang)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Execute the previous command</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-R</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Search previously used commands</td></tr></tbody></table>

If you want to recall a command in the history list, but do not want to press the arrow key repeatedly, you can press **CTRL-R** to do a reverse intelligent search.

As you start typing, the search goes back in reverse order to the first command that matches the letters you have typed. By typing more successive letters, you make the match more and more specific.

The following is an example of how you can use the **CTRL-R** command to search through the command history:

**$ ^R**                                                                      (This all happens on 1 line)  
**(reverse-i-search)'s': sleep 1000**         (Searched for 's'; matched "sleep")  
**$ sleep 1000**                                                     (Pressed Enter to execute the searched command)  
**$**

### Executing Previous Commands

The table describes the syntax used to execute previously used commands:

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Syntax</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Task</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Start a history substitution</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!$</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Refer to the last argument in a line</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!n</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Refer to the n<sup style="font-size: 12px; line-height: 1.4em; position: relative; vertical-align: baseline; top: -0.5em;">th</sup><span>&nbsp;</span>command line</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!string</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Refer to the most recent command starting with string</td></tr></tbody></table>

All history substitutions start with **!**. When typing the command: **ls -l /bin /etc /var**, **!$** will refer to **/var**, the last argument to the command.

Here are more examples:

**$ history**

1. **echo $SHELL**
2. **echo $HOME**
3. **echo $PS1**
4. **ls -a**
5. **ls -l /etc/ passwd**
6. **sleep 1000**
7. **history**

**$ !1**                              (Execute command #1 above)  
**echo $SHELL**  
**/bin/bash**

**$ !sl**                           (Execute the command beginning with "sl")  
**sleep 1000**  
**$**

### Keyboard Shortcuts

You can use keyboard shortcuts to perform different tasks quickly. The table lists some of these keyboard shortcuts and their uses. Note the case of the "hotkey" does not matter, e.g. doing **CTRL-a** is the same as doing **CTRL-A** .

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Keyboard Shortcut</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Task</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL-L</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Clears the screen</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-D</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Exits the current shell</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-Z</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Puts the current process into suspended background</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-C</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Kills the current process</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-H</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Works the same as backspace</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-A</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Goes to the beginning of the line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-W</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Deletes the word before the cursor</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-U</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Deletes from beginning of line to cursor position</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-E</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Goes to the end of the line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">Tab</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Auto-completes files, directories, and binaries</td></tr></tbody></table>

### File Ownership

In Linux and other UNIX-based operating systems, every file is associated with a user who is the owner. Every file is also associated with a group (a subset of all users) which has an interest in the file and certain rights, or permissions: read, write, and execute.

The following utility programs involve user and group ownership and permission setting:

<table width="80%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="75%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">chown</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Used to change user ownership of a file or directory</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">chgrp</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Used to change group ownership</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">chmod</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to change the permissions on the file, which can be done separately for<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">owner</strong>,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">group</strong><span>&nbsp;</span>and the rest of the<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">world</strong><span>&nbsp;</span>(often named as<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">other</strong>)</td></tr></tbody></table>

### File Permission Modes and chmod

Files have three kinds of permissions: read (**r**), write (**w**), execute (**x**). These are generally represented as in **rwx**. These permissions affect three groups of owners: user/owner (**u**), group (**g**), and others (**o**).

As a result, you have the following three groups of three permissions:

**rwx: rwx: rwx**  
 **u:   g:   o**

There are a number of different ways to use **chmod**. For instance, to give the owner and others execute permission and remove the group write permission:

**$ ls -l somefile**  
**-rw-rw-r-- 1 student student 1601 Mar 9 15:04 somefile**  
**$ chmod uo+x,g-w somefile**  
**$ ls -l somefile**  
**-rwxr--r-x 1 student student 1601 Mar 9 15:04 somefile**

where **u** stands for user (owner), **o** stands for other (world), and **g** stands for group.

This kind of syntax can be difficult to type and remember, so one often uses a shorthand which lets you set all the permissions in one step. This is done with a simple algorithm, and a single digit suffices to specify all three permission bits for each entity. This digit is the sum of:

* **4** if read permission is desired
* **2** if write permission is desired
* **1** if execute permission is desired

Thus, **7** means read/write/execute, **6** means read/write, and **5** means read/execute.

When you apply this to the **chmod** command, you have to give three digits for each degree of freedom, such as in:

**$ chmod 755 somefile**  
**$ ls -l somefile**  
**-rwxr-xr-x 1 student student 1601 Mar 9 15:04 somefile**

![File Permission Modes and chmod](https://courses.edx.org/assets/courseware/v1/5d60930deeaaca887d468867240fc6e0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chmodmint.png)
_File Permission Modes and chmod_

### Example of chown

Let's see an example of changing file ownership using **chown**, as shown in the screenshot to the right. First, we create two empty files using **touch**.

Notice it requires sudo to change the owner of **file2** to root. The second **chown** command changes both owner and group at the same time!

Finally, only the superuser can remove the files.

![chown](https://courses.edx.org/assets/courseware/v1/d99d45386528584f3f861f182577fb1a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chownrhel7.png)
_chown_

### Example of chgrp

Now, let’s see an example of changing the group ownership using **chgrp**:

![chgrp](https://courses.edx.org/assets/courseware/v1/2416814b8977e0048d01804a8319aace/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chgrouprhel7.png)
_chgrp_

### Chapter Summary

You have completed Chapter 12. Let's summarize the key concepts covered:

* Linux is a multi-user system.
* To find the currently logged on users, you can use the **who** command.
* To find the current user ID, you can use the **whoami** command.
* The **root** account has full access to the system. It is never sensible to grant full root access to a user.
* You can assign root privileges to regular user accounts on a temporary basis using the **sudo** command.
* The shell program (bash) uses multiple startup files to create the user environment. Each file affects the interactive environment in a different way. **/etc/profile** provides the global settings.
* Advantages of startup files include that they customize the user's prompt, set the user's terminal type, set the command-line shortcuts and aliases, and set the default text editor, etc.
* An environment variable is a character string that contains data used by one or more applications. The built-in shell variables can be customized to suit your requirements.
* The **history** command recalls a list of previous commands, which can be edited and recycled.
* In Linux, various keyboard shortcuts can be used at the command prompt instead of long actual commands.
* You can customize commands by creating aliases. Adding an alias to **~/.bashrc** will make it available for other shells.
* File permissions can be changed by typing **chmod permissions filename**.
* File ownership is changed by typing **chown owner filename**.
* File group ownership is changed by typing **chgrp group filename**.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

### Video: Chapter 13 Introduction

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V002500_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Learning Objectives

By the end of this chapter, you should be able to:

* Display and append to file contents using **cat** and **echo**.
* Edit and print file contents using **sed** and **awk**.
* Search for patterns using **grep**.
* Use multiple other utilities for file and text manipulation.

### Command Line Tools for Manipulating Text Files

Irrespective of the role you play with Linux (system administrator, developer or user), you often need to browse through and parse text files, and/or extract data from them. These are file manipulation operations. Thus, it is essential for the Linux user to become adept at performing certain operations on files.

Most of the time, such file manipulation is done at the command line, which allows users to perform tasks more efficiently than while using a GUI. Furthermore, the command line is more suitable for automating often executed tasks.

Indeed, experienced system administrators write customized scripts to accomplish such repetitive tasks, standardized for each particular environment. We will discuss such scripting later in much detail.

In this section, we will concentrate on command line file and text manipulation-related utilities.

![Command Line Tools for Manipulating Text Files](https://courses.edx.org/assets/courseware/v1/1003ad62cadceacd75a659e16ec77873/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cmdlinetext.png)
_Command Line Tools for Manipulating Text Files_

### cat

**cat** is short for _**concatenate**_ and is one of the most frequently used Linux command line utilities. It is often used to read and print files, as well as for simply viewing file contents. To view a file, use the following command:

**$ cat <filename>**

For example, **cat readme.txt** will display the contents of **readme.txt** on the terminal. However, the main purpose of **cat** is often to combine (concatenate) multiple files together. You can perform the actions listed in the table using **cat**.

The **tac** command (**cat** spelled backwards) prints the lines of a file in reverse order. Each line remains the same, but the order of lines is inverted. The syntax of **tac** is exactly the same as for **cat**, as in:

**$ tac file**  
**$ tac file1 file2 > newfile**

<table border="0" align="right" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat file1 file2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Concatenate multiple files and display the output; i.e. the entire content of the first file is followed by that of the second file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat file1 file2 &gt; newfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Combine multiple files and save the output into a new file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">cat file &gt;&gt; existingfile</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Append a file to the end of an existing file</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat &gt; file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Any subsequent lines typed will go into the file, until<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-D</span></strong><span>&nbsp;</span>is typed</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">cat &gt;&gt; file</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Any subsequent lines are appended to the file, until<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-D</span></strong><span>&nbsp;</span>is typed</td></tr></tbody></table>

### Using cat Interactively

**cat** can be used to read from standard input (such as the terminal window) if no files are specified. You can use the **>** operator to create and add lines into a new file, and the **>>** operator to append lines (or files) to an existing file. We mentioned this when talking about how to create files without an editor.

To create a new file, at the command prompt type **cat** > **<filename>** and press the **Enter** key.

This command creates a new file and waits for the user to edit/enter the text. After you finish typing the required text, press **CTRL-D** at the beginning of the next line to save and exit the editing.

Another way to create a file at the terminal is **cat > <filename> << EOF**. A new file is created and you can type the required input. To exit, enter **EOF** at the beginning of a line.

Note that **EOF** is case sensitive. One can also use another word, such as **STOP**.

![Using cat: the cat << EOF > somefile command and its output, along with the cat somefile command and it's output](https://courses.edx.org/assets/courseware/v1/2186f2162bb7f8d6f7fac9004f7d4784/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cateoffedora.png)
_Using cat_

### Video: Using cat

<video controls width="100%" preload="none">

<source src="https://edx-video.net/fba83d11-cb13-4df8-9239-cb8f73dc3bdc-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Working with Large Files

System administrators need to work with configuration files, text files, documentation files, and log files. Some of these files may be large or become quite large as they accumulate data with time. These files will require both viewing and administrative updating. In this section, you will learn how to manage such large files.

For example, a banking system might maintain one simple large log file to record details of all of one day's ATM transactions. Due to a security attack or a malfunction, the administrator might be forced to check for some data by navigating within the file. In such cases, directly opening the file in an editor will cause issues, due to high memory utilization, as an editor will usually try to read the whole file into memory first. However, one can use **less** to view the contents of such a large file, scrolling up and down page by page, without the system having to place the entire file in memory before starting. This is much faster than using a text editor.

![Hand truck with three boxes](https://courses.edx.org/assets/courseware/v1/22c34eedb0df480dcad0a9e2dd731131/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/free-file-transfer.jpg)

Viewing **somefile** can be done by typing either of the two following commands:

**$ less somefile**  
**$ cat somefile | less**

By default, **man** pages are sent through the **less** command. You may have encountered the older **more** utility which has the same basic function but fewer capabilities: i.e. **less** is **more**!

### head

**head** reads the first few lines of each named file (10 by default) and displays it on standard output. You can give a different number of lines in an option.

For example, if you want to print the first 5 lines from **/etc/default/grub**, use the following command:

**$ head –n 5 /etc/default/grub**

You can also just say:

**head -5 /etc/default/grub**

![head](https://courses.edx.org/assets/courseware/v1/a19d53c185f88f384a24c5b0ae6fe03a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/headubuntu.png)
_head_

### tail

**tail** prints the last few lines of each named file and displays it on standard output. By default, it displays the last 10 lines. You can give a different number of lines as an option. **tail** is especially useful when you are troubleshooting any issue using log files, as you probably want to see the most recent lines of output.

For example, to display the last 15 lines of **somefile.log**, use the following command:

**$ tail -n 15 somefile.log**

You can also just say:

**tail -15 somefile.log**

To continually monitor new output in a growing log file:

**$ tail -f somefile.log**

This command will continuously display any new lines of output in **somefile.log** as soon as they appear. Thus, it enables you to monitor any current activity that is being reported and recorded.

![tail](https://courses.edx.org/assets/courseware/v1/e218e0f357f957b78420b93f6dc63aaf/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tailubuntu.png)
_tail_

### Viewing Compressed Files

When working with compressed files, many standard commands cannot be used directly. For many commonly-used file and text manipulation programs, there is also a version especially designed to work directly with compressed files. These associated utilities have the letter "z" prefixed to their name. For example, we have utility programs such as **zcat**, **zless**, **zdiff** and **zgrep**.

Here is a table listing some **z** family commands:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zcat compressed-file.txt.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To view a compressed file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zless somefile.gz</span></strong></span><br style="line-height: 1.4em;">or<br style="line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zmore somefile.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To page through a compressed file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zgrep -i less somefile.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To search inside a compressed file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zdiff file1.txt.gz file2.txt.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To compare two compressed files</td></tr></tbody></table>

Note that if you run **zless** on an uncompressed file, it will still work and ignore the decompression stage. There are also equivalent utility programs for other compression methods besides **gzip**, for example, we have **bzcat** and **bzless** associated with **bzip2**, and **xzcat** and **xzless** associated with **xz**.

### Introduction to sed and awk

It is very common to create and then repeatedly edit and/or extract contents from a file. Let’s learn how to use **sed** and **awk** to easily perform such operations.

![Paper and pen](https://courses.edx.org/assets/courseware/v1/452cbb45fed4bda10d6125b421f77ff7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen12a.jpg)

Note that many Linux users and administrators will write scripts using comprehensive scripting languages such as Python and perl, rather than use **sed** and **awk** (and some other utilities we will discuss later). Using such utilities is certainly fine in most circumstances; one should always feel free to use the tools one is experienced with. However, the utilities that are described here are much lighter; i.e. they use fewer system resources, and execute faster. There are situations (such as during booting the system) where a lot of time would be wasted using the more complicated tools, and the system may not even be able to run them. So, the simpler tools will always be needed.

### sed

**sed** is a powerful text processing tool and is one of the oldest, earliest and most popular UNIX utilities. It is used to modify the contents of a file or input stream, usually placing the contents into a new file or output stream. Its name is an abbreviation for stream editor.

![sed](https://courses.edx.org/assets/courseware/v1/64bebc2555b3777d251a871e72e873d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen_13.jpg)
_sed_

**sed** can filter text, as well as perform substitutions in data streams.

Data from an input source/file (or stream) is taken and moved to a working space. The entire list of operations/modifications is applied over the data in the working space and the final contents are moved to the standard output space (or stream).

### sed Command Syntax

You can invoke **sed** using commands like those listed in the accompanying table.

<table border="0" align="center" height="228" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="32%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="38%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed -e command &lt;filename&gt;</span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Specify editing commands at the command line, operate on file and put the output on standard out (e.g. the terminal)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed -f scriptfile &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Specify a scriptfile containing<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">sed</strong><span>&nbsp;</span>commands, operate on file and put output on standard out</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "I hate you" | sed s/hate/love/</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Use<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">sed</strong>&nbsp;to filter standard input, putting output on standard out</td></tr></tbody></table>

The **-e** option allows you to specify multiple editing commands simultaneously at the command line. It is unnecessary if you only have one operation invoked.

![sed Command Syntax](https://courses.edx.org/assets/courseware/v1/43267d11e71aba5dee81d8e780b24579/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/fedorased.png)
_sed Command Syntax_

### sed Basic Operations

Now that you know that you can perform multiple editing and filtering operations with **sed**, let’s explain some of them in more detail. The table explains some basic operations, where **pattern** is the current string and **replace_string** is the new string:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="45%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="55%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed s/pattern/replace_string/ file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Substitute first string occurrence in every line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed s/pattern/replace_string/g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Substitute all string occurrences in every line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed 1,3s/pattern/replace_string/g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Substitute all string occurrences in a range of lines</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed -i s/pattern/replace_string/g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Save changes for string substitution in the same file</td></tr></tbody></table>

You must use the **-i** option with care, because the action is not reversible. It is always safer to use **sed** without the **–i** option and then replace the file yourself, as shown in the following example:

**$ sed s/pattern/replace_string/g file1 > file2**

The above command will replace all occurrences of **pattern** with **replace_string** in **file1** and move the contents to **file2**. The contents of **file2** can be viewed with **cat file2**. If you approve, you can then overwrite the original file with **mv file2 file1**.

Example: To convert **01/02/…** to **JAN/FEB/…**

**sed -e 's/01/JAN/' -e 's/02/FEB/' -e 's/03/MAR/' -e 's/04/APR/' -e 's/05/MAY/' \**  
    **-e 's/06/JUN/' -e 's/07/JUL/' -e 's/08/AUG/' -e 's/09/SEP/' -e 's/10/OCT/' \**  
    **-e 's/11/NOV/' -e 's/12/DEC/'**

### Video: Using sed

<video controls width="100%" preload="none">

<source src="https://edx-video.net/8a5ec909-76f5-4085-9b47-15a8181047c8-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### awk

**awk** is used to extract and then print specific contents of a file and is often used to construct reports. It was created at Bell Labs in the 1970s and derived its name from the last names of its authors: Alfred Aho, Peter Weinberger, and Brian Kernighan.

**awk** has the following features:

* It is a powerful utility and interpreted programming language.
* It is used to manipulate data files, and for retrieving and processing text.
* It works well with fields (containing a single piece of data, essentially a column) and records (a collection of fields, essentially a line in a file).

**awk** is invoked as shown in the following:

![awk](https://courses.edx.org/assets/courseware/v1/0969d1beca3f2106cc15d5fb77f74fc0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/awkmint.png)
_awk_

As with **sed**, short **awk** commands can be specified directly at the command line, but a more complex script can be saved in a file that you can specify using the **-f** option.

<table border="0" height="177" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk ‘command’&nbsp; file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Specify a command directly at the command line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk -f scriptfile file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Specify a file that contains the script to be executed</td></tr></tbody></table>

### awk Basic Operations

The table explains the basic tasks that can be performed using **awk**. The input file is read one line at a time, and, for each line, **awk** matches the given pattern in the given order and performs the requested action. The **-F** option allows you to specify a particular _field separator_ character. For example, the **/etc/passwd** file uses "**:**" to separate the fields, so the **-F:** option is used with the **/etc/passwd** file.

The command/action in **awk** needs to be surrounded with apostrophes (or single-quote (')). **awk** can be used as follows:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="25%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk '{ print $0 }' /etc/passwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print entire file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk -F: '{ print $1 }' /etc/passwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print first field (column) of every line, separated by a colon</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk -F: '{ print $1 $7 }' /etc/passwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print first and seventh field of every line</td></tr></tbody></table>

### File Manipulation Utilities

In managing your files, you may need to perform tasks such as sorting data and copying data from one location to another. Linux provides numerous file manipulation utilities that you can use while working with text files. In this section, you will learn about the following file manipulation programs:

* **sort**
* **uniq**
* **paste**
* **join**
* **split**

You will also learn about regular expressions and search patterns.

![Blue cartoon penguin carrying monkey wrench](https://courses.edx.org/assets/courseware/v1/21bf47717bec390dbeba724a8a1b6ed6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/penguin-156529_640.png)

### sort

**sort** is used to rearrange the lines of a text file, in either ascending or descending order according to a sort key. You can also sort with respect to particular fields (columns) in a file. The default sort key is the order of the ASCII characters (i.e. essentially alphabetically).

**sort** can be used as follows:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Syntax</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sort &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Sort the lines in the specified file, according to the characters at the beginning of each line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat file1 file2 | sort</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Combine the two files, then sort the lines and display the output on the terminal</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sort -r &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Sort the lines in reverse order</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sort -k 3 &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Sort the lines by the 3rd field on each line instead of the beginning</td></tr></tbody></table>

When used with the **-u** option, **sort** checks for unique values after sorting the records (lines). It is equivalent to running **uniq** (which we shall discuss) on the output of sort.

![sort](https://courses.edx.org/assets/courseware/v1/9d6bbb9d27f74d0472f790c684258fdf/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sort.png)
_sort_

### uniq

**uniq** removes duplicate consecutive lines in a text file and is useful for simplifying the text display.

Because **uniq** requires that the duplicate entries must be consecutive, one often runs sort first and then pipes the output into **uniq**; if sort is used with the **-u** option, it can do all this in one step.

To remove duplicate entries from multiple files at once, use the following command:

**sort file1 file2 | uniq > file3**

or

**sort -u file1 file2 > file3**

To count the number of duplicate entries, use the following command:

**uniq -c filename**

![uniq](https://courses.edx.org/assets/courseware/v1/f1bc4a8919c273c3e321466d5344b2c5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/suseuniq.png)
_uniq_

### paste

Suppose you have a file that contains the full name of all employees and another file that lists their phone numbers and Employee IDs. You want to create a new file that contains all the data listed in three columns: name, employee ID, and phone number. How can you do this effectively without investing too much time?

**paste** can be used to create a single file containing all three columns. The different columns are identified based on delimiters (spacing used to separate two fields). For example, delimiters can be a blank space, a tab, or an **Enter**. In the image provided, a single space is used as the delimiter in all files.

**paste** accepts the following options:

* **-d** delimiters, which specify a list of delimiters to be used instead of tabs for separating consecutive values on a single line. Each delimiter is used in turn; when the list has been exhausted, **paste** begins again at the first delimiter.
* **-s**, which causes paste to append the data in series rather than in parallel; that is, in a horizontal rather than vertical fashion.

![paste](https://courses.edx.org/assets/courseware/v1/0c746d1cc41ea999719d5cdad330d97b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen27.jpg)

### Using paste

**paste** can be used to combine fields (such as name or phone number) from different files, as well as combine lines from multiple files. For example, line one from **file1** can be combined with line one of **file2**, line two from **file1** can be combined with line two of **file2**, and so on.

To paste contents from two files one can do:

**$ paste file1 file2**

The syntax to use a different delimiter is as follows:

**$ paste -d, file1 file2**

Common delimiters are 'space', 'tab', '|', 'comma', etc.

![Using paste](https://courses.edx.org/assets/courseware/v1/56a2128c6d67fafd5051a4b462b5fddb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/paste.png)
_Using paste_

### join

Suppose you have two files with some similar columns. You have saved employees’ phone numbers in two files, one with their first name and the other with their last name. You want to combine the files without repeating the data of common columns. How do you achieve this?

The above task can be achieved using **join**, which is essentially an enhanced version of **paste**. It first checks whether the files share common fields, such as names or phone numbers, and then joins the lines in two files based on a common field.

![Join example](https://courses.edx.org/assets/courseware/v1/da3d180e87ba8b70a3312fca74ecf815/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen30.jpg)
_join_

### Using join

To combine two files on a common field, at the command prompt type **join file1 file2** and press the **Enter** key.

For example, the common field (i.e. it contains the same values) among the **phonebook** and **cities** files is the phone number, and the result of joining these two files is shown in the screen capture.

![Using join](https://courses.edx.org/assets/courseware/v1/4ca7406b9c16747faf118ba6336e0cc5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/join.png)
_Using join_

### split

**split** is used to break up (or split) a file into equal-sized segments for easier viewing and manipulation, and is generally used only on relatively large files. By default, **split** breaks up a file into 1000-line segments. The original file remains unchanged, and a set of new files with the same name plus an added prefix is created. By default, the **x** prefix is added. To split a file into segments, use the command **split infile**.

To split a file into segments using a different prefix, use the command **split infile <Prefix>**.

![split](https://courses.edx.org/assets/courseware/v1/b842783bcec2180547358c235590e3f6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch012_screen31.jpg)

### Using split

We will apply **split** to an American-English dictionary file of over 99,000 lines:

**$ wc -l american-english**  
**99171 american-english**

where we have used **wc** (word count, soon to be discussed) to report on the number of lines in the file. Then, typing:

**$ split american-english dictionary**

will split the American-English file into 100 equal-sized segments named **dictionary_xx_**. The last one will of course be somewhat smaller.

![Using split](https://courses.edx.org/assets/courseware/v1/cccb1abafbbcd04bad08b735f151cbb0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/splitubuntu.png)
_Using split_

### Regular Expressions and Search Patterns

**Regular expressions** are text strings used for matching a specific pattern, or to search for a specific location, such as the start or end of a line or a word. Regular expressions can contain both normal characters or so-called meta-characters, such as ***** and **$**.

Many text editors and utilities such as **vi**, **sed**, **awk**, **find** and **grep** work extensively with regular expressions. Some of the popular computer languages that use regular expressions include Perl, Python and Ruby. It can get rather complicated and there are whole books written about regular expressions; thus, we will do no more than skim the surface here.

These regular expressions are different from the wildcards (or meta-characters) used in filename matching in command shells such as bash (which were covered in the _Command-Line Operations_ chapter). The table lists search patterns and their usage.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Search Patterns</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">.(dot)</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Match any single character</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">a|z</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Match a or z</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Match end of a line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">^</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Match beginning of a line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Match preceding item 0 or more times</td></tr></tbody></table>

### Using Regular Expressions and Search Patterns

For example, consider the following sentence: **the quick brown fox jumped over the lazy dog**.

Some of the patterns that can be applied to this sentence are as follows:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">a..</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">matches azy</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">b.|j.</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">matches both br and ju</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">..$</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">matches og</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">l.*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">matches lazy dog</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">l.*y</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">matches lazy</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">the.*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">matches the whole sentence</td></tr></tbody></table>

### grep

**grep** is extensively used as a primary text searching tool. It scans files for specified patterns and can be used with regular expressions, as well as simple strings, as shown in the table:

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="35%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="55%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep [pattern] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Search for a pattern in a file and print all matching lines</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep -v [pattern] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print all lines that do<strong style="font-weight: bold; line-height: 1.4em;"><span>&nbsp;</span>not</strong><span>&nbsp;</span>match the pattern</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep [0-9] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print the lines that contain the numbers<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">0</strong></span><span>&nbsp;</span>through<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">9</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep -C 3 [pattern] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print context of lines (specified number of lines above and below the pattern) for matching the pattern. Here, the number of lines is specified as 3</td></tr></tbody></table>

### strings

**strings** is used to extract all printable character strings found in the file or files given as arguments. It is useful in locating human-readable content embedded in binary files; for text files one can just use **grep**.

For example, to search for the string **my_string** in a spreadsheet:  
  
**$ strings book1.xls | grep my_string**

The screenshot shows a search of a number of programs to see which ones have GPL licenses of various versions.

![strings](https://courses.edx.org/assets/courseware/v1/394fc9ada7ed399b6aa5f3d93bf08f89/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/strings.png)
_strings_

### tr

In this section, you will learn about some additional text utilities that you can use for performing various actions on your Linux files, such as changing the case of letters or determining the count of words, lines, and characters in a file.

![tr](https://courses.edx.org/assets/courseware/v1/8d86fe669e95004b6b55386e5f15957b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/trfedora.png)
_tr_

The **tr** utility is used to translate specified characters into other characters or to delete them. The general syntax is as follows:

**$ tr [options] set1 [set2]**

The items in the square brackets are optional. **tr** requires at least one argument and accepts a maximum of two. The first, designated **set1** in the example, lists the characters in the text to be replaced or removed. The second, **set2**, lists the characters that are to be substituted for the characters listed in the first argument. Sometimes these sets need to be surrounded by apostrophes (or single-quotes (')) in order to have the shell ignore that they mean something special to the shell. It is usually safe (and may be required) to use the single-quotes around each of the sets as you will see in the examples below.

For example, suppose you have a file named **city** containing several lines of text in mixed case. To translate all lower case characters to upper case, at the command prompt type **cat city | tr a-z A-Z** and press the **Enter** key.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="65%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Command</span></strong></td><td width="35%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Usage</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convert lower case to upper case</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr '{}' '()' &lt; inputfile &gt; outputfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Translate braces into parenthesis</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "This is for testing" | tr [:space:] '\t'</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Translate white-space to tabs</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "This&nbsp;&nbsp; is&nbsp;&nbsp; for &nbsp;&nbsp; testing" | tr -s [:space:]</span></strong></span><br style="line-height: 1.4em;"></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Squeeze repetition of characters using<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-s</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "the geek stuff" | tr -d 't'</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Delete specified characters using<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-d</span></strong><span>&nbsp;</span>option</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "my username is 432234" | tr -cd [:digit:]</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Complement the sets using<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-c</span></strong><span>&nbsp;</span>option</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr -cd [:print:] &lt; file.txt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Remove all non-printable character from a file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr -s '\n' ' ' &lt; file.txt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Join all the lines in a file into a single line</td></tr></tbody></table>

### tee

**tee** takes the output from any command, and, while sending it to standard output, it also saves it to a file. In other words, it _**tees**_ the output stream from the command: one stream is displayed on the standard output and the other is saved to a file.

For example, to list the contents of a directory on the screen and save the output to a file, at the command prompt type **ls -l | tee newfile** and press the **Enter** key.

Typing **cat newfile** will then display the output of **ls –l**.

![Screenshot of tee](https://courses.edx.org/assets/courseware/v1/afb2ed8327b3ff3ea608c1dffb16a555/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tee.png)
_tee_

### wc

**wc** (**w**ord **c**ount) counts the number of lines, words, and characters in a file or list of files. Options are given in the table below.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Option</span></strong></td><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Description</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">–l</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Displays the number of lines</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-c</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Displays the number of bytes</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-w</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Displays the number of words</td></tr></tbody></table>

By default, all three of these options are active.

For example, to print only the number of lines contained in a file, type **wc -l filename** and press the **Enter** key.

![wc](https://courses.edx.org/assets/courseware/v1/68d3426354bc524157608efe82db0ca6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wcrhel7.png)
_wc_

### cut

**cut** is used for manipulating column-based files and is designed to extract specific columns. The default column separator is the **tab** character. A different delimiter can be given as a command option.

For example, to display the third column delimited by a blank space, at the command prompt type **ls -l | cut -d" " -f3** and press the **Enter** key.

![cut](https://courses.edx.org/assets/courseware/v1/48dd7d485d39f6cafc82a3a0a1c2d01c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cutrhel7.png)
_cut_

### Chapter Summary

You have completed Chapter 13. Let’s summarize the key concepts covered:

* The command line often allows the users to perform tasks more efficiently than the GUI.
* **cat**, short for concatenate, is used to read, print, and combine files.
* **echo** displays a line of text either on standard output or to place in a file.
* **sed** is a popular stream editor often used to filter and perform substitutions on files and text data streams.
* **awk** is an interpreted programming language, typically used as a data extraction and reporting tool.
* **sort** is used to sort text files and output streams in either ascending or descending order.
* **uniq** eliminates duplicate entries in a text file.
* **paste** combines fields from different files. It can also extract and combine lines from multiple sources.
* **join** combines lines from two files based on a common field. It works only if files share a common field.
* **split** breaks up a large file into equal-sized segments.
* Regular expressions are text strings used for pattern matching. The pattern can be used to search for a specific location, such as the start or end of a line or a word.
* **grep** searches text files and data streams for patterns and can be used with regular expressions.
* **tr** translates characters, copies standard input to standard output, and handles special characters.
* **tee** saves a copy of standard output to a file while still displaying at the terminal.
* **wc** (word count) displays the number of lines, words, and characters in a file or group of files.
* **cut** extracts columns from a file.
* **less** views files a page at a time and allows scrolling in both directions.
* **head** displays the first few lines of a file or data stream on standard output. By default, it displays 10 lines.
* **tail** displays the last few lines of a file or data stream on standard output. By default, it displays 10 lines.
* **strings** extracts printable character strings from binary files.
* The **z** command family is used to read and work with compressed files.

## Chapter 14: Network Operations

### Learning Objectives

By the end of this chapter, you should be able to:

* Explain basic networking concepts, including types of networks and addressing issues.
* Configure network interfaces and use basic networking utilities, such as **ifconfig**, **ip**, **ping**, **route** and **traceroute**.
* Use graphical and non-graphical browsers, such as Lynx, w3m, Firefox, Chrome and Epiphany.
* Transfer files to and from clients and servers using both graphical and text mode applications, such as Filezilla, ftp, sftp, curl and wget.

### Introduction to Networking

A network is a group of computers and computing devices connected together through communication channels, such as cables or wireless media. The computers connected over a network may be located in the same geographical area or spread across the world.

![Image](https://courses.edx.org/assets/courseware/v1/11505fb59c6ba03d861023ab12c3c0a8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen03.jpg)

A network is used to:

* Allow the connected devices to communicate with each other.
* Enable multiple users to share devices over the network, such as music and video servers, printers and scanners.
* Share and manage information across computers easily.

Most organizations have both an internal network and an Internet connection for users to communicate with machines and people outside the organization. The Internet is the largest network in the world and can be called _"the network of networks"_.

### IP Addresses

Devices attached to a network must have at least one unique network address identifier known as the **IP** (Internet Protocol) address. The address is essential for routing packets of information through the network.

Exchanging information across the network requires using streams of small packets, each of which contains a piece of the information going from one machine to another. These packets contain data buffers, together with headers which contain information about where the packet is going to and coming from, and where it fits in the sequence of packets that constitute the stream. Networking protocols and software are rather complicated due to the diversity of machines and operating systems they must deal with, as well as the fact that even very old standards must be supported.

![IP Addresses](https://courses.edx.org/assets/courseware/v1/6aefe557b5aedfc43e2983372dd202d0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen04.jpg)
_IP Addresses_

### IPv4 and IPv6

There are two different types of IP addresses available: IPv4 (version 4) and IPv6 (version 6). IPv4 is older and by far the more widely used, while IPv6 is newer and is designed to get past limitations inherent in the older standard and furnish many more possible addresses.

IPv4 uses 32-bits for addresses; there are _only_ 4.3 billion unique addresses available. Furthermore, many addresses are allotted and reserved, but not actually used. IPv4 is considered inadequate for meeting future needs because the number of devices available on the global network has increased enormously in recent years.

IPv6 uses 128-bits for addresses; this allows for 3.4 X 10<sup>38</sup> unique addresses. If you have a larger network of computers and want to add more, you may want to move to IPv6, because it provides more unique addresses. However, it can be complex to migrate to IPv6; the two protocols do not always inter-operate well. Thus, moving equipment and addresses to IPv6 requires significant effort and has not been quite as fast as was originally intended. We will discuss IPv4 more than IPv6 as you are more likely to deal with it.

One reason IPv4 has not disappeared is there are ways to effectively make many more addresses available by methods such as NAT (Network Address Translation).  NAT enables sharing one IP address among many locally connected computers, each of which has a unique address only seen on the local network. While this is used in organizational settings, it is also used in simple home networks. For example, if you have a router hooked up to your Internet Provider (such as a cable system) it gives you one externally visible address, but issues each device in your home an individual local address.

![IPv4 and IPv6](https://courses.edx.org/assets/courseware/v1/fa98328f7ff2e180a79cead9ee3e433f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen05.jpg)

### Decoding IPv4 Addresses

A 32-bit IPv4 address is divided into four 8-bit sections called [octets](https://en.wikipedia.org/wiki/Octet_(computing)).

Example:  
IP address →            172  .          16  .          31  .         46  
Bit format →     10101100.00010000.00011111.00101110

_**NOTE**_: Octet is just another word for byte.

Network addresses are divided into five classes: A, B, C, D and E. Classes A, B and C are classified into two parts: Network addresses (Net ID) and Host address (Host ID). The Net ID is used to identify the network, while the Host ID is used to identify a host in the network. Class D is used for special multicast applications (information is broadcast to multiple computers simultaneously) and Class E is reserved for future use. In this section you will learn about classes A, B and C.

![Decoding IPv4 Addresses](https://courses.edx.org/assets/courseware/v1/610943ad6bb219df591ec8659288e630/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen06.jpg)
_Decoding IPv4 Addresses_

### Class A Network Addresses

Class A addresses use the first octet of an IP address as their Net ID and use the other three octets as the Host ID**.** The first bit of the first octet is always set to zero. So you can use only 7-bits for unique network numbers. As a result, there are a maximum of 126 Class A networks available (the addresses 0000000 and 1111111 are reserved). Not surprisingly, this was only feasible when there were very few unique networks with large numbers of hosts. As the use of the Internet expanded, Classes B and C were added in order to accommodate the growing demand for independent networks.

Each Class A network can have up to 16.7 million unique hosts on its network. The range of host addresses is from **1.0.0.0** to **127.255.255.255**.

_**NOTE**_: The value of an octet, or 8-bits, can range from 0 to 255.

![Class A Network Addresses](https://courses.edx.org/assets/courseware/v1/1867a1e02d2827251e50b65a03bcaa1b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen07.jpg)
_Class A Network Addresses_

### Class B Network Addresses

Class B addresses use the first two octets of the IP address as their Net ID and the last two octets as the Host ID. The first two bits of the first octet are always set to binary 10, so there are a maximum of 16,384 (14-bits) Class B networks. The first octet of a Class B address has values from 128 to 191. The introduction of Class B networks expanded the number of networks but it soon became clear that a further level would be needed.

Each Class B network can support a maximum of 65,536 unique hosts on its network. The range of host addresses is from **128.0.0.0** to **191.255.255.255**.

![Class B Network Addresses](https://courses.edx.org/assets/courseware/v1/7e40d0c228a2ac28dd4e1e9af18ba3ce/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen08.jpg)
_Class B Network Addresses_

### Class C Network Addresses

Class C addresses use the first three octets of the IP address as their Net ID and the last octet as their Host ID. The first three bits of the first octet are set to binary 110, so almost 2.1 million (21-bits) Class C networks are available. The first octet of a Class C address has values from 192 to 223. These are most common for smaller networks which don't have many unique hosts.

Each Class C network can support up to 256 (8-bits) unique hosts. The range of host addresses is from **192.0.0.0** to **223.255.255.255**.

![Class C Network Addresses](https://courses.edx.org/assets/courseware/v1/376a6fe8144e0d5799f331a803e1d33d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen09.jpg)
_Class C Network Addresses_

### IP Address Allocation

Typically, a range of IP addresses are requested from your Internet Service Provider (ISP) by your organization's network administrator. Often, your choice of which class of IP address you are given depends on the size of your network and expected growth needs. If NAT is in operation, such as in a home network, you only get one externally visible address!

![IP Address Allocation](https://courses.edx.org/assets/courseware/v1/303c5dc5b32edde05f599cac40512b7d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen10a.jpg)
_IP Address Allocation_

You can assign IP addresses to computers over a network either manually or dynamically. Manual assignment adds static (never changing) addresses to the network. Dynamically assigned addresses can change every time you reboot or even more often; the Dynamic Host **C**onfiguration Protocol (DHCP) is used to assign IP addresses.

### Name Resolution

Name Resolution is used to convert numerical IP address values into a human-readable format known as the hostname. For example, **104.95.85.15** is the numerical IP address that refers to the hostname whitehouse.gov. Hostnames are much easier to remember!

Given an IP address, you can obtain its corresponding hostname. Accessing the machine over the network becomes easier when you can type the hostname instead of the IP address.

You can view your system’s hostname simply by typing **hostname** with no argument.

_**NOTE**_: If you give an argument, the system will try to change its hostname to match it, however, only root users can do that.

The special hostname localhost is associated with the IP address **127.0.0.1** and describes the machine you are currently on (which normally has additional network-related IP addresses).

![Screenshot Showing Server IP Address of The Linux Foundation Website](https://courses.edx.org/assets/courseware/v1/c4e92d4d86a678c688c053c06672df41/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen12.jpg)
_Screenshot Showing Server IP Address of The Linux Foundation Website_

<video controls width="100%" preload="none">

<source src="https://edx-video.net/fccd6182-2956-47b2-a3d8-6dd2e15ef226-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Network Configuration Files

Network configuration files are essential to ensure that interfaces function correctly. They are located in the **/etc** directory tree. However, the exact files used have historically been dependent on the particular Linux distribution and version being used.

For Debian family configurations, the basic network configuration files could be found under **/etc/network/**, while for Red Hat and SUSE family systems one needed to inspect **/etc/sysconfig/network**.

Modern systems emphasize the use of Network Manager, which we briefly discussed when we considered graphical system administration, rather than try to keep up with the vagaries of the files in **/etc**. While the graphical versions of Network Manager do look somewhat different in different distributions, the **nmtui** utility (shown in the screenshot) varies almost not at all, as does the even more sparse **nmcli** (command line interface) utility. If you are proficient in the use of the GUIs, by all means, use them. If you are working on a variety of systems, the lower level utilities may make life easier.

![Network Manager](https://courses.edx.org/assets/courseware/v1/30ad387df9ee4d04b71b8a402855df8c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/nmtui.png)
_Network Manager_

Recent Ubuntu distributions include **netplan**, which is turned on by default, and supplants Network Manager. Since no other distribution has shown interest, and since it can easily be disabled if it bothers you, we will ignore it.

### Network Interfaces

Network interfaces are a connection channel between a device and a network. Physically, network interfaces can proceed through a network interface card (NIC), or can be more abstractly implemented as software. You can have multiple network interfaces operating at once. Specific interfaces can be brought up (activated) or brought down (deactivated) at any time.

Information about a particular network interface or all network interfaces can be reported by the **ip** and **ifconfig** utilities, which you may have to run as the superuser, or at least, give the full path, i.e. **/sbin/ifconfig**, on some distributions. **ip** is newer than **ifconfig** and has far more capabilities, but its output is uglier to the human eye. Some new Linux distributions do not install the older **net-tools** package to which **ifconfig** belongs, and  so you would have to install it if you want to use it.

![Network Interfaces](https://courses.edx.org/assets/courseware/v1/13f3ece7b614bbaab0872571831112b2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ipiconfigrhel7.png)
_Network Interfaces_

### The ip Utility

To view the IP address:

**$ /sbin/ip addr show**

To view the routing information:

**$ /sbin/ip route show**

**ip** is a very powerful program that can do many things. Older (and more specific) utilities such as **ifconfig** and **route** are often used to accomplish similar tasks. A look at the relevant man pages can tell you much more about these utilities.

![ip utility](https://courses.edx.org/assets/courseware/v1/a863fadf4376afe31b1e3fea08fcc1cc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/iprhel7.png)
_ip Utility_

### ping

**ping** is used to check whether or not a machine attached to the network can receive and send data; i.e. it confirms that the remote host is online and is responding.

To check the status of the remote host, at the command prompt, type **ping <hostname>**.

**ping** is frequently used for network testing and management; however, its usage can increase network load unacceptably. Hence, you can abort the execution of **ping** by typing **CTRL-C**, or by using the **-c** option, which limits the number of packets that **ping** will send before it quits. When execution stops, a summary is displayed.

![ping](https://courses.edx.org/assets/courseware/v1/ff267f7328fc6da9070a550a1b43d40b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pingc8.png)
_ping_

### route

A network requires the connection of many nodes. Data moves from source to destination by passing through a series of routers and potentially across multiple networks. Servers maintain routing tables containing the addresses of each node in the network. The IP routing protocols enable routers to build up a forwarding table that correlates final destinations with the next hop addresses.

![route](https://courses.edx.org/assets/courseware/v1/fe2820385b830a22cf8deccad8e0428c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/routeubuntu.png)
_route_

One can use the **route** utility or the newer **ip route** command to view or change the IP routing table to add, delete, or modify specific (static) routes to specific hosts or networks. The table explains some commands that can be used to manage IP routing:

<table border="0" height="218" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Task</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Show current routing table</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ route –n</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ip route</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Add static route</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ route add -net address</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ip route add</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Delete static route</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ route del -net address</span></strong><span>&nbsp;</span>or<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ip route del</span></strong></td></tr></tbody></table>

### traceroute

**traceroute** is used to inspect the route which the data packet takes to reach the destination host, which makes it quite useful for troubleshooting network delays and errors. By using **traceroute**, you can isolate connectivity issues between hops, which helps resolve them faster.

To print the route taken by the packet to reach the network host, at the command prompt, type **traceroute <address>**.

![traceroute](https://courses.edx.org/assets/courseware/v1/58901958924b2bc7e0ffe898fb384926/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tracerouterhel7.png)
_traceroute_

### More Networking Tools

Now, let’s learn about some additional networking tools. Networking tools are very useful for monitoring and debugging network problems, such as network connectivity and network traffic.

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="25%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Networking Tools</strong></span></td><td align="center" bgcolor="#003f60" width="55%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ethtool</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Queries network interfaces and can also set various parameters such as the speed</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">netstat</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Displays all active connections and routing tables; useful for monitoring performance and troubleshooting</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">nmap</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Scans open ports on a network; important for security analysis</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tcpdump</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Dumps network traffic for analysis</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">iptraf</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Monitors network traffic in text mode</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mtr</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Combines functionality of ping and traceroute and gives a continuously updated display</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dig</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Tests DNS workings; a good replacement for host and nslookup</td></tr></tbody></table>

### Video: Using More Networking Tools

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V004400_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Graphical and Non-Graphical Browsers

Browsers are used to retrieve, transmit, and explore information resources, usually on the World Wide Web. Linux users commonly use both graphical and non-graphical browser applications.

The common graphical browsers used in Linux are:

* [Firefox](https://www.mozilla.org/en-US/firefox/)
* [Google Chrome](https://www.google.com/chrome/)
* [Chromium](https://www.chromium.org/Home)
* [Konqueror](https://kde.org/applications/internet/org.kde.konqueror)
* [Opera](https://www.opera.com/)

Sometimes, you either do not have a graphical environment to work in (or have reasons not to use it) but still need to access web resources. In such a case, you can use non-graphical browsers, such as the following:

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Non-Graphical Browsers</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><a href="http://lynx.browser.org/" target="_blank" style="color: rgb(0, 104, 141); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; text-decoration: none; transition: all 0.1s linear 0s;">lynx</a></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Configurable text-based web browser; the earliest such browser and still in use</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><a href="http://www.elinks.cz/" target="_blank" style="color: rgb(0, 104, 141); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; text-decoration: none; transition: all 0.1s linear 0s;">elinks</a></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Based on Lynx; it can display tables and frames</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><a href="http://w3m.sourceforge.net/" target="_blank" style="color: rgb(0, 104, 141); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; text-decoration: none; transition: all 0.1s linear 0s;">w3m</a></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Another text-based web browser with many features</td></tr></tbody></table>

### wget

Sometimes, you need to download files and information, but a browser is not the best choice, either because you want to download multiple files and/or directories, or you want to perform the action from a command line or a script. **wget** is a command line utility that can capably handle the following types of downloads:

* Large file downloads
* Recursive downloads, where a web page refers to other web pages and all are downloaded at once
* Password-required downloads
* Multiple file downloads.

To download a web page, you can simply type **wget <url>**, and then you can read the downloaded page as a local file using a graphical or non-graphical browser.

![wget](https://courses.edx.org/assets/courseware/v1/47e400802600472e68f58d081c51a252/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wgetc8.png)
_wget_

### curl

Besides downloading, you may want to obtain information about a URL, such as the source code being used. **curl** can be used from the command line or a script to read such information. **curl** also allows you to save the contents of a web page to a file, as does **wget**.

You can read a URL using **curl <URL>**. For example, if you want to read [http://www.linuxfoundation.org](https://www.linuxfoundation.org/), type **curl http://www.linuxfoundation.org**.

To get the contents of a web page and store it to a file, type **curl -o saved.html http://www.mysite.com**. The contents of the main index file at the website will be saved in **saved.html**.

![curl](https://courses.edx.org/assets/courseware/v1/f82c5e92a716627d3623a7cb1286613d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/curlrhel7.png)
_curl_

### FTP (File Transfer Protocol)

When you are connected to a network, you may need to transfer files from one machine to another. File Transfer Protocol (FTP) is a well-known and popular method for transferring files between computers using the Internet. This method is built on a client-server model. FTP can be used within a browser or with stand-alone client programs.

![File Transfer Protocol](https://courses.edx.org/assets/courseware/v1/6c4efd743bc9707314f89c414e219e88/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen33.jpg)
_File Transfer Protocol_

FTP is one of the oldest methods of network data transfer, dating back to the early 1970s. As such, it is considered inadequate for modern needs, as well as being intrinsically insecure. However, it is still in use and when security is not a concern (such as with so-called anonymous FTP) it can make sense. However, many websites, such as [kernel.org](https://www.kernel.org/), have abandoned its use.

### FTP Clients

FTP clients enable you to transfer files with remote computers using the FTP protocol. These clients can be either graphical or command line tools. Filezilla, for example, allows use of the drag-and-drop approach to transfer files between hosts. All web browsers support FTP, all you have to do is give a URL like **ftp://ftp.kernel.org** where the usual **http://** becomes **ftp://**.

Some command line FTP clients are:

* **ftp**
* **sftp**
* **ncftp**
* **yafc** (Yet Another FTP Client).

FTP has fallen into disfavor on modern systems, as it is intrinsically insecure, since passwords are user credentials that can be transmitted without encryption and are thus prone to interception. Thus, it was removed in favor of using **rsync** and web browser https access for example. As an alternative, **sftp** is a very secure mode of connection, which uses the Secure Shell (**ssh**) protocol, which we will discuss shortly. **sftp** encrypts its data and thus sensitive information is transmitted more securely. However, it does not work with so-called anonymous FTP (guest user credentials).

![ FTP Clients](https://courses.edx.org/assets/courseware/v1/0daf82fa22922b50848d2d73df3cfa1c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen34.jpg)
_FTP Clients_

### SSH: Executing Commands Remotely

Secure Shell (SSH) is a cryptographic network protocol used for secure data communication. It is also used for remote services and other secure services between two devices on the network and is very useful for administering systems which are not easily available to physically work on, but to which you have remote access.

![SSH: Executing Commands Remotely](https://courses.edx.org/assets/courseware/v1/b19e7547d1f707f6ba4b134c31f43a31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen37.jpg)
_SSH: Executing Commands Remotely_

To login to a remote system using your same user name you can just type **ssh some_system** and press **Enter**. **ssh** then prompts you for the remote password. You can also configure ssh to securely allow your remote access without typing a password each time.

If you want to run as another user, you can do either **ssh -l someone some_system** or **ssh someone@some_system**. To run a command on a remote system via SSH, at the command prompt, you can type **ssh some_system my_command**.

### Copying Files Securely with scp

We can also move files securely using Secure Copy (scp) between two networked hosts. scp uses the SSH protocol for transferring data.

To copy a local file to a remote system, at the command prompt, type **scp <localfile> <user@remotesystem>:/home/user/** and press **Enter**.

You will receive a prompt for the remote password. You can also configure **scp** so that it does not prompt for a password for each transfer.

![Copying Files Securely with scp](https://courses.edx.org/assets/courseware/v1/83970c9d6a9a9462fe7463ada6b79e45/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen38.jpg)
_Copying Files Securely with scp_

### Video: Using SSH Between Two Virtual Machines

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002000_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

## Chapter Summary

You have completed Chapter 14. Let’s summarize the key concepts covered:

* The IP (Internet Protocol) address is a unique logical network address that is assigned to a device on a network.
* IPv4 uses 32-bits for addresses and IPv6 uses 128-bits for addresses.
* Every IP address contains both a network and a host address field.
* There are five classes of network addresses available: A, B, C, D & E.
* DNS (Domain Name System) is used for converting Internet domain and host names to IP addresses.
* The **ifconfig** program is used to display current active network interfaces.
* The commands **ip addr show** and **ip route show** can be used to view IP address and routing information.
* You can use **ping** to check if the remote host is alive and responding.
* You can use the **route** utility program to manage IP routing.
* You can monitor and debug network problems using networking tools.
* Firefox, Google Chrome, Chromium, and Epiphany are the main graphical browsers used in Linux.
* Non-graphical or text browsers used in Linux are Lynx, Links, and w3m.
* You can use **wget** to download webpages.
* You can use **curl** to obtain information about URLs.
* FTP (File Transfer Protocol) is used to transfer files over a network.
* ftp, sftp, ncftp, and yafc are command line FTP clients used in Linux.
* You can use **ssh** to run commands on remote systems.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)



## Chapter 15: The Bash Shell and Basic Scripting

### Learning Objectives

By the end of this chapter, you should be able to:

* Explain the features and capabilities of bash shell scripting.
* Know the basic syntax of scripting statements.
* Be familiar with various methods and constructs used.
* Test for properties and existence of files and other objects.
* Use conditional statements, such as if-then-else blocks.
* Perform arithmetic operations using scripting language.

### Shell Scripting

Suppose you want to look up a filename, check if the associated file exists, and then respond accordingly, displaying a message confirming or not confirming the file's existence. If you only need to do it once, you can just type a sequence of commands at a terminal. However, if you need to do this multiple times, automation is the way to go. In order to automate sets of commands, you will need to learn how to write shell scripts. Most commonly in Linux, these scripts are developed to be run under the **bash** command shell interpreter. The graphic illustrates several of the benefits of deploying scripts.

![Features of Shell Scripts: Combine long and repetitive sequences of commands into one simple command; Share procedures among several users; Quick prototyping, no need to compile; Create new commands using a combination of utilities; Provide a controlled interface to users; Automate tasks and reduce risk of errors](https://courses.edx.org/assets/courseware/v1/86597edd8ece86b852333387ed386d8b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch14_screen03.jpg)

**Features of Shell Scripts**

**_NOTE:_** _Many of the topics discussed in this and the next chapter have already been introduced earlier, while discussing things that can be done at the command line. We have elected to repeat some of that discussion in order to make the sections on scripting stand on their own, so the repetition is intentional._

### Command Shell Choices

The command interpreter is tasked with executing statements that follow it in the script. Commonly used interpreters include: **/usr/bin/perl**, **/bin/bash**, **/bin/csh**, **/usr/bin/python** and **/bin/sh**.

Typing a long sequence of commands at a terminal window can be complicated, time consuming, and error prone. By deploying shell scripts, using the command line becomes an efficient and quick way to launch complex sequences of steps. The fact that shell scripts are saved in a file also makes it easy to use them to create new script variations and share standard procedures with several users.

Linux provides a wide choice of shells; exactly what is available on the system is listed in **/etc/shells**. Typical choices are:

**/bin/sh**  
**/bin/bash**  
**/bin/tcsh**  
**/bin/csh**  
**/bin/ksh**  
**/bin/zsh**

Most Linux users use the default bash shell, but those with long UNIX backgrounds with other shells may want to override the default.

![Command Shell Choices](https://courses.edx.org/assets/courseware/v1/8ddc714dd87a83c3b2724d72c86a42a4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_chapter14_screen_5.jpeg)
_Command Shell Choices_

### Shell Scripts

Remember from our earlier discussion, a shell is a command line interpreter which provides the user interface for terminal windows. It can also be used to run scripts, even in non-interactive sessions without a terminal window, as if the commands were being directly typed in. For example, typing **find . -name "*.c" -ls** at the command line accomplishes the same thing as executing a script file containing the lines:

**#!/bin/bash**  
**find . -name "*.c" -ls**

The first line of the script, which starts with **#!**, contains the full path of the command interpreter (in this case **/bin/bash**) that is to be used on the file. As we have noted, you have quite a few choices for the scripting language you can use, such as **/usr/bin/perl**, **/bin/csh**, **/usr/bin/python**, etc.

![Shell Scripts - Screenshot of the find . -name ](https://courses.edx.org/assets/courseware/v1/0eb4ca4bc524fd56385e35895ee29687/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findcrhel.png)
_Shell Scripts_

### A Simple bash Script

Let's write a simple bash script that displays a one line message on the screen. Either type:

**$ cat > hello.sh**  
**#!/bin/bash**  
**echo "Hello Linux Foundation Student"**

and press **ENTER** and **CTRL-D** to save the file, or just create **hello.sh** in your favorite text editor. Then, type **chmod +x hello.sh** to make the file executable by all users.

You can then run the script by typing **./hello.sh** or by doing:

**$ bash hello.sh**  
**Hello Linux Foundation Student**

_**NOTE**_: If you use the second form, you do not have to make the file executable.

![A Simple bash Script; this is a screenshot of the commands used as examples in this section and their output](https://courses.edx.org/assets/courseware/v1/4fca06e1c36113a2f4e0fc7975e8020b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/hellosuse.png)
_A Simple bash Script_

### Interactive Example Using bash Scripts

Now, let's see how to create a more interactive example using a bash script. The user will be prompted to enter a value, which is then displayed on the screen. The value is stored in a temporary variable, **name**. We can reference the value of a shell variable by using a **$** in front of the variable name, such as **$name**. To create this script, you need to create a file named **getname.sh** in your favorite editor with the following content:

**#!/bin/bash**  
**# Interactive reading of a variable**  
**echo "ENTER YOUR NAME"**  
**read name**  
**# Display variable input**  
**echo The name given was :$name**

Once again, make it executable by doing **chmod +x getname.sh**.

In the above example, when the user types **./getname.sh** and the script is executed, the user is prompted with the string **ENTER YOUR NAME**. The user then needs to enter a value and press the **Enter** key. The value will then be printed out.

_**NOTE**_: The hash-tag/pound-sign/number-sign (**_#_**) is used to start comments in the script and can be placed anywhere in the line (the rest of the line is considered a comment). However, note the special magic combination of **_#!_**, used on the first line, is a unique exception to this rule.

![Interactive Example Using bash Scripts, this is a screenshot of the example provided in text](https://courses.edx.org/assets/courseware/v1/7c1b84e695c8774f7ffb474cf9321a74/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/getnamesuse.png)
_Interactive Example Using bash Scripts_

### Return Values

All shell scripts generate a return value upon finishing execution, which can be explicitly set with the **exit** statement. Return values permit a process to monitor the exit state of another process, often in a parent-child relationship. Knowing how the process terminates enables taking any appropriate steps which are necessary or contingent on success or failure.

![Return Values: Representation of the parent process calling the child process, which in turn returns value to the parent process](https://courses.edx.org/assets/courseware/v1/4d9ca0cc7e62c429a040b0592dfe56dc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch14_screen10.jpg)
_Return Values_

### Viewing Return Values

As a script executes, one can check for a specific value or condition and return success or failure as the result. By convention, success is returned as **0**, and failure is returned as a non-zero value. An easy way to demonstrate success and failure completion is to execute ls on a file that exists as well as one that does not, the return value is stored in the environment variable represented by **$?**:

**$ ls /etc/logrotate.conf**  
**/etc/logrotate.conf**

**$ echo $?**  
**0**

In this example, the system is able to locate the file **/etc/logrotate.conf** and `**ls**` returns a value of **0** to indicate success. When run on a non-existing file, it returns **2**. Applications often translate these return values into meaningful messages easily understood by the user.

![Viewing Return Values on an example similar to the one provided in text](https://courses.edx.org/assets/courseware/v1/90838d9edb43aa18d3a7805b6b952da3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/returnvalmint.png)
_Viewing Return Values_

### Basic Syntax and Special Characters

Scripts require you to follow a standard language syntax. Rules delineate how to define variables and how to construct and format allowed statements, etc. The table lists some special character usages within bash scripts:

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Character</strong></span></td><td align="center" bgcolor="#003f60" width="70%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">#</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to add a comment, except when used as<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">\#</span></strong>, or as<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">#!</span></strong><span>&nbsp;</span>when starting a script</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">\</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used at the end of a line to indicate continuation on to the next line</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to interpret what follows as a new command to be executed next</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Indicates what follows is an environment variable</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&gt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Redirect output</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&gt;&gt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Append output</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&lt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Redirect input</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">|</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Used to pipe the result into the next command</td></tr></tbody></table>

There are other special characters and character combinations and constructs that scripts understand, such as **(..)**, **{..}**, **[..]**, **&&**, **||**, **'**, **"**, **$((...))**, some of which we will discuss later.

### Splitting Long Commands Over Multiple Lines

Sometimes, commands are too long to either easily type on one line, or to grasp and understand (even though there is no real practical limit to the length of a command line).

In this case, the concatenation operator (**\**), the backslash character, is used to continue long commands over several lines.

Here is an example of a command installing a long list of packages on a system using Debian package management:

**$~/> cd $HOME**  
**$~/> sudo apt-get install autoconf automake bison build-essential \**  
    **chrpath curl diffstat emacs flex gcc-multilib g++-multilib \**   
    **libsdl1.2-dev libtool lzop make mc patch \**  
    **screen socat sudo tar texinfo tofrodos u-boot-tools unzip \**  
    **vim wget xterm zip**

The command is divided into multiple lines to make it look readable and easier to understand. The **\** operator at the end of each line causes the shell to combine (concatenate) multiple lines and executes them as one single command.

![Screenshot of an example of splitting long commands over multiple lines - similar to the one given in text](https://courses.edx.org/assets/courseware/v1/5b9f46e3e0919a56bacc51f56da06592/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/continue.png)
_Splitting Long Commands Over Multiple Lines_

### Putting Multiple Commands on a Single Line

Users sometimes need to combine several commands and statements and even conditionally execute them based on the behavior of operators used in between them. This method is called chaining of commands.

There are several different ways to do this, depending on what you want to do. The `**;**` (semicolon) character is used to separate these commands and execute them sequentially, as if they had been typed on separate lines. Each ensuing command is executed whether or not the preceding one succeeded.

Thus, the three commands in the following example will all execute, even if the ones preceding them fail:

**$ make ; make install ; make clean**

However, you may want to abort subsequent commands when an earlier one fails. You can do this using the **&&** (and) operator as in:

**$ make && make install && make clean**

If the first command fails, the second one will never be executed. A final refinement is to use the **||** (or) operator, as in:

**$ cat file1 || cat file2 || cat file3**

In this case, you proceed until something succeeds and then you stop executing any further steps.

Chaining commands is not the same as piping them; in the later case succeeding commands begin operating on data streams produced by earlier ones before they complete, while in chaining each step exits before the next one starts.

![Screenshot with an example of putting multiple commands on a single line: cd / ; echo doing ls on / ; ls ; cd $HOME ; echo doing ls on $Home ; ls doing ls on / ](https://courses.edx.org/assets/courseware/v1/60f1cf664b8f4f4e3543445ce02b4c2d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/multcommint.png)
_Putting Multiple Commands on a Single Line_

### Output Redirection

Most operating systems accept input from the keyboard and display the output on the terminal. However, in shell scripting you can send the output to a file. The process of diverting the output to a file is called output redirection. We have already used this facility in our earlier sections on how to use the command line.

The **>** character is used to write output to a file. For example, the following command sends the output of `**free**` to **/tmp/free.out**:

**$ free > /tmp/free.out**

To check the contents of **/tmp/free.out**, at the command prompt type **cat /tmp/free.out**.

Two **>** characters (**>>**) will append output to a file if it exists, and act just like **>** if the file does not already exist.

![Screenshot with an example of output redirection: ls /etc/grub.d . /tmp/grubd](https://courses.edx.org/assets/courseware/v1/891c3d95be4e45c6e5c18bc85a7592bc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/outredirectubuntu.png)
_Output Redirection_

### Input Redirection

Just as the output can be redirected to a file, the input of a command can be read from a file. The process of reading input from a file is called input redirection and uses the **<** character.

The following three commands (using **wc** to count the number of lines, words and characters in a file) are entirely equivalent and involve input redirection, and a command operating on the contents of a file:

**$ wc < /etc/passwd**  
**49  105 2678 /etc/passwd**

**$ wc /etc/passwd**  
**49  105 2678 /etcpasswd**

**$ cat /etc/passwd | wc**  
**49  105 2678**

### Built-In Shell Commands

Shell scripts execute sequences of commands and other types of statements. These commands can be:

* Compiled applications
* Built-in bash commands
* Shell scripts or scripts from other interpreted languages, such as perl and Python.

Compiled applications are binary executable files, generally residing on the filesystem in well-known directories such as **/usr/bin**. Shell scripts always have access to applications such as **rm**, **ls**, **df**, **vi**, and **gzip**, which are programs compiled from lower level programming languages such as C.

In addition, bash has many built-in commands, which can only be used to display the output within a terminal shell or shell script. Sometimes, these commands have the same name as executable programs on the system, such as **echo**, which can lead to subtle problems. bash built-in commands include **cd**, **pwd**, **echo**, **read**, **logout**, **printf**, **let**, and **ulimit**. Thus, slightly different behavior can be expected from the built-in version of a command such as **echo** as compared to **/bin/echo**.

A complete list of bash built-in commands can be found in the bash man page, or by simply typing **help**, as we review on the next page.

![Built-In Shell Commands: There are different typs of commands - for compiled applications, like rm, ls, df, vi, gzip. We also have built-in bash commands, like cd, pwd, echo, read, logout, printf, let, ulimit, and commands for other scripts.](https://courses.edx.org/assets/courseware/v1/552b91648741f8ce6769d7859aec989f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_chapter14_screen_15.jpg)
_Built-In Shell Commands_

### Commands Built in to bash

We already enumerated which commands have versions built in to bash, in our earlier discussion of how to get help on Linux systems. Once again, here is a screenshot listing exactly which commands are available.

![Screenshot listing exactly which commands are available; these commands can also be retrieved from the man pages](https://courses.edx.org/assets/courseware/v1/79040611925a7890d2337fb896445e08/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/helpbash.png)
_Commands Built in to bash_

### Script Parameters

Users often need to pass parameter values to a script, such as a filename, date, etc. Scripts will take different paths or arrive at different values according to the parameters (command arguments) that are passed to them. These values can be text or numbers as in:

**$ ./script.sh /tmp**  
**$ ./script.sh 100 200**  
  
Within a script, the parameter or an argument is represented with a **$** and a number or special character. The table lists some of these parameters.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 652px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Parameter</strong></span></td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Meaning</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$0</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Script name</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$1</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">First parameter</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$2</span></strong>,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$3</span></strong>, etc.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Second, third parameter, etc.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">All parameters</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$#</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Number of arguments</td></tr></tbody></table>

### Using Script Parameters

If you type in the script shown in the figure, make the script executable with **chmod +x param.sh**. Then, run the script giving it several arguments, as shown. The script is processed as follows:

**$0** prints the script name: **param.sh**

**$1** prints the first parameter: **one**

**$2** prints the second parameter: **two**

**$3** prints the third parameter: **three**

**$*** prints all parameters: **one two three four five**

The final statement becomes: **All done with param.sh**

![Using Script Parameters. A screenshot of the cat param.sh command and its output](https://courses.edx.org/assets/courseware/v1/a7d08ff7b0604bb8bd5d324cc162d17f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/scriptparams.png)
_Using Script Parameters_

### Command Substitution

At times, you may need to substitute the result of a command as a portion of another command. It can be done in two ways:

* By enclosing the inner command in **$( )**
* By enclosing the inner command with backticks **(**`**)**

The second, backticks form, is deprecated in new scripts and commands. No matter which method is used, the specified command will be executed in a newly launched shell environment, and the standard output of the shell will be inserted where the command substitution is done.

Virtually any command can be executed this way. While both of these methods enable command substitution, the **$( )** method allows command nesting. New scripts should always use this more modern method. For example:

**$ ls /lib/modules/$(uname -r)/**

In the above example, the output of the command **uname –r** (which will be something like **5.13.3**), is inserted into the argument for the **ls** command.

![Command Substitution: a screenshot of the commands provided in this section and their output](https://courses.edx.org/assets/courseware/v1/9d5313940c7ba6bfcf850ccd3cfe7159/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/uname-rhel.png)
_Command Substitution_

### Environment Variables

Most scripts use variables containing a value, which can be used anywhere in the script. These variables can either be user or system-defined. Many applications use such environment variables (already covered in some detail in the _User Environment_ chapter) for supplying inputs, validation, and controlling behavior.

As we discussed earlier, some examples of standard environment variables are **HOME**, **PATH**, and **HOST**. When referenced, environment variables must be prefixed with the **$** symbol, as in **$HOME**. You can view and set the value of environment variables. For example, the following command displays the value stored in the **PATH** variable:

**$ echo $PATH**

However, no prefix is required when setting or modifying the variable value. For example, the following command sets the value of the **MYCOLOR** variable to blue:

**$ MYCOLOR=blue**

You can get a list of environment variables with the **env**, **set**, or **printenv** commands.

![Environment Variables: a screenshot with different environment variables: echo $MY_FAVORITE_OS; MY_FAVORITE_OS=Linux; echo $MY_FAVORITE_OS Linux; env | grep LANG](https://courses.edx.org/assets/courseware/v1/59918633e922e55ffec6d63ac36f6f08/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/envubuntu.png)
_Environment Variables_

### Exporting Environment Variables

While we discussed the export of environment variables in the section on the "_User Environment_", it is worth reviewing this topic in the context of writing bash scripts.

By default, the variables created within a script are available only to the subsequent steps of that script. Any child processes (sub-shells) do not have automatic access to the values of these variables. To make them available to child processes, they must be promoted to environment variables using the export statement, as in:

**export VAR=value**

or

**VAR=value ; export VAR**

While child processes are allowed to modify the value of exported variables, the parent will not see any changes; exported variables are not shared, they are only copied and inherited.

Typing export with no arguments will give a list of all currently exported environment variables.

![Exporting Variables: a screenshot of export | head -20](https://courses.edx.org/assets/courseware/v1/34717c82ff6e4ce8e5e5dc58c2f2e926/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/exportubuntu.png)
_Exporting Variables_

### Functions

A function is a code block that implements a set of operations. Functions are useful for executing procedures multiple times, perhaps with varying input variables. Functions are also often called subroutines. Using functions in scripts requires two steps:

1. Declaring a function
2. Calling a function

The function declaration requires a name which is used to invoke it. The proper syntax is:

**function_name () {**  
   **command...**  
**}**

For example, the following function is named **display**:

**display () {**  
   **echo "This is a sample function"**  
**}**

The function can be as long as desired and have many statements. Once defined, the function can be called later as many times as necessary. In the full example shown in the figure, we are also showing an often-used refinement: how to pass an argument to the function. The first argument can be referred to as **$1**, the second as **$2**, etc.

![Functions: a screenshot of cat testbashfunc.sh and its output; and of ./testbashfunc.sh and its output](https://courses.edx.org/assets/courseware/v1/f504c2c7131128204c2482cfc4eb4926/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bashfunubuntu.png)
_Functions_

### The if Statement

Conditional decision making, using an **if** statement, is a basic construct that any useful programming or scripting language must have.

When an **if** statement is used, the ensuing actions depend on the evaluation of specified conditions, such as:

* Numerical or string comparisons
* Return value of a command (0 for success)
* File existence or permissions

In compact form, the syntax of an **if** statement is:

**if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi**

A more general definition is:

**if condition**  
**then**  
       **statements**  
**else**  
       **statements**  
**fi**

![The if Statement: a representation of the if statement IF (A=True) Then B Else C End IF](https://courses.edx.org/assets/courseware/v1/8f788761d1ca61e862e140b8942647a5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/500px-If-Then-Else-diagram.svg.png)
_The if Statement_

### Using the if Statement

In the following example, an **if** statement checks to see if a certain file exists, and if the file is found, it displays a message indicating success or failure:

**if [ -f "$1" ]**  
**then**  
    **echo file "$1 exists"**   
**else**  
    **echo file "$1" does not exist**  
**fi**

We really should also check first that there is an argument passed to the script (**$1**) and abort if not.

Notice the use of the square brackets (**[]**) to delineate the test condition. There are many other kinds of tests you can perform, such as checking whether two numbers are equal to, greater than, or less than each other and make a decision accordingly; we will discuss these other tests.

![Sign showing two splitting arrows](https://courses.edx.org/assets/courseware/v1/fda3ff96ecc163874e0bc6e8ba1dc17b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/49fork1.png)

In modern scripts, you may see doubled brackets as in **[[ -f /etc/passwd ]]**. This is not an error. It is never wrong to do so and it avoids some subtle problems, such as referring to an empty environment variable without surrounding it in double quotes; we will not talk about this here.

### The elif Statement

You can use the **elif** statement to perform more complicated tests, and take action appropriate actions. The basic syntax is:

**if [ sometest ] ; then**  
    **echo Passed test1**   
**elif [ somothertest ] ; then**  
    **echo Passed test2**   
**fi**

In the example shown we use strings tests which we will explain shortly, and show how to pull in an environment variable with the **read** statement.

![The elif Statement: a screenshot with an example cat ./show_elif.sh](https://courses.edx.org/assets/courseware/v1/4d5cccfd1d279bcb4d7c792561ecc574/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/elif.png)
_The elif Statement_

### Testing for Files

bash provides a set of file conditionals, that can be used with the **if** statement, including those in the table.

You can use the **if** statement to test for file attributes, such as:

* File or directory existence
* Read or write permission
* Executable permission.

For example, in the following example:

**if [ -x /etc/passwd ] ; then**  
    **ACTION**  
**fi**

the **if** statement checks if the file **/etc/passwd** is executable, which it is not. Note the very common practice of putting:

**; then**

on the same line as the **if** statement.

You can view the full list of file conditions typing:

**man 1 test**.

<table border="1" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Condition</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Meaning</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-e file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file exists.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-d file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file is a directory.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-f file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file is a regular file (i.e. not a symbolic link, device node, directory, etc.)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-s file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file is of non-zero size.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;;">-g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file has<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sgid</span></strong><span>&nbsp;</span>set.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-u file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file has<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">suid</span></strong><span>&nbsp;</span>set.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-r file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file is readable.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-w file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file is writable.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-x file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Checks if the file is executable.</span></td></tr></tbody></table>

### Boolean Expressions

Boolean expressions evaluate to either TRUE or FALSE, and results are obtained using the various Boolean operators listed in the table.

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Operator</strong></span></td><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Operation</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Meaning</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">&amp;&amp;</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">AND</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">The action will be performed only if both the conditions evaluate to true.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">||</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">OR</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">The action will be performed if any one of the conditions evaluate to true.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">!</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">NOT</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">The action will be performed only if the condition evaluates to false.&nbsp;</td></tr></tbody></table>

Note that if you have multiple conditions strung together with the **&&** operator, processing stops as soon as a condition evaluates to false. For example, if you have **A && B && C** and A is true but B is false, C will never be executed.

Likewise, if you are using the **||** operator, processing stops as soon as anything is true. For example, if you have **A || B || C** and A is false and B is true, you will also never execute C.

### Tests in Boolean Expressions

Boolean expressions return either TRUE or FALSE. We can use such expressions when working with multiple data types, including strings or numbers, as well as with files. For example, to check if a file exists, use the following conditional test:

**[ -e <filename> ]**

Similarly, to check if the value of **number1** is greater than the value of **number2**, use the following conditional test:

**[ $number1 -gt $number2 ]**

The operator **-gt** returns TRUE if **number1** is greater than **number2**.

![Two circles, red one that says False and green one that says True](https://courses.edx.org/assets/courseware/v1/682aa174a76a223c71f9f7ee6718192b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/truefalse.jpg)

### Example of Testing of Strings

You can use the **if** statement to compare strings using the operator **==** (two equal signs). The syntax is as follows:

**if [ string1 == string2 ] ; then**  
   **ACTION**  
**fi**

Note that using one **=** sign will also work, but some consider it deprecated usage. Let’s now consider an example of testing strings.

In the example illustrated here, the **if** statement is used to compare the input provided by the user and accordingly display the result.

![Example of Testing of Strings: screenshot of the command cat ./testifstring.sh and its output](https://courses.edx.org/assets/courseware/v1/cfe88d1d2fd45ad3e5330dfe36d1b388/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ifstringubuntu.png)
_Example of Testing of Strings_

### Numerical Tests

You can use specially defined operators with the **if** statement to compare numbers. The various operators that are available are listed in the table:

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 472px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Operator</strong></span></td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Meaning</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-eq</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Equal to</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-ne</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Not equal to</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-gt</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Greater than</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-lt</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Less than</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-ge</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Greater than or equal to</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-le</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Less than or equal to</td></tr></tbody></table>

The syntax for comparing numbers is as follows:  
  
**exp1 -op exp2**

### Example of Testing for Numbers

Let us now consider an example of comparing numbers using the various operators:

![Example of Testing for Numbers](https://courses.edx.org/assets/courseware/v1/ec0a1d119f27a66c769d359c79c2903c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/mathtestubuntu.png)
_Example of Testing for Numbers_

### Arithmetic Expressions

Arithmetic expressions can be evaluated in the following three ways (spaces are important!):

* Using the **expr** utility  
**expr** is a standard but somewhat deprecated program. The syntax is as follows:**expr 8 + 8**  
**echo $(expr 8 + 8)**
* Using the **$((...))** syntax  
This is the built-in shell format. The syntax is as follows:**echo $((x+1))**
* Using the built-in shell command **let**. The syntax is as follows:**let x=( 1 + 2 ); echo $x**

In modern shell scripts, the use of **expr** is better replaced with **var=$((...))**.

![Arithmetic Expressions: screenshot with examples already provided in text](https://courses.edx.org/assets/courseware/v1/9dd7a4a63091202085482a6efcbb8e06/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/mathevalrhel7.png)
_Arithmetic Expressions_

## Chapter Summary

You have completed Chapter 15. Let’s summarize the key concepts covered:

* Scripts are a sequence of statements and commands stored in a file that can be executed by a shell. The most commonly used shell in Linux is bash.
* Command substitution allows you to substitute the result of a command as a portion of another command.
* Functions or routines are a group of commands that are used for execution.
* Environmental variables are quantities either preassigned by the shell or defined and modified by the user.
* To make environment variables visible to child processes, they need to be exported**.**
* Scripts can behave differently based on the parameters (values) passed to them.
* The process of writing the output to a file is called output redirection.
* The process of reading input from a file is called input redirection.
* The **if** statement is used to select an action based on a condition.
* Arithmetic expressions consist of numbers and arithmetic operators, such as **+**, **-**, and *****.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 16: More on Bash Shell Scripting

### Learning Objectives

By the end of this chapter, you should be able to:

* Manipulate strings to perform actions such as comparison and sorting.
* Use Boolean expressions when working with multiple data types, including strings or numbers, as well as files.
* Use **case** statements to handle command line options.
* Use looping constructs to execute one or more lines of code repetitively.
* Debug scripts using set **-x** and set **+x**.
* Create temporary files and directories.
* Create and use random numbers.

### String Manipulation

Let’s go deeper and find out how to work with strings in scripts.

A string variable contains a sequence of text characters. It can include letters, numbers, symbols and punctuation marks. Some examples include: **abcde**, **123**, **abcde 123**, **abcde-123**, **&acbde=%123**.

String operators include those that do comparison, sorting, and finding the length. The following table demonstrates the use of some basic string operators:

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Operator</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Meaning</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[[ string1 &gt; string2 ]]</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compares the sorting order of<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string1</span></strong><span>&nbsp;</span>and<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string2</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[[ string1 == string2 ]]</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compares the characters in<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string1</span></strong><span>&nbsp;</span>with the characters in<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">string2</strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myLen1=${#string1}</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Saves the length of<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string1</span></strong><span>&nbsp;</span>in the variable<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myLen1</span></strong>.</td></tr></tbody></table>

### Example of String Manipulation

In the first example, we compare the first string with the second string and display an appropriate message using the **if** statement.

![Comparing strings and Using if Statement](https://courses.edx.org/assets/courseware/v1/d42af5098b77f89c8bc2b5a5b5dbc0e9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/stringdemos_horizontal1.png)
_Comparing strings and Using if Statement_

In the second example, we pass in a file name and see if that file exists in the current directory or not.

![Passing a File Name and Checking if It Exists in the Current Directory](https://courses.edx.org/assets/courseware/v1/800018a909b1873c8fcd29da8159ecd6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/stringdemos_horizontal2.png)
_Passing a File Name and Checking if It Exists in the Current Directory_

### Parts of a String

At times, you may not need to compare or use an entire string. To extract the first **n** characters of a string we can specify: **${string:0:n}**. Here, **0** is the offset in the string (i.e. which character to begin from) where the extraction needs to start and **n** is the number of characters to be extracted.

To extract all characters in a string after a dot (**.**), use the following expression: **${string#*.}**.

![Parts of a String - screenshot example](https://courses.edx.org/assets/courseware/v1/55bddf886d7e365fae4c1842a4f0e58d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/stringmanip.png)
_Parts of a String_

### The case Statement

The **case** statement is used in scenarios where the actual value of a variable can lead to different execution paths. **case** statements are often used to handle command-line options.

Below are some of the advantages of using the **case** statement:

* It is easier to read and write.
* It is a good alternative to nested, multi-level **if-then-else-fi** code blocks.
* It enables you to compare a variable against several values at once.
* It reduces the complexity of a program.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-106.png)
_Features of case Statement_

### Structure of the case Statement

Here is the basic structure of the **case** statement:

**case expression in**  
   **pattern1) execute commands;;**  
   **pattern2) execute commands;;**  
   **pattern3) execute commands;;**  
   **pattern4) execute commands;;**  
   *** )       execute some default commands or nothing ;;**  
**esac**

![Structure of the case Statement - a graphical representation of the example provided in text](https://courses.edx.org/assets/courseware/v1/afb49c3ebe75ff82910621adb09a22c6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch15_screen18.jpg)
_Structure of the case Statement_

### Example of Use of the case Construct

Here is an example of the use of a **case** construct. Note you can have multiple possibilities for each case value that take the same action.

![Example of Use of the case Construct - screenshot](https://courses.edx.org/assets/courseware/v1/d8b4e5bc4dec2df7351c100a88cf194a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testcase.png)
_Example of Use of the case Construct_

### Looping Constructs

By using looping constructs, you can execute one or more lines of code repetitively, usually on a selection of values of data such as individual files. Usually, you do this until a conditional test returns either true or false, as is required.

![Looping Constructs - a graphical representation of a looping construct](https://courses.edx.org/assets/courseware/v1/5501cea8fcca399926635852bc90f847/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch15_screen23.jpg)

**Looping Constructs**

Three types of loops are often used in most programming languages:

* **for**
* **while**
* **until**

All these loops are easily used for repeating a set of statements until the exit condition is true.

### The for Loop

The **for** loop operates on each element of a list of items. The syntax for the **for** loop is:

**for _variable-name_** in _list_  
**do**  
    **execute one iteration for each item in the **_list_** until the _list_** is finished  
**done**

In this case, **variable-name** and **list** are substituted by you as appropriate (see examples). As with other looping constructs, the statements that are repeated should be enclosed by **do** and **done**.

The screenshot here shows an example of the **for** loop to print the sum of numbers 1 to 10.

![The for loop - screenshot](https://courses.edx.org/assets/courseware/v1/038af602fa06b5f5cb01872bd46f2423/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testfor.png)
_The for Loop_

### The while Loop

The **while** loop repeats a set of statements as long as the control command returns true. The syntax is:

**while condition is true**  
**do**  
    **Commands for execution**  
    **----**  
**done**

The set of commands that need to be repeated should be enclosed between **do** and **done**. You can use any command or operator as the condition. Often, it is enclosed within square brackets (**[]**).

The screenshot here shows an example of the **while** loop that calculates the factorial of a number. Do you know why the computation of 21! gives a bad result?

![The while Loop](https://courses.edx.org/assets/courseware/v1/8c4861a61a1dc05f846c70efcc38023f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testwhile.png)
_The while Loop_

### The until Loop

The **until** loop repeats a set of statements as long as the control command is false. Thus, it is essentially the opposite of the **while** loop. The syntax is:

**until condition is false**  
**do**  
    **Commands for execution**  
    **----**  
**done**

Similar to the **while** loop, the set of commands that need to be repeated should be enclosed between **do** and **done**. You can use any command or operator as the condition.

The screenshot here shows an example of the **until** loop that once again computes factorials; it is only slightly different than the test case for the **while** loop.

![The until Loop](https://courses.edx.org/assets/courseware/v1/3d9d6fd37f62074ecfb72259fd7aff2d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testuntil.png)
_The until Loop_

### Debugging bash Scripts

While working with scripts and commands, you may run into errors. These may be due to an error in the script, such as an incorrect syntax, or other ingredients, such as a missing file or insufficient permission to do an operation. These errors may be reported with a specific error code, but often just yield incorrect or confusing output. So, how do you go about identifying and fixing an error?

![Warning sign: an exclamation mark inside a triangle](https://courses.edx.org/assets/courseware/v1/b166486f15fcdf1d865381b1bac2ebee/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Chapter15_Screen29.jpg)

Debugging helps you troubleshoot and resolve such errors, and is one of the most important tasks a system administrator performs.

### Script Debug Mode

Before fixing an error (or bug), it is vital to know its source.

You can run a bash script in debug mode either by doing **bash –x ./script_file**, or bracketing parts of the script with **set -x** and **set +x**. The debug mode helps identify the error because:

* It traces and prefixes each command with the **+** character.
* It displays each command before executing it.
* It can debug only selected parts of a script (if desired) with:

**set -x    # turns on debugging**  
**...**  
**set +x    # turns off debugging**

The screenshot shown here demonstrates a script which runs in debug mode if run with any argument on the command line.

![Script Debug Mode](https://courses.edx.org/assets/courseware/v1/c79e74ef2465111f5d42ab90f5354816/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/shdebug.png)
_Script Debug Mode_

### Redirecting Errors to File and Screen

In UNIX/Linux, all programs that run are given three open file streams when they are started as listed in the table:

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">File stream<br style="line-height: 1.4em;"></strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">File Descriptor</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">stdin</strong></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Standard Input, by default the keyboard/terminal for programs run from the command line</td><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">stdout</strong></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Standard output, by default the screen for programs run from the command line</td><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">stderr</strong></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Standard error, where output error messages are shown or saved</td><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">2</td></tr></tbody></table>

Using redirection, we can save the stdout and stderr output streams to one file or two separate files for later analysis after a program or command is executed.

The screenshot shows a shell script with a simple bug, which is then run and the error output is diverted to **error.log**. Using **cat** to display the contents of the error log adds in debugging. Do you see how to fix the script?

![Redirecting Errors to File and Screen](https://courses.edx.org/assets/courseware/v1/62739a0082a4076aaac72eba972e9760/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testbasherr.png)
_Redirecting Errors to File and Screen_

### Creating Temporary Files and Directories

Consider a situation where you want to retrieve 100 records from a file with 10,000 records. You will need a place to store the extracted information, perhaps in a temporary file, while you do further processing on it.

Temporary files (and directories) are meant to store data for a short time. Usually, one arranges it so that these files disappear when the program using them terminates. While you can also use touch to create a temporary file, in some circumstances this may make it easy for hackers to gain access to your data. This is particularly true if the name and the file location of the temporary file are predictable.

The best practice is to create random and unpredictable filenames for temporary storage. One way to do this is with the **mktemp** utility, as in the following examples.

The **XXXXXXXX** is replaced by **mktemp** with random characters to ensure the name of the temporary file cannot be easily predicted and is only known within your program.

<table width="80%" border="0" height="30" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To create a temporary file</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">TEMPDIR=$(mktemp -d /tmp/tempdir.XXXXXXXX)</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To create a temporary directory</td></tr></tbody></table>

### Example of Creating a Temporary File and Directory

Sloppiness in creation of temporary files can lead to real damage, either by accident or if there is a malicious actor. For example, if someone were to create a symbolic link from a known temporary file used by root to the **/etc/passwd** file, like this:

**$ ln -s /etc/passwd /tmp/tempfile**  
  
There could be a big problem if a script run by root has a line in it like this:

**echo $VAR > /tmp/tempfile**

The password file will be overwritten by the temporary file contents.

To prevent such a situation, make sure you randomize your temporary file names by replacing the above line with the following lines:

**TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)**  
**echo $VAR > $TEMP**

Note the screen capture shows similarly named temporary files from different days, but with randomly generated characters in them.

![Example of Creating a Temporary File and Directory](https://courses.edx.org/assets/courseware/v1/433c4d5c1a0172fe4a8f3e2cabfcf2d9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tmpfilecentos.png)
_Example of Creating a Temporary File and Directory_

### Discarding Output with /dev/null

Certain commands (like **find**) will produce voluminous amounts of output, which can overwhelm the console. To avoid this, we can redirect the large output to a special file (a device node) called **/dev/null**. This pseudofile is also called the bit bucket or black hole.

All data written to it is discarded and write operations never return a failure condition. Using the proper redirection operators, it can make the output disappear from commands that would normally generate output to stdout and/or stderr:

**$ ls -lR /tmp > /dev/null**

In the above command, the entire standard output stream is ignored, but any errors will still appear on the console. However, if one does:

**$ ls -lR /tmp >& /dev/null**

both **stdout** and **stderr** will be dumped into **/dev/null**.

![Discarding Output with /dev/null - screenshot](https://courses.edx.org/assets/courseware/v1/f36fdbaed019caeb06c7a083c02c723a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/devnullrhel.png)
_Discarding Output with /dev/null_

### Random Numbers and Data

It is often useful to generate random numbers and other random data when performing tasks such as:

* Performing security-related tasks
* Reinitializing storage devices
* Erasing and/or obscuring existing data
* Generating meaningless data to be used for tests

Such random numbers can be generated by using the **$RANDOM** environment variable, which is derived from the Linux kernel’s built-in random number generator, or by the OpenSSL library function, which uses the FIPS140 (Federal Information Processing Standard) algorithm to generate random numbers for encryption

To learn about FIPS140, read Wikipedia's _["FIPS 140-2"](https://en.wikipedia.org/wiki/FIPS_140-2)_ article.

The example shows you how to easily use the environmental variable method to generate random numbers.

![Random Numbers and Data: screenshot: for n in 1 2 3 4 5 do echo A New Random Number is $RANDOM done](https://courses.edx.org/assets/courseware/v1/bea7e92c667890b6a5ae69110ca423b0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/randomubuntu.png)
_Random Numbers and Data_

### How the Kernel Generates Random Numbers

Some servers have hardware random number generators that take as input different types of noise signals, such as thermal noise and photoelectric effect. A transducer converts this noise into an electric signal, which is again converted into a digital number by an A-D converter. This number is considered random. However, most common computers do not contain such specialized hardware and, instead, rely on events created during booting to create the raw data needed.

Regardless of which of these two sources is used, the system maintains a so-called entropy pool of these digital numbers/random bits. Random numbers are created from this entropy pool.

The Linux kernel offers the **/dev/random** and **/dev/urandom** device nodes, which draw on the entropy pool to provide random numbers which are drawn from the estimated number of bits of noise in the entropy pool.

**/dev/random** is used where very high quality randomness is required, such as one-time pad or key generation, but it is relatively slow to provide values. **/dev/urandom** is faster and suitable (good enough) for most cryptographic purposes.

Furthermore, when the entropy pool is empty, **/dev/random** is blocked and does not generate any number until additional environmental noise (network traffic, mouse movement, etc.) is gathered, whereas **/dev/urandom** reuses the internal pool to produce more pseudo-random bits.

![How the Kernel Generates Random Numbers: screenshot of ls -l /dev/*random](https://courses.edx.org/assets/courseware/v1/0679d15bcba06e9661b627311a08d674/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/devrandom.png)
_How the Kernel Generates Random Numbers_

### Chapter Summary

You have completed Chapter 16. Let’s summarize the key concepts covered:

* You can manipulate strings to perform actions such as comparison, sorting, and finding length.
* You can use Boolean expressions  when working with multiple data types, including strings or numbers, as well as files.
* The output of a Boolean expression is either true or false.
* Operators used in Boolean expressions include the **&&** (AND), **||** (OR), and **!** (NOT) operators.
* We looked at the advantages of using the **case** statement in scenarios where the value of a variable can lead to different execution paths.
* Script debugging methods help troubleshoot and resolve errors.
* The standard and error outputs from a script or shell commands can easily be redirected into the same file or separate files to aid in debugging and saving results.
* Linux allows you to create temporary files and directories, which store data for a short duration, both saving space and increasing security.
* Linux provides several different ways of generating random numbers, which are widely used.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapter 17: Printing

### Learning Objectives

By the end of this chapter, you should know how to:

* Configure a printer on a Linux machine.
* Print documents.
* Manipulate postscript and PDF files using command line utilities.

### Printing on Linux

To manage printers and print directly from a computer or across a networked environment, you need to know how to configure and install a printer. Printing itself requires software that converts information from the application you are using to a language your printer can understand. The Linux standard for printing software is the Common UNIX Printing System (CUPS).

![Printer](https://courses.edx.org/assets/courseware/v1/514ce391fd913757d030e1f09c150a28/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_03.jpg)

Modern Linux desktop systems make installing and administering printers pretty simple and intuitive, and not unlike how it is done on other operating systems. Nevertheless, it is instructive to understand the underpinnings of how it is done in Linux.

### CUPS Overview

CUPS is the underlying software almost all Linux systems use to print from applications like a web browser or LibreOffice. It converts page descriptions produced by your application (put a paragraph here, draw a line there, and so forth) and then sends the information to the printer. It acts as a print server for both local and network printers.

Printers manufactured by different companies may use their own particular print languages and formats. CUPS uses a modular printing system which accommodates a wide variety of printers and also processes various data formats. This makes the printing process simpler; you can concentrate more on printing and less on how to print.

![CUPS Logo](https://courses.edx.org/assets/courseware/v1/b8f78f6dba29b1dc4c034cf9d4675136/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/CUPs_Logo.png)

Generally, the only time you should need to configure your printer is when you use it for the first time. In fact, CUPS often figures things out on its own by detecting and configuring any printers it locates.

### How Does CUPS Work?

CUPS carries out the printing process with the help of its various components:

* Configuration files
* Scheduler
* Job files
* Log files
* Filter
* Printer drivers
* Backend.

You will learn about each of these components on the next few pages.

![How CUPS Works](https://courses.edx.org/assets/courseware/v1/28c1710704f1ec7b7ccd6077c7aa31f4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_05.jpg)
_How CUPS Works_

### Scheduler

CUPS is designed around a print scheduler that manages print jobs, handles administrative commands, allows users to query the printer status, and manages the flow of data through all CUPS components.

![Scheduler](https://courses.edx.org/assets/courseware/v1/1203221f84765ec536df6fdfb185fb41/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_06.jpg)
_Scheduler_

We will look at the browser-based interface that can be used with CUPS,  which allows you to view and manipulate the order and status of pending print jobs.

### Configuration Files

The print scheduler reads server settings from several configuration files, the two most important of which are **cupsd.conf** and **printers.conf**. These and all other CUPS related configuration files are stored under the **/etc/cups/** directory.

**cupsd.conf** is where most system-wide settings are located; it does not contain any printer-specific details. Most of the settings available in this file relate to network security, i.e. which systems can access CUPS network capabilities, how printers are advertised on the local network, what management features are offered, and so on.

**printers.conf** is where you will find the printer-specific settings. For every printer connected to the system, a corresponding section describes the printer’s status and capabilities. This file is generated or modified only after adding a printer to the system, and should not be modified by hand.

You can view the full list of configuration files by typing **ls -lF /etc/cups**.

![/etc/cups/ directory](https://courses.edx.org/assets/courseware/v1/de0cfde1b60578e057bc993ba743d0b4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/etccupsubuntu.png)
_/etc/cups/ Directory_

### Job Files

CUPS stores print requests as files under the **/var/spool/cups** directory (these can actually be accessed before a document is sent to a printer). Data files are prefixed with the letter **d** while control files are prefixed with the letter **c**.

![/var/spool/cups directory](https://courses.edx.org/assets/courseware/v1/2b1b29c43960fe465f11db866b7038ab/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varspoolcups.png)
_/var/spool/cups Directory_

After a printer successfully handles a job, data files are automatically removed. These data files belong to what is commonly known as the **print queue**.

![Print Queue](https://courses.edx.org/assets/courseware/v1/b27d7c01c145f191b20af19557961c06/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_08.jpg)
_Print Queue_

### Log Files

Log files are placed in **/var/log/cups** and are used by the scheduler to record activities that have taken place. These files include access, error, and page records.

To view what log files exist, type:  
  
**$ sudo ls -l /var/log/cups**

![Viewing the Log Files Using ls -l /var/log/cups](https://courses.edx.org/assets/courseware/v1/42b65f75b623d2abba013731fde26998/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varlogcups.png)
_Viewing Log Files Using ls -l /var/log/cups_

Note on some distributions permissions are set such that you do not need to use **sudo**. You can view the log files with the usual tools.

![Viewing the Log Files Using $sudo ls -l /var/log/cups](https://courses.edx.org/assets/courseware/v1/8982f4095d6fedbc55e436c682674f3d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_09.jpg)
_Viewing Log Files Using $ sudo ls -l /var/log/cups_

### Filters, Printer Drivers, and Backends

CUPS uses **filters** to convert job file formats to printable formats. **Printer drivers** contain descriptions for currently connected and configured printers, and are usually stored under **/etc/cups/ppd/**. The print data is then sent to the printer through a filter, and via a **backend** that helps to locate devices connected to the system.

![Filters, Printer Drivers, and Backends](https://courses.edx.org/assets/courseware/v1/9337f33810fd20eecf2a2eb5a05b51fc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_10.jpg)
_Filters, Printer Drivers, and Backends_

So, in short, when you execute a print command, the scheduler validates the command and processes the print job, creating job files according to the settings specified in the configuration files. Simultaneously, the scheduler records activities in the log files. Job files are processed with the help of the filter, printer driver, and backend, and then sent to the printer.

### Managing CUPS

Assuming CUPS has been installed you'll need to start and manage the CUPS daemon so that CUPS is ready for configuring a printer. Managing the CUPS daemon is simple; all management features can be done with the **systemctl** utility:

**$ systemctl status cups**

**$ sudo systemctl [enable|disable] cups**

**$ sudo systemctl [start|stop|restart] cups**

**_NOTE_**_:_ _The_ next section _demonstrates this on Ubuntu, but is the same for all major current Linux distributions._

### Video: Managing the CUPS Daemon

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002100_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Configuring a Printer from the GUI

Each Linux distribution has a GUI application that lets you add, remove, and configure local or remote printers. Using this application, you can easily set up the system to use both local and network printers. The following screens show how to find and use the appropriate application in each of the distribution families covered in this course.

When configuring a printer, make sure the device is currently turned on and connected to the system; if so it should show up in the printer selection menu. If the printer is not visible, you may want to troubleshoot using tools that will determine if the printer is connected. For common USB printers, for example, the **lsusb** utility will show a line for the printer. Some printer manufacturers also require some extra software to be installed in order to make the printer visible to CUPS, however, due to the standardization these days, this is rarely required.

![Configuring a Printer from the GUI](https://courses.edx.org/assets/courseware/v1/e9032460f5217fca7de5f2a6c2250028/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/rh8settings.png)
_Configuring a Printer from the GUI_

### Video: Adding a Network Printer

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002600_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Adding Printers from the CUPS Web Interface

A fact that few people know is that CUPS also comes with its own web server, which makes a configuration interface available via a set of CGI scripts.

This web interface allows you to:

* Add and remove local/remote printers
* Configure printers:

– Local/remote printers– Share a printer as a CUPS server

* Control print jobs:– Monitor jobs

– Show completed or pending jobs– Cancel or move jobs.

The CUPS web interface is available on your browser at: [http://localhost:631](http://localhost:631/).

Some pages require a username and password to perform certain actions, for example to add a printer. For most Linux distributions, you must use the root password to add, modify, or delete printers or classes.

![Screenshot of the CUPS Website](https://courses.edx.org/assets/courseware/v1/1dd8bc3bbcec1fee255a3ff121034328/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cups_web.png)
_Screenshot of the CUPS Website_

### Printing from the Graphical Interface

Many graphical applications allow users to access printing features using the **CTRL-P** shortcut. To print a file, you first need to specify the printer (or a file name and location if you are printing to a file instead) you want to use; and then select the page setup, quality, and color options. After selecting the required options, you can submit the document for printing. The document is then submitted to CUPS. You can use your browser to access the CUPS web interface at [http://localhost:631/](http://localhost:631/) to monitor the status of the printing job. Now that you have configured the printer, you can print using either the Graphical or Command Line interfaces.

The screenshot shows the GUI interface for **CTRL-P** for CentOS, other Linux distributions appear virtually identical.

![GUI interface for CTRL-P for CentOS](https://courses.edx.org/assets/courseware/v1/91be7ab270ff6ac96da0a42409b190fe/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/printingrhel7.png)
_GUI Interface for CTRL-P for CentOS_

### Printing from the Command-Line Interface

CUPS provides two command-line interfaces, descended from the System V and BSD flavors of UNIX. This means that you can use either **lp** (System V) or **lpr** (BSD) to print. You can use these commands to print text, PostScript, PDF, and image files.

These commands are useful in cases where printing operations must be automated (from shell scripts, for instance, which contain multiple commands in one file).

**lp** is just a command line front-end to the **lpr** utility that passes input to **lpr**. Thus, we will discuss only **lp** in detail. In the example shown here, the task is to print **$HOME/.emacs**.****

![Printing from the Command-Line Interface](https://courses.edx.org/assets/courseware/v1/66b0064f81cd4f18fa50ccd9fde41bf9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lprhel7.png)
_Printing from the Command-Line Interface_

### Using lp

**lp** and **lpr** accept command line options that help you perform all operations that the GUI can accomplish. **lp** is typically used with a file name as an argument.

Some **lp** commands and other printing utilities you can use are listed in the table:

<table border="0" width="60%" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lp &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To print the file to default printer</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lp -d printer &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To print to a specific printer (useful if multiple printers are available)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">program | lp<br style="line-height: 1.4em;">echo string | lp</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To print the output of a program</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lp -n number &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To print multiple copies</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpoptions -d printer</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To set the default printer</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpq -a</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To show the queue status</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpadmin</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To configure printer queues</td></tr></tbody></table>

**lpoptions** can be used to set printer options and defaults. Each printer has a set of tags associated with it, such as the default number of copies and authentication requirements. You can type **lpoptions help** to obtain a list of supported options. **lpoptions** can also be used to set system-wide values, such as the default printer.

### Video: Printing Using lp

<video controls width="100%" preload="none">

<source src="https://edx-video.net/4cf89569-6b26-4f3e-b8ba-915db0f1a759-mp4_720p.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Managing Print Jobs

You send a file to the shared printer. But when you go there to collect the printout, you discover another user has just started a 200 page job that is not time sensitive. Your file cannot be printed until this print job is complete. What do you do now?

In Linux, command line print job management commands allow you to monitor the job state as well as managing the listing of all printers and checking their status, and canceling or moving print jobs to another printer.

Some of these commands are listed in the table.

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Command</span></strong></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Usage</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpstat -p -d</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To get a list of available printers, along with their status</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpstat -a</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To check the status of all connected printers, including job numbers</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cancel job-id</span></strong><br style="line-height: 1.4em;">OR<br style="line-height: 1.4em;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lprm job-id</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To cancel a print job</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpmove job-id newprinter</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">To move a print job to new printer</td></tr></tbody></table>

### Working with PostScript and PDF

PostScript is a standard  page description language. It effectively manages scaling of fonts and vector graphics to provide quality printouts. It is purely a text format that contains the data fed to a PostScript interpreter. The format itself is a language that was developed by Adobe in the early 1980s to enable the transfer of data to printers.

![Working with PostScript and PDF](https://courses.edx.org/assets/courseware/v1/0361c9466d73a78da7b4a4846bd6b984/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Ch13_Screen_42.jpg)

**Working with PostScript and PDF**

Features of PostScript are:

* It can be used on any printer that is PostScript-compatible; i.e. any modern printer
* Any program that understands the PostScript specification can print to it
* Information about page appearance, etc. is embedded in the page.

Postscript has been for the most part superseded by the PDF format (Portable Document Format) which produces far smaller files in a compressed format for which support has been integrated into many applications. However, one still has to deal with postscript documents, often as an intermediate format on the way to producing final documents.

### Working with enscript

**enscript** is a tool that is used to convert a text file to PostScript and other formats. It also supports Rich Text Format (RTF) and HyperText Markup Language (HTML). For example, you can convert a text file to two columns (**-2**) formatted PostScript using the command:

**$ enscript -2 -r -p psfile.ps textfile.txt**

This command will also rotate (**-r**) the output to print so the width of the paper is greater than the height (aka landscape mode) thereby reducing the number of pages required for printing.

The commands that can be used with **enscript** are listed in the table below (for a file called **textfile.txt**).

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="70%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">enscript -p psfile.ps textfile.txt</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convert a text file to PostScript (saved to<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">psfile.ps</span></strong></span>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">enscript -n -p psfile.ps textfile.txt</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convert a text file to n columns where n=1-9 (saved in<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">psfile.ps</span></strong></span>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">enscript textfile.txt</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Print a text file directly to the default printer</td></tr></tbody></table>

### Converting between PostScript and PDF

Most users today are far more accustomed to working with files in PDF format, viewing them easily either on the Internet through their browser or locally on their machine. The PostScript format is still important for various technical reasons that the general user will rarely have to deal with.

From time to time, you may need to convert files from one format to the other, and there are very simple utilities for accomplishing that task. **ps2pdf** and **pdf2ps** are part of the **ghostscript** package installed on or available on all Linux distributions. As an alternative, there are **pstopdf** and **pdftops** which are usually part of the **poppler** package, which may need to be added through your package manager. Unless you are doing a lot of conversions or need some of the fancier options (which you can read about in the man pages for these utilities), it really does not matter which ones you use.

Another possibility is to use the very powerful **convert** program, which is part of the **ImageMagick** package. Some newer distributions have replaced this with Graphics Magick**,** and the command to use is **gm convert**.

Some usage examples:

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdf2ps file.pdf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Converts&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.pdf</span></strong>&nbsp;to<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.ps</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ps2pdf file.ps</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Converts&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.ps</span></strong><span>&nbsp;</span>to<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.pdf</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pstopdf input.ps output.pdf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Converts&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.ps</span></strong><span>&nbsp;</span>to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.pdf</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftops input.pdf output.ps</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Converts&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.pdf</span></strong><span>&nbsp;</span>to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.ps</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">convert input.ps output.pdf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Converts&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.ps</span></strong><span>&nbsp;</span>to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.pdf</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">convert input.pdf output.ps</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Converts<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.pdf</span></strong><span>&nbsp;</span>to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.ps</span></strong></td></tr></tbody></table>

### Viewing PDF Content

Linux has many standard programs that can read PDF files, as well as many applications that can easily create them, including all available office suites, such as LibreOffice.

The most common Linux PDF readers are:

1. evince is available on virtually all distributions and is the most widely used program.
2. okular is based on the older kpdf and is available on any distribution that provides the KDE environment.

These open source PDF readers support and can read files following the PostScript standard. The proprietary Adobe Acrobat Reader, which was once widely used on Linux systems, is fortunately no longer available, as it did defective rendering and was unstable and poorly maintained.

![Adobe Acrobat Reader, Okular and Evince logo](https://courses.edx.org/assets/courseware/v1/c727cbca47c30e1108756b2d4152353d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_Screen_46.jpg)

### Manipulating PDFs

At times, you may want to merge, split, or rotate PDF files; not all of these operations can be achieved while using a PDF viewer. Some of these operations include:

* Merging/splitting/rotating PDF documents
* Repairing corrupted PDF pages
* Pulling single pages from a file
* Encrypting and decrypting PDF files
* Adding, updating, and exporting a PDF’s metadata
* Exporting bookmarks to a text file
* Filling out PDF forms.

In order to accomplish these tasks there are several programs available:

* qpdf
* pdftk
* ghostscript.

**qpdf** is widely available on Linux distributions and is very full-featured. **pdftk** was once very popular but depends on an obsolete unmaintained package (**libgcj**) and a number of distributions have dropped it; thus we recommend avoiding it. **Ghostscript** (often invoked using **gs**) is widely available and well-maintained. However, its usage is a little complex.

### Using qpdf

You can accomplish a wide variety of tasks using **qpdf** including:

<table border="1" width="100%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"></tr></tbody><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="40" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --empty --pages 1.pdf 2.pdf -- 12.pdf</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Merge the two documents&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>&nbsp;and<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">2.pdf</span></strong>. The output will be saved to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">12.pdf</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --empty --pages 1.pdf 1-2 -- new.pdf</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Write only pages 1 and 2 of&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>. The output will be saved to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">new.pdf</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --rotate=+90:1 1.pdf 1r.pdf</span></strong></span></p><p style="color: rgb(69, 69, 69); margin: 20px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --rotate=+90:1-z 1.pdf 1r-all.pdf</span></strong><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"></span></strong></span></p></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Rotate page 1 of&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">1.pdf</strong></span><span>&nbsp;</span>90 degrees clockwise and save to<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">1r.pdf</strong></span>.</p><p style="color: rgb(69, 69, 69); margin: 20px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Rotate all pages of&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</strong></span><span>&nbsp;</span>90 degrees clockwise and save to&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">1r-all.pdf</strong></span></p></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span face="courier new, courier" style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">qpdf --encrypt mypw mypw 128 -- public.pdf private.pdf</strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Encrypt with 128 bits&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">public.pdf</strong></span>&nbsp;using as the passwd<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">mypw</strong></span><span>&nbsp;</span>with output as<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">private.pdf</strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span face="courier new, courier" style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">qpdf --decrypt --password=mypw private.pdf file-decrypted.pdf</strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Decrypt<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">private.pdf</strong></span><span>&nbsp;</span>with output as<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">file-decrypted.pdf</strong></span>.</td></tr></tbody></table>

![Using qpdf to crypt/decrypt files](https://courses.edx.org/assets/courseware/v1/8741f9a6b933b1a95e363a20c73d3c77/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/qpdfcrypt.png)
_Using qpdf to Crypt/Decrypt Files_

### Video: Using qpdf

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000400_DTH.mp4">

Sorry, your browser doesn't support embedded videos.
</video>

### Using pdftk

**pdftk** has now been ported to Java! Marc Vinyals has developed and maintained a port to Java for **pdftk** which can be found [here](https://gitlab.com/pdftk-java/pdftk), together with instructions for installation. Some distributions such as Ubuntu, may install this version only.

You can accomplish a wide variety of tasks using **pdftk** including:

<table border="1" width="100%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"></tr></tbody><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Command</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Usage</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftk 1.pdf 2.pdf cat output 12.pdf</span></strong></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Merge the two documents<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong><span>&nbsp;</span>and<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">2.pdf</span></strong>. The output will be saved to<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">12.pdf</span></strong>.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftk A=1.pdf cat A1-2 output new.pdf</span></strong></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Write only pages 1 and 2 of&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>. The output will be saved to&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">new.pdf</span></strong>.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftk A=1.pdf cat A1-endright output new.pdfabc</span></strong></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Rotate all pages of&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>&nbsp;90 degrees clockwise and save result in&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">new.pdf</span></strong>.</span></td></tr></tbody></table>

### Encrypting PDF Files with pdftk

If you’re working with PDF files that contain confidential information and you want to ensure that only certain people can view the PDF file, you can apply a password to it using the **user_pw** option. One can do this by issuing a command such as:

**$ pdftk public.pdf output private.pdf user_pw PROMPT**

When you run this command, you will receive a prompt to set the required password, which can have a maximum of 32 characters. A new file, **private.pdf**, will be created with the identical content as **public.pdf**, but anyone will need to type the password to be able to view it.

![Screenshot showing encrypted PDF file](https://courses.edx.org/assets/courseware/v1/36d90570d210656beea8e67715021db3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pdfencryptsuse.png)
_Encrypted PDF File_

### Using Ghostscript

Ghostscript is widely available as an interpreter for the Postscript and PDF languages. The executable program associated with it is abbreviated to gs.

![Ghostscript logo](https://courses.edx.org/assets/courseware/v1/6d510a9766cd8587516cf87cf5edf2c1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/500px-Ghostscript.svg.png)

This utility can do most of the operations pdftk can, as well as many others; see man gs for details. Use is somewhat complicated by the rather long nature of the options. For example:

* Combine three PDF files into one:

**$ gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite  -sOutputFile=all.pdf file1.pdf file2.pdf file3.pdf**

* Split pages 10 to 20 out of a PDF file:

**$ gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dDOPDFMARKS=false -dFirstPage=10 -dLastPage=20\**  
**-sOutputFile=split.pdf file.pdf**

### Using Additional Tools

You can use other tools to work with PDF files, such as:

* **pdfinfo**   
It can extract information about PDF files, especially when the files are very large or when a graphical interface is not available.
* **flpsed**   
It can add data to a PostScript document. This tool is specifically useful for filling in forms or adding short comments into the document.
* **pdfmod**   
It is a simple application that provides a graphical interface for modifying PDF documents. Using this tool, you can reorder, rotate, and remove pages; export images from a document; edit the title, subject, and author; add keywords; and combine documents using drag-and-drop action.

For example, to collect the details of a document, you can use the following command:  
  
**$ pdfinfo /usr/share/doc/readme.pdf**

![Using Additional Tools: pdfinfo, flpsed, pdfmod](https://courses.edx.org/assets/courseware/v1/5c4cda1c771ca4c7a29e6bb1d4a3d5ea/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_Screen_53.jpg)
_Using Additional Tools: pdfinfo, flpsed, pdfmod_

## Chapter Summary

You have completed Chapter 17. Let’s summarize the key concepts covered:

* CUPS provides two command-line interfaces: the System V and BSD.
* The CUPS interface is available at [http://localhost:631](http://localhost:631/).
* **lp** and **lpr** are used to submit a document to CUPS directly from the command line.
* **lpoptions** can be used to set printer options and defaults.
* PostScript effectively manages scaling of fonts and vector graphics to provide quality prints.
* **enscript** is used to convert a text file to PostScript and other formats.
* Portable Document Format (PDF) is the standard format used to exchange documents while ensuring a certain level of consistency in the way the documents are viewed.
* **pdftk** joins and splits PDFs; pulls single pages from a file; encrypts and decrypts PDF files; adds, updates, and exports a PDF’s metadata; exports bookmarks to a text file; adds or removes attachments to a PDF; fixes a damaged PDF; and fills out PDF forms.
* **pdfinfo** can extract information about PDF documents.
* **flpsed** can add data to a PostScript document.
* **pdfmod** is a simple application with a graphical interface that you can use to modify PDF documents.

![Tux the Penguin wearing the square academic cap](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## PART TWO

This article has a part 2. We couldn't fit the entire thing in one article. 

Read the second part here: [https://www.freecodecamp.org/news/introduction-to-linux-part-2/](https://www.freecodecamp.org/news/introduction-to-linux-part-2/)

