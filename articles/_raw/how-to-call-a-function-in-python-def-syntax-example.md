---
title: How to Call a Function in Python – Def Syntax Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-20T16:17:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-call-a-function-in-python-def-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/callFunction.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python and other programming languages, you can use functions to avoid\
  \ repeting yourself and to reuse pieces of code.\nTo make functions work, you don’t\
  \ just write them and say goodbye – you have to call them too. \nBefore you call\
  \ a function, you n..."
---

In Python and other programming languages, you can use functions to avoid repeting yourself and to reuse pieces of code.

To make functions work, you don’t just write them and say goodbye – you have to call them too. 

Before you call a function, you need to write it with the def keyword. So in this article, I will not just show you how to call a function, I will also show you how to create it.

## What We'll Cover
- [How to Define a Function with the `def` Keyword](#heading-how-to-define-a-function-with-the-def-keyword)
- [How to Call a Function in Python](#heading-how-to-call-a-function-in-python)
- [How to Call a Nested Function in Python](#heading-how-to-call-a-nested-function-in-python)
- [Final Thoughts](#heading-final-thoughts)


## How to Define a Function with the `def` Keyword

To define a function in Python, you type the def keyword first, then the function name and parentheses. 

To tell Python the function is a block of code, you specify a colon in front of the function name. What follows is what you want the function to do.

The basic syntax of a function looks like this:
```py
def function_name():
    # What you want the function to do
```

An example of a function looks like this:
```py
def learn_to_code():
    print("You can learn to code for free on freeCodeCamp")

```
What we want this function to do is to print the text `You can learn to code for free on freeCodeCamp` to the terminal. 

To make this function run, you have to call it. That’s what we’ll do next.

## How to Call a Function in Python

To call a function, simply use its name followed by the arguments in the parentheses.

The syntax for calling a function looks like this:
```py
function_name()
```

To call a function we defined earlier, we need to write `learn_to_code()`:

```py
def learn_to_code():
    print("You can learn to code for free on freeCodeCamp")

learn_to_code()
# Output: You can learn to code for free on freeCodeCamp
```

**N.B**: Make sure you don’t specify the function call inside the function block. It won’t work that way because the call will be treated as a part of the function to run.

![ss1-3](https://www.freecodecamp.org/news/content/images/2022/07/ss1-3.png)

You can see the function didn’t print the text to the terminal because I attempted to call it inside the function block.

![ss2-4](https://www.freecodecamp.org/news/content/images/2022/07/ss2-4.png)

And here you can see the function runs because I called it outside the function block.


## How to Call a Nested Function in Python

It can be confusing to call a nested function, so I want to show you how to do it.

Below is the nested function:
```py
def learn_to_code():
    print("You can learn to code for free on freeCodeCamp")

    def learn_what_language():
        print("You can learn any programming language on the freeCodeCamp YouTube channel")
  
```

The `learn_what_language` function is a part of the `learn_to_code` function because it is nested inside it.

If you type `learn_to_code()` and run the code, only the outer function (learn_to_code) gets called: 

![ss3-3](https://www.freecodecamp.org/news/content/images/2022/07/ss3-3.png)
You can see that only the outer function gets called and the inner function is greyed out.

To call the inner function too, you should type `learn_what_language()` precisely. But where? 

You should look right under the def keyword of the inner function and type the function call there.

But if you do this only, it won’t still work because you have to call the outer function too.

![ss4-3](https://www.freecodecamp.org/news/content/images/2022/07/ss4-3.png)
You can see the inner function (`learn_what_language`) still didn’t do what we want it to do.

To make it work, you have to call both functions where necessary:
```py
def learn_to_code():
    print("You can learn to code for free on freeCodeCamp")

    def learn_what_language():
        print("You can learn any programming language on the freeCodeCamp YouTube channel")
    
    learn_what_language()

learn_to_code()

"""
Output:
You can learn to code for free on freeCodeCamp
You can learn any programming language on the freeCodeCamp YouTube channel
"""
 ```

![ss5-4](https://www.freecodecamp.org/news/content/images/2022/07/ss5-4.png)
You can see everything works as expected.

## Final Thoughts

I hope this article helps you learn how to properly call a function in Python.

If you want to learn Python more, you can check out the [freeCodeCamp Python curriculum](https://www.freecodecamp.org/learn/scientific-computing-with-python/). It's free.

Keep coding :)


