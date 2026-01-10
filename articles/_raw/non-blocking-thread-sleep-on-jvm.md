---
title: How to Use Thread.sleep Without Blocking on the JVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-21T17:39:16.000Z'
originalURL: https://freecodecamp.org/news/non-blocking-thread-sleep-on-jvm
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/164b263b-0d10-452b-9bd0-b14c22adeb31-screen-shot-2019-11-15-at-122953-pm-4-1.png
tags:
- name: Java
  slug: java
- name: Scala
  slug: scala
seo_title: null
seo_desc: 'By Daniel Sebban

  JVM Languages like Java and Scala have the ability to run concurrent code using
  the Thread  class. Threads are notoriously complex and very error prone, so having
  a solid understanding of how they work is essential.

  Let''s start with ...'
---

By Daniel Sebban

JVM Languages like Java and Scala have the ability to run concurrent code using the `Thread`  class. Threads are notoriously complex and very error prone, so having a solid understanding of how they work is essential.

Let's start with the Javadoc for `Thread.sleep`:

> Causes the currently executing **thread** to sleep (temporarily **cease execution)** for the specified number of milliseconds

What are the implications of `**cease execution**`, also known as **blocking**, and what does it mean? Is it bad? And if so can we achieve **non-blocking sleep**?

### What We'll Cover in This Article

This post covers a lot of ground and hopefully you will learn a lot of cool things.

* What happens at the **OS level when sleeping**?
* The **problem with sleeping**
* **Project Loom** and virtual threads
* Functional programming and design
* **ZIO** Scala library for concurrency

Yes, all of this is coming up below.

But first, let’s start with this simple Scala snippet that we will change throughout the post to achieve what we want:

```scala
println("a")
Thread.sleep(1000)
println("b")
```

It's quite simple: it prints “a” and then 10 seconds later in prints “b”

Let’s focus on `Thread.sleep` and try to understand **HOW** it achieves sleeping. Once we understand the how, we will be able to see the problem and define it more concretely.

## How Does Sleeping Work at the OS Level?

Here is what happens when you call `Thread.sleep` under the hood.

* It calls the thread API of the underlying OS
* Because the JVM uses a one to one mapping between Java and kernel threads, it asks the OS to give up the thread’s “rights” to the CPU for the specified time
* When the time has elapsed the OS scheduler will wake the thread via an interrupt (this is efficient) and assign it a CPU slice to allow it to resume running

The critical point here is that the sleeping thread **is completely taken out and is not reusable while sleeping**.

### Limitations of Threads 

Here are few important limitations that come with threads:

* There is a limit to how many threads you can create. After around 30K, you will get this error:

```
java.lang.OutOfMemoryError : unable to create new native Thread
```

* JVM Threads can be expensive memory-wise to create, as they come with a dedicated stack
* Too many JVM threads will incur overhead because of expensive context switches and the way they share finite hardware resources

Now that we understand more about what goes on behind the scenes let’s go back to the sleeping problem.

## The Problem with Sleeping 

Let’s define the problem more concretely and run a snippet to show the issue we are facing. We will use this function to illustrate the point:

```scala
def task(id: Int): Runnable = () => 
{
  println(s"${Thread.currentThread().getName()} start-$id")
  Thread.sleep(10000)
  println(s"${Thread.currentThread().getName()} end-$id")
}
```

This simple function will

* print `**start**` followed by the thread id
* sleeps for 10 seconds
* print `**end**` followed by the thread id

### Your mission if you accept it is to run 2 tasks concurrently with 1 thread

We want to run 2 tasks concurrently, meaning the whole program should take a total of 10 seconds. But we only have 1 thread available.

Are you up for this challenge?

Let’s play a little bit with the number of tasks and threads to get a sense of what the problem is exactly.

### `1 task -> 1 thread`

```scala
new Thread(task(1)).start()
```

```
12:11:08 INFO  Thread-0 start-1
12:11:18 INFO  Thread-0 end-1
```

Let’s fire up `jvisualvm` to check out what the thread is doing:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vissualm_vm_1.png)

You can see that the Thread-0 is in the purple `sleeping` state. 

Hitting the thread dump button will print this:

