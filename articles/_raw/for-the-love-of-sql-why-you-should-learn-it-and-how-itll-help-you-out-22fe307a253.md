---
title: 'For the love of SQL: why you should learn it and how it’ll help you out'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-03T21:22:53.000Z'
originalURL: https://freecodecamp.org/news/for-the-love-of-sql-why-you-should-learn-it-and-how-itll-help-you-out-22fe307a253
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wdnZPs8tLOGbEfECpoh5Kg.png
tags:
- name: big data
  slug: big-data
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Matthew Oldham

  I recently read a great article by the esteemed @craigkerstiens describing why he
  feels SQL is such a valuable skill for developers. This topic really resonated with
  me. It lined up well with notes I’d already started sketching out ...'
---

By Matthew Oldham

I recently read [a great article](http://www.craigkerstiens.com/2019/02/12/sql-most-valuable-skill/) by the esteemed [@craigkerstiens](http://twitter.com/craigkerstiens) describing why he feels SQL is such a valuable skill for developers. This topic really resonated with me. It lined up well with notes I’d already started sketching out for a similar article about developing a love for data.

The more I fleshed out my topic, however, the more I realized that many of my points and examples seemed to be centering around SQL. Reading Craig’s article convinced me to redirect my focus and talk more about why I personally have such an affinity for SQL.

In short, Craig makes the following assertions about SQL (and I quote):

> 1. It is valuable across different roles and disciplines

> 2. Learning it once doesn’t really require re-learning

> 3. You seem like a superhero. You seem extra powerful when you know it because of the amount of people that aren’t fluent

I’ve found all these points to be true in my own experience, and I’d like to recast and expand on each one.

#### The Versatility Effect

The SQL skillset has proven to be an extremely valuable asset in my career. In fact, I believe SQL to be the single most powerful and versatile “programming” language I know.

I have been able to use SQL to solve many problems, and it’s my go-to tool anytime I face a new challenge. In fact, I keep an instance of [PostgreSQL](https://www.postgresql.org/) running on my laptop so I can quickly hop into my [favorite SQL GUI](https://www.dbvis.com/) whenever I need to test something out.

Here are just some of the cool things I’ve been able to do with SQL:

![Image](https://cdn-media-1.freecodecamp.org/images/C8Q-vL5taSoDEP9SRX2Y02hLc1oA5EHLso5h)
_SQL FTW!_

Are you having a hard time believing that list above? I promise you there’s not an ounce of exaggeration in it. Now, are there some items there that were dependent upon other capabilities of the RDBMS I was using at the time? Sure. Regardless, each of those solutions was implemented in SQL.

#### The Bicycle Effect

While Structured Query Language has certainly undergone changes and has been expanded over the years, I agree with Craig that the fundamentals have not changed. The overall level of volatility compared to other languages has been relatively low.

I would argue that this fact only strengthens the argument that one should invest the time to learn SQL. You can be confident that you’ll get a lot of mileage out of such an investment without having to look up the latest conventions the next time you need to use it.

So, learn SQL! Here are some great places to get started:

[**SQL Tutorial — Essential SQL For The Beginners**](http://www.sqltutorial.org/)  
[_This SQL tutorial helps you get started with SQL quickly and effectively through many practical examples. After the…_www.sqltutorial.org](http://www.sqltutorial.org/)

There are even interactive tutorials:

[**SQLBolt — Learn SQL — Introduction to SQL**](https://sqlbolt.com/)  
[_SQLBolt provides a set of interactive lessons and exercises to help you learn SQL_sqlbolt.com](https://sqlbolt.com/)

There are also some versatile sandboxes out there that allow you to run SQL in various dialects without having to install anything. For example, [SQL Fiddle](http://sqlfiddle.com/):

![Image](https://cdn-media-1.freecodecamp.org/images/-Yav499rZkhE8ee4JtdnkvLE4pgFfRcUUc76)
_SQL Fiddle_

Or, [DB Fiddle](https://www.db-fiddle.com/):

![Image](https://cdn-media-1.freecodecamp.org/images/yvN5Y8Qk9QgHq1V1A1MorV5GjCbi2Vh3Yxw-)
_DB Fiddle_

#### The Superhero Effect

I remember a colleague once saying he broke into a cold sweat every time he had to write SQL. ?

It sounds exaggerated, but SQL can be intimidating to anyone who properly regards the database as the sensitive asset it is and is not familiar with how to safely interact with it. SQL, being one of the adults in the room, also doesn’t get as much attention as other shiny new programming languages. That means that it remains a less common skillset among contemporary and emerging developers.

As such, having a solid understanding of SQL and the insight to see the set-based facets of a given problem or challenge provides the opportunity to be a hero.

One of my favorite personal experiences was helping a customer debug a slow and complex [SAS](https://en.wikipedia.org/wiki/SAS_(software)) program. The goal of this program was to extract a list of state transitions from an audit table in order to measure the mean duration a widget spent in each phase of a given business workflow. The implementation of these calculations was complex and required building multiple local data sets.

I remember reverse engineering this program and realizing that I could solve the problem much more easily using a single SQL query and the magical [LAG](http://www.sqltutorial.org/sql-window-functions/sql-lag/) window function.

The customer was simply blown away.

Not just because he learned about the LAG function, but because he saw just how powerful SQL can be.

An even more dramatic example was during a large data warehouse migration where I replaced an entire Java program (that took more than 20 minutes to complete!) with a single SQL query that ran in seconds. The original author of the program was shocked! That was a really good day. ?

So, I encourage you to dive into SQL today and broaden your skillset with one of the most versatile tools I’ve had the pleasure of working with. If you already know SQL and agree, or if I’ve convinced you to give it a try, please consider leaving me a comment.

