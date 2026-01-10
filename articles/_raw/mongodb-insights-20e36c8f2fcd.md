---
title: How to decide if MongoDB is right for you
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-29T07:38:53.000Z'
originalURL: https://freecodecamp.org/news/mongodb-insights-20e36c8f2fcd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JkS75JaEP1Zk1aVJIMkdBQ.png
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
- name: NoSQL
  slug: nosql
- name: Productivity
  slug: productivity
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Luc Claustres

  For the past couple of years, I built web applications around MongoDB. In this short
  article I would like to answer some of the recurrent questions or misunderstanding
  most developers have when evaluating it:


  What is the licensing?

  ...'
---

By Luc Claustres

For the past couple of years, I built web applications around [MongoDB](https://www.mongodb.com/). In this short article I would like to answer some of the recurrent questions or misunderstanding most developers have when evaluating it:

* What is the licensing?
* What does it mean MongoDB is a NoSQL database?
* What about MongoDB performances?

![Image](https://cdn-media-1.freecodecamp.org/images/1*JkS75JaEP1Zk1aVJIMkdBQ.png)

### Licensing

Yes, MongoDB is licensed under Free Software Foundation’s [GNU AGPL v3.0](https://www.mongodb.com/community/licensing). Practically, this means that enhancements you make to MongoDB must be released to the community. The source code of any derived work has to be distributed as well.

You might wonder if your application is a derived work. I must confess I never found a simple definition of such a term. However, in the specific case of MongoDB, they simply [recognize that applications using their database are a separate work](https://www.mongodb.com/blog/post/the-agpl). Moreover, their supported drivers are released under [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0). This is a [permissive license](https://en.wikipedia.org/wiki/Permissive_software_licence). It does not require you to publish your source code, and your application usually only talks to MongoDB using a driver.

As a consequence, you don’t need to be concerned with the licensing of MongoDB to build your app around it. They even send signed letters asserting the promise to legal departments if there are questions. They also provide commercial licenses if the signed letter isn’t enough.

> Note: although a great deal of experience make me trust this analysis, I am not a lawyer. The view presented here is my personal understanding and is not an official one.

### NoSQL

Yes, MongoDB is a NoSQL database. This word can be pretty confusing. I will try to analyze the most common ideas with a focus on how this applies to MongoDB.

#### Document-oriented

In traditional SQL databases, data is arranged in the form of tables and rows. Each row has a fixed number of columns that can only store data of a specific type (e.g., Integer, Text, Datetime). This defines the _schema_ of your data.

In MongoDB, data is stored in the form of [BSON objects](http://bsonspec.org/) organized into _collections._ Data is usually handled in the form of [JSON objects](http://www.json.org/). This makes mapping objects into the database a simple task, _normally eliminating anything similar to an_ [_object-relational mapping_](https://en.wikipedia.org/wiki/Object-relational_mapping).

#### Transactional

Prior to v4, MongoDB provided only document-wide transactions. Writes were never partially applied to an inserted or updated document. The operation was atomic in the sense that it either fails or succeeds. For the document in its entirety, it was said to be [ACID](https://en.wikipedia.org/wiki/ACID_(computer_science)) at the document level. As a consequence, there was no possibility of atomic changes that span multiple documents. You had to emulate the required database transactions (e.g. using [2 phase commit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol)).

Since v4, MongoDB supports multi-document ACID transactions, making it the only open source database to combine the document model with ACID guarantees.

#### Schema-less (really?)

This means you don’t have to tell the database the structure of your data and the primitive types to be used before being able to manage it. This also means you can mix documents that have different structures in the same collection of data.

One of the great benefits is that _schema migrations become easier_ (most of the adjustments to the database are transparent and automatic). Rollback is unlikely to cause problems. Another advantage is that _dynamically extending existing data models with custom attributes at runtime is straightforward_.

But all this does not mean you don’t have any schema at all. If it is not **explicitly** declared, it shines **implicitly** from your application logic. It might be declared in other ways to handle form/data validation. Anyway, you still have to explicitly tell the database how to create indices to ensure good performance.

Indeed, schema design is the cornerstone of making awesome databases, whether SQL or not. If you do not understand your data and the limitations of hardware and software, you can not effectively design a schema.

#### Non-relational (really?)

This means that you don’t have to always create a relation between two documents to handle aggregated data structures.

Indeed, in relational databases, the SQL JOIN clause allows you to combine rows from two or more tables using a common field between them. Document-oriented databases such as MongoDB are designed to store **denormalized** data. Ideally, there should be no relationship between collections: if the same data is required in two or more documents, it must be repeated. One of the great benefits is that a _single read operation_ is required to get all data.

But you can still create relations and refer to another document if you’d like or have the need:

* by ID, then you can “populate” it manually with a second query or using [DBRefs](https://docs.mongodb.com/manual/reference/database-references/#dbrefs)
* by any other field, then you can use the `[$lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)`[operator](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)

This makes MongoDB really flexible and allows you to choose how to handle the relations between your objects _on a case-by-case basis_.

### Performance

#### Read/Write

Yes, MongoDB like any other “true” database is made to handle a huge volume of data. _In a nutshell, hundreds or thousands of objects is nothing for a database,_ so you don’t have to worry if you have such numbers. You can find a lot of benchmarks around. Here is a simple one to give you some rough order of magnitude. The documents stored are really simple and typically represent a time-stamped measurement:

```
{    value: random(0,100),    timestamp: date}
```

Because of the way MongoDB delegates memory management to the operating system, having more complex documents (typically containing tens of attributes) does not affect results significantly

Both attributes have been indexed. MongoDB automatically adds and indexes the document unique ID. I tested three requests:

* find the maximum value of the collection using the [aggregation framework](https://docs.mongodb.com/manual/aggregation/)
* find the 100 greatest values greater than 99.9
* get a single document by ID

The “maximum request” is not benefitting from indexes because of the aggregation, while the “greater than” and “by ID” requests can use it. You will see how this is important for performance.

The test configuration was MongoDB 3.4.1 64 bits — OS Windows 7 Pro SP1 — CPU Core i7–4712HQ 2.3GHz — 16Go RAM—SSD HD, and the test results were the following:

So if you build the correct indices querying a billion documents, it is still performant enough for most applications on a single server. If needed, you can increase performance using [sharding](https://docs.mongodb.com/manual/sharding/).

Here are the scripts used to create/query the database for this test:

And the run commands:

```
// Launch server./mongod --dbpath "C:\Program Files\MongoDB\Server\3.4\data" --port 27018// Insertion exemple for 10e7./mongo --port 27018 --eval "var arg1=10000000" create_collection.js// Requests./mongo --port 27018 --eval "" query_collection.js
```

#### Memory

Yes, MongoDB often looks like it uses all available RAM. It actually relies on different storage engines. [WiredTiger](https://docs.mongodb.com/manual/core/wiredtiger/) is the default starting in MongoDB 3.2, and [MMAPv1](https://docs.mongodb.com/manual/core/mmapv1/) is the default for MongoDB versions before 3.2. However, they work pretty similarly. Via the file system cache, they _automatically use all free memory that is not used by the engine cache or by other processes_. And this is coherent if you’d like to have maximum performances.

So system resource monitors often show that MongoDB uses a lot of memory, _but its usage is dynamic_. If another process suddenly needs half the server’s RAM, MongoDB will yield cached memory to the other process.

As a consequence, the single parameter you can tune to optimize memory usage is the engine cache size. For example, by default, the WiredTiger engine uses 50% of RAM minus 1 GB, which can be pretty large on servers with a lot of memory. This can even cause some trouble if you use containers with limited memory, [so simply find out the right balance for your use case](https://docs.mongodb.com/manual/faq/storage/#to-what-size-should-i-set-the-wiredtiger-internal-cache).

#### Conclusion

I hope you know have a more precise idea of the benefits provided by MongoDB if it suits your needs. Recently, MongoDB has started a Database as a Service offer called [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) that might be useful for you to test out.

_If you liked this article feel free to have a look at [our Open Source solutions](https://kalisio.com/#projects), the [Kalisio](https://kalisio.com/) team !_

