---
title: How to Create a Table in SQL – Postgres and MySQL Example Query
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-10-25T22:53:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-table-in-sql-postgres-and-mysql-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/xavier-foucrier-UYHhyLwM1Wk-unsplash.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: null
seo_desc: "Knowing how to create tables in SQL is an important and fundamental concept.\
  \ \nIn this tutorial, I will walk you through the SQL syntax for the CREATE TABLE\
  \ statement using code examples for both PostgreSQL and MySQL.  \nBasic CREATE TABLE\
  \ Syntax\nHere ..."
---

Knowing how to create tables in `SQL` is an important and fundamental concept. 

In this tutorial, I will walk you through the `SQL` syntax for the `CREATE TABLE` statement using code examples for both PostgreSQL and MySQL.  

## Basic `CREATE TABLE` Syntax

Here is the basic syntax for the `CREATE TABLE` statement:

```sql
CREATE TABLE table_name(
	column1 data_type column_constraint,
    column2 data_type column_constraint,
    column3 data_type column_constraint,
    column4 data_type column_constraint,
    ... etc
);
```

For the first part, you need to start with the `CREATE TABLE` statement followed by the name of the table you want to create. 

If I wanted to create a table of teacher information, then I would write something like this:

```sql
CREATE TABLE teachers();
```

Inside the parenthesis, you will add the information for creating the columns for the table. If you forget the parenthesis, then you will get an error message.

```sql
CREATE TABLE teachers;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-19-at-5.54.40-PM.png)

The semicolon at the end of the parenthesis tells the computer it is the end of the `SQL` statement. You will sometimes hear this referred to as a statement terminator. 

### What are `MySQL` storage engines?

According to the `MySQL` [documentation](https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html):

> Storage engines are MySQL components that handle the SQL operations for different table types.

`MySQL` uses these storage engines to perform CRUD (create, read, update and delete) operations on the database. 

In `MySQL`, you have the option to specify the type of storage engine you want to use for your table. If you omit the `ENGINE` clause then the default will be InnoDB. 

```sql
CREATE TABLE table_name(
	column1 data_type column_constraint,
    column2 data_type column_constraint,
    column3 data_type column_constraint,
    column4 data_type column_constraint,
    ... etc
)ENGINE=storage_engine;
```

### What is the `IF NOT EXISTS` clause?

There is an optional clause called `IF NOT EXISTS` that will check if the table you want to create already exists in the database.  You can place that clause just before the table name. 

```sql
CREATE TABLE IF NOT EXISTS teachers();
```

If the table already exists, then the computer will not create a new table. 

If you omit the `IF NOT EXISTS` clause and try to create a table that already exists in the database, then you will get an error message.

In this example, I first created a table called teachers. But if I try to create that same table in the next command I will run into an error. 

```sql
CREATE TABLE IF NOT EXISTS teachers();
CREATE TABLE teachers();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-19-at-5.27.02-PM.png)

## How to create columns in the table

Inside the parenthesis for the `CREATE TABLE` statement, you are going to list the names of the columns you want to create along with their data types and constraints.

This is an example of how we can add four columns of  `school_id`, `name`, `email` and `age` to our teachers table. Each column name should be separated by commas. 

```sql
CREATE TABLE teachers(
	school_id data_type column_constraint, 
	name data_type column_constraint,
    email data_type column_constraint, 
	age data_type column_constraint
);

```

According to the `MySQL` [documentation](https://dev.mysql.com/doc/refman/8.0/en/create-table.html#create-table-types-attributes):

> MySQL has a hard limit of 4096 columns per table, but the effective maximum may be less for a given table. The exact column limit depends on several factors.

If you are working on smaller `MySQL` personal projects, then you probably won't have to worry about exceeding the number of columns for your tables. 

According to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/limits.html), there is a limit of 1600 columns per table. Similar to `MySQL`, an exact limit can vary depending on disk space or performance restrictions. 

### Data types in `SQL`

When you are creating columns in the table, you need to assign it a data type. Data types describe the type of value inside the columns. 

Here are six popular categories of data types in `SQL`:

1. Numeric (int, float, serial, decimal, etc)
2. Data and time (timestamp, data, time, etc) 
3. Character and string (char, varchar, text, etc)
4. Unicode (ntext, nvarchar, etc.)
5. Binary (binary, etc.)
6. Miscellaneous (xml, table, etc.)

This article will not go through every single data type but will cover some of the popular ones. 

