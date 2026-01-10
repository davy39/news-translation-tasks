---
title: What to keep in mind when architecting a system
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T17:54:27.000Z'
originalURL: https://freecodecamp.org/news/what-to-keep-in-mind-when-architecting-a-system-912ec5c6f79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GRF6gYIhUy5WBdbsqLWm3A.png
tags:
- name: Devops
  slug: devops
- name: software design
  slug: software-design
- name: software development
  slug: software-development
- name: System Architecture
  slug: system-architecture
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ayelet Sachto

  Architecture may sound like a “scary ” or overwhelming subject, but actually, applying
  logic and approaching the problem methodologically simplifies the process drastically.

  When you architect a system, service, or feature, you actua...'
---

By Ayelet Sachto

Architecture may sound like a “scary ” or overwhelming subject, but actually, applying logic and approaching the problem methodologically simplifies the process drastically.

When you architect a system, service, or feature, you actually design a **solution** to a problem in a **specific context**. The solution should answer a real need and solve the problem **at hand.**

Throughout the text, I’ll be using **solution** in order to emphasize that the **systems, services, and features** we build are part of a bigger **flow**.

![Image](https://cdn-media-1.freecodecamp.org/images/i1p8jGfhA263VAS7AsivCRtMxclqCJV36XT5)

When designing a solution think about the entire environment flow you affect.

* Think about what happens before the data reaches your code
* What triggers your feature or service
* Who sends it?
* Is it something automatic?
* Is it a user?

This will also help you think about tests and edge cases you want to address, what happens after, who would use it and how.

#### 1.Understand the problem

Start from understating the problem at hand and understand your boundaries. Don’t optimize for an unknown future, focus on the current situation and most importantly, **don’t make assumptions.** Don’t limit yourself by requirements that are not there.

> Make sure you have all the information you need to understand the problem, don’t be afraid to do research, Google is your friend ;)

![Image](https://cdn-media-1.freecodecamp.org/images/w9FZSfuNF8PsaTT9F8Puxl4mqP1gcDKVTEbI)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### 2. Understand your boundaries and set priorities

Solution architecture is always a trade-off between concerns, such as resilience, security, data integrity, throughput, scalability, performance and of course cost.

> Think about value vs friction

Understand your constraints. What are your **must-haves**. If you have a product team, work with them in order to understand the business need, impact and SLA’s. This will help you understand your considerations and limitations better.

Use **data** to make **priorities**, avoid assumptions when possible and be data-driven.

* How many users?
* Number of requests?
* Size of requests?

Test your service in order to estimate the resources that are needed.

> Make sure you address the maximum rate you want to support and not only the average (look at percentage vs average).

Think **about** solving the problem and not just **how** to solve it. First think about the solution and only after that think about the implementation. When you free yourself from the expectation of how the solution **should** look like, you understand that a solution can be provided in many forms. It can be a system, service, feature, process or even documentation.

#### 3. Ask WHY?

Challenging people and even yourself can be frustrating sometimes. But asking **why** can help you solve the real problem, understand the mandatory requirements and your boundaries, and can help you avoid mistakes and understand the motivation from the business side.

* Why is it a real pain?
* Why should it be done like this?
* Why it works like this today?

> Challenge yourself and ask questions. It will help make better decisions and better solutions.

![Image](https://cdn-media-1.freecodecamp.org/images/9T5m8DCeqFgZhYxrTs1XjV5MMWIWK42xILAl)
_Photo by [Unsplash](https://unsplash.com/@emilymorter?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Emily Morter</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### 4. Your solution is not in a vacuum

Context is important. A startup of 4 people that needs to provide MVP and is limited by funds will and should solve a problem differently than a team in a big organization that needs to create a sustainable product that will need to be maintained by several teams.

Going back to my first statement, after you understand the problem think about the context.

* What are the tools you have at your disposal?
* Are you part of a big organization?
* Are there any limitations such as time or money?
* Who will maintain the solution?

Think about what is right for **your** situation, define what _production ready_ means to **you**, and whether it should be highly available (HA). Think about the [ROI](https://en.wikipedia.org/wiki/Return_on_investment). Should you address Edge cases?

* How would you design a solution that will return values from a database?
* And what if I told you that it would be used only once a week until the end of the year. Would it change your answer? Would it affect the design?
* If you have 1 day to build a solution would it be the same as if you had a month?

**Think about growth**. For different solutions and different companies, growth means different things. It can be from a **scale** perspective, such as supporting the growth of additional users. It can also be from a **functionality** perspective, where your solution should be **flexible** to enable other developers to add /modify functionality with ease.

#### 5. Cost

As engineers and developers, we sometimes do not stop to think about the cost of our solutions and services. From my experience it is mostly due to lack of awareness and not willingness.

When we are at university, we are “pumped” with performance and complexity concerns, and taught to think about the efficiency of the solution. But when designing a product that will be used, we need to also think about efficiency with regards to cost. You can build an amazing stable and reliable service that provides value, but if its ROI is not high or if your company won’t be able to afford the cost, it will be axed in favor of other alternatives.

> Remember, performance and infrastructure are not free.

#### 6. Production deployment is only the beginning

An important concept that sometimes is neglected is **maintenance**. Is our system or service stable and easy to maintain, debug, troubleshoot and fix?

Production deployment is only the beginning of our solution. Make sure it can be easily maintained, make sure it is production ready and can serve real traffic and users. When developing your solution, think about end to end monitoring, focusing on application monitoring vs. utilization, and make sure to add logging and documentation.

> When designing your solution, think about a simple and easy to maintain design, as much as the requirements allow for it of course.

As developers, we are sometimes drawn to new “flashy” and trendy technologies. Stop to think whether this technology is mature enough. Could it be maintained in production? Could a different stack be more efficient or offer fewer risks?

#### Wrapping up

To recap, if you want to architect the best solution EVER, start from understanding the problem and your limitations, and know the context of the solution you are trying to design for.

Then think about what happens with your solution after it’s up.

Unless you have unlimited funds (which is never the case), think about your solution’s cost and make sure that it maintainable.

If you liked what you read, be sure to ? it below!

Let me know in the comments ❤ if you like more architecture posts and/or would like me to deep dive about each of the points above.

