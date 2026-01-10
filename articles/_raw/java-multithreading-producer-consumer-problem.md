---
title: How to Solve the Producer-Consumer Problem in Java using Multithreading
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-03-04T17:48:32.000Z'
originalURL: https://freecodecamp.org/news/java-multithreading-producer-consumer-problem
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/producer-consumer-problem-image.jpeg
tags:
- name: Java
  slug: java
- name: multithreading
  slug: multithreading
seo_title: null
seo_desc: 'Concurrency is an important part of Java applications. Each application
  has multiple processes running at the same time. This helps utilize resources efficiently
  and improve performance.

  Multithreading is a method of achieving concurrency. It uses th...'
---

Concurrency is an important part of Java applications. Each application has multiple processes running at the same time. This helps utilize resources efficiently and improve performance.

Multithreading is a method of achieving concurrency. It uses the concept of threads – lightweight processes – to execute multiple tasks in parallel. A very popular application of multithreading is the producer-consumer problem.

In this tutorial, we are going to understand what the producer-consumer problem is and touch upon threads and multithreading briefly. Then, we are going to understand how to solve the producer-consumer problem in Java using threads.

Now, I assume you have a basic knowledge of Java. If not, then check out the following resources.

* [Free Java Courses for Beginners](https://www.freecodecamp.org/news/learn-java-free-java-courses-for-beginners/)
    
* [Basics of Java Programming](https://www.freecodecamp.org/news/learn-the-basics-of-java-programming/)
    

## Table of Contents

* [What is the Producer-Consumer Problem?](#heading-what-is-the-producer-consumer-problem)
    
* [Solution using Producer and Consumer Threads and Issue with Synchronization](#heading-solution-using-producer-and-consumer-threads)
    
* [Introducing Synchronization in the Message Queue Class](#heading-introducing-synchronization-in-the-message-queue)
    
* [Producer with Multiple Consumers](#heading-producer-with-multiple-consumers)
    
* [Solution using Java Concurrency's BlockingQueue Class](#heading-solution-using-java-concurrencys-blockingqueue-class)
    

## What is the Producer-Consumer Problem?

The producer-consumer problem is a synchronization problem between different processes. There are three entities in this problem: a producer, a consumer, and a memory buffer. Both the producer and consumer share the same memory buffer.

The producer produces some items and pushes them into the memory buffer. A consumer then consumes these items by popping them out of the buffer. If the buffer is empty, then the consumer waits for the producer to push an item, which it consumes after the producer pushes it.

The memory buffer is of fixed size. If it is full, the producer waits for the consumer to consume an item before pushing a new one. The producer and consumer cannot access the buffer at the same time – that is, it's mutually exclusive. Each process should wait for the other to finish its work on the buffer before it can access the buffer.

Operating systems often encounter this problem where multiple processes access the same memory space to perform their tasks.

We will solve this problem using multithreading, so I assume you have a basic idea about what multithreading is and how it works. If not, then you can [read through this tutorial](https://www.freecodecamp.org/news/how-to-get-started-with-multithreading-in-java/).

We'll start with an attempt to solve it simply using threads and a separate class for message queue. Then, we'll understand its issues and how to overcome them in the next approach. We'll also see other approaches to the problem. Make sure to stick around until the end.

## Solution using Producer and Consumer Threads

Let's go over our requirements first.

* Producer and Consumer tasks run in separate threads
    
* Common data bus, typically a message queue, used by both producer and consumer.
    
* If not full, producer pushes data into queue, or waits for it to be consumed
    
* If not empty, consumer takes data out of the queue, or waits for producer to publish.
    

These are the things we need to implement to solve this problem. Let's create the message queue first.

### Message Queue

To set up a message queue, we'll use a class that contains the queue and methods to publish and consume messages.

```java
class Data { 
	Queue<String> q; 
    int capacity; 
    
    Data(int cap) { 
    	q = new LinkedList<>(); 
        capacity=cap; 
    } 
    // other methods 
}
```

Here, we have used Java's `Queue` class to store our messages. Each message is of type `String`. But in bigger applications, the message or payload could be of any object type. We also define the capacity of the message queue.

Next, we'll implement the `publish()` method. The method accepts a new message to be published.

```java
public void publish(String msg) { // publish message to the queue }
```

First, we check if the queue is full. We can't publish a new message if the queue has reached capacity.

```java
if(q.size() == capacity){ 
	return; 
}
```

If the queue is not full, then add the message to the queue.

```java
q.add(msg);
```

We'll add print statements to understand the workflow better.

```java
public void publish(String msg) { 
	String name=Thread.currentThread().getName(); 
    if(q.size() == capacity){ 
    	System.out.println("Queue Full!"+name+" waiting for message to be consumed..."); 
        return; 
    } 
    q.add(msg); 
    System.out.println("Message published:: "+msg); 
    System.out.println("Queue: "+ q); 
    System.out.println(); 
}
```

Here, we just print the thread that is inside the method, the message published, and the resulting queue.

Let's implement the `consume()` method now. This method does not take any arguments and works similarly to the `publish()` method. We first check if the queue is empty, before removing anything from the queue.

```java
if(q.size()==0){ 
	return; 
}
```

Then, we remove the message.

```java
q.poll();
```

Again, we'll add print statements to understand the workflow better.

```java
public void consume()  { 
	String name=Thread.currentThread().getName(); 
	if(q.size()==0){ 
		System.out.println(name+" waiting for new message..."); 
		return; 
	} 
    String msg = q.poll(); 
    System.out.println(name+" has consumed msg:: "+msg); 
    System.out.println("Queue: "+ q); 
    System.out.println(); 
}
```

### Producer Thread

Let's write the producer logic now. We'll create a class `Producer` that will run in a thread. There are [several ways to create threads](https://www.javatpoint.com/how-to-create-a-thread-in-java) in Java. We'll use the `Runnable` interface to create our thread since it's the most preferred approach.

```java
class Producer implements Runnable{ 
	Data data; 
    public Producer(Data data) { 
    	this.data = data; 
	} 
    
    @Override public void run() { } 
}
```

The producer has access to the data bus object which is passed to it via the constructor. The producer logic goes inside the `run()` method. By overriding the run method, you are writing functionality that runs in a thread.

Now, a producer's ways of producing and publishing data differs in every application. For this post, we are going to simulate a functionality where the producer keeps publishing messages every few seconds.

We'll define a list of messages that the producer can use.

```java
final String[] messages={"Hi!!", "How are you!!", "I love you!", "What's going on?!!", "That's really funny!!"};
```

Here's the producer logic inside the `run()` method:

```java
public void run() { 
	int i=0; 
    try { 
    	while(true){ 
        	Thread.sleep(1000); 
            data.publish(messages[i]); 
            i=(i+1)%messages.length; 
		} 
	} catch (InterruptedException e) {} 
}
```

In this code, the producer is publishing a message from the messages list every 1000 ms. `Thread.sleep(_some_delay_)` pauses execution of the thread for a certain period. Since it throws an exception, we surround the code with a try-catch block.

This is just for demonstration purposes – don't worry about the logic. Our implementation works regardless of the producer or consumer logic.

### Consumer Thread

Similar to producer thread, let's simulate the consumer logic.

```java
class Consumer implements Runnable{ 
	Data data; 
    public Consumer(Data data) { 
    	this.data = data; 
	} 
    @Override public void run() { 
    	try { 
        	while(true){ 
            	Thread.sleep(2000); 
                data.consume(); 
            } 
        } catch (InterruptedException e) {} 
    } 
}
```

Here, the consumer tries to consume a message every 2000 ms.

### Putting it all Together

Now, we have our message queue along with the producer and consumer classes. Let's create one producer and one consumer thread and start them.

We'll create a `Data` object with capacity of 5 messages and create our producer and consumer threads with the objects of the `Producer` and `Consumer` classes.

```java
public class Main { 
	public static void main(String[] args) { 
    	Data data = new Data(5); 
        Thread producer=new Thread(new Producer(data), "producer"); 
        Thread consumer=new Thread(new Consumer(data), "consumer");
        producer.start(); 
        consumer.start(); 
	} 
}
```

The `run()` method executes in a separate thread when `start()` is called.

### Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-23-211626-1.png align="left")

*Inconsistent output*

Here, the output is inconsistent with the desired workflow. Even after publishing the first message, the consumer is still waiting. Then, a consumer has consumed a message `Hi!!` that doesn't exist. The state of the queue is also inconsistent.

You will probably get a different output, since thread execution depends on the core OS. But the issue still persists. Why does this happen?

### Synchronization Issue With the Data Class

Both producer and consumer threads run simultaneously, working on the same resource. They are accessing the message queue at the exact same time. Both the threads may start with one version of the resource and by the time they perform an operation, they are working on a different version.

This leads to a [race](https://www.javatpoint.com/race-condition-in-operating-system) condition. Both threads end up competing for the same resource and give inconsistent results. The producer thread is trying to add a message to the queue, while at the same time a consumer is trying to consume a message. There's no way of controlling which message the consumer could get.

To solve this issue, we need some kind of mechanism to ensure that only one thread can operate on a shared resource at a time. In this case, we'll use the concept of [synchronization](https://www.geeksforgeeks.org/synchronization-in-java/).

At a glance, a synchronized function or a block can only be executed by one thread at a time. A thread entering such a block acquires a "lock" on the object and any other threads have to wait until the thread releases this lock – that is, until it finishes working on the shared resource.

We'll use a similar method to solve our issue.

## Introducing Synchronization in the Message Queue

To ensure the message queue is only accessed by one thread (producer or consumer) at a time, a thread needs to secure a lock on the `Data` object before performing any operations.

### How to Use the `synchronized` Keyword

An object can be made mutually exclusive by using the synchronized keyword. We'll use the `synchronized` keyword with the `publish()` and `consume()` methods.

```java
public synchronized void publish(String msg)
```

```java
public synchronized void consume()
```

Now, a thread needs to acquire a lock on the object before entering these methods.

### What are the `wait()` and `notify()` Methods?

We have achieved synchronization – only one thread can access a shared resource at a time to ensure consistency. Now, we need to establish communication between the producer and consumer threads.

Let's understand what we need first. If the queue is full, the producer needs to wait for a consumer to consume an item. Similarly, if the queue is empty, the consumer needs to wait until the producer pushes an item.

Also, when a producer pushes an item, it needs to notify all the waiting consumer threads about the action. The is also true when the consumer consumes an item. So, how do we establish this communication?

We can do this using the `wait()` and `notify()` methods. When the `wait()` method is called, the thread releases the lock on the object and enters a waiting state until another thread calls the `notify()` or `notifyAll()` method.

`notify()` wakes up one thread that is in the waiting state, while `notifyAll()` wakes up all waiting threads. When a thread wakes up again, it has to re-acquire the lock on the object. If another thread has the lock, then this thread needs to wait until the other thread releases the lock.

You can learn more about the `wait()` and `notify()` methods [here](https://www.baeldung.com/java-wait-notify).

### How to Communicate Between Threads using wait() and notify()

Let's use the above methods. A producer needs to wait before it pushes an item if the queue is full. So, invoke the `wait()` method if the queue is at capacity. Similarly, the consumer needs to wait if the queue is empty.

To wake up threads from the waiting state, call `notifyAll()` after the producer publishes a message and the consumer consumer a message. This will notify all the waiting threads.

Here is the updated `publish()` method:

```java
public synchronized void publish(String msg) throws InterruptedException { 
	String name=Thread.currentThread().getName(); 
    if(q.size() == capacity){ 
    	System.out.println("Queue Full!"+name+" waiting for message to be consumed..."); 
        wait(); 
	} 
    q.add(msg); 
    System.out.println("Message published:: "+msg); 
    System.out.println("Queue: "+ q); 
    System.out.println(); 
    notifyAll(); 
}
```

And here's the updated `consume()` method:

```java
public synchronized void consume() throws InterruptedException { 
	String name=Thread.currentThread().getName(); 
    if(q.size()==0){ 
    	System.out.println(name+" waiting for new message..."); 
        wait(); 
 	} 
    String msg = q.poll(); 
    System.out.println(name+" has consumed msg:: "+msg);
    System.out.println("Queue: "+ q); 
    System.out.println(); 
    notifyAll(); 
}
```

`wait()` and `notify()` can throw `InterruptedException`, so we add a `throws` declaration to the methods.

### Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-132435-1.png align="left")

*Output with Synchronization‌*

This time, the output is more consistent and we are getting the expected behavior. The producer keeps publishing messages and the consumer consumes those messages.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-134924-1.png align="left")

*Producer waiting*

Here, the queue is full and the producer waits for the consumer to consume a message. Only after that does the producer publish a new message.

## Producer with Multiple Consumers

So far, we have tackled the problem with one producer and one consumer. In a real-world application, there could be multiple producers and consumers, all of them running in separate threads.

Let's add more consumer threads to see how we could handle this scenario:

```python
for(int i=1;i<=5;i++){ 
	new Thread(new Consumer(data), "Consumer "+i).start();
}
```

Here, we have created 5 consumer threads, labelled them, and started them one by one. But, this is not enough. There is an issue with the existing approach.

Let's reduce the consumer sleep time and run the code:

```java
Thread.sleep(500);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-203117.png align="left")

*Multiple consumers issue*

Here, after consumer 5 has consumed a message, the other consumers are able to consume even if the queue is empty.

The issue lies in the following condition:

```java
if(q.size()==0){
	wait();
}
```

Let's understand the workflow first. Consider Consumer 5 (C5) and Consumer 1 (C1). C5 secures the lock on the method and enters it. The queue is initially empty, so it releases the lock and waits for the producer. At the same time, C1 secures the lock and enters the method. It also waits for the producer.

So, C5 and C1 are waiting. The producer publishes a message. C5 and C1 are notified and they wake up. C5 reacquires the lock and proceeds to consume the message, while C1 waits for C5 to release the lock. Here, C1 is not waiting because of `wait()` – it has woken up and now it's waiting at the next line.

After C5 consumes the message and releases the lock, C1 continues and tries to consume the message. But the queue is empty now, so it receives null or throws an exception. This also happens with the other threads.

To prevent this, we need to check if the queue is empty once again. So, instead of using an `if` condition, we use a `while` loop like this:

```python
while(q.size()==0){
            wait();
        }
```

This checks if the queue is empty every time a thread wakes up. So, if multiple threads wake up at the same time, it should check if another thread has emptied the queue.

We do the same for checking if the queue is full.

```java
while(q.size() == capacity){
            wait();
        }
```

This time, the code runs without any issues.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-204943.png align="left")

*Multiple consumers correct output*

Here is the complete code for `Data` class:

```java
class Data {
    Queue<String> q;
    int capacity;
    Data(int cap) {
        q = new LinkedList<>();
        capacity=cap;
    }

    public synchronized void publish(String msg) throws InterruptedException {
        String name=Thread.currentThread().getName();
        while(q.size() == capacity){
            System.out.println("Queue Full!"+name+" waiting for message to be consumed...");
            wait();
        }
        q.add(msg);
        System.out.println("Message published:: "+msg);
        System.out.println("Queue: "+ q);
        System.out.println();
        notifyAll(); 
    }

    public synchronized void consume() throws InterruptedException {
        String name=Thread.currentThread().getName();
        while(q.size()==0){
            System.out.println(name+" waiting for new message...");
            wait();
        }
        String msg = q.poll();
        System.out.println(name+" has consumed msg:: "+msg);
        System.out.println("Queue: "+ q);
        System.out.println();
        notifyAll();
    }
}
```

You can create any number of producers and consumers and test this code in multiple scenarios.

## Solution using Java Concurrency's BlockingQueue Class

So far you have learned what the producer-consumer problem is and how it can be solved. But, while working on real-time applications, we probably won't implement synchronization manually.

Instead, we can use the `BlockingQueue` class from `java.util.concurrent` package. The difference between `Queue` and `BlockingQueue` is that it waits for the queue to become non-empty before a message can be consumed. Similarly, it waits for the queue to have space before publishing a new message.

We can initialize the blocking queue in the following way:

```java
BlockingQueue<String> q = new ArrayBlockingQueue<>(10);
```

This creates a blocking queue of capacity 10. To publish an item, we use the `put()` method, and to remove an item, we use the `take()` method.

Let's first use this in our Producer class:

```java
class Producer implements Runnable{
    BlockingQueue<String> q;
    final String[] messages={"Hi!!", "How are you!!", "I love you!", "What's going on?!!", "That's really funny!!"};
    public Producer(BlockingQueue<String> q) {
        this.q = q;
    }

    @Override
    public void run() {
        int i=0;
        try {
            while(true){
                Thread.sleep(500);
                
                q.put(messages[i]);
                
                System.out.println("Message published:: "+messages[i]);
                i=(i+1)%messages.length;
            }
        } catch (InterruptedException e) {}
    }
    
}
```

Here, we are not using a separate `Data` class with synchronized methods, since the `put()` and `take()` methods of `BlockingQueue` are synchronized. Here, if the queue is full, the `put()` method waits for a consumer to consume a message.

Similarly, let's update our Consumer class:

```java
class Consumer implements Runnable{
    BlockingQueue<String> q;

    public Consumer(BlockingQueue<String> q) {
        this.q = q;
    }

    @Override
    public void run() {
        try {
            while(true){
                Thread.sleep(1500);
                
                String msg=q.take();

                String name=Thread.currentThread().getName();
                System.out.println(name+" has consumed msg:: "+msg);
            }
        } catch (InterruptedException e) {}
    }    
}
```

Here, if the queue is empty, the `take()` method waits for the producer to publish a message.

Let's create our `BlockingQueue` object and start these threads:

```java
public class Main {
    public static void main(String[] args) {
        BlockingQueue<String> q = new ArrayBlockingQueue<>(10);
        Thread producer = new Thread(new Producer(q));
        producer.start();
        for(int i=1;i<=5;i++){
            new Thread(new Consumer(q), "Consumer "+i).start();
        }
    }
    
}
```

Here, we have one producer thread and 5 consumer threads. Let's see the output:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-28-115531.png align="left")

*Output for BlockingQueue implementation*

In the output, you can see that after consumers 1, 3, and 2 have consumed a message, the other consumers wait for a message to be published before consuming it.

There could be a few inconsistencies while printing these messages since the thread only stops at the `put()` or `take()` methods and not the `println()` statements. But the code runs properly. Again, the output will be different each time you run the code.

So, while working on big projects, you can use the `BlockingQueue` class. But it's important to understand how to deal with the whole producer-consumer problem from scratch. This is really helpful, especially during interviews, since you typically won't be allowed to use the `BlockingQueue` class.

## Conclusion

In this tutorial, you learned about an important problem in concurrency, the product-consumer problem. And you learned how you can solve it using multithreading in Java.

In total, we implemented four different approaches:

First, I started out with a very basic and straightforward implementation. Running the producer and consumer in separate threads helped achieve concurrency. But since they used the same message queue, there was a synchronization problem.

Therefore, in the next approach, we added synchronization to fix the issue. Then, we added more consumers who would all wait for the producer. There, we learned why it is important to check the full and empty conditions every time a thread wakes up.

After going through the whole implementation from scratch, we saw a simple way to solve the Producer-Consumer problem in Java using BlockingQueue. By understanding different approaches and their issues, you can get a better idea of how to tackle a problem. I hope this guide helps with your future endeavors.

If you are unable to understand the content or find the explanation unsatisfactory, let me know. New ideas are always appreciated! Feel free to connect with me on Twitter. Till then, goodbye!
