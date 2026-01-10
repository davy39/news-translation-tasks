---
title: 'The next steps on my Outreachy journey: Docker, big challenges, and small
  victories'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T19:03:44.000Z'
originalURL: https://freecodecamp.org/news/the-next-steps-on-my-outreachy-journey-docker-big-challenges-and-small-victories-2c3a2dd2277a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2-_OdNIVPbRBjJKb7OiNgw.jpeg
tags:
- name: Docker
  slug: docker
- name: internships
  slug: internships
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Toni Shortsleeve

  This has been an interesting couple of weeks for me. As a result, I was slightly
  delayed in getting this article out.

  I was recently selected to intern at Outreachy. Outreachy is a program that organizes
  three-month paid internshi...'
---

By Toni Shortsleeve

This has been an interesting couple of weeks for me. As a result, I was slightly delayed in getting this article out.

I was recently selected to intern at Outreachy. Outreachy is a program that organizes three-month paid internships with free and open-source software projects for people who are typically underrepresented in tech.

As an Outreachy intern, I have been tasked with writing about my experience every couple of weeks. This is unique for me, as I am used to editing instead of writing.

In my first [article](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e), I had just been accepted as an [Outreachy](https://www.outreachy.org/) intern working with [LibreHealth](http://librehealth.io/). The next [article](https://medium.freecodecamp.org/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619) discussed my preparation to begin the actual internship after I was accepted. Today, I’ll share where I am at the moment, since the internship began.

### Wanting to learn more

I recently submitted my latest revision of the documentation I’ve been working on, and I am waiting for feedback. Meanwhile, I realized I still didn’t have enough information about the Radiology module and the LibreHealth Toolkit that runs it.

My intern-mate [@adele](https://medium.com/@nguimatiobest) turned me onto a great [blog](https://ivange94blog.wordpress.com/) site. Ivange Larry Ndumbe is a GSOC 2017 intern who worked on the LibreHealth Radiology Module.

A couple of his articles led me in the right direction to help set-up the Toolkit. It turned out that I needed to download Docker. But there was just one problem: I had no idea what Docker was or what it does.

### Some twists and turns

But sometimes, timing is everything. Right around that time, I was fortunate to edit [Let me guide you through your first date with Docker](https://medium.freecodecamp.org/let-me-guide-you-through-your-first-date-with-docker-f03f35567d95) for freeCodeCamp’s Medium publication. This gave a me good introduction to the Docker downloads. Except the Docker Windows download is only for Windows 10.

Do you remember Windows 95, Vista, and XP? My computer does. They were best friends through each new upgrade until Windows 8. I am perfectly happy with much of my software upgrades over the years. But I found that some of my favorites were no longer available after the upgrade. And personally, I’m not impressed enough with Windows 10 to give up my favorite suites. This has been the source of my angst over this past session.

More research led me to the Docker [Toolbox](https://docs.docker.com/toolbox/overview/). But first, the Docker documentation said:

> Make sure your Windows system supports Hardware Virtualization Technology and that virtualization is enabled.

**This was scary.**

![Image](https://cdn-media-1.freecodecamp.org/images/pa-0s9ghXHuagCoD9VBrxNUSX2wLk2X9SlEv)

Back for more research. I (sort of ) found a strategy to enable the Virtualization [here](https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html).

I had to go inside my computer BIOS as it was turning on, and change a code before it fully loaded.

It took a lot of reboots. I had to play with the suggested `F-keys` while being fast enough to catch it before the system totally moved forward in the turning-on phase. Then I repeated the reboot with a different `F-key` until I found the right one at the right time. After going through all those `F-keys` I tried the `Delete` key. Success!

Of course, my switch was hidden in the Advanced Section, and I had to search to find the right commands for it. But the next reboot had my Virtualization Enabled!

### One victory at a time

Now it was time to download the Docker Toolbox. It took a couple of tries, but then I was ready to run the `docker-compose` command. But I forgot to run the command as an Administrator, and my access was denied.

So I ran it again, as Administrator this time. And I received a `File Not Found` error.

Back to the research. The [freeCodeCamp](https://www.freecodecamp.org/) [PairProgrammingWomen](https://gitter.im/FreeCodeCamp/PairProgrammingWomen) chatroom has been great in connecting with me through private message and sending me helpful links. And my tech mentor has been awesome in providing even more helpful links and information.

I’ve finally managed to get the Docker Compose to work! But now I can’t access my localhost. My mentor is continuing to work with me on this. It’s a process.

### Moving forward

I’m going to keep following the suggestion I got from the freeCodeCamp chatroom of using the Read-Search-Ask method. I’m also going to pour over all of those links and continue with creating a manageable Radiology facility.

This will be a great User Guide by the time we finish. Thank you for being with me as I continue my internship journey with Outreachy and LibreHealth journey. Until next time!

