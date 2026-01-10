---
title: List Flatten in Python – Flattening Nested Lists
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-20T17:02:03.000Z'
originalURL: https://freecodecamp.org/news/list-flatten-in-python-flattening-nested-lists
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/flattenList.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Lists are one of the core data structures of Python. Due to their flexibility,
  there are a lot of things you can do with lists. And one of those things is turning
  a list of lists into a single list.

  It is also possible to turn a list of dictionaries,...'
---

Lists are one of the core data structures of Python. Due to their flexibility, there are a lot of things you can do with lists. And one of those things is turning a list of lists into a single list.

It is also possible to turn a list of dictionaries, a list of tuples, or a list of both tuples and dictionaries into a single list. We’ll learn a few ways to do these things in this article.


## What We’ll Cover
- [How to Flatten a List with the `sum()` Function ](#heading-how-to-flatten-a-list-with-the-sum-function)
- [How to Flatten a List with a Nested `for` Loop](#heading-how-to-flatten-a-list-with-a-nested-for-loop)
- [How to Flatten a List with List Comprehension](#heading-how-to-flatten-a-list-with-list-comprehension)
- [How to Flatten a List with Numpy](#heading-how-to-flatten-a-list-with-numpy)
- [How to Flatten a List with the `more_itertools` Package](#heading-how-to-flatten-a-list-with-the-moreitertools-package)
- [Wrapping Up](#heading-wrapping-up)


## How to Flatten a List with the `sum()` Function 
You typically use the `sum()` function to do what its name implies – add numbers together. But you can also use it to flatten out a list of lists into a single list.

The `sum()` function takes an iterable of numbers you want to add together and an optional starting point:

```py
sum(iterable, starting_point)
```

If you specify the list of lists you want to flatten as the iterable and an empty list as the starting point, the list will be flattened out. Here’s how to do it: 

```py
first_list_of_lists = [[12, 45, 2], [3, 7, 3, 1], [23, 89, 10, 9]]
flattened_first_list_of_lists = sum(first_list_of_lists, [])

print(flattened_first_list_of_lists) # [12, 45, 2, 3, 7, 3, 1, 23, 89, 10, 9]
```

You can see the list got flattened out. 

But this method won’t work for a list of tuples, a list of dictionaries, or a list of tuples and dictionaries because you cannot concatenate those. 

Using the `sum()` function will also not work for a 2-dimensional list containing strings or a 3-dimensional list. You will see how to flatten a list in those circumstances as you read on.


## How to Flatten a List with a Nested `for` Loop
A nested `for` loop is a `for` loop inside another `for` loop. This is how you can flatten out a list of lists for loop:

```py
list_of_lists = [[12, 45, 2], [3, 7, 3, 1], [23, 89, 10, 9]]

flattened_list_of_lists = []
for sublist in list_of_lists:
    for num in sublist:
        flattened_list_of_lists.append(num)
        
print(flattened_list_of_lists) # [12, 45, 2, 3, 7, 3, 1, 23, 89, 10, 9]
```

The code above loops through each dimension of the array and appends them into an empty list I called `flattened_list_of_lists` with the append() method.

This method would also be ideal for flattening a nested list of strings:

```py
list_of_names = [["Olsen", "Joy"], ["Di Marco", "Ascensio"], ["Modric", "Ann"]]

flattened_list_of_names = []
for sub_list in list_of_names:
    for name in sub_list:
        flattened_list_of_names.append(name)

print(flattened_list_of_names)
```

Using a nested loop would also let you flatten a list of tuples, a list of dictionaries, or a list of lists, tuples, and dictionaries combined.

Flattening a list of tuples:

```py
list_of_tuples = [1, 2, 3, (4, 5), (2, 4, 24)]

flattened_list_of_tuples = []
for sub_list in list_of_lists:
    for num in sub_list:
        flattened_list_of_tuples.append(num)

print(flattened_list_of_tuples) # [12, 45, 2, 3, 7, 3, 1, 23, 89, 10, 9]
```

Flattening a list of dictionaries:

```py
list_of_dicts = [ {1,  2, 3}, { "d": 4, "e": 5, "f": 6}]

flattened_list_of_dicts = []
for sub_list in list_of_dicts:
    for num in sub_list:
        flattened_list_of_dicts.append(num)

print(flattened_list_of_dicts) # [1, 2, 3, 'd', 'e', 'f']
```

Flattening a list containing list, tuple, and dictionary:

```py
multi_data_list = [[1, 2, 3], (4, 5, 6), {7, 8, 9}, {"a": 1, "b": 2, "c": 3, "z": 0}]

flattened_multi_data_lists = []
for sub_list in multi_data_list:
    for data in sub_list:
        flattened_multi_data_lists.append(data)

print(flattened_multi_data_lists)
```


## How to Flatten a List with List Comprehension
List comprehension helps you create a list from a string or another list. So, it’s possible to create a new list from a list of lists. Here’s how the syntax for list comprehension looks:

```py
[expression for element in iterable_data if condition == True]
```

Remember that you can iterate through strings, so you can create a list from a string this way:

```py
my_str = "freeCodeCamp"
list_from_letters = [letter for sub_list in my_str for letter in sub_list]

print(list_from_letters) # ['f', 'r', 'e', 'e', 'C', 'o', 'd', 'e', 'C', 'a', 'm', 'p']
```

You can also create a list from a list of lists this way – flattening the list in the process:

```py
list_of_names = [["Olsen", "Joy"], ["Di Marco", "Ascensio"], ["Modric", "Ann"]]
flattened_names = [name for sub_list in list_of_names for name in sub_list]

print(flattened_names) # ['Olsen', 'Joy', 'Di Marco', 'Ascensio', 'Modric', 'Ann']
```


## How to Flatten a List with Numpy
You can use the `concatenate()` function of the `numpy` library to flatten a list this way:

```py
import numpy as np

first_list_of_lists = [[1, 2], [4, 5]]
second_list_of_lists = [[6, 7], [8, 9]]

flattened_first_list_of_lists = np.concatenate(first_list_of_lists) 
flattened_second_list_of_lists = np.concatenate(second_list_of_lists) 

print(flattened_first_list_of_lists) # [1 2 4 5]
print(flattened_second_list_of_lists) # [6 7 8 9]
```


## How to Flatten a List with the `more_itertools` Package
The `more_itertools` package is a set of utilities that provides functions and methods for looping through any iterable data in Python. You can install it by running `pip install more_itertools` or `pip3 install more_itertools`.

`more_itertools` has a flatten() function for flattening a list:

```py
from more_itertools import flatten

list_of_lists = [[2, 4, 5], [3, 9, 5, 2], [2, 4, 1, 2 ]]
flattened_list = list(flatten(list_of_lists)) 

print(flattened_list) # [2, 4, 5, 3, 9, 5, 2, 2, 4, 1, 2]
```

If you also have a list that has deeply nested lists, `more_itertools` provides a `collapse()` function you can use to break all of them into one single list:

```py
from more_itertools import collapse

list_of_lists_2 = [[1, 2], [[3, 4]], [5, [6, 7]]]
flattened_list_of_lists_2 = list(collapse(list_of_lists_2))

print(flattened_list_of_lists_2) # [1, 2, 3, 4, 5, 6, 7]
```


## Wrapping Up
Flattening a list is not an uphill task with the availability of the `sum()` function, list comprehension, and libraries like `Numpy` and `more_itertools`. 

Even if you don’t want to do it in the “Pythonic way”, you can use a nested `for` loop as you saw here.

And if you have a list with deeply nested lists or lists, the `collapse()` function of `more_itertools` can help you flatten them out.

If you enjoyed reading this article, don’t hesitate to share it with your friends and family.


