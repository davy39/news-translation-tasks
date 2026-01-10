---
title: Java For Loop Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-07T17:41:44.000Z'
originalURL: https://freecodecamp.org/news/java-for-loop-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/java-for-loop.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "You can use loops in programming to carry out a set of instructions repeatedly\
  \ until a certain condition is met.\nThere are three types of loops in Java: \n\n\
  for loop.\nwhile loop. \ndo...while loop.\n\nIn this article, we'll focus on the\
  \ for loop, its synt..."
---

You can use loops in programming to carry out a set of instructions repeatedly until a certain condition is met.

There are three types of loops in Java: 

* `for` loop.
* `while` loop. 
* `do...while` loop.

In this article, we'll focus on the `for` loop, its syntax, and some examples to help you use it in your code. 

The `for` loop is mostly used when you know the number of times a loop is expected to run before stopping. 

## Java For Loop Syntax

Here's what the syntax of `for` loop in Java looks like:

```java
for (initialization; condition; increment/decrement) {
   // code to be executed
}
```

In the syntax above:

* **initialization** denotes an initial variable declared at the starting point of the loop, usually an integer.
* **condition** denotes the number of times the loop is supposed to run.
* **increment/decrement** increases/decreases the value of the initial variable every time the loop runs. As the increment/decrement happens, the variable's value tends towards the specified **condition**.

## Java For Loop Example

In this section, you'll see some practical code examples of the `for` loop in Java:

#### Java For Loop Example #1

```java
class ForLoopExample {
    public static void main(String[] args) {
        for(int x = 1; x <=10; x++) {
            System.out.println(x);
            // 1
            // 2
            // 3
            // 4
            // 5
            // 6
            // 7
            // 8
            // 9
            // 10
        }
    }
}
```

In the code above, we used a `for` loop to print numbers from 1 to 10. 

But how does it work? Take a look the conditions given: `(int x = 1; x <=10; x++)`.

At first, `x` was set to 1. 

The second condition —  `x <=10` — denotes that the loop is expected to run as long the value of `x` is less than or equal to 10. 

The third condition — `x++` — increases the value of `x` every time the loop runs. 

The loop then prints the value of `x` every time it is increased.

#### Java For Loop Example #2

In this example, you'll learn how to print all the values stored in an array. 

```java
class ForLoopExample {
    public static void main(String[] args) {
        int[] oddNumbers = {1, 3, 5, 7};
        for (int i = 0; i < oddNumbers.length; i++) {
          System.out.println(oddNumbers[i]);
          // 1
          // 3
          // 5
          // 7
        }
    }
}
```

The conditions in the code above are a bit different compared to the first example, but the logic is the same. 

`i` has an initial value of 0 because the index of an array in Java starts at 0. The first element is 0, the second is 1, and so on. 

`i < oddNumbers.length` means that the code is expected to run as long as the value of `i` is less than the length of the array. The length of the array is 4 so that means `i < 4`. 

i++ increases the value of `i` every time the code runs until the condition `i < 4` is `false`.

The code prints 1, 3, 5, 7 in the console. 

Without a loop, you'd achieve the same result by doing something like this:

```java
class ForLoopExample {
    public static void main(String[] args) {
        int[] oddNumbers = {1, 3, 5, 7};
          System.out.println(oddNumbers[0]); // 1
          System.out.println(oddNumbers[1]); // 3
          System.out.println(oddNumbers[2]); // 5
          System.out.println(oddNumbers[3]); // 7
    }
}
```

Imagine having an array with 100 elements. You'd have to type one hundred `println` methods to print all of them. 

With a loop, you can achieve that with a line of code. 

## Summary

In this article, we talked about the `for` loop in Java. We use loops to execute code repeatedly until a condition is met. 

We first saw the syntax for using the `for` loop in Java. We then looked at some practical code examples showing how the loop works. 

Happy coding!

