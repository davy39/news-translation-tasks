---
title: Epics are dead. Here’s what we should do instead.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-18T21:59:26.000Z'
originalURL: https://freecodecamp.org/news/epics-are-dead-heres-what-we-should-do-instead-279bada1e644
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OaKd4OM6oZkPAvbQ.jpg
tags:
- name: agile
  slug: agile
- name: business
  slug: business
- name: Productivity
  slug: productivity
- name: Scrum
  slug: scrum
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Bertil Muth

  What has not been declared dead already? Test Driven Development was buried years
  ago. Still, it continues to spread. Of course, Agile is dead as well. But even traditional
  companies come into contact with Scrum. The dead continue to l...'
---

By Bertil Muth

What has not been declared dead already? [Test Driven Development was buried](https://dhh.dk//2014/tdd-is-dead-long-live-testing.html) years ago. Still, it continues to spread. Of course, [Agile is dead](https://www.youtube.com/watch?v=a-BOSpxYJ9M) as well. But even traditional companies come into contact with Scrum. The dead continue to live, but declaring something dead is always good for a snappy headline. In that sense, witness how I destroy epics as an agile practice.

### What are epics?

The term is vague. This has advantages. Epics are more for communication than specification. The vagueness makes them versatile. But there is a risk of misunderstandings. I stick to Mike Cohn’s definition:

> A Scrum epic is a large user story. ([Source](https://www.mountaingoatsoftware.com/blog/stories-epics-and-themes))

I use the term like this: An epic is a story that is too big to be implemented in a Scrum sprint. The items at the top of the Product Backlog are thus not epics, but little stories. Down in the backlog you will typically find epics. Over time, the epics are “sliced” into stories that can be pulled into a sprint.

That is what I have taught for years in my training courses. It seems to be the general consensus. Intuitive at first glance. I’m here to explain why it’s not practical.

### 3 impractical ways to deal with epics

So far, I’ve come across three ways companies deal with epics. None of them is practical. Let’s call them:

#### Dissolution

![Image](https://cdn-media-1.freecodecamp.org/images/OO4-EKucR2gZhVJilqHLfLwnBOBxvqM0fgkA)
_1. Dissolution_

#### Links

![Image](https://cdn-media-1.freecodecamp.org/images/hT9ibQZCCuFNl60RAWY2ZkOvmR7-1idajU0k)
_2. Links_

#### Trees

![Image](https://cdn-media-1.freecodecamp.org/images/9PrBM9HZpNEftSfygOJFwVKtoCpYMVZj15ga)
_3. Trees_

### 1. Dissolution

The principle of dissolution is simple. An epic is completely broken down into its components, the individual little stories.

For example, an epic “Book flight” of an online flight portal can be broken down into the individual process steps. So “Log in”, “Search flight”, and so on. Every process step becomes a story. The team estimates the story. As long as it is too big, the team continues to slice it. Once all stories are small enough to fit into sprints, the team deletes the epic and starts development for the stories.

It’s the underlying idea of completeness that bothers me. The dissolution suggests that a topic can be completed with a predetermined scope.   
But if changes to the stories are possible during development, you can’t define all the stories upfront.

The Scrum Guide says:

> A product backlog is never complete. […] Requirements never stop changing.

If you have to deliver a fixed scope, stop pretending. Forget about epics, and describe the detailed requirements upfront. Just don’t claim to be agile then.

### 2. Links

If you don’t dissolve your epics completely, it makes sense to use links. The epics remain, down in the backlog. You link new little stories to the epics from which they derive.

The risk is that over time, the amount of epics increases. The backlog becomes bloated. It contains epics that you don’t need any more. The stakeholder is no longer in the company. Or the topic is no longer relevant.

Of course, you can clean up your backlog from time to time. I regard this as non-value-added work. And you can avoid it, as I will describe later.

### 3. Trees

Another way is the depiction of epics and stories as a tree:

![Image](https://cdn-media-1.freecodecamp.org/images/fQdxdGv7x3ec26JpDMXcMLhbuvOwBjyXHO8F)
_Depiction of epics as a tree_

You group the little stories by epic. Not a bad idea. But what you lose is the ordered list of the backlog. How do you determine the implementation order then?

Of course you can use a digital tool that supports both views. The risk: you invest too much time and effort in the tools. What are the views? What are the attributes? What is the underlying data model? Interesting questions. But in an agile approach they should not have high priority.

In summary, the idea of grouping is good. But doing it is time-consuming.

### The alternative to epics

There has long been an alternative. It is even mentioned in the same blog post by Mike Cohn, which I linked above.

I am talking about _themes_.

A theme can be thought of as an additional attribute of the stories. Normally, several stories share the same theme. The story “Search flight” could have the theme “Book flight”. A snippet from the backlog could look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/-iL6f0xFP4aFfnxgRCmzK3Nkouv1csAh-S5m)
_User Stories with theme_

Themes are not managed as separate backlog elements. This eliminates the cleanup work discussed in the Links chapter. That’s good.

But what you lose is the process of gradual refinement from the big epics to the stories that can be implemented in a sprint. That’s bad.

Luckily, there are practices that make it possible to do this refinement outside of the backlog. One way to identify themes is a use case diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/A9k8qh6lfEKpCj0aqpFMpxLiuE4igVNT5cua)

The nice thing about such diagrams is that they show the “Big Picture” due to the high level of abstraction and the graphical representation. For that, a backlog is unsuitable.

The use case names later become themes in the backlog. But how do you get from the use cases to the stories? For this, Jeff Patton's Story Mapping is a good fit:

![Image](https://cdn-media-1.freecodecamp.org/images/KrweoAjq2JO5T6ckmRnIY7DRq5pPCd3HlH3E)

The top two lines of the example map show the use cases “Book flight” and “Manage profile” and their basic flow. Under the individual steps, the team hangs the alternatives: other processes, errors and so on. These yellow notes are called user tasks.

In Backlog Refinement, the team derives the stories from the user tasks. A task can serve as the title of the story. The team adds details like acceptance criteria to the stories.

### The consequences

Applying this alternative approach has consequences. For example, the Product Backlog will only contain stories for the next 1–2 sprints. So maybe 10–20 stories.

All activities like further prioritization, estimation and elaboration of the acceptance criteria only take place with these stories. As the 10th agile principle says:

> Simplicity — the art of maximizing the amount of work not done — is essential.

If management wants to have insights into the progress of development, this is possible on three levels:

* **Use case diagrams or themes** provide the long-term perspective for management. For 1 year, or even beyond. But: they are not suitable for specifying details.
* **Story maps** form the basis for release planning. Stakeholders interested in the release create the story map with team members. (Due to new findings, the scope may change during development.)
* Those who want to have a deep insight and influence the details during development participate in **Sprint Review** and **Backlog Refinement**.

Only at low altitude, we see the details. And the Product Backlog is basically like a shopping list. Would you write down what you want to buy in a year?

Last, but not least, the death of epics heralds the dying of consumerism. If you want something, you have to agree with the team and work closely together.

### Post mortem

In the discussion with colleagues, they pointed out that even after a dissolution of an epic, small stories can be added. That’s right, and for me it’s an acceptable solution. What is lost in this case, however, is the “Big Picture” that I have shown in the use case diagram.

Ultimately, the suitability of a product for users determines its success. Not how it was made. This applies to all development practices, including epics.  
Maybe you have come up with a sensible way to deal with epics? 

_Learn how to [manage your Product Backlog effectively](https://skl.sh/2Edz9Zu) by visiting my online course. This article was first published on [HOOD Blog](https://blog.hood-group.com/blog/2019/01/02/epics-sind-tot/) in German._

