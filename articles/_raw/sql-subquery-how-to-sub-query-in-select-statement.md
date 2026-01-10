---
title: SQL Subquery – How to Sub Query in SELECT Statement
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-04T17:08:48.000Z'
originalURL: https://freecodecamp.org/news/sql-subquery-how-to-sub-query-in-select-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/subqueries.png
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "A SQL subquery is a query inside a query. So, in SQL, a subquery is also\
  \ called a nested query or an inner query. The outer query in which the inner query\
  \ is inserted is the main query. \nSQL admins usually use subqueries inside the\
  \ WHERE clause to na..."
---

A SQL subquery is a query inside a query. So, in SQL, a subquery is also called a nested query or an inner query. The outer query in which the inner query is inserted is the main query. 

SQL admins usually use subqueries inside the WHERE clause to narrow down the result of the main query (or outer query). 

You usually put subqueries inside brackets and you can use them with comparison operators such as =, <, >, <=, and >=.

A valid use case of a subquery is using it with the SELECT statement when you don’t know the exact value in the database. Even if you know the value, you can still use a subquery to get more data about the value.

In this article, you will learn how to use subqueries inside the SELECT statement.

## How to Use SQL Subqueries with the Select Statement
I’ll be working with an `employees` table in an `employees_data` database. Running `SELECT * FROM employees` gives me the following table:

![ss1](https://www.freecodecamp.org/news/content/images/2022/10/ss1.png) 

### Example 1 of Subqueries

To get the data of those earning more than the average wage, I ran the following query and subquery:

```sql
SELECT * FROM employees
WHERE wage > (SELECT AVG(wage) FROM employees)
```

In the query above:
- the main query selected everything from the employees table
- the subquery (`SELECT AVG(wage) FROM employees`) got the average wage of the employees
- the WHERE clause I specified (`WHERE wage >`) was responsible for getting every employee with a salary less than the average wage. 

The query returns the following data:
![ss2](https://www.freecodecamp.org/news/content/images/2022/10/ss2.png) 

To show you the average wage, in particular, I could run only the subquery:
![ss3](https://www.freecodecamp.org/news/content/images/2022/10/ss3.png) 

You can see the average wage is 1250.0000. So, the query and subquery helped us get all the employees with a wage more than the average wage of 1250.0000.

To adjust the query so I can get data of the employees earning less than the average wage, we only need to change the greater than symbol (>) to less than (<):

```sql
SELECT * FROM employees
WHERE wage < (SELECT AVG(wage) FROM employees)
```

![ss4](https://www.freecodecamp.org/news/content/images/2022/10/ss4.png) 

### Examples of SQL Subqueries

To get the wage of the employees from the USA, including their names and country, I combined the WHERE clause with the IN statement. The IN statement lets you use multiple values inside a WHERE clause.

```sql
SELECT name, country, wage FROM employees 
WHERE country IN (SELECT country 
         FROM employees 
         WHERE country = 'USA') ;
```

![ss5](https://www.freecodecamp.org/news/content/images/2022/10/ss5.png) 

To show you that you can really use multiple values inside the WHERE clause with the help of the IN statement, I got the wage of some employees with known names by running this query:

```sql
SELECT name, wage FROM employees
WHERE name IN ('Denis Jack', 'Ola Ajayi', 'Uche Ugo');
```

Here is the result:

![ss6](https://www.freecodecamp.org/news/content/images/2022/10/ss6.png) 

## Conclusion
This article showed you what you need to know about SQL subqueries and how to use them with the SELECT statement.

However, subqueries are not limited to the SELECT statement only. You can use subqueries in all the CRUD operations of SQL – INSERT, SELECT, UPDATE, and DELETE.

If you find the article helpful, don’t hesitate to share it with your friends and family.



