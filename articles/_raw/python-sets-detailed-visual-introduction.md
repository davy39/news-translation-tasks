---
title: 'Python Sets: A Detailed Visual Introduction'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-01-06T13:19:00.000Z'
originalURL: https://freecodecamp.org/news/python-sets-detailed-visual-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/Sets-3.png
tags:
- name: Computer Science
  slug: computer-science
- name: learning to code
  slug: learning-to-code
- name: programing
  slug: programing
- name: Python
  slug: python
- name: Sets
  slug: sets
seo_title: null
seo_desc: "Welcome\nIn this article, you will learn the fundamentals of Sets in Python.\
  \ This is a very powerful built-in data type that you can use in your Python projects.\
  \ \nWe will explore:\n\nWhat sets are and why they are relevant for your projects.\n\
  How to crea..."
---

## Welcome

In this article, you will learn the fundamentals of Sets in Python. This is a very powerful built-in data type that you can use in your Python projects. 

**We will explore:**

* What sets are and why they are relevant for your projects.
* How to create a set.
* How to check if an element is in a set.
* The difference between sets and frozensets.
* How to operate with sets (in this part we will dive into the basics of set theory).
* How to add and remove elements from sets and how to clear them.

**Let's begin! ⭐️**

## 🔹 Sets in Context

Let me start by telling you why would you want to use sets in your projects. In mathematics, a set is a collection of distinct objects. In Python, what makes them so special is the fact that **they have no duplicate elements**, so they can be used to remove duplicate elements from lists and tuples efficiently. 

According to the [Python Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets):

> Python also includes a data type for _sets_. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries.

**❗️Important:** The elements of a set must be immutable (they cannot be changed). Immutable data types include strings, tuples, and numbers such as integers and floats.

## 🔸 Syntax

To create a set, we start by writing a pair of curly brackets `{}` and within those curly brackets, we include the elements of the set separated by a comma and a space.  

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-66.png)

**💡 Tip:** Notice that this syntax is different from Python dictionaries because we are not creating key-value pairs, we are simply including individual elements within curly brackets `{}`.

### Set()

Alternatively, we can use the [set()](https://docs.python.org/3/library/stdtypes.html#set) function to create a set (see below). 

To do this, we would pass an iterable (for example, a list, string, or tuple) and this iterable would be converted to a set, removing any duplicate elements. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-64.png)

This is an example in IDLE:

```python
# Set
>>> {1, 2, 3, 4}
{1, 2, 3, 4}

# From a list
>>> set([1, 2, 3, 4])
{1, 2, 3, 4}

# From a tuple
>>> set((1, 2, 3, 4))
{1, 2, 3, 4}
```

