---
title: The Code Execution Cannot Proceed Because msvcp140.dll Was Not Found – How
  to Fix on a Windows 10 PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-19T17:47:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-the-code-execution-cannot-proceed-because-msvcp140-dll-was-not-found
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/msvcpdll-3.png
tags:
- name: error handling
  slug: error-handling
- name: Microsoft
  slug: microsoft
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "msvcp140.dll is a Microsoft C Dynamic Linked Library file responsible for\
  \ running certain Windows apps and games – especially those built on C++. \nSometimes,\
  \ when you're trying to open an app or game, you might get the error “the code execution\
  \ canno..."
---

msvcp140.dll is a Microsoft C Dynamic Linked Library file responsible for running certain Windows apps and games – especially those built on C++. 

Sometimes, when you're trying to open an app or game, you might get the error “the code execution cannot proceed because msvcp140.dll was not found”. 

This error can come in another form, too – "The program can’t start because MSVCP140.dll was not found. Try reinstalling the program to fix this problem".

This could happen because the file is really missing, or it's available but corrupt. 

You can scan your computer with Windows Defender or a third-party antivirus program, but this doesn’t always fix the error.

If you are getting this error while opening a game or app on your Windows 10 PC, you’ve come to the right place. Because in this article, I’m going to show you 3 ways you can fix the error and start using your app or playing your game once again.

## Solution 1: Reinstall the App

As suggested in the error message, reinstalling the program that's triggering the "msvcp140.dll was not found" error can fix the problem for you.

To reinstall an app, do the following:

**Step 1**: Click on Start and select Settings.
![opensettings-2](https://www.freecodecamp.org/news/content/images/2022/01/opensettings-2.jpg)

**Step 2**: Select Apps from the menu tiles.
![ss-1-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-3.jpg)

**Step 3**: Click on the app causing the error and select Uninstall.
![ss-](https://www.freecodecamp.org/news/content/images/2022/01/ss-.jpg)

**Step 4**: Restart your computer, then reinstall the app by downloading it from the vendor’s website or Microsoft store.

## Solution 2: Run the SFC Scan

Since the error could be triggered by a corrupt file, the System File Checker scan can help fix it. When you run this program, it checks your computer files for corruption and fixes them.

To run the SFC scan, follow the steps below:

**Step 1**: Click on Start and search for “cmd”. Click on Run as Administrator on the right, because you need to run the scan as an admin.
![cmd-admin-2](https://www.freecodecamp.org/news/content/images/2022/01/cmd-admin-2.jpg)

**Step 2**: Paste in `sfc /scannow` and hit `ENTER`.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-1.png)

**Step 3**: When the scan is done, close the Command Prompt and restart your PC.

## Solution 3: Install Microsoft Visual C++ Redistributable

If any of the solutions above fail to work for you, then installing Microsoft Visual C++ redistributable package will fix it. 

This is because `msvcp140.dll` and another DLL file called `vcruntime140.dll` are both constituents of the Microsoft Visual C++ package.

The following step by step guide shows you how to install Microsoft Visual C++ redistributable:

**Step 1**: To download the file, go to the official Microsoft Visual C++ redistributable download page and click Download.
![ss-3-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-2.png)

**Step 2**: On the next page, you will see the option to download the file for a 32-bit operating system and another for a 64-bit operating system. Select the one for your OS and click “Next”.
![ss-4b-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4b-1.png)

**Step 3**: Open the downloaded file and follow the installation Wizard to install it.
![ss-5-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-2.png)

If you have the Microsoft Visual Studio 2015 package installed already and you still get this error, you should uninstall and then reinstall the package.

I hope this guide helps you fix the error. 

Thank you for reding.


