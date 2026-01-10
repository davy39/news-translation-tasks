---
title: Cast a Function in SQL – Convert Char to Int SQL Server Example
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-08T19:35:48.000Z'
originalURL: https://freecodecamp.org/news/cast-a-function-in-sql-convert-char-to-int-sql-server-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Cast-a-Function-in-SQL---Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "Converting from one data type to another is a common operation you'll perform\
  \ when working in databases. \nAnd SQL provides a useful utility known as CAST to\
  \ achieve this. We'll see how it works in this article.\nWhat is the CAST Function\
  \ in SQL?\nCAST ..."
---

Converting from one data type to another is a common operation you'll perform when working in databases. 

And SQL provides a useful utility known as CAST to achieve this. We'll see how it works in this article.

## What is the CAST Function in SQL?

CAST enables us to convert from one data type to another. It is very helpful in concatenating results of different data types. It also helps us perform calculations on two different data types.

CAST does not alter the data in the database. The conversion is valid only during the life of the query. But it is possible to convert and insert in a new column or table. 

### Syntax of CAST in SQL

Below is the syntax of the CAST function:

```sql
CAST ( expression AS data_type [ ( length ) ])
```

Where,

* `expression` is the query such as: `id as VARCHAR`
* `data_type` is the target data type.
* `length` determines the length of the target data type. This part is optional.

## How to Use the CAST Function in SQL

### Sample table

Let's create a table `store_locations` as shown below:

```sql
-- create a table named store_locations

CREATE TABLE store_locations (
  id INTEGER PRIMARY KEY,
  store_name VARCHAR(10) NOT NULL,
  store_id INTEGER NOT NULL,
  postal_code VARCHAR(10)
);

```

Where,

* `id` is the Primary Key.
* `store_name` is the store's name with `VARCHAR` datatype.
* `store_id` is the ID of the store and an `INTEGER`.
* `postal_code` is store's postal address with type `VARCHAR`. 

After inserting some values, our table looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-24.png)
_store_locations table_

### How to convert `char` to `int` in SQL

Let's check out an example of how to convert the char (VARCHAR) datatype into int.

In our example, our task is to generate a new column which adds (sums) the `store_id` and `postal_code` to generate another unique ID.

Remember, `store_id` is an `INTEGER`, whereas `postal_code` is `VARCHAR`. To convert `postal_code` into an integer, we can use CAST like this:

```sql
-- convert char to int
-- generate a new id by adding store id and postal code

select store_id, postal_code, store_id + cast(postal_code AS INTEGER) AS [StoreID-Postalcode] from store_locations


```

**Output**:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-25.png)
_Combining the columns store_id and postal_code_

### How to convert `int` into `char` in SQL

In this example, our goal is to combine two columns – `store_name` and `store_id` – to generate a new column.

Remember, `store_name` is a `VARCHAR`, whereas `store_id` is an `INTEGER`.

If we try to add `int` and `char` without casting, what would be the result?

We would get an exception as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-26.png)
_Type conversion exception_

Let's cast and see the results.

```bash
-- conversion from int to char
-- storename + store ID

select store_name, store_id, store_name + ' - ' + cast(store_id AS VARCHAR) AS [Storename-storeId]
from store_locations
```

**Output:**

We can see that our output has been concatenated without error.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-27.png)

## Wrapping Up

The CAST function is very useful to convert data types and perform complex calculations. 

Do give these commands a try and experiment with different data types like 'date'. 

