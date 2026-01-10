---
title: SQL HAVING – How to Group and Count with a Having Statement
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-30T15:59:48.000Z'
originalURL: https://freecodecamp.org/news/sql-having-how-to-group-and-count-with-a-having-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/sqlHaving.png
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'In SQL, you use the HAVING keyword right after GROUP BY to query the database
  based on a specified condition. Like other keywords, it returns the data that meet
  the condition and filters out the rest.

  The HAVING keyword was introduced because the WHE...'
---

In SQL, you use the `HAVING` keyword right after `GROUP BY` to query the database based on a specified condition. Like other keywords, it returns the data that meet the condition and filters out the rest.

The `HAVING` keyword was introduced because the `WHERE` clause fails when used with aggregate functions. So, you have to use the `HAVING` clause with aggregate functions instead of `WHERE`.

With the `HAVING` clause, you can arrange the data in your database into many groups when you use it with the `GROUP BY` keyword. So, you can use it in a large database.

## How to Use the `HAVING` Keyword.
Suppose I have a table named `students` in a `student_scores` database.
`SELECT * FROM students` returns the following:
![ss1-6](https://www.freecodecamp.org/news/content/images/2022/08/ss1-6.png)

You can get only the names and scores by running `SELECT name, score 
FROM students`.
![ss2-6](https://www.freecodecamp.org/news/content/images/2022/08/ss2-6.png)

You can then use the `HAVING` keyword to filter out some students based on a condition. For example, those who have a score greater than 70.

But before that, you must use the `GROUP BY` clause like this:
```sql
GROUP BY name, score
```
This won’t return anything yet. So you need to bring in the `HAVING` keyword:
```sql
HAVING score > 70
```
Now, I’m able to get students who scored higher than 70:
![ss3-6](https://www.freecodecamp.org/news/content/images/2022/08/ss3-6.png) 

The full query looks like this:
```sql
SELECT name, score 
FROM students 
GROUP BY name, score
HAVING score > 70
```
I’m also able to get the students who scored more than 90 this way:
```sql
SELECT name, score 
FROM students 
GROUP BY name, score 
HAVING score > 90
```

The table also has an age column, so I can get the students who are over 14 years this way:
```sql
SELECT name, age 
FROM students 
GROUP BY name, age 
HAVING age > 14
```
![ss4-7](https://www.freecodecamp.org/news/content/images/2022/08/ss4-7.png) 

### An error occurs if you use `WHERE` with an aggregate function
```sql
SELECT name, count(*)
FROM students
GROUP BY name
WHERE COUNT(*) > 0
```
![ss5-7](https://www.freecodecamp.org/news/content/images/2022/08/ss5-7.png) 

The error goes away if you use `HAVING`:
```sql
SELECT name, count(*)
FROM students
GROUP BY name
HAVING COUNT(*) > 0
```
![ss6-6](https://www.freecodecamp.org/news/content/images/2022/08/ss6-6.png) 

### You can use any operator you want!
The operator is not exclusive to comparisons. So, I’m able to get students who are 13 years by changing the HAVING statement to `HAVING age = 13`:
![ss7-5](https://www.freecodecamp.org/news/content/images/2022/08/ss7-5.png) 

I got the students who scored 90 this way: 
```sql
SELECT name, score 
FROM students 
GROUP BY name, score 
HAVING score = 90
```
![ss8-5](https://www.freecodecamp.org/news/content/images/2022/08/ss8-5.png) 

### If the condition in the HAVING statement is not met, no row will be returned:
```sql
SELECT name, score 
FROM students 
GROUP BY name, score 
HAVING score = 100
```
![ss9-4](https://www.freecodecamp.org/news/content/images/2022/08/ss9-4.png) 

### An Error Occurs if you Use `HAVING` without `GROUP BY`
```sql
SELECT COUNT(*)
FROM students 
HAVING score > 80
```
![ss10-4](https://www.freecodecamp.org/news/content/images/2022/08/ss10-4.png) 

In this case, you have to use the `WHERE` clause:
```sql
SELECT COUNT(*)
FROM students 
WHERE score > 80
```
![ss11-4](https://www.freecodecamp.org/news/content/images/2022/08/ss11-4.png) 

## Wrapping Up

In this article, you learned how to query databases using the `HAVING` keyword. 

Remember that you have to use the `HAVING` clause with `GROUP BY` so you can get the desired data, just as you’ve seen in this article. 

In situations where you can’t use the `HAVING` clause, you probably need to use `WHERE`.

Thank you for reading.                                       




