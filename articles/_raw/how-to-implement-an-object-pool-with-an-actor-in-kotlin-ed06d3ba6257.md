---
title: How to implement an Object-Pool with an Actor in Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T19:33:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-an-object-pool-with-an-actor-in-kotlin-ed06d3ba6257
coverImage: https://cdn-media-1.freecodecamp.org/images/0*0aDugHie8xlGjhOZ
tags:
- name: actor model
  slug: actor-model
- name: concurrency
  slug: concurrency
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By osha1

  We use object pool in jasync-sql to manage connections to the database. In this
  post, I will share how it is done in a performant, lock-free manner using Kotlin
  coroutines with an Actor.

  An object pool has a very simple API to work with. It ...'
---

By osha1

We use object pool in [jasync-sql](https://github.com/jasync-sql/jasync-sql) to manage connections to the database. In this post, I will share how it is done in a performant, lock-free manner using Kotlin coroutines with an Actor.

An object pool has a very simple API to work with. It is a pool of objects with two methods: `take()` and `return()`.

On first sight it looks like a very simple problem. The main catch here is that it has to be both performant and thread-safe, and that’s what makes it interesting and tricky to implement.

### But hey! Why do we need an object pool anyway?

[jasync-sql](https://github.com/jasync-sql/jasync-sql) is a library to access relational databases like MySQL and PostgreSQL. Database connections are a great example of the need for object pools. The access to the database is done by obtaining a connection from a **Connection-Pool**, using it and returning it back to the pool.

With a connection pool we get a couple of advantages over creating connections per each SQL query:

* _Reusing connections_ — since the overhead of initiating a connection to the database is high (handshake, etc), connection pools allow keeping connections alive, thus reducing that overhead.
* _Limiting resources_ — creating a DB connection per user request can be overwhelming to the DB. Using a pool effectively adds a barrier, limiting the number of maximum number of concurrent connections.

> Well, I am sold, but…

### Isn’t a Connection Pool a solved problem in the Java world?

Yes it is a solved problem if you’re using [JDBC](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/). In that case [HikariCP](https://brettwooldridge.github.io/HikariCP/) is an excellent choice from my experience, but there are a lot of others. In the case of jasync-sql it is not possible to use [HikariCP](https://brettwooldridge.github.io/HikariCP/), because [HikariCP](https://brettwooldridge.github.io/HikariCP/) works with the JDBC API, and the jasync-sql driver is not implementing that full-fledged API, only a subset of it.

> What about other Object pools in Java world?

There are numerous implementations, but it turns out that you usually find some specific requirement that was not implemented by that pool you’re using.

In our case, that requirement was non-blocking. In our pool, all operations have to be non-blocking since the library is async. For example, the `take()` operation in most implementations returns an object immediately or blocks until an object is ready. Our `take()` returns a `Future<Connecti`on>, which will be completed and continued when the connection is ready to use.

I haven’t seen such an implementation in the wild.

I really like this answer from Stack Exchange:

[**Is object pooling a deprecated technique?**](https://softwareengineering.stackexchange.com/questions/115163/is-object-pooling-a-deprecated-technique)  
[_Software Engineering Stack Exchange is a question and answer site for professionals, academics, and students working…_softwareengineering.stackexchange.com](https://softwareengineering.stackexchange.com/questions/115163/is-object-pooling-a-deprecated-technique)

Another requirement that makes it hard to find an alternative is the need to try and stay compatible as much as possible with the current implementation we have.

In case you want to see other implementations you can check here:

[**object pool in java - Google Search**](https://www.google.co.il/search?q=object+pool+in+java)  
[_object pool is a collection of a particular object that an application will create and keep on hand for those…_www.google.co.il](https://www.google.co.il/search?q=object+pool+in+java)

### So how did we implement Object Pool?

Before we dive into the details, let’s observe other requirements from the object pool that were omitted above for clarity but are necessary details.

#### Interfaces

The Object pool interface looks like this:

```
interface AsyncObjectPool<T&gt; {  fun take(): CompletableFuture&lt;T>  fun giveBack(item: T): CompletableFuture<AsyncObjectPool<T>>  fun close(): CompletableFuture<AsyncObjectPool<T>>
```

```
}
```

In addition, when a pool wants to create new objects (connections) it will call the `ObjectFactory`. The factory has a couple more methods to handle the object lifecycle:

* _validate_ — a method to check that the object is still valid. The method should be fast and check only in-memory constructs. For connections we usually check that the last query did not throw an exception and did not get a termination message from [netty](https://netty.io/).
* _test_ — similar to validate, but a more exhaustive check. We allow test method to be slow and access the network etc. This method is used to check that idle objects are still valid. For connections, that will be something similar to `select 0`.
* _destroy_ — called to clean up the object when the pool is not using it anymore.

The complete interface is:

```
interface ObjectFactory<T> {  fun create(): CompletableFuture<;out T>  fun destroy(item: T)  fun validate(item: T): Try<T>  fun test(item: T): CompletableFuture<T>
```

```
}
```

For pool configuration we have the following properties:

* `maxObjects` — maximum number of connections we allow.
* `maxIdle` — time that we leave the connection open without use. After that time it will be reclaimed.
* `maxQueueSize` — when a request for a connection arrives and no connection is available, we put the request on hold in a queue. In case the queue is full (its size passed `maxQueueSize`) it will not wait but instead return an error.
* `createTimeout` — maximum time to wait for a new connection to be created.
* `testTimeout` — maximum time to wait for a test query on an idle connection. If it passes we will consider the connection as erroneous.
* `validationInterval` — on this interval, we will test if the idle connections are active and free up connections that passed `maxIdle`. We will also remove connections that passed `testTimeout`.

#### Original implementation

The first implementation of object pool was single threaded. All operations were sent to a worker thread that was responsible to execute them. This method is known as [thread-confinement](https://www.javaspecialists.eu/archive/Issue218.html). Object creation and test operations were blocking and query execution itself was non-blocking.

This method is problematic because operations are done one after another. On top of that, there are a couple of operations that are blocking as mentioned above. There were various cases of high latency when working in some scenarios and use cases (like [here](https://github.com/mauricio/postgresql-async/issues/91) for example).

As a workaround `PartitionedPool` was introduced. This is a workaround to the _block_ issue with the above single-threaded approach. The partitioned pool creates multiple `SingleThreadedObjectPools`, each with its own worker. When a connection is requested, a pool is selected by a modulus on the thread id. The partitioned pool is actually a pool of pools ;-)

I mentioned this is a workaround since it has its own problems: you might still be blocking, but at a lower rate — plus it consume more threads and resources.

#### Actor based implementation

An Actor is an entity that has a mailbox. It receives messages to its mailbox and processes them one after the other. The mailbox is a sort of a channel to pass events from the outside world to the actor.

A coroutines actor employs lock-free algorithms to allow fast and performant execution of events without the need for locks and `synchronized` blocks.

![Image](https://cdn-media-1.freecodecamp.org/images/0*T1B40xs7Fsf-gnfZ)
_“wall rack filled with paper document lot” by [Unsplash](https://unsplash.com/@californong?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Nong Vang</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

You can see an elaborated explanation [here](https://www.brianstorti.com/the-actor-model/).

In our case those events will be `take` and `giveBack`. In addition to those, we will have internal messages that the actor sends to itself like `objectCreated` etc. That allows the actor to have states that does not suffer from concurrency problems, as it is always confined to the same sequential execution. In addition the channel that passes those events is a queue that is using lock-free algorithms so it is very efficient, avoids contention, and generally has very high performance.

There is an excellent video explaining how this was implemented (note that this is “heavy” algorithmic staff):

Let’s recap what we have until now:

* An actor receives messages and processes them one by one.
* Usually messages will contain a `CompletableFuture` that should be completed when the actor processes it.

Messages will be completed immediately or delayed (like in case we are waiting for a connection to be created). If it is delayed the actor will put the `Future` in a queue, and will use a callback mechanism to notify itself when the original future can be completed.

* Message processing in the actor should not be blocked or delay the actor. If this happens, it will delay all messages waiting to be processed in the queue and will slow down the entire actor operation.

**That’s why, in case we have long running operations inside the actor, we use the callback mechanism.**

#### Let’s see more details on the use cases

`Take` — someone wants an object from the pool. It will send a message with a callback to the actor. The actor will do one of the following things:

* If the object is available — the actor will simply return it.
* If the pool hasn’t passed the limit of created objects — the actor will create a new object and return it when the object is ready.

In such a case, object creation can take time, so the actor will connect the callback from the object creation to the original take request callback.

* Will put the request in a queue for an available object (unless the queue is full and in that case will just return an error).

`GiveBack` — someone wants to give an object back to the pool (release it). This is also done by a message to the actor. The actor will do one of the following:

* If someone is waiting on the wait queue — it will borrow the object to it.
* In other cases it will just keep the object on the pool for requests to come, so the object remains idle.

`Test` — periodically, someone from outside will notify the actor to test connections:

* The actor will release the idle connection that hasn’t been used for a long time (it’s configurable).
* The actor will test other idle objects using the `ObjectFactory`. It will send a callback to the factory and mark those objects as _In Use_, to prevent from borrowing them until the test is completed.
* The actor will check for timeouts in tests and destroy time-outed objects.

Those are the main use cases.

#### Leaks

![Image](https://cdn-media-1.freecodecamp.org/images/0*64dZ7F9trDtbSdWq)
_“selective focus photography of brown faucet” by [Unsplash](https://unsplash.com/@leipuri?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jouni Rajala</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

There can be all sort of leaks in an object pool. Some are internal bugs which I hope are easier to spot and fix, and others are objects that were taken but not returned due to some user error. In such cases, objects might remain in the “_In Use”_ queue forever.

To avoid such cases, the _“In Use”_ Map is using Java’s [WeakHashMap](https://www.baeldung.com/java-weakhashmap). So if a user lost a connection it will be automatically removed from the map when it is cleaned by Java’s Garbage-Collector.

In addition we added a log message in such cases that says: **“LEAK-DETECTED”**.

### That’s it!

The full Kotlin source code of the object pool is available here:

[**jasync-sql/jasync-sql**](https://github.com/jasync-sql/jasync-sql/blob/bacdd12243d89a5e2a46501bb5303815a9fd11e7/db-async-common/src/main/java/com/github/jasync/sql/db/pool/ActorBasedObjectPool.kt)  
[_Java async database driver for MySQL and PostgreSQL written in Kotlin - jasync-sql/jasync-sql_github.com](https://github.com/jasync-sql/jasync-sql/blob/bacdd12243d89a5e2a46501bb5303815a9fd11e7/db-async-common/src/main/java/com/github/jasync/sql/db/pool/ActorBasedObjectPool.kt)

In an upcoming post I will compare performance metrics of the different implementations.

If you want to read more about Kotlin there is a nice introduction here:

And for coroutines in general check out this video:

Finally if you want to learn more about Actors implementation using coroutines in Kotlin, then head over here:

[**Kotlin/kotlinx.coroutines**](https://github.com/Kotlin/kotlinx.coroutines/blob/master/docs/shared-mutable-state-and-concurrency.md)  
[_Library support for Kotlin coroutines . Contribute to Kotlin/kotlinx.coroutines development by creating an account on…_github.com](https://github.com/Kotlin/kotlinx.coroutines/blob/master/docs/shared-mutable-state-and-concurrency.md)

Thanks for reading! ❤️

![Image](https://cdn-media-1.freecodecamp.org/images/0*0aDugHie8xlGjhOZ)
_“aerial photography of woman on pink swimming floats” by [Unsplash](https://unsplash.com/@tom_grimbert?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tom Grimbert</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

