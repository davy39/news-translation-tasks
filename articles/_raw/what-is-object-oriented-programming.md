---
title: OOP Meaning – What is Object-Oriented Programming?
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2022-09-06T17:15:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-object-oriented-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/OOP--1-.png
tags:
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: 'In today''s technology driven society, computer programming knowledge is
  in high demand. And as a developer, you''ll need to know various programming languages.

  Over the past few decades, many programming languages have risen in popularity.
  You can see...'
---

In today's technology driven society, computer programming knowledge is in high demand. And as a developer, you'll need to know various programming languages.

Over the past few decades, many programming languages have risen in popularity. You can see how popular languages are ranked in this real time ranking chart [here](https://www.tiobe.com/tiobe-index//). 

While new languages are being created, existing ones are always being updated to make them better.

Although most programming languages have some similarities, each one has specific rules and methods which makes it unique. 

One concept that is common among many programming languages is **Object Oriented Programming**.

When I first came across this term, it was a bit confusing. It took me some time to really understand it's importance in programming. But this also doubled as an opportunity for me to learn its key concepts, and know how important it is for a developer's career and being able to solve challenges.

In this article we will go over Object Oriented Programming (OOP) as a whole, without relying on a particular language. You'll learn what it is, why it's so popular as a programming paradigm, its structure, how it works, its principles, and more. 

Let's get started.

# What is Object-Oriented Programming?

If you were to conduct a fast internet search on what object-oriented programming is, you'll find that OOP is defined as a programming paradigm that relies on the concept of classes and objects.

Now, for a beginner, that might be a little bit confusing – but no need to worry. I will try to explain it in a simplest way possible, just like the famous phrase "Explain it to me like I'm 5".

Here's a brief overview of what you can achieve with OOP: you can use it to structure a software program into simple, reusable code blocks (in this case usually called classes), which you then use to create individual instances of the objects.

So let's find an easier definition of object-oriented programming and learn more about it.

## Explain OOP Like I'm 5

The word object-oriented is a combination of two terms, object and oriented. 

The dictionary meaning of an object is "an entity that exists in the real world", and oriented means "interested in a particular kind of thing or entity".

In basic terms, OOP is a programming pattern that is built around objects or entities, so it's called object-oriented programming. 

To better understand the concept, let's have a look at commonly used software programs: A good example to explain this would be the use of a printer when you are printing a document.

The first step is initiating the action by clicking on the print command or using keyboard shortcuts. Next you need to select your printer. Afterwards you will wait for a response telling you if the document was printed or not. 

Behind what we can't see, the command you clicked interacts with an object (printer) to accomplish the task of printing.

Perhaps you might wonder, how exactly did OOP become so popular?

# How OOP Became Popular

The concepts of OOP started to surface back in the 60s with a programming language called [Simula](https://en.wikipedia.org/wiki/Simula). Even though back in the day, developers didn't completely embrace the first advances in OOP languages, the methodologies continued to evolve.

Fast forward to the 80s, and an editorial written by David Robinson was one of the first introductions to OOP, as many developers didn't know it existed. 

By now languages like C++ and Eiffel had become more popular and mainstream among computer programmers. The recognition continued to grow during the 90s, and with the arrival of Java, OOP attracted a huge following.

In 2002 in conjunction with the release of the .NET Framework, Microsoft introduced a brand new OOP language called C# – which is often described as the most powerful programming language

It's interesting that, generations later, the concept of organizing your code into meaningful objects that model the parts of your problem continues to puzzle programmers. 

Many folks who haven't any idea how a computer works find the thought of object-oriented programming quite natural. In contrast, many folks who have experience with computers initially think there's something strange about object oriented systems. 

# Structure of OOP

![Image](https://www.freecodecamp.org/news/content/images/2022/09/OOP.png)

Imagine that you are running a pet shop, with lots of different breeds and you have to keep track of the names, age, days attended to, and other common upkeep details. How would you design reusable software to handle this? 

Keep in mind we have many breeds, so writing code for each would be tiresome. But we can group related information together so that we can produce shorter and more reusable code. 

That's where the building blocks come in to help us do this by using **Classes, Objects, Methods** and **Attributes**.

Let's take a deep dive and understand what exactly these building blocks are:

* **Classes** - these are user-defined data types that act as the blueprint for objects, attributes, and methods. 

* **Objects** - These are instances of a class with specifically defined data. When a class is defined initially, the description is the only object that is defined. 

* **Methods** - These are functions that are defined inside a class that describe the behavior of an object. They are useful for re-usability or keeping functionality encapsulated inside one object at a time. Code re-usability is a great benefit when debugging.

* **Attributes** - These are defined in the class template and represent the state of an object. Objects contain data stored in the attribute field.

# Principles of OOP 

![OOP](https://www.freecodecamp.org/news/content/images/2021/10/Creative-Business-Template-Presentation--2-.png)

In order for us to know how to write good OOP code, we need to understand the 4 pillars of OOP we should adhere to: 

* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

Let's dive in and better understand what exactly each of these mean.

## Encapsulation

This is the concept that binds data together. Functions manipulate the info and keep it safe. No direct access is granted to the info in case it's hidden. If you wish to gain access to the info, you need to interact with the article in charge of the info.

If you're employed in a company, chances are high that you've had experience with encapsulation. 

Think about a human resources department. The human resources staff members encapsulate (hide) the data about employees. They determine how this data will be used and manipulated. Any request for the worker data or request to update the info must be routed through them.

By encapsulating data, you make the information of your system safer and more reliable. You're also able monitor how the information is being accessed and what operations are performed on it. This makes program maintenance easier and simplifies the debugging process. 

## Abstraction

Abstraction refers to using simple classes to represent complexity. Basically, we use abstraction to handle complexity by allowing the user to only see relevant and useful information. 

A good example to explain this is driving an automatic car. When you have an automatic car and want to get from point A to point B, all you need to do is give it the destination and start the car. Then it'll drive you to your destination. 

What you don't need to know is how the car is made, how it correctly takes and follows instructions, how the car filters out different options to find the best route, and so on. 

The same concept is applied when constructing OOP applications. You do this by hiding details that aren't necessary for the user to see. Abstraction makes it easier and enables you to handle your projects in small, managable parts.

## Inheritance

Inheritance allows classes to inherit features of other classes. As an example, you could classify all cats together as having certain common characteristics, like having four legs. Their breeds further classify them into subgroups with common attributes, like size and color.

You use inheritance in OOP to classify the objects in your programs per common characteristics and performance. This makes working with the objects and programming easier, because it enables you to mix general characteristics into a parent object and inherit these characteristics within the child objects.

For example, you'll define an employee object that defines all the overall characteristics of employees in your company. 

You'll be able to then define a manager object that inherits the characteristics of the employee object but also adds characteristics unique to managers in your company. The manager object will automatically reflect any changes within the implementation of the employee object.

## Polymorphism

This is the power of two different objects to reply to one form. The program will determine which usage is critical for every execution of the thing from the parent class which reduces code duplication. It also allows different kinds of objects to interact with the same interface.

## Examples of OOP Languages 

Technology and programming languages are evolving all the time. We have seen the rise of may langs under the OOP category, but **Simula** is credited as the first OOP language. 

Programming languages that are considered pure OOP treat everything like objects, while the others are designed primarily with some procedural process. 

*Examples of OOP langs:*
* Scala 
* Emerald
* Ruby
* JADE 
* Java
* Python
* C++
* JavaScript
* Visual Basic .NET
* PHP

And many more.

## Benefits of OOP

During the 70s and 80s, procedural-oriented programming languages such as C and Pascal were widely used to develop business-oriented software systems. But as the programs performed more complex business functionality and interacted with other systems, the shortcomings of structural programming methodology began to surface. 

Because of this, many software developers turned to object-oriented methodologies and programming languages to solve the encountered problems. The benefits of using this languages included the following: 

* **Code Re-usability** - through inheritance, you can reuse code. This means a team does not have to write the same code multiple times. 

* Improved integration with modern operating systems. 

* **Improved Productivity** - developers can construct new programs easily and quickly through the use of multiple libraries.

* Polymorphism enables a single function to adapt to the class it is placed in.

* Easy to upgrade, and programmers can also implement system functionalities independently.

* Through **Encapsulation** objects can be self-contained. It also makes troubleshooting and collaboration on development easier.

* By the use of encapsulation and abstraction, complex code is hidden, software maintenance is easier, and internet protocols are protected. 

## Wrapping Up 

Today, most languages allow developers to mix programming paradigms. This is often because they will be used for various programming methods. 

For instance, take JavaScript – you can use it for both OOP and functional programming. When you're coding object-oriented JS, you have to think carefully about the structure of the program and plan at the start of coding. You might do this by viewing how you'll be able to break the necessities into simple, reusable classes which will be accustomed blueprint instances of objects.

Developers working with OOP typically agree that in general, using it allows for better data structures and re-usability of code. This saves time in the long term.


