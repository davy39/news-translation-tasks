---
title: Python Split String – How to Split a String into a List or Array in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-04T20:24:05.000Z'
originalURL: https://freecodecamp.org/news/python-split-string-how-to-split-a-string-into-a-list-or-array-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Split-String---How-to-Split-a-String-into-a-List-or-Array-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nIn this article, we will walk through a comprehensive\
  \ guide on how to split a string in Python and convert it into a list or array.\
  \ \nWe'll start by introducing the string data type in Python and explaining its\
  \ properties. Then we'll..."
---

By Shittu Olumide

In this article, we will walk through a comprehensive guide on how to split a string in Python and convert it into a list or array. 

We'll start by introducing the string data type in Python and explaining its properties. Then we'll discuss the various ways in which you can split a string using built-in Python methods such as `split()`, `splitlines()`, and `partition()`.

Overall, this article should be a useful resource for anyone looking to split a string into a list in Python, from beginners to experienced programmers.

## What is a String in Python?

A string is a group of characters in Python that are encased in single quotes (`' '`) or double quotes (`" "`). This built-in Python data type is frequently used to represent textual data. 

Since strings are immutable, they cannot be changed once they have been created. Any action that seems to modify a string actually produces a new string.  
  
Concatenation, slicing, and formatting are just a few of the many operations that you can perform on strings in Python. You can also use strings with a number of built-in modules and functions, including `re`, `str()`, and `len()`. 

There's also a wide range of string operations, including `split()`, `replace()`, and `strip()`, that are available in Python. You can use them to manipulate strings in different ways.

```py
myString = "Hello world"

```

Let's now learn how to split a string into a list in Python.

## How to Split a String into a List Using the `split()` Method

The `split()` method is the most common way to split a string into a list in Python. This method splits a string into substrings based on a delimiter and returns a list of these substrings.

```py
myString = "Hello world"
myList = myString.split()

print(myList)

```

Output:

```bash
['Hello', 'world']

```

In this example, we split the string `"Hello world"` into a list of two elements, `"Hello"` and `"world"`, using the `split()` method.

## How to Split a String into a List Using the `splitlines()` Method

The `splitlines()` method is used to split a string into a list of lines, based on the newline character `(\n)`.

```py
myString = "hello\nworld"
myList = myString.splitlines()

print(myList)

```

Output:

```bash
['hello', 'world']

```

In this example, we split the string `"hello\nworld"` into a list of two elements, `"hello"` and `"world"`, using the `splitlines()` method.

## How to Split a String into a List Using Regular Expressions with the `re` Module

The `re` module in Python provides a powerful way to split strings based on regular expressions.

```py
import re

myString = "hello world"
myList = re.split('\s', myString)

print(myList)

```

Output:

```bash
['hello', 'world']

```

In this example, we split the string `"hello world"` into a list of two elements, `"hello"` and `"world"`, using a regular expression that matches any whitespace character `(\s)`.

## How to Split a String into a List Using the `partition()` Method

The `partition()` method splits a string into three parts based on a separator and returns a tuple containing these parts. The separator itself is also included in the tuple.

```py
myString = "hello:world"
myList = myString.partition(':')

print(myList)

```

Output:

```bash
('hello', ':', 'world')

```

In this example, we split the string `"hello:world"` into a tuple of three elements, `"hello"`, `":"`, and `"world"`, using the `partition()` method.

Note: The most common method for splitting a string into a list or array in Python is to use the `split()` method. This method is available for any string object in Python and splits the string into a list of substrings based on a specified delimiter.

## When to Use Each Method

So here's an overview of these methods and when to use each one for quick reference:

1. `split()`: This is the most common method for splitting a text into a list. You can use this method when you want to split the text into words or substrings based on a specific delimiter, such as a space, comma, or tab.
2. `partition()`: This method splits a text into three parts based on the first occurrence of a delimiter. You can use this method when you want to split the text into two parts and keep the delimiter. For example, you might use `partition()` to split a URL into its protocol, domain, and path components. The `partition()` method returns a tuple of three strings.
3. `splitlines()`: This method splits a text into a list of strings based on the newline characters (`\n`). You can use this method when you want to split a text into lines of text. For example, you might use `splitlines()` to split a multiline string into individual lines.
4. Regular expressions: This is a more powerful method for splitting text into a list, as it allows you to split the text based on more complex patterns. For example, you might use regular expressions to split a text into sentences, based on the presence of punctuation marks. The `re` module in Python provides a range of functions for working with regular expressions.

## Conclusion

These are some of the most common methods to split a string into a list or array in Python. Depending on your specific use case, one method may be more appropriate than the others.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

