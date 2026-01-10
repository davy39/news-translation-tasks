---
title: How to get rid of NullPointerException
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T14:38:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-rid-of-nullpointerexception-3cdf9199f9fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gq_k-Dj-b2hkTN_-kw5RaQ.png
tags:
- name: clean code
  slug: clean-code
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By shani fedida

  OverOps, an Israeli company which helps developers understand what happens in production,
  carried out research on what the top Java exceptions were in production. Want to
  guess which one is in #1 place? NullPointerException.


  NullPoin...'
---

By shani fedida

OverOps, an Israeli company which helps developers understand what happens in production, carried out [research](https://blog.takipi.com/the-top-10-exceptions-types-in-production-java-applications-based-on-1b-events/) on what the top Java exceptions were in production. Want to guess which one is in #1 place? `NullPointerException`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qhtt3vCy6mUF-z2X.png)
_NullPointerException OverOps’s monster_

Why is this exception is so frequent? I argue (as does Uncle Bob ?) that it is n**ot** because developers forget to add null checks.

The reason: **developers use nulls too often.**

### **So where do all those NULLs come from?**

In C# and Java, all reference types can point to `null`. We can get a reference to point to `null` in the following ways:

* “uninitialized” reference type variables — variables which are initialized with nulls and are assigned their real value afterward. A bug can cause them never to be reassigned.
* uninitialized reference-type class members.
* explicit assignment to `null` or returning `null` from a function

Here are some patterns I noticed in functions returning `null`:

#### Error handling

Returning `null` when the input is invalid. This is one way of returning error codes. I think it is an old school programming style, originating in the time when exceptions didn’t exist.

#### Missing optional data for entities

An entity’s property can be optional. When there is no data for an optional property, it returns `null`.

#### Hierarchical models

In hierarchical models, we usually can navigate up and down. When we are at the top, we need a way to say so, usually it is by returning `null`.

#### Find functions

When we want to find an entity by criteria in a collection, we return `null` as a way to say the entity was not found.

### What are the problems with using nulls?

#### It will blow up. Eventually…

The code in which the `NullPointerException` is raised can be very far from where the bug is. **It makes tracing the real problem harder.** Especially if the code is branched.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ULzFy6tmPqxYQKpuwWc3A.png)
_I am happy now but I will blow up eventually._

In the following code example, there is a bug, somewhere in class A, causing `entity` to be null. But the `NullPointerException` is raised inside a function of class B. Real-life code can be much more complicated.

#### Hidden errors

I encounter `null` checks which seems like the developer was thinking:

* “I know I should check for `null` but I don’t know what it means when the function returns `null` and I don’t know what to do with it,” or
* “ I think this cannot be null but just to make sure, I don’t want it to blow up production”

It usually looks like this:

Those kinds of `null` checks cause some code logic to not trigger, **without the ability to know about it**. Writing that kind of code means that some logic of a flow failed but the whole flow succeeded. It also can cause a bug in some other functionality which assumed the other function did its job.

Imagine you buy a ticket to a show online. You got a success message! The day of the show finally arrived, you leave work early, arrange a babysitter, and go to see the show. When you arrive you discover you don’t have tickets! and there are no empty seats. You return home upset and confused?. C**an you see how this kind of null check can cause this situation ?**

It also makes the code branched and ugly ?

### Missing non-nullable reference types in C# and Java

In C# and Java **reference types can always point to `null`**. This leads to a situation that we cannot know, by looking at a function signature, if `null` is a valid input or output of it. I believe most of the functions don’t return or accept `null`.

Because it is hard to know if a function returns `null` or not (unless documented), developers are either inserting `null` checks when not needed, or don’t check for `nulls` when needed — and yes, sometimes putting null checks when needed ?.

This poor design choice causes the problems I described before in “Hidden errors” and a lot of `NullPointerException` errors, of course. Lose-lose situation. ?

