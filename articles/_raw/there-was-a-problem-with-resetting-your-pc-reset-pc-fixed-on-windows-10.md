---
title: There Was a Problem with Resetting Your PC [Reset PC Fixed on Windows 10]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-08T17:20:41.000Z'
originalURL: https://freecodecamp.org/news/there-was-a-problem-with-resetting-your-pc-reset-pc-fixed-on-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/reset.png
tags:
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'There are a number of reasons why you might want to reset your PC. From
  malware attacks to bad PC health, or maybe you just want to start afresh – the list
  goes on.

  When you''re resetting your PC, you might get the error "There was a problem resetting...'
---

There are a number of reasons why you might want to reset your PC. From malware attacks to bad PC health, or maybe you just want to start afresh – the list goes on.

When you're resetting your PC, you might get the error "There was a problem resetting your PC". This error could take another form like "There was a problem refreshing your PC" and so on. 

If you're experiencing this issue after attempting to reset your Windows 10 PC, you've come to the right place. Because, in this detailed guide, I'm going to show you 4 ways you can fix the issue and proceed to completely reset your PC.

Three of the solutions I will be showing you require admin permissions and will be done in the command line, which you can always access even if your computer is stuck in the reset loop.

To access the command line on a Windows 10 PC stuck in the reset loop, attempt to perform startup repair if you're prompted to, then choose command prompt
![startup-repair-windows](https://www.freecodecamp.org/news/content/images/2021/12/startup-repair-windows.jpg)

But since you don't get to use the GUI (Graphics User Interface) to open the command prompt as an admin if your computer is stuck in the reset loop, how then do you use the command line as an admin? Execute the command `powershell "start cmd -v runAs"`.

## How to Fix the Error "There was a Problem Resetting your PC"

### Perform a SFC Scan

The system file checker (SFC) scan lets you perform a command-line-based scan that finds and fixes corrupt files that might be preventing your computer from successfully resetting.

To perform the SFC scan, you need to follow the steps below:

**Step 1**: Hit the` WIN` key on your keyboard and search for "cmd'. Then choose Run as Administrator on the right to use the command prompt as an administrator. Make sure you click “Yes” in the next prompt.
![ss-1-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-2.jpg)

**Step 2**: In the command line, type in `sfc /scannow` and hit `ENTER`. The scan might take more than 15 minutes, so just be patient.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-2-1.png)

**Step 3**: Restart your PC and attempt to reset it again.

If this doesn't fix the issue, proceed to the next fix – DISM scan.

### Perform a DISM Scan

Performing a DISM scan to fix this issue is officially recommended by Microsoft. 

DISM stands for Deployment Image Servicing and Management Tool. It is a command-line executable that you can use to repair a Windows image and modify Windows installation media.

The steps below explain how to run a DISM scan:

**Step 1**: Hit the` WIN` key on your keyboard and search for "cmd'. Then choose Run as Administrator on the right to use the command prompt as an admin. Make sure you click “Yes” in the next prompt.
![ss-1-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-2.jpg)

**Step 2:** Paste in `dism /Online /Cleanup-Image /RestoreHealth` and hit `ENTER`. This takes even more time than the SFC scan, so be patient.
![ss-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-3.png)

**Step 3**: Once the scan is completed, restart your computer and attempt to reset it again.
![completed-scan](https://www.freecodecamp.org/news/content/images/2021/12/completed-scan.png)

### Disable and Re-enable ReAgentC.exe

REAgentC is a Windows recovery tool that attempts to fix errors with startup once your computer fails to boot.

Since that is what REAgent.exe does, there might be errors with it if your PC fails to reset. So, disabling and re-enabling it can fix the issue for you.

You can disable and re-enable REAgent.exe with the steps highlighted below:

**Step 1**: Hit the` WIN` key on your keyboard and search for "cmd'. Then choose Run as Administrator on the right.
![ss-1-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-2.jpg)

**Step 2**: Type in `reagentc /disable` and hit `ENTER` to disable REAgent.exe

**Step 3**: Type in `reagentc /enable` and hit `ENTER` to re-enable REAgent.exe
![ss-4](https://www.freecodecamp.org/news/content/images/2021/12/ss-4.png)

**Step 4**: Restart your PC and try resetting it once more.

### Refresh Windows from Windows Security

Before going through this fix, make sure your files are backed up.

Windows Security (formerly Windows Defender) is widely known as a powerful antivirus program for Windows 10 computers, but there's more to it. 

With Windows Security, you can give your Windows 10 PC a fresh start. The steps below show you how to do it.

**Step 1**: Press `WIN` (Windows logo key) + I on your keyboard to launch Settings.

**Step 2**: Choose Updates and Security from the menu tiles.
![ss-5-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-5-1.jpg)

**Step 3**: Switch to the Windows Security tab on the left and select "Device performance & health".
![ss-6-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-2.jpg)


**Step 5**: Click on the "Additional info" link under Fresh start.
![ss-7-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-7-2.jpg)

**Step 6:** Click on the "Get Started" button.
![ss-8-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-8-1.jpg)

**Step 7**: Follow the rest of the prompts to refresh your PC with Windows Security.

## Final Words

This guide took you through several ways you can fix your PC when it won't reset properly. Now hopefully you can reset your computer and start using it again successfully.

As a last resort, you can install a fresh Windows 10 OS from a bootable USB drive or DVD if you're still getting the error after trying the fixes suggested in this article. In fact, some errors don't disappear unless you do this.

Be aware that you can also experience this problem on Windows 8 and 8.1, so you can apply the same fixes suggested in this article.


