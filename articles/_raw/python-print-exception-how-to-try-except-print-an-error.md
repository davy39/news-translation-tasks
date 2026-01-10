---
title: Python Print Exception – How to Try-Except-Print an Error
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-15T21:31:00.000Z'
originalURL: https://freecodecamp.org/news/python-print-exception-how-to-try-except-print-an-error
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pythonExceptionHandling.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "Every programming language has its way of handling exceptions and errors,\
  \ and Python is no exception. \nPython comes with a built-in try…except syntax with\
  \ which you can handle errors and stop them from interrupting the running of your\
  \ program.\nIn thi..."
---

Every programming language has its way of handling exceptions and errors, and Python is no exception. 

Python comes with a built-in `try…except` syntax with which you can handle errors and stop them from interrupting the running of your program.

In this article, you’ll learn how to use that `try…except` syntax to handle exceptions in your code so they don’t stop your program from running.


## What We'll Cover
- [What is an Exception?](#heading-what-is-an-exception)
- [The `try…except` Syntax](#heading-the-tryexcept-syntax)
- [How to Handle Exceptions with `try…except`](#heading-how-to-handle-exceptions-with-tryexcept)
- [How to Print an Exception with `try…except`](#heading-how-to-print-an-exception-with-tryexcept)
- [How to Print the Exception Name](#heading-how-to-print-the-exception-name)
- [Conclusion](#heading-conclusion)


## What is an Exception?
In Python, an exception is an error object. It is an error that occurs during the execution of your program and stops it from running – subsequently displaying an error message.

When an exception occurs, Python creates an exception object which contains the type of the error and the line it affects.

Python has many built-in exceptions such as `IndexError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError` `KeyError`, and many more. 


## The `try…except` Syntax
Instead of allowing these exceptions to stop your program from running, you can put the code you want to run in a `try` block and handle the exception in the `except` block.

The basic syntax of `try…except` looks like this:
```py
try:
  # code to run
except:
  # handle error
```


## How to Handle Exceptions with `try…except`
You can handle each of the exceptions mentioned in this article with `try…except`. In fact, you can handle all the exceptions in Python with `try…except`.

For example, if you have a large program and you don’t know whether an identifier exists or not, you can execute what you want to do with the identifier in a `try` block and handle a possible error in the `except` block:

```py
try:
  print("Here's variable x:", x)
except:
  print("An error occured") # An error occured
```

You can see that the `except` ran because there’s no variable called `x` in the code.

Keep reading. Because I will show you how to make those errors look better by showing you how to handle exceptions gracefully.


## How to Print an Exception with `try…except`
But what if you want to print the exact exception that occurred? You can do this by assigning the `Exception` to a variable right in front of the `except` keyword.

When you do this and print the Exception to the terminal, it is the value of the `Exception` that you get.

This is how I printed the ` ZeroDivisionError ` exception to the terminal:

```py
try:
    res = 190 / 0
except Exception as error:
    # handle the exception
    print("An exception occurred:", error) # An exception occurred: division by zero
```

And this is how I printed the `NameError` exception too:

```py
try:
  print("Here's variable x:", x)
except Exception as error:
  print("An error occurred:", error) # An error occurred: name 'x' is not defined
```

You can follow this pattern to print any exception to the terminal.


## How to Print the Exception Name
What if you want to get the exact exception name and print it to the terminal? That’s possible too. All you need to do is use the `type()` function to get the type of the exception and then use the `__name__` attribute to get the name of the exception.

This is how I modified the `ZeroDivisionError` example to print the exact exception:

```py
try:
    res = 190 / 0
except Exception as error:
    # handle the exception
    print("An exception occurred:", type(error).__name__) # An exception occurred: ZeroDivisionError
```

And this is how I modified the other example to print the `NameError` example:

```py
try:
  print("Here's variable x:", x)
except Exception as error:
  print("An error occurred:", type(error).__name__) # An error occurred: NameError
```

Normally, when you encounter an Exception such as `NameError` and `ZeroDivisionError`, for example, you get the error in the terminal this way:

![Screenshot-2023-03-13-at-17.58.33](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-17.58.33.png)

![Screenshot-2023-03-13-at-17.58.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-17.58.54.png) 

You can combine the `type()` function and that error variable to make the exception look better:

```py
try:
  print("Here's variable x:", x)
except Exception as error:
  print("An error occurred:", type(error).__name__, "–", error) # An error occurred: NameError – name 'x' is not defined
```

```py
try:
    res = 190 / 0
except Exception as error:
    # handle the exception
    print("An exception occurred:", type(error).__name__, "–", error) # An exception occurred: ZeroDivisionError – division by zero
    
```


## Conclusion
As shown in this article, the `try…except` syntax is a great way to handle errors and prevent your program from stopping during execution.

You can even print that `Exception` to the terminal by assigning the error to a variable, and get the exact type of the `Exception` with the `type()` function.

Happy coding!


