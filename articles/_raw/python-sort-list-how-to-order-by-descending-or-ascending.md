---
title: Python Sort List – How to Order By Descending or Ascending
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-03T14:49:55.000Z'
originalURL: https://freecodecamp.org/news/python-sort-list-how-to-order-by-descending-or-ascending
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/thisisengineering-raeng-64YrPKiguAE-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, you can sort data by using the sorted() method or sort() method.\
  \ \nIn this article, I will provide code examples for the sorted() and sort() methods\
  \ and explain the differences between the two.\nWhat is the sort() method in Python?\n\
  This meth..."
---

In Python, you can sort data by using the `sorted()` method or `sort()` method. 

In this article, I will provide code examples for the `sorted()` and `sort()` methods and explain the differences between the two.

## What is the sort() method in Python?

This method takes a list and sorts it in place. This method does not have a return value.

In this example, we have a list of numbers and we can use the `sort()` method to sort the list in ascending order. 

```py
my_list = [67, 2, 999, 1, 15]

# this prints the unordered list
print("Unordered list: ", my_list)

# sorts the list in place
my_list.sort()

# this prints the ordered list
print("Ordered list: ", my_list)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-1.41.09-PM.png)

If the list is already sorted then it will return None in the console. 

```py
my_list = [6, 7, 8, 9, 10]

# this will return None because the list is already sorted
print(my_list.sort())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-1.30.28-PM.png)

The `sort()` method can take in two optional arguments called `key` and `reverse`. 

`key`  has the value of a function that will be called on each item in the list. 

In this example, we can use the `len()` function as the value for the `key` argument. `key=len` will tell the computer to sort the list of names by length from smallest to largest. 

```py
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]

print("Unsorted: ", names)
names.sort(key=len)
print("Sorted: ", names)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-2.11.37-PM.png)

`reverse` has a boolean value of `True` or `False`. 

In this example, `reverse=True` will tell the computer to sort the list in reverse alphabetical order.

```py
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]

print("Unsorted: ", names)
names.sort(reverse=True)
print("Sorted: ", names)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-2.25.43-PM.png)

## How to use the sorted() method in Python

This method will return a new sorted list from an iterable. Examples of iterables would be lists, strings, and tuples.

One key difference between `sort()` and `sorted()` is that `sorted()` will return a new list while `sort()` sorts the list in place. 

In this example, we have a list of numbers that will be sorted in ascending order. 

```py
sorted_numbers = sorted([77, 22, 9, -6, 4000])

print("Sorted in ascending order: ", sorted_numbers)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.07.42-PM.png)

The `sorted()` method also takes in the optional `key` and `reverse` arguments. 

In this example, we have a list of numbers sorted in descending order. `reverse=True` tells the computer to reverse the list from largest to smallest. 

```py
sorted_numbers = sorted([77, 22, 9, -6, 4000], reverse=True)

print("Sorted in descending order: ", sorted_numbers)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.15.06-PM.png)

Another key difference between `sorted()` and `sort()` is that the `sorted()` method accepts any iterable whereas the `sort()` method only works with lists. 

In this example, we have a string broken up into individual words using the `split()` method. Then we use `sorted()` to sort the words by length from smallest to largest.  

```py
my_sentence = "Jessica found a dollar on the ground"

print("Original sentence: ", my_sentence)
print(sorted(my_sentence.split(), key=len))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.42.55-PM.png)

We can also modify this example and include the `key` and `reverse` arguments.

This modified example will now sort the list from largest to smallest. 

```py
my_sentence = "Jessica found a dollar on the ground"

print("Original sentence: ", my_sentence)
print(sorted(my_sentence.split(), key=len, reverse=True))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.48.21-PM.png)

We can also use the `sorted()` method on `tuples`. 

In this example, we have a collection of `tuples` that represents the band student's name, age and instrument.

```py
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]
```

We can use the `sorted()` method to sort this data by the student's age. The `key` has the value of a `lambda` function which tells the computer to sort by age in ascending order. 

A `lambda` function is an anonymous function without a name. You can define this type of function by using the `lambda` keyword. 

```py
lambda student: student[1]
```

To access a value in a `tuple`, you use bracket notation and the index number you want to access. Since we start counting at zero, the age value would be `[1]`. 

Here is the complete example.

```py
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]

print(sorted(band_students, key=lambda student: student[1]))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-9.05.22-PM.png)

We can modify this example and sort the data by instrument instead. We can use `reverse` to sort the instruments through reverse alphabetical order. 

```py
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]

print(sorted(band_students, key=lambda student: student[2], reverse=True))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-9.10.16-PM.png)

## Conclusion

In this article, we learned how to work with Python's `sort()` and `sorted()` methods. 

The `sort()` method only works with lists and sorts the list in place. It does not have a return value. 

The `sorted()` method works with any iterable and returns a new sorted list. Examples of iterables would be lists, strings, and tuples.

Both of these methods have two optional arguments of `key` and `reverse`. 

`key` has the value of a function that will be called on each item in the list. 

`reverse` has a boolean value of `True` or `False`. 


