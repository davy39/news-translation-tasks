---
title: How to Write Clean Code in C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T21:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-clean-code-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e51740569d1a4ca3c7c.jpg
tags:
- name: C++
  slug: c-2
- name: clean code
  slug: clean-code
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "Clean Code Guidelines\nWhen coding, the coding style you follow can be\
  \ really important. Especially when you are working with a team or you plan on sharing\
  \ your code. \nMost of these guidelines are standard and can be applied to most\
  \ programming langua..."
---

# **Clean Code Guidelines**

When coding, the coding style you follow can be really important. Especially when you are working with a team or you plan on sharing your code. 

Most of these guidelines are standard and can be applied to most programming languages. However, here you have applications and snippets with C++ code, so you can get familiar with it more easily. 

Remember that these are only recommendations for achieving clarity, which can be a personal preference. So take these pieces of advice into account but don’t take them to the letter. Sometimes breaking some of these rules can lead to cleaner code.

## **Use good variable names and make comments**

Make sure you create good variable names. For example, if you are creating a game, avoid using the variable “a” and instead use something like “p1” when referring to player 1. 

The [hungarian notation](https://en.wikipedia.org/wiki/Hungarian_notation) is commonly used and can give you some guidelines for declaring variables.

Also, PLEASE, use comments.Not kidding, just try to read some old projects you made without comments… now imagine being someone else who didn’t even code it.

## **Global variables**

Global variables can be easy to use, and when you're just working with a little code it might look like a great solution. But when the code gets larger and larger, it becomes harder to know when are they being used.

Instead of using global variables you could use variables declared in functions. This can help you tell what values are being passed so you can identify errors faster.

```cpp
#include <iostream>
using namespace std;

// Global variables are declared outside functions
int cucumber; // global variable "cucumber"
```

## **Using goto, continue, etc.**

This is a common discussion among programmers. Just like global variables, these types of statements are usually considered bad practice. They are considered bad because they lead to [“spaguetti code”](https://en.wikipedia.org/wiki/Spaghetti_code). 

When we program we want a linear flow. But when using those statements the flow is modified and lead to a “twisted and tangled” flow.

Goto was used in the past. But when while, for, if functions came around, however, with the introduction of those structured programming was created. In general avoid using goto unless you are sure it will make your code cleaner and easier to read. An example might be using it in nested loops.

The usage of break and continue are practically the same. Use them in switches and try to make functions with one purpose so you only have one exit point.

![img](https://imgs.xkcd.com/comics/goto.png)

## **Avoid changing the control variable inside of a for loop**

Usually there are work arounds to get around this that look clearer and less confusing, eg. while loops. Do this:

```cpp
int i=1;
while (i <= 5)
{
    if (i == 2)
        i = 4;

    ++i;
}
```

Instead of:

```cpp
for (int i = 1; i <= 5; i++)
{
    if (i == 2)
    {
       i = 4;
    }
    // Do work
}
```

## **Declare constants and types at the top**

They are usually declared after libraries. This groups them together and makes them easier to read. For local variables it's the same: declare them at the top (Other people prefer declaring them as late as possible in order to save memory see: [cplusplus.com](http://www.cplusplus.com/forum/general/33612/)).

## **Use only one return function at the end**

Just like I said before, I tend to make only one entry and exit to make the flow clearer.

## **Use curly braces even when writing one-liners**

Doing this systematically will help you do it faster. And in case you want to change the code in the future you will be able to do it without worries.

Instead of:

```cpp
for (int i = 1; i <= 5; i++)
    //CODE
```

Do this:

```cpp
for (int i = 1; i <= 5; i++)
{
    //CODE
}
```

## **Other recommendations**

Use `for` when you know the number of iterations, but use `while` and `do while` when you don’t.

Use const, pass by value/reference when suitable. This will help with saving memory.

Write const in caps, datatypes starting with T and variables in lower case.

```cpp
const int MAX= 100;             //Constant
typedef int TVector[MAX];       //Data type
TVector vector;                 //Vector
```

