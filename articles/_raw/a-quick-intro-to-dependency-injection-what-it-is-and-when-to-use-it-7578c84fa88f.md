---
title: 'A quick intro to Dependency Injection: what it is, and when to use it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-18T22:25:28.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rU6KNs9KfdROiENL-UQTNA.jpeg
tags:
- name: Design
  slug: design
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Bhavya Karia

  Introduction


  In software engineering, dependency injection is a technique whereby one object
  (or static method) supplies the dependencies of another object. A dependency is
  an object that can be used (a service).


  That’s the Wikipedi...'
---

By Bhavya Karia

### Introduction

> In [software engineering](https://en.wikipedia.org/wiki/Software_engineering), **dependency injection** is a technique whereby one object (or static method) supplies the dependencies of another object. A dependency is an object that can be used (a [service](https://en.wikipedia.org/wiki/Service_(systems_architecture))).

That’s the Wikipedia definition but still, but it’s not particularly easy to understand. So let’s understand it better.

Before understanding what it means in programming, let’s first see what it means in general as it will help us understand the concept better.

Dependency or dependent means relying on something for support. Like if I say we are relying too much on mobile phones than it means we are dependent on them.

So before getting to [**dependency injections**](https://en.wikipedia.org/wiki/Dependency_injection), first let’s understand what a dependency in programming means.

When class A uses some functionality of class B, then its said that class A has a dependency of class B.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0P-1JhnUaZeobDUAajIbhA.jpeg)
_Showing dependencies between classes_

In Java, before we can use methods of other classes, we first need to create the object of that class (i.e. class A needs to create an instance of class B).

**So, transferring the task of creating the object to someone else and directly using the dependency is called dependency injection.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*TF-VdAgPfcD497kAW77Ukg.png)
_What if code could speak?_

### Why should I use dependency injection?

Let’s say we have a car class which contains various objects such as wheels, engine, etc.

Here the car class is responsible for creating all the dependency objects. Now, what if we decide to ditch **MRFWheels** in the future and want to use **Yokohama** Wheels?

We will need to recreate the car object with a new Yokohama dependency. But when using dependency injection (DI), we can change the Wheels at runtime (because dependencies can be injected at runtime rather than at compile time).

You can think of DI as the middleman in our code who does all the work of creating the preferred wheels object and providing it to the Car class.

It makes our Car class independent from creating the objects of Wheels, Battery, etc.

#### There are basically three types of dependency injection:

1. **constructor injection:** the dependencies are provided through a class constructor.
2. **setter injection:** the client exposes a setter method that the injector uses to inject the dependency.
3. **interface injection:** the dependency provides an injector method that will inject the dependency into any client passed to it. Clients must implement an interface that exposes a [setter method](https://en.wikipedia.org/wiki/Setter_method) that accepts the dependency.

**So now its the dependency injection’s responsibility to:**

1. Create the objects
2. Know which classes require those objects
3. And provide them all those objects

If there is any change in objects, then DI looks into it and it should not concern the class using those objects. This way if the objects change in the future, then its DI’s responsibility to provide the appropriate objects to the class.

#### Inversion of control —the concept behind DI

This states that a class should not configure its dependencies statically but should be configured by some other class from outside.

It is the fifth principle of **S.O.L.I.D** — the five basic principles of object-oriented programming and design by [**Uncle Bob**](https://en.wikipedia.org/wiki/Robert_C._Martin) — which states that a class should depend on abstraction and not upon concretions (in simple terms, hard-coded).

According to the principles, a class should concentrate on fulfilling its responsibilities and not on creating objects that it requires to fulfill those responsibilities. And that’s where **dependency injection** comes into play: it provides the class with the required objects.

_Note: If you want to learn about **SOLID** principles by Uncle Bob then you can head to this [link](https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design#toc-single-responsibility-principle)._

#### Benefits of using DI

1. Helps in Unit testing.
2. Boiler plate code is reduced, as initializing of dependencies is done by the injector component.
3. Extending the application becomes easier.
4. Helps to enable loose coupling, which is important in application programming.

#### Disadvantages of DI

1. It’s a bit complex to learn, and if overused can lead to management issues and other problems.
2. Many compile time errors are pushed to run-time.
3. Dependency injection frameworks are implemented with reflection or dynamic programming. This can hinder use of IDE automation, such as “find references”, “show call hierarchy” and safe refactoring.

You can implement dependency injection on your own (Pure Vanilla) or use third-party libraries or frameworks.

#### **Libraries and Frameworks that implement DI**

* [Spring](https://www.tutorialspoint.com/spring/spring_dependency_injection.htm) (Java)
* [Google Guice](https://github.com/google/guice) (Java)
* [Dagger](http://square.github.io/dagger/) (Java and Android)
* [Castle Windsor](https://github.com/castleproject/Windsor) (.NET)
* [Unity](https://www.microsoft.com/en-us/download/details.aspx?id=39944)(.NET)

**To learn more about dependency injection, you can check out the below resources:**

[**Java Dependency Injection — DI Design Pattern Example Tutorial — JournalDev**](https://www.journaldev.com/2394/java-dependency-injection-design-pattern-example-tutorial)

[**Using dependency injection in Java — Introduction — Tutorial — Vogella**](http://www.vogella.com/tutorials/DependencyInjection/article.html)

[**Inversion of Control Containers and the Dependency Injection pattern — Martin Fowler**](https://www.martinfowler.com/articles/injection.html)

Hope it helps!

If you liked the article and want to read more amazing articles, then do follow me here ([Bhavya Karia](https://medium.com/@bhavyankaria)) and show your support as it motivates me to write more.

If you have any questions or feedback for me than let’s connect on [LinkedIn,](https://www.linkedin.com/in/bhavya-karia-1b115a93/) [Twitter ,](https://twitter.com/thebhavyakaria) [Facebook](https://www.facebook.com/karia.bhavya).

#### Edit 1:

**_Thanks to [Sergey Ufocoder](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined) now this article has been converted into the Russian language. My Russian friends and who all can read the Russian language do give it a read._**

[Link to the article](https://medium.com/@xufocoder/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-de1367295ba8)

**_Also, if you want to apply DI in JavaScript and are looking for a library then [Jo Surikat](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined) suggests that you give a try to his library._**

[Di-Ninja](https://di-ninja.github.io/di-ninja/)

**_One more awesome DI library in JavaScript was suggested by [Nicolas Froidure](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined)._**

[knifecycle](https://github.com/nfroidure/knifecycle)

#### Edit 2:

**_If you are a PHP developer then don’t worry, got you all covered as well. [Gordon Forsythe](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined) recommended this amazing library which you all might want to try out._**

[auryn](https://github.com/rdlowrey/auryn)

Thanks for all the kind words that I have been receiving. Do share the article so that more and more people can be benefited.

If you learnt even a thing or two, please share this story!

