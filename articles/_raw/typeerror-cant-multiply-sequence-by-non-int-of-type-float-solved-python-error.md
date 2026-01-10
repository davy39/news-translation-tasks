---
title: 'TypeError: can''t multiply sequence by non-int of type float [Solved Python
  Error]'
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-02T16:36:15.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cant-multiply-sequence-by-non-int-of-type-float-solved-python-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-355948.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn what the Python error TypeError: can''t
  multiply sequence by non-int of type float means.

  Firstly, I will explain why this error gets raised. You will also learn how to solve
  the error and how to avoid it in the first p...'
---

In this article, you will learn what the Python error `TypeError: can't multiply sequence by non-int of type float` means.

Firstly, I will explain why this error gets raised. You will also learn how to solve the error and how to avoid it in the first place.

Here is what we will cover:

1. [What is the `TypeError: can't multiply sequence by non-int of type float` error in Python?](#intro)
    1. [How does the `TypeError: can't multiply sequence by non-int of type float` error occur in Python?](#reason)
2. [How to solve the `TypeError: can't multiply sequence by non-int of type float` error in Python](#solution)

## What Is The `TypeError: can't multiply sequence by non-int of type float` Error in Python? <a name="intro"></a>

There are two types of numbers in Python:

- integers – whole numbers that can be positive, negative, or zero.
- floating-point numbers – positive or negative numbers with a decimal point.

You can multiply an integer with a string to create a repeating sequence of characters:

```python
print("Python" * 3)

# output

# PythonPythonPython
```

And as a reminder, strings are any characters enclosed in single or double quotation marks – including numbers:

```python
print("3" * 3)

# output

# 333
```

But look at what happens when you try to multiply a string with a floating-point number:

```python
print("3" * 3.3)

# output

# Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    print("3" * 3.3)
# TypeError: can't multiply sequence by non-int of type 'float'
```

An error gets raised – specifically a `TypeError`.

A `TypeError` is an exception in Python that gets raised when you try to operate on a data type that doesn't support that specific operation.

As the error message lets you know, you cannot perform multiplication between a string (or sequence) and a floating point number (or float), as Python doesn't support that operation between those two data types.

### How Does The `TypeError: can't multiply sequence by non-int of type float` Error Occur in Python? <a name="reason"></a>

The `TypeError: can't multiply sequence by non-int of type float` error commonly occurs when you use the Python `input()` function, which takes user input. This is because, by default, the `input()` function returns the user input as a string.

Let's take the following hypothetical example. Say that I ask a user to enter their age and store their answer in a variable with the name `user_age`:

```python
user_age = input("Please enter your age: ")
```

I can check the data type of the value stored in the variable `user_age` by using the `type()` function and then print the result to the console:

```python
user_age = input("Please enter your age: ")

print(type(user_age))

# output

# Please enter your age: 29
# <class 'str'>
```

From the output, you can see that even though I entered an integer, the return data type is of type string.

If I then, for whatever reason, wanted to multiply the user's age with a floating-point number, I would get the `TypeError: can't multiply sequence by non-int of type float` error:

```python
user_age = input("Please enter your age: ")

print(user_age * 0.5)

# output

# Please enter your age: 29
# Traceback (most recent call last):
#  File "main.py", line 3, in <module>
#    print(user_age * 0.5)
# TypeError: can't multiply sequence by non-int of type 'float'
```

## How To Solve The `TypeError: can't multiply sequence by non-int of type float` Error in Python <a name="solution"></a>

To solve the `TypeError: can't multiply sequence by non-int of type float` error, convert the string into a floating-point number before multiplying it with a float.

As you saw earlier on, the following throws the `TypeError: can't multiply sequence by non-int of type float` error:

```python
print("3" * 3.3)

# output

# Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    print("3" * 3.3)
# TypeError: can't multiply sequence by non-int of type 'float'
```

If you convert the string `"3"` to a float before multiplying it with the floating-point number `3.3`, there will be no error.

To convert a string to a float, use the `float()` function:

```python
print(float("3") * 3.3)

# output

# 9.899999999999999
```

And you can do the same when you use the `input()` function. Convert the value the user enters to a floating-point number using the `float()` function.

Here is how you would re-write the example using the `input()` function from earlier on:

```python
user_age = float(input("Please enter your age: "))

print(user_age * 0.5)

# output

# Please enter your age: 29
# 14.5
```

The `float()` function converts the string value returned by the `input()` function into a floating-point number, and you can multiply that value with a floating-point number.

## Conclusion

And there you have it! You now know how to solve the `TypeError: can't multiply sequence by non-int of type float` error in Python!

I hope you found this tutorial helpful.

To learn more about the Python programming language, check out freeCodeCamp's [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thank you for reading, and happy coding!



