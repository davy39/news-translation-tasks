---
title: SQL Distinct Statement – How to Query, Select, and Count
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-30T16:24:19.000Z'
originalURL: https://freecodecamp.org/news/sql-distinct-statement-how-to-query-select-and-count
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/anthony-riera-kylWNDQFd5A-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "In SQL, you can make a database query and use the COUNT function to get\
  \ the number of rows for a particular group in the table. \nIn this article, I will\
  \ show you how to use the COUNT function with a few code examples. \nWhat is the\
  \ COUNT function in S..."
---

In SQL, you can make a database query and use the `COUNT` function to get the number of rows for a particular group in the table. 

In this article, I will show you how to use the `COUNT` function with a few code examples. 

## What is the COUNT function in SQL?

This SQL function will return the count for the number of rows for a given group.

Here is the basic syntax:

```sql
SELECT COUNT(column_name) FROM table_name;
```

The `SELECT` statement in SQL tells the computer to get data from the table.  

`COUNT(column_name)` will not include `NULL` values as part of the count. 

A `NULL` value in SQL is referring to values that are not present in the table. 

Sometimes you can use an `*` inside the parenthesis for the `COUNT` function.

```sql
SELECT COUNT(*) FROM table_name;
```

The `COUNT(*)` function will return the total number of items in that group including `NULL` values. 

The `FROM` clause in SQL specifies which table we want to list.

You can also use the `ALL` keyword in the `COUNT` function. 

```sql
SELECT COUNT(ALL column_name) FROM table_name;
```

The `ALL` keyword will count all values in the table including duplicates. You can omit this keyword because the `COUNT` function uses the `ALL` keyword as the default whether you write it or not. 

Sometimes you will see the `DISTINCT` keyword used with the `COUNT` function.

```sql
SELECT COUNT(DISTINCT column_name) FROM table_name;
```

The `DISTINCT` keyword will only count unique values that are `NOT NULL`. The computer will ignore any duplicate values. 

## How to use the COUNT function in SQL

In this example, we have a table for young campers with the columns of `id`, `name`, `age` and `counselor`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.35.37-AM.png)

If we want to select all of the rows in our table, then we can use the following syntax:

```sql
SELECT COUNT(*) FROM campers;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.37.18-AM.png)

As you can see, the query returned the number 12 which represents the total number of rows in our `campers` table. 

### Using the `WHERE` clause

We can use the `WHERE` clause to specify the number of rows for the name of a particular camp counselor. 

In this example, we want to count the number of rows for the camp counselor by the name of Ashley. 

In the `WHERE` clause, we need to specify `counselor` with a value of `"Ashley"`.

```sql
 WHERE counselor="Ashley";
```

This is the complete code:

```sql
SELECT COUNT(*) FROM campers WHERE counselor="Ashley";
```

This is what the result would return:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.47.03-AM.png)

If we take a look at our table from earlier, we can see that `"Ashley"` only appears 4 times. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.35.37-AM.png)

We can modify our result to count how many rows there are for campers that are 11 years old.

In the `WHERE` clause, we need to specify `age` with a value of `11`.

```sql
WHERE age=11;
```

This is the complete code:

```sql
SELECT COUNT(*) FROM campers WHERE age=11;
```

This is what the result would return:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.50.46-AM.png)

If we take a look at our table from earlier, we can see that there are only three 11 year old campers.

### How to use the `GROUP BY` clause

We can use the `GROUP BY` clause and `COUNT` function to see the number of 11, 12, and 13 year old campers in our table.

We first have to select the `age` column and use the `COUNT` function:

```sql
SELECT age, COUNT(*)
```

We then have to specify the `campers` table and group the results by `age`:

```sql
FROM campers GROUP BY age;
```

This is what the code looks like all together:

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age;
```

This is what the results look like:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.23.35-AM.png)

### How to use the `ORDER BY` clause

We can modify our example for the list of ages and use the `ORDER BY` clause to list the results from smallest to largest.

This is the code for the `ORDER BY` clause:

```sql
ORDER BY COUNT(*);
```

We add that clause at the end of the `SELECT` statement like this:

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age ORDER BY COUNT(*);
```

This is what the modified example looks like:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.28.18-AM.png)

If we wanted the count results to be sorted from largest to smallest, then we can use the `DESC` keyword.

This is the code for the `ORDER BY` clause using the `DESC` keyword:

```sql
ORDER BY COUNT(*) DESC;
```

This is the complete code:

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age ORDER BY COUNT(*) DESC;
```

This is what the new result would look like:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.31.52-AM.png)

### How to use the `HAVING` clause

We can use the `HAVING` clause to specify a condition for the `COUNT` function. 

We can modify the code to only show results for ages where the count is less than 5. 

This is what the code looks like for the `HAVING` clause:

```sql
HAVING COUNT(*)<5;

```

This is what the complete code looks like:

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age HAVING COUNT(*)<5;

```

This is what the modified results look like:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.48.28-AM.png)

We can see that the 12 year olds were removed from this result because the count was larger than 5. 

## Conclusion

In SQL, you can make a database query and use the `COUNT` function to get the number of rows for a particular group in the table. 

Here is the basic syntax:

```sql
SELECT COUNT(column_name) FROM table_name;
```

`COUNT(column_name)` will not include `NULL` values as part of the count.

A `NULL` value in SQL refers to values that are not present in the table.

Sometimes you can use an `*` inside the parenthesis for the `COUNT` function.

```sql
SELECT COUNT(*) FROM table_name;
```

The `COUNT(*)` function will return the total number of items in that group including `NULL` values.

I hope you enjoyed this article and best of luck on your SQL journey.

