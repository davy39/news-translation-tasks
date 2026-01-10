---
title: List to String Python – join() Syntax Example
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-07T23:24:00.000Z'
originalURL: https://freecodecamp.org/news/python-list-to-string-join-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/david-clode-5uU8HSpfwkI-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Sometimes you want to convert your Python lists into strings. This tutorial
  will show you an example of how you can do this.

  But first, let''s explore the difference between the Python list data structure
  and the Python string data structure.

  What is ...'
---

Sometimes you want to convert your Python lists into strings. This tutorial will show you an example of how you can do this.

But first, let's explore the difference between the Python list data structure and the Python string data structure.

## What is a List in Python?

In Python, a list is an ordered sequence of elements. Each element in a list has a corresponding index number that you can use to access it.

You can create a lists by using square brackets and can contain any mix of data types.

```py
>>> exampleList = ['car', 'house', 'computer']
```

Note that I will be showing code from the Python REPL. The input I'm typing has `>>>` at the beginning of it. The output doesn't have anything at the beginning of it. You can launch this REPL by going into your terminal and typing `python` then hitting enter.

Once you've initialized a Python list, you can access its elements using bracket notation. Keep in mind that the index starts at zero rather than 1. Here's an example of inputs and outputs:

```py
>>> exampleList[0]
'car'

>>> exampleList[1] 
'house'

>>> exampleList[2] 
'computer'
```

## What is a String in Python?

A string is just a sequence of one or more characters. For example, `'car'` is a string.

You can initialize it like this:

```py
>>> exampleString = 'car'
```

And then you can call your string data structure to see its contents:

```py
>>> exampleString
'car'

```

## How to Convert a Python List into a Comma-Separated String?

You can use the .join string method to convert a list into a string.

```py
>>> exampleCombinedString = ','.join(exampleList)
```

You can then access the new string data structure to see its contents:

```py
>>> exampleCombinedString
'car,house,computer'
```

So again, the syntax is `[seperator].join([list you want to convert into a string])`.

In this case, I used a comma as my separator, but you could use any character you want.

Here. Let's join this again, but this time, let's add a space after the comma so the resulting string will be a bit easier to read:

```py
>>> exampleCombinedString = ', '.join(exampleList)
>>> exampleCombinedString
'car, house, computer'

```

There you go.

## How do you concatenate lists in Python?

There are a number of ways to concatenate lists in Python. The most common is to use the `+` operator:

```py
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> list1 + list2
[1, 2, 3, 4, 5, 6]
```

Another option is to use the `extend()` method:

```py
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6]
```

Finally, you can use the `list()` constructor:

```py
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> list3 = list1 + list2
>>> list3
[1, 2, 3, 4, 5, 6]
```

## How do you convert a list to an array in Python?

One way to do this is to use the NumPy library.

First import NumPy:

```py
import numpy as np
```

Then run the np.array() method to convert a list to an array:

```py
>>> a = np.array([1, 2, 3])
>>> print(a)
[1 2 3]
```

## Can we convert a list into a dictionary in Python?

Most definitely. First, let's create a dictionary using the built-in `dict()` function. Example  `dict()` syntax:

```py
d = dict(name='John', age=27, country='USA') 
print(d)
```

Which will output:

```py
{'age': 27, 'country': 'USA', 'name': 'John'}
```

In this example, we create a dictionary object by using the `dict()` function. The `dict()` function accepts an iterable object. In this case, we use a tuple.

### How to Create a Dictionary from a List

You can also create a dictionary from a list using the `dict()` function.

```py
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d)

```

Which will output:

```py
{'a': 1, 'b': 2, 'c': 3}

```

Note that in this example, we used the `zip()` function to create a tuple.

### How to Create a Dictionary from Another Dictionary:

You can create a dictionary from another dictionary. You can use the dict() function or the constructor method to do this.

```py
d = dict(a=1, b=2, c=3) print(d)

```

Which will output:

```py
{'a': 1, 'b': 2, 'c'}

```

## There are so many awesome things you can do with Python Lists, Arrays, Dictionaries, and Strings

I am really just scratching the surface here. If you want to go way deeper, and apply a lot of these methods and techniques on real world projects, freeCodeCamp.org can help you. 

If you want to learn more about programming and technology, try [freeCodeCamp's core coding curriculum](https://www.freecodecamp.org/learn). It's free.

