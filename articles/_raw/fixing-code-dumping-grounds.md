---
title: How Code Becomes A Dumping Ground (And How To Fix It!)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-18T20:36:52.000Z'
originalURL: https://freecodecamp.org/news/fixing-code-dumping-grounds
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/ashim-d-silva-Kw_zQBAChws-unsplash.jpg
tags:
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
- name: refactoring
  slug: refactoring
seo_title: null
seo_desc: 'By James Hickey

  Earlier in my career, I faced a sort of career crisis.

  I was part of a team creating a large analytics platform in the automotive industry.
  This application had the typical "enterprise-y" layered architecture you would expect
  ("Busine...'
---

By James Hickey

Earlier in my career, I faced a sort of career crisis.

I was part of a team creating a large analytics platform in the automotive industry. This application had the typical "enterprise-y" layered architecture you would expect ("Business Layer", "Data Access Layer", "Core", etc.).

You would expect to find business logic - the really important business logic - embedded somewhere inside of the code from these layers. But, usually, the really important business rules were coded into stored procedures.

**Stored procedures**, if you don't know, is like a function you create inside of a database that uses an SQL-like syntax to process data, store it, etc.

I wondered what the purpose of the layers was. They didn't have any code except for passing data to stored procedures or showing data returned by one.

I started to learn more about object-oriented programming, industry best-practices, SOLID, other programming paradigms, application architecture, etc.

From this career crisis, I discovered that these problems have already been solved! It just takes research, time and practice to learn and grow skilled in them.

## Object-Oriented?

One thing I discovered is that all the projects I've been on that were doing "Object-Oriented" programming were _not_ doing true OOP. Just because you use classes doesn't mean you are doing OOP. Especially if you are using stored procedures to encode all your business rules.

### A Short Aside: The Great Debate

It needs to be brought up: is object-oriented programming or functional programming better?

For starters, most people don't understand what OOP was intended to be in the first place. Similar to how Agile today is usually misunderstood (e.g. just because you are having daily stand-ups, using story points, kanban, etc. it doesn't mean you are doing Agile).

Alan Kay is considered one of the fathers of OOP. [In a certain email](http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en), he gave some frank explanations about what OOP was supposed to be.

> "I thought of objects being like biological cells and/or individual computers on a network, only able to communicate with messages (so messaging came at the very beginning -- it took a while to see how to do messaging in a programming language efficiently enough to be useful)...

> OOP to me means only messaging, local retention and protection and hiding of state-process, and extreme late-binding of all things...

> But just to show how stubbornly an idea can hang on, all through the seventies and eighties, there were many people who tried to get by with 'Remote Procedure Call' instead of thinking about objects and messages."

For those familiar with microservices, the actor model, and other advanced programming paradigms, your Spidey sense is tingling. These are actually more closely related to true OOP.

So, is FP better than true OOP?

I don't think so. I think they both have their merits. Many languages today are embracing both paradigms and allowing developers to use the tools and methods that work best for the given problem!

What you'll usually find are classes that expose all their properties or internal data members. An HTTP request or database query will fill-up all the properties, and then, perhaps, something else will work on that object's data.

Instead of what Alan Kay intended to be as little "bundles" that pass messages to each other (see aside above), most developers are using objects as mere "data holders". Glorified variables, as it were.

What you'll also find in many codebases are very generic classes like `User`, `Customer` or `Order`.

Is that bad? Well, **yes**.

Let me ask you a question:

Is `User` used in many different unrelated places in your application?

For example, is your `User` class used in the billing part of your code, the user profile parts, the shipping parts, etc.?

Most systems are doing something like that.

What will end up happening is that, because these classes are so generic, **they become dumping grounds for code which we don't know where it belongs.**

Instead of taking the time to think about the business need for this new code we've written, often we feel that it's easier to put into our generic classes. It's all shareable, right? And we're all about code-reuse, right?

## Coupling

So... what if I changed the `User` class to conform to some billing logic? What are the chances that I've also broken the shipping feature by changing this class? I don't know, but it's **higher than 0%.**

This `User` class has coupled all your features together. This causes lots of problems.

Ideally, we want our code to be orthogonal (that's just a fancy word that means changing code in one place won't affect other unrelated places).

We want to be able to change the shipping feature, for example, and **not have to test our entire application again.** But, if we're sharing our `User` class everywhere then, to have confidence that we didn't break stuff, we need to re-test **everything.**

This leads to a fear of changing code. The fear of making our code better. It also leads to a lot of bugs.

If you are building out the payment feature for your application - you shouldn't have to think about whether you are breaking the shipping feature at the same time! This causes a huge cognitive load that doesn't need to be there.

### Another Aside: Warning Sign

