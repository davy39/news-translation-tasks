---
title: An introduction to Vert.x, the fastest Java framework today
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T16:52:04.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-vert-x-the-fastest-java-framework-today-27d8661ceb14
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RovqxSyUULpHDMxwYGXQPA.png
tags:
- name: Java
  slug: java
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Martin Budi

  If you’ve recently googled “best web framework” you might have stumbled upon the
  Techempower benchmarks where more than three hundred frameworks are ranked. There
  you might have noticed that Vert.x is one of the top ranked, if not the ...'
---

By Martin Budi

If you’ve recently googled “best web framework” you might have stumbled upon the Techempower benchmarks where more than three hundred frameworks are ranked. There you might have noticed that Vert.x is one of the top ranked, if not the [first](https://www.techempower.com/benchmarks/#section=data-r17&hw=cl&test=fortune) by some measures.

So let’s talk about it.

Vert.x is a polyglot web framework that shares common functionalities among its supported languages Java, Kotlin, Scala, Ruby, and Javascript. Regardless of language, Vert.x operates on the Java Virtual Machine (JVM). Being modular and lightweight, it is geared toward microservices development.

Techempower benchmarks measure the performance of updating, fetching and delivering data from a database. The more requests served per second, the better. In such an IO scenario where little computing is involved, any non-blocking framework would have an edge. In recent years, such a paradigm is almost inseparable from Node.js which popularized it with its single-threaded event loop.

Vert.x, like Node, operates a single event loop. But Vert.x also takes advantage of the JVM. Whereas Node runs on a single core, Vert.x maintains a thread pool with a size that can match the number of available cores. With greater concurrency support, Vert.x is suitable for not only IO but also CPU-heavy processes that require parallel computing.

Event loops, however, are half of the story. The other half has little to do with Vert.x.

To connect to a database, a client requires a connector driver. In the Java realm, the most common driver for Sql is JDBC. The problem is, this driver is blocking. And it’s blocking at the socket level. A thread will always get stuck there until it returns with a response.

Needless to say, the driver has been a bottleneck in realizing a fully non-blocking application. Fortunately there has been progress (albeit unofficial) on [an async driver](https://github.com/mauricio/postgresql-async) with several active forks, among them:

* [https://github.com/jasync-sql/jasync-sql](https://github.com/jasync-sql/jasync-sql) (for Postgres and MySql)
* [https://github.com/reactiverse/reactive-pg-client](https://github.com/reactiverse/reactive-pg-client) (Postgres)

#### **The golden rule**

Vert.x is pretty simple to work with, and an http server can be brought up with a few lines of code.

<script src="https://gist.github.com/inmyth/aeab72a71cb6afa05b4ba93776c8fbf6.js"></script>

The method requestHandler is where the event loop delivers the request event. As Vert.x is un-opinionated, handling it is free style. But keep in mind the single important rule of non-blocking thread: don’t block it.

When working with concurrency we can draw from so many options available today such as Promise, Future, Rx, as well as Vert.x’s own idiomatic way. But as the complexity of an application grows, having async functionality alone is not enough. We also need the ease of coordinating and chaining calls while avoiding callback hell, as well as passing any error gracefully.

Scala Future satisfies all the conditions above with the additional advantage of being based on functional programming principles. Although this article doesn’t explore Scala Future in depth, we can try it with a simple app. Let’s say the app is an API service to find a user given their id:

<script src="https://gist.github.com/inmyth/3df58e683efb0b66e9123a536a5cb171.js"></script>

There are three operations involved: checking request parameter, checking if the id is valid, and fetching the data. We will wrap each of these operations in a Future and coordinate the execution in a “for comprehension” structure.

* The first step is to match the request with a service. Scala has a powerful pattern matching feature that we can use for this purpose. Here we intercept any mention of “/user” and pass it into our service.
* Next is the core of this service where our futures are arranged in a sequential for-comprehension. The first future **f1** wraps parameter check. We specifically want to retrieve the id from the get request and cast it into int. (Scala doesn’t require explicit return if the return value is the last line in the method.) As you see, this operation could potentially throw an exception as id might not be an int or not even available, but that is okay for now.
* The second future **f2** checks the validity of id. We block any id lower than 100 by explicitly calling Future.failed with our own CustomException. Otherwise we pass an empty Future in the form of Future.unit as successful validation.
* The last future **f3** retrieves the user with the id provided by **f1.** As this is just a sample, we don’t really connect to a database. We just return some mock string.
* **map** runs the arrangement that yields the user data from **f3** then prints it into the response.
* Now if in any part of the sequence an error occurs, a Throwable is passed to **recover**. Here we can match its type to a suitable recovery strategy. Looking back in our code, we have anticipated several potential failures such as missing id, or id that was not int or not valid which would throw specific exceptions. We are handling each of them in handleException by passing an error message to client.

This arrangement provides not only an asynchronous flow from the start to the end but also a clean approach to handling errors. And as it is streamlined across handlers we can focus on things that matter, like database query.

#### **Verticles, Event Bus, and other gotchas**

Vert.x also offers a concurrency model called verticle which resembles the Actor system. (If you’d like to learn more, head over to my [Akka Actor guide](https://medium.freecodecamp.org/still-using-synchronized-try-akka-actor-instead-ac2f2b22a9ed).) Verticle isolates its state and behavior to provide a thread-safe environment. The only way to communicate with it is through an event bus.

However, the Vert.x event bus requires its messages to be String or JSON. This makes it difficult to pass arbitrary non-POJO objects. And in a high performance system, dealing with JSON conversion is undesirable as it imposes some computing cost. If you are developing IO applications, you may be better off not using either verticle or event bus, as such applications have little need for local state.

Working with some Vert.x components can also be pretty challenging. You might find lack of documentation, unexpected behavior, and even failure to function. Vert.x might be suffering from its own ambition, as developing new components would require porting across many languages. This is a difficult undertaking. For that reason sticking to the core would be the best.

If you are developing a public API, then vertx-core should be enough. If it’s a web app, you may add vertx-web which provides http parameter handling and JWT/Session authentication. These two are the ones that dominated the benchmarks anyway. There is some decrease in performance in some tests for using vertx-web, but as it seems to have stemmed from optimization, it might get ironed out in the subsequent releases.

