---
title: Test-driven development might seem like twice the work — but you should do
  it anyway
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T11:25:44.000Z'
originalURL: https://freecodecamp.org/news/isnt-tdd-test-driven-development-twice-the-work-why-should-you-care-4ddcabeb3df9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C1mf126YNJHmaaMUbaYYyQ.png
tags:
- name: General Programming
  slug: programming
- name: Quality Assurance
  slug: quality-assurance
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Navdeep Singh

  Isn’t Test Driven Development (TDD) twice the work? Should you do it anyway?

  The short answer to the first question is NO. On the surface, it may seem like without
  TDD, time is only required to create the feature. With TDD, you need ...'
---

By Navdeep Singh

Isn’t Test Driven Development (TDD) twice the work? Should you do it anyway?

The short answer to the first question is **NO**. On the surface, it may seem like without TDD, time is only required to create the feature. With TDD, you need time to create the test AND create the feature, thus doubling the development time required.

What you’re not considering is the amount of time required for QA testing and debugging when the feature isn’t performing properly.

> Case studies were conducted with three development teams at Microsoft and one at IBM that adopted TDD. The results of the case studies indicated that the pre-release defect density of the four products decreased between 40% and 90% relative to similar projects that did not use the TDD practice.

> Subjectively, the teams experienced a 15–35% increase in initial development time after adopting TDD. ([source](https://www.microsoft.com/en-us/research/wp-content/uploads/2009/10/Realizing-Quality-Improvement-Through-Test-Driven-Development-Results-and-Experiences-of-Four-Industrial-Teams-nagappan_tdd.pdf))

That 40–90% decrease in pre-release defects means that QA teams and customers weren’t finding and reporting those issues. Engineering wasn’t trying to recreate bugs and develop patches, all of which have associated costs.

![Image](https://cdn-media-1.freecodecamp.org/images/rsCNd3MzBvEUjx9bQ-QYiXjG1vaZ4V35yZCr)
_Number of Iterations per task_

When discussing TDD, we consider a task to be a subset of a requirement that can be implemented in a few days or less. TDD software engineers develop production code through rapid iterations, as shown in the figure above.

### What Is TDD?

![Image](https://cdn-media-1.freecodecamp.org/images/JWJWnEz2BCL7beWEwIlBRSKv4Qretm6OXGtn)

Test-Driven Development is an approach to writing software in which the developer uses specifications to shape the way they implement a feature. For short, we describe it as the “red-green-refactor cycle”.

Before writing any code that adds new functionality to an application, the developer first writes an automated test describing how the new code should behave, and watches it turn red (fail to pass). They then write the code to the specification, and the test turns green (it passes). Finally, the developer takes a little time to make sure that the code just written is as clean as possible (refactoring).

### Why you should care about TDD

Automated testing gives your software developers the confidence to make changes to the software and to know that no bugs were created as a byproduct.

Additionally, it allows more agility for developers who aren’t familiar with the details of the software to confidently modify the source code without introducing errors.

Let’s discuss some really cool advantages of TDD.

#### 1. TDD Helps You Prevent Bugs

![Image](https://cdn-media-1.freecodecamp.org/images/FOKSPU5-luiwfkdcFbOqWqRWYBhJyD3TwncA)

First, test suites ensure comprehensive test coverage of the codebase, so bugs are less likely to pop up unnoticed. Second, test suites allow developers to work out potential issues before the application is ready to go into production. Finally, because test suites are constantly maintained, they guarantee software quality.

#### 2. Self Explanatory code (well-documented)

Because refactoring code is a built-in step in TDD, you end up with a much cleaner codebase as you go. Apps built with TDD tend to have less duplication, fewer edge cases that aren’t thought through, and a better overall architecture.

The test serves as a specification for what the code that will be written should **do**. As long as you’re writing good stories, your development team should be able to build exactly what you asked for. If your team agrees to use [Acceptance Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development#TDD_and_ATDD), you can even write tests that describe how you want it to work in plain English!

#### 3. Avoid the bugger debugger problem

![Image](https://cdn-media-1.freecodecamp.org/images/VFYfcFvkkNINz-pUynhdPkrrXDXYwt6SKECJ)

Typically, when talking tech about software development, there are two main types of testing that can be integrated: functional and non-functional. These two types of testing practices are further divided into numerous types of testing techniques as you can see here:

![Image](https://cdn-media-1.freecodecamp.org/images/U4QtKTWFv4bTw1VsmXZTSIfgG2xPwz7gBLTx)
_And the list goes on_

It becomes really important to strategize the testing plan before project commencement, since that helps in clearly defining the roles and responsibilities of developers with respect to testers when it comes to testing.

For example:

* Unit and Integration tests to be performed by developers before handing out builds to testers
* User acceptance testing to be performed by the testers
* Performance testing and UI testing should be done by both

A brief description of a few very important testing methodologies from the diagram above, that should be included in almost every test plan, are covered below.

**Unit Testing** involves testing individual units of source code to determine if they are fit for use. Intuitively, one can view a unit as the smallest testable part of an application. [**Faking, Mocking, and Stubbing**](https://www.martinfowler.com/articles/mocksArentStubs.html) **are indispensable while writing unit tests for code which has API interactions_._**

**Integration testing** involves a combination of two or more “units” being tested. Integration tests verify that the components of the software all work together or “integrate” appropriately.

**Performance testing** is used to ensure that software applications will perform well under their expected workload. The features and functionality supported by a software system are not the only concerns. A software application’s performance, like its **response time, reliability, resource usage,** and **scalability**, matters**.** The goal of performance testing is not to find bugs, but to eliminate performance bottlenecks.

#### 4. You can forecast troubles

![Image](https://cdn-media-1.freecodecamp.org/images/KGS6NPx9YOIVplTrknkvNnydeZpmVo9pdtPZ)
_A solid TDD approach alarms you about troubles upfront_

The benefit of a comprehensive test suite is that it alerts you to changes early. For example, if your checkout flow stops charging users’ credit cards, you’ll know it right away, because the tests will fail. It also means that if someone makes a mistake and something doesn’t work the way it was supposed to, it will be obvious.

This is good, because it will give you a chance to fix it before it goes to production. If it becomes necessary down the road, you can even start a campaign of deep refactoring without fear, because you’ll have an ironclad test suite that will remain green.

#### 5. Save Money

![Image](https://cdn-media-1.freecodecamp.org/images/dCY0sc49bVWFBMBR5Fk-dKyUTTjEEnwDBvMw)

When code is complicated, it gets much harder to get anything done — one little change over here can result in a big problem over there. When following TDD, developers can make changes with confidence and your QA team will catch fewer regressions. In development speak, **“time saved is equal to money earned.”**

#### 6. Invest the saved time in innovations and research

![Image](https://cdn-media-1.freecodecamp.org/images/u7Z0aFmVNsdtWOYuf2Z80vDXQKgG1DfuL83g)
_Spend the saved time in innovation_

If we just adopted a TDD approach, much of this money (time saved as expressed in point 5) could be spent on new innovations instead.

#### **7. TDD Helps You Avoid Scope Creep**

The nightmare of any project manager is scope creep — any unexpected growth in the scope of work which leads to delays in project delivery.

Scope creep can happen for various reasons: poorly defined tasks, misinterpretation of project requirements, lack of documentation, and so on. There are many methods aimed at mitigating scope creep, and TDD is one of them.

Thanks for reading! Please share it if you found it useful :)

