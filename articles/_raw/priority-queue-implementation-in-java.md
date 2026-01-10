---
title: Priority Queues in Java Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T17:34:47.000Z'
originalURL: https://freecodecamp.org/news/priority-queue-implementation-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99d7740569d1a4ca21ff.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: 'By Aditya Sridhar

  Priority Queues are used very often in real life applications. In this article we
  will learn what priority queues are and how we can use them in Java.

  Before we discuss what a priority queue is, let''s see what a regular queue is.

  A ...'
---

By Aditya Sridhar

Priority Queues are used very often in real life applications. In this article we will learn what priority queues are and how we can use them in Java.

Before we discuss what a priority queue is, let's see what a regular queue is.

A regular queue follows a first in first out ( FIFO ) structure. This means that if 3 messages – m1, m2 and m3 – go into the queue in that order, then they come out of the queue in the exact same order. 

## Why do we need queues?

Let us say that we have data producers ( for example, when a user clicks on a web page ) which are extremely fast. But then we want to consume this data at a slower pace later. 

In this case, the producer would push all of the messages into the queue, and a consumer would consume these messages later from the queue at a slower pace.

## What is a priority queue?

As mentioned earlier, a regular queue has a first in first out structure. But in some scenarios we want to process messages in a queue based on their priority and not based on when the message entered the queue.

Priority queues help consumers consume the higher priority messages first followed by the lower priority messages.

## Priority queues in Java

Now let's see some actual Java code that will show us how to use priority queues.

### Priority queues with natural ordering

Here is some code showing how to create a simple priority queue for strings 

```java
private static void testStringsNaturalOrdering() {
        Queue<String> testStringsPQ = new PriorityQueue<>();
        testStringsPQ.add("abcd");
        testStringsPQ.add("1234");
        testStringsPQ.add("23bc");
        testStringsPQ.add("zzxx");
        testStringsPQ.add("abxy");

        System.out.println("Strings Stored in Natural Ordering in a Priority Queue\n");
        while (!testStringsPQ.isEmpty()) {
            System.out.println(testStringsPQ.poll());
        }
    }
```

The first line tells us that we are creating a priority queue:

```java
Queue<String> testStringsPQ = new PriorityQueue<>();
```

PriorityQueue is available in java.util package. 

Next we are adding 5 strings in random order into the priority queue. For this we use the **add()** function as shown below:

```java
testStringsPQ.add("abcd");
testStringsPQ.add("1234");
testStringsPQ.add("23bc");
testStringsPQ.add("zzxx");
testStringsPQ.add("abxy");
```

In order to get the latest item from the queue we use the **poll()** function as shown below:

```java
testStringsPQ.poll()
```

**poll()** will give us the latest item and also remove it from the queue. If we want to get the latest item in the queue without removing it, we can use the **peek()** function:

```java
testStringsPQ.peek()
```

Finally, we print out all the elements from the queue by using the poll() function as shown below:

```java
while (!testStringsPQ.isEmpty()) {
   System.out.println(testStringsPQ.poll());
}
```

Here is the output of the above program:

```bash
1234
23bc
abcd
abxy
zzxx
```

Since we did not tell the priority queue how to prioritize its content, it used a default natural ordering. In this case, it gave us the data back in the ascending order of the strings. This is not the same order in which items were added to the queue. 

### What about having a custom ordering?

This is possible as well, and we can do it with the help of a **comparator.**

Let's create an integer priority queue now. But this time let's get the result in descending order of value.

In order to achieve this, first we need to create an integer comparator:

```java
 static class CustomIntegerComparator implements Comparator<Integer> {

        @Override
        public int compare(Integer o1, Integer o2) {
            return o1 < o2 ? 1 : -1;
        }
    }
```

In order to create a comparator, we implement the **comparator** interface and override the **compare** method. 

By using **o1 < o2 ? 1 : -1** we will get the result in descending order. If we had used **o1 > o2 ? 1 : -1,** then we would have gotten the result in ascending order

Now that we have the comparator, we need to add this comparator to the priority queue. We can do this like this:

```java
Queue<Integer> testIntegersPQ = new PriorityQueue<>(new CustomIntegerComparator());
```

Here is the rest of the code which adds elements into the priority queue and prints them:

```java
   testIntegersPQ.add(11);
        testIntegersPQ.add(5);
        testIntegersPQ.add(-1);
        testIntegersPQ.add(12);
        testIntegersPQ.add(6);

        System.out.println("Integers stored in reverse order of priority in a Priority Queue\n");
        while (!testIntegersPQ.isEmpty()) {
            System.out.println(testIntegersPQ.poll());
        }
```

The output of the above program is given below:

```bash
12
11
6
5
-1
```

We can see that the comparator has done its job well. Now the priority queue is giving us the integers in descending order.

