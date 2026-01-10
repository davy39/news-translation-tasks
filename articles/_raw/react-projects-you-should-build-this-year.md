---
title: 7 React Projects You Should Build in 2021
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-22T17:04:07.000Z'
originalURL: https://freecodecamp.org/news/react-projects-you-should-build-this-year
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/7-react-projects-for-2021-2.png
tags:
- name: JavaScript
  slug: javascript
- name: portfolio
  slug: portfolio
- name: React
  slug: react
- name: side project
  slug: side-project
seo_title: null
seo_desc: 'React is a JavaScript library that is ideal for creating impressive apps.
  There are countless projects that you can make with React, but here are seven that
  are on my list to build in 2021.

  Why have I selected these seven projects in particular? I pi...'
---

React is a JavaScript library that is ideal for creating impressive apps. There are countless projects that you can make with React, but here are seven that are on my list to build in 2021.

_Why have I selected these seven projects in particular?_ I picked them because they build off of one another. They requ. ire you to know similar, essential concepts like authentication, working with an API and database, using a React router for adding pages to your app, and playing media like audio or video. 

Plus, many applications can be (and often are) integrated into one another. Social media apps can include chat apps, music or video apps can include e-commerce apps, and so on.

In other words, **building any of these projects** will give you the skills and knowledge required to build the rest of the apps on the list, including your own personal projects.

Along with each project, I have provided several real-world examples which you can use to find inspiration, plus some ideas about what tools I would possibly use to build each app.

## 1. Realtime Chat App

**Real-world examples**: Slack, Messenger, Discord, Crisp Chat

Virtually all of use some kind of realtime chat app, whether it's a mobile application like WhatsApp or Viber or a productivity tool like Slack or Discord. It could also be part of a chat widget within a website where customers can directly talk with the site owners. 

All chat apps allow users to send messages to others in realtime, to react to messages, and they show when users are online or offline. 

### How to build a realtime chat app: 

* Build your project with create-react-app or Next.js. 
* Use a service like Firebase or GraphQL subscriptions to create and get messages in realtime to users.
* Add reactions to message with emoji using the npm package emoji-mart
* Deploy to the web using Firebase Tools

## 2. Social Media App

**Real-world examples**: Facebook, Twitter, Instagram

The app you're likely most familiar with is a social media application. In many ways it's similar to a chat app, but expanded to a larger community of users. 

These users can interact with each other in different ways: they can follow one another to receive their posts, add media like images and video to share with others, and enable users to interact with posts such as liking or commenting on them.

### How to build a social media app: 

* Build your frontend with create-react-app, and backend using a Node API
* Use a database like Postgres or MongoDB, along with an ORM like Prisma (Postgres) or Mongoose (MongoDB)
* Use social authentication with Google, Facebook or Twitter, using Passport or a simpler service like Auth0
* Deploy the backend to Heroku, frontend to Netlify

## 3. E-Commerce App

**Real-world examples:** Shopify, Etsy, Dev.to Storefront

Storefronts where we can buy digital or physical products online are everywhere. E-commerce apps add the ability for users to add and remove items from a shopping cart, view their cart, and checkout using a credit card, as well as other payment options like Google Pay and Apple Pay. 

If you're looking for inspiration, checkout out some simpler storefronts like a Shopify storefront, rather than looking at a massive retailer like Amazon or Walmart.

### How to build an e-commerce app: 

* Create the app with create-react-app or Next.js
* Add the `stripe` NPM package, plus `use-shopping-cart` to easily handle payments directly with Stripe Checkout
* Build a Node API to handle creating sessions with Stripe
* Deploy the backend to Heroku, frontend to Netlify (or deploy both on Heroku)

## 4. Video Sharing App

**Real-world examples:** YouTube, TikTok, Snapchat

A video sharing app is probably the most broad category, as video is used across so many different apps and in many different ways. 

You have video sharing apps like YouTube, which allow you to search any browser and look for any video that you could imagine that users have created. Also, tik tok and Snapchat give us the ability to watch videos from other users that are recorded in a much shorter, more accessible format, and are more oriented around interactions like likes and views.

### How to build a video sharing app: 

* Create the app with create-react-app, and create the backend with Node/Express
* Use Cloudinary for image and video uploads to the Cloudinary API
* Use a database like Postgres or MongoDB, along with an ORM like Prisma (Postgres) or Mongoose (MongoDB)
* Deploy the backend to Heroku, frontend to Netlify (or deploy both on Heroku)

## 5. Blogging / Portfolio App

**Real-world examples:** Medium, Dev.to, HashNode

This app example is perhaps the most practical. The most immediately practical choice for you to build a blogging or portfolio app is something that showcases your skills. It allows you to show off what you can do as a developer, while also allowing you to include posts and content that reflect what you know. 

Making these applications with tools like Gatsby or Nextjs (which are both React frameworks) is now easier than ever.

### How to build a blogging or portfolio app: 

* Create the app with Gatsby or Next.js
* Use markdown for blog posts with a special markdown transformer plugin such as `remark`
* Deploy the site to Netlify or Vercel

## 6. Forum App

**Real-world examples:** Reddit, StackOverflow, freeCodeCamp Forum

A forum application is where we go when we want to get help, and as programmers we visit forums like Reddit and Stack Overflow to get our coding questions answered. 

Forums also combine many elements of chat and social media apps through posts, comments, and reactions. A forum is more of a more organized version of a social media app where users can more easily find answers to questions they're looking for. 

### How to build a forum app: 

* Build your frontend with create-react-app, and backend using a Node API
* Use a database like Postgres or MongoDB, along with an ORM like Prisma (Postgres) or Mongoose (MongoDB)
* Use social authentication with Google, Facebook or Twitter, using Passport or a simpler service like Auth0
* Deploy the backend to Heroku, frontend to Netlify

## 7. Music Streaming App

**Real-world examples:** Spotify, Soundcloud, Pandora

Just as React applications are perfect for serving video content, they're also great for streaming media like music. 

Music apps have a similar structure to video sharing apps and may or may not allow users to upload their own music. They do allow users to listen to music, like songs, comment on them, and perhaps even purchase music. 

In this way, a streaming music app can combine elements of a video sharing app as well as an e-commerce app.

### How to build a music streaming app: 

* Create the app with create-react-app, and create the backend with Node/Express
* Use Cloudinary for image and video uploads to the Cloudinary API
* Use a database like Postgres or MongoDB, along with an ORM like Prisma (Postgres) or Mongoose (MongoDB)
* Deploy the backend to Heroku, frontend to Netlify (or deploy both on Heroku)

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

