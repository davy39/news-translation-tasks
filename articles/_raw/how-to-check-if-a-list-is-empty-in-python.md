---
title: Python isEmpty() equivalent – How to Check if a List is Empty in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-19T04:52:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-list-is-empty-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/kelly-sikkema--1_RZL8BGBM-unsplash--1-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "A list is one of the data structures in Python that you can use to store\
  \ a collection of variables. \nIn some cases, you have to iterate through and perform\
  \ an operation on the elements of a list. But you can't loop/iterate through a list\
  \ if it has no..."
---

A [list](https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/) is one of the data structures in Python that you can use to store a collection of variables. 

In some cases, you have to iterate through and perform an operation on the elements of a list. But you can't loop/iterate through a list if it has no elements in it. 

In this article, you'll learn how to check if a list is empty by: 

* Using the `not` operator. 
* Using the `len()` function. 
* Comparing the list to an empty list.

## How To Check if a List Is Empty in Python Using the `not` Operator

The `not` operator in Python is used for logical negation. Here's an example:

```python
x = True
y = False

print(not x)  # Output: False
print(not y)  # Output: True

```

`not` returns true when an operand is false, and false if an operand is true. 

You can check if a collection is empty using the logic above. Here's how:

```python
people_list = [] 

if not people_list:
    print("Your list is empty")
else:
    print("Your list is not empty")
    
# Your list is empty
```

In the code above, we used an `if` statement and the `not` operator to check if the `people_list` was empty. 

## How To Check if a List Is Empty in Python Using the `len()` Function

You can use the `len()` function in Python to return the number of elements in a data structure. 

Here's an example: 

```python
people_list = ["John", "Jane", "Jade", "Doe"] 

print(len(people_list))
# 4
```

Using the `len()` function, we printed the length of the `people_list` list which had four elements. 

You can also get the length of an empty list:

```python
people_list = [] 

print(len(people_list))
# 0
```

Now that we know that the length of an empty list is 0, we use it to check if a list is empty:

```python
people_list = [] 

if len(people_list) == 0:
    print("Your list is empty")
else:
    print("Your list is not empty")

# Your list is empty
```

## How To Check if a List Is Empty in Python By Comparing To an Empty List

An interesting way to check if a list is empty is by comparing it to another empty list. That is:

```python
people_list = [] 

if people_list == []:
    print("Your list is empty")
else:
    print("Your list is not empty")

# Your list is empty
```

In the example above, we compared the `people_list` list to an empty list: `if people_list == []`

You can play around with the code by adding elements to the list to see which `if...else` statement gets executed. 

## Summary

In this article, we saw how to check if a list is empty in Python by using three different methods. 

We saw how to check if a list is empty by using the `not` operator, and the `len()` function. 

We also saw how check if a list is empty by comparing it to an empty list. 

Happy coding!

