---
title: How to Install Kali Linux on Your Computer
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2022-09-15T19:37:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-kali-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/install-kali-linux-article-image.png
tags:
- name: kali
  slug: kali
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Kali Linux (formerly known as BackTrack) is an open-source Linux distro\
  \ developed and funded by Offensive Security. \nIt’s basically an ethical hacker's\
  \ dream operating system, because it has most of the tools you'll ever need built-in.\
  \ From Metasploi..."
---

Kali Linux (formerly known as BackTrack) is an open-source Linux distro developed and funded by Offensive Security. 

It’s basically an ethical hacker's dream operating system, because it has most of the tools you'll ever need built-in. From Metasploit to JohntheRipper to the one and only Aircrack-ng, this OS has it all. 

But enough of the history lesson. Let’s jump right in and learn how to install Kali Linux on your computer.

# Requirements

Before we carry on, you should know that this is the process for installing on the bare system itself and you should do this with extreme caution. 

If you wish to dual boot your machine, you will need to partition your hard drive to give Kali at least 20 GB of hard disk space and then install it on that partition.

Now you are going to need some ingredients for this masterpiece:

1. A Computer (Minimum Requirements: 20GB Hard Disk space, 2GB RAM, Intel Core i3 or AMD E1 equivalent)
2. A USB stick (6 GB or more)
3. A Kali .iso file
4. Rufus (To create a bootable drive)
5. A really cool head (Trust me, you’ll need it 🥶)

# How to Install Kali Linux on Your Computer – Step by Step

### Step 1: Download the iso file

Go to kali.org and hit the download button.

