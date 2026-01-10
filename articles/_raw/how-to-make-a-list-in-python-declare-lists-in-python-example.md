---
title: How to Make a List in Python – Declare Lists in Python Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-06T21:19:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/kelly-sikkema--1_RZL8BGBM-unsplash--2-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "You can use some of the inbuilt data structures in Python to organize and\
  \ store a collection of variables. \nSome of these data structures include Lists,\
  \ Sets, Tuples, and Dictionaries. Each of them have their own syntax and features.\
  \ \nIn this article..."
---

You can use some of the inbuilt data structures in Python to organize and store a collection of variables. 

Some of these data structures include Lists, Sets, Tuples, and Dictionaries. Each of them have their own syntax and features. 

In this article, we'll focus on Lists. You'll see some of the features of lists in Python, how to create them, and how to add, access, change, and remove items in a list.

## Features of a List in Python

Here are some of the features of a list in Python:

* Items in a list can have **duplicates**. This means that you can add two or more items with the same name.
* Items in a list are **ordered**. They remain in the same order as you create and add items to a list.  
* Items in a list are **changeable**. This means that you can modify the value of an item in a list. You'll see how to do this in the examples in this article.

## How to Create a List in Python

To create a list in Python, we use square brackets (`[]`). Here's what a list looks like:

```txt
ListName = [ListItem, ListItem1, ListItem2, ListItem3, ...]
```

Note that lists can have/store different data types. You can either store a particular data type or mix them. 

In the next section, you'll see how to add items to a list.

## How to Add Items to a List in Python

Before we start adding items to the list, let's create it. This will help you understand the syntax in the last section. 

```python
names = ["Jane", "John", "Jade", "Joe"]


```

In the code above, we created a list called `names` with four items – `Jane`, `John`, `Jade`, and `Joe`. 

We can use two methods to add items to a list – the `append()` and `insert()` method. 

### How to Add Items to a List in Python Using the `append()` Method

Using dot notation, we can attach the `append()` method to a list to add an item to the list. 

The new item to be added will be passed in as a parameter to the `append()` method.

```python
names = ["Jane", "John", "Jade", "Joe"]
names.append("Doe")

print(names)
# ['Jane', 'John', 'Jade', 'Joe', 'Doe']
```

In the code above, we added "Doe" to list using the `append()` method: `names.append("Doe")`.

### How to Add Items to a List in Python Using the `insert()` Method

The `append()` method, seen in the last section, adds an item at the last index of a list. 

When adding items to a list using the `insert()` method, you specify the index where it should be placed. 

Here's an example:

```python
names = ["Jane", "John", "Jade", "Joe"]
names.insert(2, "Doe")

print(names)
# ['Jane', 'John', 'Doe', 'Jade', 'Joe']
```

In our example, we added "Doe" at the second index. Lists are zero-indexed so the first item is 0, the second item is 1, the third item is 2, and so on. 

## How to Access Items in a List in Python

You can access items in a list using the item's index. 

```python
names = ["Jane", "John", "Jade", "Joe"]

print(names[0])
# Jane
```

In the example above, we printed the item with index 0: `print(names[0])`. The item printed out was "Jane" because it is the first item in the list. 

Index 0 = Jane  
Index 1 = John  
Index 2 = Jade  
Index 3 = Joe

Using negative indexing, we can access items starting from the end of the array. Here's an example:

```python
names = ["Jane", "John", "Jade", "Joe"]

print(names[-1])
# Joe
```

Index -1 = Joe  
Index -2 = Jade  
Index -3 = John  
Index -4 = Jane

## How to Change the Value of Items in a Python List

To change the value of an item in a list, you have to make reference to the item's index and then assign a new value to it. 

Here's an example:

```python
names = ["Jane", "John", "Jade", "Joe"]
names[0] = "Doe"

print(names)
# ['Doe', 'John', 'Jade', 'Joe']
```

In the code above, we changed the value of the first item from "Jane" to "Doe" using the item's index: `names[0] = "Doe"`.

## How to Remove Items in a List in Python

We can use the following methods to remove an item from a list:

* The `remove()` method.
* The `pop()` method. 
* The `del` keyword. 

### How to Remove Items in a List in Python Using the `remove()` Method

```python
names = ["Jane", "John", "Jade", "Joe"]

names.remove("John")

print(names)
# ['Jane', 'Jade', 'Joe']
```

As you can see in the example above, we passed in the item to be removed as a parameter in the `remove()` method: `names.remove("John")`.

### How to Remove Items in a List in Python Using the `pop()` Method

```python
names = ["Jane", "John", "Jade", "Joe"]

names.pop()

print(names)
# ['Jane', 'John', 'Jade']
```

The `pop()` method removes the last item in the list. 

You can also specify a particular item to be removed using its index. Here's an example:

```python
names = ["Jane", "John", "Jade", "Joe"]

names.pop(2)

print(names)
# ['Jane', 'John', 'Joe']
```

### How to Remove Items in a List in Python Using the `del` Keyword

```python
names = ["Jane", "John", "Jade", "Joe"]

del names[1]

print(names)
# ['Jane', 'Jade', 'Joe']
```

In the code above, we removed the second item using the `del` keyword by specifying the item's index: `del names[1]`.

If you do not specify any index when using the `del` keyword, the entire list will be deleted. That is:

```python
names = ["Jane", "John", "Jade", "Joe"]

del names

print(names)
# name 'names' is not defined
```

Trying to access a list after deleting it like we did above will throw an error your way saying the list is not defined. 

If you want to empty a list and still have a reference to it without getting an error, then you can use the `clear()` method. Here's an example:

```python
names = ["Jane", "John", "Jade", "Joe"]

names.clear()

print(names)
# []
```

The `clear()` method empties the list. When you try to access the list, you get `[]` returned because all the items have been "cleared".

## Summary

In this article, we talked about lists in Python. 

We saw some of the features of a list in Python and how to create list.

We also saw how to add, access, change, and remove items in a list in Python. 

Happy coding!

