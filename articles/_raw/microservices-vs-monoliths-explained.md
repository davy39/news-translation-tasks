---
title: 'Microservices vs Monoliths: Benefits, Tradeoffs, and How to Choose Your App''s
  Architecture'
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-05-14T00:18:44.000Z'
originalURL: https://freecodecamp.org/news/microservices-vs-monoliths-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/cover--3-.png
tags:
- name: Microservices
  slug: microservices
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: 'When you''re tasked with designing an application, one of the first questions
  that probably comes to your mind is whether to design a microservice or a monolith.

  The consequences of this seemingly simple and innocuous decision are potentially
  signific...'
---

When you're tasked with designing an application, one of the first questions that probably comes to your mind is whether to design a microservice or a monolith.

The consequences of this seemingly simple and innocuous decision are potentially significant, and they're often not fully thought through. A wrong decision can be very expensive, not just financially, but also expensive with regard to the time required to develop the application and the time required to deploy any future changes.

There is no objectively correct approach, though. It all depends on what problem you are trying to solve and what trade-offs you are able to live with.

This article will explain the differences between monoliths and microservices as well as some heuristics to help you decide how to choose between the two architectures.

## Table of Contents

1. [Monoliths vs Microservices: An Analogy](#heading-monoliths-vs-microservices-an-analogy)
    
2. [What is a Monolith?](#heading-what-is-a-monolith)
    
3. [What are Microservices?](#heading-what-are-microservices)
    
4. [Data Management in Microservices](#heading-data-management-in-microservices)
    
5. [Database Isolation in Microservices](#heading-database-isolation-in-microservices)
    
6. [How to Choose Between Monoliths and Microservices](#heading-how-to-choose-between-monoliths-and-microservices)
    
7. [Why you should start with a Monolith](#heading-why-you-should-start-with-a-monolith)
    
8. [Why you should start with a Microservice](#heading-why-you-should-start-with-a-microservice)
    
9. [Hybrid Architecture – A Middle Ground](#heading-hybrid-architecture-a-middle-ground)
    
10. [Bringing it Together](#heading-bringing-it-together)
    

## Monoliths vs Microservices: An Analogy

Before we go into the technical details of monoliths and microservices, let’s quickly explain the difference between the two architectures using an analogy.

A monolithic architecture is like a typical restaurant, where all kinds of dishes are prepared in one large kitchen and a single menu is presented to guests to choose from.

Just as the restaurant offers everything from starters to desserts in one place, a monolith includes all functionalities in one codebase.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a75fc63-2d14-4379-819f-24cfa8c9d8fe_1504x603.png align="left")

*A typical restaurant is like a monolithic application*

A microservice architecture is like a food court composed of several small, specialised stalls, each serving a different type of cuisine. Here, you can pick and choose dishes from various stalls, each expertly preparing its own menu.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d8efa02-6ab9-4013-bc09-18343063139a_2462x1394.png align="left")

*A food court is like a microservice application*

In a microservice architecture, the application is divided into smaller, independent services. Just as each stall in the food court manages its own menu, staff, and kitchen, in a microservice architecture, different services run separately and are responsible for handling their specific functionalities.

Customers can pick and choose dishes from any stall, mixing and matching as they like, just as different microservices can be used in combination to create a comprehensive application. Each service is self-contained and communicates with other services through simple, well-defined interfaces.

## What is a Monolith?

In a monolith, all the code needed for the all the features of the application is in a single codebase and gets deployed as a single unit.

Let's look at an e-commerce application, for example. Some of the important features of an e-commerce application are:

1. **Product search service**: Manages product listings, descriptions, inventory, prices, and categories. It's responsible for providing up-to-date information about products to other services and users.
    
2. **Payment service**: Handles processing of payments and transactions. It interacts with external payment gateways and provides secure payment options to customers.
    
3. **Order management service**: Manages the lifecycle of customer orders from creation to completion. This includes handling order processing, status updates and order cancellation.
    
4. **Recommendation service**: Provides personalised product recommendations to users based on their search history and past purchases.
    

In a monolithic application, the code for these features will be in a single codebase and deployed as a single unit. This is illustrated in the image below where the application is deployed to a single server with a separate database.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35d7463a-4c95-4f64-81c1-7a41bdb21d45_2246x752.png align="left")

*Monolithic e-commerce application deployed on a single server*

The database is hosted on a separate server to improve performance and security, while the application servers handle the business logic.

Even in a monolithic architecture, the application can be duplicated and deployed across multiple servers, with a load balancer distributing traffic between the servers. This is illustrated below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F808895de-b53d-4b39-9adf-55007d185976_2442x1358.png align="left")

*Monolithic e-commerce application deployed on two separate servers*

## What are Microservices?

Microservices are independently deployable services modeled around a business domain.

In contrast to a monolithic architecture, where all the application components are tightly integrated and deployed as a single unit, a microservices architecture breaks down the application into smaller, independently deployable services. Each service runs its own process and communicates with other services over a network, typically using [HTTP/REST](https://lightcloud.substack.com/i/137067496/rest), [RPC](https://lightcloud.substack.com/i/137067496/rpc), or message queues.

We can brea the monolithic e-commerce application we talked about above down into a microservice architecture, as shown below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9c9f2b4-fb93-411d-88dc-330628b222f5_2440x1022.png align="left")

*Microservice e-commerce application*

The following are some key differences between the monolithic and microservices e-commerce application:

In the microservice architecture, every feature of the application is in a separate codebase. This separation ensures we have independently deployable services modeled around business domains (Product Search Service, Payment Service, Order Management Service and Recommendation Service).

Having a separate codebase for every service ensures:

1. **Simplified deployment:** With each service in its own codebase, it can be updated, tested, and deployed independently of others.
    
2. **Fault Tolerance**: Separate codebases contribute to fault tolerance. If one service experiences a failure, it does not necessarily compromise the operation of others. This is crucial for maintaining the overall system's availability and reliability. For example, if the payment service fails, only customers that want to purchase an item will be affected. Other customers can still search through the application for things to buy, track existing orders, and get recommendations for things they might want to buy.
    
3. **Technology Flexibility**: Separate codebases allow each service to be developed using the technology stack best suited to its needs. Different teams can choose different programming languages, frameworks, or databases depending on what works best for the specific functionality of that service.
    
4. Each service is deployed on its own servers. The servers hosting each service can be scaled independently based on its specific demand and resource requirements. This is much more efficient than scaling a monolithic application where scaling up often means scaling the entire application, even if only one part of it is under heavy load. For example, the payment service might be really busy during a promotion/sale. This can be independently scaled instead of scaling the entire application, which can be a waste of money.
    

Each service has its own database (if it needs a database). This ensures:

1. Every microservice can run independently of other services. If every service used the same database (as is the case in a monolithic application), a database failure will bring down the entire application.
    
2. The databases can be scaled independently as needed. Some databases will be busier than others, so having the flexibility to scale them independently is useful.
    
3. Every microservice uses the right type of database. Some microservices might function better with different types of databases. For example, Elasticsearch would be ideal for the product search database of the e-commerce application due to its powerful full-text search capabilities, while a relational SQL database will be better suited for the order and payment databases.
    
4. An [API Gateway](https://lightcloud.substack.com/p/api-gateway-explained) sits in front of the services. This acts as the middle-man between users and the many services they may need to access. The API Gateway handles [authorisation and authentication](https://lightcloud.substack.com/i/138365595/authorisation-and-authentication), [request routing](https://lightcloud.substack.com/i/138365595/request-routing) and [rate limiting](https://lightcloud.substack.com/i/138365595/rate-limiting).
    

### Data Management in Microservices

Managing data between services is the most complex part of a microservice architecture. Communication between services is either synchronous or asynchronous.

**Synchronous Communication:** Services communicate directly with each other. This is a straightforward approach, easy to understand and implement.

For example, in an e-commerce application, when a customer places an order, the Order Management Service might directly call the Product Search Service to check if the item is in stock before proceeding.

**Asynchronous Communication:** Services do not wait for a direct response from another service. Instead, they communicate through events or messages using a message broker.

In the e-commerce example, when a new order is placed, the Order Management Service will publish an "Order Created" event to a message queue. The Product Search Service, subscribing to this queue, reacts to the event at its own pace and updates the inventory accordingly. This decouples the services, allowing them to operate and scale independently.

Synchronous communication is simpler to understand and implement but lacks [fault tolerance](https://lightcloud.substack.com/i/59017006/fault-tolerance).

### Database Isolation in Microservices

In a microservice architecture, it is a standard practice to prevent services from directly accessing the databases of other services. You'd typically do this to ensure that each service can manage its data schema independently, without affecting other services.

Looking back at our e-commerce example, suppose the Payment Service decides to change its data schema and rename a column called “amount” to “order\_value”, as “amount” can be quite an ambiguous term. If the Order Management Service were directly querying the Payment Service’s database, any direct SQL queries from the Order Management Service to the Payment Service’s database on this column would fail because of this schema change.

To handle these dependencies and changes securely and efficiently, the services should interact via APIs rather than via direct database access. By providing an API as an interface, the Payment Service can abstract the complexities of its underlying data model.

For instance, regardless of whether the database field is named “amount” or “order\_value”, the API can expose a parameter called “payment\_amount”. This allows the Payment Service to internally map “payment\_amount” to whatever the current database schema is using.

## How to Choose Between Monoliths and Microservices

Choosing between a monolith and a microservice architecture depends on what problem you are trying to solve and what trade-offs you are able to live with.

Microservices are newer and more popular with the large technology companies. Most technical books and blogs cover the architectures of these large companies.

But the engineering problems of large companies operating at scale are not necessarily the same engineering problems faced by smaller companies.

Copying what the large technology companies do is reasoning by analogy. This is not necessarily wrong, but it can introduce unnecessary complexities for a smaller company/startup. Better to reason by first principles, or better yet, choose better analogues.

You can look at what other startups are doing, or what the technology giants of today did when they were much smaller. For example, [Etsy, Netflix and Uber](https://blog.dreamfactory.com/microservices-examples/) all started as monoliths before migrating to a microservice architecture.

### Why you should start with a Monolith

Creating an application should be done for one reason and one reason alone: to build something that people want to use. Users of your application do not care if you use a microservice or monolith. They care that you are solving a problem for them.

To quote [Paul Graham](https://paulgraham.com/startuplessons.html):

> “Almost everyone’s initial plan is broken. If companies stuck to their initial plans, Microsoft would be selling programming languages and Apple would be selling printed circuit boards. In both cases, their customers told them what their business should be and they were smart enough to listen”.

There is arguably no need to spend so much time designing and implementing a highly complex microservice architecture when you are not even sure that you are building something that people want to use.

So, why should you start with a monolith when building an application?

1. **Simplicity**: A monolith does not require dealing with the complexities of a distributed system, such as network latency, data consistency, or inter-service communication. This lack of complexity not only makes the initial development phase smoother but also reduces the overhead for new developers, who can contribute more quickly without having to understand the intricacies of a distributed system
    
2. **Ease of Iteration**: In the early stages of a product, rapid iteration based on user feedback is critical. The product direction is still evolving, and quick pivots or adjustments are necessary based on user input. This is usually easier to achieve with a simple monolithic architecture.
    
3. **Low Cost**: Running a monolithic application can be less expensive in the early stages, as it typically requires less infrastructure and fewer resources than a distributed microservices architecture. This is crucial for startups and small businesses where money can be in short supply.
    

Beginning with a monolith often aligns better with the practical realities of launching and iterating on a new application.

### Why you should start with a Microservice

1. **Scalability from the Start:** One of the strongest arguments for microservices is their innate ability to scale. If you anticipate rapid growth in usage or data volume, microservices allow you to scale specific components of the application that require more resources without scaling the entire application. This can be particularly valuable for applications expected to handle varying loads or for services that might grow unpredictably.
    
2. **Resilience:** Microservices enhance the overall resilience of the application. Because each service is independent, failures in one area are less likely to bring down the whole system. This isolation helps in maintaining resilience by ensuring that parts of your application can still function even if others fail.
    
3. **Flexible Tech Stacks:** Microservices allow different teams to use the technology stacks that are best suited for their specific needs. Going back to our e-commerce example, the other services may be written in Java, but the recommendation service can be written in Python if the team responsible for building that has more expertise in Python. This is a very crude example, but the principle holds. A microservice architecture gives teams flexibility on which technology they can use. Taken to its logical extreme, this can also be a flaw since it can add additional complexity to the overall architecture. Introducing a different language for a service might require different build tools and deployment processes.
    

## Hybrid Architecture – A Middle Ground

The formal, academic definition of a microservice is that it is an independently deployable service modeled around a business domain. Under the thumb of this definition, each business domain should be a separate service.

But you're not confined to this strict definition when it comes to implementing a design. Let’s look at our e-commerce microservice application again.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc244781f-08a0-42b1-a928-ddc95e02d437_2440x1022.png align="left")

*Microservice e-commerce application*

We can choose to keep the product search service as a microservice. Since more people search for products than buy them, we may want the ability to scale this service independently of the others.

Also, this service will need its own dedicated full text search database like Elasticsearch or Solr. SQL databases are not well-suited for full text search and product filtering.

We can also choose to keep the recommendation service as a microservice since this will be written in a different language from the other services. This service will also need its own separate graph database like Neo4j to help make recommendations to users about what to buy based on their past searches and purchases.

We are left with the payment service and the order management service which can be combined into a monolith. This is illustrated below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F113147b6-7a41-49a1-a4ad-88130de2f9fd_2334x922.png align="left")

*Hybrid monolithic/microservice architecture*

In this example, we haven’t followed the academic definition of a microservice architecture, where every service is modeled around a business domain. Instead, we have chosen to be pragmatic and create microservices because we want to use a specific technology and because we want to be able to scale some services independently.

## Bringing it Together

In a monolith, all the code needed for the all the features of an application is in a single codebase and is deployed as a single unit. In a microservices architecture, the application is divided into smaller, independent components, each responsible for specific features or functionalities. Each microservice has its own codebase and can be deployed independently of others.

Choosing between a monolith and a microservice depends on the problem you are trying to solve and what trade-offs you are able to live with.

Monoliths provide simplicity, ease of iteration and low cost. Microservices provide scalability, resilience and a more flexible tech stack.

For startups, the simplicity, ease of iteration, and cost-efficiency of a monolithic architecture make it an ideal initial choice, allowing them to focus on developing core features and finding product-market fit without the overhead of managing a distributed system.

For a more established company with growing needs for scalability, resilience, and technological flexibility, a microservice architecture can be a better choice.
