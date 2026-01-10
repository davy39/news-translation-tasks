---
title: How to make your code more readable with abstraction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-05T11:14:16.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-understandable-by-using-abstraction-4b522307130c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*0jBreLbQiLwEDd_g.jpg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Tiago Antunes

  While you’re learning how to program, it’s common to see people using a term called
  abstraction. You start questioning yourself: what is abstraction and why is it important?

  In this article, I will be explaining to you the concept of...'
---

By Tiago Antunes

While you’re learning how to program, it’s common to see people using a term called **abstraction.** You start questioning yourself: what is abstraction and why is it important?

In this article, I will be explaining to you the concept of abstraction and how to use it, and I’ll give some examples in Python.

### First things first: What’s abstraction?

According to my [Foundations of Programming teacher](https://en.wikipedia.org/wiki/Jo%C3%A3o_Pav%C3%A3o_Martins):

> “Abstraction is a simplified specification of an entity”

What this means is that an abstraction is a representation of a computation entity. It is a way to conceal its particular information and only give the most relevant information to the programmer.

An abstraction is also situational: each one suits a need, so you can associate _good abstraction with the particular use of that entity._

Let’s take a look into Binary Search Tree’s (If you don’t know what they are check out my [article](https://medium.freecodecamp.org/trees-in-programming-the-oxygen-of-efficient-code-6c7c11a3dd64) about them). We can define a node as an entity with the following properties:

```
A Node has:    Node * left    Node * right    int val
```

Here we would say a Node has two pointers to other nodes and an int value. But **how useful** is this to someone compared to a function `insert(node, value)` and it would just correctly insert it? That way, you would just need to call it and it was done. Simple.

This is how abstraction is useful. All the libraries you use in your programs use it so that it becomes really simple to use a library.

### Ok but how good is Data Abstraction?

Data abstraction allows us to transform a complex data structure into one that’s simple and easy to use. The effect of this is that a program with a high level of code complexity can be transformed into one that looks close to English (let’s call it _high-level code_).

A data type is made of 2 things: properties and methods, which can be public or private. The public ones are the only way to use the data. They should cover all the functionalities you wish the data to be able to do.

What happens then if you’re using your abstract code? It doesn’t really matter if your internal properties change as long as the methods still receive the same arguments and do the same thing as before. If something is wrong, you only need to change it once.

Let’s pick an example and work with it: Vectors

We’ll assume that Vectors are:

* Objects with 2 values, x and y
* x and y are both non-negative numbers

This way Vectors are something like (2 ,5), (0, 19), and so on.

A good way to create abstractions is to use Objects. They provide information concealment and representation anonymity. This allows the user to keep the abstraction.

Let’s start by defining our class (I won’t be defining type validation to keep the code cleaner, but you should do it):

![Image](https://cdn-media-1.freecodecamp.org/images/20fnPffDOv4fnL3eURvntvd9XCYz9XS4ui0v)

So we defined multiple methods and we have a lot of stuff now that we can do:

![Image](https://cdn-media-1.freecodecamp.org/images/hpEw8SBFt3eI6dQi0klMZHYXrWD9ZlQZ5oUe)

For a 2D Vector this may seem simple. If you start implementing this in bigger and more complex programs, you’ll notice they come in really handy.

Let’s now make a different implementation of the class vector (change its internal state) to something with the same methods but with different code:

![Image](https://cdn-media-1.freecodecamp.org/images/UtEBOgQTBAPSEEFf1QCa1AUEDnXtWvZV4f8-)
_The implementation is different, but the output is the same_

If we run the same commands, the output will still be the same. This is because of the abstraction we used, even if the code changed entirely. This is why it’s very important to use abstraction. It allows for flexibility in your code and independence of other people’s code.

Let’s now use another example, this time with 2 classes: City and Citizen.

![Image](https://cdn-media-1.freecodecamp.org/images/RdwMtL7GiE7tKQPC3BzTc9-oPhaYGevI5oN4)
_A City is made of Citizens_

And we get the following:

![Image](https://cdn-media-1.freecodecamp.org/images/4ACkQNAQl4-GxE9XaPu7uwvcmmza9FZ5CDEX)

```
### OUTPUT ###City population is 1000, random: Citizen is a female 20 years oldCity population is 1000, random: Citizen is a male 74 years old
```

But imagine now that we want to change how the Citizen class works inside. If we didn’t use abstraction, we would have to change the whole code! That’s a lot of work!

![Image](https://cdn-media-1.freecodecamp.org/images/J9d8o3vpSR3cO1tzWQNnAhvB3B13ccR2o2aE)
_Now we’ve changed the Citizen class, really fast — and everything still works!_

Now if the code is run again we know that it’s working, although the results are different. As you can see, we changed a whole class, but everything works!

### Wrapping up

At first abstraction might look like it’s not needed. The lower the level of the language you’re using, the more important it is to use abstraction. This avoids having complex code and really keeps it all simple. In languages like C it’s really really useful. If you doubt it, check this [project I made](https://github.com/TiagoMAntunes/critical_path) where I implemented abstraction and it was really easy to understand what was going on.

If you have any questions or something you want to talk about or discuss, leave a comment below!

Don’t forget to follow me on [Instagram](https://www.instagram.com/tm.antunes/) and [Twitter](https://twitter.com/tm_antune)!

