---
title: Python map() – List Function with Examples
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-11-09T17:50:02.000Z'
originalURL: https://freecodecamp.org/news/python-map-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-andrew-neel-2859169.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python offers a number of functional programming utilities even though
  it''s primarily an object-oriented programming language. And the most notable one
  is the map() function.

  In this article, we''ll explore what the map() function is and how to use it...'
---

Python offers a number of functional programming utilities even though it's primarily an object-oriented programming language. And the most notable one is the map() function.

In this article, we'll explore what the `map()` function is and how to use it in your code.

# The map() function in Python

The `map()` function (which is a built-in function in Python) is used to apply a function to each item in an *iterable* (like a Python list or dictionary). It returns a new iterable (a *map object)* that you can use in other parts of your code.

The general syntax for this is:

```python
map(function, iterable, [iterable1, iterable2, ...])
```

Let's see an example: imagine you have a list of numbers, and you want to create a new list with the *cubes* of the numbers in the first list. A traditional approach would involve using the *for* loop:

```python
org_list = [1, 2, 3, 4, 5]
fin_list = []

for num in org_list:
    fin_list.append(num**3)

print(fin_list) # [1, 8, 27, 64, 125]
```

which is perfectly valid, but let's see how using the `map()` function simplifies your code:

```python
org_list = [1, 2, 3, 4, 5]

# define a function that returns the cube of `num`
def cube(num):
    return num**3
   
fin_list = list(map(cube, org_list))
print(fin_list) # [1, 8, 27, 64, 125]
```

Don't know about you, but I find this to be much cleaner logic.

> In case you're wondering what went on behind the scenes, the `map()` function essentially iterated through each element of the iterable (in our case, `org_list`) and applied the cube function on it. It finally returned a new iterable (`fin_list` ) with the result.

## How to Use Lambda Expressions in Python

Instead of writing a separate function to calculate the cube of a number, we can use a *lambda* expression in its place. Here's how you'd do that:

```python
fin_list = list(map(lambda x:x**3, org_list))
print(fin_list) # [1, 8, 27, 64, 125]
```

Much cleaner, wouldn't you agree?

## How to Use Built-in Functions in Python

You can also pass in built-in Python functions. For example if you had a list of strings, you can easily create a new list with the length of each string in the list.

```python
org_list = ["Hello", "world", "freecodecamp"]
fin_list = list(map(len, org_list))
print(fin_list) # [5, 5, 12]
```

## How to Use Functions with Multiple Iterables in Python

So far we've passed into `map()` functions that take only one argument (recall the `cube(num)`). But what if your function takes in multiple arguments? An example of this would be the `pow(x, y)` function that takes in 2 arguments (it returns the result of x^y).

To apply a function with multiple arguments, simply pass in another iterable name following the first one.

```python
base = [1, 2, 3, 4]
power = [1, 2, 3, 4]

result = list(map(pow, base, power))
print(result) # [1, 4, 27, 256]
```

# Wrapping Up

In this article, you've learned how to work with the `map()` function in Python. You also saw how it can dramatically reduce the size of your code, making it more readable and bug-free.

You should now be comfortable working with `map()` using built-in functions, lambda expressions, and even your own custom function!

Be sure to [follow me on Twitter](http://twitter.com/jasmcaus) for updates on future articles. Have a nice one!
