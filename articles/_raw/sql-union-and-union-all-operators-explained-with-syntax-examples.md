---
title: The SQL Union and Union All Operator Explained with Syntax Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T22:40:00.000Z'
originalURL: https://freecodecamp.org/news/sql-union-and-union-all-operators-explained-with-syntax-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f73740569d1a4ca42a7.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'For this guide we’ll discuss the UNION Operator section of the SQL statement.

  The UNION Operator is used to combine the results of multiple select statements
  into one result set.

  The SQL statements must have the same number of columns in their Select...'
---

For this guide we’ll discuss the UNION Operator section of the SQL statement.

The UNION Operator is used to combine the results of multiple select statements into one result set.

The SQL statements must have the same number of columns in their Select Statement.

### Basic Example

SQL Statement

```
SELECT 'aaaaa'
UNION
SELECT 'bbbbbbbbb';

```

Output

```
+-----------+
| aaaaa     |
+-----------+
| aaaaa     |
| bbbbbbbbb |
+-----------+
2 rows in set (0.00 sec)

```

### Example using the student tables

SQL Statement

```
SELECT StudentID, FullName FROM student WHERE studentID BETWEEN 1 AND 5
UNION
SELECT studentID, studentEmailAddr FROM `student-contact-info` WHERE studentID BETWEEN 7 AND 8;

```

Output

```
+-----------+--------------------------------+
| StudentID | FullName                       |
+-----------+--------------------------------+
|         1 | Monique Davis                  |
|         2 | Teri Gutierrez                 |
|         3 | Spencer Pautier                |
|         4 | Louis Ramsey                   |
|         5 | Alvin Greene                   |
|         7 | Maximo.Smith@freeCodeCamp.org  |
|         8 | Michael.Roach@freeCodeCamp.ort |
+-----------+--------------------------------+
7 rows in set (0.00 sec)

```

## SQL UNION ALL Operator

The UNION ALL operator is an extension to UNION operator where it should result you a A+B of rows in the ouptput assuming A and B is your input, in simple terms UNION ALL doesn’t deduplicate.

### Basic Syntax

SQL Statement

```
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION ALL
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];

```

As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

