---
title: SQL DATE – Function, Query, Timestamp Example Format
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-11-15T18:58:58.000Z'
originalURL: https://freecodecamp.org/news/sql-date-function-query-timestamp-example-format
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/date.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Dates are an integral part of any programming language, and SQL is no exception.
  When you insert data into your SQL database, you can add a date and query the database
  based on that date.

  In this article, you’ll learn about DATE functions in SQL and ...'
---

Dates are an integral part of any programming language, and SQL is no exception. When you insert data into your SQL database, you can add a date and query the database based on that date.

In this article, you’ll learn about DATE functions in SQL and how to query a database with dates. We'll also take a look at some time functions.

## What We'll Cover
- [Date Functions in SQL](#heading-date-functions-in-sql)
  - [ADDDATE()](#heading-adddate)
  - [CURRENT_DATE()](#heading-currentdate)
  - [CURRENT_TIME();](#heading-currenttime)
  - [CURRENT_TIMESTAMP();](#heading-currenttimestamp)
  - [NOW()](#heading-now)
  - [DATE](#heading-date)
  - [DATE_SUB](#heading-datesub)
  - [DATEDIFF](#heading-datediff)
  - [DAY](#heading-day)
  - [MONTH](#heading-month)
  - [YEAR](#heading-year)
- [How to Query a Database Based on Dates](#heading-how-to-query-a-database-based-on-dates)
- [Conclusion](#heading-conclusion)


## Date Functions in SQL
### `ADDDATE()`

The ADDDATE() function does what the name implies – it adds an interval to a `date` or `datetime`. 

You can use the `ADDDATE()` function in this format: `ADDDATE(date, INTERVAL value addunit)`.

- `date` is the date you’re working with. For MySQL, the date format is YYY-MM-DD and is required.
- `INTERVAL` is a required keyword
- `value` is an integer representing the interval you want to add
- `addunit` is what the interval should represent. That is year, month, day, hours, minutes, seconds, and other relevant units.

For example, running the query below returns '2022-10-22'. This means that 10 days got added to '2022-10-12'. 

```sql
SELECT ADDDATE("2022-10-12", INTERVAL 10 DAY);
```

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/11/ss1-2.png) 

If you want, you can use it with month or year:

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/11/ss2-2.png) 

### `CURRENT_DATE()`

The CURRENT_DATE() function shows exactly what it says – the current date. It returns the date in the YYYY-MM-DD format.

For instance, `SELECT CURRENT_DATE()` returns the date I started writing this article:
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/11/ss3-1.png) 

### `CURRENT_TIME();`

The CURRENT_TIME function shows the current time.

```sql
SELECT CURRENT_TIME();
```

![ss4-1](https://www.freecodecamp.org/news/content/images/2022/11/ss4-1.png) 

### `CURRENT_TIMESTAMP();`

The current timestamp function returns the current date and time. It’s the combination of CURRENT_DATE() and CURRENT_TIME().

```sql
SELECT CURRENT_TIMESTAMP();
```

### `NOW()`

The NOW() function returns the current date and time.

```sql
SELECT NOW();
```

![ss5-1](https://www.freecodecamp.org/news/content/images/2022/11/ss5-1.png) 

### `DATE`

You can use the DATE function to extract the date part of a timestamp.

```sql
SELECT DATE("2022-11-14 12:00:00");
```

![ss6](https://www.freecodecamp.org/news/content/images/2022/11/ss6.png) 

### `DATE_SUB`

The DATE_SUB() function subtracts a day, month, or year from a date.
In the query below, I subtracted 10 days from the date I started writing this article:

```sql
SELECT DATE_SUB("2022-11-14", INTERVAL 10 DAY);
```

![ss7](https://www.freecodecamp.org/news/content/images/2022/11/ss7.png) 

### `DATEDIFF`

The DATEDIFF() function returns the number of days between two dates. 

```sql
SELECT DATEDIFF("2023-11-14", "2022-11-14");
```

![ss8](https://www.freecodecamp.org/news/content/images/2022/11/ss8.png) 

### `DAY`

This function returns the day within a specified date.

```sql
SELECT DAY("2022-11-14");
```

![ss9](https://www.freecodecamp.org/news/content/images/2022/11/ss9.png) 

### `MONTH`

The MONTH function returns the month in a specified date.

```sql
SELECT MONTH("2022-11-14");
```

![ss10](https://www.freecodecamp.org/news/content/images/2022/11/ss10.png) 

### `YEAR`

The YEAR function returns the year in a specified date.

```sql
SELECT YEAR("2022-11-14");
```

![ss11](https://www.freecodecamp.org/news/content/images/2022/11/ss11.png) 

## How to Query a Database Based on Dates
To show you how to query a database using dates, I’ll be using the table below:

![ss12](https://www.freecodecamp.org/news/content/images/2022/11/ss12.png) 

To select some particular date between one date and another, you can use the `BETWEEN` and `AND` keywords while specifying the dates. 

In the query below, I select all the items added to the database in 2021:

```sql
SELECT *
FROM brands
WHERE date_added BETWEEN "2021-01-01" AND "2021-12-31";
```

![ss13-1](https://www.freecodecamp.org/news/content/images/2022/11/ss13-1.png) 

Combining the `DATE_SUB()` and `NOW()` functions, I was able to get the items added to the database in the last 3 months:

```sql
SELECT *
FROM brands
WHERE date_added > DATE_SUB(NOW(), INTERVAL 3 MONTH);
```

![ss14](https://www.freecodecamp.org/news/content/images/2022/11/ss14.png)

## Conclusion
This article showed you some important functions you can use to work with dates and query your database within SQL.

If you find the article useful, don’t hesitate to share it with friends and family. 

Thanks for reading.


