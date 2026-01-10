---
title: How to Run Android Games on Linux with Android-x86
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-08-17T16:09:12.000Z'
originalURL: https://freecodecamp.org/news/run-android-games-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/jose-article-photo.jpeg
tags:
- name: Android
  slug: android
- name: Games
  slug: games
- name: Linux
  slug: linux
- name: virtual machine
  slug: virtual-machine
seo_title: null
seo_desc: 'In this article, you''ll learn how you can use virtual machines on Linux
  while having fun with vintage games.

  If you have an Android phone, one of your guilty pleasures might be playing some
  very entertaining games. Or it could be that there is an app...'
---

In this article, you'll learn how you can use virtual machines on Linux while having fun with vintage games.

If you have an Android phone, one of your guilty pleasures might be playing some very entertaining games. Or it could be that there is an application that only runs on your phone.

And then you think – what if you could run the same games on your desktop PC?

To simplify the scenario, let's assume the applications run on Android.

One approach to solve your problem is to run an Android emulator on your PC. But some of them, like [Android-x86](https://www.android-x86.org/download.html), require rebooting your machine so they can take control of the hardware.

If you don't mind a small performance hit you can run a virtual machine at the same time as your native operating system. Specifically on Linux, there are several choices, like [QEMU](https://www.qemu.org/) and [VirtualBox](https://www.virtualbox.org/), to name a few.

By the end of this article you will be able to do the following:

* Install VirtualBox on Fedora Linux
    
* Run android-x86 and finish the basic setup
    
* Install an application from the Google Play Store, just like on your phone.
    

## **Basic Requirements**

Before you start, I assume that you have the following:

* Ability to run commands as the superuser (like [SUDO](https://www.sudo.ws/))
    
* An account on Google.com, so you can use the Play store from within the virtual machine.
    

# **How to Install VirtualBox**

The first step is to install VirtualBox. For practical purposes, our installation will be basic, just enough to run our games:

```python
sudo dnf install -y kernel-devel kernel-devel-5.14.18-100.fc33.x86_64
curl --remote-name --location https://www.virtualbox.org/download/oracle_vbox.asc
sudo rpm --import ./oracle_vbox.asc
sudo dnf install -y https://download.virtualbox.org/virtualbox/6.1.36/VirtualBox-6.1-6.1.36_152435_fedora33-1.x86_64.rpm
sudo dnf install -y virtualbox-guest-additions.x86_64
sudo /sbin/vboxconfig
```

## **How to Install the Android-x86 ISO**

The first step is to download the ISO image from [Android-x86](https://sourceforge.net/projects/android-x86/). This ISO contains the Android operating system that will be installed on our virtual hard drive.

After that we can set up our virtual machine like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/virtualbox-androidx86.png align="left")

*How a finished virtual machine looks like on VirtualBox*

![Image](http://localhost:63342/4f800f8a-bbed-4dd8-b03c-00449c9f6698/1437651526/fileSchemeResource/59ea74abf47f101ded05f883e4d4c256-virtualbox-androidx86.png?_ijt=r1jlidvb50q7p9rgbjri12egof align="left")

A few things to note:

* After booting the first time, I found that 1GB for the Android image was not enough. Performance improved a lot after I bumped the ram to 3GB.
    
* Another change was the 'Graphics Controller'. Originally it was VMSVGA but then Android refused to start in graphic mode, so I switched to VboxVGA and it worked.
    
* 2 CPUS and 8GB of disk space were enough for my game.
    
* Finally, I specified that the IDE controller was the android-x86 ISO.
    

To start the virtual machine, you click the 'Start' button on the GUI, and then you will have to make a few decisions like bootable partition:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-partition.png align="left")

*Partitioning your virtual disk. We assign 8 GB and make sure the partition can boot*

Once this is done you can choose your new partition to perform the installation:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-newpartition.png align="left")

*After the new partition is created, you can choose it and you can install the Android OS there*

Then the installation will proceed:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-install.png align="left")

*The installer copies the files from the Android ISO image into the virtual hard drive*

After the installation is complete, you can shut down the virtual machine.

## **First Boot**

Now you'll need to go to the advanced options and select the virtual disk (instead of the ISO image) to boot:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/android-x86-boot-from-disk.png align="left")

*You can either boot from disk on this menu or change the boot order on the virtual machine*

After that, Android will ask you some basic setup information, just like it does on your phone. The final result may look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-running.png align="left")

*The virtual machine looks exactly like your Android phone.*

## **How to Install Games from the Google Play Store**

In my case I decided to install a game where I can fight forces of evil as 1970 [Mazinger Z/ Tranzor Z](https://en.wikipedia.org/wiki/Mazinger_Z) (Yes, I love [Go Nagai](https://en.wikipedia.org/wiki/Go_Nagai) Mazinger Z). To do that, search on the play store and install the game:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/android-x86-play-store.png align="left")

*After Android is running and your credentials are set you can download and install any Android program you want.*

And now, success! We got the game up and running.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-mazingerz.png align="left")

*Sorry, but now it is time to play as Mazinger Z!*

# **What Did We Learn Here?**

* We managed to install a virtual machine engine and successfully run the Android operating system along with our regular Fedora OS
    
* You saw how you can try and discard whole operating systems' setup, without going through the hassle of setting up a dual boot system with Grub on Linux
    

Another nice feature of running the game inside a virtual machine is that you can fully freeze the game, then come back and restore it at exactly the same point where you left it.

Finally, you can do many more things with a virtual machine than just running games, for example:

* You can [analyze malware safely](https://www.varonis.com/blog/malware-analysis-tools), run un-trusted applications, and contain any damage they can cause.
    
* Try a new operating system version before deciding to commit a proper installation (not a big issue these days as most of them provide a lice CD you can boot to try), but this is still very convenient.
    
* Be able to run multiple operating systems simultaneously, without rebooting your machine. You most likely will start trying more advanced options of your virtual machine of choice, like [VirtualBox](https://www.virtualbox.org/manual/ch09.html).
    

Playing games on your PC is a gateway for learning more complex stuff later. Also the fun factor is undeniable. Enjoy!
