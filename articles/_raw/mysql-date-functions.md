---
title: MySQL Date Functions – Explained with Example Queries
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-01-25T17:15:13.000Z'
originalURL: https://freecodecamp.org/news/mysql-date-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/image-162-1.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'SQL is a programming language we use to interact with relational databases.
  SQL databases contain tables, which contain rows of data. These tables can contain
  a wide range of data types.

  In this article, you''ll learn how MySQL functions help make dat...'
---

SQL is a programming language we use to interact with relational databases. SQL databases contain tables, which contain rows of data. These tables can contain a wide range of data types.

In this article, you'll learn how MySQL functions help make date management very easy. 

These functions help perform various tasks. Some perform simple tasks like adding days to dates, finding how many days are between two dates, or even more complicated tasks like how to tell how far into a year a date is by number of days.

Before proceeding, keep in mind that this article was written on `2023-01-24`. So your results on running the queries here might be slightly different based on when you read it.

## How to Use the `CURRENT_DATE` Function in SQL

This function returns today's date in the format '**YYYY-MM-DD**'. It is one of the simplest MySQL functions to use. It takes no arguments at all.

```sql
SELECT CURRENT_DATE;
-- Returns 2023-01-24
```

This function has synonymous functions that work just the way it does: `CUR_DATE` and `CURRENT_DATE()` will return the exact same result as `CURRENT_DATE`.

## How to Use the `ADDDATE` Function in SQL

This functions performs additions, or subtractions, on date values. It takes an interval that can be in days, or months, or even years. This interval can be positive or negative. The function takes this format:

```sql
ADDDATE(date/expr, INTERVAL expr unit);
```

Here, the `date/expr` refers to the base date value to be added to or subtracted from. And the `INTERVAL` is a constant keyword that has to come before the `expr` that is used to set the value of the increment in numbers. Finally, you have the unit, which can be `day`, `week`,  `month`, `quarter` or even `year`.  The `unit` can also be a smaller value like `second` or even `microsecond`. Check the [MySQL docs](https://dev.mysql.com/doc/refman/8.0/en/expressions.html#temporal-intervals) for more possible values.

This functions works exactly the same as the `DATE_ADD` and you can use them interchangeably.

Using ADDDATE, you can find the date of 45 days from today like this:

```sql
SELECT ADDDATE(CURRENT_DATE, INTERVAL 45 DAY);
-- Returns 2023-03-10
```

To get the date of the day 7 months and 3 weeks ago, use the ADDDATE like this:

```sql
SELECT ADDDATE(
	ADDDATE(CURRENT_DATE, INTERVAL -7 MONTH), 
	INTERVAL -3 WEEK
);
-- Returns 2022-06-03
```

Here, we called the ADDDATE function twice. First, to get the date of 7 months ago. Then, we called it again to get the date of 3 weeks before that time.

A common use case of ADDDATE in real life applications is to get data values to be used in a WHERE clause as a range. 

For example, if you had an `employees` table with a `hiredate` field that stores their resumption date. To see all employees that resumed in the past year (where `hiredate` > the date of a year ago), use ADDDATE like this:

```sql
SELECT * 
FROM employees 
WHERE hiredate > ADDDATE(CURRENT_DATE, INTERVAL -1 YEAR);
```

Another common case would be when you have to filter by a time range. In a `songs` table with a `released` field, to fetch all songs released in the last three weeks except for the ones released this week, use ADDDATE like this:

```sql
SELECT * 
FROM songs 
WHERE released 
BETWEEN ADDDATE(CURRENT_DATE, INTERVAL -3 WEEK) 
AND ADDDATE(CURRENT_DATE, INTERVAL -1 WEEK);
```

## How to Use the `DATEDIFF` Function in SQL

This function returns the number of days between two dates. It takes in the two dates to be subtracted. Let's use `DATEDIFF` to find the number of days between today and `2023-03-10`.

```sql
SELECT DATEDIFF('2023-03-10', CURRENT_DATE);
-- Returns 45
```

Rearranging the dates and calling the function again results in a difference in the response:

```sql
SELECT DATEDIFF(CURRENT_DATE, '2023-03-10');
-- Returns -45
```

You can use this function with the `ABS` function to get the absolute value and not have issues with the negative sign or value.

```sql
SELECT ABS(DATEDIFF(CURRENT_DATE, '2023-03-10'));
-- Returns 45
```

This is very useful when you have to return data with respect to time. `For example, in many blogs, you see a part that says something like 'Posted 7 days ago'. You can use the `DATEDIFF` to get this value easily.

## How to Use the `DATE_FORMAT` Function in SQL

This function lets you present your data anyhow you want it. This is a very useful function. It takes in the date to be formatted, and also a string representing the desired format. The function takes this format:

```sql
DATE_FORMAT(date, format)
```

The format string can be of any length and each character in it defines a specific format and must be prefixed by the percentage symbol, `%`. For example, given the date `2023-03-10`, you can present this as `Fri 10th March, 2023` like so:

```sql
SELECT DATE_FORMAT('2023-03-10', '%a %D %M, %Y');
```

Here, we passed in the format string `'%a %D %M, %Y'`. But, what does this truly mean? Here's a few things to note:

* The provided format string, `'%a %D %M, %Y'`, is exactly the same shape as the result, `Fri 10th March, 2023`. This means you can shape the result anyhow you like – even the space characters matter. Every character in the format string is returned as part of the result, except it is prefixed using the percentage sign, then it is read as a format character. For example, rewriting the format string to `'45 days from today is %a, %D day of %M, %Y'` will result in `45 days from today is Fri, 10th day of March, 2023`.
* The `a` used results in the abbreviated weekday name, Fri.
* The `D` returned the day of the month with English suffix, 10th.
* The `M` returned the name of the month, March.
* The `Y` returned the year, 2023.

There are many more characters that you can use in the format string, and you can find them [here](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format).

## How to Use the `MAX` and `MIN` Functions in SQL

While these functions aren't limited or specific to date data type, they are very useful when working with dates. You can use the MAX to find the latest record in a table. You can use the MIN to find the oldest record in a table.

In a table of `employees`, with a `birthday` field storing their date of birth, you can find the oldest employee using the MAX function like this:

```sql
SELECT *
FROM employees
WHERE birthday = (SELECT MAX(birthday) from employees);
```

Or alternatively, like this:

```sql
SELECT *
FROM employees
ORDER BY birthday DESC
LIMIT 1;
```

You could get the youngest employee using the MIN function:

```sql
SELECT *
FROM employees
WHERE birthday = (SELECT MIN(birthday) from employees);
```

```sql
SELECT *
FROM employees
ORDER BY birthday
LIMIT 1;
```

## **Summary**

I hope you now understand the MySQL date functions we discussed here, their variations and arguments, and when to use them so you can write better queries. You can find more of these functions [here](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html).

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

