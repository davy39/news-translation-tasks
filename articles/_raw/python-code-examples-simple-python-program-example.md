---
title: The Python Code Example Handbook – Simple Python Program Examples for Beginners
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-05-04T17:20:38.000Z'
originalURL: https://freecodecamp.org/news/python-code-examples-simple-python-program-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Python-Code-Examples-Handbook-Mockup.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: handbook
  slug: handbook
- name: Python
  slug: python
seo_title: null
seo_desc: 'Python is a high-level, general purpose, interpreted programming language.
  It''s well-known for being very easy to learn yet powerful, and it has many uses
  in many different fields.

  If you''re someone trying to get started with Python, it''s easy to get...'
---

Python is a high-level, general purpose, interpreted programming language. It's well-known for being very easy to learn yet powerful, and it has many uses in many different fields.

If you're someone trying to get started with Python, it's easy to get lost among all the excellent learning resources on the internet. 

Now this article isn't trying to be another head in that crowd. Rather, here I'll introduce you to Python basics and I'll point you in the right direction.

In this article, I'll introduce to the fundamentals of the Python programming language with the help of a ton of code examples. I'll explain them in great detail and include links for further study. 

Once I've introduced you to the language at a basic level, I'll suggest you some excellent learning resources and explain how to make the best of them.

While I'll explain the code examples thoroughly, I'm assuming that you're familiar with common programming concepts such as expressions, statements, variables, functions, and so on. So I'll not spend time explaining these programming concepts in detail – rather I'll focus on Python's way of implementing/using them.

Without any further ado, let's jump in!

## Table of Contents

