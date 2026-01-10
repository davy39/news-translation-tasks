---
title: Python Index – How to Find the Index of an Element in a List
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-02T20:59:13.000Z'
originalURL: https://freecodecamp.org/news/python-index-find-index-of-element-in-list
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-olya-kobruseva-5408919.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Suchandra Datta\nWhen you're learning to code, you eventually learn\
  \ about lists and the different operations you can perform on them. \nIn this article,\
  \ we'll go through how you can find the index of a particular element which is stored\
  \ in a list in..."
---

By Suchandra Datta

When you're learning to code, you eventually learn about lists and the different operations you can perform on them. 

In this article, we'll go through how you can find the index of a particular element which is stored in a list in Python.

## What is a List in Python?

A list in Python is an in-built data type which allows us to store a bunch of different values, like numbers, strings, datetime objects and so on. 

Lists are ordered, which means the sequence in which we store the values is important. 

List indices start from zero and end at the length of the list minus one. For more detailed information on list data type, check out [this comprehensive guide](https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/).

Let's see an example of lists:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-173.png)

```python
fruits = ["apple", "orange","grapes","guava"]
type(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

```

Here we created a list of 4 items, where we see that the first item in the list is at index zero, the second item is at index 1, the third item is at index 2, and so on. 

For the fruits list, the valid list indices are 0, 1, 2 and 3.

## How to Find the Index of Items in a List in Python

Let's do the reverse. That is, given a list item, let's find out the index or position of that item in the list. 

```
index = fruits.index('orange')
#The value of index is 1

index = fruits.index('guava')
#The value of index is 3

index = fruits.index('banana')
#This raises a ValueError as banana is not present in list

```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-174.png)

Python lists provide us with the index method which allows us to get the index of the first occurrence of a list item, as shown above. 

We can also see that the index method will raise a VauleError if we try to find the index of an item which does not exist in the list. 

For greater detail on the index method, check out the official docs [here](https://docs.python.org/3/tutorial/datastructures.html).

The basic syntax of the index method is this:

```python
list_var.index(item)
```

We can also specify a sublist in which to search, and the syntax for that is:

```python
list_var.index(item, start_index_of_sublist, end_index_of_sublist)
```

To illustrate this further, let's look at an example. 

Suppose we have a **book_shelf_genres** list where the index signifies the shelf number. We have many shelves containing math books. Shelf numbers also start from zero. We want to know which shelf after shelf 4 has any math books.

```python
book_shelf_genres = ["Fiction", "Math", "Non-fiction", "History", "Math", "Coding", "Cooking", "Math"]
index = book_shelf_genres.index("Math")
#The value of index is 1
```

We can see the problem here: using just `index()` will give the first occurrence of the item in the list – but we want to know the index of "Math" after shelf 4. 

To do that, we use the index method and specify the sublist to search in. The sublist starts at index 5 until the end of the **book_shelf_genres** list, as shown in the code snippet below

```python
index = book_shelf_genres.index("Math", 5)
#The value of index is 7
```

Note that giving the end index of the sublist is optional. To find index of "Math" after shelf number 1 and before shelf number 5, we will simply do this:

```python
index = book_shelf_genres.index("Math", 2, 5)
#The value of index is 4
```

## How to Find the Index of a List Item with Multiple Occurrences in Python

What if we need to know the index of a list item which occurs multiple times in a list? The index method won't give us every occurrence. 

In this case, we can find the multiple occurrences using list comprehension as follows:

```python
book_shelf_genres = ["Fiction", "Math", "Non-fiction", "History", "Math", "Coding", \
                     "Cooking", "Math"]

[i for i in range(0, len(book_shelf_genres)) if book_shelf_genres[i]=="Math"]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-229.png)

As shown in this code snippet, we loop over the indices of the list. At each index we check if the item at that index is Math or not. If it is Math then we store that index value in a list. 

We do this entire process using list comprehension, which is just syntactic sugar that allows us to iterate over a list and perform some operation. In our case we are doing decision making based on the value of list item. Then we create a new list.

With this process, we now know all the shelf numbers which have math books on them.

## How to Find the Index of List Items in a List of Lists in Python

```python
programming_languages = [["C","C++","Java"],["Python","Rust","R"],\
                         ["JavaScript","Prolog","Python"]]

[ (i, x.index("Python")) for i, x in enumerate(programming_languages) if "Python" in x ]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-230.png)

Here we use list comprehension and the index method to find the index of "Python" in each of the sublists. 

We pass the programming_languages list to the enumerate method which goes over each item in list and returns a tuple containing the index and item of the list at that index. 

Each item in programming_languages list is also a list. The in operator then checks whether "Python" is present in this list or not. If present, we store the sublist index and index of "Python" inside the sublist as a tuple. 

The output is a list of tuples. The first item in the tuple specifies the sublist index, and the second number specifies the index within the sublist. 

So (1,0) means that the sublist at index 1 of the programming_languages list has the "Python" item at index 0.

## How to Find the Index of a List Item that May Not Exist in a List in Python

In many cases, we will end up trying to get the index of an item but we are not sure if the item exists in the list or not. 

If we have a piece of code which tries to get index of an item which isn't present in the list, the index() method will raise a ValueError. In the absence of exception handling, this ValueError will cause abnormal program termination. 

Here's two ways in which we can avoid or handle this situation:

```python
books = ["Cracking the Coding Interview", "Clean Code", "The Pragmatic Programmer"]
ind = books.index("The Pragmatic Programmer") if "The Pragmatic Programmer" in books else -1
                                            
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-180.png)

One way is to check using the "in" operator if the item exists in list or not. The in operator has the basic syntax of

```python
var in iterable
```

where iterable could be a list, tuple, set, string or dictionary. If var exists as an item in the iterable, the in operator returns True. Else it returns False. 

This is ideal for our case. We will simply check if an item exists in the list or not and only when it exists we will call index() method. This makes sure that the index() method doesn't raise a ValueError.

If we don't want to spend time checking if an item exists in the list or not, especially for large lists, we can handle the ValueError like this:

```python
books = ["Cracking the Coding Interview", "Clean Code", "The Pragmatic Programmer"]
try:
    ind = books.index("Design Patterns")
except ValueError:
    ind = -1
ind
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-181.png)

## Wrapping up

Today we learnt how to find the index of an item in a list using the `index()` method. 

We also saw how to use the index method over sublists, how to find the index of items in a list of lists, how to find every occurrence of an item in a list, and how to check for items in lists which may not be present. 

I hope you found this article useful and an enjoyable read. Happy coding!

