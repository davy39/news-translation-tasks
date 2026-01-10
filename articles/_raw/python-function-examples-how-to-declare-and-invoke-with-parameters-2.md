---
title: Python Function Examples – How to Declare and Invoke with Parameters
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-24T19:04:21.000Z'
originalURL: https://freecodecamp.org/news/python-function-examples-how-to-declare-and-invoke-with-parameters-2
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/david-clode-vb-3qEe3rg8-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Python has a bunch of helpful built-in functions you can use to do all\
  \ sorts of stuff. And each one performs a specific task. \nBut did you know that\
  \ Python also allows you to define your own functions?\nThis article will show you\
  \ how to create and cal..."
---

Python has a bunch of helpful built-in functions you can use to do all sorts of stuff. And each one performs a specific task. 

But did you know that Python also allows you to define your own functions?

This article will show you how to create and call your own Python functions. It will also give you an overview of how to pass input parameters and arguments to your functions.

## What is a Function?

A function is an isolated block of code that performs a specific task.

Functions are useful in programming because they eliminate needless and excessive copying and pasting of code throught a program.

If a certain action is required often and in different places, that is a good indicator that you can write a function for it. Functions are meant to be reusable.

Functions also help organize your code.

If you need to make a change, you'll only need to update that certain function. This saves you from having to search for different pieces of the same code that have been scattered in different locations in your program by copying and pasting.

