---
title: Python Dictionary Methods – Dictionaries in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-28T15:32:21.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/python_dict.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, a dictionary is one of the core data structures. It is a sequence\
  \ of key-value pairs separated by commas and surrounded by curly braces. \n\nIf\
  \ you’re familiar with JavaScript, Python dictionaries are like JavaScript objects.\n\
  Python provides..."
---

In Python, a dictionary is one of the core data structures. It is a sequence of key-value pairs separated by commas and surrounded by curly braces. 

![keyvalue](https://www.freecodecamp.org/news/content/images/2022/07/keyvalue.png)

If you’re familiar with JavaScript, Python dictionaries are like JavaScript objects.

Python provides more than 10 methods for working with dictionaries.

In this article, I will show you how to create a dictionary in Python and work with it using those methods.

## What We'll Cover
- [How to Create a Dictionary in Python](#how-to-create-a-dictionary-in-Python)
- [Methods for Working with Python Dictionaries](#methods-forworking-with-python-dictionaries)
  - [How to Use the `get()` Dictionary Method](#how-to-use-the-get-dictionary-method)
  - [How to Use the `items()` Dictionary Method](#how-to-use-the-items-dictionary-method)
  - [How to Use the `keys()` Dictionary Method](#how-to-use-the-keys-dictionary-method)
  - [How to Use the `values()` Dictionary Method](#how-to-use-the-values-dictionary-method)
  - [How to Use the `pop()` Dictionary Method](#how-to-use-the-pop-dictionary-method)
  - [How to Use the `popitem()` Dictionary Method](#how-to-use-the-popitem-dictionary-method)
  - [How to Use the `update()` Dictionary Method](#how-to-use-the-update-dictionary-method)
  - [How to Use the `copy()` Dictionary Method](#how-to-use-the-copy-dictionary-method)
  - [How to Use the `clear()` Dictionary Method](#how-to-use-the-clear-dictionary-method)
- [Conclusion](#heading-conclusion)


## How to Create a Dictionary in Python
To create a dictionary, you open up a curly brace and put the data in a key-value pair separated by commas.

The basic syntax of a dictionary looks like this:
```py
demo_dict = {
"key1": "value1",
"key2": "value2", 
"key3": "value3"
}
```

Note that the values can be of any data type and can be duplicated, but the key must not be duplicated. If the keys are duplicated, you will get an invalid syntax error.
 

## Methods for Working with Python Dictionaries
I will be working with the dictionary below to show you how the dictionary methods work:
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}
```
### How to Use the `get()` Dictionary Method
The get method returns the value of a specified key. 

In the code below, I was able to get the founder of freeCodeCamp by passing the `founder` key inside the `get()` method:
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

founder = first_dict.get("founder")
print(founder)

# Output: Quincy Larson
```

### How to Use the `items()` Dictionary Method

The `items()` method returns all the entries of the dictionary in a list. In the list is a tuple representing each of the items.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

items = first_dict.items()
print(items)

# Output: dict_items([('name', 'freeCodeCamp'), ('founder', 'Quincy Larson'), ('type', 'charity'), ('age', 8), ('price', 'free'), ('work-style', 'remote')])
```

### How to Use the `keys()` Dictionary Method

The `keys()` returns all the keys in the dictionary. It returns the keys in a tuple – another Python data structure.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

dict_keys = first_dict.keys()
print(dict_keys)

# Output: dict_keys(['name', 'founder', 'type', 'age', 'price', 'work-style'])
```

### How to Use the `values()` Dictionary Method

The values method accesses all the values in a dictionary. Like the `keys()` method, it returns the values in a tuple.

```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

dict_values = first_dict.values()
print(dict_values)

# Output: dict_values(['freeCodeCamp', 'Quincy Larson', 'charity', 8, 'free', 'remote'])
```

### How to Use the `pop()` Dictionary Method

The `pop()` method removes a key-value pair from the dictionary. To make it work, you need to specify the key inside its parentheses. 
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.pop("work-style")
print(first_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free'}
```
You can see the `work-style` key and its value have been removed from the dictionary.

### How to Use the `popitem()` Dictionary Method

The `popitem()` method works like the `pop()` method. The difference is that it removes the last item in the dictionary.

```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.popitem()
print(first_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free'}
```

You can see that the last key-value pair ("work-style": "remote") has been removed from the dictionary.

### How to Use the `update()` Dictionary Method

The `update()` method adds an item to the dictionary. You have to specify both the key and value inside its braces and surround it with curly braces.

```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.update({"Editor": "Abbey Rennemeyer"})
print(first_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free', 'work-style': 'remote', 'Editor': 'Abbey Rennemeyer'}
```
The new entry has been added to the dictionary.


### How to Use the `copy()` Dictionary Method

The `copy()` method does what its name implies – it copies the dictionary into the variable specified.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

second_dict = first_dict.copy()
print(second_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free', 'work-style': 'remote'}
```

### How to Use the `clear()` Dictionary Method

The clear method removes all the entries in the dictionary.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.clear()
print(first_dict)

# Output: {}
```

## Conclusion  

In this article, you learned how to create a Python dictionary and how to work with it using the built-in methods provided by Python.

If you find the article helpful, don’t hesitate to share it with friends and family.

Keep coding :)


