---
title: 'TypeError: module object is not callable [Python Error Solved]'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-04T22:17:35.000Z'
originalURL: https://freecodecamp.org/news/typeerror-module-object-is-not-callable-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/brett-jordan-XWar9MbNGUY-unsplash--1-.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, we'll talk about the \"TypeError: 'module' object is not\
  \ callable\" error in Python. \nWe'll start by defining some of the keywords found\
  \ in the error message — module and callable. \nYou'll then see some examples that\
  \ raise the error, a..."
---

In this article, we'll talk about the "TypeError: 'module' object is not callable" error in Python. 

We'll start by defining some of the keywords found in the error message — `module` and `callable`. 

You'll then see some examples that raise the error, and how to fix it.

Feel free to skip the next two sections if you already know what modules are, and what it means to call a function or method. 

## What Is a Module in Programming?

In modular programming, modules are simply files that contain similar functionalities required to perform a certain task. 

Modules help us separate and group code based on functionality. For example, you could have a module called `math-ops.py` which will only include code related to mathematical operations. 

This makes easier to read, reuse, and understand the code. To use a module in a different part of your code base, you'd have to import it to gain access to all the functionalities defined in the module.

In Python, there are many built-in modules like `os`, `math`, `time`, and so on.

Here's an example that shows how to use the `math` module: 

```python
import math

print(math.sqrt(25))
//5.0
```

As you can see above, the first thing we did before using the `math` module was to import it: `import math`.

We then made use of the module's `sqrt` method which returns the square root of a number: `math.sqrt(25)`.

All it took us to get the square root of 25 was two lines of code. In reality, [the `math` module alone has over 3500 lines of code](https://github.com/python/cpython/blob/main/Modules/mathmodule.c). 

This should help you understand what a module is and how it works. You can also create your own modules (we'll do that later in this article).

## What Does `callable` Mean in the “TypeError: module object is not callable” Error?

In Python and most programming languages, the verb "call" is associated with executing the code written in a function or method. 

Other similar terms mostly used with the same action are "invoke" and "fire". 

Here's a Python function that prints "Smile!" to the console:

```python
def smile():
    print("Smile!")
```

If you run the code above, nothing will be printed to the console because the function `smile` is yet to be called, invoked, or fired. 

To execute the function, we have to write the function name followed by parenthesis. That is:

```python
def smile():
    print("Smile!")
    
smile()
# Smile!
```

Without the parenthesis, the function will not be executed.

Now you should understand what the term `callable` means in the error message: "TypeError: 'module' object is not callable". 

## What Does the “TypeError: module object is not callable” Error Mean in Python?

The last two sections helped us understand some of the keywords found in the "TypeError: 'module' object is not callable" error message. 

To put it simply, the "TypeError: 'module' object is not callable" error means that modules cannot be called like functions or methods. 

## How to Fix the “TypeError: module object is not callable” Error in Python

There are generally two ways that the "TypeError: 'module' object is not callable" error can be raised: calling an inbuilt or third party module, and calling a module in place of a function. 

#### Error Example #1

```python
import math

print(math(25))
# TypeError: 'module' object is not callable

```

In the example above, we called the `math` module (by using parenthesis `()`)  and passed 25 as a parameter hoping to perform a particular math operation: `math(25)`. But we got the error.

To fix this, we can make use of any math method provided by the `math` module. We'll use the `sqrt` method:

```python
import math

print(math.sqrt(25))
# 5.0
```

#### Error Example #2

For this example, I'll create a module for calculating two numbers:

```python
# add.py

def add(a,b):
    print(a+b)
    
```

The name of the module above is `add` which can be derived from the file name **add.py**.

Let's import the `add()` function from the `add` module in another file:

```python
# main.py
import add

add(2,3)
# TypeError: 'module' object is not callable
```

You must be wondering why we're getting the error even though we imported the module.

Well, we imported the module, not the function. That's why. 

To fix this, you have to specify the name of the function while importing the module:

```python
from add import add

add(2,3)
# 5
```

We're being specific: `from add import add`. This is the same as saying, "from the add.py module, import the `add` function".

You can now use the `add()` function in the **main.py** file.

## Summary

In this article, we talked about the "TypeError: 'module' object is not callable" error in Python. 

This error occurs mainly when we call or invoke a module as though it were a function or method. 

We started by discussing what a module is in programming, and what it means to call a function – this helped us understand what causes the error. 

We then gave some examples that showed the error being raised and how to fix it. 

Happy coding!

