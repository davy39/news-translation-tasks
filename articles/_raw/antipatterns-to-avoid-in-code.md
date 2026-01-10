---
title: Anti-patterns You Should Avoid in Your Code
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-11-23T21:23:30.000Z'
originalURL: https://freecodecamp.org/news/antipatterns-to-avoid-in-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/6-anti-patterns--2-.png
tags:
- name: spaghetti code
  slug: spaghetti-code
- name: anti pattern
  slug: anti-pattern
- name: clean code
  slug: clean-code
seo_title: null
seo_desc: 'Every developer wants to write structured, simply planned, and nicely commented
  code. There are even a myriad of design patterns that give us clear rules to follow,
  and a framework to keep in mind.

  But we can still find anti-patterns in software that...'
---

Every developer wants to write structured, simply planned, and nicely commented code. There are even a myriad of design patterns that give us clear rules to follow, and a framework to keep in mind.

But we can still find anti-patterns in software that was written some time go, or was written too quickly.

A harmless basic hack to resolve an issue quickly can set a precedent in your codebase. It can be copied across multiple places and turn into an anti-pattern you need to address.

## So What's an Anti-pattern?

In software, anti-pattern is a term that describes how NOT to solve recurring problems in your code. Anti-patterns are considered bad software design, and are usually ineffective or obscure fixes.

They generally also add "technical debt" - which is code you have to come back and fix *properly* later.

The six anti-patterns I will discuss in this article are **Spaghetti Code**, **Golden Hammer**, **Boat Anchor**, **Dead Code**, **Proliferation of Code** and the **God Object**.

## Spaghetti Code

**Spaghetti Code** is the most well known anti-pattern. It is code with little to zero structure.

Nothing is modularised. There are random files strewn in random directories. The whole flow is difficult to follow, and is utterly tangled together (like spaghetti).

Normally, this is an issue where someone hasn't carefully thought out the flow of their program beforehand and just started coding.

### What does it do?! I can't follow this

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1601054755926/AQtiQmp0X.png align="left")

This is not only a maintenance nightmare, but it makes it nigh on impossible to add new functionality.

You will constantly break things, not understand the scope of your changes, or give any accurate estimates for your work as it's impossible to foresee the countless issues that crop up when doing such archaeology/guesswork.