**💡 Tip:** To create an empty set, you must use the [set()](https://docs.python.org/3/library/stdtypes.html#set) function because using an empty set of curly brackets, like this `{}`, will automatically create an empty **dictionary**, not an empty set.

```python
# Creates a dictionary, not a set.
>>> type({})
<class 'dict'>

# This is a set
>>> type(set())
<class 'set'>
```

## 🔹 Duplicate Elements are Removed

If the iterable that you pass as the argument to `set()` has duplicate elements, they are removed to create the set.

For example, notice how duplicate elements are removed when we pass this list:

```python
>>> a = [1, 2, 2, 2, 2, 3, 4, 1, 4]
>>> set(a)
{1, 2, 3, 4}
```

and notice how duplicate characters are removed when we pass this string:

```python
>>> a = "hhheeelllooo"
>>> set(a)
{'e', 'l', 'o', 'h'}
```

## 🔸 Length

To find the length of a set, you can use the built-in function [len()](https://docs.python.org/3/library/stdtypes.html#set):

```python
>>> a = {1, 2, 3, 4}
>>> b = set(a)
>>> len(b)
4
```

In mathematics, the number of elements of a set is called the "**cardinality**" of the set.

## 🔹 Membership Testing

You can test if an element is in a set with the `in` operator:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-65.png)

This in an example:

```python
>>> a = "hhheeelllooo"
>>> b = set(a)
>>> b
{'e', 'l', 'o', 'h'}

# Test if the characters 'e' and 'a' are in set b
>>> 'e' in b
True
>>> 'a' in b
False
```

## 🔸 Sets vs. Frozensets

Sets are mutable, which means that they can be modified after they have been defined. 

According to the [Python Documentation](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset):

> The [`set`](https://docs.python.org/3.8/library/stdtypes.html#set) type is **mutable** — the contents can be changed using methods like `add()` and `remove()`. Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set.

Since they cannot contain values of mutable data types, if we try to create a set that contains sets as elements (nested sets), we will see this error:

```python
TypeError: unhashable type: 'set'

```

This is an example in IDLE. Notice how the elements that we are trying to include are sets:

```python
>>> a = {{1, 2, 3}, {1, 2, 4}}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a = {{1, 2, 3}, {1, 2, 4}}
TypeError: unhashable type: 'set'
```

### Frozensets

To solve this problem, we have another type of set called frozensets. 

They are **immutable**, so they cannot be changed and we can use them to create nested sets.

According to the [Python Documentation](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset):

> The [`frozenset`](https://docs.python.org/3.8/library/stdtypes.html#frozenset) type is immutable and [hashable](https://docs.python.org/3.8/glossary.html#term-hashable) — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.

To create a frozenset, we use:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-67.png)

💡 **Tip:** You can create an empty frozenset with `frozenset()`.

This is an example of a set that contains two frozensets:

```
>>> a = {frozenset([1, 2, 3]), frozenset([1, 2, 4])}
>>> a
{frozenset({1, 2, 3}), frozenset({1, 2, 4})}
```

Notice that we don't get any errors and the set is created successfully. 

## 🔹 Introduction to Set Theory

Before diving into set operations, we need to explore a little bit of set theory and Venn diagrams. We will dive into each set operation with its corresponding equivalent in Python code. Let's begin. 

### Subsets and Supersets

You can think of a subset as a "smaller portion" of a set. That is how I like to think about it. If you take some of the elements of a set and make a new set with those elements, the new set is a subset of the original set. 

It's as if you had a bag full of rubber balls of different colors. If you make a set with all the rubber balls in the bag, and then take some of those rubber balls and make a new set with them, the new set is a subset of the original set. 

Let me illustrate this graphically. If we have a set A with the elements 1, 2, 3, 4:

```
>>> a = {1, 2, 3, 4}
```

We can "take" or "select" some elements of a and make a new set called B. Let's say that we chose to include the elements 1 and 2 in set B:

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
```

Every element of B is in A. Therefore, B is a subset of A. 

This can be represented graphically like this, where the new set B is illustrated in yellow:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-69.png)

**💡 Note:** In set theory, it is a convention to use uppercase letters to denote sets. This is why I will use them to refer to the sets (A and B), but I will use lowercase letter in Python (a and b).

### .issubset()

We can check if B is a subset of A with the method [.issubset(<other>)](https://docs.python.org/3/library/stdtypes.html#frozenset.issubset):

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> b.issubset(a)
True
```

As you can see, B is a subset of A because the value returned is `True`.

But the opposite is not true since not all the element of A are in B:

```python
>>> a.issubset(b)
False
```

Let's see something very interesting:

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2, 3, 4}
>>> a.issubset(b)
True
>>> b.issubset(a)
True
```

If two sets are equal, one is a subset of the other and vice versa because all the elements of A are in B and all elements of B are in A. This can be illustrated like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-70.png)

### Using <=

We can achieve the same functionality of the `.issubset()` method with the `<=` comparison operator:

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2, 3, 4}
>>> a <= b
True
```

This operator returns `True` if the left operand is a subset of the right operand, even when the two sets are equal (when they have the same elements).

### Proper Subset

But what happens if we want to check if a set is a **proper subset** of another? A proper subset is a subset that is not equal to the set (does not have all the same elements). 

This would be a graphical example of a proper subset. B does not have all the elements of A:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-69.png)

