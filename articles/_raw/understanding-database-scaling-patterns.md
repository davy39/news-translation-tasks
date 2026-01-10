---
title: A guide to understanding database scaling patterns
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T17:07:05.000Z'
originalURL: https://freecodecamp.org/news/understanding-database-scaling-patterns
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/database-1954920_1920.jpg
tags:
- name: coding
  slug: coding
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: scaling
  slug: scaling
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kousik Nath

  There are lot of articles online describing database scalability patterns, but they
  are mostly scattered articles — just techniques that are defined haphazardly without
  much context. I find that they are not defined in a step by step m...'
---

By Kousik Nath

There are lot of articles online describing database scalability patterns, but they are mostly scattered articles — just techniques that are defined haphazardly without much context. I find that they are not defined in a step by step manner, and don't discuss when to choose which scaling option, which scaling options are feasible in practise, and why. 

Therefore, I am planing to discuss some of the techniques in detail in future articles. To start, I feel it’s better if I discuss step by step techniques with some context in my own way. This article is a high level article — I will not discuss scaling techniques in details here, but will provide an overview. So let's get started.

### A case study

Assume you have built a startup which offers ride sharing at a cheap cost. Initially when you start, you target a city and hardly have tens of customers after your initial advertisement. 

You save all customers, trips, locations, bookings data, and customer trip history in the same database or most likely in a single physical machine. There is no fancy caching or big data pipeline to solve problems since your app is very new. This is perfect for your use case at this moment since there are very few customers and your system hardly books 1 trip in 5 minutes, for example.

But as time goes on, more people start signing up in your system since you are the cheapest service in the market and thanks to your promotion and ads. You start booking, say, 10 bookings per minute, and slowly the number increases to 20, 30 bookings per minute. 

At this point of time, you realize that the system has started performing poorly: API latency has increased a lot, and some transactions deadlock or starve and eventually they fail. Your app is taking more time to respond, causing customer dissatisfaction. What can you do to solve the problem?

## Pattern 1 - Query Optimization & Connection Pool implementation:

The first solution that comes in mind is that the cache frequently uses non-dynamic data like booking history, payment history, user profiles and so on. But after this application layer caching, you can’t solve the latency problem of APIs exposing dynamic data like the current driver's location or the nearest cabs for a given customer or current trip cost at a certain moment in time after the trip starts. 

You identify that your database is probably heavily normalized, so you introduce some redundant columns (these columns frequently appear in `WHERE` or `JOIN ON` clause in queries) in highly used tables for the sake of denormalization. This reduces join queries, breaks a big query into multiple smaller queries, and adds their results up in the application layer.

Another parallel optimization that you can do is tweaking around database connections. Database client libraries and external libraries are available in almost all programming languages. You can use connection pool libraries to cache database connections or can configure connection pool size in the database management system itself. 

Creating any network connection is costly since it requires some back & forth communication between client & server. Pooling connections may help you to optimize the number of connections. Connection pool libraries may help you to multiplex connections — multiple application threads can use the same database connection. I shall see if I can explain connection pooling in detail in a separate article later.

Your measure latency of your APIs & find probably 20–50% or more reduced latency. This is good optimization at this point in time.

You have now scaled your business to one more city, more customer sign up, you slowly start to do 80–100 bookings per minute. Your system is not able to handle this scale. Again you see API latency has increased, database layer has given up, but this time, no query optimization is giving you any significant performance gain. You check the system metric, you find disk space is almost full, CPU is busy 80% of the time, RAM fills up very quickly.

## Pattern 2 - Vertical Scaling or Scale Up:

After examining all system metrics, you know there is no other easy solution rather than upgrading the hardware of the system. You upgrade your RAM size by 2 times, upgrade disk space by, say, 3 times or more. This is called vertical scaling or scaling up your system. You inform your infrastructure team or devops team or third party data centre agents to upgrade your machine.

**But how do you set up machine for vertical scaling?**

