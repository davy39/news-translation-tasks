---
title: Python List .remove() - How to Remove an Item from a List in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-03-02T19:49:19.000Z'
originalURL: https://freecodecamp.org/news/python-list-remove-how-to-remove-an-item-from-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pavel-danilyuk-5496463.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you''ll learn how to use Python''s built-in remove() list
  method.

  By the end, you''ll know how to use remove() to remove an item from a list in Python.

  Here is what we will cover:


  Syntax of the remove() method

  Remove an element from a ...'
---

In this article, you'll learn how to use Python's built-in `remove()` list method.

By the end, you'll know how to use `remove()` to remove an item from a list in Python.

Here is what we will cover:

1. [Syntax of the `remove()` method](#syntax)
2. [Remove an element from a list using `remove()`](#demo-intro)
3. [`remove()` removes only the first occurrence of an item](#first-occurrence)
    1.  [How to remove all occurrences of an item](#all-occurrences)

## The `remove()` Method - A Syntax Overview <a name="syntax"></a>

The `remove()` method is one of the ways you can remove elements from a list in Python. 

The `remove()` method removes an item from a list by its **value** and not by its index number.

The general syntax of the `remove()` method looks like this:

```python
list_name.remove(value)
```

Let's break it down:

- `list_name` is the name of the list you're working with.
- `remove()` is one of Python's built-in list methods. 
- `remove()` takes one single **required** argument. If you do not provide that, you'll get a `TypeError` – specifically you'll get a `TypeError: list.remove() takes exactly one argument (0 given)` error.
- `value` is the specific value of the item that you want to remove from `list_name`.

The `remove()` method does not return the value that has been removed but instead just returns `None`, meaning there is no return value.

If you need to remove an item by its index number and/or for some reason you want to return (save) the value you removed, use the [`pop()` method](https://www.freecodecamp.org/news/python-pop-how-to-pop-from-a-list-or-an-array-in-python/) instead.


## How to Remove an Element from a List Using the `remove()` Method in Python <a name="demo-intro"></a>

To remove an element from a list using the `remove()` method, specify the value of that element and pass it as an argument to the method.

`remove()` will search the list to find it and remove it.

```python
#original list
programming_languages = ["JavaScript", "Python", "Java", "C++"]

#print original list
print(programming_languages)

# remove the value 'JavaScript' from the list
programming_languages.remove("JavaScript")

#print updated list
print(programming_languages)

#output

#['JavaScript', 'Python', 'Java', 'C++']
#['Python', 'Java', 'C++']
```

If you specify a value that is not contained in the list, then you'll get an error – specifically the error will be a `ValueError`:

```python
programming_languages = ["JavaScript", "Python", "Java", "C++"]

#I want to remove the value 'React'
programming_languages.remove("React")

#print list
print(programming_languages)

#output

# line 5, in <module>
#programming_languages.remove("React")
#ValueError: list.remove(x): x not in list
```

To avoid this error from happening, you could first check to see if the value you want to remove is in the list to begin with, using the `in` keyword.

It will return a Boolean value – `True` if the item is in the list or `False` if the value is not in the list.

```python
programming_languages = ["JavaScript", "Python", "Java", "C++"]

#check if 'React' is in the 'programming_languages' list
print("React" in programming_languages)

#output
#False
```

Another way to avoid this error is to create a condition that essentially says, "If this value is part of the list then delete it. If it doesn't exist, then show a message that says it is not contained in the list".

```python
programming_languages = ["JavaScript", "Python", "Java", "C++"]

if "React" in programming_languages:
    programming_languages.remove("React")
else:
    print("This value does not exist")
    
#output
#This value does not exist
```

Now, instead of getting a Python error when you're trying to delete a certain value that doesn't exist, you get a message returned, saying the item you wanted to delete is not in the list you're working with.

## The `remove()` Method Removes the First Occurrence of an Item in a List <a name="first-occurrence"></a>

A thing to keep in mind when using the `remove()` method is that it will search for and will remove only the **first** instance of an item.

This means that if in the list there is more than one instance of the item whose value you have passed as an argument to the method, then only the first occurrence will be removed.

Let's look at the following example:

```python
programming_languages = ["JavaScript", "Python", "Java", "Python", "C++", "Python"]

programming_languages.remove("Python")

print(programming_languages)

#output
#['JavaScript', 'Java', 'Python', 'C++', 'Python']
```

In the example above, the item with the value of `Python` appeared three times in the list.

When `remove()` was used, only the first matching instance was removed – the one following the `JavaScript` value and preceeding the `Java` value. 

The other two occurrences of `Python` remain in the list.

What happens though when you want to remove all occurrences of an item? 

Using `remove()` alone does not accomplish that, and you may not want to just remove the first instance of the item you specified.

### How to Remove All Instances of an Item in A List in Python <a name="all-occurrences"></a>
 
One of the ways to remove all occurrences of an item inside a list is to use list comprehension.

List comprehension creates a new list from an existing list, or creates what is called a sublist.

This will not modify your original list, but will instead create a new one that satisfies a condition you set.


```python
#original list
programming_languages = ["JavaScript", "Python", "Java", "Python", "C++", "Python"]

#sublist created with list comprehension
programming_languages_updated = [value for value in programming_languages if value != "Python"]


#print original list
print(programming_languages)

#print  new sublist that doesn't contain 'Python'
print(programming_languages_updated)

#output

#['JavaScript', 'Python', 'Java', 'Python', 'C++', 'Python']
#['JavaScript', 'Java', 'C++']
```

In the example above, there is the orginal `programming_languages` list. 

Then, a new list (or sublist) is returned. 

The items contained in the sublist have to meet a condition. The condition was that if an item in the original list has a value of `Python`, it would not be part of the sublist.

Now, if you don't want to create a new list, but instead want to modify the already existing list *in-place*, then use the slice assignment combined with list comprehension.

With the slice assignment, you can modify and replace certain parts (or slices) of a list.

To replace the whole list, use the `[:]` slicing syntax, along with list comprehension. 

The list comprehension sets the condition that any item with a value of `Python` will no longer be a part of the list.

```python
programming_languages = ["JavaScript", "Python", "Java", "Python", "C++", "Python"]

programming_languages[:] = (value for value in programming_languages if value != "Python")

print(programming_languages)

#output

#['JavaScript', 'Java', 'C++']
```

## Conclusion

And there you have it! You now know how to remove a list item in Python using the `remove()` method. You also saw some ways of removing all occurrences of an item in a list in Python.

I hope you found this article useful.

To learn more about the Python programming language, check out freeCodeCamp's [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thanks for reading and happy coding 😊 !


