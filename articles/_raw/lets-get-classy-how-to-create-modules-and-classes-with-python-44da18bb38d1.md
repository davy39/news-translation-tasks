---
title: 'Let’s get classy: how to create modules and classes with Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T20:47:24.000Z'
originalURL: https://freecodecamp.org/news/lets-get-classy-how-to-create-modules-and-classes-with-python-44da18bb38d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0PG2toS66TDJQQ7AtHGJ-Q.png
tags:
- name: class
  slug: class
- name: coding
  slug: coding
- name: modules
  slug: modules
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Hari Santanam

  In object-oriented computer languages such as Python, classes are basically a template
  to create your own objects. Objects are an encapsulation of variables and functions
  into a single entity. Objects get their variables and function...'
---

By Hari Santanam

In object-oriented computer languages such as Python, classes are basically a template to create your own objects. Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes.

Say what?

Here are some examples that will help you understand — read on. There is also an interactive code shell, simply press the “Run” button at the top of the specific window.

The simplest way to describe classes and how to use them is this:

Imagine you have great powers. You create a species (“class”).

Then you create attributes for that species (“properties”) — height, weight, limbs, color, powers, and so on.

Then you create an instance of that species — Fido the dog, Drogon from Game of Thrones, and so on. Then you work with these instances:

* In a game, for instance, they would engage in action, interact, using their attributes.
* In a banking app, they would be the different transactions.
* In a vehicle buy/sell/trade/lease app, the vehicle class could then spawn sub-classes such as cars. Each would have attributes such as mileage, options, features, color, and trim.

You can already see why this is useful. You are creating, re-using, adapting, and enhancing items in a very efficient, logical, and useful way.

By now, you have probably realized that this is a way to classify and group, one that that is similar to how humans learn:

* Animals are living things that are not human or trees, in a basic sense
* then you move on to different types of animals — dogs, cats are probably the first animals most of us learnt about
* then you move to different attributes of animals — shapes, sizes, sounds, appendages and so on.

For instance, when you were a child, your first understanding of a dog was probably something with four legs that barked. Then you learnt to distinguish that some were real dogs, others were toys. That this “dog” concept contained many types.

Creating and using classes is basically:

* building a template to put “things” in — a classification
* which can then be operated on. For example, pulling up all the people with dogs that you could request to link to a blog on pets, or all bank clients who might be good prospects for a new credit card.

The main point here is **classes** are objects that can produce instances of those templates, on which operations and methods can be applied. It is an excellent way to conceptualize, organize, and build a hierarchy for any organization or process.

As our world gets more complex, this is a way to mimic that complexity from a hierarchical perspective. It also builds a deeper understanding of the processes and interactions for business, technical, and social settings from a virtual information technology point.

An example might be a video game you create. Each character could be a “class”, with its own attributes, that interacts with instances of other classes. King George of the “King” class might interact with Court Jester Funnyman of the “Clown” class, and so on. A King might have a royal “servant” class, and a “servant” class would always have a “King” class, for example.

This is what we will do:

* create a class and use it
* create a module and move the class creation and initiation to the module
* call the module in a new program to use the class

