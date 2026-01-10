---
title: SQL Select Into Statement Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-18T23:02:00.000Z'
originalURL: https://freecodecamp.org/news/sql-select-into-statement-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f37740569d1a4ca416c.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: "What does the SQL Select Into statement do?\nThe  SELECT INTO  statement\
  \ is a query that allows you to create a  new  table and populate it with the result\
  \ set of a  SELECT statement. \nTo add data to an existing table, see the INSERT\
  \ INTO statement in..."
---

## What does the SQL Select Into statement do?

The  `SELECT INTO`  statement is a query that allows you to create a  _new_  table and populate it with the result set of a  `SELECT statement`. 

To add data to an existing table, see the [INSERT INTO](https://guide.freecodecamp.org/sql/sql-select-into-statement/guides/src/pages/sql/sql-insert-into-select-statement/index.md) statement instead.

`SELECT INTO`  can be used when you are combining data from several tables or views into a new table.1 The original table is not affected.

The general syntax is:

```
SELECT column-names
  INTO new-table-name
  FROM table-name
 WHERE EXISTS 
      (SELECT column-name
         FROM table-name
        WHERE condition)

```

This example shows a set of a table that was “copied” from the “Supplier” table to a new one called SupplierUSA which holds the set related to the column country of value ‘USA’.

```
SELECT * INTO SupplierUSA
  FROM Supplier
 WHERE Country = 'USA';

```

**Results** : 4 rows affected 2

|ID|CompanyName|ContactName|City|Country|Phone|
| --- | --- | --- | --- | --- | --- |
|2|New Orleans Cajun Delights|Shelley Burke|New Orleans|USA|(100) 555-4822|
|3|Grandma Kelly’s Homestead|Regina Murphy|Ann Arbor|USA|(313) 555-5735|
|16|Bigfoot Breweries|Cheryl Saylor|Bend|USA|NULL|
|19|New England Seafood Cannery|Robb Merchant|Boston|USA|(617) 555-3267|


Please see the manual for your database manager and have fun trying different options yourself.

Further reading:

1. (Microsoft - Inserting Rows by Using SELECT INTO)[[https://technet.microsoft.com/en-us/library/ms190750(v=sql.105).aspx](https://technet.microsoft.com/en-us/library/ms190750(v=sql.105).aspx)]
2. (dofactory - SQL SELECT INTO Statement)[[http://www.dofactory.com/sql/select-into](http://www.dofactory.com/sql/select-into)]

