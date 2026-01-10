---
title: Python Iterate Over Dictionary – How to Loop Through a Dict
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-10T21:10:23.000Z'
originalURL: https://freecodecamp.org/news/python-iterate-over-dictionary-how-to-loop-through-a-dict
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Iterate-Over-Dictionary---How-to-Loop-Through-a-Dict-2.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  In this article, we will talk about dictionaries, and also learn how to loop through
  a dictionary in python.

  Python Dictionaries

  In Python, a dictionary is a built-in data structure used to store and organize
  data in key-value pairs...'
---

By Shittu Olumide

In this article, we will talk about dictionaries, and also learn how to loop through a dictionary in python.

## Python Dictionaries

In Python, a dictionary is a built-in data structure used to store and organize data in key-value pairs. 

A dictionary has two parts for each entry: a key and a value. The associated value can be accessed using the key, a special identifier. Any data type, including a number, string, list, or another dictionary, may be used as the value.

Dictionaries can be created by explicitly assigning values to keys or by using the `dict()` constructor function. They are indicated by curly braces `{ }`. Here is an illustration of a basic dictionary:

```py
DemoDict = {'name': 'John', 'age': 25, 'city': 'New Jersey'}

```

In this example, the keys are `'name'`, `'age'`, and `'city'`, and the corresponding values are `'John'`, `25`, and `'New Jersey'`, respectively.

We will now check out the different methods for looping through a dictionary: the `items()` method, the `keys()` method, the `values()` method, and using list comprehension.

## How to Iterate Through a Dict Using the `items()` Method

We can use the `items()` method to loop through a dictionary and get both the key and value pairs.

Let's consider an example:

```py
DemoDict = {'apple': 1, 'banana': 2, 'orange': 3}

# Loop through the dictionary
for key, value in my_dict.items():
    print(key, value)

```

Output:

```bash
apple 1
banana 2
orange 3

```

## How to Iterate Through a Dict Using the `keys()` Method

If we only want to loop through the keys of the dictionary, we can use the `keys()` method.

```py
DemoDict = {'apple': 1, 'banana': 2, 'orange': 3}

# Loop through the keys of the dictionary
for key in my_dict.keys():
    print(key)

```

Output:

```bash
apple
banana
orange

```

## How to Iterate Through a Dict Using the `values()` Method

Similarly, if we only want to loop through the values of the dictionary, we can use the `values()` method.

```py
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# Loop through the values of the dictionary
for value in my_dict.values():
    print(value)

```

Output:

```bash
1
2
3

```

## How to Iterate Through a Dict Using List Comprehension 

Finally, we can also use list comprehension to loop through a dictionary and get both the key and value pairs.

Let's demonstrate this with an example:

```py
my_dict = {'apple': 2, 'banana': 3, 'orange': 4}

# Loop through the dictionary using list comprehension
[(key, value) for key, value in my_dict.items()]

```

Output:

```bash
[('apple', 1), ('banana', 2), ('orange', 3)]

```

**Note**: The output of list comprehension is a list of tuples where each tuple contains a key-value pair of the dictionary.

## Key Differences Between Methods of Looping Through a Dictionary in Python

### Compatibility with different Python versions:

* The `items()` method and `values()` method were introduced in Python 3, so they are not compatible with Python 2. If you need to write code that is compatible with both Python 2 and 3, you should use a basic for loop to iterate through the keys of the dictionary.
* The `keys()` method is compatible with both Python 2 and 3, so it is a good option if you need to write code that works on both versions of Python.

### Performance:

* In general, using a basic for loop to iterate through the keys of a dictionary is the fastest method of looping through a dictionary in Python. This is because it avoids the overhead of creating a list of the dictionary's keys or items.
* The `items()` method is slower than a basic for loop because it creates a new list of tuples that contains the key-value pairs of the dictionary.
* The `values()` method is also slower than a basic for loop because it creates a new list of the values of the dictionary.

### Access to keys, values, or both:

* When using a basic for loop to iterate through a dictionary, you only have access to the keys of the dictionary. To access the corresponding values, you need to use the keys as the index to the dictionary.
* The `items()` method provides a way to access both the keys and values of the dictionary in a single loop. This is convenient when you need to work with both the keys and values of a dictionary.
* The `values()` method, on the other hand, allows you to access only the values of the dictionary. This can be useful when you don't need the keys but just want to work with the values themselves.

## Conclusion

Dictionaries are incredibly useful for storing and retrieving data in a flexible and efficient manner. They are commonly used in Python programming for tasks such as data analysis, web development, and machine learning.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

