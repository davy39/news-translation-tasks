---
title: How to Scale a Distributed System
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-13T23:37:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-scale-a-distributed-system
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/photo-1515378960530-7c0da6231fb1-1.png
tags:
- name: database
  slug: database
- name: distributed systems
  slug: distributed-systems
- name: scalability
  slug: scalability
- name: scaling
  slug: scaling
seo_title: null
seo_desc: "By Apoorv Tyagi\nDesigning a distributed system that supports millions\
  \ of users is a complex task, and one that requires continuous improvement and refinement.\
  \ \nRecently I read a book by Alex Xu called \"System Design Interview – An Insider's\
  \ Guide\". T..."
---

By Apoorv Tyagi

Designing a distributed system that supports millions of users is a complex task, and one that requires continuous improvement and refinement. 

Recently I read a book by Alex Xu called "_System Design Interview – An Insider's Guide_". This article, inspired by the first part of the book, shares some popular techniques used by many large tech companies to scale their architecture to support up to a million users.

This is not an exhaustive list, but if you're a newer developer who's just getting started, this can help you build a stronger foundation for your career.

## **Use a **Load** B**alancer****

A load balancer is a device that evenly distributes network traffic across several web servers. In this architecture, the clients do not connect to the servers directly – instead they connect to the public IP of the load balancer. 

Using a load balancer also protects your site in the event of web server failure – and this, in turn, improves availability. For example,

* If one server goes down, all the traffic can be routed to the second server. This prevents the overall system from going offline.
* If in the future the traffic grows and these two servers are not enough to handle all the requests properly, then you just need to add more servers to your pool of web servers and the load balancer automatically starts distributing requests to them.

### Load Balancing Algorithms

Let's look at some of the algorithms which a load balancer can use to choose a web server from a pool for an incoming request:

* **Round Robin** – You start from the first server in the pool, move down to the next server, and when you're done with the last server you loop back up to the first and start working down the pool again.
* **Load-based server** – You assign a server based on whichever server has the smallest load currently, thereby increasing throughput.
* **IP Hashing** – You assign a server by hashing the IP address of incoming requests and using the hash value to do the modulo operation with the number of servers available in the server pool.

## **Use **Cach**ing**

A cache stores the result of the previous responses so that any subsequent requests for the same data can be served faster. So you can use caching to minimize the network latency of a system.

You can significantly improve the performance of an application by decreasing the network calls to the database. This is because repeated database calls are expensive and cost time. 

For example, every time a new user loads a website's home page, one or more database calls are made to fetch the data. This increases the response time. Caching can alleviate this problem by storing the results you know will get called often and those whose results get modified infrequently.

Here are a few considerations to keep in mind before using a cache:

* **Set an expiration policy:** You should always have an expiration policy on your cache. If you don't have one, the data will get stored in the cache permanently and it will become stale.
* **Sync the cache and database:** You should build a mechanism to keep the database and the cache in sync. If any data modifying operations occur in the databases and the same change doesn't reflect in the cache then it will introduce inconsistencies in your system. 
* **Set an eviction policy**: You should have an algorithm that can decide which existing items will get removed once the cache is full and you get a request to add other items to the cache. Least-recently-used (LRU) is one of the most popular cache eviction policies used today.

## **Use a **Content** D**elivery** N**etwork (CDN)****

A CDN or a Content Delivery Network is a network of geographically distributed servers that help improve the delivery of static content from a performance perspective. CDN servers are generally used to cache content like images, CSS, and JavaScript files.

Here is how a CDN works:

* When a client sends a request, a CDN server to the client will deliver all the static content related to the request.
* If the CDN server does not have the required file, it then sends a request to the original web server.
* The CDN caches the file and returns it to the client.
* Let's say now another client sends the same request, then the file is returned from the CDN.

Here are a few considerations to keep in mind before using a CDN:

* **Cost**: CDNs are generally run by third-party providers and they charge you for the data transfers in and out of the CDN. So caching infrequently used assets should not be stored in the CDN.
* **Fallback Mechanism**: If a CDN fails, you should be able to detect it and start sending requests for resources from the original web server. So you should build a mechanism for how your application copes with a CDN failure.

## **Set Up a **Message** Q**ueue****

A message queue allows an asynchronous form of communication. It acts as a buffer for the messages to get stored on the queue until they are processed.

The architecture of a message queue includes an input service, called publishers, that creates messages, publishes them to a message queue, and sends an event. Another service called subscribers receives these events and performs actions defined by the messages.

Both publishers and subscribers are decoupled from each other and that's what makes the message queue a preferred architecture for building scalable applications.

### Message queue example

Consider the following use case:

