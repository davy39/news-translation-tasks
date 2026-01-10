---
title: Python List Sorting – How to Order Lists in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-26T16:31:59.000Z'
originalURL: https://freecodecamp.org/news/python-list-sorting-how-to-order-lists-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/sort-list-in-python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Dillion Megida\nThere are many reasons you might want to sort lists\
  \ in your Python applications. \nIn this article, I'll show you how to order lists\
  \ in ascending and descending order depending on what you need to do.\nWhat is a\
  \ List in Python?\nA list..."
---

By Dillion Megida

There are many reasons you might want to sort lists in your Python applications. 

In this article, I'll show you how to order lists in ascending and descending order depending on what you need to do.

## What is a `List` in Python?

A list is a data type in Python where you can store multiple values of different data types (including nested lists).

Here are examples of lists:

```python
numList = [1, 2, 3, 4, 5]

stringList = ["banana", "orange", "apple"]

mixedList = [1, "banana", "orange", [5, 6]]
```

You can access items in a list using their index position. Index positions start from 0 in lists:

```python
stringList = ["banana", "orange", "apple"]

print(stringList[1])
# "orange"
```

## How to Sort Lists in Python

You can sort a list in Python using the `sort()` method.

The `sort()` method allows you to order items in a list. Here's the syntax:

```python
list.sort(reverse=True|False, key=sortFunction)
```

The method accepts two optional arguments:
* `reverse`: which sorts the list in the reverse order (descending) if `True` or in the regular order (ascending) if `False` (which it is by default)
* `key`: a function you provide to describe the sorting method

By default, you can order strings and numbers in ascending order, without passing an argument to this method:

```python
items = ["orange", "cashew", "banana"]

items.sort()
# ['banana', 'cashew', 'orange']
```

In the above, you can see that the sorted list has **b** first (in banana), then **c** (in cashew), as this comes after b, and finally, **o** (in orange) which is later in the alphabetical order.

Note that this method modifies the original array.

For descending order, you can pass the reverse argument:

```python
items = [6, 8, 10, 5, 7, 2]

items.sort(reverse=True)
# [10, 8, 7, 6, 5, 2]
```

By passing `True` to the `reverse` argument, you see the numbers in the `items` list are sorted in reverse, which is descending order.

### How to specify a sort function

What if you tried this on a list of dictionaries? Let's see:

```python
items = [{
    'name': 'John',
    'age': 40
}, {
    'name': 'Mike',
    'age': 45
}, {
    'name': 'Jane',
    'age': 33
}, {
    'name': 'Asa',
    'age': 42
}]

items.sort()
```

You'll get an error because dictionaries are not orderable. This is where you can specify a sorting criteria using the `key` argument:

```python
items = [
  {
  'name': 'John',
  'age': 40
  },
  {   
    'name': 'Mike',
    'age': 45
  },
  {   
    'name': 'Jane',
    'age': 33
  },
  {   
    'name': 'Asa',
    'age': 42
  }
]

def sortFn(dict):
  return dict['age']

items.sort(key=sortFn)
# [
#   {'name': 'Jane', 'age': 33},
#   {'name': 'John', 'age': 40},
#   {'name': 'Asa', 'age': 42},
#   {'name': 'Mike', 'age': 45}
# ]
```

As you will notice in the code block above, using a sort function, we have specified that the sorting decision should be based on the `age` key in each dictionary.

If the `reverse` argument is passed as `True` here, the sorted dictionaries will be in descending order.

Here's another example using a sort function:

```python
items = ["cow", "elephant", "duck"]

def sortFn(value):
    return len(value)

items.sort(key=sortFn, reverse=True)
# ['elephant', 'duck', 'cow']
```

In this case, the sort function returns the length of the values in the list as a criterion for the sorting process. By passing `reverse` of `True`, you can see that the sorted list has the longer string first, followed by the shorter one.

## Wrapping Up

When building applications, there are many scenarios for sorting lists. It could be sorting a list of files based on a `last_opened` key. It could be sorting products based on a `price` key. As you can see there are numerous criteria you can use in real-world applications.

In this article, we've seen how to sort lists in Python in ascending and descending order using different methods.



