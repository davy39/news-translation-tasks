---
title: 'Serverless vs Fully Managed Services: What''s the Difference?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-03T16:51:37.000Z'
originalURL: https://freecodecamp.org/news/serverless-fully-managed-service-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cloud-pic.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Periklis Gkolias

  If you''re new to cloud technologies, you might be confused about the difference
  between serverless technologies and managed services.

  So in this article you''ll learn what these terms mean and what the main differences
  are.


  What A...'
---

By Periklis Gkolias

If you're new to cloud technologies, you might be confused about the difference between serverless technologies and managed services.

So in this article you'll learn what these terms mean and what the main differences are.

![Clouds. Credits to Zbynek Burival](https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80)


## What Are Managed Services?

A managed service let the end-user focus on *using* a service rather than *setting up* the service. 

Now, this doesn't mean that the cloud provider can read your thoughts. Rather, any input the service requires happens via a user-friendly form. 

Managed services fit into the category of PaaS products (Platform as a Service).

One of the most famous managed services around is Amazon's [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/). In ElasticBeanstalk you can 
a) set up some parameters 
b) provide a Docker image

and the service will set up the rest for you. It will handle things like:

- Virtual machines
- A webserver (if needed)
- Exposing your application to the public
- Monitoring and logging infrastructure
- Semi-automated configuration
- Load balancing
- Scaling 

And more.

You will be able to see the results of the Elastic Beanstalk operation, for example the virtual machines that were bootstrapped, as a result. 

Usually, you won't be able to access and fiddle around with them. Otherwise, it is not a managed service – you are the manager.

![AWS ElasticBeanStalk](https://cdn-images-1.medium.com/fit/t/1600/480/1*Fd6rk1k1FHPZcg4aK_OXtQ.png)

So a managed service is essentially an abstraction of a...non-managed service. The abstraction is usually interfaced via web forms. And in a managed service as a user, you don't bother with updates, patches, and so on. 

This is because you have no access to the machines. Someone has to do the laundry. Usually, you have only limited choices, if any, on the underlying system. That might be the operating system or the version of the software used.

Fairly simple, right? Let's go to serverless that is a bit more complex.

## What Does Serverless Mean?

With the word serverless we're referring to a different computing model, one that's different from the "traditional" one which is server-oriented. 

In server-oriented computing (or serverfull if you like more sophisticated words), we use virtual or physical machines to set up and execute our application.

Qualities like the availability and the performance of your applications are strongly bound to the health of your machines. 

We've perfected clusterisation solutions over time (and other tools) to make the decline of machines' health less and less important. 

What about the cost, though? Why do we still pay for idle or underutilized servers (either in money or in lost CPU cycles)? If we need to scale a cluster of machines, why does this take time?

Here comes serverless. Serverless fits in the category of FaaS products (Function as a service).

The name is a bit misleading, though – the server where the code runs does in fact exist. 

You just don't need to care about it, just like in managed services. Serverless goes a bit further, however – your application runs, when you need it, and for just as long as it should. There are no idle times.

You never get to see the server in your virtual machine dashboard and of course, you don't know any details about the server.

Serverless implementations are usually event-driven. The instances are idle unless an event occurs. 

> Something to note: there might be a case where you have instructed your servers to not be idle which is known as "scale-to-one". They get busy and when they're done, they go idle again. If they get too busy they get support from other clones (also known as horizontal scaling).


## Advantages of Going Serverless

There are few benefits of serverless implementations. A big one is that they scale easily and effectively. This is because they are usually based on lightweight installation media, like Docker images/containers, and you don't need to provision extra machines.

In theory, with serverless computing, you have the whole cloud infrastructure of the provider at your feet. With the respective costs, of course. :)

Speaking about costs, serverless code is billed per second and at a higher rate than a machine lease. So it is recommended that you run it for relatively short workloads.

Some providers put a hard limit on how long serverless code can run. This is to also avoid unpleasant surprises on your bill.

One notable example of full-stack serverless and the cost benefits that come with it is acloud.guru. 

I remember studying for the AWS Architect certification using one of their courses (awesome content btw, highly recommended), and the instructor mentioning that "We pay $400 per month with Serverless and it would be around $100,000 using servers".

### What about the disadvantages of serverless?

One of the cons of serverless architecture relates to time-critical applications. 

Usually, newly deployed serverless functions experience some kind of latency also known as a "cold start". There are mitigations that can help you deal with cold starts, called -surprise, surprise- "warm starts". But you may want to check other architectures for such requirements.

By the way, serverless solutions provided by the cloud providers (like AWS Lambda, Azure Functions) are actually managed, too. That means you can set up your serverless architecture using high-level abstractions and input your preferences/configuration with the forms they provide.

## Managed Services + Serverless

As you have probably figured out by now, serverless and managed services have some interesting similarities. We can sum them up like this: Don't worry about the infrastructure, focus on your business value.

There is a very interesting public service that comes with both flavors, managed and serverless. This is AWS Aurora. Aurora is a managed database, compatible with MySQL and Postgresql. 

![Lend from David Zhang](https://miro.medium.com/max/960/1*1_5fnrCrSYmyCUhugLxU5A.jpeg)

There are two flavors of Aurora. There is the managed option, where you set up a database using a form, and it brings up a few virtual machines and takes care of their health. In this case, you can just focus on deploying a good database schema. 

In this managed method, the database is running 24/7/365. Or at least that's the goal, as it offers very high availability and otherwise works in the same way as any database server you have used in the past.

There is also the serverless flavor, where Aurora is set up in a serverless way. In that case, you have the storage "deployed" 24/7/365 as above. You cannot have serverless storage, which is contradictory (according to my current knowledge at least). :) 

But the processes that perform data manipulations on your data, like fetch and update, can be easily converted to serverless functions. 

Aurora serverless often costs a lot less, as the data manipulations run on an as-needed basis. But if the database is fairly busy the costs might be higher than in a serverfull architecture. 

That being said, it's better to use Aurora serverless when your workload is intermittent and unpredictable.

## What is Openfaas?

In this article, I've explained these technologies in the context of public cloud providers.

If you want to run serverless computing / FaaS without relying on a public provider, you can use OpenFaas (future article to come). 

![OpenFaaS logo](https://avatars.githubusercontent.com/u/27013154?s=280&v=4)

This technology will not only give you more control over your architecture. It will also help you realize that the serverless model relies on clustering technologies like Kubernetes. Also, you will learn how you can set up scaling rules and cold/warm starts.

## Conclusion

Thank you for reading until the end. We spoke about Serverless technologies and compared them with managed services. 

They have some serious overlap but cover different needs as well. If you need to add something I would love to hear your thoughts.


