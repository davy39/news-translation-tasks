---
title: 'The SQL Where Clause Explained: In, Between, Like, and Other Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-22T23:16:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-where-clause-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f1d740569d1a4ca40e1.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'What is a SQL Where Clause?

  The WHERE  Clause (and/or,  IN ,  BETWEEN , and  LIKE )

  The  WHERE  clause is used to limit the number of rows returned.

  In this case all five of these will be used is a some what ridiculous  WHERE  clause.

  Here is the cur...'
---

## What is a SQL Where Clause?

### The `WHERE`  Clause (and/or,  `IN` ,  `BETWEEN` , and  `LIKE` )

The  `WHERE`  clause is used to limit the number of rows returned.

In this case all five of these will be used is a some what ridiculous  `WHERE`  clause.

Here is the current full student list to compare to the  `WHERE`  clause result set:

```
select studentID, FullName, sat_score, rcd_updated from student;

```

```
+-----------+------------------------+-----------+---------------------+
| studentID | FullName               | sat_score | rcd_updated         |
+-----------+------------------------+-----------+---------------------+
|         1 | Monique Davis          |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+---------------------+
9 rows in set (0.00 sec)

```

Rows will be presented that…

* `WHERE`  Student IDs are between 1 and 5 (inclusive)
* `OR`  studentID = 8

Here’s an updated query, where any record that has an SAT score that’s in this list (1000, 1400) will not be presented:

```
select  studentID, FullName, sat_score, recordUpdated
from    student
where   (studentID between 1 and 5 or studentID = 8)
        and
        sat_score NOT in (1000, 1400);

```

```
+-----------+----------------------+-----------+---------------------+
| studentID | FullName             | sat_score | rcd_updated         |
+-----------+----------------------+-----------+---------------------+
|         1 | Monique Davis        |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez       |       800 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey         |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene         |      1200 | 2017-08-16 15:34:50 |
|         8 | Donald D. Chamberlin |      2400 | 2017-08-16 15:35:33 |
+-----------+----------------------+-----------+---------------------+
5 rows in set (0.00 sec)

```

*As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

