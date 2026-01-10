---
title: The SQL Primary Key Constraint Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-13T22:52:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-primary-key-constraint-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f53740569d1a4ca4205.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'A primary key is a column or a set of columns that uniquely identifies
  each row in a table.

  It’s called a “constraint” because it causes the system to restrict the data allowed
  in these column(s). In this case…


  to contain data (NOT NULL)

  be UNIQUE f...'
---

A primary key is a column or a set of columns that uniquely identifies each row in a table.

It’s called a “constraint” because it causes the system to restrict the data allowed in these column(s). In this case…

* to contain data (NOT NULL)
* be UNIQUE from all other rows in the table.
* Each table can have only ONE primary key

Primary keys are mostly used to maintain the data integrity of each row.

It also allows the system and applications to be sure they are reading, updating and joining the data correctly.

### Example with create table

Here is a create table command that will also create a primary key using two fields.

```
CREATE TABLE priKeyExample(
rcdKey_id_a INT NOT NULL,
rcdKeySeq_id INT NOT NULL,
someData varchar(256) NOT NULL,
PRIMARY KEY(rcdKey_id_a,rcdKeySeq_id));

```

### Example with alter table

The existing one must be deleted first

```
DROP INDEX `primary` ON priKeyExample;

```

Now we’ll add the new one.

```
ALTER TABLE priKeyExample 
ADD CONSTRAINT myPriKey PRIMARY KEY(rcdKey_id_a,rcdKeySeq_id);

```

As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

