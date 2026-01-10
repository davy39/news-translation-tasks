---
title: The Decorator Design Pattern is kind of like a waffle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-25T23:29:10.000Z'
originalURL: https://freecodecamp.org/news/the-decorator-design-pattern-is-kind-of-like-a-waffle-264e8c816715
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4FU5faISak9BmmtnI12bpQ.jpeg
tags:
- name: design patterns
  slug: design-patterns
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sihui Huang

  The decorator pattern is about adding extra features to an existing object.

  Does that sound like French?

  No worries.

  We will come back to this later.

  Let’s take a look at some waffles first!

  The genius part about waffles is that they s...'
---

By Sihui Huang

The decorator pattern is about adding extra features to an existing object.

Does that sound like French?

No worries.

We will come back to this later.

Let’s take a look at some waffles first!

The genius part about waffles is that they start plain and simple. Because they are plain, almost everything tastes good with them

Some common toppings for waffles are strawberries, blueberries, blackberries, bananas, almonds, and syrups.

![Image](https://cdn-media-1.freecodecamp.org/images/1*czVXA_H5JrZH1rsHkZTZxg.jpeg)

Let’s try to create a collection of different waffle objects.

There will be StrawberryWaffle, BlueberryWaffle, BlackberryWaffle, BananaWaffle, AlmondWaffle, and SyrupWaffle.

Wait, we can have strawberries and blueberries on the same waffle. This gives us a StrawberryBlueberryWaffle.

We can also have strawberries and blackberries on the same waffle. This gives us a StrawberryBlackberryWaffle.

No one is forbidding us from putting three toppings on the same waffle. This gives us a StrawberryBlueberryBlackberryWaffle.

To make things simple, let’s consider strawberries, blueberries, and blackberries as potential toppings. There are eight different combinations[1].

Does this mean we need to create eight different objects for our waffle collection?

If we add bananas into our potential toppings list, there are 16 different combinations[2].

It’s obvious that adding a single topping to our toppings list causes an explosion in our waffle collection.

**It’s not feasible to create a different waffle class for each possible combination of toppings.** There must be a better way to do this.

What if, when we want a StrawberryWaffle instead of creating a StrawberryWaffle, we create a Waffle and add strawberries to it?

What about StrawberryBlueberryWaffle then? ???

???We **can create a Waffle, add strawberries to it, and add blueberries to it!???**

### Creating Waffle Classes

Let’s take a look at the plain waffle class:

You can create a waffle, serve it, and eat it like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*weV8NQ2k6szFGp3W7UdUcw.png)

And here is the StrawberryWaffle class:

**Notice we pass a waffle object inside the StrawberryWaffle constructor to create a StrawberryWaffle.**

The StrawberryWaffle class has:

1. The passed-in waffle
2. Strawberries as a topping
3. A `serve` method that calls the passed-in waffle’s `serve` method. Then prints `topped with strawberries`
4. A `eat` method that calls the passed-in waffle’s `eat` method and then prints `and then eat some strawberries`

You can create a strawberry waffle, serve it, and eat it like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hT_swQasc2fUWEHllWt5qQ.png)

Here are the BlueberryWaffle and BlackberryWaffle classes:

And you can use them like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*M_3M_f0UkDH4UKQy772tTw.png)

### Pulling the Common Part Out

Noticing the StrawberryWaffle class, the BlueberryWaffle class, and the BlackberryWaffle class are almost identical except for their `topping`, we can pull the common parts out as a parent class.

In `WaffleDecorator`, `topping` is no longer an attribute of the object. Instead, it’s a method that can be overridden by a child class.

Now we can rewrite `StrawberryWaffle`, `BlueberryWaffle`, and `BlackberryWaffle` to inherit `WaffleDecorator` to gain these common functionalities:

And they should still work the same as before:

![Image](https://cdn-media-1.freecodecamp.org/images/1*F7esdyzUOeEKlE8gqgEQpw.png)

Here are the classes we create:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kmCmAVV-67wkMqDhR09dvg.png)

### Creating a BlueberryStrawberry Waffle

Now we have `Waffle`, `StrawberryWaffle`, `BlueberryWaffle`, and `BlackberryWaffle`.

It’s time to achieve the goal we originally set out:

**create a Waffle, add strawberries to it, and add blueberries to it**.

Just like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*QiuxdYN-dwhk0t1f47Hl_A.png)

And we can:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vegaZ1Te-NyaLWGzhWO_0A.png)

### What is happening?! ???

Let’s take a closer look at how we created the `blueberry_strawberry_waffle`:

First, we created a `plain_waffle` with `Waffle`: `plain_waffle = Waffle.new`

