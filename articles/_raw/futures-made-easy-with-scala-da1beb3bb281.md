---
title: Futures Made Easy with Scala
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-26T22:06:18.000Z'
originalURL: https://freecodecamp.org/news/futures-made-easy-with-scala-da1beb3bb281
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DBWep0oc9Om-9DzWoasoZQ.jpeg
tags:
- name: Java
  slug: java
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Martin Budi

  Future is an abstraction to represent the completion of an asynchronous operation.
  Today it is commonly used in popular languages from Java to Dart. However, as modern
  applications are becoming more complex, composing them is also beco...'
---

By Martin Budi

Future is an abstraction to represent the completion of an asynchronous operation. Today it is commonly used in popular languages from Java to Dart. However, as modern applications are becoming more complex, composing them is also becoming more difficult. Scala utilizes a functional approach that makes it easy to visualize and construct Future composition.

This article aims to explain the basics in a pragmatic way. No jargon, no foreign terminology. You don’t even have to be a Scala programmer (yet). All you need to have is some understanding of a couple of higher-order functions: map and foreach. So let’s get started.

In Scala, a future can be created as simple as this:

```scala
Future {"Hi"} 
```

Now let’s run it and make a “Hi World”.

```scala
Future {"Hi"} .foreach (z => println(z + " World"))
```

That’s all there is. We just ran a future using `foreach`, manipulated the result a bit, and printed it to the console.

But how is it possible? So we normally associate foreach and map with collections: we unwrap the content and tinker with it. If you look at it, it’s conceptually similar to a future in the way we want to unwrap the output from `Future{}`and manipulate it. To have this happen the future needs to be completed first, hence “running” it. This is the reasoning behind the functional composition of Scala Future.

In realistic applications, we want to coordinate not just one but several futures at once. A particular challenge is how to arrange them to run **sequentially** or **simultaneously**.

#### **Sequential run**

When several futures start one after another like a relay race we call it sequential run. A typical solution would simply be placing a task in the previous task’s callback, a technique known as chaining. The concept is correct but it doesn’t look pretty.

In Scala, we can use for-comprehension to help us abstract it. To see how it looks, let’s just go straight to an example.

```scala
import scala.concurrent.ExecutionContext.Implicits.global

object Main extends App {

  def job(n: Int) = Future {
    Thread.sleep(1000)
    println(n) // for demo only as this is side-effecting 
    n + 1
  }

  val f = for {
    f1 <- job(1)
    f2 <- job(f1)
    f3 <- job(f2)
    f4 <- job(f3)
    f5 <- job(f4)
  } yield List(f1, f2, f3, f4, f5)
  f.map(z => println(s"Done. ${z.size} jobs run"))
  Thread.sleep(6000) // needed to prevent main thread from quitting 
                     // too early 
}
```

The first thing to do is importing _ExecutionContext_ whose role is to manage thread pool. Without it, our future will not run.

Next, we define our “big job” which simply waits for a second and returns its input incremented by one.

Then we have our for-comprehension block. In this structure, each line inside assigns a job’s result to a value with `&l`t;- which will then be available for any subsequent futures. We have arranged our jobs so that except for the first one, each one takes in the output of the previous job.

Also, note that the result of a for-comprehension is also a future with output determined by **yield.** After the execution, the result will be available inside `map`. For our purpose, we simply put all the jobs’ outputs in a list and take its size.

Let’s run it.

