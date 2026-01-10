---
title: 'The pros and cons of different data formats: key-values vs tuples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T16:44:57.000Z'
originalURL: https://freecodecamp.org/news/the-pros-and-cons-of-different-data-formats-key-values-vs-tuples-f526ad3fa964
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1LI9TzwDU1l6IyJFBRcULw.jpeg
tags:
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Hieu Nguyen (Jack)

  How data is formatted under the hood


  _Photo by [Unsplash](https://unsplash.com/photos/1K6IQsQbizI?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Franki Chamaki on <a ...'
---

By Hieu Nguyen (Jack)

#### How data is formatted under the hood

![Image](https://cdn-media-1.freecodecamp.org/images/7XaDSrL1K83J1dBxAzMjovGc4jrC9Hfqd968)
_Photo by [Unsplash](https://unsplash.com/photos/1K6IQsQbizI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Franki Chamaki</a> on <a href="https://unsplash.com/search/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Working on [Vasern](http://github.com/vasern/vasern) (a client database for React Native) has given me an opportunity to try and test different data formats which include key-value, column-oriented, document, and tuples. Each format was designed to suit different scenarios.

The criteria of these tests focus on performance, the ability to lookup values, and space efficiency. Besides, it is not required to have on-disk sorted keys and indices. They will be loaded into memory for fast lookup.

In this post, I will recap the pros and cons of the two common formats: **key-values** and **tuples format.** Also, I’ll introduce **tagged key-values**, an extension of key-values with index lookup, which benefits from the tuples format.

### Key-Value Store

![Image](https://cdn-media-1.freecodecamp.org/images/D07YYA0726oX0lONmcxCzk9GUxcLbNa2c2Qn)
_A collection of the key-value store_

Key-values store a collection of key-and-value pairs, where sometimes the value represents more than one value, separated by delimiters (i.e. a comma). Those pairs are organized into blocks with fixed-length (for fast traverse between records).

![Image](https://cdn-media-1.freecodecamp.org/images/mctmmR2ACQsQhkEYXwqTiYnLdOCvqHKKrDQO)
_Example of single-block key-value store layout (“\0” represents null/empty value)_

**Advantages of the key-value store:**

* Simple data format makes write and read operations fast
* Value can be anything, including JSON, flexible schemas

**Disadvantages:**

* Optimized only for data with single key and value. A parser is required to store multiple values.
* Not optimized for lookup. Lookup requires scanning the whole collection or creating separate index values

### Tuples Data Store (RDBMS)

The tuples data format has existed for many decades. It is used in relational databases such as MySQL, Postgres, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/a-xcLNN9JVKQjs6Jd8vPqZstcJDmixKSqfYq)
_An example of the tuples data format in Relational Database_

Unlike the key-values format, it relies on the predefined schema to organize records into rows, and its values in fixed-length columns. Each value only/usually represents a single piece of information.

**Advantages of tuples data store:**

* Structured data format helps traverse through values of records quickly
* Optimized for lookup (common use of SQL for querying records)

**Disadvantages:**

* Constrained by schema structure
* Change of schema usually requires rewriting the whole database

### Tagged Key-Value Store

![Image](https://cdn-media-1.freecodecamp.org/images/J-Kuww82Dhi4q8ZQCrcMQ2CJGtZ88cWEIQiR)
_Uhmm, TKVF (tagged-key-value format)_

Tagged Key-Value is an extended version of Key-Value storage — it has more than one key for a single value. In other words, it has a key, indexes (or tags) and a body value for each record. Where:

* **Key** and **Indexes** will be loaded into memory on startup
* **Body value** can be anything from a plain string, BSON/JSON, or comma-separated value.

**Advantages of Tagged Key-Value store:**

* Semi-structured, which helps traverse through records and indexes fast
* Optimized for lookup (through keys and indexes)
* A record **body** can be anything, ideal for flexible schemas
* Space efficiency (key, indices are organized in tight columns)

**Disadvantages:**

* Change of schema that includes **indices** might need data migration

![Image](https://cdn-media-1.freecodecamp.org/images/-PoMvWSH9PIYAiyGs1141mhgVsyJQBliHyvP)
_A format example of the tagged-key-value_

#### Vasern with Tagged Key-Value Store

Vasern is a client database for React Native. The latest version was released under beta for testing and was using key-value storage.

In the upcoming [**0.3.0-RC version**](https://github.com/vasern/vasern/tree/0.3.0-rc)**,** Vasern is switching to a tagged key-value store layout. Focus is on its powerful lookup feature and space efficiency.

Below is a demo query. It’s beautiful, isn’t it?

![Image](https://cdn-media-1.freecodecamp.org/images/Mo1NpiljkgEHIkRV1JxndzR1CgmqoHRiNY9v)
_A demo of Vasern query_

### Conclusion

There are many databases with different data formats to choose for an application. Two common formats are:

* **Key-Value pairs** — fast read and write but not optimized for lookup. It’s often used as simple data storage, NoSQL.
* **Tuples** — support multi typed-values, indexes, optimized for lookup, but a lack of schema flexibility. Commonly used for Relational Databases.

By combining the strengths mentioned above, the **Tagged-Key-Values** format is flexible with data schema, and is able to look up records through keys and indices. This is often better suited for a client’s database.

**If you found this article useful, please click on the** ? **button a few times to make others find the article and show your support! ?**

**Thanks for reading!**

