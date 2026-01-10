---
title: Joining Lists in Python – How to Concat Lists
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-14T16:30:27.000Z'
originalURL: https://freecodecamp.org/news/joining-lists-in-python-how-to-concat-lists
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Joining-Lists-in-Python---How-to-Concat-Lists-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nThe process of combining two or more strings, lists,\
  \ or other data structures into a single entity is known as concatenation in programming.\
  \ \nConcatenation produces a new object with all the components of the original\
  \ objects, arran..."
---

By Shittu Olumide

The process of combining two or more strings, lists, or other data structures into a single entity is known as concatenation in programming. 

Concatenation produces a new object with all the components of the original objects, arranged in the concatenation order.

Concatenation in the context of strings refers to joining one string to the end of another string to create a longer string. For instance, creating the string `"helloworld"` by joining the words `"hello"` and `"world"` together.

Concatenation in the context of lists means that you create a new list that incorporates every element from two or more lists. For instance, the list `[1, 2, 3, 4, 5, 6]` would be created from concatenating the two lists `[1, 2, 3]` and `[4, 5, 6]`.

Concatenation is a common programming operation that is used to combine data for a variety of purposes, including creating reports, handling large data sets, and creating intricate data structures.

## List Concatenation in Python

Concatenation of lists is a common operation in Python programming. In many situations, you might need to merge two or more lists into a single list to perform some operations on the combined data. 

Python offers a variety of methods for concatenating lists, from straightforward built-in functions to more sophisticated methods involving list comprehension and slicing. 

In this article, we'll look at various Python concatenation techniques. By the time you're done reading, you'll know exactly how to concatenate lists in Python and be able to select the approach that works best for your particular use case.

## How to Concatenate Lists Using the `+` Operator

The first and the simplest technique to concatenate two lists is using the  `**+**` operator. It creates a new list by concatenating the two lists together.

Example:

```py
first_list = [1, 2, 3]
second_list = [4, 5, 6]

#concatenating the two lists
concat_list = first_list + second_list

#print the concatenated list
print(concat_list)

```

Output:

```bash
[1, 2, 3, 4, 5, 6]

```

## How to Concatenate Lists Using the `*` Operator

You can use the `*` operator to repeat a list a certain number of times. By repeating a list and concatenating it with itself, we can achieve concatenation of multiple copies of a list.

Example:

```py
first_list = [1, 2, 3]
second_list = first_list * 3

print(second_list)

```

Output:

```bash
[1, 2, 3, 1, 2, 3, 1, 2, 3]

```

## How to Concatenate Lists Using List Comprehension

List comprehension is a concise and readable way to create a new list in Python by iterating over an existing iterable object (like a list, tuple, string, etc.) and applying a transformation or filter to each element in the iterable.

List comprehension syntax:

```py
new_list = [expression for item in iterable if condition]

```

Here, `expression` is the operation or function to apply to each element in the iterable, `item` is a variable that takes on each element of the iterable in turn, `iterable` is the original iterable object, and `condition` is an optional condition that filters which elements to include in the new list.

You can use list comprehension to concatenate multiple lists into a single list. Let's have a look at an example.

```py
#define the lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = [7, 8, 9]

#using list comprehension
fourth_list = [x for lst in [first_list, second_list, third_list] for x in lst]


print(fourth_list)

```

Output:

```bash
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```

## How to Concatenate Lists Using the `append()` Method in a Loop

An element can be added to the end of an existing list in Python by using the `append()` method, which is a built-in function of lists.

The syntax for using `append()` is:

```py
list_name.append(element)

```

From the code, `list_name` is the name of the list to which you want to add an element, and `element` is the value that you want to add to the list.

You can use the `append()` method inside a loop to append the elements of one list to another.

Example:

```py
first_list = [1, 2, 3]
second_list = [4, 5, 6]

for element in second_list:
    first_list.append(element)
    
print(first_list)

```

Output:

```bash
[1, 2, 3, 4, 5, 6]

```

## How to Concatenate Lists Using the `extend()` Method

By concatenating an existing list with another iterable object, the `extend()` method of lists in Python enables you to add multiple elements to an existing list.

The syntax for `extend()` is as follows:

```py
list_name.extend(iterable)

```

Here, `iterable` is any iterable object (such as a list, tuple, string, etc.) that contains the elements you want to add to the list, and `list_name` is the name of the list to which you want to add elements.

You can use the `extend()` method to append all the elements of one list to the end of the original list.

Example:

```py
first_list = [1, 2, 3]
second_list = [4, 5, 6]

#using the extend() method
first_list.extend(second_list)

print(first_list)

```

Output:

```bash
[1, 2, 3, 4, 5, 6]

```

## So When Should You Use Each Method?

**Using the `*` operator**: You can use the `*` operator in list concatenation when you want to repeat a list a certain number of times or to create a new list by repeating the elements of the original list by a scalar value.

**Using the `+` operator**:  This method is simple and easy to read, but it can be inefficient when dealing with large lists as it creates a new list every time it's used.

**Using the `append()` method**: The `append()` method in Python adds an element to the end of a list. You don't typically use it for list concatenation, but rather for adding individual elements to an existing list.  
  
**Using the `extend()` method**: This method involves using the `extend()` method to add elements of one list to the end of another list. The `extend()` method modifies the original list instead of creating a new list, making it more memory efficient than the + operator. But, it can still be slower than the list comprehension method for very large lists.

## Conclusion

In this article, we have explored different ways to concatenate lists in Python, including using the `+` operator, the `*` operator, the `extend()` method, the `append()` method, and list comprehension. We have also discussed the best method you can use for your use case.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

