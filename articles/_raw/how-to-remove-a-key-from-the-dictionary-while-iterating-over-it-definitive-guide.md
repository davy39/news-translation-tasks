---
title: How to Remove a Key from a Dictionary While Iterating Over it
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2022-07-06T21:56:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-key-from-the-dictionary-while-iterating-over-it-definitive-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Freecodecamp_dictionary_delete_iterate.jpeg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python dictionaries allow you to store values in a Key and Value format.

  You can access the values using the key. You can also iterate through the complete
  dictionary to access every element.

  Sometimes while iterating through the dictionary, you may ...'
---

Python dictionaries allow you to store values in a `Key` and `Value` format.

You can access the values using the key. You can also iterate through the complete dictionary to access every element.

Sometimes while iterating through the dictionary, you may need to remove a key from the dictionary.

This tutorial will teach you how to remove a key from a dictionary **while iterating over it**.

To remove a key directly without iterating, read the freeCodeCamp tutorial [How to Remove a key from a Python Dictionary](https://www.freecodecamp.org/news/how-to-remove-a-key-from-a-python-dictionary-delete-key-from-dict/).

## How to Create a Dictionary

Let's first create a dictionary with some key-value pairs using the assignment operator.

To add a key to the dictionary using different methods, read [How to Add a Key to a Dictionary](https://www.stackvidhya.com/python-add-key-to-dictionary/)

After creating the dictionary, you can use the `for` loop to iterate through it and print the values to check if the dictionary has been created successfully.

**Here's the code:**

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for key in yourdict.keys():
    print(key, yourdict[key])

```

You can print the values in the dictionary as follows.

**Output:**

```
    one 1
    two 2
    three 3
    four 4

```

To check if a key exists in a dictionary without iterating over it, read [how to check if a key exists in dictionary in Python](https://www.stackvidhya.com/check-if-key-exists-in-dictionary-python/).

## How to Check the Python Version

Python 2 and Python 3 work _differently_ when you try to delete a key from a dictionary while iterating.

To check which version of Python you are using, use the below code snippet.

**Here's the code:**

```python
import sys
print(sys.version)

```

**Output:**

```
3.8.2 (default, Sep  4 2020, 00:03:40) [MSC v.1916 32 bit (Intel)]

```

You'll see whatever version you have. And now you know which version of Python you are using.

You can follow the appropriate methods explained below.

## How to Delete A Key from a Dict Based on Key Value – Python 3

This section teaches you how to delete a key from a dictionary using Python 3.

You need to convert the `keys` to a `list` using the `list(dict.keys())` and [iterate through a dictionary](https://www.stackvidhya.com/iterate-through-dictionary-python/) using the `for` loop.  

While converting the `keys` to a `list`, Python 3 creates a _new copy_ of the keys in the list. There will be no reference to the dictionary during the iteration.

If you do not convert it into a list, then the [keys](https://docs.python.org/3/library/stdtypes.html#dict.keys) method just returns a new view of the keys with reference to the currently iterated dictionary.

Now, during each iteration of the list of keys, you can check if the `key` is _equal to the item_ you need to _delete._ If it is `True`, you can delete the `key` using the `del` statement.

**Here's the code:**

The below code demonstrates how to remove a key from the dictionary while iterating over it using Python 3.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for k in list(yourdict.keys()):
    if k == "four":
        del yourdict[k]

yourdict

```

As you can see in the code below, the key _four_ gets deleted from the dictionary while iterating through it.

**Output:**

```
    {'one': 1, 'two': 2, 'three': 3}

```

If you use the `dict.keys()` method to iterate and issue a `del` statement, you’ll see the below error in Python 3.

```python
RuntimeError: dictionary changed size during iteration

```

## How to Delete a Key from a Dict Based on Values – Python 3

This section teaches you how to remove a key from a dictionary based on the value of the key while iterating over the dictionary.

First, you need to convert the dictionary keys to a `list` using the `list(dict.keys())` method.

During each iteration, you can check if the _value of a key_ is equal to the desired value. If it is `True`, you can issue the `del` statement to delete the key.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for k in list(yourdict.keys()):
    if yourdict [k] == 4:
        del yourdict[k]

print(yourdict)

```

The key _four_ gets deleted based on its value _4_.

**Output:**

```python
{‘three’: 3, 'two': 2, 'one': 1}

```

## How to Delete a Key from a Dict Based on the Key – Python 2

This section teaches you how to remove a key from a dictionary while iterating over it using Python 2.

You can directly [iterate through a dictionary](https://www.stackvidhya.com/iterate-through-dictionary-python/) using the `dict.keys()` method. In Python 2, the `dict.keys()` method creates a copy of the keys and iterates over the `copy` instead of iterating through the keys directly. So there will be _no reference_ to the dictionary directly while iterating.

Now during each iteration, you can check if the item is _equal to the key_ you want to delete. And if it is equal, you can issue the `del` statement. It’ll remove the key from the dictionary.

**Here's the code:**

The below code demonstrates how to remove a key from dictionary while iterating over it using Python 2.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for k in yourdict.keys():
    if k == "four":
        del yourdict[k]

yourdict

```

The key _four_ gets deleted, and only the other items are available in the dictionary.

**Output:**

```
    {'one': 1, 'two': 2, 'three': 3}

```

This is how you can remove a key based on the key.

## How to Delete a Key in a Dict Based on Values – Python 2

This section teaches you how to remove a key from a dictionary based on the value of the key while iterating over the dictionary.

Iterate over the dictionary using the `dict.items()` method. It’ll return the key-value pair during each iteration.

Then you can check if the `value` of the current iteration _equals your desired value_ to be removed. Then issue the `del` statement to remove the key from the dictionary.

```python
yourdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for key, val in yourdict.items():
    if val == 3:
        del yourdict[key]

print(yourdict)

```

The key _three_ gets deleted based on its value _3_. All other items are available in the dictionary.

**Output:**

```python
{'four': 4, 'two': 2, 'one': 1}

```

## Why Do Python 3 and Python 2 Work Differently?

When using the `dict.keys()` method, Python 3 returns a _view_ of the keys. This means there is a reference to the dictionary while iterating over it. 

On the other hand, Python 2 returns a _copy_ of the keys, meaning there is NO dictionary reference while iterating it. This means that deletion will be successful without problems.

## Conclusion

In this article, you’ve learned how to remove a key from a dictionary while iterating over it in different versions of Python – Python 2 and Python 3.

You’ve also learned how to delete a key based on a key or the value of a key.

If you liked this article, feel free to share it.

You can check out my other [Python tutorials here](https://www.stackvidhya.com).