![The Kali Homepage](https://miro.medium.com/max/1400/1*MTx3vLNW5O0Gy_0EFUO1YA.png)
_The Kali Homepage | Credit: kali.org_

What you're trying to get is an iso file, which is just a way of packaging software. Operating systems are usually packed like this (but also malicious software, so be careful where you get them💀).

Here you are given a lot of options, but go for the ‘Bare Metal’. There are options for 64-bit, 32-bit, and Apple M1 here (though I have no clue why the last one exists). Choose the tab applicable to your system, and download the Installer. For torrent lovers, the torrent is also available.

![The Installer option](https://miro.medium.com/max/1400/1*KVktfnfGlFhxwq48ZFDG7Q.png)
_The Installer option | Credit: kali.org_

### Step 2: Create a bootable drive

You can download Rufus from [rufus.ie](https://www.freecodecamp.org/news/p/6d73416e-2b28-475d-b6b2-7c5dc3964de9/rufus.ie) (Rufus 3.18 as at the time of writing). In order to make the stick bootable, we are going to run Rufus and make a few changes. 

Connect the stick and select it under the ‘Device’ options. Under ‘Boot selection’ select your newly downloaded Kali iso file. Now for the tricky part.

![The Rufus Software](https://miro.medium.com/max/948/1*PcHN4n41T7vT_ASJKg-gsw.png)
_The Rufus Software | Credit: Mercury_

Before we proceed, a quick lesson: a partition scheme/table is the format in which a hard disk saves data. Think of it like your video files saved in .mp4 or .mkv – they are both videos but different formats. 

Most computers have one of the following formats: GPT (GUID Partition Table) or MBR (Master Boot Record). You may not be able to boot your drive if you pick the wrong option here. 

Summary of it all: Pick the MBR option if the computer is old or using a legacy BIOS. Pick GPT if it is a newer computer and using a UEFI BIOS. If the drive doesn’t show up in the boot menu, change to the other option and try again.

You could also go to the advanced drive properties and check the box with ‘Add fixes for old BIOSes’. This should make the drive more compatible with your computer if it is a very old one. And by old, I mean ancient 👴.

![How to prepare the USB stick](https://miro.medium.com/max/1400/1*TD1nOvt2bDkjxmOek_DAJw.gif)
_How to prepare the USB stick | Credit: Mercury_

Back to easier ground now, you can leave the default format options. Hit the Start Button and wait for the image to be written to the stick (This takes some time so, relax 😌).

### Step 3: Access the Kali Installer Menu

To boot the computer from the new Kali USB stick, you’ll need to disable secure boot if it is enabled in the BIOS settings. 

You may need to do a little research into how to access your BIOS and boot menu. It usually involves spamming (continuously pressing) a key on your keyboard when the computer starts to boot. 

As mentioned before, if you are dual booting, take note of the partition size you made for Kali so you don’t overwrite your other OS (been there, done that 😢).

![A Legacy BIOS](https://miro.medium.com/max/1278/1*mDXhfALgd5keOGJ-EaqIRg.png)
_A Legacy BIOS | Credit: VMware_

After disabling secure boot, we can finally boot to the drive. At startup, you’ll have to access the boot menu and then choose the stick you just made. You should be welcomed with the Kali Installer Menu.

![The Kali Installer Menu](https://miro.medium.com/max/1280/1*jzUeRWajgAmI-fZDZHC__A.png)
_The Kali Installer Menu | Credit: Mercury_

Note: You can also edit the boot menu configuration in the BIOS menu, but that is permanent and may need to be changed post-installation. It is usually preferred to find a way to access the boot menu when starting up the computer, as this will only be a temporary configuration.

The installer menu only allows the keyboard for input so you’ll have to use the arrow keys, Enter, and Esc to navigate it.

### Step 4: Begin the installation

Select graphical install, and you can now use your mouse. Select your preferred language, region, and keyboard layout in the following menus:

![Language Menu](https://miro.medium.com/max/1400/1*NYEFJGMOfhqBxQXNB4T0sw.png)
_Language Menu | Credit: Mercury_

![Region Menu](https://miro.medium.com/max/1400/1*Mv9NdJx-fOQd-BWBKmI-0w.png)
_Region Menu | Credit: Mercury_

You computer will attempt to make some network configurations, but you can easily skip that as it won’t be needed for an offline install. 

Fill in a hostname as this will identify your computer on a public network. You can skip the domain name part as this isn’t necessary. Next, type in your full name for your new user account.

![Full Name setup](https://miro.medium.com/max/1400/1*lsyFOCMClUzHtprvS4l26g.png)
_Full Name setup | Credit: Mercury_

Quick lesson: On the terminal, Linux allows you to send and receive emails with commands. However, Gmail and Yahoo make sending a lot easier these days. You may never have to use this feature in your lifetime.

Next type, in the username for your account (This could be your hacker alias 😎).

![Username Setup](https://miro.medium.com/max/1400/1*_tBWjY1VXwNIap2D2ZxdEA.png)
_Username setup | Credit: Mercury_

Choose a strong password/passphrase to input in the next menu.

![Password setup](https://miro.medium.com/max/1400/1*oo1HJdHuJROqIFqTWQFyeA.png)
_Password setup | Credit: Mercury_

Select your time zone. This is important as it could affect your network configurations post-installation.

![Image](https://miro.medium.com/max/1400/1*tfQU397sBK6jqj4TD5ukWw.png)
_Time zone setup | Credit:_

### Step 5: Set up the storage

Next would be to select the partitioning method. Now for the cool head mentioned earlier. If you want to format the entire hard drive for Kali, the Guided options will be best. 

LVM (Logic Volume Management) is a feature that allows you to have relatively flexible partitions. This means that you can extend, shrink or even merge partitions while the OS is being run. It's a pretty nifty feature.

The encrypted LVM feature keeps your data safe if someone unauthorized gets access to your hard drive. Just note that there is a trade-off here: your hard drive will tend to be slower than if it wasn’t encrypted. So most people go with the ‘Guided -use entire disk’ option.

![Partitioning Method](https://miro.medium.com/max/1400/1*ar1ZHAmH9VaWZ8qmZ7qHHQ.png)
_Partitioning method setup | Credit: Mercury_

If you are dual-booting, though, you will need to choose the manual option and make the necessary configurations. I’ll go with the use entire disk option here.

Choose the hard drive you want to install Kali on. I’m using a virtual machine so my only option is a small 21 GB drive.

![Hard Disk selection](https://miro.medium.com/max/1400/1*tRfnHIpCEArhsD6qEFmgeg.png)
_Hard Disk selection | Credit: Mercury_

Choose how you want your files to be partitioned. Each option differs by separating certain important directories in separate partitions (More on that in a later post).

![Image](https://miro.medium.com/max/1400/1*zeEHKH-6fP37V1-N1Wkyug.png)
_Partitioning Scheme | Credit: Mercury_

Finish up the partitioning changes.

![Partitioning changes](https://miro.medium.com/max/1400/1*NykY9Az_TGa-CgJutaNSeA.png)
_Partition changes info | Credit: Mercury_

Select ‘Yes’ to write the changes to the disk.

![Partition verification](https://miro.medium.com/max/1400/1*OrAElo4Z8TWXZNneinBb3g.png)
_Partition Changes verification | Credit: Mercury_

### Step 5: Chose software and a desktop look

Now, choose the software you wish to install. Check the desktop environment and collection of tools options, as these will help you avoid having to install a lot of things later.

Desktop environments are basically the way the desktop looks to the user. Kali offers Xfce (most common), Gnome, and KDE. I’m a sucker for Gnome so I went with that option. You can still install all three and later configure your computer to choose the one you’d like.

![Software Installation Menu](https://miro.medium.com/max/1400/1*PriqVPIylnMw2y4jVttyZQ.png)
_Software Installation Menu | Credit: Mercury_

You can check the sixth box to install the top 10 most popular tools on Kali. These are:  
 1. [Aircrack-ng](https://en.wikipedia.org/wiki/Aircrack-ng)  
 2. [Burpsuite](https://portswigger.net/burp)  
 3. [Crackmapexec](https://mpgn.gitbook.io/crackmapexec/)  
 4. [Hydra](https://en.wikipedia.org/wiki/Hydra_(software))  
 5. [Johntheripper](https://en.wikipedia.org/wiki/John_the_Ripper) (jtr)  
 6. [Metasploit](https://en.wikipedia.org/wiki/Metasploit_Project)  
 7. [Nmap (Network Mapper)](https://en.wikipedia.org/wiki/Nmap)  
 8. [Responder](https://medium.com/mii-cybersec/gaining-credentials-easily-with-responder-tool-b821f33e342b)  
 9. [Sqlmap](https://sqlmap.org/)  
 10. [Wireshark](https://en.wikipedia.org/wiki/Wireshark)

As a hacker, you’re definitely going to need one of these sooner or later, so it’s best if you check that box. You can check the ‘default — recommended tools’ box if you want a whole bunch of tools on your system, but note that this will take a lot of time and space. Hit continue and wait.

Quick tip: It is generally recommended that you only have the tools you absolutely need on your computer. This is because additional tools could slow your computer down, you could waste data updating tools you never use, and you are likely to be more vulnerable if there is an active exploit on the loose.

### Step 6: Install the GRUB bootloader

The GRUB boot loader is a piece of software that allows you to pick which OS to boot from when the computer starts up. For both single boot readers and dual boot readers, the best option here is ‘Yes’.

![Grub Bootloader setup](https://miro.medium.com/max/1400/1*gv_rjUlcVZrlrdVPnXHilQ.png)
_Grub Bootloader setup | Credit: Mercury_

Select the your hard drive.

![Image](https://miro.medium.com/max/1400/1*b85vz6AEzj_whbr59CP50g.png)
_Grub Bootloader setup | Credit: Mercury_

Mission Accomplished 🎉🥂. You have successfully installed your Kali Linux OS. Hit continue to clean up and reboot your computer.

![Image](https://miro.medium.com/max/1400/1*H850ppmBcM7hX17PP_4asA.png)
_Grub Bootloader setup | Credit: Mercury_

Note: If you performed dual boot, you may need to change the boot menu to load Kali first before Windows so you have the option of choosing which OS to use.

Once booted up, your screen should be like the one below.

![Login screen](https://miro.medium.com/max/1400/1*tTWw2J3Vkuk-YmbMhpakQA.png)
_Login screen | Credit: Mercury_

If you installed the xfce desktop environment, you will have to put in your username, enter your password, and you should have a nice looking desktop.

![Kali desktop](https://miro.medium.com/max/1400/1*2UuoX7GI3gID0Ghekvt4OQ.png)
_Kali Linux Desktop | Credit: Mercury_

## Conclusion

Alright so let's do a quick recap of what we did:

1. Downloaded the iso file
2. Created a bootable drive
3. Accessed the Kali Installer Menu
4. Began the installation
5. Set up the Storage
6. Installed the GRUB bootloader

And finally, enjoy your new OS. Happy hacking! 🙃

### Helpful Resources

1. Kali website: [kali.org](http://kali.org)
2. You can read about the [difference between MBR and GPT in this freeCodeCamp article](https://www.freecodecamp.org/news/mbr-vs-gpt-whats-the-difference-between-an-mbr-partition-and-a-gpt-partition-solved/).
3. Here's an article from Kali Linux about [how to change your desktop environment](https://www.kali.org/docs/general-use/switching-desktop-environments/)

### Acknowledgements

Thanks to [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), and my family for the inspiration, support and knowledge used to put this article together. You’re the real MVPs.

