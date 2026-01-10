---
title: 'Typeerror: string indices must be integers – How to Fix in Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-21T15:18:02.000Z'
originalURL: https://freecodecamp.org/news/typeerror-string-indices-must-be-integers-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/blake-connally-B3l0g6HLxr8-unsplash.jpg
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, there are certain iterable objects – lists, tuples, and strings\
  \ – whose items or characters can be accessed using their index numbers. \nFor example,\
  \ to access the first character in a string, you'd do something like this:\ngreet\
  \ = \"Hello Wo..."
---

In Python, there are certain iterable objects – lists, tuples, and strings – whose items or characters can be accessed using their index numbers. 

For example, to access the first character in a string, you'd do something like this:

```python
greet = "Hello World!"

print(greet[0])
# H
```

To access the value of the first character in the `greet` string above, we used its index number: `greet[0]`.

But there are cases where you'll get an error that says, "TypeError: string indices must be integers" when trying to access a character in a string. 

In this article, you'll see why this error occurs and how to fix it.

## What Causes "TypeError: string indices must be integers" in Python?

There are two common reasons why the "TypeError: string indices must be integers" error might be raised. 

We'll talk about these reasons and their solutions in two different sub-sections.

### How to Fix the `TypeError: string indices must be integers` Error in Strings in Python

As we saw in last section, to access a character in a string, you use the character's index. 

We get the "TypeError: string indices must be integers" error when we try to access a character using its string value rather the index number. 

Here's an example to help you understand:

```python
greet = "Hello World!"

print(greet["H"])
# TypeError: string indices must be integers
```

As you can see in the code above, we got an error saying `TypeError: string indices must be integers`. 

This happened because we tried to access `H` using its value ("H") instead of its index number. 

That is, `greet["H"]` instead of `greet[0]`. That's exactly how to fix it.

The solution to this is pretty simple:

* Never use strings to access items/characters when working with iterable objects that require you to use index numbers (integers) when accessing items/characters.

### How to Fix the `TypeError: string indices must be integers` Error When Slicing a String in Python

When you slice a string in Python, a range of characters from the string is returned based on given parameters (`start` and `end` parameters). 

Here's an example:

```python
greet = "Hello World!"

print(greet[0:6])
# Hello 
```

In the code above, we provided two parameters – 0 and 6. This returns all the characters within index 0 and index 6. 

We get the "TypeError: string indices must be integers" error when we use the slice syntax incorrectly. 

Here's an example to demonstrate that:

```python
greet = "Hello World!"

print(greet[0,6])
# TypeError: string indices must be integers
```

The error in the code is very easy to miss because we used integers – but we still get an error. In cases like this, the error message may appear misleading.

We're getting this error because we used the wrong syntax. In our example, we used a comma when separating the `start` and `end` parameters: `[0,6]`. This is why we got an error.

To fix this, you can change the comma to a colon.

When slicing strings in Python, you're required to separate the `start` and `end` parameters using a colon – `[0:6]`.

## Summary

In this article, we talked about the "TypeError: string indices must be integers" error in Python. 

This error happens when working with Python strings for two main reasons – using a string instead of an index number (integer) when accessing a character in a string, and using the wrong syntax when slicing strings in Python. 

We saw examples that raised this error in two sub-sections and learned how to fix them.

Happy coding!


