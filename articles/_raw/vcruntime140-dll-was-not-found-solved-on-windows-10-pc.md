---
title: vcruntime140.dll Was Not Found [Solved on Windows 10 PC]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-04T14:11:12.000Z'
originalURL: https://freecodecamp.org/news/vcruntime140-dll-was-not-found-solved-on-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Vcruntime.png
tags:
- name: error
  slug: error
- name: how-to
  slug: how-to
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Have you ever tried to open an app on your computer only to see the error
  "The program can''t start because vcruntime140.dll is missing from your computer.
  Try reinstalling it to fix this problem."?

  This is a common issue with Windows 10 and it can be...'
---

Have you ever tried to open an app on your computer only to see the error "The program can't start because vcruntime140.dll is missing from your computer. Try reinstalling it to fix this problem."?

This is a common issue with Windows 10 and it can be quite frustrating.

But don't worry – in this guide, I'll explain what the error is about, and most importantly, show you two different ways you can fix it.

## What is the "vcruntime140.dll was not found" error and what causes it?

The extension, ".dll" has to do with Dynamic Link Libraries (DLLs), which are libraries that contain the code and data used by a program. 

Once a program is created, it is associated with a DLL, which gets fired only when that particular program is launched.

If the required DLL is missing or corrupted, then an error message giving the user a heads-up on how to fix it gets displayed.

A required DLL could be missing due to malware, incomplete installation, and mostly missing files from Microsoft Visual Studio 2015 Redistributable.

## How to Fix the vcruntime140.dll Was Not Found Error

You can fix the vcruntime140.dll was not found error by installing the Microsoft Visual Studio 2015 package or repairing it. 

If you get this error while trying to use the program WAMP Server – a program that lets you make WordPress websites locally and code PHP – this is all you need to do.

You can also fix the error by downloading the vcruntime140.dll file in particular and moving it to the right folder on your Windows 10 computer.

### Solution 1: Install or Repair Microsoft Visual Studio 2015 Redistributable

**Step 1**: Download the Visual Studio 2015 Redistributable installation package from the [official Microsoft Visual C++ redistributable download page](https://www.microsoft.com/en-us/download/details.aspx?id=52685).
![ss-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-1.png)

Immediately after you click the download button, you will see the option to download the file for a 32-bit operating system and another for a 64-bit operating system.
![ss-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-2.png)

Choose the one that corresponds to the OS of your Windows 10 computer.

**Step 2**: Open up the downloaded file and follow the installation wizard to install it.
![ss-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-3.png)

**Step 3**: Make sure you agree to the license and conditions by tick-marking the checkbox, then click install.

If you have the Microsoft Visual Studio 2015 package installed already and you still get this error, you should "Repair" the package instead.

### How too repair the Microsoft Visual Studio 2015 Redistributable

**Step 1**: Go to Control Panel by clicking Start and searching for “control panel” and hitting `ENTER`.

**Step 2**: Under Programs, select “Uninstall a program”.
![ss-4-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-3.jpg)

**Step 3**: Look for the Microsoft Visual Studio 2015 Redistributable program and right-click on it, then select “Change”.
![ss-5-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-5-3.jpg)

**Step 4**: Click “Repair”.
![ss-6-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-2.jpg)

### Solution 2: Download the vcruntime140.dll File

**Step 1**: Download the vcruntime140.dll file from this [website](https://www.dll-files.com/vcruntime140.dll.html). 
![ss-7-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-7-1.png)

Choose the option that corresponds to your operating system and a Zip file will be downloaded.
![ss-8](https://www.freecodecamp.org/news/content/images/2021/11/ss-8.png)

**Step 2**: Extract the Zip file with the native Windows 10 extract option or an app like WinRAR.

**Step 3**: Drag and drop the vcruntime140.dll file to the installation directory of the app displaying the error message. 

Make sure to confirm that this fixes the issue, otherwise, download and install Microsoft Visual Studio 2015 Redistributable instead.

## Conclusion

In this guide, you learned how to fix the pesky vcruntimed140.dll not found error, so you can use apps and play games seamlessly on your Windows 10 computer.

Apart from the two solutions explained in this article, you can also upgrade your Windows 10 to the latest version which can fix the error as well.

Thank you for reading. If you find this article helpful, consider sharing it with your friends.



