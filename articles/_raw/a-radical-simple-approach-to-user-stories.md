---
title: A radically simple approach to user stories
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-17T19:01:36.000Z'
originalURL: https://freecodecamp.org/news/a-radical-simple-approach-to-user-stories
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/adorable-book-boy-1250722.jpg
tags:
- name: agile
  slug: agile
- name: backlog
  slug: backlog
- name: Scrum
  slug: scrum
- name: user story
  slug: user-story
seo_title: null
seo_desc: 'By Bertil Muth

  User stories are a great way to plan development work. In theory. But how do you
  avoid getting burned in practice? I propose a radically simple approach.

  Here''s a popular template to describe a user story:


  Here''s an example user story...'
---

By Bertil Muth

User stories are a great way to plan development work. In theory. But how do you avoid getting burned in practice? I propose a radically simple approach.

Here's a popular template to describe a user story:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/grafik-18.png)

Here's an example user story:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/grafik-22.png)

User stories look at software from a perspective of user value. After implementing a story, the developers can get feedback from users whether they're satisfied or if there's something they'd like changed. That's the core idea of agile development.

Good user stories follow the three Cs: **Card**, **Conversation**, and **Confirmation** [1].

**Card** means: user stories are short. They focus on the value provided to the user. You can write them on an index card, or a Post-it. Of course, a Post-it doesn't contain all the information necessary for development.

So the team developing the software has **conversations** about the stories. Input from users and business stakeholders is necessary, but developers bring their ideas to the table as well. It's important that everybody keeps an open mind in these discussions. 

The team documents the results of the conversations as acceptance criteria. Checking the acceptance criteria later serves as **confirmation** that the team has implemented the story correctly.

## Acceptance criteria and INVEST

The acceptance criteria should answer questions like:

* What are the possible user inputs?   
For example: "The payment options are MasterCard, Visa, [...] PayPal_."_
* How does the system react to user input, or a business relevant event? Under which conditions?  
For example: "When the user enters a wrong credit card number, the system shows the following error message: [...]"

There are many ways to document acceptance criteria. Bullet points, sketches, examples, tables. Development starts a few days after the conversation about the story. So developers need just enough documentation to remember the conversation.

How does a team check if a story has a good enough quality to start implementing it? The **INVEST** criteria define a quality checklist for each story [2]:

* **I** for **Independent**. The story can be implemented independently of other stories. This facilitates priority changes.
* **N** for **Negotiated**. The conversation between developers and stakeholders about the details of the story has happened.
* **V** for **Valuable**. The story provides visible value for users. In contrast to implementation tasks like querying the database, for example.
* **E** for **Estimable**. The developers can estimate the story.
* **S** for **Small**. The story can be implemented quickly. In Scrum for example in a Sprint.
* **T** for **Testable**. The story is so concrete that the team can derive test cases.

## The problems in practice

I like user stories. In product planning, they shift the focus from technical details to users and their needs. That's good.

And yet, in my work as an agile coach and trainer for agile approaches, I've started questioning the common way people deal with them.

I've seen backlogs with hundreds of stories that became extremely hard to manage. I've witnessed people use the terms "feature", "epic" and "business requirement" without sharing an understanding what that even means. I've heard endless discussions about detailed acceptance criteria, and how to slice stories based on them. It was frustrating.

I claim there is an alternative. A simple way to avoid all these traps. First, you need to understand that there are two fundamental levels of user stories.

## Goals deliver value, but can't be implemented

In one of my courses, I ask questions like: "What can you do with a web shop?_"_  
The typical answers are: "Buy a  product", or "Order products".

What the participants talk about are goals. If we were a team developing a web shop, we might come up with the following user story:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/grafik-23.png)

Is this goal level story valuable to the user? Yes! It reflects the needs of the web shop customer.

Can you implement this goal directly? No! In order to implement a goal, you need to derive steps to reach it first. For the story "Buy Product", the steps might look like these:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/grafik.png)

Each step could be documented with the user story template: "As a web shop customer, I want to enter the address so that the product is shipped to me."

Can you implement this step level story directly? Yes! As soon as you have clarified the acceptance criteria. But is it valuable for the user? Without the other steps, no.

Value only emerges when the goal has been reached. Each step represents progress towards the goal. But independently, the step has no value. Does it make sense to use the story template for it then?

## A radically simple approach

The stories at the goal level are coarse grained. They can be used for long-term planning, without wasting effort on details:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/grafik-1.png)

You can often realize good user stories at the goal level independently of each other. And they deliver value. They are **I**ndependent, **N**egotiated, and **V**aluable. But they are not **S**mall, easily **E**stimable and **T**estable. Because you cannot define acceptance criteria for them without talking about steps.

The stories at the step level are **N**egotiated, **E**stimable, **S**mall, and **T**estable. However, they are not **I**ndependent and do not provide **V**alue alone. 

How do you combine the two kinds of stories into one simple approach? Here's my proposal. 

The team picks a goal, say "Buy product". The team then reflects: "What is the simplest way to reach the goal? And how can we reduce architectural risks early?"

Let's assume that the team sees the greatest risk in the communication with PayPal, because they've never implemented an interface to PayPal before. 

So what does a simple way to get to the "Buy product" goal look like? The team puts goal level story, step level stories and acceptance criteria as stickie notes below each other:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/grafik-2.png)

Here's what the acceptance criteria say (green stickies). There is only one fixed product that can be ordered. No search, no choice. The user interface is basic, and only allows users to pay with PayPal. 

These are the first steps that the developers implement. Once the developers have implemented a step, they demonstrate it to company internal stakeholders. At latest when a goal is reached, the team involves users. Getting feedback and deriving insights for further iterations is crucial. 

In later iterations, the team adds and changes stories. Examples include: more products, a search capability, and new payment methods. Or the team picks another story as a goal. Whatever is most valuable and makes sense at a given point in time. 

## Summary

You focus on a few goals to look further ahead. But you only discuss the acceptance criteria of the steps that you will implement in a few days. You implement the steps and gather feedback. You use the feedback to inform what you will develop in the future.

That way, everybody has a clear idea of what happens in development. You avoid wasteful discussions. And you keep backlog management to a minimum.

I've followed this approach many times. When everybody involved is on board, it works great. It makes development a joy. 

And that's it.  

Sources:

[1] Ron Jeffries 3Cs: [https://ronjeffries.com/articles/019-01ff/3cs-revisited/](https://ronjeffries.com/articles/019-01ff/3cs-revisited/)

[2] Bill Wake on INVEST criteria: [https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

_To [get the basics of agile software development right](https://skl.sh/2Cq497P), visit my online course. If you want to keep up with what I'm doing or drop me a note, follow me on [dev.to](https://dev.to/bertilmuth), [LinkedIn](https://www.linkedin.com/in/bertilmuth/) or [Twitter](https://twitter.com/BertilMuth). Or visit my [GitHub project](https://github.com/bertilmuth/requirementsascode)._


