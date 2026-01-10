---
title: Python Length of List – How to Find the Size of a List
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-31T16:56:55.000Z'
originalURL: https://freecodecamp.org/news/python-length-of-list-how-to-find-the-size-of-a-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/18.-length-of-list.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  A list is a data structure in Python that contains multiple elements in a particular
  order. And sometimes you might need to get the size of a list. I''ll show you how
  to do that in this article.

  How to Create a List in Python

  You can...'
---

By Dillion Megida

A list is a data structure in Python that contains multiple elements in a particular order. And sometimes you might need to get the size of a list. I'll show you how to do that in this article.

## How to Create a List in Python

You can create lists in Python with square brackets. In the square brackets, you specify the different elements (or values) separated by commas.

You can store strings, numbers, lists, and so on in a list:

```python
items = ["python", True, [50, 30], 80]

print(items)
# ['python', True, [50, 30], 80]

print(items[2][0])
# 30
```

Here, we also have a nested list.

So how do we get the length of a list? For a list with just a few items, it's easy to count the items manually. But a longer list may not be that easy. 

Well, you can do this easily in Python. I'll show you two ways: a long way, and a shorter way.

I have a [short video on this topic](https://youtu.be/Ao9P6zTGMgQ) you can also check out.

## How to Get the Size of a List Using a `for loop` in Python

You can get the size of a list by looping through the list and keeping track of the size using a variable. Here's what I mean:

```python
languages = ["python", "javascript", "ruby", "java", "go"]

# initialize size variable
size = 0

for value in languages:
  # increment variable in every loop
  size = size + 1

print(size)
# 5
```

In this example, we have an array of five values. First, we initialize a `size` variable to 0. Then we have the for loop statement, where we loop through each value in the array. In each loop, we increment the `size` variable by 1. In the end, the `size` variable will hold the size of the list.

Let's look at the short way next.

## How to Get the Size of a List Using the `len` Function in Python

The `len` function returns the number of values in an iterable in Python. It's a simple and efficient function for this purpose. An iterable can be a list or a dictionary.

Let's see an example for getting the length of a list:

```python
languages = ["python", "javascript", "ruby", "java", "go"]

length = len(languages)

print(length)
# 5
```

By passing the `languages` list as an argument to `len`, the function returns the number of values in it, which is 5.

The `len` isn't only for lists as I mentioned earlier. You can also use it on dictionaries and strings:

```python
dict = {
  "name": "Dillion",
  "age": 70,
  "language": "python"
}

print(len(dict))
# 3

sentence = "I am Dillion"

print(len(dict))
# 12
```

For the `dict` dictionary, `len` returns the number of properties. For the `sentence` string, `len` returns the number of characters.

## Wrapping Up

In this article, we've seen how to get the size of a list using a long approach – the `for loop` statement – and a shorter and more efficient approach – the `len` function.

If you enjoyed this, please share it. :)


