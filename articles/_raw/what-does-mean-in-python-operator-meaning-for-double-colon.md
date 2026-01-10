---
title: 'What Does :: Mean in Python? Operator Meaning for Double Colon'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-30T07:21:33.000Z'
originalURL: https://freecodecamp.org/news/what-does-mean-in-python-operator-meaning-for-double-colon
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/nikolai-chernichenko-hFBsF-CX5eQ-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'You can use the double colon (::) in Python to slice or extract elements
  in a collection such as a list or string.

  In this article, you''ll learn the syntax and how to use :: to slice a list in Python.
  You''ll also learn how to use the parameters assoc...'
---

You can use the double colon (`::`) in Python to slice or extract elements in a collection such as a list or string.

In this article, you'll learn the syntax and how to use `::` to slice a list in Python. You'll also learn how to use the parameters associated with this method of slicing. 

## Python Double Colon (`::`) Syntax

Here's what the syntax for the double colons looks like:

```txt
collection[start:stop:step]
```

In the syntax above: 

* **collection** denotes the data collection (list, string, array, and so on). 
* **start** denotes where the slicing operation should start from.
* **stop** denotes where the operation should stop. 
* **step** denotes the sequence of iterating through the elements.

If you look closely at the syntax, you can see how the colons separate each parameter. 

In the next, you'll see examples of how the parameters above work. 

### Python Double Colon Example #1

In this example, we'll focus on the `start` parameter:

```python
number_list = [2,4,6,8,10,12]

print(number_list[2:])
# [6, 8, 10, 12]
```

In the example above, we created a list called `number_list` with these elements: [2,4,6,8,10,12]. 

We then used the `start` parameter to slice the list starting from the second index: `number_list[2:]`.

Here are the indexes: 

2 => index 0  
4 => index 1  
6 => index 2  
8 => index 3  
10 => index 4  
12 => index 5

Recall that we're slicing from the index 2. So all the elements from the second index to the end of the list will be returned: `[6, 8, 10, 12]`.

This is the same as saying, "Print all the elements of the list starting from the specified index." The specified index will be printed too. 

Note that the `start` parameter comes before the first colon. 

### Python Double Colon Example #2

In this section, you'll see how to use the `stop` parameter. It comes after the first colon and before the second colon. 

Unlike the `start` parameter, the specified index will not be included. The slicing operation will stop at the index that comes before the specified index.

Here's an example: 

```python
number_list = [2,4,6,8,10,12]

print(number_list[:2])
# [2, 4]
```

Similar to the last section, the specified index is 2. Here are the indexes:

2 => index 0  
4 => index 1  
6 => index 2  
8 => index 3  
10 => index 4  
12 => index 5

Using the `stop` parameter, you get all the elements in list that come before the specified index. 

Index 2 in the list is 6. The elements that come before it are 2 and 4 so they get printed out: `[2, 4]`. The other elements are "sliced off". 

### Python Double Colon Example #3

The `step` parameter works in an interesting way. This is used to specify the sequence to be followed while slicing through a collection. 

The `step` parameter comes after the second colon.

Without specifying values for the `start` and `stop` parameters, you have access the whole list. No element gets sliced off.

Since we've already talked about the `start` and `stop` parameters, we'll not assign any value to them. You'll understand the `step` parameter better if we work with all the elements in the list. 

```python
number_list = [2,4,6,8,10,12]

print(number_list[::2])
# [2, 6, 10]
```

We finally have the two colons close to each other: `number_list[::2]`. 

We used a `step` value of 2. This means the list will jump two steps repeatedly during the iteration. 

The first element is 2. Two steps from 2 lands us at 6. Two steps from 6 lands us at 10. Two steps from lands us nowhere because there is no other element to complete the second step. 

You can liken the `step` parameter to walking up the stairs. With our code example, you'd stop and print out an element every time you take two steps. 

## Summary

The double colons (`::`) in Python are used to specify how a slice operation should work. They can be used to slice through some data collections. 

In this article, we saw how to use the `start`, `stop`, and `step` parameters to slice through a list. 

We saw an example for each parameter. This helped in showing the difference between each of them and how they affect the structure of a list. 

Happy coding!

