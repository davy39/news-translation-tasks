---
title: RTC Connecting Discord – How to Fix the Server Error
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-02T17:10:47.000Z'
originalURL: https://freecodecamp.org/news/rtc-connecting-discord-how-to-fix-the-server-error
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Discord.png
tags:
- name: Chat
  slug: chat
- name: discord
  slug: discord
- name: messaging
  slug: messaging
seo_title: null
seo_desc: 'Discord is an instant messaging app that lets you communicate through voice,
  video, and texts. It is available in a web-based form, a desktop app, and a mobile
  app.

  But sometimes, when you''re trying to establish a voice call connection, you''ll
  get an...'
---

Discord is an instant messaging app that lets you communicate through voice, video, and texts. It is available in a web-based form, a desktop app, and a mobile app.

But sometimes, when you're trying to establish a voice call connection, you'll get an error that says “RTC Connecting Discord”. This message will keep showing without any meaningful progress.

So what does this error mean?

Discord uses the Real-time Chat protocol (RTC) to run concurrent communication. So if you are experiencing the “RTC Connecting Discord” problem, it is a network issue.

In this article, I will show you 5 changes you can make to your network configurations to fix the RTC Connecting Discord issue. 3 of the fixes involve your computer network settings, while the remaining 2 happen right in your Discord app. 

## How to Fix RTC Connecting Discord by Updating your Network Driver

If your device relies on an outdated network adapter driver for internet connections, it could have a negative effect on your internet experience – and could cause this issue as well. 

So, updating your network driver can fix the issue.

**The steps below take you through how you can update your network adapter driver.**

**Step 1**: Click on Start (Windows logo) and search for "device manager". Hit `ENTER` to open the first search result – which is always Device Manager. You can click on the "Device Manager" search result, too.
![ss-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-1.jpg)

**Step 2**: Expand "Network Adapters."

**Step 3**: Look for the adapter in use, right-click on it and select "update driver".
![ss-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-2.jpg)

**Step 4**: Select "Search automatically for drivers".
![ss-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-3.jpg)

Windows will now search the internet for an updated driver and install it for you.

## How to Fix RTC Connecting Discord by Changing your Domain Name Server 

A domain name server (DNS) is assigned to you by your ISP (Internet Service Provider). Domain name servers make it possible to reach websites by typing addresses (URLs) to the browser instead of some unreadable numbers.

Changing this DNS to a widely used DNS like that of Google or Cloudflare can help you fix the RTC Connecting Discord issue.

**To change your DNS to Google’s, follow the steps below.**

**Step 1:** Right-click on Start and choose “Run” to open the Run dialogue.
![ss-4](https://www.freecodecamp.org/news/content/images/2021/12/ss-4.jpg)

**Step 2**: Type in `“Control ncpa.cpl”` (without quotes) and hit `ENTER`. This will open up your network connection devices.
![ss-5-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-5-2.png)

**Step 3**: Right-click on your current network and select “Properties”.
![ss-6-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-1.jpg)

**Step 4**: Look for Internet Protocol Version 4 (TCP/IPv4) and double-click it.
![ss-7](https://www.freecodecamp.org/news/content/images/2021/12/ss-7.jpg)

**Step 5**: Click on the “Use the following DNS server address” radio button and type in the following values:
- 8.8.8.8 for Preferred DNS Server
- 8.8.4.4 for Alternate DNS Server

![ss-8](https://www.freecodecamp.org/news/content/images/2021/12/ss-8.jpg)

**Step 6**: Click Ok.

Complete the setup with the next fix.

## How to Fix RTC Connecting Discord by Clearing your Computer Network Cache in the Command Line

If you’re using the web-based Discord, this fix can work for you.

You can clear your network cache on your browser, but a more effective way to do it is to clear it right on your Windows 10 computer in the command line.

The steps below show you how to do it.

**Step 1**: Hit the `WIN` (Windows logo) key on your keyboard and search for "cmd". 

You have to use the Command Prompt as an administrator, so you should select "Run as Administrator" on the right instead of just hitting `ENTER` to open it.

**Step 2**: Enter and execute the following commands one after the other:

- `ipconfig /release`
- `ipconfig /flushdns`
- `ipconfig /renew`

**Step 3**: Restart your computer.
![ss-9](https://www.freecodecamp.org/news/content/images/2021/12/ss-9.png)

![ss-10](https://www.freecodecamp.org/news/content/images/2021/12/ss-10.png)


## How to Fix RTC Connecting Discord by Disabling QoS

Discord’s QoS (Quality of Service) communicates to your router that the units of data being transmitted are of high priority. This could make your router misbehave, and cause the RTC Connecting Discord issue. 

So, disabling the QoS might fix it for you in case you have it enabled.

**Follow the steps below to disable QoS on Discord**.

**Step 1**: Launch Discord, then click on Settings on the bottom left corner. 
![ss-11](https://www.freecodecamp.org/news/content/images/2021/12/ss-11.jpg)

**Step 2**: Select Voice and Video on the left panel.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/12/ss-12.jpg)

**Step 3**: Scroll down to the QoS section and disable it.
![ss-13](https://www.freecodecamp.org/news/content/images/2021/12/ss-13.jpg)

**Step 4**: Restart the Discord app.

## How to Fix RTC Connecting Discord by Changing the Audio Subsystem in Discord

In Discord, the Legacy audio subsystem has always been suggested as the best because it is the highest quality compared to the Standard and Experimental audio subsystems.

Changing your Audio subsystem to Legacy can make you establish quality audio – which can end up fixing the RTC Connecting Discord issue.

**These steps take you through how to change your Audio subsystem to Legacy**.

**Step 1**: Open Discord and click on Settings on the bottom left corner.  
![ss-11](https://www.freecodecamp.org/news/content/images/2021/12/ss-11.jpg)

**Step 2**: Select Voice and Video.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/12/ss-12.jpg)

**Step 3**: Scroll down to the Audio Subsystem dropdown and select “Legacy”.
![ss-14](https://www.freecodecamp.org/news/content/images/2021/12/ss-14.jpg)

**Step 4**: Restart Discord. 

## Conclusion

This article showed you how you can fix the RTC Connecting Discord problem you might experience when you are trying to use Discord's audio call feature.

Apart from the solutions explained in this article, you can try other minor fixes such as: 
- Restarting your devices – computer and router
- Double-checking internet connection
- Using a VPN

Thanks a lot for reading this article. If you find it helpful, share it with your friends and loved ones.


