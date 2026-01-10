---
title: 8 React Projects to Build in 2023
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-01-05T00:22:40.000Z'
originalURL: https://freecodecamp.org/news/react-projects-to-improve-your-skills
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/8-react-projects.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: null
seo_desc: "If you want to be good at React, building projects is one of the best ways\
  \ to do it. \nI have put together eight different projects that will not only show\
  \ you what's possible to make with React, but give you some inspiration on what\
  \ apps to make. \nAd..."
---

If you want to be good at React, building projects is one of the best ways to do it. 

I have put together eight different projects that will not only show you what's possible to make with React, but give you some inspiration on what apps to make. 

Additionally, I will give you all the tools that you need to effectively build out each project in the list. 

Let's get started!

## Todo App

If you want to get started building projects, there's no better starting place than a simple todo app.

A todo application will feature basic CRUD functionality, meaning that you can create, read, update and delete todos. Todos can be replaced with whatever type of content that you want. In fact, many applications we use on a daily basis could arguably be considered glorified todo apps. 

The benefit of building a todo app is that the entire app can be made in a short period of time. If you can build a todo app without any tutorial to guide you, it is a good test to see your proficiency with React. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-03-at-12.37.07-PM.png)
_TodoMVC todo app_

Todo apps are a great project to begin with because you do not need any third-party libraries to build them. You can make your todo app as complex as you like, which will help you become confident with concepts that you want to learn. Want to add authentication or a database to your app? Feel free to do so! You can truly make it as simple or complex as you like.

### Stack To Use

* Barebones React app
* Core React features (State, Context, and so on.)
* That's it!

## Personal Blog

A step up from the basic todo app is a blog website. 

If you would like to write in **Markdown**, which is a popular style of writing and formatting text, your blog will likely consist of a number of Markdown (.md) files. 

If you want the content to be included locally within the project to make it a bit more difficult, you could try fetching it from an external source like a CMS (content management system) such as Sanity or Contentful. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-03-at-1.11.07-PM.png)
_Next Blog Starter Kit (https://next-blog-starter.vercel.app/)_

In either case, this blog is going to consist of static pages so you can use any static site generator that you like. 

A good framework choice for this blog could be **Next.js** or **Gatsby**. Both are ideal to make text-driven websites like blogs because they are server-rendered frameworks and give you better SEO. This is compared to a traditional client-rendered React app (one made with Create React App, for example). 

Our stack will consist of one of these React frameworks plus a transformer to convert our markdown content into HTML when our site is built. A good choice to transform our markdown content is the `remark` npm package. 

If you want to make an even more impressive blog, with dynamic content, then you can consider using **MDX**. MDX is very similar to plain markdown, but it also allows you to include your own custom React components within the markdown. 

To use MDX, you would use a package like `next-mdx-remote` if you're using Next.js. The plain `mdx-js/mdx` package also works great.

### Stack To Use

* Next.js/Gatsby
* Markdown or MDX (`remark` or `mdx-js/mdx`)
* CMS (Contentful or Sanity)

Just a quick note: for each of these projects, I won't be talking about styling. I personally prefer using plain CSS in the form of TailwindCSS. You can head to Tailwind's website to see how to easily set that up for whatever React framework you're using.

## E-commerce App

The next step up from our blog project is an e-commerce app. 

It has a lot of similar features to our blog, including the fact that most of the content is going to be largely static and unchanging. 

Once again, the data can be sourced locally or fetched from a CMS at build time. What's different about an e-commerce app is that it allows us to venture into working with a server of some sort. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-15.png)
_Next.js E-commerce App_

If you want your customers to purchase an item through Stripe, for example, you might want to set up a **webhook** that will receive an event from Stripe when your customer has purchased a particular item. This is essential for managing things like your product inventory. 

To very easily write server-side code, you could use an API route so that you don't have to set up a complete Node.js project. This function would process different events that take place upon checkout or after checkout. 

Additionally, if you don't want to have to touch any server-side code, you can avoid the `stripe` npm package entirely and just use **Stripe checkout** or a **Stripe payment link**. 

Going forward, every project that we're going to touch on will involve a server of some sort. Most every application you use has a backend and a frontend. React will always be the frontend of our application but be aware that for any of these projects, you can very easily set up a server for your application to handle things like talking with a database when you have a framework like Next.js. 

Next.js includes a special type of page called an **API route**, which allows you to do server-side things such as authentication, webhooks, reading and writing to a database, and much more. Additionally, we'll touch on some solutions like Firebase that don't require you to make a backend at all!

### Stack To Use

* Next.js
* Stripe (using API Routes for webhooks)
* CMS (Contentful or Sanity to store products)

## News/Community App (Reddit Clone)

A Reddit clone that is centered around sharing links or very simple posts is a good step up from our todo app. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-3e6d6becfc.gif)
_Reddit clone, built with React_

We are still creating, updating, and deleting data, but this time it's going to be saved in a database. We might allow users to add different types of content, like a video or a link or a short post. We can use Firebase for our project to get started, which will give us the **Firestore database**. 

