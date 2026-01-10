---
title: What is Bonjour on my Computer? Windows 10 Bonjour Program PC Guide
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-02T18:23:02.000Z'
originalURL: https://freecodecamp.org/news/what-is-bonjour-on-my-computer
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/bonjour.png
tags:
- name: configuration
  slug: configuration
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Apple devices work well and connect readily with other Apple devices. But
  they have a hard time communicating with devices running other operating systems
  like Windows and Linux.

  If you have both Apple and Windows devices, you might want to share fil...'
---

Apple devices work well and connect readily with other Apple devices. But they have a hard time communicating with devices running other operating systems like Windows and Linux.

If you have both Apple and Windows devices, you might want to share files between them over a local network. And this is what Apple's Bonjour service makes happen under the hood. 

In this guide, I will take you through what Bonjour is and how you can get it running on your Windows 10 computer.

## What is Apple's Bonjour Program?

Bonjour is Apple's implementation of zero-configuration networking (zeroconf). It allows devices running both Windows and Apple operating systems (like macOS and iOS) to connect and share resources without any configuration settings.

With Bonjour, you can locate other devices such as scanners and printers on a local network and connect with them. You can also share files irrespective of the operating system you are using, whether it's Windows, macOS, or Linux. 

## How Bonjour Works on a Computer

Bonjour is not a regular software product. Unlike other software and apps, you don't get to use Bonjour directly.

Instead, Bonjour runs in the background and connects devices together by using a "link addressing scheme", which automatically assigns IP addresses to devices on a local network.

Examples of apps that use Bonjour include iTunes, Skype, iChat, and iPhoto.


## How to Get Bonjour Up and Running on Windows 10

Unlike Apple devices which work hand in hand with Bonjour, you might have to manually install Bonjour on your Windows 10 computer. 

Bonjour is not available to be downloaded as a standalone app, so you'll need to download an app that uses it. 

It used to come attached with Mac apps such as iTunes and the Safari browser in a zip folder, but these days, the iTunes app may download it for you over a WiFi network.

However, you can install Bonjour for your Windows 10 computer by downloading the Bonjour SDK (Software Development Kit) from the [Apple Developer Website](https://developer.apple.com/bonjour/).

Make sure you select Bonjour SDK for Windows as shown below:
![bonjour-sdk](https://www.freecodecamp.org/news/content/images/2021/11/bonjour-sdk.jpg)

Once you do that, you will have to sign in with your Apple ID. If you don't have one, you can create it.

When you sign in successfully, you will be presented with different versions of Bonjour SDK. Download the one you want and install it by opening up the installer and following the prompts.
![versions](https://www.freecodecamp.org/news/content/images/2021/11/versions.png)

When the Bonjour SDK gets installed, the Bonjour program gets installed with it as well.


## Do you need Bonjour on your Windows 10 computer?

If you use an app that depends on Bonjour to run on a Windows computer, you definitely need Bonjour for the app to function effectively. 

In addition, if you use devices that cut across multiple operating systems such as macOS, Windows, and Linux, you might need to connect them together to share resources such as files and devices – and you'll need Bonjour for that to happen. This will also give you the advantage of zero-configuration.

Lastly, if you don't use an Apple device like a Mac but you have friends who do, you should consider getting Bonjour installed on your device, so you can share files and other resources with them.

## How to Stop or Uninstall Bonjour on Windows 10

If you stop using an app that depends on Bonjour to work, or you want to say goodbye for any other reason, you might want to stop Bonjour. You can do this from the Task Manager.

**Step 1**: Click on Start, or press the `WIN` (Windows) key on your keyboard.

**Step 2**: Search for "task manager" and hit `ENTER`.
![ss-1a](https://www.freecodecamp.org/news/content/images/2021/11/ss-1a.png)

**Step 3**: Click on the Services tab. Here you will see Bonjour Service, which is sometimes available as `"mDNSResponder.exe"`.
![ss-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-1.jpg)

**Step 4**: Right-click on it and select “Stop”.
![ss-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-2.jpg)

### To uninstall Bonjour, you can do it in the Settings app.

**Step 1**: Click on Start, or press the `WIN` (Windows) key on your keyboard, and Select Settings to open the Settings app.
![ss-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-3.jpg)

**Step 2**: Select Apps.
![ss-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-4.jpg)

**Step 3**: On the Apps & Features tab, scroll till you find Bonjour, or search for it.
![ss-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-5.jpg)

**Step 4**: Select uninstall, and again, uninstall.
![ss-6](https://www.freecodecamp.org/news/content/images/2021/11/ss-6.jpg)

Please note that to get rid of the Bonjour service totally, you might have to uninstall the app using it as well. If you installed Bonjour through the Bonjour SDK, make sure you uninstall the Bonjour SDK as well.

## Conclusion

Bonjour is a useful service that gives you more flexibility if you work with devices that use multiple operating systems. 

This guide showed youß what the Bonjour service is, what it does, and how you can have more control over it on your Windows 10 computer.

Thank you for reading. If you find this article helpful, please share it with your friends and family.




