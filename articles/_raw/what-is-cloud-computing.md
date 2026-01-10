---
title: What is Cloud Computing? Introduction to the Cloud for Beginners
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2024-01-03T21:40:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-cloud-computing
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/cloud-sky.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
seo_title: null
seo_desc: 'As the digital landscape continues to evolve and technology marches forward,
  cloud computing has remained an important topic for developers to learn.

  You''ve probably encountered cloud requirements in job listings, heard people talk
  about it in conver...'
---

As the digital landscape continues to evolve and technology marches forward, cloud computing has remained an important topic for developers to learn.

You've probably encountered cloud requirements in job listings, heard people talk about it in conversations, or seen ads by companies offering cloud services – and now you're interested in learning more about it.

In this article, I'll demystify the cloud for you, breaking down complex concepts into easy-to-understand bits. 

Here's what we'll cover in this article:

* [The World Before Cloud Computing](#heading-the-world-before-cloud-computing)
* [What Is Cloud Computing?](#heading-what-is-cloud-computing)
* [Cloud Service Providers](#heading-cloud-service-providers)
* [Different Cloud Services](#heading-different-cloud-services)
* [Challenges that Cloud Computing Helps Solve](#heading-challenges-that-cloud-computing-helps-solve)
* [How Can Cloud Computing Help You?](#heading-how-can-cloud-computing-help-you)
* [Cloud Deployment Models](#heading-cloud-deployment-models)

So let's dive in and learn cloud computing basics so you can start your journey into this growing field.

## The World Before Cloud Computing

To understand cloud computing, it is important to understand the problem cloud computing tries to solve. This will help you understand its history and appreciate the convenience it brings into the world of technology.

Before the cloud, deploying web services was a very expensive process. To deploy a web application, you had to purchase servers with the correct amount of storage and memory, keep them on-site, setup these servers, and use them to host your application. 

This comes with many additional costs, other than the original server costs, like electricity and the data required to keep your server up and online every time. There are also security concerns, as you'll need to prevent your server from being damaged or stolen by bad actors. 

Beyond all this, many developers are not exactly server specialists. So you would either have to train your developers to become system admins or hire system admins to setup and configure the servers to work with your applications. Then to deploy a new application, you'd have to repeat the whole process with new costs.

Scaling applications wasn't easy before the cloud. If you tried to manage costs and not buy too many servers, or hire many system engineers, you might end up with insufficient compute power and you'd need to scale. Scaling means buying more servers (or replacing existing ones with better ones), configuring them to match existing configurations, and deploying your applications on them. 

These are some of the issues we faced before cloud computing. Now, you might wonder, "how does cloud computing solve these?". Let's find out.

## What Is Cloud Computing?

> **Cloud computing** is the on-demand availability of computer system resources, especially data storage (cloud storage) and computing power, without direct active management by the user.   
>   
> Cloud computing relies on sharing of resources to achieve coherence and typically uses a pay-as-you-go model, which can help in reducing capital expenses but may also lead to unexpected operating expenses for users. – [Wikipedia](https://en.wikipedia.org/wiki/Cloud_computing)

Think of Cloud Computing like renting a computer from a cybercafe. In a cybercafe, they have the computers ready for use – you just come in, pay for your desired time, and use the computer for that period. 

In the case of cloud computing, you don't have to worry about buying the computer, or protecting it, or covering the running costs. The cloud provider covers all these worries. You rarely ever have to worry about software issues, or the absence of specific software on these computers. And the best part? You only pay for the computer you use, and only for the time you use it.

So in more relatable terms, say you have a web application to deploy. You go to a cloud service provider, select specific server requirements your application requires, select software dependencies, and deploy your application, with zero worries.

Cloud computing as explained to a five year old is _"letting someone else manage your computing needs"_. You have some website that you need to put online, or maybe a mobile app, or some other piece of technology, and instead of having to buy servers to deploy it, someone else buys and sets up the servers. You simply upload your files. Its almost the same as renting an apartment, but now you are renting compute space on another computer.

## Cloud Service Providers

Companies that provide these cloud services are called cloud services providers. These companies already have many servers, and system engineers. They're concerned with all the stuff you don't have to worry about like server costs and running costs. They provide a web interface where you can access their servers and use them when you need. 

Currently, the most popular cloud service providers are Google (Google Cloud Platform), Amazon AWS (Amazon Web Services), and Microsoft (Azure). These companies offer similar services, but with various different price models, features, and so on. 

Here's a summary of what each of them offers:

### Google

They offer IaaS (Compute Engine), Containers As A Service, CaaS, (Kubernetes Engine), and PaaS (App Engine) services. They also offer data storage services, with tools like Google Cloud Storage, Cloud SQL, and Cloud Bigtable. 

### AWS

This is the first cloud services provider. They offer IaaS (Elastic Compute, EC2), CaaS (Elastic Kubernetes Service, EKS)  and PaaS (Elastic Beanstalk) services. They also offer data storage services, with tools like Amazon S3, and DynamoDb.

### Microsoft

They offer IaaS (Virtual Machine), CaaS (Kubernetes Service, AKS), and PaaS (App Service) services. They also offer data storage services, with tools like Cosmos DB.

To maximise resources, cloud service providers have their clients sharing servers. The clients don't have to know or worry about this allocation.

Now let's understand what some of the above acronyms/terms mean so you have a better idea of what these cloud services are.

## Different Cloud Services

Cloud service providers offer plenty of different computing services. Here are the most common services:

### SaaS (Software As A Service)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/saas-778x445.jpeg)
_[Geek Super](https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fgeeksuper.com%2Fadvantages-of-saas-platforms-for-online-courses%2F&amp;psig=AOvVaw0J54lC0WsxXAoS0L2czE27&amp;ust=1652833369985000&amp;source=images&amp;cd=vfe&amp;ved=0CA0QjhxqFwoTCIDvwOio5fcCFQAAAAAdAAAAABAO)_

This service involves you just using some software without any knowledge of its source code or host environment or development details. You just use it and trust that it's being managed and updated properly.

### PaaS (Platform As A Service)

Here, you focus only on your application development as everything has been handled (the hardware, computing environments, and required software).

### IaaS (Infrastructure As A Service)

This is the most flexible of all cloud services. Here you have the most control over things. You can customise and change things as you see fit. 

But you don't own the servers. The cloud service provider only provides you with the infrastructure you need, and you are responsible for creating your own computing environments and installing required software for your application to work.

The idea here is similar to buying hardware. The only difference is that now, you're renting it and it's virtual (to you).

## Challenges that Cloud Computing Helps Solve

Cloud computing removes the need to purchase and setup servers on-site every time a new application needed to be developed. This is a great advantage as it saves companies a lot of money – both on servers, as well as on the engineers who would setup and configure the servers to work for your applications.

Scaling isn't usually easy as it often involves a lot of setup and configuration. For example, to provide more storage for an application, you could get an external data store and connect to the current server. This definitely has its limits, though. 

A point will likely come when you need a better server, or an additional server. Either way, every software that you installed to get it running on the former server would have to be installed again on the new server. Application files would have to be moved, and so on.

Also, these applications are often underutilising these hardware resources. This, from the business perspective, is a loss. An initial fix to this was virtualisation. This basically meant creating virtual (contained) environments where the application has all of its required software and can function well on the servers. These led to better utilisation of resources. But it definitely wasn't the perfect solution. 

## How Can Cloud Computing Help You?

Cloud computing offers plenty benefits, some of which are highlighted here:

* It is cheaper to pay a subscription than to build a whole datacenter. You have plans that let you use only what you use.
* Scaling and management are responsibilities of the cloud service provider.
* Easy setup. Developers get to just focus on the code as all the actual server and hardware setup can be done using a user interface provided by the cloud service provider. This leads to faster development time, and applications are shipped faster.
* Accessibility. Cloud service providers tend to have multiple datacenters around the world, making sure your users always get access to your services as fast as possible.
* Data security. Because your data is not stored in your physical space anymore, it's more difficult for bad actors to come in and damage or steal your servers.

## Cloud Deployment Models

A cloud deployment model determines where your data (and applications) is stored and how your customers interact with it.

### Public cloud

Here, everything is handled by the cloud service provider. It's the most popular model. When using a public cloud, you're not concerned about the server maintenance, and you're sure of high reliability and the possibility of unlimited scalability. This usually means you share servers with other people. 

It is the cheapest model, and companies usually use a pay-as-you-go model (so you never have to commit too much upfront financially). 

A potential issue with this is, having everything handled by the cloud service provider means you have little or no control over the services.

### Private cloud

This is similar to the traditional ways of hosting applications. Here, you do have your own data centers. This means that only you get to use the servers and have unlimited control over them. 

Now, the difference is, you provide a self service interface to users of your servers, usually developers in your company. You still have to manage the physical servers, and you're responsible for their maintenance and scaling.

This method can be more secure than the public cloud, as you have control and can setup as much security as possible. It also comes in very handy if you have data that must not get out due to compliance requirements.

But this method is way more cost intensive, although with a more predictable or fixed pricing model. These servers and hardware are expensive. Having them means having someone to manage them, which means more expense. Scaling also means buying new devices every time. 

### Hybrid cloud

![Image](https://www.freecodecamp.org/news/content/images/2022/05/What-is-Hybrid-Cloud.jpeg)
_Hybrid Cloud | [W3Codemasters](https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fw3codemasters.in%2Fwhat-is-hybrid-cloud-benefits-of-a-unified-hybrid-cloud-platform%2F&amp;psig=AOvVaw3ekfLv5gwNG2kjXGoFfWA4&amp;ust=1652833178148000&amp;source=images&amp;cd=vfe&amp;ved=0CA0QjhxqFwoTCPj5qKKp5fcCFQAAAAAdAAAAABAI)_

This approach merges both the public and cloud methods. It basically allows you more flexibility. You get to use public services, and also setup your own when you need to. Here you're able to comply with regulations, through your servers, and also offer high accessibility, through a cloud service provider. This method is perfect for organizations trying to migrate from one model to another, keeping the business operation during the transition.

An example application of this would be hosting an application on a public cloud and connecting it to a database on a secured private cloud.

This method is also more expensive than the public cloud as you do have to cater for some of the servers. It could also get complicated as data gets distributed between multiple servers and applications.

### How to Choosed a Deployment Model

The choice between public, private, or hybrid cloud deployment models depends on an organization's unique requirements. 

* Public clouds offer cost efficiency and global reach
* Private clouds provide enhanced security and control
* Hybrid clouds offer flexibility and a strategic balance between the two.

The decision ultimately hinges on factors such as security needs, compliance requirements, scalability, and the level of control desired over the IT infrastructure.

## **Conclusion**

Now you should have have enough information to kickstart your career in cloud computing.

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

