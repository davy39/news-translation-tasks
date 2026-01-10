---
title: Lambda Expressions in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T23:41:00.000Z'
originalURL: https://freecodecamp.org/news/lambda-expressions-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e32740569d1a4ca3bd6.jpg
tags:
- name: Lambda Expressions
  slug: lambda-expressions
- name: Python
  slug: python
seo_title: null
seo_desc: 'Lambda Expressions

  Lambda Expressions are ideally used when we need to do something simple and are
  more interested in getting the job done quickly rather than formally naming the
  function. Lambda expressions are also known as anonymous functions.

  Lam...'
---

## **Lambda Expressions**

Lambda Expressions are ideally used when we need to do something simple and are more interested in getting the job done quickly rather than formally naming the function. Lambda expressions are also known as anonymous functions.

Lambda Expressions in Python are a short way to declare small and anonymous functions (it is not necessary to provide a name for lambda functions). 

Lambda functions behave just like regular functions declared with the `def` keyword. They come in handy when you want to define a small function in a concise way. They can contain only one expression, so they are not best suited for functions with control-flow statements. 

### Syntax of a Lambda Function

`lambda arguments: expression`

Lambda functions can have any number of arguments but only one expression.

### Example code

```py
# Lambda function to calculate square of a number
square = lambda x: x ** 2
print(square(3)) # Output: 9

# Traditional function to calculate square of a number
def square1(num):
  return num ** 2
print(square(5)) # Output: 25
```

In the above lambda example, `lambda x: x ** 2` yields an anonymous function object which can be associated with any name. So, we associated the function object with `square`. So from now on we can call the `square` object like any traditional function, for example `square(10)`

## **Examples of lambda functions**

### **Beginner**

```py
lambda_func = lambda x: x**2 # Function that takes an integer and returns its square
lambda_func(3) # Returns 9
```

### **Intermediate**

```py
lambda_func = lambda x: True if x**2 >= 10 else False
lambda_func(3) # Returns False
lambda_func(4) # Returns True
```

### **Complex**

```py
my_dict = {"A": 1, "B": 2, "C": 3}
sorted(my_dict, key=lambda x: my_dict[x]%3) # Returns ['C', 'A', 'B']
```

## Use-case

Let’s say you want to filter out odd numbers from a `list`. You could use a `for` loop:

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = []

for num in my_list:
     if num % 2 != 0:
         filtered.append(num)

print(filtered)      # Python 2: print filtered
# [1, 3, 5, 7, 9]
```

Or you could write this as a one liner with list-comprehensions:

```python
filtered = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0]
```

But you might be tempted to use the built-in `filter` function. Why? The first example is a bit too verbose and the one-liner can be harder to understand. But `filter` offers the best of both words. What is more, the built-in functions are usually faster.

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered = filter(lambda x: x % 2 != 0, my_list)

list(filtered)
# [1, 3, 5, 7, 9]
```

NOTE: in Python 3 built in functions return generator objects, so you have to call `list`. In Python 2, on the other hand, they return a `list`, `tuple`or `string`.

So what happened? You told `filter` to take each element in `my_list` and apply the lambda expressions. The values that return `False` are filtered out.

#### **More Information:**

* [Official Docs](https://docs.python.org/3/reference/expressions.html#lambda)

