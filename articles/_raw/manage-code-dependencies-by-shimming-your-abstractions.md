---
title: How to Manage Code Dependencies by Shimming Your Abstractions
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-04-19T23:19:44.000Z'
originalURL: https://freecodecamp.org/news/manage-code-dependencies-by-shimming-your-abstractions
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/Always-Shim-your-Abstractions.png
tags:
- name: clean code
  slug: clean-code
- name: dependency management
  slug: dependency-management
seo_title: null
seo_desc: 'Dependencies are a very common part of any sufficiently mature codebase.
  And it''s important to cleanly handle any third party code that your program relies
  on to function.

  There are multiple ways to get third party code included and updated. And I re...'
---

Dependencies are a very common part of any sufficiently mature codebase. And it's important to cleanly handle any third party code that your program relies on to function.

There are multiple ways to get third party code included and updated. And I read something recently which has easily become my favourite way of doing this, so I had to share it.

This method is to **Always Shim Your Abstractions.**

To properly break down what this means, let's define each word before we talk about the bigger idea that it encompasses.

## Abstractions

Developers often use **abstractions** in code to simplify a system.

**Abstractions** are a way of hiding complicated code inside something, and they normally provide an easy interface to use it. 

So for example, let's say we have some complex code that ends up doing lots of very specific math. We can wrap all that logic up in a function and provide a really easy interface where you just pass in your number and the function will do the work.

We are essentially not forcing the person who uses our code to worry about the implementation details. They can just call the function and they'll get their answer back – they don't have to worry about what the function is doing "under the hood".

_That's_ the strength of abstracting details away in your code. 

You can abstract things away in a multitude of data structures or code architecture. And you can abstract implementation details inside a prototype, class, function or more.  
  
If you had to understand every single line of code in a big codebase (let's say a 2 million line codebase) you'd never be able to start coding.

You can create a reusable, simple to understand, and easily changeable codebase by **abstracting** away certain details into the correct modules/separating out your code.

### How code abstraction works

An example of abstracting away logic would be: imagine if you were creating a machine to make coffee for your users. There could be two approaches:

#### How to Create it With Abstraction

* Have a button with the title "Make coffee"

#### How to Create it Without Abstraction

* Have a button with the title "Boil the water"
* Have a button with the title "Add the cold water to the kettle"
* Have a button with the title "Add 1 spoon of ground coffee to a clean cup"
* Have a button with the title "Clean any dirty cups"
* And all the other buttons

Can you see how when we use abstraction we don't expect the user to know how the machine makes coffee? But in the machine without **abstraction**, the user has to know in which order to press each button which forces the user to understand how the coffee is made.

There's one definition we need to cover before we can move on and understand the concept I introduced at the beginning (always shim your abstractions), and that's shimming.

## Shimming

**Shimming** is the act of putting something in front of something else to intercept data being passed. 

Let's look at an example of how it works.

Let's say a bank has a really old API that doesn't accept JSON due to some technical legacy defect. Instead it can only accept XML. We'll call this **LegacyAPI**.

But a high percentage of developers who want to hit this bank API want to send JSON. The bank refuses to change LegacyAPI as it's too risky and might break the API. So much of their system depends on it, and they can't risk doing lots of new development and taking huge parts of their system down if they make a mistake.

They could always **shim** LegacyAPI if they don't want to do new development on it.

They could do this by creating an API that sits "in front" of LegacyAPI. We'll call it **NewAPI**. 

The wording "in front" just means the order of who first deals with the network request. By "in front" we just mean NewAPI will be the first to receive the network requests. 

You would tell the developers they can now hit NewAPI with JSON as they wanted, and NewAPI will turn the JSON into XML for the LegacyAPI and both parties can be satisfied.

The bank can now expand their services (they can accept JSON, for example) via the NewAPI without changing their old legacy API that they were wary of changing.

This is just one example of **shimming**. And just to review, it is essentially adding something in front of something else to act like a man in the middle to pass data to something else.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-50.png)
_A diagram of how **NewAPI** intercepts **LegacyAPI** network requests._

Hopefully you have a good understanding of what shimming is and what abstractions are. Let's bring both definitions together to define what we mean by **Always Shim Your Abstractions**.

