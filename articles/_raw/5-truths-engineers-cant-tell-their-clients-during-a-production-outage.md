---
title: 5 Truths Engineers Can't Tell Their Clients During a Production Outage
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2020-10-06T05:01:00.000Z'
originalURL: https://freecodecamp.org/news/5-truths-engineers-cant-tell-their-clients-during-a-production-outage
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9850740569d1a4ca1957.jpg
tags:
- name: Devops
  slug: devops
- name: Freelancing
  slug: freelancing
- name: software development
  slug: software-development
seo_title: null
seo_desc: "My birthday present this year was a production outage. \nSome people go\
  \ for cake and ice cream. Others plan a fun outing. I got an outage instead of an\
  \ outing. And it was anything but fun.\nIn the midst of it, my colleague and I vacillated\
  \ between tria..."
---

My birthday present this year was a production outage. 

Some people go for cake and ice cream. Others plan a fun outing. I got an outage instead of an outing. And it was anything but fun.

In the midst of it, my colleague and I vacillated between triaging the issue and fuming about how difficult it was to find its source. 

And as I came up for air to connect with my patient and insightful wife, I shared with her how inadequate I felt, and consulted with her in how to communicate effectively with the affected client.

They needed to know we were going to fix it. They needed that fix to be fast. They needed to know the fix would last. 

We tactfully crafted emails and had reassuring phone calls with them. We updated them often and gave them the right amount of transparency and technical insight.

But here are the truths that we couldn't tell them.

## 1. We were not prepared for this

As is the case with many engineers on many projects, we inherited this application. We were left with little documentation and poor tools for debugging production. And there are too many moving parts to count. 

It's like we're taking a fire extinguisher into a forest fire.

Our time and your financial budget didn't allow for extensive preparations for a production outage, and now we're facing the heat. In more ways than one, we were not prepared for this.

## 2. The cause of the outage could be one of 20 things

The cause? Might be the server. Might be the code. Might be the database or a third-party package. Might be food poisoning. Might be our fault. Might be yours.

The solution? Might just need a restart. Might need an index on that database table. Might need to update that package or configuration setting. Might need Pepto-Bismol. Might need to burn the whole thing and start again.

## 3. We have absolutely no idea how long it's going to take to fix

A restart of the server could take ten minutes. A rebuild of the server could take anywhere from ten hours to ten days. We might be able to track down the bug in a few minutes, or we may never discover what actually happened. 

It all depends on identifying the cause, and we've already established that could be one of 20 (or more) things.

We've also established that we weren't prepared for this. Might as well leave us alone and trust that we care enough to fix the problem as fast as possible. 

In the meantime, we'd suggest you considering reworking your definition of "fast".

## 4. We need the problem to manifest again before we can figure out the cause

Because we have so little in the way of tools and documentation, we're basically flying blind. Thankfully, we've installed some monitoring tools to help us out. 

The catch is that those tools can only monitor things going forward. So we need this intermittent issue to show up again before we can actually diagnose the problem.

We could certainly try this in a staging or test environment, and we did, but it's not succumbing to the same problems that production is experiencing. And, actually, it's an entirely different setup than production. 

Our only option at this point is to take down production again. Tell your team to hold on tight while we pound production, not to try to fix it, but just to reproduce the problem so our tools can capture what's happening.

## 5. You really should be paying us more for this level of stress

We're not sleeping. Barely eating. Our families haven't seen us for days. We spend all our time in front of a computer except for short bursts in front of the refrigerator, in the bathroom, or in the corner in the fetal position.

These stress levels warrant double pay, at least. But we realize now is not the time to negotiate a new contract. We're all in survival mode, and apparently, production's health is more important than our own. 

And that's the reason why you should pay us (a lot) more during an emergency outage.

## Concluding Thoughts

These are truths that engineers really can't communicate to their clients during the crisis of a production outage. 

If you've thought some of these things, just know that many of us have thought them. If you resonate with these sentiments, many of us have felt this way. Production outages cause immense amounts of pressure and stress. 

If you're wondering about the actual circumstances of my birthday outage, the issue was an intermittently unexpected response from a third-party email service. It caused an application error, but that error wasn't caught. 

Instead, the request was tried again. And again. And then a few hundred (thousand?) more times until it brought the server to its knees. We'd restart the server and within another hour it was down again.

It took days to track down the actual cause, as our monitoring and debugging tools weren't honed. We saw spiked CPU and RAM usage but no clear link to rogue processes. We couldn't reproduce the problem in any environment but production. And the offending code was abstract and utilized libraries we weren't familiar with.

Next time, we'll be more prepared. We've installed tools to give us profiling capability and stack tracing for requests in production. We're going to be more cautious in implementing third-party tools and ensure our application can gracefully handle their failure. 

I, personally, plan to negotiate a higher rate (likely 1.5 or 2 times my normal rate) for outages that make me drop all my other responsibilities.

Our preparation should also include a commitment to staying calm and silencing doubt. Panicking causes us to chase symptoms instead of focusing in on the source. Doubt tries to convince us we can't figure out the problem and never will be able to. 

Operating out of a place of calm and confidence will bring that needed reassurance to our clients, and help us effectively navigate production outages. And have more fun on our birthdays.

