---
title: What to consider for painless Apache Kafka integration
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T18:04:27.000Z'
originalURL: https://freecodecamp.org/news/what-to-consider-for-painless-apache-kafka-integration-df559e828876
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca635740569d1a4ca6eb0.jpg
tags:
- name: Apache Kafka
  slug: apache-kafka
- name: architecture
  slug: architecture
- name: big data
  slug: big-data
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adi Polak

  Apache Kafka’s real-world adoption is exploding, and it claims to dominate the world
  of stream data. It has a huge developer community all over the world that keeps
  on growing. But, it can be painful too. So, just before jumping head fir...'
---

By Adi Polak

Apache Kafka’s real-world adoption is exploding, and it claims to dominate the world of stream data. It has a huge developer community all over the world that keeps on growing. But, it can be painful too. So, just before jumping head first and fully integrating with Apache Kafka, let’s check the water and plan ahead for painless integration.

![Image](https://cdn-media-1.freecodecamp.org/images/DdJhig6V7tsyyPxWQThFzKGd6R-8dbmw3-nw)
_nPhoto by [Unsplash](https://unsplash.com/photos/5fNmWej4tAA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Helloquence</a> on <a href="https://unsplash.com/search/photos/computer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### What is it?

Apache Kafka is an open source framework for asynchronous messaging and it’s a distributed streaming platform. It is TCP based. The messages are persisted in topics. Message producers are called _publishers_ and message consumers are called _subscribers_.

Consumers can subscribe to **one or more topics** and consume all the messages in that topic. Messages are written into the topic partitions.

_Topics_ are always multilayer subscriber, they can have zero, one, or many consumers that subscribe to the data written to it. For each topic Kafka maintains a partition log. Metadata for the partition’s logs and topics are usually managed by Zookeeper.

If you would like to learn more about Kafka message delivery semantics — like, _at most once_, _at least once_ and _exactly once —_ read [here](http://bit.ly/2Shu9L5).

Many tech companies have already integrated Apache Kafka into their production as a **message broker, user activities tracking pipeline, metrics gatherer, log aggregation mechanism, stream processing device** and much more. Apache Kafka is written in Scala and Java.

#### Why Kafka?

* _Kafka provides **High Availability** and **Fault Tolerance** message logs._ Kafka clusters retain all published records. It is by default **persistent —** If you don’t set a limit for Kafka, it will keep records until it runs out of disk space. When **data loss** means awful failure for the product, this is essential for recovery.
* **Multiple Topic Consumers** — when configuring the consumers under multiple consumers groups, it helps to reduce the old bottleneck of sending the data to multiple applications for processing. Kafka is distributed, hence, it can send information to consumers from various physical machines/services instances. Replicating topics to a secondary cluster is also relatively easy using Apache Kafka’s mirroring feature, MirrorMaker — see an [example](http://bit.ly/2CsENsU) of mirroring data between two HDInsight clusters. **Just remember**, if multiple consumers are defined as part of the same group (defined by the group.id) the data will be balanced over all the consumers within the group.
* Kafka is **polyglot** — there are many clients in C#, Java, C, python and more. The ecosystem also provides a REST proxy which allows easy integration via HTTP and JSON.
* **Real-Time Handling** — Kafka can handle real-time data pipelines for real time messaging for applications.
* **Scalable** — due to distributed architecture, Kafka can scale out without incurring any downtime.
* and more…

### Let’s make integration with Kafka painless

![Image](https://cdn-media-1.freecodecamp.org/images/ltseK3C8ZbvxjNtH95aPcVfZhWGx1wCqoapf)

#### Here are 6 things to know before integrating:

**1 — Apache Zookeeper can become a pain point with a Kafka cluster**

In the past ( versions < 0.81) Kafka used Zookeeper to maintain offsets of each topic and partition. Zookeeper used to take part in the read path, where too frequent commits and too many consumers led to sever performance and stability issues.

On top of that, it is better to use commits manually with old Zookeeper-based consumers, since careless auto-commits could lead to data loss.

The newer versions of Kafka offer their own management, where the consumer can use Kafka itself to manage offsets. This means that there is a specific topic that manages the read offsets instead of Zookeeper.

Yet, Kafka still needs a cluster with Zookeeper, even in the later versions 2.+. Zookeeper is used to store Kafka configs (reassigning partitions when needed) and the Kafka topics API, like create topic, add partition, etc.

The load on Kafka is strictly related to the number of consumers, brokers, partitions and frequency of commits from the consumer.

![Image](https://cdn-media-1.freecodecamp.org/images/YHjRwjTTwgWD4nilJIADm7GF9KkNyZPWG4NG)

**2 — You shouldn’t send large messages or payloads through Kafka**

According to Apache Kafka, for better throughput, the max message size should be **10KB_._** If the messages are larger than this, it is better to check the alternatives or find a way to chop the message into smaller parts before writing to Kafka. Best practice to do so is using a message key to make sure all chopped messages will be written to the same partition.

**3 — Apache Kafka can’t transform data**

Many developers are mistaken and think that they can create Kafka parsers or do a data transformation over Kafka. However, Kafka does not enable transformation of data. If you are using Azure services, there is a great list of [data factories services](http://bit.ly/2Sk8rpS) that you can use to transform the data like [Azure Databricks](http://bit.ly/2Lv6uEm), [HDInsights Spark](http://bit.ly/2EK5EDp) and others that connects to Kafka.

Another solution is using [Apache Kafka stream](https://kafka.apache.org/documentation/streams/). This is actually a new API that is build on top of Kafka’s producer and consumer clients. It’s significantly more powerful and also more expressive than the Kafka consumer client.

The `[KafkaStreams](https://kafka.apache.org/10/javadoc/org/apache/kafka/streams/KafkaStreams.html)` client allows us to perform continuous computation on input coming from one or more input topics and sends output to zero, one, or more output topics. Internally a `KafkaStreams` instance contains a normal `[KafkaProducer](https://kafka.apache.org/10/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html)` and `[KafkaConsumer](https://kafka.apache.org/10/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)` instance that is used for reading input and writing output.

Another option is using Flink, check it out [here](https://www.baeldung.com/kafka-flink-data-pipeline).

**4 — Apache Kafka supports a binary protocol over TCP**

Apache Kafka communication protocol is TCP based. It doesn’t support MQTT or JMS or other non-based TCP protocols out of the box. However, many users have written adaptors to read data from those protocols and write to Apache Kafka. For example [kafka-jms-client](https://github.com/adispennette/apache-kafka-jms).

![Image](https://cdn-media-1.freecodecamp.org/images/ScLTW1xegqrB9bKdZwmPrT0WUgzsmRzycyFV)
_Simple TCP handshake_

**5 — Apache Kafka management / support and the steep learning curve**

As of today, there are limited _free_ UI based management system for Apache Kafka, and most the the DevOps I worked with are using scripting tools. However, it can be tedious for beginner to jump into Apache Kafka scripting tools without taking the time for training. The Learning curve is steep and takes some time to get moving and integrate into big running systems.

For experienced DevOps/ developers it might take a few months (2+) to fully understand how to integrate, support and work with Apache Kafka. It is important to learn how Kafka works in order to use the configuration in the way that will best suit the system’s needs.

Here’s a list of management tools that you can use for **almost free (**some are restricted to personal/community use):

* [KafkaTool](http://www.kafkatool.com/) — GUI application for managing and using **Apache Kafka** clusters.
* [Confluent platform](https://www.confluent.io/product/confluent-platform/) — full enterprise streaming platform solution.
* [KafDrop](https://github.com/HomeAdvisor/Kafdrop) — tool for displaying information such as brokers, topics, partitions, and even lets you view messages. It is a lightweight application that runs on Spring Boot and requires very little configuration.
* [Yahoo Kafka Manager](https://github.com/yahoo/kafka-manager) —another tool for monitoring Kafka, yet it offers much less than the rest.

**Supporting Managed Kafka on the cloud**

Today almost all clouds support Kafka, if it is fully managed or using integration with Confluent from the cloud store up to just purchasing Kafka machines:

* [Confluent Cloud- Kafka as a Service](https://www.confluent.io/confluent-cloud/)
* [Azure Event Hub](http://bit.ly/2Ah5MGo)- fully managed Kafka
* [Managed Kafka on HDInsight — Azure](http://bit.ly/2BEpPyp)
* [Kafka Machine on Google cloud](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/kafka?pli=1)
* [Kafka on AWS using Confluent solution](https://aws.amazon.com/quickstart/architecture/confluent-platform/)
* ... many more

**6 — Kafka is no magic — There is still a possibility of data loss**

Apache Kafka is probably the most popular tool for distributed asynchronous messaging. This is mainly due to his **high throughput, low latency, scalability, centralised and real time** abilities. Most of this is due to using data replicas which in Kafka are called partitions.

However, with misconfiguration there is a high chance of _data loss_ when machines/processes are failing, and they will fail. Therefore, it’s important to understand how Kafka works and what the product/system requirements are.

**7 — Kafka built-in failure testing framework Trogdor**

To assist you in finding the right configuration, the Kafka team created [Trogdor](https://cwiki.apache.org/confluence/display/KAFKA/Fault+Injection). Trogdor is a failure testing framework.

**How it works**

* Configure Kafka the way you would in production
* Create a producer that generates messages with sequence 1…X million.
* Run the producer
* Run the consumer
* Create failure by crashing and/or hanging broker.
* Test and check that every event produced was consumed.
* … if that’s not the case, it is better to go back and update the configuration accordingly!

#### On top of that, it is important to remember that Apache Kafka …

* Is **_not a RPC_** —Apache Kafka is a messaging system. For RPC, service X needs to be aware of Service Y and the call signature. For example, in Kafka, if you send a message it doesn't mean that someone will consume it, ever. In RPC, there is always a consumer since the service itself is aware of the consumer Y and creates a call to its signature/function.
* It is **_not a Database_** — it’s not a good place to save messages since you can’t jump between them or create a search without an expensive full scan.

#### Just a word about KSQL

An interesting library brought to us by the Confluent Community is [KSQL](https://github.com/confluentinc/ksql). It is build on top of Kafka stream. KSQL is a completely interactive SQL interface. You can use it without writing any code. KSQL is under the Confluent Community licensing.

### TL;DR

Apache Kafka has many benefits, yet before adding it in production, one should be aware that:

* It has a steep learning curve — make time to learn the bits and bits of Kafka
* You must manage cluster resources — be aware of the requirements like Zookeeper
* You can still lose data with Apache Kafka
* Most clouds provide managed Apache Kafka
* It won’t transform data
* It’s not a Database
* It support binary protocol over TCP protocol
* At the moment, you can’t sent large messages using Kafka
* You should use Trogdor for fault testing of your system

All that being said, Apache Kafka is probably the best tool for messaging and streaming tasks.

Thank you [Gwen Shapira](https://www.freecodecamp.org/news/what-to-consider-for-painless-apache-kafka-integration-df559e828876/undefined) for your input and guidance along the way.

If you enjoyed this story, please click the ? button. Feel free to leave a comment below.

![Image](https://cdn-media-1.freecodecamp.org/images/aPn5w0kq5WP9lvUQ2a7dF1Yx-bUxVfvMDO1i)

[Follow me](https://medium.com/@adipolak) here, or [here](https://twitter.com/adipolak) for more posts about Scala, Kotlin, Big data, clean code and software engineers nonsense. Cheers!

