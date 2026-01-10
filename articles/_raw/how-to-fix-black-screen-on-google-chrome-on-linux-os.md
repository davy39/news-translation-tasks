---
title: How to Fix Google Chrome Black Screen on Linux OS (Wayland)
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-04-27T19:33:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-black-screen-on-google-chrome-on-linux-os
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Fix---1-.png
tags:
- name: Google Chrome
  slug: chrome
- name: Linux
  slug: linux
- name: Problem Solving
  slug: problem-solving
seo_title: null
seo_desc: 'If you are a Linux user, then you''ve likely used the GNOME Desktop Environment
  at least once.

  The latest GNOME DE (Desktop Environment) uses Wayland nowadays. And while it''s
  possible to remove Wayland and select Xorg if you want, most users are start...'
---

If you are a Linux user, then you've likely used the GNOME Desktop Environment at least once.

The latest GNOME DE (Desktop Environment) uses Wayland nowadays. And while it's possible to remove Wayland and select Xorg if you want, most users are starting to use Wayland as their daily driver. 

And if you still use the Chrome or Chromium browsers, you'll often face the black screen issue during screen sharing.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Untitled-design.png)

If you typically use Wayland on your desktop, you'll have these issues while screen sharing, especially in Google Meet. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Untitled-design--1-.png)

In this article, I will show you a very simple trick that will help you solve the black screen issue during screen sharing on any kind of Chromium browser including the most popular browser, Google Chrome. 

I have used Ubuntu for writing this article, but the same process is applicable to all other Linux OS distros running on Wayland.

## The Black Screen Issue 

If you're having the black screen issue in Google Meet in a Chromium browser (Chrome, Brave, Vivaldi, etc), it probably looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-38-51.png)

Sometimes it might happen because screen sharing in Wayland gets broken or because of other issues. A lot of users also say it happens as developers are trying hard to increase the security level. 

The issue of screen sharing might become common for many people in the usual way. A lot of users go back to X11 only for this issue or try the pipewire solution to fix this.

I will show you the solution using the pipewire technology so that you do not need to go back to X11 only for solving this issue. 😊

Go to **`chrome://flags/#enable-webrtc-pipewire-capturer`** using the address bar of your browser.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-23.png)

You will get a long list, but we are interested in **WebRTC PipeWire Support**. You will see that the option is on the Default mode right now.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-31.png)

We need to change it to **Enabled**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-40.png)

Simply click the drop down menu, and click **Enabled**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-54.png)

Now you will see a prompt on the below right side to relaunch the browser so this can take effect.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-54-1.png)

Click on **Relaunch**. It will simply restart your browser.

The issue has been solved! ✌️

## How to Test Screen Sharing

Now if you want to share your screen as usual, you can definitely do that. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-40-27.png)

Whenever you want to share the screen, a prompt will appear and will request you to select the monitor. You have to share the monitor. If you have only one monitor like I do, then you would get one monitor. Simply click on that and click **Share**. 

You will also get to see the preview of the screen sharing.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-40-40.png)

You may need to select the monitor again in the prompt. Simply select the monitor and click Share as earlier.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-40-47.png)

From now on, you can share your screen on Google Meet from Wayland.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-41-07.png)

## Conclusion

If this article helps you resolve the black screen issue for your Linux DE, then I've been successful. 😊

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

