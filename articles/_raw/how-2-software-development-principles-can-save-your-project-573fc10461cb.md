---
title: How two software development principles can save your project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-18T01:38:33.000Z'
originalURL: https://freecodecamp.org/news/how-2-software-development-principles-can-save-your-project-573fc10461cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5IVmxQk8nIcC_qJ4n2fWBw.jpeg
tags:
- name: coding
  slug: coding
- name: design patterns
  slug: design-patterns
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jordy Baylac

  Introduction

  In this post I will focus on explaining how one Design Pattern (Inversion Of Control)
  and one Practice (YAGNI) can reduce the possibility of having a failed software
  project. You can start applying these techniques right ...'
---

By Jordy Baylac

### Introduction

In this post I will focus on explaining how one Design Pattern (**Inversion Of Control**) and one Practice (**YAGNI**) can reduce the possibility of having a failed software project. You can start applying these techniques right away.

If you are an Engineering Manager, this is a good read if you want to reduce the volatility on the marginal cost of features ?.

### Inversion of Control (IoC)

Did I mean _Dependency Injection_? Not really, but we can use Dependency Injection as the tool to achieve Inversion Of Control between dependencies.

**IoC** can help in changing the dependency direction. It can help in situations when component A depends on component B, and now you want A to be unaware of the implementation details of B.

**Current situation**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RCx6u3_JOxc8XPZxR134UQ.png)
_Component A depends on Component B._

**Target situation**

![Image](https://cdn-media-1.freecodecamp.org/images/1*1ZjKqM1zSvmGvr5ygWptdA.png)
_Component A does not depends on the implementation details of component B._

With the last approach, component A does not depend on the specifics of component B. In fact, new implementations of _IBehaviourB_ could be added to the project without even touching component A.

#### Code example

_An unknown application having three well-known layers._

```
UI -> REST API -> Database
```

Zooming into the REST API we found _UsersController_ class. We noted that it is reading and writing from/to a _SQLServer Database_. Below is a possible implementation on C#:

If you consider the above solution not to be a good design, you are right ?.

In the example, _UsersController_ is **tightly coupled** with the SQLServer implementation. The _postUser_ method makes it difficult to write **Tests** (remember that a unit-test should not hit databases or external services). As the application scales there will be a high dependency on the specific SQLServer library used. If somebody decides to split the application by domain area, it can be late ?.

This code example corresponds with the **“current situation”** presented at the beginning of the article. In this case:

* **A** = _UsersController_
* **B** = _System.Data.SqlClient_ on .NET

But wait…

**What if we apply Inversion of Control** so that UsersController does not depend on a specific SQLServer implementation? What if we make the REST API unaware of what Persistence layer we are using?

?, ok, let’s do it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*E4rMivDDauz8sM-KiJuCEA.jpeg)

**20 days later** ?:

For simplicity’s sake, we have denoted three source files, but in practice, they could be split or located on separates assemblies or folders. This solution corresponds with the **“target situation”** presented at the beginning. In this case:

* **A** = _UsersController_
* **B** = _SQLUserService_
* **IBehaviourB** = _IUserService_.

We did it!

Oh, but wait, how is the _IUserService_ dependency injected on the constructor of _UsersController_? Well, the implementation details of that are out of the scope of this article. However, if you are interested, check out the tutorial I added at the end.

#### Benefits

* Our architecture is open for extensions. Also, we reduced the necessity of modification in existing classes. **Open/Close** principle ?
* Tests are easy to write. We can inject a mock _UserService_ when testing UsersController ?
* Business logic is not coupled and does not depend on any _persistence_ strategy. ⭐️

### YAGNI

_You aren’t going to need it!_

I consider that every developer should adopt YAGNI as one of their core practices. This principle can save you from over engineering and having unused code (_untouchable_). It can also save your job.

**A funny small story:**

I worked in a project where Software Architects decided to represent almost all **boolean** columns in the database with a **char** datatype. At least they were using English — **true** was stored as “Y”, **false** with “N”. This makes sense right? When I asked how so magical a solution was conceived, they replied:

_“In this way, we are open to the possibility that a third state can come in”._

I never understood how a **true/false** thing can have a third state (perhaps they thought about qubits). As you may note, this ended up being a really bad decision and the consequences were present all over the code. I found things like:

```
if (supportVisa === "Y" || supportVisa === "y") { ...
```

Code readability was affected, and SQL queries were also affected.

But this didn’t stop there. With time, the software added internationalization to its user interfaces. Some configuration and catalogs were provided by the client itself using a GUI application. We get to the point in which some of our **boolean** columns had “S” and “N” (**S**i and **N**o in Spanish).

The code was really unmaintainable. I don’t want to talk about the solution they proposed ?.

### Conclusions

According to Uncle Bob, _good developers will try to maximize the number of decisions not made_. Do not write something that you believe is going to be helpful in six months. Instead, wait the six months, take a look at your architecture, see how much it has evolved, and then, do the work. Apply YAGNI.

You should manage your dependencies properly. Inversion of Control will guide you on that.

I hope to get into your conscious and help you be a better developer.

> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” ― **Martin Fowler**

### Read more on

* [Dependency Injection on C#](https://www.codeproject.com/Articles/1234518/Dependency-Injection-using-Unity-Resolve-dependenc)
* [TypeScript dependency injection.](https://nehalist.io/dependency-injection-in-typescript/)
* [Martin Fowler on YAGNI](https://martinfowler.com/bliki/Yagni.html)

**Please share your thoughts and ask any questions. I’ll be glad to answer** them. ? F**ind me** o**n t[witter.](https://twitter.com/jbaylacc)**

