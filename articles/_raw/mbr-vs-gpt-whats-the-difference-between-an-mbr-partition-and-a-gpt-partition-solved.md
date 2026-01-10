---
title: 'MBR vs GPT: What''s the Difference Between an MBR Partition and a GPT Partition?
  [Solved]'
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-12T04:12:00.000Z'
originalURL: https://freecodecamp.org/news/mbr-vs-gpt-whats-the-difference-between-an-mbr-partition-and-a-gpt-partition-solved
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9842740569d1a4ca190c.jpg
tags:
- name: hardware
  slug: hardware
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'If you''re building a PC, you might have been asked how you want to install
  your operating system – MBR or GPT?

  The differences between an MBR and GPT partition are pretty straightforward. But
  there''s a lot of background information that will help you...'
---

If you're building a PC, you might have been asked how you want to install your operating system – MBR or GPT?

The differences between an MBR and GPT partition are pretty straightforward. But there's a lot of background information that will help you get a clearer picture about each type of partition table, and when you should choose one over the other.

In this article we'll go into what a partition is, the difference between an MBR and GPT partition, whether you should upgrade from one type of partition to another, and more.

## What's a partition?

A partition is a virtual division of a hard disk drive (HDD) or solid state drive (SSD). Each partition can vary in size and typically serves a different function.

For example, in Windows there is usually a small recovery partition and a large file system partition labeled `C:`. The `C:` partition is what most people are familiar with, as it's where you usually install your programs and store your various files.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/disk-management.png)
_Windows Disk Manager – [Source](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/overview-of-disk-management)_

