---
title: An introduction to service and micro-service-oriented architectures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-22T14:02:25.000Z'
originalURL: https://freecodecamp.org/news/service-and-micro-service-oriented-architectures-explained-2f8d5da0ecdd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2myWvKpboVAA2sSZ
tags:
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pulkit Kumar

  We’ve come a long way from the traditional three-tier monolith architecture. In
  order to achieve a fast, robust and scalable model of development, you might try
  to align your application architecture with certain philosophies and deve...'
---

By Pulkit Kumar

We’ve come a long way from the traditional three-tier monolith architecture. In order to achieve a fast, robust and scalable model of development, you might try to align your application architecture with certain philosophies and development patterns, hoping that it might make it easier to manage the team and development timelines.

But when you actually figure out that there are so many development patterns out there that you can’t decide on any particular one because every other seems better, you might want to read this post.

Let’s start with the basics and gain some clarity on the jargon.

### What is Microservice Oriented Architecture?

Apart from microservice being a buzzword, from the design principles of microservices, it can be simply defined as:

> A highly cohesive, single purpose and decentralized service.

That is, a service which has one and only one purpose and is self-sufficient.

Any service which matches the properties mentioned in the definition can be termed a microservice. The design principles mentioned are:

1. _Single purpose_: The service should be focused on one and only one purpose. The service should be domain and goal focused. For example, a microservice can just be focused on a login mechanism.
2. _High cohesion_: The service should be self-sufficient in terms of domain requirements and domain infrastructure. The service should have all the features it needs for serving the single purpose. For example, a login microservice can have its own database.
3. _Decentralized_: The service should be decentralized from other services and infrastructure from a logical point of view such that any changes required in the microservice should not involve changes in any other microservice. For example, a login microservice should have its own set of infrastructure components and changes required in the login microservice should not involve changes in any other microservice.

![Image](https://cdn-media-1.freecodecamp.org/images/tqdyaeQCiW1OZR1Sy9ag0SBELh8aj9SPH6p-)

Using the microservice architecture pattern, you can split your application team into multiple teams _focused on the microservice_. For example, a search microservice can have its own team and a login microservice can have its own team. Both the teams can include people with expertise in the same domains such as database, frontend, and backend, given the fact that both microservices can have their own database, frontend, and backend.

Pros of using microservice oriented architecture include:

* Teams can be arranged around features/components in the product.

Changes in a feature/component require a change in only that particular set.

* Bug pointing and localizing is easy.
* Symphony of domains can bring up innovative solutions.
* Managing the feature becomes easy.
* More resources on a particular feature can be added if there’s a need to add some push.

Cons of using microservice oriented architecture include:

* Microservice-mesh can be an overhead to manage.
* Resourcing in terms of developers can be expensive.
* Teams might grow as components/features in the application do.
* Localization of solutions might happen if knowledge is not shared frequently across teams.
* Quality of code is different across microservices.

### What is Service Oriented Architecture?

> In a service-oriented architecture, services are divided on the basis of their role in the application layer.

For example, database service, frontend service, backend service, etc are logical segregations of services. These services are utilized by various components of the application.

![Image](https://cdn-media-1.freecodecamp.org/images/3UCYoQ9-Cvgq8-umTYfsCCnScRPrJIfTTwQL)

Service-oriented architectures might be a better choice when the application doesn’t have a very large ecosystem of diverse features/components and components can logically share the services.

Using the service-oriented architecture pattern, teams can be easily split _with respect to their domain expertise_.

For example, teams can be simply divided into backend, devops, database, mobile, etc. If any component requires a service, the client (developing the component) will contact the service team and thus, all the core information about the service stays _localized_ with the service team.

Pros of using service-oriented architecture include:

* Quality of code is consistent through the domain.
* Knowledge sharing is easy within the domain.
* Mistakes aren’t repeated since the domain team is aware of previous failures.
* More resources can be put on service if the need be.

Cons of using service-oriented architecture include:

* Bug/break in one service can affect multiple services/layers.
* Symphony of domains is missing due to which innovation might be lacking.
* Teams might end up working on only one layer if not managed properly.
* Managing multiple features is hard since it might involve changes across multiple services.
* One service might end up changing a lot.

### What is common in both?

Both the development patterns differ from the traditional monolith in a significant way.

> But both require teams and components to focus on one and only one thing.

Segregation and localization concepts are at the core in both the patterns. Both patterns are generally aligned with the DevOps philosophy to deliver fast growth across teams.

### Conclusion

Since the monolith can’t serve the needs of modern and agile development, you might want to align your development practices as well as your teams with one of the two approaches.

Microservice is a buzzword these days but that doesn’t mean it the best solution to your problems.

If your application demands segregation of teams based on expertise area such as database, frontend, backend, data-science, etc, then the Service-oriented approach might be the best for you.

If your application needs many different plug-in features which require their own resources such as their own database, frontend, backend, etc, you might want to go with microservice oriented architecture and focus the teams on particular feature-sets.

However, you can also go with the hybrid approach. The hybrid approach might be useful when you’re building a platform with multiple applications.

For example, if you want to build an in-house app store, the team developing the platform (app-store/platform team) can be further divided in a service-oriented pattern; whereas the teams building apps (app-teams) can be focused and divided into microservices.

[Sign up for my newsletter](http://eepurl.com/gcFOaX) to get _free access_ to software consulting, courses, articles, weekly-digests, and list-exclusive offers.

