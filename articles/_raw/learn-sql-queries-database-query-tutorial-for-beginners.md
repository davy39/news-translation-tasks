---
title: Learn SQL Queries – Database Query Tutorial for Beginners
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-10T00:05:46.000Z'
originalURL: https://freecodecamp.org/news/learn-sql-queries-database-query-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/jan-antonin-kolar-lRoX0shwjUQ-unsplash--1-.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'SQL stands for Structured Query Language and is a language that you use
  to manage data in databases. SQL consists of commands and declarative statements
  that act as instructions to the database so it can perform tasks.

  You can use SQL commands to cre...'
---

SQL stands for Structured Query Language and is a language that you use to manage data in databases. SQL consists of commands and declarative statements that act as instructions to the database so it can perform tasks.

You can use SQL commands to create a table in a database, to add and make changes to large amounts of data, to search through it to quickly find something specific, or to delete a table all together.

In this article, we'll look at some of the most common SQL commands for beginners and how you can use them to effectively query a database – that is, make a request for specific information.

## The Basic Structure of a Database

Before we get started, you should understand the hierarchy of a database.

An SQL database is a collection of related information stored in tables. Each table has columns that describe the data in them, and rows that contain the actual data. A field is a single piece of data within a row. So to fetch the desired data we need to get specific.

For example, a remote company can have multiple databases. To see a full list of their databases, we can type `SHOW DATABASES;` and we can zone in on the `Employees` database. 

The output will look something like this:

```
+--------------------+
|     Databases      |
+--------------------+
| mysql              |
| information_schema |
| employees          |
| test               |
| sys                |
+--------------------+
```

A single database can have multiple tables. Taking the example from above, to see the different tables in the `employees` database, we can do `SHOW TABLES in employees;`. The tables can be `Engineering`, `Product`, `Marketing`, and `Sales` for the different teams the company has.

```
+----------------------+
| Tables_in_employees  |
+----------------------+
| engineering          |
| product              |
| marketing            |
| sales                |
+----------------------+
```

All tables then consist of different columns that describe the data.

To see the different columns use `Describe Engineering;`. For example the Engineering table can have columns that define a single attribute like `employee_id`, `first_name`, `last_name`, `email`, `country`, and `salary`. 

Here's the output:

```
+-----------+-------------------+--------------+
| Name      |         Null      |      Type    |  
+-----------+-------------------+--------------+
|EMPLOYEE_ID| NOT NULL          | INT(6)       |  
|FIRST_NAME | NOT NULL          |VARCHAR2(20)  |
|LAST_NAME  | NOT NULL          |VARCHAR2(25)  | 
|EMAIL      | NOT NULL          |VARCHAR2(255) |
|COUNTRY    | NOT NULL          |VARCHAR2(30)  |
|SALARY     | NOT NULL          |DECIMAL(10,2) |
+-----------+-------------------+--------------+
```

Tables also consist of rows, which are individual entries into the table. For example a row would include entries under `employee_id`, `first_name`, `last_name`, `email`, `salary`, and `country`. These rows would define and provide info about one person on the Engineering team.

## Basic SQL Queries

All the operatations that you can do with data follow the CRUD acronym.

CRUD stands for the 4 main operations we perform when we query a database: Create, Read, Update, and Delete.

We `CREATE` information in the database, we `READ`/Retrieve that information from the database, we `UPDATE`/manipulate it, and if we want we can `DELETE` it.

Below we'll look at some basic SQL queries along with their syntax to get started.

### SQL `CREATE DATABASE` Statement

To create a database named `engineering`, we can use the following code:

```sql
CREATE DATABASE engineering;
```

### SQL `CREATE TABLE` Statement