### Priority queue with Java objects

Up to this point, we've seen how we can use strings and integers with priority queues. 

In real life applications we would generally be using priority queues with custom Java objects.

Let's first create a class called CustomerOrder which is used to store customer order details:

```java
public class CustomerOrder implements Comparable<CustomerOrder> {
    private int orderId;
    private double orderAmount;
    private String customerName;

    public CustomerOrder(int orderId, double orderAmount, String customerName) {
        this.orderId = orderId;
        this.orderAmount = orderAmount;
        this.customerName = customerName;
    }

    @Override
    public int compareTo(CustomerOrder o) {
        return o.orderId > this.orderId ? 1 : -1;
    }

    @Override
    public String toString() {
        return "orderId:" + this.orderId + ", orderAmount:" + this.orderAmount + ", customerName:" + customerName;
    }

    public double getOrderAmount() {
        return orderAmount;
    }
}
```

This is a simple Java class to store customer orders. This class implements **comparable interface,** so that we can decide on what basis this object needs to be ordered in the priority queue. 

The ordering is decided by the **compareTo** function in the above code. The line **o.orderId > this.orderId ? 1 : -1** instructs that the orders should be sorted based on descending order of the **orderId** field

Below is the code which creates a priority queue for the CustomerOrder object:

```java
CustomerOrder c1 = new CustomerOrder(1, 100.0, "customer1");
CustomerOrder c2 = new CustomerOrder(3, 50.0, "customer3");
CustomerOrder c3 = new CustomerOrder(2, 300.0, "customer2");

Queue<CustomerOrder> customerOrders = new PriorityQueue<>();
customerOrders.add(c1);
customerOrders.add(c2);
customerOrders.add(c3);
while (!customerOrders.isEmpty()) {
	System.out.println(customerOrders.poll());
}
```

In the above code three customer orders have been created and added to the priority queue. 

When we run this code we get the following output:

```bash
orderId:3, orderAmount:50.0, customerName:customer3
orderId:2, orderAmount:300.0, customerName:customer2
orderId:1, orderAmount:100.0, customerName:customer1
```

As expected, the result comes in descending order of the **orderId**.

### What if we want to prioritize based on orderAmount?

This is again a real life scenario. Let's say that by default the CustomerOrder object is prioritized by the orderId. But then we need a way in which we can prioritize based on orderAmount. 

You may immediately think that we can modify the **compareTo** function in the **CustomerOrder c**lass to order based on orderAmount. 

But the **CustomerOrder c**lass may be used in multiple places in the application, and it would interfere with the rest of the application if we modify the **compareTo** function directly.

The solution to this is pretty simple: we can create a new custom comparator for the CustomerOrder class and use that along with the priority queue

Below is the code for the custom comparator:

```java
 static class CustomerOrderComparator implements Comparator<CustomerOrder> {

        @Override
        public int compare(CustomerOrder o1, CustomerOrder o2)
        {
            return o1.getOrderAmount() < o2.getOrderAmount() ? 1 : -1;
        }
    }
```

This is very similar to the custom integer comparator we saw earlier. 

The line `o1.getOrderAmount() < o2.getOrderAmount() ? 1 : -1;` indicates that we need to prioritize based on descending order of **orderAmount**.

Below is the code which creates the priority queue:

```java
  CustomerOrder c1 = new CustomerOrder(1, 100.0, "customer1");
        CustomerOrder c2 = new CustomerOrder(3, 50.0, "customer3");
        CustomerOrder c3 = new CustomerOrder(2, 300.0, "customer2");
        Queue<CustomerOrder> customerOrders = new PriorityQueue<>(new CustomerOrderComparator());
        customerOrders.add(c1);
        customerOrders.add(c2);
        customerOrders.add(c3);
        while (!customerOrders.isEmpty()) {
            System.out.println(customerOrders.poll());
        }
```

In the above code we are passing the comparator to the priority queue in the following line of code:

```java
Queue<CustomerOrder> customerOrders = new PriorityQueue<>(new CustomerOrderComparator());
```

Below is the result when we run this code:

```bash
orderId:2, orderAmount:300.0, customerName:customer2
orderId:1, orderAmount:100.0, customerName:customer1
orderId:3, orderAmount:50.0, customerName:customer3
```

We can see that the data comes in descending order of the orderAmount.

## Code

All the code discussed in this article can be found in [this GitHub repo](https://github.com/aditya-sridhar/java-priority-queue-example).

## Congrats **?**

You now know how to use priority queues in Java.

## **About the author**

I love technology and follow the advancements in the field. I also like helping others with my technology knowledge.

Feel free to connect with me on my LinkedIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Feel free to read more of my articles on my blog at [adityasridhar.com.](https://adityasridhar.com/)




