---
title: How a hackathon is kind of like a real-life triathlon — but with more caffeine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T21:26:47.000Z'
originalURL: https://freecodecamp.org/news/how-a-hackathon-is-kind-of-like-real-life-triathalon-but-with-more-caffeine-50226ded1708
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tXS2niLfdGKZxdCvgnAjCA.png
tags:
- name: Life lessons
  slug: life-lessons
- name: slack
  slug: slack
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Alec Jones

  I’m 15, and I recently signed up for the Global Hackathon by Product Hunt. It runs
  for the month of November and there are 7,950 people participating from around the
  world ?. Crazy!

  From what I’ve seen in my 3 years as a student program...'
---

By Alec Jones

I’m 15, and I recently signed up for the [Global Hackathon](https://www.producthunt.com/hackathon) by Product Hunt. It runs for the month of November and there are 7,950 people participating from around the world ?. Crazy!

From what I’ve seen in my 3 years as a student programmer, developers love hackathons. They’re an opportunity for product makers meet up, drink Red Bulls, and stay up all night coding.

It’s kind of like a triathlon for developers, who often go for days with minimal sleep. It’s a hard-fought race to the finish (if you even manage to finish). And it’s a chance to compete under pressure.

### The three stages of a hackathon

Shortly after I registered for the month-long event, I realized that competing in this hackathon is similar to entering a real triathlon. Just like in a regular triathlon, there are 3 stages, which all require a lot of skill and endurance:

* The first stage is about coming up with the idea (the swim).
* The second stage is about turning the idea into something real (the cycle).
* The third and final stage telling everyone how helpful your product is and convincing them to try it (the run).

### Compressing all of these stages into a short moment in time

I’ve already built something that started out as an idea. It’s called Christopher Bot, a Facebook Messenger bot that helps high school students remember their homework, and it’s been written about [here](http://www.bbc.com/news/technology-39013950) and [here](https://www.theglobeandmail.com/news/british-columbia/bc-teen-creates-facebook-chatbot-to-help-students-stay-organized/article34278474/) and [here](http://www.metronews.ca/news/canada/2017/03/12/facebook-tool-created-by-b-c-teen-to-plan-homework-gains-popularity-overseas.html). It also got acquired! But, you can read about that [in my other Medium story here](https://medium.freecodecamp.org/the-ups-and-downs-of-building-and-marketing-a-chat-bot-when-youre-14-8a072830b43c).

Before choosing to work on Christopher Bot, I had lots of ideas for products to build. My dad and I talked about how some ideas catch on, and some don’t. The ideas that catch on always seem to solve a problem.

If enough people have a problem and your product solves it well, and you can find a way to share your solution with those people, it has a good chance of succeeding.

I followed that advice when I chose to work on a homework bot. Students often forget what homework they’re assigned during the day, so I needed to build something that would stop people from forgetting their assignments. Christopher Bot was born.

I’m using that same advice in the Product Hunt hackathon.

I needed to find a problem. And in that problem, there would be a solution.

But where to begin?

### Swimming for an idea

In the Product Hunt competition, there are a bunch of existing platforms you can build for: Google Assistant, Slack, Blockchain, Artificial Intelligence and Augmented Reality. You don’t have to build for any of them, but some cool prizes are awarded within these specific categories.

Seeing these options actually made things easier for me. It narrowed down the list of possible problems to solve. All I had to do was find a problem in one of these categories.

I’m not yet familiar with blockchain technology… or AR or AI. So that made things even easier. Google Assistant is cool and could be interesting to develop for, but it turns out I’ve spent a fair bit of time using Slack.

I think Slack is pretty awesome and I’ve tried out a bunch of Slack apps. So I decided to build something in the Slack category.

At first, I thought about building something that would remind you about all your mentions in public channels — because once you click on a channel with a notification for you, the notification disappears and you have to respond right away or you might forget that you were mentioned.

But then came some bad news. My dad (who likes to talk these things through with me) experiences this notification problem, but he showed me that Slack already has a built-in solution.

You can mark important messages where you’re mentioned as “unread”, and you can even tell Slack bot to remind you about an important message after a specific period of time.

So it was back to the drawing board for me. ☹️

During the same conversation where I found out that bit of disappointing news, I also noticed that **there’s no easy way to DM multiple people at the same time**.

Was this even a real problem? It turns out (based on some quick Google searches) that people have asked about how to do this in Slack — and even in products that compete with Slack.

If you’re part of a big team and you want to ask multiple people the same question, but you don’t want everyone in a channel (or in a group DM) to see their responses, there’s no easy way to do it in Slack.

I checked hundreds of existing apps in the Slack app directory — and couldn’t find anything to solve this particular problem. But I found that the most popular slack apps are the ones that solved other problems for teams… another reminder that I needed to work on solving a real problem.

For example, getting everyone on your team to vote on something (like where to go for lunch) is a pain. So the people behind Simplepoll decided to solve that problem by enabling someone on a Slack team to easily create a quick poll, ask their team to vote, collect the responses, and count up the votes.

They found a problem common to many teams and built a nice simple solution. Which is exactly what I wanted to do.

My hackathon project is an idea that’s based on a real problem for Slack teams…

The problem: You want to ask multiple people the same question but you don’t want the entire team — or even a portion of the team — to see the question OR the responses. You can’t use a group DM or public channel… because everyone will see what you wrote, and see the responses (unless people are instructed to respond privately in a DM). It’s not very ideal.

Another less than ideal solution is to go down the list of team members and create a new DM, one after the other, by pasting the same message for each person. It’s so tedious that I think most people wouldn’t even bother.

So my entry for this hackathon is called [**MultiDM**](https://www.producthunt.com/upcoming/multidm), a very simple Slack app that gives you and your team the ability to DM multiple people at the same time — using a single message, sent from any channel.

(Swim stage finished!)

Let’s say you think of an important HR-related question you want to ask 5 people on your team. And let’s say you’re already in the #general channel.

From the channel, you would just type “_/multidm @john @jane @henry @samantha @jake I need your birthdate for HR — can you please let me know ASAP?_”

Nobody will see the message you typed into #general. Instead, each of the 5 team members will receive a normal-looking DM from you — which they can respond to normally, and you’ll receive their answers without anyone else seeing the answers or even knowing that you asked multiple people the same question.

So that’s it. Next up is the long, difficult cycling stage. ??

If you’re interested, you can sign up to be one of the first to try [MultiDM](https://www.producthunt.com/upcoming/multidm).

Thanks for reading about my process for choosing a product idea. Most ideas aren’t successful because they don’t solve a real problem. People use products that fix a problem.

So for your next product (or hackathon idea), first find a problem, and then go build something to solve it!

