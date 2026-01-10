---
title: Nested Functions in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T00:54:00.000Z'
originalURL: https://freecodecamp.org/news/nested-functions-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e24740569d1a4ca3b94.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'A nested function is simply a function within another function, and is
  sometimes called an "inner function". There are many reasons why you would want
  to use nested functions, and we''ll go over the most common in this article.

  How to define a nested ...'
---

A nested function is simply a function within another function, and is sometimes called an "inner function". There are many reasons why you would want to use nested functions, and we'll go over the most common in this article.

### How to define a nested function

To define a nested function, just initialize another function within a function by using the `def` keyword:

```py
def greeting(first, last):
  # nested helper function
  def getFullName():
    return first + " " + last

  print("Hi, " + getFullName() + "!")

greeting('Quincy', 'Larson')
```

**Output:**

```sh
Hi, Quincy Larson!
```

As you can see, the nested `getFullName` function has access to the outer `greeting` function's parameters, `first` and `last`. This is a common use case for nested functions–to serve as small helper function to a more complex outer function.

## Reasons to use nested functions

While there are many valid reasons to use nested functions, among the most common are encapsulation and closures / factory functions.

### Data encapsulation

There are times when you want to prevent a function or the data it has access to from being accessed from other parts of your code, so you can _encapsulate_ it within another function. 

When you nest a function like this, it's hidden from the global scope. Because of this behavior, data encapsulation is sometimes referred to as **data hiding** or **data privacy**. For example:

```py
def outer():
  print("I'm the outer function.")
  def inner():
    print("And I'm the inner function.")
  inner()

inner()
```

**Output:**

```sh
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    inner()
NameError: name 'inner' is not defined
```

In the code above, the `inner` function is only available from within the function `outer`. If you try to call `inner` from outside the function, you'll get the error above.

Instead, you must call the `outer` function like so:

```py
def outer():
  print("I'm the outer function.")
  def inner():
    print("And I'm the inner function.")
  inner()

outer()
```

**Output:**

```sh
I'm the outer function.
And I'm the inner function.
```

### Closures

But what would happen if the outer function returns the inner function itself, rather than calling it like in the example above? In that case you would have what's known as a closure.

The following are the conditions that are required to be met in order to create a closure in Python:

These are the conditions you need to create a closure in Python:

> 1. There must be a nested function  
>   
> 2. The inner function has to refer to a value that is defined in the enclosing scope  
>   
> 3. The enclosing function has to return the nested function  
>   
> - Source: [https://stackabuse.com/python-nested-functions/](https://stackabuse.com/python-nested-functions/)

Here's a simple example of a closure:

```py
def num1(x):
  def num2(y):
    return x + y
  return num2

print(num1(10)(5))
```

**Output:**

```sh
15
```

Closures make it possible to pass data to inner functions without first passing them to outer functions with parameters like the `greeting` example at the beginning of the article. They also make it possible to invoke the inner function from outside of the encapsulating outer function. All this with the benefit of data encapsulation / hiding mentioned before.

Now that you understand how and why to nest functions in Python, go out and nest 'em with the best of 'em.

