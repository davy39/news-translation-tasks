---
title: 'Understanding Microservices: From Idea To Starting Line'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T04:04:05.000Z'
originalURL: https://freecodecamp.org/news/microservices-from-idea-to-starting-line-ae5317a6ff02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SlOGiH26JSP3h6uijnAi3A.jpeg
tags:
- name: learning
  slug: learning
- name: Microservices
  slug: microservices
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Michael Douglass

  Over the last two months, I have invested most of my free time learning the complete
  ins-and-outs of what the microservices architecture really entails. After much reading,
  note taking, white-boarding, and many hours writing, I fe...'
---

By Michael Douglass

Over the last two months, I have invested most of my free time learning the complete ins-and-outs of what the microservices architecture really entails. After much reading, note taking, white-boarding, and many hours writing, I feel like I have achieved a level of understanding such that I am ready to take the first step. Allow me to share what I have learned from start to finish.

![Image](https://cdn-media-1.freecodecamp.org/images/2rznJAMhE-qZgITEtIMEB-FIJOASann1LjP1)
_I have read and learned. Now it is time to take those first steps into the world of Microservices. First, for you, I document what I have learned and discovered thus far. — Image courtesy of [Pexels.com](https://www.pexels.com/photo/bridge-feet-railings-shoes-244371/" rel="noopener" target="_blank" title=")_

### Microservices: High-Level, What Are They?

Microservices is an architecture in which different component pieces of a software design are created and housed as individual, isolated services. Each is deployed separately and they communicate through well-defined network-based interfaces. Microservices are intended to be “small” (loosely defined) and kept to a single bounded context.

There are many benefits to microservices. Because of their isolation and strict requirement to communicate through well-defined interfaces, microservices prevent quick and dirty solutions often found in monoliths. These hacks inside of a monolith result in a loss of cohesion and an increase in coupling — two primary causes of complexity.

Many will argue that you can maintain this behavior in a monolith. In reality, because it is easy and because there are too few architects working in our code bases, monoliths typically fall due to this very failing.

> Complexity comes from low cohesion and high coupling. Microservices provides the structure to keep that at bay.

This benefit cannot be overstated. Because we keep the complexity monster at bay, development on systems a decade old can continue to move along at the speeds of development when the system was brand new.

Time and again, the complexity brought on by loose cohesion and tight coupling has been the cause of slow development on older projects. Cohesion and coupling is traditionally the technical debt grasping onto our feet, slowing us down. Pile enough of it up over the years, and you will be slogging through it.

When the services are written with them in mind, and the infrastructure provides it, other benefits can include horizontal scalability, testability, reliability, observability, replaceability, and language independence.

The downside for microservices is that to achieve these benefits, you must provide an underlying infrastructure which supports them. Without that support, you can easily find yourself with an unreliable and opaque system — or you find yourself reinventing the reliability wheel in every single service. This is a great lead-in to the next section…

### Microservices: High-Level Requirements (The Macro)

An environment which supports microservices fundamentally needs a set of baseline requirements to ensure some level of sanity. If you are going to run microservices, your organization must be willing to bear the overhead of starting and supporting them. The overhead will not be insignificant. It will take time and money to do microservices well.

A successful microservices architecture must have an internal committee or group responsible for defining the **_macro-architecture_** _—_ this will define what infrastructure will be provided for the development and operation of microservices along with policies which all microservices must adhere. This committee must be the strongest of your development staff, and it may even be one or more people who do not even work for you yet.

> The macro-architecture is one part provided infrastructure and one part policy requirements for all microservices.

Each organization’s macro-architecture will be unique. Each area listed below is completely open to negotiation around where to draw the line for your group: you can provide the teams with a fixed service or library of code to provide the required functionality. You can either mandate its use, or make its use optional. You could simply provide acceptance criteria to which a microservice must adhere, but provide no implemented library or service to help fulfill the requirement. Lastly, you could choose to do and require nothing for any given category.

> Choose wisely what you leave out of your macro-architecture. For every choice you allow the individual development teams to make, you must be willing to live with differing decisions, implementations, and operational behaviors.

You are the committee, and it is always best when people in the organization make these decisions — therefore, I cannot provide you with a baked manifesto.

As you are starting out, it is also important to keep this macro-architecture documentation open to change and receptive to the needs of the teams and the business. Now, let us turn to looking at the different categories for which macro-architecture decisions must be made.

#### Continuous Integration/Continuous Delivery

Core to the concept of microservices is the ability to build and execute tests in a very fast manner. Every commit to the microservice should result in a tested build. Once the tests pass and the build system is happy, a push button or an automatic deployment to production is the next important aspect. Cutting time to deploy allows rapid iteration and enables any number of good coding practices.

This is an easy one to fulfill these days. There are any number of build systems which provide access to pipeline builds. [Team City](https://www.jetbrains.com/teamcity/). [Bamboo](https://www.atlassian.com/software/bamboo). [Jenkins with Blue Ocean](https://jenkins.io/). Try them out and pick one. For the most part, the feature sets are fairly standard across the leaders of the pack.

An organization should strive for consistency in how services are built and deployed. Therefore, the macro-architecture should define the build tool and pipeline processes. The teams should have a voice in the conversation leading to the choice, but they should not be allowed to go rogue on this one.

#### Virtual Machines/Containers

Hand in hand with CI/CD is the ability to spin up a number of instances of a specific version of your service. The macro-architecture needs to consider how teams will manage doing this for both development, test, staging, and production environments.

For staging and production you are often faced with the desire to do canary roll-outs with trivial roll-back in the event of a failure. Having common infrastructure, policies, and procedures around how you package and deploy a service will make this easier for development and operations.

Load monitoring and instance control management should also be considered and facilitated by this portion of the macro-architecture. How to determine when more instances of a given service are needed, and having a consistent way to put them into production will be critical to long term success.

#### Logging

It is vital to monitor your microservices in production. To do so efficiently, you need to enable quick location of disparate information. This implies that the macro-architecture should strongly consider including the following:

1. A logging service for centralized logging. This can be the [Elastic Stack](https://www.elastic.co/products), [Slack](https://slack.com/), [Graylog](https://www.graylog.org/), and others of their ilk. You want a logging stack that includes a strong parser/visualizer because you are going to be dealing with a bunch of data. Part of your infrastructure can be one of these services, and a guarantee that each host in the environment will be configured to transfer log files on behalf of each service.
2. Definition of trace IDs to enable the location of all logs across all microservices handling a single external request. The concept here is that, for every external request coming into your microservices, you generate a unique ID, and that ID is passed to any internal microservices calls used to handle that request. Thus through a search for a single trace ID, you can find all microservices calls resulting from a single external access.
3. Base formatting requirements for server, service, instance, timestamp and trace IDs.

#### Monitoring

This is another “must provide” for the macro-architecture. Microservices will each need to decide on the best metrics to measure and monitor which will ensure individual success, but the macro-architecture will have specific instrumentation it will need from every service in order to provide oversight of the overall health of the system. Some macro-level data points include:

* The volume of messages, failures, successes, retries, and drops.
* The latency of requests.
* The ratio of received messages to sent messages.
* Status of circuit breakers.
* And more. Much, much more.

Instrumentation is one area where [The Tao of Microservices](https://amzn.to/2G3g3Ly) really shines, and I highly recommend it for a good understanding of the breadth and depth of monitoring in microservices.

#### Service Registration & Location

This is often overlooked when a microservices architecture is small because a few microservices can always find each other relatively easily. However, as time goes on and the number of microservices grows, the configuration necessary to connect everyone together statically becomes too constraining and eventually error prone. Many solutions can be had including DNS and configuration services (etc, etc.)

The macro-architecture of your microservices environment must define how this is done — even if the first iteration is `/etc/services.yaml` deployed and synchronized to all hosts.

This is not something that the development teams on individual services should set in place — it should be ubiquitous and managed from the macro-architecture level.

There are many, existing open source projects attempting to solve this problem including some of the service mesh software listed at the end of this article.

#### Communication Mechanisms

Microservices should have some level of control in how they implement their interfaces. Both the network level protocol and the application level protocol should provide some level of flexibility. Using Google Protocol Buffers over raw TCP could be just as available as using JSON RPC over HTTPS. That said, the macro-architecture should provide some guidance, some restrictions, and maybe even some infrastructure to help facilitate communication.

If a microservices infrastructure is going to work together in a common domain name space under HTTPS URIs, then you will want standardization around the naming and routing. The requests should have a common and consistent method by which ingress user requests as well as service-to-service requests are authenticated, authorized, and routed.

A microservices infrastructure which wants to permit the use of messaging as a communication device should consider providing an operations-managed messaging bus. This enables rapid development and deployment of services without teams needing to first focus on starting and then long-term managing a messaging service. It also fosters decoupling of services which want to communicate through the messaging service — if I have to know which messaging queuing service each service uses, I am growing more coupled.

Providing the infrastructure for your messaging layer also enables you to provide message routing to your services — something which can greatly enhance the flexibility of your macro-architecture. The ability to route requests through different versions of a service based on various criteria affords a lot of flexibility and helps to further maintain decoupling.

#### Load Balancing & Resiliency

Microservices are often used in environments where scaling and availability are expected. Traditionally, network devices provide load balancing functionality. But in a microservices environment, it is more typical to see this moved into the software layer of the macro-architecture’s infrastructure.

Code through which services communicate can utilize service location to discover all network locations of a given service, and it can then directly perform load balancing logic right there at the distributed edge.

Resiliency means remaining stable even in the face of errors. Retries, deadlines, default behaviors, caching behaviors, and queuing are a few of the ways microservices provide resiliency.

Just like load balancing, some part of resiliency is a perfect match for the infrastructure to handle at the edge— such a retries and circuit breaking (automatic error responses for services exceeding a failure threshold in the recent past).

However, the individual service should consider what resiliency role it should play internally. For example, an account signup system, where losing a signup equates to losing money, should take ownership of ensuring that every signup goes through — even if it means a delayed creation that results in an email to the account owner once successful. Internal queuing and management of pending signups may be best managed directly by this mission-critical service.

#### Persistence: Database, NoSQL, and so on

A microservices architecture completely isolates each microservice from the rest. Ultimately, they understand their own data storage needs best, and should, therefore, be individually encouraged to control their own destiny as it relates to data persistence. However, you still do not need to allow the wild, wild west to rule the day, and thus the macro-architecture should provide guidance (sometimes heavy-handed).

Here are some options you can look to include in the macro-architecture:

1. One or more data storage services including an SQL based relational database and a NoSQL storage system. These provided data storage services should include built-in backups. A microservice should utilize unique credentials with limited access to a schema restricted to only that microservice’s data. In this scheme, the operations team providing the storage service are responsible for its operation.
2. If you allow the microservices to bring their own persistence, you should have strict policy requirements for backups and disaster recovery. Think about off-site backups, recovery time, fail-over time, and so on. In this model, the development team is responsible for the operation of the storage service.

You should absolutely, without a doubt, refuse to permit the traditional “open access, one database to rule them all” mentality which permeates the world of monolith development. If your disparate services are able to communicate through the database, unexpected coupling will occur. Services must only have access to its own data stores, and cross-service communication must be maintained through their well-defined network interfaces.

I recently stumbled upon extremely nasty coupling of the database sort in an older monolith. The complexity was immediately obvious and my sadness grew exponentially.

#### Security

Your services need to know to whom they are talking (authentication) and what data and operations are permitted (authorization) to said identity. There are several potential concepts here:

* Let the IP network protect the services — if you run all of your microservices on a protected network, and you want to transfer trust to your development staff to not abuse access, then this might work for you. Keep in mind that a breach of a single service implies full access to all other services.
* Service-level authentication — shared keys or certificate-based authentication allows a called service to validate a calling service. You will need a secure way to distribute and update keys and certificates to keep this secure. Use a Key Management Service.
* User-level authentication — not only are services talking to services, but they are quite often talking on behalf of a user or even directly to a user. There must be a means of authenticating and authorizing the user-level credential to the resource at hand.

Start simple — this is an area that can break an organization out the gate, and it is probably best to start simple. You likely already have a few different services that talk to one another, and you are likely using some IP access-control lists to protect them. Start simple, add to the complexity as a natural evolution of the system.

#### Amendment X — Reserved Powers

> The powers not delegated to the infrastructure by the macro-architecture are reserved to the individual services respectively, or to the developers of such.

Do not underestimate the power of this statement. If the macro-architecture does not cover an aspect of the environment, the developers are free to choose and choose they will. The more teams you have, the more solutions you will find yourself maintaining. Therefore, do two things with your macro-architecture:

1. Consider very carefully what you leave out. If you follow the “start small” principle, you are likely not going to be providing a lot of ready-made infrastructures to cover the details of the macro-architecture. This is perfectly acceptable. However, you can still provide guidance and requirements around those areas in order to minimize the chaos.
2. Iterate rapidly. As the first few services come online, meet and discuss the entire macro-architecture. What is working? What is not working? What do you need to change now? (How very agile of me!) Do this on a regular basis. You will hear this again in a few moments.

### Who Should Use Microservices?

> Everyone should use Microservices.

There, I said it, and I will defend it relentlessly. Yes, I realize that there are plenty of people, likely far smarter and more learned than I am, who state, philosophically: “If you are not Netflix and you are not Amazon, then the overhead of using a microservices architecture is going to drown you.”

> The notion that I have to be Netflix or Amazon to make productive use of a microservices architecture brings, and I hope you quote me on this, one word to mind: Hogwash.

#### It’s All About Size…

The reality here is that the smaller your organization, the smaller your needs for a fully fledged microservices architecture. However, there is no reason to abandon the entire movement and leaving behind the benefits these very smart people have realized, even when you are a small shop with small services.

Your initial microservices macro-architecture conversations need to focus on precisely what you **_need_** to get started and then figure out how to get that into place. Build some services, observe their behaviors, and learn from what is and is not working for you.

Reconvene your microservices macro-architecture committee and use your new found experience along with your healthy reading and growing understanding of the industry-wide ecosystem to determine what the next evolution of your macro-architecture must be. Rinse and repeat. Iterate.

> Your microservices macro-architecture should continuously evolve right alongside the every day, iterative development you already do.

We live and breath this “agile” world of iterative design and development. There is very little reason that it should not apply to the infrastructure surrounding our services. Even if you never actually realize a fully idealized microservices architecture, but you have these architecture conversations and continually add small iterations of infrastructure and macro-architecture — you will have reaped many of the benefits over time.

Most importantly, because you focus each iteration of the microservices macro-architecture from a position of what you need at-the-time, you will have spent your time on the most valuable components of your organization.

Perhaps you started with a healthy CI/CD pipeline that took over 85% of your existing monolithic development jobs. Dividends! Next, you standardize your deployments into docker images and provide tooling around launching, migrating, and rolling back new versions. Dividends! Then add in consistent logging and monitoring, and you start to visualize and report on messaging flows through your systems. Dividends! Now as you are adding new services, you realize that the coupling of services talking directly to one another is holding you back, and you add a messaging service to your infrastructure and begin moving some functionality to event-based triggers. Dividends!

I do not believe you need to be Amazon or Netflix to reap the benefits of a microservices architecture. In some cases, you can use the knowledge of how these architectures work **inside** of a single monolith, and the dividends can be quite rich indeed.

From the start, or years after the monolith begins to fail under its own weight, you can use the knowledge of how to separate services to shore it up and make it more stable. A monolith which is internally designed with good separation between services makes an easy target for microservices when success demands more from it. (Just realize that it takes architects to maintain the integrity of a monolith, and beyond the start of a system it will be difficult to achieve long-term.)

### The Macro-Architecture Infrastructure

One of my key questions, when I began this journey, was how I would provide any desired, baseline infrastructure to the developers of services within my organization. My reading lead me to understand three primary methods:

1. Run systems which provide the services along with documentation on the proper use thereof. An example here is to provide a CI/CD system and guidelines on how to configure your service’s pipeline. This is perhaps the simplest of the two, because we are all very used to having this type of prepared infrastructure managed by an operations team.
2. Provide code which developers can bake into their systems to perform the desired functionality. An example here would be a shared library that can be used to perform service location and load balancing. This restricts the ability for teams to choose their own language, but the benefit of not creating this infrastructure multiple times can outweigh that cost.
3. If language independence is truly desired for your services, the infrastructure components can be placed in a sidecar implementation which runs as a secondary process alongside each service. The sidecar then represents the service, and provide access to other services, in the infrastructure. Sidecars appear to be more prevalent in the industry than I had first thought possible.

### Off The Open-Source-Shelf Infrastructure

There are a plethora of options available to get yourself started with a microservices macro-architecture. You would be extremely remiss to not consider the options as a part of your initial macro-architecture conversations. Some of these existing infrastructure pieces make getting started quite easy — further supporting my stance that everybody can benefit from this.

Some of the more cohesive off-the-shelf infrastructure projects are referred to as service meshes. Service meshes provide a control plane (clustered management of the service mesh proxies and other macro services) and a data plane (the proxy services through which your services communicate). They typically operate in the form of a sidecar proxy which provides the microservices networking functionality out of the box. Using one of these can give you a head start on the bulk of the functionality — and for many people, they may be more than you will ever need.

These projects are all relatively young, and they are going to impose limitations on your environment that you might not have otherwise chosen. However, they are designed and developed by people who know microservices very well, and you can both use their insights into what works and save a lot of time not recreating the technologies yourself.

Here are a few that I have found and done at least a moderate amount of investigation into (these descriptions are surface-reading only — see the respective sites for more information!).

#### [Netflix](https://netflix.github.io/)

Netflix is hot on the scene with microservices architecture, and they have [open sourced](https://netflix.github.io/) much of their base run-time services and libraries. They work in the JVM, and include [Eureka](https://github.com/Netflix/eureka) for service discovery, [Archaius](https://github.com/Netflix/archaius) for distributed configuration, [Ribbon](https://github.com/Netflix/ribbon) for resilient and intelligent inter-process and service communication, [Hystrix](https://github.com/Netflix/hystrix) for latency and fault tolerance at run-time, and [Prana](https://github.com/Netflix/prana) as a sidecar for non-JVM based services.

The Netflix-provided infrastructure pieces may be too big for a smaller shop. But if you are working in the JRE already, adding support for Eureka, Ribbon, and Hystrix can quickly grant you many benefits with potentially small amounts of investment.

#### [Spring Cloud](http://projects.spring.io/spring-cloud/)

Spring has long been a central place to go for frameworks enabling quick and easy JVM-based software development. Their Spring Cloud specialized section includes integrations with a lot of cloud infrastructure, including the above mentioned Netflix libraries among many others. If you are going to go the JVM route, it will be worth your while to get to know Spring Cloud.

#### [**Linkerd**](https://linkerd.io/) **(Service Mesh)**

This service mesh, written by Buoyant, was released to the open source world early in 2016. It runs as a sidecar and acts as a proxy between your services. It provides you with: load balancing, circuit breaking, service discovery, dynamic request routing, HTTP proxy integration, retries and deadlines, TLS, transparent proxying, distributed tracing, and instrumentation. Protocol support includes HTTP/1.x, HTTP/2, gRPC, and anything TCP-based.

Linkerd tries to not tie you down to any one technology — it supports running locally, in Docker, in Kubernetes, in DC/OS, in Amazon ECS, and more.

As a sidecar application, it can be run once per service or once per host — so if you run multiple services per host, you can save on process overhead with Linkerd. They boast a couple of very well known names on their used by list.

Interestingly, you can integrate Linkerd with Istio (covered below). I am unclear what the benefits of this are, but a surface reading says there may be something there.

#### [**Conduit**](https://conduit.io/) (Service Mesh)

In December 2017, almost two years after Linkerd, Buoyant released another service mesh specifically for Kubernetes clusters. They took their lessons learned, and are creating Conduit with the intention of being an extremely lightweight service mesh.

The Conduit tooling works in tandem with the Kubernetes tooling to inject itself into your cluster. Once injected, most of the work happens behind the scenes through proxying and the use of standard Kubernetes service naming schemes. It claims good end-to-end visibility, but I do not see good screenshots of that, and have not yet tested it out myself.

A big caution here is the Alpha status and the _extremely_ new creation— February 2018. They have published a [Roadmap to Production](http://v) with an insight of where they are going. For now, I would test drive it and keep this one on the “to watch” list.

#### [**Istio**](https://istio.io) **(Service Mesh)**

Istio is a service mesh which came to us in May of 2017. Internally they are using Envoy (covered next). They have instructions for deploying on top of Kubernetes, Nomad, Consul, and Eureka.

As a sidecar, it provides automatic load balancing, fault injecting, traffic shaping, timeouts, circuit breaking, mirroring, and access controls for HTTP, gRPC, WebSocket, and TCP traffic. Ingress and Egress traffic is afforded the same feature set. Automatic metrics, logs, and traces are available quickly through included visualization tools. They also enable infrastructure level, run-time routing of messages based on content and meta information about the request.

The downside is it is very young and restricted to specific deployment environments — though there is some documentation that may help you deploy in other environments using manual methods.

Istio uses iptables to transparently proxy network connections through the sidecar — in the Kubernetes world this is truly transparent to you, but in other environments, you are involved in making that work. (It honestly looks like most of these mesh services are using iptables’ transparent proxy mechanisms to hook their sidecars into your applications.)

On the upside, the security feature set feels mature and well thought out. All egress connections are, by default, denied until explicitly permitted — and that is refreshing! You protect your services within your mesh the same way you protect it at the ingress and Egress — nice!

The out-of-the-box visualization of your services as a network diagram and various per-service metrics provides you immediate observability into your environment. Large-scale deployments will likely need to own moving this into larger deployments, but as a getting started environment it is very nice.

#### [**Envoy**](https://www.envoyproxy.io/) **(Data Plane)**

Originally built by Lyft, but released after Linkerd in 2016, this one has the appearance of being the most mature. It boasts _very large_ companies on its “Used By” list. It is written in C++ and is intended to be run as a sidecar like the rest. It was built to support running a single service or application as well as supporting a service mesh architecture.

That said, Envoy is not a full-service mesh as it only provides the data plane and you must manage the Envoy processes yourself or use Istio (which, by default, uses the Envoy proxy).

A quick look through the documentation shows a healthy list of features, including filters, service discovery, health checking, load balancing, circuit breaking, rate limiting, TLS, statistics, tracing, logging, and much more. Connection type supported include HTTPS, TCP, and Websockets.

I am impressed with Envoy from the window dressing, and given Istio’s use of Envoy, I will most likely experience it through a test drive of Istio first (and will only look at Envoy alone if I feel there is something Istio is hiding or preventing me from utilizing fully).

### Jump Start — Excitement Abounds!

I am extremely excited to sit down with each of these existing technologies and give them a thorough run-through. With the sheer amount of functionality they already provide, I would be woefully remiss to not understand them and include them as the basis for whatever microservices macro-architecture I support in my organization.

Building all of this functionality from scratch, and not taking advantage of the great work already done by so many fine, brilliant individuals would be a crime. I would rather my organization spend its time on the services and functionality that makes them money — or, if we must extend more functionality to the macro-architecture infrastructure, spend that time contributing back to one of these projects.

Utilizing one of these service meshes will require us to understand it extremely well. We must be able to discern the implications it has upon our macro-architecture, and we must document those very carefully into our macro-architecture. Oh yes, even if you choose a service mesh, you must still write down a macro-architecture for your microservices infrastructure. These service meshes are only providing you an immense jump start, and, in some cases, answering some of the questions for you.

### In Closing

It has been an exciting time for me to get back to my very technical roots and dig deeper into modern architecture concepts through microservices. I look forward to continuing this journey, and I hope to hear from any of you who have done so and may have tips for me that I had not thought to include here. Thank you all for your attention, and I hope you got something out of this article.

I would like to close with a listing of the books I recently read in my quest for knowledge, one that I am currently reading, and two that I plan to read based on recommendations in other books and by multiple experts in software architecture.

#### [The Tao of Microservices](http://amzn.to/2pmifTF) by Richard Rodger

A great introduction to the world of microservices with a strong focus on the broad spectrum of requirements necessary to enter into this world.

Richard starts with practical definitions and direction on how to build microservices followed by an overview of what it takes to run microservices.

This book provides a good understanding of messages as transport, pattern matching for routing, and the large effort monitoring and measuring your environment will be.

_Warning: The author spends the first third of the book being rather derogatory towards any non-microservices approach to development. Read past that and he does have a good book._

#### [Microservices: Flexible Software Architecture](http://amzn.to/2HJGeTz) by Eberhard Wolff

This book is broken up into logical sections. The first two give a lot of repetitive background information on microservices presenting what they are, are not, and when you should and should not use them.

There is a severe lack of commas in the book, which sometimes trips you up, but the material is very good. Part 3 turned this book into a complete winner for me when he began covering very specific pieces of information.

#### Reading and Will Read List

The following books are currently in my queue to read based on recommendations in the previous books and also by experts in software architecture.

[Martin Fowler](https://martinfowler.com/articles/microservices.html) is one such expert who quickly rose to the top in my searching and reading. His website is an invaluable resource as well.

* [Domain Driven Design](https://amzn.to/2pJgU9P) by Eric Evans — I am currently reading this one, because literally everybody (even [Object Thinking](https://amzn.to/2GelWBo)) references it. The deference it receives in the developer community is much like the Bible, and it shares a similar price tag. I am a third of the way through it, and it is definitely solidifying and putting names to practices I have used for some time. I look forward to more time with it.
* [Building Microservices: Designing Fine-Grained Systems](https://amzn.to/2IU6Qmm) by Sam Newman. Martin Fowler speaks very highly of this one. It purports to “provide lots of examples and practical advice.” I understand many of the principles, and now I want to see more practical examples to further refine and firmly seat them.
* [Production Ready Microservices](https://amzn.to/2IXBICD) by Susan J. Fowler. I believe Susan is going to drive more into this concept of a macro-architecture for microservices. In this article, I have attempted to do in brief what I hope she will do in much more detail.

#### How I Got Here

As I said in the opening, I have been on this mission for a couple of months. If you are interested in seeing the progression of my journey and possibly gain more insight into some of these topics, please peruse my earlier investigative posts:

* [Microservices: A Journey of Understanding](https://codeburst.io/microservices-architecture-e6907b97a42a)
* [Microservices: Early Thoughts Before That First Step](https://codeburst.io/microservices-architecture-early-thoughts-before-that-first-step-fecc2ef9d64)
* [Microservices Architecture: It Takes A Platform — Eureka!](https://codeburst.io/microservices-architecture-it-takes-a-platform-eureka-97f61af90d5c)

