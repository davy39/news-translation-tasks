---
title: How to Merge Dictionaries in Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2021-12-09T17:16:36.000Z'
originalURL: https://freecodecamp.org/news/merge-dictionaries-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Black-Moon-Blog-Banner--1--1.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, a dictionary is a collection you use to store data in {key:value}\
  \ pairs. It is ordered and mutable, and it cannot store duplicate data. \nWe write\
  \ a dictionary using curly brackets like this:\nmy_dict = {\n    \"id\": 1,\n  \
  \  \"name\": \"Ashutosh\",..."
---

In Python, a dictionary is a collection you use to store data in `{key:value}` pairs. It is ordered and mutable, and it cannot store duplicate data. 

We write a dictionary using curly brackets like this:

```python
my_dict = {
    "id": 1,
    "name": "Ashutosh",
    "books": ["Python", "DSA"]
}

```

Sometimes, we need to merge two or more dictionaries to create a bigger dictionary. For example:

```python
dict_one = {
    "id": 1,
    "name": "Ashutosh",
    "books": ["Python", "DSA"]
}

dict_two = {
    "college": "NSEC",
    "city": "Kolkata",
    "country": "India"
}

merged_dict = {
    "id": 1,
    "name": "Ashutosh",
    "books": ["Python", "DSA"],
    "college": "NSEC",
    "city": "Kolkata",
    "country": "India"
}

```

In the `merged_dict` we have the key-value pairs of both `dict_one` and `dict_two`. This is what we wish to achieve programmatically. 

There are various ways we can do this in Python:

1. Using a for loop
2. Using the `dict.update()` method
3. Using the `**` operator
4. Using the `|` (Union) operator (for Python 3.9 and above)

Let's explore each way one after another.

## How to Merge Dictionaries in Python Using a For Loop

We can merge two or more dictionaries using for loop like this:

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"],
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> for key,value in dict_two.items():
...     merged_dict[key] = value
... 
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC'}
>>> for key,value in dict_three.items():
...     merged_dict[key] = value
... 
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

But the problem with this method is that we need to run so many loops to merge the dictionaries. 

So what's another option?

## How to Merge Dictionaries in Python Using the `dict.update()` Method

If you explore the `dict` class, there are various methods inside it. One such method is the `update()` method which you can use to merge one dictionary into another.

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
...     "books": ["Python", "DSA"]
... }
>>> dict_two = {
...     "college": "NSEC",
...     "city": "Kolkata",
...     "country": "India"
... }
>>> dict_one.update(dict_two)
>>> dict_one
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

But the problem when we use the `update()` method is that it modifies one of the dictionaries. If we wish to create a third dictionary without modifying any of the other dictionaries, we cannot use this method. 

Also, you can only use this method to merge two dictionaries at a time. If you wish to merge three dictionaries, you first need to merge the first two, and then merge the third one with the modified dictionary.

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"],
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> dict_one.update(dict_two)
>>> dict_one
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC'}
>>> dict_one.update(dict_three)
>>> dict_one
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

Let's explore some other options.

## How to Merge Dictionaries in Python Using the `**` operator

You can use the double-asterisk (**) method to unpack or expand a dictionary like this: 

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"]
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> merged_dict = {**dict_one, **dict_two, **dict_three} 
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

Using the `**` operator to merge the dictionaries doesn't affect any of the dictionaries.

## How to Merge Dictionaries in Python Using the `|` Operator

Starting with Python 3.9, we can use the Union ( `|` ) operator to merge two or more dictionaries. 

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"],
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> merged_dict = dict_one | dict_two | dict_three
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

This is the most convenient method available for merging dictionaries in Python.

## Conclusion

We have explored several different methods for merging dictionaries. If you have Python 3.9 or above, you should use the `|` operator. But if you use older versions of Python, you can still use the other methods discussed above.

