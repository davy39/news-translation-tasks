---
title: List indexOf for Python? How to Get the Index of an Item in a List with .index()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-12T17:51:33.000Z'
originalURL: https://freecodecamp.org/news/list-indexof-for-python-how-to-get-the-index-of-an-item-in-a-list-with-index
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/kelly-sikkema-377gw1wN0Ic-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "There are various techniques that we can use to get the index of a list\
  \ item in Python, such as the enumerate() function, a for loop, and the index()\
  \ method. \nIn this article, we'll focus on how to get the index of an item in a\
  \ list using the index()..."
---

There are various techniques that we can use to get the index of a list item in Python, such as the `enumerate()` function, a `for` loop, and the `index()` method. 

In this article, we'll focus on how to get the index of an item in a list using the `index()` method.

We'll start by looking at the syntax of the `index()` method, and then see some examples to help you understand how to use it in your code.

## What Is the Syntax of the `index()` Method in Python?

The `index()` method takes in the item whose index is to be returned as a parameter. But that isn't the only parameter you can use in the `index()` method. 

Here's what the syntax looks like:

```txt
list.index(item, start, end)
```

Here's a breakdown of the parameters above:

* `item` denotes the item whose index is to be searched for.
* `start`, which is an optional parameter, denotes the starting point where an item search is to begin. This is useful when you have an item with duplicates. 
* `end` denotes the index where the search for an item's index should stop/end. This parameter is also optional. 

## How to Get the Index of an Item in a List With `.index()`

In this section, you'll see how to use the `index()` method to get the index of an item in a list. You'll also see how to use all the parameters. 

Here's the first example:

```python
listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara']

print(listOfNames.index('Jane'))
# 1
```

In the code above, we created a list of names: `listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara']`.

Using the `index()` method, we got the index of "Jane" in the list: `listOfNames.index('Jane')`

When printed to the console, 1 was printed out. 

In case you don't understand why 1 was returned, then note that lists are zero-indexed – so the first item is 0, the second is 1 and so on. That is:

'John' => index 0  
'Jane' => index 1  
'Doe' => index 2  
'Ihechikara' => index 3

### How to Use the `start` and `end` Parameters with the `index()` Method in Python

In this section, you'll see how to use the `start` and `end` parameters with the `index()` method.

```python
listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara', 'John', 'Jane', 'Doe', 'Ihechikara']

print(listOfNames.index('Jane', 2))
# 5
```

In the list above, we have names with duplicate values: `['John', 'Jane', 'Doe', 'Ihechikara', 'John', 'Jane', 'Doe', 'Ihechikara']`.

But we want to get the index of the second "Jane" item. Knowing that the index of the first "Jane" item is 1, we can start the search after that item. 

So to start the search from an index after the first "Jane" item, we added another parameter to the `index()` method: `listOfNames.index("Jane", 2)`. Now the search for the index of an item with a value of "Jane" will start from index 2. 

We got 5 returned because that is the index of the second "Jane" item. Without specifying an index to start from, the `index()` method will return the first index of a specified item.

Here's a second example for you to understand how to use the `end()` parameter:

```python
listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara', 'John', 'Jane', 'Doe', 'Ihechikara']

print(listOfNames.index("Jane", 2,4))
# ValueError: 'Jane' is not in list
```

In the example above, we specified index 2 as the `start` index and index 4 as the `end` index. We are searching for the index of "Jane" within the specified range (index 2 and 4). 

We got an error returned: `ValueError: 'Jane' is not in list`. This is because "Jane" is not within the specified range. 

Recall that we started from index 2, so:

Index 2 (`start` index) => 'Doe'  
Index 3 => 'Ihechikara'  
Index 4 (`end` index) => 'John'

From the indexes above, you can see that "Jane" does not exist within the range so an error was returned. 

You get a ValueError in a list when:

* The item being searched for doesn't exist in the list. 
* The item being searched for doesn't fall within a specified search (start and end) range.

## Summary

In this article, we talked about the `index()` method in Python. You use it to find the index of an item in a list.

We saw some examples that showed how to use the `index()` method and its `start` and `end` parameters. 

Happy coding!

