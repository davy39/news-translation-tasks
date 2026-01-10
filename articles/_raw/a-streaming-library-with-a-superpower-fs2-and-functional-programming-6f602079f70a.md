---
title: 'A streaming library with a superpower: FS2 and functional programming'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:20:26.000Z'
originalURL: https://freecodecamp.org/news/a-streaming-library-with-a-superpower-fs2-and-functional-programming-6f602079f70a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mi3HukEz9_JHfv3Z5lp93g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Daniel Sebban

  Scala has a very special streaming library called FS2 (Functional Streams for Scala).
  This library embodies all the advantages of functional programming (FP). By understanding
  its design goals you will get exposure to the core ideas ...'
---

By Daniel Sebban

Scala has a very special streaming library called FS2 (Functional Streams for Scala). This library embodies all the advantages of functional programming (FP). By understanding its design goals you will get exposure to the core ideas that make FP so appealing.

FS2 has one central type: `**Stream[Effect,Output]**`

You might get from this type that it’s a `Stream` and that it emits values of type `Output`.

The obvious question here is what is `Effect`? What is the link between `Effect` and `Output`? And what advantages does FS2 have over other streaming libraries?

### Overview

I will start by reviewing what problems FS2 solves. Then I compare `List` and `Stream` with several code examples. After that, I will focus on how to use `Stream` with a DB or any other IO. That is where FS2 shines and where the `Effect`type is used. Once you will understand what `Effect` is, the advantages of Functional Programming should be evident to you.

At the end of this post you will get the answers to the following questions:

* What problems can I solve with FS2?
* What can I do with `Stream` that `List` cannot ?
* How can I feed data from an API/File/DB to `Stream` ?
* What is this `Effect` type and how does it relate to functional programming?

Note: The code is in Scala and should be understandable even without prior knowledge of the syntax.

### What problems can I solve with FS2?

1. Streaming I/O: Loading incrementally big data sets that would not fit in memory and operating on them without blowing your heap.
2. Control Flow (not covered): Moving data from one/several DBs/files/APIs to others in a nice declarative way.
3. Concurrency (not covered): Run different streams in parallel and make them communicate together. For example loading data from multiple files and processing them concurrently as opposed to sequentially. You can do some advanced stuff here. Streams can communicate together **during** the processing stage and not only at the end.

### `List` vs `Stream`

`List` is the most well known and used data structure. To get a feel for how it differs from an FS2 `Stream`, we will go through a few use cases. We will see how `Stream` can solve problems that `List` cannot.

### Your data is too big and does not fit in memory

Let’s say you have a very big file (40GB) `fahrenheit.txt`. The file has a temperature on each line and you want to convert it to `celsius.txt`.

### Loading a big file using `List`

```scala
import scala.io.Source
val list = Source.fromFile("testdata/fahrenheit.txt").getLines.toList
java.lang.OutOfMemoryError: Java heap space
  java.util.Arrays.copyOfRange(Arrays.java:3664)
  java.lang.String.<init>(String.java:207)
  java.io.BufferedReader.readLine(BufferedReader.java:356)
  java.io.BufferedReader.readLine(BufferedReader.java:389)
```

