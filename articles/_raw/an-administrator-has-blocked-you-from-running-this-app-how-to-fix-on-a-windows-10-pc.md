---
title: An Administrator Has Blocked You From Running This App –  How to Fix on a Windows
  10 PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-21T15:51:17.000Z'
originalURL: https://freecodecamp.org/news/an-administrator-has-blocked-you-from-running-this-app-how-to-fix-on-a-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/dadminError.jpg
tags:
- name: error
  slug: error
- name: Security
  slug: security
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "Sometimes when you decide to open an app or file or install or open a program\
  \ on your Windows 10 PC, you might get the error \"An administrator has blocked\
  \ you from running this app\". \nYou get this error because Windows 10 is optimized\
  \ for protection ..."
---

Sometimes when you decide to open an app or file or install or open a program on your Windows 10 PC, you might get the error "An administrator has blocked you from running this app". 

You get this error because Windows 10 is optimized for protection against malware through Windows Defender and User Account Control (UAC).

But at times, this protection is overly sensitive. So, on some occasions, the error occurs even when you're trying to run trusted apps or open trusted files.

Today is hopefully the last day you'll see this error pop up on your Windows 10 PC. Because in this article, I will show you 5 ways to fix it, so you can start using your computer without the fear of the error.

**PS**: If you're getting this error while running a trusted app or trying to open a trusted file, the solutions provided in this article are for you. If you don't trust the app, use any of the solutions only if you're ready to take a risk.

## Table of Contents
- [Temporarily Disable Your Antivirus Program](#heading-solution-1-temporarily-disable-your-antivirus-program)
- [Disable the Windows Smartscreen Feature](#heading-solution-2-disable-the-windows-smartscreen-feature)
- [Unblock the File](#heading-solution-3-unblock-the-file)
- [Run the App with the Command Prompt](#heading-solution-4-run-the-app-with-the-command-prompt)
- [Make Changes to the Group Policy](#heading-solution-5-make-changes-to-the-group-policy)
- [Conclusion](#heading-conclusion)

## Solution 1: Temporarily Disable Your Antivirus Program

If you get the "An administrator has blocked you from running this app" error, it could be because of your antivirus app. 

So, disabling the antivirus app could provide a solution.

Whether you use the inbuilt Windows Defender or a third-party antivirus program, the steps below will help disable it.

**Step 1**: Press `ALT` + `SHIFT` + `ESC` on your keyboard to open the Task Manager.

**Step 2**: Switch to the Startup tab.

**Step 3**: Locate your Antivirus Program in the list, right-click on it and select "Disable".
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-4.jpg)

**PS**: If you don't find your antivirus program in the startup tab, then check the Processes tab.

## Solution 2: Disable the Windows Smartscreen Feature

The Windows Smartscreen is an anti-malware feature that works with Windows Defender to block malware.

Sometimes, it triggers this error even when you're using a trusted app.

To disable Smartscreen, follow the steps below:

**Step 1**: Press `WIN` + `S` on your keyboard and search for "smartscreen", then click on the "App & Browser Control" search result.
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-2.jpg)

**Step 2**: Open the "Reputation-based protection settings" link.
![ss-3-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-3.jpg)

**Step 3**: Turn off the toggle under "Potentially unwanted app blocking".
![ss-4-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-3.jpg)

## Solution 3: Unblock the File

If you're getting the error while opening a file, this solution is for you.

**Step 1**: Right-click on the file and select Properties.
![ss-5-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-3.jpg)

**Step 2**: In the General tab, check "Unblock" under "Security".

**Step 3**: Click Apply and then Ok.
![ss-6-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-3.jpg)

## Solution 4: Run the App with the Command Prompt

Command prompt allows you to run an app and bypass the administrator check. 

So you can avoid getting this error if you run the app triggering the error using the command prompt.

The following steps show you how to run any app with the command prompt:

**Step 1**: Locate the app triggering the error, right-click on it and select Open file location.
![ss-7-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-1.jpg)

**Step 2**: Right-click on the file and select properties.
![ss-8-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-8-3.jpg)

**Step 3**: In the General tab, copy the texts under location. Don't close the Properties window yet.
![ss-9-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-9-1.png)

**Step 4**: Click on Start and search for "cmd", then select Run as Administrator on the right.
![cmd-admin-3](https://www.freecodecamp.org/news/content/images/2022/01/cmd-admin-3.jpg)

**Step 5**: In the command prompt, paste the text you copied in step 3, then minimize the command prompt.
![ss-10-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-10-2.png)

**Step 5**: Head back to the Properties opened in Step 1 and copy the file name.
![ss-11-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-11-1.png)

**Step 6**: Maximize the Command Prompt, type "\" (slash) in front of the text you pasted in Step 4, and paste in the file name, as you can see in the screenshot below.
![ss-12-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-12-1.png)

**Step 7**: Hit `ENTER` to finally launch the app.

## Solution 5: Make Changes to the Group Policy

With the Group Policy, you can make changes you won't easily find anywhere else on your computer.

One of these changes can be made on the User Accounts Control (UAC) to allow apps to escape the administrator check.

To make the changes that will get rid of the error, follow the steps below:

**Step 1**: Press `WIN` + `R` on your keyboard to open the Run dialogue.

**Step 2**: In the run dialogue, type in "gpedit.msc" and hit `ENTER` on your keyboard.
![ss-13-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-13-1.png)

**Step 3**: Under Computer Configuration, expand Windows Settings, Security Settings, and Local Policies. 

**Step 4**: Click on Security Options. Don’t attempt to expand it, just click on it.
![ss-14-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-14-1.jpg)

**Step 5**: Navigate to the bottom and double-click "User Account Control: Run all administrators in Admin Approval Mode".
![ss-15](https://www.freecodecamp.org/news/content/images/2022/01/ss-15.jpg)

**Step 6**: Select Disable, click Apply, and then Ok.
![ss-16](https://www.freecodecamp.org/news/content/images/2022/01/ss-16.jpg)

## Conclusion

This article showed you 5 different ways you can fix the "An administrator has blocked you from running this app" error. 

This error message is only one of the 3 ways the error could come up.

If you're getting it in the form of "Your system administrator has blocked this program Group Policy, GPO, Regedit", then [solution 5](#heading-solution-5-make-changes-to-the-group-policy) is for you.

If you're getting it in the form of "Your system administrator has blocked this program uTorrent, Avast, AVG", then [solution 1](#heading-solution-1-temporarily-disable-your-antivirus-program) is for you.

In short, you'll just need to figure out the source of the error and then choose the solution that's right for your situation. 

If you find this article helpful, consider sharing it with your friends and family.

Thank you for reading.


