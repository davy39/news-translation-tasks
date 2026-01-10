---
title: List Comprehension in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-18T16:20:35.000Z'
originalURL: https://freecodecamp.org/news/list-comprehension-in-python-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/christian-wiediger-WkfDrhxDMC8-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Lists are a helpful and frequently used feature in Python. \nAnd list comprehension\
  \ gives you a way to create lists while writing more elegant code that is easy to\
  \ read.\nIn this beginner-friendly article, I'll give an overview of how list comprehensio..."
---

Lists are a helpful and frequently used feature in Python. 

And list comprehension gives you a way to create lists while writing more elegant code that is easy to read.

In this beginner-friendly article, I'll give an overview of how list comprehension works in Python. I'll also show plenty of code examples along the way.

Let's get started!

## How to use a `for` loop to create a list in Python

One way to create a list in Python is by using a `for` loop.

For example, you can use the `range()` function to create a list of numbers ranging from 0 - 4.

```python
#first create an empty list
my_list = []

#iterate over the numbers 0 - 4 using the range() function
#range(5) creates an iterable, starting from 0 up to (but not including) 5
#Use the .append() method to add the numbers 0 - 4 to my_list

for num in range(5):
    my_list.append(num)
    
#print my_list
print(my_list)

#output
#[0, 1, 2, 3, 4]
```

What if you already have a list of numbers, but want to create a new list with their squares?

You could again use a `for` loop, like so:

```python
#initial list of numbers
numbers = [1,2,3,4,5,6]

#create a new,empty list to hold their squares
square_numbers = []

#iterate over initial list
#multiply each number by itself
#use .append() method, to add the square to the new list, square_numbers

for num in numbers: 
    square_numbers.append(num * num)

#print new list
print(square_numbers)

#output
#[1, 4, 9, 16, 25, 36]
```

But there is a quicker and more succinct way to achieve the same results – by using list comprehension.

## What is list comprehension in Python? A syntax overview

When you're analyzing and working with lists in Python, you'll often have to manipulate, modify, or perform calculations on every single item in the list, all at once.

You may also need to create new lists from scratch, or create a new list based on the values of an already existing list.

List comprehension is a fast, short, and elegant way to create lists compared to other iterative methods, like `for` loops.

The general syntax for list comprehension looks like this:

```
new_list = [expression for variable in iterable]
```

Let's break it down:

- List comprehensions start and end with opening and closing square brackets, `[]`.
- Then comes the `expression` or operation you'd like to perform and carry out on each value inside the current iterable. The results of these calculations enter the new list.
- The `expression` is followed by a `for` clause.
- `variable` is a temporary name you want to use for each item in the current list that is going through the iteration.
- The `in` keyword is used to loop over the iterable.
- `iterable` can be any Python object, such as a list, tuple, string and so on.
- From the iteration that was performed and the calculations that took place on each item during the iteration, new values were created which are saved to a variable, in this case `new_list`. **The old list (or other object) will remain unchanged**.
- There can be an optional `if` statement and additional `for` clause.

## How to use list comprehension in Python

Using the same example from earlier on, here is how you'd create a new list of numbers from 0 - 4 with the `range()` function in just one single line, using list comprehension:

```python
new_list = [num for num in range(5)]

print(new_list)

#output
#[0, 1, 2, 3, 4]
```

This has the same output as the `for` loop example, but with significantly less code!

Let's break it down:

- the iterable in this case is a sequence of numbers from 0 to 4, using `range(5)`. `range()` constructs a list of numbers.
- You use the `in` keyword to iterate over the numbers.
- The `num` following the `for` clause is a variable, a temporary name for each value in the iterable. So `num` would be equal to `0` in the first iteration, then `num` would be equal to `1` in the next iteration and so on, until it reached and equalled the number 4, where the iteration would stop.
- The `num` before the `for` clause is an expression for each item in the sequence.
- Finally, the new list (or other iterable) that is created gets stored in the variable `new_list`.

You can even perform mathematical operations on the items contained in the iterable and the result will be added to the new list:

```python
new_list = [num * 2 for num in range(5)]

print(new_list)

#output
#[0, 2, 4, 6, 8]
```

Here each number in `range(5)` will be multiplied by two and the new value will be stored in the variable `new_list`.

What if you had a pre-existing list where you wanted to manipulate and modify each item in it? This would be similar to the example from earlier on, where we created a list of squares.

Again, you can achieve that with just one line of code, using list comprehension:

```python
#initial list
numbers = [1,2,3,4,5,6]

#new list
#num * num is the operation that takes place to create the squares

square_numbers = [num * num for num in numbers]

print(square_numbers)

#output
[1, 4, 9, 16, 25, 36]
```

### How to use conditionals with list comprehension in Python

Optionally, you can use an `if` statement with a list comprehension.

The general syntax looks like this:

```
new_list = [expression for variable in iterable if condition == True]
```

Conditionals act as a filter and add an extra check for additional precision and customisation when creating a new list.

This means that the value in the expression has to meet certain criteria and a certain condition you speficy, in order to go in the new list.

```python
new_list = [num for num in range(50) if num % 2 == 0]

print(new_list)

#output
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

In the example above, only the values where the condition `num % 2 == 0` is checked and evaluates to True will enter `new_list`.

The modulo operator is used on every single one of the numbers in the sequence of numbers starting from 0 and ending in 49.

If the remainder of the numbers when divided by 2 is 0, then and only then does it enter the list.

So in this case, it creates a list of only even numbers.

You can then make it as specific as you want.

For example, you could add more than one condition, like so:

```python
new_list = [num for num in range(50) if  num > 20 and num % 2 == 0]

print(new_list)

#output
#[22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

In this example, there are two conditions `num > 20` and `num % 2 == 0`. 

The `and` operator indicates that *both* have to be met in order for the value to be added to the new list.

The values that don't meet the conditions are excluded and are not added.

### How to use list comprehension on strings in Python

You can create a new list with the individual characters contained in a given string.

```python
fave_language_chars = [letter for letter in "Python"]

print(fave_language_chars)

#output
#['P', 'y', 't', 'h', 'o', 'n']
```

The new list that gets created is comprised of all the separate letters contained in the string "Python", which acts as an iterable.

Just like numbers, you can perform operations on the characters contained in a string and customize them depending on how you want them to be in the new list you create.

If you wanted all letters to be uppercase, you would do the following:

```python
fave_language_chars_upper = [letter.upper() for letter in "Python"]

print(fave_language_chars_upper)

#output
#['P', 'Y', 'T', 'H', 'O', 'N']
```

Here you use the `.upper()` method to convert every single letter in "Python" to uppercase and add them to the `fave_language_chars_upper` variable.

The same goes if you wanted all your letters to be lowercase - you'd instead use the `lower()` method.

## Conclusion

And there you have it! You now know the basics of list comprehension in Python.

It offers an elegant and concise syntax for creating new lists based on existing lists or other iterables.

If you're interested in learning more about Python, freeCodeCamp has a [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

In this project-based curriculum, you'll start with learning programming fundamentals and advance to more complex subjects such as data structutes. You'll also build five projects to put to practice what you've learned.

Thanks for reading and happy coding!


