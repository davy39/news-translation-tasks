---
title: Learn SQL with These 5 Easy Recipes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-23T21:25:00.000Z'
originalURL: https://freecodecamp.org/news/sql-recipes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a17740569d1a4ca236c.jpg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By Jackson Bates

  SQL (Structured Query Language) is a powerful and expressive language for dealing
  with data from relational databases. But it can seem daunting to the uninitiated.

  The "recipes" I''m going to share with you today are some basic exampl...'
---

By Jackson Bates

SQL (Structured Query Language) is a powerful and expressive language for dealing with data from relational databases. But it can seem daunting to the uninitiated.

The "recipes" I'm going to share with you today are some basic examples from a simple database. But the patterns you'll learn here can help you write precise queries. These will have you feeling like the data equivalent of a MasterChef in no time.

_A note about syntax: Most of the queries below are written in the style used for PostgreSQL from the psql command line. Different SQL engines can use slightly different commands._

_Most of the queries below should work in most engines without tweaking, although some engines or GUI tools might require the omission of quotation marks around table and column names._

## Dish 1: Return all the users created within a particular date range

### Ingredients

* SELECT
* FROM
* WHERE
* AND

### Method

```sql
SELECT *
FROM "Users"
WHERE "created_at" > "2020-01-01"
AND "created_at" < "2020-02-01";
```

This simple dish is a versatile staple. Here we are returning users that meet two particular conditions by chaining the `WHERE` conditions with an `AND` statement. We can extend this further with more `AND` statements.

While the example here is for a specific date range, most queries require some sort of condition to filter the data usefully.

## Dish 2: Find all comments for a book, including the user that made the comment

### (New) Ingredients

* JOIN

### Method

```sql
SELECT "Comments"."comment", "Users"."username"
FROM "Comments"
JOIN "Users"
ON "Comments"."userId" = "Users"."id"
WHERE "Comments"."bookId" = 1;
```

This query assumes the following table structure:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/simpleERD.png)
_ERD showing Users that can have many Comments, and Books that can also have many Comments_

One of the things that can start to confuse novices with SQL is the use of JOINs to find data from associated tables.

The ERD (Entity Relationship Diagram) above shows three tables, Users, Books, and Comments, and their associations.

Each table has an `id` which is **bold** in the diagram to show that it is the primary key for the table. This primary key is always a unique value and is used to tell records in tables apart.

The _italic_ column names `userId` and `bookId` in the Comments table are foreign keys, which means they are the primary key in other tables and are used here to reference those tables.

The connectors in the ERD above also show the nature of the relationships between the 3 tables. 

The single point end on the connector means 'one' and the split end on the connector means 'many', so the User table has a 'one-to-many' relationship with the Comments table. 

A user can have many comments, for example, but a comment can only belong to a single user. Books and Comments have the same relationship in the diagram above.

The SQL query should make sense based on what we now know. We are returning only the named columns, i.e. the comment column from the Comments table and the username from the associated Users table (based on the referenced foreign key). In the example above we constrain the search to a single book, again based on the foreign key in the Comments table.

## Dish 3: Count the number of comments added by each user

### (New) Ingredients

* COUNT
* AS
* GROUP BY

### Method

```sql
SELECT "Users"."username", COUNT("Comments"."id") AS "CommentCount"
FROM "Comments"
JOIN "Users"
ON "Comments"."userId" = "Users"."id"
GROUP BY "Users"."id";
```

This little query does a few interesting things. The easiest to understand is the `AS` statement. This allows us to arbitrarily, and temporarily, rename columns in the data that gets returned. Here we rename the derived column, but it's also useful when you have multiple `id` columns, since you can rename them things like `userId` or `commentId` and so on.

The `COUNT` statement is a SQL function that, as you'd expect, counts things. Here we count the number of comments associated with a user. How does it work? Well the `GROUP BY` is the important final ingredient.

Let's briefly imagine a slightly different query:

```sql
SELECT "Users"."username", "Comments"."comment"
FROM "Comments"
JOIN "Users"
ON "Comments"."userId" = "Users"."id";
```

Notice, no counting or grouping. We just want each comment and who made it.

The output might look something like this:

