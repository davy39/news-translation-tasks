---
title: A practical introduction to Test Driven Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-01T16:34:33.000Z'
originalURL: https://freecodecamp.org/news/practical-tdd-test-driven-development-84a32044ed0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Yd-MlvHYafduLBLFkSgH4Q.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: test driven development
  slug: test-driven-development
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Luca Piccinelli

  Test Driven Development is hard! This is the untold truth about it.

  These days you read a ton of articles about all the advantages of doing Test Driven
  Development (TDD). And you probably hear a lot of talks at tech conferences tha...'
---

By Luca Piccinelli

#### Test Driven Development is hard! This is the untold truth about it.

These days you read a ton of articles about all the advantages of doing Test Driven Development (TDD). And you probably hear a lot of talks at tech conferences that tell you to “Do the tests!”, and how cool it is to do them. 

And you know what? Unfortunately, they are right (not necessarily about the “cool” part, but about the useful part). **Tests are a MUST**! The typical advantages we list when it comes to talking about TDD are real:

* You write better software
* You have protection from breaking the world when new features are introduced
* Your software is self documented
* You avoid over-engineering

Even if I’ve always agreed with these advantages, **there was a time when I thought that I didn’t need TDD to write good and maintainable software.** Of course, now I know I was wrong, but why did I have this idea despite the shiny magic of the pros? The reason is just one: and let me ask Rihanna to say it for me…

### **The Cost!**

It costs a lot! Probably someone is thinking “_but it costs even more if you don’t do the tests_” — and this is right, too. But these two costs come at different times:

* you do TDD ➡ you have a cost **now**.
* You don’t do TDD ➡ you will have a cost **in the future**.

So, how do we come out of this impasse?

The most effective way to get something done is doing it as naturally as possible. The nature of people is to be lazy (here software developers are the best performers) and greedy, so you have to find your way of **reducing the costs now**. It’s easy to say, but so hard to do!

Here I will share my experience and what has worked for me in turning the benefit/cost ratio to my favour.

But before I do that, let’s analyze some typical difficulties in applying TDD.

### Are you able to test the sum of two numbers?

Generally speaking, theory is not optional; you have to master it in order to master the practice. However trying to apply at once all the theoretical knowledge you’ve previously acquired could have the following effect:

The typical theory lesson on TDD starts with something like this:

And here you are like

Then comes this:

* red ➡ green ➡ refactor cycle
* unit, acceptance, regression, integration tests
* mocking, stubs, fakes
* if you are lucky (or maybe unlucky ?), someone will tell you about contract testing
* and if you are very lucky (or maybe very unlucky ?) you will touch legacy codebase refactoring

The going gets tough, but you are an experienced developer and all these concepts are not that hard to handle for you. Then class ends; you go home, and throughout the next days you diligently do some code katas to fix the concepts just learned. So far so good.

#### The struggle is real

Next comes a real world project, with real deadlines and real timing costs — but you are motivated to apply your shiny new TDD. You start thinking about the architecture of your software and start writing tests for the first class and the class itself — let’s call it **Class1**.

Now you think about the first user of Class1, let’s call it **UsageOfAClass,** and again you test and write it. Class1 is a collaborator of UsageOfAClass, so are you going to mock it? Ok let’s mock it. But what about real interactions of Class1 and UsageOfAClass? Maybe you should test them all as well? Let’s do it.

At this point, inside of you, you start hearing a little voice that says “_I_ _would develop much faster if I didn’t have to write these tests…_”. You don’t listen to this evil voice and proceed straight to the next test.

**Class2** is going to be used by UsageOfAClass and it persists itself inside a Db. So, do we have to test Class2, its interaction with UsageOfAClass, and the persistence in the Db? But wait… did anyone mention how to cope with I/O testing during the TDD theory class?

The theory behind TDD is not that hard to understand, but applying it to the real world can be really complex if you don’t approach it the right way.

### Just do it

