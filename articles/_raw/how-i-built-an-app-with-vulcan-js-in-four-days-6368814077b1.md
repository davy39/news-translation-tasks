---
title: How I built an app with Vulcan.js in four days
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:27:58.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nnLl46hdkKTPVF8pI0Ifhg.png
tags:
- name: Vulcanjs
  slug: vulcanjs
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eric Burel

  How unambitious I was, a few months ago, when I published “Vulcan: 15 days for an
  app”! 15 days is 3 weeks of work. If you include conception time, that’s a month
  of delay. What if we could reduce it to a week? What if we could develop ...'
---

By Eric Burel

How unambitious I was, a few months ago, when I published “[Vulcan: 15 days for an app](https://hackernoon.com/the-vulcan-js-challenge-15-days-for-an-app-e3735d1e3d4c)”! 15 days is 3 weeks of work. If you include conception time, that’s a month of delay. What if we could reduce it to a _week_? What if we could develop production-ready applications in a matter of _days_? Here is how we are achieving this goal.

### Day 0: Some context

#### Stop calling yourself a Startup just because you produce sloppy code faster than others

I run a development and consulting company named LBKE. We take a deep interest in technologies that help produce high quality applications in a very limited amount of time. Think React Native+Expo for mobile, or Meteor for web applications.

Through the years, the expected quality of Minimum Valuable Products (MVPs) has surged. People are fed up with low quality prototypes sold as “products”.

Now, they want their software without bugs (no way!), they want a good UX (how picky they are!), they want tools that truly answer their needs (ugh!). And of course, they don’t want to pay more for that.

![Image](https://cdn-media-1.freecodecamp.org/images/UiFG9dkquYx6dslh8XvrjMd0rwC0KRFAx89v)

#### Toward the 4 days app

For the entrepreneur, designing and building such a Minimum _Loveable_ Product is a lot of work. But money is tight, and time is money, so you have to be smart about how you spend it.

**Our goal: being able to produce a SaaS application in 4 days.** We do not mean a throwaway app that won’t bear further development. We believe that well-designed technologies should allow both long-run development and very fast development: scaling up, and scaling _down_. For most projects, there is no need for prototyping technologies. Except if you build spaceships, but you don’t, do you?

Also, we do not like relying on 3rd party services/softwares that pop websites in a few clicks. If your product is truly innovative you likely feel _awfully_ limited by such services.

So, how do we achieve this miracle without using a magic wand? Let’s discover it through a real life example, GestiResto, a web application that helps restaurant owners to manage their recipes. _Side note: I live in France, we don’t joke about food here, so I really took this project to heart._

### Day 1: Picking our spaceship

#### Meet Vulcan.js, aka Meteor-on-steroids

Meteor is a famous full-stack JavaScript framework. From its very beginning, it has always emphasized productivity and developer experience. It pioneered many awesome features and patterns, like isomorphic development (reuse the same code server side and client side).

[Vulcan.js](http://vulcanjs.org/) is basically the good elements of Meteor, plus the good elements of the JavaScript ecosystem, in a single framework. It relies on the latest technologies: React for the frontend, and Apollo (GraphQL) for client/server communication.

![Image](https://cdn-media-1.freecodecamp.org/images/8dCr7Zq2kiRzH1kC6GLpl-NRTiXZxyXODWin)
_Join us on Slack!_

As a bonus, it includes a lot of packages and examples for the most common features (sending newsletters, adding a forum, etc.). Vulcan is the direct grandchild of the famous Meteor app/framework Telescope, it has been created by [Sacha Greif](https://www.freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1/undefined). It thus benefits from years of experience despite its modernity.

If you want to know more about Vulcan and how it helps cut development time, you can checkout [my previous article](https://medium.com/dailyjs/write-less-code-ship-more-apps-how-vulcan-js-makes-me-an-efficient-developer-71c829c76417) in DailyJS.

So, Vulcan.js is definitely a solid candidate to meet our self-imposed 4 day deadline!

#### A user management system out-of-the-box

One of the most beloved features of Vulcan is its account system, which it inherits from Meteor. It includes signup/signin/logout, permission management, enrollment/forgotten password workflows (+ programmatic email sending), and a nice user interface. Oh, and also it’s quite easy to add 3rd party auth with services such as [Google Oauth](https://medium.com/@teaganatwater/setting-up-google-oauth-in-vulcanjs-aa53c6010d21).

![Image](https://cdn-media-1.freecodecamp.org/images/RRHcKcYJ2xMkH6BfSW6jszCO85Se7R7kXDlU)
_The day 1 application. The authentication system is fully functional at this point. Material design can be obtained with the [vulcan:more-material-ui](https://github.com/ErikDakoda/vulcan-material-ui" rel="noopener" target="_blank" title="">vulcan:material-ui</a> and <a href="https://github.com/lbke/vulcan-more-material-ui" rel="noopener" target="_blank" title=") packages._

Accounts management is really something you DON’T want to think about in the early stages of your app life-cycle. How many hours have been lost setting up Passport.js! The amount of paid authentication services such as Auth0 shows that this problem is not yet solved, so it’s really a very nice feature.

So, our first day has been well spent. We now have a complete user management system including database, server , UI, and back-office, and we set up a nice Material UI layout with the remaining time.

![Image](https://cdn-media-1.freecodecamp.org/images/Ia55kHRNdUxfIhphz29YA9T-mUFNVu9AGqV7)

### Day 2: Hosting

#### Hosting on AWS with Meteor Up

Why hosting on day 2 already? Because life taught us that it is a very bad idea to test your app in production the last day. In an agile fashion, a feature is only done when validated in a real life context. So, we can’t consider the application to be set up if we did not run it in a production environment.

Meteor Up is a wonderful tool to automatically deploy Meteor apps (so Vulcan apps too) on a distant server. It handles everything, from containerization of the app with Docker to SSL certificate generation with Let’s Encrypt. Setup is easy, deployment is a one line command. There are barely any drawbacks to it.

I picked AWS for the hosting. It has the big advantage of proposing free services for 12 months. I must admit that I had hard times setting up my first EC2 instance. However there are many tutorials on the web and it’s worth the initial trouble. Also, I am currently writing [a package to enable daily backup of the MongoDB database on AWS S3](https://github.com/lbke/vulcan-mongo-backup) to make your data safe.

#### A staging application on Zeit’s Now + Mongolab

Sooner or later, you will need to test that your app works in production, without actually sending it to production. That’s what we call a staging environment. You can use AWS too, but let’s try a free solution instead to cut costs.

![Image](https://cdn-media-1.freecodecamp.org/images/duoWiDFwqKTIjBmUyBr31D2xZQFHst7jqdxG)
_Cheers to all companies that provide free services and contribute to open source._

Zeit’s Now service is well suited for this usage. It offers free hosting. You can use mLab for the database, as it provides a free sandbox environment too. To be honest I have nothing much to say here, because the set up is as easy as ABC, and fully [documented here](http://docs.vulcanjs.org/deployment.html#Meteor-Now). Not even a bug. _What’s my purpose as a developer if there are no bugs???_

Okay, so, at the end of day 2, our app is in production and we have an intermediate demonstration environment. Nice! That’s cool, because **less time for generic features is more time for valuable features.**

### Day 3: Business logic

#### An app is a bunch of forms and lists

Now, let’s get down to business. Most components of an application can be separated in 3 large categories: List, Form, and Details. This model apply to a LOT of websites.

![Image](https://cdn-media-1.freecodecamp.org/images/KIACKwgfrO6zLnELdGZCLsIAJKvKSFVBxFuH)

See Medium: the home page contains a List of articles. This page is a “Details” page of the article you are reading. At the bottom, you’ll find a List of comments with a comment Form. Even the “applause” button on the left (which I invite you to click thoroughly), is a simplistic Form like component.

Good news: Vulcan includes a whole lot of helpers to facilitate the creation of List, Form and Details components. It includes nice GraphQL resolvers and React HOCs. You barely need to write your own. There are even a few React components that work out-of-the-box. The most advanced of them is the SmartForm, which automatically generates a customizable creation/edition form for any collection.

I won’t list all the features Vulcan.js has to offer, but basically you can safely trust it to make your development process _really_ fast.

#### Creating a recipe (or proposing an application or publishing an article or…)

In GestiResto, the 2 mains features are creating and listing recipes. The recipe creation form must display statistics. The details are confidential, so here is a screenshot of an equivalent form developed for [Awesome Vulcan](https://www.awesome-vulcan.com).

But that makes no difference, because here is the point: Vulcan can auto-generate forms out-of-the-box for whatever type of data you can imagine, whether it’s a recipe or a helicopter. I mean, the JSON representation of a helicopter.

![Image](https://cdn-media-1.freecodecamp.org/images/Bbs1OzlDpIAL0mzR8G0PMsve7ipAJG-EB3wj)
_This form has been auto-generated using Vulcan core SmartForm component. The “Links” input is a custom React component tailored for our specific needs._

The recipe list is even simpler. We focused on building a nice `RecipeItem` that allows users to quickly preview the recipe information, as well as triggering some common actions (exporting, deleting…). Of course, it includes a text based search input, for free.

![Image](https://cdn-media-1.freecodecamp.org/images/muf7M03u5G1aYr6wk3DgJYSeQVi3rqj9PevF)
_No, I am never ever going to give you access to the “Secret Recipe”. Except, maybe, if you clap for this article._

![Image](https://cdn-media-1.freecodecamp.org/images/8cGzC3JcfzKn6jCsiNDOAuM4scQ1DvVwbqD6)

### Day 4: Deliver!

Since we did most of the valuable parts of the job on Day 3, we are left one last day to cleanup and improve the application. Now we can implement the love-to-have features: a component that automatically computes the final price of your recipe, a button that generates a nice PDF export, and a homepage that makes the difference.

![Image](https://cdn-media-1.freecodecamp.org/images/7XlmaXGrLXotB4gP4mlKeSEonK2QXiRIMsx8)
_Look how happy is our chef! That’s because his app is built on 100% organic-open-source technologies._

Eventually, we’re on Day 5. The client has just tested the app delivered yesterday evening, and says to you: “I’ve tested the app, it’s nice! I think of adding feature X to page Y, how long does it takes to add component Z in your opinion?…”. **And then you know you did a good job!**

### Want to build your own app in 4 days?

Take a look at our open source application [Awesome Vulcan](https://www.awesome-vulcan.com). It provides a reusable basis for professional apps with a Material UI look. It also demonstrates the use of a few packages we implemented.

**I hope it will help you in your journey toward the 4 days application!**

<a href="https://twitter.com/LBKE_FR" target="_blank"><img src="https://cdn-media-1.freecodecamp.org/images/rxG0NpyqOMowC2nFVuSOHsg4pjJFkMs7w5bn"/></a>

I am the co-founder of the French company Lebrun Burel Knowledge Engineering (LBKE) — [https://www.lebrun-burel.com](https://www.lebrun-burel.com)

_Always happy to talk about code, machine learning, innovation and entrepreneurship!_

