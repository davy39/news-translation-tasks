---
title: Python While Loop Tutorial – While True Syntax Examples and Infinite Loops
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-11-13T15:54:56.000Z'
originalURL: https://freecodecamp.org/news/python-while-loop-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/While-loops-image-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Welcome! If you want to learn how to work with while loops in Python, then\
  \ this article is for you. \nWhile loops are very powerful programming structures\
  \ that you can use in your programs to repeat a sequence of statements. \nIn this\
  \ article, you will..."
---

Welcome! If you want to learn how to work with while loops in Python, then this article is for you. 

While loops are very powerful programming structures that you can use in your programs to repeat a sequence of statements. 

**In this article, you will learn:**

* What while loops are.
* What they are used for.
* When they should be used.
* How they work behind the scenes.
* How to write a while loop in Python.
* What infinite loops are and how to interrupt them.
* What `while True` is used for and its general syntax.
* How to use a `break` statement to stop a while loop.

You will learn how while loops work behind the scenes with examples, tables, and diagrams.

Are you ready? Let's begin. 🔅

## 🔹 Purpose and Use Cases for While Loops

Let's start with the purpose of while loops. What are they used for?

They are used to repeat a sequence of statements an unknown number of times. This type of loop runs **while** a given condition is `True` and it only stops when the condition becomes `False`.

When we write a while loop, we don't explicitly define how many iterations will be completed, we only write the condition that has to be `True` to continue the process and `False` to stop it.

**💡 Tip:** if the while loop condition never evaluates to `False`, then we will have an infinite loop, which is a loop that never stops (in theory) without external intervention. 

**These are some examples of real use cases of while loops:**

* **User Input:** When we ask for user input, we need to check if the value entered is valid. We can't possibly know in advance how many times the user will enter an invalid input before the program can continue. Therefore, a while loop would be perfect for this scenario.
* **Search:** searching for an element in a data structure is another perfect use case for a while loop because we can't know in advance how many iterations will be needed to find the target value. For example, the Binary Search algorithm can be implemented using a while loop.
* **Games:** In a game, a while loop could be used to keep the main logic of the game running until the player loses or the game ends. We can't know in advance when this will happen, so this is another perfect scenario for a while loop. 

## 🔸 How While Loops Work

Now that you know what while loops are used for, let's see their main logic and how they work behind the scenes. Here we have a diagram:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-24.png)
_While Loop_

**Let's break this down in more detail:**

* The process starts when a while loop is found during the execution of the program.
* The condition is evaluated to check if it's `True` or `False`. 
* If the condition is `True`, the statements that belong to the loop are executed. 
* The while loop condition is checked again. 
* If the condition evaluates to `True` again, the sequence of statements runs again and the process is repeated.
* When the condition evaluates to `False`, the loop stops and the program continues beyond the loop.

One of the most important characteristics of while loops is that the variables used in the loop condition are not updated automatically. We have to update their values explicitly with our code to make sure that the loop will eventually stop when the condition evaluates to `False`.

## 🔹 General Syntax of While Loops

Great. Now you know how while loops work, so let's dive into the code and see how you can write a while loop in Python. This is the basic syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-105.png)
_While Loop (Syntax)_

**These are the main elements (in order):**

* The `while` keyword (followed by a space).
* A condition to determine if the loop will continue running or not based on its truth value (`True` or `False` ).
* A colon (`:`) at the end of the first line.
* The sequence of statements that will be repeated. This block of code is called the "body" of the loop and it has to be indented. If a statement is not indented, it will not be considered part of the loop (please see the diagram below). 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-7.png)

