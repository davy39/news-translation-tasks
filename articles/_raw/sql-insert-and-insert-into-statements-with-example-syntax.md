---
title: 'SQL Insert Into and Insert Statements: With Example MySQL Syntax'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T22:46:00.000Z'
originalURL: https://freecodecamp.org/news/sql-insert-and-insert-into-statements-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f67740569d1a4ca4277.jpg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'This article will walk you through how to use both Insert and Insert Into
  statements in SQL.

  How to use Insert in SQL

  Insert queries are a way to insert data into a table. Let’s say we have created
  a table using

  CREATE TABLE example_table ( name varc...'
---

This article will walk you through how to use both Insert and Insert Into statements in SQL.

## How to use Insert in SQL

Insert queries are a way to insert data into a table. Let’s say we have created a table using

`CREATE TABLE example_table ( name varchar(255), age int)`

**example_table**

Name Age

Now to add some data to this table , we’ll use  **INSERT**  in the following way:

`INSERT INTO example_table (column1,column2) VALUES ("Andrew",23)`

**example_table**

NameAgeAndrew23

Even the following will work, but it’s always a good practice to specify which data is going into which column.

`INSERT INTO table_name VALUES ("John", 28)`

**example_table**

NameAgeAndrew23John28

## How to use Insert Into in SQL

To insert a record in a table you use the  `INSERT INTO`  statement.

You can do it in two ways, if you want to insert values only in some columns, you have to list their names including all mandatory columns. The syntax is:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

```

The other way is inserting values to all columns in the table, it is not necessary to specify the columns names. The syntax is:

```
INSERT INTO table_name 
VALUES (value1, value2, value3, ...);

```

Here’s an example inserting a record in the table Person in both ways:

```
INSERT INTO Person
VALUES (1, ‘John Lennon’, ‘1940-10-09’, ‘M’);

```

And

```
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, ‘John Lennon’, ‘1940-10-09’, ‘M’);

```

Some SQL versions (for example, MySQL) support inserting multiple rows at once. For example:

```
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, ‘John Lennon’, ‘1940-10-09’, ‘M’), (2, ‘Paul McCartney’, ‘1942-06-18’, ‘M’),
(3, ‘George Harrison’, ‘1943-02-25’, ‘M’), (4, ‘Ringo Starr’, ‘1940-07-07’, ‘M’)

```

Note that the entire original query remains intact - we simple add on data rows enclosed by parentheses and separated by commas.

## You can even use Insert Into in a Select Statement.

You can insert records in a table using data that are already stored in the database. This is only a copy of data and it doesn’t affect the origin table.

The  `INSERT INTO SELECT`  statement combines  `INSERT INTO`  and  `SELECT`  statements and you can use any conditions you want. The syntax is:

```
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;

```

Here is an example that inserts in the table Person all the male students from the table Students.

```
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
SELECT Id, Name, DateOfBirth, Gender
FROM Students
WHERE Gender = ‘M’

```


