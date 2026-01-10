---
title: Python range() Function Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-17T11:55:33.000Z'
originalURL: https://freecodecamp.org/news/python-range-function-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-christina-morillo-1181671.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn how to use the range() function in Python
  with the help of code examples along the way.

  What is the range() Function in Python? range() Function Syntax Breakdown

  Python''s built-in range() function is mainly used when w...'
---

In this article, you will learn how to use the `range()` function in Python with the help of code examples along the way.


## What is the `range()` Function in Python? `range()` Function Syntax Breakdown
Python's built-in `range()` function is mainly used when working with `for` loops – you can use it to loop through certain blocks of code a specified number of times.

The `range()` function accepts three arguments – one is required, and two are optional.

By default, the syntax for the `range()` function looks similar to the following:

```
range(stop)
```

The `stop` argument is **required**. 

The `range()` function returns a sequence of numbers starting from `0`, incrementing by `1`, and ending at the value you specify as `stop` (non-inclusive). 

But what if you want to iterate through a range of two numbers you specify and don't want to start the counting from `0`?

You can pass a second **optional** start argument, `start`, to specify the starting number. The syntax to do so looks like this:
```
range(start, stop)
```

This syntax generates a sequence of numbers based on the `start` (inclusive) and `stop` (non-inclusive) values that increment by `1`.

Lastly, if you don't want the default increment to be `1`, you can specify a third **optional** argument, `step`. The syntax to do that looks like this:
```
range(start, stop, step)
```

This syntax generates a sequence of numbers that starts counting at `start` (inclusive) and increments according to `step` until it reaches `stop` (non-inclusive).


## How to Use the `range()` Function with Only the `stop` Argument
When using only the `stop` argument with `range()`, the counting starts at `0` and increments by `1`.  The counting stops when you reach the value you specify as `stop`. 

Keep in mind that the `stop` value you specify is not inclusive!

If you specify a `stop` argument of `5`, the range includes the numbers `0 - 4`  and not `0 - 5` – the counting will stop at `4` and not `5`.

Let's take a look at the example below:
```python
for num in range(5):
    print(num)
    
# output 

# 0
# 1
# 2
# 3
# 4
```

In this example, I specified a `range(5)`.

The function started counting from `0`, incremented by `1` on each iteration and ended at `4`.


## How to Use the `range()` Function with the `start` And `stop` Arguments
If you want to have a range of two numbers, you use two arguments – `start` and `stop`. Keep in mind that the `start` value is inclusive, whereas the `stop` value is not.

If you want a range of values from 5 inclusive to 10 inclusive, you write a `range(5,11)` like so:
```python
for num in range(5,11):
  print(num)
  
# output

# 5
# 6
# 7
# 8
# 9
# 10
```

You can pass negative integer values to `range()` as well:
```python
for num in range(-5, 1):
  print(num)

# output

# -5
# -4
# -3
# -2
# -1
# 0
```

Something to note here is that you cannot pass float values to `range()`.

In this example, when I pass two float values as arguments, an error gets raised:
```python
for num in range(5.2, 4.3):
  print(num)

# output

# Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    for num in range(5.2, 4.3):
# TypeError: 'float' object cannot be interpreted as an integer
```
   
You can pass either negative or positive integers as `start` and `stop` arguments.


## How to Use the `range()` Function with the `start`, `stop`, And `step` Arguments
By default, the increment value is `1` and is not specified. That said, you can change it by passing a `step` argument to the `range()` function.

Let's take a look at the following example:
```python
for num in range(10,21,2):
  print(num)
  
# output

# 10
# 12
# 14
# 16
# 18
# 20
```

In the example above, I generated a sequence of numbers from `10` to `20` and incremented the steps by `2`. I achieved this by specifying a step value of `2`.

Something to note is that `step` can be either a negative or positive number, but it cannot be `0`.

Here is how you can generate a range with a negative `step` argument:
```python
for num in range(20, 11, -2):
  print(num)

# output

# 20
# 18
# 16
# 14
# 12
```

The code above generates a sequence of numbers in reverse.

And look at what happens when the `step` is `0`:
```python
for num in range(10, 21 0):
  print(num)

# output

#  File "main.py", line 1
#    for num in range(10, 21 0):
                            ^
# SyntaxError: invalid syntax
```


## How to Create A List of Numbers Using the `range()` Function
You can create a list of numbers by passing the `range()` function as an argument to the `list()` constructor like so:

```python
my_numbers_list = list(range(5))

print(my_numbers_list)

# output

# [0, 1, 2, 3, 4]
```
    
In the example above, I created a list of numbers from `0` to `4`.


## How to use The `len()` Function with `range()` in Python
Say you have a list of items and want to do something to the items depending on how long the list is.

For that, you could use `range()` and pass the length of your list as an argument to the function.

To calculate the length of a list, use the `len()` function.

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]

programming_languages_length = len(programming_languages)

for languages in range(programming_languages_length):
  print("Hello World")
  
# output

# Hello World
# Hello World
# Hello World
# Hello World
```

## Conclusion
And there you have it! You now know how to use the `range()` function in Python.

To learn more about Python, check out freeCodeCamp's [Python for beginners course](https://www.freecodecamp.org/news/python-programming-course/).

Thanks for reading, and happy coding!


