---
title: Object-Oriented Programming in Python – Explained in Plain English
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2023-09-07T18:39:52.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--524-.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: null
seo_desc: '“Any fool can know. The point is to understand.” - Albert Einstein


  Object-oriented programming is a popular way to write computer programs.

  Because of this, all programmers should understand what OOP is, what languages you
  can use to program this wa...'
---

> “Any fool can know. The point is to understand.” - Albert Einstein

Object-oriented programming is a popular way to write computer programs.

Because of this, all programmers should understand what OOP is, what languages you can use to program this way, and why it is important.

When asked [in simple terms what exactly object-oriented software is](https://fossbytes.com/steve-jobs-tells-the-best-definition-of-object-oriented-programming/), Steve Jobs said:

> _Objects are like people. They’re living, breathing things that have knowledge inside them about how to do things and have memory inside them so they can remember things._   
>   
> _And rather than interacting with them at a very low level, you interact with them at a very high level of abstraction, like we’re doing right here._ However, what does it actually mean in code?

This guide will cover the basics, including some concepts most tutorials fail to address, like:

* What is "__init__" ?
* How do methods and functions differ?
* What does the "self" parameter in Python mean?

The purpose of this guide is to help you understand the basics of object-oriented programming in Python. So let's dive in.

### What we'll cover:

1. [What is OOP](#heading-what-is-oop)?
2. [What are classes and instances of classes?](#heading-what-are-classes-and-instances-of-classes-or-objects)
3. [How to create classes with "__init__"](#heading-how-to-create-classes-with-init)
4. [What is the self keyword?](#heading-what-is-the-self-keyword)
5. [Instance variables vs class variables](#heading-instance-variables-vs-class-variables)
6. [Methods in OOP – Correcting inflation price example](#heading-methods-in-oop-correcting-inflation-price-example)
7. [Where to go from here](#heading-where-to-go-from-here)

This tutorial assumes you know the [basics of Python programming](https://www.youtube.com/watch?v=rfscVS0vtbw).

Feel free to use the code and images of the posts in the GitHub repository below.

## What is OOP?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/pexels-binyamin-mellish-106399.jpg)
_Photo by [Binyamin Mellish from Pexels](https://www.pexels.com/photo/house-lights-turned-on-106399/)_

Suppose you run a construction company. Your business is expanding. It is your goal to build 100 new houses.

You decide that all the houses will have more or less the same structure.

By doing it this way, you can lower costs and better manage all the complexities involved in building homes.

Each house will be built using the same house plan, designed by an architect.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/pexels-jeshootscom-834892.jpg)
_Photo by [JESHOOTS.com](https://www.pexels.com/photo/floor-plan-on-table-834892/)_

Instead of designing each house from scratch, all the houses you build will have a similar floor plan.

In this case, you can say that your company builds houses in a house-oriented way.

In this analogy:

* A drawing = a class
* The house = an instance of a class or object
* House-oriented building = Object-oriented programming

In the same way that house-oriented building is an efficient way to build new houses, object-oriented programming is an efficient way of writing computer programs.  
  
To ensure that everything went smoothly when building your first home, you started giving instructions to people on how to do things.  
  
Likewise, programming begins with writing programs that give instructions to do certain things in a certain way.  
  
In object-oriented programming, however, you create blueprints for managing and creating data.  
  
With house-oriented building, you draw out a house plan and decide what material is needed to build it.  
  
And in coding, using blueprints to create objects allows you to reuse your code and build upon it easily.  
  
It is easier to manage the logistics of building houses when you have one house plan to choose from, and you can scale the number of houses to whatever number you wish. The same goes for code and object-oriented programming.

### The main principles of OOP

Just as there various are good practices for building homes, there are also good practices in object-oriented programming.

To write great code, OOP follows four pillars:

* Polymorphism – Ability of an object to take many forms
* Inheritance – Child classes acquire properties from parent classes
* Encapsulation – Protects data and methods from outside misuse by binding them together
* Abstraction – Handles complexity by hiding unnecessary details from the user.

To relate this to our house-oriented building example:

* Polymorphism – The ability of a house to have different types of roofs, windows, doors, and so on.
* Inheritance – A house gaining a new feature, like an garage.
* Encapsulation – Keeping kids out of the garage by using a garage key.
* [Abstraction](https://www.freecodecamp.org/news/what-is-abstraction-in-programming/) – Ignoring the construction materials and frame of the house, and instead just considering how the final product looks.

In the above examples, we've talked about the general concepts –not the code behind each concept. And we won't cover the code here. Even so, you can get an idea of what each concept is and why it is important.

If you want to learn more about the code, [you can read this tutorial](https://www.freecodecamp.org/news/object-oriented-programming-in-python/).

### Can You Write Object-Oriented Code in Different Languages?

Using Object-Oriented Programming (OOP) in different programming languages is possible, but you may use different techniques based on the language and the kind of program you're creating.

For example, let's take Java. It's designed specifically for OOP. In Java, you create classes and objects to structure your code. 

It's like creating blueprints and then building with those blueprints. 

But some languages, like C, work in a more procedural manner. They're like following a recipe step by step instead of using blueprints.

In the case of Python, it is a very flexible programming language. You can use OPP in Python, where you make those blueprints with classes.

It can also be used for procedural programming, where you give straightforward instructions like a to-do list.

Using OOP can be super helpful when you're working on complex software projects. 

It helps you keep things organized, makes it easier to update your code, and lets you reuse parts of your code in different places. 

## What are Classes and Instances of Classes (or Objects)?

Instances are created based on a class. Classes are blueprints that show how an instance of a class will look.

Instance variables have data unique to that instance that's not shared among all classes. 

Each instance has unique attributes just like every house does.

But, how does all of this look like in actual code? 

### How to create classes manually:

```python
class house():
    pass

house1 = house()
house2 = house()

house1.address = 1234;
house1.state = "california"
house1.Alarm = False;
house1.price = 300000;

house2.address = 5678;
house2.state = "texas"
house2.Alarm = True;
house2.price = 100000;

print(house1.state)
print(house2.price)

>>> california
>>> 100000
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/manually.png)

In the first line, we created a blueprint for the house without anything predefined.

This is the same as when an architect has a blank sheet of paper that is the blueprint for a house – the sheet exists, but it contains nothing.

We then created 2 houses with the same characteristics:

* Address of the house
* State of the house
* If it has an alarm or not
* Price of the house

But to add each characteristic, we had to insert the value manually.

But, what if you wanted to create 100 houses with the individual characteristics filled out for each house?

Adding all these class attributes manually is quite boring and time-consuming.

Let's see how we can simplify this:

### How to create classes with `__init__`:

```python
class house():
    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price


house1 = house(1234, "california", False , 300000)

house2 = house(5678, "texas", True , 100000)

print(house1.state)
print(house2.price)

>>> california
>>> 100000
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/automatic.py-1.png)

The outputs of both this code block and the one in the previous section are the same.

The first one has 18 lines and creating a house is difficult. The second one has 14 lines and a house can be easily created.

This is the essence of programming – automating things and making them easier.

You might have some questions about the code above. Let's look at it in more detail.

### What is `__init__`?

`__init__` is the Python constructor. It tells the Python interpreter that you want to **create** a class with **certain attributes**, such as price, state, and so on in this case.

It has the double underscores so that the interpreter can distinguish between the code variables and [Python special methods.](https://docs.python.org/3/reference/datamodel.html#special-method-names)

The [use of underscores](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name) is out of the scope for this article, so just know what these do here.

The attributes you want are next to the constructor.

But, why is a "self" variable there? And what does self mean?

## What is the `self` Keyword?

The `self` keyword just lets you know that a certain attribute changes from object to object.

Below is an example of what I mean:

```py
self.address = address
```

Is the same thing as writing:

```py
house1.address = 1234;
```

However, by writing:

```python
  def __init__(self, address, state, alarm, price):
        self.address = address
        self.state = state
        self.alarm = alarm
        self.price = price
```

You are saying you want to **create a house** (`__init__`) with four characteristics: address, state, alarm, and price.

The you are saying that, in any instance of the class, the .**characteristic** of a house is the same as the one in the parameters.

This way, when writing:

```python
house1 = house(1234, "california", False , 300000)
```

It will think:

```
house1.address = 1234
house1.state = "california"
house1.alarm = False
house1.price = 300000
```

Note: Instead of using self, you can use whatever variable you want. It is just for convention to reference the instance of the class we are using.

Also, this way, you give a value to each attribute of a class really easily.

### Why all this confusion?

This way, you can create attributes based off other attributes that need to be declared again:

```python
class house():
    def __init__(self, address, street , state):
        self.address = address
        self.street = street
        self.state = state

        self.completeAddress = str(address) + " " + state


house = house(1234, "california", "awesome road")

print(house.completeAddress)

>>>1234 awesome road
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/completeAddress.py.png)

With self, we can create other attributes based on the `__init__` parameters.

The `__init__` function does not have a `completeAddress` parameter.

It was built based on the address, street, and state values.

(Note that this is a random address and isn't real.)

### Instance variables vs class variables

So as of right now we have seen that we can build many houses based off a single house plan. 

But, we're not done yet. Let's say that you want every home to have a big living room carpet

![Image](https://www.freecodecamp.org/news/content/images/2022/08/pexels-pixabay-carpet.jpg)
_Photo by [Pixabay from Pexels](https://www.pexels.com/photo/apartment-carpet-floor-furniture-276666/)_

Each room will have the **same** carpet in every house. Other things in the house, like the sofa, can be **different**.

Let's also assume that all houses will have a sofa.

So in OOP, the sofa is an **instance variable**, because each instance of the class will have its own value for that attribute. 

For example, the attributes:

* address
* state
* alarm
* price

are all instance variables, because they are unique to each instance.

So the sofa is an **instance variable** – but the carpet is an **class variable.**

Because it is a class variable, all instances of the class will have that variable.

Another example of a class variable is the name of the company that builds the houses:

```python
class house():

    company_name = "Awesome building company"

    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price


house1 = house(1234, "california", False , 300000)

house2 = house(5678, "texas", True , 100000)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/automaticV2.py.png)

The class variable here is the company name: "Awesome building company".

Again, a variable containing instance-specific data is called an instance variable – it's not shared between classes. 

Variables such as state or price are instance variables.

* Instance variables = particular characteristics of each house (different)
* Class variables = Name of the company that builds the house (same)

All instances of the classes contain class variables, and every instance of a class has its own instance variables.

### What if variables change over time?

House prices and inflation are really high in 2023. So high that the prices of the homes no longer reflect their actual value. The price of the house – or any item – can change over time based on various factors.

For example, over time, a house that was valued at $50,000 dollars will now cost $54,000 due to 8% inflation.

The price has gone up. So now you have a problem:

How are you going to update the new price of a house, given that inflation is currently 8%?

One of the answers to that question is to use a method to update the price.

A method is, in simple words, a function inside a class. It is just a function, but it's associated with a class when we use it.

## Methods in OOP – Correcting Inflation Price Example

We will now look on 3 ways to correct the price:

1. Building an instance method inside the class to correct the price
2. Using the class method to correct the price 
3. Using a function to correct the price 

All of these perform the same operation, just in a different manner.

### How to build an instance method inside the class to correct the price

In this first example, we will create a instance method inside the class `house` to correct the price called `correctPriceMethod()`:

```python
class house():

    company_name = "Awesome building company"

    inflation_coefficient = 1.08

    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price

    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/ray-so-export.png)

In this code, I created a method called `correctPriceMethod()`:

```python
    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient
```

This way, all houses created with the house class will have a method to update their prices.

For example, let's say we have an apartment with the following information:

```
apartment1 = house(1234, "california", False , 300000)

apartment1.correctPriceMethod()

print(apartment1.price)


```

In the following line:

```
 apartment.correctPriceMethod():
```

The method updates the price from $300,000 to $324,000 to reflect inflation.

Below is the same code again, but with two more apartments to showcase two other ways of updating the price. Let's look at the first method here:

```python
class house():

    company_name = "Awesome building company"

    inflation_coefficient = 1.08

    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price

    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient
        
#----------------------------------------------------------------

apartment1 = house(1234, "california", False , 300000)
apartment2 = house(1234, "california", False , 300000)
apartment3Price = 300000

print(apartment1.price)

apartment1.correctPriceMethod()
print(apartment1.price)

>>> 300000
>>> 324000
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2-1.png)

I have updated the price of apartment 1 with the `correctPriceMethod`.

So I updated the price with a method in a class instance.

### How to use the class method to correct the price

In this example, instead of using a instance method, I will use a class method to correct the inflation to update apartment 2.

In other words, instead of calling the method `apartment1.correctPriceMethod()`, I will use `house.correctPriceMethod(apartment2)`:

```
class house():

    company_name = "Awesome building company"

    inflation_coefficient = 1.08

    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price

    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient

#-----------------------------------------------------------

apartment1 = house(1234, "california", False , 300000)
apartment2 = house(1234, "california", False , 300000)
apartment3Price = 300000

apartment1.correctPriceMethod()

#-----------------------------------------------------------
print(apartment2.price)

house.correctPriceMethod(apartment2)
print(apartment2.price)

>>> 300000
>>> 324000
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/3-1.png)

This time, I updated the price with the class method instead of the instance method.

To put it another way, `house.correctPriceMethod(apartment2)` and `apartment2.correctPriceMethod()` are the same thing.

The first one gets the method from the class, while the second one gets the method from the instance of the class.

### How to use a function to correct the price 

So we have seen how to update the price with an instance method and a class method.

In this final example, we will simply use a function to update the inflation.

Now I will update the price for a third apartment, but this time with a function:

```
def correctPricefunction(apartment):
    return apartment * 1.08
```

Let's add this to the code:

```
class house():

    company_name = "Awesome building company"

    inflation_coefficient = 1.08

    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price

    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient

#-----------------------------------------------------------

apartment1 = house(1234, "california", False , 300000)
apartment2 = house(1234, "california", False , 300000)
apartment3Price = 300000

apartment1.correctPriceMethod()

#-----------------------------------------------------------

house.correctPriceMethod(apartment2)

#-----------------------------------------------------------

def correctPricefunction(apartment):
    return apartment * 1.08

print(apartment3Price)

apartment3Price = correctPricefunction(apartment3Price)
print(apartment3Price)

>>> 300000
>>> 324000
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/4.png)

We do the same thing with just the price of the apartment3 – but we are using a function this time.

That's right, we have the same thing. There is no change.

A method is simply a function associated with a class, while a function is just a function by itself.

By using a method, you are isolating the function that changes data from the class instead of data not from the class.

In Python, there are some cases where it is [better to use a function that a method](https://stackoverflow.com/questions/8108688/in-python-when-should-i-use-a-function-instead-of-a-method).

## Where to Go from Here?

This article scratches the surface of object oriented programming.

To fully understand it, it is good to learn the same thing from different perspectives.

There are many things you can do to learn more about object oriented programming:

1. You can dive in and learn more with this YouTube course from the freeCodeCamp channel:

%[https://www.freecodecamp.org/news/learn-object-oriented-programming-with-python/]

2.  Learn and write the actual code behind the 4 main pillars of OOP in Python:

* Polymorphism
* Encapsulation
* Inheritance
* Abstraction

3.  Apply and do OOP [projects in Python](https://www.freecodecamp.org/news/python-projects-for-beginners/) and in a [different programming language](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/).

4.  More advanced: Learn the main [software design patterns](https://www.freecodecamp.org/news/the-basic-design-patterns-all-developers-need-to-know/).

## Wrapping Up

Here's what we covered in this tutorial:

* What classes are
* What the self keyword is and why it is easy to understand
* What class variables are
* Difference between functions and methods

You also learned about some best practices to follow in object-oriented programming.

Thank you for reading!