```
|----------|-----------------------------|
| username | comment                     |
|----------|-----------------------------|
| jackson  | it's good, I liked it       |
| jackson  | this was ok, not the best   |
| quincy   | excellent read, recommended |
| quincy   | not worth reading           |
| quincy   | I haven't read this yet     |
------------------------------------------
```

Now imagine we wanted to count Jackson's and Quincy's comments - easy to see at a glance here, but harder with a larger dataset as you can imagine.

The `GROUP BY` statement essentially tells the query to treat all the `jackson` records as one group, and all the `quincy` records as another. The `COUNT` function then counts the records in that group and returns that value:

```
|----------|--------------|
| username | CommentCount |
|----------|--------------|
| jackson  | 2            |
| quincy   | 3            |
---------------------------
```

## Dish 4: Find users that have not made a comment

### (New) Ingredients

* LEFT JOIN
* IS NULL

### Method

```sql
SELECT "Users"."username"
FROM "Users"
LEFT JOIN "Comments"
ON "Users"."id" = "Comments"."userId"
WHERE "Comments"."id" IS NULL;
```

The various joins can get very confusing, so I won't unpack them here. There is an excellent breakdown of them here: [Visual Representations of SQL Joins](https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins), which also accounts for some of the syntax differences between various flavours or SQL.

Let's imagine an alternate version of this query quickly:

```
SELECT "Users"."username", "Comments"."id" AS "commentId"
FROM "Users"
LEFT JOIN "Comments"
ON "Users"."id" = "Comments"."userId";
```

We still have the `LEFT JOIN` but we've added a column and removed the `WHERE` clause.

The return data might look something like this:

```
|----------|-----------|
| username | commentId |
|----------|-----------|
| jackson  | 1         |
| jackson  | 2         |
| quincy   | NULL      |
| abbey    | 3         |
------------------------
```

So Jackson is responsible for comments 1 and 2, Abbey for 3, and Quincy has not commented.

The difference between a `LEFT JOIN` and an `INNER JOIN` (what we've been calling just a `JOIN` until now, which is valid) is that the inner join only shows records where there are values for both tables. A left join, on the other hand, returns everything from the first, or left, table (the `FROM` one) even if there is nothing in the right table. An inner join would therefore only show the records for Jackson and Abbey.

Now that we can visualize what the `LEFT JOIN` returns, it's easier to reason about what the `WHERE...IS NULL` part does. We return only those users where the commentId is a null value, and we don't actually need the null value column included in the output, hence its original omission.

## Dish 5: List all comments added by each user in a single field, pipe separated

### (New) Ingredients

* GROUP_CONCAT or STRING_AGG

### Method (MySQL)

```sql
SELECT "Users"."username", GROUP_CONCAT("Comments"."comment" SEPARATOR " | ") AS "comments"
FROM "Users"
JOIN "Comments"
ON "Users"."id" = "Comments"."userId"
GROUP BY "Users"."id";
```

### Method (Postgresql)

```sql
SELECT "Users"."username", STRING_AGG("Comments"."comment", " | ") AS "comments"
FROM "Users"
JOIN "Comments"
ON "Users"."id" = "Comments"."userId"
GROUP BY "Users"."id";
```

This final recipe shows a difference in syntax for a similar function in two of the most popular SQL engines.

Here is a sample output we might expect:

```
|----------|---------------------------------------------------|
| username | comments                                          |
|----------|---------------------------------------------------|
| jackson  | it's good, I liked it | this was ok, not the best |
| quincy   | excellent read, recommended | not worth reading   |
----------------------------------------------------------------
```

We can see here that the comments have been grouped and concatenated / aggregated, that is joined together in a single record field.

## **Bon** **Appetit**

Now that you have some SQL recipes to fall back on, get creative and serve up your own data dishes! 

I like to think of `WHERE`, `JOIN`, `COUNT`, `GROUP_CONCAT` as the _Salt, Fat, Acid, Heat_ of database cooking. Once you know what you're doing with these core elements, you are well on your way to mastery.

If this has been a useful collection, or you have other favourite recipes to share, drop me a comment or follow on Twitter: [@JacksonBates](https://twitter.com/jacksonbates).

