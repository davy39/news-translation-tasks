---
title: Coding With a Chromebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:18:00.000Z'
originalURL: https://freecodecamp.org/news/coding-with-a-chromebook
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9c740569d1a4ca26a5.jpg
tags:
- name: chromebook
  slug: chromebook
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Chromebooks are awesome. They''re relatively simple and inexpensive devices
  that run Chrome OS, a stripped down Linux based operating system developed by Google.

  While they''re perfect for people who just need a web browser to perform basic tasks,
  if y...'
---

Chromebooks are awesome. They're relatively simple and inexpensive devices that run [Chrome OS](https://en.wikipedia.org/wiki/Chrome_OS), a stripped down Linux based operating system developed by Google.

While they're perfect for people who just need a web browser to perform basic tasks, if you're getting into development with just a Chromebook, you might be wondering if it's better to invest in a PC.

But with all the cloud-based technologies and recent updates to Chrome OS, you've got a lot of options. We'll go over a few of the popular ones here.

## Cloud-based solutions

If you're completely new to web development, there's of course [freeCodeCamp.org](https://www.freecodecamp.org/). The entire curriculum can be completed entirely in the browser and by leveraging tools like [CodePen](https://codepen.io/), [CodeSandbox](https://codesandbox.io/), [Glitch](https://www.freecodecamp.org/news/p/633c27ad-f2a2-4b7a-a56b-e85620d957dc/glitch.me), and [Repl.it](https://repl.it/) for more complex projects.

Even experienced developers use one or more of the sites listed above for quick prototyping and for easily sharing their projects with others, all for free. While they might be slower than a native dev environment, the fact that you can access them from any internet connected device and that everything is saved to their servers is a big plus.

## Linux for Chromebooks

As of [Chrome OS v.69](https://9to5google.com/2018/09/18/google-chrome-os-69-stable-release/), you can enable Linux for Chromebooks and install a beta version of the Linux shell on [select Chromebooks](https://www.chromium.org/chromium-os/chrome-os-systems-supporting-linux). Though the list of supported devices is short, most if not all future Chromebooks are expected to [support this feature](https://www.zdnet.com/article/all-chromebooks-will-also-be-linux-laptops-going-forward/).

What basically happens is that Chrome OS runs a version of Debian in a virtual machine. Because Debian is what Ubuntu, a popular Linux distribution/operating system, is based on, you should be able to install anything on your Chromebook like you would on a Debian/Ubuntu machine.

For example, if you want to install Firefox, all you need to do is open up the terminal and enter `sudo apt install firefox`.

There are some disadvantages, though. Currently this feature is in beta, and hardware acceleration is still not supported in non-Chrome OS applications. 

Things like Firefox or VSCode will run slower than on other machines running a Linux distribution like Ubuntu natively. This also means that video decoding is a bit slower, too, and playback may suffer as a result. Also, devices like microphones and webcams are not supported yet.

Check out [this page](https://support.google.com/chromebook/answer/9145439?hl=en) for more information about what's not supported yet.

