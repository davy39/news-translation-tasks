---
title: Asynchronous-IO vs Asynchronous-Request Processing in java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T17:24:24.000Z'
originalURL: https://freecodecamp.org/news/java-async-io-async-request-processing-in-http-request-1a04f395d8c7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5htxZQ3yUYwLMuoHND11ug.png
tags:
- name: asynchronous
  slug: asynchronous
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: Sockets
  slug: sockets
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Bhuvan Gupta

  In this article, I am trying to explain the difference between Async-IO and Async-Request
  processing in the HTTP request in the Java world.

  In the pre-Java 1.4 world, Java provides an API to send/receive data over the network
  socket. ...'
---

By Bhuvan Gupta

In this article, I am trying to explain the difference between Async-IO and Async-Request processing in the HTTP request in the Java world.

In the pre-Java **_1.4_** world, Java provides an API to send/receive data over the network socket. The original authors of JVM mapped this API behavior to OS socket API, almost one to one.

So, what is the OS socket behaviour? OS provides [Socket programming api](https://www.csd.uoc.gr/~hy556/material/tutorials/cs556-3rd-tutorial.pdf), which has send/recv **blocking call**. Since java is just a process running on top of linux(OS), hence this java program has to use this blocking api provided by OS.

The world was happy and java developers started using the API to send/receive the data. But they had to keep one java thread for every socket(client).

Everybody was writing their own flavor of HTTP servers. Code sharing was becoming hard, the java world demanded a standardization.  
**Enters the java servlet Spec.**

Before moving on lets define few terms:

**Java Server Developer**: People who are using the java socket api and implementing http protocol like tomcat.

**java Application Developer:** People who are building buisness application on top of tomcat.

GETTING BACK NOW

Once the java servlet spec entered the world, it said:

_Dear java server developers,_ please provide a method like below:

```
doGet(inputReq, OutPutRes)
```

so that _java application developer_ can implement `doGet` and they can write their business logic. Once _“application developer”_ wants to send the `response`, he can call `OutPutRes.write().`

**A thing to Note:**Since socket api is blocking, hence OutPutRes.write() is also blocking. Also, the additional limitation was that the response object is committed on **doGet method** exit.

Due to these limitations, people had to use one thread for processing one request.

Time passed and the internet took over the world. [_one Thread per Request_](https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request) started to show limitations.

### Problem 1:

The [thread-per-request](https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request) model fails when there are long pauses during the processing of each request.

> _For Example: fetching data from sub-service take long time._

Under such a situation, the thread is mostly sitting idle and JVM can run out of thread easily.

### Problem 2:

Things got even worse with [http1.1 persistent connection](https://en.wikipedia.org/wiki/HTTP_persistent_connection). As with persistent connection, the underlying TCP connection will be kept alive and the server has to block _one thread per connection._

> _But why does the server have to block_ one thread per connection?  
> _Since OS provides a blocking socket Recv api, the jvm has to call the OS blocking Recv method in order to listen for more requests on same tcp connection from the client._

### **The world demanded a solution!**

**The First Solution** came from the creator of JVM. They introduced [NIO(**ASYNC-IO**)](https://en.wikipedia.org/wiki/Non-blocking_I/O_(Java)). Nio is the non-blocking API for sending/receiving data over socket.

**Some background:** the OS along with blocking socket api also provides a non-blocking version of the socket api.

But how does the OS provide that .. Does it fork a thread internally and that thread gets blocked???

The ANSWER is no… the OS instruct the hardware to interupt when there is data to read or write.

NIO allowed the _“**java server developer”**_ to tackle **problem 2** of blocking _one thread per TCP connection_. With NIO being an HTTP persistent connection, the thread does not require it to block on _recv_ call. Instead, it can now process it only when there is data to be processed. This allowed one thread to monitor/handle a large number of persistent connections.

**The Second Solution** came from servlet spec. Servlet Spec got an upgrade and they introduced [**async support**](https://docs.oracle.com/javaee/7/tutorial/servlets012.htm) **(Async Request Processing).**

```
AsyncContext acontext = req.startAsync();
```

> **_IMPORTANT:_** _This upgrade removed the limitation of committing the response object on **doGet** method completion._

This allowed the “**_Java Application Developer”_** to tackle **Problem 1,** by offloading work to background threads. Now instead of keeping the thread waiting during the long pause, the thread can be used to handle other requests.

### CONCLUSION:

_Async-IO_ in java is basically using the non-blocking version on OS socket API.

_Async request processing_ is basically the servlet spec standardization of how to process more requests with one thread.

### REFERENCES:

[https://www.scottklement.com/rpg/socktut/tutorial.pd](https://www.scottklement.com/rpg/socktut/tutorial.pdf)f  
[https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request](https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request)

> _Motivation of article: Team Learning/Knowledge Sharing_

