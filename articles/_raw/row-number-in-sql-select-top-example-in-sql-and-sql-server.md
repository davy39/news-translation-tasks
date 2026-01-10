---
title: ROW_NUMBER in SQL – Select Top Example in SQL and SQL Server
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-08T19:14:49.000Z'
originalURL: https://freecodecamp.org/news/row-number-in-sql-select-top-example-in-sql-and-sql-server
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/ROW_NUMBER-in-SQL---Select-Top-Example-in-SQL-and-SQL-Server.png
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: "SQL, or structured query language, lets us gather data from a database\
  \ through queries. It also enables us to insert, update, and delete that data. \n\
  In this blog post, we will focus on how to fetch data and limit the results using\
  \ SQL. \nWhy should yo..."
---

SQL, or structured query language, lets us gather data from a database through queries. It also enables us to insert, update, and delete that data. 

In this blog post, we will focus on how to fetch data and limit the results using SQL. 

## Why should you limit SQL query results?

A database is usually a huge collection of data. Sometimes we don't need to fetch all of the results. To limit the results, we can optimize the query. 

Limiting query results is important for DB performance. Fetching a large result when it is not required incurs extra load on the database and impacts user experience. 

## How to limit query results in SQL

The syntax is different for SQL Server, Oracle, and MySQL for limiting the data.

* MySQL uses `LIMIT`.
* ORACLE uses `FETCH FIRST` .
* MS Access and SQL Server use `TOP`.

We'll see examples of how each one works in detail below.

### Demo Database

We have the following table named `students` with their details as you can see below:

<table>
<thead>
<tr>
<th>ID</th>
<th>Name</th>
<th>Gender</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Ryan</td>
<td>M</td>
</tr>
<tr>
<td>2</td>
<td>Joanna</td>
<td>F</td>
</tr>
<tr>
<td>3</td>
<td>Miranda Andersen</td>
<td>F</td>
</tr>
<tr>
<td>4</td>
<td>Dalia Mata</td>
<td>F</td>
</tr>
<tr>
<td>5</td>
<td>Lilianna Boyd</td>
<td>F</td>
</tr>
<tr>
<td>6</td>
<td>Lexie Sharp</td>
<td>M</td>
</tr>
<tr>
<td>7</td>
<td>Jazlene Cordova</td>
<td>F</td>
</tr>
<tr>
<td>8</td>
<td>Brycen Werner</td>
<td>M</td>
</tr>
<tr>
<td>9</td>
<td>Karissa Turner</td>
<td>F</td>
</tr>
<tr>
<td>10</td>
<td>Aisha Dodson</td>
<td>F</td>
</tr>
<tr>
<td>11</td>
<td>Aydin Reeves</td>
<td>M</td>
</tr>
</tbody>
</table>

### How to limit a query in MySQL

Below is the syntax for MySQL.

```sql
SELECT  (expression)
FROM 
    table_name
LIMIT 5;

```

As an example, we'll select the first 5 records from the table.

Let's use our table `students` for this demonstration.

```mysql
-- fetch top 5 values from table

SELECT * FROM students
LIMIT 5;
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-7.png)

### How to Combine LIMIT with ORDER BY

When you combine LIMIT with ORDER BY, you can get more meaningful results. For example we can use this to find the top 5 students who scored greater than 70% on their exam.

Let's order our table `students` with the column `name` and choose the top 5 from the result. You can do that like this:

```sql
SELECT * FROM students
order by name
LIMIT 5;
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-13.png)

### How to limit results – Oracle syntax

Below is the equivalent syntax for our first example in Oracle.

```sql
SELECT * FROM students
FETCH FIRST 5 ROWS ONLY;
```

In older versions of Oracle, you can use ROWNUM to restrict the number of rows returned by a query.

Example:

```sql
SELECT * FROM 
students 
WHERE ROWNUM < 5;
```

### How to limit results in SQL – MS Access syntax

Below is the equivalent syntax for our first example in MS Access.

```sql
SELECT TOP 5 * FROM students;

```

## Wrapping up

The LIMIT functionality can be very powerful for query optimization when combined with sorting. Efficient queries are lighter on the system and swift for the user. It is always recommended to LIMIT the results where applicable.

