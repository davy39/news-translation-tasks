---
title: SQL Aggregate Functions – How to GROUP BY in MySQL and PostgreSQL
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-01T15:57:13.000Z'
originalURL: https://freecodecamp.org/news/sql-aggregate-functions-how-to-group-by-in-mysql-and-postgresql
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/agg.png
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
seo_desc: "In SQL, aggregate functions let you perform a calculation on multiple data\
  \ and return a single value. That’s why they are called “aggregate” functions. \n\
  Those aggregate functions are AVG(), COUNT(), SUM(), MIN(), and MAX(). \nWhile making\
  \ queries with..."
---

In SQL, aggregate functions let you perform a calculation on multiple data and return a single value. That’s why they are called “aggregate” functions. 

Those aggregate functions are `AVG()`, `COUNT()`, `SUM()`, `MIN()`, and `MAX()`. 

While making queries with the aggregate functions, you can also use them in combination with the `GROUP BY` clause and `HAVING` statement in any relational database – MySQL PostgreSQL, and others. 

In this article, you will learn how to use aggregate functions on their own and with the `GROUP BY` clause and `HAVING` statement.

## What We'll Cover
- [How to Use Aggregate Functions](#heading-how-to-use-aggregate-functions)
- [Syntax of Aggregate Functions](#heading-syntax-of-aggregate-functions)
- [How to Use the `AVG()` Aggregate Function](#heading-how-to-use-the-avg-aggregate-function)
  - [How to use the `AVG()` Function with `GROUP BY` and `HAVING`](#heading-how-to-use-the-avg-function-with-group-by-and-having)
- [How to Use the `COUNT()` Aggregate Function](#heading-how-to-use-the-count-aggregate-function)
  - [How to Use `COUNT()` with `GROUP BY` and `HAVING`](#heading-how-to-use-count-with-group-by-and-having)  
- [How to Use the `MAX()` Aggregate Function](#heading-how-to-use-the-max-aggregate-function)
  - [How to Use `MAX()` with `GROUP BY` and `HAVING`](#heading-how-to-use-max-with-group-by-and-having)
- [How to Use the `MIN()` Aggregate Function](#heading-how-to-use-the-min-aggregate-function)
  - [How to Use `MIN()` with `GROUP BY` and `HAVING` ](#heading-how-to-use-min-with-group-by-and-having)
- [How to Use the `SUM()` Aggregate Function](#heading-how-to-use-the-sum-aggregate-function)
  - [How to Use `SUM()` with `GROUP BY` and `HAVING`](#heading-how-to-use-sum-with-group-by-and-having)  
- [Conclusion](#heading-conclusion)


## How to Use Aggregate Functions
 
To show you how the aggregate functions work, I’ll be working with an `employees` table in an `employees_data` database.
 
Running `SELECT * FROM employees` got me the following:
![ss1](https://www.freecodecamp.org/news/content/images/2022/09/ss1.png)

## Syntax of Aggregate Functions
The syntax for working with aggregate functions looks like this:
```sql
aggregate_function(MODIFIER | expression)
```
- the aggregate function could be `AVG`, `COUNT`, `MAX`, `MIN`, or `SUM`
- the modifier could be all the values or the values in a particular column

This syntax would make more sense in practice, so let’s get to use it with the aggregate functions.
 
## How to Use the `AVG()` Aggregate Function
The `AVG()` aggregate function gets the total number of data and calculates their average.

I was able to get the average wage paid to the employees this way:
```sql
SELECT AVG(wage) 
FROM employees
```
![ss2](https://www.freecodecamp.org/news/content/images/2022/09/ss2.png) 

The query below gets the average wage of junior developers:
```sql
SELECT AVG(wage) 
FROM employees
WHERE role = "Junior dev"
```
![ss3](https://www.freecodecamp.org/news/content/images/2022/09/ss3.png) 

### How to use the `AVG()` Function with `GROUP BY` and `HAVING`
You can get the average number of entries (rows) in a particular column with the `GROUP BY` clause and `HAVING` statement. This means you have to combine those two with `AVG()`.

For instance, I was able to get the average wage paid to employees in each row with this query:
```sql
SELECT role, AVG(wage) 
FROM employees
GROUP BY role
```
![ss4](https://www.freecodecamp.org/news/content/images/2022/09/ss4.png) 

I was also able to get the average wage of senior developers by using the HAVING statement:
```sql
SELECT role, AVG(wage) 
FROM employees
GROUP BY role
HAVING role = "Senior dev"
```
![ss5](https://www.freecodecamp.org/news/content/images/2022/09/ss5.png) 

## How to Use the `COUNT()` Aggregate Function

`COUNT()` returns the number of rows in a table based on the condition (or filter) you apply.

For example, to get the total number of rows, I ran the query below:
```sql
SELECT COUNT(*) 
FROM employees
```
And I got 20:
![ss6](https://www.freecodecamp.org/news/content/images/2022/09/ss6.png) 

To get the total number of employees from the USA, I ran the query below:
```sql
SELECT COUNT(*) 
FROM employees
WHERE country = "USA"
```
![ss7](https://www.freecodecamp.org/news/content/images/2022/09/ss7.png) 

And to get the employees who are technical writers, I did this:
```sql
SELECT COUNT(*) 
FROM employees
WHERE role = "Tech Writer"
```
![ss8](https://www.freecodecamp.org/news/content/images/2022/09/ss8.png) 

### How to Use `COUNT()` with `GROUP BY` and `HAVING`
In a large database, you can use the `GROUP BY` clause and `HAVING` statement in combination with COUNT() to get the total number of entries (rows) in a particular column.

In the database I’m using in this article, I was able to get the total number of employees in each row with the GROUP BY clause:
```sql
SELECT role, COUNT(*) 
FROM employees
GROUP BY role
```
![ss9](https://www.freecodecamp.org/news/content/images/2022/09/ss9.png) 

To get the number of only the employees that are senior developers, I attached `HAVING role = "Senior dev"` to the query:
```sql
SELECT role, COUNT(*) 
FROM employees
GROUP BY role
HAVING role = "Senior dev"
```
![ss10](https://www.freecodecamp.org/news/content/images/2022/09/ss10.png) 

## How to Use the `MAX()` Aggregate Function
The `MAX()` function returns the maximum value within non-NULL values. This means it would ignore fields that are empty and return the highest value within those that are not empty. 

For example, to get the highest wage in the `employees` table, I used the `MAX()` function like this:
```sql
SELECT MAX(wage) 
FROM employees
```
![ss11](https://www.freecodecamp.org/news/content/images/2022/09/ss11.png) 

To get the maximum wage for mid-level developers, I used the `WHERE` statement:
```sql
SELECT MAX(wage) 
FROM employees
WHERE role = "Mid level dev"
```
![ss12](https://www.freecodecamp.org/news/content/images/2022/09/ss12.png) 

### How to Use `MAX()` with `GROUP BY` and `HAVING`
To get the maximum wage in each role, the `GROUP BY` clause comes in handy:
```sql
SELECT role, MAX(wage) 
FROM employees
GROUP BY role
```
![ss13](https://www.freecodecamp.org/news/content/images/2022/09/ss13.png) 

And to get the maximum wage in a particular role, combining the HAVING statement with the `GROUP BY` clause gets it done: 

```sql
SELECT role, MAX(wage) 
FROM employees
GROUP BY role
HAVING role = "Tech writer"
```
![ss14](https://www.freecodecamp.org/news/content/images/2022/09/ss14.png) 

## How to Use the `MIN()` Aggregate Function
The `MIN()` function is the opposite of the `MAX()` function – it returns the minimum value within non-NULL values. 

For example, I got the lowest wage on the `employees` table this way:
```sql
SELECT MIN(wage) 
FROM employees
```
![ss15](https://www.freecodecamp.org/news/content/images/2022/09/ss15.png) 

### How to Use `MIN()` with `GROUP BY` and `HAVING`
Again, to get the minimum wage in each role, the `GROUP BY` clause can get it done:
```sql
SELECT role, MIN(wage) 
FROM employees
GROUP BY role
```
![ss16](https://www.freecodecamp.org/news/content/images/2022/09/ss16.png) 

And to get the minimum wage of a particular role, the `HAVING` statement and `GROUP BY` clause are what to use:
```sql
SELECT role, MIN(wage) 
FROM employees
GROUP BY role
HAVING role = "Junior dev"
```
![ss17](https://www.freecodecamp.org/news/content/images/2022/09/ss17.png) 

## How to Use the `SUM()` Aggregate Function
The SUM() aggregate function adds the number of entries in a column based on the filter applied.

The query below gets the total number of wages paid to employees:
```sql
SELECT SUM(wage) 
FROM employees
```
![ss18](https://www.freecodecamp.org/news/content/images/2022/09/ss18.png) 

### How to Use SUM() with `GROUP BY` and `HAVING`

To get the sum of the total wages paid for employees in each role, I selected the role, used `SUM()` on the wages, and grouped them by the role:
```sql
SELECT role, SUM(wage) 
FROM employees
GROUP BY role
```
![ss19](https://www.freecodecamp.org/news/content/images/2022/09/ss19.png) 

To get the total wages paid to technical writers only, I used the `HAVING` statement:
```sql
SELECT role, SUM(wage) 
FROM employees
GROUP BY role
HAVING role = "Tech Writer"
```
![ss20](https://www.freecodecamp.org/news/content/images/2022/09/ss20.png) 

## Conclusion
This article took you through what aggregate functions are in SQL, their syntax, and how to use them. 

In addition, you also learned how to use aggregate functions with the `GROUP BY` clause, `HAVING`, and `WHERE` statements.

If you want to learn how the `HAVING` statement works, you should read [this article](https://www.freecodecamp.org/news/sql-having-how-to-group-and-count-with-a-having-statement/) I wrote on it.

Thank you for reading.



