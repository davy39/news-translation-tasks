---
title: SQL CONVERT – The DATE to String or DATETIME Function
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-10T18:30:50.000Z'
originalURL: https://freecodecamp.org/news/sql-convert-the-date-to-string-or-datetime-function-2
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/dateToString.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'When you''re working with SQL, you''ll need to learn how to format dates
  properly.

  This is because dates are an important aspect of any SQL and other software-related
  activities. You need to be able to work with dates to add timestamps to entries
  and k...'
---

When you're working with SQL, you'll need to learn how to format dates properly.

This is because dates are an important aspect of any SQL and other software-related activities. You need to be able to work with dates to add timestamps to entries and keep track of when things happen, for example. Almost everything is dependent on a date.

In this article, I want to show you how to convert a date and datetime to a string in SQL with the `CONVERT()` and `STR_TO_DATE()` functions.

## What We'll Cover
- [How to Convert Date to String with the `CONVERT()` Function](#heading-how-to-convert-date-to-string-with-the-convert-function)
- [How to Convert Date to String with the `STR_TO_DATE()` Function](#heading-how-to-convert-date-to-string-with-the-strtodate-function)
- [How to use the `DATE_FORMAT()` to Change the Time Format](#heading-how-to-use-the-dateformat-to-change-the-time-format)
- [Conclusion](#heading-conclusion)

## How to Convert Date to String with the `CONVERT()` Function

The `CONVERT()` function expects two arguments:

- the date – has to be a string, or with built-in date getters like `NOW()` or `SYSDATE()`
- the data type – the type of data you want to convert the date to.

Here's the `CONVERT()` function in action:
```sql
SELECT CONVERT(NOW(), CHAR);
```

![ss1](https://www.freecodecamp.org/news/content/images/2023/01/ss1.png) 

The query above used the `NOW()` function to get the current date and time. The second argument, `CHAR`, is the data type the date got converted to. 

You can also use `SYSDATE()` in its place if you want to:

```sql
SELECT CONVERT(SYSDATE(), CHAR);
``` 
![ss2](https://www.freecodecamp.org/news/content/images/2023/01/ss2.png)

There are many other functions you can use for working with dates. I wrote about them [in this tutorial](https://www.freecodecamp.org/news/sql-date-function-query-timestamp-example-format/) if you'd like to read more.

Functions are not the only parameter you can use as the first argument of the convert function. You can use a date written as a string, then specify `DATE` as the data type you want to convert it to:

```sql
SELECT CONVERT("2023-01-10", DATE)
```

![ss3](https://www.freecodecamp.org/news/content/images/2023/01/ss3.png) 


## How to Convert Date to String with the `STR_TO_DATE()` Function

The `STR_TO_DATE()` function is another useful function for converting a date or date time. It accepts two parameters:

- the date – it has to be a string. For example, '09-01-2023'

- the format – the format you want the date to get converted to. For example `mm-dd-yyyy`. You specify the format like this `%d-%m-%Y`.

Here's how the `STR_TO_DATE()` function works:

```sql
SELECT STR_TO_DATE('09-01-2023', '%d-%m-%Y')
```

![ss4](https://www.freecodecamp.org/news/content/images/2023/01/ss4.png) 

You can also use a slash (`/`) to separate the date and the format:

```sql
SELECT STR_TO_DATE('09/01/2023', '%d/%m/%Y')
```

**N.B.**: If you don’t use the same separator for the date and format, you'll get null in return. 

![ss5](https://www.freecodecamp.org/news/content/images/2023/01/ss5.png) 

If you enter the day as the nth day for that date, you have to change the `d` in the format to a capital letter:

```sql 
SELECT STR_TO_DATE('9th-01-2023', '%D-%m-%Y')
``` 

![ss6](https://www.freecodecamp.org/news/content/images/2023/01/ss6.png) 

And if you enter the month as the abbreviation for that month, you have to change the `m` in the format to a capital letter:

```sql
SELECT STR_TO_DATE('9th-JAN-2023', '%D-%M-%Y')
```

![ss7](https://www.freecodecamp.org/news/content/images/2023/01/ss7.png) 

Next, we'll look at how you can work with date formats with the `DATE_FORMAT()` function.


## How to Use the `DATE_FORMAT()` to Change the Time Format

If you want the month as the full name of that month, change the `m` in the format to a capital letter and use the `DATE_FORMAT()` function:

```sql
SELECT DATE_FORMAT('2023-01-09', '%d-%M-%y')
```

![ss8](https://www.freecodecamp.org/news/content/images/2023/01/ss8.png) 

If you want the day as the nth number of that day, change the d in the format to a capital letter:

```sql
SELECT DATE_FORMAT('2023-01-09', '%D-%M-%y')
```

![ss9](https://www.freecodecamp.org/news/content/images/2023/01/ss9.png) 

And if you want the year in full, change the y to a capital letter:

```sql
SELECT DATE_FORMAT('2023-01-09', '%D-%M-%Y')
```

![ss10](https://www.freecodecamp.org/news/content/images/2023/01/ss10.png) 


## Conclusion
This article showed you how to convert a date to a string with the `CONVERT()` and `STR_TO_DATE()` functions. We also looked at how you can change the date format with the `DATE_FORMAT()` function.

If you find this article helpful, don’t hesitate to share it with your friends on social media.