This complies with the DRY (Don't Repeat Yourself) principle in software development.

The code inside a function runs only when they the function is called.

Functions can accept arguments and defaults and may or not return values back to the caller once the code has run.

## How to Define a Function in Python

The general syntax for creating a function in Python looks something like this:

```
def function_name(parameters):
    function body
```

Let's break down what's happening here:

- `def` is a keyword that tells Python a new function is being defined.
- Next comes a valid function name of your choosing. Valid names start with a letter or underscore but can include numbers. Words are lowercase and separated by underscores. It's important to know that function names can't be a Python reserved keyword.
- Then we have a set of opening and closing parentheses, `()`. Inside them, there can be zero, one, or more *optional* comma separated parameters with their *optional* default values. These are passed to the function.
- Next is a colon, `:`, which ends the function's definition line.
- Then there's a new line followed by a level of indentation (you can do this with 4 spaces using your keyboard or with 1 Tab instead). Indentation is important since it lets Python know what code will belong in the function.
- Then we have the function's body. Here goes the code to be executed – the contents with the actions to be taken when the function is called.
- Finally, there's an *optional* return statement in the function's body, passing back a value to the caller when the function is exited.

Keep in mind that if you forget the parentheses`()` or the colon `:` when trying to define a new function, Python will let you know with a `SyntaxError`.


## How to Define and Call a Basic Function in Python

Below is an example of a basic function that has no return statement and doesn't take in any parameters. 

It just prints `hello world` whenever it is called.


```python
def hello_world_func():
    print("hello world")
```

Once you've defined a function, the code will not run on its own.

To execute the code inside the function, you have make a *function invokation* or else a *function call*.

You can then call the function as many times as you want.

To call a function you need to do this:

```
function_name(arguments)
```

Here's a breakdown of the code:

- Type the function name.
- The function name has to be followed by parentheses. If there are any required arguments, they have to be passed in the parentheses. If the function doesn't take in any arguments, you still need the parentheses.

To call the function from the example above, which doesn't take in any arguments, do the following:

```python
hello_world_func()

#Output
#hello world 
```

## How to Define and Call Functions with Parameters

So far you've seen simple functions that don't really do much besides printing something to the console. 

What if you want to pass in some extra data to the function?

We've used terms here like *parameter* and *arguments*.

What are their definitions exactly?

Parameters are a named placeholder that pass information into functions.

They act as variables that are defined locally in the function's definition line.


 ```python
def hello_to_you(name):
    print("Hello " + name)
```

In the example above, there is one parameter, `name`.

We could've used `f-string formatting` instead – it works the same way as the previous example:

```python
def hello_to_you(name):
    print(f"Hello {name}")
```

There can be a list of parameters inside the parentheses, all separated by commas.


```python
def name_and_age(name,age):
    print(f"I am {name} and I am {age} years old!")
```

Here, the parameters in the function are `name` and `age`.

When a function is called, arguments are passed in.

Arguments, like parameters, are information passed to functions.

In particular, they are the actual values that correspond to the parameters in the function definition.

Calling the function from a previous example and passing in an argument would look like this:

```python
def hello_to_you(name):
    print(f"Hello {name}")
    
    
hello_to_you("Timmy")
#Output
# Hello Timmy
```

The function can be called many times, passing in different values each time.

```python
def hello_to_you(name):
    print(f"Hello {name}")
    
hello_to_you("Timmy")
hello_to_you("Kristy")
hello_to_you("Jackie")
hello_to_you("Liv")

#Output:
#"Hello Timmy"
#"Hello Kristy"
#"Hello Jackie"
#"Hello Liv"
```

The arguments presented so far are called **positional arguments**.

All positional arguments are very much **required**.

### The number of positional arguments matters

When calling functions, you need to pass the correct number of arguments, otherwise there will be an error.

When it comes to positional arguments, the number of arguments passed in to the function call has to be exactly the same as the number of parameters in the function's definition. 

You can't leave any out or add in any more.

Say that you have this function that takes in two parameters:

```python
def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
```

If the function is called with just one argument passed in, like this, there will be an error:

```python
def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
    

hello_to_you("Timmy")
```

Output:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello_to_you() missing 1 required positional argument: 'last_name'
```

If the function is called with three arguments passed in, there will again be an error:

```python
def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
    

hello_to_you("Timmy","Jones",34)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello_to_you() takes 2 positional arguments but 3 were given
```

There will also be an error if we pass in *no* arguments.

```python
def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
    

hello_to_you()
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello_to_you() missing 2 required positional arguments: 'first_name' and 'last_name'
```

Instead, we need two arguments, since two parameters are listed in the function definition.


```python
def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
    

hello_to_you("Timmy","Jones")
#Output:
# Hello,Timmy Jones
```


### The order of positional arguments matters

Besides including the correct *number* of arguments, it is important to note that the *order* in which the arguments are passed in matters.

Arguments need to be passed in the exact same order as the order of the parameters that have been declared in the function's definition.

It works like variable assignment. 

The first argument is the value of the first parameter in the function's definition. The second argument is the value of the second parameter in the function's ddefinition – and so on.

```python
def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
    

hello_to_you("Timmy","Jones")
#Output
#Hello,Timmy Jones 
#you can visualise it like:
#first_name = "Timmy"
#last_name = "Jones"
```

If the order is not correct, the output might not make much sense and not be what you intended it to be.


```python
def fave_language(name,language):
    print(f"Hello, I am {name} and my favorite programming language is {language}")

    
fave_language("Python","Dionysia")
#output:
#Hello, I am Python and my favorite programming language is Dionysia
#it is like you did
#name="Python"
#language = "Dionysia"
```

### How to use keyword arguments in Python functions

So far you've seen one type of argument, positional arguments.

With positional arguments, functions are called with just the values passed in the function call. There, each value directly corresponds with the number, order, and position of each parameter in the function definition.

However, functions in Python can accept another type of argument, that is **keyword arguments**.

In this case, instead of just passing in values in the function call, you instead specify the name of the parameter and then the value you want to assign it, in the form of `key = value`. 

Each key matches each parameter in the function definition.

Explicitely calling the name of parameters and the values they take helps in being extra clear about what you're passing in and avoids any possible confusion.

```python
def fave_language(name,language):
    print(f"Hello, I am {name} and my favorite programming language is {language}")

    
fave_language(name="Dionysia",language="Python")
#output:
#Hello, I am Dionysia and my favorite programming language is Python
```

Keyword arguments, as seen above, can be in a particular order. But they are more flexible than positional arguments in the sense that order of arguments now does not matter. 

So you could do this and there would be no errors:

```python
def fave_language(name,language):
    print(f"Hello, I am {name} and my favorite programming language is {language}")

    
fave_language(language="Python",name="Dionysia")
#output:
#Hello, I am Dionysia and my favorite programming language is Python
```

But you still have to give the correct *number* of arguments.

You can use both positional and keyword arguments together in a function call, like the example below where there is one positional argument and one keyword argument:

```python
def fave_language(name,language):
    print(f"Hello, I am {name} and my favorite programming language is {language}")

    
fave_language("dionysia",language="Python")
#output:
#Hello, I am dionysia and my favorite programming language is Python
```

In this case, order matters again. 

Positional arguments always come first and all keyword arguments should follow the positional arguments. Otherwise there will be an error:

```python
def fave_language(name,language):
    print(f"Hello, I am {name} and my favorite programming language is {language}")

    
fave_language(language="Python","dionysia")
```


### How to define a parameter with a default value in Python

Function arguments can also have default values. They are known as *default or optional arguments*.

For a function argument to have a default value, you have to assign a default value to the parameter in the function's definition.

You do this with the `key=value` form, where `value` will be the default value for that parameter.

```python
def fave_language(language="python"):
    print(f"My favorite  programming language is {language}!")
    
fave_language()
#output
#My favorite  programming language is python!
```

As you see, default arguments are *not* required in the function call, and the value of `language` will always default to Python if another value isn't provided in the call.

However, default values can be easily overriden if you provide another value in the function's call:

```python
def fave_language(language="python"):
    print(f"My favorite  programming language is {language}!")
    
fave_language("Java")
#prints "My favorite  programming language is Java!" to the console
```

There can be more than one default value passed to the function.

When the function is called, none, one, some, or all of the default arguments can be provided and order does not matter. 

```python
def personal_details(name="Jimmy",age=28,city="Berlin"):
    print(f"I am {name},{age} years old and live in {city}") 
    
#We can do:

personal_details()
#output:
#I am Jimmy,28 years old and live in Berlin

personal_details(age=30)
#I am Jimmy,30 years old and live in Berlin

personal_details(city="Athens",name="Ben",age=24)
##I am Ben,24 years old and live in Athens
```


Default arguments can be combined with non-default arguments in the function's call.

Here is a function that accepts two arguments: one positional, non-default (`name`) and one optional, default (`language`).

```python
def fave_language(name,language="Python"):
    print(f"My name is {name} and my favorite  programming language is {language}!")
    
fave_language("Dionysia")
#output:
#"My name is Dionysia and my favorite  programming language is Python!" 
```

The default argument, `langyage="Python"`, is *optional*. But the positional argument, `name`, will always always required. If another `language` is not passed in, the value will always default to Python.

Another thing to mention here is that, when defaults and non defaults are used together, the order they are defined in the function defintion matters.

All the positional arguments go first and are followed by the default arguments.

This will not work:

```python
def fave_language(language="Python",name):
    print(f"My name is {name} and my favorite  programming language is {language}!")
    
fave_language("Dionysia")
```

Output:

```
 File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```


## Conclusion

In this article, you learned how to declare functions and invoke them with parameters in the Python programming language.

This was an introduction on how to create simple functions and how to pass data into them, with parameters. We also went over the different types of  arguments like *positional*, *keyword*, and *default* arguments.

To recap:
 - The order and number of *positional* arguments matters.
 - With *keyword* arguments, order does not matter. Number does matter, though, since each keyword argument corresponds with each parameter in the function's definition.
 - *Default* arguments are entirely optional. You can pass in all of them, some of them, or none at all.

If you are interested in going more in-depth and learning more about the Python programming language, freeCodeCamp has a [free Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/). 

You'll start from the basics and fundamentals of the language and then progress to more advanced concepts like data structures and relational databases. In the end you'll build 5 projects to put to practice what you've learnt.

Thank you for reading and happy learning.




