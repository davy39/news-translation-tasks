---
title: How to Dual Boot Any Linux Distribution With Windows – and Get Rid of It When
  You Need To
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2021-12-23T16:32:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-dual-boot-any-linux-distribution-with-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/How-to-Dual-Boot-Any-Linux-Distribution-With-Windows.png
tags:
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
- name: Windows
  slug: windows
seo_title: null
seo_desc: Gone are the days when Linux and Windows were like two opposing forces.
  Microsoft has embraced the open-source community quite cordially in recent years,
  and as a result we have things like Windows Subsystem for Linux baked right into
  our Windows ins...
---

Gone are the days when Linux and Windows were like two opposing forces. Microsoft has embraced the open-source community quite cordially in recent years, and as a result we have things like [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) baked right into our Windows installations.

That doesn't mean that we no longer need a full blown Linux installation. In fact, machines with both Windows and Linux running side by side are quite common.

But do you know what's more common than machines running both operating systems? Machine owners who have tried to dual boot their machines and ended up losing a lot of data in the process.

So if you're one of the victims or one of those who are trying to avoid possible disasters in their upcoming dual booting adventure, this article is for you. Here you'll learn about:

* How to install any Linux distribution alongside Windows
* How to get rid of Linux without messing up Windows if necessary
* Common problems, misconceptions, and their solutions, and
* Some generally geeky stuff to impress you peers

Without any further ado, let's grab a mug of coffee or tea or at least water and jump right into the process.

## Some Assumptions I’m Making

Before I jump into the core of the tutorial, I want to clarify a few things. To make this entire article approachable, I'm making following assumptions about your system:

* Your computer is using UEFI and not BIOS
* You already have Windows installed on your machine
* You have a USB drive large enough (4GB) to boot Linux from
* You have enough space (25GB) to install Linux on your HDD or SSD

That's pretty much it. If you have all of the above ready, you're good to go.

## How to Create a Bootable Linux USB Drive

There are multiple tools that can help you to create a bootable Linux USB drive. Among all these tools, my favorites are:

* [balenaEtcher](https://www.balena.io/etcher/)
* [Fedora Media Writer](https://getfedora.org/en/workstation/download/)

Both of these tools are open-source, free to use, and available on pretty much all major platforms. For this article, I'll go with Fedora Media Writer simply because there are not a lot of tutorials talking about it and because I use it personally.

Like the name suggests, Fedora Media Writer is a tool created by Red Hat for making bootable Linux USBs. Once you've downloaded the program, install it on your system and fire it up.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/fedora-media-writer.png)

This is how it looks. As you can see, you've got the option to download the latest Fedora ISOs as well as an option to pick a custom image file from your drives.

Unless you're planning on installing Fedora (spoiler! it's my favorite) on your machine, you'll have to go ahead and download your desired ISO file. 

In this article, I'll use [Ubuntu](https://ubuntu.com/) because it's more popular among newcomers. But the things you'll learn here can be applied to any other Linux distribution.

Go ahead and download the ISO for Ubuntu from their [download](https://ubuntu.com/download/desktop) page. Ubuntu 20.04 LTS (the latest long term release at the time of writing) is around 2.67GB in size. Once you've finished downloading the file, go back to Fedora Media Writer, click on "Custom Image", and select the ISO file you've just downloaded.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/fmw-ready-to-write.png)

The "Write to Disk" button is grayed out because there are no USB drives attached to the computer. Connect your USB drive and the button should turn bright red.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/fmw-ready-to-write-with-usb-drive.png)

Recheck that the correct USB drive is selected in the dropdown and hit the "Write to Disk" button. Depending on your machine's transfer rate, this process may take a few minutes. Once it's done, disconnect the USB drive and set it aside. You'll need it soon.

## How to Prepare Your Computer for Installing Linux

Again, it's not uncommon to find people who have failed to boot from a Linux USB drive. This can happen if you haven't configured your computer properly. 

To do so, go to your Control Panel. Not the new Settings application, but the OG Control Panel.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/control-panel-1.png)