We should always keep in mind that theory must be bent to our needs and not the contrary.

The main goal is to get the job done. So my advice is, **just do it**!

**Start simple and just do your task up to the end.** Then, when you get stuck in some theoretical mind loop like:

* is this a unit or an integration test?
* here should I mock it or not?
* oh crap, here I should write a new collaborator, so a brand new suite of infinite unit tests just to write “hey, banana”…

just forget about theory for a while and take a step forward. Just do it as it comes!

Once you are done with your task, have a look back at your work. **Looking back** at the completed job, it will be much easier to analyze what would have been the right thing to do.

### Practical TDD

Just do it. By the way, I think this is also the right approach to TDD.

What was wrong in how we built Class1, Class2 and UsageOfAClass? **The approach.**

This is a bottom-up approach:

* analyze the problem
* figure out an architecture
* start building it from unit components

This approach is the best friend of **over-engineering**. You typically build the system in order to prevent changes that you think will come in the future, without knowing if they actually will. Then when some requirement changes, it typically happens in a way that doesn’t fit your structure, no matter how good it is.

For me **the key to drastically reducing the immediate cost** of writing with TDD has been to take a top-down approach:

1. bring a user story
2. write a very simple test of a use case
3. make it run
4. go back to step 2 until all use cases are complete

While doing this process, don’t worry too much about architecture, clean code (well, remember at least to use decent variables names) or any kind of complication that is not currently needed. Just do what you know you need **now**, up to the end.

**Tests of the story clearly state what are the current and known requirements.**

Once you are done, take a look at your big ball of spaghetti mud code, get over the shame, and look deeper at what you have done:

* it works! And tests prove it.
* All the system is there, **and just what is actually needed to get the job done**.

Now you have an overview of all the parts of your system, so you can refactor with the knowledge of the domain that you couldn’t have had when you started from scratch. And tests will make sure that nothing will break while refactoring.

### Refactoring

The best way for me to start to refactor is to identify areas of responsibility and separate them in private methods. This step helps identify responsibilities and their inputs and outputs.

After that, classes of collaborators are almost there and you just need to move them into different files.

As you proceed, first write tests for the classes that pop out from the process and iterate until you are satisfied with the result. And remember, if you get stuck somewhere, just do it! If you do something bad, once you are done you will have more information on how to get over the mistake the next time you face it. **Getting the job done is the priority**, to the best of your current abilities.

This way, if you analyze your errors to learn from them, you will also refine your abilities.

### The next user story

Continue developing your product following these steps:

* take a story
* make it work completely in a “test — code” cycle.
* refactor

While adding features you will continue to change your software and maybe even its structure. But as the system grows, the cost of change will maintain a linear growth thanks to the two main features of TDD:

* architecture discovery (that helps to control the complexity)
* protection from breaking changes

The system will not be over-engineered, as architecture is going to emerge as stories get completed. You don’t think about what could be future requirements; if you end up needing it, then the cost to implement it will be low.

#### What can make it go wrong?

The size of the story. What you build up to the end must be the right size. Not too big (otherwise it will take too much time to get any feedback) or too small (otherwise you won’t have the overview).

What if the story is too big? Split it up in pieces that can be built from the start to the end.

### What’s next?

In the next article I will give a practical example of the concepts I explained here. We will implement, step by step, the [Bowling Game kata](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata) starting from an acceptance test.

It is not a real world problem, but it has enough complexity to see how TDD can help in handling it.

Please share your opinion and suggestions about this article. Do you agree with me or do you think that all this is a bunch of rubbish? Let me know what you think in comments; it would be very nice to start a conversation on TDD and share our experiences.

I want to thank [Matteo Baglini](https://www.freecodecamp.org/news/practical-tdd-test-driven-development-84a32044ed0b/undefined) for helping me to find my way through a practical approach to software development and TDD.

Thank you for reading!

Cover image courtesy of [testsigma](https://testsigma.com/blog/ai-driven-test-automation/).

