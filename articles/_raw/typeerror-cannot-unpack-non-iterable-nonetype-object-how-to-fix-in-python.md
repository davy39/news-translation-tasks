---
title: 'Typeerror: cannot unpack non-iterable nonetype object – How to Fix in Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-18T19:50:05.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cannot-unpack-non-iterable-nonetype-object-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/markus-spiske-iar-afB0QQw-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "When you're working with iterable objects like Lists, Sets, and Tuples\
  \ in Python, you might want to assign the items in these objects to individual variables.\
  \ This is a process known as unpacking. \nDuring the process of unpacking items\
  \ in iterable ob..."
---

When you're working with iterable objects like Lists, Sets, and Tuples in Python, you might want to assign the items in these objects to individual variables. This is a process known as unpacking. 

During the process of unpacking items in iterable objects, you may get an error that says: "TypeError: cannot unpack non-iterable NoneType object".

This error mainly happens when you try to assign an object with a `None` type to a set of individual variables. This may sound confusing at the moment, but it'll be much clearer once we see some examples. 

Before that, let's talk about some of the key terms seen in the error message. We'll discuss the following terms: TypeError, unpacking, and NoneType.

## What Is a TypeError in Python?

A TypeError in Python occurs when incompatible data types are used in an operation. 

An example of a TypeError, as you'll see in the examples in the sections that follow, is the use of a `None` data type and an iterable object in an operation. 

## What Is Unpacking in Python?

To explain unpacking, you have to understand what packing means. 

When you create a list with items in Python, you've "packed" those items into a single data structure. Here's an example:

```python
names = ["John", "Jane", "Doe"]
```

In the code above, we packed "John", "Jane", and "Doe" into a list called `names`. 

To unpack these items, we have to assign each item to an individual variable. Here's how:

```python
names = ["John", "Jane", "Doe"]

a, b, c = names

print(a,b,c)
# John Jane Doe
```

Since we've created the `names` list, we can easily unpack the list by creating new variables and assigning them to the list: `a, b, c = names`.

So `a` will take the first item in the list, `b` will take the second, and `c` will take the third. That is:

`a` = "John"  
`b` =  "Jane"  
`c` = "Doe"

## What Is NoneType in Python?

NoneType in Python is a data type that simply shows that an object has no value/has a value of `None`. 

You can assign the value of `None` to a variable but there are also methods that return `None`. 

We'll be dealing with the `sort()` method in Python because it is most commonly associated with the "TypeError: cannot unpack non-iterable NoneType object" error. This is because the method returns a value of `None`. 

Next, we'll see an example that raises the "TypeError: cannot unpack non-iterable NoneType object" error.

## Example of "TypeError: cannot unpack non-iterable NoneType object" error

In this section, you'll understand why we get an error for using the `sort()` method incorrectly before unpacking a list.

```python
names = ["John", "Jane", "Doe"]

names = names.sort()

a, b, c = names

print(a,b,c)
# TypeError: cannot unpack non-iterable NoneType object
```

In the example above, we tried to sort the `names` list in ascending order using the `sort()` method.

After that, we went on to unpack the list. But when we printed out the new variables, we got an error. 

This brings us to the last important term in the error message: `non-iterable`. After sorting, the `names` list became a `None` object and not a list (an iterable object).

This error was raised because we assigned `names.sort()` to `names`. Since `names.sort()` returns `None`, we have overridden and assigned `None` to a variable that used to be a list. That is:

`names` = `names.sort()`   
but `names.sort()` = `None`  
so `names` = `None`

So the error message is trying to tell you that there is nothing inside a `None` object to unpack. 

This is pretty easy to fix. We'll do that in the next section.

## How to Fix “TypeError: Cannot Unpack Non-iterable NoneType Object” Error in Python

This error was raised because we tried to unpack a `None` object. The simplest way around this is to not assign `names.sort()` as the new value of your list. 

In Python, you can use the `sort()` method on a collection of variables without the need to reassign the result from the operation to the collection being sorted. 

Here's a fix for the problem:

```python
names = ["John", "Jane", "Doe"]

names.sort()

a, b, c = names

print(a,b,c)
Doe Jane John
```

Everything works perfectly now. The list has been sorted and unpacked. 

All we changed was `names.sort()` instead of using `names` = `names.sort()`.

Now, when the list is unpacked, `a, b, c` will be assigned the items in `names` in ascending order. That is:

`a` = "Doe"  
`b` = "Jane"  
`c` = "John"

## Summary

In this article, we talked about the "TypeError: cannot unpack non-iterable NoneType object" error in Python. 

We explained the key terms seen in the error message: TypeError, unpacking, NoneType, and non-iterable.

We then saw some examples. The first example showed how the error could be raised by using the `sort()` incorrectly while the second example showed how to fix the error.

Although fixing the "TypeError: cannot unpack non-iterable NoneType object" error was easy, understanding the important terms in the error message is important. This not only helps solve this particular error, but also helps you understand and solve errors with similar terms in them. 

Happy coding!

