---
title: How the Python Lambda Function Works – Explained with Examples
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-10-25T20:37:45.000Z'
originalURL: https://freecodecamp.org/news/python-lambda-function-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-45246--1-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'One of the beautiful things about Python is that it is generally one of
  the most intuitive programming languages out there. Still, certain concepts can
  be difficult to grasp and comprehend. The lambda function is one of them.

  I''ve been there. When I ...'
---

One of the beautiful things about Python is that it is generally one of the most intuitive programming languages out there. Still, certain concepts can be difficult to grasp and comprehend. The lambda function is one of them.

I've been there. When I first started learning Python, I skipped the lambda function because it wasn't clear to me. But with time, I began to understand it. So don't worry – if you're struggling with it, too, I've got you covered.

This tutorial will teach you what a lambda function is, when to use it, and we'll go over some common use cases where the lambda function is commonly applied. Without further ado let's get started.

## What is a Lambda Function?

Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.

Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement. They're also useful when you want to use the function once.

## How to Define a Lambda Function

You can define a lambda function like this:

```python
lambda argument(s) : expression
```

1. `lambda` is a keyword in Python for defining the anonymous function.
    
2. `argument(s)` is a placeholder, that is a variable that will be used to hold the value you want to pass into the function expression. A lambda function can have multiple variables depending on what you want to achieve.
    
3. `expression` is the code you want to execute in the lambda function.
    

Notice that the anonymous function does not have a return keyword. This is because the anonymous function will automatically return the result of the expression in the function once it is executed.

Let's look at an example of a lambda function to see how it works. We'll compare it to a regular user-defined function.

Assume I want to write a function that returns twice the number I pass it. We can define a user-defined function as follows:

```python
def f(x):
  return x * 2

f(3)
>> 6
```

Now for a lambda function. We'll create it like this:

```python
lambda x: x * 3
```

As I explained above, the lambda function does not have a return keyword. As a result, it will return the result of the expression on its own. The x in it also serves as a placeholder for the value to be passed into the expression. You can change it to whatever you want.

Now if you want to call a lambda function, you will use an approach known as immediately invoking the function. That looks like this:

```python
(lambda x : x * 2)(3)

>> 6
```

The reason for this is that since the lambda function does not have a name you can invoke (it's anonymous), you need to enclose the entire statement when you want to call it.

## When Should You Use a Lambda Function?

You should use the lambda function to create simple expressions. For example, expressions that do not include complex structures such as if-else, for-loops, and so on.

So, for example, if you want to create a function with a for-loop, you should use a user-defined function.

## Common Use Cases for Lambda Functions

### How to Use a Lambda Function with Iterables

An iterable is essentially anything that consists of a series of values, such as characters, numbers, and so on.

In Python, iterables include strings, lists, dictionaries, ranges, tuples, and so on. When working with iterables, you can use lambda functions in conjunction with two common functions: `filter()` and `map()`.

#### `Filter()`

When you want to focus on specific values in an iterable, you can use the filter function. The following is the syntax of a filter function:

```python
filter(function, iterable)
```

As you can see, a filter function requires another function that contains the expression or operations that will be performed on the iterable.

For example, say I have a list such as `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Now let's say that I’m only interested in those values in that list that have a remainder of 0 when divided by 2. I can make use of `filter()` and a lambda function.

Firstly I will use the lambda function to create the expression I want to derive like this:

```python
lambda x: x % 2 == 0
```

Then I will insert it into the filter function like this:

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)

>> <filter at 0x1e3f212ad60> # The result is always filter object so I will need to convert it to list using list()

list(filter(lambda x: x % 2 == 0, list1))
>> [2, 4, 6, 8, 10]
```

#### `Map()`

You use the `map()` function whenever you want to modify every value in an iterable.

```python
map(function, iterable)
```

For example, let's say I want to raise all values in the below list to the power of 2. I can easily do that using the lambda and map functions like this:

```python
list1 = [2, 3, 4, 5]

list(map(lambda x: pow(x, 2), list1))
>> [4, 9, 16, 25]
```

### Pandas Series

Another place you'll use lambda functions is in data science when creating a data frame from Pandas. A series is a data frame column. You can manipulate all of the values in a series by using the lambda function.

For example, if I have a data frame with the following columns and want to convert the values in the name column to lower case, I can do so using the Pandas apply function and a Python lambda function like this:

```python
import pandas as pd

df = pd.DataFrame(
    {"name": ["IBRAHIM", "SEGUN", "YUSUF", "DARE", "BOLA", "SOKUNBI"],
     "score": [50, 32, 45, 45, 23, 45]
    }
)
```

![image](https://user-images.githubusercontent.com/73393430/188447505-9ae1baa2-9225-4834-a630-c32b9d1a29f3.png align="left")

```python
df["lower_name"] = df["name"].apply(lambda x: x.lower())
```

The apply function will apply each element of the series to the lambda function. The lambda function will then return a value for each element based on the expression you passed to it. In our case, the expression was to lowercase each element.

![image](https://user-images.githubusercontent.com/73393430/188447749-a483bbad-a91f-40df-b008-5695efe05073.png align="left")

## Conclusion

In this tutorial you learnt the basics of the lambda function and how you can commonly apply it. Thank you for taking your time to read this.
