---
title: 'Draconian, free, or nanny state: Concurrency ideologies in Java, C#, C, C++,
  Go, and Rust'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T17:18:18.000Z'
originalURL: https://freecodecamp.org/news/concurrency-ideologies-of-programming-languages-java-c-c-c-go-and-rust-bd4671d943f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9cwOzRARFWi3osKGXCZsSw.jpeg
tags:
- name: concurrency
  slug: concurrency
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Srinath Perera

  Why we need Concurrency

  Once, there was a good old time when clock speed doubled every 18 months. This phenomenon
  was called Moore’s law. If a programmer’s program was not fast enough, they could
  wait, and soon computers would catch...'
---

By Srinath Perera

### Why we need Concurrency

Once, there was a good old time when clock speed doubled every 18 months. This phenomenon was called Moore’s law. If a programmer’s program was not fast enough, they could wait, and soon computers would catch up.

It was too good to last, and it did not. CPU designers still kept up with Moore’s Law by adding more cores to computers.

This created a problem for programmers. In the new world, our programs will run twice as fast every 18 months, but only if it is a parallel program that uses more core.

Hence, for a programmer, the ability to write code in parallel environments is a critical skill. This post explores how different programming languages support parallel and concurrent programs.

### Classical Concurrency Primitives

Almost all operating systems support multiple threads of execution. Concurrent programmers, however, need help to solve two other problems.

* Shared Data — Shared data, if accessed concurrently, may produce unexpected results.
* Signaling between threads — Some use cases need programmers to control the execution order of threads. Other examples are wanting threads to wait at a certain point, wait for another thread, run in specific order, never overtake another thread, and have no more than N threads in the critical region.

Programming languages provide different primitives to aid programmers in controlling the above situations. Let’s take a look at those classical Primitives:

1. Locks (also called Mutex) — ensure that only one thread is executed in selected regions of the code
2. Monitors — they do the same, but slightly better than locks, as they force you to unlock
3. (Counting) Semaphores — powerful abstractions that can support a wide range of coordination scenarios
4. Wait-and-notify — does the same, but is weaker then Semaphores. The programmer has to handle missed notify triggers before the wait
5. Conditional Variables — let a thread sleep and awaken when a given condition occurs
6. Channels and buffers with conditional waiting — listen to and collect messages if there is no thread to receive (with optionally bounded buffers)
7. Non-blocking data structures (such as Nonblocking queue, Atomic counters) — These are clever data structures that allow access from many threads without using locks or a minimal amount of locks.

These primitives overlap on what they can do. Any programming language can get the full power of concurrency with just a few. For example, locks and semaphores can do every concurrency use case you can imagine.

### Language Support for Primitives

The concurrency primitive is not selected just for its power. Different primitives have different programming models. This necessitates different ways of thinking about the problem. Different programming languages have selected different subsets that best match their language model. The choice depends on the designer’s tastes as well as the language’s philosophy.

Let’s explore a few of those choices.

#### Java and C#

Java and C# have chosen not to choose at all. Both support all primitives.

Java first started by only supporting monitors (the **synchronized** keyword) and wait-and-notify. It was a nightmare to send signals across threads. I remember spending hours on “missed signal” and still getting it wrong.

Soon Java designers realized their mistake. They added a concurrency package which has everything including non-blocking data structures.

The only primitive not supported in its pure forms is channels and buffers. However, if you want them, it is easy to mimic channels with queues and buffers. Although your implementation would never match Go or Erlang in performance.

C#, coming late, learned from Java. It also has pretty much everything. C# also has a few higher level helper constructs that Java does not. This solves common problems such as barriers. For more detail, check out the [C# Threading package](https://msdn.microsoft.com/en-us/library/system.threading%28v=vs.110%29.aspx).

### C and C++

C initially depended on operating system calls to do multithreading. Back then code was not portable. Instead, third-party concurrency libraries provided this functionality. Unfortunately, since the language does not pin down the API, there were many libraries available.

