---
title: Python Reverse List – How to Reverse a Range or Array
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-22T14:54:14.000Z'
originalURL: https://freecodecamp.org/news/python-reverse-list-how-to-reverse-a-range-or-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/markus-winkler-Q2J2qQsoYH8-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this tutorial, you''ll learn some of the different ways you can reverse
  lists and list ranges in Python. And we''ll look at some coding examples along the
  way.

  Let''s get started!

  How to create a range in Python

  An efficient way to create a list of a...'
---

In this tutorial, you'll learn some of the different ways you can reverse lists and list ranges in Python. And we'll look at some coding examples along the way.

Let's get started!

## How to create a range in Python

An efficient way to create a list of a range of numbers in Python is to use the built-in `range()` function.

To create a list with a range of numbers, you use the `list()` constructor and inside that, the `range()` function.

The range function takes up to three paramaters – the `start, stop, and step` parameters, with the basic syntax looking something like this:

`range(start, stop, step)`.

The `start` parameter is the number from which the counting will start.

The `stop` parameter is the number up to – but not including – the one where the counting will stop.

The `step` parameter is the number that determines how numbers will be incremented.

Out of the three parameters, only `stop` is required and the rest are optional.

If you only include the `stop` parameter, keep in mind that by default the counting starts at 0 and then the counting ends one number before the one you specified.

For example:

```python
#creates a list of numbers that 
#start at 0 and end at 3, not 4.

my_range = list(range(4))

print(my_range)
#output
#[0, 1, 2, 3]
```

So, here is how you would put all these together in order to create a list of a range of numbers:

```python
#creates a list of range of numbers:
#starting from 0
#up to, but not including, 10
# and the counting is incremented by 1

my_range = list(range(0, 10, 1))

#print to the console
print(my_range)

#output
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#check type using the built-in type() method
print(type(my_range))

#output
#<class 'list'>
```

## How to reverse a range in Python

To reverse a range of numbers in Python with the `range()` function, you use a negative step, like `-1`.

The example below creates a list of a range of numbers starting from 9 up to, but not including, -1 (so the counting stops at 0) and the counting of the sequence is decremented by 1 each time:

```python
my_range = list(range(9, -1, -1))

print(my_range)
#output
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(type(my_range))
#<class 'list'>
```

When *reversing* a list, you need to include the `start` and `step` parameters.

## How to reverse an array in Python

An array in programming is an ordered collection of items, all of which are of the same data type.

Each item in the collection has an its own index number.

However, unlike other programming languages, arrays aren't a built-in data structure in Python.

Instead, you use lists, and Python offers a few ways to reverse them.

## How to reverse a list in Python using the `.reverse()` method

Using this built-in Python method, the list changes *in place*. This means that the original order of the list is affected. 

The initial order of the items gets updated and altered.

For example, say you have the following list:

```python
#initial list
my_list = [10,20,30,40,50]

print("My initial list is: ",my_list)

#output
#My initial list is:  [10, 20, 30, 40, 50]
```

To change `my_list`'s items to have an order of `50, 40, 30, 20,10`, you'd do:

```python
#initial list
my_list = [10,20,30,40,50]

#reverse order of items
my_list.reverse()

print("This is what the list looks like now: ", my_list)

#output
#This is what the list looks like now:  [50, 40, 30, 20, 10]
```

You see that the initial order of the list has now changed and the elements inside it have been reversed.

## How to reverse a list in Python using the slicing operator

The slicing operator works similarly to the `range()` function you saw earlier on.

It also accepts the `start`, `stop`, `step` arguments.

The syntax looks like this: `start:end:step`.

For example:

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[1:3:1]

print(my_list2)

#output
#[20, 30]
```

In the example above, we wanted to fetch the items starting from index 1 up to, but not including, the item with index 3, incrementing one number at a time.

Indexing in Python starts from 0, so the first element has an index of 0, the second element has an index of 1, and so on.

When you want to print all items, you use one of the two following ways:

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[:]

#or..

my_list2 = my_list[::]

#print to the console
print(my_list2)

#output
#10, 20, 30, 40, 50]
```

So, you either use one or two colons to output all items contained in the list.

Now, to reverse all the items inside the list using the slicing operator, you have to include the step.

In this case you use two colons to represent the `start` and `end` arguments, and a negative step for decrementing:

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[::-1]

print(my_list2)

#output
#[50, 40, 30, 20, 10]
```

In this case a new list is created, with the original order of the list not being affected.

## How to reverse a list in Python using the `reversed()` function

Don't confuse this with the `.reverse()` method! The built-in `reversed()` function reverses the order of a list and lets you access each individual item one at a time.

```python
my_list = [10,20,30,40,50]

for num in reversed(my_list): 
    print(num)
    
#output
#50
#40
#30
#20
#10
```

The `reversed()` function accepts a list as an argument and returns an iterable, reversed version of the items contained in the list.

If you wanted to store the return value from the `reversed()` function for later use, you'd instead have to enclose it inside the `list()` constructor and assign the new list to a variable, like so:

```python
#initial list
my_list = [10,20,30,40,50]

#use reversed() function to reverse order of my_list
#store new list that gets created to the variable my_new_list
my_new_list = list(reversed(my_list))

print(my_new_list)
#output
#[50, 40, 30, 20, 10]
```


## Conclusion

And there you have it - you now know the basics of how reversing lists in Python works!

If you want to learn more about Python, freeCodeCamp offers a [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

In this project-based curriculum, you'll start from the ground up. You'll learn programming fundamentals and advance to more complex topics. In the end you'll build 5 projects to put your new skills to practice.

Thanks for reading and happy coding!


