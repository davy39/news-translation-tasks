---
title: Python If-Else Statement Example
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-10T17:05:36.000Z'
originalURL: https://freecodecamp.org/news/python-if-else-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/rosie-steggles-h1OhvEIIcxs-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'If-Else statements – AKA conditional logic – are the bedrock of programming.
  And Python has these in spades.

  Python offers several options for evaluating variables, their states, and whether
  specific conditions are met:


  Vanilla if-else statements

  if...'
---

If-Else statements – AKA conditional logic – are the bedrock of programming. And Python has these in spades.

Python offers several options for evaluating variables, their states, and whether specific conditions are met:

* Vanilla if-else statements
* if statements without the else part
* nested if-else statements
* else-if or `elif` statements
* and looped if-else statements in the form of for-else and while-else

We'll talk about all of these, and also explain the extremely useful double-equals `==` operator.

## How do you write an if-else statement in Python?

If you're just looking for an example to copy-paste, here is a super simple if-else statement in Python:

```py
if x < y:
	print("x is less than y")
else:
	print("x is equal to or greater than y")
```

Note that the fact that Python is a whitespace-sensitive ensures that these if-else statements are easy to read – even when they get nested several layers deep.

With that out of the way, let's talk a bit more about conditional logic, and why if-else statements are so important to Python and other programming languages.

## How do we use the if-else statement?

If-else statements are a form of conditional logic. Essentially, what that means is

1. We test a condition. For example, whether a given variable equals another given variable.
2. If the condition is true, we execute the following block of code.
3. And if the condition is false, we execute a different block of code.

This is absolutely critical to any sort of programming. You cannot have turing-complete programming languages without some sort of conditional logic. In Python, that means lots of if-else statements.

## How is if statement different from if else statement in Python?

So you don't technically need the `else` part of the if-else statement. For example:

```py
age = int(input("Enter your age: ")) 
if age >= 18: print("You are eligible to vote!")

```

To see how this works, here is the Python REPL:

```py
>>> age = int(input("Enter your age: "))
Enter your age: 20
>>> if age >= 18: print("You are eligible to vote!")
You are eligible to vote!

>>> age = int(input("Enter your age: "))
Enter your age: 17
>>> if age >= 18: print("You are eligible to vote!")
[nothing happens]

```

As you can see, this is sort of like an if-else statement with an invisible `else`. If the `else` part was there, and the condition was not met, it would just be like "OK. Carry on then."

## What is the difference between Else and Elif construct of IF statement?

If you want to have more potential conditions, you can use an `elif` statement.

Here is an example `elif` statement:

```py
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

```

You'll note that the `elif` operator appears between the initial `if` and `else` operators.

Also note that you can use as many `elif` as you want.

```py
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
elif condition4:
    statement4
elif condition5:
    statement5
else
	statement6
```

## What is for else and while else in Python?

You can combine conditional logic with loops by using a `for else` or `while else` statement.

Here is an example `for else` statement that hits the `break` and exits:

```py
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This code will only execute if the for loop completes without hitting a break statement.")

# this will output:
0
1
2
3
4
5

```

And here is the same `for if` statement that starts from a higher number, which will skip the `break` event and finish. Take a look at the code and its output:

```py
for i in range(6,10):
    print(i)
    if i == 5:
        break
else:
    print("This code will only execute if the for loop completes without hitting a break statement.")

# this will output:
6
7
8
9
This code will only execute if the for loop completes without hitting a break statement.

```

## Can you have multiple if statements in Python?

Absolutely. You can have as many nested if statements as you want. Be careful, though. This can lead to the so-called "pyramid of doom."

Here's an example of nested if statements:

```py
if x == 5:
	if y == 10:
	    print("x is 5 and y is 10")
	else:
	    print("x is 5 and y is something else")
else:
	print("x is something else")

```

Notice how there are two if-else statements, but one of them is nested inside the other. This is OK for a lay or two, but it can get confusing quickly:

```py
if x == 1:
    if y == 2:
        if z == 3:
            print("x, y, and z are all equal to 1, 2, and 3, respectively")
        else:
            print("x and y are equal to 1 and 2, respectively, but z is not equal to 3")
    else:
        print("x is equal to 1 but y is not equal to 2")
else:
    print("x is not equal to 1")

```

## Can you have 3 conditions in an if statement?

Yes. But if you do this, it probably makes sense to use some `elif` operators in your statement for clarity.

Here is an example if statement with 3 conditions:

```py
if (condition1):
    # execute code1
elif (condition2):
    # execute code2
elif (condition3):
    # execute code3

```

## What does `==` mean in Python?

The Python `==` operator – also known as the equality operator – is a comparison operator that returns True if both of the operands (the variables or values on the left and the right of the `==`) are equal. Otherwise it will return False.

This is an extremely common tool for crafting if statements and other conditional logic.

Learn it. Know it. Love it.

## I hope you learned a lot about if statements.

I sure did in dusting off my Python knowledge and writing this tutorial. I hope you've found this helpful.

If you want to learn more about Python programming, and technology in general, try [freeCodeCamp's core coding curriculum](https://www.freecodecamp.org/learn). It's free.

