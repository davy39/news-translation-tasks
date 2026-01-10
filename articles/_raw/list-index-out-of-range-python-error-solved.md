---
title: List Index Out of Range – Python Error [Solved]
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-03T22:13:38.000Z'
originalURL: https://freecodecamp.org/news/list-index-out-of-range-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/kelly-sikkema--1_RZL8BGBM-unsplash--3-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, we'll talk about the IndexError: list index out of range\
  \ error in Python. \nIn each section of the article, I'll highlight a possible cause\
  \ for the error and how to fix it.\nYou may get the IndexError: list index out of\
  \ range error for..."
---

In this article, we'll talk about the `IndexError: list index out of range` error in Python. 

In each section of the article, I'll highlight a possible cause for the error and how to fix it.

You may get the `IndexError: list index out of range` error for the following reasons:

* Trying to access an index that doesn't exist in a list. 
* Using invalid indexes in your loops.
* Specifying a range that exceeds the indexes in a list when using the `range()` function. 

Before we proceed to fixing the error, let's discuss how indexing work in Python lists. You can skip the next section if you already know how indexing works.

## How Does Indexing Work in Python Lists?

Each item in a Python list can be assessed using its index number. The first item in a list has an index of zero. 

Consider the list below:

```python
languages = ['Python', 'JavaScript', 'Java']

print(languages[1])
# JavaScript
```

In the example above, we have a list called `languages`. The list has three items — 'Python', 'JavaScript', and 'Java'. 

To access the second item, we used its index: `languages[1]`. This printed out `JavaScript`. 

Some beginners might misunderstand this. They may assume that since the index is 1, it should be the first item. 

To make it easier to understand, here's a breakdown of the items in the list according to their indexes: 

Python (item 1) => Index 0  
JavaScript (item 2) => Index 1  
Java (item 3) => Index 2

As you can see above, the first item has an index of 0 (because Python is "zero-indexed"). To access items in a list, you make use of their indexes. 

## What Will Happen If You Try to Use an Index That Is Out of Range in a Python List?

If you try to access an item in a list using an index that is out of range, you'll get the `IndexError: list index out of range` error. 

Here's an example:

```python
languages = ['Python', 'JavaScript', 'Java']

print(languages[3])
# IndexError: list index out of range
```

In the example above, we tried to access a fourth item using its index: `languages[3]`. We got the `IndexError: list index out of range` error because the list has no fourth item – it has only three items. 

The easy fix is to always use an index that exists in a list when trying to access items in the list. 

## How to Fix the `IndexError: list index out of range` Error in Python Loops

Loops work with conditions. So, until a certain condition is met, they'll keep running. 

In the example below, we'll try to print all the items in a list using a `while` loop. 

```python
languages = ['Python', 'JavaScript', 'Java']

i = 0

while i <= len(languages):
    print(languages[i])
    i += 1

# IndexError: list index out of range
```

The code above returns the  `IndexError: list index out of range` error. Let's break down the code to understand why this happened. 

First, we initialized a variable `i` and gave it a value of 0: `i = 0`. 

We then gave a condition for a `while` loop (this is what causes the error):  `while i <= len(languages)`.

From the condition given, we're saying, "this loop should keep running as long as `i` is **less than** or **equal to** the **length** of the `language` list". 

The `len()` function returns the length of the list. In our case, 3 will be returned. So the condition will be this: `while i <= 3`. The loop will stop when `i` is equal to 3.

Let's pretend to be the Python compiler. Here's what happens as the loop runs.

Here's the list: `languages = ['Python', 'JavaScript', 'Java']`. It has three indexes — 0, 1, and 2.

When `i` is 0 => Python

When `i` is 1 => JavaScript

When `i` is 2 => Java

When `i` is 3 => Index not found in the list. `IndexError: list index out of range` error thrown.

So the error is thrown when `i` is equal to 3 because there is no item with an index of 3 in the list.

To fix this problem, we can modify the condition of the loop by removing the equal to sign. This will stop the loop once it gets to the last index. 

Here's how:

```python 
languages = ['Python', 'JavaScript', 'Java']

i = 0

while i < len(languages):
    print(languages[i])
    i += 1
    
    # Python
    # JavaScript
    # Java

```

The condition now looks like this: `while i < 3`.

The loop will stop at 2 because the condition doesn't allow it to equate to the value returned by the `len()` function. 

## How to Fix the `IndexError: list index out of range` Error in When Using the `range()` Function in Python

By default, the `range()` function returns a "range" of specified numbers starting from zero. 

Here's an example of the `range()` function in use:

```python
for num in range(5):
  print(num)
    # 0
    # 1
    # 2
    # 3
    # 4
```

As you can see in the example above, `range(5)` returns 0, 1, 2, 3, 4. 

You can use the `range()` function with a loop to print the items in a list. 

The first example will show a code block that throws the  `IndexError: list index out of range` error. After pointing out why the error occurred, we'll fix it. 

```python
languages = ['Python', 'JavaScript', 'Java']


for language in range(4):
  print(languages[language])
    # Python
    # JavaScript
    # Java
    # Traceback (most recent call last):
    #   File "<string>", line 5, in <module>
    # IndexError: list index out of range
```

The example above prints all the items in the list along with the `IndexError: list index out of range` error. 

We got the error because `range(4)` returns 0, 1, 2, 3. Our list has no index with the value of 3. 

To fix this, you can modify the parameter in the `range()` function. A better solution is to use the length of the list as the `range()` function's parameter. 

That is:

```python
languages = ['Python', 'JavaScript', 'Java']


for language in range(len(languages)):
  print(languages[language])
    # Python
    # JavaScript
    # Java
```

The code above runs without any error because the `len()` function returns 3. Using that with `range(3)` returns 0, 1, 2 which matches the number of items in a list.

## Summary

In this article, we talked about the  `IndexError: list index out of range` error in Python. 

This error generally occurs when we try to access an item in a list by using an index that doesn't exist within the list. 

We saw some examples that showed how we may get the error when working with loops, the `len()` function, and the `range()` function. 

We also saw how to fix the `IndexError: list index out of range` error for each case. 

Happy coding!