```SQL
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

This query creates a new table inside the database.

It gives the table a name, and the different columns we want our table to have are also passed in.

There are a variety of datatypes that we can use. Some of the most common ones are: `INT`, `DECIMAL`, `DATETIME`, `VARCHAR`, `NVARCHAR`, `FLOAT`, and `BIT`.

From our example above, this could look like the following code:

```sql
CREATE TABLE engineering (
employee_id  int(6) NOT NULL,
first_name   varchar(20) NOT NULL,
last_name  varchar(25) NOT NULL,
email  varchar(255) NOT NULL,
country varchar(30),
salary  decimal(10,2) NOT NULL
);
```

The table we create from this data would look something similar to this:

|employee_id | first_name | last_name | email |country |salary |
| ---         | :--        | --:       | :-:   |:-:   | :-:   |
|&#xfeff; |


### SQL `ALTER TABLE` Statement

After creating the table, we can modify it by adding another column to it.

```sql
ALTER TABLE table_name 
ADD column_name datatype;
```

For example, if we wanted we could add a `birthday` column to our existing table by typing:

```sql
ALTER TABLE engineering
ADD  birthday date;
```

Now our table will look like this:

|employee_id | first_name | last_name | email |country |salary |birthday |
| ---         | :--        | --:       | :-:   |:-:   | :-:   |:-:   |
|&#xfeff; |


### SQL `INSERT` Statement

This is how we insert data into tables and create new rows. It's the `C` part in CRUD.

```sql
INSERT INTO table_name(column1, column2, column3,..) 
VALUES(value1, 'value2', value3,..);
```

In the `INSERT INTO` part, we can specify the columns we want to fill with information.

Inside `VALUES` goes the information we want to store. This creates a new record in the table which is a new row. 

Whenever we insert string values, they are enclosed in single quotes,`''`.


For example:

```sql
INSERT INTO table_name(employee_id,first_name,last_name,email,country,salary) 
VALUES
(1,'Timmy','Jones','timmy@gmail.com','USA',2500.00);
(2,'Kelly','Smith','ksmith@gmail.com','UK',1300.00);
```

The table would now look like this:

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly      |Smith       |ksmith@gmail.com|UK|1300.00


### SQL `SELECT` Statement

This statement fetches data from the database. It is the `R` part of CRUD.

```sql
SELECT  column1,column2
FROM    table_name;
```

From our example earlier, this would look like the following:

```sql
SELECT first_name,last_name
FROM   engineering;
```

Output:

```
+-----------+----------+
|FirstName  | LastName |
+-----------+----------+
| Timmy     | Jones    |
| Kelly     | Smith    |
+-----------+----------+
```


The `SELECT` statement points to the specific column we want to fetch data from that we want shown in the results.

The `FROM` part determines the table itself.

Here's another example of `SELECT`:

```sql
SELECT * FROM table_name;
```

The asterisk `*` will grab all the information from the table we specify.

### SQL `WHERE` Statement

`WHERE` allows us to get more specific with our queries.

If we wanted to filter through our `Engineering` table to search for employees that have a specific salary, we would use `WHERE`.

```sql
SELECT employee_id,first_name,last_name,email,country
FROM engineering
WHERE salary > 1500
```

The table from the previous example:

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly      |Smith       |ksmith@gmail.com|UK|1300.00


Would now have the output below:

```
+-----------+----------+----------+----------------+------------+
|employee_id|first_name|last_name |email           |country     |
+-----------+----------+----------+----------------+------------+
|          1| Timmy    |Jones     |timmy@gmail.com | USA        |
+-----------+----------+----------+----------------+------------+
```


This filters through and shows the results that satisfy the condition – that is, it shows *only* the rows of the people whose salary is `more than 1500`.

### SQL `AND`, `OR`, and `BETWEEN` Operators

These operators allow you to make the query even more specific by adding more criteria to the `WHERE` statement.

The `AND` operator takes in two conditions and they both must be `true` in order for the row to be shown in the result.

```sql
SELECT column_name
FROM table_name
WHERE column1 =value1
    AND column2 = value2;
```

The `OR` operator takes in two conditions, and either one must be true in order for the row to be shown in the result.

```sql
SELECT column_name
FROM table_name
WHERE column_name = value1
    OR column_name = value2;
```

The `BETWEEN` operator filters out within a specific range of numbers or text.

```sql
SELECT column1,column2
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

We can also use these operators in combination with each other.

Say our table was now like this:

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly       |Smith       |ksmith@gmail.com|UK|1300.00
|3           |Jim         |White       |jwhite@gmail.com|UK|1200.76
|4           |José Luis   |Martìnez    |jmart@gmail.com|Mexico| 1275.87
|5           |Emilia      |Fischer     |emfis@gmail.com | Germany| 2365.90
|6           |Delphine    |Lavigne     |lavigned@gmail.com| France| 2108.00
|7           |Louis      |Meyer     |lmey@gmail.com | Germany| 2145.70

If we used a statement like the one below:

```sql
SELECT * FROM engineering
WHERE  employee_id BETWEEN 3 AND 7
        AND 
        country = 'Germany';
```

We'd get this output:

