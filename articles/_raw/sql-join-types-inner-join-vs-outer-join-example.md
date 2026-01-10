---
title: SQL Join Types – Inner Join VS Outer Join Example
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-24T00:08:46.000Z'
originalURL: https://freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-269399.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "In a relational database, all information should only be present once.\
  \ But you might have information that's separated into different tables that's related\
  \ to each other. \nAnd you might want to put this related information together to\
  \ analyse its dat..."
---

In a relational database, all information should only be present once. But you might have information that's separated into different tables that's related to each other. 

And you might want to put this related information together to analyse its data – that is, you might want to join all the data (or some of it) together. In this case, you'll need to use SQL's `JOIN` statement. Let's learn how it works.

## What is a JOIN in SQL?

The JOIN operator lets you combine related information in various ways, as I explained briefly above. There are various types of joins, divided into two main categories – INNER joins and OUTER joins.

The biggest difference between an INNER JOIN and an OUTER JOIN is that the inner join will keep only the information from both tables that's related to each other (in the resulting table). An Outer Join, on the other hand, will also keep information that is not related to the other table in the resulting table.

Let's see how INNER JOINs and OUTER JOINs work in detail to understand them better.

## How to Use an INNER JOIN in SQL

The inner join will keep only the information from the two joined tables that is related. If you imagine the two tables as a [Venn diagram](https://en.wikipedia.org/wiki/Venn_diagram), the table resulting from an INNER JOIN will be the green highlighted part below where they overlap:

![Two circles, one labelled table 1 and one labelled table 2, with a section in common. The section in common is colored in green.](https://www.freecodecamp.org/news/content/images/2021/08/i-1.PNG)
_Venn diagram representation for Inner Join_

Here's the syntax for an inner join:

```sql
SELECT * FROM table1
    JOIN table2
    ON relation;
```

We'll see how this works below with an example.

## How to Use an OUTER JOIN in SQL

If you want to keep all the data, and not just the data related to each other, you can use an OUTER join. 

There are three types of Outer Join: `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`. The differences between them involve which unrelated data they keep – it can be from the first table, from the second, or from both of them. The cells without data to fill will have a value of `NULL`.

Note: `LEFT JOIN` is the mostly universally implemented in all versions of SQL. But this is not the case for `RIGHT JOIN` and `FULL JOIN`, which are not implemented in various SQL versions.

Let's see how each one works individually. Then we'll see how they all work with examples below.

### LEFT OUTER JOIN in SQL

The LEFT OUTER JOIN, or simply Left Join, will keep the unrelated data from the left (the first) table.

You can imagine it with a Venn diagram with two circles, with the resulting table being the green highlighted part which includes both the common/overlapping part, and the rest of the left circle.

![Two circles with a superimposed part. The left circle is labelled as table 1, the right circle is tabelled as table 2. The superimposed part and the rest of the table 1 cirlcle are colored in green.](https://www.freecodecamp.org/news/content/images/2021/08/t1-1.PNG)
_Venn diagram representation for Left Outer Join_

The syntax looks like the below. You'll see that it is similar to the Inner Join syntax, but with the `LEFT` keyword added.

```sql
SELECT columns
  FROM table1
  LEFT JOIN table2
  ON relation;
```

### RIGHT OUTER JOIN in SQL

The RIGHT OUTER JOIN, or simply Right Join, will keep the data in the second table that's not related to the first table.

You can imagine it with a Venn diagram with two circles, with the resulting table being the green highlighted part which includes both the overlapping part, and the rest of the right circle.

![Two circles with a superimposed part. The left circle is labelled as table 1, the right circle is tabelled as table 2. The superimposed part and the rest of the table 2 cirlcle are colored in green.](https://www.freecodecamp.org/news/content/images/2021/08/t2-1.PNG)
_Venn diagram representation for Right Outer Join_

The syntax is as below, the only difference is the `RIGHT` keyword.

```sql
SELECT columns
  FROM table1
  RIGHT JOIN table2
  ON relation;
```

### FULL OUTER JOIN in SQL

You can think of the FULL OUTER JOIN as the combination of a Left Join and Right Join. It will keep all rows from both tables, and the missing data will be filled in with `NULL`.

You can imagine it with a Venn diagram with two circles, with the resulting table being the green highlighted part which includes everything: the overlapping part, the left circle, and the right circle.

![Two circles with a superimposed part. The left circle is labelled as table 1, the right circle is tabelled as table 2. Everything is colored in green.](https://www.freecodecamp.org/news/content/images/2021/08/t1t2-1.PNG)
_Venn diagram representation for Full Outer Join_

The syntax is as below, using the `FULL` keyword.

```sql
SELECT columns
  FROM table1
  FULL JOIN table2
  ON relation;
```

## Examples of SQL JOIN operator

A possible database for a vet clinic could have one table for pets and one for the owners. Since an owner could have multiple pets, the pets table will have an `owner_id` column that points to the owners table.

| id  | name   | age | owner_id |
| --- | ---    | --- | ---      |
| 1   | Fido   | 7   | 1        | 
| 2   | Missy  | 3   | 1        |
| 3   | Sissy  | 10  | 2        |
| 4   | Copper | 1   | 3        |
| 5   | Hopper | 2   | 0        |

| id | name | phone_number |
| --- | --- | --- |
| 1 | Johnny | 4567823 |
| 2 | Olly | 7486513 |
| 3 | Ilenia | 3481365 |
| 4 | Luise | 1685364 |

You could use simple query to get a table with the pet name and the owner name next to each other. Let's do it with all the different JOIN operators.

### SQL INNER JOIN example

Let's do it first using `JOIN`.

In this case you would `SELECT` the column `name` from the `pets` table (and rename it `pet_name`). Then you would select the `name` column from the `owners` table, and rename it `owner`. That would look like this: `SELECT pets.name AS pet_name, owners.name AS owner`.

You would use `FROM` to say that the columns are from the `pets` table, and `JOIN` to say that you want to join it with the `owners` table, using this syntax: `FROM pets JOIN owner`.

And finally you would say that you want to join two rows together when the `owner_id` column in the `pets` table is equal to the `id` column in the `owner` table with `ON pets.owner_id = owners.id`.

Here it is all together:

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  JOIN owners
  ON pets.owner_id = owners.id;
```

You would get a table as below, where only the pets connected to an owner and the owners connected to a pet are included.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |

### SQL LEFT JOIN example

Let's do the same query using `LEFT JOIN` so you can see the difference. The query is the same other than adding the `LEFT` keyword.

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  LEFT JOIN owners
  ON pets.owner_id = owners.id;
```

In this case the rows from the left table, `pets`, are all kept, and when there is data missing coming from the `owners` table, it is filled with `NULL`.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |
| Hopper | NULL |

It seems there is a pet that is not registered with an owner.

### SQL RIGHT JOIN example

If you do the same query using `RIGHT JOIN` you would get yet a different result.

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  RIGHT JOIN owners
  ON pets.owner_id = owners.id;
```

In this case all the rows from the right table, `owners`, are kept, and if there is a missing value, it is filled with `NULL`.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |
| NULL | Louise |

It seems there is an owner that does not have a pet registered.

### SQL FULL JOIN example

You could do the same query again, using `FULL JOIN`.

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  FULL JOIN owners
  ON pets.owner_id = owners.id;
```

The resulting table is again different – in this instance all rows from the two tables are kept.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |
| Hopper | NULL |
| NULL | Louise |

It seems that there is a pet without an owner and an owner without a pet in our database.

# Conclusion

In a relational database, all data should be written only once. To then analyse this data you need something to join the related data together. 

In this article, you have learned how to use the JOIN operator to do so. I hope it will be useful for you, have fun!

