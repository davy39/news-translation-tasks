---
title: How to Download Applications Fast Using Mirrors On Manjaro Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-11-09T18:57:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-download-application-fast-on-manjaro-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/1631592932_Manjaro-Linux-211-with-fresh-desktop-environments.png
tags:
- name: Linux
  slug: linux
- name: performance
  slug: performance
- name: servers
  slug: servers
seo_title: null
seo_desc: 'If you are running Linux OS, you''ve likely already heard about mirror
  repositories. According to Quora,


  In Linux, a mirror is a copy of programs available for download. If you are close
  (in networking terms, maybe or maybe not geographically) to one...'
---

If you are running Linux OS, you've likely already heard about mirror repositories. According to Quora,

> In Linux, a mirror is a copy of programs available for download. If you are close (in networking terms, maybe or maybe not geographically) to one of the mirror sites listed, you might choose the mirror site as your main source of downloads so you get better response times.


Different Linux-based operating systems have different methods to help you choose the fastest mirrors. But most of the workarounds are pretty much the same.

I've used [Manjaro](https://manjaro.org/) for a pretty long time, and it's one of the most popular Linux-based operating systems out there. So I decided to write this article about it.

As many of us like to use the CLI (Command Line Interface) for downloading the necessary applications and packages in Linux-based operating systems, having a decent internet speed is very useful. Mirror repositories/servers help us with that.

## Why Mirror Servers Are Useful

As Linux is getting more and more popular, there are a lot of servers getting created in various countries that keep the same data that is present in the official servers. 

We call these mirror servers because those servers only mirror (copy) the original data from the original sources and keep those data in their servers. This helps users nearer to them get the data at a decent speed.

Also, these mirror servers/repositories lessen the pressure on the global international servers. 

But keep in mind, all mirror servers might not have a decent reputation for containing malware/non-updated data and so on. The best practice before adding any mirror server is to search on Google/Reddit for that. 

I always prefer the official community on Reddit as I can get legit information from their large user base. 

If you simply search on Reddit, then you'll get countless subreddits for Linux users. Official forums and docs are also really helpful for this information. 

By default, Linux Operating Systems comes with global server/repositories for downloading applications and packages, as they have customers from all over the globe. But if you want to switch to a specific server from where you can download the necessary packages at a decent speed, you can do that manually.

### Mirror Server Use Case

If you are not super familiar with these mirror servers/repositories, let me also provide you with a real-case scenario.

Suppose, you want to download a file, and that file is hosted on multiple servers that are situated in different countries. 

Let's say you are in Bangladesh, and you want to download an application. When you start downloading the application file, it starts downloading from the global international server located in the USA. Naturally, it will take longer to download from that server given the long distance, right?

But it might also be possible that the same application file is also hosted in India, a country near your country. If you download the application file from the Indian server instead, then it will definitely take less time. 

That's because this server is nearer than the other one in the USA – so the distance the data has to travel is smaller. Thus, you can download and get your application file faster.

Now let's see how to enable a mirror server.

## How to Enable the Fastest Mirror on Manjaro Linux

Start by simply opening your terminal. Then apply the following command:

```bash
sudo pacman-mirrors --country all --api --protocols all --set-branch stable && sudo pacman -Syyu
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot_20220318_034726.png)

Enter the password and press the `Enter` key.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot_20220318_034736.png)

It'll take some time depending on your internet speed. Then it will automatically select the fastest mirror it can find for you. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot_20220318_034748.png)

After that, I would suggest that you reboot your PC / logout and log in to the session again. 

That's it! If you want to know more about it, then the [official wiki](https://wiki.manjaro.org/index.php/Pacman-mirrors) is also available for you here.

## Conclusion

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

_The cover image has been taken from [here](https://marketresearchtelecast.com/manjaro-linux-21-1-with-fresh-desktop-environments/155191/)._

