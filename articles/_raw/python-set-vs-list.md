---
title: Python Set VS List – Sets and Lists in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-05T15:52:53.000Z'
originalURL: https://freecodecamp.org/news/python-set-vs-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/setvlist.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, set and list are both data structures for storing and organizing\
  \ any values. Those values could be numbers, strings, and booleans. \nIn this article,\
  \ we'll look at the differences between set and list. But before that, let's take\
  \ a look at ..."
---

In Python, `set` and `list` are both data structures for storing and organizing any values. Those values could be numbers, strings, and booleans. 

In this article, we'll look at the differences between `set` and `list`. But before that, let's take a look at what both `set` and `list` are.

## What We'll Cover
- [What is a Python `set`?](#heading-what-is-a-python-set)
- [How to Create a Set in Python](#heading-how-to-create-a-set-in-python)
- [What is a Python `list`?](#heading-what-is-a-python-list)
- [How to Create a List in Python](#heading-how-to-create-a-list-in-python)
- [What is the Difference between a Set and a List?](#heading-what-is-the-difference-between-a-set-and-a-list)
- [Conclusion](#heading-conclusion)

## What is a Python `set`?
A `set` is a collection of unordered and unique values. The values in a `set` are unique because there cannot be any duplicates. 

The items in a set are also immutable – you can't change them. But you can still add and remove from the collection.

In short, a `set` stores multiple values in curly braces or inside the `set()` constructor.


### How to Create a Set in Python
To create a set in Python, you can use the `set()` constructor or curly braces.

Set with the `set()` constructor:

```py
country_set = set(("USA", "Ukraine", "Nigeria", "Ghana"))
print(country_set) #{'Ghana', 'USA', 'Ukraine', 'Nigeria'}
```

Notice I used two parentheses to create the list. That's because the `set()` constructor expects one argument. Putting all the values in another set of parentheses makes all the values a single argument.

The set can also contain multiple data types – strings, numbers, or booleans:

```py
multi_set = set(("freeCodeCamp", True, 12))
print(multi_set) #{True, 12, 'freeCodeCamp'}
```

You can also create a set with curly braces like this:

```py
fruit_set = {"Apple", "Avocado", "Mango", "Cashew"}
print(fruit_set) #{'Mango', 'Apple', 'Avocado', 'Cashew'}
```

And you can include multiple data types in a set created with curly braces:

```py
random_set = {True, "Laptop", "Phone", 5}
print(random_set) #{True, 'Laptop', 5, 'Phone'}
```


## What is a Python `list`?
A list is a variable for storing multiple values in Python. It's one of the built-in data structures in Python along with sets, tuples, and dictionaries. If you're familiar with JavaScript, a Python list is like a JavaScript array.

### How to Create a List in Python
You can create a Python list with the `list()` constructor or square brackets:

```py
# List with list() constructor
rand_list = list(("Rice", "Salad", "Eba", 4, True))
print(rand_list) # ['Rice', 'Salad', 'Eba', 4, True]

# List with square brackets
another_rand_list = ["Pele", 1, True]
print(another_rand_list) # ['Pele', 1, True]
```

## What is the Difference between a Set and a List?

| **Basis** | **Set** | **List** |
| ----------- | ----------- | ----------|
|**Creation**| You create a `set` with the `set()` constructor or curly braces. | You create a `list` with the `list()` constructor or square brackets. |
| **Duplicate**| A set cannot have duplicate values. All values must be unique.| A list can have duplicate values. |
| **Order**| A set is unordered. When you print the items in a list, they don't come in the order you arranged them. | A list is ordered. When printed, the items in the list are returned in the same order put in. |
| **Mutation**| You can't change the items of a set, but you can add to the set and remove from it. | You can change the items in a list and you can add to the list.|


## Conclusion
Sets and lists are built-in data structures you can use to store and arrange values in Python. 

If you're wondering which to use, it depends on the use case. If you don’t want the values in the data to change, you can use a set. But if you want the items to change, you can use a list. You can also take into account whether the order of the items matters to you or not.

That's why this article took you through what `set` and `list` are, how to create them, and most importantly the differences between the two of them.

Thanks for reading.



