---
title: What I learned from my first ever software development internship
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T16:27:43.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-my-first-ever-software-development-internship-701aa756a72f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*IPx0r2K1gi55ZWAx
tags:
- name: internships
  slug: internships
- name: Ruby on Rails
  slug: ruby-on-rails
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Viraj Chavan

  I was a student at an engineering college in India. After 3 and a half years years
  of learning computer science academically, I now had a chance to test my knowledge
  in the real world through an internship.

  In this article, I’ll be sh...'
---

By Viraj Chavan

I was a student at an engineering college in India. After 3 and a half years years of learning computer science academically, I now had a chance to test my knowledge in the real world through an internship.

In this article, I’ll be sharing my internship experience at [Josh Software](http://joshsoftware.com/), Pune with the hope that it is helpful to other IT and computer engineering students that are looking for internships.

Like most of my colleagues at the college, I had a very limited view about software development in general and didn’t know what to expect from an internship.

Lucky for me, I was assigned a live project, which was based on Ruby on Rails, something that I had already developed an interest for.

After I had learned PHP and MySQL in the 2nd year of my studies, I built a basic web app, and all that it did was some CRUD (Create, Read, Update, Destroy) operations. I remember talking with a friend who had similar skills to mine, and said “Even we can build Facebook now that we know PHP and MySQL!”

How ridiculously simple things seemed at that time. Now I understand how complex building/maintaining a software can be.

So here’s what I learned from my Internship while working on a live project.

### General lessons

#### Scale Makes a huge difference

![Image](https://cdn-media-1.freecodecamp.org/images/1*SsdGma80xb-AXYYFbEle5A.png)

* How many users are going to use the software?
* How much data will be processed?
* What are the expected response times for a function?

These are questions that we, as college students, hardly think about. Our college projects were usually short-sighted. In real-world projects though, the above questions fundamentally affect decisions about hardware, technologies/tools to be used, system architecture, algorithms, and so on.

#### Working with a large codebase

Back in college, we used to work on projects that had like 15 - 20 files or so. Built in under a week, the whole project could be **understood** in a few hours.

Now the project I’m working on has hundreds of files spread across dozens of folders. It can take months to understand the whole project, and hours to debug a bug that’s spread across multiple files. And the first time you look at the whole project directory, you don’t know where to start understanding the code.

#### Writing maintainable code

Knowing that the code you write will be read, understood, and improved/changed by someone else (or even yourself) in the future makes you write code that’s maintainable.

In college, all I focused on was getting the expected functionality to be complete, and never considered whether the code I wrote was maintainable.

This resulted in scrambled pieces of code that somehow worked at the time. But two days later even I wouldn’t understand why I had written a certain piece of code that way. And changing some part of the code almost always broke other parts. ?

**Code Maintainability is easier to recognise by its absence**, like when something you thought should take an hour ends up taking a week.

#### Using a version control system - properly

When I first started building small software, all the files existed on my own development machine, and maybe they were backed up to Google Drive as regular files.

Then I got to know about GitHub, but I merely used it as a safe storage place for my code. I used the GitHub desktop app to commit all changes on just the master branch. I even hesitated using it through the command line.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0o9GZUzXiNnI4poEvxvy8g.png)

Now not a day goes by that I don’t use Git. It’s such a great tool for collaboratively writing code, distributed development, branching out for new features, pull requests, and so on.

Here’s a [little article](https://www.git-tower.com/learn/git/ebook/en/command-line/basics/why-use-version-control) on why version control systems are awesome!

#### The importance of using a Test Driven Development approach

During my internship, I was assigned to work on a new feature that was to be added to the main project .

I wrote the code and tested if it was working the way it was supposed to. It worked perfectly, or so I thought. I deployed the feature to the production confidently, and moved on to work on something else.

After a few hours, [Rollbar](https://rollbar.com), a real time error reporting tool burst with a number of errors in our code deployed to production. I checked the errors and they seemed unrelated to anything I had ever worked on.

After some debugging, all of those errors traced back to a single method. A method that was called in numerous places, and in which I had modified just a single line, and hadn’t checked where else it was used.

Now this could’ve been avoided if the code that used that method had test cases written for it, and if I had checked if all the test cases ran successfully before deploying the code. That made me realize the importance of test driven development.

[Here’s an article](http://sd.jtimothyking.com/2006/07/11/twelve-benefits-of-writing-unit-tests-first/) to understand why writing test cases is important.

### Things specific to Ruby on Rails/ Web Development

#### The MVC Architecture

Back in my college days, when I developed applications in PHP, I had no clue what Model, View, and Controller were. Any project was so complexly scrambled that I couldn’t find in which file a piece of important logic was written. The HTML embedded PHP scripts at odd places and I had placed all the files in just one folder.

Then I learned about the Rails framework, and got accustomed with the MVC architecture.

> Model-View-Controller (MVC) is an architectural pattern that separates an application into three main logical components - Model, View, and Controller. Each of these components are built to handle specific development aspects of an application ([source](https://medium.freecodecamp.org/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053))

MVC really simplifies things and is an important part of many major frameworks.

#### Dealing with Databases

In the last 6 months, I haven’t written a single direct SQL database query. Yet I deal with databases everyday, even doing some complex operations. This is thanks to the ORM (Object Relational Mapper) that Ruby On Rails uses.

ORMs convert object-oriented programming language such as Ruby into database lingo in which to perform operations. Which makes data access more portable and abstracted from the required database queries that are necessary when manipulating data.

Thanks to ORM, it’s much much easier to query the database. This gives a big [advantage to beginners](https://m.signalvnoise.com/conceptual-compression-means-beginners-dont-need-to-know-sql-hallelujah-661c1eaed983), who can start writing applications without even knowing SQL.

#### Writing/Using REST APIs (Application Programming Interfaces)

[APIs](https://hackernoon.com/what-are-web-apis-c74053fa4072) make it easier for one application to talk to another.

APIs make some other applications’s functionalities easily accessible to our application. For example, I once developed a Road Trip Planner application that used the Google Maps API to show various places on a map that a user could visit on a particular route.

APIs can also be used to separate the front-end and the back-end completely. For example, we can write the back-end as an API-only Rails application that can be used by a web site, an Android/iOS application, or even some third party applications.

#### Using ElasticSearch for searching

Although I don’t know much about ElasticSearch so far, but I’ve learned that it’s a NOSQL, distributed full text database. It acts as a distributed search engine that is incredibly easy to scale and returns results at lightning speed.

Why would we need it for searching? Because having millions of records in a regular database can make it really complex to make efficient searches.   
With Elasticsearch, we can index the documents needed to be searched and it can perform queries across all those millions of documents and return accurate results in a **fraction of a second**.

Elasticsearch has a Restful API, which makes it really easy to query the searches and get the results.

[Here’s a tutorial](http://joelabrahamsson.com/elasticsearch-101/) that helped me, and here are some [use cases](https://www.elastic.co/blog/found-uses-of-elasticsearch) of Elasticsearch.

#### Using asynchronous/background tasks

Sometimes the user will perform an action on our application that takes a considerable amount of time to complete. We don’t want the user to sit there waiting for this action to complete, so we send it off to a background worker.

[Here’s a link](https://blog.iron.io/every-web-application-needs-background/) that explains it better.

In Ruby On Rails, I came across [Sidekiq](https://sidekiq.org/), which makes it [easy to handle background tasks efficiently](https://medium.com/@aledalgrande/3-ways-to-make-your-web-pages-more-responsive-with-sidekiq-a3fcb1e9dcef).

Thanks for reading! If you found this article helpful, give me some claps. ?

There’s still a long way to go!

Check out my Github profile [here](https://github.com/virajvchavan).

