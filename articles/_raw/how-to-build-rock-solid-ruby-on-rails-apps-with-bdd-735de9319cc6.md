---
title: How to build rock-solid Ruby on Rails apps with BDD
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T02:15:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-rock-solid-ruby-on-rails-apps-with-bdd-735de9319cc6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C238nEDrqoXjgjjASFwfRg.png
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Marko Anastasov

  Learn best practices for building sustainable web apps with behavior-driven development.



  _“Why do we fall sir? So that we can learn to pick ourselves up.”_—Alfred (Michael
  Cane) in Batman Begins


  I built my first Rails app ten ye...'
---

By Marko Anastasov

#### Learn best practices for building sustainable web apps with behavior-driven development.

![Image](https://cdn-media-1.freecodecamp.org/images/w-cGH0pyQD50cfQWGoB0EBzDfkdm91xuVbiZ)

> _“_Why do we fall sir? So that we can learn to pick ourselves up._”_   
> —Alfred (Michael Cane) in Batman Begins

I built my first Rails app ten years ago. I’ve tried all approaches, and if there’s one thing that I’m certain of, it’s that I can’t work without writing tests. And writing tests first is what has helped me advance my programming skills the most.

It’s pretty simple. We want to feel and be as productive on day 1000 as we are on day 1 of the project. We want to be fast. For that we need clean code.

We can’t get everything right in the first pass, so we need to refactor. However, we can’t refactor under a constant fear that we’ll break stuff and ship bugs to production without knowing it. We need confidence that when we do break the code, we can detect and fix the issue right away.

Where does confidence come from? The automated test suite gives us confidence. Confidence that we can change, remove, or add new code, and no major problem will happen as long as our tests are passing.

So if tests are the foundation, let’s write them first. Do that for a while, and you’ll notice how clean and effective both your code and tests come out.

### Understanding the “behavior” point of view

When applying test-driven development (TDD), developers can easily fall into the trap of using unit tests to test what an object or method **is**, rather than what it **does**, which is a lot more useful.

An example would be writing a test which asserts that a collection of comments is specifically an array, and not one of its unique features, such as being sorted by time. In most cases, it shouldn’t matter if we change the implementation of that collection to return a custom enumerable class. More generally:

> Changing the implementation of an object shouldn’t break its test suite, as long as what the object does remains the same.

**Behavior-driven development** (BDD) puts focus on behavior — what a thing does — on all levels of development.

Initially, the word “behavior” may seem strange. Another way to frame this is to think about descriptions. We can describe every low-level method, object, button or screen to another person — and what we will be describing is exactly what a behavior is. Adopting this approach changes the way we approach writing code.

#### The “Given / When / Then” communication pattern

Most problems in software development are communication problems. For example, product manager fails to describe every use case of a proposed functionality. Developers misunderstand the scope of a feature. Product team doesn’t have a protocol to verify if a feature is done.

BDD simplifies the language we use to describe scenarios in which software should be used:

> _*Given*_ some context or state of the world,

> *_When*_ something happens,

> *_Then*_ we expect some outcome.

_Given, When, Then_ are simple words we can use to describe a complex feature, code object, or a single method equally well. It’s a pattern that all members of the team in various roles can understand.

These expressions are also built-in in many testing frameworks, such as [Cucumber](https://cucumber.io). A clear formulation of the problem and the solution that we need to implement helps us write better code.

### Overview of BDD tools for Rails

[Ruby on Rails](http://rubyonrails.org) was the first web framework to ship with an integrated testing framework. This acted as a springboard for further advancements of the craft.

At the same time, the expressiveness of Ruby and the productivity boost in developing web applications with Rails attracted many experienced and high-profile engineers to the community early on.

When you generate a new Rails application with default options, it sets the scene for testing using `test/unit`, a testing library that comes with Ruby. However, there are tools which make BDD easier to apply. I recommend using [RSpec](http://rspec.info/) as the main testing library and [Cucumber](https://cukes.info/) for writing high-level acceptance tests.

#### RSpec

RSpec is a popular BDD testing library for Ruby. Tests written using RSpec — called **specs** — are executable examples of expected behavior of a piece of code in a specified context. This is much easier to understand by reading the following code:

```
describe ShoppingCart do  context "when first created" do    it "is empty" do      shopping_cart = ShoppingCart.new      expect(shopping_cart).to be_empty    end  endend
```

Well-written specs are easy to read, and as a result, understand. Try reading the code snippet above out loud. We are **describing** a shopping cart, saying that, given a blank context, when we create a new shopping cart, we `expect(shopping_cart).to be_empty`.

Running this spec produces output which resembles a specification:

```
ShoppingCart  when first created    is empty
```

We could use RSpec to specify an entire system, however we can also use a tool which helps us write and communicate even more naturally.

#### Cucumber

As I explained in the first chapter of this guide, we want to test-drive the analysis phase of every new feature. To do that, we need **customer acceptance tests** to drive the development of the code which will actually implement the feature.

If you are a developer working in a sufficiently complex organization, you may want to have somebody else, like a customer or product, manager write acceptance tests for you (disclaimer: I’ve never worked in such environment). In most cases, the developer writes them. This is a good practice, because it helps us understand better what it is that we need to build. Cucumber provides the language and format to do that.

Cucumber reads plain text descriptions of application features, organized in **scenarios**. Each step in the scenario is implemented using concrete code, and it automates interaction with your application from the user’s standpoint. For example:

```
Feature: Reading articles
```

```
Scenario: Commenting on an article  Given I am logged in  And I am reading an article with "2" comments  When I reply to the last comment  Then the article should have "3" comments  And I should be subscribed to follow-up comments
```

If this were a web application, the scenario above could automatically boot a test instance of the application, open it a web browser, perform steps as any user would do, and then check if certain expectations have been met.

### The BDD cycle in Rails

In practice, BDD implies an **outside-in** approach. We start with an acceptance test, then write code in the views, and work our way down to the models. This approach helps us discover any new objects or variables we may need to effectively implement our feature early on, and make the right design decisions based on this.

The BDD cycle in Rails consists of the following steps:

1. **Start with a new Cucumber scenario**. Before you write it, make sure to analyze and understand the problem. At this point you need to know how the user interface allows a user to do a job. Do not worry about the implementation of scenario steps.
2. **Run the scenario and watch it fail**. This will tell you which steps are failing, or pending implementation. At first, most of your steps will be pending (undefined).
3. **Write a definition of the first failing or pending spec**. Run the scenario and watch it fail.
4. **Test-drive the implementation of a Rails view** using the red-green-refactor cycle with RSpec. You’ll discover instance variables, controllers and controller actions that the view will need to do its job. This is also the only phase which has been proved to be optional in practice. An alternative approach is to simply prepare the views and controllers before moving on to the next step.
5. **Test-drive the controller** using the red-green-refactor cycle with RSpec. Make sure that the instance variables are assigned and that the actions respond correctly. The controllers are typically driven with a mocking approach. With the controller taken care of, you will know what the models or your domain objects should do.
6. **Test-drive domain objects** using the same red-green-refactor cycle with RSpec. Make sure that they provide the methods needed by the controller and the view. If you are working on a new feature for which a model does not exist yet, you should now generate the model and the corresponding database migrations. At this point you’ll know exactly what you need them to do.
7. Once you have implemented all the objects and methods you need and the corresponding specs are passing, **run the Cucumber scenario you started with to make sure that the step is satisfied**.

![Image](https://cdn-media-1.freecodecamp.org/images/8WeEWJUk4SLlPc0tC5VrxooSOTwqSZaRHvr0)
_The BDD cycle in Ruby on Rails web development_

Once the first scenario step passes, move onto the next one and follow the same steps. Once your entire scenario has been implemented — the scenario is passing, along with all underlying specs — take a moment to reflect if there is something that you can **refactor** further.

Once you’re sure that you’ve completed the scenario, either move on to the next one, or show your work to others. If you work with a team, **create a pull request** or an equivalent request for a code review. Opening a pull request should automatically trigger a [continuous integration](https://semaphoreci.com/blog/2017/03/02/what-is-proper-continuous-integration.html) build. When there are no more related scenarios left, show your work to your project manager or client, asking them to verify that you’ve built the right thing by deploying a feature branch to a staging server.

This post is adapted from [**Rails Testing Handbook**](https://semaphoreci.com/ebooks/rails-testing-handbook), a free ebook published by [Semaphore](https://semaphoreci.com). If you’ve made it this far and want to see some hands-on examples of writing behavior-driven code, [download the book](https://semaphoreci.com/ebooks/rails-testing-handbook) and let me know what you think of it. Thanks!

