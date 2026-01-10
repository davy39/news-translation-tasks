---
title: Python Sleep – time.sleep() in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-17T17:22:29.000Z'
originalURL: https://freecodecamp.org/news/python-sleep-time-sleep-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/sleep.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "While running a Python program, there might be times when you'd like to\
  \ delay the execution of the program for some seconds. \nThe Python time module\
  \ has a built-in function called time.sleep() with which you can delay the execution\
  \ of a program.\nWith..."
---

While running a Python program, there might be times when you'd like to delay the execution of the program for some seconds. 

The Python time module has a built-in function called `time.sleep()` with which you can delay the execution of a program.

With the sleep() function, you can get more creative in your Python projects because it lets you create delays that might go a long way in helping you bring in certain functionalities.

In this article, you will learn how to use the `time.sleep()` method to create delays.

Just note that delays created with `time.sleep()` do not stop the execution of the whole program – they only delay the current thread.

## Basic Syntax of `time.sleep()`

To use `time.sleep()` in your program, you have to import it from the time module first.

After importing the `sleep()` function, specify the number of seconds you want the delay to run inside the parenthesis.

```py
import time
time.sleep(delayInSeconds)
```

## Basic Example of `time.sleep()`

In the code snippet below, I put a delay of 5 seconds between the 2 print statements, so the second print statement will run 5 seconds after the first print statement runs:

```py
import time

print("Hello world")

time.sleep(5)

print("Hello campers")
```
![ss1](https://www.freecodecamp.org/news/content/images/2022/03/ss1.gif)

You can also specify the delay in floating-point numbers:

```py
import time

print("Hello world")

time.sleep(3.5)

print("Hello campers")
```
![ss2](https://www.freecodecamp.org/news/content/images/2022/03/ss2.gif)

## More Examples of time.sleep()

You can get more creative with delays created by time.sleep() by combining it with `ctime()`, another built-in function from the time module that stands for “current time”.

```py
import time

print("Execution started at: ", time.ctime())

time.sleep(10)
print("Hello world")

print("Execution ended at at: ", time.ctime())

# Output
# Executiuon started at:  Thu Mar 17 10:37:55 2022
# Hello world
# Executiuon ended at at:  Thu Mar 17 10:38:05 2022
```

You can also use time.sleep() to create multiple delays while looping through iterable data such as list or tuple.

The example below shows how I did it with a list:

```py
import time

# Creating the list
legendaryFootballers = ["Okocha", "Pele", "Eusebio", "Martha", "Cruyff", "MAradona"]

for legend in legendaryFootballers:

    # Creating the delay
    time.sleep(2)

    # Individual legends in the list will be printed after 2 seconds
    print(legend)
```

The output:
![ss3](https://www.freecodecamp.org/news/content/images/2022/03/ss3.gif)

## Conclusion 

This article took you through how to use the `time.sleep()` function in Python. 

`time.sleep()` is an exciting built-in function that can be useful for creating delays in your Python projects, whether they're games, web projects, or AI systems.

Keep coding!


