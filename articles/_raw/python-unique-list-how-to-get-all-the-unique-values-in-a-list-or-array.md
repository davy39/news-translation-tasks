---
title: Python Unique List – How to Get all the Unique Values in a List or Array
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-17T16:51:44.000Z'
originalURL: https://freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/skye-studios-NDLLFxTELrU-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Amy Haddad

  Say you have a list that contains duplicate numbers:

  numbers = [1, 1, 2, 3, 3, 4]


  But you want a list of unique numbers.

  unique_numbers = [1, 2, 3, 4]


  There are a few ways to get a list of unique values in Python. This article will
  sh...'
---

By Amy Haddad

Say you have a list that contains duplicate numbers:

```python
numbers = [1, 1, 2, 3, 3, 4]
```

But you want a list of _unique_ numbers.

```python
unique_numbers = [1, 2, 3, 4]
```

There are a few ways to get a list of unique values in Python. This article will show you how.

# Option 1 – Using a Set to Get Unique Elements

Using a **`set`** one way to go about it. A set is useful because it contains unique elements.

You can use a set to get the unique elements. Then, turn the set into a list. 

Let’s look at two approaches that use a set and a list. The first approach is verbose, but it’s useful to see what’s happening each step of the way.

```python
numbers = [1, 2, 2, 3, 3, 4, 5]


def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(get_unique_numbers(numbers))
# result: [1, 2, 3, 4, 5]
```

Let’s take a closer look at what’s happening. I’m given a list of numbers, **`numbers`**. I pass this list into the function, **`get_unique_numbers`**.

Inside the function, I create an empty list, which will eventually hold all of the unique numbers. Then, I use a **`set`** to get the unique numbers from the **`numbers`** list.

```python
unique_numbers = set(numbers)
```

I have what I need: the unique numbers. Now I need to get these values into a list. To do so, I use a for loop to iterate through each number in the set.

```python
for number in unique_numbers:
       list_of_unique_numbers.append(number)
```

On each iteration I add the current number to the list, `list_of_unique_numbers`. Finally, I return this list at the end of the program.

There’s a shorter way to use a set and list to get unique values in Python. That’s what we’ll tackle next.

### A Shorter Approach with Set

All of the code written in the above example can be condensed into one line with the help of Python’s built-in functions.

```python
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
# Result: [1, 2, 3, 4, 5]
```

Although this code looks very different from the first example, the idea is the same. Use a set to get the unique numbers. Then, turn the set into a list.

```python
unique_numbers = list(set(numbers))
```

It’s helpful to think “inside out” when reading the above code. The innermost code gets evaluated first: **`set(numbers)`**. Then, the outermost code is evaluated: **`list(set(numbers))`**.

# Option 2 – Using Iteration to Identify Unique Values

Iteration is another approach to consider. 

The main idea is to create an empty list that’ll hold unique numbers. Then, use a for loop iterate over each number in the given list. If the number is already in the unique list, then continue on to the next iteration. Otherwise, add the number to it. 

Let's look at two ways to use iteration to get the unique values in a list, starting with the more verbose one.

```python
numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


print(get_unique_numbers(numbers))
# Result: [20, 30, 40]
```

Here’s what’s happening each step of the way. First, I’m given a list of numbers, **`numbers`**. I pass this list into my function, **`get_unique_numbers`**.

Inside the function, I create an empty list, **`unique`**. Eventually, this list will hold all of the unique numbers. 

I use a for loop to iterate through each number in the **`numbers`** list.

```python
 for number in numbers:
       if number in unique:
           continue
       else:
           unique.append(number)
```

The conditional inside the loop checks to see if the number of the current iteration is in the **`unique`** list. If so, the loop continues to the next iteration. Otherwise, the number gets added to this list.

Here’s the important point: only the unique numbers are added. Once the loop is complete, then I return **`unique`** which contains all of the unique numbers.

## A Shorter Approach with Iteration

There’s another way to write the function in fewer lines.

```python
numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique
#Result: [20, 30, 40]

```

The difference is the conditional. This time it’s set up to read like this: if the number is not in **`unique`**, then add it.

```python
if number not in unique:
    unique.append(number)
```

Otherwise, the loop will move along to the next number in the list, **`numbers`**. 

The result is the same. However, it’s sometimes harder to think about and read code when the boolean is negated. 

There are other ways to find unique values in a Python list. But you’ll probably find yourself reaching for one of the approaches covered in this article.

_I write about learning to program, and the best ways to go about it on [amymhaddad.com](http://amymhaddad.com/). Follow me on Twitter: [@amymhaddad](https://twitter.com/amymhaddad)._  


  


  


  

