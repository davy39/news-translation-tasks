---
title: Python .pop() – How to Pop from a List or an Array in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-03-01T20:30:51.000Z'
originalURL: https://freecodecamp.org/news/python-pop-how-to-pop-from-a-list-or-an-array-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-olia-danilevich-4974912.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, you'll learn how to use Python's built-in pop() list method.\n\
  By the end, you'll know how to use pop() to remove an item from a list in Python.\n\
  Here is what we will cover:\n\nAn overview of lists in Python\n How to delete list\
  \ items usin..."
---

In this article, you'll learn how to use Python's built-in `pop()` list method.

By the end, you'll know how to use `pop()` to remove an item from a list in Python.

Here is what we will cover:

1. [An overview of lists in Python](#intro)
2. [ How to delete list items using `pop()`](#pop-intro)
    1. [Syntax of the `pop()` method](#syntax)
    2. [Use the `pop()` method with no parameter](#no-parameter)
    3. [Use the `pop()` method with optional parameter](#with-parameter)
    4. [Dealing with common errors](#errors)

## What are Lists In Python and How to Create Them <a name="intro"></a>

Lists are a built-in data type in Python. They act as containers, storing collections of data.

Lists are created by using square brackets, `[]`, like so: 

```python
#an empty list
my_list = []

print(my_list)
print(type(my_list))

#output

#[]
#<class 'list'>
```

You can also create a list by using the `list()` constructor:

```python
#an empty list
my_list = list()

print(my_list)
print(type(my_list))

#output

#[]
#<class 'list'>
```

As you saw above, a list can contain `0` items, and in that case it is considered an empty list.

Lists can also contain items, or list items. List items are enclosed inside the square brackets and are each separated by a comma, `,`.

List items can be homogeneous, meaning they are of the same type. 

For example, you can have a list of only numbers, or a list of only text:

```python
# a list of integers
my_numbers_list = [10,20,30,40,50]

# a list of strings
names = ["Josie", "Jordan","Joe"]

print(my_numbers_list)
print(names)

#output

#[10, 20, 30, 40, 50]
#['Josie', 'Jordan', 'Joe']
```

List items can also be heterogeneous, meaning they can all be of different data types. 

This is what sets lists apart from arrays. Arrays require that items are only of the same data type, whereas lists do not.

```python
#a list containing strings, integers and floating point numbers
my_information = ["John", "Doe", 34, "London", 1.76]

print(my_information)

#output

#['John', 'Doe', 34, 'London', 1.76]
```

Lists are *mutable*, meaning they are changeable. List items can be updated, list items can be deleted, and new items can be added to the list.


## How to Delete Elements from a List Using the `pop()` Method in Python <a name="pop-intro"></a>

In the sections that follow you'll learn how to use the `pop()` method to remove elements from lists in Python.

### The `pop()` Method - A Syntax Overview <a name="syntax"></a>

The general syntax of the `pop()` method looks like this:

```python
list_name.pop(index)
```

Let's break it down:

- `list_name` is the name of the list you're working with.
- The built-in `pop()` Python method takes only one **optional** parameter.
- The optional parameter is the index of the item you want to remove.

### How to Use the `pop()` Method With No Parameter <a name="no-parameter"></a>

By default, if there is no index specified, the `pop()` method will remove the **last** item that is contained in the list.

This means that when the `pop()` method doesn't have any arguments, it will remove the last list item.

So, the syntax for that would look something like this:

```python
list_name.pop()
```

Let's look at an example:

```python
#list of programming languages
programming_languages = ["Python", "Java", "JavaScript"]

#print initial list
print(programming_languages)

#remove last item, which is "JavaScript"
programming_languages.pop()

#print list again
print(programming_languages)

#output

#['Python', 'Java', 'JavaScript']
#['Python', 'Java']
```

Besides just removing the item, `pop()` also returns it.

This is helpful if you want to save and store that item in a variable for later use.

```python
#list of programming languages
programming_languages = ["Python", "Java", "JavaScript"]

#print initial list
print(programming_languages)


#remove last item, which is "JavaScript", and store it in a variable
front_end_language = programming_languages.pop()

#print list again
print(programming_languages)

#print the item that was removed
print(front_end_language)

#output

#['Python', 'Java', 'JavaScript']
#['Python', 'Java']
#JavaScript
```

### How to Use the `pop()` Method With Optional Parameter <a name="with-parameter"></a>

To remove a specific list item, you need to specify that item's index number. Specifically, you  pass that index, which represents the item's position, as a parameter to the `pop()` method.

Indexing in Python, and all programming languages in general, is zero-based. Counting starts at `0` and not `1`.

This means that the first item in a list has an index of `0`. The second item has an index of `1`, and so on.

So, to remove the first item in a list, you specify an index of `0` as the parameter to the `pop()` method.

And remember, `pop()` returns the item that has been removed. This enables you to store it in a variable, like you saw in the previous section.

```python
#list of programming languages
programming_languages = ["Python", "Java", "JavaScript"]

#remove first item and store in a variable
programming_language = programming_languages.pop(0)

#print updated list
print(programming_languages)

#print the value that was removed from original list
print(programming_language)

#output

#['Java', 'JavaScript']
#Python
```

Let's look at another example:

```python
#list of programming languages
programming_languages = ["Python", "Java", "JavaScript"]

#remove "Java" from the list
#Java is the second item in the list which means it has an index of 1

programming_languages.pop(1)

#print list 
print(programming_languages)

#output
#['Python', 'JavaScript']
```

In the example above, there was a specific value in the list that you wanted to remove. In order to successfully remove a specific value, you need to know it's position.

### An Overview of Common Errors That Occur When Using the `pop()` Method <a name="errors"></a>

Keep in mind that you'll get an error if you try to remove an item that is equal to or greater than the length of the list - specifically it will be an `IndexError`.

Let's look at the following example that shows how to find the length of a list:

```python
#list of programming languages
programming_languages = ["Python", "Java", "JavaScript"]

#find the length of the list
print(len(programming_languages))

#output
#3
```

To find the length of the list you use the `len()` function, which returns the total number of items contained in the list.

If I try to remove an item at position 3, which is equal to the length of the list, I get an error saying that the index passed is out of range:

```python
#list of programming languages
programming_languages = ["Python", "Java", "JavaScript"]

programming_languages.pop(3)

#output

# line 4, in <module>
#    programming_languages.pop(3)
#IndexError: pop index out of range
```

The same exception would be raised if I had tried to remove an item at position 4 or even higher.

On a similar note, an exception would also be raised if you used the `pop()` method on an empty list:

```python
#empty list
programming_languages = []

#try to use pop() on empty list
programming_languages.pop()

#print updated list
print(programming_languages)

#output
#line 5, in <module>
#    programming_languages.pop()
#IndexError: pop from empty list
```

## Conclusion

And there you have it! You now know how to remove a list item in Python using the `pop()` method.

I hope you found this article useful.

To learn more about the Python programming language, check out freeCodeCamp's [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thanks for reading and happy coding!




