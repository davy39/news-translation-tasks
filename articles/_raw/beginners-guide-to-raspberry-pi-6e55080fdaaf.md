---
title: Beginner’s Guide to Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T22:26:53.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-raspberry-pi-6e55080fdaaf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rD9cweBR5NdgFg-l8koTOQ.png
tags:
- name: education
  slug: education
- name: Internet of Things
  slug: internet-of-things
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sean Choi

  It’s the little things that count.


  Raspberry Pi 3 Model B+

  Many question what the term Internet of Things (IoT) means or what it actually represents.
  In simple terms, IoT is a term for categorizing anything that can connect to the
  Inter...'
---

By Sean Choi

#### It’s the little things that count.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rD9cweBR5NdgFg-l8koTOQ.png)
_Raspberry Pi 3 Model B+_

Many question what the term _Internet of Things (IoT)_ means or what it actually represents. In simple terms, _IoT_ is a term for categorizing anything that can connect to the Internet. This includes your Alexa, HomePod, Android watch, Samsung smart refrigerator and many more. Even if you realize that IoT is a term meant to describe a group of little devices that connect to the Internet that talk to each other, it is still rather unclear how these little devices actually do what they do.

In contrast, everyone knows generally what a Macbook or a computer does and what they are capable of doing. Interestingly, the internals of these IoT devices are very similar to the computers that we use everyday, which includes a processing unit, memory, network and/or bluetooth module and some other sensors.

What many people don’t realize is how easy it is to make your own _IoT_ device using a small computer. In fact, you might wonder if there even exists a readily available, cheap, and powerful small computer. The good news is that it actually **exists** and it’s **really** **powerful.**

### Raspberry Pi is EXACTLY That.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzvXMi0Yw0nq3tMRkoSyWQ.png)
_Raspberry Pi 3 (raspberrypi.org)_

[Raspberry Pi](https://amzn.to/2PLBxk1) is a small computer that fits snugly in your hand. Don’t be fooled by it’s size and just look at the hardware specs for the latest (3+) generation Raspberry Pi.

* 1.4 GHz 64-bit quad-core [ARM Cortex-A53](https://en.wikipedia.org/wiki/ARM_Cortex-A53), 1GB RAM
* 2.4/5Ghz dual band 802.11ac Wireless LAN, 10/100/1000Mbps Ethernet
* Bluetooth 4.2
* 4 USB ports, Full HDMI port, Combined 3.5mm audio jack and composite video port, 40 GPIO pins
* Micro SD card slot, VideoCore IV 3D graphics core, Camera interface (CSI), Display interface (DSI),

As you can see, this little beast houses a Quad-Core CPU, fast wireless, bluetooth module and enough RAM to do most things you do on your computer. Better yet, [this only costs $35](https://amzn.to/2PLBxk1), or about a reasonable dinner out (or [3 avocado toasts in SF](https://sf.eater.com/2017/5/23/15677684/avocado-toast-prices-menu-costs-san-francisco)).

Raspberry Pis have an interesting naming convention. They are categorized by a combination of model name and generation. The model names include A, A+, B, B+, Zero and Compute Module (Compute Module is intended mainly for industrial applications, so we won’t touch on it in this article).

Each model is differentiated by available connectors and the size of the main board. There are various generations built so far, which are largely categorized by numbers from 1 to 3. Each generation is mainly differentiated by the chip performance. The latest and the most powerful version is called _Raspberry Pi 3+ Model B+_.

As a reference, here are some images that show what parts are available in each of the models.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sgjYyv_QE0J8ZHyh48mCiQ.png)
_Raspberry Pi Model Zero_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zm0VfWGhkxG_wJPyMTXvNA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*E4pQ7ipQ7hGuMt2kstmORQ.png)
_Raspberry Pi 1 Model A (left), Raspberry Pi 1 Model A+ revision 1.1 (right)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*t0OXJ9YgOHEDDPYn63yPxg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fdW23Z7okJlTkNMyqqT9vQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NjVZqwr3uKVZu_nd1f5d3g.png)
_Raspberry Pi 1 Model B (left), Raspberry Pi 1,2 Model B+ (middle), Raspberry Pi 3Model B+ (right)_

