---
title: Stateful vs Stateless Architecture – Explained for Beginners
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-08-21T21:08:59.000Z'
originalURL: https://freecodecamp.org/news/stateful-vs-stateless-architectures-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/cover-photo.png
tags:
- name: architecture
  slug: architecture
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: 'In programming, "state" refers to the condition of a system, component,
  or application at a particular point in time.

  As a simple example, if you are shopping on amazon.com, whether you are currently
  logged into the site or if you have anything store...'
---

In programming, "state" refers to the condition of a system, component, or application at a particular point in time.

As a simple example, if you are shopping on amazon.com, whether you are currently logged into the site or if you have anything stored in your cart are some examples of state.

State represents the data that is stored and used to keep track of the current status of the application. Understanding and managing state is crucial for building interactive and dynamic web applications.

The concept of a “state” crosses many boundaries in architecture. Design patterns (like REST and GraphQL), protocols (like HTTP and TCP), firewalls and functions can be stateful or stateless. But the underlying principle of “state” cutting across all of these domains remains the same.

This article will explain what state means. It will also explain stateful and stateless architectures with some analogies and the benefits and tradeoffs of both.

## What is Stateful Architecture?

Imagine you go to a pizza restaurant to eat some food. In this restaurant, there is only a single waiter, and the waiter takes detailed notes on your table number, what you ordered, your preferences based on past orders, like what type of pizza crust you like or toppings you are allergic to, and so on.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3d2bd50-8945-4fb4-b36a-1d4730beebe5_1726x1080.png align="left")

*Illustration of a waiter taking a person's order at a pizza restaurant*

All of these pieces of information that the waiter writes down in their notepad are the customer's state. Only the waiter serving you has access to this information. If you want to make a change to your order or check how its coming along, you need to speak to the same waiter that took your order. But since there is only one waiter, that is not a problem.

Now, suppose the restaurant starts to get busier. Your waiter has to respond to other guests so more waiters are called to work. You now want to check the status of your order and make a small change to it – a plain crust instead of a cheesy crust. The only available waiter is different from the one who initially took your order.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b483849-6dc8-4a90-a491-199150d71547_1566x1020.png align="left")

*Illustration showing a different waiter being unable to help the customer change their order*

This new waiter does not have details of your order, that is your state. Naturally, they will not be able to check the status of your order or make changes to it. A restaurant that operates like this, where only the waiter that initially took your order can give you updates about it, or make changes to it, follows a stateful design.

Similarly, a stateful application will have a server that remembers clients' data (that is, their state). All future requests will be routed to the same server using a load balancer with sticky sessions enabled. In this way, the server is always aware of the client.

The diagram below shows two different users trying to access a web server through a load balancer. Since the application state is maintained on the servers, the users must always be routed to the same server for every single request in order to preserve state.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd494a45c-284b-4dd8-a6f1-5eb072157c70_1028x834.png align="left")

*Diagram showing how a stateful application works*

Sticky sessions is a configuration that allows the load balancer to route a user's requests consistently to the same backend server for the duration of their session. This is in contrast to [traditional load balancing](https://lightcloud.substack.com/i/102200211/load-balancing-explained), where requests from a user can be directed to any available backend server in a round-robin or other load distribution pattern.

What is the problem with a stateful architecture? Imagine a restaurant run in this manner. While it may be ideal and easy to implement for a small, family run restaurant with only a few customers, such a design is **not fault tolerant** and **not scalable**.

What happens if the waiter who took a customer's order has an emergency and needs to leave? All the information regarding that order leaves with that waiter as well. This disrupts the customer’s experience, since any new waiter brought in to replace the old one has no knowledge of previous orders. This is a design that is not fault tolerant.

Also, having to distribute requests so that the same customer can only speak to the same waiter means that the load on different waiters is not equally distributed. Some waiters will be overwhelmed with requests if you have a very demanding customer who always modifies or adds things to their order. Some of the other waiters will have nothing to do, and can’t step in to help. Again, this is a non scalable design.

Similarly, storing state data for different customers on different servers is not fault tolerant and not scalable. A server failure will lead to loss of state data. So, if a user is logged in and about to checkout for a large order on Amazon.com for example, the user will be forced to re-authenticate and the user's basket will be empty. They would have to log in again and fill up their basket from scratch – a poor user experience.

