---
title: With Open in Python – With Statement Syntax Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-12T17:20:54.000Z'
originalURL: https://freecodecamp.org/news/with-open-in-python-with-statement-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/withOpen.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'The Python programming language has various functions and statements for
  working with a file. The with statement and open() function are two of those statements
  and functions.

  In this article, you will learn how to use both the with statement and ope...'
---

The Python programming language has various functions and statements for working with a file. The `with` statement and `open()` function are two of those statements and functions.

In this article, you will learn how to use both the `with` statement and `open()` function to work with files in Python.


## What Does `Open()` Do in Python?

To work with files in Python, you have to open the file first. So, the `open()` function does what the name implies – it opens a file for you so you can work with the file.

To use the open function, you declare a variable for it first. The `open()` function takes up to 3 parameters – the filename, the mode, and the encoding. You can then specify what you want to do with the file in a print function.

```py
my_file = open("hello.txt", "r")
print(my_file.read())

# Output : 
# Hello world
# I hope you're doing well today
# This is a text file
```

That’s not all. The `open()` function does not close the file, so you also have to close the file with the `close()` method.

So, a proper way to use the open function looks like this:

```py
my_file = open("hello.txt", "r")
print(my_file.read())
my_file.close()

# Output : 
# Hello world
# I hope you're doing well today
# This is a text file

```

The read mode is the default file mode in Python, so if you don’t specify the mode, the code above still works fine:

```py
my_file = open("hello.txt")
print(my_file.read())
my_file.close()

# Output : 
# Hello world
# I hope you're doing well today
# This is a text file
```


## How Does the `With` Statement Work in Python?

The `with` statement works with the `open()` function to open a file.

So, you can re-write the code we used in the `open()` function example like this:

```py
with open("hello.txt") as my_file:
    print(my_file.read())

# Output : 
# Hello world
# I hope you're doing well today
# This is a text file
```

Unlike `open()` where you have to close the file with the `close()` method, the `with` statement closes the file for you without you telling it to. 

This is because the `with` statement calls 2 built-in methods behind the scene – `__enter()__` and `__exit()__`.

The `__exit()__` method closes the file when the operation you specify is done.

With the `write()` method, you also write to the file as I did below:

```py
with open("hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("I hope you're doing well today \n")
    my_file.write("This is a text file \n")
    my_file.write("Have a nice time \n")

with open("hello.txt") as my_file:
    print(my_file.read())

# Output: 
# Hello world 
# I hope you're doing well today
# This is a text file
# Have a nice time
```

**You can also loop through the file and print the text line by line:
**
```py
with open("hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("I hope you're doing well today \n")
    my_file.write("This is a text file \n")
    my_file.write("Have a nice time \n")

with open("hello.txt") as my_file:
    for line in my_file:
        print(line)

# Output:
# Hello world 

# I hope you're doing well today 

# This is a text file

# Have a nice time 
```


## Conclusion

You might be wondering which way you should use to work with files between the combo of `with` and `open()` and just the `open()` function. 

I would advise you to use the combination of `with` and `open()` because the `with` statement closes the file for you and you get to write less code.

Keep coding :)


