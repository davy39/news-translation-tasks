---
title: SQL Where Contains String – Substring Query Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-23T22:36:06.000Z'
originalURL: https://freecodecamp.org/news/sql-where-contains-string-substring-query-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/sqlSubstring.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "If you’re working with a database, whether large or small, there might\
  \ be occasions when you need to search for some entries containing strings. \nIn\
  \ this article, I’ll show you how to locate strings and substrings in MySQL and\
  \ SQL Server.\nI‘ll be usi..."
---

If you’re working with a database, whether large or small, there might be occasions when you need to search for some entries containing strings. 

In this article, I’ll show you how to locate strings and substrings in MySQL and SQL Server.

I‘ll be using a table I call `products_data` in a `products_schema` database. Running `SELECT * FROM products_data` shows me all the entries in the table:

![Screenshot-2023-03-23-at-10.39.24](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-10.39.24.png)

Since I’ll be showing you how to search for a string in SQL Server too, I have the `products_data` table in a `products` database:

![Screenshot-2023-03-23-at-10.42.05](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-10.42.05.png)


## What We'll Cover
- [How to Query for Strings in SQL with the `WHERE` Clause and `LIKE` Operator](#heading-how-to-query-for-strings-in-sql-with-the-where-clause-and-like-operator)
- [How to Query for Strings in SQL Server with the `CHARINDEX` Function](#heading-how-to-query-for-strings-in-sql-server-with-the-charindex-function)
- [How to Query for Strings in SQL Server with the `PATINDEX` Function](#heading-how-to-query-for-strings-in-sql-server-with-the-patindex-function)
- [How to Query for Strings in MySQL with the `SUBSTRING_INDEX()` Function](#heading-how-to-query-for-strings-in-mysql-with-the-substringindex-function)
- [Conclusion](#heading-conclusion)


## How to Query for Strings in SQL with the `WHERE` Clause and `LIKE` Operator
The `WHERE` clause lets you get only the records that meet a particular condition. The `LIKE` operator, on the other hand, lets you find a particular pattern in a column. You can combine these two to search for a string or a substring of a string.

I was able to get all the products that have the word “computer” in them by combining the `WHERE` clause and `LIKE` operator by running the query below:

```sql
SELECT * FROM products_data
WHERE product_name LIKE '%computer%'
```

![Screenshot-2023-03-23-at-11.01.49](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.01.49.png)

The percentage sign before and after the word “computer” means, **find the word “computer” whether it’s in the end, middle, or start**. 

So, if you put the percentage sign at the start of a substring you’re searching by, it means, **find that substring at the end of a string**. For Example, I got every product that ends with “er” by running this query:

```sql
SELECT * FROM products_data
WHERE product_name LIKE '%er'
```

![Screenshot-2023-03-23-at-11.07.53](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.07.53.png)

And if it’s at the end of a string, it means, **find that substring at the start of a string**. For example, I was able to get the product that starts with “lap” with this query:

```sql
SELECT * FROM products_data
WHERE product_name LIKE 'lap%'
```

![Screenshot-2023-03-23-at-11.09.59](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.09.59.png)

This method also works fine in SQL Server:

![Screenshot-2023-03-23-at-11.19.51](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.19.51.png)


## How to Query for Strings in SQL Server with the `CHARINDEX` Function
CHARINDEX() is an SQL server function for finding the index of a substring in a string. 

The `CHARINDEX()` function takes 3 arguments – the substring, the string, and the starting position. The syntax looks like this:

```sql
CHARINDEX(substring, string, start_position)
```

If it finds a match, it returns the index where it finds the match, but if it doesn’t find a match, it returns 0. Unlike many other languages, counting in SQL is 1-based. 

Here’s an example:

```sql
SELECT CHARINDEX('free', 'free is the watchword of freeCodeCamp') position;
```

![Screenshot-2023-03-23-at-12.33.03](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.33.03.png)

You can see the word free was found in position 1. That’s because ‘f’ itself is at position 1:

![Screenshot-2023-03-23-at-12.36.22](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.36.22.png)

If I specify 25 as the position, SQL Server would find a match starting from the “freeCodeCamp” text:

```sql
SELECT CHARINDEX('free', 'free is the watchword of freeCodeCamp', 25);
```

![Screenshot-2023-03-23-at-12.39.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.39.10.png)

I was able to use the `CHARINDEX` function to search for all products that have the word “computer” in them by running this query:

```sql
SELECT * FROM products_data WHERE CHARINDEX('computer', product_name, 0) > 0
```

That query is saying, **start from index 0, as long as they’re more than 0, get me every product that has the word “computer” in them in the `product_name` column**. This is the result:

![Screenshot-2023-03-23-at-12.43.31](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.43.31.png) 


## How to Query for Strings in SQL Server with the `PATINDEX` Function
`PATINDEX` stands for “pattern index”. So, with this function, you can search for a substring with regular expressions. 

`PATINDEX` takes two arguments – the pattern and the string. The syntax looks like this:

```sql
PATINDEX(pattern, string)
``` 

If `PATINDEX` finds a match, it returns the position of that match. If it doesn’t find a match, it returns 0. Here’s an example:

```sql
SELECT PATINDEX('%ava%', 'JavaScript is a Jack of all trades');
```

![Screenshot-2023-03-23-at-12.52.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.52.54.png)

To apply `PATINDEX` to the example table, I ran this query:

```sql
SELECT product_name, PATINDEX('%ann%', product_name) position
FROM products_data
```

But it only listed every product and returned the index where it found the match:

![Screenshot-2023-03-23-at-13.08.46](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-13.08.46.png)

You can see it found the word “ann” at index 3 of the product Scanner. On many occasions, you might not want this behavior because you would want it to show only the item matched.

I made it return only what gets matched by using the `WHERE` clause and `LIKE` operator:

```sql
SELECT product_name, PATINDEX('%ann%', product_name) position
FROM products_data
WHERE product_name LIKE '%ann%'
```

![Screenshot-2023-03-23-at-13.11.28](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-13.11.28.png)

Now it's behaving as you would want.


## How to Query for Strings in MySQL with the `SUBSTRING_INDEX()` Function
Apart from the solutions I’ve already shown you, MySQL has an inbuilt `SUBSTRING_INDEX()` function with which you can find a part of a string.

The `SUBSTRING_INDEX()` function takes 3 compulsory arguments – the string, the substring to search for, and a delimiter. The delimiter has to be a number. 

When you specify the compulsory arguments, the `SUBSTRING_INDEX()` function will get you every part of the string that occurs before the delimiter you specify. Here’s an example:

```sql
SELECT SUBSTRING_INDEX("Learn on freeCodeCamp with me", "with", 1);
```

![Screenshot-2023-03-23-at-14.14.14](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-14.14.14.png)

In the query above, "Learn on freeCodeCamp with me" is the string, "with" is the substring and 1 is the delimiter. In this case, the query will get you “Learn on freeCodeCamp”:

The delimiter can also be a negative number. If it’s a negative number, it gets you each part of the string that occurs after the delimiter you specify. Here’s an example:

```sql
SELECT SUBSTRING_INDEX("Learn on freeCodeCamp with me", "with", -1);
```

![Screenshot-2023-03-23-at-14.16.09](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-14.16.09.png)


## Conclusion
This article showed you how to locate a substring in a string in SQL using both MySQL and SQL Server.

`CHARINDEX()` and `PATINDEX()` are the functions with which you can search for a substring in a string inside SQL Server. `PATINDEX()` is more powerful because it lets you use regular expressions.

Since `CHARINDEX()` and `PATINDEX()` don’t exist in MySQL, the first example showed you how you can find a substring in a string with the `WHERE` clause and `LIKE` operator.

Thank you for reading!


