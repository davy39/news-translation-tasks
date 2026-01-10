---
title: Event sourcing essentials you need to know when starting out
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T18:47:14.000Z'
originalURL: https://freecodecamp.org/news/event-sourcing-essentials-you-need-to-know-when-starting-out-13af35d9f932
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6-84rquRE2oH4sJXRIabKA.png
tags:
- name: '#Domain-Driven-Design'
  slug: domain-driven-design
- name: Event Sourcing
  slug: event-sourcing
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Noël Widmer

  Event Sourcing is a thought challenge when starting out. In this story, I will describe
  my experiences from the perspective of an engineer.

  My goal is to help you decide if you want to invest the resources to get started
  with Event Sou...'
---

By Noël Widmer

Event Sourcing is a thought challenge when starting out. In this story, I will describe my experiences from the perspective of an engineer.

My goal is to help you decide if you want to invest the resources to get started with Event Sourcing.

![Image](https://cdn-media-1.freecodecamp.org/images/vRIbN9ppLB4ixj1hzxbGQ6AcoQKdy-8Fi-xn)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo is offered a choice._

### About The Author

Hi ? I’m Noël. I live near Zurich (Switzerland) and am proudly working on Switzerland’s largest E-Commerce platform. My team and I have applied Event Sourcing throughout the last 12 months, and w**e learned a lot.**

I want to share four essentials with you that I wish we knew one year ago.

### A Tiny Introduction To Event Sourcing

This article is not about introducing you to the concepts of Event Sourcing.   
I still feel like I should take **one step** back though — to paint a clearer picture.

In state-oriented applications, you store the result of some computation in your data store. You might also keep a log where you archive old states for auditing or debugging purposes. But by storing state you lose the information about the transition from one state to the other. If a user’s username has disappeared, you’ll be wondering how that could have happened.

![Image](https://cdn-media-1.freecodecamp.org/images/w-5nI8fUU3m3DDBwt8QBX-g1g5YtG5F7A4OU)
_Storing state in a state-oriented application._

Sourcing events preserves that information. This is achieved by storing state transitions rather than the resulting state.

![Image](https://cdn-media-1.freecodecamp.org/images/H9prmbzan1lBxdV6YTG2H9xzWvxT8iLzrXZl)
_Storing state transitions (events) in an event sourced application._

The current state can be restored by applying all events to an empty canvas. That means we can still access the current state but need to invest computational resources to do so.

There are many articles on the web that go into more detail. Martin Fowler [wrote one about it](https://martinfowler.com/eaaDev/EventSourcing.html). And Greg Young [talks a lot about Event Sourcing](https://youtu.be/kZL41SMXWdM?t=2). Greg is so obsessed with event sourcing that [he implemented a data store which is specifically designed for event sourcing](https://eventstore.org/). My team is using Greg’s event store — it’s great!

### 1) Event Sourcing Is Not A Silver Bullet

Once you fall for the bitter sweet taste of Event Sourcing it becomes compelling to apply the concept to all your problems.

This will provide you with loads of data to analyze and you will have a powerful foundation to detect interesting correlations in it. You’ll be able to detect inefficient processes and make them more efficient.

And every engineer’s (my) favorite:

Tracking down a bug becomes much easier when you can “time travel” to the exact moment when the bug happened. In the end you will save time and money.

Well — not quite. ☝️

Sourcing your events sure allows you to do the analysis. **But you still need to do it.** This will cost time. Luckily, “time travel” comes for free. Enhanced debugging is thus guaranteed from day one.

Seth Godin wrote a [great blog post](https://seths.blog/2019/02/the-am-pm-problem-the-curse-of-too-much-data/) on the subject. It’s a 2 minute read, so check it out.

Now you know about the price you’ll pay if you use your events for analytical purposes which is the main business benefit of Event Sourcing after all.

There is another cost though. Event Sourcing will increase the complexity of your application. Instead of dealing with your application’s current state you’ll have to deal with everything that has ever happened since it went live. Events that are no longer used will remain in your data store and you’ll have to support them for a long time.

It’s great if you deploy a feature and keep iterating on it. Just be aware that there are now multiple versions of that feature’s events in your data store and you’ll have to support all of them. Even if you no longer create new instances of those events.

Event Sourcing imposes additional time complexities that you will have to get used to. Apply it where you see a non-zero chance that the collected data becomes relevant. Where I’d define “relevant” as:

* the data could give you more insight into your domain
* the data could help your business to improve their processes on their own
* the data could help you find bugs faster

Note that I added the word “could” in each of the last three bullet points. It’s likely you won’t know the exact benefit of Event Sourcing in advance. Make your best guess.

### 2) Recognize The Functional Nature Of Event Sourcing

The authors of the famous [Patterns, Principles, and Practices of Domain-Driven Design](https://www.amazon.com/Patterns-Principles-Practices-Domain-Driven-Design/dp/1118714709) recommend object-oriented programming languages like C# or Java.

I assume that the implicit reasoning behind that recommendation is the number of people using such languages. It’s true. New team members will likely have an easier start into the domain when confronted with familiar languages.

But I disagree. [So does Greg Young](https://youtu.be/kZL41SMXWdM?t=2). **Event Sourcing is not an object-oriented concept.**

One might argue that state transitions are objects too. And indeed. You can model everything as objects. Just because you can does not imply that this is the best model to use.

Consider using a language that supports functional paradigms. Especially [tagged unions](https://en.wikipedia.org/wiki/Tagged_union) and [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching) are extremely valuable. Working with your events will feel natural and you won’t have to fight your language’s type system. If your team has no experience with the functional world it might be best to stick to familiar languages though.

Even more important to understand is that **choosing a relational data store will be a painful experience**. You’re not dealing with relational data when sourcing your events. Each event has its own schema which can change over time. Using a relational data store will hurt.

> [SQL is the master of nothing but it sucks at nothing.](https://youtu.be/kZL41SMXWdM?t=1597) - Greg Young

### 3) Expect A Steep Learning Curve

As with all new things there will be learning involved. Don’t try to sidestep it. That won’t work.

![Image](https://cdn-media-1.freecodecamp.org/images/0jNwGHRNDnjJDzwwr2h76zYC7XkT91P1oIv2)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo learns something special._

A great way to learn is to prototype. Try this:

* build at least one prototype of your first event sourced application
* run and observe your prototype for a while
* implement new features and get used to iterating on what you’ve built

Iterate as often as possible before your go live. Once you are live it won’t be as easy to implement new learnings.

Go live once your team feels confident with maintaining the application.

Also think about how your team will introduce new team members to Event Sourcing. New joiners are already in an overwhelming position and learning new concepts won’t make it any easier for them.

Figure out a way to introduce them to Event Sourcing in a soft and safe way. This is important to figure out once you start getting new team members. It’s fine to delay it until that happens.

### 4) Prepare for political debates

Have you realized that your company wants **cheap** and **quality** results **today**?

Oh my, who am I talking to — of course you did. ?

Will _they_ like it when you experiment with a mind-bending concept _they_ might never heard of? And what is your company’s tech stack like? Do you usually use object-oriented programming languages in combination with relational data stores? Will _they_ like it when you switch to a functional tech stack?

Depending on your companies culture you might have to fight your colleagues on multiple fronts. Act as an example. Tell the truth. You know it will be hard, especially in the beginning. Share your concerns. Make sure everyone involved knows the risks and what you’ll do to prevent them.

And don’t leave out how you picture the Event Sourcing paradise. Get the business on board by allowing them to build reports based on your valuable events. They’ll love it.

Get the concerned engineering people on board by sharing the improved debugging experience. Engineers are stubborn, they might still not like it.

I found it useful to practice such debates with my colleagues. Establish a safe environment for training and encourage your team members to take part.

![Image](https://cdn-media-1.freecodecamp.org/images/Y7d79Cv8qbHMWOoWken3t-86JsVOnSWRJ-n3)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo trains in a safe environment._

Be ready and know your stuff. You’ll make it! ?

### Conclusion

Let me summarize.

* More data isn’t always good.
* Additional data without the time to analyze it is useless.
* Analysis without the intention and time to act on the result is useless.
* Event Sourcing enhances the ability to debug your application.
* Event Sourcing is a functional paradigm.
* Expect a steep learning curve.
* Not everybody will be happy about your plans.

That’s it. My intention was to prepare your expectations to my experiences. Don’t worry. Be determined and **choose the red pill!**

### The Matrix

All images in this story are borrowed from the movie [The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&qid=1550756146&s=movies-tv&sr=1-6).

I’ve spent 9 years writing object-oriented code and working with relational data stores. About two years ago I started to experiment with functional code and non-relational data stores. The mind shift has been one of the most important lessons in my career to date.

Question your environment. Find the flaws. Exit the Matrix and get to experience a whole new world.

Farewell. Until next time. And good luck!

![Image](https://cdn-media-1.freecodecamp.org/images/nCTTljApCmGwNVYDCtgOabSoZ6V7wjQIvAC0)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo receives a goodbye gift._

**I only write about programming and technology. If you follow me, I won’t waste your time.** ?