![Image](https://cdn-media-1.freecodecamp.org/images/dzz5CXOB2TXLAzGnPcxQJpjjlgjaz-VomVBW)
_Sequential run_

We can see the five futures fired one-by-one. It is important to note that this arrangement should only be used when the future is dependent on the previous future.

#### **Simultaneous or Parallel run**

If the futures are independent of each other then they should be fired simultaneously. For this purpose, we’re going to use _Future.sequence_. The name is a bit confusing, but in principle it simply takes a list of futures and transforms it into a future of list. The evaluation, however, is done asynchronously.

Let’s create an example of mixed sequential and parallel futures.

```scala
val f = for {
  f1 <- job(1)
  f2 <- Future.sequence(List(job(f1), job(f1)))
  f3 <- job(f2.head)
  f4 <- Future.sequence(List(job(f3), job(f3)))
  f5 <- job(f4.head)
} yield f2.size + f4.size
f.foreach(z => println(s"Done. $z jobs run in parallel"))
```

Future.sequence takes a list of futures that we wish to run simultaneously. So here we have f2 and f4 containing two parallel jobs. As the argument fed into Future.sequence is a list, the result is also a list. In a realistic application, the results may be combined for further computation. Here we’ll take the first element from each list with `.head` then pass it to f3 and f5 respectively.

Let’s see it in action:

![Image](https://cdn-media-1.freecodecamp.org/images/9yDEuET5UU-nSsW8VyNKMY4rkBP9igBs8w7s)
_Parallel run_

We can see the jobs in 2 and 4 fired simultaneously indicating successful parallelism. It is worth noting that parallel execution is not always guaranteed since it depends on available threads. If there are not enough threads then only some of the jobs will run in parallel. The others, however, will wait until some more threads are freed.

#### **Recovering from errors**

Scala Future incorporates **recover** that acts as a back-up future when an error occurs**.** This allows the future composition to finish even with failures. To illustrate, consider this code:

```scala
Future {"abc".toInt}
.map(z => z + 1)
```

Of course, this will not work, as “abc” is not an int. With **recover,** we can salvage it by passing a default value. Let’s try passing a zero:

```scala
Future {"abc".toInt}
.recover {case e => 0}
.map(z => z + 1)
```

Now the code will run and produce one as a result. In composition, we can fine-tune each future like this to make sure the process won’t fail.

However, there are also times when we want to reject errors explicitly. For this purpose, we can use _Future.succesful and Future.failed_ to signal validation result. And if we don’t care about individual failure we can position recover to catch _any_ error inside the composition.

Let’s work another bit of code using for-comprehension that checks if the input is a valid int and lower than 100. Future.failed and Future.successful are both futures so we don’t need to wrap it in one. Future.failed in particular requires a _Throwable_ so we’re going to create a custom one for input larger than 100. After putting it all up together we would have as follows:

```scala
val input = "5" // let's try "5", "200", and "abc"
case class NumberTooLarge() extends Throwable()
val f = for {
   f1 <- Future{ input.toInt }
   f2 <- if (f1 > 100) {
            Future.failed(NumberTooLarge())
          } else {
            Future.successful(f1)
          }
} yield f2
f map(println) recover {case e => e.printStackTrace()}
```

Notice the positioning of recover. With this configuration, it will simply intercept any error occurring inside the block. Let’s test it with several different inputs “5”, “200”, and “abc”:

```
"5"   -> 5
"200" -> NumberTooLarge stacktrace
"abc" -> NumberFormatException stacktrace 
```

“5” reached the end no problem. “200” and “abc” arrived in recover. Now, what if we want to handle each error separately? This is where pattern matching comes into play. Expanding the recover block, we can have something like this:

```scala
case e => 
  e match {
    case t: NumberTooLarge => // deal with number > 100
    case t: NumberFormatException => // deal with not a number
    case _ => // deal with any other errors
  }
}
```

You might probably have guessed it but an all-or-nothing scenario like this is commonly used in public APIs. Such service wouldn’t process invalid input but needs to return a message to inform the client what they did wrong. By separating exceptions, we can pass a custom message for each error. If you like to build such service (with a very fast web framework), head over to my [Vert.x article](https://medium.freecodecamp.org/an-introduction-to-vert-x-the-fastest-java-framework-today-27d8661ceb14).

#### **The world outside Scala**

We have talked a lot about how easy Scala Future is. But is it really? To answer it we need to look at how it’s done in other languages. Arguably the closest language to Scala is Java as both operate on JVM. Furthermore, Java 8 has introduced Concurrency API with _CompletableFuture_ which is also able to chain futures. Let’s rework the first sequence example with it.

![Image](https://cdn-media-1.freecodecamp.org/images/LDS0WqYRsLYNTCV4gnEh0U6DsDn8HOUGi6lb)
_Sequential run in Java_

That’s sure a lot of stuff. And to code this I had to look up _supplyAsync_ and _thenApply_ among so many methods in the documentation. And even if I know all these methods, they can only be used within the context of the API.

On the other hand, Scala Future is not based on API or external libraries but a functional programming concept that is also used in other aspects of Scala. So with an initial investment in covering the fundamentals, you can reap the reward of less overhead and higher flexibility.

#### Wrapping up

That’s all for the basics. There’s more to Scala Future but what we have here has covered enough ground to build real-life applications. If you like to read more about Future or Scala, in general, I’d recommend [Alvin Alexander tutorials](https://alvinalexander.com/scala/how-use-multiple-scala-futures-in-for-comprehension-loop), [AllAboutScala](http://allaboutscala.com/tutorials/chapter-9-beginner-tutorial-using-scala-futures/), and [Sujit Kamthe’s article](https://medium.com/beingprofessional/understanding-functor-and-monad-with-a-bag-of-peanuts-8fa702b3f69e) that offers easy to grasp explanations.

