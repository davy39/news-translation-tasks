---
title: SQL Count – How to Select, Sum, and Average Rows in SQL
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-29T20:04:04.000Z'
originalURL: https://freecodecamp.org/news/sql-count-how-to-select-sum-and-average-rows-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/safar-safarov-koOdUvfGr4c-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "In SQL, there are two built-in functions to sum or average the data in\
  \ your table. \nIn this article I will show you how to use the SUM and AVG functions\
  \ in SQL using code examples. \nHow to use the SUM function in SQL\nIf you need\
  \ to add a group of num..."
---

In SQL, there are two built-in functions to sum or average the data in your table. 

In this article I will show you how to use the **`SUM`** and **`AVG`** functions in SQL using code examples. 

## How to use the SUM function in SQL

If you need to add a group of numbers in your table you can use the `SUM` function in SQL. 

This is the basic syntax:

```sql
SELECT SUM(column_name) FROM table_name;
```

The `SELECT` statement in SQL tells the computer to get data from the table.

The `FROM` clause in SQL specifies which table we want to list.

In this example, we have a table called `students` with the columns of `id`, `name`, `date`, and `total`. We want to add up the total number of candy bars sold by all of the students. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.42.26-AM.png)

We can use this syntax to get the total number of candy bars sold:

```sql
SELECT SUM(total) FROM students;

```

The result would be 41.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.44.54-AM.png)

We can also get the sum for each student using the `GROUP BY` clause. 

The first part is to select the name and sum for the total number of candy bars sold, like this:

```sql
SELECT name, SUM(total)
```

The second part is to group the sum by name:

```sql
FROM students GROUP BY name;
```

Here is the complete code to group the total number of candy bars sold by student name. 

```sql
SELECT name, SUM(total) FROM students GROUP BY name;

```

This is what the result would look like in our table:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.54.14-AM.png)

Right now the results are grouped alphabetically by student name. 

We can modify the code to sort the list of results from largest total to smallest using the `ORDER BY` clause. 

```sql
SELECT name, SUM(total) FROM students GROUP BY name ORDER BY total DESC;
```

The `DESC` keyword tells the computer to sort from largest to smallest total. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-6.05.02-AM.png)

If we wanted to sort the total from smallest to largest, then we would omit the `DESC` keyword.

```sql
SELECT name, SUM(total) FROM students GROUP BY name ORDER BY total;

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-6.07.10-AM.png)

## How to use the AVG function in SQL

The `AVG` function finds the arithmetic mean for a group of records in a SQL table. An average, or arithmetic mean, is the sum of a group of numbers divided by the count for that group. 

For example, 2+4+4+6+6+8 is 30 divided 6 which results in an average of 5. 

This is the basic syntax for the `AVG` function:

```sql
SELECT AVG(column_name) FROM table_name;
   
```

In this example, we have a table called `students`, with columns of `id` , `name`, `date`, and `scores`.  We want to find the average of all the students' test scores in our table.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-4.10.47-AM.png)

We have to use this syntax to get the average for the test scores:

```sql
SELECT AVG(scores) FROM students; 
```

The average would be 85.333. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-4.21.21-AM.png)

We can also use the `ROUND` function to round our result to the nearest integer. 

```sql
SELECT ROUND(AVG(scores)) FROM students; 
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-4.32.05-AM.png)

We can also get the average for each student using the `GROUP BY` clause. 

The first part is to select the name and average for the scores, like this:

```sql
SELECT name, ROUND(AVG(scores))
```

The second part is to group the average scores by name:

```sql
FROM students GROUP BY name;
```

This is what the code looks like all together:

```sql
SELECT name, ROUND(AVG(scores)) FROM students GROUP BY name;
```

This is what the result looks like in the table:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.17.28-AM.png)

## Conclusion

There may be times were you need to find the sum or average of records in your table.

If you need to add a group of numbers in your table you can use the `SUM` function in SQL.

This is the basic syntax:

```sql
SELECT SUM(column_name) FROM table_name;
```

If you need to arrange the data into groups, then you can use the `GROUP BY` clause.

The `AVG` function finds the arithmetic mean for a group of records in a SQL table. An average, or arithmetic mean, is the sum of a group of numbers divided by the count for that group.

This is the basic syntax.

```sql
SELECT AVG(column_name) FROM table_name;

```

I hope you enjoyed this tutorial and best of luck on your SQL journey. 

  


 


