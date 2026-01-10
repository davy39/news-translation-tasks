---
title: 'Laravel’s Polymorphic Relationships: A Practical Use Case'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T14:31:26.000Z'
originalURL: https://freecodecamp.org/news/a-practical-use-case-for-laravels-polymorphic-relationships-231ab425b95a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*js7-5fdBmy0r36PW32dqYA.png
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Joe Dixon

  Recently, when working on my side hustle Zero to Grow, I ran into quite a complex
  database design issue.

  The solution involves a use case for Laravel’s Polymorphic relations that goes way
  beyond the comments example in the documentation....'
---

By Joe Dixon

Recently, when working on my side hustle [Zero to Grow](https://zerotogrow.io/), I ran into quite a complex database design issue.

The solution involves a use case for Laravel’s Polymorphic relations that goes way beyond the [comments](https://laravel.com/docs/5.5/eloquent-relationships#polymorphic-relations) example in the documentation.

### What’s the problem

To get under the hood of this problem, you’ll need to understand a little bit more about the app I am building.

[Zero to Grow](https://zerotogrow.io/) is an app aimed at developers who want to grow their side projects. Whether their goal is to increase traffic, retention, conversions or anything else; this app is here to help.

Upon signup, the user is asked to define the overall goals that they wish to achieve and the metrics they need to track along the way.

Once their goals are defined, the user then creates and runs tests on their side hustle with the aim of meeting those goals. An example of a test would be ‘Send at least one tweet per day to increase engagement’.

As with goals, the user needs to define the metrics to track in order to determine whether or not the test was successful.

It should be possible for metrics to be updated as often as the user requires throughout the course of the test or goal.

To make things more complicated, we also have the concept of ideas. They can be either private to an individual user or made publicly available for others to use.

Ideas are always the starting point of tests. The user will find an idea, either by creating it themselves or by searching the public directory, and begin testing it to see its impact on the overall goal.

### Designing the schema

In order to understand how polymorphic relations can help, I’m going to talk you through the schema I designed to solve this problem, piece by piece.

#### Goals and metrics

A user may wish for their primary goal to be increasing the overall conversion rate of a landing page. To effectively measure this, they might want to track the total visitors to the landing page along with the total number of signups.

Upon starting the goal, the user should enter the base and target metric values. During the lifetime of the goal, they should regularly update the metrics with the latest values.

The data structure would look something like this.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fzAQFZrAMwAXD0SK.png)

This diagram is telling us each goal can have one or many metrics and each metric can have one or many entries.

With this data structure, users will be able to create a goal and assign it with all of the metrics they wish to track. They will then be able to update the goal with new entries as required during the lifetime of the goal.

#### Ideas and metrics

A user should be able to define an idea and associate any metrics that should be tracked. In this respect, the data structure will look similar to that of goals and metrics above. However, we don’t need to worry about tracking the metrics until the user starts testing it.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mvuBFDL9ZwBMMdD6.png)

As with the previous example, each idea can have many metrics, which will satisfy our requirements.

#### Tests

Tests are where things start to get interesting.

As previously mentioned, ideas can be made publicly available and therefore tested by lots of different users. The fact that each test needs to be assigned to a goal makes this all the more complex.

Upon launching a new test, the user should enter its base and target metric values. Then, during the lifetime of the test, they should regularly add the latest values.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yZwfhqpnClreNfpN.png)

Essentially, this is a 3-way pivot table. The default naming convention for this table in Laravel would be `idea_goal_user`. It doesn’t exactly roll off the tongue.

Usually, I find that pivot tables tend to encapsulate some sort of feature or behavior, and I prefer to name it in a way that reflects this. In this instance, the combination of a goal, idea and user is everything needed to run a test. As such, this table becomes `tests`. It allows an idea to be used by multiple users as well as be assigned a goal.

What you may have noticed in the diagram above is that the `entries` table facilitates a many-to-many relationship between the `tests` and `metrics` tables.

A key design decision had to be made here. The fact that ideas are publicly available and can be tested by multiple users means that if this many-to-many relationship didn’t exist, it would be impossible to tell which user had entered a value against the metric.

### How Polymorphic relationships can help

In looking at this schema, there are a couple of places where polymorphic relations can be used.

First, the most obvious place to extract a polymorphic relation is between both the goals and ideas tables to the metrics table. Although different relations, the data for storing is identical between the two and so is the perfect use case.

Rather than defining separate tables for defining metrics such as `goal_metrics` and `idea_metrics`, simply define a single table and use a one-to-many polymorphic relationship to both. The migration might look something like this.

With the model relationships defined like so:

That’s all that is needed for this relationship. Making use of it is no different from defining a standard one-to-many relationship.

The second use case is a little bit more difficult to spot and you might disagree with my approach. However, in my opinion, this is a really elegant solution.

Both metrics for goals and metrics for tests have a relationship with an entries table. This is where values associated with the defined metrics are stored.

For goals, the relationship should really be a one-to-many. A metric can have many entries, but an entry belongs to a metric.

With tests, the relationship is slightly different as the metrics are defined against an idea that can be tested by multiple users. As such, each test can have many metrics and each metric can belong to many tests. This is a many-to-many relationship.

To solve this problem, an intermediate (or pivot) table can be defined between tests and metrics. It makes sense to call this table `entries` and store the values entered directly into this pivot table.

Although the relation between entries and bot tests and goals are different, I think in this case, it makes sense to break standard database normalization and use a single table to store all data entry of metrics.

The implementation might look something like this:

With the model relationships defined like so:

Interacting with these relationships is still extremely simple.

There you have it, a many-to-many polymorphic relationship.

As I mentioned earlier, it’s not the only way to solve this problem. You may wish to tackle the last many-to-many relationship using separate tables. Even though it breaks convention, keeping all of the metric entry data in the same table is a particularly graceful solution and a great example of the power of Laravel’s native polymorphic relationships.

For me, designing the solution in this way makes it much easier to ‘grok’ what the application is doing for both new folks going into the project and myself, six months down the line. Ultimately though, to each their own! Would you have taken a different route? If so, let’s chat in the comments below — I’d love to read your thoughts.

Originally published at [joedixon.co.uk](https://joedixon.co.uk/a-practical-use-case-for-laravels-polymorphic-relationships).

