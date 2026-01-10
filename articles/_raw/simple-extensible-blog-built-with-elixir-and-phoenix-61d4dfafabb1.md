---
title: How to build a simple, extensible blog with Elixir and Phoenix
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-28T18:06:58.000Z'
originalURL: https://freecodecamp.org/news/simple-extensible-blog-built-with-elixir-and-phoenix-61d4dfafabb1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*qT3nBMIsmRiQa4nc
tags:
- name: Elixir
  slug: elixir
- name: Phoenix framework
  slug: phoenix
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Raman Sah

  In this post, we’ll discuss how to build a boilerplate Phoenix web app with user
  authentication and an admin panel, along with image upload in Elixir.

  TodoMVC has become a de facto tool to compare various JavaScript-based MV* frameworks....'
---

By Raman Sah

In this post, we’ll discuss how to build a boilerplate Phoenix web app with user authentication and an admin panel, along with image upload in Elixir.

[TodoMVC](http://todomvc.com/) has become a de facto tool to compare various JavaScript-based MV* frameworks. Along the same lines, I feel that a blog application can be a tiebreaker in choosing a new backend or API framework.

So let’s get started and build one in Phoenix. We’ll follow the default setup, that is Phoenix hooked up with Ecto running on PostgreSQL.

Here are the final screens to give you an idea of what the app will look like at the end.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x59piiG96eAfObns-aPzvQ.png)

The landing page will show all the published blogs in a card layout. A card can be clicked to view that particular post.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxWIdSAc-p9elJI3x2yQKw.png)

We will have a dashboard that will show the statistics in brief. Access to this page requires admin user login.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwuFgK253CAjphO0IVu8Ow.png)

There will be a separate section that has an overview of all the posts. Here you can publish / modify / delete posts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fkzXp5iJjFJPzyk-bu1NFg.png)

This is the post editor layout featuring a markdown editor along with a file picker for the featured image.

> _Note: The full working code is hosted on [GitHub](https://github.com/ramansah/cms). There are numerous files in the project which cannot be shared in a single blog. So I have explained the specific ones which I assume are critical._

Let’s keep the project’s name as CMS for now. So we’ll start with creating a new project with `mix phx.new cms`. Run `mix deps.get` to install dependencies.

Generate a migration file for users and posts, respectively.

```
# User migration file
```

```
mix phx.gen.schema Auth.User users name:string email:string password_hash:string is_admin:boolean
```

```
# Posts migration file
```

```
mix phx.gen.schema Content.Post posts title:string body:text published:boolean cover:string user_id:integer slug:string
```

Two tables have to be created in the database which represent users and posts. I’ve kept it rather simple, keeping only the required fields and expanding when the need arises.

Subsequently, we can define changesets and additional methods in the user and post schema as well.

**user.ex**

**post.ex**

```
@derive {Phoenix.Param, key: :slug}
```

Since we want the posts to have a readable and SEO friendly URL structure, we inform route helpers to reference `slug` instead of `id` in the URL namespace.

The routes are described here:

Resources which are specific to the admin section are clubbed together and assigned a pipeline which forces authentication.

Meanwhile, global routes are treated with passive authentication. User details are fetched if a session is present but the pages are still accessible. Login and home pages belong here.

Executing `mix phx.routes` gives me this output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*C0G1-utBGFbtv8332dWFfA.png)

The view is divided into three logical sections:

1. Navigation bar
2. Sidebar
3. Main Content

While the navigation bar is always visible, the sidebar appears only if an admin user is logged in. Browsing content will be inside the admin context. The links in the sidebar will grow as and when the app evolves.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UkNS-kHZ4Dpo9lgMpzqSdA.png)

The Admin.Post controller follows the typical CRUD architecture and includes an action to toggle the published state of a given post.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwuFgK253CAjphO0IVu8Ow.png)

A lot of controls reside in the index page of admin’s post section. Here, posts can be deleted, published and modified.

**templates/admin/post/index.html.eex**

To keep the template uncluttered, we can define convenience view helpers like formatting time etc. separately.

**views/admin/post_view.ex**

Arc along with arc_ecto provides out of the box file upload capabilities. Since a post features a cover image, we have to define an arc configuration in our app.

Each post in our blog requires two versions of cover images — original which is visible inside specific post view and a thumb version with a smaller footprint to populate the cards. For now, let’s go with 250x250 resolution for the thumb version.

Coming back to the app’s landing page, it will house the cards for all the published posts. And each post will be accessible through the slug formed.

```
controllers/page_controller.ex
```

This project explores Phoenix — how a Phoenix app is structured and how to dismantle a Phoenix-based project. I hope you’ve learned something and enjoyed it!

The full working app is on Github : [https://github.com/ramansah/](https://github.com/ramansah/votex)cms. Feel free to clone ? and do clap if you find this blog useful ?

