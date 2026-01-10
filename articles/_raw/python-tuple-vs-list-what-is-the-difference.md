---
title: Python Tuple VS List – What is the Difference?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-20T21:15:57.000Z'
originalURL: https://freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-christina-morillo-1181359--1-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Tuples and lists are two of the four available built-in data types that
  you can use to store data in Python.

  They are both useful and they might seem similar at first glance. But they have
  significant differences and each one is best used in differen...'
---

Tuples and lists are two of the four available built-in data types that you can use to store data in Python.

They are both useful and they might seem similar at first glance. But they have significant differences and each one is best used in different cases.

This article will give you an overview of how tuples and lists work. We'll discuss their individual characteristics and their unique use cases, and I'll present their similarities and differences along the way.

You can try out the code examples shown in the article using the interactive Python shell, which you get when you install Python on your computer.

Let's get started!

## What Are Tuples and Lists in Python?

Tuples and Lists are both built-in data structures in Python.

They are containers that let you organise your data by allowing you to  store an ordered collection of one or more items.

A tuple has a class  of 'tuple', `<class 'tuple'>`, and a list has a class  of 'list', `<class 'list'>`.

You can always use the `type()` built-in function and pass the object as the argument that you want to test. This lets you check wether it's a tuple or a list.

Say you have created a tuple named `my_tuple`. You can check its type like so:

```python
>>>type(my_tuple)

#output
<class 'tuple'>
```

This is particularly useful for debugging. 

Now lets look at some other similarities between tuples and lists.

## Similarities Between Tuples and Lists in Python

As I mentioned before, tuples and lists are indeed similar, and they share some features which we'll cover now.

### Tuples and lists can both store multiple items under a single variable

Tuples and lists can either be empty or can contain one or even multiple items under a single variable. 

The only difference is in the syntax: you create tuples by surrounding the items inside them with opening and closing round brackets, `()`, whereas lists are denoted and defined by the presence of opening and closing square brackets,`[]`.

To create an *empty* tuple, you either use parentheses on their own,`()`, or the `tuple()` constructor method.

```python
>>>type(())
<class 'tuple'>

>>>my_tuple = ()

>>>type(my_tuple)
<class 'tuple'>

#or..


>>>my_tuple = tuple()

>>>type(my_tuple)
<class 'tuple'>
```

To create an *empty* list you could just use two empty square brackets alone or call the `list()` constructor method.

```python
>>>type([])
<class 'list'>


>>>my_list = []

#or..

>>>my_list = list()
```


When creating a tuple with *one item*, don't forget to add a comma at the end.

```python
>>>age = (28,)
```

If you are using the `tuple()` method to create the tuple, don't forget that it needs double parentheses.

```
>>>age = tuple((28,))

>>>type(age)
<class 'tuple'>
```

If you do not add the trailing comma, Python will not acknowledge it as a tuple.

```python
>>>age = (28)

>>>type(age)
<class 'int'>
```


When creating a list with *one item*, you don't have to worry about adding the trailing comma.

```python
>>> age = [28]

>>> type(age)
<class 'list'>
```

The items stored are generally similar in nature and are related to one another in some way.

You can create a tuple or a list that contains just a sequence of strings, just a sequence of integers, or just a sequence of Boolean values, with each item in the sequence separated by a comma.

You can also create a tuple or list that contains a mix of different data types.

```python
>>>my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False]

#or..

>>>my_information = list(("Dionysia",27,True,"Lemonaki",7,"Python",False))

print(my_information)
['Dionysia', 27, True, 'Lemonaki', 7, 'Python', False]
```

Lists and tuples can contain duplicate items and values can be repeated, appearing multiple times.

```python
>>>information = ("Jimmy",50,True,"Kate",50)

>>>print(information)
('Jimmy', 50, True, 'Kate', 50)

or..

>>>my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False,27,"Python",27]
```

If you forget the commas, you'll get an error:

```python
>>>information = ("Jimmy" 50,True,"Kate",50)
File "<stdin>", line 1
    >>>information = ("Jimmy" 50,True,"Kate",50)
    ^
SyntaxError: invalid syntax
```

```python
>>>my_information = ["Dionysia" 28,True,"Lemonaki",7,"Python",False]
 File "<stdin>", line 1
    my_information = ["Dionysia" 28,True,"Lemonaki",7,"Python",False]
                                 ^
SyntaxError: invalid syntax
```

To check the length and determine how many items there are in a tuple or a list, you use the `len()` method.

```python
>>>my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False,27,"Python",27]

>>>len(my_information)
7
```

### Tuples and Lists in Python both support unpacking

Essentially, when creating a tuple or a list, many values are 'packed' into a single variable as I mentioned earlier on.

```python
>>>front_end = ("html","css","javascript")
```

Those values can be 'unpacked' and assigned to individual variables.

```python
>>>front_end = ("html","css","javascript")

>>>content,styling,interactivity = front_end

>>>content
'html'

>>>styling
'css'

>>>interactivity
'javascript'
```


Make sure that the variables you create are the exact same number as the values inside the tuple/list, otherwise Python will throw you an error:

```python
>>>front_end = ("html","css","javascript")

>>>content,styling = front_end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)


#or..


>>>front_end = ("html","css","javascript")

>>>content,styling,interactivity,data =  front_end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
```


### You can access items by their index in both tuples and lists in Python 

As mentioned earlier, tuples and lists are both an **ordered** collection of items.

The  order is set and unchangeable, and it's preserved throughout the whole life of the program.

The order in which the items are specified will always remain the same from the time they were created.

Each value in a tuple and a list has a unique identifier, also known as an index.

Each item in a tuple and list can therefore be accessed by referencing that index.

Indexing in Python (and in most programming languages and Computer Science in general) starts at `0`. 

