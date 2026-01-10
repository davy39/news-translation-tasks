---
title: Why I built the simplest async universal React Redux boilerplate I could
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T23:46:38.000Z'
originalURL: https://freecodecamp.org/news/why-i-built-the-simplest-async-universal-react-redux-boilerplate-i-could-1b5ef6206d3d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VeM-5lsAtrrJ4jXH96h5kg.png
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By William Woodhead

  I set myself a task last week.

  I was checking out some “Get Started” Universal React Redux Boilerplates and found
  that a lot of them are really complex. They include heaps of dependencies, and have
  functionality that can take week...'
---

By William Woodhead

I set myself a task last week.

I was checking out some “Get Started” Universal [React](https://reactjs.org/) [Redux](https://redux.js.org/) Boilerplates and found that a lot of them are really complex. They include heaps of dependencies, and have functionality that can take weeks to unpick.

**In general, boilerplates serve two functions for me:**

1. Get started quicker, since the app is already scaffolded
2. Learn about how to scaffold an app

I am much more interested in the second item. As a developer, I like to understand how things fit together, how things work **under the hood**.

Therefore I set myself the task:

> Create the simplest possible Async Universal React Redux boilerplate.

Sounds great, but what does it all mean?

**Just want to see the code?** Check out this [GitHub Repo](https://github.com/william-woodhead/simple-universal-react-redux).

### What is async universal React Redux boilerplate?

Let’s unpick each word, one by one.

#### Universal

Essentially, Universal describes an app that is both server-side rendered, and has dynamic client-side routing.

**Why is this important?** Server-side rendering is important for SEO and for rich links and metadata — like when you post a weblink in Twitter or Slack.

Client-side routing offers your users a fluid experience on your website, because the browser doesn’t have to reload when the user navigates between pages.

#### Async

Async means that we want to fetch data from external APIs before we render the page. We want to render the page server-side with data that is an asynchronous request away.

**Why is this important?** This is really important for apps where data or content is stored separately from the website code. Let’s say we have data in a database, or we are requesting data from the Twitter API. We want to get our hands on this data before we render the page.

#### React

React is the functional rendering library that has been developed by the team at Facebook to work on both the server-side and the client-side. React gives us the functionality we need to render a page server-side, but still initialize the app client-side.

#### Redux

Redux is a state management package that has been developed to be easy to use on both server-side and client-side. Redux give us the functionality we need to pass state between the server and the client.

#### Boilerplate

Defined by the [Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/english/boilerplate) as:

> Text that can be copied and used … in computer programs, with only very small changes.

### Why do you need Universal apps?

A lot of websites just render on the client-side. Google Search can now index pages that render on the client-side, so why do we need to go through the pain of creating Universal apps?

#### Rich links and metadata

The main reason is for rich links and metadata. When you post a page into Twitter or LinkedIn, they scrape the raw HTML of the page returned from the server to find metadata.

If your app is rendered on the client-side, this metadata will not be available to the scrapers, because no JavaScript is run.

This can be a huge issue. Imagine the difference between just your weblink being rendered as text and your weblink being rendered with rich images and metadata. Here’s an example:

**Slack post of [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=boilerplate&utm_campaign=awareness) without metadata**

![Image](https://cdn-media-1.freecodecamp.org/images/KNIboYOszuVHPmRe-6S6WJ030391L31ffecy)

**Slack post of [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=boilerplate&utm_campaign=awareness) with metadata — spot the difference**

![Image](https://cdn-media-1.freecodecamp.org/images/cNfmlcRQDHXFiE-i4AkJEOrXTj0i8HPwwT-B)

**Note:** Check out [howdoesitlookonsocial.com](http://howdoesitlookonsocial.com) to see how your metadata is rendered on social sites.

### The simplest boilerplate I could make

Creating universal apps is really complex. There isn’t a standardized way of approaching it yet. A lot of the existing boilerplates are hideously complex.

That’s why I tried to make the simplest boilerplate possible that works on both Mac and Windows.

There is nothing superfluous in the source code. The webpage couldn’t be simpler. It looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/BsPNbL90GiJ4iuQFnZRLUPPsn2YFa9adSYmC)

I want developers to be able to unpick all the different functions and packages used in it, hack around with it, test different parts, and ultimately build great universal apps on top of it.

So here is the [GitHub repo link](https://github.com/William-Woodhead/simple-universal-react-redux).

Check it out — clone it, install it, run it. See what you think. I would love any feedback. And if you like it, make sure you star it and share it!

_If you liked this story, please ? and please share with others. Also please check out my company p[ilcro.com.](https://www.pilcro.com/?utm_source=medium&utm_medium=boilerplate&utm_campaign=awareness) Pilcro is the brand management app for G-Suite._

![Image](https://cdn-media-1.freecodecamp.org/images/CsWVmNZ2bnvwrdu3apMKDKvdhxOCY1awxFvU)

