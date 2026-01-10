---
title: A quick introduction to Functional Reactive Programming (FRP)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-11T11:26:26.000Z'
originalURL: https://freecodecamp.org/news/functional-reactive-programming-frp-imperative-vs-declarative-vs-reactive-style-84878272c77f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2K8v7kw0Nz1ncohxmil5KA.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Reactive Programming
  slug: reactive-programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Navdeep Singh

  FRP represents an intersection of two programming paradigms. But, before we dig
  deeper into the concepts, we need to know a bit more about some basic terms.


  FRP: reacting to events

  Imperative programming

  Traditionally, we write code...'
---

By Navdeep Singh

FRP represents an intersection of two programming paradigms. But, before we dig deeper into the concepts, we need to know a bit more about some basic terms.

![Image](https://cdn-media-1.freecodecamp.org/images/zmvecVovUlqx5GTj1gMqLVhLKHEiES7Fy42x)
_FRP: reacting to events_

### Imperative programming

Traditionally, we write code that describes how it should solve a problem. Each line of code is sequentially executed to produce a desired outcome, which is known as imperative programming. The imperative paradigm forces programmers to write “how” a program will solve a certain task. Note that in the previous statement, the keyword is “how.”

Here’s an example:

```
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]var numbersLessThanFive = [Int]()for index in 0..<numbers.count     {    if numbers[index] < 5         {        numbersLessThanFive.append(numbers[index])        }    }
```

As you can see, we sequentially execute a series of instructions to produce a desired output.

### Functional programming

Functional programming is a programming paradigm where you model everything as a result of a function that avoids changing state and mutating data. We will discuss concepts such as state and data mutability and their importance in subsequent sections, but for reference:

* consider **state** as one of the different permutations and combinations that your program can have at any given time during its execution
* **data mutability** is the concept where a given dataset might change over a given course of time during program execution.

The same example that was given using imperative programming can be used in the following way using the functional approach:

```
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]let numbersLessThanFive = numbers.filter { $0 < 5 }
```

We feed the filter function with a closure containing a certain criterion. That criterion is then applied to each element in the numbers array, and the resulting array contains elements that satisfy our criteria.

**Notice the declaration of the two arrays in both the examples.**

In the first example, the `numbersLessThanFive` array was declared as a `var`, whereas in the second example, the same array was declared as a `let`.

Does it ring some bells?

Which approach is better, which array is safer to work with?

What if more than one thread is trying to work with the same array and its elements?

Isn’t a constant array more reliable?

### Reactive programming

Reactive programming is the practice of programming with asynchronous data streams or event streams. An **event stream** can be anything like keyboard inputs, button taps, gestures, GPS location updates, accelerometer, and iBeacon. You can listen to a stream and react to it accordingly.

You might have heard about reactive programming, but it might have sounded too intimidating, scary, or cryptic to even try out. You might have seen something like this:

```
var twoDimensionalArray = [ [1, 2], [3, 4], [5, 6] ]let flatArray = twoDimensionalArray.flatMap { array in    return array.map { integer in        return integer * 2    }}print(flatArray)Output : [2, 4, 6, 8, 10, 12]
```

At first glance, the preceding code might feel a bit obscure, and this might be the reason you turned your back on this style of programming. Reactive programming, as we mentioned earlier, is programming with event streams.

However, the bigger question still remains unanswered. **What is functional reactive programming (FRP)?**

FRP is the **combination** of functional and reactive paradigms. In other words, it is reacting to data streams using the functional paradigm. FRP is not a utility or a library — it changes the way you architect your applications and the way you think about your applications.

In the next blog I will talk about basic building blocks of reactive programming — till then stay tuned and enjoy reading:)

To have a solid grasp over reactive concepts and write iOS applications in RxSwift you can read my book: [Reactive programming in Swift 4](https://www.amazon.com/Reactive-Programming-Swift-easy-maintain-ebook/dp/B078MHNSL1/ref=asap_bc?ie=UTF8).

More of my projects and downloadable code are in [my public github repos](https://github.com/NavdeepSinghh)

You can read more about the topic [here](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754)

Thanks for reading, please share it if you found it useful :)

