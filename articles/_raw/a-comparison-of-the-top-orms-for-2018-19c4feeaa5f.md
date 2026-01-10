---
title: Which JavaScript ORM should you be using in 2018?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-03T22:24:30.000Z'
originalURL: https://freecodecamp.org/news/a-comparison-of-the-top-orms-for-2018-19c4feeaa5f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1fDVMWj-QH04s4QxaGwOsg.jpeg
tags:
- name: api
  slug: api
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By John Vandivier

  NOTE: May 2018: Read From TypeORM to LoopBack: A Retrospective for an updated perspective!

  — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

  This article reviews Object Relational Mapping (ORM) solutions in the JavaScrip...'
---

By John Vandivier

**NOTE: May 2018: Read** [***From TypeORM to LoopBack: A Retrospective***](https://hackernoon.com/from-typeorm-to-loopback-a-retrospective-188ea18527a2) for an updated perspective!

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

This article reviews [Object Relational Mapping](https://en.wikipedia.org/wiki/Object-relational_mapping) (ORM) solutions in the JavaScript ecosystem, and identifies an ideal solution based on specific requirements.

### **What is an ORM and Why is it so Important?**

ORM solutions are useful to facilitate data-driven API development. Users have concrete needs which drive the data model of an application. In legacy development, this data architecture is typically implemented and version controlled using database scripts such as SQL scripts. A separate library is then used for the server application to execute CRUD actions on the database.

ORMs work as a high-level API to execute CRUD, and these days quality ORMs also allow us to initialize the data through code. Complex data manipulation, cleaning and so on, is often easier in code. While dedicated Extract, Transform and Load ([ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load)) tools exist, the same ETL tasks can be easily implemented in ORM.

Implementing extract, transform, and load with code allows a system to more easily integrate data from very different sources. SQL databases of multiple flavors, NoSQL data, file system data, and third party data can all be integrated under a single language with a JavaScript ORM.

Finally, code-oriented data control also allows a system to implement data usage at run time or in the build process, and flexibly adapt usage during the development process as needed.

To restate, ORMs improve developer productivity by providing a high-level API, in a single language, with functionality that would traditionally require several different tools and skill sets. Fewer skill needs, tool needs, and hours required facilitates project margin. Unforeseen requirements and project timeline are better prepared with flexible build and run-time data configuration.

### **Preferred ORM Capabilities**

The particular project context leading to this ORM review requires the implementation of a cutting edge, CMS-like, [universal JavaScript](https://medium.com/@mjackson/universal-javascript-4761051b7ae9) application.

Cutting edge universal JavaScript frameworks come in essentially 3 flavors: Angular, React, and Vue. That is to say [Angular Universal](https://universal.angular.io/), [Next](https://github.com/zeit/next.js/), and [Nuxt](https://nuxtjs.org/).

Node natively supports file system operations, so Content Management System data requirements amount to a preference for wide-ranging database support. In total, the following requirements are considered:

1. Support for Mongo and MySQL, with preference to support of additional options
    
2. Integrate with Webpack
    
3. Integrate with Express
    
4. Minimal [hit to performance](https://medium.com/@ameykpatil/why-orm-shouldnt-be-your-best-bet-fffb66314b1b) at run time
    
5. Intuitive syntax
    
6. Extra features
    
7. High Github star to issue ratio
    
8. Actively maintained with no build failures or deprecated dependencies
    

### **The Candidates and Results**

Each candidate received a score between 0 and 10 for each preferred capability. A score of 5 means acceptable. The average for a column may be more or less than 5. For example, an ORM with support for multiple NoSQL databases and no support for any SQL database will receive a score between 2 and 4. 0 indicates the complete lack of a feature.

![Image](https://cdn-media-1.freecodecamp.org/images/xZdD-bktDeeZ0Q6fQxxooOyg0kaoWEu3DA3J align="left")

*View* [*this Google Sheet*](https://docs.google.com/spreadsheets/d/1sSbY8SLWA9lvvnTHX41t0TVPXwZ4A4ddO_KJMa20fA4/edit#gid=0) *to click the hyperlinks or copy data as a table.*

A special shout-out to [joi](https://github.com/hapijs/joi), [pg](https://github.com/go-pg/pg), and [knex](http://knexjs.org/). These libraries are not full ORMs but they are great at what they do. If you don’t need a full blown ORM, take a look and see if they can address your need.

### **Conclusion**

The totals reflect the overall usefulness of each solution. The top 5 results were:

1. Loopback
    
2. Waterline
    
3. Mongoose
    
4. TypeORM
    
5. Sequelize
    

A combination of project-specific needs, omitted factors, and personal preference lead to the top 3 picks.

Waterline is heavily integrated into the Sails framework and Mongoose only supports MongoDB.

Sequelize and NodeORM2 are restricted to SQL and they lack API generation.

Due to the TypeScript syntax, TypeORM integrates nicely with an Angular project.

As a developer, I recommend prototyping more than one top solution to identify the real winner. The top 3 solutions, which are all prototyping candidates, include:

1. Loopback
    
2. TypeORM
    
3. Caminte
    

I submitted this information to other developers on the project, and as a team we decided to try out TypeORM first. Check back later for the retrospective!

What do you think of this result? Leave a comment or contribute you thoughts to [this Slant comparison](https://www.slant.co/improve/topics/11235/~javascript-orms).
