---
title: Python Sorted List – And How to Sort or Reverse an Array in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-24T17:24:10.000Z'
originalURL: https://freecodecamp.org/news/python-sort-lists-and-reverse-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Python-Sorted-List---And-How-to-Sort-or-Reverse-an-Array-in-Python--by-Shittu-Olumide-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nArrays and lists in Python are very interesting data\
  \ structures. \nBoth lists and arrays consist of ordered, mutable items – but arrays\
  \ contain items of the same type, while lists can store multiple types of items.\
  \ \nIn this article, ..."
---

By Shittu Olumide

Arrays and lists in Python are very interesting data structures. 

Both lists and arrays consist of ordered, mutable items – but arrays contain items of the same type, while lists can store multiple types of items. 

In this article, we will learn how to reverse an array using slicing and the `reverse()` method. We will also talk about how to sort lists in Python using the `sort()` method, `sorted()` function, and the `heapq` module. 

## Outline

1. How to reverse an array in Python.  
- Using the slicing.  
- Using the `reverse()` method.
2. How to sort a list in Python.  
- Using the `sort()` method.  
- Using the `sorted()` function.  
- Using the `heapq` module.

## How to Reverse an Array in Python

Reversing an array is often a more effective brute-force approach for a variety of issues. And sometimes we might need to search through an array starting from the back.

### How to reverse an array using slicing

Slicing allows us to access a specific range of elements in a sequence, such as an array, list, or string. We can specify the range we want to access using two indices separated by a colon. 

To reverse the array, we can specify a step value of `-1`, which means we will start from the end of the array and move towards the beginning, in reverse order. 

The syntax of slicing to reverse an array in Python looks like this:

```py
arrayName[::-1]

```

Here's the code to reverse an array using slicing:

```py
# import the array module
import array
    
# declare an array
x = array.array("i", [1, 2, 3, 4, 5])

#slicing the array
print('The reversed array is ', x[::-1])

```

Output:

```bash
The reversed array is  array('i', [5, 4, 3, 2, 1])

```

### How to reverse an array using the `reverse()` method

Python also provides a `reversed()` method for arrays. The array is not duplicated by the `reversed()` method, nor is the original array altered in any way. 

Instead, an iterator is returned. The purpose of this method is to simplify reverse iteration over sequences.

```py
import array as arr

# initializing array with integers
x = arr.array("i", [1, 2, 3, 4, 5])

# passing the array in reversed()
reversed(x)

print("The reversed array: ", x)

```

Output:

```bash
The reversed array:  array('i', [1, 2, 3, 4, 5])

```

Note that the array's order will also be reversed if it contains mutable items like dictionaries, lists, or other arrays. In order to prevent this, we can first use the `copy()` method to make a shallow copy of the array.

## How to Sort a List in Python

A sorted list is one that keeps its items in order, usually in ascending order. A sorted list is a data structure that enables us to maintain the original order of elements while sorting them, in contrast to the `sorted()` function. Because a new sorted list is not created, the original list is modified in place.

Let's consider the methods we can use to sort a list in Python.

### How to sort a list using the `sort()` method

The `sort()` method is a built-in function of the list class that sorts the elements of the list in ascending order. The syntax of the `sort()` method is as follows:

```py
list.sort(key=None, reverse=False)

```

The function of one argument to extract a comparison key from each element in the list is specified by the key parameter. We can specify whether to sort the list in ascending or descending order using the reverse parameter.

Example:

```py
# Creating a list of numbers
num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sorting the list in ascending order
num.sort()

print(num)

```

Output:

```bash
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

```

As we can see the list is sorted from 1 to 9 without any errors, although some of the elements in the list gets printed twice.

### How to sort a list using the `sorted()` function.

The `sorted()` function is a built-in function that returns a new sorted list from the given iterable. The syntax of the `sorted()` function is as follows:

```py
sorted(iterable, key=None, reverse=False)

```

The sequence of elements that need to be sorted makes up the iterable parameter. A function of one argument is specified by the key parameter in order to extract a comparison key from each element of the list. You can sort a list in either ascending or descending order using the reverse parameter.

Here is an example:

```py
# Creating a list of numbers
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Creating a new sorted list
sorted_nums = sorted(nums)

print(sorted_nums)

```

Output:

```bash
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

```

### How to sort a list using the `heapq` module

Python's heapq module offers functions for working with heap queues. A function called `heappushpop()` in the `heapq` module allows us to push an item onto a heap, pop it, and then return the smallest item from it.

Here is an illustration of how to use `heappushpop()` to order a list of numbers in ascending order:

```py
import heapq

# define a function that takes in a list
def sort_list(lst):
    heap = []
    for item in lst:
        heapq.heappush(heap, item)

    sorted_lst = []
    for i in range(len(heap)):
        sorted_lst.append(heapq.heappop(heap))

    return sorted_lst

# Example usage:
lst = [5, 2, 9, 1, 5, 6]
sorted_lst = sort_list(lst)
print(sorted_lst)

```

Output:

```bash
[1, 2, 5, 5, 6, 9]

```

Here is another example:

```py
import heapq

my_list = [3, 5, 2, 7, 1]

# Convert the list into a heap
heapq.heapify(my_list)

# Create an empty list to store the sorted values
sorted_list = []

# Pop the smallest value from the heap and add it to the sorted list until the heap is empty
while my_list:
    sorted_list.append(heapq.heappop(my_list))

print(sorted_list)

```

Output:

```bash
[1, 2, 3, 5, 7]

```

## Conclusion

Sorting and reversing a list or array are common tasks in Python, and there are multiple ways to accomplish these tasks. We discussed three popular approaches for sorting lists in Python – using the built-in `sort()` method and `sorted()` function and the `heapq` module.

Additionally, we explored how to reverse an array using both the built-in `reverse()` function and slicing. 

Sorting and reversing lists and arrays can be an important part of data processing and analysis, and it is essential to understand how to implement these tasks efficiently in Python.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

