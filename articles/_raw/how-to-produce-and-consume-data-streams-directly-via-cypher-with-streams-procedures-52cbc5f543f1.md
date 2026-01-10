---
title: How to produce and consume data streams directly via Cypher with Streams Procedures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T17:13:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-produce-and-consume-data-streams-directly-via-cypher-with-streams-procedures-52cbc5f543f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*47Ktwi-Gdj5S7keZpiteZA.gif
tags:
- name: Apache Kafka
  slug: apache-kafka
- name: data
  slug: data
- name: Neo4j
  slug: neo4j
- name: streaming
  slug: streaming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Andrea Santurbano

  Leveraging Neo4j Streams — Part 3

  This article is the third part of the Leveraging Neo4j Streams series (Part 1 is
  here, Part 2 is here). In it, I’ll show you how to bring Neo4j into your Apache
  Kafka flow by using the streams pr...'
---

By Andrea Santurbano

#### Leveraging Neo4j Streams — Part 3

This article is the third part of the **Leveraging Neo4j Streams** series (Part 1 is [here](https://medium.freecodecamp.org/how-to-leverage-neo4j-streams-and-build-a-just-in-time-data-warehouse-64adf290f093), Part 2 is [here](https://medium.freecodecamp.org/how-to-ingest-data-into-neo4j-from-a-kafka-stream-a34f574f5655)). In it, I’ll show you how to bring Neo4j into your **Apache Kafka** flow by using the streams procedures available with [**Neo4j Streams**](https://medium.com/neo4j/a-new-neo4j-integration-with-apache-kafka-6099c14851d2).

In order to show how to integrate them, simplify the integration, and let you test the whole project by hand, I’ll use [**Apache Zeppelin**](https://towardsdatascience.com/building-a-graph-data-pipeline-with-zeppelin-spark-and-neo4j-8b6b83f4fb70)**, a notebook runner that simply allows you to [natively interact with Neo4j](https://towardsdatascience.com/building-a-graph-data-pipeline-with-zeppelin-spark-and-neo4j-8b6b83f4fb70).**

### What is a Neo4j Stored Procedure?

Starting from Neo4j 3.x, the concept of [**user-defined procedures and functions**](https://neo4j.com/docs/java-reference/current/extending-neo4j/procedures/) was introduced. These are custom implementations of certain functionalities and/or business rules that can’t be (easily) expressed in Cypher itself.

Neo4j provides a number of built-in procedures. The [APOC](http://neo4j-contrib.github.io/neo4j-apoc-procedures/) library adds another 450 to cover all kinds of uses from data integration to graph refactorings.

### What are the streams procedures?

The Neo4j Streams project comes out with two procedures:

* `streams.publish`: allows custom message streaming from Neo4j to the configured environment by using the underlying configured Producer
* `streams.consume`: allows consuming messages from a given topic.

### Set-Up the Environment

Going to the following [Github repo](https://github.com/conker84/leveraging-neo4j-streams), you’ll find everything necessary in order to replicate what I’m presenting in this article. What you will need to start is [**Docker**](https://docs.docker.com/), and then you can simply spin-up the stack by entering into the directory and from the Terminal execute the following command:

```
$ docker-compose up
```

This will start-up the whole environment that comprises:

* Neo4j + Neo4j Streams module + APOC procedures
* Apache Kafka
* Apache Spark (which is not necessary in this article, but it’s used in the previous two)
* Apache Zeppelin

By going into Apache Zeppelin @ `http://localhost:8080` you’ll find in directory `Medium/Part 3` one notebook called “**Streams Procedures**” which is the subject of this article.

### streams.publish

This procedure allows custom message streaming from Neo4j to the configured environment by using the underlying configured Producer.

It takes two variables as input and returns nothing (as it sends its payload asynchronously to the stream):

* **topic**, _type String_: where the data will be published
* **payload**, _type Object_: what you want to stream.

Example:

```
CALL streams.publish('my-topic', 'Hello World from Neo4j!')
```

The message retrieved from the Consumer is the following:

```
{"payload": "Hello world from Neo4j!"}
```

You can send any kind of data in the payload: **nodes, relationships, paths, lists, maps, scalar values and nested versions thereof**.

In case of nodes and/or relationships, if the topic is defined in the patterns provided by the Change Data Capture (CDC) configuration, their properties will be filtered according to the configuration.

Following is a simple video that shows the procedure in action:

![Image](https://cdn-media-1.freecodecamp.org/images/jmaPyKRDXsCEdwZEdeMzNyE2BoKXolGMEbjR)
_The streams.publish procedure in action_

### streams.consume

This procedure allows for consuming messages from a given topic.

It takes two variables as input:

* **topic**, _type String_: where you want to consume the data
* **config**, _type Map<String, Obje_ct>: the configuration parameters

and returns a list of collected events.

The **config** params are:

* **timeout**, _type Long_: it’s the value passed to Kafka `[Consumer#poll](https://kafka.apache.org/10/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html#poll-long-)` method (milliseconds). Default 1000.
* **from**, _type String_: it’s the Kafka configuration parameter `auto.offset.reset`

Use:

```
CALL streams.consume('my-topic', {<config>}) YIELD event RETURN event
```

Example: Imagine you have a producer that publishes events like this:

```
{"name": "Andrea", "surname": "Santurbano"}
```

We can create user nodes in this way:

```
CALL streams.consume('my-topic', {<config>}) YIELD eventCREATE (p:Person{firstName: event.data.name, lastName: event.data.surname})
```

Following is a simple video that shows the procedure in action:

![Image](https://cdn-media-1.freecodecamp.org/images/m0Lui2cBqiT0OQO9DTuiQfOYHZmpAKwRB4Ys)
_The stream.consume procedure in action_

So this is the end of the “Leveraging Neo4j Streams” series, I hope you enjoyed it!

If you have already tested the Neo4j-Streams module or tested it via this notebook, please fill out our [**feedback survey**](https://goo.gl/forms/VLwvqwsIvdfdm9fL2).

If you run into any issues or have thoughts about improving our work, [please raise a GitHub issue](http://github.com/neo4j-contrib/neo4j-streams/issues).

