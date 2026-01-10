---
title: Python Decorators Explained For Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-06T18:50:33.000Z'
originalURL: https://freecodecamp.org/news/python-decorators-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/python_decorators_explained.png
tags:
- name: beginner
  slug: beginner
- name: decorator
  slug: decorator
- name: Python
  slug: python
seo_title: null
seo_desc: "By Roy Chng\nIn the world of Python programming, decorators can be an elegant\
  \ and powerful tool in the hands of experienced developers. \nDecorators give you\
  \ the ability to modify the behavior of functions without altering their source\
  \ code, providing ..."
---

By Roy Chng

In the world of Python programming, decorators can be an elegant and powerful tool in the hands of experienced developers. 

Decorators give you the ability to modify the behavior of functions without altering their source code, providing a concise and flexible way to enhance and extend their functionality.

In this article, I'll go over the intricacies of how to use decorators in Python, and show examples of where they are useful.

## Quick Function Recap

Simply put, a function is a way of running a block of code repeatedly with different arguments. 

In other words, it can take inputs, use those inputs to run some pre-defined set of code, and then return an output.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/functions.png)
_Functions take in inputs, use it to run a set of code and returns an output_

In Python, a function is written like so:

```python
def add_one(num):
	return num + 1
```

When we want to call it, we can write the function's names with parenthesis and pass in the necessary inputs (arguments):

```python
final_value = add_one(1)
print(final_value) # 2
```

Note that for the most part, arguments and parameters mean the same thing. They are the variables used in the function. 

The difference lies in where we are referring to them. Arguments are what we pass into the function when calling it, and parameters are what is declared in the function.

## How to Pass Functions as Arguments

Commonly, when calling functions with arguments, we pass values such as Integers, Floats, Strings, Lists, Dictionaries and other data types.

But, something we can also do is to pass a function as an argument as well:

```python
def inner_function():
	print("inner_function is called")
    
def outer_function(func):
	print("outer_function is called")
 	func()
   
outer_function(inner_function)
# outer_function is called
# inner_function is called
    
```

In this example we create two functions: `inner_function` and `outer_function`.

 `outer_function` has a parameter called `func` which it calls after it itself is called.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/first_class_citizens.png)
_outer_function executes first. It then calls the function that was passed as a parameter_

Think about it like how we can treat functions like any other value or variable. 

The proper term for this is that functions are **first class citizens**. This means that they are just like any other object and can be passed as arguments into other functions, be assigned to variables, or returned by other functions.

So, `outer_function` can take in a function as a parameter and call it when it is executed.

## How to Return Functions

Another benefit of being able to treat functions as objects is that we can define them in other functions and return them as well:

```python
def outer_function():
	print("outer_function is called")
    
	def inner_function():
    		print("inner_function is called")
      
	return inner_function
```

Note that in this example, when we return `inner_function`, we didn't call it. 

We only returned the reference to it, so that we can store and call it later on:

```python
returned_function = outer_function()
# outer_funciton is called

returned_function()
# inner_function is called
```

If you are like I am, this might seem interesting and all, but you are still probably wondering how this can be useful in actual programs 🤔.  This is something we'll take a look at in a moment!

## How to Create Decorators in Python

Accepting functions as arguments, defining functions within other functions, and returning them are exactly what we need to know to create decorators in Python. We use decorators to add additional functionality to existing functions.

For example, if we wanted to create a decorator that will add 1 to the return value of any function, we can do it like so:

```python
def add_one_decorator(func):
	def add_one():
    	value = func()
        return value + 1
        
	return add_one
```

Now, if we have a function that returns a number, we can use this decorator to add 1 to whatever value it outputs.

```python
def example_function():
	return 1
    
final_value = add_one_decorator(example_function)
print(final_value()) # 2
```

In this example, we call the `add_one_decorator` function and pass in the reference to `example_function`. 

When we call the `add_one_decorator` function, it creates a new function, `add_one`, defined within it and returns a reference to this new function. We store this function in the variable `final_value`.

So, when executing the `final_value` function, the `add_one` function is called.

The `add_one` function defined within `add_one_decorator` will then call `example_function`, store its value, and add one to it.

Ultimately, this results in `2` being returned and printed to the console.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/python_decorators-1.gif)
_Process of how the code will execute_

Notice how we didn't have to change the original `example_function` to modify its return value and to add functionality to it. This is what makes decorators so useful!

Just to clarify, decorators aren't specific to Python. They're a concept that can be applied in other programming languages. But in Python, you can make use of them easily using the `@` syntax.

## How to Use the `@` Syntax in Python