**💡 Tip:** The [Python style guide](https://www.python.org/dev/peps/pep-0008/#indentation) (PEP 8) recommends using 4 spaces per indentation level. Tabs should only be used to remain consistent with code that is already indented with tabs.

## 🔸 Examples of While Loops

Now that you know how while loops work and how to write them in Python, let's see how they work behind the scenes with some examples.

### How a Basic While Loop Works

Here we have a basic while loop that prints the value of `i` **while** `i` is less than 8 (`i < 8`):

```python
i = 4

while i < 8:
    print(i)
    i += 1
```

If we run the code, we see this output:

```
4
5
6
7
```

Let's see what happens behind the scenes when the code runs:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-16.png)

* **Iteration 1:** initially, the value of `i` is 4, so the condition `i < 8` evaluates to `True` and the loop starts to run. The value of `i` is printed (4) and this value is incremented by 1. The loop starts again. 
* **Iteration 2:** now the value of `i` is 5, so the condition `i < 8` evaluates to `True`. The body of the loop runs, the value of `i` is printed (5) and this value `i` is incremented by 1. The loop starts again.
* **Iterations 3 and 4:** The same process is repeated for the third and fourth iterations, so the integers 6 and 7 are printed.
* Before starting the fifth iteration, the value of `i` is `8`. Now the while loop condition `i < 8` evaluates to `False` and the loop stops immediately.

💡 **Tip:** If the while loop condition is `False` before starting the first iteration, the while loop will not even start running. 

### User Input Using a While Loop

Now let's see an example of a while loop in a program that takes user input. We will the `input()` function to ask the user to enter an integer and that integer will only be appended to list if it's even. 

This is the code:

```python
# Define the list
nums = []

# The loop will run while the length of the
# list nums is less than 4
while len(nums) < 4:
    # Ask for user input and store it in a variable as an integer.
    user_input = int(input("Enter an integer: "))
    # If the input is an even number, add it to the list
    if user_input % 2 == 0:
        nums.append(user_input)
```

The loop condition is `len(nums) < 4`, so the loop will run while the length of the list `nums` is strictly less than 4.

**Let's analyze this program line by line:**

* We start by defining an empty list and assigning it to a variable called `nums`.

```python
nums = []
```

* Then, we define a while loop that will run while `len(nums) < 4`.

```python
while len(nums) < 4:
```

* We ask for user input with the `input()` function and store it in the `user_input` variable.

```python
user_input = int(input("Enter an integer: "))
```

**💡 Tip:** We need to convert (cast) the value entered by the user to an integer using the `int()` function before assigning it to the variable because the `input()` function returns a string ([source](https://docs.python.org/3/library/functions.html#input)).

* We check if this value is even or odd. 

```python
if user_input % 2 == 0:
```

* If it's even, we append it to the `nums` list. 

```python
nums.append(user_input)
```

* Else, if it's odd, the loop starts again and the condition is checked to determine if the loop should continue or not.

If we run this code with custom user input, we get the following output:

```python
Enter an integer: 3
Enter an integer: 4    
Enter an integer: 2    
Enter an integer: 1
Enter an integer: 7
Enter an integer: 6    
Enter an integer: 3
Enter an integer: 4    
```

This table summarizes what happens behind the scenes when the code runs:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-86.png)

💡 **Tip:** The initial value of `len(nums)` is `0` because the list is initially empty. The last column of the table shows the length of the list at the end of the current iteration. This value is used to check the condition before the next iteration starts. 

As you can see in the table, the user enters even integers in the second, third, sixth, and eight iterations and these values are appended to the `nums` list. 

Before a "ninth" iteration starts, the condition is checked again but now it evaluates to `False` because the `nums` list has four elements (length 4), so the loop stops. 

If we check the value of the `nums` list when the process has been completed, we see this:

```python
>>> nums
[4, 2, 6, 4]
```

Exactly what we expected, the while loop stopped when the condition `len(nums) < 4` evaluated to `False`.

Now you know how while loops work behind the scenes and you've seen some practical examples, so let's dive into a key element of while loops: the condition. 

## 🔹 Tips for the Condition in While Loops

Before you start working with while loops, you should know that the loop condition plays a central role in the functionality and output of a while loop. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-25.png)

You must be very careful with the comparison operator that you choose because this is a very common source of bugs. 

For example, common errors include:

* Using `<` (less than) instead of `<=` (less than or equal to) (or vice versa).
* Using `>` (greater than) instead of `>=` (greater than or equal to) (or vice versa).  

This can affect the number of iterations of the loop and even its output. 

Let's see an example:

If we write this while loop with the condition `i < 9`:

```python
i = 6

while i < 9:
    print(i)
    i += 1

```

We see this output when the code runs:

```python
6
7
8
```

The loop completes three iterations and it stops when `i` is equal to `9`.

This table illustrates what happens behind the scenes when the code runs:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-20.png)

