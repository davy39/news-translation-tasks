---
title: How to Architect a Full-Stack Application from Start to Finish
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2022-10-04T17:49:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-full-stack-application-from-start-to-finish
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/jeremy-thomas-FO7bKvgETgQ-unsplash.jpg
tags:
- name: full stack
  slug: full-stack
- name: software architecture
  slug: software-architecture
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: "Software architecture is a massive topic. That said, I think I can give\
  \ you a simple method you can use to approach the architecture of a full-stack application.\
  \ \nIn particular, I want to talk about the order in which you should think about\
  \ and build..."
---

Software architecture is a massive topic. That said, I think I can give you a simple method you can use to approach the architecture of a full-stack application. 

In particular, I want to talk about the _order_ in which you should think about and build out the pieces of a typical web application.

My advice is that **for each feature** you should:

1. Design the front-end
2. Build the front-end
3. Build the persistence layer (back-end database and data models)
4. Build the API (back-end application)

_The best way is a front -> back -> middle approach._

## Why Start with the Front-End?

Assuming you're working with a good product team (or maybe you're a team of one so you _are_ the product team) the most important thing is the end-user experience. As a result, it makes the most sense to start on the front-end. 

Only by designing and building the front-end will you learn what kinds of requirements you'll have for the back-end of your application.

The user of front-end code is the customer. The user of back-end code is front-end code.

## How Do you Build a Front-End without a Back-End to Connect to?

This is the beauty of starting with the front-end. Start by mocking up all of the data that fills in your UI. For example, instead of writing code like this:

```js
const resp = await fetch(userUrl)
const user = await resp.json()
```

You would simply write:

```js
const user = {
    id: 1,
    username: "bobbyjoe",
    email: "bobbyjoe@example.com",
    profilePictureUrl: "https://fakewebsite.com/fakeimageurl.jpeg"
}
```

Then you would write all the rest of the front-end code like you normally would. By the time you're done, you'll know _exactly_ what kind of data you'll need your back-end to store and serve. 

And by the time you do get around to building the back-end, you can just swap out those mock JSON objects for `fetch` requests.

## Create the Data Model and Database Schema

Okay, so you've built out the front-end for your new feature, and you've mocked all the data that you've decided will need to be stored on the back-end. Now it's time to decide how you'll model that data inside your database.

I like to go straight from the front-end to the database. This is because the way you store data in the database is more important to get right than the way you serve the data from your API – well, at least if the consumer of your API is your own team (or you).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/well.jpeg)
_Obi Wan writing APIs for himself_

[Changing database schemas is _hard_](https://wagslane.dev/posts/keep-your-data-raw-at-rest/). It's much easier to slap a `/v2` endpoint on your back-end than to rewrite your persistence layer. 

For that reason, thinking about how you're going to store your data, and giving priority to that design, will generally lead to less headache down the road.

Typically, once you have the front-end built you have all the information you need to design a solid database schema.

For example, maybe you know you need:

* To store users, each with an email and profile picture
* To allow users to join, create, and leave organizations

With that in mind, and assuming you're using a relational SQL database like Postgres, you can probably start with something like:

* A `users` table with `id`, `created_at`, `email`, and  `profile_picture_url` fields
* A `organizations` table with `id`, `created_at`, and `name` fields
* A `users_organizations` table with `id`, `user_id`, `organization_id`, and `role` fields

Users go in the `users` table, organizations go in the `organizations` table, and the `users_organizations` table is a joining table to keep track of which users are a part of which organizations and what their role is. For example, they might be an `admin` or a `member`. 

If you're unfamiliar with all this SQL terminology, you can check out my [Learn SQL course](https://boot.dev/learn/learn-sql) on [Boot.dev](https://boot.dev/).

## Lastly, Build the Back-end Application

Now that you know which data your front-end needs, and how you can best model it in your database, you final task is to glue it all together with a back-end API. 

Start with the simplest API you can.

Don't build complex joining capabilities to start. Don't build crazy pagination or filtering features if you don't need them. You can always add new endpoints and parameters later in order to fulfill performance needs as they arise. I'm a big fan of [optimizing for simplicity first](https://wagslane.dev/posts/optimize-for-simplicit-first/).

Anyhow, that's not to say you won't need anything more complex than a few CRUD endpoints – you might. If you do, at least you have all the information in front of you in order to make a well-informed decision. 

Don't build more than what the front-end requires, and try to use the simple data models you created in the database.

With all that in mind, expect to go back and forth on a few things. Don't feel bad if you missed a feature on the front-end and need to go back and add it. Or maybe you overlooked how slow a certain view in your app would load if you store the data in a certain way in your database. This can be an iterative process, and it should be.

## One Final Note: Don't Do Waterfall

I want to double stress the fact that you should be doing this on a _per-feature_ basis. I'm not advocating that you plan an entire application up front. You should still be practicing iterative product development.

Good luck, and if you need help learning back-end development feel free to check out what I'm building over on [Boot.dev](https://boot.dev/)!

