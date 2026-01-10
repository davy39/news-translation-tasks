---
title: How to Convert a List to an Array and Back in Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-04-12T00:04:30.000Z'
originalURL: https://freecodecamp.org/news/convert-lists-to-arrays-and-back-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/dare.JPG
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: null
seo_desc: 'Arrays and lists are two of the most commonly used data structures in Python.

  You can use both arrays and lists to store collections of values, but they have
  some key differences.

  For example, arrays are more efficient than lists for certain operatio...'
---

Arrays and lists are two of the most commonly used data structures in Python.

You can use both arrays and lists to store collections of values, but they have some key differences.

For example, arrays are more efficient than lists for certain operations, such as mathematical operations on large collections of numerical data. But lists are more flexible and easier to work with in many cases.

Sometimes, you may need to convert between arrays and lists in Python. For example, you may have data stored in a list that you need to pass to a function that requires an array. Or you may have an array that you need to manipulate using list operations.

In this article, we will explore how to convert lists to arrays and arrays to lists in Python.

## How to Convert a List to an Array in Python

To convert a list to an array in Python, you can use the `array` module that comes with Python's standard library. The `array` module provides a way to create arrays of various types, such as signed integers, floating-point numbers, and even characters.

Here's an example of how to convert a list to an array in Python:

```python
import array

my_list = [1, 2, 3, 4, 5]
my_array = array.array('i', my_list)

print(my_array)
```

In this code, we first import the `array` module. We then create a list called `my_list` containing the values 1 through 5.

Next, we create an array called `my_array` by calling the `array()` function and passing it two arguments: the type code `'i'`, which specifies that we want an array of signed integers, and `my_list`, which is the list we want to convert.

When we print `my_array`, we should see the following output:

```python
array('i', [1, 2, 3, 4, 5])
```

This shows that `my_array` is now an array containing the same values as `my_list`.

## How to Convert an Array to a List in Python

To convert an array back to a list, we can use Python's built-in `list()` function. Here's an example of how to convert an array to a list in Python:

```python
import array

my_array = array.array('i', [1, 2, 3, 4, 5])
my_list = list(my_array)

print(my_list)
```

In this code, we first create an array called `my_array` containing the values 1 through 5. Next, we create a list called `my_list` by calling the `list()` function and passing it `my_array`.

When we print `my_list`, we should see the following output:

```python
[1, 2, 3, 4, 5]
```

This shows that `my_list` is now a list containing the same values as `my_array`.

## Conclusion

In this article, we explored how to convert arrays and lists in Python. You learned that you can use the `array` module to create arrays of various types and the `list()` function to convert arrays back to lists.

Converting between arrays and lists can be useful in many situations, such as when you need to pass data between functions or when you need to manipulate data using list operations. By understanding how to convert arrays and lists, you can work more effectively with data in Python.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