Overall, I find that the idea of segmenting your business features/functions via different physical folders or even entirely different projects altogether is best. [I've written about this before](https://dev.to/jamesmh/the-life-changing-and-time-saving-magic-of-feature-focused-code-organization-1708).

But, when it comes to our code at a deeper level, we can still tend to design our classes and objects in a way that's still too generic and leads to much coupling.

Anytime I find classes that have simple names like `User` or `Customer`, a warning signal goes off. I'd much rather see classes that are created for a specific context.

For example, if I saw a class named `UserForAuthentication` or `PaymentsCustomer` then I would be more confident that these classes aren't being thrown around and reused in too many contexts.

Here's a basic way that might help get started on analyzing your classes. Take your class name and answer these questions:

Is there a subject? (user, client, order, etc.)

Is there a context for that subject? (shipping, orders, dashboard, etc.)

Is there even perhaps an action being performed on the subject? (as we'll see in more details soon)

If you cannot answer 2 of those questions then I'd say there's a good chance that your class might be doing too much by being too generic.

## One Of These Things Is Not Like The Others

There's a programming principle called the Single Responsibility Principle.

When looking at classes or methods that are doing too much, using the SRP as a guiding light can help us to make code that is easier to maintain, less coupled and therefore leads to fewer bugs.

Let's look at a generic `User` class that might be similar to code you've seen before:

```typescript
class User {
    public firstName: string;
    public lastName: string;
    public id: number;
    public jwtToken: string;
    public homeAddress: string;
    public creditCardNo: string;

    public getFullName(): string {
        return this.firstName + " " + this.lastName;
    }

    public decodeJwtToken(): string {
        return decode(this.jwtToken);
    }
}

```

Look familiar?

Given the name of the class, we should start to be suspicious that it's too generic of a class.

## You Have Mail

You've been tasked with adding a new business requirement. We need users to be able to pay for their products using PayPal.

This `User` class is already used in multiple places like the user profile, shipping and payment features.

All we need to do is add the user's PayPal email address to the user. Right?

## Breaking It Up

Usually, you will get new business requirements that require _more_ changes to your code than this. But this is a simple example.

If we start changing this `User` class so that it works with the payment feature then we risk affecting the user profile or the shipping feature (since they use this class too).

What should we do?

The best thing to do here is _create a different user class that's used within each specific context._

Out of this should come classes like `UserForAuthentication`, `UserProfileUser`, `ShippingUser` and `PaymentUser`.

Are those models/classes going to contain similar pieces of data that all of them will need? Sure.

Will they also have pieces of data that are only used in one context? Sure.

For example, the user's `id` is needed everywhere.

But, the user's home address is only ever needed by shipping. Why then, does the payment feature need access to that data? It doesn't.

Here's what these classes might look like:

```typescript
class UserProfileUser {
    public firstName: string;
    public lastName: string;
    public id: number;
    public homeAddress: string;
    
    public getFullName(): string {
        return this.firstName + " " + this.lastName;
    }
}

class ShippingUser {
    public id: number;
    public homeAddress: string;
}

class UserForAuthentication {
    public id: number;
    public jwtToken: string;

    public decodeJwtToken(): string {
        return decode(this.jwtToken);
    }
}

class PaymentUser {
    public id: number;
    public creditCardNo: string;
}

```

## Keep Separate Things Separate

Notice that the home address is needed by `UserProfileUser` and `ShippingUser`. Is that bad?

We've had it drilled into us so much that duplicating code is a bad thing. So much so, that it's this idea that's caused the problems we're talking about right now!

Sometimes, it's better to "duplicate" code and/or data - if they are within different contexts. Again, we want to avoid coupling our features and classes together.

Let me ask you a question:

_Is it probable that the behavior for the home address within the user profile will be different than the behavior for it in the shipping feature?_

The answer: **yes.**

So then, we are talking about two different things. It's the same raw data but **not the same business function or concept**_._

Shipping needs the home address so that it knows **where to send products.**

The user profile needs the home address **so the user can update its values from a UI.**

_Not the same things._

Also, consider that it might also make sense to add an address to the `PaymentUser` class too. But, should this context share the same address as shipping?

Well, is it possible that your shipping address wouldn't be the same address you want to bill to? Sure! This happens all the time!

Using the Single Responsibility Principle, we see that these two concepts/responsibilities should be kept separate.

Also, notice that _most_ of our pieces of data are **not** being shared. The JWT token, for example, is only needed for authenticating a user. Why would we ever need that piece of data inside our Shipping feature's code?

Now, that information is isolated.

**Also, any methods that act on that data will also be moved and not inappropriately called by another feature's code.**

This was a simple example, and in most cases, this can get a little trickier than we might want. In the end, though, keeping different business concepts separate from each other will make your code easier to understand within a specific context, easier to maintain and will become less error-prone!

This is an excerpt from my book  ["Refactoring TypeScript: Keeping Your Code Healthy"](https://leanpub.com/refactoringtypescript). This section of the book has **more** techniques for you to help deal with these kinds of dumping grounds. If you enjoyed this article then [check out the book for more content like this!](https://leanpub.com/refactoringtypescript)

You can [connect with me](https://twitter.com/jamesmh_dev) on Twitter too.

