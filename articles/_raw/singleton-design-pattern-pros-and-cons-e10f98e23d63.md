---
title: Let’s examine the pros and cons of the Singleton design pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-24T13:33:45.000Z'
originalURL: https://freecodecamp.org/news/singleton-design-pattern-pros-and-cons-e10f98e23d63
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GOAK3XdRvjrcpX9dq0fUrQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Navdeep Singh


  Design patterns are conceptual tools for solving complex software problems. These
  patterns are simple and elegant solutions that have evolved over time and may have
  become generally accepted as the best way to address certain design...'
---

By Navdeep Singh

> Design patterns are conceptual tools for solving complex software problems. These patterns are simple and elegant solutions that have evolved over time and may have become generally accepted as the best way to address certain design challenges. — _Me, in my ebook_ Reactive Programming with Swift 4

### Singleton Design Pattern

The Singleton pattern encapsulates a shared resource within a single unique class instance. This instance arbitrates access to the resource and storage-related state information. A class method provides the reference to this instance, so there is no need to pass the reference around. Any object that has access to the Singleton’s class header can use the Singleton.

This design pattern defines the structure of a class that can have only one instance. **A Singleton encapsulates a unique resource and makes it readily available throughout the application**. The resource might be hardware, a network service, a persistent store, or anything else that can be modeled as a unique object or service.

One example from Cocoa touch is a physical device running an iOS application. For an executing app, there is only one iPhone or iPad with a single battery and a screen. UIDevice is a Singleton class here since it provides one channel to interact with the underlying features. In case the unique resource has a writable configuration, this sort of discrepancy can lead to problems such as race condition and deadlock. Since they are unique, **Singletons act as a control, ensuring orderly access to the shared resource.**

> Singletons may often be modeled as a server within the application that accepts requests to send, store, or retrieve data and configure the resource state.

### Implementation

Implementation of the Singleton pattern often typically creates a single object using the factory method, and this instance/object is called a shared instance in most cases. Since the access to the instance is passed on through a class method, the need to create an object is eliminated. Let’s look at the Singleton implementation in code.

For this example, we have used the **command line tool** Xcode template to create a project and name it Singleton. Our Singleton class is called **SingletonObject**, which we created as a normal Cocoa class, and it is a subclass of **NSObject**. The project setup looks like this so far:

![Image](https://cdn-media-1.freecodecamp.org/images/DrYEzG5i3dVViHfhA5b7kxvwdpti2SZvtLAp)

Then we added a class method called **sharedInstance** as discussed earlier since this is how the class will make the Singleton available. Its return value is of the **SingleObject** type, as follows:

```
func sharedInstance() -> SingletonObject {         }
```

The function stores the instance in a static local reference called **localSharedInstance**. Static locals are much like global objects — they retain their value for the lifetime of the application, yet they are limited in scope. **These qualities make them ideal to be a Singleton, since they are permanent and yet ensure that our Singleton is only available through sharedInstance_._**

This is one of the ways in which our Singleton implementation ensures that the Singleton stays singular. The basic structure of shared instance consists of a conditional block that tests whether a Singleton instance has been allocated. But surprisingly, that’s the older way of doing things (or may be the way to go in other languages). In Swift, however, the implementation has changed to merely one line, and we don’t require a method. The implementation looks like this:

```
class SingletonObject: NSObject {    static let sharedInstance = SingletonObject()}
```

Simple, isn’t it?

#### Singleton design pattern — Pros and cons

> Singletons are not the answer to every problem. Like any tool, they can be short in supply or can be overused.

Some developers are critical of Singletons for various reasons. We will examine this critique and discuss ways to address them briefly. The criticisms, for the most part, fall into two categories:

* **Singletons hinder unit testing:** A Singleton might cause issues for writing testable code if the object and the methods associated with it are so tightly coupled that it becomes impossible to test without writing a fully-functional class dedicated to the Singleton.
* **Singletons create hidden dependencies:** As the Singleton is readily available throughout the code base, it can be overused. Moreover, since its reference is not completely transparent while passing to different methods, it becomes difficult to track.

To avoid these complications, when considering the Singleton pattern, you should make certain that the class is a Singleton. Also, while thinking of designing the Singleton design pattern, keep testing in mind and use dependency injection whenever possible — that is, try to pass the Singleton as a parameter to the initializer whenever possible.

For other updates, you can follow me on Twitter on my twitter handle @NavRudraSambyal

To read more about various other Design patterns and practice examples, you can follow the link to my book [Reactive programming in Swift 4](https://www.amazon.com/Reactive-Programming-Swift-easy-maintain-ebook/dp/B078MHNSL1/ref=asap_bc?ie=UTF8)

Thanks for reading, please share it if you found it useful :)

