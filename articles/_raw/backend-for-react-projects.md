---
title: What Backend Should You Use for React?
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-22T21:04:58.000Z'
originalURL: https://freecodecamp.org/news/backend-for-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/backend-for-react.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: React
  slug: react
seo_title: null
seo_desc: "What backend should you choose for the React projects you are building?\
  \ \nThere are so many different options to pick from, how do you know whether the\
  \ backend you choose is the right one? \nIn this guide, you'll learn how to pick\
  \ the appropriate backe..."
---

What backend should you choose for the React projects you are building? 

There are so many different options to pick from, how do you know whether the backend you choose is the right one? 

In this guide, you'll learn how to pick the appropriate backend for the type of React application you're making in the simplest and least expensive way possible. 

Let's dive in!

## Does My App Need a Backend?

As React developers, building our project largely focuses on what the user sees, which is known as the **frontend**. 

In every React project, we manage data on the client through state and user interactions. However, many apps are not possible without data that comes from the backend.

The **backend** takes care of getting or updating data in our application and it is hidden away from the user. 

Most backends consists of two parts:

1. A place to store our data (often a database)
2. A method for retrieving the data (often an API) 

But here's the good news: based off of the type of application you're making, you may not need either. 

## Stage 1: No Backend

If you are building an app where your data changes very infrequently, you probably don't need a database or an API.

For example, if you are building a personal blog that you update a few times a week at best and that is built as a static site using Next.js or Gatsby, you don't need a backend.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/react-and-nextjs.jpg)
_Static sites built with Gatsby or Next.js may not need a backend_

Instead, you could simply write your blog posts as markdown files, which are stored and tracked (using Git) within a project folder.

If you have an e-commerce application where the product data rarely changes, you could store all of app data in JSON files that you simply import and use within your React application.

If you are fine updating files manually and re-deploying your project, that may be all that you need.

What type of backend you choose depends upon some key features of your data you need to ask yourself:

* Does my data change often? 
* Am I fine managing my data as local files and folders? 
* Can my app data or files be tracked in version control (Git)?
* Are other people going to be updating the data? 
* Will my application need authentication?

Depending on your answers to these questions, you might be able to get away with using static files as your data source. 

Going this route will ultimately save a lot of money on database and hosting costs, since static sites can be hosted on a free tier of many hosting providers.

## Stage 2: Content Management Systems 

If you're need more features than static files alone can provide, content management systems are the next step

**Content management systems** or (CMS) give us tools to more easily manage our content. They often give us dedicated applications with built-in editors to more easily view, update, and structure our data.

What we specifically need for our React application is a headless CMS.

A **headless CMS** does not have a visible interface, since React will be serve as the user interface for our app.

A CMS is ideal for your application if you simply have too much data to manage as separate files or want other potentially non-technical users to edit or add content to your app.

Some of the simplest CMSs range from Excel-like sheets like Google Sheets and Airtable, to note-taking apps like Notion.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/alt-cms-examples.jpg)
_You can use tools like Google Sheet, Airtable and Notion to function as your app's CMS_

The benefit of these solutions is that they are easy to get started with, have a generous free tier, and have their own built-in API to fetch data.

There are other CMSs that offer developer-friendly features such as image and media asset management as well as more expansive API features. 

Some of the more developer-friendly CMSs include:

* Sanity
* GraphCMS
* Contentful

![Image](https://www.freecodecamp.org/news/content/images/2024/08/sanity-graph-cms-contentful.jpg)
_Sanity, GraphCMS, and Contentful are more powerful, dev-friendly CMSs_

And if you are looking for content management systems that are the most powerful, with features like built-in authentication and updating data from your React client, check out:

* Strapi
* KeystoneJS

![Image](https://www.freecodecamp.org/news/content/images/2024/08/strapi-keystonejs.jpg)
_Want a CMS that is basically a complete backend? Check out Strapi or KeystoneJS_

## Stage 3: Backend as a Service

The limitation with content management systems is that they are great for managing and accessing data.

However, when you need to add more complex, custom features such as updating data from your React client, authenticating users, protecting content, and real-time data, a standard CMS falls short.

Managing a database and building a complete API to interact with that database is a daunting challenge, especially if you've only worked on the frontend.

If this is the case for you, it may be worth looking into a **backend as a service** (BaaS). It will give you much of the power of a custom-built backend without the domain-specific knowledge.

The most popular BaaS is **Firebase**, and for good reason. It gives you a ton of features that you simply could not build on your own, including dozens of authentication strategies, real-time NoSQL databases, cloud storage, machine learning tools, and much more.

There are many other BaaSs that give you the productivity of Firebase, with little to no code required:

* Supabase
* Hasura
* Appwrite

![Image](https://www.freecodecamp.org/news/content/images/2024/08/firebase-supabase-hasura.jpg)
_Firebase, Supabase, and Hasura are all great backends to use if you aren't comfortable building your own_

**Caveat**: The speed of development for all of the services can help you build and ship your applications faster. But be aware that all of them have their own associated costs, such as the cloud storage you use and number of database operations you perform (reads/writes).

## Stage 4: Build Your Own Backend

Before considering this stage, you should look intently at whether you could potentially use options 1 through 3.

This is the most advanced option to choose as a React developer because it requires the most knowledge, time, and coding skills.

With that being said, it is also the most customizable, considering that you can build exactly what you need to power your app.

Entire books have been written on just parts of building your own backend, but here is what I would recommend as someone who has built many production applications using a custom backend.

I recommend using a **SQL database** such as Postgres or MySQL. Services such as Heroku, Render.com, and PlanetScale offer hosted databases (often with free daily backups) at great prices.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/heroku-render-planetscale.jpg)
_Heroku, Render.com and PlanetScale are some of the best places for your database to live_

Unless you are very comfortable and confident writing raw SQL statements and know all of the security precautions to take to avoid nasty things like SQL injection, use an **object relational mapper** (an ORM) to create a database schema and interact with it.

I highly recommend using **Prisma** as your ORM. It generates all the code required to perform every kind of operation against your database as well as types for each.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-22-at-1.31.43-PM.png)
_Use Prisma as your ORM_

While you can certainly build a custom Node backend using your favorite Node library or framework (Express, Fastify, Nest.js), I would advise you to start small and use a feature like Next.js' API routes.

Tools like Next API routes allow you to build your API fast without the need to run and manage your server code in a separate repository.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

