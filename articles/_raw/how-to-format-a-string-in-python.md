---
title: How to Format a String in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T17:19:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/How-To-Format-A-String-in-python.jpg
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: "By Suchin Ravi\nFormatting a string is something you'll do all the time\
  \ when you're coding in Python. For every variable, tuple, and dictionary and the\
  \ logic that we define, we eventually have to either print or display it in some\
  \ form. \nAnd each of t..."
---

By Suchin Ravi

Formatting a string is something you'll do all the time when you're coding in Python. For every variable, tuple, and dictionary and the logic that we define, we eventually have to either print or display it in some form. 

And each of these, without exception, require us to format the required output into a string before we can finally print it or use the relevant function to display the string in Python. 

You may have already used the `str` function and worked with string literals, but there many times when we need something more. With this in mind, let's look at how we can format strings using different Python3 techniques.

# How to Format a String Using Concatenation: print(‘Hello’+name)

This is the simplest – and thus the easiest – technique to get started with. It is also the way I prefer to teach someone who has just started coding. 

Using the portions in the literal order and the ‘+’ operators make it easy to grasp without any prior knowledge of coding. 

```python
name = 'YoungWonks'
year = 2014

string = 'Hello, ' + name
print(string)

string = name + ' was started in ' + str(year)
print(string)
```

This is the result:

```bash
Hello, YoungWonks 
YoungWonks was started in 2014
```

The above example demonstrates how we can join variables using the addition operator to create a formatted string. The thing to keep in mind here is that we will need to convert all the variables to strings. Here, the variable name is a string already and year is an integer. 

# How to Format a String the Old Way: print ‘Hello %s’ % name

This approach was more often used in Python2, when the language was still young and evolving. It's a technique that is easy to understand for veteran coders who come from a C programming background. 

Here, as you can see in the code below, we're defining the placeholder with the type of data specified and the argument(s) at the end of the statement. This resembles the C language (and other languages too).

```python
name = 'YoungWonks'
year = 2014

string = 'Hello, %s ' % name
print(string)

string = '%s was started in %d' % (name, year)
print(string)
```

And here's the result:

```bash
Hello, YoungWonks 
YoungWonks was started in 2014
```

In the above example, we define the variables that we want to format into the strings. Then we create the string with the placeholders for the variables. 

Bear in mind that the placeholders should match the types of the corresponding variables. We can link the actual variables to the placeholders using the % symbol at the end of the statement.

# How to Format a String using Format: ‘’.format()

This is a technique that many Python programmers consider a breath of fresh air, since it makes things easier for you. 

It was introduced in early Python3. Essentially, the new syntax removed the ‘%’ symbols and instead provided `.format()` as a string method, which accepts positional arguments for substitutions described in the curly braces. 

We can also specify keyword arguments here, although this does feel a little verbose at times.  
  
There is more that you can do with the `str.format` method, such as specifying precision, rounding, and zero padding. For the purposes of this article, we will only focus on the basic usage. 

```python
name = 'YoungWonks'
year = 2014

string = '{} was started in {}'.format(name, year)
print(string)

string = '{0} was started in {1}'.format(name, year)
print(string)

yw = {'name': 'YoungWonks', 'year': 2014}
string = "{name} was started in {year}.".format(name=yw['name'], year=yw['year'])
print(string)
```

Here's the result:

```bash
YoungWonks was started in 2014
YoungWonks was started in 2014
YoungWonks was started in 2014
```

In the above example, we create the variables to be formatted into the string. Then, in the simples form, we can use {} as placeholders for the variables to be used. We then apply the `.format()` method to the string and specify the variables as an ordered set of parameters. 

The second part of the example uses indices of the ordered parameters in the placeholders. 

The third part of the example also shows us how to use a dictionary in the formatting of the string while also using named parameters in the .format method.

# How to Format a String using F Strings: f'hello {name}'

Also short for format string, f strings are the most recent technique that Python3 now supports so they're being adopted rapidly. 

F strings addresses the verbosity of the `.format()` technique and provide a short way to do the same by adding the letter f as a prefix to the string. This method seems to have the best of the two techniques:

1. The literal ordering of concatenation
2. The modularity of the `.format()` method

Because of these advantages, more and more developers seem to be using it. I think it also happens to be simpler for students to learn, and easier to adopt if you're still new to coding.

```python
name = 'YoungWonks'
year = 2014
string = f'{name} was started in {year}'
print(string)

string = f'{name} was started in {2013 + 1}.'
print(string)

yw = {'name': 'YoungWonks', 'year': 2014}
string = f"{yw['name']} was started in {yw['year']}."
print(string)
```

```bash
YoungWonks was started in 2014 
YoungWonks was started in 2014.
YoungWonks was started in 2014.
```

As you may have noticed, the above example is similar to the `.format()` method. Here we use the {} for placeholders in the strings but also specify the variables directly within the placeholder. 

This method takes effect when we use the lowercase letter `f` at the beginning of the string. You can also use method with other datatypes such as dictionaries.

# Do we need to know and use all these string formatting methods? 

All of this is relevant knowledge when you're learning Python. Even though you won't often use the old style of string formatting, there are some older forums, Stack Overflow posts, and many older Machine Learning libraries that still use these older styles. 

Because of this, it’s good to know them so you can recognize what's happening and potentially debug an issue.  
  
Of the other three methods we discussed here, you can use any of them to format your strings in Python. Just pick which one works best based on the context and even your mood that day!  
  
The `+` is useful when you're working with quick and simple statements. You can also use it to make debugging states while developing a simple project. 

For example, if we were to make a simple number guessing game then we could use the  `+` operator as shown below:

```python
import random
random_number = random.randint(1,100)
user_guess = None
while True:
	print('Please guess the number between 1 and 100 : ')
    user_guess = int(input())
    if user_guess == random_number:
    	print('Correct!')
    else:
    	print("Try Again!")
        
    #prints for debugging
    print("Random Number: "+ str(random_number))
    print("User Guess: "+ str(user_guess))
```

The debug statements used in the above code are not going to remain in your final code. (You wouldn't want to give away the number to be guessed, would you?) So you can use the concatenation approach in your prints while developing your code.

When you're adding logging statements, you may prefer the `.format()` or `f string` methods since they'll make your statements more modular. It will also be easier to specify precision/formatting for the data type itself.

# Are there any other string formatting techniques in Python?

Yes! Template strings are one such technique which are provided as a class within the string module of the Python standard library. It is imported as a module and the `.substitute()` method is used to replace placeholders. 

That being said, I have never had to use this in my coding experiences so far and only learned about it while doing research for this blog. 

# Conclusion 

Python string formatting is an important day-to-day tool for a Python programmer to know. Each coding language seems to format strings in a similar way. It is also a very important part of why we use scripting languages.

Of these different ways of formatting strings, it seems like the `f string` method is here to stay, along with `.format()` and concatenation. We may see the Python2 syntax fade away as most legacy libraries begin to support Python3.

Here is a [useful cheat sheet](https://www.youngwonks.com/resources/python-cheatsheet) that contains more basic Python syntax and also some string methods for your reference. 

# String Formatting in Other Languages

Other programming languages seem to follow similar syntax when it comes to precision and representation, and rely on variable substitutions. But they differ in how they output formatted strings to the console. 

C++ is the visible outlier here with the `cout` method from the standard library. Java, true to its nature, uses `System.out.println()`, while JavaScript uses `console.log()`. You will find a comparable method for each language out there.  
  
_Suchin Ravi is an educator & technologist, and teaches computer science at YoungWonks. He works as a lead software developer at Wonksknow LLC._ 

  
  



