---
title: A quick intro to function composition in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-12T20:42:35.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-function-composition-in-swift-17f5c9999cee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_o81YbJg_qxXhHaZFWiWhQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Boudhayan Biswas

  Programmers come across functions every day. A function represents a special type
  of relationship: every input value that the function takes is associated with some
  output value. So in a more generic way, a function is a rule whic...'
---

By Boudhayan Biswas

Programmers come across functions every day. A function represents a special type of relationship: every input value that the function takes is associated with some output value. So in a more generic way, a function is a rule which maps some input values to one output value.

The basic idea behind function composition is applying one function to the result of another function. So it is a mathematical concept of combining functions into one function.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QDF5FSC7IE8GxFd-Y5DbrQ.jpeg)
_Function Composition_

#### Getting started

Let’s discuss it along with the mathematical concept. In the above diagram, “f” and “g” are two functions. We can represent the functions as below:

```
f: A -> Bg: B -> C
```

If we do composition of these two functions, then we can represent it as “g o f” (you can say g of f).

```
(g o f): A -> C such that (g o f)(a) = g(f(a)) for all a in A
```

Let’s try to explore it more with a simple example:

```
Let f(a) = 2a + 3 & g(a) = 3a + 5, then function composition
```

```
(g o f)(a) = g(f(a)) = 3(f(a)) + 5 = 3(2a + 3) + 5 = 6a + 14
```

This concept is not only applicable in mathematics — we can also apply it in programming languages. Those languages are called functional programming languages. Understanding this concept improves your code readability and makes it easier to understand for other programmers.

#### An introduction to Swift as a functional programming language

Now, the good news is that swift is also a functional programming language. In Swift programming, a function has the most important role, so you’ll interact with them daily. A Swift function can return a value, and then we can use the returned value as an input into another function. This is a common programming practice.

#### Implementing function composition in swift

Suppose we have an array of integers, and we want the output to be a squared array of unique even integers. So for that normally, we would implement functions like below:

This code gives us the correct output, but as you can see, the code’s readability is not great. Also, the function calling order looks like the opposite from what we’d want, and it might create confusion for some new programmers. This block of code is hard to analyze.

So here comes function composition to rescue us from all of the above problems. We can achieve function composition by taking advantage of generics, closure, and the infix operator.

So let’s look what is happening in the above block of code:

1. We have declared a custom infix operator “>>>”. It has left associativity and precedence order just like the + operator.
2. We have declared a function whose name is the same as the infix operator’s name. The function uses three generics T, U, V and it takes two closures as input parameters.
3. The left parameter is a closure, and it takes an input of type T and returns an output of type U.
4. The right parameter is also a closure, and it takes an input of type U and returns the output of type V.
5. Now, the >>> function returns a function or closure, which has the type of (T) → V. The output closure takes an input of type T and returns the output of type V. Here the output of the left parameter is the input of the right parameter.

```
left :  (T) -> U right: (U) -> V
```

```
Output Type: (T) -> V
```

If you understand the mathematical representation of function composition, then you can see that it is exactly the same with Swift’s implementation.

6. In the function body, it returns the result of the right parameter on the left parameter.

Now if we want the same result (a squared array of unique even integers), we can do this with function composition.

It is a chain of functions which returns the same result. The function order now looks similar to what a human being might think. It has better readability and is easier to understand for everyone.

Thank you for reading!