In Linux, there's typically a root partition (`/`), one for swap which helps with memory management, and large `/home` partition. The `/home` partition is similar to the `C:` partition in Windows in that it's where you install most of your programs and store files.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/yCyXA.png)
_GParted in Linux – [Source](https://bbs.archlinux.org/viewtopic.php?id=155698)_

If you bought your computer from a store and the operating system is already installed, then the manufacturer has already taken care of the partitions. You don't need to worry about them unless you want to do something like dual-boot Windows and Linux from the same HDD or SDD.

Even if you're installing the operating system yourself, most times the installer will suggest default partitions and partition sizes. Again, you usually don't need to make any adjustments.

Now that you have a high-level overview of what a partition is, we can dive into the differences between MBR and GPT partitions.

**Note:** I'll be using the term "drive" to refer to both HDDs and SSDs from now on.

## An overview of MBR and GPT partitions

Before a drive can be divided into individual partitions, it needs to be configured to use a specific partition scheme or table.

A partition table tells the operating system how the partitions and data on the drive are organized. For example, the screenshots above show the partition tables on the drive, and each individual partition is shown as a rectangular block.

There are two main types of partition tables: MBR and GPT.

MBR stands for Master Boot Record, and is a bit of reserved space at the beginning of the drive that contains the information about how the partitions are organized. The MBR also contains code to launch the operating system, and it's sometimes called the Boot Loader.

GPT is an abbreviation of GUID Partition Table, and is a newer standard that's slowly replacing MBR.

Unlike an MBR partition table, GPT stores the data about how all the partitions are organized and how to boot the OS throughout the drive. That way if one partition is erased or corrupted, it's still possible to boot and recover some of the data.

If you bought your computer within the last five years or so, it's very likely that it's using GPT partition tables rather than the older MBR tables.

## Differences between MBR vs GPT partitions

There are a number of differences between MBR and GPT partitions, but we'll cover some of the main ones here.

First, the maximum capacity of MBR partition tables is only about 2 terabytes. You can use a drive that's larger than 2 terabytes with MBR, but only the first 2 terabytes of the drive will be used. The rest of the storage on the drive will be wasted.

In contrast, GPT partition tables offer a maximum capacity of 9.7 zetabytes. 1 zetabyte is about 1 billion terabytes, so you're unlikely to run out of space anytime soon.

Next, MBR partition tables can have a maximum of 4 separate partitions. However, one of those partitions can be configured to be an _extended partition_, which is a partition that can be split up into an 23 additional partitions. So the absolute maximum number of partitions an MBR partition table can have is 26 partitions.

GPT partition tables allow for up to 128 separate partitions, which is more than enough for most real world applications.

As MBR is older, it's usually paired with older Legacy BIOS systems, while GPT is found on newer UEFI systems. This means that MBR partitions have better software and hardware compatibility, though GPT is starting to catch up.

We'll take a brief look at both Legacy BIOS and UEFI a bit later in the article.

## Should you upgrade from MBR to GPT?

If one of your drives is currently using an MBR partition table, you might be asking yourself if you should upgrade to the newer GPT standard.

In short, probably not. As the saying goes, if it ain't broke, don't fix it.

It's very easy to ruin the MBR sector of the drive, making it impossible to boot up again. Then you'll either need to create a recovery USB drive with Windows or Linux and try to repair the MBR, or completely wipe the drive and reinstall the operating system.

Speaking from experience, it's not worth the headache.

That said, there are some cases where you might consider upgrading from MBR to GPT.

For example, maybe you want to upgrade your drive to one that's greater than 2 terabytes, or you need more than 26 partitions. Even in these cases, you'll need to make sure that your hardware can even support a GPT partition table and a UEFI BIOS.

If you've done the research are positive you want to make the jump to GPT, make sure you have a backup of your drive and all important data. Worst case scenario, you'll be able to roll back without having to reinstall everything and start from scratch.

## An overview of BIOS

I've mentioned BIOS a few times before. While it's a bit outside the scope of this article, a basic understanding of BIOS is necessary to understand one of the last main differences between MBR and GPT partitions.

BIOS stands for Basic Input/Output System, and is the software that's stored on a chip on a computer's motherboard that runs when you first turn it on.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/xThDu5d.jpg)
_A BIOS chip on a Gigabyte motherboard – [Source](https://forums.tomshardware.com/threads/gigabyte-ab350-gaming-3-cpu-led-on-no-posting.3103246/)_

The BIOS does things like configure the keyboard, mouse, and other hardware, set the system clock, test the memory, and so on. Then it looks for a drive and loads the boot loader on the drive, which is either an MBR or GPT partition table.

Usually when you first turn on your computer you'll see a logo from either your computer or motherboard's manufacturer. 

Often there's a message below the logo saying which key to press to configure the computer's BIOS. This key is usually Delete, Escape, or F2, though it varies by manufacturer.

As mentioned previously, there are two main types of BIOS – Legacy BIOS and UEFI BIOS:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/windows-boot-screen-bios.jpg)
_A Legacy BIOS configuration screen – [Source](https://fossbytes.com/intel-end-legacy-bios-support-2020-uefi/)_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/29143-uefiasus.jpg)
_A UEFI BIOS Configuration screen – [Source](https://www.tested.com/tech/pcs/2894-what-you-should-know-about-uefi-and-windows-boot-times/)_

Legacy BIOS are older, and are entirely keyboard driven. They're usually simple in terms of UI, and have either a black or blue-screen-of-death background color.

UEFI stands for Unified Extensible Firmware Interface, and can be thought of as a newer type of BIOS. UEFI often includes graphics to show fan speed, temperature, and CPU clock speeds, and can sometimes be controlled with a mouse or trackpad.

## MBR and GPT BIOS

Because MBR is an older standard, it's paired with Legacy BIOS systems (and Legacy BIOS can only access drives with an MBR partition). This is not necessarily a bad thing, as support for Legacy BIOS is better.

But again, one of the most obvious limitations of MBR partitions is that it can only handle drives that are up to 2 terabytes.

The newer GPT standard is paired with UEFI BIOS systems. Though support for both GPT and UEFI BIOS is not as great as MBR/Legacy BIOS, it's gaining ground. 

More manufacturers are switching over to UEFI BIOS, which in turn requires drives to use the newer GPT format. But requirement for GPT formatted drives comes with the advantage of a much higher capacity and up to 128 partitions.

## In closing

While understanding the difference between MBR and GPT partitions is a bit like peeling an onion, hopefully you got through it without tearing up.

If all you want is a quick reference for the differences between MBR and GPT partitions, here's a handy table:

|   | MBR | GPT |
|---|:---:|:---:|
| Maximum capacity | 2TB | 9.7ZB (~9.7 billion terabytes) |
| Maximum partitions | 26 | 128 |
| Partition/boot data location | At the beginning of the drive | Throughout the drive |
| BIOS type | Legacy BIOS | UEFI |

And please, don't be like my younger self – make sure you have a backup before you mess around with your partitions. Actually, make two backups.

