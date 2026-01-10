---
title: Python While Loop Tutorial – Do While True Example Statement
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-24T17:47:29.000Z'
originalURL: https://freecodecamp.org/news/python-while-loop-tutorial-do-while-true-example-statement
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Blue-Engagement-Essentials-Blog-Banner.png
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: null
seo_desc: 'Loops are a sequence of instructions executed until a condition is satisfied.
  Let''s look at how while loops work in Python.

  What are loops?

  If you are learning to code, loops are one of the main concepts you should understand.
  Loops help you execute ...'
---

Loops are a sequence of instructions executed until a condition is satisfied. Let's look at how while loops work in Python.

## What are loops?

If you are learning to code, loops are one of the main concepts you should understand. Loops help you execute a sequence of instructions until a condition is satisfied. 

There are two major types of loops in Python. 

* For loops
* While loops

Both these types of loops can be used for similar actions. But as you learn to write efficient programs, you will know when to use what. 

In this article, we will look at while loops in Python. To learn more about for loops, [check out this article recently published on freeCodeCamp](https://www.freecodecamp.org/news/for-loops-in-python/). 

## While Loops

The concept behind a while loop is simple: _While a condition is true -> Run my commands._

The while loop will check the condition every time, and if it returns "true" it will execute the instructions within the loop. 

Before we start writing code, let's look at the flowchart to see how it works. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/while-loop.jpg)

Now let's write some code. Here's how you write a simple while loop to print numbers from 1 to 10.

```python
#!/usr/bin/python

x = 1

while(x <= 10):
	print(x)
	x = x+1
```

If you look at the above code, the loop will only run if x is less than or equal to 10. If you initialise x as 20, the loop will never execute. 

Here is the output of that while loop:

```
> python script.py
1
2
3
4
5
6
7
8
9
10
```

### Do-While Loop

There are two variations of the while loop – while and do-While. The difference between the two is that do-while runs at least once. 

A while loop might not even execute once if the condition is not met. However, do-while will run once, then check the condition for subsequent loops. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/do-while.jpg)

In spite of being present in most of the popular programming languages, Python does not have a native do-while statement. But you can easily emulate a do-while loop using other approaches, such as functions. 

Let's try the do-while approach by wrapping up the commands in a function. 

```
#!/usr/bin/python

x = 20

def run_commands():
	x = x+1
	print(x)


run_commands()
while(x <= 10):
	run_commands()
```

The above code runs the "run_commands()" function once before invoking the while loop. Once the while loop starts, the "run_commands" function will never be executed since x is equal to 20. 

### While - Else

You can add an "else" statement to run if the loop condition fails. 

Let's add an else condition to our code to print "Done" once we have printed the numbers from 1 to 10.

```
#!/usr/bin/python

x = 1

while(x <= 10):
	print(x)
	x = x+1
else:
	print("Done")
```

The above code will first print the numbers from 1 to 10. When x is 11, the while condition will fail, triggering the else condition. 

### Single Line While Statement

If you only have a single line of code within your while loop, you can use the single line syntax. 

```
#!/usr/bin/python

x = 1
while (x): print(x)
```

### Infinite Loops

If you are not careful while writing loops, you will create infinite loops. Infinite loops are the ones where the condition is always true. 

```
#!/usr/bin/python

x = 1
while (x >= 1):
	print(x)
```

The above code is an example of an infinite loop. There is no command to alter the value of x, so the condition "x is greater than or equal to 1" is always true. This will make the loop run forever.

Always be careful while writing loops. A small mistake can lead to an infinite loop and crash your application. 

## Loop Control

Finally, let's look at how to control the flow of a loop while it is running.  

When you are writing real world applications, you will often encounter scenarios where you need to add additional conditions to skip a loop or to break out of a loop.

### Break

Let's look at how to break out of the loop while the condition is true. 

```
#!/usr/bin/python

x = 1
while (x <= 10):
    if(x == 5):
    	break
    print(x)
    x += 1
```

In the above code, the loop will stop execution when x is 5, in spite of x being greater than or equal to 1. 

### Continue

Here's another scenario: say you want to skip the loop if a certain condition is met. However, you want to continue subsequent executions until the main while condition turns false. 

You can use the "continue" keyword for that, like this:

```
#!/usr/bin/python

x = 1
while (x <= 10):
    if(x == 5):
    	x += 1
    	continue
    print(x)
```

In the above example,  the loop will print from 1 to 10, except 5. When x is 5, the rest of the commands are skipped and the control flow returns to the start of the while program. 

## Summary

Loops are one of the most useful components in programming that you will use on a daily basis. 

For and while are the two main loops in Python. The while loop has two variants, while and do-while, but Python supports only the former. 

You can control the program flow using the 'break' and 'continue' commands. Always be aware of creating infinite loops accidentally. 

I regularly write on topics including Artificial Intelligence and Cybersecurity. If you liked this article, [you can read my blog here](https://medium.com/manishmshiva). 

