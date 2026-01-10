---
title: How to Create a NoSQL Database with RavenDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-09T15:06:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-nosql-database-with-ravendb
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-05-at-9.18.04-AM.jpg
tags:
- name: database
  slug: database
- name: NoSQL
  slug: nosql
seo_title: null
seo_desc: "By Nahla Davies\nIf you look at any website or application today, somewhere\
  \ under the hood there is a database. After all, we live in the world of Big Data.\
  \ And the volume of data is growing exponentially. \nWith so much data at hand,\
  \ we need ever more..."
---

By Nahla Davies

If you look at any website or application today, somewhere under the hood there is a database. After all, we live in the world of Big Data. And the volume of data is growing exponentially. 

With so much data at hand, we need ever more sophisticated ways to store it and process it. 

So job markets continue to be strong for most computer professionals [working remotely from home](https://www.freecodecamp.org/news/my-personal-tips-on-working-from-home-during-this-covid-19-season/), including database architects and database administrators. 

There are even more opportunities in data science and analytics. But you need a solid foundation in database programming to take advantage of these opportunities.

In this article, I'll introduce you to the RavenDB database management system. We'll review some essential RavenDB features and after that I'll walk you through setting up your first RavenDB database.

## What is RavenDB?

RavenDB is a cross-platform, distributed, ACID-compliant, document-based, NoSQL database that offers high performance while remaining fairly easy to use. 

Knowledge of data programming is also crucial for web and software development, which has become one of the [most lucrative remote working jobs](https://www.waveapps.com/freelancing/web-development/back-end-web-developer-salary) in the United States today. 

## RavenDB Features

To use RavenDB effectively, you should understand how each of its features works and why they're important.

### Cross-platform

RavenDB is available for Windows, Linux, and Raspberry Pi. Mac users can run RavenDB within the Docker container system. 

This gives developers great flexibility when developing databases and associated applications.

### Distributed database

Generally speaking, a distributed database hosts data in multiple physical locations (for example, different sites or computers). 

While the specifics of RavenDB's distributed architecture are beyond the scope of this article, you should understand two of its fundamental elements: clusters and nodes.

**Clusters** are collections of an odd number of machines, with a minimum of three. Each machine in the cluster is a **node**. Databases can spread across one or more nodes in the cluster. In some instances, an entire database may be present on each node in a cluster. 

In addition to data distribution, clusters self-manage distribution of work, along with failure and recovery efforts.

Distributed database architecture allows for high transaction throughput, that is, high performance. RavenDB can handle up to 150,000 writes and 1 million reads per second. 

Distributed architecture also is more resilient when failures occur compared to traditional relational databases. 

The distributed architecture of NoSQL databases (see below) makes them useful for developing mobile applications. Still, you should remain vigilant against mobile security risks, as [89% of mobile device vulnerabilities](https://tokenist.com/mobile-device-security/) do not require physical access to the mobile device.

### ACID-compliant

ACID is an acronym for a set of database properties that help ensure the reliable processing of database transactions: 

* **Atomicity** ensures that every database transaction is treated as a single unit, no matter how many statements the transaction includes. Atomicity prevents problematic partial updates. During processing, transactions either succeed or fail as units. If a single statement within the transaction fails, the entire transaction fails. Other database clients can never perceive a transaction to be partially resolved. 
* **Consistency** ensures that transactions comply with all data validation rules in the database. If a transaction generates non-compliant data, the database rolls back to the prior valid version. 
* **Isolation** ensures that when multiple transactions take place concurrently, the transactions do not affect each other and do not attempt to use data from an in-process transaction. The final database update for a set of concurrent transactions is the same as if each transaction was processed in series.
* **Durability** prevents the loss of completed transaction data, even in the event of post-processing system failures. Completed transaction data becomes permanent in the database system, typically in non-volatile memory.

Most NoSQL databases are not ACID-compliant. RavenDB is an exception, [using ACID principles to drive high performance](https://www.ibm.com/docs/en/cics-ts/5.4?topic=processing-acid-properties-transactions) while also ensuring data integrity and reliability.

### NoSQL

The value of NoSQL versus SQL if often debated. For our purposes, we can simplify the difference. 

In traditional relational databases, SQL programming dominates. In non-relational, distributed databases, NoSQL reigns. 

SQL databases rely on tables. NoSQL databases can use other bases, including documents (as RavenDB does), dynamic tables, key-value pairs, and more.

NoSQL databases rely on distributed architecture to scale horizontally. As the database size increases, it is split among several different nodes in a cluster. SQL databases scale vertically – more data requires larger servers.

Searches are also frequently faster in NoSQL databases. Whereas SQL database queries rely on joins or combinations of data from multiple tables into a new table, NoSQL queries typically do not need joins. 

Since many NoSQL implementations are cloud-based, developers must always keep [encryption of their databases](https://www.freecodecamp.org/news/understanding-encryption-algorithms/) and applications front of mind for security purposes.

### Document-based

Document-based does not mean that Raven only stores PDFs or word processing documents. For the purposes of NoSQL databases, a document is a collection of structured (actually semi-structured) [self-contained data](https://ravendb.net/articles/nosql-document-oriented-databases-detailed-overview). 

You can use one of several languages to code the documents that will eventually reside in the NoSQL database, including Extensible Markup Language (XML) and JavaScript Object Notation (JSON). RavenDB primarily uses JSON documents.

Document-based databases are generally more efficient than their relational counterparts because they store all information about an object in a single document instance rather than spread across multiple tables. This structure increases database efficiency, as it does not require object-relational mapping.

## How to Create a New RavenDB Database

It's relatively simple to create a new RavenDB database. But before creating a database, you first need to install the RavenDB system. 

You can [download RavenDB on its website](https://ravendb.net/) depending on your chosen operating system (Windows, Linux, or [Raspberry Pi](https://www.raspberrypi.org/software/)), and there's a Docker version for Mac users. 

Installation is quick and easy. You must select whether you want to use a secure or non-secure version. 

Secure versions require you to either have or obtain a security certificate, but getting one through RavenDB is also painless. Free certificate licenses are available for the entry-level version of RavenDB.

Once you have installed RavenDB, only a few steps remain before you are working in your first database:

1. Login to your RavenDB application and go to your dashboard.
2. You will see a menu item for Databases on the dashboard, which you will click to start the process.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-05-at-9.18.04-AM-1.jpg)

3.   The window that opens includes a dropdown to search for existing databases, a search box, and a New database button. Click on it.

4.   Once you have opened the new database, you must name it. Names may be as long as 128 characters, including letters, numbers and a limited selection of special characters (“-”, “_”, “.”).

5.   After naming your database, you must assign a replication factor, which specifies distribution of your data across nodes. A replication factor of one means all data is in a single node. For settings above 1, you can choose between dynamic distribution or manual replication node setting (with the appropriate license).

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-05-at-9.22.36-AM.jpg)

6.   After completing these steps, you will return to the main database window. All that is left to do is click on the database name, and you are ready to begin creating documents.

For true beginners, RavenDB offers users the option to populate an empty database with sample data so that you can get a better feel for how to work in the database.

## Wrap-up

RavenDB is a powerful, robust, easy-to-use and easy-to-learn [NoSQL database system](https://www.freecodecamp.org/news/nosql-databases-5f6639ed9574/). 

For users looking to improve their database design and administration skills, RavenDB is a user-friendly training ground.  


  
  

