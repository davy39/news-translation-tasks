---
title: Python For Loop Example – How to Write Loops in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-26T19:01:37.000Z'
originalURL: https://freecodecamp.org/news/python-for-loop-example-how-to-write-loops-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/forLoop.png
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: null
seo_desc: 'If you are just getting started in Python, for loops are one of the fundamentals
  you should learn how to use.

  In the Python programming language, for loops are also called “definite loops” because
  they perform the instruction a certain number of time...'
---

If you are just getting started in Python, for loops are one of the fundamentals you should learn how to use.

In the Python programming language, for loops are also called “definite loops” because they perform the instruction a certain number of times. 

This is in contrast to while loops, or indefinite loops, which execute an action until a condition is met and they are told to stop.

For loops are useful when you want to execute the same code for each item in a given sequence. With a for loop, you can iterate over any iterable data such as lists, sets, tuples, dictionaries, ranges, and even strings.

In this article, I will show you how the for loop works in Python. You will also learn about the keyword you can use while writing loops in Python.

## Basic Syntax of a For Loop in Python

The basic syntax or the formula of for loops in Python looks like this:

```py
for i in data:
    do something
```

- `i` stands for the iterator. You can replace it with anything you want
- `data` stands for any iterable such as lists, tuples, strings, and dictionaries
- The next thing you should do is type a colon and then indent. You can do this with a tab or press the spacebar 4 times.

## Python For Loop Example
As I mentioned above, you can iterate over any iterable data with a for loop.

### How to Iterate Over a String with a For Loop
You can iterate over string as shown below:
```py
name = "freeCodeCamp"

for letter in name:
    print(letter)
```
This will print all the letters in the string individually:
```py
# Output: 
# f
# r
# e
# e
# C
# o
# d
# e
# C
# a
# m
# p
```

What if you want to print the letters in a single line? 

You can do that by passing whitespace to the `end` parameter right inside the `print()` statement. With this, you tell Python that you want whitespace instead of a new line in the console.

```py
name = "freeCodeCamp"

for letter in name:
    print(letter, end=" ")

# Output: f r e e C o d e C a m p 
```

### How to Iterate Over a List with a For Loop

To iterate over a list with the for loop, define the list as separate data and then write the for loop, like this:

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    print(lang)

# Output: 
# Python
# JavaScript
# PHP       
# Rust      
# Solidity  
# Assembly  
```

Don’t forget that you can print all the items in one line with the end keyword:

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    print(lang, end=" ")

# Output: Python JavaScript PHP Rust Solidity Assembly 
```

### How to Iterate Over a Tuple with a For Loop
A tuple is an iterable data type in Python, so you can write a for loop to print the items in it.
```py
footballers_tuple = ("Ronaldo", "Mendy", "Lukaku", "Lampard", "Messi", "Pogba")

for footballer in footballers_tuple:
    print(footballer, end=" ")

# Output: Ronaldo Mendy Lukaku Lampard Messi Pogba 
```

You can get a little more creative by making people know that the names in the tuple represent some active footballers:

```py
footballers_tuple = ("Ronaldo", "Mendy", "Lukaku", "Lampard", "Messi", "Pogba")

for footballer in footballers_tuple:
    print(footballer, "is an active footballer")

# Output: 
# Ronaldo is an active footballer
# Mendy is an active footballer  
# Lukaku is an active footballer 
# Lampard is an active footballer
# Messi is an active footballer  
# Pogba is an active footballer  
```

### How to Iterate Over a Set with For Loop

You can print the individual items in a set with the for loop like this:

```py
soc_set = {"Twitter", "Facebook", "Instagram", "Quora"}

for platform in soc_set:
    print(platform, end=" ")

# Output: Twitter Facebook Instagram Quora
```

You can also get more creative with this. In the example below, with the help of an if statement, I was able to print the platform that is about to be bought by Elon Musk:

```py
soc_set = {"Twitter", "Facebook", "Instagram", "Quora"}

for platform in soc_set:
    if(platform == "Twitter"):
        print(platform, "is about to be bought by Elon Musk.")

# Output: Twitter is about to be bought by Elon Musk.
```

### How to Iterate Over a Dictionary with For Loop

Dictionary is a collection of data in key-value pair form. A dictionary is probably the data type you can do the most with using a for loop.

For example, you can get the keys in a dictionary by looping through it:

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key in fcc_dict:
    print(key, end=" ")

# Output: name type mode paid 
```

You can also get the values with a for loop:

```py
for values in fcc_dict.values():
    print(values , end=" ")

# Output: freeCodeCamp non-profit remote no 
```

You can get the keys and values in a dictionary with a for loop:

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key, value in fcc_dict.items():
    print(key, value)

# Output: 
# name freeCodeCamp
# type non-profit
# mode remote
# paid no
```

I don’t know any other programming language that can do this in such an elegant and clean way!

You can even replace the `key, value` with anything you want and it’ll still work as expected:

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for a, b in fcc_dict.items():
    print(a, b)

# Output: 
# name freeCodeCamp
# type non-profit
# mode remote
# paid no
```

You can also execute a particular instruction when the iteration reaches a certain key. In the example below, I printed “freeCodeCamp is a non-profit organization” to the console when the key equals `type`:

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for a, b in fcc_dict.items():
    # print(a, b)
    if a == "type":
        print("freeCodeCamp is a non-profit organization")

# Output: freeCodeCamp is a non-profit organization
```

### How to Iterate Over Numbers with For Loop by Using the `range()` Function

Iterating through an integer throws the popular `int object not iterable` error in Python. But you can get around this by using the `range()` function to specify that you want to iterate through the numbers between two certain numbers.

The range`()` function accepts two arguments, so you can loop through the numbers within the two arguments. Example below:

```py
for i in range(1, 10):
    print(i, end="")

# Output: 123456789
```

You can extract the range to a variable and it would still work:

```py
my_num = range(1, 10)

for i in my_num:
    print(i, end="")

# Output: 123456789
```

Note that the result is inclusive of the first number but exclusive of the second number.

## How to Use the Break Keyword in Python
You can use the `break` keyword to stop the loop before it ends.

In the example below, the execution did not get to Solidity and Assembly because I broke out of the loop when `lang` was equal to Rust:

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    if lang == "Rust":
        break
    print(lang, end=" ")
# Output: Python JavaScript PHP 
```


## How to Use the Continue Keyword in Python
You can use the `continue` keyword to skip the current iteration and continue with the rest.

In the example below, with the continue keyword, I made the loop skip PHP and continue the loop after it:

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    if lang == "PHP":
        continue
    print(lang, end=" ")

# Output: Python JavaScript Rust Solidity Assembly 
```

## How to Use the Else Keyword in Python
You can use the `else` keyword to specify that a block of code should run after the loop is done:

```py
for i in range(10):
    print(i)
else:
    print("Do + ne = Done")

# Output: 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Do + ne = Done
```

## Conclusion 
The for loop in Python doesn’t look as complicated as it is in many other programming languages. But its implementation remains powerful when it runs.

For loop is a very powerful feature of Python with which you can get a lot done. 

Thank you for reading. If you find this article helpful, share it with your friends and family!