Scalability will also be difficult to achieve during peak times like Black Friday with a stateful design. New servers will be added to the [auto scaling group](https://lightcloud.substack.com/i/102200211/auto-scaling-explained) but since sticky sessions are enabled, clients will be routed to the same server, causing them to be overwhelmed, which can cause an increase in response times - a poor user experience.

Stateless architectures solve a lot of these problems.

## What is Stateless Architecture?

“Stateless” architecture is a confusing term, as it implies the system is without state. A stateless architecture does not, however, mean that state information is not stored. It simply means that state information is stored outside of the server. Therefore, the state of being stateless only applies to the server.

Bringing back the restaurant analogy, waiters in a stateless restaurant can be thought of as having perfectly forgetful memories. They do not recognise old customers, and can’t recall what you ordered or how you like your pizza. They will simply take note of customers' orders on a separate system, say a computer, that is accessible by all the waiters. They can then revert back to the computer to get details of an order and make changes to it as required.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bc5ab03-b96a-4e4b-b27e-ad9077a4bdc3_1852x932.png align="left")

*Illustration of a "forgetful" waiter taking an order and then consulting the computer about orders*

By storing the ‘state’ of a customer's order on a central system accessible by other waiters, any waiter can serve any customer.

In a stateless architecture, HTTP requests from a client can be sent to any of the servers.

State is typically stored on a separate database, accessible by all the servers. This creates a fault tolerant and scalable architecture since web servers can be added or removed as needed, without impacting state data.

The load will also be equally distributed across all servers, since the load balancer will not need a sticky session configuration to route the same clients to the same servers.

The diagram below shows two different users trying to access a web server through a load balancer. Since the application state is maintained separately from the servers, the users can be routed to any of the servers, which will then get the state information from an external database accessible by both servers.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F360b7c09-6e3c-4443-a05b-b58f70dc0039_1322x804.png align="left")

*Illustration showing a diagram of stateless architecture*

Typically, state data is stored in a cache like [Redis](https://redis.io/), an in-memory data store. Storing state data in-memory improves read and write times, compared to storing it on disk, as explained [here](https://lightcloud.substack.com/i/81969975/compute-memory-and-storage-an-analogy).

## Bringing it Together

This article has described how stateful and stateless web applications work and the trade-offs of both. But the principle of statefulness and statelessness apply beyond web applications.

If we look at network protocols as an example, HTTP is a stateless protocol. This means that each HTTP request from a client to a server is **independent** and carries **no knowledge of previous requests** or their context. The server treats each request as a separate and isolated transaction, and it doesn't inherently maintain information about the state of the client between requests.

State is either maintained on the servers (stateful architecture) or in a separate database outside the servers (stateless architecture). The HTTP protocol itself does not maintain state.

Unlike the stateless nature of HTTP, [the TCP protocol](https://www.freecodecamp.org/news/tcp-vs-udp/) is connection-oriented and stateful. It establishes a connection between two devices (usually a client and a server) and maintains a continuous communication channel until the connection is terminated.

The same logic applies to firewalls as well, which can be stateful or stateless.

In AWS, a security group is a virtual firewall that controls inbound and outbound traffic for virtual machines or instances within a cloud environment. Security groups are stateful. When you allow a specific incoming traffic flow, the corresponding outgoing traffic flow is automatically allowed as well. In other words, the state of the connection is tracked.

Network Access Control Lists (NACLs) are used to control inbound and outbound traffic at the subnet level in AWS. NACLs are stateless. Being stateless means that you must explicitly define rules for both incoming and outgoing traffic.

Unlike security groups, where response traffic is automatically allowed when you allow incoming traffic, NACLs require you to define separate rules for inbound and outbound traffic.

Functions and design patterns can also be stateful or stateless.

The key principle behind something that is stateful is that it has perfect memory or knowledge of previous calls or requests, while something that is stateless has no memory or knowledge of previous calls or requests.

Hopefully you now have a good grasp of how stateful and stateless applications work and can decide which option is best for your applications.
