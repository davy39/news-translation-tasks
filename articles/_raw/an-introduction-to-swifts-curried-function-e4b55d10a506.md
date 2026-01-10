---
title: An introduction to function currying in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T05:01:42.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-swifts-curried-function-e4b55d10a506
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kx8jzRIUN8lytiKmR8ALPA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Boudhayan Biswas

  When you hear the word “curry”, the very first thing that probably passes through
  your mind is a great part of Indian cuisine. Indian people use a very complex combination
  of spices to prepare the dish. They put all the ingredient...'
---

By Boudhayan Biswas

When you hear the word “**curry**”, the very first thing that probably passes through your mind is a great part of Indian cuisine. Indian people use a very complex combination of spices to prepare the dish. They put all the ingredients in one by one to make a great curry.

So the main trick is to put all the ingredients one by one. Similarly, in programming, **currying** is the technique of converting a function that takes multiple arguments into a function that takes one argument at a time and then returns a function.

But in any programming language, we can easily declare a function that takes multiple arguments at a time, and most programmers are used to it. So why use currying?

Besides making your food exceptional, it is used to allow the chaining of operations on a particular dataset. So instead of writing complex algorithms with some nested loops, you can accomplish the same with some simple commands.

It makes use of code reusability, and the less code you have to write, the fewer errors you’ll have! You can present currying / un-currying as a way to state the elimination and introduction of rules for and in constructive logic. This provides a connection to a more elegant motivation for why it exists.

Programmers have the option to declare every function in two equivalent ways. In currying, a function takes just one argument and returns a function. Then the returned function takes one argument and returns the final result.

So in every programmer’s mind, there may be one question: why would we take the more complicated direction, that is, first writing a function that returns a function, and then again calling the second function?

Lets first look at the more popular style of defining a function:

```swift
func multiply1(_ x: Int, _ y: Int) -> Int {
  return x*y
}
```

The above function takes two arguments and returns their multiplication result.

Now we can define the same function in a different way:

```
func multiply2(_ x: Int) -> (Int) -> Int {
  return { $0 * x }
}
```

The difference between these two functions is in their calling style:

```
multiply1(3, 4) //returns 12
```

```
multiply2(3)(4) //returns 12
```

In the first function, we pass both the arguments at the same time. In the second function, we pass the first argument (which itself returns a function), and then we pass the second argument.

Actually, both the functions are doing the same thing here. These two examples show how we can always transform a function that takes multiple arguments at a time into a series of functions that take one argument at a time. This is the process of **currying**. So **_multiply2_** function is the curried version of **_multiply1_**.

We can represent the second function as a chain of functions like this:

```
//Benefit: 1
```

```
multiply2(3)(multiply2(4)(multiply2(5)(6))) //returns 360
```

```
//Benefit: 2
```

```
let multiplier = multiply2(2)
```

```
let integerList = 1...100
```

```
let x = integerList.map(multiplier) //returns [2, 4, 6, 8, 10, 12 ...]
```

These are some of the benefits of the curried function. You can always chain up the operations with some simple steps. Awesome, right?

Let’s look at an another example:

Now let’s create a **MorningWalk** for Sunday and add 100 steps into it.

So basically here we are calling the **_addSteps()_** instance method on the instance itself.

But we can also do the same thing in the curried way like this:

This is doing the same thing as we did above. First, we are assigning the **_addSteps_** and **_minusSteps_** methods into two different variables. Here at this stage, we are not calling any functions. We have just made references to the functions, the same as function pointers. In the next step, we are actually calling the functions that are stored inside **_stepIncreaser_** and **_stepDecreaser_**.

Now, **_stepIncreaser_** takes a single argument which is the **MorningWalk** instance, and returns a function whose type is **_(Int) ->_** (). So the returned function takes an argument of type Int and returns nothing. Here, the returned function a**_nd addStep_**s() function have the same type of method signature. The same concept applies to t**_he stepDecrea_**ser.

So, at last, we can say that an instance method in Swift is also a type method. It takes an instance of the class as an argument and returns a function, which will then take other arguments and return/update the final result.

We can call the above methods like this also:

#### Conclusion

In this article, we had a function with more than one argument. We transformed it into a function which always took a single argument at a time, resulting in another function, until there was no argument left. This then gave us the final result. So we can say that functions are nothing more than ordinary values which can be produced and returned by other functions.

Now you have something new and interesting to try out on your daily programming tasks!