* Before the first iteration of the loop, the value of `i` is 6, so the condition `i < 9` is `True` and the loop starts running. The value of `i` is printed and then it is incremented by 1. 
* In the second iteration of the loop, the value of `i` is 7, so the condition `i < 9` is `True`. The body of the loop runs, the value of `i` is printed, and then it is incremented by 1. 
* In the third iteration of the loop, the value of `i` is 8, so the condition `i < 9` is `True`. The body of the loop runs, the value of `i` is printed, and then it is incremented by 1. 
* The condition is checked again before a fourth iteration starts, but now the value of `i` is 9, so `i < 9` is `False` and the loop stops. 

In this case, we used `<` as the comparison operator in the condition, but what do you think will happen if we use `<=` instead?

```python
i = 6

while i <= 9:
    print(i)
    i += 1
```

We see this output:

```python
6
7
8
9
```

The loop completes one more iteration because now we are using the "less than or equal to" operator `<=` , so the condition is still `True` when `i` is equal to `9`.

This table illustrates what happens behind the scenes:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-21.png)

Four iterations are completed. The condition is checked again before starting a "fifth" iteration. At this point, the value of `i` is `10`, so the condition `i <= 9` is `False` and the loop stops. 

## 🔸 Infinite While Loops

Now you know how while loops work, but what do you think will happen if the while loop condition never evaluates to `False`? 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-109.png)

### What are Infinite While Loops?

Remember that while loops don't update variables automatically (we are in charge of doing that explicitly with our code). So there is no guarantee that the loop will stop unless we write the necessary code to make the condition `False` at some point during the execution of the loop. 

If we don't do this and the condition always evaluates to `True`, then we will have an **infinite loop**, which is a while loop that runs indefinitely (in theory).

Infinite loops are typically the result of a bug, but they can also be caused intentionally when we want to repeat a sequence of statements indefinitely until a `break` statement is found. 

Let's see these two types of infinite loops in the examples below. 

💡 **Tip:** A bug is an error in the program that causes incorrect or unexpected results. 

### Example of Infinite Loop

This is an example of an unintentional infinite loop caused by a bug in the program:

```python
# Define a variable
i = 5

# Run this loop while i is less than 15
while i < 15:
    # Print a message
    print("Hello, World!")
    
```

Analyze this code for a moment. 

Don't you notice something missing in the body of the loop? 

That's right! 

The value of the variable `i` is never updated (it's always `5`). Therefore, the condition `i < 15` is always `True` and the loop never stops. 

If we run this code, the output will be an "infinite" sequence of `Hello, World!` messages because the body of the loop `print("Hello, World!")` will run indefinitely. 

```python
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
.
.
.
# Continues indefinitely
```

To stop the program, we will need to interrupt the loop manually by pressing `CTRL + C`.

When we do, we will see a `KeyboardInterrupt` error similar to this one:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-116.png)

To fix this loop, we will need to update the value of `i` in the body of the loop to make sure that the condition `i < 15` will eventually evaluate to `False`. 

This is one possible solution, incrementing the value of `i` by 2 on every iteration:

```python
i = 5

while i < 15:
    print("Hello, World!")
    # Update the value of i
    i += 2
```

Great. Now you know how to fix infinite loops caused by a bug. You just need to write code to guarantee that the condition will eventually evaluate to `False`. 

Let's start diving into intentional infinite loops and how they work. 

