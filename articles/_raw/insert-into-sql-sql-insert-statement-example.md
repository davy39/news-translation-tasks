---
title: Insert Into SQL – SQL Insert Statement Example
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-06T16:10:39.000Z'
originalURL: https://freecodecamp.org/news/insert-into-sql-sql-insert-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-markus-spiske-177598.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'If you''ve created an empty table in your database you''ll need to add
  records to it. In this article you will learn how you can add records to your tables
  using the INSERT statement in SQL.

  Keep in mind that if the syntax presented here doesn''t work, ...'
---

If you've created an empty table in your database you'll need to add records to it. In this article you will learn how you can add records to your tables using the `INSERT` statement in SQL.

Keep in mind that if the syntax presented here doesn't work, you can check in the documentation for the implementation of SQL you are using. Most stuff works the same across the board, but there are some differences.

# SQL `INSERT` Statement Syntax

An `INSERT` statement specifies into which table you want to add a record. You write the command `INSERT INTO table_name`, then the keyword `VALUES` followed by the values you want to add in each column inside parenthesis and separated by commas, as below:

```sql
INSERT INTO table_name
VALUES (value1, value2, value3...);
```

The values will be added to the columns in the order in which the columns have been defined in the table. 

## How to Give a Value to the Selected Columns

Let's say that you instead want to give a value to only a few columns – for example if you want to avoid manually setting the `id` so it's done automatically. You would use the syntax below:

```sql
INSERT INTO table_name(column1, column2...)
VALUES (value1, value2...);
```

The values will be assigned to the columns in the order in which they are written in the parenthesis.

# SQL `INSERT` Statement Examples

Let's create a table, and then we will use `INSERT` to add the first few records to it.

The code below will create a table named `users` that has 5 columns. We'll have an `id` column that will be the `PRIMARY KEY` (the column that will always have unique values and allow us to uniquely identify a row), and then  the `name`, `age`, `state`, and `email` columns.

```sql
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  age INTEGER, state TEXT, email TEXT);
```

Let's add the first record to this table using the first syntax we looked at.

We will add the user `Paul` with an `id` of `1` , an `age` of `24`, from the `state` of `Michigan`, and with an email address of `paul@example.com` using the query below:

```sql
INSERT INTO users
VALUES (1, "Paul", 24, "Michigan", "paul@example.com");
```

This will make the table look like this:

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |

With this syntax you must have a value for each column or it will throw an error and not work.

Now let's add a couple other records, using the second kind of syntax seen above.

```sql
INSERT INTO users (name, state)
VALUES ("Molly", "New Jersey");

INSERT INTO users (name, state, age)
VALUES ("Robert", "New York", 19);
```

In this case the first value is assigned to the first mentioned column, so `"Molly"` is assigned to the `name` column, and `"New Jersey"` to the `state` column. Then for the other record, the column `name` is given the value of `"Robert"`, the column `state` gets `"New York"`, the column `age` is assigned `19`.

What happens to the columns that have not been assigned a value? The column with a type of `INTEGER PRIMARY KEY AUTOINCREMENT` is updated automatically, making sure that each row has a unique value. When a value is not specified for other columns, they are assigned a value of `NULL`.

Now the table looks like the below. Note that the `id` column has been updated to have unique values in each row, even if we have not explicitly assigned a value to it. The other columns that have not been assigned a value have a value of `NULL`.

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | NULL | New Jersey | NULL |
| 3 | Robert | 19 | New York | NULL |

# Conclusion

When you first create a table in your database, it is empty. This article explains how to add records to a table, which is a good place to start to create a database.

