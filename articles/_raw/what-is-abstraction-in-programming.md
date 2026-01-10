---
title: What is Abstraction in Programming – And Why is it Useful?
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2022-07-13T22:54:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-abstraction-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--518-.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: null
seo_desc: 'Did you know that abstraction is one of the most important concepts for
  any software engineer to know?

  That''s right!

  Without the use of abstraction when developing new technologies and concepts, we
  would never have been able to invent most software o...'
---

Did you know that abstraction is one of the most important concepts for any software engineer to know?

That's right!

Without the use of abstraction when developing new technologies and concepts, we would never have been able to invent most software or even most things.

So, understanding this concept is truly important for software development.

## What is Abstraction in Programming?

You have used abstraction in many ways but you might not have known it. 

Abstraction thinking is one of the things humans do in so many areas:

* Philosophy
* Art
* Mathematics
* Computer science
* and so much more …

But what is it truly? You'll learn all about it in this article.

## What We'll Cover:

1. Abstraction Analogy
2. Python Example of Abstraction
3. General Electronics Example of Abstraction
4. Embedded Systems Example of Abstraction
5. Why is Understanding Abstraction Useful?

## Abstraction Analogy

![Image](https://www.freecodecamp.org/news/content/images/2022/07/pexels-torsten-dettlaff-70912.jpg)
_Photo by Torsten Dettlaff from Pexels: https://www.pexels.com/photo/black-coupes-70912/_

Let's say you are in a driving school to get your driver's license.

In the school, you learn how the main car components work:

* Brakes
* Transmission
* Suspension system
* Battery

You don't need to understand at a technical level each component to learn how to drive.

You just need a mental image as of what the brakes do when you press your foot down. Or what happens in the transmission when you change gears...and so on.

You only need a **basic mental representation** of the component you are using.

This means that you only need an **abstraction** of the car component.

Our use of abstractions to learn and use things is everywhere:

* You don't need to know the inner parts of a car to drive it. But knowing how they work can make you a **better driver.**
* You don't need to know the inner parts of a bicycle to know how to ride it. But knowing how that works can make you a **better rider.**
* You don't need to know the inner parts of a function or framework in programming to use it. But knowing how those things work can make you a **better programmer.**

## Python Example of Abstraction

![Image](https://www.freecodecamp.org/news/content/images/2022/03/code.png)

This is code written in Python. We are just using the print function to output the text “Hello world” on the screen.

To do this, you just need to know how to use the print function. 

You don't need to understand how it works under the hood.

But it is good sometimes to understand how a certain function works in the background in order to use it more effectively. 

By knowing how it works:

* You will become a better programmer by understanding other people's code
* You will understand bugs in any libraries you use more easily
* Instead of importing a whole library, you can copy the code you need from another project. A project with fewer dependencies will be easier to manage

For example, let's say you want to use the [Python statistics module](https://docs.python.org/3/library/statistics.html), which is a build-in module in Python. This means that Python already comes with the module in its library.

You don't need to [import it with PIP](https://www.freecodecamp.org/news/how-to-use-pip-install-in-python/).

Let's say I want to use the [mean function](https://docs.python.org/3/library/statistics.html#statistics.mean):

```
from statistics import mean 

randomList = [-1.0, 2.5, 3.25, 5.75]

print(mean(randomList))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/python-example.png)

If there is no data, the [Statistics.error](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError) will be raised.

This will print out 2,625.

But how does that work inside?

If you go to [https://github.com/python/cpython/blob/main/Lib/statistics.py](https://github.com/python/cpython/blob/main/Lib/statistics.py), you will find at line 414 the code for the mean function:

```python
def mean(data):
    """
    Return the sample arithmetic mean of data.
    >>> mean([1, 2, 3, 4, 4])
    2.8
    >>> from fractions import Fraction as F
    >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
    Fraction(13, 21)
    >>> from decimal import Decimal as D
    >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
    Decimal('0.5625')
    If ``data`` is empty, StatisticsError will be raised.
    """
    T, total, n = _sum(data)
    if n < 1:
        raise StatisticsError('mean requires at least one data point')
    return _convert(total / n, T)
    
    
 
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/https-__github.com_python_cpython_blob_main_Lib_statistics.py.png)

This is the inside code that runs when you use the statistics built in module Python gives you.

## General Electronics Example of Abstraction

Any embedded system or electronic device requires circuits.

Circuits are made up of many wires and components. Electronics engineers design these devices.

In any electrical engineering or related program, college student not only learn how to design circuits, but also learn the actual physics behind each component that makes up the circuit.

After college, many electrical engineers _work_ on small circuits to develop electronics for calculators, microwaves, printers, and other devices.

While electrical engineers work to make the circuits, who works to make the components?

Well, some electrical engineers, materials engineers, applied physicists, and others.

In this example, we will use applied physicists – scientists that apply physics to solve hard technical problems.

Some applied physicists focus on the study and creation of the components used in a circuit.

Some applied physicists bother with developing stuff that will become the building blocks of circuits like:

* LED's
* LCD displays
* Capacitors
* Photo resistors

Electrical engineers develop the circuits and electronics applications with these components.

They don't care at the same level of detail as applied physics about the composition of these components.

What they care about is using this materials to solve problems with electronics.

That is abstraction!

The applied physicists focus on the level of abstraction where components are created, with what materials, with the time to create them...

The electrical engineer focuses on the level of abstraction where components are used to create circuits and devices.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/abstraction.drawio.png)
_**What each professional works in?**_

## Embedded Systems Example of Abstraction

An embedded systems engineer (engineers that create small computer systems with a dedicated function, like a toaster, scientific calculator, mouse, keyboard, and so on) needs to know how to code close to the hardware.

To do that, they needs to have a good understanding of C and assembly language, since they are closely related to one another.

For example, in critical embedded systems (real-time applications that process data and events that have critically defined time constraints) like:

* Medical devices
* Airplane control systems
* Missile guidance systems

An engineer needs to be able to understand the C code and assembly. Assembly normally is used in very specific functions when pure assembly runs better than compiled C code.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/abstraction.drawio-2.png)
_**Example of different levels of abstraction**_

Each box is a different level of abstraction.

Those electrical components are made and studied by applied physics, material engineers, and some electrical engineers.

Those software components (functions, classes) are used and created by the embedded systems programmers.

## Why is Understanding Abstraction Useful?

Understanding abstraction will enable you to understand when you need to know something technical or just how to use it.

Another reason to understand abstraction well is when you start learning a framework outside your work area.

When you first learn a framework, you learn how to use it. As you learn how the framework works, you start understanding its limits. 

As a result, you learn how classes and functions are actually written.

By understanding libraries, frameworks, and other aspects of programming, at an advanced level, you will be able to create your own libraries and frameworks.

This way, you will be able to progress in your career and you may even be able to solve some hard work problems.

Reducing dependencies in a project is another reason to understand abstraction.

When you use a few functions from an outside library, you can see how the code is written and simply add your own function or class.

That way, your project has fewer dependencies. This makes it easier for people to run your code without having to install other dependencies.

## Wrapping up

Thanks for reading! Now you know:

* What abstraction is
* Three abstraction examples: Python, general electronics, and embedded systems
* Why understanding abstraction is useful

