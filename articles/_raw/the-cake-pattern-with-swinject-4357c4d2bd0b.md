---
title: How (and why) to use the Cake Pattern with Swinject
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-22T07:01:01.000Z'
originalURL: https://freecodecamp.org/news/the-cake-pattern-with-swinject-4357c4d2bd0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AhTCkEaoe0JVpI8zJAxSTg.png
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'By Peter-John Welcome

  In my previous article, I showed how we can use the Cake Pattern to do dependency
  injection without any libraries. I got a lot of awesome feedback from many people
  suggesting alternative methods, which indicates that there is lo...'
---

By Peter-John Welcome

In my [previous article](https://medium.com/swift-programming/dependency-injection-with-the-cake-pattern-3cf87f9e97af), I showed how we can use the Cake Pattern to do dependency injection without any libraries. I got a lot of awesome feedback from many people suggesting alternative methods, which indicates that there is lots of interest in this topic.

One of the questions I got asked, which is very important, was how do we swap out our implementation with a mock for testing.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o8JOg5rpHYKVQ5DfjCvvMA.png)

In the comments, I made some suggestions. One of these was to use a dependency container.

[Swinject](https://github.com/Swinject/Swinject), which is a framework, is one of the dependency injection frameworks out there that implements a dependency container pattern.

You may be wondering: why we would need the cake pattern if we can just use [Swinject](https://github.com/Swinject/Swinject)? Or why would we try to use them together? Well, this comes down to personal preference. But I’d like to show how we can use these two together.

### **Getting Started**

In order for us to use [Swinject](https://github.com/Swinject/Swinject) in our project, we will need to install the pod.

```
pod 'Swinject'
```

Once we have our pod installed, we will start by creating two protocols. The first one will be a Registrable protocol that will have a register method that takes three parameters.

1. Dependency — this will be the type we are registering on the container.
2. Implementation — The implementation for the dependency we want it to resolve to.
3. ObjectScope — The scope in which we want this dependency to live. (Optional)

Our second protocol will be the Resolvable protocol which will have two methods on it. The first one is a resolve method, which will take a dependency type and return a concrete implementation of that type. The second one is a reset method that will reset the Resolvable for us (useful for testing).

We will now create a dependency container class that will conform to these protocols.

We will create a Swinject container and a static instance on our dependency container class.

**Warning: This code is written in Swift 4, where private can be used in extensions (not like in Swift 3, were fileprivate was needed).**

First, we will conform to the Registrable protocol and use the Swinject container we created and register our dependencies on it, with its respective implementations. We will also specify the objectScope to be graph by default.

Swinject provides four different built-in scopes. Please see the link below to the documentation where it is excellently explained.

[**Swinject/Swinject**](https://github.com/Swinject/Swinject/blob/master/Documentation/ObjectScopes.md)  
[_Swinject - Dependency injection framework for Swift with iOS/macOS/Linux_github.com](https://github.com/Swinject/Swinject/blob/master/Documentation/ObjectScopes.md)

Next, we conform to the Resolvable protocol and again use the same Swinject container to resolve the dependencies. We will reset the container in the reset method by removing all the registered dependencies on the container.

We now have a dependency container — Yay!! But how do we use this container to resolve our dependencies?

We will create a Resolver factory that will handle this for us. It will first have a container property of type Resolvable, and this will be initialized with the dependency container class instance. We make this container of type Resolvable so that we can swap it out with any dependency container instance that conforms to that protocol.

We will now create two static methods that will be resolving and resetting our container when using our Resolvable container.

We have created this Resolver factory, and now it’s time to use it.

When creating our protocol extension (where we were resolving our implementation in the previous article), we can now use our Resolver factory.

We also need to remember that we will now have to register our dependency on our container.

There we go, we have the cake pattern with with Swinject as our dependency container.

### **Benefits**

The benefits of this approach are that we are decoupling the components of our application and providing a single source of resolving for these components. It also makes it much easier for us to swap out implementations with mocks for testing.

This gives us the option to share components anywhere in our application, as we will be able to resolve any dependency at any time with our injectable protocol extensions.

### **Unit Tests**

How would we test this? Well, all we need to do is call reset on the Resolver and then register the dependencies with mock implementations.

We now have our mocks being injected. Looks like we’re done.

Go try it! Let me know what you guys think.

Swinject is very powerful, and this article just demonstrates its basic functionality. If you would like me to explore more of its features, let me know in the comments below.

Get in Touch!

For the full example, you can find it on my Github.

[**pjwelcome/CakePatternWithSwinject**](https://github.com/pjwelcome/CakePatternWithSwinject)  
[_CakePatternWithSwinject - Cake pattern with Swinject as a dependency container_github.com](https://github.com/pjwelcome/CakePatternWithSwinject)[**Peter-John (@pjapplez) | Twitter**](https://twitter.com/pjapplez)  
[_The latest Tweets from Peter-John (@pjapplez). Mobile App Developer, Technology Explorer, Photographer, Co-Founder…_twitter.com](https://twitter.com/pjapplez)

[**Peter John Welcome — Google+**](https://plus.google.com/u/0/+PeterJohnWelcome)

Thanks to [Ashton Welcome](https://plus.google.com/111778165757216259863), and [Keegan Rush](https://medium.com/@RushKeegan) for reviewing this post.

