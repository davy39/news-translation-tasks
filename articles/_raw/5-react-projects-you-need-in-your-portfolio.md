---
title: 5 React Projects You Need In Your Portfolio
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-01-27T03:26:45.000Z'
originalURL: https://freecodecamp.org/news/5-react-projects-you-need-in-your-portfolio
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/5-React-Projects.png
tags:
- name: portfolio
  slug: portfolio
- name: React
  slug: react
seo_title: null
seo_desc: 'You''ve put in the work and now you have a solid understanding of the React
  library.

  On top of that, you have a good grasp of JavaScript and are putting its most helpful
  features to use within your React code.

  You''ve made a great deal of progress... b...'
---

You've put in the work and now you have a solid understanding of the React library.

On top of that, you have a good grasp of JavaScript and are putting its most helpful features to use within your React code.

You've made a great deal of progress... but now what do you do?

How do you bridge the gap between knowing the fundamentals of React and becoming a professional developer?

Many developers run into this problem when they reach this intermediate stage of learning React or any other JavaScript library. They know most of the library itself as well as the JavaScript to use it effectively, but they don't know the next step to take.

## Why You Should Be Building Apps

After you've learned the basics of React, you need to get comfortable building apps with the skills you've gained. This practice lies at the core of being an effective React developer—knowing how to build apps on your own and utilizing the right tools in the React ecosystem to do so.

But what apps should you be building with React to level-up your ability as a developer?

In this article, we'll go through 5 different types of apps that you should consider building after the basic todo app. The great benefit of building apps is that, once deployed, they can be linked to your portfolio as a powerful, immediate way of showing employers your expertise.

For each type of app, I'll cover popular examples that you can use as inspiration, the tools I would recommend to build each feature, along with a short demo of such an app that I've personally made using React.

## How to Start Building Apps With React

Unlike learning React itself, where you can find dozens of articles to dive deeper into any related concept, the process of building an app is largely a self-directed activity without much guidance. 

If you're getting started building apps on your own, I would recommend searching for articles that teach you the basics of building an app and dive into the app source code that they provide. Even the process of reading code itself will make you a better developer.

If these examples look too daunting to build yourself, remember what you know as a React developer—to break applications down into composable components. Every application must be built piece-by-piece, component-by-component. Focus on building out one feature at a time. With practice, you'll get a better sense of how what tools you'll need for each feature as well as the common patterns behind building apps in general.

> Note: One misconception that I had when starting to build real applications like these was that I had to build an entire backend / API with Node or Python to get the functionality I needed. 

> You don't need to do so. Look into powerful serverless technologies like Firebase, AWS Amplify, or Hasura that give you a complete backend out of the box without the need to create and deploy one yourself. Invest in tools that make you more productive and save time.

## Build a Social Media App

If I had to recommend only one app for you to add to your portfolio, it would be a social media app. Twitter, Facebook, and Instagram are quite sophisticated, and include an ever-growing number of features to keep users engaged. On top of that, it's the kind of app you likely know best regarding how it should function.

There are a number of features common among almost all social media apps: 

* the ability for users to make posts with text and/or media files, 
* a live feed of those posts, 
* enabling other users to like and comment on posts, 
* as well as user authentication. 

And once you've got that down, you can add profiles for each of your users, where they can personalize their account as well as manage the users they're following.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/social-media-cropped-min.gif)

**App examples:** Instagram, Twitter, Snapchat, Reddit

**Technologies to utilize:**

* Create React App or Next.js to make a dynamic UI of posts, likes, and messages
* Firebase, AWS Amplify, or Hasura (using GraphQL with subscriptions) for real-time data
* Serverless functions like AWS Lambda or Firebase Functions for notifications
* Cloudinary or Firebase storage for uploading pictures or video

## Build an E-Commerce App

Pick a few of your favorite sites and I guarantee at least one of them has an e-commerce app embedded in it, even if it's just a small storefront. E-commerce apps are ubiquitous, and I bet that you'll be called upon to build one at some point in your career as a developer.

It is tempting to build an impressive, large-scale e-commerce platform like Amazon, but I would recommend working on something smaller and more focused. 

Instead of a marketplace that provides all things to all people, go with an industry that interests you. For example, if you like home goods, you might take a look at what Crate & Barrel or Williams-Sonoma have built for their sites.

