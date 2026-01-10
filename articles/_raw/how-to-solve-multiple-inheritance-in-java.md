---
title: How to Solve the Problem of Multiple Inheritance in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-01T14:42:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-multiple-inheritance-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-edward-jenner-4253062.jpg
tags:
- name: inheritance
  slug: inheritance
- name: Java
  slug: java
seo_title: null
seo_desc: "By Nahla Davies\nJava is one of the most popular object-oriented programming\
  \ languages in use today. \nBecause it is platform-independent, you will find Java\
  \ applications on every type of device and every operating system. And because Java\
  \ is relativel..."
---

By Nahla Davies

Java is one of the most popular object-oriented programming languages in use today. 

Because it is platform-independent, you will find Java applications on every type of device and every operating system. And because [Java is relatively easy to learn](https://www.freecodecamp.org/news/get-started-coding-with-java/), it is one of the first languages that many programmers pick up.

An important feature of Java that you should be familiar with is class inheritance. Inheritance allows programmers to optimize code by facilitating class reuse. When you can reuse code that has already been tested and debugged, the software development life cycle becomes shorter and less costly.

While theoretically a simple concept, coding inheritance relationships require attention to detail. This is particularly true with respect to multiple inheritance, where a single child class inherits properties from multiple parent classes. 

Java rejects multiple inheritance relationships because they create ambiguities, but there are a few ways you can accomplish many of the same effects if you know what to do.

In this article, we'll consider the problems with multiple inheritance and discuss alternative coding options in Java.

## Inheritance Terminology

Sometimes, to be a successful programmer, you have to learn to problem solve in order to find workarounds for common bugs or problems. This is a necessary part of coding securely and smartly. 

One such problem deals with multiple inheritance (or rather, the lack thereof) in Java.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-73.png)
_[Image Source](https://www.tutorialspoint.com/java/java_inheritance.htm)_

To fully understand inheritance in Java, you need to familiarize yourself with basic [object-oriented programming](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/) (OOP) inheritance terminology. 

* **Class:** Classes are a fundamental template structure in object-oriented programming languages. A class defines the common properties for a group of objects.
* **Parent Class:** Also known as base classes or superclasses, a parent class is an extensible class that provides features to a child class. This is where reusability comes into play. The parent class definitions and functions are reused when creating child classes.
* **Child Class:** More generically called a subclass, a child class inherits features from another class. Child classes are extended or derived classes.
* **Inheritance:** The relationship between the parent and child classes.

## OOP Inheritance Types

There are many popular object-oriented programming languages in use today, including [Java, C++](https://stackoverflow.blog/2021/02/22/choosing-java-instead-of-c-for-low-latency-systems/), JavaScript, Python, PHP, Ruby, and Perl. While inheritance is a common concept across these OOP languages, not all inheritance types exist in each language.

It is crucial to know the general inheritance types and the limitations on inheritance in the specific language you are using. The more you know about inheritance, the more effective a software developer you will be. 

Types of inheritance supported by Java include:

* **Single-level inheritance:** When a child class derives features from a single parent class.
* **Multi-level inheritance:** This is a tiered form of single-level inheritance. In multi-level inheritance, a child class can also act as a parent class to other child classes. The relationship between each level is linear – no branches are extending above as in multiple inheritance. The ultimate child class then has features from every level above it.
* **Hierarchical inheritance:** The opposite of multiple inheritance. In hierarchical inheritance, a single parent class has more than one child class. So rather than having branches above it, it branches below.
* **Hybrid inheritance:** As its name suggests, hybrid inheritance is a combination of other inheritance types.

In addition to the inheritance types above, there are other types that Java does not support.

* **Multiple inheritance:** In multiple inheritance, a child class has more than one parent class. While Java and [JavaScript](https://www.freecodecamp.org/news/functional-programming-in-javascript-for-beginners/) do not support multiple inheritance, OOP languages such as C++ do.
* **Multipath inheritance:** A hybrid of multiple, multi-level, and hierarchical inheritance, in multipath inheritance a child class derives its features and functions from a parent class and several child classes of the parent class. Because multipath inheritance relies on multiple inheritance, Java does not support its use.

## Why Java Doesn’t Support Multiple Inheritance

The primary problem with multiple inheritance is that it has the potential to create ambiguities in child classes. In a 1995 overview whitepaper, Java lead designer James Gosling stated that the [issues with multiple inheritance](https://www.researchgate.net/publication/345758345_Java_an_Overview_the_original_Java_whitepaper) were one of the motivations for the creation of Java.

The difficulties inherent in multiple inheritance are most clearly seen in the diamond problem. In [the diamond problem](https://www.freecodecamp.org/news/multiple-inheritance-in-c-and-the-diamond-problem-7c12a9ddbbec/), parent class A has two distinct child classes B and C; that is, child classes B and C extend class A.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-74.png)
_[Image Source](https://www.dotnettricks.com/learn/oops/understanding-inheritance-and-different-types-of-inheritance)_

Now we create a new child class D, which extends both class B and class C. Note that we have multiple inheritance (D extends B and C), hierarchical inheritance (B and C extend A), and multilevel inheritance (D extends A, B, and C).

In the diamond problem, child classes B and C inherit a method from parent class A. Both B and C override the inherited method. But the new methods in B and C conflict with each other. 

Ultimate child class D inherits the two independent and conflicting methods from its multiple parents B and C. It is unclear which method class D should use, so there is ambiguity. Other OOP programming languages implement various methods for addressing the multiple inheritance ambiguity.

## How to Solve the Multiple Inheritance Problem in Java

Just because multiple inheritance is problematic does not mean that it is not useful. There are many situations where you may want one class to have features from several other classes. 

Just think about that Tesla Roadster you will buy when you become a wildly successful software developer. It will draw characteristics from both the sports car class and the electric car class. 

Or maybe you are using a private browser to read this article, which has features from the online data privacy solution class and the general internet browser class.

But you can’t extend multiple classes in Java. So how does Java deal with the multiple inheritance issue? 

Well, it uses structures called interfaces. Interfaces are [abstract types that specify behaviors](https://www.freecodecamp.org/news/java-interfaces-explained-with-examples/) for classes to implement. Because they are abstract, interfaces do not contain detailed instructions for their behaviors. Instead, the classes provide concrete implementations of interface behaviors.

Interfaces have several defining characteristics:

* Unlike classes, you do not instantiate interfaces. Instead, classes implement interfaces
* Interfaces contain only public constant definitions and method headers
* Interfaces can only extend other interfaces, not classes
* Interfaces can extend multiple interfaces, and classes can implement multiple interfaces

Now, we can effectively bypass the diamond problem with interfaces. Recalling that only interfaces can only extend other interfaces and any class that needs multiple inheritance characteristics must implement multiple interfaces, we can redefine the diamond problem classes. 

What were previously classes A, B, and C now become interfaces A, B, and C. Interfaces B and C still extend interface A, but there are no concrete functions in any of these interfaces, just defined behaviors. Class D remains a class, which is responsible for the concrete implementation of the behaviors found in interfaces B and C. 

Note one key distinction here: Class D is not extending interfaces B and C. It is instead implementing them. So you do not actually have a multiple inheritance. Instead, you have simply redefined the problem.

## Conclusion

Understanding inheritance is necessary for any effective coder. For Java programmers, it is equally important to know the limitations of inheritance and the built-in Java workaround for the traditional problems with multiple inheritance. 

Learning [how to put interfaces in place](https://www.freecodecamp.org/news/polymorphism-in-java-tutorial-with-object-oriented-programming-example-code/) to recreate the effects of multiple inheritance in Java will increase your effectiveness and hireability.

