---
title: How to Use Join and String_agg in Microsoft SQL Server
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T13:49:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-join-and-string-agg-in-microsoft-sql-server
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Untitled-design.png
tags:
- name: database
  slug: database
- name: Microsoft
  slug: microsoft
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By Thanoshan MV

  In this article, we’ll look at how to use join on more than two tables and aggregate
  the result using the function STRING_AGG() in Microsoft SQL Server.

  If you don’t know about Microsoft SQL Server, I’ll briefly explain to you what it...'
---

By Thanoshan MV

In this article, we’ll look at how to use join on more than two tables and aggregate the result using the function `STRING_AGG()` in Microsoft SQL Server.

If you don’t know about Microsoft SQL Server, I’ll briefly explain to you what it is😃. Let's get started.

## What is Microsoft SQL Server?

Microsoft SQL Server is a Relational Database Management System that revolutionized how businesses handle data. It helps you store and manage data.

If you’re familiar with other relational database management systems such as MySQL or PostgreSQL, then picking up Microsoft SQL Server should be pretty easy.

I’m running on the [default instance of SQL server](https://docs.microsoft.com/en-us/sql/relational-databases/lesson-1-connecting-to-the-database-engine?view=sql-server-ver15#connect).

Now, let’s consider a problem.

### The Problem: How to Get Employee Details and Projects

Let’s say we have three tables, namely `Employee`, `Project`, and `EmployeeProject`. The below image is the relational database design:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/msssql--1-.png)
_Figure 1: Relational Database Design for the problem_

The problem is to get all the employee details and their corresponding projects.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Employee-1.png)
_Figure 2: Employee table_

![Image](https://www.freecodecamp.org/news/content/images/2021/03/EmployeeProject-1.png)
_Figure 3: EmployeeProject table_

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Project1.png)
_Figure 4: Project table_

Things to consider: not all the employees from table `Employee` mapped with table `EmployeeProject` and not all the projects in table `Project` mapped with table `EmployeeProject` .

Our main goal is to retrieve all the employee details from table `Employee` whether they are mapped with `EmployeeProject` or not.

We can try to solve this problem by using joins. As you can see, we have to join three tables in order to solve this problem. First, we need to join tables `Employee` and `EmployeeProject` . Then we'll join the resulting table with `Project` .

Let’s go through some scenarios to solve this problem.

### Solution #1: Use Inner Join

Let’s go with `INNER JOIN` everywhere!

```sql
SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId 
FROM Employee AS e INNER JOIN EmployeeProject AS ep 
ON e.Id = ep.EmployeeId
```

This will give us:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/innerjoin1.png)
_Figure 5_

Let’s think of the above table as `Employee-EmployeeProject` . It contains all the employee details as well as their corresponding project ids.

With the help of `Employee-EmployeeProject`, we’ll be able to access the `Project` table. Let’s do that:

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p 
INNER JOIN
(SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId
FROM Employee AS e INNER JOIN EmployeeProject AS ep
ON e.Id = ep.EmployeeId) AS abc 
ON p.Id = abc.ProjectId
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/innerjoin2.png)
_Figure 6_

Great! 😃 Now we are able to retrieve employee details as well as their corresponding projects. But our main goal is missing (that is, to get all the employee details) as we’re missing Sophia Ashley’s details.

Scenario 1 worked, but we didn't accomplish our goal. 😆

### Solution #2: Use Left Join

Let’s get all the details from employees whether they are mapped with `EmployeeProject` or not (our goal) by using `LEFT JOIN` with `Employee` table:

```sql
SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId
```

This query will give us:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/leftjoin-emp-empProj-.png)
_Figure 7_

As you can see from the above figure, we are able to retrieve Sophia Ashley’s details since we’re using `LEFT JOIN` on `Employee` table with `EmployeeProject` table.

Let’s think of the above table as `Employee-EmployeeProject` . It contains all the employee details as well as their corresponding project ids (including `NULL` for when it doesn’t contain any `ProjectId` value).

Similar to scenario 1, now we can access project names since we know `ProjectId` . Remember, our goal is to retrieve all the employee details whether they have a project or not.

To ensure that, we’ll need to retrieve all the values from `Employee-EmployeeProject` when joining with `Project` table:

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-6.png)
_Figure 8_

Great work! We achieved our goal. 😃

This is good stuff. But it would be great if we were able to group these rows and return one row per employee. This is our new wish! 😉

This leads us to question how we can group these results. We can group these rows by using `GROUP BY` .

So, we’ll `GROUP BY` the results in rows by `FirstName` :

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

And the output is:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/groupby-error.png)
_Figure 9_

What happened?

It says column `LastName` is invalid in the select list because it is **not contained** in either an **aggregate function** or the **GROUP BY clause**. This error is applicable to all the remaining columns in the selected list except `FirstName` .

