---
title: Here’s what makes Apache Kafka so fast
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T19:50:39.000Z'
originalURL: https://freecodecamp.org/news/what-makes-apache-kafka-so-fast-a8d4f94ab145
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P6PWPLZ7vv1LzN2jo1lNvA.png
tags:
- name: big data
  slug: big-data
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kartik Khare

  What is Apache Kafka?

  Apache Kafka is a distributed streaming platform, which allows you to:


  Publish and subscribe to streams of records, similar to a message queue or enterprise
  messaging system.

  Store streams of records in a fault-...'
---

By Kartik Khare

#### What is Apache Kafka?

[Apache Kafka](https://kafka.apache.org/) is a distributed streaming platform, which allows you to:

* Publish and subscribe to streams of records, similar to a message queue or enterprise messaging system.
* Store streams of records in a fault-tolerant durable way.
* Process streams of records as they occur.

If you haven’t used Kafka before, you can head here to [quick start](https://kafka.apache.org/quickstart) and come back to this article once you have become familiar with the use case.

Kafka supports a high-throughput, highly distributed, fault-tolerant platform with low-latency delivery of messages. Here, we are going to focus on the low-latency delivery aspect.

#### Low latency in I/O = Filesystem?

Most traditional data systems use random-access memory (RAM) as their data store, as RAM provides extremely low latencies.

Although this approach makes them fast, the cost of RAM is much more than disk. Such systems are usually costlier to run when you have 100s of GBPS data flowing through the system.

Kafka relies on the filesystem for the storage and caching. The problem is disks are slower than RAM. This is because the seek-time through a disk is large compared to the time required for actually reading the data.

But if you can avoid seeking, then you can achieve latencies as low as RAM in some cases. This is done by Kafka through **Sequential I/O**.

One advantage of Sequential I/O is you get a cache without writing any logic in your application for it. Modern operating systems allocate most of their free memory to disk-caching. So, if you are reading in an ordered fashion, the OS can always read-ahead and store data in a cache on each disk read.

This is much better than maintaining a cache in a JVM application. This is because JVM objects are “heavy” and can lead to high garbage collection, which becomes worse as data size increases.

#### Don’t use trees

Most modern databases use one form of [tree data structure](https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c) or another for persistent data storage. For example, MongoDB uses [BTree](https://en.wikipedia.org/wiki/B-tree), while Cassandra uses [LSM tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree).

These structures provide [O(log N) search performance](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/).

For a messaging system which requires many read and write operations to be performed simultaneously, using trees can lead to a lot of random I/O. This results in lot of disk seeks — which is disastrous for performance.

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is a much better data structure for a messaging system. Most of the time, data is appended to the system, and reads are simple. All such operations are O(1) — which is much more performant.

#### Don’t copy!

One of the major inefficiencies of data processing systems is the [serialization and deserialization](https://en.wikipedia.org/wiki/Serialization) (translating into formats suitable for storing and transmitting) of data during transfers.

This can be made faster by using better binary data formats, such as protocol buffers or Flat buffers, instead of JSON.

But how can you avoid serialization/deserialization altogether?

Kafka tackles this in two ways :

1. Use a standardized binary data format for [producers, brokers and consumers](https://kafka.apache.org/documentation/#api) (so data can be passed without modification)
2. Don’t copy the data in application (“zero-copy”)

The first one is self explanatory. It’s the second one which needs attention.

A common data transfer from file to socket might go as follows:

1. The OS reads data from the disk into pagecache in the kernel space
2. The application reads the data from kernel space into a user-space buffer
3. The application writes the data back into kernel space into a socket buffer
4. The OS copies the data from the socket buffer to the NIC buffer, where it is sent over the network

However, if we have the same standardized format for data which doesn’t require modification, then we have no need for step 2 (copying the data from kernel space to user-space).

If we keep data in the same format as it will be sent over the network, then we can directly copy data from pagecache to NIC buffer. This can be done through an OS [sendfile system call](http://man7.org/linux/man-pages/man2/sendfile.2.html).

More details on the zero-copy approach can be found in this [article](https://www.ibm.com/developerworks/linux/library/j-zerocopy/).

#### What else?

Kafka uses many other techniques apart from the ones mentioned above to make systems much faster and efficient:

1. Batching of data to reduce network calls, and also converting a lot of random writes into sequential ones.
2. Compression of batches (and not individual messages) using [LZ4](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm)), [SNAPPY](https://en.wikipedia.org/wiki/Snappy_(compression)) or [GZIP](https://en.wikipedia.org/wiki/Gzip) codecs. Much of the data is consistent across messages within a batch (for example, message fields and metadata information). This can lead to better compression ratios.

To learn more about Kafka’s design, you can refer to their [official article](https://kafka.apache.org/0102/documentation.html#majordesignelements).

Important to note is that all of the above techniques can be applied in most of the systems to achieve low-latencies. They don’t involve meddling with the kernel, tuning the garbage collection, using native applications, or using extreme data structures.

One downside, though, is that some of these techniques are specific to cases similar to a messaging platform. They would not be suitable for a more general distributed database.

**_If you are curious about more designs like this or if you have any opportunity, connect with me on [LinkedIn](http://www.linkedin.com/in/kartik-khare) or [Facebook](https://www.facebook.com/KK.corps) or drop a mail to [kharekartik@gmail.com](mailto:kharekartik@gmail.com)_**

