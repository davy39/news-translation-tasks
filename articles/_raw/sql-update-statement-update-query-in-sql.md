---
title: SQL Update Statement – Update Query in SQL
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-06T21:25:14.000Z'
originalURL: https://freecodecamp.org/news/sql-update-statement-update-query-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-thirdman-5961549.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "Once you have created a table in a database, it will rarely need to stay\
  \ the same forever. You will likely need to modify the records in it. \nAnd to help\
  \ you do that, there is a useful statement, aptly named UPDATE, that you can use\
  \ to change the rec..."
---

Once you have created a table in a database, it will rarely need to stay the same forever. You will likely need to modify the records in it. 

And to help you do that, there is a useful statement, aptly named `UPDATE`, that you can use to change the records as needed.

Note: If the syntax presented here doesn't work, check the documentation for the implementation of SQL you are using. Most stuff works the same across the board, but there are some differences.

# SQL UPDATE Syntax

To use the `UPDATE` method, you first determine which table you need to update with `UPDATE table_name`. After that, you write what kind of change you want to make to the record with the `SET` statement. Finally, you use [a `WHERE` clause](https://www.freecodecamp.org/news/sql-where-clause-examples/) to select which records to change. 

**It's really important to use that `WHERE` clause**, otherwise you are going to make the same change to the whole table.

```sql
UPDATE table_name
SET change to make
WHERE clause to select which records to change;
```

# SQL UPDATE Example

We have a table named `users` that looks like below:

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | NULL | New Jersey | NULL |
| 3 | Robert | 19 | New York | NULL |

There are a few incomplete records in this table. When the users give us the missing info, we can add it using `UPDATE` statements.

The user Robert is missing an email address. All rows selected by the `WHERE` clause will be updated, so we need to be careful: we could select the record to update using the name column, but names are not unique – we could have multiple Roberts in our table. 

The best way to select a row to update it (to make sure you are updating only the row you want to update) is to use the `PRIMARY KEY` column in which values are always unique. In this case that's the column named `id`.

So let's update the email address using this query:

```sql
UPDATE users
SET email="robert@example.com"
WHERE id=3;
```

Now the table will look like this:

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | NULL | New Jersey | NULL |
| 3 | Robert | 19 | New York | robert@example.com |

## How to Update Multiple Columns at the Same Time

Molly is missing a value in two different columns. We can use a single `UPDATE` statement, separating the assignments with commas, like so:

```sql
UPDATE users
SET age=22, email="molly@example.com"
WHERE id=2;
```

The table will now look like this:

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | 22 | New Jersey | molly@example.com |
| 3 | Robert | 19 | New York | robert@example.com |

# Make sure to change only the records you want to change

This is a security concern. Our examples have only few lines, but in a real life situation it could be the database of an app or website with hundreds, thousands, or even millions of users. And you don't want to cause trouble for so many people.

So before you issue an `UPDATE` query, send a `SELECT` query with the same `WHERE` clause. If it returns the record you want to update, go for it. Otherwise you need to change the `WHERE` clause.

For example, before sending the update for the user Molly, we could have sent a `SELECT` statement to check that the clause we have used, `WHERE id=2`, is the correct one:

```sql
SELECT * FROM users
WHERE id=2;
```

This query returns the record below, so you are good to go with the `UPDATE` query to complete the data.

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 2 | Molly | NULL | New Jersey | NULL |

# Conclusion

Once you create your tables and add records to them, there will always be times when you need to update a row. This article explained how to do that using the SQL `UPDATE` statement.

Thanks for reading!

