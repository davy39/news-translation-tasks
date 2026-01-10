---
title: Python Function Guide with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T22:43:00.000Z'
originalURL: https://freecodecamp.org/news/python-function-guide-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d54740569d1a4ca372d.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Introduction to Functions in Python

  A function allows you to define a reusable block of code that can be executed many
  times within your program.

  Functions allow you to create more modular and DRY solutions to complex problems.

  While Python already p...'
---

## Introduction to Functions in Python

A function allows you to define a reusable block of code that can be executed many times within your program.

Functions allow you to create more modular and [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) solutions to complex problems.

While Python already provides many built-in functions such as `print()` and `len()`, you can also define your own functions to use within your projects.

One of the great advantages of using functions in your code is that it reduces the overall number of lines of code in your project.

### **Syntax**

In Python, a function definition has the following features:

1. The keyword `def`
2. a function name
3. paranthesis’()’, and within paranthesis input parameters,although the input parameters are optional.
4. a colon ’:’
5. some block of code to execute
6. a return statement (optional)

```python
# a function with no parameters or returned values
def sayHello():
  print("Hello!")

sayHello()  # calls the function, 'Hello!' is printed to the console

# a function with a parameter
def helloWithName(name):
  print("Hello " + name + "!")

helloWithName("Ada")  # calls the function, 'Hello Ada!' is printed to the console

# a function with multiple parameters with a return statement
def multiply(val1, val2):
  return val1 * val2

multiply(3, 5)  # prints 15 to the console
```

Functions are blocks of code that can be reused simply by calling the function. This enables simple, elegant code reuse without explicitly re-writing sections of code. This makes code both more readable, makes for easier debugging, and limits typing errors.

Functions in Python are created using the `def` keyword, followed by a function name and function parameters inside parentheses.

A function always returns a value,The `return` keyword is used by the function to return a value, if you don’t want to return any value, the default value `None` will returned.

The function name is used to call the function, passing the needed parameters inside parentheses.

```python
# this is a basic sum function
def sum(a, b):
  return a + b

result = sum(1, 2)
# result = 3
```

You can define default values for the parameters, that way Python will interpretate that the value of that parameter is the default one if none is given.

```python
def sum(a, b=3):
  return a + b

result = sum(1)
# result = 4
```

You can pass the parameters in the order you want, using the name of the parameter.

```python
result = sum(b=2, a=2)
# result = 4
```

However, it is not possible to pass a keyword argument before a non-keyword one

```python
result = sum(3, b=2)
#result = 5
result2 = sum(b=2, 3)
#Will raise SyntaxError
```

Functions are also Objects, so you can assign them to a variable, and use that variable like a function.

```python
s = sum
result = s(1, 2)
# result = 3
```

### **Notes**

If a function definition includes parameters, you must provide the same number of parameters when you call the function.

```python
print(multiply(3))  # TypeError: multiply() takes exactly 2 arguments (0 given)

print(multiply('a', 5))  # 'aaaaa' printed to the console

print(multiply('a', 'b'))  # TypeError: Python can't multiply two strings
```

The block of code that the function will run includes all statements indented within the function.

```python
def myFunc():
print('this will print')
print('so will this')

x = 7
# the assignment of x is not a part of the function since it is not indented
```

Variables defined within a function only exist within the scope of that function.

```python
def double(num):
x = num * 2
return x

print(x)  # error - x is not defined
print(double(4))  # prints 8
```

Python interprets the function block only when the function is called and not when the function is defined.So even if the function definition block contains some sort of error, the python interpreter will point that out only when the function is called.

Now let's look at some specific functions with examples.

## max() function

`max()` is a built-in function in Python 3. It returns the largest item in an iterable or the largest of two or more arguments.

### Arguments

This function takes two or more numbers or any kind of iterable as an argument. While giving an iterable as an argument we must make sure that all the elements in the iterable are of the same type. This means that we cannot pass a list which has both string and integer values stored in it. Syntax: max(iterable, *iterables[,key, default]) max(arg1, arg2, *args[, key])

Valid Arguments:

```text
max(2, 3)
max([1, 2, 3])
max('a', 'b', 'c')
```

Invalid Arguments:

```text
max(2, 'a')
max([1, 2, 3, 'a'])
max([])
```

### Return Value

