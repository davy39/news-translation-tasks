---
title: Functions in Python – Explained with Code Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-07-28T17:24:21.000Z'
originalURL: https://freecodecamp.org/news/functions-in-python-a-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/FUNCTIONS-IN-PYTHON.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In any programming language, functions facilitate code reusability. In\
  \ simple terms, when you want to do something repeatedly, you can define that something\
  \ as a function and call that function whenever you need to. \nIn this tutorial,\
  \ we shall learn ..."
---

In any programming language, functions facilitate _code reusability_. In simple terms, when you want to do something repeatedly, you can define that something as a function and call that function whenever you need to. 

In this tutorial, we shall learn about user-defined functions in Python.

When you started coding in Python, you'd have used the built-in `print()` function in your `Hello World!` program 😀 and the `input()` function to read in input from the user. 

So long as you know how to _use_ these functions, you don't have to worry about how they've been implemented. 

In programming, this is called _abstraction._ It lets you use functions by calling the function with required arguments, without having to worry about how they actually work.

There's a whole wealth of built-in functions in Python. In this post, we shall see how we can define and use our own functions. Let's get started!

## Python Function Syntax

The following snippet shows the general syntax to define a function in Python:

```python
def function_name(parameters):
    # What the function does goes here
    return result 
```

* You need to use the `def` keyword, give your function a name, followed by a pair of parentheses, and end the line with a colon (:). 
* If your function takes arguments, the names of the arguments (parameters) are mentioned inside the opening and closing parentheses.
* Please note that in _function definition,_ the arguments that your function consumes are referred to as _parameters_.
* When you call the function with specific values for these parameters, they're called _arguments_ or actual parameters. This is because the _arguments_ in the _function call_ are the values used for the function's parameters.
* Then, you begin an indented block. This is the body of the function that describes what your function does.
* There's a `return` statement that returns the result of the operation on the arguments. The `return` statement returns control to the point where the function was originally called.

Note that the `arguments` and the `return` statement are optional. This means that you could have a function that takes in _no arguments_, and _returns nothing_. 😀

Let's now try to understand the above statements using simple examples.

## How to Create a Simple Function in Python

Let's now create a simple function in Python that greets the user, as shown below: 

```python
def my_func():
  print("Hello! Hope you're doing well")


```

As you can see, the function `my_func()`:

* takes no arguments, 
* returns nothing, and
* prints out `"Hello! Hope you're doing well"` whenever it's _called_.

Note that the above function definition is inert until the function is triggered or called. Let's go ahead and call the function `my_func()` and check the output.

```python
my_func()

# Output
Hello! Hope you're doing well
```

## How to Create a Function with Arguments in Python

Now, we shall modify the function `my_func()` to include the `name` and `place` of the user.

```python
def my_func(name,place):
  print(f"Hello {name}! Are you from {place}?")
```

We can now call `my_func()` by passing in two strings for the `name` and `place` of the user, as shown below.

```python
my_func("Jane","Paris")

# Output
Hello Jane! Are you from Paris?
```

What happens if you specify the `place` first and then the `name`? Let's find out.

```python
my_func("Hawaii","Robert")

# Output
Hello Hawaii! Are you from Robert?
```

We get `Hello Hawaii! Are you from Robert?` – and this doesn't make sense. 🙂What's causing this problem? 

The arguments in the function call are _positional arguments_. This means that the first argument in the function call is used as the value of the first parameter (`name`)  and the second argument in the function call is used as the value of the second parameter ( `place` ) 

See the code snippet below. Instead of specifying only the arguments, we've mentioned the parameters and the values they take. 

```python
my_func(place="Hawaii",name="Robert")

# Output
Hello Robert! Are you from Hawaii?
```

These are called _keyword arguments._ The order of arguments in the function call does not matter so long as the names of the parameters are correct.

## How to Create a Function with Default Arguments in Python

What if we had certain parameters that take a specific value most of the time during the function calls? 

Can we not do better than calling the function with the same value for a particular parameter? 

Yes we can do better, and that's what `default arguments` are for! 😀

Let's create a function `total_calc()` that helps us calculate and print out the total amount to be paid at a restaurant. Given a `bill_amount` and the percentage of the `bill_amount` you choose to pay as tip (`tip_perc` ), this function calculates the total amount that you should pay. 

Note how the function definition includes the default value of the parameter `tip_perc` to be used when the user doesn't specify a tip percentage.

