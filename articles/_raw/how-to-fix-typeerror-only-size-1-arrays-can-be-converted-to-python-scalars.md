---
title: 'TypeError: only size-1 arrays can be converted to Python scalars'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-30T21:39:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-typeerror-only-size-1-arrays-can-be-converted-to-python-scalars
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/brett-jordan-XWar9MbNGUY-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, you can use the numpy library when working with arrays and certain\
  \ math concepts like matrices and linear algebra. \nBut like every other aspect\
  \ of learning and working with a programming language, errors are unavoidable. \n\
  In this article, ..."
---

In Python, you can use the `numpy` library when working with arrays and certain math concepts like matrices and linear algebra. 

But like every other aspect of learning and working with a programming language, errors are unavoidable. 

In this article, you'll learn how to fix the "TypeError: only size-1 arrays can be converted to Python scalars" error which mostly occurs when using the `numpy` library. 

## What Causes the `TypeError: only size-1 arrays can be converted to Python scalars` Error in Python?

The "TypeError: only size-1 arrays can be converted to Python scalars" error is raised when we pass in an array to a method that accepts only one parameter. 

Here's an example:

```python
import numpy as np

y = np.array([1, 2, 3, 4])
x = np.int(y)

print(x)

# TypeError: only size-1 arrays can be converted to Python scalars

```

The code above throws the "TypeError: only size-1 arrays can be converted to Python scalars" error because we passed the `y` array to the NumPy `int()` method. The method can only accept one parameter. 

In the next section, you'll see some solutions for this error. 

## How to Fix the `TypeError: only size-1 arrays can be converted to Python scalars` Error in Python

There are two general solutions for fixing the "TypeError: only size-1 arrays can be converted to Python scalars" error.

### Solution #1 – Using the `np.vectorize()` Function

The `np.vectorize()` function can accept a sequence/an array as its parameter. When printed out, it returns an array.

Here's an example:

```python
import numpy as np

vector = np.vectorize(np.int_)
y = np.array([2, 4, 6, 8])
x = vector(y)

print(x)
# [2, 4, 6, 8]
```

In the example above, we created a `vector` variable which will "vectorize" any parameter passed to it: `np.vectorize(np.int_)`. 

We then created an array and stored it in the `y` variable: `np.array([2, 4, 6, 8])`. 

Using the `vector` variable we created initially, we passed the `y` array as a parameter: `x = vector(y)`. 

When printed out, we got the array — `[2, 4, 6, 8]`.

### Solution #2 – Using the `map()` Function

The `map()` function accepts two parameter in this case — the NumPy method and the array. 

```python
import numpy as np

y = np.array([2, 4, 6, 8])
x = np.array(list(map(np.int_, y)))

print(x)
# [2, 4, 6, 8]
```

In the example above, we nested the `map()` function in a `list()` method so that we get the array retuned as a list and not a map object. 

### Solution #3 – Using the `astype()` Method

We can use the `astype()` method to convert a NumPy array to integers. This will prevent the "TypeError: only size-1 arrays can be converted to Python scalars" error from being raised. 

Here's how: 

```python
import numpy as np

vector = np.vectorize(np.int_)
y = np.array([2, 4, 6, 8])
x = y.astype(int)

print(x)
# [2 4 6 8]
```

## Summary

In this article, we talked about the "TypeError: only size-1 arrays can be converted to Python scalars" error in Python.

It is raised when we pass an array as a parameter to a `numpy` method that accepts only one parameter. 

To fix the error, we used different methods like the `np.vectorize()` function, `map()` function, and `astype()` method. 

Happy coding!