* [High Level Overview of Python](#heading-high-level-overview-of-python)
* [How to Write Hello, World! in Python](#heading-how-to-write-hello-world-in-python)
* [Variables in Python](#heading-variables-in-python)
* [Data Types in Python](#heading-data-types-in-python)
* [How to Write Comments in Python](#how-to-write-comments-in-python)
* [Strings in Python](#heading-strings-in-python)
* [Numbers in Python](#heading-numbers-in-python)
* [How to Handle User Input in Python](#heading-how-to-handle-user-input-in-python)
* [if-else-elif in Python](#if-else-elif-in-python)
* [match-case in Python](#heading-match-case-in-python)
* [Lists and Tuples in Python](#heading-lists-and-tuples-in-python)
* [Loops in Python](#heading-loops-in-python)
* [Dictionaries in Python](#heading-dictionaries-in-python)
* [Functions in Python](#heading-functions-in-python)
* [Additional Python Learning Resources](#heading-additional-python-learning-resources)
* [Conclusion](#heading-conclusion)

## High Level Overview of Python

Before I jump into coding, you'll need to have Python installed and ready to go on your system. Depending on the system you're running – Windows, macOS or Linux – the installation process will differ.

If you're on Windows, my fellow freeCodeCamp author [Md. Fahim Bin Amin](https://www.freecodecamp.org/news/author/fahimbinamin/) has written an excellent guide on [How to Install Python on Windows](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/). Another author [Dillion Megida](https://www.freecodecamp.org/news/author/dillionmegida/) has written another excellent article on [How to Install Python 3 on Mac](https://www.freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide/).

Some platforms, such as some of the modern Linux distributions, come with a fairly up-to-date version of Python pre-installed. So if you're on Linux, execute the following command to check your version of Python:

```shell
python3 --version
```

Having any version of Python 3 installed on your system will suffice. Apart from Python, you'll also need a code editor or IDE well suited for writing Python code.

In my [Python IDE – Best IDEs and Editors for Python](https://www.freecodecamp.org/news/python-ide-best-ides-and-editors-for-python/) article I've listed three of the best code editors and IDEs that you may use for writing Python code.

So if you have Python and a code editor or IDE ready to go, let's move on to writing your first piece of Python code.

### How to Write Hello, World! in Python

Somewhere in your computer, create a new file named `program.py` and put the following code in it:

```python
print('Hello, World!')
```

To run this code, open your terminal inside the directory where you've put the `program.py` file and execute the following command:

```shell
# on Windows and macOS
python program.py

# on Linux
python3 program.py
```

The output of the code will be whatever you've passed as the parameter of the `print()` function, which in the case of this code snippet is:

```shell
Hello, World!
```

As you may have already guessed, `print()` is a built-in Python function that prints whatever you give it on the console. The function can print strings, numbers, expressions – more or less anything that you can throw at it.

```python
print('Hello, World!')
print(100)
print(5 + 5)
```

The first statement prints out the string `Hello, World!` just like before. The second one prints out a number and the third one prints out the result of the `5 + 5` expression:

```shell
Hello, World!
100
10
```

One thing that you may or may not have noticed is that the three print statements have been outputted in three separate lines. Whereas in other languages such as C/C++/C#/Java you have to append a newline character explicitly.

As it turns out, `print()` functions as newline character by default and you can override this default behavior as follows:

```python
print('Hello, World!', end=' | ')
print(100, end=' | ')
print(5 + 5)
```

Now the output of the program will be:

```shell
Hello, World! | 100 | 10
```

Which means any string you pass as the value of the `end` parameter will be used as the terminating character of the printed line. 

Here, I've used `|` as the terminating character of the first two statements. However, I've used the default newline character as the terminating character of the last statement.

You can learn more about the `print()` function by playing around with it or by reading the [official docs](https://docs.python.org/3/library/functions.html#print) on the function.

### Variables in Python

To declare a variable in Python, you start by writing out the name of the variable, then an equals sign, followed by the value of the variable:

```python
name = 'Farhan'

print('My name is ' + name)
```

Output of this code will be:

```shell
My name is Farhan
```

As you can see, there is no special keyword for declaring a variable. Python is smart enough to get the type of the variable from the value you're assigning. 

In the example above, the `name` variable contains the `Farhan` string. Since the word `Farhan` is within quotes, Python will treat this variable as a string.

In Python, you can concatenate two strings using the plus sign. That's what we've done in the `print()` statement above. But if you change the code as follows:

```python
name = 'Farhan'
age = 27

print('My name is ' + name)
print('I am ' + age + 'years old')
```

And try to run this program, you'll face the following problem:

```shell
My name is Farhan
Traceback (most recent call last):
  File "C:\Users\shovi\repos\python-playground\hello-world.py", line 5, in <module>
    print('I am ' + age + 'years old')
TypeError: can only concatenate str (not "int") to str
```

As you can see, strings can be concatenated with strings only, and the `age` variable is an integer. There is a better way of embedding variables within string statements.

```python
name = 'Farhan'
age = 27

print(f'My name is {name}')
print(f'I am {age} years old')
```

I hope you've noticed the `f` in the beginning of the strings inside the `print()` statements. This `f` turns the strings into f-strings. These strings are evaluated at runtime, so inside a f-string, you can put any valid Python statement within curly braces. This makes embedding variables or even simple logic within strings very easy.

You can re-declare your variables anywhere within the program. You can even change their types if you wish to.

```python
a = 'this is a string'

a = 10

print(a)
```

This is a completely valid program and the value of `a` will be printed as `10` since you've overridden the initial value on the second line.

### Data Types in Python

In Python, there four main literal types that you need to be aware of:

| Type           | Example        |
| -------------- | -------------- |
| Integer        | 1              |
| Floating Point | 2.0            |
| Boolean        | True           |
| String         | 'freeCodeCamp' |

Integers and floating points are self-explanatory. A boolean can be either `true` or `false`, and strings in Python can be enclosed within either single quotes or double quotes. I prefer using single quotes. You may use the one you like but try not to mix both types of quotes together.

### Comments in Python

Comments in Python start with a hash symbol:

```python
# this is a comment
```

Comments written using a hash can only be single line. If you want to write multi-line comment in Python, you'll have to use quotes as follows:

```python
'''this is a comment
 that goes on
 and on
 and on...'''
```

Commenting your code as needed is a good way of documenting it. But make sure you're not adding comments where the code can be easily understood by just looking at it.

### Strings in Python

Strings in Python are ordered collections of Unicode characters. Strings can not be modified at runtime. You've already seen how to declare a string. In this section you'll learn about common string operations.

In a string, each character will have an index. And like arrays, string indexes are zero-based.

```python
name = 'Farhan'

# F -> 0
# a -> 1
# r -> 2
# h -> 3
# a -> 4
# n -> 5
```

These characters can be accessed using these indexes as follows:

```python
name = 'Farhan'

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
```

The output of this program will be as follows:

```shell
F
a
r
h
a
n
```

Another fun thing that you can do using these indexes is slicing. Assume that you want to take out a part from a string.

```python
name = 'Farhan'

print(name[0:3])
```

The output of this program will be:

```shell
Far
```

In this example, `name[0:3]` means print starting from index `0` to index `3`. Now you may think that `h` is at index `3` and you'll be right about that. But the thing about slicing is, it doesn't include the character at the ending index.

If you'd like to learn more about slicing, there is an article titled [How to Substring a String in Python](https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/) that you may find useful.

You can use the `len()` function to figure out the length of a string as follows:

```python
name = 'Farhan'

print(len(name))
```

Output from this program will be `6` since there are six characters in the string.

Python has a ton of string methods, but demonstrating each of them isn't possible here so I'll demonstrate some of the most common ones.

The first method is `capitalize()`. This method returns a copy of the given string with its first character capitalized and the rest lowercased.

```python
print('python is awesome'.capitalize())
```

Output of this code will be `Python is awesome`. If you want to convert the entire sentence to uppercase, there is the `upper()` method:

```python
print('python is awesome'.upper())
```

Output of this code will be `PYTHON IS AWESOME`. You can do the opposite using the `lower()` method:

```python
print('PYTHON IS AWESOME'.lower())
```

The output of this code will be `python is awesome`. There are the `isupper()` and `islower()` methods to check whether a string is in uppercase or lowercase.

```python
print('PYTHON IS AWESOME'.islower())
print('PYTHON IS AWESOME'.isupper())
```

Output of this code will be as follows:

```shell
False
True
```

If you want to replace all occurrences of a substring within a string, you can do so by using the `replace()` method:

```python
print('python is awesome'.replace('python', 'freeCodeCamp'))
```

This code will replace all occurrences of `python` with `freeCodeCamp`  in the given string.

Finally, there are the `split()` and `join()` methods. The first one splits a string into a list:

```python
print('python is awesome'.split(' '))
```

The method takes a delimiter to split the string on. Here, I've used space as the delimiter. Output of this code will be `['python', 'is', 'awesome']`. This is a list. We haven't covered lists yet but we will soon. For now, understand that they're like arrays.

You can produce a new string using the elements of an iterable, that is a list, using the `join()` method:

```python
print(' '.join(['python', 'is', 'awesome']))
```

I've called the `join()` method on a space so the result of this code will be a string joined using spaces in between as follows:

```python
python is awesome
```

If you want to learn more about all the string methods in Python, feel free to consult the [official documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

### Numbers in Python

Numbers in Python can be of integer, floating point, and complex types. In this article, I'll only discuss operations related to the real numbers – that is, integers and floating points.

You can perform addition, subtraction, multiplication, and division operations using integers and floating point numbers like in any other programming language:

```python
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

Output from this snippet of code will be as follows:

```shell
15
5
50
2.0
```

One thing to keep in mind is that even if you perform a division operation between two integers, the result will always be a floating point. If you want the result to be an integer, you can do so as follows:

```python
a = 10
b = 5

print(a//b)
```

This time the result will be an integer. Be careful that if there are any numbers after the decimal point, they'll be chopped off.

If you'd like to learn more about the numeric types in Python, feel free to consult the [official documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

### How to Handle User Input in Python

For taking input from the user, there is the `input()` function.

```python
name = input('What is your name? ')

print(f'Your name is {name}')
```

The output from this program will be as follows:

```shell
What is your name? Farhan
Your name is Farhan
```

The `input()` function saves the user input as a string even if the user inputs a number. So if you're taking a number as input from the user, be sure to convert it to the appropriate data type.

### if-elif-else in Python

Like any other programming language, Python has the usual `if-elif-else` statements.

```python
a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Invalid Operation!')

```

This is a very simple calculator program. Depending on the operation you choose, the calculator will perform one of the mentioned operations. 

In Python, code blocks such as the `if` block or the `elif` block or the `else` block start with the keyword and a colon.

Indentation is crucial in Python and if you indent code within a code block inappropriately, the code will fail to run.

### match-case in Python

In Python, a `match-case` is equivalent to a `switch-case` statement in other programming languages. The aforementioned calculator program can be rewritten using `match-case` as follows:

```python
a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

match op:
    case 'sum':
        print(f'a + b = {a+b}')
    case 'sub':
        print(f'a - b = {a-b}')
    case 'mul':
        print(f'a * b = {a*b}')
    case 'div':
        print(f'a / b = {a/b}')
    case _:
        print('Invalid Operation!')

```

Again, depending on the value of `op`, one of the cases will be performed. If the input from the user doesn't match any of the cases, then the wildcard `_` action will take place.

Keep in mind that `match-case` is available only on Python 3.10 and later versions. So if you're using an older version, you may not have this statement.

### Lists and Tuples in Python

Lists in Python are a sequence of values. You can modify lists at runtime. You can create a list as follows:

```python
vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels)
```

Output of this program will be `['a', 'e', 'i', 'o', 'u']`. Like strings, each element in a Python list has an index and these indexes start from zero.

```python
vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels[0])
print(vowels[1])
print(vowels[2])
print(vowels[3])
print(vowels[4])
```

Like strings you can perform slicing on lists as well and the syntax for slicing a list is the same as a string.

Lists in Python have a bunch of useful methods. To add new items to a list there are the `append()`, `extend()`, and `insert()` methods.

The `append()` method appends a new item to the list and the `extend()` method adds multiple items:

```python
vowels = ['a', 'e']

vowels.append('i')
vowels.extend(['o', 'u'])

print(vowels)
```

The `insert()` method, on the other hand, inserts an item at a given index in the list:

```python
vowels = ['a', 'i', 'o', 'u']

vowels.insert(1, 'e')

print(vowels)
```

The `pop()` method pops the last element off the list:

```python
vowels = ['a', 'e', 'i', 'o', 'u']

popped_item = vowels.pop()

print(popped_item)
print(vowels)
```

Output from this snippet of code will be:

```shell
u
['a', 'e', 'i', 'o']
```

The `remove()` method can remove a given element from the list:

```python
vowels = ['a', 'e', 'i', 'o', 'u']

vowels.remove('e')

print(vowels)
```

This will delete the `e` from the list of vowels. 

Finally there is the `clear()` method that removes all the elements from the list.

There is also the `sort()` method:

```python
vowels = ['u', 'e', 'a', 'o', 'i']

vowels.sort()

print(vowels)
```

The `sort()` method sorts the list in ascending order. This method sorts the list in place. This means it doesn't return a new list, and instead sorts the original list.

If you want to reverse the list instead, there is the `reverse()` method:

```python
vowels = ['u', 'e', 'a', 'o', 'i']

vowels.reverse()

print(vowels)
```

It's also an in place method like sort. It's just the reverse (no pun intended) of the sort method. You can learn more about lists from the [official documentation](https://docs.python.org/3/tutorial/datastructures.html).

There is also an immutable sequence type called a tuple in Python. Tuples are pretty similar to lists but you can not modify a tuple.

```python
vowels = ('a', 'e', 'i', 'o', 'u')

print(vowels)
```

The output of this code will be `('a', 'e', 'i', 'o', 'u')`. There are not many methods for the tuples. If you want to learn more about tuples, consult the [official documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences).

### Loops in Python

You can use loops in Python to iterate over a sequence type like a list.

```python
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in vowels:
    print(letter.upper())
```

There is also `while` loop but since the `for` loop is what you'll be mostly using, I won't spend time explaining `while` loops.

### Dictionaries in Python

Let's assume I've given you the line "the quick brown fox jumped over the lazy dog" and tell you to count the the number of occurrences for each letter. You can do this easily using a hashmap.

A hashmap is a collection of key-value pairs.

```
{
    key_1: value_1,
    key_2: value_2,
    key_3: value_3,
    key_4: value_4,
    key_5: value_5,
}
```

To do the task I gave you earlier, you can write the following code:

```python
sentence = 'the quick brown fox jumped over the lazy dog'

record = {}

for letter in sentence:
    if letter in record:
        record[letter] += 1
    else:
        record[letter] = 1

print(record)
```

Output for this code will be as follows:

```shell
{'t': 2, 'h': 2, 'e': 4, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 2, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'g': 1}
```

This is a dictionary. Each letter is a key and their occurrence number is the value. On the code snippet, you declare a dictionary in the second line. [Estefania Cassingena Navone](https://www.freecodecamp.org/news/author/estefaniacn/) has written an article called [Python Dictionaries 101: A Detailed Visual Introduction](https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/) which you may consult to learn more about dictionaries.

### Functions in Python

The final concept that I'll discuss is functions. Functions in programming are chunks of code that perform a certain task. 

In Python, you can declare a function using the `def` keyword followed by the function signature:

```python
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {sum(a, b)}')
elif op == 'sub':
    print(f'a - b = {sub(a, b)}')
elif op == 'mul':
    print(f'a * b = {mul(a, b)}')
elif op == 'div':
    print(f'a / b = {div(a, b)}')
else:
    print('Invalid Operation!')

```

This is the same calculator program as before, but now the operations are written within separate functions. 

To learn more about functions, you can read this article: [Functions in Python – Explained with Code Examples](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/) by [Bala Priya C](https://www.freecodecamp.org/news/author/bala-priya/).

There are a lot of other concepts that you need to learn if you want to be a great Python programmer. That's what the next section is about.

## Additional Python Learning Resources

Now that you have a basic understanding of the Python programming language, I'll suggest some high quality learning resources to continue your learning journey.

### Learn Python in 4 Hours

%[https://youtu.be/rfscVS0vtbw]

The first resource on the list is a video on the freeCodeCamp YouTube channel created by Girrafe Academy. 

The instructor has created multiple courses on the channel and is known for making concise videos. 

The video covers most of the important Python concepts within 4 hours. The instructor also makes simple projects along the way.

### Python for Everybody

%[https://youtu.be/8DvywoWv6fI]

Another beginner friendly Python course in the freeCodeCamp YouTube channel is Python for Everybody. What makes this course special is that it not only targeted at Python beginners but at people who're trying to get started with programming in general. 

The course is a little over 13 hours long and is taught by Charles R. Severance aka Dr. Chuck. He has authored some of the most amazing courses on the internet. 

If you're patient enough to sit through a 13 hour course, Python for Everybody is one of the best Python courses online.

### 12 Beginner Python Projects

%[https://youtu.be/8ext9G7xspg]

If you prefer a project-based approach, then this 3 hours course by Kylie Ying is highly recommended. 

Kylie is a freeCodeCamp team member and knows what she's doing. In this course you'll learn to make 12 beginner friendly Python projects in increasing levels of complexity.

### Learn Python by Building 5 Games

%[https://youtu.be/XGf2GcyHPhc]

If you're into gaming and want to learn Python through building classic games, then this course should be a good fit for you. 

The instructor for this course is Christian Thompson, an experienced Python programmer. If you're familiar with another programming language or you learn well by jumping into projects, dive right in.

### Intermediate Python

%[https://youtu.be/HGOBQPFzWKo]

If you've finished your first Python course and have learned all the fundamental concepts and now you're looking for the next logical step, then look no further.

Patrick Loeber has produced this 6 hour course on intermediate Python where you'll learn about a good number concepts usually not found in beginner Python courses.

### Object Oriented Programming with Python

%[https://youtu.be/Ej_02ICOIgs]

If you're struggling to understand of object oriented programming in general, this course will teach you object oriented programming with Python in 2 hours. 

The course includes tons of code examples and covers all the important concepts regarding object oriented programming with Python. I'd suggest this course right after you've finished your basic course.

### Python for Data Science

%[https://youtu.be/LHBE6Q9XlzI]

This is a bit of a specialized course. If you're thinking of getting into data science and want to learn about all the necessary Python stuff necessary for data science then this course will help you greatly. 

Don't think that this is a quick course. In its just over 12 hour runtime, this course will teach you Python programming concepts and a bunch of tools essential for data science in great detail.

### Data Structures and Algorithms in Python

%[https://youtu.be/pkYVOmU3MgA]

Having an understanding of data structures and algorithms is essential to becoming an efficient software developer. 

In this 12.5 hour course from Jovian, you'll learn about important data structures and algorithms with code examples in great detail. Regardless of what you plan to do with Python afterwards, I'd highly recommend this course.

## Conclusion

I would like to thank you from the bottom of my heart for the time you've spent reading this article. 

Although I've listed as many as good resources I could, the [freeCodeCamp YouTube channel](https://www.youtube.com/c/Freecodecamp/search?query=python) is just filled with excellent Python learning resources.

I also have a personal blog where I write about random tech stuff, so if you're interested in something like that, checkout [https://farhan.dev](https://farhan.dev). If you have any questions or are confused about anything – or just want to get in touch – I'm available on [Twitter](https://twitter.com/frhnhsin) and [LinkedIn](https://www.linkedin.com/in/farhanhasin/).

