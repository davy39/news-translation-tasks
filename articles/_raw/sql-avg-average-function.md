---
title: SQL AVG - The SQL Average Function Explained with Syntax Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-27T22:05:00.000Z'
originalURL: https://freecodecamp.org/news/sql-avg-average-function
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6f740569d1a4ca3d0f.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'What is the SQL Average (AVG) Function?

  “Average” is an Aggregate (Group By) Function. It’s used to calculate the average
  of a numeric column from the set of rows returned by a SQL statement.

  Here is the syntax for using the function:

  select grouping...'
---

## What is the SQL Average (AVG) Function?

“Average” is an Aggregate (Group By) Function. It’s used to calculate the average of a numeric column from the set of rows returned by a SQL statement.

Here is the syntax for using the function:

```
select groupingField, avg(num_field)
from table1
group by groupingField

```

Here’s an example using the student table:

```
select studentID, FullName, avg(sat_score) 
from student 
group by studentID, FullName;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/avg_function01.JPG?raw=true)

