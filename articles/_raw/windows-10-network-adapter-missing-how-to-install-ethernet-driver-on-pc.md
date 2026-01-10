---
title: Windows 10 Network Adapter Missing – How to Install Ethernet Driver on PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-07T16:34:05.000Z'
originalURL: https://freecodecamp.org/news/windows-10-network-adapter-missing-how-to-install-ethernet-driver-on-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/adapter-g446e52e4c_1280.jpg
tags:
- name: internet
  slug: internet
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'On Windows 10 and other versions of the Windows operating system, you need
  a network adapter to connect to the internet through a wired or wireless network.

  Sometimes, you might get an error that your network adapter is missing. This can
  be very frus...'
---

On Windows 10 and other versions of the Windows operating system, you need a network adapter to connect to the internet through a wired or wireless network.

Sometimes, you might get an error that your network adapter is missing. This can be very frustrating because you won't be able to connect to the internet.

There are some simple fixes you can use to fix this issue, including:

- removing and reinserting your computer battery
- turning off Antivirus and VPN apps
- restarting your computer

But these might not be enough to fix the issue.

So, in this article, I'm going to show you 5 better ways you can fix the network adapter missing error so you can start connecting your computer to the internet again.

## How to Fix Network Adapter Missing by Using the Built-in Network Reset Tool

Windows 10 has a built-in network reset tool that can reset your settings to default. This often fixes this issue for you.

To fix the network adapter missing error with this solution, follow the detailed steps below:

**Step 1**: Click on Start and select Settings.
![opensettings](https://www.freecodecamp.org/news/content/images/2022/01/opensettings.jpg)

**Step 2**: Choose Network and Internet from the menu tiles.
![ss-1-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-1.jpg)

**Step 3**: Under “Status”, click the Network reset link.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-1.jpg)

**Step 4**: Click the Reset now link.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-1.jpg)

If you use this fix, be aware that you have to reinstall any VPN app on your computer and also reenter WiFi passwords.

## How to Fix Network Adapter Missing by Checking the Driver's Power Management Settings

Windows 10 is optimized for better power management, so when your laptop battery is low, some devices could be turned off to save power. 

You could experience the network adapter missing error due to this power optimization.

To turn off this feature for your network adapter driver, follow the steps below:

**Step 1**: Right-click on Start and select Device Manager.
![devicemanager-1](https://www.freecodecamp.org/news/content/images/2022/01/devicemanager-1.jpg)

**Step 2**: Expand Network Adapters.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-1.jpg)

**Step 3**: Right-click on the affected network adapter and select Properties.
![ss-5-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-1.jpg)

**Step 4**: Switch to the Power Management tab and uncheck "Allow the computer to turn off this device to save power" and click "Ok". 
![ss-6-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-1.jpg)

## How to Fix Network Adapter Missing by Resetting Winsock Settings in the Command Line

Winsock is a program that determines how network services are used on a Windows computer.

If things go wrong with Winsock, it could cause the network adapter missing error.

To reset Winsock, follow the steps below: 

**Step 1**: Click on Start and search for "cmd", then select "Run as Administrator" on the right.
![cmd-admin](https://www.freecodecamp.org/news/content/images/2022/01/cmd-admin.jpg)

**Step 2**: In the command line, type in "netsh winsock reset" and hit `ENTER`.
![ss-7](https://www.freecodecamp.org/news/content/images/2022/01/ss-7.png)

**Step 3**: Restart your computer.

## How to Fix Network Adapter Missing by Reinstalling or Updating the Network Adapter Driver

If the solutions already discussed fail to work for your computer, then you should try and reinstall or update your network adapter driver to fix the issue.

To reinstall your network adapter driver, you should follow the steps below:

**Step 1**: Click on Start and select Device Manager.
![devicemanager-1](https://www.freecodecamp.org/news/content/images/2022/01/devicemanager-1.jpg)

**Step 2**: Expand Network Adapters.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-1.jpg)

**Step 3**: Right-click on the affected driver and select Uninstall device.
![ss-8-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-8-1.jpg)

**Step 4**: Choose Search automatically for updated driver software. 
![ss-10-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-10-1.jpg)

**Step 5**: Restart your computer and the driver will be automatically reinstalled for you.

## Conclusion

In this detailed guide, you learned how you can fix the network adapter missing error so you can connect to the internet again with your computer.

If you find this article helpful, consider sharing it with your friends and family so it can help them too.

Thank you for reading.