Our Firestore database will consist of a simple collection that will save all of the individual posts that a user has made. We can further develop it by allowing other users to add comments and likes to the posts. 

An even more developed app would include authentication. Fortunately, **Firebase Auth** makes it very easy. We can also add likes to individual comments and replies to comments for our comment threads. 

We could use any React framework for this. A good choice would be one using a **Vite** template. For our individual posts, we would need dynamic routes to fetch individual posts based off of their id. A good choice for that would be React Router.

### Stack To Use

* React (bootstrapped with Vite)
* React Router (install `react-router-dom`)
* Firestore database (from Firebase)
* Firebase Auth

## Chat App (Discord Clone)

To add to our Reddit app, we could make it into something like Discord by displaying messages in realtime. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-bd75470d3f.gif)
_Discord clone, built with React_

If we change the posts into threads, we now have a chat app where it's an ongoing conversation. 

Like the Reddit clone, users can still add any type of media that they like. A good touch would be adding link previews so when a user shares a link, such as a YouTube video, other users can get a little card that displays what is actually linked to with an image before the user clicks on it. There's a library called `react-tiny-link` that allows you to do that.

We can still use Firebase for this project. This is a good use case for the Firebase realtime database so that we don't need to refresh or reload the page to see new messages. 

Additionally, we can add different roles to our users in Discord. In the real Discord app, there are moderators with greater controls over the other users. One example feature would be to add a ban feature to remove a user from a given channel or community.

### Stack To Use

* React (bootstrapped with Vite)
* React Router (install `react-router-dom`)
* `react-tiny-link`
* Firebase realtime database
* Firebase Auth

## Messenger App (WhatsApp Clone)

An offshoot of this type of realtime app would be a messenger-style app like that of WhatsApp.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-4e59d05ac0.gif)
_WhatsApp clone, made with React_

This app would be a little bit more limited in that conversations are usually done with one person, although they don't have to be. Instead of talking in channels you will have different options to talk with one or another person at a time. 

A good touch would be to add notifications when someone messages you. This is another app example that would require realtime data functionality from your database. Firebase is always a good option for that. 

If Firebase gets boring, you could try Supabase which is a very competitive alternative also with realtime database features, but which is backed by Postgres instead of Firestore.

### Stack To Use

* React (bootstrapped with Vite)
* React Router (install `react-router-dom`)
* Supabase

## Social Media App (Twitter Clone)

What if instead of having an app where one person talks directly with another person in a very confined space, you want the opposite, where anyone can interact with anyone! 

A great example of this type of app would be Twitter.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/twitter-gif.gif)
_Twitter clone, made with React_

Twitter is an app that requires a feed as well as a trending page in a user's feed. The user will be able to see all of the posts from the people that they follow. But on the trending page, they will see all of the most popular posts across the entire website. 

To be able to figure out which posts are the most popular, you will add the ability to like (heart) a given post as well as re-share it, which allows a post to be added to or associated with another user. Finally, you will want to allow users to directly reply to other posts (like Twitter's "quote tweet" feature). 

And another fundamental feature that could be added to every app that we've covered up until this point is search. In our Twitter clone, users would likely want to be able to search for different users to follow as well as posts based on their content. 

One downside to Firebase is that it does not have the best tools for search and it's not easy to perform queries that are based on a certain keyword. This is one instance in which **Supabase** would be a superior alternative.

### Stack To Use

* React (bootstrapped with Vite)
* React Router (install `react-router-dom`)
* Supabase or Firebase

## Video Sharing App (YouTube/TikTok Clone)

The last fun project in this list is a video sharing app such as YouTube or TikTok. 

The two apps have very similar features, with YouTube primarily focusing on long form video content and Tiktok mainly consisting of super-short videos under a minute. 

Both platforms utilize an infinite scroll feature, whether you're scrolling through suggested videos or recommended videos. TikTok itself is arguably just one big infinite-scrolling feed.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-b958b9f166.gif)
_Tiktok clone, made with React_

What would be hardest to implement about both these platforms is the algorithm. You could go very far on building an app that just relies on users following other users and having a homepage with the most popular videos. Your users would first be suggested videos from the people that they follow and then the popular videos on the site. 

The most essential feature for both TikTok and YouTube is streaming video. To allow users to upload their own content you need a service that includes an upload API. Some good choices in this area are **Cloudflare Stream**, Video.js, or Mux. 

All of these tools provide you with a video player as well as an API, which would handle uploading videos that could then be posted to the site. 

I would personally build this app using my own server and database. I would probably choose **Prisma** as the ORM (object-relational mapped) to interact with the database which would be a **MySQL** database managed by Planetscale.

### Stack To Use

* Next.js (with API Routes for interacting with database)
* The `next-auth` package (to add Google Auth, among other auth providers)
* Cloudflare stream or Video.js (as our video player and to host our videos)
* Prisma (as our ORM)
* MySQL (managed by Planetscale)

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