## Why You Should Always Shim Your Abstractions

### The problem

Whenever we need to manage our dependencies, we want to make sure we stop the third party code "leaking" all over our main code.

By "leaking", I mean that the dependency code is imported multiple times to different places that need it in your code.

If you let a dependency "invade" your source code, you are becoming increasingly tightly coupled to it each time you import it.

This can (at times!) mean you will be forced to code in the direction the library choses as you are tightly coupled to it. This may end up leading to significant cognitive overhead as you are increasingly trying to make this library work in your code, but it isn't in keeping with the rest of your architectural decisions.

This can make any refactoring you need to do take much longer than if you isolated it. For example, if the dependency changes, what arguments would it need to accept to create an object in the dependency?

In addition to it being difficult to keep your build working well with the dependency, if it no longer suits your needs or you find a better library to replace it, your refactor becomes much more difficult to actually get rid of it.

### The solution

To try and stop all the above from happening, firstly let's put any dependencies we need into their own modules where they're only referenced once in your codebase. 

This is in essence our **shim**.

Whenever you need the third party dependency, you just have to import the wrapper module we put around it, to act like a "man in the middle", to provide a level before we call into our third-party dependency.

This **shim** module also allows us to make our dependencies **abstractions**. The developers who need to use our third party dependencies can just use an abstraction instead (you'll probably end up just wrapping it in a function or simple class). You'll default the arguments to sensible defaults and try to remove as much of the nitty gritty implementation details as you can.

Anywhere else that needs this dependency will just load your module and then that module can be injected where necessary.

**Why?** One big reason we already discussed is that it stops your dependencies and your code from being too tightly coupled. 

This works when you only have it in only one module. As long as everyone that is loading your module respects an interface/data contract for that module, everywhere else "gets it for free". Then you only have to change one module for lots of other places to get access to something.

This then allows us to make changes far more easily, and keeps a clean separation of concerns in the code.

We have only spoken here about one dependency – but you can see how much worse this may get if, for example, you are relying on 25 other custom libraries and you need to understand how they work. This would generally be a pretty fragile codebase, and would be a code smell.

## HTTP dependency example

Let's look at an example of a dependency you might use that makes a simple HTTP client.

It's a basic dependency that lets you hit endpoints and pass JSON etc as data.

Let's imagine then we currently are using **Fetch** in Node and we want to use **Axios** (another HTTP client we want to now switch to). We've decided to drop Fetch and switch to Axios because our application is growing in complexity and we have found that Axios now fits our use-cases better.

If Fetch has leaked all over our codebase, then our refactor to remove it is going to be much harder than it needs to be.

Rather than just go to our one module where we **shimmed** the function call, we now have to go to every place where we use it. This creates a domino effect in the source code that inevitably will occur from changing something in multiple places.

```javascript
// You're now going to have to find any place you imported fetch
// Any place you alias'd it
// And deal with any source code failures wrapping around where you have used it once it's removed
// Which might be more complex than just simply searching for
const fetch = require('node-fetch');
```

We can improve this by wrapping the dependency into an appropriate **shimmed abstraction** and isolating its usage to one place.

You also get a win when onboarding people. They'll be able to see abstractions called `API` or `DataStore` which become clear signposts as to what your classes do (rather than a library that a developer may not be familiar with). 

```javascript
// In your abstractions, you get the power to give it a descriptive
// name, if the current name isn't clear in your code too, maybe like:

var Money = require('dinero')
```

This won't be an issue for well known dependencies like **Express** or **Lodash** maybe. But I don't have a perfect memory of every NPM package and what they do. 

When you've properly **shimmed** it, it doesn't even matter to the developers using your shim if you are using Fetch or Axios "under the hood". They'll never know the difference if you change it, as long as you are sensible with the shim.

# Conclusion

I hope this gave a good overview of the benefits of **shimming**, and how it helps you maintain your dependencies.

This whole article was influenced by the writings of Sarah Dayan, found [here](https://twitter.com/frontstuff_io/status/1264189583220244480), and shared with her consent.

I share my writing on [Twitter](https://twitter.com/kealanparr) if you enjoyed this article and want to see more.

