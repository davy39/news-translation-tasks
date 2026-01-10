---
title: If you’re still using Synchronized, you should try Akka Actor instead — here’s
  why
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T06:15:28.000Z'
originalURL: https://freecodecamp.org/news/still-using-synchronized-try-akka-actor-instead-ac2f2b22a9ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qep0tBNdjhQzyunssu4jvw.jpeg
tags:
- name: Akka
  slug: akka
- name: Java
  slug: java
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Martin Budi

  Synchronized is Java’s traditional concurrency mechanism. Although it is probably
  not something we see often these days, it is still fueling many libraries. The problem
  is, synchronized is both blocking and complicated. In this article...'
---

By Martin Budi

_Synchronized_ is Java’s traditional concurrency mechanism. Although it is probably not something we see often these days, it is still fueling many libraries. The problem is, synchronized is both blocking and complicated. In this article, I’d like to illustrate the issue in a simple way and my reasoning to move to Akka Actor for better and easier concurrency.

Consider this simple code:

```java
  int x; 
 
 if (x > 0) {
   return true;
 } else {
   return false;
 }
```

So return true if _x_ is positive. Simple.

Next, consider this even simpler code:

```java
x++;
```

Yes, a counter. Very simple right?

However, all these codes can blow up spectacularly in a multi-threaded environment.

In the first example, true or false isn’t determined by the value of x. It is actually determined by the if-test. So, if another thread changes x to a negative right after the first thread passed the if-test, we’d still get true even if x is no longer positive.

The second example is pretty deceptive. Although it is just one line, there are actually three operations: reading _x_, incrementing it and putting the updated value back. If two threads run at exactly the same time, the update might be lost.

When we have different threads simultaneously accessing and modifying a variable, we have a race condition. If we just want to build a counter, Java provides thread-safe Atomic Variables, among them Atomic Integer which we can use for this purpose. Atomic Integer, however, only works on single variables. How do we make several operations atomic?

By using _synchronized_ block. First, let’s take a look at a more elaborate example.

```java
int x; 
public int withdraw(int deduct){
    int balance = x - deduct; 
    if (balance > 0) {
      x = balance;
      return deduct;
    } else {
      return 0;
    }
}
```

This is a very basic cash withdraw method. It also happens to be dangerous. Two threads running at the same time may cause the bank to issue two withdrawals even if the balance is no longer enough. Now let’s see how it works with synchronized block:

```java
volatile int x;
public int withdraw(int deduct){
  synchronized(this){
    int balance = x - deduct; 
    if (balance > 0) {
      x = balance;
      return deduct;
    } else {
      return 0;
    }
  }
}
```

The idea of synchronized block is simple. One thread enters it and locks it, while other threads wait outside. The lock is an object, in our case _this_. After it’s done, the lock is released and passed to another thread which then does the same thing. Also, note the esoteric keyword _volatile_ which is needed to prevent the thread from using the local CPU cache of _x._

Now with the threads untangled, the bank won’t accidentally issue unfunded withdrawals. However, this structure tends to grow complex with more blocks and more locks. Dealing with multiple locks is particularly risky. The blocks might inadvertently hold the key for each other and end up locking the entire app. And on top of it, we have an efficiency issue. Remember that while a thread works inside, all the other threads wait outside. And waiting threads are well … waiting. They don’t do anything else but wait.

So instead of doing such mechanism, why not just drop the job in a queue? To better visualize it, imagine an email system. When you send an email, you drop the email in the recipient’s mailbox. You don’t wait around until the person reads it.

These are the basics of the Actor model and Akka framework in general.

Actor encapsulates state and behavior. Unlike OOP’s encapsulation, though, actors do not expose their state and behavior at all. The only way for an actor to communicate with each other is by exchanging messages. Incoming messages are dropped in a mailbox and digested in first-in-first-out order. Here’s a reworked sample in Akka and Scala.

```scala
case class Withdraw(deduct: Int)
class ReplicaActor extends Actor {
  var x = 10;
  def receive: Receive = {
    case Withdraw(deduct) => val r = withdraw(deduct)
  }
}
class BossActor extends Actor {
  var replica = context.actorOf(Props[ReplicaActor])
  replica ! Withdraw(6)
  replica ! Withdraw(9)   
}
```

We have a ReplicaActor that does the work and BossActor that orders the replica around. First, notice the ! sign or _tell_. This is one of two methods (the other is _ask_) for an actor to asynchronously send a message to another actor. _tell_ in particular does so without waiting for a reply. So the boss tells the replica to do two withdraw orders and immediately leaves. These messages arrive in the replica's _receive_ where each one is popped and matched with the corresponding handler. In this case, _Withdraw_ executes the _withdraw_ method from the previous example and deducts the requested amount from state x. After it is done, the actor proceeds to the next message in the queue.

So what do we get here? For one, we no longer need to worry about locking and working with atomic/concurrent types. Actor’s encapsulation and queuing mechanism already guarantee thread-safety. And there is no more waiting since threads just drop the message and return. Results can be delivered later with _ask_ or _tell_. It’s simple and sane.

Akka is based on JVM and available in both Scala and Java. Although this article isn’t debating Java vs Scala, Scala’s pattern matching and functional programming would be very useful in managing Actor’s data messaging. At the very least it can help you write shorter code by avoiding Java’s brackets and semicolons.

