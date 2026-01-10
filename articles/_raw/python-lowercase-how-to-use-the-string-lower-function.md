---
title: Python Lowercase – How to Use the String lower() Function
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-05-09T22:04:42.000Z'
originalURL: https://freecodecamp.org/news/python-lowercase-how-to-use-the-string-lower-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-christina-morillo-1181467--1-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Strings are a fundamental part of working with Python. And the lower()
  method is one of the many integrated methods that you can use to work with strings.

  In this article, we''ll see how to make strings lowercase with the lower() method
  in Python.

  Wha...'
---

Strings are a fundamental part of working with Python. And the `lower()` method is one of the many integrated methods that you can use to work with strings.

In this article, we'll see how to make strings lowercase with the `lower()` method in Python.

## What is a string?

A string is a data type that can contain many different characters. A string is written as a series of characters between single or double quotes.

```python
>>> example_string = 'I am a String!'
>>> example_string
'I am a String!'
```

## What is a method?

A method is a function that can be used on a specific data type. Methods can take or not take arguments.

Sometimes you may wonder if a method exists. In Python you can see the whole list of string methods by using the `dir()` function with a string as argument, like so:

```python
>>> dir(example_string)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

Of these many string methods, in this article you will learn about the `lower()` method and how it works.

## How does the `lower()` method work?

The `lower()` method is a string method that returns a new string, completely lowercase. If the original string has uppercase letters, in the new string these will be lowercase. Any lower case letter, or any character that is not a letter, is not affected.

```
>>> example_string.lower()
'i am a string!'

>>> 'FREECODECAMP'.lower()
'freecodecamp'
```

## What to keep in mind when using the lower method

The `lower()` method does a pretty straightforward thing: it creates a new string were all the uppercase letters are now lowercase. But there are a few things to keep in mind when using it. Let's take a look at them.

### Strings are immutable

Strings are an immutable data type, which means they can't be changed. The original string will stay unchanged after you use the `lower()` method.

In the examples above, the `lower()` method has acted on the `example_string` but never changed it. Checking the value of `example_string` still shows the original value.

```python
>>> example_string
'I am a String!'

>>> example_string.lower()
'i am a string!'

>>> example_string
'I am a String!'
```

### The `lower()` method returns a new string

The `lower()` returns a new string. You'll need to save it in a variable if you want to use it again in your code.

```python
>>> new_string = example_string.lower()

>>> new_string
'i am a string!'
```

### Strings are case sensitive

Strings are case sensitive, so a lowercase string is different than an uppercase string.

```python
>>> 'freecodecamp' == 'FREECODECAMP'
False
```

This is useful when thinking about what the `lower()` method could be useful for. In the example you will see how this feature makes the `lower()` method useful and necessary when building a script or program that deals with strings.

## `lower()` method example: how to check if the user input matches

Let's write a small script that asks the user a question and waits for input, and gives feedback about the user's answer.

```python
answer = input("What color is the sun? ")
if answer == "yellow":
  print("Correct!")
else:
  print("That is not the correct color!")
```

This script asks the user a question, "What color is the sun?", and waits for an answer. Then it checks if the answer is "yellow", and if it is it prints "Correct!" If it isn't, it prints "That is not the correct color!".

But there is an issue with this script.

Running this script, you will have this question asked in the terminal:

```shell
$ python sun_color.py
What color is the sun? 
```

If you answer "Yellow", it says:

```shell
$ python sun_color.py
What color is the sun? Yellow
That is not the correct color!
```

Why does this happen?

Remember that strings are case sensitive. The script is checking if the user input the string `yellow` – `Yellow`, with a capital "Y", is a different string.

You can easily fix this by using the `lower()` method, and doing this small change to the `sun_color.py` file:

```python
answer = input("What color is the sun? ")
if answer.lower() == "yellow":
  print("Correct!")
else:
  print("That is not the correct color!")
```

And now, if you try again...

```
>>> python sun_color.py
What color is the sun? Yellow
Correct!
```

What changed? Writing `answer.lower()` you make sure that the checked string is completely lower case before comparing it with the correct answer string "yellow". In this way it doesn't matter if the user writes "YELLOW" or "yELLOW" or "yellow" – it is all converted to lowercase.

Thanks for reading! Now you know how to use the `lower()` method in JavaScript.

