---
title: Python For Loop - For i in Range Example
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T21:31:06.000Z'
originalURL: https://freecodecamp.org/news/python-for-loop-for-i-in-range-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/606365729618b008528a99ae.jpg
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Jeremy L Thompson

  Loops are one of the main control structures in any programming language, and Python
  is no different.

  In this article, we will look at a couple of examples using for loops with Python''s
  range() function.

  Here''s an Interactive Scr...'
---

By Jeremy L Thompson

Loops are one of the main control structures in any programming language, and Python is no different.

In this article, we will look at a couple of examples using `for` loops with Python's `range()` function.

### Here's an Interactive Scrim of a Python For Loop

<iframe src="https://scrimba.com/scrim/co4e24d97b6f708862420051b?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## For Loops in Python

`for` loops repeat a portion of code for a set of values. 

As discussed in [Python's documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements), `for` loops work slightly differently than they do in languages such as JavaScript or C. 

A `for` loop sets the iterator variable to each value in a provided list, array, or string and repeats the code in the body of the `for` loop for each value of the iterator variable.

In the example below, we use a `for` loop to print every number in our array.

```python
# Example for loop
for i in [1, 2, 3, 4]:
    print(i, end=", ") # prints: 1, 2, 3, 4,
```

We can include more complex logic in the body of a `for` loop as well. In this example we print the result of a small computation based on the value of our iterator variable.

```python
# More complex example
for i in [1, 3, 5, 7, 9]:
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # prints 1, 1, 1, 1, 1, 
```

When the values in the array for our `for` loop are sequential, we can use Python's `range()` function instead of writing out the contents of our array.

## The Range function in Python

The `range()` function provides a sequence of integers based upon the function's arguments. Additional information can be found in [Python's documentation](https://docs.python.org/3/library/stdtypes.html#range) for the `range()` function.

```python
range(stop)
range(start, stop[, step])

```

The `start` argument is the first value in the range. If `range()` is called with only one argument, then Python assumes `start = 0`.

The `stop` argument is the upper bound of the range. It is important to realize that this upper value is not included in the range.

In the example below, we have a range starting at the default value of `0` and including integers less than `5`.

```python
# Example with one argument
for i in range(5):
    print(i, end=", ") # prints: 0, 1, 2, 3, 4, 
```

In our next example, we set `start = -1` and again include integers less than `5`.

```python
# Example with two arguments
for i in range(-1, 5):
    print(i, end=", ") # prints: -1, 0, 1, 2, 3, 4, 
```

The optional `step` value controls the increment between the values in the range. By default, `step = 1`.

In our final example, we use the range of integers from `-1` to `5` and set `step = 2`.

```python
# Example with three arguments
for i in range(-1, 5, 2):
    print(i, end=", ") # prints: -1, 1, 3, 
```

## Summary

In this article, we looked at `for` loops in Python and the `range()` function.

`for` loops repeat a block of code for all of the values in a list, array, string, or `range()`.

We can use a `range()` to simplify writing a `for` loop. The `stop` value of the `range()` must be specified, but we can also modify the `start`ing value and the `step` between integers in the `range()`.

