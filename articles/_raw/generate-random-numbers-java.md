---
title: Java Random Number Generator – How to Generate Integers With Math Random
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-25T22:50:46.000Z'
originalURL: https://freecodecamp.org/news/generate-random-numbers-java
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Untitled-design--1-.png
tags:
- name: Java
  slug: java
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: random
  slug: random
seo_title: null
seo_desc: "By Thanoshan MV\nComputer generated random numbers are divided into two\
  \ categories: true random numbers and pseudo-random numbers. \nTrue random numbers\
  \ are generated based on external factors. For example, generating randomness using\
  \ surrounding noise..."
---

By Thanoshan MV

Computer generated random numbers are divided into two categories: true random numbers and pseudo-random numbers. 

True random numbers are generated based on external factors. For example, generating randomness using surrounding noises. 

But generating such true random number is a time consuming task. Therefore, we can utilize pseudo-random numbers which are generated using an algorithm and a seed value. 

These pseudo-random numbers are sufficient for most purposes. For example, you can use them in cryptography, in building games such as dice or cards, and in generating OTP (one-time password) numbers. 

In this article, we will learn how to generate pseudo-random numbers using `Math.random()` in Java. 

## 1. Use Math.random() to Generate Integers

`Math.random()` returns a double type pseudo-random number, greater than or equal to zero and less than one. 

Let's try it out with some code:

```java
    public static void main(String[] args) {
        double randomNumber = Math.random();
        System.out.println(randomNumber);
    }
    // output #1 = 0.5600740702032417
    // output #2 = 0.04906751303932033
```

`randomNumber` will give us a different random number for each execution. 

Let's say we want to generate random numbers within a specified range, for example, zero to four. 

```java
    // generate random numbers between 0 to 4
    public static void main(String[] args) {
        // Math.random() generates random number from 0.0 to 0.999
        // Hence, Math.random()*5 will be from 0.0 to 4.999
        double doubleRandomNumber = Math.random() * 5;
        System.out.println("doubleRandomNumber = " + doubleRandomNumber);
        // cast the double to whole number
        int randomNumber = (int)doubleRandomNumber;
        System.out.println("randomNumber = " + randomNumber);
    }
    /* Output #1
    doubleRandomNumber = 2.431392914284627
    randomNumber = 2
    */
```

When we cast a double to int, the int value keeps only whole number part. 

For example, in the above code, `doubleRandomNumber` is `2.431392914284627` . `doubleRandomNumber`'s whole number part is `2` and fractional part (numbers after the decimal point) is `431392914284627` . So, `randomNumber` will only hold the whole number part `2`. 

You can read more about the `Math.random()` method in the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html). 

Using `Math.random()` is not the only way to generate random numbers in Java. Next, we'll consider how we can generate random numbers using the Random class. 

## 2. Use the Random Class to Generate Integers

In the Random class, we have many instance methods which provide random numbers. In this section, we will consider two instance methods, `nextInt(int bound)`, and `nextDouble()`. 

### How to use the nextInt(int bound) method

`nextInt(int bound)` returns an int type pseudo-random number, greater than or equal to zero and less than the bound value. 

The `bound` parameter specifies the range. For example, if we specify the bound as 4, `nextInt(4)` will return an int type value, greater than or equal to zero and less than four. 0,1,2,3 are the possible outcomes of `nextInt(4)` .

As this is an instance method we should create a random object to access this method. Let's try it.

```java
    public static void main(String[] args) {
        // create Random object
        Random random = new Random();
        // generate random number from 0 to 3
        int number = random.nextInt(4);
        System.out.println(number);
    }
```

### How to use the nextDouble() method

Similar to `Math.random()` , the `nextDouble()` returns a double type pseudo-random number, greater than or equal to zero and less than one. 

```java
    public static void main(String[] args) {
        // create Random object
        Random random = new Random();
        // generates random number from 0.0 and less than 1.0
        double number = random.nextDouble();
        System.out.println(number);
    }
```

For more information, you can read the random class's [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Random.html). 

## So which random number method should you use?

`[Math.random()](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#random--)` [uses the random class](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#random--). If we only want double type pseudo-random numbers in our application, then we can use `Math.random()` . 

Otherwise, we can use the random class as it provides various methods to generate pseudo-random numbers in different types such as `nextInt()`, `nextLong()`, `nextFloat()` and `nextDouble()`. 

Thank you for reading.

Photo image by [Brett Jordan](https://unsplash.com/@brett_jordan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/random-numbers?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

You can connect with me on [Medium](https://mvthanoshan.medium.com/).

**Happy Coding!**