The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned. If the iterable is empty and default is not provided, a `ValueError` is raised.

### Code Sample

```text
print(max(2, 3)) # Returns 3 as 3 is the largest of the two values
print(max(2, 3, 23)) # Returns 23 as 23 is the largest of all the values

list1 = [1, 2, 4, 5, 54]
print(max(list1)) # Returns 54 as 54 is the largest value in the list

list2 = ['a', 'b', 'c' ]
print(max(list2)) # Returns 'c' as 'c' is the largest in the list because c has ascii value larger then 'a' ,'b'.

list3 = [1, 2, 'abc', 'xyz']
print(max(list3)) # Gives TypeError as values in the list are of different type

#Fix the TypeError mentioned above first before moving on to next step

list4 = []
print(max(list4)) # Gives ValueError as the argument is empty
```

[Run Code](https://repl.it/CVok)

[Official Docs](https://docs.python.org/3/library/functions.html#max)

## min() function

`min()` is a built-in function in Python 3. It returns the smallest item in an iterable or the smallest of two or more arguments.

### Arguments

This function takes two or more numbers or any kind of iterable as an argument. While giving an iterable as an argument we must make sure that all the elements in the iterable are of the same type. This means that we cannot pass a list which has both string and integer values stored in it.

Valid Arguments:

```text
min(2, 3)
min([1, 2, 3])
min('a', 'b', 'c')
```

Invalid Arguments:

```text
min(2, 'a')
min([1, 2, 3, 'a'])
min([])
```

### Return Value

The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments  
is returned. If the iterable is empty and default is not provided, a ValueError is raised.

### Code Sample

```text
print(min(2, 3)) # Returns 2 as 2 is the smallest of the two values
print(min(2, 3, -1)) # Returns -1 as -1 is the smallest of the two values

list1 = [1, 2, 4, 5, -54]
print(min(list1)) # Returns -54 as -54 is the smallest value in the list

list2 = ['a', 'b', 'c' ]
print(min(list2)) # Returns 'a' as 'a' is the smallest in the list in alphabetical order

list3 = [1, 2, 'abc', 'xyz']
print(min(list3)) # Gives TypeError as values in the list are of different type

#Fix the TypeError mentioned above first before moving on to next step

list4 = []
print(min(list4)) # Gives ValueError as the argument is empty
```

[Run Code](https://repl.it/CVir/4)

[Official Docs](https://docs.python.org/3/library/functions.html#min)

# divmod() function

`divmod()` is a built-in function in Python 3, which returns the quotient and remainder when dividing the number `a` by the number `b`. It takes two numbers as arguments `a` & `b`. The argument can’t be a complex number.

### Argument

It takes two arguments `a` & `b` - an integer, or a decimal number.It can’t be a complex number.

### Return Value

The return value will be the pair of positive numbers consisting of quotient and remainder obtained by dividing `a` by `b`. In case of mixed operand types, rules for binary arithmetic operators will be applied.  
For **Integer number arguments**, return value will be same as `(a // b, a % b)`.  
For **Decimal number arguments**, return value will be same as `(q, a % b)`, where `q` is usually **math.floor(a / b)** but may be 1 less than that.

### Code Sample

```text
print(divmod(5,2)) # prints (2,1)
print(divmod(13.5,2.5)) # prints (5.0, 1.0)
q,r = divmod(13.5,2.5)  # Assigns q=quotient & r= remainder
print(q) # prints 5.0 because math.floor(13.5/2.5) = 5.0
print(r) # prints 1.0 because (13.5 % 2.5) = 1.0
```

[REPL It!](https://repl.it/FGLK/0)

[Official Docs](https://docs.python.org/3/library/functions.html#divmod)

## Hex(x) function

`hex(x)` is a built-in function in Python 3 to convert an integer number to a lowercase [hexadecimal](https://www.mathsisfun.com/hexadecimals.html) string prefixed with “0x”.

### Argument

This function takes one argument, `x`, that should be of integer type.

### Return

This function returns a lowercase hexadecimal string prefixed with “0x”.

### Example

```text
print(hex(16))    # prints  0x10
print(hex(-298))  # prints -0x12a
print(hex(543))   # prints  0x21f
```

[Run Code](https://repl.it/CV0S)

[Official Documentation](https://docs.python.org/3/library/functions.html#hex)

## len() function

`len()` is a built-in function in Python 3. This method returns the length (the number of items) of an object. It takes one argument `x`.

### Arguments

It takes one argument, `x`. This argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

### Return Value

This function returns the number of elements in the argument which is passed to the `len()` function.

### Code Sample

```text
list1 = [123, 'xyz', 'zara'] # list
print(len(list1)) # prints 3 as there are 3 elements in the list1

str1 = 'basketball' # string
print(len(str1)) # prints 10 as the str1 is made of 10 characters

tuple1 = (2, 3, 4, 5) # tuple 
print(len(tuple1)) # prints 4 as there are 4 elements in the tuple1

dict1 = {'name': 'John', 'age': 4, 'score': 45} # dictionary
print(len(dict1)) # prints 3 as there are 3 key and value pairs in the dict1
```

[Run Code](https://repl.it/CUmt/15)

[Official Docs](https://docs.python.org/3/library/functions.html#len)

## **Ord function**

`ord()` is a built-in function in Python 3, to convert the string representing one Unicode character into integer representing the Unicode code of the character.

#### **Examples:**

```text
>>> ord('d')
100
>>> ord('1')
49
```

## chr function

`chr()` is a built-in function in Python 3, to convert the integer representing the Unicode code into a string representing a corresponding character.

#### **Examples:**

```text
>>> chr(49)
'1'
```

One thing is to be noted that, if the integer value passed to `chr()` is out of range then, a ValueError will be raised.

```text
>>> chr(-10)
'Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    chr(-1)
ValueError: chr() arg not in range(0x110000)'
```

## input() functions

Many a time, in a program we need some input from the user. Taking inputs from the user makes the program feel interactive. In Python 3, to take input from the user we have a function `input()`. If the input function is called, the program flow will be stopped until the user has given an input and has ended the input with the return key. Let’s see some examples:

When we just want to take the input:

# **This will just give a prompt without any message**

inp = input()

[Run Code](https://repl.it/CUqX/0)

To give a prompt with a message:

prompt_with_message = input(’‘)

# **_**

# **The ’_’ in the output is the prompt**

[Run Code](https://repl.it/CUqX/1)

3. When we want to take an integer input:

```text
number = int(input('Please enter a number: '))
```

[Run Code](https://repl.it/CUqX/2)

If you enter a non integer value then Python will throw an error `ValueError`. **So whenever you use this, please make sure that you catch it too.** Otherwise, your program will stop unexpectedly after the prompt.

```text
number = int(input('Please enter a number: '))
# Please enter a number: as
# Enter a string and it will throw this error
# ValueError: invalid literal for int() with base 10 'as'
```

4. When we want a string input:

```text
string = str(input('Please enter a string: '))
```

[Run Code](https://repl.it/CUqX/3)

Though, inputs are stored by default as a string. Using the `str()` function makes it clear to the code-reader that the input is going to be a ‘string’. It is a good practice to mention what type of input will be taken beforehand.

[Official Docs](https://docs.python.org/3/library/functions.html#input)

## How to call a function in Python

A function definition statement does not execute the function. Executing (calling) a function is done by using the name of the function followed by parenthesis enclosing required arguments (if any).

```text
>>> def say_hello():
...     print('Hello')
...
>>> say_hello()
Hello
```

The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.

```text
>>> a = 1
>>> b = 10
>>> def fn():
...     print(a)    # local a is not assigned, no enclosing function, global a referenced.
...     b = 20      # local b is assigned in the local symbol table for the function.
...     print(b)    # local b is referenced.
...
>>> fn()
1
20
>>> b               # global b is not changed by the function call.
10
```

The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object). When a function calls another function, a new local symbol table is created for that call.

```text
>>> def greet(s):
...     s = "Hello " + s    # s in local symbol table is reassigned.
...     print(s)
...
>>> person = "Bob"
>>> greet(person)
Hello Bob
>>> person                  # person used to call remains bound to original object, 'Bob'.
'Bob'
```

The arguments used to call a function cannot be reassigned by the function, but arguments that reference mutable objects can have their values changed:

```text
>>> def fn(arg):
...     arg.append(1)
...
>>> a = [1, 2, 3]
>>> fn(a)
>>> a
[1, 2, 3, 1]
```




