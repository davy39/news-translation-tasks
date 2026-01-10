---
title: How to Read a File Line by Line in Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-12-14T17:58:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-mateusz-dach-450035.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When coding in Python, there may be times when you need to open and read\
  \ the contents of a text file.\nLuckily enough, there are several ways to do this\
  \ in Python. \nThe language has many built-in functions, methods, and keywords that\
  \ you can use to cr..."
---

When coding in Python, there may be times when you need to open and read the contents of a text file.

Luckily enough, there are several ways to do this in Python. 

The language has many built-in functions, methods, and keywords that you can use to create, write, read and delete text files.

In this article, you'll learn the most common ways of reading a file. With the help of coding examples, you will know how to read a text file line by line.

Here is what we will cover:

1. [How to open a text file using the `open()` function](#open-function)
2. [How to read a text file using the `read()` method](#read-method)
3. [How to read a text file using the `readline()` method](#readline-method)
4. [How to Read a text file using the `readlines()` method](#readlines-method)
5. [How to read a text file using a `for` loop](#for-loop)

Let's dive in!

## How to Open a Text File Using the `open()` Function in Python <a name="open-function"></a>

Before you start reading a text file in Python, you first need to open it.

To open a text file, use the built-in `open()` function.

The general syntax for the `open()` function looks like this:

```python
open("filename", "mode")
```

The `open()` function accepts multiple arguments, but in this example, I'm focusing only on two: `filename` and `mode`.

Let's break down the syntax.

The first required argument that the `open()` function accepts is `filename`, which represents the full path of the file name you want to open.

When specifying the path of the file you want to open, you need to be aware of where that file is located in your folder structure.

For example, if the text file you want to open and your current file with Python code are in the same folder, you only need to reference its name and extension.

Say you have a folder with the name `projects`. 

Inside it, you have two files, `main.py`, which is the file where you write your Python code, and `example.txt`, which is the file you would like to open. That file contains the following contents:

```
I absolutely love coding!
I am learning to code for free with freeCodeCamp!
```

Both files are on the same level in the folder, so here is how you would reference `example.txt` when using the `open()` function:

```python
open("example.txt")
```

The second optional argument that the `open()` function accepts is `mode`. It specifies whether you want to read (`"r"`), write (`"w"`), or append (`"a"`) to `filename`.

The default mode is the read (`"r"`) mode.

So, to open and read `example.txt`, you could optionally use `"r"` to represent the mode you want to use:

```python
open("example.txt", mode="r")
```

With that said, you don't need to write the keyword `mode`.

Instead, you can omit it and only use the letter `"r"` - it would still have the same result:

```python
open("example.txt","r")
```

Lastly, you can omit the letter `"r"` altogether as it is the default mode:

```python
open("example.txt")
```

When you run the code from the example above, it doesn't do anything. 

You completed the first step, which is opening the text file, but you haven't read it and seen its contents.

## How to Read a Text File Using the `read()` Method in Python <a name="read-method"></a>

To read the contents of `example.txt`, let's first store the code we wrote in the previous section in a variable named `file`:

```python
file = open("example.txt")
```

Then, let's call the `read()` method on `file` and print the result to the console:

```python
file = open("example.txt")

print(file.read())

# output

# I absolutely love coding!
# I am learning to code for free with freeCodeCamp!
```

Now, you can read the contents of `example.txt`!

The `read()` method reads all the contents as a single string, which is useful when working with smaller files that don't have a lot of content in the text file.

With that said, the code above is missing something.

Once you have finished reading the text file, you need to close it. To do that, use the `close()` method. Make sure not to skip this step because forgetting to close the file may introduce bugs in your code!

```python
file = open("example.txt")

print(file.read())

# close file
file.close()
```

Now, closing the text file is a good practice, but it is something that you can easily forget to do - you may not always remember to call the `close()` method on the file.

There is an alternative available.

The `with` keyword ensures that the file is automatically closed upon code execution.

The general syntax for the `with` keyword when used with the `open()` function is the following:

```python
with open("filename") as variable:
    # do something with variable
```

So, here is how you would rewrite the code from the previous example using the `with` keyword instead of the `close()` method:

```python
with open("example.txt") as file:
  print(file.read())
  
# output

# I absolutely love coding!
# I am learning to code for free with freeCodeCamp!
```

## How to Read a Text File Using the `readline()` Method in Python <a name="readline-method"></a>

If you want to read only one single individual line from a text file, use the `readline()` method:

```python
with open("example.txt") as file:
  print(file.readline())
  
# output

# I absolutely love coding!
```

The text file `example.txt` has two lines inside it, but the `readline()` method only reads one line from the file and returns it.

The `readline()` method also adds a trailing newline character at the end of the string. 

You can optionally pass a `size` argument to the `readline()` method, which specifies the length of the returned line and the maximum number of bytes it will read.

```python
with open("example.txt") as file:
  print(file.readline(10))

# output

# I absolute
```

## How to Read a Text File Using the `readlines()` Method in Python <a name="readlines-method"></a>

The `readlines()` method reads all the lines from a file, going through the file line by line.

It then returns a list of strings:

```python
with open("example.txt") as file:
  print(file.readlines())
  
# output

# ['I absolutely love coding!\n', 'I am learning to code for free with freeCodeCamp!']
```

The `readlines()` method read all the lines in one go and stored each line from the text file as a single list item inside a list. The `readlines()` method also added a newline character `\n` at the end of each line.

## How to Read a Text File Using a `for` Loop in Python <a name="for-loop"></a>

An alternative way of reading a file line by line in Python is using a `for` loop, which is the most Pythonic approach to reading a file:

```python
with open("example.txt") as file:
  for item in file:
    print(item)
    
# output

# I absolutely love coding!

# I am learning to code for free with freeCodeCamp!
```

The `open()` function returns an iterable object.

The `for` loop gets paired with the `in` keyword - they iterate over the returned iterable file object and read each line inside it.

## Conclusion

Hopefully, this article helped you understand how to read a file line by line in Python using the `read()`, `readline()`, and `readlines()` methods and a `for` loop.

Thank you for reading, and happy coding!


