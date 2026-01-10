---
title: 'ValueError: math domain error [Solved Python Error]'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-22T16:11:13.000Z'
originalURL: https://freecodecamp.org/news/valueerror-python-math-domain-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/python-math-domain-error.png
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: null
seo_desc: "In mathematics, there are certain operations that are considered to be\
  \ mathematically undefined operations. \nSome examples of these undefined operations\
  \ are:\n\nThe square root of a negative number (√-2). \nA divisor with a value of\
  \ zero (20/0). \n\nThe \"..."
---

In mathematics, there are certain operations that are considered to be mathematically undefined operations. 

Some examples of these undefined operations are:

* The square root of a negative number (√-2). 
* A divisor with a value of zero (20/0). 

The "ValueError: math domain error" error in Python occurs when you carry out a math operation that falls outside the domain of the operation.

To put it simply, this error occurs in Python when you perform a math operation with mathematically undefined values. 

In this article, you'll learn how to fix the "ValueError: math domain error" error in Python. 

You'll start by learning what the keywords found in the error message mean. You'll then see some practical code examples that raise the error and a fix for each example. 

Let's get started!

## How to Fix the "ValueError: math domain error" Error in Python

A `valueError` is raised when a function or operation receives a parameter with an invalid value. 

A domain in math is the range of all possible values a function can accept. All values that fall outside the domain are considered "undefined" by the function. 

So the `math domain error` message simply means that you're using a value that falls outside the accepted domain of a function.

Here are some examples:

### Example #1 – Python Math Domain Error With `math.sqrt`

```python
import math

print(math.sqrt(-1))
# ValueError: math domain error
```

In the code above, we're making use of the `sqrt` method from the `math` module to get the square root of a number. 

We're getting the "ValueError: math domain error" returned because -1 falls outside the range of numbers whose square root can be obtained mathematically. 

### Solution #1 – Python Math Domain Error With `math.sqrt`

To fix this error, simply use an `if` statement to check if the number is negative before proceeding to find the square root. 

If the number is greater than or equal to zero, then the code can be executed. Otherwise, a message would be printed out to notify the user that a negative number can't be used. 

Here's a code example:

```python
import math

number = float(input('Enter number: '))

if number >= 0:
    print(f'The square root of {number} is {math.sqrt(number)}')
else: 
    print('Cannot find the square root of a negative number')
```

### Example #2 – Python Math Domain Error With `math.log`

You use the `math.log` method to get the logarithm of a number. Just like the `sqrt` method, you can't get the log of a negative number. 

Also, you can't get the log of the number 0. So we have to modify the condition of the `if` statement to check for that. 

Here's an example that raises the error:

```python
import math

print(math.log(0))
# ValueError: math domain error
```

### Solution #2 – Python Math Domain Error With `math.log`

```python
import math

number = float(input('Enter number: '))

if number > 0:
    print(f'The log of {number} is {math.log(number)}')
else: 
    print('Cannot find the log of 0 or a negative number')
```

In the code above, we're using the condition of the `if` statement to make sure the number inputted by the user is neither zero nor a negative number (the number must be greater than zero).

### Example #3 – Python Math Domain Error With `math.acos`

You use the `math.acos` method to find the arc cosine value of a number. 

The domain of the `acos` method is from -1 to 1, so any value that falls outside that range will raise the "ValueError: math domain error" error. 

Here's an example:

```python
import math

print(math.acos(2))
# ValueError: math domain error
```

### Solution #3 – Python Math Domain Error With `math.acos`

```python
import math

number = float(input('Enter number: '))

if -1 <= number <= 1:
    print(f'The arc cosine of {number} is {math.acos(number)}')
else:
    print('Please enter a number between -1 and 1.')

```

Just like the solution in other examples, we're using an `if` statement to make sure the number inputted by the user doesn't exceed a certain range. 

That is, any value that falls outside the range of -1 to 1 will prompt the user to input a correct value. 

## Summary

In this article, we talked about the "ValueError: math domain error" error in Python. 

We had a look at some code examples that raised the error, and how to check for and fix them using an `if` statement. 

Happy coding!

