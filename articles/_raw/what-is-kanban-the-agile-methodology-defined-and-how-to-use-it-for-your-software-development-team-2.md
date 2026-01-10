---
title: What is Kanban? The Agile Methodology Defined, and How to Use it For Your Software
  Development Team
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-19T11:12:13.000Z'
originalURL: https://freecodecamp.org/news/what-is-kanban-the-agile-methodology-defined-and-how-to-use-it-for-your-software-development-team-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/grafik-8.png
tags:
- name: agile
  slug: agile
- name: kanban
  slug: kanban
- name: Scrum
  slug: scrum
- name: software
  slug: software
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Bertil Muth

  Kanban was invented in the Japanese automotive industry in the first half of the
  20th century. Inspired by how supermarkets stock their shelves based on demand,
  Toyota''s goal was to reduce inventory and to improve the flow throughout t...'
---

By Bertil Muth

Kanban was invented in the Japanese automotive industry in the first half of the 20th century. Inspired by how supermarkets stock their shelves based on demand, Toyota's goal was to reduce inventory and to improve the flow throughout their whole production system.

In his book _Kanban: Successful Evolutionary Change for Your Technology Business_, David Anderson described how to apply the Kanban principles to software development. These principles are:

* Start with what you do now
* Agree to pursue incremental, evolutionary change
* Respect the current process, roles, responsibilities, and titles

## What does that mean for agile software development?

In my training courses, I ask the attendees what they already know about [agile software development](https://agilemanifesto.org/). Common answers are: "Work in Sprints", "There's a product owner", "Manage user stories in a backlog." People are influenced by the arguably most popular agile framework today, Scrum. 

Scrum comes with its own predefined roles, events and artifacts. Scrum requires you to follow the rules defined in the [Scrum Guide](https://www.scrumguides.org/), if you want to call what you're doing Scrum. Kanban is different.

Kanban starts with the process that you follow in your company now. Visualize the steps on a Kanban board. They can include everything you do, from idea to delivery. 

Each step becomes the title of a column on the board.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik-7.png)

To track your day to day work, it's best to break it down into small items. Maybe user stories that can be implemented in, at most, 2 days. Write each item on a stickie note, and hang it on the board. You can use the vertical order on the board for prioritization.

The cards move from left to right. The people doing the work pull items that have been finished by the previous process step. When they have capacity to do so. So the developers in the example pull the _Upload Image_ card into _Dev_ when they have the capacity to implement it.

## Pursuing incremental, evolutionary change 

So you have created a Kanban board that shows your process? You are making your work visible, which is a great start!

To get the benefits of Kanban, you need to do some more things. You need to:

* Limit work in process and queues
* Observe and improve flow
* Collaborate effectively

### Limit work in process and queues

Limiting work in process means: you set a maximum for the number of items you work on. That's called the Work-in-Process limit, or in short WiP limit. Here's the Kanban board with a WiP limit for some process steps.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik-9.png)

The developers can work on 5 items at a time. At most. If their column contains 5 items, they are not allowed to pull items any more. This has two consequences.

First of all: it encourages people to finish their work, instead of starting more work. Started work that isn't finished bears risks. How happy will your customers be when you can't release your software as planned? Because you started to work on all these great ideas, but you didn't go through with them? 

The second consequence of limiting work in process: bottlenecks become visible. When a process step starts work that it can't finish, people will feel it immediately. Because the next process step won't be able to pull items.

Apart from limiting the work in process, you should limit queue sizes, too. In the board above, they are shown as the dotted lines between the columns. It works the same way as limiting the work in process.

In summary: _Stop starting, start finishing_ is the motto. From concept to delivery in as little time as possible.

### Observe and improve flow

Observing a bottleneck can be painful at first. But at least you know where the major problems are in your process. And Kanban encourages you to improve the flow by removing the bottleneck.  A consistent flow enables you to deliver more reliably, and that's good for all stakeholders, including developers.

To observe the flow, you record the time at which a card enters a process step. And the time at which you complete the process step. So you know how much time the card spends in each step, and in each queue between the steps.

Based on the data, you can set up metrics that help you to improve the flow. Common metrics include:

* Cycle time: the time a card takes from the moment a team starts working on it (i.e. _Dev_) to delivery (i.e. _Release_). Improving this metric can help you improve your time to market.
* Throughput: the number of cards that move through the system in a given time. Improving this metric can help you improve the performance of your delivery organization.

A common way to get an overview of how many cards are in which process step over time is a cumulative flow chart. Ideally, the number of cards in each step but the last stays roughly the same over time. The number of released cards should mount. When the chart deviates from that, you might have a bottleneck.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Cumulative_Flow_Chart.png)

### Collaborate effectively

The Kanban metrics are a powerful tool to analyze and improve what you're doing. But they are worthless without the people doing the work. Everybody involved in the process steps should be open to the transparency that Kanban creates. 

People should work together constructively to remove bottlenecks, instead of blaming individuals. Look at the current state regularly. Are there any bottlenecks? Is there too much or too little work available for a certain process step? Is throughput sufficient? Are there other sources of discontent? What needs to be improved?

Agree on experiments that try out small changes to the system. Realize the changes. Later, look if the experiments worked out as expected. To be able to implement the changes, management support is often crucial.

## When to use Kanban

Kanban is very flexible. It can be used in combination with Scrum, which is called [Scrumban](https://en.wikipedia.org/wiki/Scrumban). It can be used outside of product development. You can even use it to plan a trip or organize what you do in your free time.

I found it especially helpful when working in Scrum Sprints is not possible or is difficult. Example: two companies where one is customer, and the other is supplier, and a hand-off is inevitable. Another example is when you're working on a product that involves both software and hardware, and multiple engineering disciplines are involved. 

Kanban can also be used inside your company when development works in an agile fashion, but not all of the rest of the company does.  It can be used to facilitate the cooperation between strategic planning and software development.

Don't think that just because you have trouble implementing Scrum, there's no way to become more agile. Kanban starts with what you do now. And if you take it seriously, it will help you improve. One small step at a time.

_To_ [_learn more about agile software development_](https://skl.sh/2Cq497P)_, visit my online course. To keep up with what I’m doing or drop me a note, follow me on_ [_dev.to_](https://dev.to/bertilmuth)_,_ [_LinkedIn_](https://www.linkedin.com/in/bertilmuth/) _or_ [_Twitter_](https://twitter.com/BertilMuth)_. Or visit my_ [_GitHub project_](https://github.com/bertilmuth/requirementsascode)_._

