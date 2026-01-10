---
title: Yes, I coded a Semaphore and no, I am not an OS developer.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T21:06:56.000Z'
originalURL: https://freecodecamp.org/news/yes-i-coded-a-semaphore-and-no-i-am-not-an-os-developer-c721650e1887
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qKfV6Xbz-CAx11Hgd__z5Q.jpeg
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sajal Sarwar Sharma

  When you might be using semaphores in your daily coding life


  Semaphores!


  You are sitting in an 8th standard Mathematics classroom reading about Pythagorean
  Triplets, you are mugging up the Pythagoras Theorem. The famous equat...'
---

By Sajal Sarwar Sharma

#### When you might be using semaphores in your daily coding life

![Image](https://cdn-media-1.freecodecamp.org/images/1*qKfV6Xbz-CAx11Hgd__z5Q.jpeg)
_Semaphores!_

> You are sitting in an 8th standard Mathematics classroom reading about Pythagorean Triplets, you are mugging up the Pythagoras Theorem. The famous equation _(a * a)+ (b * b) = (c * c)_ is etched into your mind_._

> Fast forward 10 years — you still recount that day and wondered why in god’s name you were taught that equation, you never really came across anything practical in life that uses this equation and this makes you question our existing education system.

This is one scenario which makes us wonder whether those educational years of our life were actually worth the effort. A lot of us will agree that a majority of our education isn’t actually helping us in our practical lives.

I am a Software developer working in a SaaS product, and I come up with such revelations that make me contemplate the stark differences between my theoretical knowledge and practical life. But once in a while, things pop up in the most unusual scenarios and places. They make me wonder whether we ignore and don’t really appreciate what’s actually happening under the hood that drives our everyday lives.

### The problem statement

So the story starts when one fine day I was sitting peacefully in my cosy warm corner of the office doing my usual API development. A user ticket popped up that said they had received multiple communications from our service and they were annoyed by it. I double checked the code, but it could not have happened. The cron that runs and sends communication to the end user should only have sent it once (and **this cron runs every hour**).

At the same time I received a pagerduty stating that there was a CPU utilisation surge in my cron server. It usually happens once in a while when there are a lot of jobs to be processed by multiple crons. I casually checked the system, and to my surprise I found the issue that was causing all the havoc and those user tickets.

To my horror, I saw multiple instances of the same communication cron running at the same time, picking the same jobs and sending communications. This explained everything. (This should not have happened — the 1st instance of the cron should have completed its execution before the 2nd instance started running. That’s how cron jobs should work).

That particular day, there was a surge in the number of jobs that the cron should be handling which was causing the cron to keep running way past its usual execution time. This led to the overlap (in other words, it kept running even after an hour, and then the 2nd instance popped up).

My work was cut out for me: I had to make the execution faster, and **never allow multiple instances of the same cron to run simultaneously**.

### The solution

The first thing that popped up in my mind was to implement **Semaphores** (finally those Operating System classes came rushing forward in my memory). My professor was right in saying that one fine day I would use this technique to save my own life.

> _“Today is that day”, I thought._

So I googled and came upon a lot of useful resources to accomplish my task. I will be writing about my learnings here and how finally I realised that I have actually implemented the Semaphore concept all along.

### Step 1

In your system file directory, create a file named **myCronPID.txt** which will store the process ID (PID) of the cron running at that particular instance. According to Wikipedia:

> In computing, the **process identifier** (normally referred to as the **process ID** or **PID**) is a number used by most operating system kernels — such as those of UNIX, macOS and Microsoft Windows — to uniquely identify an active **process**.

### Step 2

Find out the process ID (PID) of the cron running. This can be done using the code below (I will be using PHP for reference).

### Step 3

For the first time, the file **myCronPID.txt** will be empty. Store the current PID obtained in step 2 in this file. The next time, while obtaining the PID of the cron currently running (lets say 5678), get the PID from the file **myCronPID.txt**. The PID obtained from the file (lets say 1234) will be the process ID of the cron instance that was running previously. Check if the PID 1234 is still in the execution/running state. This can be found easily.

In Linux systems, there’s a folder **_/proc_** that has folders for the currently running processes in the system. The name of the folders in this **/proc** folder are the process IDs. So let’s say if **/proc** folder contains a folder **1234,** then it implies that a process with PID 1234 is in running state. If it doesn’t have such a folder, it implies there’s no process with PID 1234 running at that particular instant.

### Step 4

In this step, obtain the PID from myCronPID.txt file and check if the process is still running using the code given in Step 3.

1. If _isProcessRunning_ returns true, then it implies that the previous running cron instance hasn’t completed its execution. Therefore, the new instance which called the function _isProcessRunning_ should not resume with its execution.
2. If _isProcessRunning_ returns false, then it implies the previous cron instance has completed its execution. The new instance which called the function _isProcessRunning_ should resume its execution and put its own process ID in myCronPID.txt

### **Step 5**

Bringing it all together:

In you’re running cron Instance, just invoke the above class object with its appropriate constructor.

**$fileName** — It will be the name of the file which will store the PID of the cron file.

**$rootDir —** It will be the root directory of your current project.

After the invocation, use the methods of the Util in your Cron code as follows:

This will make sure that there won’t be multiple cron instances of the same job running simultaneously.

### Wrapping up

After researching all this and writing the above code, I figured out that I have implemented nothing but Semaphores all along. My OS Professor would have been proud today.

This made me contemplate again: we are just mugging up the concepts. We are not looking into the intricacies of our learnings, but rather we are working on such abstract layers that we don’t take time out to appreciate the beauty of the work that is actually happening under the hood.

Our education system is not always crippled. The way we learn things makes all the difference. Try changing yourself rather than complaining. The world is full of wonders and it’s beautiful.

PS: I hope you like my article, correct me if I am wrong anywhere.

