---
title: What is the Strangler Fig Pattern and How it Helps Manage Legacy Code
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-06-15T17:43:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-strangler-pattern-in-software-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Strangler-Fig.png
tags:
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Any sufficiently old codebase eventually starts to contain legacy code.
  Architecture, performance, comments, and more begin to degrade the moment after
  they are written.

  Some parts of the codebase last longer than other parts, but inevitably new codi...'
---

Any sufficiently old codebase eventually starts to contain legacy code. Architecture, performance, comments, and more begin to degrade the moment after they are written.

Some parts of the codebase last longer than other parts, but inevitably new coding standards emerge to reduce technical debt. Then you have to rework a large application, with zero downtime, making a "new way" of working without breaking anything in your release or development. 

The **Strangler Fig Pattern** is one effective way to solve this problem.

## What is a Strangler Fig?

The name **[Strangler Fig Pattern](https://en.wikipedia.org/wiki/Strangler_fig)** actually comes from a collection of plants that grow by "strangling" their hosts. 

They grow in areas where competition for light is intense, and they have evolved to have their seeds dispersed (normally by birds) to the top of a host tree where they can get sunlight easily. 

Their roots grow down around the tree and the seedlings grow upwards to consume all the sunlight they can. This "strangles" the tree and the fig seedlings can often kill their host tree they landed on.

Here's an image of a Strangler Fig, which I found on Wikipedia .

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-99.png)
_An image of a strangler fig, where the roots grow down the tree trunk to the soil whilst the seedlings grow up above the trees canopy. [Source](https://upload.wikimedia.org/wikipedia/commons/4/46/Ficus_watkinsiana_on_Syzygium_hemilampra-Iluka.jpg)._

So how does this apply to software? 🤔

# What is the Strangler Fig Pattern?

To completely re-write a large, complex codebase with lots of different interactions often with different teams results in a planning nightmare. 

In big complicated **brown-field** projects like this, going **big-bang** (where everything is released at once) generally forces you to: 

* understand every interaction in depth to ensure you won't break anything when you release
* have all new bug fixes done both in the new and old codebase as you re-write it
* keep both merged and up-to date
* spend weeks in test
* deal with tons of callouts and out of hours support for the new codebase's rollout 

To top it all off, it normally ends with developers doing a lot of overtime along with an influx of bugs.

One big difficulty we are trying to remove when we use the **Strangler Fig** is making whoever is using your software aware of where your new software is now accessible.

When you are rewriting your backend, for example, if you put everything on a new endpoint and kindly ask your users to point to your new endpoint. But then if something goes wrong, you may have to ask them all to point back to the old one. 

You may end up going back and forth between these two endpoints if you have really difficult bugs, which might frustrate your users.

When we use the **Strangler Fig pattern** we can avoid all the above.

## Why Strangle Our Code

The **Strangler Fig pattern** aims to incrementally re-write small parts of your codebase, until after a few months/years, you have strangled all your old codebase and it can be totally removed.

The rough flow is: add a new part to your system that isn't used yet, switch on the new part of the code – normally with a feature flag so it coexists with the old code – and finally remove the old code.

### Benefits of the Strangler Fig pattern

Aside from helping you avoid all the issues we've already discussed, it also:

* reduces your risk when you need to update things 
* starts to immediately give you some benefit piece by piece
* allows you to push your changes in small modular pieces, easier for release
* ensures zero down time
* is generally more agile
* makes your rollbacks easier 
* allows you to spread your development on the codebase over a longer period of time if you have multiple priorities.

There are multiple ways of implementing the **Strangler Fig pattern** and it depends on the system you're removing, and so on. So let's get concrete and cover an example.

## Façade Payment Provider Example

Let's say as an example you have a huge monolithic back-end codebase to handle payments. It is **huge**. A few million lines of code, with multiple endpoints, that you want to re-write into something new for your company, for a multitude of reasons.

Performance is now poor, the architecture is too confusing to onboard new developers, and there is lots of [dead-code](https://www.freecodecamp.org/news/antipatterns-to-avoid-in-code/) you need to remove but don't want to break anything. 

Breaking a huge codebase involving customer payments might just cause the unlucky developer who pushed up last to lose their job!

Okay. How do you slowly choke out this old codebase? Even more tricky, you don't want to just put a new endpoint there and force everyone to move. You have hundreds of customers using this software, they can't just flip back and forth between your endpoints if you have bugs and need to rollback.

Just to add one last challenge, you don't want to change your interfaces to these endpoints either. Everything being passed as arguments or returned should remain the same.

## The Strangler Fig Pattern-based Solution

We can create a façade that intercepts requests going to the legacy endpoints.

The new façade will hand off to the new API you've written, or hand off to the legacy API if you haven't rewritten that piece of the codebase yet.

This façade is essentially a [shim](https://en.wikipedia.org/wiki/Shim_(computing)) to catch network requests and hand them off to the right place. 

You can then gradually migrate across to the new API piece by piece, and your users will be unaware of any changes to your underlying code as you have correctly abstracted it away.

If you are doing this correctly you will generally:

* Just have the legacy way at the beginning
* Make the new API 
* Make it coexist with the legacy API, where you can turn it on and off with feature flags
* Move more and more across to the new API
* Delete the old way when fully migrated

The **strangling** part is happening piece by piece where you remove more and more responsibility from the legacy API and into the new API.

## **Conclusion**

I hope this has explained what the **Strangler Fig Pattern** is along with some of its benefits.

I have seen this pattern used in real software projects and it works _really effectively._ It was easily one of the most complicated projects I worked on and the **Strangler Fig** made it so much easier.

It stops you from writing software projects for months, and then crossing your fingers and sending it to production whilst hoping you haven't forgotten anything.

There were two invaluable resources that were very useful when I was writing this:

* _Strangler Fig Application_ by Martin Fowler [here](https://martinfowler.com/bliki/StranglerFigApplication.html), and 
* _Avoid rewriting a legacy system from scratch, by strangling it_ found [here](https://understandlegacycode.com/blog/avoid-rewriting-a-legacy-system-from-scratch-by-strangling-it/).

I share my writing on [Twitter](https://twitter.com/kealanparr) if you enjoyed this article and want to see more.