Make sure Control Panel is either on "Small icons" or "Large icons" mode and not on the "Category mode". Now go to "Power Options" and from the left side-bar, click on "Choose what the power buttons do".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/turn-off-fast-startup.png)

Click on the Change settings that are currently unavailable link and uncheck the "Turn on fast startup (recommended)" option and hit "Save changes". 

According to Walter Glenn's [article](https://www.howtogeek.com/243901/the-pros-and-cons-of-windows-10s-fast-startup-mode/),

> Fast Startup combines elements of a cold shutdown and the hibernate feature. When you shut down your computer with Fast Startup enabled, Windows closes all applications and logs off all users, just as in a normal cold shutdown.   
>   
> At this point, Windows is in a state very similar to when it’s freshly booted up: No users have logged in and started programs, but the Windows kernel is loaded and the system session is running.   
>   
> Windows then alerts device drivers that support it to prepare for hibernation, saves the current system state to the hibernation file, and turns off the computer.  
>   
> When you start the computer again, Windows does not have to reload the kernel, drivers, and system state individually. Instead, it just refreshes your RAM with the loaded image from the hibernation file and delivers you to the login screen. This technique can shave considerable time off your start up.

I know this sounds like a nice to have feature, but the problem is, if you keep fast startup enabled in a dual boot system, Linux will be unable to use any of the drives shared between the two operating systems because they're hibernated and held by Windows.

Next, boot into your motherboard's UEFI configuration screen. Depending on your motherboard or laptop brand, the key can change but in most cases pressing the "Del" key should get you in.

Once you're there, you'll have to change one setting in particular:

* **Turn off secure boot** – this is one of the features of UEFI that helps prevent attacks and malware during boot. Disabling it is not strictly necessary but depending on the distribution you've chosen you may or may not face issues during installation. Disable it to be safe.

Save the updated settings and boot back to Windows. Now it's time to prepare some disk space for Linux to fit into.

## How to Create Additional Partitions for Installing Linux

Now it's time to make some room for the new OS. Based on the state of your HDD or SSD, it can either be very straightforward or quite tricky. 

Let me explain what we're going to do. There is a utility built into Windows called "Disk Management" that's useful when you want to mess around with your partitions.

You can use this to squeeze out some space out of your existing partitions. To do so, open Disk Management by searching for it in the start menu.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-in-start-menu.png)

Keep in mind that it may pop up as "Create and format hard disk partitions" instead of Disk Management. Fire it up and have a good look at its user interface:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management.jpg)

This screenshot is from one of my machines that doesn't have Linux installed. I'll use this device as the guinea pig for this article. It has a 512GB NVME SSD and 8GB of RAM. 

The user interface is divided into two parts. The top one is a list of all your partitions and the bottom part has all the physical disks connected to your computer listed vertically.

The below screenshot is from my desktop workstation that has a 250GB NVME SSD and a 1TB HDD. I have both Windows and Linux installed on the second disk. So if you have multiple disks on your machine as well, I would suggest you install the OS on the disk that contains the EFI partition. 

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-desktop.jpg)

If you look at the beginning of Disk 1, that 550MB FAT32 partition is the EFI. On your machine, it may be much smaller.

Let's get back to our guinea pig device. As you can see from the screenshot, the Windows (C:) partition is almost 250GB. I'll cut off 108GB from this partition.

* 100GB for root
* 8GB for swap

In Linux, the root directory contains all other directories and files on the system. When your RAM gets full, Linux moves the inactive pages from memory to the swap space. Having a swap space is not mandatory but it's good to have.

There is no hard and fast rule for determining the swap space. The recommended size for swap when you have a 4GB-8GB RAM is 2 times that size, and for 8GB-16GB is 1.5 times that size. Considering I don't do any memory intensive tasks on this laptop, I will break the rule here.

