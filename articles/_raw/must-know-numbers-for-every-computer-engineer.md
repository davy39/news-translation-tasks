---
title: These are the numbers every computer engineer should know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-14T17:32:57.000Z'
originalURL: https://freecodecamp.org/news/must-know-numbers-for-every-computer-engineer
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/numbers.jpg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: Google
  slug: google
- name: internet
  slug: internet
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kousik Nath

  In 2010, Jeff Dean from Google gave a wonderful talk at Stanford that made him quite
  famous. In it, he discussed a few numbers that are relevant to computing systems.
  Then Peter Norvig published those numbers for the first time on the ...'
---

By Kousik Nath

In 2010, [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean_(computer_scientist)) from Google gave a wonderful talk at Stanford that made him quite famous. In it, he discussed a few numbers that are relevant to computing systems. Then Peter Norvig [published](http://norvig.com/21-days.html) those numbers for the first time on the internet. 

Time passed, and the numbers changed. Here is a very good [interactive web UI](https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html) of those numbers which roughly tells how much they have changed over the years as a function of time.

This article is not only a compilation of Jeff Dean's estimated data, but rather it brings together all such numbers from different sources. This should help you as a system designer and architect. While designing, you can use these numbers to estimate the amount of resources your system needs.

## Rough estimation of latency data for 2019:

1. L1 cache reference: 1 nanosecond.
2. L2 cache reference: 4 nanoseconds.
3. Mutex Lock / Unlock: 17 nanoseconds.
4. Main memory / RAM reference: 100 nanoseconds.
5. Compress 1 KB with Zippy (currently called [Snappy](https://en.wikipedia.org/wiki/Snappy_(compression))): 2000 nanoseconds or 2 microseconds.
6. CPU branch [mispredict](https://en.wikipedia.org/wiki/Branch_predictor): 3 nanoseconds.
7. Solid State Drive (SSD) random read: 16 microseconds.
8. Disk (Hard drive / magnetic drive) seek: 3 milliseconds.
9. Read 1,000,000 bytes sequentially from main memory: 4 microseconds.
10. Read 1,000,000 bytes sequentially from SSD: 62 microseconds.
11. Read 1,000,000 bytes sequentially from disk: 947 microseconds.
12. Round trip network request in same data centre : 500 microseconds.
13. Send 2000 bytes over commodity network: 62 nanoseconds.

## Time Taken for payload to travel over TCP:

Here is the amount of time required to transmit various data payloads on typical cell networks around the world assuming no data loss.

RTT — Round Trip Time — Total time taken for a data packet (bunch of data bytes) to travel from sender to receiver and receiver to sender over the network. In short, it’s called Ping time.

1. Transfer of 1 byte to 13,000 bytes (roughly 13 KB) data takes 1 round trip or 1 RTT. Rough time taken — USA: 150 milliseconds, India: 1200 milliseconds, Brazil: 600 milliseconds.
2. 13,001 bytes — 39,000 bytes (13 KB to 39 KB) takes 2 RTT. Rough time taken — USA: 300 milliseconds, India: 2400 milliseconds, Brazil: 1200 milliseconds.
3. 39,001 bytes — 91,000 bytes (39 KB to 91KB) takes 3 RTT. Rough time taken-USA: 450 milliseconds, India: 3600 milliseconds, Brazil: 1800 milliseconds.
4. 91,001 bytes — 195,000 bytes (91 KB to 195 KB) takes 4 RTT. Rough time taken — USA: 600 milliseconds, India: 4800 milliseconds, Brazil: 2400 milliseconds.

So the greater the response size means more bytes, a longer round trip, more API latency, and ultimately a less user friendly app.

This post will be updated when new or updated numbers are found. Please let me know if you are aware of new numbers.

This article is originally published on Author's [medium wall](https://medium.com/@kousiknath/must-know-numbers-for-every-computer-engineer-6338a12c292c). If you like it, please give claps.

Reference:

1. [https://colin-scott.github.io/blog/2012/12/24/latency-trends/](https://colin-scott.github.io/blog/2012/12/24/latency-trends/)
2. [https://blog.std.in/2015/05/23/http-response-sizes-and-tcp/](https://blog.std.in/2015/05/23/http-response-sizes-and-tcp/)
3. [https://medium.com/@kousiknath/must-know-numbers-for-every-computer-engineer-6338a12c292c](https://medium.com/@kousiknath/must-know-numbers-for-every-computer-engineer-6338a12c292c)

