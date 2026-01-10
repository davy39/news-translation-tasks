---
title: Python List.append() – How to Append to a List in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-13T15:10:46.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-how-to-append-to-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/append-to-a-list.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  How do you append (or add) new values to an already created list in Python? I will
  show you how in this article.

  But first things first...

  What is a List in Python?

  A List is a data type that allows you to store multiple values of e...'
---

By Dillion Megida

How do you append (or add) new values to an already created list in Python? I will show you how in this article.

But first things first...

## What is a `List` in Python?

A `List` is a data type that allows you to store multiple values of either the same or different types in one variable.

Take a look at the example below:

```python
age = 50
name = "Python"
isRunning = False
```

In this code, `age`, `name` and `isRunning` only hold one value each, of the `number`, `string`, and `boolean` data types, respectively. 

Let's say you wanted to store all the things you bought in the market using this approach:

```python
item1 = "banana"
item2 = "apple"
item3 = "orange"
```

Creating three separate variables for related items may not be the best approach.

With lists, you can create a variable that holds multiple values. Here's how:

```python
numbers = [1, 2, 3]

strings = ["list", "dillion", "python"]

mixed = [10, "python", False, [40, "yellow"]]
```

The `numbers` variable is a list containing three number values.

The `strings` variable is a list containing three string values.

The `mixed` variable is a list containing a number, a string, a boolean, and even another list.

So for the items you bought at the market, you can store them like this:

```python
items = ["banana", "apple", "orange"]
```

And you can access each item using its index position in the list, starting from 0 (as lists are zero-indexed in Python):

```python
print(items[0], items[1], items[2])
# banana apple orange
```

## How to Append Data to a List in Python

We've briefly seen what lists are. So how do you update a list with new values? Using the `List.append()` method. 

The `append` method receives one argument, which is the value you want to append to the end of the list. 

Here's how to use this method:

```python
mixed = [10, "python", False]

mixed.append(40)

print(mixed)
# [10, 'python', False, 40]
```

Using the `append` method, you have added `40` to the end of the `mixed` list.

You can add any data type you want, including other lists:

```python
mixed = [10, "python", False]

mixed.append([True, "hello"])

print(mixed)

# [10, 'python', False, [True, 'hello']]
```

## Wrapping up

Lists are useful for creating variables that hold multiple values (especially when these values are related)

Lists have many methods in Python that you can use to modify, extend, or reduce the lists. In this article, we've looked at the `append` method which adds data to the end of the list.


