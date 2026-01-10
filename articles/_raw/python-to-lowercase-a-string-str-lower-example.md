---
title: Python to Lowercase a String – str.lower() Example
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-26T20:12:09.000Z'
originalURL: https://freecodecamp.org/news/python-to-lowercase-a-string-str-lower-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/string-lowercase.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  Strings can be in different formats such as lowercase, capitalized, and uppercase.
  In this article, I''ll show you how to convert a string to lowercase in Python.

  A lowercase string has all its characters in small letters. An example...'
---

By Dillion Megida

Strings can be in different formats such as lowercase, capitalized, and uppercase. In this article, I'll show you how to convert a string to lowercase in Python.

A lowercase string has all its characters in small letters. An example is **python**.

A capitalized string has the first letter of each word capitalized, and the remaining letters are in small letters. An example is **Python**.

An uppercase string has all its characters in capital letters. **PYTHON** is an example.

Python has numerous string methods for modifying strings in different ways. To convert a string to lowercase, you can use the `lower` method.

The lower method of strings returns a new string from the old one with all characters in lowercase. Numbers, symbols, are all other non-alphabetical characters remain the same.

## str.lower() Examples in Python

Here's how to use the `lower` method in Python:

```python
text = "HellO woRLd!"

lower = text.lower()

print(lower)
# hello world!
```

A good use case of the `lower` method is for comparing strings to evaluate their equality regardless of the case. 

In Python, "Hello World" is not equal to "hello world" because equality is case-sensitive as you can see in the code below:

```python
text1 = "Hello World"
text2 = "hello world"

print(text1 == text2)
# False
```

`text1` has an upper "H" and "W" whereas `text2` has a lower "h" and "w". Because the cases of these characters are different, `text1` is not equal to `text2` even though they have the same characters.

To compare both strings while ignoring their case, you can use the lower method like this:

```python
text1 = "HeLLo worLD"
text2 = "HellO WORLd"

print(text1 == text2)
# False

print(text1.lower() == text2.lower())
# True
```

By converting both strings to lowercase, you can correctly check if they have the same characters.

## How to Use `upper` in Python

The opposite of lowercase is uppercase, and Python also has a method for that as well. As you may have guessed, the `upper` method in Python returns a new string where all the characters are in uppercase. 

You can use it similarly to the `lower` method like this:


```python
text = "hello World!"

upper = text.upper()

print(upper)
// HELLO WORLD!
```

You can also use this method to check that two strings have the same set of characters. But in most applications today, developers use the lowercase comparison approach.

That's it! Now you know how to convert a string to all lowercase or uppercase letters in Python.


