---
title: Ascending Order with SQL Order By
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-20T14:29:04.000Z'
originalURL: https://freecodecamp.org/news/ascending-order-with-sql-order-by
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/brett-jordan-M3cxjDNiLlQ-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "In this article, I will show you a few code examples on how you can sort\
  \ your data in ascending order using the ORDER BY clause in SQL. \nORDER BY syntax\n\
  This is the basic syntax to sort your data in ascending order:\nSELECT columns FROM\
  \ table\nORDER BY..."
---

In this article, I will show you a few code examples on how you can sort your data in ascending order using the `ORDER BY` clause in SQL. 

## ORDER BY syntax

This is the basic syntax to sort your data in ascending order:

```sql
SELECT columns FROM table
ORDER BY column;
```

If you want to sort by descending order, then you have to use the `DESC` keyword.

```sql
SELECT columns FROM table
ORDER BY column DESC;
```

The `SELECT` statement in SQL tells the computer to get data from the table. 

The `FROM` clause in SQL specifies which table we want to list. 

In this example, we have a table of musicians with the columns of `id`, `name`, `age`, `instrument` and `city`:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-2.57.23-AM.png)

Right now, this table is sorted automatically by `id` in ascending order. 

If we wanted to sort the `name` column in ascending order, then we would have to use this syntax: 

```sql
SELECT * FROM musicians
ORDER BY name;
```

The `*` character tells the computer to select all of the columns in the table. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.03.11-AM.png)

You can see that the `names` are now sorted alphabetically and the `id`'s are no longer in the correct ascending order. 

If we wanted to sort the data by `city`, then we can use this syntax.

```sql
SELECT * FROM musicians
ORDER BY city;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.22.34-AM.png)

You can also sort multiple columns in ascending order in the same command.

In this new musician example, we can sort the `age` and `city` columns in ascending order. 

```sql
SELECT * FROM musicians
ORDER BY age, city;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.13.46-AM.png)

We can see there are three 19 year old musicians with their respective cities alphabetically sorted in the table. We can also see the two 38 year old musicians with their cities properly sorted in alphabetical order. 

If we wanted to sort some of the data in ascending order and other data in descending order, then we would have to use the `ASC` and `DESC` keywords. 

In this new musician example, we want to sort the `age` column in descending order and the `instrument` column in ascending order. 

Here is the syntax:

```sql
SELECT * FROM musicians
ORDER BY age DESC, instrument ASC;
```

We have to use both the `ASC` and `DESC` keywords next to the column names to tell the computer how to sort the data. 

The result would look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.33.26-AM.png)

We can see in our table that both Oscar and Jenny are the oldest. But Oscar is the top result because drums comes before trombone alphabetically. 

We see the same situation with Jess and Dave. Even though they are the same age, Jess is higher in the table because flute comes before trumpet alphabetically. 

## Conclusion

You can sort your table data in ascending order using the `ORDER BY` clause in SQL.

```sql
SELECT columns FROM table
ORDER BY column;
```

If you want to sort by descending order then you also have to use the `DESC` keyword.

```sql
SELECT columns FROM table
ORDER BY column DESC;
```

The `*` character tells the computer to select all of the columns in the table. 

```sql
SELECT * FROM table
ORDER BY column;
```

If you want to sort multiple columns in ascending order then you would list the columns you want to sort next to the `ORDER BY` clause.

```sql
SELECT * FROM table
ORDER BY column1, column2;
```

If you want to sort some of the data in ascending order and other data in descending order, then you would have to use the `ASC` and `DESC` keywords. 

```sql
SELECT * FROM table
ORDER BY column1 ASC, column2 DESC;
```

That is how to use the `ORDER BY` clause in SQL to sort data in ascending order. 