There are languages like [Kotlin](https://kotlinlang.org/docs/reference/null-safety.html) that aim to eliminate `NullPointerException` errors by differentiating between nullable references and non-nullable references. This allows catching the `null` assigned to non-`null` references, and making sure developers check for `null` before dereferencing nullable references, **all at compile time**.

Microsoft is adopting the same approach by introducing [Nullable Reference Types](https://msdn.microsoft.com/en-us/magazine/mt829270.aspx) in C#8.

### So what should we do?

#### Listen to Uncle Bob

[Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin), who is widely known as “Uncle Bob,” wrote one of the most famous books about clean code called (surprisingly) [“Clean Code”](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882). In this book, Uncle Bob claims, **we should not return `nulls` and should not pass `null` to a function.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*HGcUEEzNp9mTmK5w.jpg)

#### But how?

I want to propose some **technical patterns** for eliminating null usage. **I am not saying this is the best solution for every scenario — just options**.

**Using the option type**

The [option type](https://en.m.wikipedia.org/wiki/Option_type?wprov=sfla1&fbclid=IwAR3Y-vZX-mrpINhipnr_tjyZ4P8KZH0yLCtvcJqbtaMxry2DO6HJWdSP3XA) is a different way to represent an optional value. This type asks if a value exists and, if so, accesses the value. **When trying to access the value which doesn’t exist, it raises an exception**. This solves the problem of `NullPointerException` raised in code areas away from the bug. In Java there is [Optional<T>](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html);class. In C# (until C# 7 ) there [is the Nullabl](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/nullable-types/)e type which is only for value types but you can create your own or [use a l](https://github.com/nlkl/Optional)ibrary.

A straightforward approach is to replace a reference that can be `null` (by logic) with this type:

**Splitting the function into two**

Each function that returns `null` will be converted to two functions. One function with the same signature throws an exception instead of returning `null`. The second function returns a boolean representing if it is valid or not to call the first function. Let’s see an example:

If the code holding an `IEmployee` instance assumes this employee has a manager the code should call to `Manager`. But if this assumption doesn’t exist the code should call to `HasManager` and handle the two possible outputs.

Let’s see another example:

The logic of `ContainsEmployeById` is basically the same as `FindEmployeById` but without returning the employee. Now let’s say that those functions reach the DB, we have a performance problem here. Let’s introduce a similar but different pattern: the `boolean` function when returning `true` will also return the data we search for. It looks like this:

A common use of this pattern is `int.Parse` and `[int.TryParse](https://docs.microsoft.com/en-us/dotnet/api/system.int32.tryparse?view=netframework-4.7.2#System_Int32_TryParse_System_String_System_Int32__)`.

The fact that I can separate a function to two functions and each has its own usages is a sign that returning `null` is a **code smell for violating the Single Responsibility Principle**.

### Splitting the interface

A practical guideline we can derive from the [Liskov principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) is that a class **must implement all functions** of an interface it implements. Returning `null` or throwing an exception are ways to not implement a function. So returning `null` is a **code smell for violating the Liskov principle.**

If a class can’t implement a specific interface’s function **we can move that function to another interface** and each class will implement only the interface it can.

Now instead of asking `employee.HasManager` — which we will do if we used the first approach “Splitting the function into two” — we ask employee is `IManagedEmployee`.

### I am not working alone and not on a greenfield project. What now?

In existing codebases, there area lot of code returning reference types. We cannot know if `null` is valid output or not.

The first quick win I wish you to have is to **change your coding conventions** so `null` is not a valid input or output to a function. Or, at least when you decide that `null` is a valid output, use **the Option type.**

There are some tools which can help to enforce this convention like [ReSharper](https://www.jetbrains.com/help/resharper/Code_Analysis__Value_Analysis.html) and [NullGuard](https://github.com/Fody/NullGuard). I guess, although I haven’t tried this yet, you can add a [custom rule to SonarQube](https://docs.sonarqube.org/display/DEV/Adding+Coding+Rules) which will alert when the word `null` appears.

I would love to know what you think. Are you going to embrace this convention? And if not, why? What’s holding you back?

If you encounter a scenario in which you think returning `null` is the right design choice, or the patterns I suggested are not good, I would love to know.

Thanks [Mark Kazakov‏](https://www.linkedin.com/in/mark-kazakov-98994197/) for the funny meme, [Alex Zhitnitsky](https://www.linkedin.com/in/alex-zhitnitsky-86567238/) from OverOps for answering my questions, [Baot](https://www.facebook.com/baot.tech/) for organizing a great writing event for new bloggers, [Itzik Saban](https://www.linkedin.com/in/itzik-saban-54b93829/) , [Amitay Horwitz](https://www.linkedin.com/in/amitayhorwitz/) and [Max Ophius](https://www.facebook.com/max.ophius) for giving me feedback.