So, the first item has an index of `0`, the second item has an index of `1`, and so on.

You write the name of the tuple or list and then the name of the index in square brackets.

```python
>>>names = ("Jimmy","Timmy","John","Kate")

>>>names[2]
'John'
```
Or like this:
```
>>>programming_languages = ["Python","JavaScript","Java","C"]

>>>programming_languages[0]
'Python'

>>>programming_languages[1]
'JavaScript'
```

Alright, now that we've seen how they're similar, now let's look at the ways in which tuples and lists differ.

## Differences between Tuples and Lists in Python

### Tuples are immutable whereas lists are mutable in Python

Tuples are **immutable** in Python, which menas that once you have created a tuple the items inside it cannot change. 

Tuples can't be continually changed.

If you try to change the value of one of the items, you'll get an error:

```python
>>>names = ("Jimmy","Timmy","John","Kate")

>>>names[2] = "Kelly"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

You can't add, replace, reassign, or remove any of the items since tuples can't be changed.

This also means that tuples have a fixed length. Their length never changes throughout the program's lifecycle.

#### When to use tuples

Tuples are great to use if you want the data in your collection to be read-only, to never change, and always remain the same and constant.

Because of this ability and the guarantee that data is never changed, tuples can be used in dictionaries and sets, which require the elements contained inside them to be of an immutable type.

#### When to use lists

On the other hand, you can easily change and modify lists because lists are **mutable**.

This means that lists are changeable – you can add items to a list, remove items from a list, move items around and switch them easily in a list.

Lists are useful when you want your data to be flexible, or not always stay the same, and be modified when needed.

Lists support a variety of built-in Python methods that perform certain operations on the list which you can't use on tuples.

This means that the length and size of lists grows and shrinks throught the program's lifecycle.

Now let's look at some simple ways to change lists.

## How to Update Lists in Python

Since lists are mutable, you'll need to know some basic ways you can update the data in them.

### How to update an item in a list in Python

To update a single, particular item in a list, you reference its index number in square brackets and then assign it a new value.

```python
#general syntax
>>>list_name[index] = new_value

>>>programming_languages = ["Python","JavaScript","Java","C"]
>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']

>>>programming_languages[2] = "C++"
>>>print(programming_languages)
['Python', 'JavaScript', 'C++', 'C']
```

### How to add items to a list in Python

There are a few built-in methods in Python for adding items to lists.

The `.append()` method adds one new item to the *end* of the list.

```python
#general syntax
>>>list_name.append(item)

>>>programming_languages = ["Python","JavaScript","Java","C"]
>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']

>>>programming_languages.append("C++")

>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C', 'C++']
```

To add one item at a specific position, you use the `.insert()` method.

This inserts an item into the list at the given position. The rest of the elements in the list that come after the item you want to add are all pushed one position to the right.

```python
#general syntax
>>>list_name.insert(index,item)

>>>names = ["Cody","Dillan","James","Nick"]
>>>print(names)
['Cody', 'Dillan', 'James', 'Nick']


>>>names.insert(0,"Stephanie")

>>>print(names)
['Stephanie', 'Cody', 'Dillan', 'James', 'Nick']
```

If you want to add more than one item to your list, you use the `.extend()` method.

This adds an iterable at the *end* of the list. For example you could add a new list at the end of an existing list.

```python
#general syntax
>>>list_name.extend(iterable)

>>>programming_languages = ["Python","JavaScript"]
>>>more_programming_languages = ["Java","C"]

#add more_programming_languages to programming_languages
>>>programming_languages.extend(more_programming_languages) 

>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']
```

### How to delete items from a list in Python

There are two built-in methods for deleting items from a list in Python.

One is the `.remove()` method. This removes the first instance of the item you specify.

```python
#general syntax
>>>list_name.remove(item)

>>>programming_languages = ["Python", "JavaScript", "Java", "C"]
>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']

>>>programming_languages.remove("Java")
>>>print(programming_languages)
['Python', 'JavaScript', 'C']

#deletes only first occurence
>>>programming_languages = ["Python", "JavaScript", "Java", "C","Python"]
>>>programming_languages.remove("Python")
>>>print(programming_languages)
['JavaScript', 'Java', 'C', 'Python']
```

The other way is using the `.pop()` method.

Without passing an argument, it will remove the last item in a list.

You can pass in as an argument the index of the specific item you want to remove.

In both cases the removed value is returned, which is useful. If you wanted, you could store it in a variable for later use.

```python
>>>programming_languages = ["Python", "JavaScript", "Java", "C"]

>>>programming_languages.pop()
'C'


>>>print(programming_languages)
['Python', 'JavaScript', 'Java']

#store returned value in a variable
>>>programming_languages = ["Python", "JavaScript", "Java", "C"]

>>>fave_language = programming_languages.pop(0)
>>>print(fave_language)
Python
```

## Conclusion

This marks the end of our introduction to how tuples and lists work and how they're commonly used.

To recap, the **similarities** between tuples and lists are:

- They are both considered objects in Python.
- They are containers, used to store data. That data can be of any type.
- They are both ordered and maintain that order the whole time. Once the order of the items is defined, it will not change.
- In both tuples and lists you can access individual items by index.

The **differences** between tuples and lists are:

- Tuples are **immutable**. Use them when you know for sure that your data will not change in your program's lifecycle or when you want a guarantee that your data will always remain the same.
- Lists are **mutable**. You can add and remove items. Lists grow and shrink throughout the life of a program. Use them when your data is meant to be changed.

If you want to learn Python in depth, freeCodeCamp offers a free [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You start from the absolute basics and advance to more complex subjects such as data structures and relational databases. At the end, there are five practice projects to solidify your knowledge.

Thanks for reading and happy learning!