You are building an application for ticket booking. As soon as a user completes their booking, a message confirming their payment and ticket should be triggered. This task may take some time to complete and it should not make our system wait for processing the next request.

Here, we can push the message details along with other metadata like the user's phone number to the message queue. Another worker service picks up the jobs from the message queue and asynchronously performs the message creation and sending tasks.

The publishers and the subscribers can be scaled independently. When the size of the queue increases, you can add more consumers to reduce the processing time.

## **Choose Your **Database** Wisely**

According to [Wikipedia](https://en.wikipedia.org/wiki/Database):

> A database is an organized collection of data stored and accessed via a computer system. 

Databases are used for the persistent storage of data. We generally have two types of databases, relational and non-relational.

### ➔ Relational Database

A relational database has strict relationships between entries stored in the database and they are highly structured. This is to ensure data integrity. For example, adding a new field to the table when its schema doesn't allow for it will throw an error.

Another important feature of relational databases is ACID transactions.

#### ACID transactions

These are a set of features that describe any given transactions (a set of read or write operations) that a good relational database should support.

**Atomicity** means that when a transaction that comprises more than one operation takes place, the database must guarantee that if one operation fails the entire transaction fails. Either it happens completely or doesn't happen at all.

**Consistency** means that each transaction in a database does not violate the data integrity constraints whenever the database changes state and does not corrupt the data. In simple terms, consistency means for every "read" operation, you'll receive the most recent "write" operation results.

**Isolation** means that you can run multiple concurrent transactions on a database, without leading to any kind of inconsistency. All these multiple transactions will occur independently of each other.

**Durability** means that once the transaction has completed execution, the updated data remains stored in the database. It will be saved on a disk and will be persistent even if a system failure occurs.

### ➔ Non-Relational Databases

A non-relational database has a less rigid structure and may or may not have strict relationships between the entries stored in the database. The data typically is stored as key-value pairs. For example:

```
[
    { 
        firstName: "Apoorv",
        lastName: "Tyagi",
        gender: "M"
    },
    { 
        name: "Judit",
        rank: "Polgar",
        gender: "F"
    },
    {
      //...
    },
]

```

Similar to the ACID properties of relational databases, the non-relational database offers BASE properties:

**Basically Available (BA)** which states that the system guarantees availability even in the presence of multiple failures. 

**Soft State (S)** means the state of the system may change over time, even without application interaction due to eventual consistency. In NoSQL, unlike RDBMS, it is believed that data consistency is the developer's responsibility and should not be handled by the database.

**Eventual Consistency (E)** means that the system will become consistent "eventually". However, there's no guarantee of when this will happen.

### NoSQL vs SQL

Non-relational databases (also often referred to as NoSQL databases) might be a better choice if:

* Your application requires low latency. Since there are no complex JOIN queries.
* You have a large amount of unstructured data, or you do not have any relation among your data.

## How to Scale a Database 

Let's now look at the various ways you can scale your database:

### Vertical vs horizontal database scaling

In vertical scaling, you scale by adding more power (CPU, RAM) to a single server.

In horizontal scaling, you scale by simply adding more servers to your pool of servers.

For low-scale applications, vertical scaling is a great option because of its simplicity. But vertical scaling has a hard limit. It is practically not possible to add unlimited RAM, CPU, and memory to a single server. 

Because of this, it is recommended that you go for horizontal scaling (also known as sharding) for large-scale applications.

### Database replication

This is the process of copying data from your central database to one or more databases.

You do database replication using primary-replica (formerly known as master-slave) architecture. The primary database generally only supports write operations. All the data modifying operations like insert or update will be sent to the primary database.

On the other hand, the replica databases get copies of the data from the primary database and only support read operations. All the data querying operations like read, fetch will be served by replica databases.

Advantages of database replication:

* **Performance Improvements**: Database replication improves performance significantly as all the writes and updates happen in the primary node and all the read operations are distributed to replica nodes, thereby allowing more queries to run in parallel.
* **High Availability**: Since we create replicas of data across different nodes available in different parts of the world, the application remains functional even if one database node goes offline as you can access data from other nodes. In case the failure occurs in the primary node, any one of the replica nodes will get promoted to a primary node and serve the write/update operations until the original primary node comes back online.

## Wrapping Up

That's it. Thanks for stopping by. I hope you found this article interesting and informative!

My DMs are always open if you want to discuss further on any tech topic or if you've got any questions, suggestions, or feedback in general:

* [Twitter](https://twitter.com/apoorv__tyagi)
* [LinkedIn](https://www.linkedin.com/in/apoorvtyagi/)
* [GitHub](https://github.com/apoorvtyagi)
* [Blog](https://apoorvtyagi.tech/)

Happy learning! 💻 😄

