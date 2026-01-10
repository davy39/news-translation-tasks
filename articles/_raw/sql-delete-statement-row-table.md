---
title: SQL Delete Statement - How to Delete a Row or Table, Explained with Syntax
  Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-09T21:38:00.000Z'
originalURL: https://freecodecamp.org/news/sql-delete-statement-row-table
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ed0740569d1a4ca3f52.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'To delete a record in a table you use the  DELETE  statement.

  Be careful. You can delete all records of the table or just a few. Use the  WHERE  condition
  to specify which records do you want to delete. The syntax is:

  DELETE FROM table_name

  WHERE con...'
---

To delete a record in a table you use the  `DELETE`  statement.

Be careful. You can delete all records of the table or just a few. Use the  `WHERE`  condition to specify which records do you want to delete. The syntax is:

```
DELETE FROM table_name
WHERE condition;

```

Here is an example deleting from the table Person the record with Id 3:

```
DELETE FROM Person
WHERE Id = 3;

```

Using DELETE to remove all records from a given table

```
DELETE * FROM Person
;

```

Or depending on your RDBMS you could use the TRUNCATE TABLE statement which deletes all records from a table and depending on your RDBMS may or may not allow rollback. DELETE is DML and TRUNCATE is DDL.

```
TRUNCATE TABLE Person;

```

