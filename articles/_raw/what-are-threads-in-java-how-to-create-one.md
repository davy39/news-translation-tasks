---
title: What are Threads in Java? How to Create a Thread with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-28T22:23:36.000Z'
originalURL: https://freecodecamp.org/news/what-are-threads-in-java-how-to-create-one
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Copy-of-Copy-of-How-Encapsulation-is-Achieved-in-Python--1-.png
tags:
- name: Java
  slug: java
- name: multithreading
  slug: multithreading
seo_title: null
seo_desc: "By Bikash Daga (Jain)\nThreads in Java are pre-defined classes that are\
  \ available in the java.package when you write your programs. Generally, every program\
  \ has one thread which is provided from the java.package. \nAll of these threads\
  \ use the same mem..."
---

By Bikash Daga (Jain)

Threads in Java are pre-defined classes that are available in the java.package when you write your programs. Generally, every program has one thread which is provided from the java.package. 

All of these threads use the same memory, but they are independent. This means that any exception in a thread will not affect how other threads work, despite them sharing the same memory.

## What You'll Learn:

* In this article we will learn about how to create a thread
* We will learn about the concept of multi tasking.
* We will learn about the lifecycle of threads and also about the thread class.

## What are Threads in Java?

Threads allow us to do things more quickly in Java. That is, they help us perform multiple things all at once. 

You use threads to perform complex operations without any disturbance in the main program. 

When various multiple threads are executed at the same time, this process is known as multi-threading. 