To cut off some space from your desired partition, right click on it from the bottom part and click on "Shrink". Once you do that, Disk Management will start calculating the amount available for shrinking.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/querying-for-available-space.jpg)

You may think that the entire free space of a partition should be shrinkable, but that's not true. Sometimes there are unmovable files scattered around your partition that may prevent you from using the full free space. In those cases, use a tool like [Defraggler](https://www.ccleaner.com/defraggler) to optimize your drive.

After Disk Management has finished querying the partition, you'll see the following window:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/shrink-window.jpg)

As you can see, I have 160311MB of space available to shrink. Dividing the value by 1024 will give you the size in gigabytes which in my case is around 156GB.

But I want to shrink my partition by 108GB. Multiplying this value by 1024 gives the value in megabytes of 110592MB.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/calculate-shrink-amount.jpg)

Once you have your desired size calculated, hit the "Shrink" button. The shrinking process doesn't take that long. Once the process is done the bottom part of the user interface will update.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-after-shrink.jpg)

As you can see, I now have 108GB of unallocated space. To be honest, this is enough for proceeding to the next step. But to make your life easier, I would suggest that you create two RAW partitions before going forward.

To do so, right click on the unallocated space and click on the "New Simple Volume" option. A new wizard window will show up. Press the "Next" button and on the next step, the wizard will ask about the new partition's size:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-creation-size.jpg)

I want to create the 100GB root partition. Multiplying that value by 1024 gives the value in megabytes which is 102400MB. Once you have the size calculated, hit "Next".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-creation-drive-letter.jpg)

In the next step, the wizard will ask you about the drive letter. Choose "Do not assign a drive letter or drive path" and hit "Next".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-creation-format.jpg)

In this step, select the "Do not format this volume" option and hit "Next". Finally hit finish on the last step. Follow the same process for creating your swap partition.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-after-creating-partitions.jpg)

I now have a 100GB RAW partition for the Linux root and a 8GB RAW partition for swap. Close the disk management tool and grab another mug of coffee or tea or at least water because we're going deeper into the rabbit hole.

## How to Install Linux Alongside Windows

Okay everyone, it's getting real now. We're going to do it. But first, you'll have to figure out which key to use to get into your boot menu.

On the device I'm using, pressing the F2 button takes me to the UEFI configuration screen. From there, pressing F8 takes me to the boot menu. So make sure you've done the research for your device.

Some tutorials may instruct you to change the boot order from your UEFI configuration screen, but I don't recommend doing that. The SSD or HDD that contains your bootloader should always be on the top.

Now connect the bootable USB device that you set aside on the first section and reboot your computer into the boot menu. From the boot menu, select the bootable USB drive and hit enter.

The GNU GRUB menu will appear. Pick the first one that says "Ubuntu". Wait until the file integrity check finishes or you can just skip it by hitting "Ctrl + C" on your keyboard.

You'll hear a beautiful chime and with that, the majestic Ubuntu installer will show up:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ubuntu-installer-1.png)

Before you hit the "Continue" button, I would suggest that you get connected to the internet. If you're using an ethernet cable then you should be connected already. But if you're using wireless, then check the top right corner of your screen for the Wifi icon:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/wifi.png)

Once you're connected, hit the "Continue" button on the installer:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/keyboard-layout.png)

Pick the correct keyboard layout for yourself and hit "Continue".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/updates-and-other-software.png)

The "Normal installation" will give you a bunch of useful software and games from the get go, whereas the "Minimal installation" will give you the essentials only.

Keep the "Download updates while installing Ubuntu" option checked. This will download updated package files from the internet during installation.

The third option needs some explanation. Assume that you're using an NVIDIA GPU. When Ubuntu detects that GPU, Ubuntu will load the open-source drivers for NVIDIA GPUs known as "nouveau". 

If you check the "Install third-party software for graphics and Wi-Fi hardware and additional media formats" option, NVIDIA will attempt to install proprietary drivers provided by NVIDIA itself. It'll also install codecs for proprietary media formats such as MPEG. 

