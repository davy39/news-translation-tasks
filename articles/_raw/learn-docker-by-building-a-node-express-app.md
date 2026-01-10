---
title: Learn Docker by Building a Node / Express App
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-04-29T20:05:04.000Z'
originalURL: https://freecodecamp.org/news/learn-docker-by-building-a-node-express-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/dockerdevops.png
tags:
- name: Docker
  slug: docker
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Docker is an open source project that makes it easy to create containers
  and container-based apps. Docker''s lightweight and portable software containers
  simplify application development, testing, and deployment.

  We just released a course on the freeC...'
---

Docker is an open source project that makes it easy to create containers and container-based apps. Docker's lightweight and portable software containers simplify application development, testing, and deployment.

We just released a course on the freeCodeCamp.org YouTube channel that will help you learn the core fundamentals of Docker by building a Node/Express app with a MongoDB and Redis database.

Sanjeev Thiyagarajan developed this course. Sanjeev has a ton of experience working with Docker and he is thoroughly qualified to teach this course.

First, you will learn how to use a single container. Gradually you will add more complexity to the app by integrating a MongoDB container and then finally adding in a Redis database for authentication.

You will learn how to do things manually with the cli and also how to use Docker compose. The course focuses on the challenges of moving from a development environment to a production environment. You will learn how to deploy with a Ubuntu VM as the production server and utilize a container orchestrator like Docker Swarm to handle rolling updates.

Here are the sections in this course:

### Part 1: Introduction

* Intro & demo express app
* Custom Images with Dockerfile
* Docker image layers & caching
* Docker networking opening ports
* Dockerignore file
* Syncing source code with bind mounts
* Anonymous Volumes hack
* Read-Only Bind Mounts
* Environment variables
* loading environment variables from file
* Deleting stale volumes
* Docker Compose
* Development vs Production configs

### Part 2: Working with multiple containers

* Adding a MongoDB Container
* Communicating between containers
* Express Config file
* Container bootup order
* Building a CRUD application
* Sign up and Login
* Authentication with sessions & Redis
* Architecture Review
* Nginx for Load balancing to multiple node containers
* Express CORS

### Part 3: Moving to Prod

* Installing docker on Ubuntu(Digital Ocean)
* Setup Git
* Environment Variables on Ubuntu
* Deploying app to production server
* Pushing changes the hard way
* Rebuilding Containers
* Dev to Prod workflow review
* Improved Dockerhub workflow
* Automating with watchtower 
* Why we need an orchestrator
* Docker Swarm
* Pushing changes to Swarm stack

Watch the full course below or [on the freeCodeCamp.org YouTube channel](https://www.youtube.com/watch?v=9zUHg7xjIqQ) (5-hour watch).

%[https://www.youtube.com/watch?v=9zUHg7xjIqQ]


