---
title: Why Is Test-Driven Development Useful?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-08T10:59:55.000Z'
originalURL: https://freecodecamp.org/news/why-test-driven-development-4fb92d56487c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1_HDbOMLg5KeS8tYsbpJYg.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: TDD (Test-driven development)
  slug: tdd
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Fagner Brack

  Tips on how to apply TDD more efficiently, and why it''s a valuable technique

  There''s a common pattern we follow when we start a project using TDD. We describe
  the specifications of what we expect the system to do in the form of a spec...'
---

By Fagner Brack

#### Tips on how to apply TDD more efficiently, and why it's a valuable [technique](https://medium.com/@fagnerbrack/the-trick-to-write-better-software-lies-on-the-technique-944015f84ce4)

There's a common pattern we follow when we start a project using TDD. We describe the specifications of what we expect the system to do in the form of a special test. This "special test" can be an end-to-end with the front-end or an integration test that executes an HTTP request to test the back-end.

It's the first test we write. We do it before a single line of code is written. That special test will serve as a guideline to make sure we don't break anything that prevents the regular flow from working. If we don't do that and rely solely on unit tests, there's a chance that, eventually, we will have all tests passing but the server will not be starting or the user won’t be able to do anything on the screen.

> When starting a project using TDD, there's a common pattern to create a special test to make sure we don’t break anything that prevents the regular flow from working.

After we make that special test pass with a naive implementation (or we can keep it failing if we are using [ATDD](https://www.agilealliance.org/glossary/atdd/) to drive the application internals), we start building the units of the system using a similar pattern on a micro level, never breaking any test we created earlier. We describe each unit of the system through a failing test and make it pass with a naive implementation first. Then, we identify [smells](https://medium.com/@fagnerbrack/code-smell-92ebb99a62d0) and [refactor](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) it if necessary so that we can keep the cycle going over and over again.

That’s called the [Red/Green/Refactor cycle of TDD](http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html).

This cycle will drive us to build all the pieces of our application with enough confidence that it will be robust and maintainable. It will also expose problems early if we were to get stuck due to the wrong assumption of how the API is supposed to behave.

There's one important thing we should be careful about: we should **avoid [refactoring](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) code or adding a new test while another test is failing.** If we do that, there's a high chance we will get stuck because of the unnecessary cognitive load of worrying about another rule we have already covered. To prevent that, we need to fix the failing test before starting anything else.

> In TDD, we should **avoid [refactoring](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) code or adding a new test while another test is failing.**

There are circumstances where one would prefer writing tests after writing the code. However, there are some negative effects that come with that approach:

* We can miss important functionality because it’s harder to know if the coverage matches our expectation.
* It can [create false positives](https://medium.com/@fagnerbrack/mocking-can-lean-to-nondeterministic-tests-4ba8aef977a0) because we won’t see a failing test first.
* It can make us [over-engineer](https://hackernoon.com/how-to-accept-over-engineering-for-what-it-really-is-6fca9a919263) the architecture because we won’t have any guidelines to force us to write the minimum amount of code that fits in our most basic requirements.
* It's harder to validate if the message for the failing test is clear and pointing to the cause of that failure or not.

One thing to keep in mind is that TDD can be posed as a discipline, but [there's no way to create a discipline for writing tests after the production code](http://blog.cleancoder.com/uncle-bob/2017/03/07/SymmetryBreaking.html).

There are [cases when there's no value in applying TDD or automated testing](https://8thlight.com/blog/uncle-bob/2014/04/30/When-tdd-does-not-work.html) at all. It's when we're testing some IO layers, support functions for the tests, or things built using a declarative language like HTML or CSS (we can test the visual in CSS, but not the CSS code). However, testing is a fundamental part of the process that ensures a complex piece of functionality satisfies a set of expectations. That alone allows us to be confident enough that each part of the system works as expected.

> There are cases when there's no value in applying TDD or automated testing at all, like when testing IO layers, support functions for the tests, or code written with a declarative language.

There's a concept called [The Transformation Priority Premise](https://8thlight.com/blog/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html). The [TL;DR](https://en.wikipedia.org/wiki/TL;DR) is that there are some transformations we can apply when making the code more generic in the "green" phase of the TDD cycle.

"[Refactor](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3)" is when we change the structure of the code without changing its behavior. The Transformations are not called "[refactoring](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3)" because they change the structure **and the behavior** of the code to make it more generic.

An example of using the Transformation Priority is when we make a test that forces us from returning a single constant to returning an argument that will contain more than one value. In this case, it's the **constant->scalar** priority transformation.

> _So what are these transformations? Perhaps we can make a list of them:_  
>   
> _*** ({}–>nil)**_ no code at all -> code that employs nil  
>   
> _*** (nil->constant)**_  
>   
> _*** (constant->constant+)**_ a simple constant to a more complex constant  
>   
> _*** (constant->scalar)**_ replacing a constant with a variable or an argument  
>   
> _*** (statement->statements)**_ adding more unconditional statements.  
>   
> _*** (unconditional->if)**_ splitting the execution path  
>   
> _*** (scalar->array)**_  
>   
> _*** (array->container)**_  
>   
> _*** (statement->recursion)**_  
>   
> _*** (if->while)**_  
>   
> _*** (expression->function)**_ replacing an expression with a function or algorithm  
>   
> _*** (variable->assignment)**_ replacing the value of a variable.  
>   
> _There are likely others._  
>   
> _— Excerpt from [The Transformation Priority Premise](https://8thlight.com/blog/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html) article_

> In TDD, The Transformation Priority Premise can give us a guideline for the "green" phase.

[Writing correct software is hard](https://medium.com/@fagnerbrack/the-trick-to-write-better-software-lies-on-the-technique-944015f84ce4). TDD is a common pattern where we use the tests to help driving the implementation of our system while retaining a huge percentage of test coverage. However, it's not a [Silver Bullet](https://medium.com/@fagnerbrack/how-to-reject-the-belief-on-the-silver-bullet-1d86b686acbb).

If we are using TDD, we should avoid [refactoring](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) the code when the tests are failing. To make it pass in the "green" phase, we use the Transformation Priority Premise to guide us in the most naive implementation approach we can take before [refactoring](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3).

In comparison with other ways of writing tests, TDD can take more time in the beginning. However, as with every new skill, with enough practice we will reach a plateau, and the time it takes to apply TDD will be no different than the time it would take to write tests in a traditional way.

The difference now is that your software will be less likely to behave in a way you didn't expect.

And for all practical means, that's no different than 100% test coverage.

Thanks for reading. If you have some feedback, reach out to me on [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) or [Github](http://github.com/FagnerMartinsBrack).

