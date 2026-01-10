---
title: Python New Line and How to Python Print Without a Newline
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-06-20T23:20:47.000Z'
originalURL: https://freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/New-Line.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'Welcome! The new line character in Python is used to mark the end of a
  line and the beginning of a new line. Knowing how to use it is essential if you
  want to print output to the console and work with files.

  In this article, you will learn:


  How to i...'
---

**Welcome!** The new line character in Python is used to mark the end of a line and the beginning of a new line. Knowing how to use it is essential if you want to print output to the console and work with files.

**In this article, you will learn:**

* How to identify the new line character in Python.
* How the new line character can be used in strings and print statements.
* How you can write print statements that don't add a new line character to the end of the string.

**Let's begin! ✨**

## 🔹 The New Line Character 

The new line character in Python is:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-142.png)

**It is made of two characters:**

* A backslash. 
* The letter `n`.

If you see this character in a string, that means that the current line ends at that point and a new line starts right after it:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-224.png)

You can also use this character in **f-strings**:

```python
>>> print(f"Hello\nWorld!")
```

## 🔸 The New Line Character in Print Statements

By default, print statements add a new line character "behind the scenes" at the end of the string. 

Like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-145.png)

This occurs because, according to the [Python Documentation](https://docs.python.org/3/library/functions.html#print):

The default value of the `end` parameter of the built-in `print` function is `\n`, so a new line character is appended to the string.

**💡 Tip:** Append means "add to the end".

This is the function definition:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-146.png)

Notice that the value of `end` is `\n`, so this will be added to the end of the string.

If you only use one print statement, you won't notice this because only one line will be printed:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-147.png)

But if you use several print statements one after the other in a Python script:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-214.png)

The output will be printed in separate lines because `\n` has been added "behind the scenes" to the end of each line:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-218.png)

## 🔹 How to Print Without a New Line

We can change this default behavior by customizing the value of the `end` parameter of the `print` function.

If we use the default value in this example:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-219.png)

We see the output printed in two lines:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-221.png)

But if we customize the value of `end` and set it to `" "`

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-222.png)

A space will be added to the end of the string instead of the new line character `\n`, so the output of the two print statements will be displayed in the same line:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-223.png)

You can use this to print a sequence of values in one line, like in this example:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-210.png)

The output is:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-211.png)

**💡 Tip:** We add a conditional statement to make sure that the comma will not be added to the last number of the sequence. 

Similarly, we can use this to print the values of an iterable in the same line:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-225.png)

The output is:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-213.png)

## 🔸 The New Line Character in Files

The new line character `\n` is also found in files, but it is "hidden". When you see a new line in a text file, a new line character `\n` has been inserted.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-150.png)

You can check this by reading the file with `<file>.readlines()`, like this:

```python
with open("names.txt", "r") as f:
    print(f.readlines())
```

The output is:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-207.png)

As you can see, the first three lines of the text file end with a new line `\n` character that works "behind the scenes."

**💡 Tip:** Notice that only the last line of the file doesn't end with a new line character.

## 🔹 In Summary

* The new line character in Python is `\n`. It is used to indicate the end of a line of text.
* You can print strings without adding a new line with `end = <character>`, which `<character>` is the character that will be used to separate the lines.

**I really hope that you liked my article and found it helpful.** Now you can work with the new line character in Python. 

[Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

