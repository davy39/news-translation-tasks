---
title: The SQL In Statement Explained with Example Syntax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-08T22:33:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-in-statement-explained-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f7b740569d1a4ca42d0.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'The IN Operator defined

  The  IN  operator is used in a  WHERE  or  HAVING  (as part of the  GROUP BY ) to
  limit the selected rows to the items “IN” a list.

  Here is the current full student list to compare to the  WHERE  clause result set:

  select stud...'
---

## The IN Operator defined

The  `IN`  operator is used in a  `WHERE`  or  `HAVING`  (as part of the  `GROUP BY` ) to limit the selected rows to the items “IN” a list.

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

Rows will be presented that have an SAT score in this list (1000, 2400):

```
select studentID, FullName, sat_score, rcd_updated
from student
where sat_score in (1000, 2400);

```

```
+-----------+------------------------+-----------+---------------------+
| studentID | FullName               | sat_score | rcd_updated         |
+-----------+------------------------+-----------+---------------------+
|         3 | Spencer Pautier        |      1000 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+---------------------+
4 rows in set (0.00 sec)

```