## 🔹 How to Make an Infinite Loop with While True

We can generate an infinite loop intentionally using `while True`. In this case, the loop will run indefinitely until the process is stopped by external intervention (`CTRL + C`) or when a `break` statement is found (you will learn more about `break` in just a moment).

This is the basic syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-35.png)

Instead of writing a condition after the `while` keyword, we just write the truth value directly to indicate that the condition will always be `True`.

Here we have an example:

```python
>>> while True:
	print(0)

	
0
0
0
0
0
0
0
0
0
0
0
0
0
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    print(0)
KeyboardInterrupt
```

The loop runs until `CTRL + C` is pressed, but Python also has a `break` statement that we can use directly in our code to stop this type of loop.

### The `break` statement

This statement is used to stop a loop immediately. You should think of it as a red "stop sign" that you can use in your code to have more control over the behavior of the loop.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-110.png)

According to the [Python Documentation](https://docs.python.org/3/tutorial/controlflow.html?highlight=break#break-and-continue-statements-and-else-clauses-on-loops):

> The [`break`](https://docs.python.org/3/reference/simple_stmts.html#break) statement, like in C, breaks out of the innermost enclosing [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) loop.

This diagram illustrates the basic logic of the `break` statement:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-111.png)
_The `break` statement_

**This is the basic logic of the `break` statement:**

* The while loop starts only if the condition evaluates to `True`. 
* If a `break` statement is found at any point during the execution of the loop, the loop stops immediately.
* Else, if `break` is not found, the loop continues its normal execution and it stops when the condition evaluates to `False`. 

We can use `break` to stop a while loop when a condition is met at a particular point of its execution, so you will typically find it within a conditional statement, like this:

```
while True:
    # Code
    if <condition>:
    	break
    # Code
```

This stops the loop immediately if the condition is `True`.

💡 **Tip:** You can (in theory) write a `break` statement anywhere in the body of the loop. It doesn't necessarily have to be part of a conditional, but we commonly use it to stop the loop when a given condition is `True`.

Here we have an example of `break` in a `while True` loop:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-41.png)

**Let's see it in more detail:**

The first line defines a `while True` loop that will run indefinitely until a `break` statement is found (or until it is interrupted with `CTRL + C`).

```python
while True:
```

The second line asks for user input. This input is converted to an integer and assigned to the variable `user_input`. 

```
user_input = int(input("Enter an integer: "))
```

The third line checks if the input is odd. 

```
if user_input % 2 != 0:
```

If it is, the message `This number is odd` is printed and the `break` statement stops the loop immediately.

```
print("This number of odd")
break
```

Else, if the input is even , the message `This number is even` is printed and the loop starts again.

```
print("This number is even")
```

The loop will run indefinitely until an odd integer is entered because that is the only way in which the `break` statement will be found. 

Here we have an example with custom user input:

```python
Enter an integer: 4
This number is even
Enter an integer: 6
This number is even
Enter an integer: 8
This number is even
Enter an integer: 3
This number is odd
>>> 
```

## 🔸 In Summary

* While loops are programming structures used to repeat a sequence of statements while a condition is `True`. They stop when the condition evaluates to `False`. 
* When you write a while loop, you need to make the necessary updates in your code to make sure that the loop will eventually stop.
* An infinite loop is a loop that runs indefinitely and it only stops with external intervention or when a `break` statement is found. 
* You can stop an infinite loop with `CTRL + C`.
* You can generate an infinite loop intentionally with `while True`.
* The `break` statement can be used to stop a while loop immediately. 

**I really hope you liked my article and found it helpful.** Now you know how to work with While Loops in Python. 

Follow me on Twitter [@EstefaniaCassN](https://twitter.com/EstefaniaCassN) and if you want to learn more about this topic, check out my online course [Python Loops and Looping Techniques: Beginner to Advanced](https://www.udemy.com/course/python-loops-and-looping-techniques-beginner-to-advanced/?referralCode=EEABE054BAB98C00CC8E). 

