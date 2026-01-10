---
title: Python Convert String to Int – How to Cast a String in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-29T16:47:01.000Z'
originalURL: https://freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/glenn-carstens-peters-npxXWgQ33ZQ-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When you''re programming, you''ll often need to switch between data types.

  The ability to convert one data type to another gives you great flexibility when
  working with information.

  There are different built-in ways to convert, or cast, types in the Py...'
---

When you're programming, you'll often need to switch between data types.

The ability to convert one data type to another gives you great flexibility when working with information.

There are different built-in ways to convert, or cast, types in the Python programming language.

In this article, you'll learn how to convert a string to an integer.

Let's get started!

## Data types in Python

Python supports a variety of data types.

Data types are used for specifying, representing, and categorizing the different kinds of data that exist and are used in computer programs. 

Also, different operations are available with different types of data – one operation available in one data type is often not available in another.

One example of a data type is strings.

Strings are sequences of characters that are used for conveying textual information. 

They are enclosed in single or double quotation marks, like so:

```python
fave_phrase = "Hello world!"

#Hello world! is a string,enclosed in double quotation marks
```

Ints, or integers, are whole numbers. 

They are used to represent numerical data, and you can do any mathematical operation (such as addition, subtraction, multiplication, and division) when working with integers.

Integers are *not* enclosed in single or double quotation marks.

```python
fave_number = 7

#7 is an int
#"7" would not be an int but a string, despite it being a number. 
#This is because of the quotation marks surrounding it
```

### Data type conversion

Sometimes when you're storing data, or when you receive input from a user in one type, you'll need to manipulate and perform different kinds of operations on that data.

Since each data type can be manipulated in different ways, this often means that you'll need to convert it.

Converting one data type to another is also called type casting or type conversion. Many languages offer built-in cast operators to do just that – to explicitly convert one type to another.

## How to convert a string to an integer in Python

To convert, or cast, a string to an integer in Python, you use the `int()` built-in function.

The function takes in as a parameter the initial string you want to convert, and returns the integer equivalent of the value you passed.

The general syntax looks something like this: `int("str")`.

Let's take the following example, where there is the string version of a number:

```python
#string version of the number 7
print("7")

#check the data type with type() method
print(type("7"))

#output

#7
#<class 'str'>
```

To convert the string version of the number to the integer equivalent, you use the `int()` function, like so:

```python
#convert string to int data type
print(int("7"))

#check the data type with type() method
print(type(int("7")))

#output

#7
#<class 'int'>
```

### A practical example of converting a string to an int

Say you want to calculate the age of a user. You do this by receiving input from them. That input will always be in string format.

So, even if they type in a number, that number will be of `<class 'str'>`.

If you want to then perform mathematical operations on that input, such as subtracting that input from another number, you will get an error because you can't carry out mathematical operations on strings.

Check out the example below to see this in action:

```python
current_year = 2021

#ask user to input their year of birth
user_birth_year_input = input("What year were you born? ")

#subtract the year the user filled in from the current year 
user_age = current_year - user_birth_year_input

print(user_age)

#output

#What year were you born? 1993
#Traceback (most recent call last):
#  File "demo.py", line 9, in <module>
#    user_age = current_year - user_birth_year_input
#TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

The error mentions that subtraction can't be performed between an int and a string.

You can check the data type of the input by using the `type()` method:

```python
current_year = 2021

#ask user to input their year of birth
user_birth_year_input = input("What year were you born? ")

print(type(user_birth_year_input))

#output

#What year were you born? 1993
#<class 'str'>
```

The way around this and to avoid errors is to convert the user input to an integer and store it inside a new variable:

```python
current_year = 2021

#ask user to input their year of birth
user_birth_year_input = input("What year were you born? ")

#convert the raw user input to an int using the int() function and store in new variable
user_birth_year = int(user_birth_year_input)

#subtract the converted user input from the current year
user_age = current_year - user_birth_year

print(user_age)

#output

#What year were you born? 1993
#28
```

## Conclusion

And there you have it - you now know how to convert strings to integers in Python!

If you want to learn more about the Python programming language, freeCodeCamp has a [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) to get you started. 

You'll start with the fundamentals and progress to more advance topics like data structures and relational databases. In the end, you'll build five projects to practice what you learned.

Thanks for reading and happy coding!