You can [read more here](https://en.wikipedia.org/wiki/Spaghetti_code) about the **Spaghetti Code** anti-pattern.

## Golden Hammer

> "I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail." Abraham Maslow

Imagine a scenario with me: your dev team is very, very competent at the brand new Hammer architecture. It has worked fantastically for all your past set of issues. You are the world's leading Hammer architecture team.

But now, somehow, everything always ends up using this architecture. A flat head screw? Hammer. Phillips head screw? Hammer. You need an Allen wrench? No you don't, hammer it.

You start to apply an architectural approach that doesn't *quite* fit what you need but gets the job done. You are over reliant on one pattern and need to learn the best tool for the best job.

Your whole program could end up taking a serious performance hit because you are trying to ram a square into a circle shape. You know it takes twice as long to code up, and to execute a program using the hammer architecture for this problem, but it's *easier* and it's what you're comfortable with.

It also isn't very predictable. Different languages have common fixes to the problems they face, and their own standards. You can't apply every single rule that worked well for you in one language to the next, with no issues.

Don't neglect consistently learning in your career. Pick the right language for your problem. Think about the architecture, and push out your comfort zone. Research and investigate new tools and new ways of approaching the problems you face.

You can [read more here](https://sourcemaking.com/antipatterns/golden-hammer) about the **Golden Hammer** anti-pattern.

## Boat Anchor

The **Boat Anchor** anti-pattern is where programmers leave code in the codebase because *they might need it later.*

They coded something slightly out of specification and it isn't needed yet, but they're sure they will next month. So they don't want to delete it. Send it to production and later when they need it, they can quickly get it working.

But this causes maintenance nightmares in the codebase that contains all that obsolete code. The huge issue is that their colleagues will have a hard time working out what code is obsolete and doesn't change the flow, versus the code that does.

Imagine you are on a hot fix, and are desperately trying to work out what is responsible for sending customers' card details to the API to withdraw funds from their bank. You could waste time reading and debugging obsolete code, without realising you aren't even in the right place in the codebase.

The final issue is, obsolete code makes your build time longer and you may mix-up working and obsolete code. You could even start to inadvertently "turn it on" in production.

Now you can probably see why it's called the boat anchor anti-pattern – it is heavy to carry (adds technical debt) but doesn't do anything (quite literally, the code serves no purpose, it doesn't work).

You can [read more here](https://sourcemaking.com/antipatterns/boat-anchor) about the **Boat anchor** anti-pattern.

## **Dead Code**

Have you ever had to look at code written by someone who doesn't work at your company any longer? There's a function that doesn't look like it is doing anything. But it is called from everywhere! You ask around and no-one else is quite sure what it's doing, but everyone's too worried to delete it.

Sometimes you can see what it's doing, but the context is missing. You are able to read and understand the flow, but *why?* It doesn't look like we need to hit that endpoint anymore. The response is always the same response for every different user.

This is commonly described as the **Dead code** anti-pattern. When you can't see what is "actual" code necessary to the flow and successful execution of your program, versus what was only needed 3 years ago, and not now.

This particular anti-pattern is more common in proof on concept or research code that ended up in production.

One time at a tech meet up I met a guy who had this exact problem. He had tons of dead code, which he knew was dead, and lots he suspected was dead. But he could not get permission from management to ever remove all the dead code.

He referred to his approach as **Monkey testing,** where he started to comment out and turn off things to see what blew up in production. Maybe a little too risky!

If you don't fancy **Monkey testing** your production app, try to frame technical debt to management as ["technical risk"](https://killalldefects.com/2019/12/24/technical-debt-as-risks/) to better explain why you think it's so important to tidy up.

Or even write down everything your particular module/section does you want to re-write, and take an iterative approach to remove piece by piece the dead code. Checking every time you haven't broken anything.

You don't have to drop a huge rewrite with thousands of changes. But you will either understand why it's so crucial and document why it's needed, or delete the dead code as you desired.

You can [read more here](https://sourcemaking.com/antipatterns/lava-flow) about the **Dead code** anti-pattern.

## **Proliferation of Code**

Objects or modules regularly communicate with others. If you have a clean, modularised codebase you often will need to call into other separate modules and call new functions.

The **Proliferation of Code** anti-pattern is when you have objects in your codebase that only exist to invoke another more important object. Its purpose is only as a middleman.

This adds an unnecessary level of abstraction (adds something that you have to remember) and serves no purpose, other than to confuse people who need to understand the flow and execution of your codebase.

A simple fix here is to just remove it. Move the responsibility of invoking the object you *really* want to the calling object.

You can [read more here](https://flylib.com/books/en/4.425.1.31/1/) about the **Proliferation of Code** anti-pattern.

## God Object

If everywhere in your codebase needs access to one object, it might be a God object.

God objects do *too* much. They are responsible for the user id, the transaction id, the customer's first and last name, the total sum of the transaction, the item/s the user is purchasing...you get the picture.

It is sometimes called the **Swiss Army Knife** anti-pattern because you only really need it to cut some twine, but it also can be a nail file, saw, pair of tweezers, scissors, bottle opener and a cork screw too.

In this instance you need to separate out and modularise your code better.

Programmers often compare this problem to asking for a banana, but receiving a gorilla holding a banana. You got what you asked for, but more than what you need.

The SOLID principles explicitly discuss this in object orientated languages, to help us model our software better ([if you don't know what the SOLID principles are, you can read this article](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/)).

The S in the acronym stands for Single Responsibility - every class/module/function should have responsibility over one part of the system, not multiple.

You can see this problem over and over again, how about the below interface?

```typescript
interface Animal {
        numOfLegs: string;
        weight: number;
        engine: string;
        model: string;
        sound: string;
        claws: boolean;
        wingspan: string;
        customerId: string;
}
```

Can you see by even just briefly scanning this interface that the responsibility of this is far too broad, and needs refactoring? Whatever implements this has the potential to be a God object.

How about this?

```typescript

interface Animal {
        numOfLegs: string;
        weight: number;
        sound: string;
        claws: boolean;
}

interface Car {
        engine: string;
        model: string;
}

interface Bird {
        wingspan: string;
}

interface Transaction {
        customerId: string;
}
```

Interface segregation will keep your code clear about where the responsibilities lie, and stop forcing classes that only need `wingspan` to also implement the `engine`, `customerId` and `model` and so on.

You can [read more here](https://en.wikipedia.org/wiki/God_object) about the **God object** anti-pattern.

## Conclusion

In any large codebase there is a constant balance between managing technical debt, starting new development, and managing a queue of bugs for your product.

I hope this article has given you an eye for spotting when you might be going down the rabbit hole of an anti-pattern, and some tools to resolve it cleanly.

I share my writing on [Twitter](https://twitter.com/kealanparr) if you enjoyed this article, and want to see more.
