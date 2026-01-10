---
title: 'An intro to Amazon Fargate: what it is, why it’s awesome (and not), and when
  to use it.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T19:14:00.000Z'
originalURL: https://freecodecamp.org/news/amazon-fargate-goodbye-infrastructure-3b66c7e3e413
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-5KIBlv5vzflb1zgsu9WJg.jpeg
tags:
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: fargate
  slug: fargate
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Emmanuel Marboeuf

  When Amazon announced Fargate in late 2017 at AWS re:Invent (along with EKS) it
  really fell under the radar. None of the blogs or influencers that I was following
  at that time really talked about it other than something along the...'
---

By Emmanuel Marboeuf

When Amazon [announced](https://www.youtube.com/watch?v=8i82i9QYUGs) Fargate in late 2017 at AWS re:Invent (along with EKS) it really fell under the radar. None of the blogs or influencers that I was following at that time really talked about it other than something along the lines of:

> Oh yeah and there is this new thing that will allow ECS users to run containers directly in the cloud.

As a developer, that really blew my mind. **Let’s see why.**

### The productivity boom

I feel like there have been **five** major revolutions in the software development world that dramatically increased developers’ productivity and ability to write and deploy production level applications with maximum efficiency.

They all solved major issues, too. Here’s my breakdown of revolutions and the issues they solved:

* Emergence of Cloud Services (IaaS)  
**Infrastructure cost and scalability**
* Open source community, Conferences , Workshops, Tech Blogs, Stack overflow, and so on   
**Limited access to knowledge**
* Versioning systems, Collaboration tools, Continuous integration tools   
**Concurrent engineeringSystems discrepancy and integration hell**
* Containerized architecture  
**Difficulty in building applications across inconsistent environments**
* Serverless Computing Services (PaaS)   
**Servers and systems administration**

Each and every one of these revolutions has one common trait: they all give **more** **control to software engineers.** They do this by encouraging good practices and code sharing with a collaborative workflow, and they lower the need for expensive dedicated servers, System administrators, DevOps, IT support, and so on.

Great, but wait — where is **Fargate** in all this?

### Your ship is the issue

![Image](https://cdn-media-1.freecodecamp.org/images/1*o5kiw7FwodkMegfRDNfktg.jpeg)
_Life jacket is advised_

See, when Docker brought containers to the masses, it quickly became a new standard in development and was widely adopted.

Soon after, and following the success of **Kubernetes**, AWS launched their own (more basic) container management service: Amazon Elastic Container Service (ECS). It introduced the concept of Tasks.

A task can be any instance of containers working together. From a web application that runs a web server, several micro services, a database and a reverse proxy, to a list of shell script batches that will run periodically.

Being an early adopter of ECS, I really liked it and it worked great for a while. But eventually, having to manage these **extra layers** (Tasks and containers) instead of just EC2 instances became more and more complicated.

I also wasn’t comfortable with its **security**. The more layers you have in your stack, the more you have to be vigilant. Each of these layers brings about more complexity along with the increased likelihood of security misconfigurations and vulnerabilities.

Indeed, with ECS your containers are running in **EC2 container instances in a cluster** that you will configure for auto-scaling. Each instance can host multiple different tasks. Each task can run multiple containers.

Because your tasks will be deployed randomly (by default) on the same kind of **EC2 instances with available resources**, you face the following issues:

* One cluster follows the same rules for auto-scaling and automatically provisions the same kind of EC2 instances.
* Some containers will need totally different resources but still have to work together.
* Some containers don’t necessarily follow the same rules for autoscaling.
* Sometimes several containers in the same task need their own load balancer, and having multiple load balancers for the same task is not possible.

The preferred workaround when facing these issues was to:

* manually deploy some of your instances with different resources based on need
* attach these instances to your cluster
* run one container by task
* link your EC2 instances manually together
* write complex strategy placement constraints on ECS to make sure the right task was on the right machine that had the appropriate resource depending on what it did

That is a **lot** of work, it’s pretty **tedious**, and it’s **hard to maintain.** And it kind of defeats the purpose of working with containers in a first place.

Someone had to come up with a better idea.

### Let them float

As it turns out, the AWS team had the same issues. They thought about it for the past year, and worked on solving the problem below:

> How could we run containers without having to worry about servers and clusters?

**And this is what AWS Fargate is about**. It completely abstracts the underlying infrastructure, and you see each and every one of your containers as a single machine.

You just have to specify what resource you need for every container and it will do the heavy lifting for you. You don’t have to manage multi-layered access rules anymore. You can fine tune the permissions between your containers like you would do between single EC2 instances.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aLMrzsEK-E9EGIjxXvQ48Q.jpeg)
_containers on Fargate (artist rendering)_

It’s like your containers become the ships with their own sail, rudder, and crew and are able to float to their destination on their own.

### Containers as a Service (CaaS)

I actually believe that **Containers as a Service (CaaS) is the real PaaS** that developers have been awaiting for years. It allows developers to deploy their containers directly in the cloud without having to worry about everything in between.

Of course there are already a lot of technologies out there that allow you to run your code seamlessly on the cloud without having to worry about scale or server administration (like the amazing **Heroku**, **Lambda,** or even in its own way **Google app engine)**. But all have limitations.

* You have to choose between losing a bit of flexibility
* You have to stick to the supported languages
* You can’t use the supported languages because your project needs a native low level library that’s only available on very specific systems
* Your project uses a cutting edge technology that won’t be available to the masses in the next few years
* Some of these platforms are very (very) expensive, especially when scaling up

**Fargate (Or CaaS)** brings you the best of both worlds.

**Containerized architecture** brings you the flexibility and control that you need. It allows you to use **any kind of technology** running in **any** **kind of system** you want. The container aspect will ensure that you will have the same behavior on every host, whether it’s a dev, testing, staging or prod environment.

I find this point critical for a lot of tech startups. In fact, sometimes one of your competitive advantages is the use of a state-of-the-art technology that you’ve participated in developing, or the smart re-use of another one in a totally new and revolutionary context.

**Serverless deployment** allows you to focus on writing great code. No provisioning, easy scaling.

### Limits

#### CaaS vs PaaS

It is true that you are giving up some cool aspects of real PaaS. Yes you will still have to **manually update** your container’s images, and sometimes you’ll have to write your own Docker images. This can be a struggle at first if you don’t know the basics of **system administration**.

But, it also means that you can do pretty much anything you can think about and have complete **flexibility and freedom** in the systems, languages, tools, libraries, and versions that you want to use.

#### Cost

Let’s face it, Cloud services (IaaS) are **more expensive** than having your own infrastructure (if you could scale it up and down on demand). For the same reason, not having to provision, manage, and scale your servers has a cost. It might not be the best solution yet for some of your simplest use-cases.

Let’s hope they are going to work on **bringing the cost down.** As good as the product is, it’s hard to justify almost 4 [times the price of an on-demand](https://aws.amazon.com/fargate/pricing/) equivalent EC2 instance (for t2.medium for example).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_GhNwtmR-m63DOx6b9GXDg.png)
_Comparison Fargate and EC2 prices in USD_

### Should I switch all my ECS tasks to Fargate ?

Not yet. As stated above, you are going to more than triple your costs in some cases. Until they bring the cost down, you may be better off using standard EC2 instanes.

However, Fargate may be more beneficial for you in the following use-cases:

* If you have trouble auto-scaling your ECS tasks efficiently and often end up with a lot of unused **CPU or Memory**. With Fargate, you **only pay for the resources that you have defined in your tasks**.
* For your tasks that will run **on demand or on a schedule** and don’t need a dedicated EC2 instance. With Fargate, you **only pay when your task is running.**
* For your tasks that have **peaks Memory and/or CPU usage**. Just because it will save you the time and hassle of the configuration and management of such cases.

### Bonus

For those who prefer **Kubernetes** over **ECS**, Fargate will soon be able to run [Elastic Container Service for Kubernetes](https://aws.amazon.com/eks/).

