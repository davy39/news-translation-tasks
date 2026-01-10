---
title: How to Write Common Date Functions in SQL with Examples
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2023-03-13T16:49:25.000Z'
originalURL: https://freecodecamp.org/news/common-date-functions-in-sql-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-bich-tran-760710.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'When querying data from a database, you will frequently encounter the date
  datatype. Depending on what you want to achieve, you may need to extract subset
  information from the date column, perform some operation, and so on.

  SQL provides a variety of ...'
---

When querying data from a database, you will frequently encounter the date datatype. Depending on what you want to achieve, you may need to extract subset information from the date column, perform some operation, and so on.

SQL provides a variety of date functions that can assist you with your task. In this tutorial, we will look at various common date functions in SQL and some examples to show how they work. Without further ado let's get started.

Note: There are numerous SQL flavors available, and the functions for completing a specific task may differ between flavors. This tutorial will concentrate on three of the most popular SQL flavors: **PostgreSQL, MySQL, and SQL server**. We will start with PostgreSQL functions and then present the variants of the other flavors if they differ from PostgreSQL.

## Date Data types

Date data types are one of the built in data types in SQL that you use to store date values. A date value is usually stored across all database management systems or flavors in the timestamp format, that is `YYYY-MM-DD HH:MM:SS` – for example `2022-01-01 10:08:56`.

Before we get started, we will be using this table we created to explain the function we will be talking about later in the article. You can create it using the following query. Note the SQL flavor we are using is PostgreSQL.

```sql
DROP TABLE IF EXISTS student;

CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  student_name VARCHAR(30),
  admitted_date DATE
);

INSERT INTO student VALUES (11, 'Ibrahim', '2012-10-01');
INSERT INTO student VALUES (7, 'Taiwo', '2013-12-01');
INSERT INTO student VALUES (9, 'Nurain', '2012-11-21');
INSERT INTO student VALUES (8, 'Joel', '2012-10-31');
INSERT INTO student VALUES (10, 'Mustapha', '2015-11-01');
INSERT INTO student VALUES (5, 'Muritadoh', '2011-09-01');
INSERT INTO student VALUES (2, 'Yusuf', '2022-05-03');
INSERT INTO student VALUES (3, 'Habeebah', '2012-11-01');
INSERT INTO student VALUES (1, 'Tomiwa', '2013-04-01');
INSERT INTO student VALUES (4, 'Gbadebo', '2008-10-01');
INSERT INTO student VALUES (12, 'Tolu', '2009-11-21');


SELECT * FROM student;
```

## Common SQL Date Functions

Let's look at the common date functions you will work with on a daily basis.

### How to use the `Now()` function

You use the `Now()` function to return the current timestamp (date +time) of the computer system where the database management system is currently hosted. In PostgreSQL it also includes the time zone of the timestamp as shown below.

