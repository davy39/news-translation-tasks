---
title: How to Define And Call Functions in Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-03T21:18:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-define-and-call-functions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/CD.JPG
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python is a powerful and versatile programming language that offers a wide
  range of functionalities for developers.

  One of the most essential features of Python is the ability to define and call functions.

  A function is a block of code that performs ...'
---

Python is a powerful and versatile programming language that offers a wide range of functionalities for developers.

One of the most essential features of Python is the ability to define and call functions.

A function is a block of code that performs a specific task. In Python, defining and calling functions is easy and can greatly improve the readability and reusability of your code.

## How to Define a Function

Defining a function in Python involves two main steps: defining the function and specifying the arguments it takes.

To define a function, you use the def keyword followed by the name of the function and parentheses (). If the function takes any arguments, they are included within the parentheses. The code block for the function is then indented after the colon.

Here's an example:

```python
def greet(name):
    print("Hello, " + name + "! How are you?")
```

In this example, we define a function called `greet` that takes one argument called `name`. The function then prints out a greeting message to the console that includes the name argument.

## How to Call a Function

Once you have defined a function, you can call it in your code as many times as you need.

To call a function in Python, you simply type the name of the function followed by parentheses (). If the function takes any arguments, they are included within the parentheses.

Here's an example:

```python
greet("John")
```

In this example, we call the greet function with the argument "John". The output to the console would be:

```python
Hello, John! How are you?
```

## Python Function Code Examples

Here's a complete code example that defines and calls the greet function:

```python
def greet(name):
    print("Hello, " + name + "! How are you?")

greet("John")
```

When you run this code, it will output the following to the console:

```python
Hello, John! How are you?
```

Let's take a more advanced example of defining and calling functions in Python.

Let's say you want to write a function that takes in a list of integers and returns a new list with all the even numbers in the original list. Here's how you could define and call this function:

```python
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
```

In this example, we define a function called get\_even\_numbers that takes one argument called numbers. The function then creates an empty list called even\_numbers and loops through each number in the numbers list.

If the number is even, it is added to the even\_numbers list using the append method. Finally, the function returns the even\_numbers list.

To call this function, we first create a list of numbers called numbers with the values \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]. We then call the get\_even\_numbers function with the numbers list as an argument and assign the returned value to a new list called even\_numbers.

Finally, we print out the even\_numbers list to the console.

When you run this code, it will output the following to the console:

```python
[2, 4, 6, 8, 10]
```

This is the list of even numbers in the original numbers list.

This example demonstrates how to define a more complex function that performs a specific task, and how to call that function with the appropriate arguments.

By breaking down complex tasks into smaller, reusable functions, you can make your code more readable, maintainable, and efficient.

## Conclusion

Defining and calling functions in Python is a straightforward process that can greatly improve the functionality and readability of your code.

With Python's simple syntax and powerful capabilities, you can define and call functions with any number of arguments and perform any number of tasks within the function code block.

So go ahead and start defining and calling functions in your Python code to take your programming skills to the next level.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