To check this, we can use the `<` comparison operator:

```python
# B is not a proper subset of A because B is equal to A
>>> a = {1, 2, 3, 4}
>>> b = {1, 2, 3, 4}
>>> b < a
False

# B is a proper subset of A because B is not equal to A
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> b < a
True
```

### Superset

**If B is a subset of A, then A is a superset of B**. A superset is the set that contains all the elements of the subset.  

This can be illustrated like this (see below), where A is a superset of B:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-97.png)

### .issuperset()

We can test if a set is a superset of another with the [.issuperset()](https://docs.python.org/3/library/stdtypes.html#frozenset.issuperset) method:

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> a.issuperset(b)
True
```

We can also use the operators `>` and `>=`. They work exactly like `<` and `<=`, but now they determine if the left operand is a **superset** of the right operand:

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> a > b
True
>>> a >= b
True
```

### Disjoint Sets

Two sets are disjoint if they have no elements in common. For example, here we have two disjoint sets:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-83.png)

### .isdisjoint()

We can check if two sets are disjoint with the [.isdisjoint()](https://docs.python.org/3/library/stdtypes.html#frozenset.isdisjoint) method:

```python
# Elements in common: 3, 1
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a.isdisjoint(b)
False

# Elements in common: None
>>> a = {3, 1, 4}
>>> b = {8, 9, 0}
>>> a.isdisjoint(b)
True
```

## 🔸 Set Operations

We can operate on sets to create new sets, following the rules of set theory. Let's explore these operations.

### Union

This is the first operation that we will analyze. It creates a new set that contains all the elements of the two sets (without repetition).

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-72.png)

This is an example:

```python
>>> a = {3, 1, 7, 4}
>>> b = {2, 8, 3, 1}
>>> a | b
{1, 2, 3, 4, 7, 8}
```

💡 **Tip:** We can assign this new set to a variable, like this:

```python
>>> a = {3, 1, 7, 4}
>>> b = {2, 8, 3, 1}
>>> c = a | b
>>> c
{1, 2, 3, 4, 7, 8}
```

In a diagram, these sets could be represented like this (see below). This is called a Venn diagram, and it is used to illustrate the relationships between sets and the result of set operations.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-74.png)
_Venn Diagram. Union._

We can easily extend this operation to work with more than two sets:

```python
>>> a = {3, 1, 7, 4}
>>> b = {2, 8, 3, 1}
>>> c = {1, 0, 4, 6}
>>> d = {8, 2, 6, 3}

# Union of these four sets
>>> a | b | c | d
{0, 1, 2, 3, 4, 6, 7, 8}
```

💡 **Tip:** If the union contains repeated elements, only one is included in the final set to eliminate repetition.

### Intersection

The intersection between two sets creates another set that contains all the elements that are **in** **both A and B**.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-77.png)

This is an example:

```python
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a & b
{1, 3}
```

The Venn diagram for the intersection operation would be like this (see below), because only the elements that are **in both A and B** are included in the resulting set:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-78.png)
_Venn Diagram. Intersection._

We can easily extend this operation to work with more than two sets:

```python
>>> a = {3, 1, 7, 4, 5}
>>> b = {2, 8, 3, 1, 5}
>>> c = {1, 0, 4, 6, 5}
>>> d = {8, 2, 6, 3, 5}

# Only 5 is in a, b, c, and d.
>>> a & b & c & d
{5}
```

### Difference

The difference between set A and set B is another set that contains all the **elements of set A that are not in set B**.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-79.png)

This is an example:

```python
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a - b
{6}
```

The Venn diagram for this difference would be like this (see below), because only the elements of A that are not in B are included in the resulting set:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-80.png)
_Venn Diagram. Difference._

💡 **Tip:** Notice how we remove the elements of A that are also in B (in the intersection). 

We can easily extend this to work with more than two sets:

```python
>>> a = {3, 1, 7, 4, 5}
>>> b = {2, 8, 3, 1, 5}
>>> c = {1, 0, 4, 6, 5}

# Only 7 is in A but not in B and not in C
>>> a - b - c
{7}
```

