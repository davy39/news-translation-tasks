---
title: 'TypeError: builtin_function_or_method object is not subscriptable Python Error
  [SOLVED]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-11-02T23:43:20.000Z'
originalURL: https://freecodecamp.org/news/typeerror-builtin-function-or-method-object-is-not-subscriptable-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/built_in_not_subable.png
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "As the name suggests, the error TypeError: builtin_function_or_method object\
  \ is not subscriptable is a “typeerror” that occurs when you try to call a built-in\
  \ function the wrong way. \nWhen a \"typeerror\" occurs, the program is telling\
  \ you that you’re ..."
---

As the name suggests, the error `TypeError: builtin_function_or_method object is not subscriptable` is a “typeerror” that occurs when you try to call a built-in function the wrong way. 

When a "typeerror" occurs, the program is telling you that you’re mixing up types. That means, for example, you might be concatenating a string with an integer.

In this article, I will show you why the TypeError: builtin_function_or_method object is not subscriptable occurs and how you can fix it. 

## Why The TypeError: builtin_function_or_method object is not subscriptable Occurs 
Every built-in function of Python such as `print()`, `append()`, `sorted()`, `max()`, and others must be called with parenthesis or round brackets (`()`). 

If you try to use square brackets, Python won't treat it as a function call. Instead, Python will think you’re trying to access something from a list or string and then throw the error.

For example, the code below throws the error because I was trying to print the value of the variable with square braces in front of the `print()` function:
 
And if you surround what you want to print with square brackets even if the item is iterable, you still get the error:

```py
gadgets = ["Mouse", "Monitor", "Laptop"]
print[gadgets[0]]

# Output: Traceback (most recent call last):
#   File "built_in_obj_not_subable.py", line 2, in <module>
#     print[gadgets[0]]
# TypeError: 'builtin_function_or_method' object is not subscriptable
``` 

This issue is not particular to the `print()` function. If you try to call any other built-in function with square brackets, you also get the error. 

In the example below, I tried to call `max()` with square brackets and I got the error:

```py
numbers = [5, 7, 24, 6, 90]
max_num = max(numbers)
print[max_num]

# Traceback (most recent call last):
#   File "built_in_obj_not_subable.py", line 11, in <module>
#     print[max_num]
# TypeError: 'builtin_function_or_method' object is not subscriptable

```

## How to Fix the TypeError: builtin_function_or_method object is not subscriptable Error

To fix this error, all you need to do is make sure you use parenthesis to call the function.

You only have to use square brackets if you want to access an item from iterable data such as string, list, or tuple:

```py
gadgets = ["Mouse", "Monitor", "Laptop"]
print(gadgets[0])

# Output: Mouse
```
```py
numbers = [5, 7, 24, 6, 90]
max_num = max(numbers)
print(max_num)

# Output: 90
```

## Wrapping Up
This article showed you why the TypeError: builtin_function_or_method object is not subscriptable occurs and how to fix it.

Remember that you only need to use square brackets (`[]`) to access an item from iterable data and you shouldn't use it to call a function.

If you’re getting this error, you should look in your code for any point at which you are calling a built-in function with square brackets and replace it with parenthesis.

Thanks for reading.



