---
title: How to use a concurrent task queue in your Redux-Sagas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T21:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-concurrent-task-queue-in-your-redux-sagas-39e598c4fcae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8HhqBBy6h6Ag7wO_mqCMug.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Shy Alter

  In this guide, you will learn what a concurrent task queue is, some of the best
  use cases, and how to write one.

  The queue is one of the most used data structures. You probably use it every day
  when you shop for groceries (even online) o...'
---

By Shy Alter

In this guide, you will learn what a concurrent task queue is, some of the best use cases, and how to write one.

The queue is one of the most used data structures. You probably use it every day when you shop for groceries (even online) or when you send a text message to your friends.

The concurrent task queue is a very powerful pattern that can really help you handle tasks over time or improve your performance.

**TL;DR at the bottom**

### Let’s start with the basics

#### What is a Queue? ???‍

A queue is a linear structure in which values are added at one end and removed from the other. This discipline gives rise to a first-in/first-out behavior (FIFO) that is the defining feature of queues. The two fundamental queue operations are enqueue (add to back) and dequeue (remove from the front) ([source](https://stanford.edu/~stepp/cppdoc/Queue-class.html)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Li-9xbwJWffXSSERtTX86g.png)
_Representation of a [wikipedia](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)" rel="noopener" target="_blank" title="FIFO (computing and electronics)">FIFO</a> (first in, first out) queue (<a href="https://en.wikipedia.org/wiki/Queue_(abstract_data_type)" rel="noopener" target="_blank" title="))_

#### Ok, when should we use it?

Use a queue when you need to maintain the order of events and process the value by that order.

#### Great, you convinced me! But why do I need the concurrency thing?

As I mentioned above, a queue is able to process one value at a time. But sometimes it’s not fast enough.

**Consider the following case** ?:

You are at your favorite grocery store and have just arrived at the cashier, but unfortunately there are many people waiting. To speed up the process, the store opened several more registers and each additional cashier has their own queue. So you just have to choose one. If one of the cashiers is having a technical problem or they’re just slow, that queue will be delayed even if the other slots are free.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R4Dvy6CM9tbCiALKvVrshA.png)
_([@andreagiuliaderba](http://twitter.com/andreagiuliaderba" rel="noopener" target="_blank" title="Twitter profile for @andreagiuliaderba))_

Concurrent task queue to the rescue! ?

We will use only one queue for our purposes. In that way, every time a slot becomes free, we will dequeue a person from the queue and send him to the free slot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nidy8yr16nMUBA153rhwEQ.png)
_single concurrent queue ([@andreagiuliaderba](http://twitter.com/andreagiuliaderba" rel="noopener" target="_blank" title="Twitter profile for @andreagiuliaderba))_

**Hooray!** ?

### Now let’s examine a use case

Last week I was working on a Google Chrome extension that sniffs and downloads HLS [streams](https://en.m.wikipedia.org/wiki/HTTP_Live_Streaming) (HTTP Live stream).

HLS streams are combined from multiple chunks that are fetched one by one and streamed to your browser as a single video. You can have thousands of files per stream, and you need to download them all.

We will use our beloved **queue** to speedup the process and make sure that one slow fetch is not gonna hold up the others.

### **TL;DR: here’s the code**

Now let’s look at it piece by piece.

#### 1. The handler

This simple handler gets the URI from the payload and then:

* fetches the chunk
* transforms it to a blob
* emits a **chunk-ready** redux event
* gets the current count of ready chunks
* checks if it’s **“all done”**

#### 2. Create the queue

Using the handler, we create a new queue with **5 workers.** We get back the **watcher** task and a **queue channel.** Then we are going to run (fork) the watcher task so it will start listening to tasks.

#### 3. Push the tasks

We map all the segments to a put task (into the **queue channel** that we got back), and then we fire all the tasks together.

#### 4. Wait for all the chunks to be ready or for the action to be cancelled

Now we are waiting for the first action to be called **all-done** or to be **cancelled.** After that we can cancel the watcher and act according to the action that has been received.

### And that’s it!

If you want to see it live, visit [https://github.com/puemos/hls-downloader-chrome-extension](https://github.com/puemos/hls-downloader-chrome-extension), and download the Chrome extension.

I hope you learned something new! If you have any questions, please comment below so everybody can benefit.

