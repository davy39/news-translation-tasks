---
title: SQL Aggregate Functions – With Example Data Queries for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-15T15:48:09.000Z'
originalURL: https://freecodecamp.org/news/sql-aggregate-functions-with-example-data-queries-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/sql-aggregate-functions.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Veronica Stork\nWhat is an Aggregate Function?\nSQL aggregate functions\
  \ will seem very familiar if you have worked with spreadsheets. \nHave you ever\
  \ used SUM in Google Sheets or Excel? The SUM function exists in SQL as well, and\
  \ is called an aggrega..."
---

By Veronica Stork

## What is an Aggregate Function?

SQL aggregate functions will seem very familiar if you have worked with spreadsheets. 

Have you ever used `SUM` in Google Sheets or Excel? The `SUM` function exists in SQL as well, and is called an _aggregate function._ 

Aggregate functions do a particular task across database rows. For example, say you run a yearly fundraiser. You have a database of donors along with the amount they donated each year. 

You might use the `COUNT` function to determine how many donations were received, or the `SUM` function to find out how much you have made in total this year. 

We will use the following small data set for illustrative purposes.

| name | email | donation_2020 | donation_2021
| ---- | ------ | -------- | ----------- |
| Andrew Jones | ajones@someemail.com | 400 | 500 |
| Maria Rodriguez | maria77@someemail.com | 1000 | 350 |
| Gerry Ford | NULL | 25 | 25 |
| Isabella Munn | isamun91@someemail.com | 250 | NULL |
| Jennifer Ward | jjw1972@someemail.com | 2000 | 2300 |
| Rowan Parker | NULL | 5000 | 4000 |

In this article, we will cover the following aggregate functions: `COUNT`, `SUM`, `MIN/MAX`, and `AVG`.

## The COUNT function

The `COUNT` function returns a count of rows. In its simplest form, `COUNT` counts the total number of rows in your table. 

To get that value from our donor table, you would run the following query: `SELECT COUNT(*) FROM donors`. This will return the total number of donors, which in this case is 6. Here, of course, you could just count the rows in this example, but let's imagine there are a lot more rows.

You might want to count only certain rows, however. In our donor database example, say you want to count the number of donors who have an email listed. 

If you run the query `SELECT COUNT(email) FROM donors`, you will get 4, which is the total number of donors with non-null values in the email column. 

Keep in mind that unless you use an alias, the column returned will simply be labeled "count". If you want a more descriptive name, run a query using `AS` to create an alias, for example `SELECT COUNT(email) FROM donors AS email_count`.

## The SUM function

SUM is a super handy aggregate function you can use to add together numerical values from different rows. 

In our donor database, you could use `SUM` to add up all of the 2021 donations by running the query `SELECT SUM(donation_2021) FROM donors`. Note that `SUM` ignores `NULL` values, so the result of this query will be 7175.

Remember that `SUM`, like other aggregate functions, works across rows, not columns. 

So in our example, you could use it to add together everyone’s donations from 2021 (represented by the `donation_2021` column), but not to add together all of one person's donations from the `donation_2020` column and the `donation_2021` column.

## The MIN and MAX functions

As you might guess, you can use MIN and MAX to find the minimum and maximum values in a particular column of a database. 

In our example data, imagine you want to find the minimum and maximum donation amounts for 2021. You could do this by running the query: `SELECT MIN(donation_2021) AS "Minimum donation 2021", MAX(donation_2021) AS "Maximum donation 2021" FROM donors`. 

Note that in this example, we are assigning aliases to the returned columns using quotation marks. Quotation marks are not necessary if your alias has no spaces in it, but we are using quotes here so we can use spaces.

An interesting side note: you can use `MIN` and `MAX` on non-numeric values. `MIN` will find the smallest number, the closest letter to A, or the earliest date. `MAX` will find the largest number, the closest letter to Z, or the latest date. Very handy!

## The AVG function

Finally, the `AVG` function averages numeric values from a particular column. As with `SUM`, it ignores `NULL` values. 

To get an average of all of the donations from 2020, you can run the following query: `SELECT AVG(donation_2020) FROM donors`. The result of this query would be 1435.

## Wrapping Up

As you have seen, aggregate functions are easy and useful tools for analyzing data in SQL. `AVG`, `MIN/MAX`, `SUM` , and `COUNT` are an important addition to your SQL skillset.  


  


  

