---
title: How to Use *args and **kwargs in Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-03-23T18:55:00.000Z'
originalURL: https://freecodecamp.org/news/args-and-kwargs-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/args.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, we'll discuss *args and ****kwargs** in Python along with\
  \ their uses and some examples.\nWhen writing a function, we often need to pass\
  \ values to the function. These values are called function arguments. \nProblem\
  \ with Function Argumen..."
---

In this article, we'll discuss **`*args`** and `****kwargs**` in Python along with their uses and some examples.

When writing a function, we often need to pass values to the function. These values are called **function arguments**. 

## Problem with Function Arguments

Let's define a function to add two numbers in Python. We'll write it like this:

```python
def add(x, y):
    return x+y

print(add(2,3))
```

Output:

```bash
5
```

What if you need to add three numbers? Simple, we can modify the function to accept three arguments and return their sum as:

```python
def add(x, y, z):
    return x+y+z

print(add(2, 3, 5))
```

Output:

```bash
10
```

Wasn't that quite simple? Yes, it was!

But what if we're again required to add two numbers only? Will our modified function help us get the sum? Let's see:

```python
def add(x, y, z):
    return x+y+z


print(add(2, 3))
```

Output:

```bash
Traceback (most recent call last):
  File "D:\Quarantine\Test\Blog-Codes\args-kwargs\main.py", line 14, in <module>
    print(add(2, 3))
TypeError: add() missing 1 required positional argument: 'z'
```

You see the problem?

The problem arises when we have a variable number of arguments. Should we keep modifying the function to accept the exact number of arguments? Of course not, we won't be doing this.

So there must be some other way to do it. This is where **`*args`** and `****kwargs**` jump in.

You can use `*args` and `****kwargs**` as arguments of a function when you are unsure about the number of arguments to pass in the functions.

## How to Use *args in Python

**`*args`** allows us to pass a variable number of non-keyword arguments to a Python function. In the function, we should use an asterisk (**`*`**) before the parameter name to pass a variable number of arguments.

```python
def add(*args):
    print(args, type(args))

add(2, 3)
```

Output:

```bash
(2, 3) <class 'tuple'>
```

Thus, we're sure that these passed arguments make a tuple inside the function with the same name as the parameter excluding **`*`**.

Now let's rewrite our `**add()**` function with a variable number of arguments.

```python
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))
```

Output:

```bash
5
10
17
26
```

Note that the name of the argument need not necessarily be `**args**` – it can be anything. In this case it's `**numbers**`. But it's generally a standard way to use `***args**` as the name.

## How to Use **kwargs in Python

**`**kwargs`** allows us to pass a variable number of keyword arguments to a Python function. In the function, we use the double-asterisk (**`**`**) before the parameter name to denote this type of argument.

```python
def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


total_fruits(banana=5, mango=7, apple=8)
```

Output:

```bash
{'banana': 5, 'mango': 7, 'apple': 8} <class 'dict'>
```

Thus we see that the arguments, in this case, are passed as a [dictionary](https://ireadblog.com/posts/127/everything-you-need-to-know-about-python-dictionaries) and these arguments make a dictionary inside the function with name same as the parameter excluding **`**`**.

Now, let's complete the `**total_fruits()**` function to return the total number of fruit.

```python
def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total


print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))
```

Output:

```bash
20
30
12
```

Note that the name of the argument need not necessarily be `**kwargs**` – again, it can be anything. In this case, it's `**fruits**`. But it's generally a standard way to use `****kwargs**` as the name.

## Conclusion

In this article, we learned about two special keywords in Python – **`*args`** and `****kwargs**`. These make a Python function flexible so it can accept a variable number of arguments and keyword arguments, respectively.

Thanks for reading!

You can find the code for this blog [here](https://gist.github.com/ashutoshkrris/fe85f95ced7f0df2488aef122a7e1910).

