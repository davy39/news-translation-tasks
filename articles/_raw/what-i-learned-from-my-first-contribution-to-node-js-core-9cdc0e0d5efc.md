---
title: What I Learned from My First Contribution To Node.js Core
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-26T18:44:36.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-my-first-contribution-to-node-js-core-9cdc0e0d5efc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TMcOrpatfD5sTKioEqsMKg.jpeg
tags:
- name: lessons learned
  slug: lessons-learned
- name: Node.js
  slug: nodejs
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yael Hermon

  A couple of weeks ago my very first PR for Node.js core was merged! A few days later,
  I decided to tweet about it and share how positive this experience was, hoping to
  encourage others to contribute as well.

  Later, Uri Shaked suggested...'
---

By Yael Hermon

A couple of weeks ago my very first PR for Node.js core was merged! A few days later, I decided to tweet about it and share how positive this experience was, hoping to encourage others to contribute as well.

Later, [Uri Shaked](https://www.freecodecamp.org/news/what-i-learned-from-my-first-contribution-to-node-js-core-9cdc0e0d5efc/undefined) suggested I share my experience in a short blog post. Uri always has great ideas. Thanks, Uri!

#### How did I end up with this PR?

I’m glad you asked. Let me start with a little background. I love Node.js, and contributing to it was actually on my bucket list for a really long time. I never got around to doing it because I always told myself that I didn’t have the time for it, or that I might not be qualified enough, or other lame excuses.

The plot twist happened when I was working on a talk for a JavaScript-Israel meetup about the [V8 Garbage Collector](https://docs.google.com/presentation/d/14CVuylg19RUnNLz525ecSHTyN7upVdF196WNtzhqdoA/edit?usp=sharing). [Benjamin Gruenbaum](https://github.com/benjamingr), a Node.js core collaborator, asked me if I would like him to connect me with V8 engineers to review my slides. Umm…_obviously_ I would.

So he did, which turned out pretty awesome. Benji also asked me if I was interested in contributing to Node.js core. Again, I said yes. No more excuses. Stuff just got real.

#### Setting up the environment

I first had to build Node.js on my machine. It was surprisingly easy, thanks to the [great docs](https://github.com/nodejs/node/blob/master/BUILDING.md) Node.js has. Next, I decided to play around and start debugging it.

I’d be lying if I said it was smooth sailing from the start. The last time I worked with C++ was back in 2012. I was rusty. Moreover, back then I had a completely different environment than I have now. I had a Windows PC with Visual Studio on it, while now I am running VSCode on a Mac.

I love VSCode so I wanted to setup VSCode for this project too. I soon found an [extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) and configured things to work. For my debugging configuration, I ended up setting up a node debugger and a lldb debugger to attach to the Node process. That worked great.

#### Working on an actual issue!

So Benji connected me with [Anna](https://github.com/addaleax), who’s the Node.js core collaborator who implemented ‘[worker_threads](https://nodejs.org/api/worker_threads.html)’. Benji also pointed me at this [issue](https://github.com/nodejs/node/issues/24636). I looked at the issue and tried reproducing it with as little code as possible, just to get rid of the noise.

I struggled with creating a test case that reproduced the issue, since it was caused by a race condition. The code that failed when running inside Node.js wouldn’t fail in my testing environment. Eventually, I found something that failed on all of my runs. Although it might not fail on every machine, or every time, Anna confirmed it was good enough. Next, I started debugging it to see what was actually happening there.

If you’ve never heard of ‘worker threads’, that’s probably because they are quite new and are currently in an experimental state. Workers let you create multiple environments running on independent threads. They are useful for performing CPU-intensive JavaScript operations, without blocking the main thread.

The main thread and the worker thread can communicate with each other through a message channel between them. In addition to this message channel, there is another message channel where internal messages are sent, such as stdout of the worker. When you `console.log` inside the worker, it arrives to the main thread through this internal message channel and the main thread handles it by pushing it to its stdout stream.

The problem was that we were calling the `kDispose` function in the JS worker class before waiting for all messages from worker’s stdio to be processed by the main thread through the internal message port. So when the worker thread finished, we lost the references for the parent side stdio streams, and a message to the parent could possibly arrive after that.

At first, I tried lots of different approaches to getting this fixed, including setting a promise to be resolved when the message port was done, awaiting it before disposing, and passing JS callbacks to the C++ layer.

Chatting with Anna about it revealed to me that a _drain_ method existed for the MessagePort and it emitted all its incoming messages synchronously. So in the end, all the messages from it would be processed. In fact, _drain_ was already called for the external MessagePort. How hadn’t I seen this function all this time? ? I added a call to d_rain_ also on the internal MessagePort. The fix was that simple.

An important thing to remember is — it’s totally fine trying out weird approaches along the way. That’s how you learn. And after debugging lots of worker_threads code, I can say that I know some of its codebase pretty well now :)

Benji and Anna were so welcoming right from the beginning. This was a great experience. I learned a lot from Anna and from the code, which was very challenging. It’s definitely not something I usually deal with in my day-to-day.

I can’t wait to work on my next issue!

