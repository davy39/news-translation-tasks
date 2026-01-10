---
title: How to use PyCharm to debug your Python code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T16:02:46.000Z'
originalURL: https://freecodecamp.org/news/debugging-with-pycharm-be282bcd6172
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gx9zzO6SmaEn8btnqGxhGw.png
tags:
- name: coding
  slug: coding
- name: debugging
  slug: debugging
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ori Roza

  Debugging code in any language might be frustrating, but it is especially so in
  Python where we cannot recognize a bug immediately.

  In addition, Python provides us with the PDB library as a tool for debugging, which
  can also be difficult ...'
---

By Ori Roza

Debugging code in any language might be frustrating, but it is especially so in Python where we cannot recognize a bug immediately.

In addition, Python provides us with the PDB library as a tool for debugging, which can also be difficult to handle.

Luckily, we have the PyCharm IDE. It uses PyDev and gives us a new experience of debugging!

In this article, I will go over of the main and most useful debugging features PyCharm has to offer and teach you how to use them efficiently.

### **Breakpoints**

Breakpoints might be unnecessary when we are facing a bug which occurs in a certain condition.

Also, when we have a lot of them, it’s a mess.

Fortunately, PyCharm gives us the ability to manage breakpoints in an efficient way:

1. Press Ctrl+Shift+F8 (or Run->View Breakpoints)
2. All the breakpoints that we set on the project will be listed as shown below (see 1)

![Image](https://cdn-media-1.freecodecamp.org/images/IHZir8fKIXc1VaiKH5CGgCkTd5vL-oD0mBhX)

3. As we can see, for each breakpoint we can set a condition that will trigger the breakpoint (see 2)

4. Also, we can set a very special condition which controls whether the breakpoint will be triggered when an exception occurs (see 3) in two different states:

a. On termination (after the script ends)

b. On raise (before the script ends)

![Image](https://cdn-media-1.freecodecamp.org/images/SJGgsckNaq4mVIilo6VIxgdDQqWssYOVUwGa)

### **Attach to local processes**

Have you ever wondered to yourself whether it’s possible to debug a remote process?

**Yes you can**! (and it’s so easy!)

Whether you execute other processes in the background or create them as a part of the flow, PyCharm provides you with a very efficient way to debug remote processes:

1. As shown below, open Run->Attach to Local Process

![Image](https://cdn-media-1.freecodecamp.org/images/oI2Ghz8BzkjVL0eVIio1sQ6U0AUVXzQ1Nw-k)

2. Now choose the Python process you want to be debugged:

![Image](https://cdn-media-1.freecodecamp.org/images/jiRdyqnMR6OkAL2eHmmNugs3Q3bxrPHY5ptz)

3. Then, the process you chose will be debugged in PyCharm:

![Image](https://cdn-media-1.freecodecamp.org/images/lvUB8VZzwEh8qGMO1IaJYJsfxM6vYhU4utBP)

### **Python Interpreter With The Loaded Environment**

Making calculations and manipulating the variables of the current debugged code saves time and allows us to make changes on an actual sandbox!

PyCharm provides us a Python interpreter with the loaded environment.

1. On the console tab, press the marked button:

![Image](https://cdn-media-1.freecodecamp.org/images/mNjPxZPfvIRxBgiGUy4KJE0DqSiFsP28vkhb)

2. As you can see below, the interpreter recognizes our variables!

![Image](https://cdn-media-1.freecodecamp.org/images/gmMkT9W-rclIcNk0gT7zuPJu40ubqLQOkHez)

### **Conclusion**

PyCharm provides us many great tools, and this debugger is one of them.

Debugging can be hard sometimes, but if you use the right tools, it can be easier and even fun!

I hope this article taught you something new, and I am looking forward to your feedback. Please, do tell — was this useful for you?

