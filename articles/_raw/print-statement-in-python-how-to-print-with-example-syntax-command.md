---
title: Print Statement in Python – How to Print with Example Syntax Command
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-12-10T17:45:08.000Z'
originalURL: https://freecodecamp.org/news/print-statement-in-python-how-to-print-with-example-syntax-command
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-wendelin-jacober-1440504.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'How to print out information is one of the first things you learn as a
  beginner programmer.

  This article goes over what you need to know about printing in Python, and we''ll
  look at plenty of code examples along the way.

  Let''s get started!

  What is pri...'
---

How to print out information is one of the first things you learn as a beginner programmer.

This article goes over what you need to know about printing in Python, and we'll look at plenty of code examples along the way.

Let's get started!

## What is print used for?

Printing is most likely the first thing you'll learn when you embark on your Python learning journey.

It is somewhat of a tradition to write a "Hello World" program as your first lines of code. And you do that by using the `print()` function to output that piece of text to the console.

Printing is mostly used for displaying information to the console, whether it's showing a certain message or computational result. But it's also used for debugging purposes.

### Printing in Python 2 vs printing in Python 3

In order to print something to the console in Python 2, all you had to do was use the `print` keyword:

```python
print "Hello world"

#output
#Hello world
```

This was called a print statement.

In Python 3 the print statement was replaced by the `print()` function.

```python
print("Hello world")

#output
#Hello world
```

If you don't add the set of opening and closing parentheses that follow `print` in Python 3, you'll get an error when you run the code:

```python
print "Hello world"

#output
#File "/Users/dionysialemonaki/python_articles/demo.py", line 1
#    print "Hello world"
#   ^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean #print(...)?
```

So in Python 2, the print keyword was a statement, whereas in Python 3 print is a function.

## `print()` Syntax in Python

The full syntax of the `print()` function, along with the default values of the parameters it takes, are shown below.

This is what `print()` looks like underneath the hood:

```
print(*object,sep=' ',end='\n',file=sys.stdout,flush= False)
```

Let's break it down:

- `*object` can be none, one, or many data values to be printed, and it can be of any data type. Objects get converted to a string before printing.
- `sep` is an optional parameter that specifies how more than one object are separated. The default is `' '` – a space.
- `end` is an optional paramater that specifies with what the line will end. By default the print call ends with a newline, with `\n` being the newline character.
- `file` is an optional paramater which is an object with a write method – it can write and append (add) the output to a file. The default is `sys.stdout` (or system standard output) and the output is displayed on the screen.
- `flush` is a boolean parameter that specifies whether the stream will be forcibly flushed or buffered. Flushed means whether the print call will immediately take affect. The default value is False (or buffered).

The `print()` function has no return value.

## How to Print Objects in Python

Even if you don't pass in any arguments to `print()` – that is you don't pass any object/s to be printed – you still need to include a set of empty parentheses.

This will just output a blank line to the console in such a case.

This is best illustrated when using the Python REPL (Read Eval Print Loop).

To start a new session, after installing Python on your machine type `python3`. When you're done, type `exit()` to end the session.

```python
>>> print()

>>> 
```

It's similar to hitting they `Enter` key on your keyboard when writing in a word processor. Just like the Enter key creates a new line and moves the cursor to a new line, in the same way calling `print()` with no arguments displays an empty line.

## How to Print Strings in Python

You print strings by passing the string literal as an argument to `print()`, enclosed in either single or double quotation marks.

The output will be the string literal, without the quotes.

```python
print("I am learning Python")

#output
#I am learning Python
```

If you have a set string or phrase you want to print, you can store it in a variable and pass the variable name as the argument to `print()`.

```python
greeting = "Hey there!"

print(greeting)

#output
#Hey there!
```

It's a best practice to give meaningful names to variables, according to the content stored inside them. This will make code more readable for yourself and anyone else you're working with.

As shown in the `print()` syntax earlier, there can be more than one object passed as arguments (`*object`).

You can do this by **separating each argument with a comma**.

```python
print("Hello","there!")

#output
#Hello there!
```
There are two arguments: "Hello" and "there!".

In the examples below, the arguments are a string literal and a variable.

```python
full_name = "John Doe"

print("Hey",full_name)

#output
#Hey John Doe
```

