---
title: SQL Inner Join – How to Join 3 Tables in SQL and MySQL
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-04-01T18:19:05.000Z'
originalURL: https://freecodecamp.org/news/sql-inner-join-how-to-join-3-tables-in-sql-and-mysql
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pixabay-269399--1-.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'When you''re working with your database, you might need to put together
  data from a few different tables. This article will show you how.

  I have already written about SQL joins here and here, but let''s take a moment to
  review how a join works first, a...'
---

When you're working with your database, you might need to put together data from a few different tables. This article will show you how.

I have already written about SQL joins [here](https://www.freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example/) and [here](https://www.freecodecamp.org/news/sql-left-join-example-join-statement-syntax/), but let's take a moment to review how a join works first, and particularly the syntax specific to MySQL.

## SQL Join Statement

Join is a statement that lets you put together two tables, matching rows that are related to each other, and keeping only the rows that can be matched, not keeping unpaired rows.

```sql
SELECT * FROM table1 
  INNER JOIN table2
  ON table1.id = table2.id;
```

The `SELECT ... FROM` statement indicates which is the first table, then the second table name is written just after the `INNER JOIN` keywords. 

How the two tables should be joined is written in the `ON` statement. In this case the two tables are joined using the relationship `table1.id = table2.id`.

It is possible to use multiple join statements together to join more than one table at the same time.

```sql
SELECT *
  FROM table1
  INNER JOIN table2
  ON table1.id = table2.id
  INNER JOIN table3
  ON table2.id = table3.id;
```

To do that you add a second `INNER JOIN` statement and a second `ON` statement to indicate the third table and the second relationship.

Let's talk a moment about the relationships you can have between tables and why you might want to join three tables together.

## Relationships Between Tables in SQL

When you have tables that are related to each other, their relationships could be one of various types.

### one-to-many

In a one-to-many kind of relationship, one row of the first table can be related to multiple rows of the second table.

In a relational database this can be implemented with the second table having a `first_table_id` column that says to which row of the first table that row is related.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-11.png)

### many-to-one

In a many-to-one kind of relationship, one row of the first table can be related to one single row of the second table, and one row of the second table can be related to multiple rows of the first table.

In a relational database this can be implemented with the first table having a `second_table_id` column that says to which row of the second table that row is related.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-10.png)
_Many-to-one_

### many-to-many

In this case multiple rows are related to multiple rows.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-9.png)
_Many-to-many_

This kind of relationship can't be represent as is with SQL tables – you need to add a coupling table between the two tables so that only many-to-one and one-to-many relationships are present between tables. 

Each row of the table in the middle represents one relationship between the rows of the left table and and the rows of the right table.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-12.png)

In practice in MySQL, that middle table will have a column for `first_table_id` and a column for `second_table_id`, with each combination being unique.

## Joining SQL Tables in Practice

Let's imagine we have an organization's database, where we have a table with teams (their name, and other identifing info), and a table with projects (name, progress, and so on).

| id | team_name | specialty |
| --- | --- | --- | --- |
| 1 | Banana Throwers | Bananas |
| 2 | Wood gnawers | Gnawing on wood |
| 3 | The Pink Elephants | Stomping on the ground |
| 4 | Fluffy potatoes | Working and sleeping |

| id | project_name | progress |
| --- | --- | --- |
| 1 | Dam building | Some more wood gnawing and ground stomping needed |
| 2 | Banana Cake | Someone is eating all the bananas |
| 3 | Sleep research | To much sleeping not enough research |

As a team can work on multiple projects, and a project can be worked on by multiple teams, there is also a third table that keeps track of team-project matches.

| project_id | group_id |
| --- | --- |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 3 | 1 |
| 3 | 2 |
| 3 | 3 |
| 3 | 4 |

We can use a `JOIN` statement to put everything together when we need to view the info from the tables in a human readable way, like this:

```mysql
SELECT
  teams.team_name AS team_name,
  projects.project_name AS project_name
FROM TABLE teams
INNER JOIN matches
  ON teams.id = matches.team_id
INNER JOIN matches
  ON matches.project_id = projects.id
ORDER BY teams.id;
```

We choose which columns to show from each table with a `SELECT` statement.

We specify how the rows of the tables are to be combined with an `ON` statement.

And we order the rows in the way we prefer with an `ORDER BY` statement.

The `ON` statements `teams.id = matches.team_id` and `matches.projects_id = projects.id` mean that the rows are combined using the rows of the `matches` table. Each row of the output table has the project name and the team name combined using the pairs of project id and team id in the `matches` table.

The output table will look like below. 

| Team_name | Project_name |
| --- | --- |
| Banana Throwers | Banana Cake |
| Banana Throwers | Sleep Research |
| Wood gnawers | Dam Bulding |
| Wood gnawers | Sleep Research |
| The Pink Elephants | Dam Building |
| The Pink Elephants | Dam Building |
| Fluffy potatoes | Sleep Research |

There is no column directly from the `matches` table. The `matches` table is not shown in the output but it is used as instructions for how to combine the rows of the `teams` and `projects` tables.

## Conclusion

The `JOIN` statement lets you join together one or more tables. It has to be used in conjunction with the `ON` statement to determine the relationship between the rows of a table and the rows of a different table. 

In this article you have learned how to use the `JOIN` statement to join together three different tables.