Each model has it’s own tradeoffs. For example, Raspberry Pi Model Zero is the smallest of them all and consumes only 100 mA (0.5W) of power on average. (An average desktop houses a 200~1400W power supply). But, it only houses a single-core CPU, has lower RAM, and lacks a full HDMI port.

However, its smaller size allows it to fit into more spaces, which makes it useful for building devices that are space- and power-constrained. So, having multiple models to choose from increases your options for your project.

### What software does it run?

Unfortunately, Raspberry Pi does not run Mac OS X or Windows. Instead, it runs a version of Linux called [Raspbian](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/). You can choose to install Raspbian on a micro SD card yourself with NOOBS installer, or purchase a pre-loaded micro SD card like one seen [here](http://amzn.to/2DO09P0). Once you plug in the micro SD card with Raspbian installed and turn on the Raspberry Pi, you get the following loading screen:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HBm9igWAM0uNQJdViGyGag.jpeg)
_Raspbian loading screen. Image from [https://alternativeto.net/software/raspbian/](https://alternativeto.net/software/raspbian/" rel="noopener" target="_blank" title=")_

As you can see, the desktop looks just like a regular desktop on your large PC. By default, you get a web browser, terminal, image viewer, calculator and many more features.

Raspbian also lets you install tons of software from it’s own open source software repository at no cost. The process of installing a software is also quite simple. You can utilize the _apt-get_ command, a popular Linux command to install software from various repositories, to install any available software.

For example,`sudo apt-get install scratch2` will install the popular [scratch programming language](https://scratch.mit.edu/). Browse around various repositories and StackOverflow, and you will soon realize you can do just about anything with these devices.

### What can you ACTUALLY do with this?

Ok, so now you have a small computer that runs a bunch of free software. What can you actually do with it? Well, here’s an easy and fun Python project that I have implemented with a group of middle school students as part of a coding class.

Using a [Raspberry Pi compatible temperature/humidity/pressure sensor with LED screen](https://amzn.to/2NCMdwd), I taught the concept of randomness using random colors on the LED screen rather than numbers. My students loved how they could visually and physically interact with their own code. You can see the video of the project here:

Using the same device, we also built a calculator, gaming device, weather station and much more. I found them a very useful and cost efficient way to teach introductory programming to young students. I plan to cover the details of my curriculums in an article some other time.

One of my colleagues at Stanford built a customized Raspberry Pi secured espresso machine to protect our precious coffee. The idea is somewhat similar to a Raspberry Pi secured door lock as seen [here](https://www.youtube.com/watch?v=bAcK80fm1_0).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6oZ2WsV6LCygftHXzgbcig.jpeg)
_Raspberry Pi secured door lock by HackerHouse_

There are many, many articles on using a Raspberry Pi to build fun and useful IoT devices. Here are some list of them I found: [Raspberry Pi Security Camera](https://pimylifeup.com/raspberry-pi-security-camera/), [Raspberry Pi Media Center](https://www.makeuseof.com/tag/kodi-raspberry-pi-media-center/), [Raspberry Pi Code Club](https://projects.raspberrypi.org/en/codeclub).

### Wrapping up

I hope this article gives some basic insights on what Raspberry Pis are, how they are built and what they are used for. Also, I hope this article somewhat demystifies what IoT really means.

In essence, IoT is a movement to connect millions of little things using the Internet, and Raspberry Pi is one of the ways to power those little things. I truly believe that the future lies in IoT and I hope everyone try to participate in bringing it a step closer to us.

> It’s the little things that count, hundreds of ’em.

> — Cliff Shaw.

_This is my first article on Medium! Any comment for corrections, improvements and applauses is greatly appreciated!_

