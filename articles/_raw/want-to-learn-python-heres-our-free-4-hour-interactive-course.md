---
title: Want to learn Python? Here's our free 4-hour interactive course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-03T13:06:34.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-python-heres-our-free-4-hour-interactive-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/gpython.jpg
tags:
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Per Harald Borgen

  Python is a popular, versatile and easy-to-learn language. It''s the go-to language
  for AI, Machine Learning and Data Science. Some say it''s also the easiest programming
  language to get started with.

  If this sounds like a programm...'
---

By Per Harald Borgen

Python is a popular, versatile and easy-to-learn language. It's the go-to language for AI, Machine Learning and Data Science. Some say it's also the easiest programming language to get started with.

If this sounds like a programming language you want to learn, keep reading! Over the next few paragraphs, I'll guide you through [the free 4-hour interactive Python course](https://scrimba.com/g/gpython?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) that we launched today. 

%[https://twitter.com/scrimba/status/1234834344461643778]

This course aims to give you a solid foundation in both Python and basic programming in general. It's great for beginners looking for an interactive and engaging way to learn to code.

The course has been created by our brilliant teacher [Olof Paulson](https://twitter.com/OlofPaulson), who's one of the advocates for the Khan Academy in Swedish. Olof has a background in finance, is experienced in writing algorithms, and has a passion for open and accessible education.

Now let's have a look at how the course is laid out!

## 1. Course Introduction

This course covers all the topics you need to go from a beginner to an intermediate Python developer. It goes through:

* Outputting data and program flow
* Strings, Variables
* Arithmetic operations and comparisons
* Lists, Tuples, Sets and Dictionaries
* Conditionals, if and elifs
* While and for loops
* Functions / Return Statements
* Objects, Classes and Inheritance
* List / Dictionary Comprehensions and Lambda functions
* Modules

## 2. Running Python on Scrimba with Brython

To get a back-end language like Python to run on a front-end platform like Scrimba, we use the Brython plugin in the `index.html` file to recompile Python code into Javascript.

Generally, we'll be using the minimum JS (`brython.min.js`) version but for more functionality, simply uncomment the standard lib version (`brython_stdlib.js`).

```html
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.8.0/brython.min.js"></script>
	<!--<script type="text/javascript"
     src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.8.0/brython_stdlib.js"></script>-->
</head>

```

It's also worth noting a few Brython oddities in Scrimba:

1. The `input()` box is the JS prompt and not seen in the cast but works when you run local code.
2. The Scrimba minibrowser sometimes hovers in the corner during some tutorials - you don't have to worry about it.

## 3. Print Statement and Programflow

When we write Python, we often want to test that it is working as expected. To do this, we use the `print()` command to output data to the console.

```python
print('Welcome to Python 101!')

```

**Note:** The computer reads code from top to bottom, so it runs commands nearer the top first.

## 4. Variables

Variables are used to save data for use later on. We declare variables using their name in lower case followed by the basic assignment operator (`=`). Note that if the variable name consists of more than one word, they should be separated with an underscore (`_`).

```python
failed_subjects="6"

```

We use variables in our code by preceding them with a plus sign (`+`).

```python
print('Your son Eric is failing' + failed_subjects + ' subjects.')

```

## 5. Datatypes & Typecasting

The basic datatypes of Python are:

* **Strings** - these surrounded by two quotation marks (can be double or single quotes).
* **Integers** - these are whole numbers.
* **Floats** - numbers with decimal points.
* **Booleans** - these take on the value `true` or `false`.

To find out which data type you are using, use `type()`

```python
print(type('hello'))

```

**Note:** If you want to use quotes or an apostrophe in a string, surround the entire string with double quotes. Alternatively, you can use Python's escape character, which is the backslash (`\`)

```python
a="it's"
b='it\'s'

```

There are rules around mixing data types, for example you can't put numbers inside a string. `Typecasting`, or changing the type, resolves this.

* `str()` changes data to a string.
* `int()` changes data to an integer.
* `float()` changes data to a float.

```python
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')

```

## 6. Variables & Datatypes - Exercise

It's time for your very first Scrimba Python challenge! In this cast, you can put your new-found knowledge of variables and datatypes to the test. Try to solve the challenge by yourself, and then [check out Olof's solution](https://scrimba.com/p/pNpZMAB/cZPZ6wSb?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to see whether you're on the right track.

## 7. Arithmetic Operations

Here, we learn that the basic arithmetic operations in Python are addition, subtraction, multiplication, float division (which returns a floating point number), floor division (which rounds the result down to the nearest integer), modulus (which returns the remainder of the calculation) and exponent (which multiplies a number the to power of another number).

```python
a=10
b=3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

```

## 8. Strings - Basics / Slicing

In this cast, we learn about some of the basic concepts when it comes to using strings.

* Multiplying strings allows us to print a string multiple times. There are three ways of doing this (the final one inserts a space between strings):

```python
print(msg+msg)
print(msg*2)
print(msg,msg)

```

We can change the case of the strings in a number of ways:

* `upper()` changes the string to upper case.
* `lower()` changes the string to lower case.
* `capitalize()` capitalizes a string's first word.
* `title()` capitalizes every word in a string.

```python
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())

```

We can use the following functions to find out information about a string:

* `print(len(msg))` tells us how many characters the string has (in this case, `msg`).
* `print(msg.count('Python'))` counts the number of instances of a word or letter - note that this is case sensitive.

We access strings with square brackets (`[]`).

```
print(msg[0])

```

**Note:** Python strings are 0-indexed, i.e. the first character is counted as 0 and not 1. Using negative indexes starts the count from the end of the string.

Returning parts of a string is known as _slicing_. Olof shows us how to slice with some examples:

* `print(msg[a:])` returns everything after the character in the position specified.
* `print(msg[a:b])` returns everything between the positions specified, not including the end position.
* `print(msg[:b])` returns everything until the position specified, again, not including the end position.

## 9. Exercise - Strings - Basics / Slicing

It's time for an exercise on strings. As well as allowing us to practice the skills we've learned in previous casts, this challenge also gets us thinking about a skill Olof hasn't explicitly told us:

![Python 101 scope](https://dev-to-uploads.s3.amazonaws.com/i/jvrzvgqn5zmn0fx82b87.png)

  
_Click the image to access the challenge._

This is a great intro to life as a bona fide programmer - don't forget that Google is your friend! Check out the [rest of the cast](https://scrimba.com/p/pNpZMAB/c8rPnyCa?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to see how Olof did it.

## 10. Strings -2 Find/replace, String Formatting

This cast teaches us even more about working with strings.

* We can create multi-line strings with triple quotes:

```python
msg="""Dear Terry,,
You must cut down the mightiest
tree in the forest with…
a herring! <3"""

```

Olof runs us through some examples of working with strings:

`print(msg.find('Python'))` returns the position of the words or characters we search for (in this case, 'Python').

`print(msg.replace('Python','Java'))` allows us to replace words or characters in a string. Note that strings are immutable in Python, so to use the result of this function, you need to save it to a variable.

```python
msg1=msg.replace('Python','C')

```

`print('Python' in msg)` tells us whether a word or character exists in a string by returning `true` or `false`.

`msg1 = f'[{name}] loves the color {color}!'` allows us to format strings so that they are more readable.

## 11. User Input

In Python, we capture user input and print it like this:

```python
name= input('What is your name?: ')
print(name)

```

This brings up a user input field which looks like this:

![User input field in Python](https://dev-to-uploads.s3.amazonaws.com/i/rgz3kqhih93de1z2vk08.png)

## 12. User Input - Exercise

It's time to flex our programming muscles with a user input exercise! In this cast, you'll be building a distance converter using the hints below:

![User inputs challenge hints](https://dev-to-uploads.s3.amazonaws.com/i/hkdtyr6irt83v1vjd9m6.png)

  
_Click the image to access the challenge._

As usual, give the challenge a go on your own and then check [Olof's solution](https://scrimba.com/p/pNpZMAB/ceMDmvTB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to see whether you got it right.

## 13. Lists - Basics

Whereas a variable holds one piece of data, a list holds multiples pieces.

```py
friends = ['John','Michael','Terry','Eric','Graham']

```

Lists are also zero-indexed, and can be accessed with square brackets, just like strings:

```py
print(friends[1])

```

We can also use the same commands we used with strings to find out a string's length, find certain data within a string, etc.

```py
print(friends[1],friends[4])
print(len(friends))
print(friends.coun('Eric'))

```

## 14. Lists - continued

This cast takes us through a few essential skills for using lists, such as sorting (`sort()`), finding the sum, (`print(sum()`), appending new data (`append('')`), adding two lists together (`.extend()`), removing items (`.remove('')`), popping items (which removes an item but still allows you to return it) (`.pop()`), and clearing the list (`.clear()`).

## 15. Lists - Exercise

In this exercise, we will be having a go at manipulating lists.

![Description of the challenge](https://dev-to-uploads.s3.amazonaws.com/i/1nyb5f534aqwugnws457.png)

  
_Click the image to check out the solution._

Give it a go by yourself and then [check out Olof's solution](https://scrimba.com/p/pNpZMAB/cLpzgpSy?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to check how it went.

## 16. Split and Join

This cast looks at splitting and joining parts of strings.

```py
print(msg.split())
print('-'.join(friends_list))

```

## 17. Split and Join - Exercise

Here you'll use what you now know about splitting and joining to create a list of friends from a string.

As usual, have a go on your own and then [check out Olof's solution](https://scrimba.com/p/pNpZMAB/cJp2gEcW?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to check your work.

## 18. Tuples

Tuples are lists that you can't change. They look the same as lists but are surrounded by parentheses instead of square brackets.

```py
friends_tuple = ('John','Michael','Terry','Eric','Graham')

```

You should use tuples instead of lists when you want to make sure that your data won't change in the course of your program running.

## 19. Sets

Sets are similar to lists and tuples but they're unordered and remove duplicates inside themselves. They are also very fast. Sets are surrounded by curly brackets.

```py
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

```

In this cast, Olof takes us through some tips and tricks for using lists. **Note:** Creating an empty set works differently than creating an empty list or tuple:

```py
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()

```

## 20. Sets - Exercise

Here, we'll put our new-found knowledge of sets to the test. Take a look at the [end of the cast](https://scrimba.com/p/pNpZMAB/caqBRLsW?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to check your answer.

## 21. Comments

Comments are text in the code that Python ignores. They are mainly used for human-human communication, e.g. notes about the code, debugging or testing, and code documentation. Comments are preceded by the pound sign (`#`):

```py
#Hiding in the comments

```

## 22. Functions - Calling, Parameters, Arguments, Defaults

In this cast, Olof introduces us to functions - bundles of code which we can reuse later.

Functions are created (defined) with `def` and called with the function name plus parentheses `()`:

```py
def greeting():
    print("Hello Friend!")

greeting()

```

We also take another look at formatted strings, and how using them makes code more readable and more efficient.

```py
def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

```

## 23. Functions - Exercise

Here, Olof gives us the task of modifying and extending the functionality of an existing function. Give it a shot and then watch [the rest of the cast](https://scrimba.com/p/pNpZMAB/c67dzEAV?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to see if you're on the right track.

## 24. Functions - Named Notation

Named notation is the practice of naming arguments when calling a function so that the function definition understands which argument is which, even if they appear in a different order.

```py
Profile(yob=1995,weight=83.5,height=192,eye_color="blue")

```

## 25. Return statements

This cast takes us through return statements. A return statement allows us to get back our data after performing a function.

```py
def value_added_tax(amount):
    tax = amount * 0.25
    return tax

```

Olof also takes us through a few handy ways of playing with our returned data, including creating strings, sets and tuples with it.

## 26. Comparisons and Booleans

This tutorial whizzes through some ways of comparing data, including equals (`==`), is not equal (`!=`), greater than (`>`), greater than or equal to (`>=`), less than (`<`), less than or equal to (`<=`), in (`in`), not in (`not in`), is (`is`) and is not (`is not`).

We also take a look at some Boolean properties and learn that `false` evaluates to 0 and `true` evaluates to 1. Empty objects and zeroes evaluate to false and everything else (strings, numbers except 0, and so on) evaluates to true.

## 27. Conditionals: If, Else, Elif

Conditionals allow us to run different code for different circumstances. `if` statements run if the function returns true, `elif` (else if) statements run if the functions returns true after another statement has returned false, and `else` statements run if none of the preceding statements have returned true, i.e. in all other eventualities.

```py
is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")

```

## 28. If/Elif/Else - Exercise

It's time to flex our conditional muscles with an exercise. We also get the chance to have a go at some extended functionality with a temperature converter.

As usual, go ahead and see if you can solve it yourself and check your answer against [Olof's solution](https://scrimba.com/p/pNpZMAB/c2PWdWCN?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

## 29. Conditionals - Exercise Improve

The cast gives us the chance to try out some optimization by shortening code and reducing the number of conditionals it contains. 

There are many different ways of achieving this, so have a go on your own and then compare your answer to how Olof tackles it at the [end of the cast](https://scrimba.com/p/pNpZMAB/cPJDRNcr?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

## 30. While Loops

While loops are code which runs repeatedly until a condition tells it to stop. To create a loop, begin by asking yourself these questions:

What do I want to repeat?

What do I want to change each time?

How long should we repeat?

In the below example, we want to repeat adding one, we want to change `i`, and we want this to repeat until the number five is reached:

```py
i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)

```

## 31. While Loops - Exercise

It's time for an exercise on loops. In this challenge, we'll make a fun guessing game. Don't forget to consider the three loop questions in the previous chapter before you start, and then check the solution at the [end of the cast](https://scrimba.com/p/pNpZMAB/cV8WmMcM?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to see how it went.

## 32. For Loops and Nesting

For loops allow us to execute a statement for each item in a string, list, tuple or set. For example, the following code prints every number between two and eight:

```py
for number in range(2,8):
    print(number)

```

It is also possible to nest loops inside other loops. The code below prints each of the numbers 1, 2 and 3 for every friend (John 1, John 2, John 3, Terry 1, Terry 2, Terry 3, etc.)

```py
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

```

In this cast, we also learn about a couple for handy for loop keywords, such as `break` and `continue`.

## 33. For loops - Exercise

It's time to test out what we have learned about for loops with an exercise. This time, we'll be making personalized party invitations. We also have a mini-challenge of including proper capitalization

![for loops exercise description](https://dev-to-uploads.s3.amazonaws.com/i/f8sfknbcdahv4r3s75zv.png)

  
_Click the image to access the challenge._

As usual, see how it goes on your own and then [check the solution](https://scrimba.com/p/pNpZMAB/czkEGktv?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) to compare your answer.

## 34. Dictionaries

This cast introduces us to dictionaries. Dictionaries are used in Python to store key-value pairs, and they work in a similar way to a physical dictionary. You look up a word (the key) and get a definition or translation (the value) in return.

```py
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

```

Olof also runs us through how to change entries in a dictionary and add new ones, as well as how to handle the error message caused by users looking up entries which don't exist and how to run for loops over dictionary data.

```py
for key, value in movie.items():
    print(key, value)

```

## 35. Sort() and Sorted()

Here, we learn about the difference between `sort()` and `sorted()`. While both functions sort the contents of a list, only `sorted()` returns the results.

We also look at the behavior of dictionaries, tuples and strings when they are sorted and see a brief introduction to _lambda functions_ - one-line convenient throwaway functions, which we will see more on in a later tutorial. The lambda example below sorts the list according to the first entries:

```py
my_list=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key = lambda item :item[0]))

```

## 36. Exceptions: Try/Except, Raise

In this cast, Olof takes us through some techniques for handling errors. We do this with `try-except` blocks, which look like this:

```py
#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed

```

## 37. Classes and Objects

Next up, Olof shows us classes and objects. There are four main concepts to understand when it comes to classes. These are classes, objects, attributes and methods.

Classes are blueprints which show us the structure of the data required. Objects contain the actual data we use. Attributes are variables within a class and methods are functions within a class.

We initialize a class with the initialization statement `init`:

```py
class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

```

**Note:** By convention, we use the `self` keyword when naming attributes.

Having done this, we can now create instances of the class, as below:

```py
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

```

Methods are defined in classes as follows:

```py
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)

```

There are two ways of calling methods (the output is the same):

```py
film_2.nice_print()
Movie.nice_print(film_2)

```

## 38. Inheritance

In this cast, Olof shows us around the concept of inheritance. Inheritance allows us to use the methods from one class in another class without repeating all the code. We can then add further methods to differentiate the classes from each other.

```py
class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")
class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")

```

A class can inherit from multiple other classes. If the classes have different outputs for the same method, the class will choose the inherited method which is declared first. 

In the example below, the Wizard class will inherit any shared methods from the Doctor and not the Fighter.

```py
class Wizard(Doctor,Fighter):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heals 15 health points")

```

## 39. Modules

Now it's time to look at modules. Modules are code snippets which you can import and use in the code. Some commonly-used ones provided by Python are `datetime`, `random`, `string`, `os`, `math`, `browser` and `platform`

To use modules, we first need to import Brython's standard lib version:

```html
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.7.0/brython.min.js"></script>
	<script
		type="text/javascript"
		src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.7.0/brython_stdlib.js"
	></script>
	-->
</head>

```

Modules are imported with the `import` keyword and can be given an easier-to-use alias with `as`:

```py
import platform as pl

print(pl.python_version())

```

## 40. Zip / Unzip

In this cast, Olof shows us how to zip and unzip objects. Zipping allows us to combine two or more iterable objects (strings, tuples, lists, etc.).

```py
nums = [1,2,3,4]
letters = ['a','b','c','d']
combo = list(zip(nums,letters))
print(combo)

```

The example above turns the combined iterables into a list, but we could also turn it into a tuple, set or dictionary. **Note:** A dictionary is unsuitable when zipping more than two objects.

Unzipping allows us to assign results into separate variables, in this case `num`, `let` and `nam`.

```py
num,let,nam =zip(*combo)

```

## 41 Lambda Functions part 1

Here, we take a closer look at lambdas, or anonymous functions, which allow you to write single-line, throwaway function definitions which you might just use once. Compare the following:

**Standard function:**

```py
def square(x):
    return x*x
print(square(3))

```

**Lambda:**

```py
square1 = lambda x: x*x

```

**Note:** The return value in a lambda is implicit.

## 42. Lambda Functions Part 2

In this cast, we delve a little deeper into lambdas. Although we could always replicate a lambda with a standard function, there are some instances when lambdas are significantly better.

In this example, the return value of the lambda is a function, which gives us the ability to reuse the lambda for multiple different tasks. In the code below, we use a single lambda to multiply by two and five:

```py
def func(n):
    return lambda a: a*n
# a*2
doubler = func(2)
print(doubler(3))
quintipler = func(5)
print(quintipler(3))
print(type(func(3)))

```

This cast also explains that we can call lambdas as soon as we create them.

```py
print((lambda a,b,c: a+b+c)(2,3,4))

```

## 43 Lambda Functions - Exercise

Now it's time to practice creating a few of our own lambdas.

See how you get on and check your answers against [Olof's solutions](https://scrimba.com/p/pNpZMAB/cKpNKbuQ?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) as you go along.

## 44. Comprehensions - Lists

Python comprehensions allow us to create lists, tuples, sets and dictionaries with less code. **Note:** Anything which can be created in a comprehension can also be created with a for loop, however the for loop requires more code.

Olof also provides a handy slide to give as a visual comparison of for loops and comprehensions in two different cases.

![comparison of for loops and comprehensions](https://dev-to-uploads.s3.amazonaws.com/i/ifdzdxg0tux7n3u9llrq.png)

  
_Click the slide to access the cast._

## 45. Comprehensions - Dictionary

Olof now shows us how to create a new dictionary using a comprehension. Were we to do this with a for loop, the code would look like this:

```py
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

```

With a comparison, it looks like this:

```py
new_dict = {movie:yr for movie,yr in zip(movies,year)}
print(new_dict)

```

Much more concise and readable!

## 46. Randomness

This cast takes us through the `random` module and teaches us how to generate pseudo-random events. To use the module, we first import it:

```py
import random

```

We can then use the module to generate pseudo-random numbers:

```py
for i in range(5):
    print(random.random()*6)

```

Olof also shows us a variety of functions we can use with `random`.

Use of `random` is not limited to numbers though. We can also use it with iterables:

```py
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))

```

Lastly, Olof shows us the `string` modules and we learn how to create pseudo-random words.

```py
import random, string

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
word = ''
for i in range(7):
    word += random.choice(letters_numbers)
word1 = ''.join(random.sample(letters_numbers,7))
word = random.choices(letter_numbers, k=7)
print(word)
print(word1)

```

**Note:** These words are not truly random and should therefore not be used to generate passwords.

## 47. Project - Crypto machine

Now we are nearing the end of the course, Olof gives us a big project to sink our teeth into. Take a look at the instructions, follow along and attempt to do each step on your own, before checking [Olof's solution](https://scrimba.com/p/pNpZMAB/cEK2WJtd?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

## 48. Project - Math Tutor

Our second project is to create a Math tutor which tutors us in multiplication tables. Take a look at the instructions below, have a go at the project and then check out [how Olof does it](https://scrimba.com/p/pNpZMAB/cdNBZVh9?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article).

![Math Tutor project instructions](https://dev-to-uploads.s3.amazonaws.com/i/i4tlk2xmd7rymmap0q3r.png)

  
_Click the image to access the challenge._

## 49. Course Summary

Congratulations on making it to the end of the Python 101 course! We have been over outputting data and program flow, strings, variables, arithmetic operations, comparisons, lists, tuples, sets, dictionaries conditionals, loops, functions, objects, classes, inheritance, comprehensions, lambdas and modules - so you should be proud of yourself!

![Congratulations!](https://dev-to-uploads.s3.amazonaws.com/i/lzhvvngzvjy9fjvk1bjd.png)

Don't forget you can always [refer back to the course](https://scrimba.com/g/gpython?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gpython_launch_article) if you need to, or redo any exercises you felt unsure of them (or just particularly enjoyed!)

When you're ready to move on, [Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=gpython_launch_article) has a range of courses to teach you your next coding skill, so check them out!

![go get it](https://dev-to-uploads.s3.amazonaws.com/i/p3okn1zuv00xn11kge2x.png)

  
_Click the image to see Scrimba's range of courses_

Happy coding! :)

%[https://www.youtube.com/watch?v=ECW8t3Djfsg]


