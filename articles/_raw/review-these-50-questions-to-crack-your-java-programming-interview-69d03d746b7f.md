---
title: Review these 50 questions to crack your Java programming interview
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T16:41:53.000Z'
originalURL: https://freecodecamp.org/news/review-these-50-questions-to-crack-your-java-programming-interview-69d03d746b7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s73cLB7vYz05f-aw_QAgFw.png
tags:
- name: coding
  slug: coding
- name: interview questions
  slug: interview-questions
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By javinpaul

  A list of frequently asked Java questions from programming job interviews.


  Hello, everybody! Over the past few years, I have been sharing a lot of Java Interview
  questions and discussion individually. Many of my readers have requested t...'
---

By javinpaul

#### A list of frequently asked Java questions from programming job interviews.

![Image](https://cdn-media-1.freecodecamp.org/images/cA9-wkkWif9KjVOo09g1D5s5OiE8KskLLfa-)

Hello, everybody! Over the past few years, I have been sharing a lot of [Java Interview questions](http://javarevisited.blogspot.sg/2015/10/133-java-interview-questions-answers-from-last-5-years.html) and discussion individually. Many of my readers have requested that I bring them together so that they can have them in the same spot. This post is the result of that.

This article contains more than **50 Java Interview questions** covering all important topics like Core Java fundamentals, [Java Collection Framework](https://javarevisited.blogspot.com/2011/11/collection-interview-questions-answers.html), [Java Multithreading and Concurrency](https://javarevisited.blogspot.com/2014/07/top-50-java-multithreading-interview-questions-answers.html#axzz5ghebTpxm), [Java IO](https://javarevisited.blogspot.com/2014/08/socket-programming-networking-interview-questions-answers-Java.html), [JDBC](https://javarevisited.blogspot.com/2012/12/top-10-jdbc-interview-questions-answers.html), [JVM Internals](http://www.java67.com/2016/08/10-jvm-options-for-java-production-application.html), [Coding Problems](http://www.java67.com/2018/06/data-structure-and-algorithm-interview-questions-programmers.html), [Object-Oriented programming](http://www.java67.com/2015/12/top-30-oops-concept-interview-questions-answers-java.html), etc.

The questions are also picked up from various interviews and they are, by no means, very difficult. You might have seen them already in your phone or face-to-face round of interviews.

The questions are also very useful to review important topics like multithreading and collections. I have also shared some _useful resources for further learning and improvement_ like [**The Complete Java MasterClass**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) to brush up and fill gaps in your Java skills.

So what are we waiting for? Here is the list of some of the most frequently asked Java questions in interviews for both beginner and experienced Java developers.

### 50+ Java Interview Questions for 2 to 3 years Experienced Programmers

So, without wasting any more of your time, here is my list of some of the frequently asked [Core Java Interview Question](http://www.java67.com/2018/03/top-50-core-java-interview-questions.html)s for beginner programmers. This list focuses on beginners and less experienced devs, like someone with 2 to 3 years of experience in Java.

1) **How does Java achieve platform independence?** ([answer](http://www.java67.com/2012/08/how-java-achieves-platform-independence.html))  
hint: bytecode and Java Virtual Machine

2) **What is `ClassLoader` in Java?** ([answer](http://javarevisited.blogspot.sg/2012/12/how-classloader-works-in-java.html#axzz59AWpr6cb))  
hint: part of JVM that loads bytecodes for classes. You can write your own.

3) **Write a Java program to check if a number is Even or Odd?** ([answer](http://javarevisited.blogspot.sg/2013/04/how-to-check-if-number-is-even-or-odd.html#axzz59AWpr6cb))  
hint: you can use bitwise operator, like bitwise AND, remember, even the number has zero at the end in binary format and an odd number has 1 in the end.

4) **Difference between `ArrayList` and `HashSet` in Java?** ([answer](http://www.java67.com/2012/07/difference-between-arraylist-hashset-in-java.html))  
hint: all differences between `List` and `Set` are applicable here, e.g. ordering, duplicates, random search, etc. See [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections) by Richard Warburton to learn more about ArrayList, HashSet and other important Collections in Java.

![Image](https://cdn-media-1.freecodecamp.org/images/ueOwMAd5GBdw4blCOpEBpOdMOtcs-et6nPYA)

5) **What is double checked locking in Singleton?** ([answer](http://www.java67.com/2016/04/why-double-checked-locking-was-broken-before-java5.html))  
hint: two-time check whether instances is initialized or not, first without locking and second with locking.

**6) How do you create thread-safe Singleton in Java? ([answer](http://javarevisited.blogspot.sg/2012/12/how-to-create-thread-safe-singleton-in-java-example.html))**  
hint: many ways, like using Enum or by using double-checked locking pattern or using a nested static class.

**7) When to use the volatile variable in Java? ([answer](http://www.java67.com/2012/08/what-is-volatile-variable-in-java-when.html))**  
hint: when you need to instruct the JVM that a variable can be modified by multiple threads and give hint to JVM that does not cache its value.

**8) When to use a transient variable in Java? ([answer](http://www.java67.com/2012/08/what-is-transient-variable-in-java.html))**  
hint: when you want to make a variable non-serializable in a class, which implements the Serializable interface. In other words, you can use it for a variable whose value you don’t want to save. See [**The Complete Java MasterClass**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) to learn about transient variables in Java.

**9) Difference between the transient and volatile variable in Java? ([answer](http://www.java67.com/2012/11/difference-between-transient-vs-volatile-modifier-variable-java.html))**  
hint: totally different, one used in the context of serialization while the other is used in concurrency.

**10) Difference between Serializable and Externalizable in Java? ([answer](http://www.java67.com/2012/10/difference-between-serializable-vs-externalizable-interface.html))**  
hint: Externalizable gives you more control over the Serialization process.

**11) Can we override the private method in Java? ([answer](http://www.java67.com/2013/08/can-we-override-private-method-in-java-inner-class.html))**  
hint: No, because it’s not visible in the subclass, a primary requirement for overriding a method in Java.

**12) Difference between `Hashtable` and `HashMap` in Java? ([answer](http://javarevisited.blogspot.sg/2010/10/difference-between-hashmap-and.html#axzz53B6SD769))**  
hint: several but most important is `Hashtable`, which is synchronized, while `HashMap` is not. It's also legacy and slow as compared to `HashMap`.

**13) Difference between `List`and `Set` in Java? ([answer](http://javarevisited.blogspot.sg/2012/04/difference-between-list-and-set-in-java.html#axzz53n9YK0Mb))**  
hint: `List` is ordered and allows duplicate. `Set` is unordered and doesn't allow duplicate elements.

**14) Difference between `ArrayList` and `Vector` in Java ([answer](http://www.java67.com/2012/09/arraylist-vs-vector-in-java-interview.html))**  
hint: Many, but most important is that `ArrayList` is non-synchronized and fast while `Vector` is synchronized and slow. It's also legacy class like `Hashtable`.

**15) Difference between `Hashtable` and `ConcurrentHashMap` in Java? ([answer](http://javarevisited.blogspot.sg/2011/04/difference-between-concurrenthashmap.html#axzz4qw7RoNvw))**  
hint: more scalable. See [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections) by Richard Warburton to learn more.

**16) How does `ConcurrentHashMap` achieve scalability? ([answer](http://javarevisited.blogspot.sg/2017/08/top-10-java-concurrenthashmap-interview.html#axzz50U9xyqbo))**  
hint: by dividing the map into segments and only locking during the write operation.

**17) Which two methods you will override for an `Object` to be used as `Key` in `HashMap`? ([answer](http://www.java67.com/2013/06/how-get-method-of-hashmap-or-hashtable-works-internally.html))**  
hint: equals and hashcode

**18) Difference between wait and sleep in Java? ([answer](http://www.java67.com/2012/08/what-are-difference-between-wait-and.html))**  
hint: The `wait()` method releases the lock or monitor, while sleep doesn't.

**19) Difference between `notify` and `notifyAll` in Java? ([answer](http://www.java67.com/2013/03/difference-between-wait-vs-notify-vs-notifyAll-java-thread.html))**  
hint: `notify` notifies one random thread is waiting for that lock while `notifyAll` inform to all threads waiting for a monitor. If you are certain that only one thread is waiting then use `notify`, or else `notifyAll` is better. See [**Threading Essentials Mini-Course**](https://javaspecialists.teachable.com/p/threading-essentials/?product_id=539197&coupon_code=SLACK100?affcode=92815_johrd7r8) by Java Champion Heinz Kabutz to learn more about threading basics.

**20) Why you override hashcode, along with `equals()` in Java? ([answer](http://javarevisited.blogspot.sg/2015/01/why-override-equals-hashcode-or-tostring-java.html#axzz55oDxm8vv))**  
hint: to be compliant with equals and hashcode contract, which is required if you are planning to store your object into collection classes, e.g. `HashMap` or `ArrayList`.

**21) What is the load factor of `HashMap` means? ([answer](http://www.java67.com/2017/08/top-10-java-hashmap-interview-questions.html))**  
hint: The threshold that triggers the re-sizing of `HashMap` is generally 0.75, which means `HashMap` resize itself if it's 75 percent full.

**22) Difference between `ArrayList` and `LinkedList` in Java? ([answer](http://www.java67.com/2012/12/difference-between-arraylist-vs-LinkedList-java.html))**  
hint: same as an array and linked list, one allows random search while other doesn't. Insertion and deletion easy on the linked list but a search is easy on an array. See [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections)**,** Richard Warburton’s course on Pluralsight, to learn more about essential Collection data structure in Java.

**23) Difference between `CountDownLatch` and `CyclicBarrier` in Java? ([answer](http://www.java67.com/2012/08/difference-between-countdownlatch-and-cyclicbarrier-java.html))**  
hint: You can reuse `CyclicBarrier` after the barrier is broken but you cannot reuse `CountDownLatch` after the count reaches to zero.

**24) When do you use `Runnable` vs `Thread` in Java? ([answer](http://www.java67.com/2016/01/7-differences-between-extends-thread-vs-implements-Runnable-java.html))**  
hint: always

**25) What is the meaning of Enum being type-safe in Java? ([answer](http://www.java67.com/2014/04/what-java-developer-should-know-about-Enumeration-type-in-Java.html))**  
hint: It means you cannot assign an instance of different Enum type to an Enum variable. e.g. if you have a variable like `DayOfWeek` day then you cannot assign it value from `DayOfMonth` enum.

**26) How does Autoboxing of Integer work in Java? ([answer](http://javarevisited.blogspot.sg/2012/07/auto-boxing-and-unboxing-in-java-be.html#axzz59AWpr6cb))**  
hint: By using the `valueOf()` method in Java.

**27) Difference between `PATH` and `Classpath` in Java? ([answer](http://www.java67.com/2012/08/what-is-path-and-classpath-in-java-difference.html))**  
hint: `PATH` is used by the operating system while `Classpath` is used by JVM to locate Java binary, e.g. JAR files or Class files. See [Java Fundamentals: The Core Platform](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-core-platform) to learn more about `PATH`, `Classpath`, and other Java environment variable.

![Image](https://cdn-media-1.freecodecamp.org/images/io-lPE67oMG1oBh204LvPm61t7kAcLFvp-B6)

**28) Difference between method overloading and overriding in Java? ([answer](http://www.java67.com/2015/08/top-10-method-overloading-overriding-interview-questions-answers-java.html))**  
hint: Overriding happens at subclass while overloading happens in the same class. Also, overriding is a runtime activity while overloading is resolved at compile time.

**29) How do you prevent a class from being sub-classed in Java? ([answer](http://www.java67.com/2017/06/10-points-about-final-modifier-in-java.html))**  
hint: just make its constructor private

**30) How do you restrict your class from being used by your client? ([answer](http://javarevisited.blogspot.sg/2016/01/why-jpa-entity-or-hibernate-persistence-should-not-be-final-in-java.html))**  
hint: make the constructor private or throw an exception from the constructor

**31) Difference between `StringBuilder` and `StringBuffer` in Java? ([answer](http://www.java67.com/2016/10/5-difference-between-stringbuffer.html))**  
hint: `StringBuilder` is not synchronized while `StringBuffer` is synchronized.

**32) Difference between Polymorphism and Inheritance in Java? ([answer](http://www.java67.com/2014/04/difference-between-polymorphism-and-Inheritance-java-oops.html))**  
hint: Inheritance allows code reuse and builds the relationship between class, which is required by Polymorphism, which provides dynamic behavior. See [**Java Fundamentals: Object-Oriented Design**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-object-oriented-design) to learn more about OOP features.

**33) Can we override static method in Java? ([answer](http://www.java67.com/2012/08/can-we-override-static-method-in-java.html))**  
hint: No, because overriding resolves at runtime while static method call is resolved at compile time.

**34) Can we access the private method in Java? ([answer](http://www.java67.com/2012/08/can-we-override-private-method-in-java.html))**  
hint: yes, in the same class but not outside the class

**35) Difference between interface and abstract class in Java? ([answer](http://www.java67.com/2017/08/difference-between-abstract-class-and-interface-in-java8.html))**  
hint: from [Java 8](https://dzone.com/articles/5-courses-to-crack-java-certification-ocajp-1z0-80), the difference is blurred. However, a Java class can still implement multiple interfaces but can only extend one class.

**36) Difference between DOM and SAX parser in Java? ([answer](http://www.java67.com/2012/09/dom-vs-sax-parser-in-java-xml-parsing.html))**  
hint: DOM loads whole XML File in memory while SAX doesn’t. It is an event-based parser and can be used to parse a large file, but DOM is fast and should be preferred for small files.

**37) Difference between throw and throws keyword in Java? ([answer](http://www.java67.com/2012/10/difference-between-throw-vs-throws-in.html))**  
hint: throws declare what exception a method can throw in case of error but throw keyword actually throws an exception. See [**Java Fundamentals: Exception Handling**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-exception-handling) to learn more about Exception handling in Java.

![Image](https://cdn-media-1.freecodecamp.org/images/QSqKD-b97Dr36kViV1eTdvqNVNgdZRp52D7n)

**38) Difference between fail-safe and fail-fast iterators in Java? ([answer](http://www.java67.com/2015/06/what-is-fail-safe-and-fail-fast-iterator-in-java.html))**  
hint: fail-safe doesn’t throw `ConcurrentModificationException` while `fail-fast` does whenever they detect an outside change on the underlying collection while iterating over it.

**39) Difference between Iterator and Enumeration in Java? ([answer](http://javarevisited.blogspot.sg/2010/10/what-is-difference-between-enumeration.html#axzz59AWpr6cb))**  
hint: Iterator also gives you the ability to remove an element while iterating while Enumeration doesn’t allow that.

**40) What is `IdentityHashMap` in Java? ([answer](http://www.java67.com/2016/09/difference-between-identityhashmap-weakhashmap-enummap-in-java.html))**  
hint: A `Map`, which uses the `==` equality operator to check equality instead of the `equals()` method.

**41) What is the `String` pool in Java? ([answer](http://javarevisited.blogspot.sg/2016/07/difference-in-string-pool-between-java6-java7.html#axzz4pGGwsyna))**  
hint: A pool of `String` literals. Remember it's moved to heap from perm gen space in JDK 7.

**42) Can a `Serializable` class contains a non-serializable field in Java? ([answer](http://javarevisited.blogspot.sg/2016/09/how-to-serialize-object-in-java-serialization-example.html))**  
hint: Yes, but you need to make it either static or transient.

**43) Difference between this and super in Java? ([answer](http://www.java67.com/2013/06/difference-between-this-and-super-keyword-java.html))**  
hint: this refers to the current instance while super refers to an instance of the superclass.

**44) Difference between `Comparator` and `Comparable` in Java? ([answer](http://www.java67.com/2013/08/difference-between-comparator-and-comparable-in-java-interface-sorting.html))**  
hint: `Comparator` defines custom ordering while `Comparable` defines the natural order of objects, e.g. the alphabetic order for `String`. See [The Complete Java MasterClass](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) to learn more about sorting in Java.

![Image](https://cdn-media-1.freecodecamp.org/images/DOCGFtdTMhjj3faRAiQ69ZSTxf2pffyroFfv)

**45) Difference between `java.util.Date` and `java.sql.Date` in Java? ([answer](http://javarevisited.blogspot.sg/2012/04/difference-between-javautildate-and.html))**  
hint: former contains both date and time while later contains only date part.

**46) Why wait and notify method are declared in `Object` class in Java? ([answer](http://javarevisited.blogspot.sg/2012/02/why-wait-notify-and-notifyall-is.html))**  
hint: because they require lock which is only available to an object.

**47) Why Java doesn’t support multiple inheritances? ([answer](http://javarevisited.blogspot.sg/2011/07/why-multiple-inheritances-are-not.html))**  
hint: It doesn’t support because of a bad experience with C++, but with Java 8, it does in some sense — only multiple inheritances of `Type` are not supported in Java now.

**48) Difference between checked and unchecked Exception in Java? ([answer](http://javarevisited.blogspot.sg/2011/12/checked-vs-unchecked-exception-in-java.html))**  
hint: In case of checked, you must handle exception using catch block, while in case of unchecked, it’s up to you; compile will not bother you.

**49) Difference between Error and Exception in Java? ([answer](http://www.java67.com/2012/12/difference-between-error-vs-exception.html))**  
hint: I am tired of typing please check the answer

**50) Difference between Race condition and Deadlock in Java? ([answer](http://javarevisited.blogspot.sg/2012/02/what-is-race-condition-in.html#axzz59AbkWuk9))**  
hint: both are errors that occur in a concurrent application, one occurs because of thread scheduling while others occur because of poor coding. See [Multithreading and Parallel Computing in Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fmultithreading-and-parallel-computing-in-java%2F) to learn more about deadlock, Race Conditions, and other multithreading issues.

### Closing Notes

Thanks, You made it to the end of the article … Good luck with your programming interview! It’s certainly not going to be easy, but by following this roadmap and guide, you are one step closer to becoming a [DevOps engineer](https://hackernoon.com/10-free-courses-to-learn-docker-for-programmers-and-devops-engineers-7ff2781fd6e0).

If you like this article, then please share with your friends and colleagues, and don’t forget to follow [javinpaul](https://twitter.com/javinpaul) on Twitter!

#### Additional Resources

* [Java Interview Guide: 200+ Interview Questions and Answers](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-interview-questions-and-answers%2F)
* [Spring Framework Interview Guide — 200+ Questions & Answers](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fspring-interview-questions-and-answers%2F)
* [Preparing For a Job Interview By John Sonmez](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fdeveloper-job-interviews)
* [Java Programming Interview Exposed by Markham](http://www.amazon.com/Java-Programming-Interviews-Exposed-Markham/dp/1118722868?tag=javamysqlanta-20)
* [Cracking the Coding Interview — 189 Questions and Answers](http://www.amazon.com/Cracking-Coding-Interview-6th-Edition/dp/0984782850/?tag=javamysqlanta-20)
* [Data Structure and Algorithms Analysis for Job Interviews](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structure-and-algorithms-analysis%2F)
* [130+ Java Interview Questions of Last 5 Years](http://javarevisited.blogspot.sg/2015/10/133-java-interview-questions-answers-from-last-5-years.html)

> **P.S. —** If you need some FREE resources to learn Java, you can check out this list of **free Java courses** to start your preparation.  
>   
> **P. S. S. —** I have not provided the answer to the interview questions shared in the image “ How many String objects are created in the code?” can you guess and explain?

