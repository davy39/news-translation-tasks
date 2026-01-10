---
title: How To Organize Express Controllers For Large Codebases
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T22:46:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-organize-express-controllers-for-large-codebases-2d8284bbf817
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rZynfm9hux013-uclDjBfA.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Alexandre Levacher

  Three years ago, I started developing an Express.js API for a company. I wondered
  what could be the best controllers architecture to stay organized as the codebase
  grows.

  Influenced by Sails or Rails and by my research, I came t...'
---

By Alexandre Levacher

Three years ago, I started developing an Express.js API for a company. I wondered what could be the best controllers architecture to stay organized as the codebase grows.

Influenced by Sails or Rails and by my research, I came to create my own system. I did not want to overload my project using a complete framework like Sails, but rather pick lighter dependencies when needed.

So I created an organization system for the app’s controllers which I paired with a homemade loader**.** Since then, I improved both of them thanks to the experience I gained by implementing it on other projects.

Today, I’m confident enough with this method to share it, as the results are convincing.

From what I know, it’s used by a few large companies. It simplifies onboarding new developers as it makes the codebase easier to read.

✅ Here’s how to set up a clean controllers architecture.

### **The Structure**

If you don’t anticipate the growth of your app, you’ll quickly have an unorganized codebase. I designed the organization method to have wide compatibility, which means that someday you’ll not be locked into a kind of use case you can’t solve with this method.

#### Setup your file tree

* Group routes in controllers
* Create folders for each controller
* Create a routing file in each controller which describes the **path** of each route, the **method to call,** its optionally associated **middleware,** and the **restriction level.**
* Create a file for each controller's actions which contains the **method to execute** and the **middlewares**.
* Create a **spec file** for testing

Let’s see how it looks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4b15NCcOkq9zjfQcS8bEdg.png)
_? Example of controllers structure_

**Don’t be afraid to create a lot of files**. It does not slow down the development, and it makes your codebase neat and airy. ✨

### **Load your routes**

To make things work following the structure defined above, we need to use a simple loader I created: [Lumie](https://github.com/Alex-Levacher/Lumie). It will go through your controllers, read the definition files, and load your routes.

It’s a small package, you can check to code source on [GitHub](https://github.com/Alex-Levacher/Lumie).

#### Routing Files

They have been designed to be easy to read. The purpose is to be able to identify methods to update in development by having a quick look in your **.routing** files. In the following example, three routes will be created:

* [ PUT ] **/user**
* [ GET ] **/user**
* [ GET ] **/user/reset-password**

You are wondering why routes are prefixed with “**user**” although it’s not described in the routing definition. Lumie uses the name of the folder in which the routing file is to prefix routes.

Here, we are in `controllers/user/user.routing.js` . If the `user` folder has been in a subfolder `admin` for example, the routes would have been prefixed by `admin/user`.

Note that you can pass an optional `path` field to the routing definition so it will be used instead of the default one.

#### Actions & Middlewares

As you can see above, each routes configuration have an action method which is nothing more than the logic to execute when we call your API route. I recommend keeping in one file: **one action method** and **its optional associated middleware**.

#### Restrictions

For each routes configuration, you’ll choose the restriction level associated. The level value will be passed to the restriction function you’ll create to make Lumie work. See [how to initialize Lumie](https://github.com/Alex-Levacher/Lumie#%EF%B8%8F-configuration) with your own restriction function.

This should be just a function that returns a classic express middleware.

### Conclusion

I’ve been using this method for a while now. I like to have this kind of opinionated framework to follow when I develop. At the end of the day, it’s helping me to keep a nice codebase and not to take shortcuts like writing too much logic in one file or defining a route in an inappropriate file.

Thanks for reading. Tell me in the comments what you think about organizing controllers this way.

If you found this article helpful, drop some? ?

