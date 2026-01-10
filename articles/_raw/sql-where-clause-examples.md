---
title: SQL Where – Clause Examples
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-04T15:32:26.000Z'
originalURL: https://freecodecamp.org/news/sql-where-clause-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-kindel-media-7054757.jpg
tags:
- name: crud
  slug: crud
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Sometimes when you''re working with SQL, you don''t need to operate on
  an entire range of records. Or it would be really bad if you accidentally changed
  or deleted everything.

  In these cases, you''ll need to select only the part of the records on which ...'
---

Sometimes when you're working with SQL, you don't need to operate on an entire range of records. Or it would be really bad if you accidentally changed or deleted everything.

In these cases, you'll need to select only the part of the records on which you want to work, those that satisfy a certain condition. This is where SQL's `WHERE` clause is useful.

# SQL `WHERE` Clause Syntax

You write the `WHERE` clause like this:

```sql
SELECT column1, column2...
FROM table_name
WHERE condition;
```

Note that here I've written it using the `SELECT` statement, but its use is not limited to `SELECT`. You can use it with other statements like `DELETE` and `UPDATE` as well.

# SQL `WHERE` Clause in Action

Let's use this `users` table as an example of how to use the `WHERE` clause.

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 3 | Anvil | 31 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 6 | Cody | 16 | Michigan | cody@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | Wisconsin | corbin@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

## Example of SQL `WHERE` Clause with the  `SELECT` Statement

When you want to make sure that a certain event will affect people that are 50 or above, you can select only those users with the following code:

```sql
SELECT *
FROM users
WHERE age >= 50;
```

This will give a table like below, that only lists the users who are 50 or above:

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

## Example of SQL `WHERE` Clause with the `DELETE` Statement

  
Let's say that Cody has decided to remove himself from this list. You can update the table using a `DELETE` statement along with `WHERE` to make sure only Cody's record is deleted.

```sql
DELETE FROM users
WHERE name IS "Cody";
```

The `users` table will now look like below, without line 6 (where Cody's info was):

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 3 | Anvil | 31 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | Wisconsin | corbin@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

## Example of SQL `WHERE` Clause with `UPDATE` Statement

Now perhaps you have received notice that Anvil has aged up and is now 32 years old. You can change Anvil's record using the `UPDATE` statement, and you can use `WHERE` to make sure that only Anvil's record gets updated.

```sql
UPDATE users
SET age = 32
WHERE name IS "Anvil";
```

Now the table will look like this:

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 3 | Anvil | 32 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | Wisconsin | corbin@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

# Operators You Can Use with a `WHERE` Clause to Select Records

You can use operators like `=`, `>`, `<`, `>=`, `<=`, `<>` (or `!=` depending on your SQL version), `BETWEEN`, `LIKE`, `IN`.

We have already seen `>=`, "greater than or equal to", in action in the examples above.

`=` is "equal to", `>` is "greater than", `<` is "smaller than", `<=` is "smaller than or equal to", `<>` (or `!=`) is "not equal to".

The four operators, _greater than_, _smaller than_, _greater than or equal to_, and _smaller than or equal to_ are useful mostly when dealing with numbers.

The two operators, _equal to_, and _not equal to_, are useful both with numbers and and other data types.

## How to Use the `BETWEEN` Operator in SQL

`BETWEEN` allows you to specify a range of numbers. For example `WHERE age BETWEEN 24 and 51` will select all records in that age range.

```sql
SELECT * FROM users
WHERE age BETWEEN 24 AND 51;
```

There are 7 users with an age in this range:

| id | name | age | state | email |
| ---- | ---- | ---- | ---- | ---- |
| 3 | Anvil | 32 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | WIsconsin | corbin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |

## How to Use the `LIKE` Operator in SQL

`LIKE` allows you to specify a pattern. For example `WHERE name LIKE "A%"` will select all records where the name starts with an A.

```sql
SELECT * FROM users
WHERE name LIKE "A%";
```

There are 5 users with a name that starts with A in our list:

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 3 | Anvil | 32 |South Dakota | anvil@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |

### How to make a pattern to use with `LIKE`

You can make a pattern using the characters `%` and `_`. The character `%` represents any number of characters (zero, one or more). The character `_` represents exactly one character.

For example `"_ook"` could be "book", "look", "nook". But `"%ook"` could be also "ook" or "phonebook".

## How to Use the `IN` Operator in SQL

`IN` lets you choose between a list of possibilities. For example let's see which users are on the East Coast.

```sql
SELECT * FROM users
WHERE state IN ("Maine", "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida");
```

The `IN` operator is checking if the value in the `state` column is equal to one of the values in the list of East Coast states.

Only six of the users live on the East Coast:

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 11 | Zachery | 21 | Massachusetts | zachery@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |

## Let's not forget about the `IS`, `NOT`, `AND`, `OR` Operators

We already used the `IS` operator in one of our examples above. Like `WHERE name IS "Cody"`, it checks if a column has that exact value.

You can use `NOT` in front of a condition to make it the opposite. For example `WHERE age NOT BETWEEN 24 AND 51` would select only users younger than 24 and older than 51. Using this criteria, 12 users are selected:

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

You use `AND` to combine conditions so that both have to be true, for example `WHERE name LIKE "A%" AND age > 70` would select users with a name starting with A **and** that are older than 70. Only 2 users satisfy this criteria:

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |

You can use `OR` to combine conditions so that only one of the two need to be true. For example `WHERE name LIKE "A%" OR age > 70` would select users with a name starting with A **or** that are older than 70 (only one of the two parts has to be true, but both can also be true). 

There are 6 users that have a name starting with A or are older than 70 years old (or both).

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 3 | Anvil | 32 |South Dakota | anvil@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |

# Conclusion

It's really important to specify on which records you want to operate in your tables. 

With this article you have learned how to do so using the `WHERE` clause.

Thank you for reading!

