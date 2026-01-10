---
title: 'How to Handle Exceptions in Python: A Detailed Visual Introduction'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-12-22T15:27:27.000Z'
originalURL: https://freecodecamp.org/news/exception-handling-python
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/Exception-Handling-in-Python.png
tags:
- name: Exception Handling
  slug: exception-handling
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: null
seo_desc: 'Welcome! In this article, you will learn how to handle exceptions in Python.

  In particular, we will cover:


  Exceptions

  The purpose of exception handling

  The try clause

  The except clause

  The else clause

  The finally clause

  How to raise exceptions


  Are ...'
---

Welcome! In this article, you will learn how to handle exceptions in Python.

**In particular, we will cover:**

* Exceptions
* The purpose of exception handling
* The try clause
* The except clause
* The else clause
* The finally clause
* How to raise exceptions

**Are you ready? Let's begin! 😀**

## 1️⃣ Intro to Exceptions

We will start with exceptions:

* **What** are they? 
* **Why** are they relevant? 
* **Why** should you handle them?

According to the [Python documentation](https://docs.python.org/3/tutorial/errors.html#exceptions):

> Errors detected during execution are called **_exceptions_** and are not unconditionally fatal.

**Exceptions are raised when the program encounters an error during its execution.** They disrupt the normal flow of the program and usually end it abruptly. To avoid this, you can catch them and handle them appropriately.

You've probably seen them during your programming projects. 

If you've ever tried to divide by zero in Python, you must have seen this error message:

```python
>>> a = 5/0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = 5/0
ZeroDivisionError: division by zero
```

If you tried to index a string with an invalid index, you definitely got this error message:

```python
>>> a = "Hello, World"
>>> a[456]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[456]
IndexError: string index out of range
```

These are examples of exceptions.

### 🔹 Common Exceptions

There are many different types of exceptions, and they are all raised in particular situations. Some of the exceptions that you will most likely see as you work on your projects are:

* **IndexError** - raised when you try to index a list, tuple, or string beyond the permitted boundaries. For example:

```python
>>> num = [1, 2, 6, 5]
>>> num[56546546]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num[56546546]
IndexError: list index out of range
```

* **KeyError** - raised when you try to access the value of a key that doesn't exist in a dictionary. For example:

```python
>>> students = {"Nora": 15, "Gino": 30}
>>> students["Lisa"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    students["Lisa"]
KeyError: 'Lisa'
```

* **NameError** - raised when a name that you are referencing in the code doesn't exist. For example:

```python
>>> a = b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
```

* **TypeError** - raised when an operation or function is applied to an object of an inappropriate type. For example:

```python
>>> (5, 6, 7) * (1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    (5, 6, 7) * (1, 2, 3)
TypeError: can't multiply sequence by non-int of type 'tuple'
```

* **ZeroDivisionError** - raised when you try to divide by zero.

```python
>>> a = 5/0
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a = 5/0
ZeroDivisionError: division by zero
```

💡 **Tips:** To learn more about other types of built-in exceptions, please [refer to this article](https://docs.python.org/3/library/exceptions.html) in the Python Documentation.

### 🔸 **Anatomy of an Exception**

I'm sure that you must have noticed a general pattern in these error messages. Let's break down their general structure piece by piece:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-8.png)

First, we find this line (see below). A **traceback** is basically a list detailing the function calls that were made before the exception was raised. 

The traceback helps you during the debugging process because you can analyze the sequence of function calls that resulted in the exception:

```python
Traceback (most recent call last):
```

Then, we see this line (see below) with the path to the file and the line that raised the exception. In this case, the path was the Python shell <pyshell#0> since the example was executed directly in IDLE.

```python
File "<pyshell#0>", line 1, in <module>
   a - 5/0
```

**💡 Tip:** If the line that raised the exception belongs to a function, <module>  is replaced by the name of the function.

Finally, we see a descriptive message detailing the type of exception and providing additional information to help us debug the code:

```
NameError: name 'a' is not defined
```

## 2️⃣ Exception Handling: Purpose & Context

You may ask: why would I want to handle exceptions? Why is this helpful for me? By handling exceptions, you can provide an alternative flow of execution to avoid crashing your program unexpectedly.

### 🔹 Example: User Input

Imagine what would happen if a user who is working with your program enters an invalid input. This would raise an exception because an invalid operation was performed during the process. 

If your program doesn't handle this correctly, it will crash suddenly and the user will have a very disappointing experience with your product.

**But if you do handle the exception, you will be able to provide an alternative to improve the experience of the user.** 

Perhaps you could display a descriptive message asking the user to enter a valid input, or you could provide a default value for the input. Depending on the context, you can choose what to do when this happens, and this is the magic of error handling. It can save the day when unexpected things happen. ⭐️

### 🔸 What Happens Behind the Scenes?

Basically, when we handle an exception, we are telling the program what to do if the exception is raised. In that case, the "alternative" flow of execution will come to the rescue. If no exceptions are raised, the code will run as expected.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-10.png)