`List` fails miserably because of course, the file is too big to fit in memory. If you are curious, you can go check the full solution using `Stream` [here](https://functional-streams-for-scala.github.io/fs2/#about) — but do that later, read on :)

### When List won’t do…Stream to the rescue!

Let’s say I succeeded in reading my file and I want to write it back. I would like to preserve the line structure. I need to insert a newline character `\n` after each temperature.

I can use the `intersperse` combinator to do that

```scala
import fs2._
Stream(1,2,3,4).intersperse("\n").toList
```

Another nice one is `zipWithNext`

```scala
scala> Stream(1,2,3,4).zipWithNext.toList
res1: List[(Int, Option[Int])] = List((1,Some(2)), (2,Some(3)), (3,Some(4)), (4,None))
```

It bundles consecutive things together, very useful if you want to [remove consecutive duplicates](https://gist.github.com/dsebban/bb34ea4671bda8d52e2f083e2b160778).

These are only a few from a lot of very useful ones, here is the [full list](https://oss.sonatype.org/service/local/repositories/releases/archive/co/fs2/fs2-core_2.12/0.10.5/fs2-core_2.12-0.10.5-javadoc.jar/!/fs2/Stream.html).

Obviously `Stream` can do a lot of things that `List` cannot, but the best feature is coming in the next section, it's all about how to use `Stream` in the real world with DBs/Files/APIs ...

### How can I feed data from an API/File/DB to `Stream`?

Let’s just say for now that this our program

```scala
scala> Stream(1,2,3)
res2: fs2.Stream[fs2.Pure,Int] = Stream(..)
```

What does this `Pure` mean? Here is the scaladoc from the source code:

```scala
/**
    * Indicates that a stream evaluates no effects.
    *
    * A `Stream[Pure,O]` can be safely converted to a `Stream[F,O]` for all `F`.
*/
type Pure[A] <: Nothing
```

It means no effects, ok …, but **What is an effect?** and more specifically what is the effect of our program `Stream(1,2,3)`?

This program has literally no _effect_ on the world. Its only effect will be to make your CPU work and consumes some power!! It does not affect the world around you.

By affecting the world I mean it **consumes** any meaningful resource like a file, a database, or it **produces** anything like a file, uploading some data somewhere, writing to your terminal, and so on.

### How do I turn a `Pure` stream to something useful?

Let’s say I want to load user ids from a DB, I am given this function, it does a call to the DB and returns the userId as a `Long`.

```scala
import scala.concurrent.Future
def loadUserIdByName(userName: String): Future[Long] = ???
```

It returns a `[Future](https://www.scala-lang.org/api/2.12.3/scala/concurrent/Future.html)` which indicates that this call is asynchronous and the value will be available at some point in the future. It wraps the value returned by the DB.

I have this `Pure` stream.

```scala
scala> val names = Stream("bob", "alice", "joe")
names: fs2.Stream[fs2.Pure,String] = Stream(..)
```

How do I get a `Stream` of ids?

The naive approach would be to use the `map` function, it should run the function for each value in the `Stream`.

```scala
scala> userIdsFromDB.compile
res5: fs2.Stream.ToEffect[scala.concurrent.Future,Long] = fs2.Stream$ToEffect@fc0f18da
```

I still got back a `Pure`! I gave the `Stream` a function that _affects the world_ and I still got a `Pure`, not cool ... It would have been neat if FS2 would have detected automatically that the `loadUserIdByName` function has an _effect_ on the world and returned me something that is NOT `Pure` but it does not work like that. You have to use a special combinator instead of `map`: you have to use `evalMap`.

```scala
scala> userIdsFromDB.toList
<console>:18: error: value toList is not a member of fs2.Stream[scala.concurrent.Future,Long]
       userIdsFromDB.toList
                     ^
```

No more `Pure`! we got `Future` instead, yay! What just happened?

It took:

* `loadUserIdByName: Future[Long]`
* `Stream[Pure, String]`

And switched the types of the stream to

* `Stream[Future, Long]`

It separated the `Future` and isolated it! The left side that was the `Effect` type parameter is now the concrete `Future` type.

Neat trick, but how does it help me?

You just witnessed true **separation of concerns.** You can continue to operate on the stream with all the nice `List` like combinators and you don't have to worry about if the DB is down, slow or all the stuff that is related to the network (effect) concerns.

It all works until I want to use `toList` to get the values back

```scala
scala> userIdsFromDB.toList
<console>:18: error: value toList is not a member of fs2.Stream[scala.concurrent.Future,Long]
       userIdsFromDB.toList
                     ^
```

What???!!! I could swear that I used `toList` before and it worked, how can it say that `toList` is not a member of `fs2.Stream[Future,String]` any more? It is as if this function was removed the moment I started using an effect-ful stream, that's impressive! But how do I get my values back?

```scala
scala> userIdsFromDB.compile
res5: fs2.Stream.ToEffect[scala.concurrent.Future,Long] = fs2.Stream$ToEffect@fc0f18da
```

First we use `compile` to tell the `Stream` to combine all the effects into one, effectively it folds all the calls to `loadUserIdByName` into one big `Future`. This is needed by the framework, and it will become apparent why this step is needed soon.

Now `toList` should work

```scala
scala> userIdsFromDB.compile.toList
<console>:18: error: could not find implicit value for parameter F: cats.effect.Sync[scala.concurrent.Future]
       userIdsFromDB.compile.toList
                             ^
```

What?! the compiler is still complaining. That’s because `Future` is not a good `Effect` type — it breaks the philosophy of separation of concerns as explained in the next very important section.

### IMPORTANT: The ONE thing to take away from this post

A key point here, is that the DB has not been called at this point. Nothing happened really, the full program does not produce anything.

```scala
def loadUserIdByName(userName: String): Future[Long] = ???
Stream("bob", "alice", "joe").evalMap(loadUserIdByName).compile
```

### Separating program description from evaluation

Yes it might be surprising but the major theme in FP is separating the

* **Description** of your program: a good example is the program we just wrote, it’s a pure description of the problem “I give you names and a DB, give me back IDs”

And the

* **Execution** of your program: running the actual code and asking it to go to the DB

One more time our program has literally no _effect_ on the world besides making your computer warm, exactly like our `Pure` stream.

Code that does not have an effect is called **pure** and that’s what all Functional Programming is about: writing programs with functions that are **pure.** Bravo, you now know what FP is all about.

Why would you want write code this way? Simple: to achieve separation of concerns between the IO parts and the rest of our code.

Now let’s fix our program and take care of this `Future` problem.

As we said `Future` is a bad `Effect` type, it goes against the separation of concerns principle. Indeed, `Future` is eager in Scala: the moment you create one it starts to executes on some thread, you don't have control of the execution and thus it breaks. FS2 is well aware of that and does not let you compile. To fix this we have to use a type called `IO` that wraps our bad `Future`.

That brings us to the last part, what is this `IO` type? and how do I finally get my list of `usedIds` back?

```scala
scala> import cats.effect.IO
import cats.effect.IO
scala> Stream("bob", "alice", "joe").evalMap(name => IO.fromFuture(IO(loadUserIdByName(name)))).compile.toList
res8: cats.effect.IO[List[Long]] = IO$2104439279
```

It now gives us back a `List` but still, we didn't get our IDs back, so one last thing must be missing.

![Image](https://cdn-media-1.freecodecamp.org/images/ivbIHjwyNlEmckvLT6thLcPRcVRUkRGgw-dH)

### What does `IO` really mean?

`IO` comes from [cats-effect library](https://typelevel.org/cats-effect/datatypes/io.html). First let's finish our program and finally get out the ids back from the DB.

```scala
scala> userIds.compile.toList.unsafeRunSync
<console>:18: error: not found: value userIds
       userIds.compile.toList.unsafeRunSync
       ^
```

The proof that it’s doing something is the fact that it’s failing.

```
loadUserIdByName(userName: String): Future[Long] = ???
```

When `???` is called you will get this exception, it means the function was executed (as opposed to before when we made the point that nothing was really happening). When we implement this function it will go to the DB and load the ids, and it will have an **effect** on the world (network/files system).

`IO[Long]` is a **description** of **how** to get a value of type `Long` and it most certainly involves doing some I/O i.e going to the network, loading a file,...

It’s the **How** and not the **What.** It describes how to get the value from the network. If you want to execute this description, you can use `unsafeRunSync` (or other functions prefixed `unsafe`). You can guess why they are called this way: indeed a call to a DB is inherently unsafe as it could fail if, for example, your Internet connection is out.

### Recap

Let’s take a last look at `**Stream[Effect,Output]**`**.**

`Output` is the type that the stream emits (could be a stream of `String`, `Long` or whatever type you defined).

`Effect` is the way (the recipe) to produce the `Output` (i.e go to the DB and give me an `id` of type `Long`).

It’s important to understand that if these types are separated to make things easier, breaking down a problem in subproblems allows you to reason about the subproblems independently. You can then solve them and combine their solutions.

The link between these 2 types is the following :

In order for the `Stream` to emit an element of type

* `Output`

It needs to evaluate a type

* `Effect`

A special type that encodes an effective action as a value of type `IO`, this `IO` value allows the separation of 2 concerns:

* **Description**:`IO` is a simple immutable value, it’s a recipe to get a type `A` by doing some kind of IO(network/filesystem/…)
* **Execution**: in order for`IO` to do something, you need to _execute/run it_ using `io.unsafeRunSync`

#### Putting it all together

`Stream[IO,Long]` says:

This is a `Stream` that emits values of type `Long` and in order to do so, it needs to run an _effective_ function that produces`IO[Long]` for each value.

That’s a lot of details packed in this very short type. The more details you get about how things happen the fewer errors you make.

### Takeaways

* `Stream` is a **super charged** version of `List`
* `Stream(1,2,3)` is of type `Stream[Pure, Int]` , the second type `Int` is the type of all values that this stream will emit
* `Pure` means no _effect_ on the world. It just makes your CPU work and consumes some power, but besides that it does not affect the world around you.
* Use `evalMap` instead of `map` when you want to apply a function that has an effect like `loadUserIdByName` to a `Stream`.
* `Stream[IO, Long]` separates the concerns of What and How by letting you work only with the values and not worrying about how to get them (loading from the db).
* Separating program description from evaluation is a key aspect of FP.
* All the programs you write with `Stream` will do nothing until you use `unsafeRunSync`. Before that your code is effectively _pure._
* `IO[Long]` is an effect type that tells you: you will get `Long` values from IO (could be a file, the network, the console ...). It's a description and not a wrapper!r
* `Future` does not abide by this philosophy and thus is not compatible with FS2, you have to use `IO` type instead.

### FS2 videos

* Hands on screencast by Michael Pilquist: [https://www.youtube.com/watch?v=B1wb4fIdtn4](https://www.youtube.com/watch?v=B1wb4fIdtn4)
* Talk by Fabio Labella [https://www.youtube.com/watch?v=x3GLwl1FxcA](https://www.youtube.com/watch?v=x3GLwl1FxcA)

