---
title: How to Get Rid of the Activate Windows Watermark [Windows 10 PC Activation
  Message Removal]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-06T16:00:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-rid-of-the-activate-windows-watermark-windows-10-pc-activation-message-removal
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/activate.png
tags:
- name: how-to
  slug: how-to
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'If you''re a Windows user, you might have seen the "Activate Windows" message
  that displays over every other thing – including your cursor. I guess they gave
  it a z-index of infinity.

  This message gets displayed when you use a Windows OS that has an i...'
---

If you're a Windows user, you might have seen the "Activate Windows" message that displays over every other thing – including your cursor. I guess they gave it a z-index of infinity.

This message gets displayed when you use a Windows OS that has an invalid or expired license. This keeps you from being able to personalize your desktop or get updates for Windows Defender – now Windows Security. You will also be unable to install Microsoft Office.

If this is the case, you can remove the watermark because it could have a negative effect on visual hierarchy and might be embarrassing if you're taking screenshots or recording your desktop. 

This happened to me when I was using freeCodeCamp for my first round of 100DaysOfCode.
![day49](https://www.freecodecamp.org/news/content/images/2021/12/day49.jpg)

In this article, I will show you 4 ways you can remove the Activate Windows watermark on your Windows 10 PC. 

Some of the tweaks only remove the message but not the underlying problems, so you should pay attention to the last one, which will remove the message and activate your Windows as well.

## Table of Contents
- [How to Get Rid of the Activate Windows Watermark with PowerShell](#heading-how-to-get-rid-of-the-activate-windows-watermark-with-powershell)
- [How to Get Rid of the Activate Windows Watermark with Notepad](#heading-how-to-get-rid-of-the-activate-windows-watermark-with-notepad)
- [How to Get Rid of the Activate Windows Watermark by Using the Registry](#heading-how-to-get-rid-of-the-activate-windows-watermark-by-using-the-registry)
- [How to Get Rid of the Activate Windows Watermark with a Product Key](#heading-how-to-get-rid-of-the-activate-windows-watermark-with-a-product-key)
- [Conclusion](#heading-conclusion)


## How to Get Rid of the Activate Windows Watermark with PowerShell

PowerShell enables you to directly interact with your Windows OS with scripts. 

There's a PowerShell script you can execute that'll eventually get rid of the Activate Windows message. 

**To execute the script, follow the steps below.**

**Step 1**: Press `WIN` (Windows logo key) + `S` on your keyboard.

**Step 2**: Search for "powershell". You have to execute the script as an administrator, so click on "Run as Administrator" on the right.
![ss-1-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-1.jpg)

**Step 3**: Type in "slmgr /renew" (without quotes) and hit `ENTER`.
![ss-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-2.png)

**Step 4**: Restart your PC.

If you’ve made several tweaks with third-party apps in order to activate Windows, this fix might not work for you. If it doesn’t work for you, try the next one.

## How to Get Rid of the Activate Windows Watermark with Notepad

As simple as Notepad looks to everyone, you can use it to remove the Activate Windows watermark. In fact, this way is one of the most popular to get rid of the message.
	
You can use Notepad to get rid of the message with the simple steps below.

**Step 1**: Hit the `WIN` button on your keyboard and search for Notepad. Click Open on the right or the Notepad search result to launch the app.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-3-1.jpg)

**Step 2**: Make sure you’re working with a new, untiled file. Paste in the script below:

`@echo off
taskkill /F /IM explorer.exe
explorer.exe
exit`

**Step 3**: Click File in the menu and select "Save as".
![ss-4-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-4-1.jpg)

**Step 4:** Name the file "Activation.bat" and select "All files" as the format. Then save the file to any location you want.
![ss-5](https://www.freecodecamp.org/news/content/images/2021/12/ss-5.jpg)

**Step 5**: Locate the file and right-click on it, then select "Run as Admissions". 
![ss-6-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-1.png)

The script will be executed quickly and will refresh your computer.

**Step 6**: Restart your PC.

## How to Get Rid of the Activate Windows Watermark by Using the Registry

Windows 10 registry lets you make deeper changes that have significant effects on your computer.

You can get rid of the Activate Windows watermark by making a less complicated modification in the Registry, as done below.

**Step 1**: Right-click on Start and select Run.
![ss-7-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-7-1.jpg)

**Step 2**: Type in "regedit" (without quotes) into the Run dialogue and hit `ENTER`.
![ss-8](https://www.freecodecamp.org/news/content/images/2021/12/ss-8.png)

**Step 3**: Expand HKEY_CURRENT_USER, Control Panel, and then click Desktop.
![ss-9-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-9-1.png)

**Step 4**: Locate PaintDesktopVersion and double-click on it.

**Step 5**: Change the value from 1 to 0 and click Ok.
![ss-10](https://www.freecodecamp.org/news/content/images/2021/12/ss-10.jpg)

**Step 6**: Restart your computer.

## How to Get Rid of the Activate Windows Watermark with a Product Key

The best way to get rid of the Activate Windows watermark is to do what the message says - activate Windows. 

You can activate Windows with a product key you have to buy from Microsoft.

The steps below will help you use your product key to activate Windows:

**Step 1**: Click on Start and select Settings.
![ss-11-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-11-1.jpg)

**Step 2**: Choose Updates and Security from the menu tiles.
![ss-12-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-12-1.jpg)

**Step 3**: Switch to the Activation tab on the left and click on Change product key.
![ss-13-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-13-1.jpg)

**Step 4**: Enter your 24-character alphanumeric product key and click Next. 
![ss-14](https://www.freecodecamp.org/news/content/images/2021/12/ss-14.png)

Windows will get activated as long as the product key is correct.

## Conclusion
I hope these ways to get rid of the Activate Windows watermark help you out. 

If you find this article helpful, make sure to share it with your friends and family.

Thank you for reading.


