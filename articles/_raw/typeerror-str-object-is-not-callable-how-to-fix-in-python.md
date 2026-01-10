---
title: 'Typeerror: str object is not callable – How to Fix in Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-08T14:21:57.000Z'
originalURL: https://freecodecamp.org/news/typeerror-str-object-is-not-callable-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/brett-jordan-XWar9MbNGUY-unsplash--1-.jpg
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: null
seo_desc: "Every programming language has certain keywords with specific, prebuilt\
  \ functionalities and meanings. \nNaming your variables or functions after these\
  \ keywords is most likely going to raise an error. We'll discuss one of these cases\
  \ in this article — ..."
---

Every programming language has certain keywords with specific, prebuilt functionalities and meanings. 

Naming your variables or functions after these keywords is most likely going to raise an error. We'll discuss one of these cases in this article — the `TypeError: 'str' object is not callable` error in Python.

The `TypeError: 'str' object is not callable` error mainly occurs when:

* You pass a variable named `str` as a parameter to the `str()` function. 
* When you call a string like a function. 

In the sections that follow, you'll see code examples that raise the `TypeError: 'str' object is not callable` error, and how to fix them. 

## Example #1 – What Will Happen If You Use `str` as a Variable Name in Python?

In this section, you'll see what happens when you used a variable named `str` as the `str()` function's parameter. 

The `str()` function is used to convert certain values into a string. `str(10)` converts the integer `10` to a string.

Here's the first code example:

```python
str = "Hello World"

print(str(str))
# TypeError: 'str' object is not callable
```

In the code above, we created a variable `str` with a value of "Hello World". We passed the variable as a parameter to the `str()` function. 

The result was the `TypeError: 'str' object is not callable` error. This is happening because we are using a variable name that the compiler already recognizes as something different. 

To fix this, you can rename the variable to a something that isn't a predefined keyword in Python. 

Here's a quick fix to the problem:

```python
greetings = "Hello World"

print(str(greetings))
# Hello World
```

Now the code works perfectly. 

## Example #2 – What Will Happen If You Call a String Like a Function in Python?

Calling a string as though it is a function in Python will raise the `TypeError: 'str' object is not callable` error. 

Here's an example:

```python
greetings = "Hello World"

print(greetings())
# TypeError: 'str' object is not callable
```

In the example above, we created a variable called `greetings`. 

While printing it to the console, we used parentheses after the variable name – a syntax used when invoking a function: `greetings()`.

This resulted in the compiler throwing the `TypeError: 'str' object is not callable` error. 

You can easily fix this by removing the parentheses. 

This is the same for every other data type that isn't a function. Attaching parentheses to them will raise the same error. 

So our code should work like this:

```python
greetings = "Hello World"

print(greetings)
# Hello World
```

## Summary

In this article, we talked about the `TypeError: 'str' object is not callable` error in Python.

We talked about why this error might occur and how to fix it. 

To avoid getting this error in your code, you should:

* Avoid naming your variables after keywords built into Python. 
* Never call your variables like functions by adding parentheses to them.

Happy coding!