You can also do this using **concatenation** with the addition operator:

```python
full_name = "John Doe"

print("Hey " + full_name)

#output
#Hey John Doe
```

With concatenation, you have to account for the spaces otherwise you'll end end up with the following:

```python
full_name = "John Doe"

print("Hey" + full_name)

#output
#HeyJohn Doe
```

Keep in mind that you cannot add a string literal with a number.

This would result in an error:

```python
print("Hey" + 7)

#output
#Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_articles/demo.py", line 1, in #<module>
#    print("Hey" + 7)
#TypeError: can only concatenate str (not "int") to str
```

As the error suggests, you can only concatenate (add) a string to a string. This means that if you want to include a number, you'd have to convert it to its string equivalent by typecasting.

```python
#use the str() method to convert an integer to a string

print("Hey" + str(7))

#output
#Hey 7
```

A modern way to print objects is by using **`f-strings`**.

```python
full_name = "John Doe"

print(f"Hey there {full_name}")

#output
#Hey there John Doe
```

Strings are not the only objects that can be passed as arguments.

In fact, `print()` accepts all kinds of data types which you'll see in the section that follows.

### Examples of how to print the rest of Python's built-in data types

```python
#how to print ints
print(7) #output is 7

#how to print floats
print(7.0) #output is 7.0

#how to print complex
print(1j) #output is 1j

#how to print a list
print([10,20,30]) #output is [10,20,30]

#how to print a tuple
print((10,20,30)) #output is (10,20,30)

#how to print a dictionary
print({"language": "Python", "field": "data science"})
#output is {"language": "Python", "field": "data science"

#how to print a set
print({"autumn","winter","spring","summer"})
#output is {"autumn","winter","spring","summer"}

#how to print a bool
print(True) #output is True
print(False) #output is False
```

## How to Change the Way Objects Are Separated in the `print()` Function

As you've seen in the syntax for the `print()` function, `sep` determines how one object is separated from the next.

By default objects are separated by a single space.

```python
print("Hello","World")

#output
#Hello World
```

To disable that, you explicitly change the value of `sep` to the character you want.

For example, objects can be separated by dashes:
```python
print("Hello","World", sep="---")

#output
#Hello---World
```

Or you could even remove the space by adding an empty string instead:

```python
print("Hello","World", sep="")

#output
#HelloWorld
```

## How to Remove the Default Newline in `print()`

As you saw ealier in the syntax breakdown of the `print()` function, the default parameter for the keyword argument `end` was `'\n'`.

By default, after each print call, a new line is created.

If you call print two times separately, one after the other, you'll see that the second call is displayed on a newline immediately after the first call.

```python
print("Hello")
print("World")

#output
#Hello
#World
```

To disable that, you can explicitly change the value of `end` to an empty string, `""`.

```python
print("Hello ", end="")
print("World")

#output
#Hello World
```

Now both are on the same line.

You can even change it to a full stop:

```python
print("Hello", end=".")
print("World")

#output
#Hello.World
```

Anything that isn't the default value will supress the newline that gets created.

## How to Direct the `print()` Output to a File in Python

You'll mostly want to print the output to the standard output, or the command line standard output.

There may be times, however, when you'll want to direct that output to an existing file.

Say you have a text file and want to add some text using the `print()` function.

To open and write to a file in Python, you call the `open()` function. Inside it you include the name of the file, `output.txt` in this case, and the `-w` mode, meaning for writing only.

With this mode, each time you run your code the contents of the file will be deleted and replaced by any new text you add.

If you don't want to lose any content, you could use the `-a` mode instead, for appending text to the end of the file.

Inside the `print()` function you add any text you want to add to the file and set the `file` parameter equal to the placeholder name you created for the file you want to add the text to, in this case `f`.

```python
with open('output.txt', 'w') as f:
    print('Hello World!', file=f)
```

## Conclusion

Thanks for reading and making it to the end! I hope you found this tutorial helpful. You now know the basics of how to use the `print()` function in Python.

If you are interested in learning more about the Python programming language, check out freeCodeCamp's [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) to get you started. 

It covers all the fundamental programming concepts and gradually progresses to more advanced topics. In the end, you'll also build five projects to solidify your learning.

Happy coding!


