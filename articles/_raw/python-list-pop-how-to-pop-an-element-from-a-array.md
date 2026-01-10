---
title: Python list.pop() – How to Pop an Element from a Array
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-09T01:31:22.000Z'
originalURL: https://freecodecamp.org/news/python-list-pop-how-to-pop-an-element-from-a-array
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/kelly-sikkema--1_RZL8BGBM-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Python has various built-in methods you can use to interact with elements\
  \ stored in a list. These methods let you add, access, modify, and remove elements.\
  \ \nIn this article, you'll learn how to remove elements in a Python list using:\n\
  \nThe pop() metho..."
---

Python has various built-in methods you can use to interact with elements stored in a [list](https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/). These methods let you add, access, modify, and remove elements. 

In this article, you'll learn how to remove elements in a Python list using:

* The `pop()` method.
* The `remove()` method.
* The `del` keyword. 

## How to Pop an Element From a Python List Using the `pop()` Method

You can use the `pop()` method to either remove a specific element in a list or to remove the last element. 

When a parameter is used, you can specify the particular element (using the element's index number) to be removed. Without a parameter, the last element is removed. 

Here are some examples: 

### `pop()` Example #1

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

names.pop(2)

print(names)
# ['Ihechikara', 'Doe', 'Jane']
```

In the example above, we created a list called `names` with four elements: `['Ihechikara', 'Doe', 'John', 'Jane']`. 

Using the `pop()` method, we specified that the element at index 2 should be removed: `names.pop(2)`. 

The resulting list had three elements: `['Ihechikara', 'Doe', 'Jane']`

### `pop()` Example #2

In the next example, we'll use the `pop()` method without any parameter or specifying a particular element to be removed. 

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

names.pop()

print(names)
# ['Ihechikara', 'Doe', 'John']
```

Without passing the index of an element as a parameter to the `pop()` method in the list above, the last element in the list was removed. 

That is: `names.pop()`. 

## How to Remove an Element From a Python List Using the `remove()` Method

With the `remove()` method, you can pass in one parameter — the value of the element to be removed. 

You can't use the index of elements as a parameter, and you can't use the `remove()` method without a parameter. These will result in an error. 

Here's an example:

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

names.remove("Doe")

print(names)
# ['Ihechikara', 'John', 'Jane']
```

In the list above, we specified the element to be removed using its value: `names.remove("Doe")`. So the element with a value of "Doe" was removed from the list. 

An error would have been raised if we had used the index of the element — `names.remove(1)` — or used the method without a parameter — `names.remove()`.

Similarly, removing an element that doesn't exist would raise an error. 

## How to Delete an Element From a Python List Using the `del` Keyword

With the `del` keyword, you can specify which element you want to remove using its index. You can also specify a range of elements to be removed. 

Here are some examples:

### `del` Example #1

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

del names[2]

print(names)
# ['Ihechikara', 'Doe', 'Jane']
```

In the code above, we deleted the element at index 2: `del names[2]`. 

Note that the index is not specified within parenthesis but in square brackets

### `del` Example #2

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

del names[0:2]

print(names)
# ['John', 'Jane']
```

In the code above, we specified a range for the numbers to be deleted: `del names[0:2]`

With that, we're saying, "delete all the elements from index 0 and stop just before index 2". Index 2 will not be deleted – it is used as a point where the deletion will come to a halt. 

## Summary

In this article, we talked about lists in Python. 

We saw the different methods that you can use to pop/delete/remove elements in a list. 

Using code examples, we saw practical applications of each method.

Happy coding!