When we try to select values of `FirstName` and group by `FirstName`, it means that we’re going to group all the rows based on `FirstName` only and select the `FirstName` column. For example, let’s select only `FirstName` and group by `FirstName`:

```sql
SELECT abc.FirstName FROM Project AS p RIGHT JOIN 
(SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/groupbyfirstname.png)
_Figure 10_

As you can see in figure 10, we’ve grouped all the rows by `FirstName` . Here, there’s no ambiguity.

Now, let’s select `FirstName`, `LastName`, and group all the rows by `FirstName` :

```sql
SELECT abc.FirstName, abc.LastName FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/groupby-error1.png)
_Figure 11_

If we check out what the values of `LastName` are in Figure 8, we can see that we have two employees with the same `FirstName` but different `LastName`: James Johnson and James Smith.

So, when we try to group all the rows by `FirstName` and select the values of `FirstName` and `LastName`, **it leads us to an ambiguity state.**

Imagine that MSSQL asks us, “You’re selecting `FirstName` ,`LastName` and trying to group all the rows by `FirstName`. But the `FirstName` James has two different `LastName`s, Johnson and Smith. When selecting James’s last name, what should his `LastName` be? Johnson? Smith? or both?” There's ambiguity in MSSQL regarding which one to select.

To solve this FirstName and LastName issue, we can either (option 1) group all the rows by both `FirstName` and `LastName` or (option 2) enclose `LastName` into an [aggregate function](https://docs.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15#:~:text=An%20aggregate%20function%20performs%20a,All%20aggregate%20functions%20are%20deterministic.) to select only one value.

Option 1:

```sql
SELECT abc.FirstName, abc.LastName FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName, abc.LastName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/option1.png)
_Figure 12_

Option 2:

```sql
SELECT abc.FirstName, MAX(abc.LastName) AS LastName FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-11.png)
_Figure 13_

In the above FirstName and LastName issue, although both options work, option 1 makes more sense than option 2.

For more detailed information on ambiguity, check out this [stack overflow question and answer](https://stackoverflow.com/questions/13999817/reason-for-column-is-invalid-in-the-select-list-because-it-is-not-contained-in-e)!

**NOTE:** when you have a `GROUP BY` query, the selected list must be part of either the grouping criteria or must appear in aggregate functions such as `SUM` , `MAX` , `COUNT` and so on.

Again, back to our wish, we’ll try to `GROUP BY` all the rows by all columns:

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-12.png)
_Figure 14_

We’ve successfully grouped all the rows but we couldn’t retrieve one row per each employee, as each row is distinct from others if we consider all columns. This means that grouping them by all columns won’t work.

According to our new goal, we need records for Emma Cooper, James Johnson, James Smith, Maria Garcia, and Sophia Ashley (five rows). 

`GROUP BY` `FirstName` , `LastName` , `City` and `Designation` will give us these five rows, but what about `Project` ? We can't `GROUP BY` it (if we do that then the result would be similar to figure 14), but we can use an aggregate (adding together) function to aggregate `Project`.

Actually, we can use the `[STRING_AGG()](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql?view=sql-server-ver15#syntax)` MSSQL aggregate function to return one row per each employee by concatenating the `Name` column in the `Project` table and `GROUP BY` the remaining columns:

```sql
SELECT abc.FirstName, abc.LastName, abc.Designation, STRING_AGG (p.Name, ',') WITHIN GROUP (ORDER BY p.Name) AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName, abc.LastName, abc.City, abc.Designation
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-13.png)
_Figure 15_

Yay! We’ve done it. 😃 😃

The problem we discussed in this article helped us understand some of the main concepts behind Microsoft SQL Server.

Now we have a basic understanding of how to use join and `STRING_AGG`in Microsoft SQL Server.

Please feel free to let me know if you have any suggestions or questions.

Photo by [MI PHAM](https://unsplash.com/@phammi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/happy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

Connect with me on [Medium](https://mvthanoshan.medium.com/).

**Please support freeCodeCamp in their [Data Science Curriculum Pledge Drive](https://www.freecodecamp.org/news/building-a-data-science-curriculum-with-advanced-math-and-machine-learning/).** 

Thank you 😇

**Happy Coding ❤️**

### To Explore Further

1. `[STRING_AGG](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql?view=sql-server-ver15)` [(Transact-SQL) — Microsoft Docs](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql?view=sql-server-ver15)
2. [Aggregate Functions — Microsoft Docs](https://docs.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15)
3. [An overview of the](https://www.sqlshack.com/string_agg-function-in-sql/) `[STRING_AGG](https://www.sqlshack.com/string_agg-function-in-sql/)`[function in SQL — SQLShack](https://www.sqlshack.com/string_agg-function-in-sql/)
4. [An in-depth guide to `GROUP BY`](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/)

