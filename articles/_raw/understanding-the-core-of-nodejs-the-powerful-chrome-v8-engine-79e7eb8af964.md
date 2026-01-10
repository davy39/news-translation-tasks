---
title: Understanding How the Chrome V8 Engine Translates JavaScript into Machine Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T05:12:25.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-core-of-nodejs-the-powerful-chrome-v8-engine-79e7eb8af964
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T2RkznzWBPFp3JM3L7zx5A.png
tags:
- name: Chromev8
  slug: chromev8
- name: ecmascript
  slug: ecmascript
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mayank Tripathi

  Before diving deep into the core of Chrome’s V8, first, let’s get our fundamentals
  down. All of our systems consist of microprocessors, the thing that is sitting inside
  your computer right now and allowing you to read this.

  Micropr...'
---

By Mayank Tripathi

Before diving deep into the core of Chrome’s V8, first, let’s get our fundamentals down. All of our systems consist of microprocessors, the thing that is sitting inside your computer right now and allowing you to read this.

Microprocessors are tiny machines that work with electrical signals and ultimately do the job. We give microprocessors the instructions. The instructions are in the language that microprocessors can interpret. Different microprocessors speak different languages. Some of the most common are IA-32, x86–64, MIPS, and ARM. These languages directly interact with the hardware so the code written in them is called machine code. Code that we write on our computers is converted or compiled into machine code.

That’s what machine code looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*T2RkznzWBPFp3JM3L7zx5A.png)
_Source : Google_

It consists of instructions that are performed at a particular piece of memory in your system at a low level. You must feel lucky for not having to write all this to run your program!

High-level languages are abstracted from machine language. In the level of abstraction below, you can see how far JavaScript is abstracted from the machine level. C/C++ are relatively much closer to the hardware and hence much faster than other high-level languages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hmr87--VeQ_GyZesKYtEeg.png)

Now back to the V8 engine: V8 is a powerful open source Javascript engine provided by Google. So what actually is a Javascript Engine? It is a program that converts Javascript code into lower level or machine code that microprocessors can understand.

There are different JavaScript engines including [Rhino](https://en.wikipedia.org/wiki/Rhino_(JavaScript_engine)), [JavaScriptCore](https://en.wikipedia.org/wiki/WebKit#JavaScriptCore), and [SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey_(JavaScript_engine)). These engines follow the ECMAScript Standards. ECMAScript defines the standard for the scripting language. JavaScript is based on ECMAScript standards. These standards define how the language should work and what features it should have. You can learn more about ECMAScript [here](https://www.ecma-international.org/publications/standards/Ecma-262.htm).

![Image](https://cdn-media-1.freecodecamp.org/images/1*gZq22sBm1y3eq1NfhEaXeg.png)
_Source: Google_

The Chrome V8 engine :

* The V8 engine is written in C++ and used in Chrome and Nodejs.
* It implements ECMAScript as specified in ECMA-262.
* The V8 engine can run standalone we can embed it with our own C++ program.

Let us understand the last point a little better. V8 can run standalone and at the same time we can add our own function implementation in C++ to add new features to JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PA3QZ_7EWgoDGNyJID_7MA.png)

So for example: `print('hello world')`is not a valid statement in Node.js. It will give error if we compile it. But we can add our own implementation of the print function in C++ on top of the V8 which is open source at [Github](https://github.com/v8/v8), thus making the print function work natively. This allows the JavaScript to understand more than what the ECMAScript standard specifies the JavaScript should understand.

This is a powerful feature since C++ has more features as a programming language as compared to JavaScript, as it is much closer to hardware like dealing with files and folders on the hard drive.

Allowing us to write code in C++ and making it available to JavaScript makes it so we can add more features to JavaScript.

Node.js in itself is a C++ implementation of a V8 engine allowing server-side programming and networking applications.

Let’s now look at some of the open source code inside the engine. To do this, you need to go to the [v8/samples/shell.cc](https://github.com/v8/v8/blob/master/samples/shell.cc) folder.

Here you can see the implementation of different functions such as `Print` and `Read,` which are natively not available in Node.js.

Below, you can see the implementation of the `Print` function. Whenever the `print()` function is invoked in Node.js, it will create a callback and the function will be executed.

Similarly, we can add our own implementation of different new functions in C++ inside V8 allowing it to be understood by Node.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GtV0dm8WOU4l43oK58SHqg.png)

That is certainly too much to grab for a simple statement and that’s the amount of work V8 engine does under the hood.

Now you must have a clear understanding of how Node.js works and what actually is the Chrome V8 engine.

Thanks for reading this article. Let’s follow up on [**Twitter**](https://twitter.com/mayank_408), [**Linkedin**](https://www.linkedin.com/in/mayank-tripathi-a49563126/), [**Github**](https://github.com/mayank408)**,** and [**Facebook**](https://www.facebook.com/profile.php?id=100001106266064).

