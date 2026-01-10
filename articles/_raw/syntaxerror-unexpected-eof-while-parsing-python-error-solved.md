---
title: SyntaxError Unexpected EOF While Parsing Python Error [Solved]
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-21T13:47:24.000Z'
originalURL: https://freecodecamp.org/news/syntaxerror-unexpected-eof-while-parsing-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/solve.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: null
seo_desc: "Error messages help us solve/fix problems in our code. But some error messages,\
  \ when you first see them, may confuse you because they seem unclear. \nOne of these\
  \ errors is the \"SyntaxError: unexpected EOF while parsing\" error you might get\
  \ in Python...."
---

Error messages help us solve/fix problems in our code. But some error messages, when you first see them, may confuse you because they seem unclear. 

One of these errors is the "SyntaxError: unexpected EOF while parsing" error you might get in Python.

In this article, we'll see why this error occurs and how to fix it with some examples. 

## How to Fix the “SyntaxError: Unexpected EOF While Parsing” Error

Before we look at some examples, we should first understand why we might encounter this error.

The first thing to understand is what the error message means. EOF stands for **End of File** in Python. Unexpected EOF implies that the interpreter has reached the end of our program before executing all the code.

This error is likely to occur when:

* we fail to declare a statement for loop (`while`/`for`)
* we omit the closing parenthesis or curly bracket in a block of code. 

Have a look at this example:

```python
student = {
  "name": "John",
  "level": "400",
  "faculty": "Engineering and Technology"

```

In the code above, we created a dictionary but forgot to add **`}`** (the closing bracket) – so this is certainly going to throw the "SyntaxError: unexpected EOF while parsing" error our way. 

After adding the closing curly bracket, the code should look like this:

```python
student = {
  "name": "John",
  "level": "400",
  "faculty": "Engineering and Technology"
}
```

This should get rid of the error.

Let's look at another example.

```python
i = 1
while i < 11:
```

In the `while` loop above, we have declared our variable and a condition but omitted the statement that should run until the condition is met. This will cause an error.

Here is the fix:

```python
i = 1
while i < 11:
  print(i)
  i += 1
  

```

Now our code will run as expected and print the values of `i` from 1 to the last value of `i` that is less than 11. 

This is basically all it takes to fix this error. Not so tough, right? 

To be on the safe side, always enclose every parenthesis and braces the moment they are created before writing the logic nested in them (most code editors/IDEs will automatically enclose them for us).

Likewise, always declare statements for your loops before running the code.

## Conclusion

In this article, we got to understand why the "SyntaxError: unexpected EOF while parsing" occurs when we run our code. We also saw some examples that showed how to fix this error.

Happy Coding!

