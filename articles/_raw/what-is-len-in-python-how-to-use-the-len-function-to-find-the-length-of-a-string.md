---
title: What is len() in Python? How to Use the len() Function to Find the Length of
  a String
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-24T18:35:06.000Z'
originalURL: https://freecodecamp.org/news/what-is-len-in-python-how-to-use-the-len-function-to-find-the-length-of-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/leninpython.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In programming languages, getting the length of a particular data type\
  \ is a common practice. \nPython is no different because you can use the built-in\
  \ len() function to get the length of a string, tuple, list, dictionary, or any\
  \ other data type.\nIn th..."
---

In programming languages, getting the length of a particular data type is a common practice. 

Python is no different because you can use the built-in `len()` function to get the length of a string, tuple, list, dictionary, or any other data type.

In this article, I'm going to show you how to get the length of a string with the `len()` function.

## Basic Syntax for `len()` in Python

To use the `len()` function to get the length of a data type, assign the data type to a variable, then pass the variable name to the `len()` function.

Like this:
```py
len(variableName)
```
## How to Find the Length of a String with the `len()` Function

When you use the `len()` function to get the length of a string, it returns the number of characters in the string – including the spaces.

Here are 3 examples to show you how it works:

```py
name = "freeCodeCamp"
print(len(name))

# Output: 12
```

This means there are 12 characters in the string.

```py
founder = "Quincy Larson"
print(len(founder))

# Output: 13
```

This means there are 13 characters in the string.

```py
description = "freeCodeCamp is a platform for learning how to code for free"
print(len(description))

# Output: 60
```

This means there are 60 characters in the string.

## How `len()` Works with Other Data Types in Python

You might be wondering how the `len()` function works on other data types such as lists and tuples.

When you use the `len()` function on a data type like tuple or list, it returns the number of items in the tuple or list, not the number of characters.

For example, 3 gets returned for the length of the tuple below, not the number of characters of the words in it.

```py
langs = ("Python", "JavaScript", "Golang")
print(len(langs))

# Output: 3
```

So it just depends on the data type you're working with.


## Conclusion

In this article, you learned how to get the length of a string – the number of characters.

Thank you for reading.