Since C and C++ are languages closest to the OS, cutting edge thread research is often done with these two languages. For example, a quick search revealed [22 C++ concurrency](https://en.wikipedia.org/wiki/List_of_C%2B%2B_multi-threading_libraries) libraries and [6 C concurrency libraries](https://stackoverflow.com/questions/5613646/threading-in-c-cross-platform). There is no lack of power.

These libraries provide wide-range and cutting-edge technology. However, due to the diversity of APIs, there are not many programmers who are as proficient with a given API.

### Erlang

Erlang was designed from scratch for concurrency. Erlang gives full control of interactions between threads to the programmer. Programmers do all communications via message passing. This is the source of Erlang’s legendary performance on multi-core computers.

However, there is a price to pay. Erlang does not support sharing state between threads. This is no mistake. Shared state triggers synchronization between threads, which will not be under the programmer’s direct control. Such synchronization often reduces performance.

Consequently, the Erlang programming experience is foreign to most programmers. Its fully functional nature does not help either.

The primary concurrency construct in Erlang is channels. It inbuilt buffers and support for waiting on a condition. For example, you can ask a channel to wait until it receives a message that satisfies a given condition. Each process has one channel, and it can only receive from that channel.

In practice, since Erlang is a functional programming language, shared memory locks are rarely needed. Unfortunately, such use cases exist. Since Erlang does not have shared memory, you can’t lock something. However, you can create a process to represent a lock. You acquire and release a lock by sending messages to the lock just like in a distributed system.

Unless you are a programming language expert who knows functional programming intimately, resulting programs often tend to be complicated and hard to debug. By choosing Erlang, programmers tradeoff concurrency support and familiarity.

If you’d like to know more, read these articles: [Erlang for Concurrent Programming](https://queue.acm.org/detail.cfm?id=1454463) and [The Hitchhiker’s Guide to Concurrency](http://learnyousomeerlang.com/the-hitchhikers-guide-to-concurrency).

### Go

Go is much like Erlang. [Its primary mode of concurrency is through Channel and buffers, and it supports conditional waiting](https://www.golang-book.com/books/intro/10). Its core philosophy for concurrency is: [Do not communicate by sharing memory; instead, share memory by communicating](https://golang.org/doc/effective_go.html#sharing).

There is, however, a fundamental difference. Go trusts you to do the right thing. Go let you share data between threads and supports both [mutexes](https://gobyexample.com/mutexes) and [semaphores](https://github.com/golang/sync/blob/master/semaphore/semaphore.go). Further, they have relaxed the Erlang restriction that each channel is permanently assigned to a thread. You can create a channel and pass it around.

In summary, Go wants us to program concurrency like Erlang. However, while Erlang enforces it, Go trusts you to do the right thing. If Erlang is draconian, Go is a free state.

### Rust

Rust is also much like Erlang and Go. It communicates using channels that have buffers and conditional waiting. Just like Go, it relaxes the restrictions of Erlang [by letting you do shared memory](https://doc.rust-lang.org/book/second-edition/ch16-03-shared-state.html), by supporting atomic reference counting and locks, and by letting you pass channels from thread to thread.

However, Rust goes one step further. While Go trusts you to do the right thing, Rust assigns a mentor who sits with you and complains if you try to do the wrong thing. Rust’s mentor is the compiler. It does sophisticated analysis to determine the ownership of values that are passed around threads and provides compilation errors if there are potential problems.

Following is a quote from the Rust docs.

> The ownership rules play a vital role in message sending because they help us write safe, concurrent code. Preventing errors in concurrent programming is the advantage we get by making the trade-off of having to think about ownership throughout our Rust programs. — [Message passing with ownership of values](https://doc.rust-lang.org/book/second-edition/ch16-02-message-passing.html).

If Erlang is draconian and Go is a free state, then Rust is a nanny state.

Debugging concurrent programs is a nightmare. On a bad day, it can take days. So I appreciate what Rust is trying to do via compiler level analysis.

However, if you are not experienced in concurrency and try to write a concurrent Rust program, it will annoy you. Whatever you do, it will complain about concurrency in cryptic language. When you change, it will say something else, and then again. Until you understand concurrency in detail, it will not be easy.

In contrast, Go gives false security to the programmer, who thinks that their task, often falsely, is done. They might pay for it later. However, they will pay only if the code ever gets to production, if the user ever comes across the scenario, and if that error is detected. That is a lot of “if”s. Although it is unfair, the odds are that the programmer might get away with it. Humans are not that good with [delayed gratification](https://www.psychologytoday.com/us/blog/your-emotional-meter/201712/the-benefits-delaying-gratification) and the [long view](http://www.oxfordaspiremuseums.org/long-view-how-futures-thinking-can-help-us-plan-and-innovate) anyway. So programmers often prefer Go over Rust.

Rust is trying to help, but it is rarely help that gets appreciated. No one likes a nanny state.

> _Rust is not as popular as it deserves to be, because too many short-sighted devs are annoyed by Rust’s strictness, instead of appreciating the immense power they gain from that strictness.” — [rjc2013](https://www.reddit.com/r/rust/comments/8x1myq/concurrency_ideologies_of_programming_languages/e21xwqy/)_

For more information, please read [How the concurrency primitives in Rust compare to the ones in Go](https://news.ycombinator.com/item?id=7851274.)?

### Conclusion

When it comes to concurrency ideologies, programming languages give you a choice: a free state (Go), a draconian state (Erlang), or a nanny state (Rust).

If you’d like to learn more, I would recommend two resources.

First, read the [Little book of semaphores](http://greenteapress.com/wp/semaphores/), which teaches you everything about locks and semaphores.

Second, if you want to understand channels and the Erlang model, [check out MPI](http://mpitutorial.com/). You might think MPI is a dead language. It is not. Most scientific simulations are done to this day with MPI. Weather is predicted by it, vehicles are designed with it, and drugs are discovered with it. Science literally progresses using MPI. MPI uses concurrency in ways we could never imagine. For a taste of it, please check out [MPI Communication Primitives](http://www.mathcs.emory.edu/~cheung/Courses/355/Syllabus/92-MPI/group-comm.html).

If you follow the above two suggestions, you will walk away with an appreciation of the complexity and the possibilities of concurrency. It is a topic that takes a lifetime to master.

I hope this article was useful. I studied these languages while thinking about a concurrency model for Ballerina. Ballerina is a new programming language designed for distributed environments to write microservices and to integrate APIs. It includes new concurrency features, such as adaptive locking. It analyzes the code and tries to hold locks for as short a time as possible. Check it out at [https://ballerina.io.](https://ballerina.io.)

