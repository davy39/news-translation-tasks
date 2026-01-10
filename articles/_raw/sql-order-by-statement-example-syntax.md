---
title: 'The SQL Order By Statement: Example Syntax'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-12T22:50:00.000Z'
originalURL: https://freecodecamp.org/news/sql-order-by-statement-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f5e740569d1a4ca423f.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Order By is a SQL command that lets you sort the resulting output from
  a SQL query.

  Order By (ASC, DESC)

  ORDER BY gives us a way to SORT the result set by one or more of the items in the
  SELECT section. Here is an SQL sorting the students by FullName...'
---

Order By is a SQL command that lets you sort the resulting output from a SQL query.

### Order By (ASC, DESC)

ORDER BY gives us a way to SORT the result set by one or more of the items in the SELECT section. Here is an SQL sorting the students by FullName in descending order. The default sort order is ascending (ASC) but to sort in the opposite order (descending) you use DESC.

Here's the query

```
SELECT studentID, FullName, sat_score
FROM student
ORDER BY FullName DESC;

```

And here's the resulting data, presented in a nice descending table.

```
+-----------+------------------------+-----------+
| studentID | FullName               | sat_score |
+-----------+------------------------+-----------+
|         2 | Teri Gutierrez         |       800 |
|         3 | Spencer Pautier        |      1000 |
|         6 | Sophie Freeman         |      1200 |
|         9 | Raymond F. Boyce       |      2400 |
|         1 | Monique Davis          |       400 |
|         4 | Louis Ramsey           |      1200 |
|         7 | Edgar Frank "Ted" Codd |      2400 |
|         8 | Donald D. Chamberlin   |      2400 |
|         5 | Alvin Greene           |      1200 |
+-----------+------------------------+-----------+
9 rows in set (0.00 sec)

```

Here is the UN-ORDERED, current, full student list to compare to the above.

```
SELECT studentID, FullName, sat_score, rcd_updated FROM student;

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

As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

