---
title: Python List Append – How to Add an Element to an Array, Explained with Examples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-05-08T18:29:00.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-how-to-add-an-element-to-an-array-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Append.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'Welcome

  Hi! If you want to learn how to use the **append()** method, then this article is
  for you. This is a powerful list method that you will definitely use in your Python
  projects.

  In this article, you will learn:


  Why and when you should use appe...'
---

## Welcome

Hi! If you want to learn how to use the `**append()**` method, then this article is for you. This is a powerful list method that you will definitely use in your Python projects.

**In this article, you will learn:**

* Why and when you should use `append()`.
* How to call it.
* Its effect and return value.
* How it can be equivalent to `insert()` and string slicing with the appropriate arguments. 

You will find examples of the use of `append()` applied to strings, integers, floats, booleans, lists, tuples, and dictionaries.

**Let's begin! ✨**

## 🔹 Purpose

With this method, you can **add a single element to the end of a list**.

Here you can see the effect of `append()` graphically:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-59.png)

💡 **Tip:** To add a sequence of individual elements, you would need to use the `extend()` method.

## 🔸 Syntax & Parameters

This is the basic syntax that you need to use to call this method:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-60.png)

💡 **Tip:** The dot is very important since `append()` is a method. When we call a method, we use a dot after the list to indicate that we want to "modify" or "affect" that particular list.

As you can see, the `append()` method only takes one argument, the element that you want to append. This element can be of any data type: 

* Integer
* String
* Float 
* Boolean
* Another list
* Tuple
* Dictionary
* An Instance of a custom class

Basically, any value that you can create in Python can be appended to a list.

**💡 Tip:** The first element of the syntax (the list) is usually a variable that references a list.

### Example

This is an example of a call to `append()`:

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes.append("B")
```

* First, the list is defined and assigned to a variable. 
* Then, using this variable we call the `append()` method, passing the element that we want to append (the string `"B"`) as argument. 

## 🔹 Effect & Return Value

This method **mutates** (changes) the original list in memory. It doesn't return a new copy of the list as we might intuitively think, it returns `None`. Therefore, just by calling this method you are modifying the original list. 

In our previous example:

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes.append("B")
```

You can see (below) that the original list was modified after appending the element. The last element is now `"B"` and the original list is now the modified version.

```python
>>> musical_notes
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

You can confirm that the return value of `append()` is `None` by assigning this value to a variable and printing it:

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> a = musical_notes.append("B")
>>> print(a)
None
```

## 🔸 Examples

Now that you know the purpose, syntax, and effect of the `append()` method, let's see some examples of its use with various data types.

### Append a String

```python
>>> top_players = ["gino234", "nor233", "lal453"]
>>> top_players.append("auop342")

# The string was appended
>>> top_players
['gino234', 'nor233', 'lal453', 'auop342']
```

### Append an Integer

```python
>>> data = [435, 324, 275, 567, 123]
>>> data.append(456)

>>> data
[435, 324, 275, 567, 123, 456]
```

### Append a Float

```python
>>> data = [435.34, 324.35, 275.45, 567.34, 123.23]
>>> data.append(456.23)

>>> data
[435.34, 324.35, 275.45, 567.34, 123.23, 456.23]
```

### Append a Boolean Value

```python
>>> values = [True, True, False, True]
>>> values.append(False)

>>> values
[True, True, False, True, False]
```

### Append a List

This method appends a single element to the end of the list, so if you pass a list as argument, the entire list will be appended as a single element (it will be a nested list within the original list). 

```
>>> data = [[4.5, 4.8, 5.7], [2.5, 2.6, 2.7]]
>>> data.append([6.7, 2.3])

>>> data
[[4.5, 4.8, 5.7], [2.5, 2.6, 2.7], [6.7, 2.3]]
```

### Append a Tuple

This works exactly the same for tuples, the entire tuple is appended as a single element. 

```
>>> data = [[4.5, 4.8, 5.7], [2.5, 2.6, 2.7]]
>>> data.append((6.7, 2.3))

>>> data
[[4.5, 4.8, 5.7], [2.5, 2.6, 2.7], (6.7, 2.3)] 
```

**💡 Tip:** If you need to add the elements of a list or tuple as individual elements of the original list, you need to use the `extend()` method instead of `append()`. To learn more about this, you can read my article: [Python List Append VS Python List Extend – The Difference Explained with Array Method Examples](https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/)

### Append a dictionary 

Similarly, if you try to append a dictionary, the entire dictionary will be appended as a single element of the list.

```
>>> data = [{"a": 1, "b": 2}]
>>> data.append({"c": 3, "d": 4})
>>> data
[{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
```

## 🔹 Equivalence of Append and Insert 

An interesting tip is that the `insert()` method can be equivalent to `append()` if we pass the correct arguments. 

The `insert()` method is used to insert an element at a particular index (position) in the list. 

This is the syntax used to call the `insert()` method:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-61.png)

**To make it equivalent to `append()`:**

* The value of index has to be the length of the list (`len(<list>)`) because we want the element to be the last element of the list.

Here's an example that shows that the result of using insert with these arguments is equivalent to `append()`:

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes.insert(len(musical_notes), "B")
>>> musical_notes
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

But as you have seen, `append()` is much more concise and practical, so it's usually recommended to use it in this case. 

## 🔸 Equivalence of Append and List Slicing

There is also an interesting equivalence between the `append()` method and list slicing. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-62.png)

This syntax is essentially assigning the list that contains the element `[<elem>]` as the last portion (end) of the list. Here you can see that the result is equivalent to `append()`:

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes[len(musical_notes):] = ["B"]
>>> musical_notes
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

These are interesting alternatives, but for practical purposes we typically use `append()` because it's a priceless tool that Python offers. It is precise, concise, and easy to use. 

**I really hope that you liked my article and found it helpful.** Now you can work with `append()` in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

