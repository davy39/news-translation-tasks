---
title: Insert Into SQL – How to Insert Into a Table Query [Example Statement]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-10-06T16:10:50.000Z'
originalURL: https://freecodecamp.org/news/insert-into-sql-how-to-insert-into-a-table-query-example-statement
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/caspar-camille-rubin-fPkvU7RDmCo-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "If you want to add data to your SQL table, then you can use the INSERT\
  \ statement. \nIn this article, I will show you how to use the INSERT statement\
  \ to add a single row, multiple rows, and to copy rows from one SQL table to another.\n\
  Basic INSERT synta..."
---

If you want to add data to your SQL table, then you can use the `INSERT` statement. 

In this article, I will show you how to use the `INSERT` statement to add a single row, multiple rows, and to copy rows from one SQL table to another.

## Basic INSERT syntax

Here is the basic syntax for adding rows to a table in SQL: 

```sql
INSERT INTO table_name (column1, column2, column3,etc)
VALUES (value1, value2, value3, etc);
```

The first line of code uses the `INSERT` statement followed by the name of the table you want to add the data to. After the table name, you should specify the column names. 

The second line of code is where you will add the values for the rows. It is important that the number of values matches with the number of columns specified or else you will get an error message. 

## How to add a row to a SQL table

In this example we have a table called `dogs` with the columns of `id`, `name` and `gender`.  We want to add one dog called `AXEL`. 

This is what the code looks like to add `AXEL` to the table:

```sql
INSERT INTO dogs(id, name, gender) VALUES (1, 'AXEL', 'M');

```

This is what the table looks like.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.19.41-AM.png)

## What happens if the number of values does not match the columns?

As mentioned earlier, the number of columns has to match with the number of values. 

If I alter the code to remove a value, then I would get an error message. 

```sql
INSERT INTO dogs(id, name, gender) VALUES (1, 'AXEL');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.22.25-AM.png)

Since we specified 3 columns, we need to provide three values for each row added to the table. 

## What happens if you ignore column constraints? 

When you create SQL tables, you will add column constraints which serve as rules for the column. 

In our `dogs` table, the `name` and `gender` columns have a constraint of `NOT NULL`. This rule means that a value cannot be absent from the row. 

When I try to add `NULL` for the `gender`, I come back with an error message. 

```sql
INSERT INTO dogs(id, name, gender) VALUES (1, 'AXEL', NULL);

```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.46.44-AM.png)

Any constraints that you specified in the creation of your SQL table need to be respected when adding rows. 

## How to add multiple rows to a table in SQL

If you want to add multiple rows to a table all at once, then you can use this syntax:

```sql
INSERT INTO table_name (column1, column2, column3,etc)
VALUES 
	(value1, value2, value3, etc),
    (value1, value2, value3, etc),
    (value1, value2, value3, etc);
	
```

It is important to remember the commas between each of the rows or else you will get an error message.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-5.58.22-AM.png)

This is what the code would look like to add eight dogs to the table all at once:

```sql
INSERT INTO dogs(id, name, gender) 
VALUES 
    (1, 'AXEL', 'M'),
    (2, 'Annie', 'F'),
    (3, 'Ace', 'M'),
    (4, 'Zelda', 'F'),
    (5, 'Diesel', 'M'),
    (6, 'Tilly', 'F'),
    (7, 'Leroy', 'M'),
    (8, 'Olivia', 'F');
```

This is what the table looks like now:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-6.00.14-AM.png)

## How to copy rows from one table and insert them into another table

You can use the `SELECT` and `INSERT` statements to copy rows from one SQL table to another.

This is the basic syntax:

```sql
INSERT INTO table_name1 (columns) 
SELECT columns FROM table_name2;
```

In this example, I have created a `cats` table with three rows in it with the same column names as the `dogs` table. 

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-6.26.46-AM.png)

We can add all of the `cats` data into the `dogs` table using the following code:

```sql
INSERT INTO dogs SELECT * FROM  cats;

```

This is what the new `dogs` table looks like with the additional `cats`:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-06-at-6.27.43-AM.png)

## Conclusion

If you want to add data to your SQL table, then you can use the `INSERT` statement. 

Here is the basic syntax for adding rows to your SQL table:

```sql
INSERT INTO table_name (column1, column2, column3,etc)
VALUES (value1, value2, value3, etc);
```

The second line of code is where you will add the values for the rows. It is important that the number of values matches with the number of columns specified or else you will get an error message.

When you try to ignore column constraints in adding rows to the table, then you will receive an error message. 

If you want to add multiple rows to a table all at once, then you can use this syntax:

```sql
INSERT INTO table_name (column1, column2, column3,etc)
VALUES 
	(value1, value2, value3, etc),
    (value1, value2, value3, etc),
    (value1, value2, value3, etc);
```

You can use the `SELECT` and `INSERT` statement to copy rows from one SQL table to another.

This is the basic syntax:

```sql
INSERT INTO table_name1 (columns) 
SELECT columns FROM table_name2;
```

I hope you enjoyed this article and best of luck on your SQL journey. 

