---
title: How to Change Startup Programs in Windows 7, 8 And 10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T19:54:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-startup-program-in-windows-7-8-and-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d4b740569d1a4ca36f9.jpg
tags:
- name: how-to
  slug: how-to
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'By Dillion Megida

  Startup programs are programs which run automatically when a system is booted. This
  is a good practice for programs which you use frequently. It saves you the stress
  of looking for those programs, or, in some cases, manually setting...'
---

By Dillion Megida

Startup programs are programs which run automatically when a system is booted. This is a good practice for programs which you use frequently. It saves you the stress of looking for those programs, or, in some cases, manually setting them up.

Some programs also have this feature by default when they are newly installed.

But if you have too many startup programs it can slow down the boot process. This has a negative effect especially on systems with small capabilities or less processing power.

In this article, we'll learn how to open the startup apps control panel, how to enable and disable startup apps, and finally how to add our desired startup programs in Windows 7, 8 and 10.

In each of these Windows versions, there is a Control Panel for Startup Apps which shows a list of applications that can be run automatically on startup. These applications are either enabled for startup or disabled.

So let's look at the process for each Windows version.

## In Windows 7

### Open the Startup Apps Control Panel

Open the windows startup menu, then type "**MSCONFIG**".  When you press enter, the system configuration console is opened. Then click the "**Startup**" tab which will display some programs that can be enabled or disabled for startup.

### Disable/Enable Startup App

The checkboxes beside the applications indicate the status. If checked, it is enabled for startup, otherwise, it is disabled.

To disable an enabled app, simply uncheck the checkbox and click apply.

To enable a disabled app, check the checkbox and click apply.

These two processes require the system to be restarted before the changes are applied on the applications.

### Add Startup App

To add an app, you'll need to explore the Startup Folder. To do this, try any of the following methods;

- Open the start menu and type "**Startup**" (to search for it). When found, right-click and select Explore to open the folder.
- Open the start menu, select "**All Programs**" and scroll down the list until you find the Startup Folder. When found, Explore it.

Create a shortcut of your desired program, then copy it and paste it in this folder. After this, the program will automatically be added to the panel with a status of "**enabled**".

## In Windows 8

### Open the Startup Apps Control Panel

To open the panel, try any of the following;

- Open "**Task Manager**" and select the "**Startup**" tab
- Open  windows startup menu, and type "**Startup**" to search for the program. Then select any of the options provided.


### Disable/Enable Startup App

To disable a startup app which is enabled, right-click on the app and select "**Disable**".

To enable a startup app which is disabled, right-click on the app and select "**Enable**".

### Add Startup App

Press the window and letter R key to open the Run dialog. Then enter **%AppData%**. This will open a roaming folder. 

Navigate to **\Microsoft\Windows\Start Menu\Programs\Startup**. In this folder, paste the shortcut of your desired app. This will make it a startup application with a status of "enabled".

## In Windows 10

### Open the Startup Apps Control Panel

- Open the start menu, type "**Startup Apps**" (to search for it) and click any of the results.
- Open "**Task Manager**", then select the "**Startup**" tab

### Disable/Enable Startup Apps

To disable a startup app, right-click on any app in the list with a status of "**enabled**" and select "**disable**".

To enable a startup app in the list which is disabled, right-click on the app and select "**enable**".

### Add Startup App

Hold the windows and letter R key on the keyboard. In the run dialog, enter "**shell:startup**". 

In the folder, you can add any application of your choice which you'd want to run at startup. They'll be added to the list so when you access your Startup Apps, you can disable or enable them.

##  Wrap Up

If there's any application which you always run when you boot up your system, it is good practice to make it a startup program.

When your system becomes slow to boot, it's most likely because startup programs are responsible. Now you know how to disable or reduce them.