## 3️⃣ Time to Code: The try ... except Statement

Now that you know what exceptions are and why you should we handle them, we will start diving into the built-in tools that the Python languages offers for this purpose. 

**First, we have the most basic statement: try ... except.**

Let's illustrate this with a simple example. We have this small program that asks the user to enter the name of a student to display his/her age:

```python
students = {"Nora": 15, "Gino": 30}

def print_student_age():
    name = input("Please enter the name of the student: ")
    print(students[name])

print_student_age()
```

Notice how we are not validating user input at the moment, so the user might enter invalid values (names that are not in the dictionary) and the consequences would be catastrophic because the program would crash if a KeyError is raised:

```python
# User Input
Please enter the name of the student: "Daniel"

# Error Message
Traceback (most recent call last):
  File "<path>", line 15, in <module>
    print_student_age()
  File "<path>", line 13, in print_student_age
    print(students[name])
KeyError: '"Daniel"'
```

### 🔹 Syntax

We can handle this nicely using try ... except. This is the basic syntax:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-11.png)

In our example, we would add the try ... except statement within the function. Let's break this down piece by piece:

```python
students = {"Nora": 15, "Gino": 30}

def print_student_age():
    while True:
        try:
            name = input("Please enter the name of the student: ")
            print(students[name])
            break
        except:
            print("This name is not registered")
    

print_student_age()
```

If we "zoom in", we see the try ... except statement:

```
try:
	name = input("Please enter the name of the student: ")
	print(students[name])
	break
except:
	print("This name is not registered")
```

* When the function is called, the try clause will run. If no exceptions are raised, the program will run as expected. 
* But if an exception is raised in the try clause, the flow of execution will immediately jump to the except clause to handle the exception.

**💡 Note:** This code is contained within a while loop to continue asking for user input if the value is invalid. This is an example:

```python
Please enter the name of the student: "Lulu"
This name is not registered
Please enter the name of the student: 
```

This is great, right? Now we can continue asking for user input if the value is invalid. 

At the moment, we are handling all possible exceptions with the same except clause. But what if we only want to handle a specific type of exception? Let's see how we could do this.

### 🔸 Catching Specific Exceptions

Since not all types of exceptions are handled in the same way, we can specify which exceptions we would like to handle with this syntax:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-15.png)

This is an example. We are handling the ZeroDivisionError exception in case the user enters zero as the denominator:

```python
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
        except ZeroDivisionError:
            print("Please enter a valid denominator.")


divide_integers()
```

This would be the result:

```python
# First iteration
Please enter the numerator: 5
Please enter the denominator: 0
Please enter a valid denominator. 

# Second iteration
Please enter the numerator: 5
Please enter the denominator: 2
2.5
```

We are handling this correctly. But... if another type of exception is raised, the program will not handle it gracefully. 

Here we have an example of a ValueError because one of the values is a float, not an int:

```python
Please enter the numerator: 5
Please enter the denominator: 0.5
Traceback (most recent call last):
  File "<path>", line 53, in <module>
    divide_integers()
  File "<path>", line 47, in divide_integers
    b = int(input("Please enter the denominator: "))
ValueError: invalid literal for int() with base 10: '0.5'
```

We can customize how we handle different types of exceptions.

### 🔹 Multiple Except Clauses

