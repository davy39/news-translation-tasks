---
title: Python Fundamentals for Data Science
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-07-15T00:05:23.000Z'
originalURL: https://freecodecamp.org/news/python-fundamentals-for-data-science
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/1_5YaueU4meqq-bCM8y3OlkQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: null
seo_desc: 'Beginners in the field of data science who are not familiar with programming
  often have a hard time figuring out where they should start.

  With hundreds of questions about how to get started with Python for DS on various
  forums, this post (and video s...'
---

Beginners in the field of data science who are not familiar with programming often have a hard time figuring out where they should start.

With hundreds of questions about how to get started with [Python for DS](https://github.com/dswh/python_fundamentals) on various forums, this post (and video series) is my attempt to settle all those questions.

I'm a Python evangelist that started off as a Full Stack Python Developer before moving on to data engineering and then data science. My prior experience with Python and a decent grasp of math helped make the switch to data science more comfortable for me.

So, here are the fundamentals to help you with programming in Python.

Before we take a deep dive into the essentials, make sure that you have [set up your Python environment](https://youtu.be/t8AUwTDtno8) and know how to use a [Jupyter Notebook (optional).](https://www.youtube.com/watch?v=TmDUZfkdZoo&list=PLIkXejH7XPT_y00hj-mB-zTzePsMu2gRb&index=3&t=0s)

A basic Python curriculum can be broken down into 4 essential topics that include:

1. Data types (int, float, strings)
    
2. Compound data structures (lists, tuples, and dictionaries)
    
3. Conditionals, loops, and functions
    
4. Object-oriented programming and using external libraries
    

Let's go over each one and see what are the fundamentals you should learn.

## 1\. Data Types and Structures

The very first step is to understand how Python interprets data.

Starting with widely used data types, you should be familiar with integers (int), floats (float), strings (str), and booleans (bool). Here's what you should practice.

### Type, typecasting, and I/O functions:

* Learning the type of data using the `type()` method.
    

```py
type('Harshit')

# output: str
```

* Storing values into variables and input-output functions (`a = 5.67`)
    
* Typecasting — converting a particular type of variable/data into another type if possible. For example, converting a string of integers into an integer:
    

```py
astring = "55"
print(type(astring))

# output: <class 'str'>
```

```py
astring = int(astring)
print(type(astring))

# output: <class 'int64'>
```

But if you try to convert an alphanumeric or alphabet string into an integer, it will throw an error:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/2.png align="left")

Once you are familiar with the basic data types and their usage, you should learn about **arithmetic operators and expression evaluations** **(DMAS)** and how you can store the result in a variable for further use.

```py
answer = 43 + 56 / 14 - 9 * 2
print(answer)

# output: 29.0
```

### Strings:

Knowing how to deal with textual data and their operators comes in handy when dealing with the string data type. Practice these concepts:

* Concatenating strings using `+`
    
* Splitting and joining the string using the `split()` and `join()`method
    
* Changing the case of the string using `lower()` and `upper()` methods
    
* Working with substrings of a string
    

Here’s [the Notebook](https://github.com/dswh/python_fundamentals/blob/master/Notebooks/python_fundamentals_part-1.ipynb) that covers all the points discussed.

## 2\. Compound data structures (lists, tuples, and dictionaries)

### Lists and tuples (compound data types):

One of the most commonly used and important data structures in Python are lists. A list is a collection of elements, and the collection can be of the same or varied data types.

Understanding lists will eventually pave the way for computing algebraic equations and statistical models on your array of data.

Here are the concepts you should be familiar with:

* How multiple data types can be stored in a Python list.
    
* **Indexing and slicing** to access a specific element or sub-list of the list.
    
* Helper methods for **sorting, reversing, deleting elements, copying, and appending**.
    
* Nested lists — lists containing lists. For example, `[1,2,3, [10,11]]`.
    
* Addition in a list.
    

```py
alist + alist

# output: ['harshit', 2, 5.5, 10, [1, 2, 3], 'harshit', 2, 5.5, 10, [1, 2, 3]]
```

Multiplying the list with a scalar:

```py
alist * 2

# output: ['harshit', 2, 5.5, 10, [1, 2, 3], 'harshit', 2, 5.5, 10, [1, 2, 3]]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/5.png align="left")

**Tuples** are an immutable ordered sequence of items. They are similar to lists, but the **key difference is that** tuples **are immutable whereas lists are mutable.**

Concepts to focus on:

* Indexing and slicing (similar to lists).
    
* Nested tuples.
    
* Adding tuples and helper methods like `count()` and `index()`.
    

### Dictionaries

These are another type of collection in Python. While lists are integer indexed, dictionaries are more like addresses. Dictionaries have key-value pairs, and keys are analogous to indexes in lists.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/6.png align="left")

To access an element, you need to pass the key in squared brackets.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/7.png align="left")

Concepts to focus on:

* Iterating through a dictionary (also covered in loops).
    
* Using helper methods like `get()`, `pop()`, `items()`, `keys()`, `update()`, and so on.
    

Notebook for the above topics can be found [here](https://github.com/dswh/python_fundamentals/blob/master/Notebooks/python_fundamentals_part-2.ipynb).

## 3\. Conditionals, Loops, and Functions

### Conditions and Branching

Python uses these boolean variables to assess conditions. Whenever there is a comparison or evaluation, boolean values are the resulting solution.

```py
x = True

ptint(type(x))

# output: <class bool>
```

```py
print(1 == 2)

# output: False
```

The comparison in the image needs to be observed carefully as people confuse the assignment operator (`=`) with the comparison operator (`==`).

### Boolean operators (or, and, not)

These are used to evaluate complex assertions together.

* `or` — One of the many comparisons should be true for the entire condition to be true.
    
* `and` — All of the comparisons should be true for the entire condition to be true.
    
* `not` — Checks for the opposite of the comparison specified.
    

![Image](https://www.freecodecamp.org/news/content/images/2020/07/9.png align="left")

```py
score = 76
percentile = 83

if score > 75 or percentile > 90:
    print("Admission successful!")
else:
    print("Try again next year")
    
# output: Try again next year
```

Concepts to learn:

* `if`, `else`, and `elif` statements to construct your condition.
    
* Making complex comparisons in one condition.
    
* Keeping indentation in mind while writing nested `if` / `else` statements.
    
* Using boolean, `in`, `is`, and `not` operators.
    

### Loops

Often you'll need to do a repetitive task, and loops will be your best friend to eliminate the overhead of code redundancy. You’ll often need to iterate through each element of a list or dictionary, and loops come in handy for that. `while` and `for` are two types of loops.

Focus on:

* The `range()` function and iterating through a sequence using `for` loops.
    
* `while` loops
    

```py
age = [12,43,45,10]
i = 0
while i < len(age):
    if age[i] >= 18:
        print("Adult")
    else:
        print("Juvenile")
    i += 1

# output: 
# Juvenile
# Adult
# Adult
# Juvenile
```

* Iterating through lists and appending (or any other task with list items) elements in a particular order
    

```py
cubes = []
for i in range(1,10):
    cubes.append(i ** 3)
print(cubes)

#output: [1, 8, 27, 64, 125, 216, 343, 512, 729]
```

* Using `break`, `pass`, and `continue` keywords.
    

### List Comprehension

A sophisticated and succinct way of creating a list using and iterable followed by a `for` clause.

For example, you can create a list of 9 cubes as shown in the example above using list comprehension.

```py
# list comprehension
cubes = [n** 3 for n in range(1,10)]
print(cubes)

# output: [1, 8, 27, 64, 125, 216, 343, 512, 729]
```

### Functions

While working on a big project, maintaining code becomes a real chore. If your code performs similar tasks many times, a convenient way to manage your code is by using functions.

A function is a block of code that performs some operations on input data and gives you the desired output.

Using functions makes the code more readable, reduces redundancy, makes the code reusable, and saves time.

Python uses indentation to create blocks of code. This is an example of a function:

```py
def add_two_numbers(a, b):
    sum = a + b
    return sum
```

We define a function using the `def` keyword followed by the name of the function and arguments (input) within the parentheses, followed by a colon.

The body of the function is the indented code block, and the output is returned with the `return` keyword.

You call a function by specifying the name and passing the arguments within the parentheses as per the definition.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/14.png align="left")

More examples and details [here](https://github.com/dswh/python_fundamentals/blob/master/Notebooks/python_fundamentals_part-2.ipynb).

## 4\. Object-Oriented programming and using external libraries

We have been using the helper methods for lists, dictionaries, and other data types, but where are these coming from?

When we say list or dict, we are actually interacting with a list class object or a dict class object. Printing the type of a *dictionary object* will show you that it is a class dict object.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/15.png align="left")

These are all pre-defined classes in the Python language, and they make our tasks very easy and convenient.

Objects are instance of a class and are defined as an encapsulation of variables (data) and functions into a single entity. They have access to the variables (attributes) and methods (functions) from classes.

Now the question is, can we create our own custom classes and objects? The answer is YES.

Here is how you define a class and an object of it:

```py
class Rectangle:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        area = self.height * self.width
        return area

rect1 = Rectangle(12, 10)

print(type(rect1))

# output: <class '__main__.Rectangle'>
```

You can then access the attributes and methods using the dot(.) operator.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/17.png align="left")

### Using External Libraries/Modules

One of the main reasons to use Python for data science is the amazing community that develops high-quality packages for different domains and problems. Using external libraries and modules is an integral part of working on projects in Python.

These libraries and modules have defined classes, attributes, and methods that we can use to accomplish our tasks. For example, the `math` library contains many mathematical functions that we can use to carry out our calculations. The libraries are `.py` files.

You should learn to:

* Import libraries in your workspace
    

![Image](https://www.freecodecamp.org/news/content/images/2020/07/18.png align="left")

* Using the `help` function to learn about a library or function
    

![Image](https://www.freecodecamp.org/news/content/images/2020/07/19.png align="left")

* Importing the required function directly.
    

![Image](https://www.freecodecamp.org/news/content/images/2020/07/20.png align="left")

* How to read the documentation of the well-known packages like pandas, numpy, and sklearn and use them in your projects
    

## Wrap up

That should cover the fundamentals of Python and get you started with data science.

There are a few other features, functionalities, and data types that you’ll become familiar with over time as you work on more and more projects.

You can go through these concepts in GitHub repo where you’ll find the **exercise** **notebooks as well**:

%[https://github.com/dswh/python_fundamentals] 

Here is 3-part video series based on this post for you to follow along with:

%[https://youtu.be/TLLHJC79rDU] 

## Data Science with Harshit

%[https://youtu.be/yapSsspJzAw] 

You can connect with me on [LinkedIn](https://www.linkedin.com/in/tyagiharshit/), [Twitter](https://twitter.com/tyagi_harshit24), [Instagram](https://www.instagram.com/upgradewithharshit/?hl=en), and check out my [YouTube channel](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) for more in-depth tutorials and interviews.

If this tutorial was helpful, you should check out my data science and machine learning courses on [Wiplane Academy](https://www.wiplane.com/). They are comprehensive yet compact and helps you build a solid foundation of work to showcase.
