---
title: SQL LIKE Statement – How to Query SQL with Wildcard
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-22T15:01:50.000Z'
originalURL: https://freecodecamp.org/news/sql-like-statement-how-to-query-sql-with-wildcard
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/firos-nv-1wBmbnvv4TE-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "You can use the % and _ wildcards with the SQL LIKE statement to compare\
  \ values from an SQL table. But how does that work exactly? \nIn this article, I\
  \ will show you how to use the SQL LIKE statement through code examples. \nBasic\
  \ syntax of SQL LIKE st..."
---

You can use the `%` and `_` wildcards with the SQL LIKE statement to compare values from an SQL table. But how does that work exactly? 

In this article, I will show you how to use the SQL LIKE statement through code examples. 

## Basic syntax of SQL LIKE statement

Here is the basic syntax for the SQL Like statement:

```sql
SELECT FROM table_name
WHERE column LIKE 'string pattern'
```

[In SQL](https://dev.mysql.com/doc/mysql-tutorial-excerpt/5.7/en/pattern-matching.html), 

> pattern matching enables you to use `_` to match any single character and `%` to match an arbitrary number of characters (including zero characters)

For example, if we wanted to find all names in the table that started with the letter "T" then we could use this syntax:

```sql
WHERE name LIKE 'T%'
```

Or if we wanted to find all names in the table that contained the letters "on", then we could use this syntax:

```sql
WHERE name LIKE '%on%'
```

We can use the `_` wildcard to find a single character match. For example, this is the syntax to find all numbers in the `quantity` category that are 2 digits long and end with '9':

```sql
WHERE quantity LIKE '_9';

```

To better understand how these wildcards work with the SQL Like statement, let's take a look at an example table of data.

## How to use the SQL LIKE statement – example with a cars table

In this example, we have a `cars` table with the columns of `id`, `model`, `make` and `price`.

```sql
id|make|model|price
1|Honda|Civic|21000
2|Ford|Fusion|23000
3|Toyota|Camry|24000
4|Dodge|Challenger|29000
5|Tesla|Model X|104000
6|Chevrolet|Tahoe|49000
```

### How to use the `%` Wildcard with the SQL LIKE statement 

In this first example, we want to find all car models that start with the letter "C".

```sql
SELECT * FROM cars
WHERE model LIKE 'C%';
```

This code would return the following results from the `cars` table:

```sql
id|make|model|price
1|Honda|Civic|21000
3|Toyota|Camry|24000
4|Dodge|Challenger|29000
```

We can see that 3 out of the 6 entries from our `cars` table have model names that start with the letter "C".

The SQL LIKE statement is not case sensitive which means `'C%'` and `'c%'` would return identical results.

We can also use the  `%` wildcard and SQL LIKE statement to find entries that end with a character or characters. 

In this example, we want to find all of the car makers whose name ends with an "a".

```sql
SELECT * FROM cars
WHERE make LIKE '%a';
```

This code would return the following results from the `cars` table:

```sql
id|make|model|price
1|Honda|Civic|21000
3|Toyota|Camry|24000
5|Tesla|Model X|104000
```

We can see that 3 out of the 6 car makers have a name that ends with the letter "a".

### How to use multiple `%` Wildcards with the SQL LIKE statement 

In this example, we want to find all car prices that include the number 9 in them.

```sql
SELECT * FROM cars
WHERE price LIKE '%9%';
```

This code would return the following results from the `cars` table:

```sql
id|make|model|price
4|Dodge|Challenger|29000
6|Chevrolet|Tahoe|49000
```

We can see that 2 out of the 6 car prices include the number 9. 

### How to use the `_` Wildcard with the SQL LIKE statement 

We can use the `_` wildcard to find a single character match.

Let's modify our `cars` table:

```sql
id|make|model|price
30|Honda|Civic|21000
35|Ford|Fusion|23000
40|Toyota|Camry|24000
45|Dodge|Challenger|29000
50|Tesla|Model X|104000
55|Chevrolet|Tahoe|49000
```

In this example, we want to find all ids that are two digits long and end in the number 0.

```sql
SELECT * FROM cars
WHERE id LIKE '_0';
```

This code would return the following results from the `cars` table:

```sql
id|make|model|price
30|Honda|Civic|21000
40|Toyota|Camry|24000
50|Tesla|Model X|104000
```

We can see that 3 out of the 6 two-digit car ids end in the number 0. 

### How to use multiple `_` Wildcards with the SQL LIKE statement 

Let's modify our `cars` table again.

```sql
id|make|model|price
130|Honda|Civic|21000
135|Ford|Fusion|23000
140|Toyota|Camry|24000
145|Dodge|Challenger|29000
150|Tesla|Model X|104000
155|Chevrolet|Tahoe|49000
```

In this example, we want to find all ids that are three digits long and end in the number 0.

```sql
SELECT * FROM cars
WHERE id LIKE '__0';
```

This code would return the following results from the `cars` table:

```sql
id|make|model|price
130|Honda|Civic|21000
140|Toyota|Camry|24000
150|Tesla|Model X|104000
```

We had to use two underscores `_` with the SQL LIKE statement to find all ids that are three digits long and end in the number 0.

```sql
Using two underscores
'__0'

instead of just one 
'_0'
```

### How to use the NOT Operator with the SQL LIKE statement 

We can use the NOT operator in SQL to find all results that do not match the string pattern in the LIKE statement.

We can modify our last example to find all three digit ids that do not end in the number 0.

```sql
SELECT * FROM cars
WHERE id NOT LIKE '__0';
```

This code would return the following results from the `cars` table:

```sql
id|make|model|price
135|Ford|Fusion|23000
145|Dodge|Challenger|29000
155|Chevrolet|Tahoe|49000
```

### How to use the `%` and `_` Wildcards with the SQL LIKE statement 

In this example, we want to find all car makers whose second letter is an "o" and the name ends with an "a".

```sql
SELECT * FROM cars
WHERE make LIKE '_o%a';
```

The `_o` is to find all car makers whose second letter is  "o". The `%a` is to find all car makers that end with the letter "a".

This code would return the following results from the `cars` table:

```sql
id|make|model|price
130|Honda|Civic|21000
140|Toyota|Camry|24000
```

## Conclusion

You can use the `%` and `_` wildcards with the SQL LIKE statement to compare values from a SQL table. 

Here is the basic syntax for the SQL Like statement.

```sql
SELECT FROM table_name
WHERE column LIKE 'string pattern'
```

The `%` matches zero, one or more characters while the `_` matches a single character. 

In this article, we learned how to use both of these wildcards with the SQL LIKE statement using the `cars` table example. 

I hoped you enjoyed this article and best of luck on your SQL journey. 

  

