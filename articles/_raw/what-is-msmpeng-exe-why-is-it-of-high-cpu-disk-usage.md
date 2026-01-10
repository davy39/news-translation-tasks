---
title: What is msmpeng.exe? Why is it High CPU Disk Usage?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-21T15:01:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-msmpeng-exe-why-is-it-of-high-cpu-disk-usage
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/joseph-greve-BPJKc4r7_eo-unsplash.jpg
tags:
- name: Security
  slug: security
- name: Windows
  slug: windows
seo_title: null
seo_desc: "msmpeng.exe is an important part of Windows Security, formerly known as\
  \ Windows Defender. It scans your computer for various threats ranging from malware\
  \ to spyware, then renders the appropriate solution(s). \nIn this article, I will\
  \ take you through ..."
---

msmpeng.exe is an important part of Windows Security, formerly known as Windows Defender. It scans your computer for various threats ranging from malware to spyware, then renders the appropriate solution(s). 

In this article, I will take you through what mempeng.exe is, the reason why it eats up too much CPU, and 2 different ways you can stop it from using too much CPU.

## What is msmpeng.exe?

Msmpeng.exe stands for Microsoft Malware Protection Engine. Also known as Antimalware service executable, it is the built-in antivirus program for Windows 10 computers. 

This program runs in the background and scans your computer for threats such as harmful software, viruses, worms, and so on, then quarantines or deletes them. 

## Why is msmpeng.exe high CPU disk usage?

msmpeng.exe eats up too much CPU disk space because it actively runs in the background, and scans every part of your computer while doing so. This of course makes msmpeng.exe a resource-consuming program.

Apart from that, another reason why msmpeng.exe uses a high amount of CPU is that the program scans its own folder (`C:\Program Files\Windows Defender`). Low hardware resources have also been linked to msmpeng.exe consuming too much CPU disk space.

## How to Stop msmpeng.exe from Using Too Much CPU Disk Space

There are 2 main ways you can stop the Windows 10 Antimalware service executable from using up too much CPU. First, you can stop Windows Defender from scanning its own folder and disabling real-time protection, and second you can reschedule Windows Defender scans.

### Solution 1: Prevent Windows Defender from Scanning its own Folder

**Step 1**: Click on Start or Press the WIN key on your keyboard, then click on the gear icon to open the Settings app.
![ss-1-7](https://www.freecodecamp.org/news/content/images/2021/10/ss-1-7.jpg)

**Step 2**: Click on “Update and Security” from the list.
![ss-2-8](https://www.freecodecamp.org/news/content/images/2021/10/ss-2-8.jpg)

**Step 3**: Select “Windows Security” and click on “Virus and threat protection”.
![ss-3-6](https://www.freecodecamp.org/news/content/images/2021/10/ss-3-6.jpg)

**Step 4**: The Windows Security app will open up. Under “Virus & threat protection settings”, click on the “Manage Settings” link.
![ss-4-7](https://www.freecodecamp.org/news/content/images/2021/10/ss-4-7.jpg)

**Step 5**: Scroll down to “Exclusions” and click the “Add or remove exclusions” link.
![ss-5-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-5-3.jpg)

**Step 6**: On the next page, click on “Add an exclusion”, then select “Folder”.
![ss-6-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-6-5.jpg)

**Step 7**: To avoid multiple clicking, paste in “`C:\Program Files\Windows Defender`” into the editor and click on “Select Folder”.
![ss-7-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-7-3.jpg)

**Step 8**: Immediately after you click on “Select Folder”, a massive modal will appear – make sure you click Yes. 

You can now see that the folder has been added as an exclusion:
![ss-8-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-8-1.jpg)

Windows Defender won’t scan this folder anymore, so the rate of CPU usage should go down on your computer.

### Solution 2: Disable Real-time Protection and Reschedule Windows Defender scans

**Step 1**: To disable real-time protection and reschedule the scans performed by Windows Defender, press `WIN` (Windows key) to open the Run Dialogue. 

**Step 2**: Type in “taskschd.msc” and click “OK”. This will open up the Task Scheduler app.
![ss-9](https://www.freecodecamp.org/news/content/images/2021/10/ss-9.jpg)

**Step 3**: Expand the “Task Scheduler tab”, then select “Microsoft”, and then “Windows”.
![ss-10](https://www.freecodecamp.org/news/content/images/2021/10/ss-10.jpg)

**Step 4**: Scroll down and select “Windows Defender”.
![ss-11](https://www.freecodecamp.org/news/content/images/2021/10/ss-11.jpg)

**Step 5**: Right-click on “Windows Defender Scheduled Scan” and select “Properties”.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/10/ss-12.jpg)

**Step 6**: In the General tab, uncheck “Run with highest privileges”.
![ss-13](https://www.freecodecamp.org/news/content/images/2021/10/ss-13.jpg)

**Step 7**: Go to the Conditions tab and make sure every box there is unchecked.
![ss-14](https://www.freecodecamp.org/news/content/images/2021/10/ss-14.jpg)

**Step 7**: Lastly, go to the Triggers tab and click “New”.
![ss-15](https://www.freecodecamp.org/news/content/images/2021/10/ss-15.jpg)

**Step 8**: Finally, schedule the time you want Windows Defender to run scans, choose the frequency, date, and time, then click “OK”. Click “OK” again.
![ss-16](https://www.freecodecamp.org/news/content/images/2021/10/ss-16.jpg)

**Step 8**: Restart your computer. With this, msmpeng.exe should not eat up too much CPU disk space anymore.

## Wrapping up

Msmpeng.exe, also known as Antimalware service executable, is a relevant and effective program that protects your computer from threats. 

At the same time, it eats up too much CPU disk space, which might slow down your computer and reduce battery life, so you might be tempted to disable it. 

Since the protections msmpeng.exe offers are useful, you should look for ways to minimize its actions instead of disabling it permanently, like this article showed you how to do.

If CPU disk usage doesn’t reduce, you could try disabling Windows Defender permanently – but make sure you get another antivirus program for your computer if you do that.

Thank you for reading this article. Consider sharing it with your friends and family if you find it helpful.


