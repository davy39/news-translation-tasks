---
title: A Short Overview of Object Oriented Software Design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T01:18:13.000Z'
originalURL: https://freecodecamp.org/news/a-short-overview-of-object-oriented-software-design-c7aa0a622c83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DuIQNSG6UjcEXpskd4_dEQ.jpeg
tags:
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Stanislav Kozlovski

  Demonstrated by implementing a Role-Playing Game’s classes


  _[Zeppelin by Richard Wright](https://www.artstation.com/artwork/rO8e6" rel="noopener"
  target="blank" title=")

  Introduction

  Most modern programming languages support a...'
---

By Stanislav Kozlovski

#### Demonstrated by implementing a Role-Playing Game’s classes

![Image](https://cdn-media-1.freecodecamp.org/images/1*DuIQNSG6UjcEXpskd4_dEQ.jpeg)
_[Zeppelin by Richard Wright](https://www.artstation.com/artwork/rO8e6" rel="noopener" target="_blank" title=")_

### Introduction

Most modern programming languages support and encourage object-oriented programming (OOP). Even though lately we seem to be seeing a slight shift away from this, as people start using languages which are not **heavily** influenced by OOP (such as Go, Rust, Elixir, Elm, Scala), most still have objects. The design principles we are going to outline here apply to non-OOP languages as well.

To succeed in writing clear, high-quality, maintainable and extendable code you will need to know about design principles that have proven themselves effective over decades of experience.

**Disclosure:** The example we are going to be going through will be in **Python.** Examples are there to prove a point and may be sloppy in other, obvious ways.

### Object Types

Since we are going to be modelling our code around objects, it would be useful to differentiate between their different responsibilities and variations.

There are three type of objects:

#### 1. Entity Object

This object generally corresponds to some real-world entity in the problem space. Say we’re building a role-playing game (RPG), an entity object would be our simple `Hero` class:

These objects generally contain properties about themselves (such as `health` or `mana`) and are modifiable through certain rules.

#### 2. Control Object

Control objects (sometimes also called **Manager objects**) are responsible for the coordination of other objects. These are objects that **control** and make use of other objects. A great example in our RPG analogy would be the `Fight` class, which controls two heroes and makes them fight.

Encapsulating the logic for a fight in such a class provides you with multiple benefits: one of which is the easy extensibility of the action. You can very easily pass in a non-player character (NPC) type for the hero to fight, provided it exposes the same API. You can also very easily inherit the class and override some of the functionality to meet your needs.

#### 3. Boundary Object

These are objects which sit at the boundary of your system. Any object which takes input from or produces output to another system — regardless if that system is a User, the internet or a database — can be classified as a boundary object.

These boundary objects are responsible for translating information into and out of our system. In an example where we take User commands, we would need the boundary object to translate a keyboard input (like a spacebar) into a recognizable domain event (such as a character jump).

#### Bonus: Value Object

[Value objects](https://en.wikipedia.org/wiki/Value_object) represent a simple value in your domain. They are immutable and have no identity.

If we were to incorporate them into our game, a `Money` or `Damage` class would be a great fit. Said objects let us easily distinguish, find and debug related functionality, while the naive approach of using a primitive type — an array of integers or one integer — does not.

They can be classified as a subcategory of `**Entity**` objects.

### Key Design Principles

Design principles are rules in software design that have proven themselves valuable over the years. Following them strictly will help you ensure your software is of top-notch quality.

#### Abstraction

Abstraction is the idea of simplifying a concept to its bare essentials in some context. It allows you to better understand the concept by stripping it down to a simplified version.

The examples above illustrate abstraction — look at how the `Fight` class is structured. The way you use it is as simple as possible — you give it two heroes as arguments in instantiation and call the `fight()` method. Nothing more, nothing less.

Abstraction in your code should follow the [rule of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). Your abstraction should not surprise anybody with needless and unrelated behavior/properties. In other words — it should be intuitive.

Note that our `Hero#take_damage()` function does not do something unexpected, like delete our character upon death. But we can expect it to kill our character if his health goes below zero.

#### Encapsulation

Encapsulation can be thought of as putting something inside a capsule — you limit its exposure to the outside world. In software, restricting access to inner objects and properties helps with data integrity.

Encapsulation black-boxes inner logic and makes your classes easier to manage, because you know what part is used by other systems and what isn’t. This means that you can easily rework the inner logic while retaining the public parts and be sure that you have not broken anything. As a side-effect, working with the encapsulated functionality from the outside becomes simpler as you have less things to think about.

In most languages, this is done through the so-called [access modifiers](https://en.wikipedia.org/wiki/Access_modifiers) (private, protected, and so on). Python is not the best example of this, as it lacks such explicit modifiers built into the runtime, but we use conventions to work around this. The `_` prefix to the variables/methods denote them as being private.

For example, imagine we change our `Fight#_run_attack` method to return a boolean variable that indicates if the fight is over rather than raise an exception. We will know that the only code we might have broken is inside the `Fight` class, because we made the method private.

Remember, code is more frequently changed than written anew. Being able to change your code with as clear and little repercussions as possible is flexibility you want as a developer.

#### Decomposition

Decomposition is the action of splitting an object into multiple separate smaller parts. Said parts are easier to understand, maintain and program.

Imagine we wanted to incorporate more RPG features like buffs, inventory, equipment and character attributes on top of our `Hero`:

I assume you can tell this code is becoming pretty messy. Our `Hero` object is doing too much stuff at once and this code is becoming pretty brittle as a result of that.

For example, one stamina point is worth 5 health. If we ever want to change this in the future to make it worth 6 health, we’d need to change the implementation in multiple places.

The answer is to decompose the `Hero` object into multiple smaller objects which each encompass some of the functionality.

![Image](https://cdn-media-1.freecodecamp.org/images/1*etyn_SN7_v4zqGDbeazJVA.png)
_A cleaner architecture_

Now, after decomposing our Hero object’s functionality into `HeroAttributes`, `HeroInventory`, `HeroEquipment`and `HeroBuff` objects, adding future functionality will be easier, more encapsulated and better abstracted. You can tell our code is way cleaner and clearer on what it does.

There are three types of decomposition relationships:

* **association** — Defines a loose relationship between two components. Both components do not depend on one another but may work together.

**Example:** `Hero` and a `Zone` object.

* **aggregation** — Defines a weak “has-a” relationship between a whole and its parts. Considered weak, because the parts can exist without the whole.

**Example:** `HeroInventory` and `Item`.   
A `HeroInventory` can have many `Items` and an `Item` can belong to any `HeroInventory`(such as trading items).

* **composition** — A strong “has-a” relationship where the whole and the part cannot exist without each other. The parts cannot be shared, as the whole depends on those exact parts.

**Example:** `Hero` and `HeroAttributes`.   
These are the Hero’s attributes — you cannot change their owner.

#### Generalization

Generalization might be the most important design principle — it is the process of extracting shared characteristics and combining them in one place. All of us know about the concept of functions and class inheritance —both are a kind of generalization.

A comparison might clear things up: while **abstraction** reduces complexity by hiding unnecessary detail, **generalization** reduces complexity by replacing multiple entities which perform similar functions with a single construct.

In the given example, we have generalized our common `Hero` and `NPC` classes’ functionality into a common ancestor called `Entity`. This is always achieved through inheritance.

Here, instead of having our `NPC` and `Hero` classes implement all the methods twice and violate the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), we reduced the complexity by moving their common functionality into a base class.

As a forewarning — do not overdo [inheritance](https://softwareengineering.stackexchange.com/questions/260343/why-is-inheritance-generally-viewed-as-a-bad-thing-by-oop-proponents). [Many experienced people](https://en.wikipedia.org/wiki/Design_Patterns#Introduction,_Chapter_1) recommend you favor [composition over inheritance](https://stackoverflow.com/a/53354).

Inheritance is often abused by amateur programmers, probably because it is one of the first OOP techniques they grasp due to its simplicity.

#### Composition

Composition is the principle of combining multiple objects into a more complex one. Practically said — it is creating instances of objects and using their functionality instead of directly inheriting it.

An object that uses composition can be called a **composite object**. It is important that this composite is simpler than the sum of its peers. When combining multiple classes into one we want to raise the level of abstraction higher and make the object simpler.

The composite object’s [API](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82) must hide its inner components and the interactions between them. Think of a mechanical clock, it has three hands for showing the time and one knob for setting — but internally contains dozens of moving and inter-dependent parts.

As I said, composition is preferred over inheritance, which means you should strive to move common functionality into a separate object which classes then use — rather than stash it in a base class you’ve inherited.

Let’s illustrate a possible problem with over-inheriting functionality:

We just added movement to our game.

As we learned, instead of duplicating the code we used generalization to put the `move_right` and `move_left` functions into the `Entity` class.

Okay, now what if we wanted to introduce mounts into the game?

![Image](https://cdn-media-1.freecodecamp.org/images/1*dK8x5H7sJF-3px7cbJ46Jw.jpeg)
_a good mount :)_

Mounts would also need to move left and right but do not have the ability to attack. Come to think of it — they might not even have health!

I know what your solution is:

Simply move the `move` logic into a separate `MoveableEntity` or `MoveableObject` class which only has that functionality. The `Mount` class can then inherit that.

Then, what do we do if we want mounts that have health but cannot attack? More splitting up into subclasses? I hope you can see how our class hierarchy would begin to become complex even though our business logic is still pretty simple.

A somewhat better approach would be to abstract the movement logic into a `Movement` class (or some better name) and instantiate it in the classes which might need it. This will nicely package up the functionality and make it reusable across all sorts of objects not limited to `Entity`.

Hooray, composition!

#### Critical Thinking Disclaimer

Even though these design principles have been formed through decades of experience, it is still extremely important that you are able to think critically before blindly applying a principle to your code.

Like all things, too much can be a bad thing. Sometimes principles can be taken too far, you can get too clever with them and end up with something that is actually harder to work with.

As an engineer, your main trait is to critically evaluate the best approach for your unique situation, not blindly follow and apply arbitrary rules.

### Cohesion, Coupling & Separation of Concerns

#### Cohesion

Cohesion represents the clarity of responsibilities within a module or in other words — its complexity.

If your class performs one task and nothing else, or has a clear purpose — that class has **high cohesion**. On the other hand, if it is somewhat unclear in what it’s doing or has more than one purpose — it has **low cohesion**.

You want your classes to have high cohesion. They should have only one responsibility and if you catch them having more — it might be time to split it.

#### Coupling

Coupling captures the complexity between connecting different classes. You want your classes to have as little and as simple connections to other classes as possible, so that you can swap them out in future events (like changing web frameworks). The goal is to have **loose coupling**.

In many languages this is achieved by heavy use of interfaces —they abstract away the specific class handling the logic and represent a sort of adapter layer in which any class can plug itself in.

#### Separation of Concerns

Separation of Concerns (SoC) is the idea that a software system must be split into parts that do not overlap in functionality. Or as the name says — concern — A general term about anything that provides a solution to a problem _—_ must be separated into different places.

A web page is a good example of this — it has its three layers (Information, Presentation and Behavior) separated into three places (HTML, CSS and [JavaScript respectively](https://shinesolutions.com/2013/10/29/respect-the-javascript/)).

If you look again at the RPG `Hero` example, you will see that it had many concerns at the very beginning (apply buffs, calculate attack damage, handle inventory, equip items, manage attributes). We separated those concerns through **decomposition** into more **cohesive** classes which **abstract** and **encapsulate** their details. Our `Hero` class now acts as a [composite](https://en.wikipedia.org/wiki/Composite_pattern) object and is much simpler than before.

### Payoff

Applying such principles might look overly complicated for such a small piece of code. The truth is it a **must** for any software project that you plan to develop and maintain in the future. Writing such code has a bit of overhead at the very start but pays off multiple times in the long run.

These principles ensure our system is more:

* **Extendable**: **High cohesion** makes it easier to implement new modules without concern of unrelated functionality. **Low coupling** means that a new module has less stuff to connect to therefore it is easier to implement.
* **Maintainable**: **Low coupling** ensures a change in one module will generally not affect others. **High cohesion** ensures a change in system requirements will require modifying as little number of classes as possible.
* **Reusable**: **High cohesion** ensures a module’s functionality is complete and well-defined. **Low coupling** makes the module less dependent on the rest of the system, making it easier to reuse in other software.

### Summary

We started off by introducing some basic high-level object types (Entity, Boundary and Control).

We then learned key principles in structuring said objects (Abstraction, Generalization, Composition, Decomposition and Encapsulation).

To follow up we introduced two software quality metrics (Coupling and Cohesion) and learned about the benefits of applying said principles.

I hope this article provided a helpful overview of some design principles. If you wish to further educate yourself in this area, here are some resources I would recommend.

#### Further Readings

[Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8) —Arguably the most influential book in the field. A bit dated in its examples _(C++ 98)_ but the patterns and ideas remain very relevant.

[Growing Object-Oriented Software Guided by Tests](http://www.growing-object-oriented-software.com/) — A great book which shows how to practically apply principles outlined in this article (and more) by working through a project.

[Effective Software Design](https://effectivesoftwaredesign.com/category/oop/) — A top notch blog containing much more than design insights.

[Software Design and Architecture Specialization](https://www.coursera.org/specializations/software-design-architecture) — A great series of 4 video courses which teach you effective design throughout its application on a project that spans all four courses.

If this overview has been informative to you, please consider giving it the amount of claps you think it deserves so that more people can stumble upon it and gain value from it.