You allocate a bigger machine. One approach is not to migrate data manually from old machine rather set the new machine as `replica` to the existing machine (`primary`)-make a temporary `primary replica` configuration. Let the replication happen naturally. Once the replication is done, [promote the new machine to primary](https://blog.pythian.com/mysql-recipes-promoting-a-slave-to-master-or-changing-masters/?source=post_page---------------------------) & take the older machine offline. Since the bigger machine is expected to serve all request, all read / write will happen on this machine.

Cool. Your system is up & running again with increased performance.

Your business is doing very well & you decide to scale to 3 more cities — you are now operational in 5 cities total. Traffic is 3x times than earlier, you are expected to do around 300 bookings per minute. Before even achieving this target booking, you again hit the performance crunch, database index size is increasing heavily in memory, it needs constant maintenance, table scanning with index is getting slower than ever. You calculate the cost of scaling up the machine further but not convinced with the cost. What do you do now?

## Pattern 3 - Command Query Responsibility Segregation (CQRS):

You identify that the big machine is not able to handle all `read/write` requests. Also in most of the cases, any company needs transactional capability on `write` but not on `read` operations. You are also fine with a little bit of inconsistent or delayed `read` operations & your business has no issue with that either. You see an opportunity where it might be a good option to separate the `read` & `write` operations physical machine wise. It will create scope for individual machines to handle more `read/write` operations. 

You now take two more big machines & set them up as `replica` to the current machine. Database replication will take care of distributing data from `primary` machine to `replica` machines. You navigate all read queries (Query (`Q`) in `CQRS`) to the replicas — any `replica` can serve any read request, you navigate all write queries (Command (`C`) in `CQRS`) to the `primary`. There might be little lag in the replication, but according to your business use case that’s fine.

Most of the medium scale startups which serve few hundred thousand requests everyday can survive with primary-replica set up provided that they periodically archive older data.

Now you scale to 2 more cities, you see that your `primary` is not able to handle all `write` requests. Many `write` requests are having latency. Moreover, the lag between `primary` & `replica` sometimes impact customers & drivers ex — when trip ends, customer pays the driver successfully, but the driver is not able to see the payment since customer’s activity is a `write` request that goes to the `primary`, while driver’s activity is a `read` request that goes to one of the replicas. Your overall system is so slow that driver is not able to see the payment for at least half a minute — frustrating for both driver & customer. How do you solve it?

## Pattern 4 - Multi Primary Replication

You scaled really well with `primary-replica` configuration, but now you need more write performance. You might be ready to compromise a little bit on `read` request performance. Why not distribute the write request to a `replica` also?

In a `multi-primary` configuration, all the machines can work as both `primary`& `replica`. You can think of `multi-primary` as a circle of machines say `A->B->C->D->A`. `B` can replicate data from `A`, `C` can replicate data from `B`, `D` can replicate data from `C`, `A` can replicate data from `D`. You can write data to any node, while reading data, you can broadcast the query to all nodes, whoever replies return that. All nodes will have same database schema, same set of tables, index etc. So you have to make sure there are no collision in `id` across nodes in the same table, otherwise during broadcasting, multiple nodes would return different data for the same `id`. 

Generally it’s better to use `UUID` or `GUID` for id. One more disadvantage of this technique is — `read` queries might be inefficient since it involves broadcasting query & getting the correct result — basically scatter gather approach.

Now you scale to 5 more cities & your system is in pain again. You are expected to handle roughly 50 request per second. You are in desperate need to handle heavy number of concurrent requests. How do you achieve that?

## Pattern 5 - Partitioning:

You know that your `location` database is something which is getting high `write` & `read` traffic. Probably `write:read` ratio is `7:3`. This is putting a lot of pressure on the existing databases. The `location` tables contain few primary data like `longitude`, `latitude`, `timestamp`, `driver id`, `trip id` etc. It does not have a much to do with user trips, user data, payment data etc. What about separating the `location` tables in a separate database schema? What about putting that database in separate machines with proper `primary-replica` or `multi-primary` configuration? 

This is called partitioning of data by functionality. Different database can host data categorized by different functionality, if required the result can be aggregated in the back end layer. Using this technique, you can focus on scaling those functionalities well which demand high `read/write` requests. Although the back end or application layer has to take the responsibility to join the results when necessary resulting in more code changes probably.

Now imagine you have expanded your business to a total of 20 cities in your country & planning to expand to Australia soon. Your increasing demand of app requires faster & faster response. None of the above method can help you to the extreme now. You must scale your system in such a way that expanding to other countries / regions does not always need you to do frequent engineering or architecture changes. How do you do that?

## Pattern 6 - Horizontal Scaling:

You do lot of googling, read a lot on how other companies have solved the issue — and come to the conclusion that you need to scale horizontally. You allocate say 50 machines — all have the same database schema which in turn contains the same set of tables. All the machines just hold a part of data. 

Since all databases contain same set of tables, you can design the system in such a way that locality of data is there i.e; all related data lands in the same machine. Each machine can have their own replicas, replicas can be used in failure recovery. Each of the databases is called `shard`. A physical machine can have one or multiple `shards` — it’s up to your design how you want. You need to decide on `sharding key` in such a way that a single `sharding key` always refers to the same machine. So you can imagine lot of machines all holding related data in same set of tables, `read/write` requests for the same row or same set of resource land in the same database machine.

Sharding is in general hard — at least engineers from different companies say that. But when you serve millions or billions of requests, you have to make such tough decision.

I will discuss `sharding` in greater detail in my next post, so holding back my temptation to discuss more in this post.

Now since you have sharding in place, you are confident that you can scale to many countries. Your business has grown so much that investors are pushing you to scale the business across continents. You again see some problem here. API latency again. Your service is hosted in USA & people from Vietnam are having difficult time book rides. Why? What do you do about it?

## Pattern 7 - Data Centre Wise Partition:

Your business is growing in America, South Asia & in few countries in Europe. You are doing millions of bookings daily with billions of request hitting your server. Congrats - this is a peak moment for your business. 

But since requests from the app have to travel across continents through hundreds or thousands of servers in the internet, the latency arises. What about distributing traffic across data centres? You can set up a data centre in Singapore that handles all requests from South Asia, data centre in Germany can handle all requests from European countries, and a California data centre can handle all USA requests. 

Also you enable cross data centre replication which helps disaster recovery. So if California data centre does replication to Singapore data centre, in case California data centre crashes due to electricity issue or natural calamity, all USA requests can fall back to Singapore data centre and so on. 

This scaling technique is useful when you have millions of customers to serve across countries and you can’t accommodate any data loss, you have to always maintain availability of the system.

These are some general step by step techniques for database scaling. Although most of the engineers don’t get enough chance to implement these techniques, but as a whole it’s better to get a broader idea about such system which in future may help you to do better system & architecture designing.

In my next articles, I will try to discuss some of the concepts in details. Please feel free to give appropriate feedback for this post if any.

The article is originally published on the author's medium account: [https://medium.com/@kousiknath/understanding-database-scaling-patterns-ac24e5223522](https://medium.com/@kousiknath/understanding-database-scaling-patterns-ac24e5223522)