```javascript
SELECT NOW();
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-58.png align="left")

The function for getting the current timestamp in MySQL is also the same as in PostgreSQL – `Now()`. But in SQL server, you use the function `CURRENT_TIMESTAMP`.

### How to use the `current_date` function

This function, as the name implies, gets the current date of the computer system on which the SQL database is running. When retrieving the current date in PostgreSQL, you do not need to use a parenthesis, as you can see below:

```sql
SELECT current_date;
```

In MySQL, you use the `[CURDATE](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_curdate)()` function to get the current date, but SQLServer uses `[GETDATE](https://learn.microsoft.com/en-us/sql/t-sql/functions/getdate-transact-sql?view=sql-server-ver16) ()`.

### How to use the `Extract()` or `Date_Part()` functions

You use the Extract or date part functions to extract a certain part or unit of a date or date column.

Let's start with the Extract function. Its syntax looks like this:

```sql
EXTRACT(unit FROM date/date_column)
```

The unit part of the Extract function is a unit you can extract from a date such as `DAY`, `WEEK` , `YEAR` , `QUARTER` , and so on. Click [here](https://dev.mysql.com/doc/refman/8.0/en/expressions.html#temporal-intervals) to see the list of units that you can extract from a date or date column in SQL.

Say for instance in the above student table we've created earlier you wish to extract the year the students were admitted from the admitted\_date column you can achieve that using the `EXTRACT()` function as shown below.

```javascript
SELECT 
	*,
	EXTRACT(YEAR FROM admitted_date) As "Year of Admission"
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-59.png align="left")

The `EXTRACT()` function is only available in only PostgreSQL and MySQL and works similarly. Another Function that works like `EXTRACT()` is `DATEPART()` and it is also available in PostgreSQL and SQLServer. Let's look at how the `DATEPART()` function works.

The syntax for Datepart in PostgreSQL looks a little bit different from the one SQLServer uses in that it has an underscore between the date and part. You also need to pass in the unit in a single quote as shown below:

```sql
SELECT DATE_PART('Year', admitted_date)
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-60.png align="left")

For SQLServer there won't be any underscore between the date and part, and the unit will not be enclosed in single quotes. For example the above result can be generated in SQLServer as shown below.

```javascript
SELECT DATEPART(YEAR, admitted_date)
FROM student;
```

### How to add intervals or parts to dates

Intervals are units that you can add to a date – for example a days interval, time interval, and so on.

For example, say you want to add 1 day interval to all the dates in a particular table. In PostgreSQL there is no dedicated function you can use to add an interval to a particular date. Instead, you can do this using arithmetic operations.

The syntax for achieving that is shown below:

```javascript
SELECT date/date_column + INTERVAL "# unit"
```

Where # is an integer such as 3, 4, and so on, and unit can be Days, Year, and so on. Click [here](https://dev.mysql.com/doc/refman/8.0/en/expressions.html#temporal-intervals) for a list of units that can be passed as an interval.

Say, for instance, that you want to add an interval of 3 days to the `admitted_date` column in the student table. You can do this in PostgreSQL using the following query:

```sql
SELECT 
	*,
	admitted_date + INTERVAL '3 Days' AS "3_daysadded"
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-93.png align="left")

Now that you've seen how to add intervals to dates in PostgreSQL, let's see how it is done in MySQL and SQLServer. In MySQL and SQLServer there are functions that you can use to add intervals to dates.

In my SQL, the name of the function is called `DATE_ADD()` and the syntax is shown below:

```javascript
DATE_ADD(date/date_column, INTERVAL value unit)
```

For example, you can get the above table using MySQL by typing the following code:

```javascript
SELECT *,
	DATE_ADD(admitted_date, INTERVAL 3 DAY) AS "3_daysadded"
FROM student;
```

In SQLServer, the function you use is similar to the one in MySQL but with a small difference. The syntax for the function used is shown below:

```javascript
DATEADD (datepart/unit , number , date/date_column)
```

You can replicate the above table in SQLServer like this:

```sql
SELECT *,
	DATEADD (day , 3 , admitted_date) AS "3_daysadded"
FROM student;
```

### How to subtract intervals from dates

Subtracting intervals from dates in PostgreSQL works like adding intervals, except that the operator changes from plus to minus. For example, say you want to subtract 3 days from the admitted\_date column. You can do this using the below code:

```sql
SELECT 
	*,
	admitted_date - INTERVAL '3 Days' AS "3_dayssubtracted"
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-95.png align="left")

In MySQL, you use the DATESUB function to subtract intervals from the date. You can replicate the above table in MySQL using the following query:

```javascript
SELECT *,
	DATE_SUB(admitted_date, INTERVAL 3 DAY) AS "3_dayssubtracted"
FROM student;
```

In SQLServer, you still use the DATEADD function, but instead of specifying a positive value in the function parameter, you use a negative value. It looks like this:

```sql
SELECT *,
	DATEADD (day , -3 , admitted_date) AS "3_dayssubtracted"
FROM student;
```

### How to subtract two dates

To subtract two dates in PostgreSQL, there is also not a dedicated function. But you can use arithmetic operators to achieve your desired result.

```sql
SELECT '2012-10-31'::date -'2012-05-01'::date AS days;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-96.png align="left")

In MySQL, there is a function called `[DATE_DIFF](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_datediff)()` that you can use to achieve this, while for SQLServer you use the `[DATEDIFF](https://learn.microsoft.com/en-us/sql/t-sql/functions/datediff-transact-sql?view=sql-server-ver16)()` function. Click here to learn more about it.

## Conclusion

In this tutorial you've learned some common date functions you will use with when working with dates in SQL.

You learned how to get the current timestamp, get the current date, extract parts from a date, and how to add or subtract dates. Also you learned how each date function differs across different SQL flavors.

Thank you for reading. You can check out the below resources to learn more about date function across the three different SQL flavor discussed in this article.

1. [Microsoft SQL database functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16)
    
2. [Postgres date/time functions and operators](https://www.postgresql.org/docs/current/functions-datetime.html)
    
3. [MySQL date and time functions reference manual](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)