```
"Thread-0" #13 prio=5 os_prio=31 tid=0x00007f9a3e0e2000 nid=0x5b03 waiting on condition [0x0000700004ac8000]  
  java.lang.Thread.State: TIMED_WAITING (sleeping)
  at java.lang.Thread.sleep(Native Method)
  at example.Blog$.$anonfun$task$1(Blog.scala:7)
  at example.Blog$$$Lambda$2/1359484306.run(Unknown Source)
  at java.lang.Thread.run(Thread.java:748)
  Locked ownable synchronizers:        - None
```

Clearly, this thread is not usable anymore until it finishes to sleep.

### `2 tasks -> 1 thread`

Let’s illustrate the problem by running 2 such tasks with only one thread available:

```scala
import java.util.concurrent.Executors

// an executor with only 1 thread available
val oneThreadExecutor = Executors.newFixedThreadPool(1)

// send 2 tasks to the executor
(1 to 2).foreach(id =>
   oneThreadExecutor.execute(task(id)))
```

We get this output:

```
2020.09.28 21:49:56 INFO  pool-1-thread-1 start-1
2020.09.28 21:50:07 INFO  pool-1-thread-1 end-1
2020.09.28 21:50:07 INFO  pool-1-thread-1 start-2
2020.09.28 21:50:17 INFO  pool-1-thread-1 end-2
```

![Image](https://www.freecodecamp.org/news/content/images/2020/12/visualvm_3.png)

You can see the purple color (sleeping state) for the `pool-1-thread-1`. The tasks have no choice but to run one after the other because the thread is taken out each time `Thread.sleep` is used.

### `2 tasks -> 2 threads`

Let’s run the same code with 2 threads available. We get this:

```scala
// an executor with 2 threads available
val oneThreadExecutor = Executors.newFixedThreadPool(2)

// send 2 tasks to the executor
(1 to 2).foreach(id =>
   oneThreadExecutor.execute(task(id)))
```

```
2020.09.28 22:42:04 INFO  pool-1-thread-2 start-2
2020.09.28 22:42:04 INFO  pool-1-thread-1 start-1
2020.09.28 22:42:14 INFO  pool-1-thread-1 end-1
2020.09.28 22:42:14 INFO  pool-1-thread-2 end-2
```

Each thread can run one task at a time. We finally accomplished what we wanted, running 2 tasks concurrently, and the whole program finished in 10 seconds.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/visulavm_4.png)

That was easy because we used 2 threads (pool-1-thread-1 and pool-1-thread-2), but we want to do the same with only 1 thread.

Let’s identify the problem and then find a solution.

### The problem : `Thread.sleep is blocking`

We now understand that we cannot use `Thread.sleep` – it blocks the thread. 

This makes it unusable until it resumes, preventing us from running 2 tasks concurrently.

Fortunately, there are solutions, which we'll discuss next.

## First Solution: Upgrade your JVM with Project Loom

I mentioned before that JVM threads map one to one to OS threads. And this fatal design mistake leads us here.

