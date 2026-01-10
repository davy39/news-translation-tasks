---
title: For Loop in Java + forEach Loop Syntax Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-07T15:08:46.000Z'
originalURL: https://freecodecamp.org/news/for-loop-in-java-foreach-loop-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/loop.jpg
tags:
- name: Java
  slug: java
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'A loop in programming is a sequence of instructions that run continuously
  until a certain condition is met.

  In this article, we will learn about the for and forEach loops in Java.

  Syntax for a for loop in Java

  Here is the syntax for creating a for lo...'
---

A loop in programming is a sequence of instructions that run continuously until a certain condition is met.

In this article, we will learn about the `for` and `forEach` loops in Java.

## Syntax for a `for` loop in Java

Here is the syntax for creating a `for` loop:

```java
for (initialization; condition; increment/decrement) {
   // code to be executed
}
```

Let's break down some of the keywords above.

**for** specifies that we are going to create a loop. It is followed by parenthesis nesting everything required for our loop to work. 

**initialization** defines an initial variable as the starting point of the loop, usually an integer (whole number). 

**condition** specifies the number of times the loop is supposed to run.

**increment/decrement** increases/decreases the value of the initial variable every time the loop runs. As the increment/decrement happens, the variable's value tends towards the specified **condition**.

Note that each keyword is separated by a semi colon (;).

Here are a few examples:

```java
for(int x = 1; x <=5; x++) {
  System.out.println(x);
}

/*
1
2
3
4
5
*/
```

In the example above, the initial variable is `x` with a value of 1. The loop will keep running as long as the value of `x` is less than or equal to 5 – this is the condition. `x++` increases the value of `x` after each run.

We went on to print the value of `x` which stops after 5 because the condition has been met. Incrementing to 6 is impossible because it is greater than and not equal to 5. 

In the next example, we will use the `for` loop to print all the values of an array.

```java
int[] randomNumbers = {2, 5, 4, 7};
for (int i = 0; i < randomNumbers.length; i++) {
  System.out.println(randomNumbers[i]);
}

// 2
// 5
// 4
// 7
```

This is almost the same as the last example. Here, we used the length of the array as the condition and the initial variable's value as zero because the index number of the first element of an array is zero.

## Syntax for a `forEach` loop in Java

You use a `forEach` loop specifically for looping through the elements of an array. Here is what the syntax looks like:

```java
for (dataType variableName : arrayName) {
  // code to be executed
}
```

You'll notice that the syntax here is shorter than the `for` loop's. The `forEach` loop also starts with the **for** keyword.

Instead of initializing a variable with a value, we first specify the **data type** (this must match the array's data type). This is followed by our **variable's name** and the **name of the array** separated by a colon. 

Here is an example to help you understand the syntax better:

```java
int[] randomNumbers = {2, 5, 4, 7};
for (int x : randomNumbers) {
  System.out.println(x + 1);
}

/*
3
6
5
8
*/
```

In this example, we looped through each element and increased their initial value by 1. 

By default, the loop will stop once it has iterated through all the elements in the array. This means that we are not required to pass any value to our variable or specify any condition to terminate the loop.

## Conclusion

In this article, we learned what loops are as well as the syntax for creating a `for` and `forEach` loop in Java. We also saw a few examples that helped us understand when and how to use them. 

Happy Coding!  

