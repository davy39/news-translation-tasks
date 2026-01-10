---
title: What is Cloud Native? The Cloud Computing Delivery Model Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-19T18:12:13.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-cloud-native
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/GettingStartedWithCloudNative.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Services
  slug: cloud-services
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: "By Edidiong Asikpo\nWhenever I heard of the term “Cloud native”, my thoughts\
  \ would usually go to Kubernetes. I used to think “Cloud native” was a phrase used\
  \ for describing just Kubernetes. \nBut as I delved more into it, I realized my\
  \ assumption was w..."
---

By Edidiong Asikpo

  
Whenever I heard of the term “Cloud native”, my thoughts would usually go to Kubernetes. I used to think “Cloud native” was a phrase used for describing just Kubernetes. 

But as I delved more into it, I realized my assumption was wrong. Cloud native isn't just about Kubernetes – it is so much more!

In this article, I will help you understand what Cloud native means, how the cloud computing delivery model works, its benefits, architectural principles, and more. Let's get started.

## What is Cloud Native?

Cloud native is an approach to building and running apps that use the _cloud computing delivery model._

The “cloud” is really just the internet, as cliché as it may sound. It is a network of servers where information, software, applications, and services are housed and accessed. 

So what then is the _cloud computing delivery model_?

## What is the Cloud Computing Delivery Model?

While the above definition of cloud native is great, you need to know what all the terms mean – like “cloud computing delivery model”. I certainly wondered what it was when I saw it on almost every cloud native definition on the internet. 

First of all, it is helpful to know what cloud computing means to get a better understanding of the cloud computing delivery model.

### What is cloud computing?

According to Techopedia, 

> **Computing** is the process of using computer resources (storage, networking, and computing power) to complete a given goal-oriented task.  
>   
> **Cloud computing** offers on-demand availability of these computer resources (mentioned above) without direct active management by the user.   
>   
> The **Cloud computing delivery model** represents a specific, pre-packaged combination of IT resources offered by a cloud provider. 

There are a couple of cloud delivery models, but IaaS, PaaS, and SaaS are the most popular and widely used cloud delivery models.

### What is Infrastructure as a Service (IaaS)?

This cloud computing delivery model focuses on providing infrastructure like servers, networking technology, storage, and data center space as a service to users. 

This gives users the autonomy to decide what infrastructure is provisioned based on the different needs of their application. Popular examples of IaaS providers are Microsoft Azure and AWS. 

### What is Platform as a Service (PaaS)?

This is more focused on the development side of things by providing a _platform_ for developers to deploy their apps to the cloud.

Some well-known examples of PaaS providers are Netlify and Heroku. 

PaaS builds on top of IaaS, but unlike IaaS, it already handles the setup and configuration of the infrastructure your application needs. 

In cases where users want more control of their infrastructure configurations, IaaS is a good choice.

### What is Software as a Service (SaaS)?

This is the complete software product provided as a service to users that enables them to perform different activities. 

For example, Gmail is a great SaaS cloud native application used by millions of people worldwide. As a user of Gmail, you will most likely not be concerned about how it was built or the underlying infrastructure, but you know for sure that you can use this software to send and receive emails.

## What's the difference between Cloud Native Apps, Cloud Native Technologies, and Cloud Native Computing?

While learning about “Cloud Native”, I struggled with understanding the differences between cloud native, cloud native apps, cloud native technologies, and cloud native computing. I felt like they were all using the prefix cloud native but meant the same thing. 

In fact, if you search for “What is Cloud native” on Google, you will see over ten resources on the search result page. And out of these ten resources, 4 of them define or talk about Cloud native. The other 4 are either Cloud native applications, Cloud native technologies, or Cloud native computing. 

And to my surprise, these resources all had interchangeable definitions of what Cloud native meant, which got me confused. Was there a difference? Did these terminologies all mean the same thing?

I asked a couple of people about it and eventually understood the differences. So, here are my findings. 👇🏽

* **Cloud native** is an approach to building and running apps that exploits the advantages of the cloud computing delivery model.
* **Cloud native applications** are independent services, packaged as self-contained, lightweight containers that are portable and can be scaled rapidly based on the demand. They allow you to take advantage of the unique capabilities of the cloud.
* **Cloud native technologies** are the technologies used to build and scale cloud native applications, like Kubernetes, Helm, Docker, and others.
* **Cloud native computing** and cloud native mean the same thing. You can read the “Cloud native” definition above to understand better.  

## Cloud Native Architecture

Cloud native follows four architectural principles that help businesses ship products faster, implement their customer’s needs quickly, create value faster, and aid collaboration between developers and IT specialists.

Here are the four main principles that make cloud native architecture work:

### Microservices

In microservices, you break the code down into independent modules. Each feature is a standalone service, and resources are assigned to the services only when you need them. Cloud native apps are built following this architecture.

### Containers

Cloud native apps are packaged in containers. Containers provide isolation context for microservices making them highly accessible and easier to build, update, and scale.

### CI/CD

Cloud native applications run on a continuous delivery model. This fosters collaboration between developers and the Operations team to enables them to build, deploy, and release software faster without affecting end-users or developers in other teams.

### DevOps

Cloud native adopts DevOps as a practice to make continuous delivery and continuous integration (CI/CD) possible.

## Benefits of building cloud native apps

There are a number of benefits to building cloud native apps:

* **Independence:** Because Cloud native apps use the Microservices architecture, it's possible to build cloud native apps independently of each other. This gives you the opportunity to build, manage, and deploy the different components of an application independently without affecting other components.
* **Automation:** Cloud native apps run on a continuous delivery model making it possible to ship software updates immediately.
* **No downtime:** Thanks to container orchestrators such as Kubernetes, you can deploy a software update with essentially zero downtime. If an instance of the application goes down, Kubernetes will automatically spin up another one for you immediately.
* **Scalability:** Cloud native apps enable flexible deployment options across the network making it easier to develop, deploy, and iterate on the application.
* **Standards-based:** Most cloud native services follow a set of standards championed by the [CNCF](https://www.cncf.io/) Open Source organization. These standards have been vetted and approved by the community and are used by some of the biggest tech companies across the world. This helps reduce vendor lock-in and ensure that apps are built in the right way.

## Summary

I hope you enjoyed reading this article. If you want to learn more about Cloud native, here are some useful resources for further reading:

* [Cloud Native 101](https://www.youtube.com/watch?v=9Ik96SBaIvs), VMware.
* [How to start your Cloud native Kubernetes journey](https://blog.getambassador.io/how-to-start-your-cloud-native-kubernetes-journey-ee88585d9ff3), Ambassador Labs.
* [Understanding cloud-native apps](https://www.redhat.com/en/topics/cloud-native-apps), Red Hat.
* [Cloud-Based, Cloud-Native, and Cloud-Enabled apps—What's the Difference?](https://www.papertrail.com/solution/tips/cloud-based-cloud-native-and-cloud-enabled-applications-whats-the-difference/), PaperTrail.
* [What is Cloud Native?](https://www.oracle.com/cloud/cloud-native/what-is-cloud-native/), Oracle.
* [What are Cloud Native applications?](https://tanzu.vmware.com/cloud-native), VMware. 

If you have any questions, you can ask me on [Twitter](https://twitter.com/Didicodes).

  