This device I'm using has an AMD GPU and uses the open-source "amdgpu" driver. I'll leave this unchecked considering I can install the codecs as necessary by myself. Do what you prefer and hit the "Continue" button.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/installation-type.png)

Okay this step needs attention. The Ubuntu installer is smart enough to detect whether you have other OSes installed on your machine or not. If yes, the installer will offer you the option to install Ubuntu alongside them. Don't pick that option. I repeat, **don't pick that option**.

Choose "Something else" and hit the "Continue" button.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-map.png)

This part can be a bit tricky. This is why I instructed you to create the partition from Windows instead of leaving the space unallocated. If you had left it unallocated, figuring out which part of the disk you should use would have become much more difficult.

At the top you can see a multi-colored line along with legends for which color represents which partition. Find out the two partitions you created from Windows.

In my machine, "nvme0n1p4" and "nvme0n1p5" are the ones. Now from the list, find the one you created for the root (nvme0n1p4 in my case) and double click on it:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/edit-partition.png)

Choose "Ext4 journaling file system" from the "Use as" dropdown and "/" as the "Mount point" dropdown. According to the [The Linux Information Project](http://www.linfo.org/mount_point.html):

> A mount point is a directory (typically an empty one) in the currently accessible [filesystem](http://www.linfo.org/filesystem.html) on which an additional filesystem is mounted (i.e., logically attached).

Hit the "OK" button. Next double click on the partition you created for the swap space:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/swap-partition.png)

Choose "swap area" from the "Use as" dropdown menu and hit the "OK" button. There is one more partition to configure. That is the EFI partition. Scroll through the list and find the FAT32 partition.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/efi-partition.png)

On my machine, the "nvme0n1p1" is the EFI partition. Double click on it:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/use-as-efi.png)

Make sure "EFI System Partition" is selected from the "Use as" dropdown menu. This is the partition that'll contain your bootloader. Make sure you're not formatting this partition. Hit the "OK" button.

Also, the default mount point for the EFI partition is "/boot/efi". Some distributions like Fedora will require you to write this mount point manually. So make sure you're putting the correct mount point.

Recheck the partition configuration once again and if everything looks fine, hit the "Install Now" button.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/where-are-you.png)

The installer will ask you about your time zone. I live in Dhaka, Bangladesh so that's what I've chosen. Hit the "Continue" button.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/who-are-you-1.png)

Fill out all the information as you see fit and hit the "Continue" button.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/welcome-to-ubuntu.png)

The installation process shouldn't take long. Back when I was a kid, I loved looking at this slideshow.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/restart-now.png)

Once the installation is done you can either continue testing or restart. If you choose to restart, Ubuntu will instruct you to disconnect the USB drive and hit Enter.

The machine will reboot and the GRUB menu will show up again. Take a look at the list, and you'll see both Ubuntu and Windows Boot Manager on the menu. Boot into Ubuntu because you have one last thing to do.

## How to Sync the Time Between Windows and Linux

This is one of the common problems that people with a dual boot system face. When you boot into Windows and then boot into Linux, you'll find Linux's clock all messed up. The same thing will happen if you first boot into Linux and then boot into Windows.

Let me explain why this happens. Your computer (or rather every computer in the world) has two clocks. One is the system clock that lives within the OS, and the other is the hardware clock that lives in your motherboard and keeps track of time even when your computer is not running.

The problem is that Windows assumes that your hardware clock is running in your local time and Linux assumes that your hardware clock is running in UTC time and applies an offset according to your location.

The easiest way to fix this issue is to make your Linux distribution use local time like Windows does. To do so, execute the following command in the Linux terminal:

```bash
timedatectl set-local-rtc 1 --adjust-system-clock
```

Now restart your computer into Windows, sync the system clock and go back to Linux. The time should not be messed up now.

## How to Remove Linux From a Dual Boot System

