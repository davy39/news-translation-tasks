---
title: How I overcame my resistance to becoming a Pythonista
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T00:36:41.000Z'
originalURL: https://freecodecamp.org/news/resistance-to-becoming-a-pythonista-f5a734d15c61
coverImage: https://cdn-media-1.freecodecamp.org/images/0*8-Fy9RNpdEIE4XTW
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Semi Koen

  For over a decade, my main ‘mother tongue’ has been C#. I have been using it since
  version 1, and loved the journey through features such as generics, anonymity, LINQ,
  and async and combining this with design patterns, SOLID principles, ...'
---

By Semi Koen

For over a decade, my main ‘mother tongue’ has been C#. I have been using it since version 1, and loved the journey through features such as generics, anonymity, LINQ, and async and combining this with design patterns, SOLID principles, architectural styles and TDD/BDD, I now live and breathe C#. I used to snobbishly look down to the scripting languages…

_How can you call yourself a software engineer and use a scripting language? Doh!_

I work in a financial organisation in the City. The languages of choice have been Java and C#, for both Front and Back Office applications. Data Science and Machine Learning are becoming two of the most hyped modern technologies and they are now scaling in financial institutions too. As my background is in Computer Science (with my dissertation on data mining and artificial intelligence), I thought I should check it out…

I had to refresh my maths knowledge, and after an [introductory ML on Pluralsight](https://www.pluralsight.com/courses/understanding-machine-learning) and [another on Python](https://www.pluralsight.com/courses/python-getting-started), I didn’t understand what the whole fuss was about.

_Why use Python? I can do all of these things in C#… and in fact much better!_

I proudly said to my colleague: “I am not a ‘cowboy coder’… You cannot write a SOLID Python application”.  
And he said: “Why not? SOLID are just principles. You can apply them in any language”.

_This was eye opening for me._

I started researching Python: It is in the top three programming languages (as of Dec 2018) [according to TIOBE](https://www.tiobe.com/tiobe-index). StackOverflow confirms that [it has surpassed C#](https://insights.stackoverflow.com/survey/2018/#most-popular-technologies). So does the [HackerRank Report](https://research.hackerrank.com/developer-skills/2018).

_What? Am I missing a trick?_

This is how my journey to becoming a Pythonista started… I had to be convinced that it was worthwhile.

Here are the answers to two of my main reservations, i.e.:

1. I love my career in the finance sector. _What makes financial organisations use Python?_
2. I am not a ‘cowboy’ (‘cowgirl’ rather). _Do SOLID principles apply in Python?_

### Why do financial organisations use Python?

My research showed me there are several reasons:

**— Quick Time to Market:** You can go ‘from zero to hero’ pretty quickly. There is a rich set of libraries that have pretty much everything you will ever use. Writing Python programs is like building a tower with Lego. You can find the individual blocks and all you need to do is to glue them together to build your algorithm.

**— Bridges Economics and IT:** Quants and tech savvy business people can understand and also write their algorithms in Python. Developers can then integrate it in a full stack application.

**— Embraces Analysis:** Anaconda comes with an installation of the Jupyter notebook. This is every developer’s and data scientist’s playground to analyse data and create visualisations. Trading, Market Prices, financial risk modeling are some applicable areas.

### Do SOLID principles apply in Python?

YES — They do! Principles are not an end in themselves. Rather, they are guidelines to writing better and cleaner code. However, there is no silver bullet on applying them into functional/dynamic languages.

Nevertheless, here is what I have come up with:

**— Single Responsibility:** A class should have only one reason to change.

This is pretty straight forward, just gather together the functions that change for the same reason into a single class/method/entity. Same as C#.

**— Open Closed:** Classes should be open for extension and closed for modification. The base/abstract class is closed for modification. Concrete subclasses are created to modify their behaviour.

Many ways to achieve this include: inheritance, composition, design patterns (Decorator, Strategy etc). Python allows for multiple inheritance of classes, other than that it’s the same as C#.

**— Liskov Substitution:** If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of T. In other words, the derived class should extend its parent class without changing its behaviour.

As long as you can distinguish the difference between composition and inheritance, then Bob’s your uncle. Also be mindful of monkey patching as this will most certainly break this principle.

**— Interface Segregation:** Clients should not be forced to depend upon interfaces that they don’t use.

There are no interfaces in Python, so this is not too relevant. But generally it’s all about keeping the classes and the exposed methods to a minimum as well as the ability to inherit from multiple concrete classes in order to provide clients specific behaviours.

**— Dependency Inversion:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details — details should depend on abstractions.

As a dynamic language, Python doesn’t require the use of abstractions to facilitate decoupling.

What I was hoping to find when I started this analysis is that C# wins the ‘Language Battle’ over Python, but I realised that it is a poor programmer whose development toolkit contains only one programming language!

I would personally use C# to build a large scale, enterprise application (especially on the server side), but I am totally converted to Python for quicker development and proof of concepts — predominantly when it comes to the Data Science or Machine Learning domains!

Thanks for reading my first article ?

