---
title: Multiple Inheritance in C++ and the Diamond Problem
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-21T18:03:55.000Z'
originalURL: https://freecodecamp.org/news/multiple-inheritance-in-c-and-the-diamond-problem-7c12a9ddbbec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QVZomxLNxnRYhm9gGIfYyw.png
tags:
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: software design
  slug: software-design
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Onur Tuna

  Unlike many other object-oriented programming languages, C++ allows multiple inheritance.

  Multiple inheritance allows a child class to inherit from more than one parent class.

  At the outset, it seems like a very useful feature. But a use...'
---

By Onur Tuna

Unlike many other object-oriented programming languages, C++ allows multiple inheritance.

Multiple inheritance allows a child class to inherit from more than one parent class.

At the outset, it seems like a very useful feature. But a user needs to be mindful of a few _gotchas_ while implementing this feature.

In the examples below, we will cover a few scenarios that one needs to be mindful about.

We’ll start with a simple example to explain this concept in C++.

The output of this code is as follows:

```
I'm breathing as a snake.I’m crawling as a snake.
```

In the example above, we have a base class named as **LivingThing**. The **Animal** and **Reptile** classes inherit from it. Only the **Animal** class overrides the method `breathe()`. The **Snake** class inherits from the **Animal** and **Reptile** classes. It overrides their methods. In the example above, there is no problem. Our code works well.

Now, we’ll add a bit of complexity.

What if **Reptile** class overrides the `breathe()` method?

The **Snake** class would not know which `breathe()` method to call. This is the “Diamond Problem”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cI0TQYv7yOgSsHhfES1Kaw.png)

#### Diamond Problem

Look at the code below. It is like the code in the example above, except that we have overridden the `breathe()` method in the **Reptile** class.

If you try compiling the program, it won’t. You’ll be staring at an error message like the one below.

```
member ‘breathe’ found in multiple base classes of different types
```

The error is due to the “Diamond Problem” of multiple inheritance. The **Snake** class does not know which `breathe()` method to call.

In the first example, only the **Animal** class had overridden the `breathe()` method. The **Reptile** class had not. Hence, it wasn’t very difficult for the **Snake** class to figure out which `breathe()` method to call. And the **Snake** class ended up calling the `breathe()` method of the **Animal** class.

In the second example, the Snake class inherits **two** `breathe()` methods. The `breathe()` method of the **Animal** and **Reptile** class. Since we haven’t overridden the `breathe()` method in the **Snake** class, there is ambiguity.

C++ has many powerful features such as multiple inheritance. But, it is not necessary that we use all the features it provides.

I don’t prefer using multiple inheritance and use _virtual_ inheritance instead.

Virtual inheritance _solves_ the classic “Diamond Problem”. It ensures that the child class gets only a single instance of the common base class.

In other words, the **Snake** class will have only **one** instance of the **LivingThing** class. The **Animal** and **Reptile** classes share this instance.

This solves the compile time error we receive earlier. Classes derived from abstract classes must override the pure virtual functions defined in the base class.

I hope you enjoyed this overview of multiple inheritance and the “Diamond Problem”.

