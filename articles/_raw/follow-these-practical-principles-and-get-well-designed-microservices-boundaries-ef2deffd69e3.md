---
title: Follow these practical principles to get well-designed microservices boundaries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T10:33:28.000Z'
originalURL: https://freecodecamp.org/news/follow-these-practical-principles-and-get-well-designed-microservices-boundaries-ef2deffd69e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gKsnN4cbdRZfueyRWA6fjg.jpeg
tags:
- name: Design
  slug: design
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jake Lumetta

  How to avoid making your microservices too small and tightly coupled


  _Photo by [Unsplash](https://unsplash.com/photos/aIYFR0vbADk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" titl...'
---

By Jake Lumetta

#### How to avoid making your microservices too small and tightly coupled

![Image](https://cdn-media-1.freecodecamp.org/images/HCYtimj7KjfKRnaZ1wl8f1qu03qPfosHMamw)
_Photo by [Unsplash](https://unsplash.com/photos/aIYFR0vbADk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Erol Ahmed</a> on <a href="https://unsplash.com/search/photos/complex?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

One of the [core benefits of developing new systems with microservices](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith) is that the architecture allows developers to build and modify individual components independently. But problems can arise when it comes to minimizing the number of callbacks between each API.

Chris McFadden, VP of Engineering at SparkPost, recounted a story of microservices design pitfalls that may sound familiar to other developers.

In the early days of SparkPost, McFadden and his team had to solve a problem that every SaaS business has: they needed to provide basic services like authentication, account management, and billing.

The core problem, of course, wasn’t how to charge their users money. It was how to design their user account microservices to support everything that goes along with that problem domain: user accounts, API keys, authentication, business accounts, billing, and so on.

To tackle this, they created two microservices: a Users API and an Accounts API. The Users API would handle user accounts, API keys, and authentication, and the Accounts API would handle all of the billing related logic. A very logical separation, but before long, they spotted a problem.

“We had one service that was called the User API, and we had another one called the Account API. But the problem was that they were actually having several calls back and forth between them. So you would do something in accounts and have call and endpoint in users or vice versa,” Chris stated.

The two services were too tightly coupled.

“We realized that in most cases, you really don’t want to have one service calling another service in a sometimes circular way. That’s generally not a good idea,” he explained.

The solution, according to McFadden, is to apply the appropriate service boundaries.

But how does one determine those service boundaries? In contrast to the sometimes difficult-to-grasp and abstract concept of domain driven design (DDD) — a framework for microservices — practical wisdom from experienced CTOs offers a better framework for designing microservice boundaries. That wisdom, from hours of interviews, is distilled below.

### Avoid Arbitrary Rules

When designing and creating a microservice, don’t fall into the trap of using arbitrary rules. If you read enough advice, you’ll come across some of the rules below. While appealing, these are **not** proper ways to determine boundaries for microservices.

#### **Arbitrary Rule #1: A microservice should have X lines of code**

Let’s get one thing straight: there are no limitations on how many lines of code there are in a microservice. A microservice doesn’t suddenly become a monolith just because you write a few lines of extra code. The key is ensuring there is high cohesion for the code within a service (more on this later).

#### **Arbitrary Rule #2: Turn each function into a microservice**

If you have a function that computes something based on three input values, and returns a result, is that a good candidate for a microservice? Should it be a separately deployable application of its own? This really depends on what the function is and how it serves to the entire system.

#### **Other arbitrary rules**

Other arbitrary rules include those that don’t take into account your entire context such as the team’s experience, DevOps capacity, what the service is doing, and availability needs of the data.

### Five characteristics of a well-designed service

If you’ve read about microservices, you’ve no doubt come across advice on what makes a well-designed service. Much of it boils down to the principle of high cohesion and loose coupling. While sound advice, these concepts are quite abstract.

I’ve spoken with dozens of CTO’s on this topic to learn from them how they’ve drawn their microservice boundaries. I’ve distilled down some of the underlying characteristics for you below.

#### **Characteristic #1: A well-designed service doesn’t share database tables with another service**

As we saw in Chris McFadden’s case mentioned above, when it comes to designing a microservice if you have multiple services referencing the same table, that’s a red flag as it likely means your DB is a source of coupling.

It is really about how the service relates to the data, which is exactly what Oleksiy Kovrin, Head of Swiftype SRE, Elastic, told me.

“One of the main foundational principles we use when developing new services is that they should not cross database boundaries. Each service should rely on its own set of underlying data stores. This allows us to centralize access controls, audit logging, caching logic, et cetera,” he said.

Kovyrin went on to explain that if a subset of your database tables, “have no or very little connections to the rest of the dataset, it is a strong signal that component could be isolated into a separate API or a separate service.”

Darby Frey, co-founder of Lead Honestly, echoed this sentiment: “Each service should have its own tables [and] should never share database tables.”

#### **Characteristic #2: A well-designed service has a minimal amount of database tables**

The ideal size of a microservice is small enough, but no smaller. And the same goes for the number of database tables per service.

Steven Czerwinski, Head of Engineering at Scaylr, explained to me during an interview that the sweet spot for Scaylr is, “one or two database tables for a service.”

Chris McFadden elaborated in a similar vein: “We have a suppression microservices, and it handles, keeps track of, millions and billions of entries around suppressions but it’s all very focused just around suppression so there’s really only one or two tables there. The same goes for other services like webhooks.”

#### **Characteristic #3: A well-designed service is thoughtfully stateful or stateless**

When designing your microservice, you need to ask yourself whether it requires access to a database or it’s going to be a stateless service processing terabytes of data like emails or logs.

Be clear about this upfront and it will lead to a better-designed service.

Julien Lemoine of Algolia explains, “We define the boundaries of a service by defining its input and output. Sometimes a service is a network API but it can also be a process consuming files and producing records in a database (this is the case of our log processing service).”

#### **Characteristic #4: A well-designed service’s data availability needs are accounted for**

When designing a microservice, you need to keep in mind what services will rely on this new service and what’s the system-wide impact if that data becomes unavailable. Taking that into account allows you properly design data backup and recovery systems for this service.

When speaking to Steven Czerwinski, he mentioned their critical customer row space mapping data is replicated and separated in different ways due to its importance.

In contrast, “the per shard information, that’s in its own little partition. It sucks if it goes down because that portion of the customer population is not going to have their logs available, but it’s only impacting 5 percent of the customers rather than 100 percent of the customers,” Czerwinski explained.

#### **Characteristic #5: It’s a single source of truth**

The final characteristic to keep in mind is to design a service to be the single source of truth for something in your system.

To give you an example, when you order something from an eCommerce site, an order ID is generated. This order ID can be used by other services to query an Order service for complete information about the order. Using the pub/sub concept, the data that is passed around between services should be the order ID, not the attributes/information of the order itself. Only the Order service has complete information and is the single source of truth for a given order.

### Additional considerations for larger teams

These guidelines should serve all teams well, but CTOs also mentioned considerations for larger teams to take into account when designing microservice boundaries.

For larger organizations, where entire teams can be dedicated to owning a service, organizational consideration comes into play when determining service boundaries. And there are two considerations to keep in mind: independent release schedule and different uptime importance.

“The most successful implementation of microservices we’ve seen is either based on a software design principle like domain-driven design, for example, and service-oriented architecture, or the ones that reflect an organizational approach,” said Khash Sajadi, CEO of Cloud66.

“So [for the] payments team,” Sajadi continued, “they have the payment service or credit card validation service and that’s the service they provide to the outside world. So it’s not necessarily anything about software. It’s mostly about the business unit [that] provides one more service to the outside world.”

Amazon is a perfect example of a large organization with multiple teams. As mentioned in an article published in [API Evangelist](https://apievangelist.com/2012/01/12/the-secret-to-amazons-success-internal-apis/), Jeff Bezos issued a mandate to all employees informing them that every team within the company had to communicate via API. Anyone who didn’t would be fired.

This way, all the data and functionality was exposed through the interface. Bezos also managed to get every team to decouple, define what their resources were, and make them available through the API. Amazon was building a system from the ground up. This allows every team within the company to become a partner of one another.

Travis Reeder, CTO of Iron.io, commented on Bezos’ internal initiative.

“Jeff Bezos mandated that all teams had to build API’s to communicate with other teams. He’s also the guy who came up with the ‘two pizza’ rule; a team shouldn’t be larger than what two pizzas can feed,” he said.

“I think the same could apply here: whatever a small team can develop, manage and be productive with. If it starts to get unwieldy or starts to slow down, it’s probably getting too big,” Reeder told me.

### Guidelines during testing and implementation

CTOs also offered insight into red flags to watch out for to determine if a service is too small or not properly defined.

**Look out for over-reliance between two services**

If two services are constantly calling back to one another, then that’s a strong indication of coupling and a signal that they might be better off combined into one service.

Going back to the example Chris McFadden shared at the beginning of this chapter where he had two API services, accounts and users that were constantly communicating with one another, McFadden came up with an idea to merge the services and decided to call it the Accuser’s API. This turned out to be a fruitful strategy:

“What we started doing was eliminating these links [which were the] internal API calls between them. It’s helped simplify the code.” McFadden informed me.

**Does the overhead of setting up the service outweigh the benefit of having it be independent?**

Darby Frey explained, “Every app needs to have its logs aggregated somewhere and needs to be monitored. You need to set up alerting for it. You need to have standard operating procedures and run books for when things break. You have to manage SSH access to that thing. There’s a huge foundation of things that have to exist in order for an app to just run.”

### Consider these characteristics

Designing microservices is a combination of art and science, but characteristics of successful implementations of microservices provide a great checklist when designing your next set of service boundaries.

A well-designed service:

1. Doesn’t share database tables with another service
2. Has a minimal amount of database tables
3. Is thoughtfully stateful or stateless
4. Has its data availability needs accounted for
5. Is a single source of truth

_If you’ve enjoyed this article, please help it spread by clapping below! For more content like this, follow us on [Twitter](https://twitter.com/ButterCMS) and [subscribe](https://buttercms.com/blog/) to our blog._

_Jake Lumetta is the CEO of [ButterCMS](https://buttercms.com/), and is publishing [Microservices for Startups](https://buttercms.com/books/microservices-for-startups/)._

_And if you want to add a blog or CMS to your website without messing around with Wordpress, [you should try Butter CMS](https://buttercms.com/)._

