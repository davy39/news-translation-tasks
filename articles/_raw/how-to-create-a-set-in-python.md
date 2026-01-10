---
title: Python Set – How to Create a Set in Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-06-09T15:52:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-set-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Copy-of-read-write-files-python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Sets are defined as a collection of objects. They are an important concept\
  \ in math and programming. \nProgramming languages provide different ways to group\
  \ objects. Lists, dictionaries, and arrays are some examples of grouping objects.\
  \ \nPython has its..."
---

Sets are defined as a collection of objects. They are an important concept in math and programming. 

Programming languages provide different ways to group objects. Lists, dictionaries, and arrays are some examples of grouping objects. 

Python has its own methods of creating a collection of objects. In Python, creating sets is one of the ways in which we can group items together.

In this tutorial, we will learn the different methods to create sets in Python and discover their characteristics.

## Characteristics of a Set in Python

Sets exhibit the following characteristics:

* Sets are unordered. This means that they do not preserve the original order in which they were created.

```python
>>> x = {'a','b','c'}
>>> print(x)
>>> x
{'a', 'c', 'b'}

```

* Set elements must be unique, as duplicates are not allowed. In case a duplicate value is added, it will be displayed only once.

```python
>>> x = {'a','b','c','c'}
>>> print(x)
{'a', 'c', 'b'}
>>>

```

* The elements in a set must be of an immutable type. But the set itself can be modified by operations like union, intersection, and so on.

## How to Define a Set in Python

There are two main methods to create sets. One is using the `set` function and the other is to use curly braces and add objects individually.

First, you can pass an iterable in the built-in `set` function.

_Syntax:_

```python
sample_set = set(<iterable>)
```

Here, `<iterable>` can be any iterable object such as a list, string, or tuple.

**Passing `list` as an iterable:**

```python
>>> sample_set = set(['100', 'Days', 'Of', 'Code'])
>>> print(sample_set)
{'Of', '100', 'Days', 'Code'}
>>>
```

**Passing `tuple` as an iterable:**

```python
>>> sample_set = set(('Tuple', 'as', 'an', 'iterable'))
>>> print(sample_set)
{'as', 'iterable', 'an', 'Tuple'}
```

**Passing `string` as an iterable:**

```python
>>> s = 'Alpha'
>>> set(s)
{'p', 'l', 'a', 'h', 'A'}
```

You can also define an empty set. You can define an empty set like this:

```python
>>> s = set()
>>> type(s)
<class 'set'>
```

You can also define a set by individually placing objects.in curly braces.

```python
>>> s = {'I', 'Like', 'Python'}
>>> type(s)
<class 'set'>
```

An interesting point about sets is that elements can be of different data types:

```python
>>> s = {1947, 'cat', 1.179, None, 'w'}
>>> print(s)
{1.179, 'w', 1947, 'cat', None}
>>>

```

But remember, the set elements must be immutable. As tuples are immutable, we can include them in sets:

```python
>>> s = {42, 'foo', ('T','U','P','L','E'), 3.14159, None}
>>> type(s)
<class 'set'>
>>> print(s)
{3.14159, ('T', 'U', 'P', 'L', 'E'), 42, 'foo', None}

```

**Some exceptions:**

But we cannot include lists and dictionaries in sets as they are mutable.

```python
>>> a = ['This', 'is', 'a', 'list']
>>> {a}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

```

```python
>>> dictionary = {'month': 1, 'day': 12}
>>> {dictionary}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

```

## How to Determine Set Size in Python

We can check the length of a set using `len()`.

```python
>>> sample_set = set(['100', 'Days', 'Of', 'Code'])
>>> len(sample_set)
4
```

## How to Determine Set Membership

We can confirm the membership of an element using the `in` and `not in` operators.

```python
>>> sample_set = set(['100', 'Days', 'Of', 'Code'])
>>> '100' in sample_set
True
>>> '100' not in sample_set
False
>>> 'red' in sample_set
False
```

# Wrapping up

In this tutorial, we learned the different methods to create sets in Python. I hope now you're comfortable with creating sets.

I hope you found this tutorial helpful. Thank you for reading till the end.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can also read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).



<sub>Banner credits: Industrial revolution vector created by jcomp - www.freepik.com</sub>


