---
title: How I built a replacement for Heroku and cut my platform costs by 4X
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T07:15:41.000Z'
originalURL: https://freecodecamp.org/news/how-i-cut-my-heroku-cost-by-400-5b9d0220ce13
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7BLMBLZSSgAeaxDPP9MS3A.png
tags:
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kasra Bigdeli

  You can skip to What Does it Do section if you want to get directly to the business.

  2019 UPDATE: CaptainDuckDuck is now rebranded and distributed as CapRover. See https://github.com/caprover/caprover

  The Pain

  A couple of years ago, ...'
---

By Kasra Bigdeli

_You can skip to **What Does it Do** section if you want to get directly to the business._

**2019 UPDATE**: _CaptainDuckDuck is now rebranded and distributed as CapRover. See_ [https://github.com/caprover/caprover](https://github.com/caprover/caprover)

### The Pain

A couple of years ago, I started playing with server side languages — mostly Node JS. After a few days of struggle, I was able to deploy a Hello World app on my `localhost` . It was fun, until I decided to take the next step and deploy one of my projects to the internet so people could access it from a public URL like `http://www.some-awesome-web-app.com`.

At that point, I realized that there was a whole new set of technologies that I had to learn to deploy my web app. I needed to know how to build tools and deployment pipelines, how nginx routing and SSL work, and many more things…

![Image](https://cdn-media-1.freecodecamp.org/images/hBdlbmkSkNYy0mEVC8cVeOp0uMtaWYVEGGme)

Needless to say, deployment was a painful experience. I realized that I had to spend almost the same amount of time I spent coding on deploying code to the server, building, installing dependencies, and maintaining the server. It’s simply stupid! I had to spend time doing the very same things over and over.

I’d rather spend my time coding a product/service that will be used by users, not spending hours and days on how to set up HTTPS. After all, my HTTPS is no different than other hundreds of thousands HTTPS websites on the internet. There had to be a simpler way.

### The Temporary Savior

This painful experience came to an end when I came across Heroku, a ready-to-go platform for deploying apps. I told myself “Great! This is what a deployment platform needs to be!” I loved how they abstracted all the complexity behind an easy interface. You can just create an app with a simple click and push it. It immediately becomes available with a public URL. It is available for free with a small cost of sleeping after 30 minutes of inactivity. Things couldn’t be better!

It was all good. Until I got involved with some projects that required a continuous 24hr execution (a reader bot). I had to upgrade to the paid service. It wasn’t too bad, only $7 per month. But things started going crazy after I started deploying more and more apps. Some were personal projects, and some were business-related that required either higher than 512MB (free limit) ram, or 24hr continuous availability.

It didn’t take too long until I realized I was paying $100+ to Heroku. It just didn’t make sense. Some of my reader bots that require 24hr availability consume only 128MB of RAM. Yet, I had to pay for the unused RAM as well. I couldn’t share RAM/CPU across apps. It gets worse with high RAM usage apps. If I have an app that needs 1GB of RAM — I have to pay minimum $50 per month.

![Image](https://cdn-media-1.freecodecamp.org/images/JiDh9qsFhOCgnfjVNo699m7Paz8lIqKXF4FN)

Hoping to find better deals, I started looking at AWS, Digital Ocean, Vultr, and other server providers. The pricing that I saw just simply blew my mind. On Digital Ocean, for example, I could get a server with 2GB of RAM for $20 per month. I could fit 2 instances of my 1GB RAM in that machine for $20 instead of $100. **I could cut my costs by 4x**!

There’s a catch to this cheaper price. If you don’t know what that is, you didn’t read the first paragraph, _The Pain_. The problem with using these barebones server providers (as opposed to services like Heroku) is that I have to do all the work that Heroku did for me.

### In Search for the Eternal Savior

I knew what I wanted: I needed something that turns a barebone server (such as AWS or Digital Ocean) to a Heroku-like platform. As I gained more experience, I knew there must be some sort of open-source equivalent to Heroku somewhere sitting on Github. Sure enough, I was right. There is not only one, but a ton of them.

However, after spending an hour or two with each, I realized that none of them were the truly Heroku-easy solution I was looking for. Some were super basic and just had a thin interface layer with little to no documentation. Some were extremely advanced with tons of features that didn’t use. And having those features simply meant a complicated setup process and maintenance. I was looking for an easy yet performant solution.

### Building the Eternal Savior

Since I had no luck in finding a good replacement for Heroku, I decided to build one. Luckily, all the tools that I needed were available for free — from the HTTP webserver nginx for routing requests, to Docker for containerizing applications and so on.

After a few months of planning, designing, building, deleting, and starting from scratch, the project was ready.

I released the initial version of CaptainDuckDuck in Oct 2017. It’s only been about two months and there has been a ton of positive feedbacks. After the first release, which was mainly for deploying web apps, the community asked for more. They mainly wanted the ability to deploy databases and one-click apps. Just this week, I released version 0.2.1 with all these requested features :)

### What Does It Do

My goal was to enable a typical web app developer to create a Heroku-like server instance in less than 10 minutes. I am happy to say that I did it!

You simply copy and paste one line on your server and you’ll have a Heroku of your own.

* You can deploy web apps (nodejs, php, etc…) with a simple CLI deploy command.
* You can enable HTTPS by just clicking on “Enable HTTPS” button.
* You can choose from one-click apps/databases such as WordPress, MongoDB, MySQL, Parse and others.
* You can connect multiple servers to create a cluster of servers just by entering the IP addresses and credentials of the servers in the web UI.

CaptainDuckDuck is written in NodeJS. But it’s not the NodeJS that your end users deal with. The main engines that Captain uses under the hood are nginx and docker. Both are among the most trusted, production-ready tools. The NodeJS part of the CaptainDuckDuck is only being used when deploying an app to the server. Theoretically, you can kill the CaptainDuckDuck process in your server after deployment and users won’t notice any change.

### Tutorial

If you want a complete guide, I recommend watching the [video tutorial](https://www.youtube.com/watch?v=576RsaocNUE), and reading the G[ithub page](https://github.com/githubsaturn/captainduckduck). The video was made with the first release so it doesn’t have database and one click apps. But it’s a good starting point.

![Image](https://cdn-media-1.freecodecamp.org/images/fPSXo6a50qDpqxGr8kiGaFgyh2lGphosLhYv)

![Image](https://cdn-media-1.freecodecamp.org/images/RhbupzCjT8UvQH2lu4n3vn3xAZEJGeG5oL3l)

