---
title: Discord Won't Open on my PC [Solved in Windows 10]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-09T14:57:04.000Z'
originalURL: https://freecodecamp.org/news/discord-wont-open-on-my-pc-solved-in-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Discord.png
tags:
- name: Chat
  slug: chat
- name: discord
  slug: discord
- name: how-to
  slug: how-to
- name: Problem Solving
  slug: problem-solving
seo_title: null
seo_desc: "Discord is an instant messaging app you can use to communicate through\
  \ text messages, voice calls, and video calls. You can also use it to share files.\
  \ \nDiscord was originally created for gamers, but many other people now use it\
  \ these days. It has be..."
---

Discord is an instant messaging app you can use to communicate through text messages, voice calls, and video calls. You can also use it to share files. 

Discord was originally created for gamers, but many other people now use it these days. It has become an alternative to Slack for many users – especially for those who want to have an online community.

But sometimes, Discord might not open when you launch it. This could be due to pending updates, running games, and other causes.
 
In this article, I will show you 5 quick ways you can make Discord open again on a Windows 10 computer.

## Table of Contents
- [How to Fix Discord Not Opening in the Command Line](#heading-how-to-fix-discord-not-opening-in-the-command-line)
- [How to Fix Discord Not Opening by Clearing AppData](#heading-how-to-fix-discord-not-opening-by-clearing-appdata)
- [How to Fix Discord Not Opening by Clearing LocalAppData](#heading-how-to-fix-discord-not-opening-by-clearing-localappdata)
- [How to Fix Discord Not Opening by Closing Background Applications](#heading-how-to-fix-discord-not-opening-by-closing-background-applications)
- [How to Fix Discord Not Opening with the Task Manager](#heading-how-to-fix-discord-not-opening-with-the-task-manager)
- [Conclusion](#heading-conclusion)

## How to Fix Discord Not Opening in the Command Line

The number one fix I would recommend to make Discord open again is to kill the Discord task with the Command Prompt.

This is how to do it:

**Step 1**: Click on Start or press `WIN` (Windows key) on your keyboard, then search for "cmd".

**Step 2**: Hit `ENTER` or select the first search result to open the Command Prompt.

![ss-1-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-1-5.jpg)

**Step**: Type in `taskkill /F /IM discord.exe` and hit `ENTER`.

You should get a message that the Discord process has been terminated.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-2-1.png)


## How to Fix Discord Not Opening by Clearing AppData

When you clear an app's AppData, all cache files are cleared – which can fix some problems, including loading.

Go through the following steps to clear your Discord's AppData:

**Step 1**: Press `WIN` (Windows key) + R to open the Run dialogue.

**Step 2**: Type in "%appdata%" (without quotes) and press `ENTER` on your keyboard. This will open up the AppData folder.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-3-1.png)

**Step 3**: Locate the Discord folder and delete it. Delete it from your Recycle Bin too.
![ss-4-6](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-6.jpg)

## How to Fix Discord Not Opening by Clearing LocalAppData

Clearing the Discord's LocalAppData can make it open again. It can also fix the common JavaScript error associated with Discord as well. 

To clear LocalAppData, follow these steps:

**Step 1**: Press `WIN` (Windows key) + R to open the Run dialogue.

**Step 2**: Type in "%localappdata%" (without quotes) and press `ENTER` on your keyboard. This will open up the LocalAppData folder.
![ss-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-5.png)

**Step 3**: Look for the Discord folder and delete it. Go to your Recycle Bin and delete it too.
![ss-6-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-5.jpg)

Note that you might have to reinstall Discord to get it running again after clearing its LocalAppData. I can attest that this solves the issue as I recently had to do it.

## How to Fix Discord Not Opening by Closing Background Applications

A lot of games run in the background and this could have a negative effect on your Discord app.

Use the steps below to fix the issue only if you don't have useful apps running in the background.

**Step 1**: Click on Start or press `WIN` (Windows key) on your keyboard and select Settings.
![ss-7-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-7-1.jpg)

**Step 2**: Select "Privacy".
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-8-2.jpg)

**Step 3**: Click on Background apps on the left, then turn off the toggle under "Let apps run in the background".
![ss-9-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-9-1.jpg)

## How to Fix Discord Not Opening with the Task Manager

Stopping the Discord process with the Task Manager can make Discord open again as this refreshes the app.

**Step 1**: Press `CTRL` + `SHIFT` + `ESC` to open the Task Manager

**Step 2**: Make sure you are under the `Processes`. Right-click on Discord and select "End Task". 
![ss-10-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-10-2.jpg)

## Conclusion

In this article, you learned how to fix Discord when it won't open in a few different ways.

Apart from the methods discussed in this guide, you can also fix the issue by uninstalling and reinstalling Discord. 

Note that you can also fix another popular issue with Discord – JavaScript error – by using one of the fixes suggested in this article – clearing LocalAppData. I've had to do this myself.

Thanks a lot for reading. If you find this article helpful, consider sharing it with your friends. That's very much appreciated.


