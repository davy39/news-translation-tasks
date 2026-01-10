---
title: How you can build your own VR headset for $100
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-20T11:44:27.000Z'
originalURL: https://freecodecamp.org/news/build-your-own-vr-headset-for-100-13d6f2b06385
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S7v2UiCN4mJV2Llk98tuCA.jpeg
tags:
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Virtual Reality
  slug: virtual-reality
seo_title: null
seo_desc: 'By Maxime Coutte

  My name is Maxime Peroumal. I’m 16 and I built my own VR headset with my best friends,
  Jonas Ceccon and Gabriel Combe. And it ended up costing us $100.

  I started programming when I was 13, thanks to my math teacher. Every Monday and
  ...'
---

By Maxime Coutte

My name is Maxime Peroumal. I’m 16 and I built my own VR headset with my best friends, Jonas Ceccon and Gabriel Combe. And it ended up costing us $100.

I started programming when I was 13, thanks to my math teacher. Every Monday and Tuesday, my friends and I used to go to his classroom to learn and practice instead of having a meal at the cafeteria.

I spent one year building a very basic 8-bit OS from scratch and competing in robotics contests with my friends.

I then got interested in VR and with my friends we agreed that it would be really cool to create our own world in VR where we could spend time after school. But facing the fact that an Oculus was $700 at the time, we decided to build our own headset.

![Image](https://cdn-media-1.freecodecamp.org/images/RVxl0N2jdbFhf7gESlIURUc0QYT3dPctNRaK)
_3D printed parts of the headset_

### Making VR accessible to everyone?

![Image](https://cdn-media-1.freecodecamp.org/images/F5NUB8PwLFyV9FIyG4IMAXNrju71nMZwbzmw)
_DARROW; J. R. EYERMAN/THE LIFE PICTURE COLLECTION/GETTY IMAGES_

It was because of an anime called _Sword Art Online_ where the main character is in a virtual reality RPG that I fell in love with VR. I wanted to understand every aspect of it.

I bought the cheapest components I could and we started by learning the very basics of the physics and math behind VR (proper acceleration, antiderivatives, quaternions…). And then we re-invented VR. I wrote [WRMHL](https://medium.freecodecamp.org/you-can-now-create-an-arduino-and-unity3d-interactive-experience-without-latency-2d7388dcc0c), and then [FastVR](https://github.com/relativty/fastVR-sdk) with Gabriel. Putting all of this together, we ended up with a $100 VR headset.

![Image](https://cdn-media-1.freecodecamp.org/images/r7lT43yWgmgvO8r8GMeFRz1PSeZQEp2ABZPw)

### A fully hackable VR headset and development kit

To speed up VR development time, we built FastVR, an open-source SDK for developers that is easy to understand and customize. It works like this:

* The core headset computes the position of the headset in space;
* The position is sent from the headset to [**WRMHL**](https://medium.freecodecamp.org/you-can-now-create-an-arduino-and-unity3d-interactive-experience-without-latency-2d7388dcc0c), and part of the CPU’s power is dedicated to reading those messages;
* Then [**FastVR**](https://github.com/relativty/fastVR-sdk) retrieves the data and uses them to render the VR game.

Everything you need to build the headset has been open-sourced and can be hacked.

![Image](https://cdn-media-1.freecodecamp.org/images/-2xejLIdyQa9BFuKKVnrnMsBOGPEaXcBJCgW)

### Why open source?

![Image](https://cdn-media-1.freecodecamp.org/images/lEfatukim7bZsKDWueEyw77FPkqm3WOiWXtR)

I want to make VR mainstream. So I reached out to [Oussama Ammar](https://www.freecodecamp.org/news/build-your-own-vr-headset-for-100-13d6f2b06385/undefined), one of the co-founders at The Family. I talked to him about setting up a company and launching a Kickstarter.

But he convinced me that for now, it’s better to wait on starting a business, to keep meeting others who have the same goals, and to keep learning.

We took a trip to Silicon Valley and Oussama introduced me to the chief architect at Oculus, Atman Brinstock. And they gave me some precious advice: make all of this open source.

### The Next Step?

There are still a lot of technical points that we want to improve.

Our big focus right now is on a standalone VR headset, which we already have as a simple version, and cheaper 3D tracking.

All of this will be released soon.

### How do I get started?

If you want to learn more about the technical side and build your headset, just follow the guide by [**clicking here**](https://github.com/relativty/Relativ). Star the repo if you liked it ⭐️

I would love to hear about what you’ve experienced while building the headset, or if you need any help or have any questions. Ping me at [**maxime@relativty.com**](mailto:maxime@relativty.com) or [@MaximePeroumal](https://twitter.com/MaximePeroumal).