To do this, we need to add multiple `except` clauses to handle different types of exceptions differently. 

According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions):

> A try statement may have **more than one except clause**, to specify handlers for different exceptions. **At most one handler will be executed**.

In this example, we have two except clauses. One of them handles ZeroDivisionError and the other one handles ValueError, the two types of exceptions that could be raised in this try block. 

```
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
        except ZeroDivisionError:
            print("Please enter a valid denominator.")
        except ValueError:
            print("Both values have to be integers.")


divide_integers() 
```

💡 **Tip:** You have to determine which types of exceptions might be raised in the try block to handle them appropriately.

### 🔸 Multiple Exceptions, One Except Clause

You can also choose to handle different types of exceptions with the same except clause. 

According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions):

> An except clause may name **multiple exceptions** as a parenthesized tuple.

This is an example where we catch two exceptions (ZeroDivisionError and ValueError) with the same `except` clause:

```python
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
        except (ZeroDivisionError, ValueError):
            print("Please enter valid integers.")

divide_integers()
```

The output would be the same for the two types of exceptions because they are handled by the same except clause:

```python
Please enter the numerator: 5
Please enter the denominator: 0
Please enter valid integers.
```

```python
Please enter the numerator: 0.5
Please enter valid integers.
Please enter the numerator: 
```

### 🔹 Handling Exceptions Raised by Functions Called in the try Clause

An interesting aspect of exception handling is that if an exception is raised in a function that was previously called in the try clause of another function and the function itself does not handle it, the caller will handle it if there is an appropriate except clause. 

According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions):

> Exception handlers don’t just handle exceptions if they occur immediately in the try clause, but also **if they occur inside functions that are called (even indirectly) in the try clause.**

Let's see an example to illustrate this:

```
def f(i):
    try:
        g(i)
    except IndexError:
        print("Please enter a valid index")

def g(i):
    a = "Hello"
    return a[i]

f(50)
```

We have the `f` function and the `g` function. `f` calls `g` in the try clause. With the argument 50, `g` will raise an IndexError because the index 50 is not valid for the string a. 

But `g` itself doesn't handle the exception. Notice how there is no try ... except statement in the `g` function. Since it doesn't handle the exception, it "sends" it to `f` to see if it can handle it, as you can see in the diagram below:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-16.png)

Since f _does_ know how to handle an IndexError, the situation is handled gracefully and this is the output:

```python
Please enter a valid index
```

**💡 Note:** If `f` had not handled the exception, the program would have ended abruptly with the default error message for an IndexError.

### 🔸 Accessing Specific Details of Exceptions

Exceptions are objects in Python, so you can assign the exception that was raised to a variable. This way, you can print the default description of the exception and access its arguments.

According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions):

> The except clause **may specify a variable after the exception name**. The variable is bound to an exception instance with the arguments stored in instance.args.

Here we have an example (see below) were we assign the instance of `ZeroDivisionError` to the variable `e`. Then, we can use this variable within the except clause to access the type of the exception, its message, and arguments. 

```python
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
        # Here we assign the exception to the variable e
        except ZeroDivisionError as e:
            print(type(e))
            print(e)
            print(e.args)

divide_integers()
```

The corresponding output would be:

```python
Please enter the numerator: 5
Please enter the denominator: 0

# Type
<class 'ZeroDivisionError'>

# Message
division by zero

# Args
('division by zero',)
```

**💡 Tip:** If you are familiar with special methods, according to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions): "for convenience, the exception instance defines `[__str__()](https://docs.python.org/3/reference/datamodel.html#object.__str__)` so the arguments can be printed directly without having to reference `.args`."

## 4️⃣ Now Let's Add: The "else" Clause

The `else` clause is optional, but it's a great tool because it lets us execute code that should only run if no exceptions were raised in the try clause.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-17.png)

According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions):

> The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) statement has an **optional** _else clause_, which, when present, must follow all except clauses. It is useful for code that must be executed **if the try clause does not raise an exception.**

Here is an example of the use of the `else` clause:

```python
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            result = a / b
        except (ZeroDivisionError, ValueError):
            print("Please enter valid integers. The denominator can't be zero")
        else:
            print(result)

divide_integers()
```

