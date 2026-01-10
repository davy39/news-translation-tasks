---
title: Else-If in Python – Python If Statement Example Syntax
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-22T20:41:35.000Z'
originalURL: https://freecodecamp.org/news/else-if-in-python-python-if-statement-example-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Copy-of-pip--4-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When you're coding, you need to be able to check certain conditions and\
  \ change the control of the program execution accordingly. \nPython provides many\
  \ conditional statements for decision making, and if-else is one of them.\nIn this\
  \ blog post, we will ..."
---

When you're coding, you need to be able to check certain conditions and change the control of the program execution accordingly. 

Python provides many conditional statements for decision making, and `if-else` is one of them.

In this blog post, we will learn:

1. The default order of execution of statements and how we can alter it.
2. What is the `if-else` statement and its syntax.
3. How to deal with multiple conditions using `elif`.
4. A practical example of `if else` where we will write a program to check if the number is even or odd.

## Sequential order vs control structure in Python

By default, the execution of statements is in sequential. **Sequential order** means that statements are executed one after the other in the order they are written.

Let's see an example of sequential execution below by calculating the rate per hour for a worker:

```python
# Write a program to calculate total rate

hours = input("enter hours: ")
rateperhr = 10
print("Your total rate is", int(hours)*rateperhr)


```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-95.png)

What if we need to check if the number of hours exceeds 8 hours a day and goes into the overtime limit? 

Here we need to check a condition and make the decision accordingly. That is where **control structures** come in. A control structure redirects the order of execution of the statements in a program.

In Python, we can use `if`, `if-else,` `if-elif-else`, or `switch` statements for controlling the program execution. Loops are another way to control execution flow. In this blog, we will focus mainly on if-else and its derivatives.

## Introduction to the if-statement in Python

The `if` statement proceeds based on a certain condition if it is `true`. If the condition is false, then statements outside the `if` block are executed.

### Syntax of `if` statement in Python:

```python
if <expression>:
    <statement>
```

Note that the body of the `if` block is the indented sequence of statements. The colon at the end of the `<expression>` indicates the start of the `if` statement.

![Flow of if statement ](https://www.freecodecamp.org/news/content/images/2022/03/image-88.png)
_Flow of `if` statement_

**Example:**

```python
if 10<20:
  print("True, statement inside 'if'")
  print("Still inside if")

print("Statement outside 'if'")
```

**Output:**

![Example of if statement](https://www.freecodecamp.org/news/content/images/2022/03/image-87.png)
_Example of if statement_

### If-else statement in Python

What if we want to do something in case the `if` statement is false? We can do this by adding an additional `else` block.

Syntax of `if-else`:

```python
if <exprression>:
    <statement>
    <statement>
else:
    <statement>
    <statement>
```

In the `if-else` statement, we have two branches incase the statement is true or false. The `if` block is executed in case the expression is true. The `else` block is executed in case the expression is false. See how we are changing the sequence of execution? This is possible due to control structures.

## Flow of if-else statement in Python

We can summarize the flow of `if-else` statements in the following flowchart.

First, the expression is evaluated. In case the expression is true, statements inside `if` are executed and the `else` block is skipped. In case the expression is false, the `else` block statement executes.

![if-else flow diagram](https://www.freecodecamp.org/news/content/images/2022/03/image-89.png)
_if-else flow diagram_

### Example of if-else in Python:

Let's compare two numbers and find the largest.

```python
a = input("enter a number: ")
b = input("enter another number: ")

if a>b:
  print("First number is the largest")
else:
  print("Second number is the largest")
```

**Output**:

![Example of if-else](https://www.freecodecamp.org/news/content/images/2022/03/image-90.png)
_Example of if-else_

## The elif clause in Python

The `elif` statement adds another "decision" branch to `if-else`. Let's say you want to evaluate multiple expressions, then you can use `elif` as follows:

```python
if <expression>:
    <statement(s)>
elif <expression>:
    <statement(s)>
elif <expression>:
    <statement(s)>
    .
    .
    .
else:
    <statement(s)>

```

This means that when the `if` statement is false, the next `elif` expression is checked. When any one expression is true, the control goes outside the `if-else` block.

At most, one block would be executed. In case `else` is not specified, and all the statements are `false`, none of the blocks would be executed.

**Here's an example:**

```python
if 51<5:
  print("False, statement skipped")
elif 0<5:
  print("true, block executed")
elif 0<3:
  print("true, but block will not execute")
else:
  print("If all fails.")
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-91.png)

Note that the second `elif` didn't execute as the first elif evaluated to `true`.

## A practical example of if-else – is the number even or odd?

In this example, we'll check if a number is even or odd. In the logic, we have checked that if the modulus of a number is zero, it is even. This is because all even numbers, when divided by 2, have a remainder of `0`. We have checked the modulus of `0` in a separate statement, as division by zero gives a traceback error.

```python
#Take user input
inp_num = input("Enter a number: ")

#Convert string to int
inp_num = int(inp_num)

if inp_num == 0:
  print(inp_num, "is Even")
elif inp_num%2==0:
  print(inp_num, "is Even")
else:
  print(inp_num, "is Odd")
```

**Output:**

Test case #1:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-92.png)

Test case #2:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-93.png)

Test case #3:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-94.png)

## Wrapping up

In this tutorial we learned how we can control the flow of execution using `if-else` statements. Using conditional statements helps us write meaningful programs. These statements can be nested to target complex issues.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Banner image credits: [Thinking vector created by storyset - www.freepik.com](https://www.freepik.com/vectors/thinking) & canva.com


