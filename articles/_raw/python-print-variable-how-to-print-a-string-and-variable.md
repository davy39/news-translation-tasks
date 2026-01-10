---
title: Python Print Variable – How to Print a String and Variable
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-12-07T17:26:18.000Z'
originalURL: https://freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/denise-jans-_dXkaD3l574-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python is a versatile and flexible language – there is often more than
  one way to achieve something.

  In this tutorial, you''ll see some of the ways you can print a string and a variable
  together.

  Let''s get started!

  How to use the print() function in P...'
---

Python is a versatile and flexible language – there is often more than one way to achieve something.

In this tutorial, you'll see some of the ways you can print a string and a variable together.

Let's get started!

## How to use the `print()` function in Python

To print anything in Python, you use the `print()` function – that is the `print` keyword followed by a set of opening and closing parentheses,`()`.

```python
#how to print a string
print("Hello world")

#how to print an integer
print(7)

#how to print a variable 
#to just print the variable on its own include only the name of it

fave_language = "Python"
print(fave_language)

#output

#Hello world
#7
#Python
```

If you omit the parentheses, you'll get an error:

```python
print "hello world"

#output after running the code:
#File "/Users/dionysialemonaki/python_articles/demo.py", line 1
#    print "hello world"
#    ^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

If you write your Python code in Visual Studio Code, with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), you'll also get an underline and a hint which all indicate that something is not quite right:

![Screenshot-2021-12-07-at-3.08.14-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-07-at-3.08.14-PM.png)

As mentioned above, the print statement is used to output all kinds of information. This includes textual and numerical data,variables, and other data types.

You can also print text (or strings) combined with variables, all in one statement.

You'll see some of the different ways to do this in the sections that follow.

## How to print a variable and a string in Python using concatenation

To concatenate, according to the dictionary, means to link (things) together in a chain or series.

You do this by adding various things (in this case programming – you add data) together with one another, using the Python addition operator, `+`.

Keep in mind that concatenation is only used for strings, so if the variable you want to concatenate with the rest of the strings is of an integer data type, you'll have to convert it to a string with the `str()` function.

In the following example, I want to print the value of a variable along with some other text.

I add the strings in double quotes and the variable name without any surrounding it, using the addition operator to chain them all together:

```python
fave_language = "Python"

print("I like coding in " + fave_language + " the most")

#output
#I like coding in Python the most
```

With string concatenation, you have to add spaces by yourself, so if in the previous example I hadn't included any spaces within the quotation marks the output would look like this:

```python
fave_language = "Python"

print("I like coding in" + fave_language + "the most")

#output
#I like coding inPythonthe most
```

You can even add the spaces separately:

```python
fave_language = "Python"

print("I like coding in" + " " + fave_language + " "  + "the most")

#output
#I like coding in Python the most
```

This is not the most preferred way of printing strings and variables, as it can be error prone and time-consuming.

## How to print a variable and a string in Python by separating each with a comma

You can print text alongside a variable, separated by commas, in one print statement.

```python
first_name = "John"

print("Hello",first_name)

#output
#Hello John
```

In the example above, I first included some text I wanted to print in double quotation marks – in this case, the text was the string `Hello`. 

After the closing quotation mark, I added a comma which separates that piece of text from the value held in the variable name (`first_name` in this case) that I then included.

I could have added more text following the variable, like so:

```python
first_name = "John"

print("Hello",first_name,"good to see you")

#output
#Hello John good to see you
```

This method also works with more than one variable:

```python
first_name = "John"
last_name = "Doe"

print("Hello",first_name,last_name,"good to see you")

#output
Hello John Doe good to see you
```

Make sure to separate everything with a comma.

So, you separate text from variables with a comma, but also variables from other variables, like shown above.

If the comma hadn't been added between `first_name` and `last_name`, the code would've thrown an error:

```python
first_name = "John"
last_name = "Doe"

print("Hello",first_name last_name,"good to see you")

#output
#File "/Users/dionysialemonaki/python_articles/demo.py", line 4
#    print("Hello",first_name last_name,"good to see you")
#                 ^^^^^^^^^^^^^^^^^^^^
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

As you see, Python error messages are extremely helpful and make the debugging process a bit easier :)

## How to print a variable and a string in Python using string formatting

You use string formatting by including a set of opening and closing curly braces, `{}`, in the place where you want to add the value of a variable.

```python
first_name = "John"

print("Hello {}, hope you're well!")
```

In this example there is one variable, `first_name`.

Inside the print statement there is a set of opening and closing double quotation marks with the text that needs to be printed.

Inside that, I've added a set of curly braces in the place where I want to add the value of the variable `first_name`.

If I try and run this code, it will have the following output:

```python
#output
#Hello {}, hope you're well!
```

It doesn't actually print the value of `first_name`!

To print it, I need to add the `.format()` string method at the end of the string – that is immediately after the closing quotation mark:

```python
first_name = "John"

print("Hello {}, hope you're well!".format(first_name))

#output
#Hello John, hope you're well!
```

When there is more than one variable, you use as many curly braces as the number of variables you want to print:

```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!")
```

In this example, I've created two variables and I want to print both, one after the other, so I added two sets of curly braces in the place where I want the variables to be substituted.

Now, when it comes to the `.format()` method, the order in which you place the variable names inside matters.

So, the value of the variable name that will be added first in the method will be in the place of the first curly brace, the value of the variable name that will be added second will be in the place of the second curly brace, and so on.

Make sure to separate the variable names by commas inside the method:

```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!".format(first_name,last_name))

#output
#Hello John Doe, hope you're well!
```

If I'd reversed the order of the names inside the method, the output would look different:

```python
first_name = "John"
last_name = "Doe"

print("Hello {} {}, hope you're well!".format(last_name,first_name))

#output
#Hello Doe John, hope you're well!
```

## How to print a variable and a string in Python using `f-strings`

`f-strings` are a better and more readable and concise way of achieving string formatting compared to the method we saw in the previous section.

The syntax is easier and requires less manual work.

The general syntax for creating an `f-string` looks like this:

```python
print(f"I want this text printed to the console!")

#output
#I want this text printed to the console!
```

You first include the character `f` before the opening and closing quotation marks, inside the `print()` function.

To print a variable with a string in one line, you again include the character `f` in the same place – right before the quotation marks.

Then you add the text you want inside the quotation marks, and in the place where you want to add the value of a variable, you add a set of curly braces with the variable name inside them:

```python
first_name = "John"

print(f"Hello, {first_name}!")

#output
#Hello, John!
```

To print more than variable, you add another set of curly braces with the second variable name:

```python
first_name = "John"
last_name = "Doe"

print(f"Hello, {first_name} {last_name}!")

#output
#Hello, John Doe!
```

The order you place the variable names does matter, so make sure you add them according to the output you want.

If I had reversed the order of the names, I'd get the following output:

```python
first_name = "John"
last_name = "Doe"

print(f"Hello, {last_name} {first_name}!")

#output
#Hello, Doe John!
```

## Conclusion

Thanks for reading and making it to the end! You now know a few different ways of printing strings and variables together in one line in Python.

If you want to learn more about Python, check out freeCodeCamp's [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

It's suitable for beginners as it starts from the fundamentals and gradually builds to more advanced concepts. You'll also get to build five projects and  put to practice all the new knowledge you acquire.

Happy coding!



