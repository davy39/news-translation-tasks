---
title: Python Functions – How to Define and Call a Function
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-16T17:17:43.000Z'
originalURL: https://freecodecamp.org/news/python-functions-define-and-call-a-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/functions.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In programming, a function is a reusable block of code that executes a
  certain functionality when it is called.

  Functions are integral parts of every programming language because they help make
  your code more modular and reusable.

  In this article, I ...'
---

In programming, a function is a reusable block of code that executes a certain functionality when it is called.

Functions are integral parts of every programming language because they help make your code more modular and reusable.

In this article, I will show you how to define a function in Python and call it, so you can break down the code of your Python applications into smaller chunks.

I will also show you how arguments and the return keyword works in Python functions.

## Basic Syntax for Defining a Function in Python

In Python, you define a function with the `def` keyword, then write the function identifier (name) followed by parentheses and a colon.

The next thing you have to do is make sure you indent with a tab or 4 spaces, and then specify what you want the function to do for you.

```py
def functionName():
    # What to make the function do
```
## Basic Examples of a Function in Python

Following the basic syntax above, an example of a basic Python function printing “Hello World” to the terminal looks like this:

```py
def myfunction():
    print("Hello World")
``` 

**To call this function**, write the name of the function followed by parentheses:

```py
myfunction()

```

Next, run your code in the terminal by typing `python filename.py` to show what you want the function to do:

![sss-1](https://www.freecodecamp.org/news/content/images/2022/03/sss-1.png)

Another basic example of subtractig 2 numbers looks like this:

```py
def subtractNum():
    print(34 - 4)

subtractNum()
# Output: 30
```

## Arguments in Python Functions

While defining a function in Python, you can pass argument(s) into the function by putting them inside the parenthesis.

The basic syntax for doing this looks as shown below:

```py
def functionName(arg1, arg2):
    # What to do with function
    
```

When the function is called, then you need to specify a value for the arguments:

```py
functionName(valueForArg1, valueForArg2)
```

Here's an example of arguments in a Python function:

```py
def addNum(num1, num2):
    print(num1 + num2)
addNum(2, 4)

# Output: 6
```

In the example above:
- I passed 2 arguments into the function named `addNum`
- I told it to print the sum of the 2 arguments to the terminal
- I then called it with the values for the 2 arguments specified

**N.B.**: You can specify as many arguments as you want.

## How to Use the Return Keyword in Python

In Python, you can use the `return` keyword to exit a function so it goes back to where it was called. That is, send something out of the function. 

The return statement can contain an expression to execute once the function is called.

The example below demonstrates how the return keyword works in Python:

```py
def multiplyNum(num1):
    return num1 * 8

result = multiplyNum(8)
print(result)

# Output: 64
```

**What’s the code above doing?** 
- I defined a function named `multiplyNum` and passed it `num1` as an argument
- Inside the function, I used the return keyword to specify that I want `num1` to be multiplied by 8
- After that, I called the function, passed `8` into it as the value for the `num1` argument, and assigned the function call to a variable I named `result`
- With the result variable, I was able to print what I intended to do with the function to the terminal

## Conclusion

In this article, you learned how to define and call functions in Python. You also learned how to pass arguments into a function and use the return keyword, so you can be more creative with the functions you write.

If you find this article helpful, don’t hesitate to share it with your friends and family.