Run the code snippet below.👇🏽 You now have your function ready!

```python
def total_calc(bill_amount,tip_perc=10):
  total = bill_amount*(1 + 0.01*tip_perc)
  total = round(total,2)
  print(f"Please pay ${total}")
```

Let's now call the function in a few different ways. The code snippet below shows the following:

* When you call the function `total_calc` with only the `bill_amount`, by default the tip percentage of 10 is used. 
* When you explicitly specify the percentage tip, the tip percentage mentioned in the function call is used.

```python
# specify only bill_amount
# default value of tip percentage is used

 total_calc(150)
 # Output
 Please pay $165.0
 
 # specify both bill_amount and a custom tip percentage
 # the tip percentage specified in the function call is used
 
 total_calc(200,15)
 # Output
 Please pay $230.0
 
 total_calc(167,7.5)
 # Output
 Please pay $179.53
 
```

## How to Create a Function that Returns a Value in Python

So far, we've only created functions that may or may not take arguments and do not return anything. Now, let's create a simple function that returns the volume of a cuboid given the `length`, the `width`, and the `height`.

```python
def volume_of_cuboid(length,breadth,height):
  return length*breadth*height
  
  
```

Recall that the `return` keyword returns control to the point where the function was called. The function call is replaced with the `return value` from the function. 

Let's call the function `volume_of_cuboid()` with the necessary dimension arguments, as shown in the code snippet below. Note how we use the variable `volume` to capture the value returned from the function.

```
volume = volume_of_cuboid(5.5,20,6)
print(f"Volume of the cuboid is {volume} cubic units")

# Output
Volume of the cuboid is 660.0 cubic units
```

## How to Create a Function that Returns Multiple Values in Python

In our earlier example, the function `volume_of_cuboid()` returned only one value, namely, the volume of a cuboid given its dimensions. Let's see how we can return multiple values from a function.

* To return multiple values from a function, just specify the values to be returned, separated by a comma.
* By default, the function returns the values as a tuple. If there are `N` return values, we get an `N-`tuple.

Let's create a simple function `cube()` that returns the volume and total surface area of a cube, given the length of its side.

```python
def cube(side):
  volume = side **3
  surface_area = 6 * (side**2)
  return volume, surface_area
```

To verify that a tuple is returned, let's collect it in a variable `returned_values`, as shown below:

```
returned_values = cube(8)
print(returned_values)

# Output
(512, 384)
```

Now, we shall _unpack the tuple_ and store the values in two different variables.

```
volume, area = cube(6.5)
print(f"Volume of the cube is {volume} cubic units and the total surface area is {area} sq. units")

# Outputs
Volume of the cube is 274.625 cubic units and the total surface area is 253.5 sq. units
```

## How to Create a Function that Takes a Variable Number of Arguments in Python

Let's start by asking a few questions:

* What if we do not know the exact number of arguments beforehand? 
* Can we create functions that work with a variable number of arguments?

The answer is yes! And we'll create such a function right away.

Let's create a simple function `my_var_sum()` that returns the sum of all numbers passed in as the argument. However, the number of arguments could be potentially different each time we call the function.

Notice how the function definition now has `*args` instead of just the name of the parameter. In the body of the function, we loop through `args` until we've used all the arguments. The function `my_var_sum` returns the sum of all numbers passed in as arguments.

```python
def my_var_sum(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum
```

Let's now call the function `my_var_sum()` with a different number of arguments each time and quickly check if the returned answers are correct! 🙂

```python
# Example 1 with 4 numbers
sum = my_var_sum(99,10,54,23)
print(f"The numbers that you have add up to {sum}")
# Output
The numbers that you have add up to 186

# Example 2 with 3 numbers
sum = my_var_sum(9,87,45)
print(f"The numbers that you have add up to {sum}")
# Output
The numbers that you have add up to 141

# Example 3 with 6 numbers
sum = my_var_sum(5,21,36,79,45,65)
print(f"The numbers that you have add up to {sum}")
# Output
The numbers that you have add up to 251
```

## ⌛ A Quick Recap

Let's quickly summarize what we've covered. In this tutorial, we've learned:

* how to define functions, 
* how to pass in arguments to a function, 
* how to create functions with default and variable number of arguments, and
* how to create a function with return value(s).

Hope you all enjoyed reading this article. Thank you for reading. As always, until next time! 😀

