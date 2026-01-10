---
title: Python Anonymous Function – How to Use Lambda Functions
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-15T17:17:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lambda-functions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/lambda-functions-in-python.png
tags:
- name: functions
  slug: functions
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: null
seo_desc: 'You can use functions in programming to store a piece of code that can
  be invoked when needed. This prevents you from retyping the same logic every time
  you need that code.

  In this article, you''ll learn how to create and use anonymous functions in Py...'
---

You can use functions in programming to store a piece of code that can be invoked when needed. This prevents you from retyping the same logic every time you need that code.

In this article, you'll learn how to create and use anonymous functions in Python. They are also called lambda functions.

We'll begin with a quick overview of how regular functions are created in Python. Then you'll learn the syntax and practical applications of anonymous functions in Python. 

You'll also see some of the differences between lambda and regular functions in Python, and when to use lambda functions.

## How to Use Functions in Python

Functions prevent you from reinventing the wheel when certain logic is required multiple times.

Consider the code below:

```python
first_addition = 2+3 
print(first_addition) # 5 

second_addition = 3+5 
print(second_addition) # 8
```

We had to recreate the logic for addition multiple times in different variables. Imagine if you had to do this a hundred times.

With a function, you can create the logic once and reuse it as much as you want to. Here's an example in Python:

```python
def add_numbers(a,b): return a + b 

print(add_numbers(2,3)) # 5 
print(add_numbers(3,5)) # 8 
print(add_numbers(5,7)) # 12
```

Using the `def` keyword, we created a function called `add_numbers(a,b)`. It takes two parameters – `a` and `b`. The function returns the sum of `a` and `b`.

So to use the logic multiple times, we just had to call the function and pass in different parameters for different operations:

```python
print(add_numbers(2,3)) # 5 
print(add_numbers(3,5)) # 8 
print(add_numbers(5,7)) # 12 
```

Now let's take a look at anonymous/lambda functions in Python.

## How to Use Lambda Functions in Python

An anonymous function in Python is a function without a name. It can be immediately invoked or stored in a variable.

Anonymous functions in Python are also known as lambda functions.

Here's the syntax for creating a lambda function in Python:

```python
lambda parameter(s) : expression
```

There are three values that define a lambda function as seen in the syntax above:

* A lambda function is created using the `lambda` keyword.
* The keyword is followed by one or many parameters.
* Lastly, an expression is provided for the function. This is the part of the code that gets executed/returned. 

The parameter(s) and expression are separated by a colon.

Here's an example:

```python
add_numbers = lambda a,b : a + b 
  
print(add_numbers(2,3)) # 5       
```

In the code above, we created a lambda function with two parameters – `a` and `b`. The function returns the sum of the parameters.

That is: `lambda a,b : a + b` 

Note that the function has no name. We assigned the lambda function to a variable called `add_numbers` so that we can easily invoke the function through the variable. 

Without assigning a lambda function to a variable, you'd have something like this:

```python
print(lambda a,b : a + b)
# <function <lambda> at 0x7f757922fb00>
```

The code above simply returns a lambda object in the console. 

You can immediately call a lambda function using parenthesis:

```python
(lambda a,b : a + b)(2,3)
```

When the code above is printed, you'll get 5 returned.

## What Is the Difference Between Lambda and Regular Functions in Python?

Here are some differences between lambda functions and regular functions in Python:

| Lambda functions| Regular functions|
| ------------- |:-------------:|
| Defined using the lambda keyword | Defined using the def keyword |
| Can be written in one line  | Requires more than one line of code |
| No return statement required | Return statement must be defined when returning values|
| Can be used anonymously  | Regular functions must be given a name |

## When to Use a Lambda Function in Python

Although you can use both regular functions and lambda functions to achieve the same results, here are some of the reasons why you might pick a lambda function:

First of all, you can use a lambda function when you need a function that'll be used just once. This is especially useful when working with functions like `map`, `reduce`, `filter`. Consider the code below:

```python
def double_number(n):
    return n + n

numbers = [1, 3, 5, 7, 9]

double_result = map(double_number, numbers)

print(list(double_result))
# [2, 6, 10, 14, 18]
```

In the code above, we created a regular function called `double_number` which doubles the value of a number. 

Although the function was passed in as a parameter to the `map` function — `map(double_number, numbers)`, we had to write the logic before using it. 

With lambda functions, you can do this: 

```python
numbers = [1, 3, 5, 7, 9]

double_result = map(lambda x : x+x, numbers)

print(list(double_result))
# [2, 6, 10, 14, 18]
```

As you can see above, we just passed a lambda function — `lambda x : x+x` — as a parameter to the `map` function: `map(lambda x : x+x, numbers)`.

We were able to achieve the same result with fewer lines of code. There was no need for defining a function first before use. 

You can also use a lambda function when you need a function that should be invoked immediately. As you can see in the example in the previous point, we first defined the regular function before using it. Lambda functions can be invoked immediately after creating them.

Finally, lambdas are useful when you want to use a function inside a function. Or when you want to create a function that returns a function.

## Summary

In this article, we talked about lambda functions in Python. There are functions without a name and can be executed with a single line of code. 

We saw how to use regular functions in Python with some examples. 

We then saw the syntax and a practical example of using lambda functions. 

Lastly, we talked about the differences between lambda functions and regular functions in Python, and when to use lambda functions.

Happy coding!

