---
title: Python Comment Block – How to Comment Out Code in Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-11T20:11:40.000Z'
originalURL: https://freecodecamp.org/news/python-comment-block-how-to-comment-out-code-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/comments-python.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, we'll talk about comments in Python, why they are important,\
  \ and how to use them effectively in your code. \nWhen to Use Comments\nIn this\
  \ section, we'll talk about some of the general use cases for comments. These aren't\
  \ only applicab..."
---

In this article, we'll talk about comments in Python, why they are important, and how to use them effectively in your code. 

## When to Use Comments

In this section, we'll talk about some of the general use cases for comments. These aren't only applicable to Python, but to most programming languages. 

Here are some of the main reasons to comment your code:

* **Preventing code execution**: In some cases, you'll need to prevent a part of your code from running. This may be because you have no use for that code at the moment, but you want to add it anyway for future functionality.
* **Readability**: This is very important – not just for ourselves but for other developers. We can use comments to explain what each code block does. This is useful when other developers are reading our code, as it makes it easy to understand what each part of the code does.

## How to Comment out Code in Python

The syntax for comments differs in each programming language. In this section, we'll see how to add comments using Python.

Comments in Python start with the `#` symbol. Here's an example:

```python
#The code below prints Hello World! to the console
print("Hello World!")
```

In the code above, I have used a comment to explain what the code does. When the code is being executed, the interpreter will ignore the comment and run the `print()` function.

We can also comment out actual code. That is:

```python
# print("Hello World!")
print("Happy coding!")

```

When we run the code, only the second line will be interpreted.

You don't always have to place comments above the line of code they're referencing. You can also put them on the same line. That is: 

```python
print("Hello world") # Prints Hello World
```

## How to Write Multi-Line Comments in Python

In this section, we'll see how to write comments that span across multiple lines.

Unlike most other programming languages, Python has no built-in syntax for creating multi-line comments.

Fortunately, there are two ways we can work around that. Here's the first:

```python
# When this code runs,
# you will see Hello World! 
# in the console. 
print("Hello world")
```

Above, we placed the `#` symbol on each line to continue writing our comment.

In this next example, we are going to use multi-line strings (starts and ends with three quotation marks) to nest our comment. 

When you use multi-line strings in Python without assigning the string to a variable, that part of the code will be ignored. 

Here's an example:

```python
"""
When this code runs,
you will see Hello World! 
in the console.
"""
print("Hello World!")
```

## Conclusion

In this article, we learned why it is important to comment our code and how to use comments. We also saw how to create multi-line comments.

Happy coding!

