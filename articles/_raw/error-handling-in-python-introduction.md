---
title: Error Handling in Python – try, except, else, & finally Explained with Code
  Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-04-11T00:09:53.000Z'
originalURL: https://freecodecamp.org/news/error-handling-in-python-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/game-over-screen.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Gage Schaffer

  Just recently, my manager tasked me to create an automatic report. I designed the
  report to be simple. It included a few numbers from a database and some basic mathematical
  operations. I was excited to finally be able to show off my ...'
---

By Gage Schaffer

Just recently, my manager tasked me to create an automatic report. I designed the report to be simple. It included a few numbers from a database and some basic mathematical operations. I was excited to finally be able to show off my _amazing_ Python skills to the company.

I finished and shipped the product. Everything was great. At least, until about two weeks later. My report began failing randomly due to a divide-by-zero error. Cue the laugh track.

My short story is absent details, but it should highlight the importance of handling edge cases and errors when composing programs. This report should have been an opportunity to show off my Python prowess. Yet, it turned into a bit of an embarrassing, fall-on-my-face moment.

So, let’s take a moment to learn the basics of error handling using Python’s standard library. I’m going to highlight some of the things you need to get started.

Before you start handling exceptions, you should have a good grasp of Python fundamentals. You’ll need to know why the exceptions are being thrown to deal with them!

### Here's what we'll cover:

