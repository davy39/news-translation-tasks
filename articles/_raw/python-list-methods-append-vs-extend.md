---
title: Python List Methods – append( ) vs extend( ) in Python Explained with Code
  Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-06-21T21:25:11.000Z'
originalURL: https://freecodecamp.org/news/python-list-methods-append-vs-extend
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/append---vs-e-x-t-e-n-d--.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When you''re working with Python lists, you often need to combine data
  from multiple lists. So how do you do that?

  In this tutorial, we''ll see the different ways you can combine data from multiple
  lists. We''ll also learn how the list methods append() ...'
---

When you're working with Python lists, you often need to combine data from multiple lists. So how do you do that?

In this tutorial, we'll see the different ways you can combine data from multiple lists. We'll also learn how the list methods `append()` and `extend()` work through simple examples. Let's get started.

## How to Use the '+' Operator in Python

Before we look at how the `append()` and `extend()` methods work, let's see what the `+` operator for concatenating lists does. 

Consider the following example where we have two lists, `list_1` and `list_2`, that we'd like to concatenate (or join together end-to-end):

```python
list_1 = [1,2,3,4,5]
list_2 = [6,7,8]

print(list_1 + list_2)
# Output
[1, 2, 3, 4, 5, 6, 7, 8]

print(list_1)
# Output
[1, 2, 3, 4, 5]

print(list_2)
# Output
[6, 7, 8]
```

If you read through the above code snippet carefully, you can see the following. 

* `list_1 + list_2` does not add items from `list_2` to `list_1`.
* Instead, it creates a _new list_ containing items from both `list_1` and `list_2`.
* Therefore, `list_1` and `list_2` remain unchanged.

What if we want to modify `list_1` instead of creating a new list? Well, let's do just that using the `append()`and `extend()` methods in the next section.

## How to Use the append() Method in Python

In this section, we'll add items from `list_2` to `list_1` using list methods. Considering the same example lists from the previous section, let's now try to modify `list_1` by adding elements from `list_2` to it.

The code snippet below calls the `append()` method on `list_1` with `list_2` as the argument.

```python
# Let's append list_2 to list_1
list_1.append(list_2)
print(list_1)

# Output
[1, 2, 3, 4, 5, [6, 7, 8]]


# print the length of list_1
print(len(list_1))

# Output
6
```

We see that `list_2` has been appended as a _single list item at the end of_ `list_1` .   
This means that the length of `list_1` _increases by 1_ after the `append()` operation.

What if we would like to add items from `list_2` to `list_1` not as a single list at the end of `list_1` but as individual items? Let's do that in the next section.

## How to Use the extend() Method in Python

Before we start to use the `extend()` method, let's do the following.

* Loop through `list_2`
* _Append_ each item from `list_2` to `list_1`

```python
for item in list_2:
  list_1.append(item)

print(list_1)

# Output
[1, 2, 3, 4, 5, 6, 7, 8]
```

We've now added all items from `list_2` to `list_1`just the way we wanted. 😀  
We can do the same thing by calling the `extend()` method on `list_1` with `list_2` as the argument. You can see how this works in the code snippet below:

```python
# Let's extend list_1 with items from list_2
list_1.extend(list_2)
print(list_1)

# Output
[1, 2, 3, 4, 5, 6, 7, 8]

# print the length of list_1
print(len(list_1))

# Output
8
```

So if you extend a list of length `len1` with a list of length `len2` ,   
the length of the list on which the `extend()` method is called is `len1 + len2`.

### Are there any caveats yet?

What if we wish to add a single item and not the entire list (or any iterable) to our existing list? In the following example, let's add the boolean value `True` to `list_1` using `append()`as shown below.

```python
list_1 = [1,2,3,4,5]
list_1.append(True)
print(list_1)

# Output
[1, 2, 3, 4, 5, True]
```

What if we try using `extend()` to do the same thing as above? 

```python
list_1 = [1,2,3,4,5]
list_1.extend(True)
print(list_1)

# Output
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-9e4e0d6da67b> in <module>()
      1 list_1 = [1,2,3,4,5]
----> 2 list_1.extend(True)
      3 print(list_1)

TypeError: 'bool' object is not iterable
```

Oh, doing so throws an error. 😢 Let's try to parse the error message that is returned.  `TypeError: 'bool' object is not iterable`. This means that our argument was of an _incorrect type_. 

The `extend()` method requires the argument to be iterable. Internally, the `extend()` method works by looping through the iterable and adding each item in the iterable to the first list. Lists, sets, tuples and strings are all examples of iterables. 

Any object that you can loop through and access individual items is an **iterable**.  
Note that the general syntax for using the `extend()` method is `list_name.extend(iterable)`.

## Let's Try extend() and append() on Strings

Strings are essentially a sequence of characters and are therefore iterable. Let's try using the `extend()` and `append()` methods on `list_1` with a string as an argument.

Let's add the string _'Happy'_ to `list_1` using the `append()` method.

```python
list_1 = [1,2,3,4,5]
list_1.append('Happy')
print(list_1)

# Output
[1, 2, 3, 4, 5, 'Happy']
```

Let's now try adding the same string using the `extend()` method. This time we shouldn't get an error. Rather, the extend method should loop through the string and add each character to `list_1`. 

Let's check to see that this works in the following code example.🙂

```python
list_1 = [1,2,3,4,5]
list_1.extend('Happy')
print(list_1)

# Output
[1, 2, 3, 4, 5, 'H', 'a', 'p', 'p', 'y']
```

It's fairly intuitive to see that the `append()` method runs in _constant time_, while the `extend()` method should have a runtime that's proportional to the length of the iterable that's passed as an argument to the method.

## Wrapping Up

I hope this post clarifies how to use the `append()` and `extend()` methods in Python. Thank you for reading, and happy learning and coding!

### Related posts

For a general introduction to Python lists and common list methods, please check this post: [Lists in Python - A Comprehensive Guide.](https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/)

