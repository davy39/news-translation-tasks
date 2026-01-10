---
title: What is Python? How the Interpreter Works and How to Write "Hello World" in
  Python
subtitle: ''
author: Michael Para
co_authors: []
series: null
date: '2022-10-17T13:38:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-python-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/python-img.jpg
tags:
- name: beginner
  slug: beginner
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, I am going to explain what Python is and how the Python
  interpreter works. Then you''ll write your first "Hello World" program.

  What is Python?

  Python is a high-level programming language designed to do many tasks. It''s based
  on the C...'
---

In this article, I am going to explain what Python is and how the Python interpreter works. Then you'll write your first "Hello World" program.

## What is Python?

Python is a high-level programming language designed to do many tasks. It's based on the CPython interpreter which translates the Python code into something the machine can read.

Python gives us the ability to use a lot of modules and packages with our code, which are standard libraries built in with the interpreter.

You can use Python to do many tasks such as:

* Machine Learning
    
* Artificial Intelligence
    
* Data Visualization
    
* Programming Applications
    
* Web Applications
    
* Language and Game Development
    
* Data Analytics
    

and more.

Additionally, Python's syntax is pretty simple and easy to learn – often it seems that you are just writing a message to someone else. Just make sure you know the indentation rules :).

We can compare Python with other interpreted programming languages such as Java, JavaScript, PHP, and others. But you might be wondering – what is CPython?

In the following section, I am going to focus on the history of the Python interpreter in-depth, then I'll answer this question.

## Python History Overview

The first appearance of the Python programming language was in late 1980s. It was created by Guido van Rossum.

Python was designed to replace the ABC programming language which worked with Amoeba operating system.

Rossum started the implementation in 1989 and he worked on Python alone until 2018.

He named it Python because the first version of it was able to read the BBC comedy script “Monty Python's Flying Circus”.

The first release was in 1994 under version 1.0 (Python 1.0) and the second release was in 2000, named version 2.0.

In version 2.0, van Rossum added minor features such as collection systems and comprehensions.

The third version was released in 2008 and fixed a basic flaw of the language. They named this version “Py3K”, or Python 3.0.

## How Does the Python Interpreter Work?

The Python interpreter is called “CPython” and it's written in the C programming language. This is the default implementation for Python.

In the following sections, you will understand how the Python interpreter works behind the scenes.

### Source Code Analysis

Actually, any translator starts with the source code analysis. Here the Python interpreter receives the source code and initializes some instructions to do the following things:

It follows the indentation rule and checks the Python syntax. Maybe there are some incorrect lines, so it will stop the program from the execution to show the error message.

This phase is called [lexical analysis](https://codedtag.com/php/what-is-php-how-to-write-php-program/#the-lexical-analysis), which means dividing the source code files into a list of tokens

In the following step, the interpreter will generate byte codes. Let's see how that works.

### Byte Code Generation

Once the parser of the Python interpreter receives the tokens, it starts to manipulate the lexical tokens. It generates a big structure called the AST (Abstract Syntax Tree).

The interpreter converts this AST to byte code which means machine language. In Python, the byte code can be saved in a file ending with the “.pyc” extension.

In the following section, you will see how the python interpreter executes these byte codes.

### The Python Virtual Machine (PVM)

The Python interpreter initializes its runtime engine called PVM which is the Python virtual machine.

The interpreter loads the machine language with the library modules and inputs it into the PVM. This converts the byte code into executable code such as 0s and 1s (binary).

And then it prints the results.

Note that if an error happens during the PVM process, the executor will terminate the operation immediately to display the error.

Now you will learn how to install Python on your operating system.

If you have no Python software or you're using a mobile device, you can use any [online Python compiler](https://codedtag.com/python/free-online-python-compiler-interpreter/).

## How to Install Python

To install Python on your Ubuntu Linux operating system, follow these instructions:

Open your terminal and run the following command to update the Ubuntu local system repository:

```xml
sudo apt update
```

Install the latest version of Python using the following command:

```xml
sudo apt install python3
```

If you are using Windows OS, you have to follow these steps to install Python on your machine.

1. Navigate to the [python official page](https://www.python.org/downloads/windows/) and download the latest installer.
    
2. Once you choose the latest version by the above link, you have to select the bit system according to your Windows operating system.
    
3. Run the installer and follow the written instruction on the installer.
    

Once you install the program, you have to verify the current version of Python on your operating system by using the following command via terminal or CMD according to your operating system.

Just type `python` and hit enter – it will show you the result like in the below image:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-67.png align="left")

*Verifying Python Version Via CMD*

In the next section, you will learn how to write your first program with Python.

## How to Write Your First Python Program

In this program, you're going to print the classic “Hello World” message using the Python programming language.

First, create a folder and name it “CodedTag” then create a file inside and name it as a “page.py”.

Then copy and paste the following Python code:

```python
# output: Hello World
print( "Hello World" )
```

Then open the terminal and navigate to the project directory and run the following command:

```xml
python page.py
```

The output will be like the following image:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-68.png align="left")

*Execute Python Message*

Congratulations – you just wrote your first Python program.

## Wrapping Up

In this article, you learned what Python is and a bit of its history. You also learned how the Python interpreter works.

Let's summarize it in a few points:

1. The interpreter checks and searches for syntax errors and verifies indentation rules. Then it converts the source code via tokenization.
    
2. The parser receives the lexical tokens and generates an Abstract Syntax Tree.
    
3. The interpreter converts the AST to Byte Code and initializes the Python Virtual machine to execute the byte code and send back the final result.
    

Thank you for reading, If you'd like to read more of my articles, you can find them on [FlatCoding](https://flatcoding.com/). Stay tuned for my next articles.