[Project Loom](https://wiki.openjdk.java.net/display/loom/Main) aims to correct that by adding virtual threads.

Here is our code rewritten using virtual threads from Loom:

```scala
Thread.startVirtualThread(() -> {
  System.out.println("a")  
  Thread.sleep(1000)  
  System.out.println("b")
});
```

The amazing thing is that the `Thread.sleep` will not block anymore! It's fully async. And on top of that, virtual threads are super cheap. You could create hundreds of thousands of them without overhead or limitations.

All our problems are solved now – well besides the fact that Project Loom will not be available until at least JDK 17 (as of now scheduled for September 2021).

Oh well, let’s go back and try to solve the sleeping problem with what the JVM currently gives us.

### Key insight: You can express sleeping in terms of scheduling a task in the future

If you tell your boss that you are busy and you will resume your work in 10 minutes, your boss does not know that you are about to take a nap. They only see that you started your work in the morning then paused for 10 minutes then resumed.

This:

```
start
sleep(10)
end
```

is equivalent from the outside to this:

```
start
resumeIn(10s, end)
```

What we did above is to **SCHEDULE** the task to end in 10 seconds.

That’s it, we don’t need to sleep anymore. We just need to be able to schedule things in the future instead.

We've reduced one problem with another, one that is easier and has a simpler solution.

### The scheduling problem

Luckily for us, scheduling tasks is very simple to do. We just have to switch out the executor as follows:

```
val oneThreadScheduleExecutor = Executors.newScheduledThreadPool(1)
```

We can now use the `schedule` function instead of `execute`:

```scala
oneThreadScheduleExecutor.schedule
(task(1),10, TimeUnit.SECONDS)
```

Well that’s not exactly what we want. We want to split the start and end printing by 10 seconds, so let’s change our task function as follows:

```scala
def nonBlockingTask(id: Int): Runnable = () => {
  println(s"${Thread.currentThread().getName()} start-$id")
  val endTask: Runnable = () => 
  {
    println(s"${Thread.currentThread().getName()} end-$id")
  }
  //instead of Thread.sleep for 10s, we schedule it in the future, no     more blocking!
  oneThreadScheduleExecutor.schedule(endTask, 10, TimeUnit.SECONDS)
  }
```

```
2020.09.28 23:35:45 INFO  pool-1-thread-1 start-1
2020.09.28 23:35:45 INFO  pool-1-thread-1 start-2
2020.09.28 23:35:56 INFO  pool-1-thread-1 end-1
2020.09.28 23:35:56 INFO  pool-1-thread-1 end-2
```

Yes! We did it! Only one thread and 2 concurrent tasks that “sleep” 10 seconds each.

Ok great, but you cannot really write code like this. What if you want another task in the middle as follows:

```
00:00:00 start
00:00:10 middle
00:00:20 end
```

You would need to change the implementation of the `nonBlockingTask` and add another call to `schedule` in there. And that will get pretty messy very quickly.

## How to Use Functional Programming to Write a DSL with a Non-Blocking Sleep

Functional Programming in Scala is a joy, and writing a DSL (domain-specific language) using FP principles is quite easy.

Let’s start at the end. We would like our final program to look something like this:

```scala
def nonBlockingFunctionalTask(id: Int) = {
  Print(id,"start") andThen 
  Print(id,"middle").sleep(1000) andThen
  Print(id,"end").sleep(1000)
}
```

This mini-language will achieve exactly the same behavior as our previous solution but without exposing all the nasty internals of the scheduled executor and threads.

### The model

Let’s define our data types:

```scala
object Task {
sealed trait Task { self =>
  def andThen(other: Task) = AndThen(self,other)
  def sleep(millis: Long) = Sleep(self,millis)
}
  
case class AndThen(t1: Task, t2: Task) extends Task
case class Print(id: Int, value: String) extends Task 
case class Sleep(t1: Task, millis: Long) extends Task
```

In FP the data types only hold data and no behavior. So this whole code does “nothing" –  it just captures the language structure and information we want.

We need 2 functions:

* `sleep` to make a task sleep
* `andThen` to chain tasks

Notice that their implementation does nothing. It just wraps it in the correct class and that’s it.

Let’s use our `nonBlockingFunctionalTask` function:

```scala
import Task._
//create 2 tasks, this does not run them, no threads involved here
(1 to 2).toList.map(nonBlockingFunctionalTask)
```

It’s a description of the problem. It does nothing, it just builds a list with 2 tasks, each one describing what to do.

If we print the result in the REPL we get this:

```scala
res3: List[Task] = List(
//first task  
AndThen(AndThen(Print(1,start),Sleep(Print(1,middle),10000)),Sleep(Print(1,end),10000)), 
//second task  
AndThen(AndThen(Print(2,start),Sleep(Print(2,middle),10000)),Sleep(Print(2,end),10000))
)
```

Let’s write the `interpreter` that will turn this tree into one that's actually running the tasks.

### The interpreter

In FP the function that turns a description into an executable program is called the `interpreter`. It takes the description of the program, the model, and interprets it into an executable form. Here it will execute and schedule the tasks directly.

We first need a `Stack` that will allow us to encode the dependencies between tasks. Think that `start >>= middle >>= end` will each be pushed to the stack and then popped in order of execution. This will be evident in the implementation.

And now the interpreter (don’t worry if you don't understand this code, it’s a bit complicated, there is a simpler solution coming up):

```scala
def interpret(task: Task, executor: ScheduledExecutorService): Unit = {
  def loop(current: Task, stack: Stack[Task]): Unit =
  current match {
    case AndThen(t1, t2) =>
      loop(t1,stack.push(t2))
    case Print(id, value) =>  
      stack.pop match {
        case Some((t2, b)) => 
          executor.execute(() => {
          println(s"${Thread.currentThread().getName()} $value-$id")
          })   
        loop(t2,b)
        case None => 
          executor.execute(() => {
          println(s"${Thread.currentThread().getName()} $value-$id")
          })
    case Sleep(t1,millis) => 
      val r: Runnable = () =>{loop(t1,stack)}
      executor.schedule(r, millis, TimeUnit.MILLISECONDS)
}
loop(task,Nil)
}
```

And the output is what we want:

```
2020.09.29 00:06:39 INFO  pool-1-thread-1 start-1
2020.09.29 00:06:39 INFO  pool-1-thread-1 start-2
2020.09.29 00:06:50 INFO  pool-1-thread-1 middle-1
2020.09.29 00:06:50 INFO  pool-1-thread-1 middle-2
2020.09.29 00:07:00 INFO  pool-1-thread-1 end-1
2020.09.29 00:07:00 INFO  pool-1-thread-1 end-2
```

One thread running 2 concurrent sleeping tasks. That’s a lot of code and a lot of work. As usual, you should always ask yourself whether there a library that already solves this problem. Turns out there is: ZIO.

## Non-Blocking Sleep in ZIO

`**[ZIO](https://zio.dev/)**` is a functional library for asynchronous and concurrent programming. It works in a similar fashion to our little DSL, because it gives you a few types you can mix and match to describe your program and nothing more.

And then it gives us an interpreter that lets you run a ZIO program.

As I said this interpreter pattern is pervasive in the world of FP. Once you get it, a new world opens up to you.

### `ZIO.sleep` – a better version of `Thread.sleep`

`ZIO` gives us the `ZIO.sleep` function, a non-blocking version of `Thread.sleep`. Here is our function written using `ZIO`:

```scala
import zio._
import zio.console._
import zio.duration._
object ZIOApp extends zio.App {
def zioTask(id: Int) = 
  for {
  _ <- putStrLn(s"${Thread.currentThread().getName()} start-$id")
  _ <- ZIO.sleep(10.seconds)
  _ <- putStrLn(s"${Thread.currentThread().getName()} end-$id")
} yield ()
```

It’s strikingly similar to the first snippet:

```scala
def task(id: Int): Runnable = () => 
{
  println(s"${Thread.currentThread().getName()} start-$id")
  Thread.sleep(10000)
  println(s"${Thread.currentThread().getName()} end-$id")
}
```

The clear difference is the `for` syntax that allows us to chain statements with the `ZIO` type. It's very similar to the `andThen` function from our previous mini-language.

As before with our mini-language, this program is just a description. It’s pure data, and it does nothing. To do something we need the interpreter.

### The ZIO interpreter

To interpret a ZIO program, you just have to extend the `ZIO.App` interface and put it in the `run` method and `ZIO` will take care of running it, like this:

```scala
object ZIOApp extends zio.App 
{ 
override def run(args: List[String]) = {
  ZIO
  //start 2 ZIO tasks in parallel
  .foreachPar((1 to 2))(zioTasks)
  //complete program when done
  .as(ExitCode.success) 
}
```

And we get this output – the tasks complete correctly in 10 seconds:

```
2020.09.29 00:45:12 INFO  zio-default-async-3-1594199808 start-2
2020.09.29 00:45:12 INFO  zio-default-async-2-1594199808 start-1
2020.09.29 00:45:33 INFO  zio-default-async-7-1594199808 end-1
2020.09.29 00:45:33 INFO  zio-default-async-8-1594199808 end-2
```

## Takeaways

* Each JVM Thread maps to an OS thread, in a **one to one fashion**. And this is the root of a lot of problems.
* `Thread.sleep` is bad! It **blocks the current thread** and renders it unusable for further work.
* **Project Loom** (that will be available in JDK 17) will solve a lot of issues. [Here is a cool talk about it](https://www.youtube.com/watch?v=SJeAb-XEIe8).
* You can use `ScheduledExecutorService` to achieve **non-blocking sleep**.
* You can use **Functional Programming to model a language** where doing sleep is non-blocking.
* The **ZIO library** provides a non-blocking sleep out of the box.

  

