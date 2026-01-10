---
title: SQL Select – Statement and Query Examples
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-24T18:07:46.000Z'
originalURL: https://freecodecamp.org/news/sql-select-statement-and-query-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--17-.png
tags:
- name: beginner
  slug: beginner
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Structured Query Language (SQL) is a programming language that you use
  to manage data in relational databases. You can use SQL to create, read, update,
  and delete (CRUD) data in a relational database.

  You can write SQL queries to insert data with INS...'
---

Structured Query Language (SQL) is a programming language that you use to manage data in relational databases. You can use SQL to create, read, update, and delete (CRUD) data in a relational database.

You can write SQL queries to insert data with INSERT, read data with SELECT, update with UPDATE, and delete data with DELETE.

This article will teach you how to write SQL SELECT queries. You'll learn the various ways you can write these queries, and what the expected results should be.

## How to Use the SQL SELECT Statement

You can use the SQL SELECT statement to retrieve data from a database table that has been specified.

You can write your statement in various ways to get the exact data you want. These data are extracted from the database table and returned as a table.

```sql
// Syntax

SELECT expression(s)
FROM table(s)
[WHERE condition(s)]
[ORDER BY expression(s) [ ASC | DESC ]];
```

The preceding code is a very detailed syntax that encompasses a lot of information that I'll explain with examples.

Let's begin by going over the parameters and arguments:

* **expression(s)**: This represents the column(s) whose data you want to retrieve or the entire table's columns using an asterisk (`*`).
    
* **table(s)**: The name of the table(s) from which you want to retrieve records. The FROM clause must include at least one table.
    
* **WHERE condition(s)**: This is an optional field. This allows you to specify a condition that will guide the data that is retrieved for the specified column(s). If no conditions are specified, all records will be chosen.
    
* **ORDER BY expression(s)**: This is an optional field. This allows you to declare a column whose data will be used to sort the results. A comma should separate the values if you provide more than one expression.
    
* **ASC**: This is an optional expression value. ASC sorts the result set by expression in ascending order. If this is not specified, this is the default behavior.
    
* **DESC**: This is an optional expression value. DESC sorts the result set by expression in descending order.
    

## SQL Select Queries

Suppose you have a database with the name "Users" and has the following data:

| user\_id | first\_name | last\_name | age | status |
| --- | --- | --- | --- | --- |
| 1 | John | Doe | 33 | Married |
| 2 | Alice | Truss | 23 | Single |
| 3 | David | Bohle | 56 | Married |
| 4 | Aaron | Ben | 34 | Single |
| 5 | Louis | Vic | 72 | Married |
| 6 | Charles | Chris | 19 | Single |

Let's now explore various queries and see how they work.

### SQL Select All

You might need to select all the columns from a database. Instead of listing each column, you can use the asterisk (`*`) character.

```sql
SELECT *
FROM Users;
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666430594839_Untitled.drawio+19.png align="left")

### SQL Select Specified Columns

You can also fetch specified columns instead of all the columns by listing the columns and separating them by a comma:

```sql
SELECT first_name, last_name
FROM Users;
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666441467406_Untitled.drawio+27.png align="left")

### SQL Select WHERE Clause

You may want to return only rows that satisfy a specific condition. This condition can be specified using the optional `WHERE` clause. The `WHERE` clause allows you to retrieve records from a database table that match a given condition(s).

For example, suppose you only want to fetch users whose status is "single":

```sql
SELECT *
FROM Users
WHERE status = 'Single';
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666431175784_Untitled.drawio+21.png align="left")

Generally, the WHERE clause is used to filter the results. You can also use common operators like `=`, which you used, and others like `<`, `>`, `<=`, `>=`, `AND`, `BETWEEN`, and `IN`.

### SELECT Using Equality Operators

Suppose you want to fetch only users whose age is greater than 30. Then your query will be:

```sql
SELECT *
FROM Users
WHERE age > 30;
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666431269376_Untitled.drawio+22.png align="left")

You can also use other equality operators like `<`, `<=`, and `>=`.

### SELECT Using the AND Operator

You might often want to use more than one condition to filter the table's contents. You can do this with the AND operator.

```sql
SELECT *
FROM Users
WHERE status = 'Single' AND age > 30;
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666433362143_Untitled.drawio+23.png align="left")

### SELECT Using the BETWEEN Operator

You use the BETWEEN operator to get the range of data you want to filter. You can decide to use the equality and AND operator, but BETWEEN provides a better syntax.

```sql
SELECT *
FROM Users
WHERE age BETWEEN 20 AND 30;
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666433680877_Untitled.drawio+24.png align="left")

### SELECT Using the IN Operator

Also, the `IN` operator lets you set more than one exact basis for filtering each row. For example, you can fetch only rows whose value is in the bracket defined:

```sql
SELECT *
FROM Users
WHERE age IN (56,33,10);
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666433956123_Untitled.drawio+26.png align="left")

### SQL Select ORDER BY Clause

So far, you have learned how to fetch from your table with SQL, but you will notice that these data always follow the original order. You can adjust the order in which the data is fetched using the ORDER BY clause.

Two major options are Ascending (`ASC`) and descending (`DESC`) order. For example, you might want your table's rows to be arranged in ascending order based on the `first_name`:

```sql
SELECT *
FROM Users
ORDER BY first_name ASC;
```

Here is what your output will look like when you make use of this command on the user's table:

![](https://paper-attachments.dropboxusercontent.com/s_620D0D0A23556D1CE834866DA826B5C1B0E55BD04F998B1718541CB54692E6CA_1666441975760_Untitled.drawio+28.png align="left")

> **Note:** You can always combine these options and clauses in one query to fetch exactly what you want.

## Wrapping up!

In this article, you learned how to use the SQL SELECT query to retrieve data from a relational database. Other options are available, but these are the ones you'll most likely use regularly.

Have fun coding!
