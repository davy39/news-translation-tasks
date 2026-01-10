---
title: The SQL Not Operator Explained with Syntax Example
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-30T21:25:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-not-operator-explained-with-syntax-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fbc740569d1a4ca4439.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'You can use the  NOT  operator in the  WHERE  clause of  SELECT  statement.
  You use it when you want to select a condition that is not true.

  Here is a code example that selects all persons that are not male:

  SELECT Id, Name, DateOfBirth, Gender

  FROM ...'
---

You can use the  `NOT`  operator in the  `WHERE`  clause of  `SELECT`  statement. You use it when you want to select a condition that is not true.

Here is a code example that selects all persons that are not male:

```
SELECT Id, Name, DateOfBirth, Gender
FROM Person
WHERE NOT Gender = "M"

```