![Image](https://cdn-media-1.freecodecamp.org/images/1*jW3Ptmd4LenA8r0yhrsRvQ.png)

Then we created `strawberry_waffle` by passing the `plain_waffle` into the `StrawberryWaffle` constructor. `strawberry_waffle = StrawberryWaffle.new(plain_waffle)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*oTHZFfPxKqIt6_2fYg74Gg.png)

It’s worth noting that when we create the `strawberry_waffle`, we hold the passed-in `plain_waffle` as an instance variable of `strawberry_waffle`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OZ4w51QqltH6RjyNtAesMg.png)

As we can see, `strawberry_waffle.waffle` and `plain_waffle` are the same object:

![Image](https://cdn-media-1.freecodecamp.org/images/1*D1n_qoh30U6p3OMLoGDvKg.png)

At this point, when we call `strawberry_waffle.serve.` We first call `plain_waffle.serve` then print `topped with strawberries`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IWrELsik2PMCZS31d5yyIg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nounSGokjqaJo3AJJEbD-g.png)

For `strawberry_waffle.eat`, we first call `plain_waffle.eat` then print `and then eat some strawberries`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OyFpsHk0hp6m2m13NGxc1A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dj_EkO2PeewA0LWi2uqztA.png)

We create `blueberry_strawberry_waffle` by passing the `strawberry_waffle`into the `BlueberryWaffle` constructor. `blueberry_strawberry_waffle = BlueberryStrawberryWaffle.new(strawberry_waffle)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZWzIgZX5HyZ1HkedPRPvEw.png)

When we create the `blueberry_strawberry_waffle`, we hold the passed-in `strawberry_waffle` as an instance variable of `blueberry_strawberry_waffle`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*r9CRF5itgt635btmNldXgw.png)

When we call `blueberry_strawberry_waffle.serve` we first call `strawberry_waffle.serve`. Which calls `plain_waffle.serve` then prints `topped with strawberries.` Then print `topped with blueberries`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aEai4fnfaqbgbnwq6a4Y4A.png)

When we call `blueberry_strawberry_waffle.eat` we first call `strawberry_waffle.eat`. Which calls `plain_waffle.eat` then prints and then `eat some strawberries`. Then print `and then eat some blueberries`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TSLbCErIsP56O_HaOaDusw.png)

### The Key of the Magic:

`strawberry_waffle` is built on top of `plain_waffle`. And `blueberry_strawberry_waffle` is built on top of `strawberry_waffle`.

The key of being able to build waffles on top of each other is **all waffles have to obey the same interface**.

All waffles have a `serve` method and an `eat` method.

That’s why within the `StrawberryWaffle/BlueberryWaffle/BlackberryWaffle`classes, we are confident that the passed-in `waffle` has a `serve` method and an `eat` method.

And we can leverage the `serve` method and the `eat` method from the passed-in waffle when defining a new `serve` method and a new `eat` method.

A WaffleDecorator doesn’t care about the kind of waffle. It can be a plain_waffle, a strawberry_waffle, or an alien-waffle.

**All that matters is that a WaffleDecorator takes a waffle and returns a enhanced waffle. The waffle it takes and the waffle it returns obey the same interface.**

**Since all decorators taking and returning waffles obey the same interface, the result of a decorator can be passed into another decorator.**

Just like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cwj-Kt-pZ9EJYeuT3qs8MQ.png)

or this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*MbOB6SYS8sZl0vhjKxYu4w.png)

Now with `Waffle`, `StrawberryWaffle`, `BlueberryWaffle`, and `BlackberryWaffle`, we can create all eight different waffles.

Adding banana into our topping list is as easy as:

![Image](https://cdn-media-1.freecodecamp.org/images/1*MgXjPD6Y6lBS_gEAONX3-Q.png)

### You just Learned the Decorator Pattern! ???

Here’s its definition:

> Decorator attaches additional responsibilities to an object dynamically.

### Takeaways:

1. **The decorator pattern is about adding additional features to an existing object easily.**
2. **The object to be decorated (the one being passed into all decorators) and objects returned from decorators have to obey the same interface.**

Thanks for reading! I hope you enjoy the article. ?

I publish to [sihui.io](http://www.sihui.io/) weekly.

Subscribe so you won’t miss the next article from the series.

Next time we will take a look at …

![Image](https://cdn-media-1.freecodecamp.org/images/1*2oEt4tQRLIGwIFExDLUJNw.png)

[1] PlainWaffle, StrawberryWaffle, BlueberryWaffle, BlackberryWaffle, StrawberryBlueberryWaffle, StrawberryBlackberryWaffle, BlueberryBlackberryWaffle, and StrawberryBlueberryBlackberryWaffle.

[2] [C(4, 0) + C(4, 1) + C(4, 2) + C(4, 3) + C(4, 4) = 16](https://www.calculatorsoup.com/calculators/discretemathematics/combinations.php)

