---
title: Python Reverse List – Reversing an Array in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-06T19:36:06.000Z'
originalURL: https://freecodecamp.org/news/python-reverse-list-reversing-an-array-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-breakingpic-3243.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn how to reverse a list in Python.

  Firstly, I''ll introduce you to lists in Python and you''ll learn how to write them.
  After that, you will see three different ways you can reverse the list items inside
  any list you creat...'
---

In this article, you will learn how to reverse a list in Python.

Firstly, I'll introduce you to lists in Python and you'll learn how to write them. After that, you will see three different ways you can reverse the list items inside any list you create.

Here is what we will cover:

1. [What is a list in Python and how to create one](#introduction)
2. [How to reverse items in a list using the `.reverse()` method](#reverse-method)
3. [How to reverse items in a list using the `reversed()` function ](#reversed-function)
4. [How to reverse items in a list using slicing ](#slicing)


## What Is a List in Python? How to Write a List in Python Example <a name="introduction"></a>

Lists are a built-in data type in Python and one of the most powerful data structures. 

You can think of them as containers for storing multiple (typically related) collections of items under the same variable name.

To create a list in Python, you need to:

- Give the list a name.
- Use the assignment operator, `=`.
- Include `0` or more list items inside square brackets,`[]` – and make sure to separate each list item with a comma.

List items can be homogeneous, meaning they are of the same type.

For example, you can create a list of only numbers or a list of only strings (or text).

Here is how you would create a list of names:

```python
names = ["Johny", "Lenny", "Jimmy", "Timmy"]

# print list contents to the console
print(names)

# check data type for names using the type() function
print(type(names))

# output
# ['Johny', 'Lenny', 'Jimmy', 'Timmy']
# <class 'list'>
```

The example above created a list of names with four values: `Johny`, `Lenny`, `Jimmy`, and `Timmy`.

You can also create only a list of integers (or whole numbers):

```python
my_numbers = [1, 2, 3, 4, 5]

# print list contents to the console
print(my_numbers)

# check the data type for my_numbers using the type() function
print(type(my_numbers))

# output
# [1, 2, 3, 4, 5]
# <class 'list'>
```

List items can also be heterogeneous, meaning they can all be of different data types.

```python
# a list containing strings, integers, and floats (or numbers with a decimal point)

my_information = ["John", "Doe", 34, "London", 1.76]

print(my_information)

# output
# ['John', 'Doe', 34, 'London', 1.76]
```

This is what sets lists apart from arrays. 

Unlike arrays, that only store items of the same type, lists allow for more flexibility. 

Arrays require that items are only of the same data type, whereas lists do not.

Lists are mutable, meaning they are changeable and dynamic – you can update, delete, and add new list items to the list at any time throughout the life of the program.

## How to Reverse Items in a List Using the `.reverse()` Method <a name="reverse-method"></a>

The `.reverse()` method in Python is a built-in method that reverses the list *in place*.

Reversing the list *in place* means that the method modifies and changes the original list. It *doesn't* create a new list which is a copy of the original but with the list items in reverse order.

This method is helpful when you are not concerned about preserving the order of the original list.

The general syntax of the `.reverse()` method looks something like the following:

```python
list_name.reverse()
```

The `.reverse()` method doesn't accept any arguments and doesn't have a return value – it only updates the existing list.

Here is how you would use the `.reverse()` method to reverse a list of integers:

```python
#original list
my_numbers = [1, 2, 3, 4, 5]

# reverse the order of items in my_numbers
my_numbers.reverse()

# print contents of my_numbers to the console
print(my_numbers)

# output
# [5, 4, 3, 2, 1]
```

In the example above, the order of the list items in the original list is reversed, and the original list is modified and updated.

And here is how you would use the method on a list of names:

```python
names = ["Johny", "Lenny", "Jimmy", "Timmy"]

# reverse the order of items in names
names.reverse()

# print contents of names to the console
print(names)

# output
# ['Timmy', 'Jimmy', 'Lenny', 'Johny']
```

## How to Reverse Items in a List Using the `reversed()` Function <a name="reversed-function"></a>

This function is helpful when you want to access the individual list elements in reverse order. 

The general syntax for the `reversed()` function looks something similar to this:

```python
reversed(list_name)
```

The `reversed()` built-in function in Python returns a reversed iterator – an **iterable object** which is then used to retrieve and go through all the list elements in reverse order.

Returning an iterable object means that the function returns the list items in reverse order. It doesn't reverse the list in place. This means that it doesn't modify the original list, nor does it create a new list which is a copy of the original one but with the list items in reverse order.

```python
my_numbers = [1, 2, 3, 4, 5]

my_numbers_reversed = reversed(my_numbers)

# print original list
print(my_numbers)

# check the data type of my_numbers_reversed using the type() function
print(type(my_numbers_reversed))

# output
# [1, 2, 3, 4, 5]
# <class 'list_reverseiterator'>
```

You use the `reversed()` function with a `for` loop to iterate through the list items in reversed order. (If you need a refresher on `for` loops in Python, have a read through [this article](https://www.freecodecamp.org/news/python-for-loop-example-and-tutorial/))

```python
my_numbers = [1, 2, 3, 4, 5]

for number in reversed(my_numbers):
  print(number)
  
# output
# 5
# 4
# 3
# 2
# 1
```

If you then print the contents of the original list to the console, you will see that the order of the items is preserved, and the original list is not modified:

```python
my_numbers = [1, 2, 3, 4, 5]

for number in reversed(my_numbers):
  print(number)

print(my_numbers)

# output
# 5
# 4
# 3
# 2
# 1
# [1, 2, 3, 4, 5]
```

This is because the `reversed()` function takes a list as an argument and returns an iterator in reverse order. 

It will not make any changes to the existing list, and it will not create a new one.

This function doesn't reverse the list permanently, only temporarily during the execution of the `for` loop on the original list.

But what if you want to create a new list that will be a copy of the original one but with the items in reversed order using the `reversed()` function?

You can pass the result of the `reversed()` operation as an argument to the `list()` function, which will convert the iterator to a list, and store the final result in a variable:

```python
my_numbers = [1, 2, 3, 4, 5]

my_numbers_reversed = list(reversed(my_numbers))

# original list
print(my_numbers)

# new list, which is a copy of the original one with list items in reverse order
print(my_numbers_reversed)

# output
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]
```

## How to Reverse Items in a List Using Slicing <a name="slicing"></a>

Another way of reversing lists in Python is by using slicing. 

Slicing is one of the fastest ways to reverse a list in Python and offers a concise syntax. That said, it is more of an intermediate to advanced feature and not that beginner friendly compared to the `.reverse()` method, which is more intuitive and self-descriptive.

Let's go over a quick overview of how slicing works.

The general syntax looks something like the following:

```python
list_name[start:stop:step]
```

Let's break it down:

`start` is the beginning index of the slice, inclusive. 
 
Indexing in Python and Computer Science starts at `0`. 
 
The default value of `start` is `0`, and it grabs the first item from the beginning of the list. 

If you want to get the first item from the end of the list, the value would be `-1`.

```python
my_numbers = [1,2,3,4,5,]

slicing_my_numbers = my_numbers[-1:]

print(slicing_my_numbers)

# output
# [5]
```

`stop` is the ending index position and where you want the slicing to stop, not inclusive – it does not include the element located at the index you specify.

For example, if you want to slice the list from the beginning up until the item with the index `3`, here is what you would do:

```python
# the item at index 3 is the integer 4
my_numbers = [1,2,3,4,5,]

slicing_my_numbers = my_numbers[:3]

# the integer 4 is not included in the result
print(slicing_my_numbers)

# output
# [1, 2, 3]
```

`step` is the increment value, with the default value being `1`.

Now, when it comes to using slicing for reversing a list, you would need to use the reverse slicing operator `[::-1]` syntax. This sets the step to `-1` and gets all items in the list in reverse order.

```python
# original list
my_numbers = [1,2,3,4,5]

# reversing original list
my_numbers_reversed = my_numbers[::-1]

# print original list
print(my_numbers)

# print new list with the items from the original list in reverse order
print(my_numbers_reversed)

# output
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]
```

The slicing operator does not modify the original list. Rather it returns a new list, which is a copy of the items from the original list in reverse order.

## Conclusion

And there you have it! You now know how to reverse any list in Python.

I hope you found this tutorial helpful.

To learn more about the Python programming language, check out freeCodeCamp's [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thank you for reading and happy coding!


