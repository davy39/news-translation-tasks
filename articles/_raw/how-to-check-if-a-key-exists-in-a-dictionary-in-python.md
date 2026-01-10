---
title: How to Check if a Key Exists in a Dictionary in Python – Python Dict Has Key
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2023-06-27T16:59:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-key-exists-in-a-dictionary-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/CoverImage-1.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "Python is one of the most popular programming languages today. Its usage\
  \ cuts across multiple fields, but the most common ones are data science, machine\
  \ learning, and web development. \nWhen you're coding in Python, you'll use different\
  \ data structure..."
---

Python is one of the most popular programming languages today. Its usage cuts across multiple fields, but the most common ones are data science, machine learning, and web development. 

When you're coding in Python, you'll use different data structures. In Python, among the most used is the dictionary. 

A dictionary is a collection of key-value pairs that allows you to store and retrieve data. 

When working with dictionaries, it's a common practice to check if a key exists or not. This can be most helpful when you are working with a large dataset and need to access values based on their keys. 

In this article, we are going to explore different ways that we can use to check if a key exists in a dictionary in Python. Let's get started.

## Method 1: Using the `in` Operator
You can use the `in` operator to check if a key exists in a dictionary. It's one of the most straightforward ways of accomplishing the task. When used, it returns either a `True` if present and a `False` if otherwise. 

You can see an example of how to use it below:

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

if 'key1' in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")
```

From the code sample above, we check if `key1` exists in `my_dict`. If it does, then the confirmation message will be displayed. If not, the message indicating the key does not exist gets printed. 

## Method 2: Using the `dict.get()` Method
The `dict.get()` method will return the value associated with a given key if it exists and `None` if the requested key is not found. 

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

if my_dict.get('key1') is not None:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")
```

From the code sample above, we used the `dict.get()` method to get the values associated with `key1`. If the requested key is present, the `my_dict.get('key1') is not None` evaluates to True, meaning the requested key is present.

## Method 3: Using Exception Handling
Exception handling allows you to first try and access the value of the key and handle the `KeyError` exception if it occurs. 

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

try:
    value = my_dict['key1']
    print("Key exists in the dictionary.")
except KeyError:
    print("Key does not exist in the dictionary.")
```

The code sample above allows us to access the value associated with `key1`. If it exists, the code inside `try` executes and the message gets printed. But if the `KeyError` exception occurs, then it means the key does not exist and the code inside the `except` block will be executed. 

### Additional Points
* **Key exists versus value exists**
The methods we have discussed above only check if a key exists. If we were to check if a value is present, we will need to iterate through the values using methods like `dictname.values()`.

* **Performance considerations**
Different methods may have different performance implications depending on the size of your dictionary. Generally the `in` operator is best for small to medium-sized dictionaries while `dict.get()` and exemption handling are a good fit for large dictionaries.

* **Combining methods**
A good thing about working with Python dictionary methods is that you can combine them. For example, you can use the `in` operator to check if a key exists and the `dict.get()` to retrieve its value if it exists.

* **Using `dict.setdefault()`**
It allows you to check if a key exists and returns the value if present. In case the key is missing, then you can set a default value while adding it to the dictionary at the same time.

With an understanding of the above points and good practice using these methods, you should be comfortable working with dictionaries in Python. 


