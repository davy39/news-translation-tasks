---
title: 'NameError: Name plot_cases_simple is Not Defined – How to Fix this Python
  Error'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-27T15:58:39.000Z'
originalURL: https://freecodecamp.org/news/nameerror-name-plot-cases-simple-is-not-defined-how-to-fix-this-python-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/brett-jordan-Ss3U6bEtKww-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "This first step in fixing a coding error is to understand the error. Although\
  \ some error messages may seem confusing, most of them will help you fix the error.\
  \ \nIn this article, we'll be talking about an error that falls under the NameError\
  \ category ..."
---

This first step in fixing a coding error is to understand the error. Although some error messages may seem confusing, most of them will help you fix the error. 

In this article, we'll be talking about an error that falls under the **NameError** category in Python.

You'll see what a **NameError** is, some code examples to show how/why the error occurs, and how to fix them. 

## What Is a NameError in Python?

In Python, the **NameError** occurs when you try to use a variable, function, or module that doesn't exist or wasn't used in a valid way. 

Some of the common mistakes that cause this error are:

* Using a variable or function name that is yet to be defined.
* Misspelling a variable/function name when calling the variable/function. 
* Using a Python module without importing the module, and so on.

## How to Fix "NameError: Name Is Not Defined" in Python

In this section, you'll see how to fix the "NameError: Name is Not Defined" error in Python. 

I've divided this section into sub-sections to show the error above when using variables, functions, and modules.

We'll start with code blocks that raise the error and then see how to fix them.

### Example #1 - Variable Name Is Not Defined in Python

```python
name = "John"

print(age)
# NameError: name 'age' is not defined
```

In the code above, we defined a `name` variable but tried to print `age` which is yet t0 be defined. 

We got an error that says: `NameError: name 'age' is not defined` to show that the `age` variable doesn't exist. 

To fix this, we can create the variable and our code will run fine. Here's how:

```python
name = "John"
age = 12

print(age)
# 12
```

Now the value of `age` gets printed out. 

Similarly, the same error can be raised when we misspell a variable name. Here's an example:

```python
name = "John"

print(nam)
# NameError: name 'nam' is not defined
```

In the code above, we wrote `nam` instead of `name`.  To fix errors like this, you just have to spell the variable name the right way. 

### Example #2 - Function Name Is Not Defined in Python

```python
def sayHello():
    print("Hello World!")
    
sayHelloo()
# NameError: name 'sayHelloo' is not defined
```

In the example above, we added an extra o while calling the function — `sayHelloo()` instead of `sayHello()`.

We got the error: `NameError: name 'sayHelloo' is not defined`. Spelling errors like this are very easy to miss. The error message usually helps in fixing this. 

Here's the right way to call the function:

```python
def sayHello():
    print("Hello World!")
    
sayHello()
# Hello World!

```

Just like we saw in the previous section, calling a variable that is yet to be defined raises an error. The same applies to functions. 

Here's an example:

```python
def sayHello():
    print("Hello World!")
    
sayHello()
# Hello World!

addTWoNumbers()
# NameError: name 'addTWoNumbers' is not defined
```

In the code above, we called a function – `addTWoNumbers()` – that was yet to be defined in the program. To fix this, you can create the function if you need it or just get rid of the function if it is irrelevant. 

Note that calling a function before creating it will throw the same error your way. That is:

```python
sayHello()

def sayHello():
    print("Hello World!")
    
# NameError: name 'sayHello' is not defined
```

So you should always define your functions before calling them.

### Example #3 - Using a Module Without Importing the Module Error in Python

```python
x = 5.5

print(math.ceil(x))
# NameError: name 'math' is not defined
```

In the example above, we're making use of the Python `math.ceil` method without importing the `math` module. 

The resulting error was this: `NameError: name 'math' is not defined`. This happened because the interpreter did not recognize the `math` keyword.

Along with other math methods in Python, we must first import the `math` module to use it. 

Here's a fix:

```python
import math

x = 5.5

print(math.ceil(x))
# 6
```

In the first line of the code, we imported the `math` module. Now, when you run the code above, you should have 6 returned. 

## Summary

In this article, we talked about the "NameError: Name is Not Defined" error in Python. 

We first defined what a **NameError** is in Python. 

We then saw some examples that could raise a **NameError** when working with variables, functions, and modules in Python. Each example, divided into sections, showed how to fix the errors. 

Happy coding!

