---
title: A Quick Overview of the Apache Hadoop Framework
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-quick-overview-of-the-apache-hadoop-framework
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d24740569d1a4ca3622.jpg
tags:
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: hadoop
  slug: hadoop
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: Hadoop, now known as Apache Hadoop, was named after a toy elephant that
  belonged to co-founder Doug Cutting’s son. Doug chose the name for the open-source
  project as it was easy to spell, pronounce, and find in search results. The original
  yellow stu...
---

Hadoop, now known as Apache Hadoop, was named after a toy elephant that belonged to co-founder Doug Cutting’s son. Doug chose the name for the open-source project as it was easy to spell, pronounce, and find in search results. The original yellow stuffed elephant that inspired the name appears in Hadoop’s logo.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1200px-Hadoop_logo_new.svg.png)

## What is Apache Hadoop?

> The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures.  
>   
> Source: [Apache Hadoop](https://hadoop.apache.org/)

In 2003 Google released their paper on the Google File System (GFS). It detailed a proprietary distributed file system intended to provide efficient access to large amounts of data using commodity hardware. A year later, Google released another paper entitled “MapReduce: Simplified Data Processing on Large Clusters.” At the time, Doug was working at Yahoo. These papers were the inspiration for his open-source project Apache Nutch. In 2006, the project components then known as Hadoop moved out of Apache Nutch and was released.

## Why is Hadoop useful?

Every day, billions of gigabytes of data are created in a variety of forms. Some examples of frequently created data are:

* Metadata from phone usage
* Website logs
* Credit card purchase transactions
* Social media posts
* Videos
* Information gathered from medical devices

“Big data” refers to data sets that are too large or complex to process using traditional software applications. Factors that contribute to the complexity of data are the size of the data set, speed of available processors, and the data’s format.

At the time of its release, Hadoop was capable of processing data on a larger scale than traditional software.

### **Core Hadoop**

Data is stored in the Hadoop Distributed File System (HDFS). Using map reduce, Hadoop processes data in parallel chunks (processing several parts at the same time) rather than in a single queue. This reduces the time needed to process large data sets.

HDFS works by storing large files divided into chunks, and replicating them across many servers. Having multiple copies of files creates redundancy, which protects against data loss.

### **Hadoop Ecosystem**

Many other software packages exist to complement Hadoop. These programs comprise the the Hadoop Ecosystem. Some programs make it easier to load data into the Hadoop cluster, while others make Hadoop easier to use.

The Hadoop Ecosystem includes:

* Apache Hive
* Apache Pig
* Apache HBase
* Apache Phoenix
* Apache Spark
* Apache ZooKeeper
* Cloudera Impala
* Apache Flume
* Apache Sqoop
* Apache Oozie

## More Information:

* [Apache Hadoop](http://hadoop.apache.org/)