Here is the complete list of [`PostgreSQL` data types](https://www.postgresql.org/docs/8.1/datatype.html) and [`MySQL` data types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html). 

### What is `SERIAL` and `AUTO_INCREMENT`?

In `PostgreSQL`, a `SERIAL` data type is an integer that will automatically increment by one for every new row that is created. 

We can add `SERIAL` right after the `school_id` column in our teachers table. 

```sql
school_id SERIAL

```

In `MySQL`, you would use `AUTO_INCREMENT` instead of `SERIAL`. In this example, the `INT` data type is used which represents an integer. 

```sql
school_id INT AUTO_INCREMENT
```

If we added five rows to our teachers table, the output would show the numbers of 1, 2, 3, 4, 5 for the `school_id` column because the integer automatically increments by one for each new row. 

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-23-at-6.09.13-PM.png)

### What is the `VARCHAR` data type? 

A `VARCHAR` data type is a variable string length where you can set a maximum character length. 

This is an example of using the `VARCHAR` data type for the `name` and `email` columns in our teachers table. The number 30 is the maximum character length. 

```sql
name VARCHAR(30) column_constraint,
email VARCHAR(30) column_constraint,
```

### Column Constraints in SQL

These are rules that are applied to the data inside the table columns. 

Here is a list of the some of the more common column constraints:

* PRIMARY KEY - this key serves as a unique identifier for the table
* FOREIGN KEY - this key makes sure that the values in a column are also present in another table. This serves as a link between tables. 
* UNIQUE - all the values in the column need to be unique 
* NOT NULL - the values cannot be NULL. NULL is the absence of a value
* CHECK - tests a value against a boolean expression

### Examples of `PRIMARY` and `FOREIGN` keys

In our teachers table, we can add a `PRIMARY KEY` to the `school_id` column.

This is what the code would look like in PostgreSQL:

```sql
 school_id SERIAL PRIMARY KEY
```

This is what the code would look like in MySQL:

```sql
school_id INT AUTO_INCREMENT PRIMARY KEY
```

If you wanted to have more than one column for the `PRIMARY KEY`, then you would add it right after your column creations.

```sql
CREATE TABLE table_name(
	column1 data_type column_constraint,
    column2 data_type column_constraint,
    column3 data_type column_constraint,
    column4 data_type column_constraint,
    ... etc
    PRIMARY KEY (column1, column2)
);
```

If you want to link one table to another then you can use a `FOREIGN KEY`. 

Let's say we had a table called district_employees with a primary key of `district_id`. Here is what the code would look like in PostgreSQL:

```sql
CREATE TABLE district_employees(
   district_id SERIAL PRIMARY KEY,
   employee_name VARCHAR(30) NOT NULL,
   PRIMARY KEY(district_id)
);
```

In our teachers table, we can use a foreign key and reference the district_employees table.

```sql
district_id INT REFERENCES district_employees(district_id),

```

```sql
CREATE TABLE teachers(
    school_id SERIAL PRIMARY KEY,
    district_id INT REFERENCES district_employees(district_id),
    column1 data_type column_constraint,
    column2 data_type column_constraint,
    column3 data_type column_constraint,
    column4 data_type column_constraint,
    ... etc 
);
```

### Examples of `NOT NULL`, `CHECK` and `UNIQUE`

If we want to ensure that we don't have any values that are null, we can use the  `NOT NULL` constraint. 

```sql
name VARCHAR(30) NOT NULL
```

We can use the `CHECK` constraint to ensure that all of our teachers are 18 and over.  The `CHECK` constraint tests a value against a boolean expression.

```sql
age INT CHECK(age >= 18)
```

If one of our values does not meet that condition, then we will get an error message.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-19-at-10.47.07-PM.png)

We can use the `UNIQUE` constraint to make sure that all of the emails are unique.

```sql
email VARCHAR(30) UNIQUE

```

This is the final result for the teachers table:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-23-at-8.09.36-PM.png)

This is what the code would look like in PostgreSQL:

```sql
CREATE TABLE teachers(
	school_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
    email VARCHAR(30) UNIQUE,
	age INT CHECK(age >= 18)      
);
```

This is what the code would look like in MySQL:

```sql
CREATE TABLE teachers(
	school_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
    email VARCHAR(30) UNIQUE,
	age INT CHECK(age >= 18)      
);
```

I hope you enjoyed this article and best of luck on your SQL journey.


