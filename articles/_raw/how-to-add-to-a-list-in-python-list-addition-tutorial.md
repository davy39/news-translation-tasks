---
title: How to Add to a List in Python – List Addition Tutorial
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-19T17:51:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-to-a-list-in-python-list-addition-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-ono-kosuki-5999834.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'A list is a mutable sequence of elements surrounded by square brackets.
  If you’re familiar with JavaScript, a Python list is like a JavaScript array. It''s
  one of the built-in data structures in Python. The others are tuple, dictionary,
  and set.

  A lis...'
---

A list is a mutable sequence of elements surrounded by square brackets. If you’re familiar with JavaScript, a Python list is like a JavaScript array. It's one of the built-in data structures in Python. The others are tuple, dictionary, and set.

A list can contain any data type such as an integer, float, string, and boolean:

```py
num_list = [1, 2, 3, 10]

float_list = [2.9, 3.9, 4.6]

boo_list = [True, False]

string_list = ['JavaScript', 'Python', 'freeCodeCamp']
```

It can also contain a mixture of those data types:

```py
mixed_list = ['freeCodeCamp', 1, 1.1, True]
```

Since lists are mutable, you can add items to them or remove items from them. This article will show you how to add to a list.

## What We'll Cover
- [How to Add to a List in Python](#heading-how-to-add-to-a-list-in-python)
  - [How to Add to a List with the `append()` Method](#heading-how-to-add-to-a-list-with-the-append-method)
  - [How to Add to a List with the `insert()` Method](#heading-how-to-add-to-a-list-with-the-insert-method)
  - [How to Add to a List with the `extend()` Method](#heading-how-to-add-to-a-list-with-the-extend-method)
  - [How to Add a Dictionary to a List with the `append()` Method](#heading-how-to-add-a-dictionary-to-a-list-with-the-append-method)
- [Conclusion](#heading-conclusion)


## How to Add to a List in Python
Python provides 3 methods with which you can add to a list. Those methods are `append()`, `extend()`, and `insert()`.


### How to Add to a List with the `append()` Method

The `append()` element adds to the end of a list. 

Provided we have the following list:

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
```

If I want to add “Cricket” to the end of that list, I can do it with the `append()` method this way:

```py
sports_list.append("Cricket")
```

Printing `sports_list` to the console results in this:

```py
['Football', 'Basketball', 'Baseball', 'Tennis', 'Cricket']
```

You can see `Cricket` was added to the last index in the list.

You can also prompt the user to add to the list this way: 

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
new_sport = input("Please add a new sport: ")
sports_list.append(new_sport)

print(sports_list)
```

### How to Add to a List with the `insert()` Method

The `append()` method helps you add to the end of a list, but if you want to add to any index you want, you can use the `insert()` method. 

To use the `insert()` method for adding to a list, you need to specify the index, then the item you want to add:

```py
insert(index, item)
```

I have added `Athletics` to the first index (0) of the `sports_list` this way:

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_list.insert(0, "Athletics")
print(sports_list)

# Output: ['Athletics', 'Football', 'Basketball', 'Baseball', 'Tennis']
```

I also added `Wrestling` to index 2 (the 3rd index) this way:

```py
sports_list.insert(2, "Wrestling")
print(sports_list)

# Output: ['Athletics', 'Football', 'Wrestling', 'Basketball', 'Baseball', 'Tennis']
```

### How to Add to a List with the `extend()` Method

The `extend()` method adds an iterable data item to a list or adds one list to another list. So, with it, you can add a tuple, set, or dictionary to a list.  

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]

# add another list
sports_list.extend(["Golf", "Boxing"])

# Append a tuple
sports_list.extend(("Netball", "TT"))

print(sports_list)

# Output: ['Football', 'Basketball', 'Baseball', 'Tennis', 'Golf', 'Boxing', 'Netball', ‘TT']
```

### How to Add a Dictionary to a List with the `append()` Method

If you try to add a dictionary to a list with the `extend()` method, you only get the keys and not the values:

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_dict = {1: "Netball", 2: "Chess"}

sports_list.extend(sports_dict)
print(sports_list)
# Output:  ['Football', 'Basketball', 'Baseball', 'Tennis', 1, 2]
```

You can loop through the dictionary and then use the append method to add it to the list. This will give you the dictionary’s keys and values as a set of tuples in the list:

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_dict = {1: "Netball", 2: "Chess"}

for k, v in sports_dict.items():
    sports_list.append((k, v))

print(sports_list)

# Output: ['Football', 'Basketball', 'Baseball', 'Tennis', (1, 'Netball'), (2, 'Chess')]
```

If you want the dictionary as it is right inside the list, you can just use the append method without a loop:

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_dict = {1: "Netball", 2: "Chess"}

sports_list.append(sports_dict)
print(sports_list)

# Output: ['Football', 'Basketball', 'Baseball', 'Tennis', {1: 'Netball', 2: 'Chess'}]
```


## Conclusion
In this article, we looked at how to use the `append()`, `insert()`, and `extend()` methods to add to a list in Python. 

What you add to a list does not have to be a single element. That’s why I showed you how to use the `extend()` method to help you add iterables like lists, tuples, and dictionaries to a list.

Thank you for reading.


