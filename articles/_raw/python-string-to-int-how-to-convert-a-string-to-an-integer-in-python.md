---
title: 'Python String to Int: How to Convert a String to an Integer in Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T21:06:00.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-int-how-to-convert-a-string-to-an-integer-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e2a740569d1a4ca3bb5.jpg
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Chris Tse

  Unlike many other programming languages out there, Python does not implicitly typecast
  integers (or floats) to strings when you concatenate them to strings.

  Fortunately, Python has a handy built-in function str() which will convert the a...'
---

By Chris Tse

Unlike many other programming languages out there, Python does not implicitly typecast integers (or floats) to strings when you concatenate them to strings.

Fortunately, Python has a handy built-in function `str()` which will convert the argument passed in to a string format.

## The Wrong Way to Convert a String to an Integer in Python

Programmers coming from other programming languages may attempt to do the following string concatenation, which will produce an error:

```py
age = 18

string = "Hello, I am " + age + " years old"
```

[You can run this code on repl.it](https://repl.it/@christopher_tse/int-to-string-error).

The error that shows up is:

```text
Traceback (most recent call last):
  File "python", line 3, in <module>
TypeError: must be str, not int
```

Here, `TypeError: must be str, not int` indicates that the integer must first be converted to a string before it can be concatenated.

## The Correct Way to Convert a String to an Integer in Python 

Here's a simple concatenation example:

```py
age = 18

print("Hello, I am " + str(age) + " years old")

# Output
# Hello, I am 18 years old
```

[You can run this code on repl.it](https://repl.it/@christopher_tse/int-to-string-no-error).

Here's how to print `1 2 3 4 5 6 7 8 9 10` using a single string:

```py
result = ""

for i in range(1, 11):
    result += str(i) + " "

print(result)

# Output
# 1 2 3 4 5 6 7 8 9 10
```

[You can run the code on repl.it](https://repl.it/@christopher_tse/int-to-string-loop).

### Here's a line-by-Line explanation of how the above code works:

1. First of all a variable ‘result’ is assigned to an empty string.
2. The for loop is being used to iterate over a list of numbers.
3. This list of numbers is generated using the range function.
4. so range(1,11) is going to generate a list of numbers from 1 to 10.
5. On each for loop iteration this ‘i’ variable is going to take up values from 1 to 10.
6. On first iteration when the variable i=1,then the variable [result=result+str(i)+“(space character)”],str(i) converts the ‘i’ which is an integer value to a string value.
7. Since i=1, on the first iteration finally result=1.
8. And the same process goes on until i=10 and finally after the last iteration result=1 2 3 4 5 6 7 8 9 10.
9. Therefore when we finally print the result after the for loop the output on the console is ‘1 2 3 4 5 6 7 8 9 10’.

I hope you've found this helpful. Happy coding.

