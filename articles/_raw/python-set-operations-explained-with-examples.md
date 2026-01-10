---
title: Python Sets – Operations and Examples
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-10-28T18:17:35.000Z'
originalURL: https://freecodecamp.org/news/python-set-operations-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/python-sets-article-image.jpeg
tags:
- name: Python
  slug: python
- name: Sets
  slug: sets
seo_title: null
seo_desc: 'If you''re a beginner to Python, chances are you''ve come across lists.
  But have you heard about sets in Python?

  In this tutorial, we''ll explore what sets are, how to create them, and the different
  operations you can use on them.

  What are sets in Pytho...'
---

If you're a beginner to Python, chances are you've [come across lists](https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/). But have you heard about sets in Python?

In this tutorial, we'll explore what sets are, how to create them, and the different operations you can use on them.

# What are sets in Python?

In Python, sets are exactly like lists except for the fact that their elements are *immutable* (that means you cannot change/mutate an element of a set once declared). However, you can add/remove elements from the set.

If that was confusing, let me try and summarize:

> A set is a mutable, unordered group of elements, where the elements themselves are immutable.

Another characteristic of a set is that it may include elements of different types. This means you can have a group of numbers, strings, and even tuples, all in the same set!

# How to Create a Set

The most common way of creating a set in Python is by using the built-in `set()` function.

```python
>>> first_set = set(("Connor", 32, (1, 2, 3)))
>>> first_set
{32, 'Connor', (1, 2, 3)}
>>> 
>>> second_set = set("Connor")
>>> second_set
{'n', 'C', 'r', 'o'}
```

You can also create sets using the curly brace `{}` syntax:

```python
>>> third_set = {"Apples", ("Bananas", "Oranges")}
>>> type(third_set)
<class 'set'>
```

The `set()` function takes in an *iterable* and yields a list of objects which will be inserted into the set. The `{}` syntax places the objects themselves into the set.

As you've probably realized, whether you use the `set()` function or the `{}` to create a set, each element needs to be an immutable object. So if you add a list (which is a mutable object) to a set, you'll run into an error:

