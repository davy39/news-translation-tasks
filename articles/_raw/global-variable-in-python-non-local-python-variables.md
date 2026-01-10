---
title: Global Variable in Python – Non-Local Python Variables
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-10T21:21:45.000Z'
originalURL: https://freecodecamp.org/news/global-variable-in-python-non-local-python-variables
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/kevin-ku-w7ZyuGYNpRQ-unsplash.jpg
tags:
- name: Python
  slug: python
- name: variables
  slug: variables
seo_title: null
seo_desc: "In Python and most programming languages, variables declared outside a\
  \ function are known as global variables. You can access such variables inside and\
  \ outside of a function, as they have global scope. \nHere's an example of a global\
  \ variable:\nx = 10 ..."
---

In Python and most programming languages, variables declared outside a function are known as global variables. You can access such variables inside and outside of a function, as they have global scope. 

Here's an example of a global variable:

```python
x = 10 

def showX():
    print("The value of x is", x)
    
showX()
# The value of x is 10
```

The variable `x` in the code above was declared outside a function: `x = 10`. 

Using the `showX()` function, we were still able to access `x` because it was declared in a global scope. 

Let's take a look at another example that shows what happens when we declare a variable inside a function and try to access it elsewhere.

```python
def X():
    x = 10 

X()

def showX():
    print("The value of x is", x)
    
showX()
NameError: name 'x' is not defined
```

In the example above, we declared `x` inside a function and tried to access it in another function. This resulted in a NameError because `x` was not defined globally. 

Variables defined inside functions are called local variables. Their value can only be used within the function where they are declared. 

You can change the scope of a local variable using the `global` keyword – which we'll discuss in the next section.

## What is the `global` Keyword Used for in Python?

The global keyword is mostly used for two reasons:

* To modify the value of a global variable.
* To make a local variable accessible outside the local scope. 

Let's look at some examples for each scenario to help you understand better. 

### Example #1 - Modifying a Global Variable Using the `global` Keyword

In the last section where we declared a global variable, we did not try to change the value of the variable. All we did was access and print its value in a function. 

Let's try and change the value of a global variable and see what happens:

```python
x = 10 

def showX():
    x = x + 2
    print("The value of x is", x)
    
showX()
# local variable 'x' referenced before assignment
```

As you can see above, when we tried to add 2 to the value of `x`, we got an error. This is because we can only access but not modify `x`. 

To fix that, we use the `global` variable. Here's how:

```python
x = 10 

def showX():
    global x
    x = x + 2
    print("The value of x is", x)
    
showX()
# The value of x is 12
```

Using the `global` keyword in the code above, we were able to modify `x` and add 2 to its initial value. 

### Example #2 - How to Make a Local Variable Accessible Outside the Local Scope Using the `global` Keyword

When we created a variable inside a function, it wasn't possible to use its value inside another function because the compiler did not recognize the variable.

Here's how we can fix that using the `global` keyword:

```python
def X():
    global x
    x = 10 
    
X()
    
def showX():
    print("The value of x is", x)
    
showX()
# The value of x is 10
```

To make it possible for `x` to be accessible outside its local scope, we declared it using the `global` keyword: `global x`. 

After that, we assigned a value to `x`. We then called the function we used to declare it: `X()`

When we called the `showX()` function, which prints the value of `x` declared in the `X()` function, we did not get an error because `x` has a global scope. 

## Summary

In this article, we talked about global and local variables in Python.

The examples showed how to declare both global and local variables. 

We also talked about the `global` keyword which lets you modify the value of a global variable or make a local variable accessible outside its scope. 

Happy coding!

