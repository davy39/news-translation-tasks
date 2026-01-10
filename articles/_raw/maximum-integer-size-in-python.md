---
title: Int Max in Python – Maximum Integer Size
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-03T18:20:55.000Z'
originalURL: https://freecodecamp.org/news/maximum-integer-size-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/thomas-t-OPpCbAAKWv8-unsplash.jpg
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: "You can check the maximum integer size in Python using the maxsize property\
  \ of the sys module. \nIn this article, you'll learn about the maximum integer size\
  \ in Python. You'll also see the differences in Python 2 and Python 3.\nThe maximum\
  \ value of an ..."
---

You can check the maximum integer size in Python using the `maxsize` property of the `sys` module. 

In this article, you'll learn about the maximum integer size in Python. You'll also see the differences in Python 2 and Python 3.

The maximum value of an integer shouldn't bother you. With the current version of Python, the `int` data type has the capacity to hold very large integer values. 

## What Is the Maximum Integer Size in Python?

In Python 2, you can check the max integer size using the `sys` module's `maxint` property. 

Here's an example:

```python
import sys

print(sys.maxint)
# 9223372036854775807
```

Python 2 has a built-in data type called `long` which stores integer values larger than what `int` can handle. 

You can do the same thing for Python 3 using `maxsize`: 

```python
import sys

print(sys.maxsize)
# 9223372036854775807
```

Note that the value in the code above is not the maximum capacity of the `int` data type in the current version of Python. 

If you multiply that number (9223372036854775807) by a very large number in Python 2, `long` will be returned. 

On the other hand, Python 3 can handle the operation: 

```python
import sys

print(sys.maxsize * 7809356576809509573609874689576897365487536545894358723468)
# 72028601076372765770200707816364342373431783018070841859646251155447849538676
```

You can perform operation with large integers values in Python without worrying about reaching the max value. 

The only limitation to using these large values is the available memory in the systems where they're being used. 

## Summary

In this article, you have learned about the max integer size in Python. You have also seen some code examples that showed the maximum integer size in Python 2 and Python 3. 

With modern Python, you don't have to worry about reaching a maximum integer size. Just make sure you have enough memory to handle the computation of very large integer operations, and you're good to go. 

Happy coding!