The code is available in GitHub [here](https://github.com/HariSan1/class-module).

```
#TSB - Create Class in Python - rocket positions (x,y) and graph
```

```
#some items and comments bolded to call attention to processimport matplotlib.pyplot as plt
```

```
class Rocket():  def __init__(self, x=0, y=0):    #each rocket has (x,y) position; user or calling function has choice    #of passing in x and y values, or by default they are set at 0    self.x = x    self.y = y      def move_up(self):    self.y += 1      def move_down(self):    self.y -= 1      def move_right(self):    self.x += 1      def move_left(self):    self.x -= 1
```

```
#Make a series of rockets - x,y positions, I am calling it rocketrockets=[]rockets.append(Rocket())rockets.append(Rocket(0,2))rockets.append(Rocket(1,4))rockets.append(Rocket(2,6))rockets.append(Rocket(3,7))rockets.append(Rocket(5,9))rockets.append(Rocket(8, 15))  #Show on a graph where each rocket is
```

```
for index, rocket in enumerate(rockets):  #original position of rockets  print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))  plt.plot(rocket.x, rocket.y, 'ro', linewidth=2, linestyle='dashed', markersize=12)  #move the 'rocket' one up  rocket.move_up()  print("New Rocket position %d is at (%d, %d)." % (index, rocket.x, rocket.y))  #plot the new position  plt.plot(rocket.x, rocket.y, 'bo', linewidth=2, linestyle='dashed', markersize=12)  #move the rocket left, then plot the new position  rocket.move_left()  plt.plot(rocket.x, rocket.y, 'yo', linewidth=2, linestyle='dashed', markersize=12)
```

```
#show graph legend to match colors with positionplt.gca().legend(('original position','^ - Moved up', '< - Moved left'))plt.show()#plt.legend(loc='upper left')
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HVwrF6BepYaTcRAltJaPDQ.jpeg)
_Output from code above, using Python class_

Now let us create a module and move some of the code above to the module. Any time we need to create this simple set of x,y coordinates in any program, we can use the module to do so.

### What is a module and why do we need it?

A module is a file containing Python definitions and statements. Module is Python code that can be called from other programs for commonly used tasks, without having to type them in each and every program that uses them.

For example, when you call “matplotlib.plot”, you are calling a package module. If you didn’t have this module you would have to define the plot functionality in **every** program that used a plot graph.

From the Python [documentation](https://docs.python.org/2/tutorial/modules.html):

> If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead.This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.

> To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

Here’s our simple module. It takes the class creation and the functions to move an instance of that class from the program above and into its own class. We will then use this in a new program simply by calling and referencing this module:

Notice what we did above:

* created and initialized the class
* created a function to move an instance of the class in the four major directions (up, down, right, left) and the increments — as parameters, or arguments to the function
* created another function to calculate the distance between two instances of the class, using the graph distance formula

Here’s how we will use the new module to re-write the same program from the first part. Notice in the import section at the beginning, we now import the `simple_module1` module that we just created:

Here’s the output from the code using our module. Note that they are the same, except for the chart title and the shape of the position markers, which I changed for comparative purposes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M5O4PXU-UqHuXe62qSPezg.jpeg)
_Output from code from creating and calling our own module!_

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Ihrh85VkkfYuZhiH_4oAg.png)
_Comparison of the original file-left(create class, use it) and same functionality using a module, right_

![Image](https://cdn-media-1.freecodecamp.org/images/1*QnBS_HmigffIj6PBz2DvUQ.jpeg)
_Comparison of the output. On the right side, I change the marker shape for distinction, but the positions are unchanged._

That’s great, you may say — what are some other uses for this? One classic example is a bank account. A customer class might contain the name and contact details and — more importantly — the account class would have deposit and withdrawal elements.

This is grossly oversimplified but, for illustrative purposes, it is useful. That’s it — create a template, then define instances of that template with details (properties), and add value by adding, subtracting, modifying, moving, and using these instances for your program objectives.

Still wondering about classes? Ok, let’s get “classy” — here’s another simple illustration. We will call this class “Person”. It has only two properties — name and age. We will then add an instance of this with a person’s name and age, and print it. Depending on what your objective is, you can imagine all the other details you might add — for example, marital status and location preferences for a social networking app, job experience in years and industry specialization for a career related app. Press the little triangle below to see it work.

So there you have it. You can create many different classes, with parent classes, sub-classes and so on. Thanks for reading — please clap if you liked it. Here are some other references if you would like to learn more:

* [Python documentation — Classes](https://docs.python.org/3/tutorial/classes.html)
* [Python Object Oriented — Tutorials Point](https://www.tutorialspoint.com/python/python_classes_objects.htm)
* [Classes and Objects — learnpython.org](https://www.learnpython.org/en/Classes_and_Objects)

