---
title: AWS DynamoDB – NoSQL Database Guide for Beginners
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-01-11T16:50:00.000Z'
originalURL: https://freecodecamp.org/news/aws-dynamodb-database-guide-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/dynamodb.png
tags:
- name: AWS
  slug: aws
- name: database
  slug: database
- name: NoSQL
  slug: nosql
seo_title: null
seo_desc: 'What is DynamoDB?

  DynamoDB is a fully managed NoSQL database from AWS. DynamoDB is similar to other
  NoSQL databases like MongoDB, except for the fact that you don’t have to do any
  maintenance or scaling on your part.


  DynamoDB can handle more than 10...'
---

## What is DynamoDB?

DynamoDB is a fully managed [NoSQL database](https://www.mongodb.com/nosql-explained) from AWS. DynamoDB is similar to other NoSQL databases like MongoDB, except for the fact that you don’t have to do any maintenance or scaling on your part.

> DynamoDB can handle more than 10 trillion requests per day and can support peaks of more than 20 million requests per second — via AWS Documentation.

DynamoDB offers built-in security, on-demand, and point-in-time backups, cross-region replication, in-memory caching, and many other features that support business-critical workloads. 

Most importantly, DynamoDB works seamlessly with other AWS applications like S3 and Lambda.

But before we get into the article, it's important that you understand the concept of NoSQL databases.

## What are NoSQL Databases?

NoSQL stands for “**not only SQL**”. Simply put, NoSQL databases store documents in a format similar to JSON, while relational databases store data in the form of a table. 

NoSQL offers more flexibility in terms of data modeling and does not force you to have a schema to store documents. 

A few types of NoSQL databases include pure document databases (like MongoDB), key-value stores (like DynamoDB), wide-column databases (like Cassandra), and graph databases (like Neo4j). [Learn more about NoSQL databases here](https://www.couchbase.com/resources/why-nosql).

Great. Now let’s look at some of the features of DynamoDB.

## Core Features of DynamoDB

### Autoscaling

Probably the most important feature of DynamoDB is that it delivers automatic scaling of throughput and storage based on the performance or usage of your application. 

In a typical database server, the sysadmin takes care of scaling when the application encounters higher than usual traffic. 

With DynamoDB, you can create database tables that can store and retrieve any amount of data, and the scaling is automatically managed by AWS. This includes scaling up for higher traffic and scaling down for lower traffic, so you only pay for what you use.

### Data Models

DynamoDB supports both key-value and document data models. This enables you to have a flexible schema, so each row can have any number of columns at any point in time. This is crucial for growing businesses that have ever-changing requirements.

Re-defining database schema is a nightmare that many developers/database admins go through in a growing application. This data model flexibility offers a robust database solution for small as well as large businesses.

### Replication

AWS takes care of DynamoDB table replication automatically based on your choice of AWS regions (cross-region replication). Even distributed applications can have single-digit millisecond read and write performance using DynamoDB.

With replication in place, you don't have to worry about data availability. In the event of the primary source failure, you can easily access the data from a secondary reserve, reducing the probability of application downtime.

### Backups & Recovery

DynamoDB provides on-demand backups for your tables that you can enable within the AWS console. You can also enable automatic backup and archiving of your data to other AWS solutions like S3.

DynamoDB also offers Point-in-time recovery. This protects your data from accidental write/delete operations. 

With Point-in-time recovery, you can restore your database to any point in time for the last 35 days. Point-in-time recovery is achieved by storing incremental backups of your database and that is managed automatically by AWS.

### Security

DynamoDB encrypts data at rest by default and also in transit using the keys stored in AWS Key Management Service (or customer-provided keys). 

With encryption in place, you can build security-sensitive applications that meet compliance and regulatory requirements. DynamoDB also provides access control via [AWS IAM roles.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

### Monitoring

Monitoring is crucial to any business-critical application. It helps maintain reliability and also notifies personnel in case of an event or failure. 

AWS offers detailed monitoring tools like CloudWatch Logs, CloudWatch Events, and CloudTrail Logs that will help you to watch, notify, and debug all types of events in DynamoDB. You can also set custom triggers based on metrics like system errors, capacity usage, and so on.

Now let’s compare DynamoDB with two of the popular database alternatives — MySQL and MongoDB.

## DynamoDB vs MySQL

There is a major difference between MySQL and MongoDB because MySQL is a relational database. In terms of benefits, I think MySQL is limited because of the requirement of having a schema before you can start pushing data.

But MySQL is great for many use cases as well. It is often called “The world’s most popular open-source database” and it delivers a fast, multi-threaded, multi-user, and robust SQL (Structured Query Language) database server.

But being a NoSQL database gives DynamoDB much more flexibility in terms of data modeling. 

Even though AWS provides managed services for MySQL and other relational databases, DynamoDB is a database designed by AWS and not just a hosted database solution. So this offers more improvements and features that MySQL and other relational databases can’t.

## DynamoDB vs MongoDB

DynamoDB and MongoDB are closely related to each other since both are NoSQL databases. But since DynamoDB is built and maintained by AWS it offers many more features and integrations, especially with other Amazon services like S3, compared to MongoDB.

If I were running a growing company I would prefer using DynamoDB solely because of its scalability and cross-region replication features. AWS does not offer a managed MongoDB service but if you are looking for one, [MongoDB Atlas](https://www.mongodb.com/atlas/database) would be a great alternative.

Another important feature of DynamoDB over MongoDB is that MongoDB is not secure by default and you have to configure security yourself. DynamoDB is secure by default, so it might be a better option if security is a deal-breaker for you.

## Wrapping Up

AWS DynamoDB is a fully managed NoSQL database that can scale in and scale out based on demand. AWS takes care of typical functions including software patching, replication, and maintenance. 

DynamoDB also offers encryption at rest, point-in-time snapshots, and powerful monitoring capabilities. In a nutshell, it is a great option when you are building an application that needs a high-performance scalable NoSQL database.

_Loved this article?_ [**_Join my Newsletter_**](http://tinyletter.com/manishmshiva) _and get a summary of my articles and videos every Monday_ morning_._ You can also [**visit my blog here.**](https://www.hardcoder.io/)

