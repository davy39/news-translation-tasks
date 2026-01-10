---
title: How to Dual Boot Windows 10 and Ubuntu – Linux Dual Booting Tutorial
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-24T20:09:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-dual-boot-windows-10-and-ubuntu-linux-dual-booting-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/dualBoot--1-.png
tags:
- name: Linux
  slug: linux
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "You don’t have to have two different computers to use Linux and Windows\
  \ 10. It's possible to have a Linux distro installed on a computer with Windows\
  \ 10 preinstalled. \nIn this article, I will show you how to dual boot Windows 10\
  \ and the popular Ubunt..."
---

You don’t have to have two different computers to use Linux and Windows 10. It's possible to have a Linux distro installed on a computer with Windows 10 preinstalled. 

In this article, I will show you how to dual boot Windows 10 and the popular Ubuntu Linux distro. But before that, you have to install Ubuntu on your Windows 10 PC.

Before you go through this process, you must backup your files. That’s because installing an OS is a risky process. Sometimes it can overwrite the existing OS and delete all your files.

**N.B.**: Most of the processes in this article take time to get done, so you need to be patient.

## What We’ll Cover – A step-by-step Guide to Dual-Booting Windows 10 and Linux
- [Prerequisites](#heading-prerequisites) 
- [How to Partition your Hard Drive for Ubuntu](#heading-how-to-partition-your-hard-drive-for-ubuntu)
- [How to Optimize your Hard Drive for More Partition Space (Optional)](#heading-how-to-optimize-your-hard-drive-for-more-partition-space-optional)
- [How to Download Ubuntu in ISO Image Format](#heading-how-to-download-ubuntu-in-iso-image-format)
- [How to Make an Ubuntu (Linux) Bootable USB Drive](#heading-how-to-make-an-ubuntu-linux-bootable-usb-drive) 
- [How to Install Ubuntu Linux Distro along with Windows 10](#heading-how-to-install-ubuntu-linux-distro-along-with-windows-10)
- [Now You Can Dual Boot Ubuntu and Windows 10](#heading-now-you-can-dual-boot-ubuntu-and-windows-10)
- [Conclusion](#heading-conclusion)

## Prerequisites
Most importantly, there are some things you must have in place if you want to use (and dual boot) Ubuntu and Windows 10 on the same PC:

- A computer preinstalled with Windows 10
- A partitioned hard drive 
- A BIOS in UEFI mode (Unified Extensible Firmware Interface)
- An empty USB drive of at least 4Gig for creating a bootable disk
- An internet connection to download Ubuntu ISO image (the Linux distro) and Rufus (a bootable drive creation tool)

## How to Check If Your PC BIOS is in UEFI Mode
To check if your PC BIOS comes in UEFI mode, search for “system information” and hit `ENTER`.
![ss1-5](https://www.freecodecamp.org/news/content/images/2022/08/ss1-5.png) 

Look under BIOS mode to confirm that your PC BIOS mode comes as UEFI.
![ss2-5](https://www.freecodecamp.org/news/content/images/2022/08/ss2-5.png)

If your PC BIOS is not in UEFI mode, the two operating systems won’t see each other. You can learn more about the [difference between these two modes here](https://www.freecodecamp.org/news/uefi-vs-bios/).

## How to Partition your Hard Drive for Ubuntu
You have to partition your hard drive because you must set aside at least 20Gig for Ubuntu to live in and boot from. 

**To partition your hard drive, follow the steps below**:

**Step 1**: Right-click on Start and select “Disk Management”.
![ss3-5](https://www.freecodecamp.org/news/content/images/2022/08/ss3-5.png) 

**Step 2**: Right-click on your C drive and select shrink volume.
![ss4-6](https://www.freecodecamp.org/news/content/images/2022/08/ss4-6.png) 

**Step 3**: Select at least (20000) 20Gig for Ubuntu and click “Shrink”. IT can take some time to complete, so be patient.
![ss5-6](https://www.freecodecamp.org/news/content/images/2022/08/ss5-6.png) 

**Step 4** (optional): You can go ahead and assign a letter to the new volume. Right-click on the unallocated space and select “New Simple Volume”.
![ss6-5](https://www.freecodecamp.org/news/content/images/2022/08/ss6-5.png) 

**Step 5**: Follow the wizard and assign a letter to the drive, then follow the rest of it.
![ss7-4](https://www.freecodecamp.org/news/content/images/2022/08/ss7-4.png) 

After completing the wizard, the drive should be listed on your computer.
![ss8-4](https://www.freecodecamp.org/news/content/images/2022/08/ss8-4.png) 

Congrats! You’ve successfully partitioned your hard drive. 

**N.B.**: If you have a lot of free space in your hard drive but your PC still didn’t give you up to 20Gig partition space, then you need to optimize your PC’s hard drive. Proceed to the next section of this article to do that.


## How to Optimize your Hard Drive for More Partition Space (Optional)

The common purpose of hard disk optimization is to speed up your computer during boot time and make it run smoother. 

At the same time, the process will defragment the hard disk and make free space more available for partitioning.

To optimize your hard drive, click Start (Windows logo key), search for “defrag” and select “Defragment and Optimize Drives”.
![ss9-3](https://www.freecodecamp.org/news/content/images/2022/08/ss9-3.png)

Make sure your C drive is highlighted, then click “Optimize”.
![ss10-3](https://www.freecodecamp.org/news/content/images/2022/08/ss10-3.png) 

After you’ve been able to set aside at least 20Gig for Ubuntu by partitioning your hard drive, then it’s time to download Ubuntu and make a bootable USB.

## How to Download Ubuntu in ISO Image Format
The next thing is to download Ubuntu in ISO image format so you can install Ubuntu. You can download it from the Ubuntu distro website.
![ss11-3](https://www.freecodecamp.org/news/content/images/2022/08/ss11-3.png) 

After downloading Ubuntu, don’t do anything with it yet. You need to make a bootable USB and put it in there. That’s how you’ll be able to use it. 

The reason you can’t install Ubuntu just like that is that it doesn’t come as an executable. It comes in form of ISO (optical disk image). That means you have to find a disk to put it in before it can work.

The next part of this guide shows how you can put the downloaded Ubuntu ISO on a USB stick.

## How to Make an Ubuntu (Linux) Bootable USB Drive 

You won’t be able to make a bootable USB drive for Ubuntu by just placing the downloaded ISO image in it. Follow these steps to get it done:

**Step 1**: You need to download a bootable USB drive creation tool like Rufus. You can [download Rufus from their website](https://rufus.ie/en/).
![ss12-3](https://www.freecodecamp.org/news/content/images/2022/08/ss12-3.png) 

**Step 2**: Insert the empty USB drive into your Windows 10 PC. Right-click on Rufus and select “Open”.
![ss13-1](https://www.freecodecamp.org/news/content/images/2022/08/ss13-1.png) 

**Step 3**: Under “Device”, select your USB drive. And under “Boot selection”, click the “Select” button and select the Ubuntu ISO file you downloaded 

**Step 4**: Leave every other thing as default and click the “START” button to start burning the Ubuntu distro to the drive.
![ss14-1](https://www.freecodecamp.org/news/content/images/2022/08/ss14-1.png) 

**Step 5**: Click OK to start the process.
![ss15-1](https://www.freecodecamp.org/news/content/images/2022/08/ss15-1.png) 
![ss16-1](https://www.freecodecamp.org/news/content/images/2022/08/ss16-1.png)

Once the process is done, you should see “READY” on a green background. Click the Close button. Its time to install Ubuntu.

Congrats! Now you have a bootable drive with which you can install Linux.

The next step is to install the Ubuntu distro on your Windows 10 PC. To do this, you have to boot your PC from the bootable USB drive you created.

## How to Install Ubuntu Linux Distro along with Windows 10
**Step 1**: Ensure the bootable drive is inserted into your Windows 10 PC

**Step 2**: Right-click on Start, hold SHIFT, and select Restart.
![ss18-3](https://www.freecodecamp.org/news/content/images/2022/08/ss18-3.png)

**Step 2**: Select “Use a Device”.
![1-use-a-device-1](https://www.freecodecamp.org/news/content/images/2022/08/1-use-a-device-1.jpg)

**Step 3**: On the next screen, you should see several devices you can boot from. 

You may see the bootable drive as the name of the USB brand. 
![disk-1](https://www.freecodecamp.org/news/content/images/2022/08/disk-1.jpg)

It’s possible to see it as “Ubuntu” too. Some other times, you might not see it, so you need to click on “See more devices".

If you still cannot see your bootable drive, head over to your boot menu by getting into BIOS. You will see it there.

**N.B.**: You should be very careful while making changes in BIOS. Whatever you do there has a lasting effect on your computer. If you are not sure of what you're doing there, you should contact an IT professional.

**Step 4**: Choose "Install Ubuntu". You can also try it before installing it.
![3-select-install-ubuntu](https://www.freecodecamp.org/news/content/images/2022/08/3-select-install-ubuntu.jpg)

Follow other prompts of the installation wizard and make sure you don’t replace your Windows 10 OS installation with Ubuntu. This is why I suggested you back up all your files.

When you get to the point to select the partition you made, scroll to [the partition you made earlier](#heading-how-to-partition-your-hard-drive-for-ubuntu) and press `ENTER`.
![1-1-select-disk](https://www.freecodecamp.org/news/content/images/2022/08/1-1-select-disk.jpg)

Click OK to select all the space in the partition. 
![1-2-select-disk](https://www.freecodecamp.org/news/content/images/2022/08/1-2-select-disk.jpg)

This time around, the “Install now” button will not be greyed out anymore. 
![1-3-select-disk](https://www.freecodecamp.org/news/content/images/2022/08/1-3-select-disk.jpg)

Follow other prompts until Ubuntu starts installing.

After the installation is done, Ubuntu will prompt you to remove the bootable drive and press `ENTER` to reboot your Computer.


## Now You Can Dual Boot Ubuntu and Windows 10
Immediately after you reboot the computer, you should see a screen that looks as shown below:
![Snapchat-2063128211](https://www.freecodecamp.org/news/content/images/2022/08/Snapchat-2063128211.jpg) 

Now, you can select which one to boot into between Ubuntu and Windows 10. 

To boot into Ubuntu, select Ubuntu. And to boot into Windows 10, select Windows boot manager.

You can also get into your BIOS from the same place by choosing UEFI Firmware Settings.
![Snapchat-778941832](https://www.freecodecamp.org/news/content/images/2022/08/Snapchat-778941832.jpg) 

## Conclusion
I hope this article helps you dual boot Ubuntu and Windows 10 on your computer.

The ultimate aim of this article was to show you how to dual boot Ubuntu and Windows 10. 

But the article went beyond that to show you how to:
- check if your PC’s BIOS is in UEFI mode 
- partition your hard drive
- optimize your hard drive
- make a bootable USB drive 
- install Ubuntu Linux Distro along with Windows on your Windows 10 PC.

If you find this article helpful, kindly share it with your friends and family.


