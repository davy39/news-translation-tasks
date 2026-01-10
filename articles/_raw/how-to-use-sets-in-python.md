---
title: How to Use Sets in Python – Explained with Examples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-03-04T12:54:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sets-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-3-.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: 'In the vast landscape of Python programming, understanding data structures
  is akin to possessing a versatile toolkit. Among the essential tools in this arsenal
  is the Python set. Sets in Python offer a unique way to organize and manipulate
  data.

  Let''...'
---

In the vast landscape of Python programming, understanding data structures is akin to possessing a versatile toolkit. Among the essential tools in this arsenal is the Python set. Sets in Python offer a unique way to organize and manipulate data.

Let's embark on a journey to unravel the mysteries of sets, starting with an analogy that parallels their functionality to real-world scenarios.

You can get all the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/python/python-set/main.py).

## Table Of Contents

* [What are Sets in Python?](#heading-what-are-sets-in-python)
* [How to Create Sets](#heading-how-to-create-sets)
* [Basic Operations](#heading-basic-operations)
* [Set Operations](#heading-set-operations)
* [Other Useful Operations](#heading-other-useful-operations)
* [Conclusion](#heading-conclusion)

## What are Sets in Python?

Imagine you're hosting a gathering of friends from diverse backgrounds, each with their unique identity.  Now, picture this gathering as a set – a collection where each individual is distinct, much like the elements of a set in Python. 

Just as no two guests at your gathering share the same identity, no two elements in a set are identical. This notion of uniqueness lies at the heart of sets.

## How to Create Sets

In Python, you can create a set using curly braces `{}` or the `set()` constructor. Much like sending out invitations to your gathering, creating a set involves specifying the unique elements you want to include:

```python
# Syntax: Creating sets using curly braces

# Example:
guest_set1 = {"Alice", "Bob", "Charlie", "David", "Eve"}

# Syntax: Creating sets using the set() constructor

# Example:
guest_set2 = set(["David", "Eve", "Frank", "Grace", "Helen"])


```

## Basic Operations

### How to Add Elements to a Set

Adding elements to a set mirrors the act of welcoming new guests to your gathering. You can use the `add()` method to include a new element:

```python
# Syntax: Adding elements using the add() method

# Example:
guest_set1.add("Frank")

print(guest_set1)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}


```

Here, the `add()` method adds the name "Frank" to `guest_set1`, representing the arrival of a new guest named Frank to your gathering.

### How to Remove Elements from a Set

Similarly, removing elements from a set symbolizes bidding farewell to departing guests. You can use methods like `remove()` or `discard()` for this purpose:

```python
# Syntax: Removing elements using the remove() method

# Example:
guest_set1.remove("Charlie")

print(guest_set1)  # Output: {'Alice', 'Bob', 'David', 'Eve', 'Frank'}

# Syntax: Removing elements using the discard() method

# Example:
guest_set1.discard("Bob")

print(guest_set1)  # Output: {'Alice', 'David', 'Eve', 'Frank'}


```

In the first example, the `remove()` method removes the name "Charlie" from `guest_set1`, simulating the departure of the guest named Charlie from your gathering. 

In the second example, the `discard()` method removes the name "Bob" from `guest_set1`, indicating the departure of another guest named Bob.

### How to Get the Length of a Set

Just as you might count the number of guests at your gathering, you can determine the length of a set using the `len()` function:

```python
# Syntax: Getting the length of a set using the len() function

# Example:
print(len(guest_set1))  # Output: 4


```

The `len()` function returns the number of elements in `guest_set1`, indicating the total count of guests present at your gathering.

## Set Operations

### How to Join Sets

The union of two sets combines elements from both gatherings, ensuring no duplicates:

```python
# Syntax: Union of sets using the union() method

# Example:
all_guests = guest_set1.union(guest_set2)

print(all_guests)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen'}

```

Here, the `union()` method combines `guest_set1` and `guest_set2` into a new set named `all_guests`, representing the combined list of guests from both gatherings without any duplicates.

### Intersection – How to Find Common Interests

Intersection identifies elements common to both sets, much like finding shared interests among guests:

```python
# Syntax: Intersection of sets using the intersection() method

# Example:
common_guests = guest_set1.intersection(guest_set2)

print(common_guests)  # Output: {'David', 'Eve'}


```

The `intersection()` method identifies the common guests present in both `guest_set1` and `guest_set2`, storing them in the set `common_guests`.

### Difference – How to Find Unique Attributes

The difference between sets showcases elements unique to each gathering, analogous to individual characteristics:

```python
# Syntax: Difference between sets using the difference() method

# Example:
unique_to_guest_set1 = guest_set1.difference(guest_set2)

print(unique_to_guest_set1)  # Output: {'Alice', 'Frank'}


```

The `difference()` method identifies the guests present in `guest_set1` but not in `guest_set2`, storing them in the set `unique_to_guest_set1`.

### Symmetric Difference – How to Find Exclusive Elements

Symmetric difference reveals elements exclusive to each gathering, akin to unique privileges or experiences:

```python
# Syntax: Symmetric difference between sets using the symmetric_difference() method

# Example:
exclusive_guests = guest_set1.symmetric_difference(guest_set2)

print(exclusive_guests)  # Output: {'Bob', 'Charlie', 'Grace', 'Alice', 'Frank', 'Helen'}


```

The `symmetric_difference()` method identifies guests present exclusively in either `guest_set1` or `guest_set2`, storing them in the set `exclusive_guests`.

## Other Useful Operations

### How to Check for Subset and Superset – Group Dynamics

You can determine if one set is a subset or superset of another, reflecting group dynamics within the gatherings:

```python
# Syntax: Checking for subset using the issubset() method

# Example:
print(guest_set1.issubset(all_guests))  # Output: True

# Syntax: Checking for superset using issuperset() method

# Example:
print(all_guests.issuperset(guest_set1))  # Output: True


```

These methods check if `guest_set1` is a subset of `all_guests` and if `all_guests` is a superset of `guest_set1`, respectively, indicating the relationship between the two gatherings.

### How to Clear a Set

Clearing a set removes all elements, akin to resetting the gathering for a fresh start:

```python
# Syntax: Clearing a set using the clear() method

# Example:
guest_set1.clear()

print(guest_set1)  # Output: set()


```

The `clear()` method removes all elements from `guest_set1`, effectively resetting it to an empty set.

## Conclusion

By understanding the analogy and operations outlined in this guide, you're equipped to harness the power of sets in your Python journey. 

Happy coding, and may your gatherings – both digital and physical – be filled with unique experiences and fruitful interactions!

If you have any feedback, then DM me on [Twitter](https://twitter.com/introvertedbot) or [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).

