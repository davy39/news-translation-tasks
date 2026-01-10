---
title: Python Global Variables – How to Define a Global Variable Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-05-12T18:46:34.000Z'
originalURL: https://freecodecamp.org/news/python-global-variables-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/fernando-cferdophotography-tNDYN8jWyfM-unsplash.jpg
tags:
- name: Python
  slug: python
- name: variables
  slug: variables
seo_title: null
seo_desc: 'In this article, you will learn the basics of global variables.

  To begin with, you will learn how to declare variables in Python and what the term
  ''variable scope'' actually means.

  Then, you will learn the differences between local and global variable...'
---

In this article, you will learn the basics of global variables.

To begin with, you will learn how to declare variables in Python and what the term 'variable scope' actually means.

Then, you will learn the differences between local and global variables and understand how to define global variables and how to use the `global` keyword.

Here is what we will cover:

1. [An introduction to variables in Python](#intro)
    1. [Variable scope explained](#scope)
2. [How to create variables with local scope](#local)
3. [How to create variables with global scope](#global)
    1.  [The `global` keyword](#keyword)

## What Are Variables in Python and How Do You Create Them? An Introduction for Beginners <a name="intro"></a>

You can think of variables as **storage containers**.

They are storage containers for holding data, information, and values that you would like to save in the computer's memory. You can then reference or even manipulate them at some point throughout the life of the program.

A variable has a symbolic **name**, and you can think of that name as the **label** on the storage container that acts as its identifier.

The variable name will be a reference and pointer to the data stored inside it. So, there is no need to remember the details of your data and information – you only need to reference the variable name that holds that data and information.

When giving a variable a name, make sure that it is descriptive of the data it holds. Variable names need to be clear and easily understandable both for your future self and the other developers you may be working with.

Now, let's see how to actually create a variable in Python.

When declaring variables in Python, you don't need to specify their data type.

For example, in the C programming language, you have to mention explicitly the type of data the variable will hold. 

So, if you wanted to store your age which is an integer, or `int` type, this is what you would have to do in C:

```c
#include <stdio.h>
 
int main(void)
{
  int age = 28;
  // 'int' is the data type
  // 'age' is the name 
  // 'age' is capable of holding integer values
  // positive/negative whole numbers or 0
  // '=' is the assignment operator
  // '28' is the value
}
```

However, this is how you would write the above in Python:

```python
age = 28

#'age' is the variable name, or identifier
# '=' is the assignment operator
#'28' is the value assigned to the variable, so '28' is the value of 'age'
```
The variable name is always on the left-hand side, and the value you want to assign goes on the right-hand side after the assignment operator.
    
Keep in mind that you can change the values of variables throughout the life of a program:

```python
my_age = 28

print(f"My age in 2022 is {my_age}.")

my_age = 29

print(f"My age in 2023 will be {my_age}.")

#output

#My age in 2022 is 28.
#My age in 2023 will be 29.
```

You keep the same variable name, `my_age`, but only change the value from `28` to `29`.

### What Does Variable Scope in Python Mean? <a name="scope"></a>

Variable scope refers to the parts and boundaries of a Python program where a variable is available, accessible, and visible.

There are four types of scope for Python variables, which are also known as the **LEGB rule**:

- **L**ocal,
- **E**nclosing,
- **G**lobal,
- **B**uilt-in.

For the rest of this article, you will focus on learning about creating variables with global scope, and you will understand the difference between the local and global variable scopes.

## How to Create Variables With Local Scope in Python <a name="local"></a>

Variables defined inside a function's body have *local* scope, which means they are accessible only within that particular function. In other words, they are 'local' to that function.

You can only access a local variable by calling the function.

```python
def learn_to_code():
    #create local variable
    coding_website = "freeCodeCamp"
    print(f"The best place to learn to code is with {coding_website}!")

#call function
learn_to_code()


#output

#The best place to learn to code is with freeCodeCamp!
```

Look at what happens when I try to access that variable with a local scope from outside the function's body:

```python
def learn_to_code():
    #create local variable
    coding_website = "freeCodeCamp"
    print(f"The best place to learn to code is with {coding_website}!")

#try to print local variable 'coding_website' from outside the function
print(coding_website)

#output

#NameError: name 'coding_website' is not defined
```

It raises a `NameError` because it is not 'visible' in the rest of the program. It is only 'visible' within the function where it was defined.

## How to Create Variables With Global Scope in Python <a name="global"></a>

When you define a variable *outside* a function, like at the top of the file, it has a global scope and it is known as a global variable.

A global variable is accessed from anywhere in the program.

You can use it inside a function's body, as well as access it from outside a function:

```python
#create a global variable
coding_website = "freeCodeCamp"

def learn_to_code():
    #access the variable 'coding_website' inside the function
    print(f"The best place to learn to code is with {coding_website}!")

#call the function
learn_to_code()

#access the variable 'coding_website' from outside the function
print(coding_website)

#output

#The best place to learn to code is with freeCodeCamp!
#freeCodeCamp
```

What happens when there is a global and local variable, and they both have the same name?

```python
#global variable
city = "Athens"

def travel_plans():
    #local variable with the same name as the global variable
    city = "London"
    print(f"I want to visit {city} next year!")

#call function - this will output the value of local variable
travel_plans()

#reference global variable - this will output the value of global variable
print(f"I want to visit {city} next year!")

#output

#I want to visit London next year!
#I want to visit Athens next year!
```

In the example above, maybe you were not expecting that specific output.

Maybe you thought that the value of `city` would change when I assigned it a different value inside the function. 

Maybe you expected that when I referenced the global variable with the line `print(f" I want to visit {city} next year!")`, the output would be `#I want to visit London next year!` instead of `#I want to visit Athens next year!`.

However, when the function was called, it printed the value of the local variable. 

Then, when I referenced the global variable outside the function, the value assigned to the global variable was printed.

They didn't interfere with one another.

That said, using the same variable name for global and local variables is not considered a best practice. Make sure that your variables don't have the same name, as you may get some confusing results when you run your program.

### How to Use the `global` Keyword in Python <a name="keyword"></a>

What if you have a global variable but want to change its value inside a function?

Look at what happens when I try to do that:

```python
#global variable
city = "Athens"

def travel_plans():
    #First, this is like when I tried to access the global variable defined outside the function. 
    # This works fine on its own, as you saw earlier on.
    print(f"I want to visit {city} next year!")

    #However, when I then try to re-assign a different value to the global variable 'city' from inside the function,
    #after trying to print it,
    #it will throw an error
    city = "London"
    print(f"I want to visit {city} next year!")

#call function
travel_plans()

#output

#UnboundLocalError: local variable 'city' referenced before assignment
```

By default Python thinks you want to use a local variable inside a function.

So, when I first try to print the value of the variable and *then* re-assign a value to the variable I am trying to access, Python gets confused.

The way to change the value of a global variable inside a function is by using the `global` keyword:

```python
#global variable
city = "Athens"

#print value of global variable
print(f"I want to visit {city} next year!")

def travel_plans():
    global city
    #print initial value of global variable
    print(f"I want to visit {city} next year!")
    #assign a different value to global variable from within function
    city = "London"
    #print new value
    print(f"I want to visit {city} next year!")

#call function
travel_plans()

#print value of global variable
print(f"I want to visit {city} next year!")
```

Use the `global` keyword before referencing it in the function, as you will get the following error: `SyntaxError: name 'city' is used prior to global declaration`.

Earlier, you saw that you couldn't access variables created inside functions since they have local scope.

The `global` keyword changes the visibility of variables declared inside functions.

```python
def learn_to_code():
   global coding_website
   coding_website = "freeCodeCamp"
   print(f"The best place to learn to code is with {coding_website}!")

#call function
learn_to_code()

#access variable from within the function
print(coding_website)

#output

#The best place to learn to code is with freeCodeCamp!
#freeCodeCamp
```

## Conclusion

And there you have it! You now know the basics of global variables in Python and can tell the differences between local and global variables.

I hope you found this article useful.

To learn more about the Python programming language, check out freeCodeCamp's [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

You'll start from the basics and learn in an interactive and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you've learned.

Thanks for reading and happy coding!


