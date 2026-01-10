---
title: Software impedance explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-07T22:10:27.000Z'
originalURL: https://freecodecamp.org/news/software-impedance-6796cc65758b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8GFgF4KqixGeYwqcExmbjg.png
tags:
- name: Batch Processing
  slug: batch-processing
- name: General Programming
  slug: programming
- name: Signal Processing
  slug: signal-processing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Milan Mimica

  The impedance mismatch between data processing components


  It all starts with the simplest signal-processing diagram ever:


  Component A is passing the signal to component B. Let’s switch to software engineering
  jargon immediately: A p...'
---

By Milan Mimica

#### The impedance mismatch between data processing components

![Image](https://cdn-media-1.freecodecamp.org/images/sRwHZwN9J3U4vil9jWIkjayd65oGcKzKutpu)

It all starts with the simplest signal-processing diagram ever:

![Image](https://cdn-media-1.freecodecamp.org/images/nzzHsg3xL9DOOfkcN47d9rmjuX2Vj4GakPlF)

Component A is passing the signal to component B. Let’s switch to software engineering jargon immediately: A producer is invoking a method of a consumer. Invoking a method takes a finite time. We call this response time or _latency_. The producer can pass an arbitrary (but limited) amount of data to each method invocation. We call this _batch size_. Concurrency level is another variable we can play with. The producer can control the number of concurrent invocations by limiting the _window size_ of pending responses. Invoking the method concurrently indeed multiplies the throughput. Throughput (T) is a function of window size (W), batch size (B) and latency (t).

![Image](https://cdn-media-1.freecodecamp.org/images/DGlIiCyr6ZzXjHEPYYdwadfYBDIZFq7wXnv5)

We aim for maximum throughput, so increase the concurrency and use higher batch sizes. If only! Response time depends on batch size and window size. To put it more formally, response time if a function of both window size and batch size.

![Image](https://cdn-media-1.freecodecamp.org/images/bS5mNpTz-h2fAZj5gfjYhMNJW-y9WFpLlbJX)

To achieve maximum throughput we must find the highest _W_ and _B_ that produce the lowest _t_. Non-ideal _W_ and _B_ will induce a higher “resistance” in the component, or call it _back-pressure_ if you will.

> Whether it produces the data or just passing it through, a producer must adapt window size and batch size to best suit the consumer. Otherwise we have what I call software impedance mismatch.

There is no generic expression for f(W, B) as it depends on the component’s implementation. Theory is of no help here. You have to probe the consumer with different batch and window sizes to spot the ideal values that will maximize the throughput.

Once you find the ideal batch size you must build an “impedance adapter”. Here is a suggested java implementation that accumulates the items and batches them before sending them to the next component (lots of boilerplate code omitted for brevity).

Note that invoking the consumer with smaller than maximum (ideal) batch size is still allowed. This assures no additional latency is added. If the selected batch size is optimal, assuming steady item feed, invoking the consumer will take exactly the time it takes to fill _maxBatchSize_ items in the queue.

Likewise, the number of concurrent method invocations towards some consumer instance can be controlled using a semaphore.

#### Push vs. Pull mode

The above scenario depicts “push” mode, in which the producing component controls the invocation, its timing, and the mentioned key parameters. A more modern approach of dealing with back-pressure is to put the consuming component in charge of the invocation. This puts the system designer in a slightly better position, as engineers of the consuming component don’t need to communicate batch and window size to producers. Nevertheless, a similar impedance adapter is needed.

#### Conclusion

Impedance adapters are stateful components, consisting of queues, threads, callback maps, etc., which adds complexity, but matching impedance is essential in inter-component communication.

I argue that each component should specify its impedance parameters: optimal batch size and concurrency level. That way producer components can adapt to minimize the back-pressure.

Unlike the electrical impedance, the impedance in software is not limited to two dimensions. Here I show only two parameters, but often the response time depends on other variables too.

Impedance is a very dynamic property. It may depend on the data being sent, overall workload, sometimes even on variables not controlled by the caller. If needed, the consumer’s API should be designed in a way that allows the component to publish its latest impedance parameters via API. That way the producers could dynamically adapt.