Say for some reason you didn't like your time with Linux and want to get rid of it. This would be sad, but life is hard, ain't it?

Removing Linux from a dual boot system is a two step process:

1. Getting rid of the GRUB bootloader
2. Getting rid of the Linux partitions

To get rid of the GRUB bootloader you'll have to remove the corresponding files from the EFI partition. The problem is that the partition is hidden by default. 

To make if accessible you'll have to use the `diskpart` program. It's a disk management utility like the Disk Management tool but it's a command line interface.

Boot into Windows. From the start menu, open Command Prompt as an administrator. To do so, just search for "cmd" in your start menu and when the Command Prompt shows up, press the "Ctrl + Shift + Enter" key combination.

Now write `diskpart` in the command prompt window and hit enter to start the program.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/diskpart.jpg)

Next, write `list disk` and hit enter to get a list of all the connected disks:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/list-disk.jpg)

This device has only one physical disk but you may have multiple. Write `sel disk <disk number>` to select the desired disk.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/sel-disk-0.jpg)

Then write `list vol` and press enter to list out all the partitions in this disk.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/list-vol.jpg)

Judging by the size and format, I can say that Volume 4 is the EFI partition. Keep in mind this can be much smaller on your system but it will be always a FAT32 partition. Write `sel vol <volume number>` to select the desired volume.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/sel-vol-4.jpg)

Finally write `assign letter x` and hit enter to assign the letter `x` to this partition.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/assign-letter-x.jpg)

Exit `diskpart` by writing `exit` and hitting enter:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/exit.jpg)

Now the partition has become accessible. From the same command prompt window, go inside the EFI partition by writing `x:` and hitting enter.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/x.jpg)

To get a list of all the folders in there, write `dir` and hit enter.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/dir.jpg)

Now write `cd EFI` to go inside that EFI folder and write `dir` once again to list out the contents.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/cd-efi.jpg)

You'll have to get rid of that `ubuntu` folder. To do so, write `rmdir /s ubuntu` and hit enter. Command prompt will ask you whether you're sure or not. Write `Y` and hit enter to confirm. Then use `dir` one last time to make sure it's gone.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/rmdir-dir.jpg)

That's it. Next, open Disk Management once again like you did before and from the bottom part, right click on the Linux oriented partitions and choose "Delete Volume" from the list.

After deleting the partitions, you can either create a new one using the unallocated space or extend the partition on the left of it to dissolve the unallocated space.

Finally reboot your computer and check whether the Ubuntu has gone away from your machine or not.

## What About Other Linux Distributions?

The techniques learned in this article is relevant for any Linux distributions out there.

So, whenever you're dual booting a system, make sure that

* Secure Boot is disabled
* Fast Startup is disabled

And during the installation

* Do not choose any guided/automatic installation type
* Make sure to not format the EFI/ESP partition
* Make sure to mount your partitions properly

As long as you're sticking to these few rules, you should be good to go. 

Just keep in mind that there are some rare cases when a distribution may not use GRUB as a bootloader.

Take the very popular "[Pop!_OS](https://pop.system76.com/)" for example. It uses "systemd-boot" as its default bootloader. As a result you'll have to keep pressing the Space button (or maybe any button on the keyboard) during startup, otherwise the boot menu won't show up and you'll boot into Pop!_OS directly.

Another thing that I've seen: some motherboards such as my MSI B450 Tomahawk Max, chooses the Windows Boot Manager by default even though I have a working Linux installation. If you see something like this, go into your UEFI configuration screen and look for relevant options.

## Conclusion

I would like to thank you from the bottom of my heart for the time you've spent reading this article. 

I also have a personal blog where I write about random tech stuff, so if you're interested in something like that, checkout [https://farhan.dev](https://farhan.dev). If you have any questions or are confused about anything – or just want to get in touch – I'm available on [Twitter](https://twitter.com/frhnhsin) and [LinkedIn](https://www.linkedin.com/in/farhanhasin/).