Aside from products, e-commerce apps may provide a service to consumers. If it is a service that is provided locally, an interactive map could be added to the app to provide for the service provider and customer to know each others' location. Food delivery applications such as UberEats and Doordash, which require the location of the person ordering the food, come to mind.

Regardless of what's being sold, whether it's physical or virtual, every e-commerce app will consist of some storefront with the product or service details. If users can purchase multiple products at once, it should have a shopping cart where users can manage the products they want to buy. 

Finally, every e-commerce app needs a checkout process where users can either purchase their products anonymously or once they are authenticated.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/ecommerce-cropped-min.gif)

**Popular examples:** Airbnb, Uber, UberEats, Doordash, Etsy, Udemy

**Technologies to utilize:**

* Create React App or Gatsby for the storefront and displaying products
* Stripe with the package react-stripe-elements for handling payment processing
* Serverless function like Netlify / AWS Lambda to handle checkout process
* Algolia for lightning-fast product searching
* Snipcart for easily creating a cart and managing cart products

## Build an Entertainment App

This is the broadest of all of the categories. What do I mean by entertainment? An app that is focused around a certain kind of media. This could be movies, podcasts, or music to name a few. 

Some great examples of this, respectively, would be Netflix, Audible, and Soundcloud or Spotify. If you include art or design in this category, we could add sites like Behance or Dribbble to the list.

What's interesting about this category is that many entertainment apps border on social media apps. For example, an app like Tiktok, which features short, imaginative videos, is driven by high user engagement. Another app like YouTube is centered upon user interactions through likes, comments, and subscriptions.

Think about what type of media or entertainment most interests you and see if you can build a simple platform around it, where users can login and save the content that they like. After that, look into adding social elements that make it possible to add comments, like, and share content with other users on the platform.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/entertainment-cropped-min.gif)

**Popular examples:** YouTube, Netflix, Audible, Spotify, Tiktok

**Technologies to utilize:**

* Create React App, Next.js, or Gatsby to create the app UI
* npm package react-player for playing media
* Cloudinary or Firebase storage for media uploading
* Algolia for searching media by name (i.e. audio track, video, movie, etc.)

## Build a Messaging App

Messaging apps are huge. You likely have a free messaging service like WhatsApp or Viber on your phone, or one built into your social media platform like Facebook Messenger. Services like Intercom with instant messaging are also available as web apps so companies can provide immediate customer support to their users.

Any messaging app is going to consist of a conversation with two or more people where messages are sent in real-time. Similar to the social media app, I would recommend a service such as Firebase or Hasura that transports data via WebSockets for messages to be displayed immediately in the conversation.

The majority of messaging apps are on mobile devices or tablets. If this isn't your first app clone, this is a great chance to move beyond the web and build a mobile app with React Native. Better yet, you could build a web and mobile messaging app simultaneously with a package like React Native Web.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/messaging-cropped-min.gif)

**Popular examples:** WhatsApp, Viber, Discord, Messenger, Slack

**Technologies to utilize:**

* React Native or React Native Web to build as a mobile app or hybrid app (web + mobile)
* Firebase, AWS Amplify, or Hasura (using GraphQL subscriptions) to send messages in realtime
* Cloudinary or Firebase storage for sending messages with image or video content
* npm package emoji-mart for a slick Slack-like emoji picker for users to include in their messages

## Build a Productivity App

This probably the easiest type of app with which to begin, considering there are so many tutorials of basic productivity apps out there. When I speak of productivity apps, I'm referring to note-taking apps, apps for managing teams, and task lists. Generally speaking, anything that helps you accomplish a certain task or be more productive.

What's great about building a productivity app first is that it provides a good introduction to app building because of the relative simplicity of many of its features. 

You can start with something simple, such as a text editor to write formatted text with markdown easily and then expand upon it. Then add the ability to save text as individual files on your computer. After that, a feature to export that markdown as HTML to write formatted emails.

To start building a productivity app, ask what features an app could have to make your daily schedule easier and go from there.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/productivity-cropped-min.gif)

**Popular examples:** Todoist, Notion, Things, etc.

**Technologies to utilize:**

* Create React App for web or React Native for mobile
* npm package react-markdown to display markdown in your app UI
* npm package react-codemirror2 for writing code in your notes
* npm package react-draggable for re-ordering list content by clicking and dragging

Good luck with your app building journey and I'll see you in the next article.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

