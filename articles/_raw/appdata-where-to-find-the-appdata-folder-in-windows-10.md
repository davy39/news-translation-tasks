---
title: AppData – Where to Find the AppData Folder in Windows 10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T18:22:12.000Z'
originalURL: https://freecodecamp.org/news/appdata-where-to-find-the-appdata-folder-in-windows-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9975740569d1a4ca1fd7.jpg
tags:
- name: data
  slug: data
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'By Vijit Ail

  The AppData folder includes application settings, files, and data unique to the
  applications on your Windows PC. The folder is hidden by default in Windows File
  Explorer and has three hidden sub-folders: Local, LocalLow, and Roaming.

  You...'
---

By Vijit Ail

The AppData folder includes application settings, files, and data unique to the applications on your Windows PC. The folder is hidden by default in Windows File Explorer and has three hidden sub-folders: Local, LocalLow, and Roaming.

You won't use this folder very often, but this is where your important files reside. For example, your bookmarks, saved sessions, and so on.

In this guide, you will learn how to find, unhide, and access the AppData folder in Windows.

## What is the AppData Folder?

Applications in windows often store their settings and temporary data in the AppData Folder. Each windows user account has its own AppData folder. As I mentioned earlier, there are three folders inside AppData - Local, LocalLow, and Roaming. 

The Local folder is used to store data that is specific to a single windows system, which means data is not synced between multiple PCs.

The LocalLow folder is the same as the Local folder, except it is used by applications with low integrity that run with restricted security settings, for example, Mozilla Firefox in private mode.

The Roaming folder is used to store data that will be synced across multiple Windows systems. This is often used for storing settings like bookmarks, saved passwords, and so on.

## How to View the AppData Folder

There are two ways you can access the AppData folder. You can either access it manually or by using the "AppData" variable name.

You can view the AppData folder manually by going into your Users folder, which is there in the C drive. In my case, the path is `C:\Users\ADMIN`.

Next, go to the "View" tab at the top and check the "Hidden items" checkbox, as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_373.png)

Now you should be able to see the AppData folder in your User folder.

You can also access the AppData folder directly using the AppData system variable. Search for "Run" in the windows search as shown below, or press the Windows + R button to open the Run App.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_374.png)

In the run app text box, enter "%AppData%" and click OK. Windows will directly open up the Roaming folder which is inside the AppData folder.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_375.png)

## Wrap up

After reading this guide, I hope you're able to find the AppData folder in your PC. 

Typically, you won't have to worry about the data inside the AppData folder – that is why it is hidden by default. It is only used by application developers to store the necessary data required by the application. 

Everyday Windows users will only need to access or view the AppData folder if they need to create a backup of their application data.

