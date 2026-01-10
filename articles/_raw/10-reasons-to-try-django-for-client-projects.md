---
title: What is Python's Django used for? 5 Key Reasons I Use the Django Framework
  for Client Projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-08T17:51:04.000Z'
originalURL: https://freecodecamp.org/news/10-reasons-to-try-django-for-client-projects
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95fc740569d1a4ca0f26.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: "By Gwendolyn Faraday\nIf you had told me a few years ago that I would pick\
  \ Python's Django as my number one framework of choice for client projects, I would\
  \ not have believed you. \nBack then, I preferred lightweight frameworks like Flask\
  \ and Express f..."
---

By Gwendolyn Faraday

If you had told me a few years ago that I would pick Python's Django as my **number one framework of choice for client projects**, I would not have believed you. 

Back then, I preferred lightweight frameworks like Flask and Express for their flexibility and the extra control they afforded me.

What changed?

Part of it was my getting hired to work in Django! The other part was getting tired of setting up the same features over and over again from scratch for different companies – ORMs for the database, migrations, authentication systems, emails, and so on. It's time-consuming to get all these features set up and working properly. 

Well, Django gives me all of this with minimal configuration out of the box. Yes, it is awesome.

With Django, I can build applications much more quickly without sacrificing features. The developer experience is also quite good – and not just because Python is awesome. It's also because there are good debugging tools, logging is already set up, and there's a server that automatically restarts with file changes.

I could go on and on about all the good features in Django, but here I will just list my top 5. I hope this will pique your interest so that you want to try out Django for your own companies and projects.

## Django's Admin Interface

I'm listing this first because it is my number one favorite feature that comes baked into Django. 

So many clients need to have a view into their application so they can manage users, data, or content on pages. Usually, the client will not be technical or have time enough to dive into the actual code and make changes. 

So what is the best way to handle this situation?

Django's admin interface is a great solution. Without any extra configuration, you get a powerful, fully-customizable, login-protected admin area that displays all of your application's data.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screen-Shot-2021-01-31-at-9.43.58-PM.png)
_Image from [Stack Overflow](https://stackoverflow.com/questions/37572343/django-count-todays-logged-in-users)_

The data in this admin area includes any tables you want to list there as well as all tables from third-party packages like auth libraries.

## Django has Built-in Auth

Some kind of authentication is needed in almost every application so the market has many tools, services, and libraries to use. Because there are so many options, it can be difficult to choose one. Even if you use a managed service, hooking it up is not always easy. 

Well, Django comes with built-in authentication via sessions. What if you want to use tokens? Just install the Django REST Framework (DRF) library which comes with token auth.

I personally like to use DRF with the additional [dj-rest-auth](https://github.com/jazzband/dj-rest-auth) library for extra features like expiring tokens. Either way, all of these pieces work seamlessly together in the Django ecosystem and require very little configuration.

_[Here is an example of a Django repo](https://github.com/freecodeschoolindy/student-management-system) where I have token auth (and GitHub auth) setup in Django with Django REST Framework._

Any authentication system you use in a Django project will also use the ORM. So, let's talk about some of the benefits of that next.

## ORM

Have you ever tried to manually set up an ORM to connect your database to your application? For example, SQLAlchemy, TypeORM, or Sequelize. Even with good documentation, it's not easy. You have to get different types of queries to work, as well as migrations, seeding, and so much more.

Django provides all of that for you out of the box. Just plug in the credentials of your favorite database - Postgres, MySQL, Mongo, and so on - and Django handles the rest. You create models and interact with them via the same Python interface no matter what database you choose.

_Just a note here: unless you are a master of SQL or have a very special case, you should be using an ORM for interacting with Databases in every application._

All of the features listed so far are not exclusive to Python's Django alone. The difference is that most frameworks let you set up your own ORM, Authentication, and so on. Django does all of this with very little effort. This means that you can ship features, MVPs, and applications more quickly.

## Speed of development

Python is a language that is commonly used for quickly prototyping and building applications. Django gives you the speed and power of Python with many additional built-in features to help build web application and APIs much more quickly.

Making decisions and researching tools and libraries takes a lot of time away from actually writing code. Django has well-documented ways of doing things, which cuts out all of the extra time you might spend figuring out a good solution for yourself. 

From bootstrapping a project for you, to creating complex queries, and deploying your application, Django has you covered with [great documentation](https://docs.djangoproject.com/en/3.1/) and [a large community](https://forum.djangoproject.com/) to help you if you get stuck.

It is not just the core Django libraries that can help you to build applications more quickly, though. Django also has thousands of plugins with a common API so you can have certain expectations for how to use any of them in your project.

## Django Plugins

Want to build a CMS? Django has a plugin for that. Actually quite a few of them. If you search Github and [DjangoPackages.org](https://djangopackages.org/), you will find a plethora of solutions for almost any use case.

Here are some of my favorites:

* [Django Rest Framework](https://www.django-rest-framework.org/): Routers, serializers, and other tools to make building APIs simple.
* [Django Graphene](https://github.com/graphql-python/graphene-django): Makes it easy to add GraphQL functionality to Django apps.
* [Wagtail](https://wagtail.io/): Adds a beautiful CMS-style interface to Django with lots of built-in features for common CMS use cases.
* [Django Crispy Forms](https://github.com/django-crispy-forms/django-crispy-forms): If you are building full-stack applications, this package makes working with forms inside templates much cleaner and easier.
* [Django Debug Toolbar](https://pypi.org/project/django-debug-toolbar/): This is a must for Django projects. You can debug everything from SQL queries to templates using this tool.

I hope I have given you enough of a taste of Django to want to try it out for yourself. Let me know how that goes :)

I work with a great team as a senior software developer over at [RocketBuild](https://rocketbuild.com/)! We build a lot of cool projects in Django, React, and other technologies.

If you want to see more Django, Python, and JavaScript content, check out my YouTube channel, [Faraday Academy](https://www.youtube.com/c/FaradayAcademy). Or, get in touch with me on Twitter, [@faradayacademy](https://twitter.com/faradayacademy).