If no exception are raised, the result is printed:

```python
Please enter the numerator: 5
Please enter the denominator: 5
1.0
```

But if an exception is raised, the result is not printed:

```python
Please enter the numerator: 5
Please enter the denominator: 0
Please enter valid integers. The denominator can't be zero
```

💡 **Tip:** According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions):

> The use of the `else` clause is better than adding additional code to the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the `try` … `except` statement.

## 5️⃣ The "finally" Clause

The finally clause is the last clause in this sequence. It is **optional**, but if you include it, it has to be the last clause in the sequence. The `finally` clause is **always** executed, even if an exception was raised in the try clause.  

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-19.png)

According to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions):

> If a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause is present, the [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause will execute as the last task before the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement completes. The [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause **runs whether or not the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement produces an exception.**

The finally clause is usually used to perform "clean-up" actions that should always be completed. For example, if we are working with a file in the try clause, we will always need to close the file, even if an exception was raised when we were working with the data.

Here is an example of the finally clause:

```python
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            result = a / b
        except (ZeroDivisionError, ValueError):
            print("Please enter valid integers. The denominator can't be zero")
        else:
            print(result)
        finally:
            print("Inside the finally clause")

divide_integers()
```

This is the output when no exceptions were raised:

```
Please enter the numerator: 5
Please enter the denominator: 5
1.0
Inside the finally clause
```

This is the output when an exception was raised:

```python
Please enter the numerator: 5
Please enter the denominator: 0
Please enter valid integers. The denominator can't be zero
Inside the finally clause
```

Notice how the `finally` clause **always** runs.

**❗️Important:** remember that the `else` clause and the `finally` clause are optional, but if you decide to include both, the finally clause has to be the last clause in the sequence.

## 6️⃣ Raising Exceptions

Now that you know how to handle exceptions in Python, I would like to share with you this helpful tip: **you can also choose when to raise exceptions in your code.** 

This can be helpful for certain scenarios. Let's see how you can do this:

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-20.png)

This line will raise a ValueError with a custom message.

Here we have an example (see below) of a function that prints the value of the items of a list or tuple, or the characters in a string. But you decided that you want the list, tuple, or string to be of length 5. You start the function with an if statement that checks if the length of the argument `data` is 5. If it isn't, a ValueError exception is raised:

```python
def print_five_items(data):
    
    if len(data) != 5:
        raise ValueError("The argument must have five elements")
    
    for item in data:
        print(item)

print_five_items([5, 2])
```

The output would be:

```python
Traceback (most recent call last):
  File "<path>", line 122, in <module>
    print_five_items([5, 2])
  File "<path>", line 117, in print_five_items
    raise ValueError("The argument must have five elements")
ValueError: The argument must have five elements
```

Notice how the last line displays the descriptive message:

```python
ValueError: The argument must have five elements
```

You can then choose how to handle the exception with a try ... except statement. You could add an else clause and/or a finally clause. You can customize it to fit your needs. 

### 🔹 Helpful Resources

* [Exceptions](https://docs.python.org/3/tutorial/errors.html#exceptions)
* [Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
* [Defining Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)

**I hope you enjoyed reading my article and found it helpful.** Now you have the necessary tools to handle exceptions in Python and you can use them to your advantage when you write Python code. ? [Check out my online courses](https://www.udemy.com/user/estefania-cn/). You can follow me on [Twitter](https://twitter.com/EstefaniaCassN). 

⭐️ You may enjoy my other freeCodeCamp /news articles:

* [The @property Decorator in Python: Its Use Cases, Advantages, and Syntax](https://www.freecodecamp.org/news/python-property-decorator/)
* [Data Structures 101: Graphs — A Visual Introduction for Beginners](https://www.freecodecamp.org/news/data-structures-101-graphs-a-visual-introduction-for-beginners-6d88f36ec768/)
* [Data Structures 101: Arrays — A Visual Introduction for Beginners](https://www.freecodecamp.org/news/data-structures-101-arrays-a-visual-introduction-for-beginners-7f013bcc355a/)

