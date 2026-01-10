---
title: Our journey into the world of Microservices — and what we learned from it.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T21:52:30.000Z'
originalURL: https://freecodecamp.org/news/our-journey-into-the-world-of-microservices-and-what-we-learned-from-it-d255b9a2a654
coverImage: https://cdn-media-1.freecodecamp.org/images/0*APjNMu9aZ4xsCz1y
tags:
- name: agile development
  slug: agile-development
- name: Life lessons
  slug: life-lessons
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ignacio Salazar Williams

  I know, I know everyone is talking about Microservices. It’s the a pattern that
  will lead us to the future of architecture, say those who talk about Digital Transformation.
  It’s the “Destroyer of Monoliths” for others, the...'
---

By Ignacio Salazar Williams

I know, I know everyone is talking about Microservices. It’s the a pattern that will lead us to the future of architecture, say those who talk about [Digital Transformation](https://enterprisersproject.com/what-is-digital-transformation). It’s the “Destroyer of Monoliths” for others, the silver bullet that will solve all of our architectural problems.

Let me tell you something about microservices. **They really are something**, but it is not just like **puff** **some magic** **Fairy dust** here is the solution to all our problems. I’m **not** going to tell you more about them as a pattern, but rather I’ll try to tell this story (my story) as best as I can. I’ll discuss how this concept, this pattern, was developed in reality, under certain circumstances. I call it The **Micro-Armageddon**.

![Image](https://cdn-media-1.freecodecamp.org/images/kHXZp0ke9-N0aBMf6LeqPV5RrjZaDIKjCtOP)
_Source from [GIPHY](https://giphy.com/gifs/oscars-awards-academy-Ho2mVZ5dvsW7S" rel="noopener" target="_blank" title=")_

On a daily basis, on my team, there were things that were out of our reach and led to problems. But it was just a matter of seeing the big picture, and working with the mentality to continually improve our components until we reached the quality standards that we as a team had.

So please follow me along this journey of goods and bads, laughs and tears, and lots of “why the heck did we do this in the first place?”

> _TL;DR?_  
> _I know it seems like a lot, but let me tell you something. If you are looking to learn from another’s mistakes about Microservices, I do highly recommend that you read this article completely. But if not, you can skip to the memes — at least it’ll make you laugh!_

### A little bit of background

![Image](https://cdn-media-1.freecodecamp.org/images/HFuGKP76J88kmX5hEOYDvZQnocRWHcqehIql)
_Source From [Innoview](http://innoview.hu" rel="noopener" target="_blank" title=")_

Let’s start with the basics. There was me (Hi!), a recently graduated student of computer science, who just got hired for some consulting (the wild west of jobs). I got assigned to this project for one of our clients (in their offices), in which our team was in charge of applying a Digital Transformation to their business. Therefore, Microservices were involved. (Now that I’m more experienced in the field, I hear these two concepts very often together.)

We were using [Node.](https://nodejs.org/en/)js as the back-end programming language (ohhhh yeeees), so that meant we were also using [Express](http://expressjs.com/) as a default framework to expose the APIs. Also, it’s important to add to the mix that we were using the Agile methodology of [Scrum](https://medium.com/chingu/a-short-introduction-to-the-scrum-methodology-7a23431b9f17) (you’ll see why I brought up this point shortly).

#### The Teams

![Image](https://cdn-media-1.freecodecamp.org/images/AyGe9CCxGMuw6dKE2txFxzMYtm-Dg511LMTF)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We were divided in two big groups: the first one, the one that I was part of, was the **Architecture Team.** We were in charge of orienting the teams and spreading the word about Microservices. The second team, the **Dev Team,** was in charge of developing the products desired by the business. There were multiple teams working on different products at the same time, along with working on the Microservices.

**The Architecture team** looked something like this:

* 1 Senior Manager (ours)
* 2 Managers (1 ours, 1 theirs)
* 10 Architects (6 ours, 4 theirs)
* 2 in charge of big data
* 3 in charge CI/CD
* 3 in charge of security
* 2 in charge of back/front end development architecture

Each **Dev Team** looked something like this:

* 1 Scrum Master (another consulting)
* 1 Product Owner (client side)
* 4 Developers (2 ours, 2 theirs)
* 1 QA
* 1 UX
* 1 Architect (client side)

> _I know that this already sounds bad, mixing it all up, but don’t you worry — for us, it was an opportunity to make things right…_

#### Developer background skills

![Image](https://cdn-media-1.freecodecamp.org/images/jmm-Fjij7bveSXWDVpeKMQVaeHMijUZyp8oG)

> None of us was born being a skilled developer, all of us were like a monkey trying to compile a basic “Hello World”. [Felipe Lazo](https://www.freecodecamp.org/news/our-journey-into-the-world-of-microservices-and-what-we-learned-from-it-d255b9a2a654/undefined)

Our team members had all kind of backgrounds, from the the ones that barely know how their own computer worked, to the ones that probably came from NASA. Some people had worked with COBOL, Java, JavaScript, C, Python, and others, and while others had worked with no languages at all.

So it would be easy to understand if some team members weren’t especially good at developing good code and structures, as many of them had no previous background in the subject. Again, there were others that had some experience. So it was perfectly fine to have all these different profiles, but it was up to us to make the best of them. We couldn’t see it as a weakness, but an opportunity for us as a team (specially when you work in an agile environment).

### The Objective

Here we were with the goal of implementing Microservices as a Back-End solution to the integration of legacy components that our client had. We planned to expose them as simple APIs in order that the teams could integrate them into their applications.

Here were the initial requirements of our Microservices:

* They had to Consume a SOAP Service and return the result as JSON. I know that for most of you (and including me), it’s going to sound really bad. But it had to be like this, because the Microservices weren’t authorized to connect to the Data Layer directly, so they had to go through SOAP [Client initial requirement].
* It had to LOG all the data that produced the Microservices into the brand new DataLake.
* Basic Authentication.
* Get them to be as fault-proof possible.

To these requirements, we had to add:

* the quality that we desired through Unit Testing (including our ambitious coverage standard of 90%)
* Static Code Analysis
* Performance test
* and some kind of Security Check.

All of this had to be manually checked locally and then checked through a rigorous Pipeline (CI/CD). I say rigorous, but it wasn’t a blocking one. It still allowed teams to deploy Microservices even though one of the jobs failed. But **don’t ever do this, or at least know the consequences**.

So far, we didn’t have many problems at all. This sounded pretty good for a basic setup in order to develop Microservices. We had DevOps, we were all in the same place, we had our methodology, we had our pattern, and we had a fantastic run-time (Node.js) that would allow us to build and follow the rules step by step to make this project a masterpiece. Well, at least that was what we thought…

### Oh boy, mistakes were made

![Image](https://cdn-media-1.freecodecamp.org/images/NI49nxrMg1e5yTrvyk9QU6RZrVo5qONSrong)
_Accurate picture of the team trying to save Microservices_

Check out this fairly accurate picture of the architecture team trying to save the Microservices from their doom. Why did this happen, you may ask? Well, this can happen when you give the freedom to multiple teams to develop their own Microservices in an Agile environment. Trouble arises when you don’t give any other explanation of what Microservices actually are, what they do, what is their purpose, how we govern them, and, most importantly, how big they have to be.

And to top all of that off, at the beginning of the project we didn’t have any reliable Version Control Software except Subversion. Meanwhile we were waiting for Git to be installed on premise.

A problem that we saw often in many immature teams was that instead of trying to put out the fire, they just spread it out even more by duplicating the Microservices and beginning to build over them. This made them even bigger and they contained useless and duplicate content.

* Microservice _Clients_ (Team A, B and C work on it)  
 — Team B is tired of all the merges, and all the fighting for who is responsible of what, plus the deployment of it.
* Microservice _Loans-Clients_ (Team B)  
 — Team B copies the exact state that they were working on in the _Clients_ Microservices. This exposes and maintains more and more useless endpoints on top of their actual useful ones.

So here we were. How the hell (actual hell) do we solve all of these problems? Well, this is what we did.

### The Symptoms

![Image](https://cdn-media-1.freecodecamp.org/images/A2j6VKJ699KC42Umz9HLnuNLJhkGTLKc8z8A)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We clearly couldn’t keep going with all of this mess, so we put on our white doctors’ coats, sterilized the room, and did an autopsy of what we had. We identified the symptoms of our unavoidable doom, prioritized the most important ones, and tried to win small victories that would allow us to take control over the situation.

> _Small victories allow you not only to prove that you know about the subject, but they also let the teams know that something can be done to improve their daily work._

#### Mini-Monolith A.K.A Macroservices

Wait what? We were talking about microservices…

![Image](https://cdn-media-1.freecodecamp.org/images/S1UIv5TkaDGJjNGUjDudUMTPXhuyKITVkeZV)

I bet you have read multiple times about the [**S.O.L.I.D**.](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf) principle, about having smart compact pieces that have the famous single responsibility principle.

What we had was nothing like that. This is why I called them **Macroservices,** after I saw what was happening.

Just picture this: in a simple domain, let’s call it _Users_, there were around 15 **POST** Operations in the same ****cough**** “Microservice.” Every single one had a different purpose under the same domain and used custom made libraries for each one of them. Plus we had all the unit and performance tests spread around in there. So it was mayhem. It was pretty much something like this:

```
.
├── app --The whole MS is in here
│   ├── controllers --All the controllers of the domain
│   │   ├── dummies
│   │   │  └── ** All the dummies for each controller **
│   │   ├── xsl
│   │   │   └── ** All xsl configuration for each controller **
│   │   ├── Controller1.js
│   │   ├── Controller2.js
│   │   ├── Controller3.js
│   │   ├── Controller4.js
│   │   ├── Controller5.js
│   │   └── **Literally 20 more controllers**
│   ├── functions --All the functions of the MS
│   │   ├── function1.js
│   │   ├── function2.js
│   │   ├── function3.js
│   │   └── function4.js
│   ├── properties --All the properties of the MS
│   │   ├── propertie1.js
│   │   └── propertie2.js
│   ├── routes --All the routes of the MS
│   │   ├── routes_useSecurity.js
│   │   └── routes_withoutSecurity.js
│   ├── services --Extra services that were consumed
│   │   ├── service1.js
│   │   └── service2.js
│   └── xsl
│      └── **A bunch of XSL to do transformations**
├── config --"Global" configurations
│   ├── configSOAP.js
│   ├── configMS.js
│   ├── environments.js
│   ├── logging.js
│   ├── userForBussinessA.js
│   └── userForBussinessB.js
├── package.json
├── README.md
├── test--All the tests
│   ├── UnitTesting
│   │   └── Controllers
│   │       └── ** All the 25 tests in theory **
│   └── PerformanceTest
│       ├── csv_development.txt
│       ├── csv_QA.txt
│       ├── csv_production.txt
│       ├── performance1.jmx
│       └── performance2.jmx
├── server.js --Express Server
├── serverKey.keytab
├── sonarlint.json
├── encryptor
├── ** Around 10 more useless files **
└── Dockerfile
```

![Image](https://cdn-media-1.freecodecamp.org/images/9omI01k5ttMHeMAnmTT3xHEgG9fFvclEkeLo)
_This was pretty much me_

First of all, this had to stop because it was ungovernable. Teams were fighting, because in order to test something in the DEV environment (which they did often), they had to go through the CI/CD pipeline. By that time in the project, it certainly wasn’t perfect.

So If **team A** modified **Controller1,** they had go to through the pipeline, with a high chance of failing (and deployment would then fail, too). They would go over and over again until they succeeded. Therefore, all the teams tried to race so they wouldn’t be the last that deployed. Because if something failed in that deploy, fingers were pointed. It meant that the team did something wrong and broke it.

> _Fun right? A healthy environment for all developers. Who doesn’t want to be there… well, NOT ME!_

### It was time to have a fresh start

![Image](https://cdn-media-1.freecodecamp.org/images/w6qPgt5B6Wy2mmnYRsbSNmY34FSk5IqKiDP3)

We needed to start fresh and do things right. Take control of who was doing what, and make them responsible. But we had to be fair: we were not going to make a team responsible for a whole domain that contained 15 operations, tests, deployments, and so on. Nobody wanted that.

> _You know, we are agile, agile people do agile things. We don’t need to waste our precious time on these fights of who owns what, raising blockers, and pointing fingers ** **rolling eyes****._

#### Step 1: Sizing Microservices

I’m going to make a **bold assertion** and say that the largest number of operations for any Microservices **must** follow the [**CRUD**](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) standard. Forget about thinking about how big the Microservices should be.

Following this rule will give you peace of mind at night, knowing that at most — at any given time — you’ll only need to have 4 operations in any subdomain. And that’s it.

This means:

#### POST — Create

CREATE procedures are the insertion of new data as the finality of the Microservices.

#### GET — Read

READ procedures read the data needed by the client.

#### PUT — Update

UPDATE procedures modify records without overwriting them.

#### DELETE — Delete

DELETE procedures delete where specified.

![Image](https://cdn-media-1.freecodecamp.org/images/3SKmmU2hZXeEdU2Owfg9z-ihdt-NS6Bq-8-k)

Using this rule allowed us to make more compact, smart, and standard Microservices. It will grant us the upper hand when the time comes to divide the Microservices, for example.

Let’s say that I have my _Clients_ Microservice in a banking Domain, and suddenly I see that I not only need our _credit clients_ but also our _loaners._ Well, that’s easy. I just divide our Domain Clients into two Subdomains: _Credit-Client_ and _Loan-Client_, and from there you can see how everything starts to fit into place.

Perfect! We now had proper microservices. It was now up to the client and the team to develop a way to know how to split the Domains, and know their Subdomains.

> _If only there was a way to do it… **cough** [**Doman Driven Design**](https://medium.com/withbetterco/what-is-domain-driven-design-bcf81fc4fdc1)._

#### Step 2: Someone has to own it

Woo-hoo, we had one of our problems fixed, but wait — now I had a bunch of smaller pieces, and everyone was working on them. And I wasn’t going to be responsible for it if it broke.

All I’ll say is: “**If you code it, you own it”**. And with this powerful wisdom you may say: “Well I know that, everyone knows that.” But no, not everyone knew that, and it is a common mistake. So be smart, and go one step further and make it a rule.

![Image](https://cdn-media-1.freecodecamp.org/images/gKCZrqk4UPKn1dD2rJ7n-QJnrCHKoBELGhYN)
_Source From D. Keith Robinson Article [Learn to love Git](https://medium.com/designing-atlassian/learn-to-love-git-part-one-the-basics-90429f456ace" rel="noopener" target="_blank" title=")_

Git allows you to develop in peace (if it’s applied well — check the link about [Learning to love Git](https://medium.com/designing-atlassian/learn-to-love-git-part-one-the-basics-90429f456ace) from D. Keith Robinson above), knowing that your code is always going to be up to date. If anyone else wants to improve it, suggest a change, or if they simply need an update, all this has to go through the owner. For the sake of this example, we will say that the owner is the architect of the DEV team who developed it. This works so well in agile environments.

#### Step 3: API Endpoint (Naming) and Versioning

The way that you name APIs could save all your developers tons of time and effort. **Naming APIs it’s not a game. It could save lives**.

It’s really important to add value to your Microservices by naming them correctly. If you don’t know what to name them, ask the business and discuss it with your team. Design driven development may help here.

Check out the [RESTful API Designing guidelines — best practices](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) for more info here. I could’ve quoted the whole page.

#### Step 4: Let’s restructure what we had

![Image](https://cdn-media-1.freecodecamp.org/images/D1OTtJsvT32jf-aLthKXqbYlnWQwbOkJpYSq)
_“A child playing with a Jenga block tower” by [Unsplash](https://unsplash.com/@mparzuchowski?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Michał Parzuchowski</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> _It’s one thing to have the concept right, but how does it look in practice?_

The next file tree that I’ll show you gets back to my idea of how much of a follower of the concept of Microservices I am. I’ve made it follow the **loose coupling** and **high cohesion** between services concept:

```
.
├── config
│   ├── artillery.js
│   ├── config.js
│   ├── develpment.csv
│   ├── processorArtillery.js
│   ├── production.csv
│   └── qa.csv
├── index.js
├── package.json
├── package-lock.json
├── README.md
├── service
│   ├── getLoans --The operation
│   │   ├── getLoans.config.json --Configuration of the resource
│   │   ├── getLoans.contract.js --Contract test
│   │   ├── getLoans.controller.js --Controller
│   │   ├── getLoans.performance.json --Performance test config
│   │   ├── getLoans.scheme.js --Scheme validator
│   │   ├── getLoans.spec.js --Unit Tests
│   │   └── Util --Local functions
│   │       ├── trimmer.js
│   │       └── requestHandler.js
│   ├── postLoans
│   │   ├── postLoans.config.json
│   │   ├── postLoans.contract.js
│   │   ├── postLoans.controller.js
│   │   ├── postLoans.performance.json
│   │   ├── postLoans.scheme.js
│   │   └── postLoans.spec.js
│   └── notFound
│       ├── notFound.js
│       ├── notFound.performance.json
│       └── notFound.spec.js
├── Util --Global functions
│   ├── headerValidator.js
│   ├── bodyValidator.js
│   ├── DBConnector.js
│   └── BrokerConnector.js
├── sonarlint.json
└── sonar-project.properties
```

Not only is the concept of making them replaceable or divisible in a Domain/Subdomain concept possible during the **DDD** process, but also in a directory/file way. For the purposes of this example, I’ve used a project in Node.js.

Each operation of our Microservices had all the components that fulfilled the requirements of its development, config, Unit Testing, Performance Tests, [Contract Test](https://martinfowler.com/bliki/ContractTest.html), scheme validations, and the Controller. So treating the operation as a whole allowed us to have control when our Microservices grow too much and have to be divided. So, we pretty much had to move the whole folder to its corresponding new Microservice. But that was it — no need to try to find the right components, or try to juggle them to make it work again.

**NOTE**: We generated the API route dynamically, so each operation is self descriptive enough, along with the _package.json_ of the project, to build the route that we exposed. This allowed us the flexibility that we wanted: no more manual editing of the routes (lots of mistakes are often made here, so we wanted to avoid them). For example:

* VERB /{{Name of Artifact}}/{{Domain}}/{{Version}}/{{Subdomain}}/   
— N**ame of Artifact:** What kind of artifact are you exposing (Microservices, [BFF](https://samnewman.io/patterns/architectural/bff/), or any other)?  
 — **Domain:** Self explanatory, the domain in which the operation belongs.  
 — **Version:** Current major version that is available of our resource.  
 — **Subdomain:** The operation that our Microservices will perform **CRUD**.
* GET/Microservice/Client/v1/loan/ — GET all the loans that have been done by all the clients.

It really sounds like magic, but I do highly recommend it. You’ll see that most of the problems you have when organizing your microservices will be reduced drastically.

#### Step 5: Documentation

![Image](https://cdn-media-1.freecodecamp.org/images/exGoVYJp-DUx9jiFKEqFceDZNDu81jww0Slj)
_A brilliant comic by Dilbert, Source [Here](http://dilbert.com/strip/2007-11-26" rel="noopener" target="_blank" title=")_

Uff, I have to say, I literally had chills. I can picture all of you agile practitioners, screaming your scrum souls out. But don’t you worry, I got you covered on this.

I’ll bring two concepts to play: first and most important, since we are exposing APIs, let’s all try this **API First Development.**

> API First Development is a strategy where the first order of business is to develop an Application Program Interface putting your target developer’s interest then build the product on top of it be it a website, mobile application or a SaaS software. By building on top of APIs with developers in mind, you and your developers are saving a lot of work while laying down the foundations for others to build on top of. ([An API-First Development Approach](https://blog.restcase.com/an-api-first-development-approach/) by restcase).

And how do we build this you may ask? Here is were our second concept come to play: [**Swagger**](https://swagger.io/)**,** one of many tools to build APIs. This tool will open the gate to design and model APIs in a clean and organized way.

You can’t ask for anything better. Not only have we already solved the problem that we usually encounter in agility about documentation, but it also improves the way that the team will develop Microservices. It gives them the right tools to interact with each other, and removes the possibility that another team might say something like: “My team needed this as output, with these characteristics from this API, and we got nothing like that.” Then you can safely say: “This is the documentation of our API, designed and approved by the architect, fulfilling the requirements of the business”. Mic drop. So any further iteration would be around the well documented API.

#### Step 6: Training

As I said early on, is up to us to make the best of our developers and teams. Take your time, identify the weaknesses and improve!

![Image](https://cdn-media-1.freecodecamp.org/images/I1erhqLk-0Kgh8G-4z7xkxTfKHmfAkVFYYQR)

I know that everyone has different preferences when training their teams, but I do highly recommend [**Coding Dojo**](http://codingdojo.org/) when it comes down to agility and optimizing your team’s time. This training technique allowed us to train all of our teams so they had the same base level of expertise in each subject (Node.js, Microservices, Unit Testing, Performance tests, and more!). It also improved how the information was transmitted to the teams — we have all had play the game of telephone, and we know how it ends most of the time. No one has time to read years of documentation. We can even apply feedback from our teams to our daily lives. So everyone WINS!

### Lessons learned & final words

![Image](https://cdn-media-1.freecodecamp.org/images/1Dbzf84WYhYQC0StYhfnrNvrlwXLADAq6X2R)
_Photo by [Unsplash](https://unsplash.com/@helloimnik?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Hello I'm Nik</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

For me it’s about knowing how all the pieces that are part of your ecosystem interact with one and other. It’s about learning how to react to them, because I can assure you that one day, you will think of a solution to a problem. But then you might end it up doing something completely different just to adapt to the requirements. That is the beauty of Microservices. They allow you to be flexible, and no matter how horrible it may look, if you follow the concept of **replaceable pieces, loose coupling,** and **high cohesion**, trust me, everything will be OK.

Microservice implementation is a journey for the brave that are willing to keep improving every single day. It’s for the ones who realize which things they could’ve done better, who see the big picture and make things right.

As I said before, I wasn’t an expert when I started, and mistakes were made. But that didn’t stop me from doing things right. For all of you that out there struggling with your own Macroservices, mini-monoliths, microservice-hell, I can tell you this: Pause, take a deep breath, do your own diagnosis and improve. It’s not too late to do things right.

