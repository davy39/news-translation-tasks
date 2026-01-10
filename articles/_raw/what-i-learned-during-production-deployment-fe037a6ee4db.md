---
title: What I learned during production deployment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T16:01:34.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-during-production-deployment-fe037a6ee4db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9tVtNJqSGjIiLwuA1_oelw.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: deployment
  slug: deployment
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Shruti Tanwar

  Production deployment. The final stage of every project. When all the hard work
  you’ve put in over the course of time goes live to be used by the target audience.
  It sure is an exciting time, especially when you’re part of the infras...'
---

By Shruti Tanwar

Production deployment. The final stage of every project. When all the hard work you’ve put in over the course of time goes live to be used by the target audience. It sure is an exciting time, especially when you’re part of the infrastructure setup process!

I had been part of deployment processes in the past. But this time, I got to work on a huge system in terms of volume, technology stack and infrastructure, which was an enticing escapade! I got to experience the whole process first hand and I learned quite a few things.

Here goes the list of my learnings which I’m gonna remember and apply throughout my career as a developer.

### The two P’illars: Preparation & Planning⏱️

It goes without saying that preparation and planning should be a part of anything you do. But when it comes to production deployment, it becomes a rule. It’s a given, **an imperative**. You need to know the intricacies of the technologies you have worked on in your project. You’d also need to think about what kind of infrastructure would be best suited for running different kinds of systems.

The system we built consisted of _nodejs, MongoDB, InfluxDB, redis, [asp.net](http://asp.net/), and rabbitMQ_ as part of its technology stack. One of the primary requirements of the system was to handle a huge volume of data on a daily basis. Thus the system had to go live with a proper deployment map in mind, which clearly stated stuff like:

* What kind of system/technology was supposed to run on what kind of machine
* The specifications regarding the clustering of systems
* How all these stand-alone boxes were going to talk to each other in a foolproof manner.

### Do local, think global ?

Well, this was some advice from my project architect/friend. Myself and some other young developers on the team did not have any prior experience deploying such a huge system in our careers. So our architect advised us to create a production identical system locally.

This meant that we needed to have a hands-on experience on everything. From a clustered _NodeJS_ environment (comprising of 8 clusters) and multiple server _MongoDB_ setup with a production-ready _Redis_ installation, to having production ready _pm2_ configs and environment variables!

And we documented everything. We worked up all the production setups on our local machines and then tested them end to end. Later we noted down all the steps it took to reach the final working infrastructure locally on our machines. This practice helped us find the typical problems encountered during infrastructure setup, and how we could overcome them.

We noted down all pointers, lessons, and particular tweaks which we performed to make the system working. It boosted up my confidence by several notches, and I felt ready to span out the production environment for our application.

### Document, Document, & Document!!?

I know, I know. This has been said a lot. Being a developer, you’ve heard it enough. You probably don’t want another lecture on the importance of documentation. So I’m gonna keep it short by just highlighting the bullet points:

* Production setup should be documented to bits. It needs to be neat, foolproof, and understandable.
* It should have all the system configurations, IP addresses, system specifications, and installation instructions. And also anything you consider important enough that you or a fellow developer should know.
* It needs to be updated as and when any change is made to the production environment of the system.

Being human, it’s quite common to think along the lines of, “Oh! I’m gonna remember that!” Trust me, **you won’t**. No one in the history of software development ever has (Okay, that might be taking it a little too far, but you get the idea.? )!

Document all the data & meta-data around your production setup. You’re gonna thank yourself later. Future developers who will be onboard your project will thank you subsequently!

### Monitoring & Logging ?

During the development tenure of a project, it’s comparatively easier to deal with bugs and errors. Something isn’t working? Lemme just quickly login to dev box and check. Well, that does not happen in production. You can’t login to a live system and start poking around just because you do not understand where the problem is coming from.

Setting up a proper monitoring and logging system is essential to keeping a health check on the live system. Intelligent monitoring systems are available in the market today which can give you error frequency reports, scheduled health check emails, and more.

We decided on [**_Sumologic_**](https://www.sumologic.com/) and [**_DataDog_**](https://www.datadoghq.com/) as our companions in spawning out the logging and monitoring system for our application. It was almost enthralling when I could figure out the problem in the system without doing a “ssh”.

**A decorous setup of a monitoring system goes a long way in laying a strong foundation for your live product**. Do not miss out on that!

Phew! Well, that’s a wrap! What are your findings? Feel free to share your learnings, advice, or pointers in the comments below!

