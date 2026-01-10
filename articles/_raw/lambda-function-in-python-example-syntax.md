---
title: Lambda Function in Python – Example Syntax
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-09-27T15:23:43.000Z'
originalURL: https://freecodecamp.org/news/lambda-function-in-python-example-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-aleksandar-pasaric-4344759.jpg
tags:
- name: beginner
  slug: beginner
- name: Lambda Expressions
  slug: lambda-expressions
- name: Python
  slug: python
seo_title: null
seo_desc: 'Lambda functions are anonymous functions that can contain only one expression.

  You may think that lambda functions are an intermediate or advanced feature, but
  here you will learn how you can easily start using them in your code.

  In Python, functions...'
---

Lambda functions are anonymous functions that can contain only one expression.

You may think that lambda functions are an intermediate or advanced feature, but here you will learn how you can easily start using them in your code.

In Python, functions are usually created like this:

```pithon
def my_func(a):
  # function body
```

You declare them with the `def` keyword, give them a name, and then add the list of arguments surrounded by round parenthesis. There could be many lines of code, with as many statements and expressions as you need inside.

But sometimes you might need a function with only one expression inside, for example a function that doubles its argument:

```python
def double(x):
  return x*2
```

This is a function that you can use, for example, with the `map` method.

```python
def double(x):
  return x*2
  
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(double, my_list))
print(new_list) # [2, 4, 6, 8, 10, 12]
```

This would be a good place to use a lambda function, as it can be created exactly where you need to use it. This means using fewer lines of code and and you can avoid creating a named function that is only used once (and then has to be stored in memory).

## How to use lambda functions in Python

You use lambda functions when you need a small function for a short time – for example as an argument of a higher order function like `[map](https://www.freecodecamp.org/news/python-map-function-how-to-map-a-list-in-python-3-0-with-example-code/)` or `filter`. 

The syntax of a lambda function is `lambda args: expression`. You first write the word `lambda`, then a single space, then a comma separated list of all the arguments, followed by a colon, and then the expression that is the body of the function.

Note that you can't give a name to lambda functions, as they are anonymous (without a name) by definition.

A lambda function can have as many arguments as you need to use, but the body must be one single expression.

### Example 1

For example, you could write a lambda function that doubles its argument: `lambda x: x*2`, and use it with the `map` function to double all elements in a list:

```python
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(lambda x: x*2, my_list))
print(new_list) # [2, 4, 6, 8, 10, 12]
```

Notice the difference between this one and the function we wrote above with the `double` function. This one is more compact, and there is not an extra function occupying space in memory.

### Example 2

Or you could write a lambda function that checks if a number is positive, like `lambda x: x > 0`, and use it with `filter` to create a list of only positive numbers.

```python
my_list = [18, -3, 5, 0, -1, 12]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list) # [18, 5, 12]
```

The lambda function is defined where it is used, in this way there is not a named function in memory. If a function is used i only one place it makes sense to use a lambda function to avoid cluttering.

### Example 3

You can also return a lambda function from a function.

If you ever need to create multiple functions that multiply numbers, for example doubling or tripling and so on, lambda can help.

Instead of creating multiple functions, you could create a function `multiplyBy` as below, and then call this function multiple times with different arguments to create the functions that double, triple, and so on.

```python
def muliplyBy (n):
  return lambda x: x*n
  
double = multiplyBy(2)
triple = muliplyBy(3)
times10 = multiplyBy(10)
```

The lambda function takes the value `n` from the parent function, so that in `double` the value of `n` is `2`, in `triple` it is `3` and in `times10` it is `10`. Now calling these functions with an argument will multiply that number.

```python
double(6)
> 12
triple(5)
> 15
times10(12)
> 120
```

If you weren't using a lambda function here, you would need to define a different function inside `multiplyBy`, something like the below:

```python
def muliplyBy (x):
  def temp (n):
    return x*n
  return temp
```

Using a lambda function uses half the lines and makes it more readable.

## Conclusion

Lambda functions are a compact way to write functions if your function includes only one small expression. They are not usually something that beginner coders use, but here you have seen how you can easily use them at any level.