```
+------------+-----------+-----------+----------------+--------+--------+
|employee_id | first_name| last_name | email          |country |salary  |
+------------+-----------+-----------+----------------+--------+--------+
|5           |Emilia     |Fischer    |emfis@gmail.com | Germany| 2365.90|
|7           |Louis      |Meyer      |lmey@gmail.com  | Germany| 2145.70|
+------------+-----------+-----------+----------------+--------+--------+
```

This selects *all* comlumns that have an `employee_id` between `3 and 7` `AND` have a country of Germany.


### SQL `ORDER BY` Statement

`ORDER BY` sorts by the columns we mentioned in the `SELECT` statement.

It sorts through the results and presents them in either descending or ascending alphabetical or numerical order (with the default order being ascending).

We can specify that with the command: `ORDER BY column_name DESC | ASC` .

```sql
SELECT employee_id, first_name, last_name,salary
FROM engineering
ORDER BY salary DESC;
```

In the example above, we sort through the employees' salaries in the engineering team and present them in descending numerical order.


### SQL `GROUP BY` Statement

`GROUP BY` lets us combine rows with identical data and similarites.

It is helpful to arrange duplicate data and entries that appear many times  in the table.

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;
```

Here `COUNT(*)` counts each row separately and returns the number of rows in the specified table while also preservering duplicate rows.

### SQL `LIMIT` Statement

`LIMIT` lets you spefify the *maximum* number of rows that should be returned in the results.

This is helpful when working through a large dataset which can cause queries to take a long time to run. By limiting the results you get, it can save you time.

```sql
SELECT column1,column2
FROM table_name
LIMIT number;
```


### SQL `UPDATE` Statement

This is how we update a row in a table. It's the `U` part of CRUD.

```sql
UPDATE table_name 
SET column1 = value1, 
    column2 = value2 
WHERE condition;
```

The `WHERE` condition specifies the record you want to edit.

```sql
UPDATE engineering
SET    country = 'Spain'
WHERE   employee_id = 1
```

Our table from before:

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly       |Smith       |ksmith@gmail.com|UK|1300.00
|3           |Jim         |White       |jwhite@gmail.com|UK|1200.76
|4           |José Luis   |Martìnez    |jmart@gmail.com|Mexico| 1275.87
|5           |Emilia      |Fischer     |emfis@gmail.com | Germany| 2365.90
|6           |Delphine    |Lavigne     |lavigned@gmail.com| France| 2108.00
|7           |Louis      |Meyer     |lmey@gmail.com | Germany| 2145.70

Would now look like this:

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|Spain|2500.00
|2           |Kelly       |Smith       |ksmith@gmail.com|UK|1300.00
|3           |Jim         |White       |jwhite@gmail.com|UK|1200.76
|4           |José Luis   |Martìnez    |jmart@gmail.com|Mexico| 1275.87
|5           |Emilia      |Fischer     |emfis@gmail.com | Germany| 2365.90
|6           |Delphine    |Lavigne     |lavigned@gmail.com| France| 2108.00
|7           |Louis      |Meyer     |lmey@gmail.com | Germany| 2145.70


This updates the country of residence column of an employee with an id of 1.

We can also update information in a table with values from another table with `JOIN`.

```sql
UPDATE table_name
SET table_name1.column_name1 = table_name2.column_name1
    table_name1.column_name2 = table_name2.column2
FROM table_name1
JOIN table_name2 
    ON table_name1.column_name = table_2.column_name;
```

  
### SQL `DELETE` Statement

`DELETE` is the `D` part of CRUD. It's how we delete a record from a table.

The basic syntax looks like this:

```sql
DELETE FROM table_name 
WHERE condition;
```

For instance, in our `engineering` example that could look like this:

```sql
DELETE FROM engineering
WHERE employee_id = 2;
```

This deletes the record of an employee in the engineering team with an id of 2.

### SQL `DROP COLUMN` Statement

To remove a specific column from the table we would do this:

```sql
ALTER TABLE table_name 
DROP COLUMN column_name;
```


### SQL `DROP TABLE` Statement

To delete the whole table we can do this:

```sql
DROP TABLE table_name;
```

## Conclusion

In this article we went over some of the basic queries you'll use as a SQL beginner. 

We learned how to create tables and rows, how to gather and update information, and finally how to delete data. We also mapped the SQL queries to their corresponding CRUD actions.

Thanks for reading and happy coding!







