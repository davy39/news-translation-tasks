---
title: Using the Simple Factory design pattern is a lot like making cheesecake
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T12:47:05.000Z'
originalURL: https://freecodecamp.org/news/using-the-simple-factory-design-pattern-is-a-lot-like-making-cheesecake-92a119cde191
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JtDoAdFERT4heuYF6gGpyg.png
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: software design patterns
  slug: software-design-patterns
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sihui Huang

  Factory Patterns are about encapsulating object creation.

  But before diving into details of the patterns, let’s talk about cheesecake. Because
  cheesecake is about … happiness! ???


  Let’s focus our gaze on six of my personal favorites: ...'
---

By Sihui Huang

Factory Patterns are about encapsulating object creation.

But before diving into details of the patterns, let’s talk about cheesecake. Because cheesecake is about … happiness! ???

![Image](https://cdn-media-1.freecodecamp.org/images/1*DX0_N89jW5HSmgl5FEuLPQ.png)

Let’s focus our gaze on six of my personal favorites: Original Cheesecake, Ore0 Cheesecake, Coffee Cheesecake, Tiramisu Cheesecake, S’mores Cheesecake, and Hazelnut Cheesecake.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GB-APPbSeUEBzrrmtsc09w.png)

And here is how we make a cheesecake:

Create a cheesecake instance based on the selected type -> Make crust -> Add layers on top of the crust -> Bake it -> Refrigerate it -> Add toppings to the cake -> Return the cake! ???

Wait … that Mango key lime cheesecake looks very tempting ???.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oxZrWU870mXJeFCF4RqPBw.png)

Let me add it to my list:

One second …

I have been having too much caffeine lately. I don’t want the coffee cheesecake to be on my list anymore. Let me update the _make_cheesecake_ method again.

Oooh…. they have a low carb version of cheesecake. It’s always nice to have a low carb option. It needs to be on my list!

So since the first time we defined `make_cheesecake`, we have updated it three times. Each time, the change was for the exact same reason — to update my cheesecake list. And everything else, `make_crust`_,_ `add_layers`_,_ `bake`_,_ `refrigerate`_,_ and `add_toppings`, remained the same.

Sorry for changing my mind every three seconds. But as they say: **change is the only constant in life (and software development).**

To be honest, we will need to change the list at least one more time: pumpkin cheesecake will be available from September. It’s WORLD FAMOUS! Without a doubt, we need to add it to the list once September arrives. Oops, that means we need to remove it from the list when the holiday season passes.

It’s obvious that my cheesecake list changes often.

There is a design principle: **encapsulate what varies**.

We should give it a try.

### It’s time for a Cheesecake Factory!

The `CheesecakeFactory` is a simple class. All it does is create and return the correct cheesecake based on a given type.

With the help of `CheesecakeFactory`, the `make_cheesecake` method becomes much simpler.

The `make_cheesecake` method can now focus on the actual steps that go into making a cheesecake without having to worry about different cheesecake types.

Our `CheesecakeFactory` is an example of using the Simple Factory. **Simple Factory is used for encapsulating object creation.**

### The Factory Pattern Family

Besides Simple Factory, there are two other members of the Factory Pattern family: **Factory Method** and **Abstract Factory.** We won’t go into the details of these two patterns.

In a nutshell, Factory Method and Abstract Factory use inheritance. Factory Method is about creating one type of object, and Abstract Factory is about creating a family of different types of objects. All three of them are about encapsulating object creation by using the design principle: encapsulate what varies.

### Benefits of using Simple Factory

Pulling the logic of creating the correct cheesecake based on a given type is a small move that gives us lots of benefits. The biggest benefit is that we can modify the cheesecake list without touching the `make_cheesecake` method and its test. All we need to do is update the `CheesecakeFactory` class and leave `make_cheesecake` and its test alone.

We want to separate the parts that vary often from the stable parts. Because each time we modify a part of our code, we might introduce bugs. The parts that vary are the fragile parts of our system. We want to keep the stable parts away from the fragile parts. So if we did introduce bugs when updating a part of the system, it would be easier for us to locate the bug.

### Takeaways:

1. **Factory Patterns are used for encapsulating object creation.**
2. **Design Principle: encapsulate what varies.**

I need to run to get a cheesecake now.

Don’t forget to subscribe so you won’t miss the next post!

Next time, we will take a look at some waaaaaaaaffles!

![Image](https://cdn-media-1.freecodecamp.org/images/1*LvuKW5NzZsznwP-Y3TfInA.png)