```py
>>> incorrect_set = {"Apples", ["Bananas", "Oranges"]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

# How to Add or Remove Elements in a Set

We already know that sets are mutable. This means you can add/remove elements in a set.

Here's an example of adding elements to a set using the `update()` function.

```py
>>> add_set = set((1, 2, 3, 4))
>>> add_set
{1, 2, 3, 4}
>>>
>>> add_set.update((1,))
>>> add_set
{1, 2, 3, 4}
>>> add_set.update(("cello", "violin"))
>>> add_set
{1, 2, 3, 4, 'violin', 'cello'}
```

But notice how nothing changes when we try to add "cello" to the set again:

```py
>>> add_set.update(("cello",))
>>> add_Set
{1, 2, 3, 4, 'violin', 'cello'}
```

This is because sets in Python *cannot* contain duplicates. So, when we tried to add `"cello"` again to the set, Python recognized we were trying to add a duplicate element and didn't update the set. This is one caveat that differentiates sets from lists.

Here's how you would remove elements from a set:

```py
>>> sub_set = add_set
>>> sub_set.remove("violin")
>>> sub_set
{1, 2, 3, 4, 'cello'}
```

The `remove(x)` function removes the element `x` from a set. It returns a `KeyError` if `x` is not part of the set:

```py
>>> sub_set.remove("guitar")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'guitar'
```

There are a couple of other ways to remove an element(s) from a set:

* the `discard(x)` method removes `x` from the set, but *doesn't* raise any error if `x` is not present in the set.
    
* the `pop()` method removes and returns a random element from the set.
    
* the `clear()` method removes all elements from a set
    

Here are some examples to illustrate:

```py
>>> m_set = set((1, 2, 3, 4))
>>> 
>>> m_set.discard(5) # no error raised even though '5' is not present in the set
>>>
>>> m_set.pop()
4
>>> m_set
{1, 2, 3}
>>>
>>> m_set.clear()
>>> m_set
set()
```

# Python set() Operations

If you remember your basic high school math, you'll probably recall mathematical set operations like *union*, *intersection*, *difference* and *symmetric difference*. Well, you can achieve the same thing with Python sets.

## 1\. Set Union

The union of two sets is the set of *all the elements* of both the sets without duplicates. You can use the `union()` method or the `|` syntax to find the union of a Python set.

```py
>>> first_set = {1, 2, 3}
>>> second_set = {3, 4, 5}
>>> first_set.union(second_set)
{1, 2, 3, 4, 5}
>>>
>>> first_set | second_set     # using the `|` operator
{1, 2, 3, 4, 5}
```

## 2\. Set Intersection

The intersection of two sets is the set of *all the common elements* of both the sets. You can use the `intersection()` method of the `&` operator to find the intersection of a Python set.

```py
>>> first_set = {1, 2, 3, 4, 5, 6}
>>> second_set = {4, 5, 6, 7, 8, 9}
>>> first_set.intersection(second_set)
{4, 5, 6}
>>>
>>> first_set & second_set     # using the `&` operator
{4, 5, 6}
```

## 3\. Set Difference

The difference between two sets is the set of all the elements in first set that *are not* present in the second set. You would use the `difference()` method or the `-` operator to achieve this in Python.

```py
>>> first_set = {1, 2, 3, 4, 5, 6}
>>> second_set = {4, 5, 6, 7, 8, 9}
>>> first_set.difference(second_set)
{1, 2, 3}
>>>
>>> first_set - second_set     # using the `-` operator
{1, 2, 3}
>>>
>>> second_set - first_set
{8, 9, 7}
```

## 4\. Set Symmetric Difference

The symmetric difference between two sets is the set of all the elements that are *either in* the first set *or* the second set *but not in both*.

You have the choice of using either the `symmetric_difference()` method or the `^` operator to do this in Python.

```py
>>> first_set = {1, 2, 3, 4, 5, 6}
>>> second_set = {4, 5, 6, 7, 8, 9}
>>> first_set.symmetric_difference(second_set)
{1, 2, 3, 7, 8, 9}
>>>
>>> first_set ^ second_set     # using the `^` operator
{1, 2, 3, 7, 8, 9}
```

# How to Modify a Set by Operations

Each of the `set()` operations that we discussed above can be used to *modify* an existing Python set. Similar to how you would use an augmented assignment syntax such as `+=` or `*=` to update a variable, you can do the same for sets:

```py
>>> a = {1, 2, 3, 4, 5, 6}
>>> b = {4, 5, 6, 7, 8, 9}
>>>
>>> a.update(b)          # a "union" operation
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>>
>>> a &= b               # the "intersection" operation
>>> a
{4, 5, 6, 7, 8, 9}
>>>
>>> a -= set((7, 8, 9))  # the "difference" operation
>>> a
{4, 5, 6}
>>>
>>> a ^= b               # the "symmetric difference" operation
>>> a
{7, 8, 9}
```

# Other Set Operations in Python

These are not so common, but they're useful in seeing how sets relate to others.

* the `a.issubset(b)` method or `<=` operator returns true if the `a` is a *subset* of `b`
    
* the `a.issuperset(b)` method or `>=` operator returns true if the `a` is a *superset* of `b`
    
* the `a.isdisjoint(b)` method return true if there are *no common elements* between sets `a` and `b`
    

# Frozen Sets in Python

Because sets are mutable, they are unhashable – which means you cannot use them as dictionary keys.

Python allows you to work around this by using a `frozenset` instead. This has all the properties of a set, except that it is *immutable* (this means that you cannot add/remove elements from the frozenset). It is also hashable, so it can be used as keys to a dictionary.

The `frozenset` datatype has all the methods of a set (such as `difference()`, `symmetric_difference`, and `union`) but because it is immutable, it doesn't have methods to add/remove elements.

```py
>>> a = frozenset((1, 2, 3, 4))
>>> b = frozenset((3, 4, 5, 6))
>>>
>>> a.issubset(b)
False
>>> a.update(b)    # raises an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'update'
```

And using `frozenset`s as dictionary keys is as simple as 1, 2, 3:

```py
>>> a = frozenset((1, 2, 3, 4))
>>> b = frozenset(("w", "x", "y", "z"))
>>>
>>> d = {a: "hello", b: "world"}
>>> d
{frozenset({1, 2, 3, 4}): 'hello', frozenset({'w', 'x', 'y', 'z'}): 'world'}
```

# Wrapping Up

That's it! You've learned about what sets are, how to create and work with them, and different operations you can use on them.

With sets done, you should now be comfortable with most of Python built-in functions. All you need to do now is practice. Good luck!

Be sure to [follow me on Twitter](http://twitter.com/jasmcaus) for more updates. Have a nice one!
