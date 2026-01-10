---
title: Page fault in nonpaged area – How to Fix the Error on a Windows 10 PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-03T16:20:21.000Z'
originalURL: https://freecodecamp.org/news/page-fault-in-nonpaged-area-how-to-fix-the-error-on-a-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/bsod.png
tags:
- name: error
  slug: error
- name: Windows
  slug: windows
seo_title: null
seo_desc: "In Windows, the nonpaged area is the part of the memory that contains critical\
  \ files your computer needs to function properly. \nThose critical files are stored\
  \ in the nonpaged area so the RAM won’t switch them back and forth between itself\
  \ and the pa..."
---

In Windows, the nonpaged area is the part of the memory that contains critical files your computer needs to function properly. 

Those critical files are stored in the nonpaged area so the RAM won’t switch them back and forth between itself and the paged area.

Once there’s an issue with this part of the RAM, the system runs a PAGE_FAULT_IN_NONPAGED_AREA error and shows a BSOD (blue screen of death). The stop code for this error is `0x00000050`.

![iiFbeMETDFDxyU5ASamYtf](https://www.freecodecamp.org/news/content/images/2022/08/iiFbeMETDFDxyU5ASamYtf.png)
[Image source](https://www.tomshardware.com/how-to/fix-page-fault-error-windows-10)

## What We'll Cover
- [What Causes the Page Fault in Nonpaged Area Error](#what-causes-the-page-fault-in-nonpaged-area-error)?
- [How to Fix the Page Fault in Nonpaged Area Error](#how-to-fix-the-page-fault-in-nonpaged-area-error)
  - [Restart your Computer](#restart-your-computer)
  - [Check your Computer’s RAM](#check-your-computers-ram)
  - [Update all Outdated Drivers](#update-all-outdated-drivers)
  - [Perform an SFC Scan](#perform-an-sfc-scan)
  - [Run the Windows Disk Checker Scan](#run-the-windows-disk-checker-scan)
- [Final Thoughts ](#final-thoughts)


## What Causes the Page Fault in Nonpaged Area Error?

The "page fault in nonpaged area" error can be caused by one or any combination of the following issues:

- Corrupt or damaged RAM
- Faulty driver 
- Windows' inability to find files that are supposed to be in the nonpaged area


## How to Fix the Page Fault in Nonpaged Area Error

### Restart your Computer

You can solve many Windows problems by simply restarting your PC. And this error is not an exception. 

This is because when you restart your computer, temporary files are cleared and every task eating up too much RAM is killed – making your computer faster.


### Check your Computer’s RAM

Since this issue is mostly caused by RAM and driver issues, the first thing I would advise you do is to check the computer’s RAM. 

If you can’t check it yourself, you should take the computer to an accredited engineer.

Sometimes, the solution to this issue could be clearing dust from the RAM or reconnecting it.

If checking your RAM fails to fix the error and you still see the BSOD (blue screen of death), [start your computer in safe mode](https://www.freecodecamp.org/news/scanning-and-repairing-drive-how-to-fix-stuck-windows-10-pc-hard-drive/#howtofixastuckscanningandrepairingdrivewithwindowspowershell) and proceed to the remaining fixes in this article.


### Update all Outdated Drivers

An outdated or corrupt driver is also one of the major causes of the page fault in nonpaged area error. So looking for outdated drivers and updating them can solve the problem for you.

To update your computer’s outdated drivers, right-click on Start and select “Device Manger”:
![device-manager](https://www.freecodecamp.org/news/content/images/2022/08/device-manager.png)

Once you see the drivers, a warning symbol will appear beside any outdated driver(s).

Expand the device that has an outdated driver:
![ss1](https://www.freecodecamp.org/news/content/images/2022/08/ss1.png)

Right click on any outdated driver and select “Update driver”:
![ss2](https://www.freecodecamp.org/news/content/images/2022/08/ss2.png)

Select “Search automatically for drivers” so Windows can check the internet for new drivers:
![ss3](https://www.freecodecamp.org/news/content/images/2022/08/ss3.png)

If a new driver is found, install it and restart your computer system.

### Perform an SFC Scan

In Windows, the system file checker (SFC) scan checks your computer for corrupt system files and restores them. So, it can help you get rid of the page fault in nonpaged area error.

To perform the SFC scan, you need to open the command line as an administrator, then type in ` sfc/scannow` and hit `ENTER`:
![ss4](https://www.freecodecamp.org/news/content/images/2022/08/ss4.png)

### Run the Windows Disk Checker Scan

Search for CMD and select “Run as Administrator” on the right:
![ss5](https://www.freecodecamp.org/news/content/images/2022/08/ss5.png)

In the command line, enter `chkdsk C: /f /r` and press `ENTER`.

If you get a message that says “Cannot run because volume is in use by another process”, type `y` and press ENTER so the scan can run when the system restarts the next time.
![ss6](https://www.freecodecamp.org/news/content/images/2022/08/ss6.png)

**N.B.**: This scan takes a very long time, especially if you have a filled-up disk space or when it is done on startup. So, be patient.


## Final Thoughts

This article showed you what the page fault in nonpaged area error is, its causes, and how to fix it.

I hope the solutions discussed in this article help you fix the issue and get rid of the BSOD for you. 

If all of the fixes fail to fix the issue for you, then the last resort is to reset your PC.


