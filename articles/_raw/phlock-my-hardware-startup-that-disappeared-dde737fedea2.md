---
title: What I learned from Phlock, my hardware startup that disappeared
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T23:04:02.000Z'
originalURL: https://freecodecamp.org/news/phlock-my-hardware-startup-that-disappeared-dde737fedea2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*93fxLukaUzCgI--XtjojUQ.png
tags:
- name: hardware
  slug: hardware
- name: Life lessons
  slug: life-lessons
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tomiwa

  Prior to starting my current company, I founded a startup called Phlock. I built
  a device that let you unlock doors using your phone and share keys with friends
  in real time. Phlock didn’t actually fail, but something much worse happened: i...'
---

By Tomiwa

Prior to starting [my current company](https://atila.ca/), I founded a startup called [Phlock](http://phlock.ca/). I built a device that let you unlock doors using your phone and share keys with friends in real time. Phlock didn’t actually fail, but something much worse happened: it simply disappeared.

Here’s a video of an early prototype:

In the summer of 2017, I came up with the idea for Atila (a platform to search for and apply to scholarships). Without ever actually making a conscious decision, I gradually started spending less time on Phlock and more time on Atila.

By the time school started in the fall, Atila had a fully functional prototype and we were planning on launching soon.

Meanwhile, the Phlock Github repo hadn’t been touched in over 2 months. I had been so busy with Atila, and Phlock was still so obscure, that few people actually knew or cared about it. It had quietly slid into the abyss.

In this article, I’d like to share with you some things I’ve learned from starting a company that disappeared.

* Start with Software - it’s called Hardware for a Reason ?
* Web Apps over Mobile Apps
* Quitting is Underrated
* Share the Journey
* Love the Process

Let’s look at each one in more detail.

### Start with software - it’s called hardware for a reason

One of my biggest lessons is that if you are a first time entrepreneur, you should really consider starting with a software as a service company. There are too many variables in a hardware startup. If it’s your first time starting a company, some of the challenges in hardware will finish your company before you even start. Or worse, after you’ve started.

#### What are the problems?

The single biggest challenge is a lack of iteration speed and the long feedback cycles. When you are starting a company, you need to be able to have a hypothesis, test the hypothesis, and iterate quickly on the response you get.

Starting a company can be so counterintuitive that, most of the time, it’s better to just release something that doesn’t even fully work yet. That way, at least people can show you why it doesn’t work and you can quickly give them a better version.

However, with hardware you typically have a hypothesis based on what the market wants. You work on it for a long period of time, then get feedback on it. The problem is, by the time you get the feedback, your company may no longer have the money, motivation, or market interest to iterate on the feedback.

The other problem with hardware is that there are too many variables that are out of your control. We entrepreneurs like to be masters of our own destiny and captains of our ship, and hardware can turn you into a wimpy leaf. When you start a company, it feels like there are so many little things that can go wrong and your company will fall.

Fortunately, with software companies, you have a lot of control over making a product that the market wants, and that gives you leverage. With software, if something doesn’t work it’s usually your fault. This is actually a liberating feeling. In hardware, there are too many external suppliers, vendors, investors, distributors and so on that have leverage over you and can impact the future of your company.

My friends often pitch me on business ideas they have. When it involves anything hardware-related, and they’ve never started a company before, I often give them the same advice.

Keep the same idea you have, but think of a subset of that problem which could be solved by a purely software solution through a web or mobile app. Build that first, and then once you know you can deliver a tangible product (and, more importantly, make something people want), you can start adding the hardware components to your idea.

### Web apps over mobile apps

If I was to redo Phlock, I would have made the mobile app into a web app or added a “phlock-lite” version that was a web app. This advice is not strictly relevant to Phlock, because there was a hardware component so a native mobile app was necessary. But I think that the future of software will be delivered through web apps over mobile apps.

I wrote another [post](http://blog.tomiwa.ca/building-atila-essential-software-startup-tech-stack/) about this (see the Progressive Web Apps section). The punchline is that web browsers, JavaScript, and web apps are becoming more powerful. But at the same time, people are becoming increasingly reluctant to download new apps from app stores. As a startup, many companies take themselves out of the game, because many people won’t download the app before they can even find out if its bad or good.

### Quitting is underrated

One of the things I learned from Phlock was a new way of thinking about quitting. There were a couple weeks when I kept working on Phlock in the name of “finish what you started” and “never give up.” But this may have been a mistake.

People either quit because something is too hard, or because what they’re doing is taking them down the wrong path. Of course the great Jedi mind trick is that many people quit the right path because it’s too hard, and then they convince themselves that they quit because they were going down the wrong path.

I myself have this issue sometimes. But then I ask myself “If this was easier, would I still want to do it?” I don’t think I consciously knew I was doing it at the time, but in retrospect, that question helped me realize my time was better spent on Atila.

### Share the journey

One thing I wish I did more during my work with Phlock was documenting and sharing more of the thoughts I had and the things I made. I think this is beneficial for two reasons:

1. The serendipity of the Internet has allowed cool opportunities to come out of people finding the things I have shared.
2. Documenting my ideas for future generations to see is pretty cool. I could also use it as a public archive that would give a snapshot of where my head was at the time, and how my thinking has changed.

Finally, I spend a lot of time in open source land and I’m always amazed by the stuff that people create and share on the Internet for free. This is why I think that giving back to the open source community whenever you can is a good thing.

I have open-sourced [some of the code I used to build Phlock](https://github.com/ademidun/phlock-public). I’ve included the Java source code for the Android app that allowed users to share keys with each other in real time, and the code that controlled the microcontroller which locked and unlocked the door deadbolt.

There are a lot of files, and parsing what can and can’t be shared will take a bit of time. So I’ll be sharing the code ad-hoc and based on community interest. If anybody wants me to upload more stuff let me know ([tomiwa@atila.ca](mailto:tomiwa@atila.ca)).

### Love the process

Looking at my folder with all the Phlock code, I have these weird mixed emotions of indifference and concern. I spent so much time and cognitive load on Phlock that leaving it to do something else was kind of sad. But at the same time, I enjoyed building Phlock and I really feel like I left it for a good reason. This is why I feel good about my choice today.

I really enjoyed the day to day grind and process of building Phlock, and the skills that I learned were effectively an investment in whatever I do next. When I have talks with people about career advice, I often ask them to focus on the median emotion of their decision. In other words, ignore the emotional high social validation of a prestigious job, and think of what a regular, unspectacular day and life as an entrepreneur would look like.

Imagine a rainy Monday morning waking up for a full day of work or a quiet Wednesday afternoon in the office. With Phlock, and now with Atila, there are many days where nothing particularly special happens, except “work stuff.” Often those are some of the best days. Finding happiness in normalcy is something that has helped me a lot, and maybe it might help you.

### Final thoughts

This post was more divergent than most of my other essays — and most of my other essays are already quite divergent. However, I think that by covering a wide range of thoughts, everyone can find a little bit of something that will be relevant to them. Thanks for reading, and have a great day.

Originally published at the [Atila Blog](https://atila.ca/blog/tomiwa/phlock-my-hardware-startup-that-disappeared)_._