### Symmetric Difference

The symmetric difference between two sets A and B is another set that contains **all the elements that are in either A or B, but not both**. We basically remove the elements from the intersection.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-81.png)

```python
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a ^ b
{2, 6, 8}
```

The Venn diagram for the symmetric difference would be like this (see below), because only the elements that are in either A or B, but not both, are included in the resulting set:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-82.png)
_Venn Diagram. Symmetric Difference_

We can easily extend this to work with more than two sets:

```python
>>> a = {3, 1, 7, 4, 5}
>>> b = {2, 8, 3, 1, 5}
>>> c = {1, 0, 4, 6, 5}
>>> d = {8, 2, 6, 3, 5}

>>> a ^ b ^ c ^ d
{0, 1, 3, 7}
```

### Update Sets Automatically

If you want to update set A immediately after performing these operations, you can simply add an equal sign after the operator. For example:

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}

# Notice the &= 
>>> a &= b
>>> a
{1, 2}
```

We are assigning the set that results from `a & b` to set `a` in just one line. You can do the same with the other operators: `^=` , `|=`, and `-=`. 

**💡 Tip:** This is very similar to the syntax that we use with variables (for example: `a += 5`) but now we are working with sets.

## 🔹 Set Methods

Sets include helpful built-in methods to help us perform common and essential functionality such as adding elements, deleting elements, and clearing the set.

### Add Elements

To add elements to a set, we use the [.add()](https://docs.python.org/3/library/stdtypes.html#frozenset.add) method, passing the element as the only argument.

```
>>> a = {1, 2, 3, 4}
>>> a.add(7)
>>> a
{1, 2, 3, 4, 7}
```

### Delete Elements

There are three ways to delete an element from a set: `.remove(<elem>)` ,`.discard(<elem>)`, and `.pop()`. They have key differences that we will explore.

The first two methods (.remove() and .discard()) work exactly the same when the element is in the set. The new set is returned:

```python
>>> a = {1, 2, 3, 4}
>>> a.remove(3)
>>> a
{1, 2, 4}

>>> a = {1, 2, 3, 4}
>>> a.discard(3)
>>> a
{1, 2, 4}
```

The key difference between these two methods is that if we use the [.remove()](https://docs.python.org/3/library/stdtypes.html#frozenset.remove) method, we run the risk of trying to remove an element that doesn't exist in the set and this will raise a `KeyError`:

```python
>>> a = {1, 2, 3, 4}
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.remove(5)
KeyError: 5
```

We will never have that problem with [.discard()](https://docs.python.org/3/library/stdtypes.html#frozenset.discard) since it doesn't raise an exception if the element is not found. This method will simply leave the set intact, as you can see in this example:

```python
>>> a = {1, 2, 3, 4}
>>> a.discard(5)
>>> a
{1, 2, 3, 4}
```

The third method ([.pop()](https://docs.python.org/3/library/stdtypes.html#frozenset.pop)) will remove and return an arbitrary element from the set and it will raise a `KeyError` if the set is empty. 

```python
>>> a = {1, 2, 3, 4}
>>> a.pop()
1
>>> a.pop()
2
>>> a.pop()
3
>>> a
{4}
>>> a.pop()
4
>>> a
set()
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.pop()
KeyError: 'pop from an empty set'
```

### Clear the Set

You can use the `.clear()` method if you need to delete all the elements from a set. For example:

```python
>>> a = {1, 2, 3, 4}
>>> a.clear()
>>> a
set()
>>> len(a)
0
```

## 🔸 In Summary

* Sets are unordered built-in data types that don't have any repeated elements, so they allow us to eliminate repeated elements from lists and tuples.
* They are mutable and they can only contain immutable elements.
* We can check if a set is a subset or superset of another set.
* Frozenset is an immutable type of set that allows us to create nested sets.
* We can operate on sets with: union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`).
* We can add elements to a set, delete them, and clear the set completely using built-in methods.

**I really hope you liked my article and found it helpful.** Now you can work with sets in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

