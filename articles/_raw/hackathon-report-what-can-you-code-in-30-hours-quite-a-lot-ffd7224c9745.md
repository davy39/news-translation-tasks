---
title: 'Hackathon Report: What can you code in 30 hours? Quite a lot!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-25T23:06:33.000Z'
originalURL: https://freecodecamp.org/news/hackathon-report-what-can-you-code-in-30-hours-quite-a-lot-ffd7224c9745
coverImage: https://cdn-media-1.freecodecamp.org/images/1*42-G6mLr8857p66NkXV7wg.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ajay NS

  What can you build in 30 hours straight? As a group of second year college students
  with a growing portfolio of work, my team and I wanted to find out. So we signed
  up to a hackathon.

  It was a Financial Technology (or ‘Fintech’) hackathon ...'
---

By Ajay NS

What can you build in 30 hours straight? As a group of second year college students with a growing portfolio of work, my team and I wanted to find out. So we signed up to a hackathon.

It was a Financial Technology (or ‘Fintech’) hackathon organized by DCB Bank in the city of Mumbai. Although we were clueless about Fintech, we wanted to give it a try, in the hope of coming with an idea that solves a general problem.

The event was hosted in the beautiful and cozy co-working space by [91 Springboard](http://www.91springboard.com/). This was an environment I hadn’t been in before.

Basically, it rents out office space for startups, freelancers and such who don’t need a huge office, but just a workspace for their team members to collaborate. 91 Springboard takes care of providing fun colorful and snug workspaces, fast internet and **unlimited coffee**, while you work hassle-free. It was really a pleasure crashing here for the weekend.

![Image](https://cdn-media-1.freecodecamp.org/images/XnC9zo9Cymm0KlCNv2Mvst7-UGVWvzRVOjnQ)

### The Idea

> To put it simply, we wanted to build a specialized chatbot.

**Why?**

It’s predicted by 2020, a huge percent of business communication will be done through chatbots.

User experience (‘UX’) is rapidly changing. With messaging apps gaining popularity, users prefer to access everything under one app. They are also in favor of one-on-one communication.

Gone are the days of emails, it’s all about real-time chat now. With today’s technology, it’s possible to create a chat-bot which can learn by itself and automate most of the tasks, allowing mass communication on an individual level.

See [here for a list](https://medium.com/the-mission/11-best-uses-of-chatbots-right-now-1c27764b7e62) of some of the best uses of chatbots right now**.**

### **What exactly did we build?**

As we were at a Fintech hackathon, we thought about a bot that carries out all the functions that can be carried out by the bank’s app and more — through chat.

Once logged in, you can ask the bot for your balance, your last few transactions, and also to carry out actions such as fund transfers. It leverages the required APIs provided by the bank for the same purposes.

![Image](https://cdn-media-1.freecodecamp.org/images/KNck0NbniE8cdF86k9Eg0wA4iwEJcxGX4Nba)

Above is a screenshot of some of our UX inspiration. This UX had a combination of natural language and multiple options, which were directly provided as links and buttons. The flow of answering users queries, suggesting the next steps and also allowing actions to be carried out, was planned.

### The Project

![Image](https://cdn-media-1.freecodecamp.org/images/HWWqgqRzXJr4PPZ6la9OYmIPj21v5ePVgS01)
_The final product_

The tech stack we chose was Ruby on Rails. We picked this because my teammates were very familiar with it, and I was focusing on wrapping up APIs and UI primarily. But this stack was totally new to me, as I’ve always worked on JavaScript or Python stacks. I wrote about my learning journey [here](https://hackernoon.com/ruby-on-rails-and-full-stack-javascript-ecadf631707).

It uses a basic PostgreSQL database to store user messages, and uses ActionCable for live data-streaming as required. The whole site (along with the chat as a widget) is built over the Materialize framework.

One of the key features we planned to use was a customized AI, rather than going for something like IBM Watson or api.ai. This was wrapped into an API using Flask.

![Image](https://cdn-media-1.freecodecamp.org/images/c9JStBkursr9SEEMdQubeJongaAtBpeRQBTo)
_Intent mapping_

Initially, when the bot has little to no training data, human assistance is required to give responses and also classify the intent of each user query for the bot to learn. Once it accumulates data, it can automate the whole process, giving appropriate responses.

A few of the scripts used for the AI are available [here](https://github.com/dhanushkamath/DCBHackathonScripts).

### The Hackathon

We managed four hours of sleep over a span of more than 30 hours, while pushing over 50,000 lines of code to production.

But it wasn’t as bad as it sounds! The place itself has this motivating vibe, and there are mentors helping you out. There were breaks in between to chill with other teams and getting to know other kick-ass developers.

While my team mates focused on the Machine Learning part and the actual chat application on Rails, I worked on the UI for the service. This included an admin panel as well as the chat widget. Quite a lot of time was spent wrapping up the AI code into RESTful APIs and fixing bugs in the main code as well.

In the end, what we had was a basic alpha version of the app we set out to build.

![Image](https://cdn-media-1.freecodecamp.org/images/2AXEaHn82ZUk7811EC-oWnUzGoytyFvGShP6)

### The Experience

> For a start, this was the most productive 30 hours of my life.

With constant bursts of motivation (and caffeine) driving me, there was no time for sitting around or lazing. Loads of fun and talented people to interact with as well, because I was one of the youngest there.

A few of the things I learned here included:

* Decoupled application architecture
* Building an app from scratch and then pushing into deployment in the shortest time possible
* Live code collaboration
* and of course, a little bit of Fintech!

Check out the project we worked on here: [chaturbots.com](http://chaturbots.com/). This is offered as a service now, so contact us for getting a custom bot built.

Hope you enjoyed this article and found it to be a good read! You can check out all my projects on [Github](http://github.com/ajayns/) and reach out to me on [Twitte](https://twitter.com/ajayns08)r!

