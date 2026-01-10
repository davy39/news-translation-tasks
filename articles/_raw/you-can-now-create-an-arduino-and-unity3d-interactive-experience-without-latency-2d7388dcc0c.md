---
title: Create an Arduino and Unity3D interactive experience with no latency !⏱
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-16T13:35:22.000Z'
originalURL: https://freecodecamp.org/news/you-can-now-create-an-arduino-and-unity3d-interactive-experience-without-latency-2d7388dcc0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GYnriIV-IBFyGDDIHjbQBA.gif
tags:
- name: arduino
  slug: arduino
- name: DIY
  slug: diy
- name: open source
  slug: open-source
- name: technology
  slug: technology
- name: Unity3D
  slug: unity3d
seo_title: null
seo_desc: 'By Maxime Coutte

  Hi, I’m 16 years old and during the holidays I like to work on little projects.
  I grew up in a very artistic environment - my father is a painter my brothers and
  sisters draw, play music, compose … And me, with my best friend we want...'
---

By Maxime Coutte

Hi, I’m 16 years old and during the holidays I like to work on little projects. I grew up in a very artistic environment - my father is a painter my brothers and sisters draw, play music, compose … And me, with my best friend we wanted to have fun with our new Arduino and Unity3D, so we started working on interactive artistic experiences. But we got stuck on one big thing. If you’ve ever wanted to transmit data from Arduino to Unity3D, you know the main issue is **INSANE LATENCY**.

#### Don’t worry about Latency, [wrmhl](https://github.com/relativty/wrmhl) is here ⚡️

![Image](https://cdn-media-1.freecodecamp.org/images/Eq8d7WJ-2ZRuoAtYB-3UtzLDkFKivnwklyUc)
_Without wrmhl (using a simple ReadLine () )_

We didn't find any free, optimized, and customizable solutions to tackle this problem. So I built [**wmrhl**](https://github.com/relativty/wrmhl). You can now connect any Arduino interface to Unity3D, and it’s completly **Open Source.**

* Just write your Arduino code, how about [A Touchless 3D Tracking Interface](https://www.youtube.com/watch?v=ikD_3Vemkf0) or a [Brain-Computer Arduino Interface](http://openbci.com/) ?
* Add a Serial print to send data from your interface to Unity3D ([see examples](https://github.com/relativty/wrmhl/blob/master/Arduino/Arduino.ino))
* Import wrmhl to Unity, and voilà!

You can use the default wrmhl protocol, or implement your own in a minute just by changing: [wrmhl/Assets/WRMHL/Scripts/Thread/wrmhlThread_Lines.cs](https://github.com/relativty/wrmhl/blob/master/Assets/WRMHL/Scripts/Thread/wrmhlThread_Lines.cs).

#### How to get started ?

just follow the guide by [**clicking here**](https://github.com/relativty/wrmhl#getting-started-%EF%B8%8F). Star the repo if you liked it ⭐️

Hope this is helpful! If you’re using it, would love to hear about what you’re building. Ping me at **maxime@relativty.com** or [@maximecoutte](https://twitter.com/maximecoutte).

