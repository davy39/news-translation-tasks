---
title: How to know if Kubernetes is right for your SaaS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T11:29:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-know-if-kubernetes-is-right-for-your-saas-315dfffe0a25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tJXXWOYkuMF3RkqZxMmvFw.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: SaaS
  slug: saas
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ben Sears

  Kubernetes is an awesome technology, and I personally have seen great gains in my
  ability to scale, deploy, and manage my own SaaS because of it. But, not everyone
  would immediately benefit from adopting it for a number of reasons:


  Lack...'
---

By Ben Sears

Kubernetes is an awesome technology, and I personally have seen great gains in my ability to scale, deploy, and manage my own SaaS because of it. But, not everyone would immediately benefit from adopting it for a number of reasons:

* Lack of familiarity with container technology
* Application architecture not being conducive to utilizing the benefits of Kubernetes
* Increased amount of effort versus time spent

If you are interested in Kubernetes but aren’t sure about investing the time/resources needed, this article is for you.

### What is your experience with containers? ?

In order to understand what Kubernetes can do for you, you first need to know what benefits containers provide. Before spending time on Kubernetes you should first:

#### Containerize your application

![Image](https://cdn-media-1.freecodecamp.org/images/AZhfT1f8jS0KnbLrYz7QXj1LYdXd9pADqp2r)

First and foremost, your application must be containerized. This means defining the steps needed to take a base OS image and install your application on it in a file (usually a Dockerfile).

Going through this process as well as defining environment variables needed to configure your application (such as the URL, username, and password of the database your app uses) will be critical to making your container image usable by Kubernetes.

Also make note of any dependencies your application needs to function and learn how to use the containerized versions of those.

#### [Understand how storage works](https://docs.docker.com/engine/admin/volumes/)

Containers are designed to hold only the code needed to run an application. Any persistent data needs to be stored elsewhere, as the process of tearing down and spinning up containers (very common when dealing with containers) also destroys any data stored within the file system of that container.

Knowing how container storage is supposed to work and how to handle things like backing up data, moving that data between containers, and accessing the data from outside the container is very valuable when considering Kubernetes.

Kubernetes makes storage management easier with features such as auto-provisioning. This has the ability to have your storage provider (such as AWS EBS) create new volumes on the fly as new containers are created, automatically mounting them.

#### [Understand how networking works](https://docs.docker.com/engine/userguide/networking/)

How you implement networking can play a large role in how you use Kubernetes. Knowing how to open specific systems to the public internet and hiding others, such as databases, while maintaining communication between services is important to understand for starters. Some more complicated operations which I’ve needed to learn were how to integrate load balancing as well as giving each customer’s instance a custom hostname (things which Kubernetes makes a lot easier).

### Does Kubernetes solve problems you are currently facing? ?

![Image](https://cdn-media-1.freecodecamp.org/images/zqFzeEAsKrXpWWtkZBdh-ju7DgxgV4-RvEcz)

If you are not using containers to deploy your application, you probably shouldn’t be using Kubernetes yet. The problems Kubernetes aims to solve are problems that arise when you try and scale a container-based infrastructure.

Here are a few of the problems I think Kubernetes is great at solving when trying to deal with containers at scale.

#### Scaling up resources

Kubernetes is basically a cluster of nodes which provide compute resources that can be consumed by container workloads. This clustered architecture allows for a very easy scale-up or scale-down of resources. You just add or a remove nodes from the cluster, and Kubernetes will automatically utilize those resources or reassign workloads on your existing resources.

This solved a major problem I faced, because I went from having a single server I had to keep scaling up (an annoying manual process) to having the ability to scale up or down my infrastructure with a single command using the CLI.

#### Performing mass updates

Another problem that Kubernetes solves is the ability to update all your containers. Before, I was writing shell scripts which would pick each relevant container and recreate it using a new image tag. The process would take over an hour, and I had no way of validating that the update was successful. With Kubernetes I was able to perform an update with a single command as in the example below:

```bash
// Update all the pods of frontend to a new image tag
$ kubectl rolling-update frontend --image=image:v2
```

Kubernetes also allows you to update any part of Kubernetes (networks, storage, etc.) with commands based on any criteria. This is a huge step up from writing your own scripts to enact changes to your infrastructure.

#### Self-healing

The last and one of the most important pieces of Kubernetes I’d like to talk about is the ability to self-heal. If Kubernetes detects something wrong with part of its infrastructure, such as a node not responding or a container not passing its health check, it will perform steps to recreate those parts of itself until things start working again.

This is extremely useful because if a piece of the cluster goes down for any reason, the workload will be reassigned and you can even have Kubernetes recreate entire servers to fix the problem.

### Will your application architecture need to change??

![Image](https://cdn-media-1.freecodecamp.org/images/I0-fuTV0uXQR1xoGvWjcyCI-eDJLgJlkrxHZ)
_Sometimes adapting your app to Kubernetes is like fitting a square peg in a round hole_

When I migrated to Kubernetes, there weren’t that many changes I had to make because it was originally architected to be a multi-instance platform deployed via containers.

Here are some of the things I’ve learned while moving my own workload to Kubernetes.

#### Startup time of your app is important

When you create a new deployment, you have to wait for your app to start before it becomes available to the end-user. This becomes a problem if your deployment process involves creating new instances when an end-user presses a button or if you are performing updates on all your customers instances, as that requires a rebuild of the pods.

When moving to Kubernetes you may need to make some changes to your codebase to make the startup process more efficient so the end-user doesn’t have a degraded experience using your product.

#### Adapting multi-tenant architectures is difficult

A multi-tenant architecture means you have a single instance of your application which manages all your end-users in partitioned tenants, usually with a single database being shared between everyone.

If your application is not built to utilize clustering (multiple servers acting as a single instance) you should not be using Kubernetes yet.

Generally I see two types of architectures when working with Kubernetes:

* Multi-instance with one instance of the app for each customer
* Multi-tenant architecture with clustering capabilities as they can utilize scaling up and down resources

I personally prefer multi-instance because they are much easier to implement compared to a clustered multi-tenant architecture. Also, the work involved in moving from multi-tenant to multi-instance isn’t too bad compared to adding cluster capabilities to a multi-instance architecture.

#### Moving to a stateless application is a large amount of effort

One of the great features of Kubernetes is the ability to scale up or down the number of pods in a deployment. But, if your application is not clustered or not stateless, this functionality is wasted since extra pods in a deployment wont be configured properly and can’t be utilized.

The process of utilizing statelessness in Kubernetes is often more trouble than it’s worth, since most times you will need to completely rework the way you handle configurations within your application.

Don’t be discouraged if you don’t want to spend the time to make your application stateless or clustered as there are many ways of adapting stateful deployments to use Kubernetes. But those have their own problems which I will not get into in this article.

### Should you adopt Kubernetes? ?

After asking yourself these questions, you should have a pretty good idea if Kubernetes will be a good fit for you at this time. Most early stage startups are probably not going to need it, and more mature ones may have a lot of investment in other technologies so it wouldn’t be feasible to switch.

I think the best case for someone moving to Kubernetes is a startup looking to move from having a Minimum Viable cloud infrastructure that is using containers to power production workloads to something more stable. That was my case, and I can say I went from having periodic downtimes due to resource mismanagement and overworked servers to not having to worry at all about my infrastructure thanks to the power of Kubernetes.

Looking to connect Kubernetes to your SaaS? Lets talk - [ben@servicebot.io](mailto:ben@servicebot.io)

![Image](https://cdn-media-1.freecodecamp.org/images/Doj-pHbdszxakMEVRnRFpJmZdW8nkJmsKoXo)

