---
title: What's New In The 2019 State of JavaScript Survey
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T00:08:16.000Z'
originalURL: https://freecodecamp.org/news/whats-new-in-the-2019-state-of-javascript-survey
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f02740569d1a4ca4055.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Sacha Greif

  We just opened the 2019 State of JavaScript survey. Go take it if you haven''t done
  so already!

  It''s now the fourth time we''re doing this survey, and each time we take a deep
  look at our big YAML file containing all our questions to see...'
---

By Sacha Greif

We just opened the [2019 State of JavaScript survey](http://survey.stateofjs.com/?source=fcc). [Go take it](http://survey.stateofjs.com/?source=fcc) if you haven't done so already!

It's now the fourth time we're doing this survey, and each time we take a deep look at our big YAML file containing all our questions to see what stays and what goes. So in case you're curious, here's a quick overview of everything new in this year's survey.

## Language & Patterns

The biggest structural change is that we now have a new "Language" section that asks about JavaScript as a language itself. Do you use destructuring? What about arrow functions? Have you looked at Maps and Sets yet? And are you more of a functional programmer or an object-oriented coder?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-27-at-8.47.13.png)

We also have a whole section all about browser APIs so we can see how popular each of them is. 

The goal is to get an idea not just of what libraries people are using, but also what their actual code looks like. 

## New Libraries: Svelte, Cypress, and more

Speaking of libraries, we also have a couple new entrants. 

First off is [Svelte](https://svelte.dev/), which has been making big waves in the community all throughout 2019. It was also our #1 "other" answer in the front-end section last year, so it only made sense to include it. 

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-26-at-16.06.57.png)

In the back-end section, we added [Nuxt](https://nuxtjs.org/) and [Gatsby](https://www.gatsbyjs.org/). They're not "traditional" back-end frameworks like Express or Koa, but they've gained so much popularity recently that not adding them felt like an oversight. 

In the testing section, we've added [Cypress](https://www.cypress.io/) and [Puppeteer](https://github.com/puppeteer/puppeteer), and in the mobile & desktop section [NW.js](https://nwjs.io/) and [Expo](https://expo.io/). 

## Resources Section

Just like we did for this year's [State of CSS](https://2019.stateofcss.com/) survey, we also added a Resources section to find out more about which blogs, resources, and podcasts are the most popular. 

## A Custom Survey Front-End

Finally, on the technical side of things the huge change this year is that we're using our own homegrown survey platform for the first time instead of relying on [Typeform](https://typeform.com/). 

This is something we had talked about for a while, but we didn't consider it seriously until we realized Typeform had changed their pricing, and that their largest plan was now capped at 10,000 responses per month! Typeform wasn't interested in accommodating us, so with the end of the year looming ever closer, I got to work to hack a survey app together. 

Thankfully I had a secret weapon in my pocket: [Vulcan.js](http://vulcanjs.org/), a full-stack JavaScript framework that's perfect for quickly putting web apps together; and I was able to build the entire app (you can [find its code here](https://github.com/StateOfJS/StateOfJS-Vulcan)) in about five days by leveraging Vulcan's form-generation module. 

Moving this fast did have a few drawbacks. We've had our share of little bugs, but nothing major so far. Also, we now require you to create an account before filling out a survey. As much as we'd like to support anonymous users, we didn't have time to implement proper safeguards against data tampering, so requiring accounts seemed like the safest choice. 

I do think this was the right choice though. As we import data from previous years into our new survey app, we'll be able to give you access to that data so you can see how your responses have evolved over time (provided you've used the same email); and also make it easier for others to access our data to make their own data visualizations. 

All that being said, the best way to experience all this new stuff is to go and see for yourself! So [take the survey](http://survey.stateofjs.com/?source=fcc), and help us figure out this year's latest JavaScript trends. 

