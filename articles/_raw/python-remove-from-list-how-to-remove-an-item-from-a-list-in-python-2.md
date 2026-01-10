---
title: Python Remove from List – How to Remove an Item from a List in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-23T18:27:48.000Z'
originalURL: https://freecodecamp.org/news/python-remove-from-list-how-to-remove-an-item-from-a-list-in-python-2
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Remove-from-List---How-to-Remove-an-Item-from-a-List-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nA list in Python is a collection of items that are ordered\
  \ and changeable. It is one of the most versatile and frequently used data structures\
  \ in Python. \nA list can contain any type of data, such as integers, strings, floats,\
  \ and e..."
---

By Shittu Olumide

A list in Python is a collection of items that are ordered and changeable. It is one of the most versatile and frequently used data structures in Python. 

A list can contain any type of data, such as integers, strings, floats, and even other lists.

In Python, lists are created by enclosing a comma-separated sequence of values in square brackets `[]`. 

For example:

```py
numbers = [1,2,3,4,5]

```

Lists are dynamic data structures, meaning they can be modified by adding, removing, or changing their elements. The index of the first element in a list is `0`, and the index of the last element is `n-1`, where n is the number of elements in the list.

You can access and manipulate lists using a variety of built-in functions and methods in Python. Some of the most commonly used functions and methods for working with lists include `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, and `len()`.

**Real-life use case**: One real-life use case of removing an item from a list in Python is in e-commerce applications. 

For example, consider an online store that maintains a list of items in a shopping cart. When a customer wants to remove an item from their cart, the `remove()` or `pop()` method can be used to delete the item from the list. This ensures that the customer's shopping cart is updated with the correct items and quantities, and provides a seamless and user-friendly experience for the customer.

In this article, we will talk about three different ways to remove an item from a list. There are several ways to remove an item from a list in Python, depending on the specific use case and requirements. 

## Method 1: How to Remove from a List Using the `remove()` Method 

The `remove()` method is used to remove the first occurrence of a specified element from a list. It takes the element to be removed as its argument and modifies the original list. For example:

```py
# Create a list of colors
colors = ["red", "green", "blue", "yellow"]

# Remove the color "green"
colors.remove("green")

# Print the updated list
print(colors)

```

Output:

```bash
["red", "blue", "yellow"]

```

## Method 2: How to Remove from a List Using the `del` Statement 

The `del` statement is a general-purpose statement in Python that you can use to delete an object or element from a list. It takes the index of the element to be deleted as its argument and modifies the original list. For example:

```py
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Delete the number at index 3
del numbers[3]

# Print the updated list
print(numbers)

```

Output:

```bash
[1, 2, 3, 5]

```

## Method 3: How to Remove from a List Using the `pop()` Method 

The `pop()` method is used to remove and return the element at a specified index from a list. It takes the index of the element to be removed as its argument and modifies the original list. If no index is specified, it removes and returns the last element in the list. For example:

```py
# Create a list of fruits
fruits = ["apple", "banana", "orange", "mango"]

# Remove the fruit at index 2
removed_fruit = fruits.pop(2)

# Print the updated list and the removed fruit
print(fruits)       
print(removed_fruit)

```

Output:

```bash
["apple", "banana", "mango"]
"orange"

```

## Conclusion

In conclusion, removing an item from a list is a common operation in Python, and there are several methods available to achieve this task. We discussed three commonly used methods: remove(), del statement, and pop() method, along with code examples and comments.

Each of these methods has its own advantages and use cases. The `remove()` method is useful when the value of the item to be removed is known, while the `del` statement is useful when the index of the item to be removed is known. The `pop()` method can be used to remove an item at a specific index and return its value.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

