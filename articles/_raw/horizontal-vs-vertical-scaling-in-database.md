---
title: Horizontal vs. Vertical Scaling – How to Scale a Database
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2022-06-09T15:26:24.000Z'
originalURL: https://freecodecamp.org/news/horizontal-vs-vertical-scaling-in-database
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Tech-Blog-Cover.png
tags:
- name: vertical
  slug: vertical
- name: database
  slug: database
- name: Horizontal
  slug: horizontal
- name: scalability
  slug: scalability
- name: scaling
  slug: scaling
seo_title: null
seo_desc: "Data Scalability\nData scalability refers to the ability of a database\
  \ to manipulate changing demands by adding and removing data. In this way, the database\
  \ grows at the same pace as the software. \nVia scaling, the database can expand\
  \ or contract the ..."
---

## Data Scalability

Data scalability refers to the ability of a database to manipulate changing demands by adding and removing data. In this way, the database grows at the same pace as the software. 

Via scaling, the database can expand or contract the capacity of the system's resources to support the application's frequently changing usage.

**There are two ways a database can be scaled:**

* Horizontal scaling (scale-out)
* Vertical scaling (scale-up)

In this article, we'll look at both methods of scaling and discuss the advantages and disadvantages of each to help you choose.

## Horizontal Scaling

This scaling approach adds more database nodes to handle the increased workload. It decreases the load on the server rather than expanding the individual servers. 

When you need more capacity, you can add more servers to the cluster. Another name for this scaling method is **Scaling out**.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/scaling-out.jpg)

### Advantages of Horizontal Scaling:

* It is easy to upgrade
* It is simple to implement and costs less
* It offers flexible, scalable tools
* It has limitless scaling with unlimited addition of server instances
* Upgrading a horizontally scaled database is easy – just add a node to the server

### Disadvantages of Horizontal Scaling:

* Any bugs in the code will become more complex to debug and understand
* The licensing fee is expensive as you will have more nodes that are licensed
* The cost of the data center will increase significantly because of the increased space, cooling, and power required

### When to use horizontal scaling:

If you are dealing with more than a thousand users, it is best to use this scaling system because when the servers receive multiple user requests, everything will scale well.

It will also not crash because there are multiple servers.

## Vertical Scaling

The vertical scaling approach increases the capacity of a single machine by increasing the resources in the same logical server. This involves adding resources like memory, storage, and processing power to existing software, enhancing its performance. 

This is the traditional method of scaling a database. Another name for this approach is **Scale-up**.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/02vertical-scaling-software-scalability.jpg)

### Advantages of Vertical Scaling:

* The cost of the data center for the space, cooling, and power will be smaller
* It is a cost-efficient software
* It is easy to use and implement – the administrator can easily manage and maintain the software
* The resources for this approach are flexible

### Disadvantages of Vertical Scaling:

* The cost may be low, but you will need to pay for a license each time you scale up
* The hardware costs more because of high-end servers
* There is a limit to the amount you can upgrade
* You are restricted to a single database vendor, and migration is challenging, or you may need to start over

### When to use vertical scaling:

The vertical scaling approach is for you if you need a system with unique data consistency.

If you don't want to worry about balancing the server's workload, vertical scaling is the best option.

## Differences Between Vertical and Horizontal Scaling

<table>
<thead>
<tr>
<th style="text-align: left">Vertical</th>
<th style="text-align: left">Horizontal</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">The license costs less</td>
<td style="text-align: left">The license costs more</td>
</tr>
<tr>
<td style="text-align: left">This method increases the power of the server with additional individual servers</td>
<td style="text-align: left">This method increases the power of the server with the existing server</td>
</tr>
<tr>
<td style="text-align: left">This data is present on one single node, and it is scaled through a multicore</td>
<td style="text-align: left">This is based on partitioning each node that contains a single part of data</td>
</tr>
</tbody>
</table>

## Which scaling method is best for your app?

When choosing how to scale your database, you must consider what's at stake when you scale up and out. 

Now we'll take a look at some factors to consider so you can choose which scaling system is best for your app:

### Load balancing

The vertical scaling system is best for balancing loads because you have a single server (vertical scaling), and there is no need to balance your load. Horizontal scaling requires you to balance the workload evenly.

### Point of failure

The horizontal scaling system has more than one server, so when one server crashes, the next one picks up the slack. This means that there is no _single point of failure_ which makes the system resilient.

But in the vertical scaling system, there is only one server, so once the server crashes, everything goes offline.

### Speed

In terms of speed, the vertical scaling system is faster because, since it runs on one server, the vertical scaling system has an _interprocess communication_ – that is, the server communicates within itself and it's fast. 

The horizontal scaling system has network calls between two or more servers. This is also known as _Remote Procedure Calls (RPC)._ RPCs are slow, though.

### Data consistency

When dealing with servers, you'll need to make sure that the data stored in them is consistent when end users send a request. 

The vertical scaling system is data consistent because all information is on a single server. But the horizontal scaling system is scaled out with multiple servers, so data consistency can be a huge issue.

### Hardware limitations

The horizontal scaling system scales well because the number of servers you throw at a request is linear to the number of users in the database or server. The vertical scaling system, on the other hand, has a limitation because everything runs on a single server.

When choosing a system to scale your database, make sure to make a pros and cons list of the information in this article. It will help you decide which to use.

## Conclusion

A cloud computing model's scalability is the ability to quickly and instantly increase or decrease an IT capacity. Knowing how the two types of scaling work is crucial as this plays a massive role in your database or server management.

Quick recap...

* A server's role is to enhance its capacity to handle the increased workload, called **Vertical scaling.**
* A system's job is to add new nodes to manage the distributed workload, termed **Horizontal scaling.**
* The horizontal scaling system scales well as the number of users increases.
* The vertical scaling system is faster due to its ability to inter-process communication.

Thanks for reading!

