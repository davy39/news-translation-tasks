---
title: Alter Table in SQL – How to Add a Column or Rename a Column in SQL
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-09T15:14:48.000Z'
originalURL: https://freecodecamp.org/news/alter-table-in-sql-how-to-add-a-column-or-rename-a-column-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-quang-nguyen-vinh-2138126.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'You have created your database and your tables, and after all this work,
  you notice that you need to add or rename a column. Well, you can use the ALTER
  TABLE statement to do so.

  Just keep in mind that you need to be really careful when you do this. ...'
---

You have created your database and your tables, and after all this work, you notice that you need to add or rename a column. Well, you can use the `ALTER TABLE` statement to do so.

Just keep in mind that you need to be really careful when you do this. If your table has a lot of rows it can cause performance issues for your database.

Note: If the syntax presented here doesn't work, check in the documentation for the implementation of SQL you are using. Most stuff works the same across the board, but there are some differences.

# How to Add a New Column with `ALTER TABLE`

To add a new column, you first need to select the table with `ALTER TABLE table_name`, and then write the name of the new column and its datatype with `ADD column_name datatype`. Put together, the code looks like this:

```sql
ALTER TABLE table_name
ADD column_name datatype;

```

## Example of using `ALTER TABLE` to add a new column

We have a database of users as below:

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | 22 | New Jersey | molly@example.com |
| 3 | Robert | 19 | New York | robert@example.com |

We have reached a point where we need to store the identity document number of our users, so we need to add a new column for that.

To add a new column to our `users` table, we need to select the table with `ALTER TABLE users` and then specify the name of the new column and its datatype with `ADD id_number TEXT`. All together, looks like this:

```sql
ALTER TABLE users
ADD id_number TEXT;
```

The table with a new column will look as below:

| id | name | age | state | email | id_number |
| -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL |
| 3 | Robert | 19 | New York | robert@example.com | NULL |

You will need to use [an `UPDATE` statement](https://www.freecodecamp.org/news/sql-update-statement-update-query-in-sql/) to add the missing info for the already existing users once it is provided.

### How to create a new column with a default value instead of NULL

You can also create a column with a default value using the `default` keyword followed by the value to use. Users will then see that default instead of having the missing values be filled in with NULL.

Let's say that we will have international users starting soon, and we want to add a `country` column. All our existing users are from the United States, so we can use that as the default value.

```sql
ALTER TABLE users
ADD country TEXT default "United States";
```

The table will then look like this:

| id | name | age | state | email | id_number | country |
| -- | -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL | United States |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL | United States |
| 3 | Robert | 19 | New York | robert@example.com | NULL | United States |

### Be Careful When Adding New Columns to Tables

If your table has already a lot of rows – like if you have already a lot of users, or a lot of stored data – adding a new column can be really resource intensive. So make sure to handle this an operation with care.

# How to Rename a Column with `ALTER TABLE`

You can rename a column with the below code. You select the table with `ALTER TABLE table_name` and then write which column to rename and what to rename it to with `RENAME COLUMN old_name TO new_name`.

```sql
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

## Example of how to rename a column

Let's look at the same table we used in the previous example:

| id | name | age | state | email | id_number | country |
| -- | -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL | United States |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL | United States |
| 3 | Robert | 19 | New York | robert@example.com | NULL | United States |

To avoid confusion between the `id` and the `id_number` columns, let's rename the first one as `user_id`. 

We will first select the table with `ALTER TABLE users` and then declare the column name so it changes to what we want to change it to with `RENAME COLUMN id TO user_id`.

```sql
ALTER TABLE users
RENAME COLUMN id TO user_id;
```

After using the query, the table will look like this:

| user_id | name | age | state | email | id_number | country |
| -- | -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL | United States |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL | United States |
| 3 | Robert | 19 | New York | robert@example.com | NULL | United States |

### Be careful when renaming a column in a table 

When you rename columns using `ALTER TABLE` you risk breaking database dependencies. 

If you use a database refactoring tool to change the name of a column instead of using `ALTER TABLE` it will manage all the dependencies and update them with the new column name. 

If you have a small database you may not need to worry, but it is important to keep in mind.

# Conclusion

In this article, you have learned how to use `ALTER TABLE` to add a column and rename a column in a table.

Just remember that both are operations that come with their own risks that are important to know. As someone said, _with great power come great responsibility –_ and `ALTER TABLE` is a great power, so use it carefully!

