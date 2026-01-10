---
title: Print Newline in Python – Printing a New Line
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-22T19:17:24.000Z'
originalURL: https://freecodecamp.org/news/print-newline-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Print-Newline-in-Python---Printing-a-New-Line-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  Working with strings or text data in programming frequently involves printing a
  newline. The end of a line is indicated by a newline character, which also advances
  the cursor to the start of the following line. Using the escape char...'
---

By Shittu Olumide

Working with strings or text data in programming frequently involves printing a newline. The end of a line is indicated by a newline character, which also advances the cursor to the start of the following line. Using the escape character `\n`, we can print a newline in Python.

Other programming languages may have different rules for printing newline characters. While some languages may have a built-in function or method to print a newline, others might use a different escape sequence.

In this article, we will explore the different ways to print a newline in Python. We will also discuss some interesting research findings about the usage of newline characters in code and its impact on readability and maintainability.

By the end of this article, you will have a better understanding of how to print a newline character in Python and how to write code that is easy to read and maintain.

## How to Print a Newline Using the `\n` Escape Sequence

The simplest and most common way to print a newline character in Python is by using the `\n` escape sequence. For example, the following code will print two lines of text, with a newline character between them:

```py
print("Hello\nWorld")

```

Output:

```bash
Hello
World

```

While using the `\n` escape sequence is straightforward and widely understood, it may not always be the best choice for improving code readability and maintainability. In particular, using multiple `\n` characters can make code harder to read and maintain, especially when dealing with long blocks of text.

## How to Print a Newline Using the `print()` Function with the End Parameter 

Another way to print a newline character in Python is by using the `print()` function with the end parameter. 

By default, the `print()` function adds a newline character at the end of the output. But we can change this behavior by specifying a different string to be used as the end parameter. 

For example, the following code will print two lines of text with a newline character between them, using the `print()` function:

```py
print("Hello", end='\n')
print("World")

```

Output:

```bash
Hello
World

```

Code readability can be enhanced by using the `print()` function with the end parameter, which makes it clearer where the newline character is being added. 

On the other hand, it might also make the code verbose and more challenging to read, particularly when working with lengthy blocks of text.

## How to Print a Newline Using the `join()` Method with the `split()` Method 

A more advanced way to print a newline character in Python is by using the `join()` method with the `split()` method. 

The `split()` method is used to split a string into a list of substrings, based on a specified separator. The `join()` method is used to join the elements of a list into a single string, using a specified separator.

By splitting a string on the newline character and then joining it back together with a newline character separator, we can print multiple lines of text. 

For example, the following code will print two lines of text with a newline character between them, using the `join()` method with the `split()` method:

```py
text = "Hello\nWorld"
lines = text.split('\n')

print('\n'.join(lines))

```

Output:

```bash
Hello
World

```

By making the code clearer and more concise by combining the `join()` and `split()` methods, this improves code readability. But when printing multiple lines of text, especially when dealing with lengthy blocks of text, this may not always be the most effective or performant method.

## How Does Using Newline Characters Affect Code?

Several studies have investigated the impact of newline characters on code readability and maintainability. 

One study found that code with consistent and predictable newline characters was easier to read and understand, especially for novice programmers. Another study found that excessive use of newline characters, or inconsistent use of indentation and whitespace, could make code harder to read and understand. 

It is important to use newline characters in a consistent and predictable way, based on the conventions and guidelines of the programming language.

## Conclusion 

In this article, we checked out three different ways we can print newline in Python, and also mentioned the importance of having well-formatted code using the newline character. 

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

