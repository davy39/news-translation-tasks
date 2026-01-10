---
title: How I select AWS services for running my apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T16:20:23.000Z'
originalURL: https://freecodecamp.org/news/how-i-select-aws-services-for-running-my-apps-14e3abb7c56a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q3V3mcHYJdMAoV_bkkQj8g.gif
tags:
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Peter Mbanugo

  Choosing which AWS service to use for running your application might be somewhat
  confusing to some of us. Even for the experienced, it may take some time to make
  a decision. Perhaps you are new to AWS, and you may still need to under...'
---

By Peter Mbanugo

Choosing which AWS service to use for running your application might be somewhat confusing to some of us. Even for the experienced, it may take some time to make a decision. Perhaps you are new to AWS, and you may still need to understand the what and why of the various AWS services. Or you might know how to use AWS, but it still takes you longer because you don’t have a process to facilitate easy selection. Let me show you how I do this and the process I follow.

### A look at the process

When you’re selecting what service to use for running an application, try to answer the following questions.

### Question 1: How much control do I need?

When answering this question, I decide what I want to have control over versus what I’d like to leave to AWS.

I choose if I want to control which operating system (OS) it’ll run on, how the network is configured, the server, the application code, and its configuration.

But with more control comes great responsibility. For example, if I’m in control of the OS, I’ll be responsible for updating it, securing it, and configuring what is exposed to the public network.

The different cloud computing options give you control and responsibility. Let’s look at these options and what we can control.

#### Option 1: Infrastructure as a Service (IaaS):

IaaS computing provides you with the highest level of flexibility and management control over your IT resources. It provides access to networking features, computers (virtual or on dedicated hardware), and data storage space. Use this option if you want to be in control of the bare metals running your app and handle all the responsibility for the following:

1. Application configuration
2. Application code
3. Server maintenance and configuration
4. Operating System
5. Antivirus
6. Network

Services available as IaaS are:

1. Elastic Compute Cloud (EC2) Instances
2. Amazon Lightsail
3. EC2 Container Service (ECS)
4. Elastic Container Service for Kubernetes (EKS)
5. AWS Batch

#### Option 2: Platform as a Service (PaaS)

PaaS computing removes the need for you to manage the underlying infrastructure (hardware, OS, networking). With this, you focus on creating and running applications, rather than constructing and maintaining the underlying infrastructure and services. Use this option if you want to control:

1. Application configuration
2. Application code
3. Server configuration

while leaving other responsibilities to AWS.

Services available as PaaS are:

1. Elastic Beanstalk
2. Mobile Hub

#### Option 3: Functions as a Service (FaaS)

FaaS computing provides you with the ability to deploy code, and set the configuration needed to run the code. You leave it to AWS to handle the underlying infrastructure and networking. Use this option if you want to control your application logic and configuration.

Also, another important reason to use it is if the application will run occasionally. That is, not always on and running, unlike the applications in the other types of cloud service offerings.

Services available in this category are:

1. Lambda
2. Step Functions

### Question 2: How will users use the app?

Another question to consider is knowing how users will use the application.

1. **Will it be always on and running, waiting for input/data to process?** Even if no input/data/request comes in, it’ll just be idle, consuming server resources and infrastructure.
2. **Will it run only when needed?** In this case, the application starts when it has a request or data to process and stops when completed.

If my application usage model satisfies question **1**, then I’ll need to use the classic model for running applications. I could use EC2 instances, ECS, or Elastic Beanstalk. If it satisfies question **2**, I’ll run with Lambda.

Sometimes we want to run background tasks. They will vary based on how long they run and how many resources they will need to run well. When faced with this problem, I will pick between using Lambda and Batch. I’ll go for Lambda if I need a task to run within the maximum allowable processing time that doesn’t require more resources than Lambda can provide. If it’s the opposite of this, I’ll go with Batch.

These two questions help me in my process of picking a service in AWS. The table below shows how to choose by answering more specific questions and knowing which services meet the criteria.

#### Selecting an IaaS product

![Image](https://cdn-media-1.freecodecamp.org/images/h62U5mxevaQkMn2X46D60gVvOk5cy4fjE3YJ)
_selecting IaaS services_

#### Selecting a PaaS product

![Image](https://cdn-media-1.freecodecamp.org/images/4oqXOGAm8OBOELjP5kMpvgot1g4tuACufMpK)
_selecting PaaS services_

#### Selecting a FaaS product

![Image](https://cdn-media-1.freecodecamp.org/images/7TjqbgkFajgcXK17OSfN4pSp4X2cVeSfnp-1)
_selecting PaaS_

The steps above should guide you and allow you to make your decisions more quickly and easily, so I hope you found them useful.

This is my process, and it’s likely to change in the future, but I’ll try to keep this post updated. I’ve left out some services relating to data/storage, which I’ll be sharing in a future post.

Please leave a comment if you would like to share your thoughts, or correct something you think I’ve got wrong. I’ve learned some of these steps from my friend [Barry Luijbregts](https://twitter.com/AzureBarry).

> _Peter is a Software Developer, tech writer, and maker of Hamoni Sync. He currently works with Field Intelligence where he helps build logistics and supply chain apps. He also gets involved in design research and customer support for these products. He’s also a Contributor to Hoodie and a member of the Offline-First community_

