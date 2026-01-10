---
title: Python Map – How to Map a List in Python 3.0, With Example Function Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-12T14:25:17.000Z'
originalURL: https://freecodecamp.org/news/python-map-function-how-to-map-a-list-in-python-3-0-with-example-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60721be2d5756f080ba9871d.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Daniel Chae\nIf you're learning how to code, the Python Map Function\
  \ is your opportunity to level up. \nPicture this: you want to become a more efficient\
  \ coder. You want your code to compile faster. You want to impress your peers with\
  \ your robust co..."
---

By Daniel Chae

If you're learning how to code, the Python Map Function is your opportunity to level up. 

Picture this: you want to become a more efficient coder. You want your code to compile faster. You want to impress your peers with your robust coding knowledge. If any of this resonates with you, then you've come to the right place. 

Before we move forward you need to understand what functions and iterables are:

Functions are code that performs a specific task.

_Examples: `len()`, `print()`, `str()`_

Iterables are objects that contain one or more members.

_Examples: list, dictionary, tuple_

The Python Map Function is a function that allows you to transform an entire iterable using another function. The key concept here is transformation which can include but is not limited to:

* Converting strings to numbers
* Rounding numbers
* Getting the length of each iterable member

You might be wondering, "why can't I just do the above with a for loop?"

The answer is, you can. But using the Python Map Function saves you memory (which means that your code runs faster) and requires less code. Let's walk through an example so you can understand what I mean. 

## First Let's Start with a For Loop

Let's say you have a list of strings that are actually numbers, but you need to convert the list of strings to integers:

`list_of_strings = ["5","6","7","8","9", "10"]`

You could use an empty list and a for loop to accomplish this:

```
list_of_strings = ["5","6","7","8","9", "10"]

result = []

for string in list_of_strings:
    result.append(int(string))
    
print(result)
```

If you ran this example you'd get:

Output: [5, 6, 7, 8, 9, 10]

### What's Happening Under the Hood with the For Loop

You may be happy with the result, but think about what your code just did. 

You told the computer to go through each member ("5", "6", "7", etc...), convert the member, and then store that member in a new list. While using a for loop to transform a list is functional, it isn't optimal.

## Python Map Function (with Example Code)

Instead, let's use the Python Map Function to produce a functional AND optimal result. We'll start with our list of strings that need to be converted:

```
list_of_strings = ["5","6","7","8","9", "10"]

```

Then we'll use the Python Map Function to transform the list of strings to a list of integers:

```
result = map(int,list_of_strings)

print(list(result))
```

If you run the above example, you'd get the same result:

Output: [5, 6, 7, 8, 9, 10]

Before we get to why the Python Map Function is more optimal than using a for loop, let's break down what we just did:

```
list_of_strings = ["5","6","7","8","9", "10"]

```

All we did here is create a variable that stores the list of strings that we want to convert to numbers. 

```
result = map(int,list_of_strings)

```

Let's break down the above code from the inside out. The Python Map Function's syntax is as follows:

```
map(insert function here, insert iterable here)
```

`map()` is simply the name of the Python Map Function, nothing fancy here.

`insert function here` is the space where you would write in a function. In the above code example, we used the `int` function. We could have used another built-in function like `len()` or we could have built our own function and used it here as well.

`insert iterable here` is the space where you would write in the iterable of your choice. In this instance, we inserted our list (`list_of_strings`).

`result` is the variable where we're storing our newly transformed members.  

Let's move on to the last line of code. Again, we'll work from the inside out:

```
print(list(result))
```

`list()` takes our newly transformed iterable members and tells our computer these members are apart of a list. 

`print()` prints out our new list! 

### What's Happening Under the Hood with the Python Map Function

Instead of iterating through each member of the list of strings, the Python Map Function transformed the entire list of strings to a list of numbers. You saved memory and your code ran faster. 

## If You Want to Transform, Python Map Function > For Loops

![Image](https://www.freecodecamp.org/news/content/images/2021/04/nubelson-fernandes-Y376h7VN27c-unsplash.jpg)

In the end, the Python Map Function is more elegant than a for loop and will help you compile your code faster. 

Using the Python Map Function will help take your coding skills to the next level and become a better programmer. In the process, you may even impress your coding peers with this new skill. 

That said, the Python Map Function is just the beginning. There are plenty more Python tricks that will help you write more elegant code and improve your programming skills. Happy coding!   

