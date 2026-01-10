---
title: How to Delete a Row in SQL – Example Query
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-23T17:56:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-a-row-in-sql-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/ujesh-krishnan-7ySd00IGyx4-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "In SQL, you can delete a row in a table by using the DELETE query and the\
  \ WHERE clause. \nIn the article, I will walk you through how to use the DELETE\
  \ query and WHERE clause to delete rows. I will also show you how to delete multiple\
  \ rows from a tabl..."
---

In SQL, you can delete a row in a table by using the `DELETE` query and the `WHERE` clause. 

In the article, I will walk you through how to use the `DELETE` query and `WHERE` clause to delete rows. I will also show you how to delete multiple rows from a table at once. 

## How to use the DELETE query in SQL

This is the basic syntax for using the the `DELETE` query:

```sql
DELETE FROM table_name
WHERE condition of which row(s) to delete;
```

In this example, we have a table called `cats` that currently has ten rows in it. The columns would be `id`, `name` and `gender`. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.28.51-AM.png)

We want to delete the row with the `id` of  8 which is Loki's row. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.30.10-AM.png)

The first line of the `DELETE` query would look like this:

```sql
DELETE FROM cats
```

In the second line, we are going to specify which row by using the `id=8` after the `WHERE` clause.

```sql
WHERE id=8;
```

Here is the complete syntax to delete Loki's row: 

```sql
DELETE FROM cats
WHERE id=8;
```

This is what the new `cats` table looks like:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.31.22-AM.png)

We can see that our `DELETE` query worked because Loki's information is no longer there. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.31.40-AM.png)

## How to Delete multiple rows from a table in SQL

One way we can delete multiple rows from our `cats` table is to change the condition from `id` to `gender`.

If we wanted to delete the rows with just the male cats, then we can use the `gender="M"` condition.

```sql
DELETE FROM cats
WHERE gender="M";
```

Our new `cats` table would look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.32.55-AM.png)

Now the `cats` table is only showing the female cats. 

## How to delete multiple rows using the BETWEEN operator with the AND operator in SQL

If we wanted to delete a number of rows within a range, we can use the `AND` operator with the `BETWEEN` operator. 

In this example, we want to delete rows with `id`s of 4-7 inclusive. 

Here is the syntax for that:

```sql
DELETE FROM cats
WHERE id BETWEEN 4 AND 7;
```

This is the result from that `DELETE` query:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.41.48-AM.png)

We can see that  rows 1-3 and 8-10 are left in our table. The `id`s of 4-7 have been successfully deleted. 

## How to delete multiple rows using the IN operator in SQL

We can specify which names to delete from the `cats` table using the `IN` operator.

In this example, I want to delete the names of Lucy, Stella, Max and Tiger from our original `cats` table here:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.48.48-AM.png)

We need to specify the column and use the `IN` operator to list the names we want deleted. 

```sql
DELETE FROM cats
WHERE name IN ("Lucy","Stella","Max","Tiger");
```

This is what the new result would look like:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.55.29-AM.png)

Our `DELETE` query was successful, because those four cats are no longer present in the table. 

## How to delete all records in the table in SQL

If you want to delete all of the information from your table, then you would use this syntax:

```sql
DELETE FROM table_name;
```

In order to delete all of the cats from our `cats` table, then we would use this code. 

```sql
DELETE FROM cats;
```

## Conclusion

In this article, we learned about the different ways to delete information from a SQL table. 

This is the basic syntax for using the `DELETE` query:

```sql
DELETE FROM table_name
WHERE condition of which row(s) to delete;
```

If you want to delete one row from the table, then you have to specify a condition. 

```sql
WHERE id=8;
```

There are a few ways to delete multiple rows in a table. 

If you wanted to delete a number of rows within a range, you can use the `AND` operator with the `BETWEEN` operator.

```sql
DELETE FROM table_name
WHERE column_name BETWEEN value 1 AND value 2;
```

Another way to delete multiple rows is to use the `IN` operator.

```sql
DELETE FROM table_name
WHERE column_name IN (value 1, value 2, value 3, etc...);
```

If you want to delete all records from the table then you can use this syntax.

```sql
DELETE FROM table_name;
```

I hope you enjoyed this article and best of luck on your SQL journey. 

