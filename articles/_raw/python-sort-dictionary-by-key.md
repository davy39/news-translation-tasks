---
title: Python Sort Dictionary by Key – How to Sort a Dict with Keys
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-25T23:57:54.000Z'
originalURL: https://freecodecamp.org/news/python-sort-dictionary-by-key
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-Python-Sort-Dictionary-by-Key---How-to-Sort-a-Dict-with-Keys.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  Sorting is a fundamental operation in computer programming that involves arranging
  elements in a specific order.

  Whether you''re working with numbers, strings, or complex data structures, sorting
  plays a crucial role in organizing an...'
---

By Shittu Olumide

Sorting is a fundamental operation in computer programming that involves arranging elements in a specific order.

Whether you're working with numbers, strings, or complex data structures, sorting plays a crucial role in organizing and manipulating data efficiently.

From small arrays to large datasets, sorting algorithms allow programmers to solve a wide range of problems, from searching for specific values to optimizing data access and analysis.

In this article, we will explore how to sort a dictionary with keys in Python. We will break down the steps for easy follow up and understanding. I recommend that you be familiar with the Python programming language to get the most out of this article.

## What is a Python Dictionary?

In Python, dictionaries are a powerful data structure used to store key-value pairs. They provide a convenient way to organize and retrieve data based on unique keys. But there may be situations where you need to sort a dictionary by its keys in a specific order.

A key in Python refers to the unique identifier associated with a specific value. It serves as a way to access and retrieve values from the dictionary based on their corresponding keys. Keys in a dictionary can be of any immutable data type, such as strings, numbers (integers or floats), or tuples. The key must be unique within the dictionary, meaning that no two keys can have the same value.

## Ways to Sort a Dict by Keys in Python

### Method 1: Using the `sorted()` Function

The simplest way to sort a dictionary by its keys is by using the `sorted()` function along with the `items()` method of the dictionary. 

The `items()` method returns a list of key-value pairs as tuples. By passing this list to the `sorted()` function, we can sort the tuples based on their first element (the keys). 

Example:

```py
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict(sorted(my_dict.items()))

print(sorted_dict)

```

Output:

```bash
{'a': 1, 'b': 2, 'c': 3}

```

In this example, the `sorted()` function takes the `my_dict.items()` list and returns a new sorted list of tuples. We use the `dict()` constructor to convert the sorted list back into a dictionary.

### Method 2: Using a List of Tuples

If you prefer a more manual approach, you can convert the dictionary to a list of tuples, sort the list using any sorting technique available in Python, and then convert it back to a dictionary. 

Example:

```py
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_list = sorted(my_dict.items())

sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value

print(sorted_dict)

```

Output:

```bash
{'a': 1, 'b': 2, 'c': 3}

```

In this example, we used the `sorted()` function to sort the `my_dict.items()` list. Then, a new empty dictionary, `sorted_dict`, is created. The sorted list is iterated over, and each key-value pair is added to the `sorted_dict` using assignment.

### Method 3: Using the `collections.OrderedDict` Class

Another approach to sorting a dictionary by key is to use the `collections.OrderedDict` class from the Python standard library. 

This class is a dict subclass that remembers the order of its elements based on the insertion order. We can leverage this feature to achieve key-based sorting. 

Example:

```py
from collections import OrderedDict

my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = OrderedDict(sorted(my_dict.items()))

print(sorted_dict)

```

Output:

```bash
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

```

In this example, the `sorted()` function is used to sort the `my_dict.items()` list, and then the sorted list is passed to the `OrderedDict()` constructor to create a new dictionary with the sorted order.

## Conclusion 

In Python, you can sort a dictionary by its keys using various methods. In this article, we explored three approaches: using the `sorted()` function, utilizing the `collections.OrderedDict` class, and manually sorting a list of tuples. Each method provides a different level of control and flexibility.

By using the `sorted()` function, we can quickly sort a dictionary by key and obtain a new dictionary as the result. If preservation of the insertion order is crucial, the `collections.OrderedDict` class is a suitable choice.

For those who prefer a more manual approach, converting the dictionary to a list of tuples, sorting the list, and then creating a new dictionary can provide more customization options.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

