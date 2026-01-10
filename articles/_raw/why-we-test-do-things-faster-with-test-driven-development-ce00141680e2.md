---
title: Why we test — do things faster with Test-Driven Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-17T15:40:24.000Z'
originalURL: https://freecodecamp.org/news/why-we-test-do-things-faster-with-test-driven-development-ce00141680e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jit5trmBsttM0DIxOKhizA.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Rainer Hahnekamp

  As we all know, unit tests provide us with some kind of safety net. They give us
  a program we can use to validate that a system works the way it is supposed to —
  especially after we make modifications or extensions.

  You are doing ...'
---

By Rainer Hahnekamp

As we all know, unit tests provide us with some kind of safety net. They give us a program we can use to validate that a system works the way it is supposed to — especially after we make modifications or extensions.

You are doing a lot of work up front by writing these tests. If you take the perspective that the real benefit comes during maintenance and extension work, then you will see testing as part of beautification or clearing up.

In this article I want to show that, in the context of a common web application, the typical validation process takes much longer than you think and that writing tests before the actual code will let you get the work done faster.

#### You may think manual checks are fast

The usual way for verifying a modification to a common web application is to validate its behavior in a browser just like an end user would do it. That means you change code, reload the browser, click on a button, and see if the expected result happens.

The duration of this process depends very much on your environment and the part of the application you are working on. If you are “lucky” to be using frameworks like Angular and Spring, their ability to support large projects comes at a price with each bootstrap and compilation. Consider this optimistic example:

* 10-second bootstrapping
* 5-second compilation
* 5-second reload and test

So we are already at 20 seconds for a manual check. That assumes that your client-side and server-side build tools, like Webpack and Maven, are optimised.

![Image](https://cdn-media-1.freecodecamp.org/images/1XdNOR82xVsdoCNIlgGw7khYRfNi2RWod0rN)
_Manual Checks require more time than you might think_

#### But checks take longer than you think

However, quite often other things hugely extend the validation time. Sometimes we developers overlook typos in the first run. And in the second. (Or the third!) Each one multiplies the time you spend checking the code.

Consider the more serious case where you are working on some kind of payment functionality in an online shop. Checking whether a button triggers an appropriate action may take little time. But the typical checkout process containing fields to fill out will take much more. If you are working on long-running jobs it easily goes beyond one minute.

You could argue that using an interpreted language might speed things up. That is true, but the point here is that you easily end up having manual testing cycles, each lasting a minute, multiple times. And that’s just to validate if some lines of code had the desired effect.

#### TDD speeds things up

Doing test driven development (TDD) right — writing the test first and the code afterwards — brings you in the powerful position that you can run virtually any specific part of isolated code within seconds.

Remember that unit tests are only testing a single class. All dependencies of that class are being mocked-up — especially for I/O operations like databases, file systems, or networking.

Replacing manual validation with these tests improves the speed dramatically. You also end up having better quality code, but more on that in a later post. The last validation run will be the manual one. That is where you actually check if things are as they are supposed to be as an end user in the browser.

#### Yes, even for those special cases

You can always come up with some situations where you find it completely counter-intuitive to apply TDD.

Think about what I call “experimental work” — the trial-and-error you have to do to discover how to use a library or service you are not very familiar with. You are already working against an unknown component. Why make it more complicated by bringing a testing framework layer around your main code?

Or consider the starting phase of a web application where you are usually working on the front end part — mostly HTML and CSS with a small part of server-side code that only “moves” data from the database to the browser.

In both cases you should apply TDD from the beginning. Creating unit tests for “experimental work” lets you do the trial-and-error part faster and equips you with a toolset you can always come back to later. Your “moving data from the database to the browser” code will grow in time, resulting in an untestable codebase where you cannot run code parts isolated from each other. You will have to do the time-consuming manual tests by yourself.

#### TDD is worth the effort

It is your responsibility to find ways to come to testable code and integrate it in your working process. Someone is paying you as an expert. That person does not understand why you sit there waiting for an application to boot or you are clicking on buttons — work that a not so highly-skilled person could do.

Writing unit tests the right way is a skill you usually do not learn at universities or in normal programming education. It is hard the first time(s), and will require quite a few hours to adjust, but you will see the first results soon and never look back.

Save your time by investing in good unit tests from the beginning and start with a modularized application from the first commit.

_Originally published at [www.rainerhahnekamp.com](https://www.rainerhahnekamp.com/en/why-we-test-do-things-faster-with-test-driven-development/) on March 15, 2017._

