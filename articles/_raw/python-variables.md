---
title: Python Variables – The Complete Beginner's Guide
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-03-22T18:30:52.000Z'
originalURL: https://freecodecamp.org/news/python-variables
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/mugshotbot.com_customize_color-yellow-image-9820e115-mode-light-pattern-texture-theme-two_up-url-https___gifcoins.io.png
tags:
- name: Python
  slug: python
- name: variables
  slug: variables
seo_title: null
seo_desc: 'Variables are an essential part of Python. They allow us to easily store,
  manipulate, and reference data throughout our projects.

  This article will give you all the understanding of Python variables you need to
  use them effectively in your projects.

  ...'
---

Variables are an essential part of Python. They allow us to easily store, manipulate, and reference data throughout our projects.

This article will give you all the understanding of Python variables you need to use them effectively in your projects.

If you want the most convenient way to review all the topics covered here, I've put together a helpful cheatsheet for you right here:

**[Download the](https://reedbarger.com/resources/python-variables)** Python variables cheatsheet (it takes 5 seconds).

## What is a Variable in Python?

So what are variables and why do we need them?

Variables are essential for holding onto and referencing values throughout our application. By storing a value into a variable, you can reuse it as many times and in whatever way you like throughout your project. 

You can think of variables as boxes with labels, where the label represents the variable name and the content of the box is the value that the variable holds.

In Python, variables are created the moment you give or **assign** a value to them.

## How Do I Assign a Value to a Variable?

Assigning a value to a variable in Python is an easy process. 

You simply use the equal sign `=` as an assignment operator, followed by the value you want to assign to the variable. Here's an example:

```python
country = "United States"
year_founded = 1776
```

In this example, we've created two variables: `country` and `year_founded.` We've assigned the string value "United States" to the `country` variable and integer value 1776 to the `year_founded` variable.

There are two things to note in this example:

1. Variables in Python are **case-sensitive**. In other words, watch your casing when creating variables, because `Year_Founded` will be a different variable than `year_founded` even though they include the same letters
2. Variable names that use multiple words in Python should be separated with an underscore `_`_._ For example, a variable named "site name" should be written as "site_name"_._ This convention is called **snake case** (very fitting for the "Python" language).

## How Should I Name My Python Variables?

There are some rules to follow when naming Python variables. 

Some of these are hard rules that must be followed, otherwise your program will not work, while others are known as **conventions**. This means, they are more like suggestions.

### Variable naming rules

1. Variable names must start with a letter or an underscore `_` character.
2. Variable names can only contain letters, numbers, and underscores.
3. Variable names cannot contain spaces or special characters.

```python
user_age = 20 # valid

website = 'https://freecodecamp.org' # valid

1password = True # invalid
```

### Variable naming conventions

1. Variable names should be descriptive and not too short or too long.
2. Use lowercase letters and underscores to separate words in variable names (known as "snake_case").

## What Data Types Can Python Variables Hold?

One of the best features of Python is its flexibility when it comes to handling various data types.

Python variables can hold various data types, including integers, floats, strings, booleans, tuples and lists:

**Integers** are whole numbers, both positive and negative.

```python
answer = 42
```

**Floats** are real numbers or numbers with a decimal point.

```python
weight = 34.592
```

**Strings** are sequences of characters, namely words or sentences.

```python
message = "Hello Python"
```

**Booleans** are True or False values.

```python
is_authenticated = True

```

**Lists** are ordered, mutable collections of values.

```python
fruits = ['apple', 'banana', 'cherry']
```

**Tuples** are ordered, immutable collections of values.

```python
point = (3, 4)

```

There are more data types in Python, but these are the most common ones you will encounter while working with Python variables.

## Python is Dynamically Typed

Python is what is known as a **dynamically-typed** language. This means that the type of a variable can change during the execution of a program. 

Another feature of dynamic typing is that it is not necessary to manually declare the type of each variable, unlike other programming languages such as Java.

You can use the `type()` function to determine the type of a variable. For instance:

```python
print(type(answer))  # Output: <class 'int'>
print(type(message))  # Output: <class 'str'>

```

## What Operations Can Be Performed?

Variables can be used in various operations, which allows us to transform them mathematically (if they are numbers), change their string values through operations like concatenation, and compare values using equality operators.

### Mathematic Operations

It's possible to perform basic mathematic operations with variables, such as addition, subtraction, multiplication, and division:

```python
# Arithmetic operations
a = 10
b = 5

sum = a + b
difference = a - b
product = a * b
quotient = a / b

print(sum, difference, product, quotient)  # Output: 15 5 50 2.0
```

It's also possible to find the remainder of a division operation by using the modulus `%` operator as well as create exponents using the `**` syntax:

```python
# Modulus operation
remainder = a % b
print(remainder)  # Output: 0

# Exponentiation
power = a ** b
print(power)  # Output: 100000
```

### String operators

Strings can be added to one another or **concatenated** using the `+` operator.

```python
# String concatenation
first_name = "Guido"
last_name = "van Rossum"
full_name = first_name + " " + last_name
print(full_name)  # Output: Guido van Rossum
```

### Equality comparisons

Values can also be compared in Python using the `<`, `>`, `==`, and `!=` operators. 

These operators, respectively, compare whether values are less than, greater than, equal to, or not equal to each other.

```python
# Comparison operations
x = 15
y = 20

print(x < y)  # Output: True
print(x > y)  # Output: False
print(x == y)  # Output: False
print(x != y)  # Output: True
```

Finally, note that when performing operations with variables, you need to ensure that the types of the variables are compatible with each other. 

For example, you cannot directly add a string and an integer. You would need to convert one of the variables to a compatible type using a function like `str()` or `[int()](https://www.freecodecamp.org/news/python-string-to-int-convert-a-string-example/)`. 

## Variable Scope

The scope of a variable refers to the parts of a program where the variable can be accessed and modified. In Python, there are two main types of variable scope:

**Global scope**: Variables defined outside of any function or class have a global scope. They can be accessed and modified throughout the program, including within functions and classes.

```python
global_var = "I am a global variable"

def access_global_var():
    print(global_var)

access_global_var()  # Output: I am a global variable

```

**Local scope**: Variables defined within a function or class have a local scope. They can only be accessed and modified within that function or class.

```python
def function_with_local_var():
    local_var = "I am a local variable"
    print(local_var)

function_with_local_var()  # Output: I am a local variable
print(local_var)  # Error: NameError: name 'local_var' is not defined

```

In this example, attempting to access `local_var` outside of the `function_with_local_var` function results in a `NameError`, as the variable is not defined in the global scope.

## Conclusion

Don't be afraid to experiment with different types of variables, operations, and scopes to truly grasp their importance and functionality. The more you work with Python variables, the more confident you'll become in applying these concepts.

Finally, if you want to fully learn all of these concepts, I've put together for you a super helpful cheatsheet that summarizes everything we've covered here.

Just click the link below to grab it for free. Enjoy!

**[Download the](https://reedbarger.com/resources/python-variables)** Python variables cheatsheet

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