1. [Try and Except Statements in Python](#heading-try-and-except-statements-in-python)
2. [Conditional Execution with the Else Clause](#heading-conditional-execution-with-the-else-clause)
3. [Built-in Exceptions](#heading-built-in-exceptions)
4. [Custom Exceptions](#heading-custom-exceptions)
5. [Performance Considerations](#heading-performance-considerations)

## Try and Except Statements in Python

The `try` and `except` statements are the primary method of dealing with exceptions. They look something like this:

```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("Something went wrong")
    
# Something went wrong
```

Let’s review the above code so we are on the same page:

1. Line 1 assigns the value 0 to a variable `x`
2. Lines 2 and 3 open a `try` clause and attempt to divide 5 by the variable `x`
3. Lines 4 and 5 open an `except` clause for any `ZeroDivisionError` and instruct 	the program to print a message should we try to divide anything by 0

You likely notice the issue. My variable `x` has the value 0, and I am trying to divide 5 by `x`. The best mathematicians in the world can’t divide by 0, and neither can Python. So, what happens?

If we do not handle the error, the program will immediately terminate upon trying to divide 5 by `x`. Since programs do not know what to do with exceptions without explicit instructions, we created the `except` clause on line 4 and provided the steps for the program to take in the event of dividing something by 0.

That’s the whole idea behind handling exceptions: you need to tell the program what to do when it has an error that it cannot simply ignore. Let’s look at how the `try` and `except` clauses work.

### Breaking Down the Try Statement

`Try` and `Except` statements follow a pattern that allows you to reliably handle problems in your code. Let’s go over the pattern.

The first step that happens is, the code in the `try` clause attempts to execute.

After that, we have three possibilities:

#### No Errors in the Try Clause

If the code in the `try` clause executes **without any errors**, the program will:

1. Execute the `try` clause
2. Skip all `except` clauses
3. Continue running as normal

```python
x = 1
try:
    print(5 / x)
except ZeroDivisionError:
    print("Something went wrong")

print("I am executing after the try clause!")

# 5.0
# I am executing after the try clause!
```

You can see that, in this modified example, there are no issues in the `try` clause (Lines 3 and 4). The code will execute, the `except` clause will be skipped, and the program will resume execution after the `try` and `except` statements conclude.

#### Errors in the Try Clause and the Exception is Specified

If the code in the `try` clause **does throw an exception** and **the type of exception is specified after any `except` keyword**, the program will:

1. Skip the remaining code in the `try` clause
2. Execute any code in the matching `except` clause
3. Continue running as normal

```python
x = 0
try:
    print(5 / x)
except:
    print("Something went wrong")
    
print("I am executing after the try clause!")

# Something went wrong
# I am executing after the try clause!
```

Back to my first example, I changed our variable `x` back to the value 0 and tried to divide 5 by `x`. This produces a `ZeroDivisionError`. Since my `except` statement specifies this type of exception, the code in that clause executes before the program resumes running as normal.

#### Errors in the Try Clause and the Exception is not Specified

Finally, if the program throws an exception in the `try` clause, **but the exception is not specified in any `except` statements**, then the program will:

1. Stop the execution of the program and throw the error

```python
x = 0
try:
    print(5 / y)
except:
    print("Something went wrong")

print("I am executing after the try clause!")

# NameError: name 'y' is not defined
```

In the above example, I’m trying to divide 5 by the variable `y`, which does not exist. This raises a `NameError`. I don’t specify to the program how to handle `NameError`s, so the only option is to terminate itself.

### Cleaning Up

`Try` and `except` are the main tools in handling errors, but an optional clause that you can use is named `finally`. The `finally` clause will always execute, whether there is an error or not.

```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("I am the except clause!")
finally:
    print("I am the finally clause!")

print("I am executing after the try clause!")

# I am the except clause!
# I am the finally clause!
# I am executing after the try clause!
```

In this example, I have created our favorite `ZeroDivisionError`. You can see that the order of execution is:

1. The `except` clause
2. The `finally` clause
3. Any code afterwards

Once we fix the `try` clause to no longer throw an error, you’ll still see a similar order of execution. Instead of the `except` clause running, the `try` clause will execute. 

```python
x = 1
try:
    print(5 / x)
except ZeroDivisionError:
    print("I am the except clause!")
finally:
    print("I am the finally clause!")

print("I am executing after the try clause!")

# 5.0
# I am the finally clause!
# I am executing after the try clause!
```

You’ll notice that the only difference is that `try` clause is successfully executed because there are no exceptions thrown. The `finally` clause and the code afterwards execute as you would expect.

This is useful for some cases when you want to clean up no matter the outcome of your `try` and `except` clauses. Actions such as closing connections, closing files, and logging are great candidates for the `finally` clause.

## Conditional Execution with the Else Clause

The other optional clause is the `else` clause. The `else` clause is simple: if the code in the `try` clause executes without throwing an error, then the code in the `else` clause will also execute.

```python
x = 1
try:
    print(5 / x)
except ZeroDivisionError:
    print("I am the except clause!")
else:
    print("I am the else clause!")
finally:
    print("I am the finally clause!")

print("I am executing after the try clause!")

# 5.0
# I am the else clause!
# I am the finally clause!
# I am executing after the try clause!
```

The order of execution for this example is:

1. The `try` clause
2. The `else` clause
3. The `finally` clause
4. Any code afterwards

If we were to experience an exception or error in the `try` clause, the `else` clause would be ignored.

```python
x = 0
try:
    print(5 / x)
except ZeroDivisionError:
    print("I am the except clause!")
else:
    print("I am the else clause!")
finally:
    print("I am the finally clause!")

print("I am executing after the try clause!")

# I am the except clause!
# I am the finally clause!
# I am executing after the try clause!
```

## Built-in Exceptions

You’ve seen me write about two different named exceptions so far: `NameError` and `ZeroDivisionError`. What if I needed other exceptions? 

There is an entire list of Python’s exceptions that come with the standard library. These will probably suit almost every need that you have in handling any errors or exceptions.

Here are just a few that might be important:

* `KeyError` – A key cannot be found in a dictionary
* `IndexError` – The index is out-of-bounds on an iterable object
* `TypeError` – A function or operation was used on the wrong type of object
* `OSError` – General operating system errors

There are a whole lot more, which can be found in the Python documentation. I encourage to take a look. Not only will you be better at handling errors, but you will also explore what _actually_ can go wrong with your Python programs.

## Custom Exceptions

If you need extended functionality, you can also define custom exceptions.

```python
class ForError(Exception):
    def __init__(self, message):
        self.message = message
    
    def foo(self):
        print("bar")
```

In the above example, I create a new class and extend it from the Exception class. Now, I can write custom functionality and treat this exception as any other object.

```python
try:
    raise FooError("This is a test error")
except FooError as e:
    e.foo()

# bar
```

Here, I raise my new `FooError` on purpose. I catch the `FooError` and give it an alias of `e`. Now, I can access my `foo()` method that I built into the class that I created. 

This opens a whole plethora of possibilities when dealing with errors. Custom logging, more in-depth tracking, or whatever else you need can all be coded and created.

## Performance Considerations

Now that you understand the basics of `try`, `except`, and exception objects, you can start considering using them in your code to gracefully handle errors. Are there any considerable impacts to code performance, though?

The short answer is no. With the release of Python 3.11, there is practically no speed reduction from using `try` and `except` statements when there are no thrown exceptions. 

Catching errors did cause some slowdowns. But generally, catching these errors is better than having the entire program crash and burn.

In earlier versions of Python, using `try` and `except` clauses did cause some extra execution time. Keep this in mind if you’re not up to date.

## To Recap

Thank you for reading this far. Your future self and customers will thank you for your error handling.

We went over the `try`, `except`, `else`, and `finally` clauses and their execution order and under what circumstances they are executed. We also reviewed the basics of creating custom exceptions. 

The most important thing to remember is that the `try` and `except` clauses are the primary ways to catch errors, and you should be using them whenever you have risky, error-prone code.

Also, keep in mind that catching errors will make your code more resilient, and make you look like a much better coder.

