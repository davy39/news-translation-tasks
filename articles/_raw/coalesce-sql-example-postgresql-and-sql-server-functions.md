---
title: Coalesce SQL – Example PostgreSQL and SQL Server Functions
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-13T18:14:20.000Z'
originalURL: https://freecodecamp.org/news/coalesce-sql-example-postgresql-and-sql-server-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/coalesce.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "In SQL, the COALESCE() function returns the first non-null value in an\
  \ entry. \nIt evaluates the values of the entries one by one, ignores the null values,\
  \ then returns the first value that is not null. It works in PostgreSQL, SQL server,\
  \ and MySQL.\nI..."
---

In SQL, the `COALESCE()` function returns the first non-null value in an entry. 

It evaluates the values of the entries one by one, ignores the null values, then returns the first value that is not null. It works in PostgreSQL, SQL server, and MySQL.

In this article, I will show you how to use the `COALESCE()` function to handle null values. But firstly, what is a null value? That’s what we are looking at next.

## What We'll Cover
- [What is a NULL Value?](#heading-what-is-a-null-value)
- [Syntax of the `COALESCE()` Function](#heading-syntax-of-the-coalesce-function)
- [How to Handle NULL Values with the `COALESCE()` Function in PostgreSQL](#heading-how-to-handle-null-values-with-the-coalesce-function-in-postgresql)
  - [Example of How to Handle NULL Values with the `COALESCE()` Function in PostgreSQL](#heading-example-of-how-to-handle-null-values-with-the-coalesce-function-in-postgresql) 

## What is a NULL Value?

Null means nothing. So when you see `NULL` in any SQL server, PostgreSQL, or MySQL, it means there’s no entry for that attribute.

A non-null value is the opposite of null value. Any integer, string, or other value apart from null is a non-null value.

## Syntax of the `COALESCE()` Function

The `COALESCE()` function accepts all common values including null. Here's the basic syntax:

```sql
COALSCE(value1, value2, value3, …)
```

After running, `COALESCE()` strips out all `NULL` values as long as there’s no error in your entries.

Here’s how it works:

```sql
SELECT COALESCE(NULL,  'freeCodeCamp', 'freeCodeCamp Blog', NULL);
```

![ss1-1](https://www.freecodecamp.org/news/content/images/2023/01/ss1-1.png) 

The `COALESCE()` function works perfectly for what it does. Even if the non-null value is the last entry and there are many NULL entries behind it, it still works:

```sql
SELECT COALESCE(NULL,  NULL, NULL, NULL, NULL, NULL, NULL, 'freeCodeCamp Blog', 12, 'JavaScript');
```

![ss2-1](https://www.freecodecamp.org/news/content/images/2023/01/ss2-1.png) 

And if there’s just one non-null value in the entry, it still works:

```sql
SELECT COALESCE(NULL,  NULL, NULL, NULL, NULL, NULL, NULL, 'JavaScript', NULL, NULL, NULL);
```

![ss3-1](https://www.freecodecamp.org/news/content/images/2023/01/ss3-1.png) 

## How to Handle NULL Values with the `COALESCE()` Function in PostgreSQL

You can use the `COALESCE()` function to handle NULL values in PostgreSQL by substituting those NULL values with a default value. 

Here’s the syntax:

```sql
SELECT COALESCE(column, defaultValue) FROM table;
```

If the NULL value is a type integer, the default value must be an integer. And if that NULL value is of type string, the default value must be a string. 

### Example of How to Handle NULL Values with the `COALESCE()` Function in PostgreSQL

I have a table `langs` with 6 entries created this way:

```sql
create table langs (yob integer, name varchar(100), purpose varchar(100));
		insert into langs (yob, name, purpose) values (NULL, 'JavaScript', 'frontend');
		insert into langs (yob, name, purpose) values (NULL, 'PHP', 'backend');
		insert into langs (yob, name, purpose) values (NULL, 'Python', 'everything');
   
        insert into langs (yob, name, purpose) values (2009, 'Golang', 'everything');
        insert into langs (yob, name, purpose) values (2010, 'Rust', 'Systems Programming');
        insert into langs (yob, name, purpose) values (NULL, 'MQL4', 'Trading Bots');
```

Here’s the table when I run `SELECT * FROM langs;`:

![ss4-1](https://www.freecodecamp.org/news/content/images/2023/01/ss4-1.png) 

This is what I got when I selected just the `yob` column (SELECT yob FROM langs;
):

![ss5-1](https://www.freecodecamp.org/news/content/images/2023/01/ss5-1.png)

I need a default value for those NULL values, so I’ll do it with syntax for handling NULL values in PostgreSQL:

```sql
SELECT COALESCE(yob, 0) FROM langs;
```

Here’s the result:

![ss6-1](https://www.freecodecamp.org/news/content/images/2023/01/ss6-1.png) 

## Conclusion
This article showed you what the `COALESCE()` function does in SQL. You can strip out NULL values in any column with it. We also looked at how you can use the `COALESCE()` function to handle NULL values in PostgreSQL. 

If you find this article helpful share it on social media with your friends and family.


