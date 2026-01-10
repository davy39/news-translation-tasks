---
title: What is dllhost.exe and COM Surrogate in Windows Task Manager? (Solved)
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2020-05-12T16:14:45.000Z'
originalURL: https://freecodecamp.org/news/what-is-dllhost-exe-and-com-surrogate-in-windows-task-manager-solved
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b18740569d1a4ca29a4.jpg
tags:
- name: error handling
  slug: error-handling
- name: Windows
  slug: windows
seo_title: null
seo_desc: COM Surrogate processes, short for Component Object Model, are necessary
  components in Windows. They are used to run software extensions that other programs
  need to run. And if those extensions crash, it is the surrogate processes that are
  affected a...
---

COM Surrogate processes, short for **Component Object Model**, are necessary components in Windows. They are used to run software extensions that other programs need to run. And if those extensions crash, it is the surrogate processes that are affected and not the programs that were running them.

There are many use cases of these processes, for example creating thumbnails of images and other files when a folder is opened. The COM Surrogate process hosts .dll files, so its name is dllhost.exe.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-172.png)
_Photo by [Unsplash](https://unsplash.com/@christinhumephoto?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Christin Hume</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## **Is COM Surrogate a virus?**

The short answer is no. COM Surrogate processes themselves cannot be viruses. However, viruses and malware can disguise themselves as a COM Surrogate process.

## Should I remove COM Surrogate?

Since it is an integrated part of Windows, I wouldn't advise you to remove it. This container process enables your OS to run COM objects that help other processes and programs to work.

## Checking the legitimacy of COM Surrogate

Since these processes are genuine components of Windows, they are widely used by cybercriminals. This has consequences – like the COM Surrogate having high CPU consumption and creating duplicates in the Task Manager. 

A simple way to check its legitimacy is:

1. Open Windows Task Manager by **right-clicking** on the taskbar and clicking Task Manager.
2. Find the COM Surrogate processes and then right-click to **Open File Location**.
3. Processes are legitimate if they are located in **C:/Windows\System32** or **C:/winnt/system32**.

## Common Errors

1. **COM Surrogate high CPU, disk usage**
2. **COM Surrogate is not responding, freeze**
3. **COM Surrogate virus**
4. **COM Surrogate taking memory**
5. **COM Surrogate always running**
6. **COM Surrogate stopped working**
7. **COM Surrogate keeps crashing, opening**

There are many reasons for these errors to occur. The most common are:

1. A third-party program incorrectly registered COM objects or they did not work correctly (if they were incompatible with current versions of Windows, outdated software).
2. If the problem occurs during drawing thumbnails in Explorer, it's because of outdated or incorrectly working codecs. 
3. Can be caused by viruses or malware, as well as damage to Windows System Files.

## How can you fix these errors?

We discussed many errors above but the most common of them is "**COM Surrogate has stopped working**". Below are the various methods to resolve it.

And even if you are having any of the other errors listed above, these methods are good to go and should help fix them, too.

### 1. Update Codecs

A manual method to solve this error is to update all the **Codecs** of Windows (7, 8 or 10) to their latest updated versions. You can download and install your latest **Windows Codec Pack** from here:

[https://www.microsoft.com/en-in/download/details.aspx?id=507](https://www.microsoft.com/en-in/download/details.aspx?id=507)

**Windows 7 Codec Pack:** [https://www.windows7codecs.com/](https://www.windows7codecs.com/)    

**Windows 8 & 10 Codec Pack:** [http://www.windows8codecs.com/](https://www.windows8codecs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-68.png)
_Installing Codecs_

### **2. Reset Internet Explorer**

The issue can also be caused due to cached files that were corrupt. In this instance, it's be best to reset IE. 

1. Hold the **Windows Key** and **Press R**. In the run dialog, type **inetcpl.cpl** and click **OK.** Go to the Advanced Tab and choose Reset. 
2. Select **Delete Personal Settings** and hit the reset button again. Once you've done all that, reboot your PC and test it out.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-69.png)
_Resetting Internet Explorer_

### 3. Check Disk For Errors

If this error occurs when opening files saved in a particular **DRIVE** other then C:\ then you should check that drive for errors. If you don't have any additional drives, just check the C:\ drive.

1. Hold the **Windows Key** and press **E**. On **Windows 7/Vista** you will see the drives listed. 
2. On Windows 8/10, chose **This PC** from the left pane to view the drives. **Right-click** on the Selected **Hard disk drive** that you want to check and then select “**Properties”**.   

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-67.png)
_Checking Disk for Errors_

 3. Click the **Tools** tab from the top and then click **Check Now** under **Error-                  Checking. Check** both the **Options** and the click **Start**.

### 4. Re-register the DLLs

1. Run the following commands in an escalated command prompt. Click Start, type **cmd,** and right click on the “**cmd**” program from the search results. Then select **Run as Administrator**.

![cmd-run-as-administrator](https://cdn.appuals.com/wp-content/uploads/2014/11/cmd-run-as-administrator.png)
_Running cmd as Administrator_

 2. In the **Command Prompt** window, type the following commands and press the        **Enter key** one by one:

`regsvr32 vbscript.dll`
`regsvr32.jscript.dll`

![2015-12-03_002655](https://cdn.appuals.com/wp-content/uploads/2015/12/2015-12-03_002655.png)
_Re-registering the DLLs_

### 5. Rollback to the Previous Display Adapter Driver

1. To do this, hold the **Windows Key** and **Press R**. In the run dialog, type **hdwwiz.cpl** and click **OK**. 
2. Scroll to the **Display Adapters** section in the Device Manager. Right click on it and select Properties. 
3. Click **Roll Back Driver** and proceed with the instructions on the screen. 

In some cases, this option is grayed out. If that is the case then attempt the methods below.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-72.png)
_Display Adapter_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-71.png)
_Roll Back Driver_

### **6. Add dllhost.exe to the DEP(Data Execution Prevention) Exception**

Go to Start > Control Panel > System > Advanced System settings> Performance settings > Data Execution Prevention.

1. Select **“**Turn on DEP for all programs and services except those I select:**”**
2. Click on “**Add“** and navigate to **C:\Windows\System32\dllhost.exe on 32-bit Windows Machine** and on a **64-bit machine, add **C:\Windows\SysWOW64\dllhost.exe****
3. After adding **dllhost.exe** to the exception list, **Apply changes** or click **OK.**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-73.png)
_Data Execution Prevention_

### 7. Switch to List or Details view / disable thumbnails

We have already discussed that **COM Surrogate** is in charge of your thumbnails. In order to avoid problems with it, you can disable thumbnails.

In addition, you can switch to **List** or **Details** view by doing the following:

1. Open **File Explorer**.
2. Click the **View tab** and choose the **List** or **Details** option.

### 8. Update your Antivirus

It has been reported that certain antivirus software, such as Kaspersky antivirus, can sometimes cause issues with the **COM Surrogate** process.

In order to fix those issues, you should install the latest version of your current antivirus software.

---

_Thank you for reading this article. I hope it will help you fix your COM Surrogate errors._

