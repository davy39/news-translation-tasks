---
title: The SQL Like Operator Explained with Example Syntax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T22:44:00.000Z'
originalURL: https://freecodecamp.org/news/sql-like-statements-explained-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f72740569d1a4ca42a2.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'You may have encountered the LIKE operator before. In this article we''ll
  explain how you can use it.

  LIKE Operator defined

  The  LIKE  operator is used in a  WHERE  or  HAVING  (as part of the  GROUP BY )
  to limit the selected rows to the items when a...'
---

You may have encountered the LIKE operator before. In this article we'll explain how you can use it.

### LIKE Operator defined

The  `LIKE`  operator is used in a  `WHERE`  or  `HAVING`  (as part of the  `GROUP BY` ) to limit the selected rows to the items when a column has a certain pattern of characters contained in it.

### This guide will demonstrate:

* Determining if a string starts or ends with a given string pattern
* Determining if a pattern exists in the middle of the string
* Determining if a string is not contained in the string

### A column starts or ends with a given string pattern

This SQL will select students that have  `FullName`  starting with “Monique” or ending with “Greene”.

```
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE 
FullName LIKE 'Monique%' OR -- note the % at the end but not the beginning
FullName LIKE '%Greene'; -- note the % at the beginning but not the end

```

```
+-----------+---------------+-----------+---------------------+
| studentID | FullName      | sat_score | rcd_updated         |
+-----------+---------------+-----------+---------------------+
|         1 | Monique Davis |       400 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene  |      1200 | 2017-08-16 15:34:50 |
+-----------+---------------+-----------+---------------------+
2 rows in set (0.00 sec)

```

### A string pattern is in the middle of the column

This SQL will select students that have “ree” anywhere in the name.

```
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE FullName LIKE '%ree%'; -- note the % at the beginning AND at the end

```

```
+-----------+----------------+-----------+---------------------+
| studentID | FullName       | sat_score | rcd_updated         |
+-----------+----------------+-----------+---------------------+
|         5 | Alvin Greene   |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman |      1200 | 2017-08-16 15:34:50 |
+-----------+----------------+-----------+---------------------+
2 rows in set (0.00 sec)

```

### A string is NOT in the column

You can place “NOT” before LIKE to exclude the rows with the string pattern instead of selecting them. This SQL excludes records that contain “cer Pau” and “Ted” in the FullName column.

```
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE FullName NOT LIKE '%cer Pau%' AND FullName NOT LIKE '%"Ted"%';

```

```
+-----------+----------------------+-----------+---------------------+
| studentID | FullName             | sat_score | rcd_updated         |
+-----------+----------------------+-----------+---------------------+
|         1 | Monique Davis        |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez       |       800 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey         |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene         |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman       |      1200 | 2017-08-16 15:34:50 |
|         8 | Donald D. Chamberlin |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce     |      2400 | 2017-08-16 15:35:33 |
+-----------+----------------------+-----------+---------------------+
7 rows in set (0.00 sec)

```

_Here is the current full student list to compare to the where clause result sets above._

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


