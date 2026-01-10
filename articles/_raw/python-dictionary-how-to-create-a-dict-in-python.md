---
title: Python Dictionary – How to Create a Dict in Python (Hashmap)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-01T15:44:00.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-how-to-create-a-dict-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Shittu-Olumide-Python-Dictionary---How-to-Create-a-Dict-in-Python--Hashmap--1.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  Welcome to this Python article on how to create a dictionary.

  A dictionary (also called a hashmap in other languages) is an unordered grouping
  of key-value pairs in Python. Since each value can be accessed by its corresponding
  key, ...'
---

By Shittu Olumide

Welcome to this Python article on how to create a dictionary.

A dictionary (also called a hashmap in other languages) is an unordered grouping of key-value pairs in Python. Since each value can be accessed by its corresponding key, it offers a practical means of storing and retrieving data.

We'll cover the fundamentals of creating a dictionary in Python in this tutorial, including how to initialize an empty dictionary, how to add and remove key-value pairs, and how to access and work with dictionary data. 

I'll illustrate each concept with examples, and demonstrate each operation with code snippets.

By the time you finish reading this article, you ought to know everything you need to use dictionaries in Python, from creating them to modifying them. And and you should be able to use this information to solve issues and construct more sophisticated programs. 

Let's begin!

## How to Create a Dict in Python

A dictionary is a type of data structure that allows us to store key-value pairs. It is also known as a hashmap in other programming languages. 

Dictionaries are useful when we want to store data in a way that is easily accessible and modifiable. To create dictionaries in Python, we use curly braces, the `dict()` constructor, and the `fromkeys()` method.

### How to create a dict using curly braces

Curly braces `{ }` are one method of creating a dictionary in Python. We can enclose a comma-separated list of key-value pairs in curly braces to make a dictionary. We use a colon and a comma to separate each pair of key-value pairs from the others.

Here's an example:

```py
MyDict = {1: "apple", 2: "banana", 3: "orange"}

```

In this example, we've created a dictionary `MyDict` with three key-value pairs:   
`1: "apple"`, `2: "banana"`, and `3: "orange"`. The keys are integers and the values are strings.

### How to create a dict using the `dict()` constructor

Another method for making a dictionary in Python is using the `dict()` constructor. The constructor `dict()` produces a dictionary from an iterable of key-value pairs as input. Both a list of tuples and arguments can be used to pass in the key-value pairs. As an illustration, consider the following.

Let's create a dictionary from a tuple.

```py
# create a dictionary from a tuple using dict() constructor
MyDict = dict(one=1, two=2, three=3)
print(MyDict)

```

Output:

```py
{'one': 1, 'two': 2, 'three': 3}

```

Let's create a dictionary from a list of tuples.

```py
# create a dictionary from a list of tuples using dict() constructor
MyList = [('one', 1), ('two', 2), ('three', 3)]
MyDict = dict(MyDict)
print(MyDict)

```

Output:

```py
{'one': 1, 'two': 2, 'three': 3}

```

In the first example, we created a dictionary with key-value pairs `one:1`, `two:2`, and `three:3` by passing them as arguments to the `dict()` constructor. 

In the second example, we created a dictionary using a list of tuples `MyList`, which contains the same key-value pairs as before. We passed `MyList` as an argument to the `dict()` constructor, which returns a dictionary with the same key-value pairs.

The `dict()` constructor can also be used to create an empty dictionary by not passing any arguments. For example, `MyDict = dict()` creates an empty dictionary `MyDict`.

### How to create a dict using the `fromkeys()` method

You can also use the built-in `fromkeys()` method to create a dictionary by selecting keys from a sequence and setting values to default values.

The first argument to the `fromkeys()` method is a list of keys, and the second (optional) argument is the value that will be assigned to each key after it has been set. The values will automatically be set to None if the second argument is not provided.

Example

```py
keys = ['a', 'b', 'c']
values = 0  # set default value to 0

MyDict = dict.fromkeys(keys, values)
print(MyDict)

```

Output:

```py
{'a': 0, 'b': 0, 'c': 0}

```

In the example above, we passed a list of keys `['a', 'b', 'c']` and a default value `0` to the `fromkeys()` method. We get a new dictionary where all keys are set the value of `0`.

## Conclusion 

In this tutorial, we learned how to create a dict in Python by focusing on three ways: using curly braces, the `dict()` constructor, and the `fromkeys()` method. With this knowledge, you can confidently create and manipulate dictionaries in your Python code.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

