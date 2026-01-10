---
title: ScyllaDB is better than Cassandra, and here’s why.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T16:07:39.000Z'
originalURL: https://freecodecamp.org/news/scylladb-its-cassandra-but-better-76e3d83a4f81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yRMqqIGUndAm3sJbqIIq1g.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kartik Khare

  ScyllaDB is one of the newest NoSQL database which offers really high throughput
  at sub millisecond latencies. The important point is that it accomplishes this at
  a fraction of the cost of a modern NoSQL database.

  ScyllaDB implements ...'
---

By Kartik Khare

[ScyllaDB](https://www.scylladb.com/) is one of the newest NoSQL database which offers really high throughput at sub millisecond latencies. The important point is that it accomplishes this at a fraction of the cost of a modern NoSQL database.

ScyllaDB implements almost all of the features of [Cassandra](http://cassandra.apache.org/) in C++. But saying it’s a mere C++ port would be an understatement. Developers at Scylla have made a lot of changes under the hood which are not visible to the user but that lead to a huge performance improvement.

### You are kidding, right?

No, [I’m not](https://www.scylladb.com/product/benchmarks/aws-c3-2xlarge-benchmark/).

As you can see (if you went to that link), for most cases, Scylla’s 99.9 percentile latency is 5–10X better than Cassandra’s.

Also in the benchmarks mentioned [here](https://www.scylladb.com/product/benchmarks/ycsb-cluster-benchmark/), a standard 3 node Scylla cluster offers almost the same performance as a 30 node Cassandra cluster (which leads to a 10X reduction in cost).

### How is this possible?

The most important point is that Scylla is written in C++14. So, it’s expected to be faster than Cassandra which purely runs on JVM.

However, there have been lots of significant low level optimizations in Scylla which makes it better than its competition.

### Shared-Nothing Approach

Cassandra relies on threads for parallelism. The problem is that threads require a context switch, which is slow.

Also, for communication between threads, you need to take a lock on shared memory which again results in wasted processing time.

ScyllaDB uses the [seastar](http://www.seastar-project.org/) framework to shard requests on each core. The application only has one thread per core. This way, if a session is being handled by core 1 and a query request for that session comes to core 2, it’s directed to core 1 for processing. Any of the cores can handle the response after that.

The advantage of the shared nothing approach is that each thread has its own memory, cpu, and NIC buffer queues.

In cases when communication between cores can’t be avoided, Seastar offers asynchronous lockless inter-core communication which is highly scalable. These lockless primitives include Futures and Promises, which are quite commonly used in programming and so are developer friendly.

### Avoid kernel

When a row is found in an SSTable, it needs to be sent over the network to the client. This involves copying data from user space to kernel space.

However, Linux kernel usually performs multi-threaded locking operations which are not scalable.

ScyllaDB takes care of this by using Seastar’s network stack.

Seastar’s network stack runs in user space and utilises [DPDK](https://dpdk.org/) for faster packet processing. DPDK bypasses the kernel to copy the data directly to NIC buffer and processes a packet within 80 CPU cycles. (source: [DPDK Website](https://dpdk.org/))

### Don’t rely on Page Cache

Page cache is great when you have sequential I/O and data is stored in the disk in the wire format.

However, in Scylla/Cassandra, we have data in form of SSTables. Page cache stores data in the same format, which takes up a large chunk of memory for small data and needs serialization/deserialization when you want to transfer it.

ScyllaDB, instead of relying on page cache, allocates most of its memory to row-cache.

Row-Cache has the data in an optimised memory format which takes up less space and doesn’t need serialization/deserialization

Another advantage of using row cache is it’s not removed when compaction occurs while the page cache is thrashed.

These are the major optimizations in ScyllaDB which make it much faster, more reliable, and cheaper than Cassandra. Scylla has many other optimizations under the hood which can be found [here](https://www.scylladb.com/product/).

**_If you are curious about more designs like those above or if you want to get in touch, connect with me on [LinkedIn](http://www.linkedin.com/in/kartik-khare) or [Facebook](https://www.facebook.com/KK.corps) or drop an email to [kharekartik@gmail.com](mailto:kharekartik@gmail.com)_**

