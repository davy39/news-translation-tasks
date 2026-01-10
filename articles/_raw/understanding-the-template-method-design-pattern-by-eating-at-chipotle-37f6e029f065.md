---
title: Understanding the Template Method design pattern by eating at Chipotle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T15:26:43.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-template-method-design-pattern-by-eating-at-chipotle-37f6e029f065
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rQ4O--pESIxq1jr_JcBPqA.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sihui Huang

  Object-Oriented Design Patterns in Life— gain an intuitive understanding of OO design
  patterns by linking them with real-life examples.


  Template Method is a commonly used design pattern in programming and real life.

  Before we dive int...'
---

By Sihui Huang

[Object-Oriented Design Patterns in Life— gain an intuitive understanding of OO design patterns by linking them with real-life examples.](http://www.sihui.io/design-patterns/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*rQ4O--pESIxq1jr_JcBPqA.png)

Template Method is a commonly used design pattern in programming and real life.

Before we dive into details of the pattern, let’s learn an important life lesson:

### Chipotle 101: How to Order at Chipotle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HgB3orsQPykXtWf7cmI1Xg.png)

There are four steps involved:

1. Choose a “vessel”: Burrito vs. Bowl vs. Tacos vs. Salad
2. Add meat: Chicken vs Steak vs. Barbacoa vs. Carnitas vs. Vegetarian
3. Add toppings: Tomato vs. Corn vs. Green Chili vs. Red Chili
4. Add extras & drinks: Chips vs. Guacamole vs. Salsa vs. Beer vs. Soda

For example, my go-to order is Bowl + Steak + (Tomato + Corn) + Guacamole and my friend Amber’s go-to order is Burrito + Chicken + (Green Chili + Red Chili) + (Chips + Soda).

If we code our go-to orders in Ruby, they will look like:

When we order, we put everything we want into the vessel and return the stuffed vessel.

Unfortunately, Amber and I decided to go on a diet for a while. And we decided that when we ordered from Chipotle, we could only get tomato as a topping and no extras. So our choices are limited to:

1. Vessel: Burrito vs. Bowl vs. Tacos vs. Salad
2. Meat: Chicken vs. Steak vs. Barbacoa vs. Carnitas vs. Vegetarian
3. Toppings: Tomato
4. No extras & drinks

During the diet, our go-to orders have to be modified to:

* Sihui: Bowl + Steak + Tomato + No extras & drinks
* Amber: Burrito + Chicken + Tomato + No extras & drinks

Putting our orders down in Ruby, we have the following:

Since both our orders have the exact same _toppings_, _extras_, and _order_ methods, it makes sense to pull them out as a parent class, _DietOrder_, and have _DietOrderSihui_ and _DietOrderAmber_ inherit from it.

Now our friend Ben wants to join our Chipotle Diet Club, and he likes Tacos with Carnitas. Then his order will be:

Ta-da, you just learned the Template Method design pattern! ? ? ?

Don’t believe me?

Take a look at the definition of the Template Method:

> The Template Method pattern is a behavioral design pattern that

> - defines the program skeleton of an algorithm in an operation,

> - deferrs some steps to subclasses.

> It lets one redefine certain steps of an algorithm without changing the algorithm’s structure.

Doesn’t this sound exactly like what we just did with our _DietOrder_ and _SihuiDietOrder/AmberDietOrder/BenDietOrder_?

_DietOrder_ defines the order skeleton: one can only get tomato as a topping and no extras & drinks, and one orders by picking a vessel and putting everything inside the chosen vessel.

_SihuiDietOrder/AmberDietOrder/BenDietOrder_ redefine the vessel and meat depending on our personal preferences.

Let’s say a month passed by, and Amber and I followed our diet strictly. We decided to reward ourselves with cheat days!

On a cheat day, we have soda as our drinks. ??? And each of us can decide which day of the month will be our cheat day.

Since Ben is new to the club, he decides to stick to the diet strictly for a bit longer.

Let’s see how it looks in Ruby:

In _DietOrder_, we ask if today is a cheat day. If so, we can have Soda as an extra. Otherwise, there are no extras. And by default, today is not a cheat day.

Amber and I get to define our own cheat days:

Since Ben is sticking with the diet strictly, he doesn’t get a cheat day.

His class doesn’t need to change.

The _is_cheat_day?_ method is a hook.

A hook provides a way for a subclass to implement an optional part of an algorithm.

If the subclass doesn’t care about the part, it can skip it and use the default implementation in the parent class.

In our case, _is_cheat_day?_ is optional. SihuiDietOrder and AmberDietOrder implement it because we want to have a cheat day each month. But Ben does not want to have a cheat day. So BenDietOrder skips implementing _is_cheat_day?_ and uses the default one from DietOrder, which always returns false.

There are two important object-oriented design principles used in the Template Method:

1. Encapsulate what varies.

In our case, the varying parts are _vessel_, _meat_, and _is_cheat_day_?. We encapsulate them in subclasses. For the parts that don’t vary, _toppings_ and _extras_, we leave them in the parent class.

2. The Hollywood Principle: Don’t call us, we’ll call you.

Yes, The Hollywood Principle is [a real thing](http://wiki.c2.com/?HollywoodPrinciple).

In Hollywood, movie producers will tell actors: “Don’t call us, we’ll call you if we find a role that fits you.”

In programming, low-level components can participate in the computation, like _AmberDietOrder_ defining its own _is_cheat_day?_, but the high-level components control when and how, like _DietOrder_ calls _is_cheat_day?_ within _extras_.

### Takeaways:

**One definition =&**gt;

> The Template Method pattern is a behavioral design pattern that

> - defines the program skeleton of an algorithm in an operation,

> - deferrs some steps to subclasses.

> It lets one redefine certain steps of an algorithm without changing the algorithm’s structure.

**Two Design Principles =&**gt;

> 1. Encapsulate what varies.

> 2. The Hollywood Principle: Don’t call us, we’ll call you.

Or…

you can just take away a Chipotle order ? ? ?

Next time, we take our design & food adventure to ???

![Image](https://cdn-media-1.freecodecamp.org/images/1*WpzelusOe2vXZa9tXugL9Q.png)

