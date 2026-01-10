---
title: What is Abstraction in Coding? A Guide for Beginners
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2024-03-19T22:29:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-abstraction-in-coding
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/EmbraceAbstractions-.png
tags:
- name: abstraction
  slug: abstraction
- name: beginners guide
  slug: beginners-guide
seo_title: null
seo_desc: 'I''ve met and talked to multiple new coders recently, and I see a common
  mistake they all seem to make.

  They don''t embrace and understand abstractions in their code, or in their learning.

  But what are abstractions? And why are they important?

  Let''s di...'
---

I've met and talked to multiple new coders recently, and I see a common mistake they all seem to make.

They don't embrace and understand **abstractions** in their code, or in their learning.

But what are **abstractions**? And why are they important?

Let's dive in!

## What is an Abstraction?

In coding, developers often use **abstractions** to simplify a system. **Abstractions** are a way of hiding complicated details from the end user, and trying to simplify whatever task you're trying to do.

But abstractions can be used in more than just code, so let's start with an example.

### Coffee machine abstractions

Imagine if you were creating a machine to make coffee for your users. There could be two approaches:

#### **How to Create it With Abstraction**

* Have a button that says "Make coffee"

#### **How to Create it Without Abstraction**

* Have a button that says "Boil the water"
* Have a button that says "Add the cold water to the kettle"
* Have a button that says "Add 1 spoon of ground coffee to a clean cup"
* Have a button that says "Clean any dirty cups"
* And all the other buttons

Can you see how, when we use abstraction, we don't expect the user to know how the machine makes coffee? But in the machine without abstraction, the user has to know in which order to press each button, which forces the user to understand how the coffee is made.

## Why You Should Abstract Your Details

When we use abstractions well, we make our system/codebase/task and so on much easier to understand and use. By hiding away complicated details inside a module, class, prototype, or function, we can make a super simple way to do complicated things.

So for example, let's say we have some complex code that ends up doing lots of complex, hard to understand math. We can wrap all that logic up in a function and provide a really easy interface where you just pass in your number and the function will do the work. 

Developers in all languages and across all ecosystems make use of abstractions. The NodeJS team doesn't force you to understand how to modify 0's and 1's on a hard-drive to save text into a file – you can simply call the `writeFile` function.

When we use abstraction, we are essentially not forcing the person who uses our code to worry about the implementation details. They can just call the function and they'll get their answer back – they don't have to worry about what the function is doing "under the hood".

_That's_ the strength of abstracting details away in your code.  
  
I used to work at a company with a codebase that was 4 million lines long. Can you imagine a senior developer expecting me to understand every function? Every module? Every class? I would have NEVER merged a single change in that codebase if I did!

You can create a reusable, simple to understand, and easily changeable codebase by **abstracting** away certain details into the correct modules/separating out your code.

## An Example Abstraction

Let's try and illustrate this with a code example.

Imagine you're working on a banking app, and you keep coming across this same weird subtraction over and over again, in different places in the code.

`const res = bankAccountBalance - 1200`

`const res = bankAccountBalance – 1500`

`const res = bankAccountBalance - 1400`

Why do we keep subtracting random numbers from everyone's bank balance once a year?! This is so unclear, there are zero comments explaining this?! What's happening? Is this an error?

Now imagine if this feature was clearer and did this:

```javascript
const minusFeesInUSDollars = (bankAccountBalance ) => {
	// Our yearly fees for this account are 1200 (USD)
    const YEARLY_FEES = 1200;
    return bankAccountBalance - YEARLY_FEES;
}
const minusFeesInGBPounds = (bankAccountBalance ) => {
	// Our yearly fees for this account are 1500 (GBP)
    const YEARLY_FEES = 1500;
    return bankAccountBalance - YEARLY_FEES;
}
const minusFeesInEuros = (bankAccountBalance ) => {
	// Our yearly fees for this account are 1400 (EUR)
    const YEARLY_FEES = 1400;
    return bankAccountBalance - YEARLY_FEES;
}
```

The example isn't perfect, because we could remove some duplication in these functions – but we have abstracted logic into "something", in this case, a function.

## Why Should I Embrace Abstractions?

I have explained **abstractions** so far in the context of code, but it can apply to your learning journey as well.

If you can't embrace **abstractions** (at least when you are starting) you will never be able to understand and excel as a developer.

Why is this the case?

Well, because there is always an **abstraction** beneath you, that you will be tempted to try and understand. This will ultimately frustrate you, overwhelm you, and **kill your learning.**

 Here's an example.

1. You start to learn React.  
  
_This is going well! I'm starting to learn my first few bits of code and render some things to my computer screen. This is going well. 😊_
2. You learn that React is a library of JavaScript.  
  
_Okay that's cool! I should learn a little bit of JavaScript before I start with React then. I'm going to stop learning React, and learn vanilla JavaScript first._
3. You learn JavaScript is a programming language made up of lots of different pieces.  
  
_Okay this is getting more complex now. There are JavaScript engines, third party API's, different runtimes. This is getting confusing._
4. You try to understand how an engine interprets JavaScript code.  
  
_Okay! So your JavaScript code is being run, by a piece of software coded in C++. What is C++?_
5. You start to learn C++.  
  
_This learning journey isn't going so well anymore. This is starting to get very confusing and much longer._
6. You learn that C++ is simply an extension of C.   
  
_What on earth is C?!_

...and so on.

If you continue to dig deeper and deeper and deeper, into every tiny little detail, you are much more likely to quit your learning journey, and it will only be because you feel overwhelmed.

And if by some miracle you haven't given up, you're going to spend a much, much longer time trying to learn some basic skills you might need for a job.

## How Do You Embrace Abstractions?

As you're learning, you're going to have to get comfortable with not fully understanding some things in your learning journey.

You can just "abstract" this knowledge away, and stick to the things that are relevant to what you're currently doing.

Don't chase down every tiny little detail that you encounter if you are new in your learning journey. Truth is, even the experts don't know everything! They normally know lots of things in a narrow area.

## One Day You Can Dig into the Abstractions

I don't want this article to come across like I am saying you should never delve below the abstractions you use everyday. But what I am saying is it won't help you to delve into the abstractions **before** you have spent a decent time coding first.

You should try to learn things as you need to learn them if you are early in your journey to become a developer.

After all, learning to code is hard enough, without committing to learning the entire ecosystem before even understanding the basics.

Once you start to become comfortable in your learning journey, and want to improve your skills, [then learn how your abstractions work](https://www.hanselman.com/blog/please-learn-to-think-about-abstractions).

## Conclusion

I hope this has been useful, and is encouraging if you are feeling overwhelmed with everything you're currently learning.

I tweet my articles [here](https://twitter.com/kealanparr) if you would like to read more.