[Multi-threading](https://www.freecodecamp.org/news/how-to-get-started-with-multithreading-in-java/) is mainly used in gaming and similar programs. Since we now know a bit about multi-threading, let's also learn about the concept of multi-tasking.

## What is Multitasking in Java?

[Multitasking](https://www.techtarget.com/whatis/definition/multitasking) is the process that lets users perform multiples tasks at the same time. There are two ways to enable multitasking in Java:

1. **Process-based multitasking**: The processes in this type of multitasking are heavy and a lot of time is consumed. This is because the program takes a long time to switch between different processes.
2. **Thread-based multi tasking**: Threads are light-weight compared to process-based multi tasking, and the time taken to switch between them is shorter.

Now let's learn about the working model of a thread.

## Thread Lifecycle in Java

### What is a thread lifecycle in Java?

In Java, a thread will always remain in one of a few different states (which we will read about below). 

The thread goes through various stages in its lifecycle. For example a thread is first born, then it gets started, and goes through these various stages until it dies. 

The thread model consists of various states. Let's learn about each of them in more detail:

1. **New**: the model is in the new state when the code is not yet running.
2. **Running state or the active stage**: this is the state when the program is under execution or is ready to execute.
3. **Suspended state**: you can use this state if you want to pause activity when something specific happens (and lets you temporarily stop execution).
4. **Blocked state**: a thread is under the blocked state when it's waiting for resources. In the blocked state, the thread scheduler clears the queue by rejecting unwanted threads which are present.
5. **Terminated state**: this state stops a thread's execution immediately. A terminated thread means that it is dead and is no longer available for use.

## Thread Methods

### What are thread methods in Java?

Thread methods in Java are very important while you're working with a multi-threaded application. The thread class has some important methods which are described by the thread itself.

Now let's learn about each of these methods:

1. **public void start()**: you use this method to start the thread in a separate path of execution. Then it invokes the run() method on the thread object.
2. **public void run()**: this method is the starting point of the thread. The execution of the thread begins from this process.
3. **public final void setName()**: this method changes the name of the thread object. There is also a `getName()` method for retrieving the name of the current context.
4. **public final void setPriority()**: you use this method to set the values of the thread object.
5. **public void sleep()**: you use this method to suspend the thread for a particular amount of time.
6. **public void interrupt()**: you use this method to interrupt a particular thread. It also causes it to continue execution if it was blocked for any reason.
7. **public final boolean isAlive()**: this method returns true if the thread is alive.

Now let's learn about creating a thread.

## How to Create a Thread in Java

There are two ways to create a thread:

First, you can create a thread using the thread class (extend syntax). This provides you with constructors and methods for creating and operating on threads.

The thread class extends the object class and implements a runnable interface. The thread class in Java is the main class on which Java’s multithreading system is based.

Second, you can create a thread using a runnable interface. You can use this method when you know that the class with the instance is intended to be executed by the thread itself. 

The runnable interface is an interface in Java which is used to execute concurrent thread. The runnable interface has only one method which is `run()`.

Now let's see the syntax of both of them:

#### How to use the extend syntax:

```
public class Main extends thread {
  public void test() {
    System.out.println("Threads are very helpful in java");
  }
}

```

Here's an example of the `extend` method:

```
public class Main extends test {
  public static void main(String[] args) {
    Main test = new Main();
    test.start();
    System.out.println("Threads are very much helpful in java");
  }
  public void run() {
    System.out.println("Threads are very helpful in java");
  }
}

```

Using the syntax of the extended class we have just implemented it in this example. Run the above code in your editor to see how it works.

#### How to use a runnable interface:

```
public class Main implements runnable {
  public void test() {
    System.out.println("Threads are very helpful in java");
  }
}
```

And here's an example of using a [runnable interface](https://docs.oracle.com/javase/7/docs/api/java/lang/Runnable.html):

```
public class cal implements test {
  public static void main(String[] args) {
    cal obj = new cal();
    Thread thread = new Thread(obj);
    thread.start();
    System.out.println("Threads are very much helpful in java");
  }
  public void run() {
    System.out.println("Threads are very much helpful in java");
  }
}

```

Since we extended the thread class, our class object will not be treated as a thread object. Run the above code in your compiler to see how it works.

## How to Implement Threads in Java – Examples

Let's see few more examples of implementing [threads in Java](https://www.scaler.com/topics/thread-in-java/):

```
class First
{
public static void main (String [ ]args) throws IOException
{
Thread t =Thread.currentThread( );
System.out.println(“CURRENTTHREAD = ” + t);
t.setName(“NewThread”);
t.setPriority(t.getPriority( ) – 1);
System.out.println(“CURRENTTHREAD = ” + t);
System.out.println(“NAME = ” + t.getName( ));
}
}

```

#### Output

```
CURRENTTHREAD =THREAD [main, 5, main]
CURRENTTHREAD =THREAD [New Thread, 4, main]
NAME = New Thread

```

Here we have created a thread then printed the current thread. Then we have set the name of the thread as a new thread and finally we have printed the name of the thread. Run the above code in your editor to see how it works.

Here's another example:

```
class First implements Runnable
{
Thread t;
First( ){
t = new Thread(this,"NEW");
System.out.println(“CHILD :” + t);
t.start();
}
public void run( ) {
try{ for(int i = 5; i>0, i- -) {
System.out.println("CHILD :" + i);
Thread.sleep(500); }
} //END OFTRY BLOCK
catch(InterruptedException e){ }
System.out.println("EXITING CHILD");
} }
class Second
{
public static void main(String [ ]args) throws IOException
{
new First();
try{
for(int i = 5; i>0, i- -)
{
System.out.println("MAIN :"  + i);
Thread.sleep(1000);
}
} //END OFTRY BLOCK
catch(InterruptedException e){ }
System.out.println("Exiting man");
}
}

```

#### Output

```
CHILD = THREAD [NEW, 5, main]
MAIN : 5
CHILD : 5
CHILD : 4
MAIN : 4
CHILD : 3
CHILD : 2
MAIN : 3
CHILD : 1
EXITING CHILD
MAIN : 2
MAIN : 1
EXITING MAIN

```

Here we have created a thread and then printed the child thread. Then we ran the for loop inside the run function and printed the child. Run the code in your editor to see how it works.

Now let's learn more about multi threading.

## Multi-Threading in Java

As I briefly explained above, multithreading in Java refers to the execution of several threads at the same time. 

Multithreading is useful because threads are independent – and in multithreading we can perform the execution of several threads at the same time without blocking the user. 

It also helps us save time as we can perform several operation at the same time. A good real time example of multi threading in Java is word processing. This program checks the spelling of what we're typing while we write a document. In this case each task will be provided by a different thread.

### Use cases of multi-threading in Java

Now that you know how multi-threading saves time by allowing you to perform multiple operation together, let's learn about some practical uses cases of multi-threading:

1. Word processing, which we discussed above.
2. Gaming.
3. Improving the responsiveness of a server.
4. Using thread synchronization functions to provide enhanced processes to process communication.

Now let's look at an example program to learn how to implement multithreading:

```
class First implements Runnable
{
Thread t; String S;
First(String Name){
S=Name;
t = new Thread(this,S);
System.out.println("CHILD :" + t);
t.start();
}
public void run( ) {
try{ for(int i = 5; i>0, i- -) {
System.out.println(S + " :" + i);
Thread.sleep(1000); }
} //END OF TRY BLOCK
catch(InterruptedException e){ }
System.out.println("EXITING " + S);
} 
}
class Second
{
public static void main(String [ ]args) throws IOException
{
new First("ONE");
new First("TWO");
new First("THREE");
try{
Thread.sleep(20000);
} //END OFTRY BLOCK
catch(InterruptedException e){ }
System.out.println("EXITING MAIN");

```

#### Output

```
CHILD =THREAD [ONE, 5, main]
CHILD =THREAD [TWO, 5, main]
CHILD =THREAD [THREE, 5, main]
ONE : 5 ONE : 2
TWO : 5 TWO : 2
THREE : 5 THREE:2
ONE : 4 ONE : 1
TWO : 4 TWO : 1
THREE : 4 THREE : 1
ONE : 3 EXITING ONE
TWO : 3 EXITINGTWO
THREE : 3 EXITINGTHREE
EXITING MAIN

```

In the code above, we have implemented multi-threading by using the run method. Then we have initiated a thread by using the constructor, since the thread is created from it. Then we can start by calling the start() method. Run the code in your editor to see how it works.

## Conclusion

A thread is a light-weight process in Java. It's a path of execution within a process. There are only two methods to create threads in Java.

In a browser, multiple tabs can be multiple threads. Once a thread is created it can be present in any of the states we discussed above.

Thank you for reading.

