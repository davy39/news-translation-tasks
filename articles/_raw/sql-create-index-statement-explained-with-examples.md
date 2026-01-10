---
title: SQL Create Index Statement Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/sql-create-index-statement-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cee740569d1a4ca34f5.jpg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'This statement is used to create an “index” on a column in an existing
  table.

  Key points on indexes:


  They are used to improve the efficiency of searches for data, presenting the data
  in a specific order, when joining tables (see the ultimate guide t...'
---

This statement is used to create an “index” on a column in an existing table.

Key points on indexes:

* They are used to improve the efficiency of searches for data, presenting the data in a specific order, when joining tables (see the [ultimate guide to `JOIN` statements](https://www.freecodecamp.org/news/the-ultimate-guide-to-sql-join-statements/)) and more.
* An index is a “system” object, meaning that it is used by the database manager.
* Part of this usage is for the database manager to update the index when the data used by the index changes in the related table. Keep this in mind because as the number of indexes increase in a database overall system performance can be impacted.
* If you find that your SQLs are running slow on a given table or tables, creating an index is the first thing to consider to correct the issue.

Here’s an example of the syntax of the `create index` statement. Note that the syntax allows for an index to be over more than one column:

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

To create a new index on the student table's field, `programOfStudy`, use the following statement:

Here’s a statement to create the index:

```sql
create index pStudyIndex
on student (programOfStudy);
```

In MySQL, you use the `ALTER TABLE` command to change and drop indexes. MySQL Workbench also provides GUI tools to manage indexes.

But this is just scratching the surface. Check out the documentation for your database manager of choice and have fun trying different options yourself.

