---
title: How to build up an intuition for recursion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-29T01:21:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-up-an-intuition-for-recursion-986032c2f6ad
coverImage: https://cdn-media-1.freecodecamp.org/images/0*qnRpwEoIjgr_h1Hr
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dawson Eliasen

  And how to use it to solve problems


  _“white corner building” by [Unsplash](https://unsplash.com/@heysupersimi?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Simone Hutsch on <a href="https://unsplash...'
---

By Dawson Eliasen

#### And how to use it to solve problems

![Image](https://cdn-media-1.freecodecamp.org/images/8aza4Gl8EaNwkDwVTGejjq-QqNXHIHXNNIO-)
_“white corner building” by [Unsplash](https://unsplash.com/@heysupersimi?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Simone Hutsch</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Recursion is one of the most intimidating topics that students face in programming. It’s hard to understand because the human brain is not capable of performing recursion — but computers are. This is exactly why recursion is such a powerful tool for programmers, but it also means that learning how to use it is exceedingly difficult. I want to help you build an intuition for recursion so you can use it to solve problems.

I am a teaching assistant for the introductory computer science course at my university. I’ve explained recursion in exactly the same way a dozen times this week. My explanation seems to help most students. This article has the most general explanation at the top, and the most specific explanation at the bottom. This way, you can start at the beginning and stop as soon as you feel you understand recursion well enough. I’ve provided some examples in Java, and they are simple enough that anyone with some programming experience can interpret them.

#### What is Recursion?

To understand recursion, let’s take a step back from programming. Let’s start by establishing a general definition for the term. Something is _recursive_ if it is defined by its own definition to some extent. That probably doesn’t help you understand recursion very much, so let’s look at a mathematical definition. You are familiar with functions — one number goes in, another number comes out. They look like this:

_f(x) = 2x_

Let’s change this idea slightly and instead think about a sequence. A sequence takes an integer number, and an integer number comes out.

_A(n) = 2n_

Sequences can be thought of as functions with inputs and outputs that are limited to only positive integers. Generally, sequences start with 1. This means that A(0) is 1. The sequence above is the following:

_A(n) = 1, 2, 4, 6, 8, 10, … where n = 0, 1, 2, 3, 4, 5, …_

Now, consider the following sequence:

_A(n) = 2 x A(n-1)_

This sequence is _recursively defined._ In other words, the value any given element depends on the value of another element. This sequence looks like this:

_A(n) = 1, 2, 4, 8, 16, … where n = 0, 1, 2, 3, 4, …_

Any element is defined as 2 times the previous element.

* The n = 4 element, 16, is defined as 2 times the previous element.
* The n = 3 element, 8, is defined as 2 times the previous element.
* The n = 2 element, 4, is defined as 2 times the previous element.
* The n = 1 element, 2, is defined as 2 times the previous element.
* **The n = 0 element, 1, is defined as…**

The n = 0 element cannot be recursively defined. There is no previous element. We call this a **base case**, and it is a necessary consequence of recursive definitions. **They must be explicitly represented in your code**. We could represent this recursive sequence in Java like so:

```
public int A(int n){    if (n == 0)        return 1;    return 2 * A(n - 1);}
```

You should familiarize yourself with the anatomy of a recursive method. Note the base case: if n is 0, the element is defined as 1. Otherwise, the element is defined as 2 times the previous element. We must recursively call the method to get the value of the previous element, and then multiply it by 2. All recursive methods will have these two components:

* Base case, which returns a well-defined value.
* Recursive case, which returns a recursively defined value.

![Image](https://cdn-media-1.freecodecamp.org/images/0E2HqB2n-Uaz7t4xog-zDG5IbGJdTFEuUN9c)
_“white rose enclosed photograph” by [Unsplash](https://unsplash.com/@anniespratt?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Annie Spratt</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Let’s do another example, continuing with the mathematics context. The Fibonacci sequence is often used to illustrate recursion. Any element of the Fibonacci sequence is the sum of the two preceding elements. It goes like this:

_F(n) = 1, 1, 2, 3, 5, 8, … where n = 0, 1, 2, 3, 4, 5, …_

* The n = 5, element, 8, is defined as the sum of the n = 4 element and the n = 3 element…

At this point, you should hesitate. In the previous example, each element depended on only one other element, now each element depends on two other elements. This complicates things.

* The n = 4 element, 5, is defined as the sum of the n = 3 element and the n = 2 element.
* The n = 3 element, 3, is defined as the sum of the n = 2 element and the n = 1 element.
* The n = 2 element, 2, is defined as the sum of the n = 1 element and the n = 0 element.
* **The n = 1 element, 1, is defined as the sum of the n = 0 element and…**

The n = 1 element cannot be recursively defined. Neither can the n = 0 element. These elements cannot be recursively defined because the recursive definition requires two preceding elements. The n = 0 element has no preceding elements, and the n = 1 element has only one preceding element. This means that there are two base cases. Before writing any code, I would write down something like this:

_The n = 0 element is defined as 1. The n = 1 element is defined as 1._

_The n element is defined as the sum of the n-1 element and the n-2 element._

Now we have an idea of how this task is recursively defined, and we can go ahead and write some code. Never start writing code without first having a natural understanding of the task.

```
public int F(int n){    if (n == 0 || n == 1)        return 1;    return F(n - 1) + F(n - 2);}
```

#### The Call Stack

![Image](https://cdn-media-1.freecodecamp.org/images/1ddahVRxpZNWjPgx-9mfnaEmalc76XpEG175)
_“assorted-title book lot” by [Unsplash](https://unsplash.com/@gotafli?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">gotafli</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="). It’s a stack of records, do you get it?_

As programmers, we want to have an intuition for recursion so that we may use it to do things. To do so effectively, we must understand how a computer processes recursion.

There is a data structure that the computer uses to keep track of method calls called the **call stack**. Each method call creates **local variables** from the method parameters. The computer needs to store these variables while the method is being executed. Then, the computer ditches the values when the method returns to avoid wasting memory.

The call stack (and stacks in general) function as you might imagine some sort of real-life stack would. Imagine a stack of papers on your desk — it starts as nothing, and then you add papers one by one. You don’t know anything about any of the papers in the stack except for the paper on top. The only way you can remove papers from the stack is by taking them off the top, one-by-one, **in the opposite order that they were added**.

This is essentially how the call stack works, except the items in the stack are **activation records** instead of papers. Activation records are just little pieces of data that store the method name and parameter values.

Without recursion, the call stack is pretty simple. Here’s an example. If you had some code that looked like this…

```
public static void main(String[] args)    System.out.println(myMethod(1));
```

…The call stack would look like this:

```
*  myMethod(int a)
```

```
*  main(String[] args)
```

Here we see two methods under execution, `main` and `myMethod`. The important thing to notice is that `main` cannot be removed from the stack until `myMethod` is removed from the stack. In other words, `main` cannot complete until `myMethod` is called, executed, and returns a value.

This is true for any case of method composition (a method within a method) — so let’s look at recursive example: the `A(int n)` method we wrote earlier. Your code might look like this:

```
public static void main(String[] args)    System.out.println(A(4));
```

```
public static int A(int n){    if (n == 0)        return 1;    return 2 * A(n - 1);}
```

When `main` is called, `A` is called. When `A` is called, it calls itself. So the call stack will start building up like so:

```
* A(4)* main(String[] args)
```

`A(4)` calls `A(3)`.

```
* A(3)* A(4)* main(String[] args)
```

Now, it’s important to note that `A(4)` cannot be removed from the call stack until `A(3)` is removed from the call stack first. This makes sense, because the value of `A(4)` depends on the value of `A(3)`. The recursion carries on…

```
* A(0)* A(1)* A(2)* A(3)* A(4)* main(String[] args)
```

When `A(0)` is called, we have reached a base case. This means that the recursion is completed, and instead of making a recursive call, a value is returned. `A(0)` comes off the stack, and the rest of the calls are then able to come off the stack in succession until `A(4)` is finally able to return its value to main.

Here’s the intuition: the return value of any method call depends on the return value of another method call. Therefore, all the method calls must be stored in memory until a base case is reached. When the base case is reached, the values start becoming well-defined instead of recursively defined. For example, `A(1)` is recursively defined until it knows the definition of the base case, 1. Then, it is well-defined as 2 times 1.

When we are trying to solve problems with recursion, it is often more effective to think about the order in which values are returned. This is the opposite of the order in which calls are made. This order is more useful because it consists of well-defined values, instead of recursively defined values.

For this example, it is more useful to consider that `A(0)` returns 1, and then `A(1)` returns 2 times 1, and then `A(2)` returns 2 times `A(1)`, and so on. However, when we are writing our code, it can easier to frame it in the reverse order (the order that the calls are made). This is another reason that I find it helpful to write the base case and the recursive case down before writing any code.

#### Helper Methods and Recursion vs. Loops

![Image](https://cdn-media-1.freecodecamp.org/images/Aicn9TpaTduZb3eahKIRYtL2DvZzb6cxf6M-)
_“two persons shaking each other's hand” by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We are programmers, not mathematicians, so recursion is simply a tool. In fact, recursion is a relatively simple tool. It’s very similar to loops in that both loops and recursion induce repetition in the program.

You may have heard that any repetitive task can be done using either a while loop or a for loop. Some tasks lend themselves better to while loops and other tasks lend themselves better to for loops.

The same is true with this new tool, recursion. **Any repetitive task can be accomplished with either a loop or recursion, but some tasks lend themselves better to loops and others lend themselves better to recursion.**

When we use loops, it is sometimes necessary to make use of a local variable to “keep track” of a calculation. Here’s an example.

```
public double sum (double[] a){    double sum = 0.0;    for (int i = 0; i < a.length; i++)        sum += a[i];    return sum;
```

```
}
```

This method takes an array of doubles as a parameter and returns the sum of that array. It uses a local variable, `sum`, to keep track of the working sum. When the loop is completed, `sum` will hold the actual sum of all values in the array, and that value is returned. This method actually has two other local variables that are less obvious. There is the double array `a`, whose scope is the method, and the iterator `i` (keeps track of the index), whose scope is the for loop.

What if we wanted to accomplish this same task using recursion?

```
public double recursiveSum(double[] a)    # recursively calculate sum
```

This task is repetitive, so it is possible to do it using recursion, though it is probably more elegantly accomplished using a loop. We just need to create a few local variables to keep track of the working sum and the index, right?

Alas, this is impossible. Local variables only exist in the context of a single method call, and recursion makes use of repeated method calls to accomplish a repetitive task. This means that local variables are pretty much useless when we are using recursion. If you are writing a recursive method and you feel as though you need a local variable, you probably need a helper method.

A **helper method** is a recursive method that makes use of **additional parameters to keep track of values.** For `recursiveSum`, our helper method might look like this:

```
public double recursiveSum(double[] a, double sum, int index){    if (index == a.length)        return sum;    sum += a[index];    return recursiveSum(a, sum, index + 1);}
```

This method builds the sum by passing the working value to a new method call with the next index. When there are no more values in the array, the working sum is the actual sum.

Now we have two methods. The “starter method,” and the helper method.

```
public double recursiveSum(double[] a)    # recursively calculate sum
```

```
public double recursiveSum(double[] a, double sum, int index){    if (index == a.length)        return sum;    sum += a[index];    return recursiveSum(a, sum, index + 1);}
```

The term “helper method” is actually a bit of a misnomer. It turns out that the helper method does all the work, and the other method is just a starter. It simply calls the helper method with the initial values that start the recursion.

```
public double recursiveSum(double[] a)    return recursiveSum(a, 0.0, 0);
```

```
public double recursiveSum(double[] a, double sum, int index){    if (index == a.length)        return sum;    sum += a[index];    return recursiveSum(a, sum, index + 1);}
```

Note that the values used in the starter call to the helper method are the same values used to initialize the local variables in the loop example. We initialize the variable used to keep track of the sum to `0.0`, and we initialize the variable used to keep track of the index to `0`.

Earlier, I said that local variables are useless in the context of recursion. This isn’t completely true, because the method parameters are indeed local variables. They work for recursion because new ones are created every time the method is called. When the recursion is executed, there are many method calls being stored in the call stack, and as a result there are many copies of the local variables.

You might ask, “If the helper method does all the work, why do we even need the starter method? Why don’t we just call the helper method with the initial values, and then you only need to write one method?”

Well, remember that we were trying to replace the method that used a for loop. That method was simple. It took an array as a parameter and returned the sum of the array as a double. If we replaced this method with one that took three parameters, we would have to remember to call it with the proper starting values. If someone else wanted to use your method, it would be impossible if he or she didn’t know the starting values.

For these reasons, it makes sense to add another method that takes care of these starting values for us.

#### Wrapping up

Recursion is a pretty challenging concept, but you made it all the way to the end of my explanation. I hope you understand the magic a little better. I now officially grant you the title of “Grand-Wizard of Recursion.” Congratulations!