![Image](https://www.freecodecamp.org/news/content/images/2023/06/at_syntax.png)
_The @ character_

As we saw above, when we want to use decorators, we have to call the decorator function and pass in the function we want to modify.

In Python, we can make use of the `@` syntax to be much more efficient.

```python
@add_one_decorator
def example_function():
	return 1
```

By writing `@add_one_decorator` above our function, it is equivalent to the following:

```python
example_function = add_one_decorator(example_function)
```

This means that whenever we call the `example_function`, we will essentially be calling the `add_one` function defined within the decorator.

## How to Pass Arguments With Decorators

When using decorators, we might also want the decorated function to be able to receive arguments when it is called from the wrapper function.

For example, if we had a function that requires two parameters and returns their sum:

```python
def add(a,b):
	return a + b
    
print(add(1,2)) # 3
```

And if we used a decorator that added 1 to the output:

```python
def add_one_decorator(func):
	def add_one():
    	value = func()
        return value + 1
        
    return add_one
    
@add_one_decorator
def add(a,b):
	return a + b
    
add(1,2)
# TypeError: add_one_decorator.<locals>.add_one() takes 0 positional arguments but 2 were given


```

When doing so, we run into an error: the wrapper function (`add_one`) doesn't take any arguments but we provided two arguments. 

To fix this, we need to pass down any arguments received from `add_one` to the decorated function when calling it:

```python
def add_one_decorator(func):
	def add_one(*args, **kwargs):
    	value = func(*args, **kwargs)
        return value + 1
        
     return add_one
     
 @add_one_decorator
 def add(a,b):
 	return a+b
    
 print(add(1,2)) # 4
```

We make use of `*args` and `**kwargs` to indicate that the `add_one` wrapper function should be able to receive any amount of positional arguments (`args`) and keyword arguments (`kwargs`). 

`args` will be a list of all the positional keywords given, in this case `[1,2].`

`kwargs` will be a dictionary with keys as the keywords arguments used and the values as the values assigned to them, in this case an empty dictionary.

Writing `func(*args, **kwargs)` indicates that we want to call `func` with the same positional and keyword arguments that was received

This ensures that all the positional and keyword arguments passed into the decorated function will be passed into the original function.

## Why Are Decorators In Python Useful? Real Code Examples

Now that we've taken a look at what exactly are Python decorators, let's see some real-world examples of when decorates are useful.

### Logging

When building larger applications, it is often helpful to have logs of what functions were executed with information, such as what arguments were used, and what the function returned during the application's runtime.

This can be incredibly useful for troubleshooting and debugging when things go wrong, to help pinpoint where the problem originiated from. Even if not for debugging, logging can be useful for monitoring the status of your program.

Here's a simple example of how we can create a simple logger (using the built-in Python `logging` package) to save information about our application as it is running, into a file named `main.log`:

```python
import logging

def function_logger(func):
    logging.basicConfig(level = logging.INFO, filename="main.log")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}")
        return result
    
    return wrapper

@function_logger
def add_one(value):
    return value + 1

print(add_one(1))
```

Whenever the `add_one` function runs, a new log will be appended to the `main.log` file:

```
INFO:root:add_one ran with positional arguments: (1,) and keyword arguments: {}. Return value: 2

```

### Caching

If we have an application that requires running the same function multiple times with the same arguments, returning the same value, it can quickly become inefficient and take up unnecessary resources.

To prevent this, it can be useful to store the arguments used and the returned value of the function any time it is called, and simply re-use the returned value if we have already called the function with the same arguments.

In Python, this can be implemented by using the `@lru_cache` decorator from the `functools` module which comes installed with Python.

**LRU** refers to **Least Recently Used**, meaning that whenever the function has been called, the arguments used and returned value will be stored. But once the number of such entries has reached the maximum size, which by default is 128, the least recently used entry will be removed.

```python
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

```

In this example, the function `fibonacci` takes in the argument `n` and if it is less than `1`, returns `n`, otherwise returning the sum of the function called with `n-1` and `n-2`.

So, if the function is called with `n=10`, it returns `55`:

```python
print(fibnoacci(10))
# 55
```

In this case, when we call the function `fibonacci(10)`, it calls the function `fibonacci(9)` and `fibonacci(8)`, and so on, until it reaches 1 or 0.

If we were to then use this function more than once:

```python
fibonacci(50)
fibonacci(100)
```

We can make use of the cache of the entries that have been saved. So when we call `fibonacci(50)`, it can stop calling the `fibonacci` function once it reaches `10` and when we call `fibonacci(100)`, it can stop calling the function once it reaches `50`, making the program far more efficient.

These examples have one thing in common, which is that they are incredibly easy to implement to your pre-existing functions in Python. You do not need to alter your code or manually wrap your function in another. 

Being able to simply use the `@` syntax makes it a breeze to leverage additional modules and packages.

## Summary

Python decorators make it possible to effortlessly extend functions without having to modify them. In this tutorial, you learned how decorators work and saw some examples of where they can be used.

If you enjoy my writing, consider checking out my [YouTube channel](https://www.youtube.com/@turbinethree) for more Python content.

Happy coding!

