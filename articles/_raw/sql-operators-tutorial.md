---
title: SQL Operators Tutorial – Bitwise, Comparison, Arithmetic, and Logical Operator
  Query Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-18T15:18:03.000Z'
originalURL: https://freecodecamp.org/news/sql-operators-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9931740569d1a4ca1e5b.jpg
tags:
- name: data
  slug: data
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By John Mosesman

  At its core, the internet and all its applications are just data.

  Every email, tweet, selfie, bank transaction, and more is just data sitting in a
  database somewhere.

  For that data to be useful, we have to be able to retrieve it. How...'
---

By John Mosesman

At its core, the internet and all its applications are just data.

Every email, tweet, selfie, bank transaction, and more is just data sitting in a database somewhere.

For that data to be useful, we have to be able to retrieve it. However, just retrieving the data is not enough—the data _also_ has to be useful and relevant to our situation.

At the database level, we request specific information from the database by writing a **[SQL query](https://en.wikipedia.org/wiki/SQL).** This SQL query specifies the data we want to receive _and_ the format we want to receive it in.

In this article we'll look at all of the most common ways to filter a SQL query. 

Here's what we'll cover:

* [Setting up your database](#heading-setting-up-your-database)
* [Creating users](#heading-creating-users)
* [Inserting users](#heading-inserting-users)
* [Filtering data with `WHERE`](#heading-filtering-data-with-where)
* [Logical operators (`AND` / `OR` / `NOT`)](#heading-logical-operators-and-or-not)
* [Comparison operators (`<`, `>`, `<=`, `>=`)](#heading-comparison-operators-lt-gt-lt-gt)
* [Arithmetic operators (`+`, `-`, `*`, `/`, `%`)](#heading-arithmetic-operators)
* [Existence operators (`IN` / `NOT IN`)](#heading-existence-operators-in-not-in)
* [Partial matching using `LIKE`](#heading-partial-matching-using-like)
* [Dealing with missing data (`NULL`)](#heading-dealing-with-missing-data-null)
* [Using `IS NULL` and `IS NOT NULL`](#heading-using-is-null-and-is-not-null)
* [Comparison operators with dates and times](#heading-comparison-operators-with-dates-and-times)
* [Existence using `EXISTS` / `NOT EXISTS`](#heading-existence-using-exists-not-exists)
* [Bitwise operators](#heading-bitwise-operators)
* [Conclusion](#heading-conclusion)

## Setting up your database

To filter our data, we first of course must have some.

For these examples we'll be using PostgreSQL, but the queries and concepts shown here will easily translate to any other modern database system (like MySQL, SQL Server, etc.).

To work with our PostgreSQL database, we can use [`psql`](https://www.postgresql.org/docs/current/app-psql.html) — the interactive PostgreSQL command line program. If you have another database client that you enjoy working with that's fine too!

To begin, let's create our database. With PostgreSQL already [installed](https://www.postgresql.org/download/), we can run the `psql` command `createdb <database-name>` at our terminal to create a new database. I called mine `fcc`:

```bash
$ createdb fcc

```

Next let's start the interactive console by using the command `psql` and connect to the database we just made using `\c <database-name>`:

```bash
$ psql
psql (11.5)
Type "help" for help.

john=# \c fcc
You are now connected to database "fcc" as user "john".
fcc=#

```

## Creating users

Now that we have a database, let's create a database table to model a potential user in our fictional system.

We'll call this table `users`, and each row in this table will represent one of our users.

This `users` table will have columns that we would expect to describe a user — things like a name, email, and an age.

Inside our `psql` session let's create the `users` table:

```sql
CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL,
  age INTEGER NOT NULL
);
```

The output shows `CREATE TABLE` which means are table creation was successful.

> **Note:** I've cleaned up the `psql` output in these examples to make it easier to read, so don't worry if the output shown here isn't exactly what you've seen in your terminal.

Let's look at the contents of our users table:

```sql
SELECT * FROM users;

 id | first_name | last_name | email | age
----+------------+-----------+-------+-----
(0 rows)

```

We haven't inserted any data into our table, so we just see the empty table structure.

If you aren't familiar with SQL queries, the one we just ran, `SELECT * FROM users`, is one of the simplest ones you can write.

The keyword `SELECT` specifies which column(s) you want to return (`*` means "all columns"), and the `FROM` keyword specifies which table you want to select from (in this case `users`).

So `SELECT * FROM users` really means _return all rows and all columns from the `users` table._ 

If we wanted to return specific columns from the `users` table, we could replace `SELECT *` with the columns we want to return — for example `SELECT id, name FROM users`.

## Inserting users

An empty table isn't very interesting, so let's insert some data into our table so we can practice querying against it:

```sql
INSERT INTO users(first_name, last_name, email, age) VALUES
('John', 'Smith', 'johnsmith@gmail.com', 25),
('Jane', 'Doe', 'janedoe@Gmail.com', 28),
('Xavier', 'Wills', 'xavier@wills.io', 35),
('Bev', 'Scott', 'bev@bevscott.com', 16),
('Bree', 'Jensen', 'bjensen@corp.net', 42),
('John', 'Jacobs', 'jjacobs@corp.net', 56),
('Rick', 'Fuller', 'fullman@hotmail.com', 16);
```

If we run that insert statement in our `psql` session, we see the output `INSERT 0 7`. This means that we have successfully inserted 7 new rows into our table.

If we run our `SELECT * FROM users` query again, we'll now see that data:

```sql
SELECT * FROM users;

id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  2 | Rick       | Fuller    | fullman@hotmail.com |  16
  3 | Bree       | Jensen    | bjensen@corp.net    |  42
  4 | Bev        | Scott     | bev@bevscott.com    |  16
  5 | Xavier     | Wills     | xavier@wills.io     |  35
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(7 rows)

```

## Filtering data with `WHERE`

So far, we've just returned all of the rows from our table. This is the default behavior of the query. To return a more selective set of rows we need to **filter the rows using a `WHERE` clause.**

There are many ways to filter our rows using a `WHERE` clause. The simplest operator we can use is the equality operator: `=`.

Say we wanted to find users whose first name was "John":

```sql
SELECT *
FROM users
WHERE first_name = 'John';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  7 | John       | Smith     | johnsmith@gmail.com |  25
(2 rows)

```

Here we appended the keyword `WHERE` to our query followed by an equality statement: `first_name = 'John'`.

Our database first looks at the `FROM` keyword to determine what data to fetch. So, the database will read this query, see `FROM users`, and go and fetch all of the rows for the `users` table from the disk.

Once all of the rows have been retrieved from the `users` table, it then runs the `WHERE` clause against each row and only returns rows where the `first_name` column value equals "John."

In our data, there are two rows that match that first name.

If we wanted to find a particular "John" in our system, we could query based on a column that we know is unique — like our `id` column.

To find the "John Jacobs" row specifically, we could query by his ID:

```sql
SELECT *
FROM users
WHERE id = 1;

 id | first_name | last_name |      email       | age
----+------------+-----------+------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net |  56
(1 row)

```

Here only one record matched the condition of `id = 1`, so we only got back one row.

### Logical operators (`AND` / `OR` / `NOT`)

We can filter by more than just the equality operator. We can also use the boolean logical operators that are found in most programming languages: _and, or,_ and _not_.

In many programming languages _and_ and _or_ are represented by `&&` and `||`. In SQL, they're simply `AND` and `OR`.

Instead of querying by ID, let's try to find the record for the person named "John Smith." To do this, we can use an `AND` in our `WHERE` clause to look for both the first name and last name condition:

```sql
SELECT *
FROM users
WHERE first_name = 'John'
  AND last_name = 'Smith';
  
 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  7 | John       | Smith     | johnsmith@gmail.com |  25
(1 row)

```

To find people with a first name of "John" _or_ a last name of "Doe":

```sql
SELECT *
FROM users
WHERE first_name = 'John'
  OR last_name = 'Doe';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(3 rows)

```

Here our result contained both _Johns_ as well as Jane _Doe_.

These `AND` and `OR` conditions can also be chained together. Let's say we wanted to find someone named exactly "John Smith", _or_ someone with a last name of "Doe":

```sql
SELECT *
FROM users
WHERE
(
  first_name = 'John'
  AND last_name = 'Smith'
)
OR last_name = 'Doe';

 id | first_name  | last_name |        email        | age
----+------------+-----------+---------------------+-----
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(2 rows)

```

If we wanted to invert this condition and find users who are _not_ named "John Smith" and also do _not_ have a last name of "Doe", we could add the `NOT` operator:

```sql
SELECT *
FROM users
WHERE NOT
(
  (
    first_name = 'John'
    AND last_name = 'Smith'
  )
  OR last_name = 'Doe'
);
 
 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  4 | Bev        | Scott     | bev@bevscott.com    |  16
  5 | Bree       | Jensen    | bjensen@corp.net    |  42
  6 | John       | Jacobs    | jjacobs@corp.net    |  56
  7 | Rick       | Fuller    | fullman@hotmail.com |  16
  3 | Xavier     | Wills     | xavier@wills.io     |  35
(5 rows)
```

> **Note:** everyone has their own personal style of how they like to format queries — do whatever makes sense to you!

### Comparison operators (`<`, `>`, `<=`, `>=`)

Similar to other programming languages, SQL also the comparison operators: `<`, `>`, `<=`, `>=`.

Let's practice using these operators against our users' `age` column.

Let's say we wanted to find users that were _eighteen years or older_:

```sql
SELECT * FROM users WHERE age >= 18;

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  3 | Bree       | Jensen    | bjensen@corp.net    |  42
  5 | Xavier     | Wills     | xavier@wills.io     |  35
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(5 rows)

```

What about users that are older than 25, but less than or equal to 35 years old?

```sql
SELECT * FROM users WHERE age > 25 AND age <= 35;

 id | first_name | last_name |       email       | age
----+------------+-----------+-------------------+-----
  5 | Xavier     | Wills     | xavier@wills.io   |  35
  6 | Jane       | Doe       | janedoe@Gmail.com |  28
(2 rows)

```

### Arithmetic operators (`+`, `-`, `*`, `/`, `%`)

We can also perform mathematical calculations on our data.

Our `users` table has an `age` column, what if we wanted to find _half_ of each person's age?

```sql
SELECT
  *,
  age / 2 AS half_of_their_age
FROM users;

 id | first_name | last_name |        email        | age | half_of_their_age
----+------------+-----------+---------------------+-----+-------------------
  1 | John       | Jacobs    | jjacobs@corp.net    |  56 |                28
  2 | Rick       | Fuller    | fullman@hotmail.com |  16 |                 8
  3 | Bree       | Jensen    | bjensen@corp.net    |  42 |                21
  4 | Bev        | Scott     | bev@bevscott.com    |  16 |                 8
  5 | Xavier     | Wills     | xavier@wills.io     |  35 |                17
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28 |                14
  7 | John       | Smith     | johnsmith@gmail.com |  25 |                12
(7 rows)

```

Here we select all of the table columns (using `SELECT *`), and we also select a new aggregate calculation: `age / 2`. We also give this value a descriptive name (`half_of_their_age`) with an alias using the `AS` keyword.

We can also find who's age is an _even number_ by using the modulus or remainder operator (`%`):

```sql
SELECT * FROM users WHERE (age % 2) = 0;

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  2 | Rick       | Fuller    | fullman@hotmail.com |  16
  3 | Bree       | Jensen    | bjensen@corp.net    |  42
  4 | Bev        | Scott     | bev@bevscott.com    |  16
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
(5 rows)

```

We can find who's age is an _odd number_ by changing our `=` condition to a "not equals" using `!=` or `<>`:

```sql
SELECT * FROM users WHERE (age % 2) <> 0;

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  5 | Xavier     | Wills     | xavier@wills.io     |  35
  7 | John       | Smith     | johnsmith@gmail.com |  25
(2 rows)

```

### Existence operators (`IN` / `NOT IN`)

If we wanted to check that a column value existed in a list of values, we can use `IN` or `NOT IN`:

```sql
SELECT *
FROM users
WHERE first_name IN ('John', 'Jane', 'Rick');

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28
  6 | John       | Jacobs    | jjacobs@corp.net    |  56
  7 | Rick       | Fuller    | fullman@hotmail.com |  16
(4 rows)

```

Similarly, we can use `NOT IN` to negate that condition:

```sql
SELECT *
FROM users
WHERE first_name NOT IN ('John', 'Jane', 'Rick');

 id | first_name | last_name |      email       | age
----+------------+-----------+------------------+-----
  3 | Xavier     | Wills     | xavier@wills.io  |  35
  4 | Bev        | Scott     | bev@bevscott.com |  16
  5 | Bree       | Jensen    | bjensen@corp.net |  42
(3 rows)

```

### Partial matching using `LIKE`

Sometimes, we may want to search for rows based on a partial-search.

Say for example we wanted to find all users that signed up for our application using a Gmail address. We can do a partial match against a column using the `LIKE` keyword. We can also specify a wildcard (or "match anything") in the match string using `%`.

To find users with an email that ends in `gmail.com`:

```sql
SELECT *
FROM users
WHERE email LIKE '%gmail.com';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
(1 row)

```

The string `%gmail.com` means "match anything that ends in `gmail.com`."

If we look back at our users data, we'll notice that we actually have two users with a `gmail.com` address:

```
('John', 'Smith', 'johnsmith@gmail.com', 25),
('Jane', 'Doe', 'janedoe@Gmail.com', 28),

```

However, Jane's email has a capital "G' in her email address. Or previous query didn't pick up this record because it was matching _exactly_ against `gmail.com` with a lowercase "g."

To do a case-insensitive match, we just need to substitute `LIKE` for `ILIKE`:

```sql
SELECT *
FROM users
WHERE email ILIKE '%gmail.com';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28
(2 rows)

```

The wildcard symbol `%` at the beginning of the string means anything that ends in "gmail.com" will be returned. That could be `bob.jones+12345@gmail.com` or `asdflkasdflkj@gmail.com` — as long as it ends in `gmail.com`.

We can also add as many wildcards (`%`) as we want.

For example, the search term `%j%o%` will return any emails that follow the pattern `<anything>` followed by a `j`, followed by `<anything>`, followed by an `o`, followed by `<anything>`:

```sql
SELECT * FROM users WHERE email ILIKE '%j%o%';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28
  5 | Bree       | Jensen    | bjensen@corp.net    |  42
  6 | John       | Jacobs    | jjacobs@corp.net    |  56
(4 rows)

```

## Dealing with missing data (`NULL`)

Next let's look at how we deal with rows with columns that have missing data.

To do that, let's add another column to our `users` table: `first_paid_at`.

This new column will be a `TIMESTAMP` (similar to a `datetime` in other languages), and it will represent the first date and time that a user paid us money for our application. Maybe we want to send them a nice card or some flowers on the anniversary of using our app?

We could drop our `users` table using `DROP TABLE users;` and re-create it, but that would also delete all of the data in our table.

To change a table without dropping it and losing the data, we can use `ALTER TABLE`:

```sql
ALTER TABLE users ADD COLUMN first_paid_at TIMESTAMP; 
```

That command returns the result `ALTER TABLE`, so our `ALTER` query succeeded.

If we query our `users` table now, we'll notice that this new column doesn't have any data in it:

```sql
SELECT * FROM users;

 id | first_name | last_name |        email        | age | first_paid_at
----+------------+-----------+---------------------+-----+---------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 |
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28 |
  3 | Xavier     | Wills     | xavier@wills.io     |  35 |
  4 | Bev        | Scott     | bev@bevscott.com    |  16 |
  5 | Bree       | Jensen    | bjensen@corp.net    |  42 |
  6 | John       | Jacobs    | jjacobs@corp.net    |  56 |
  7 | Rick       | Fuller    | fullman@hotmail.com |  16 |
(7 rows)

```

Our `first_paid_at` column is empty, and the result from our `psql` query shows it as an empty column. This column is not technically empty — it contains a special value that `psql` is choosing not to display in its output: `NULL`.

[`NULL`](https://en.wikipedia.org/wiki/Null_(SQL)) is a special value in databases. It's the absence or lack of a value, and it doesn't behave as we expect it would.

To illustrate this, let's look at the simple `SELECT` statements below:

```sql
SELECT
  1 = 1,
  1 = 2;

 ?column? | ?column?
----------+----------
 t        | f
(1 row)

```

Here we simply selected `1 = 1` and `1 = 2`. As we expect, the result of these two statements is `t` and `f` (or `TRUE` and `FALSE`). `1` is equal to `1`, and `1` is not equal to `2`.

Now let's try the same with `NULL`:

```sql
SELECT 1 = NULL;

 ?column?
----------

(1 row)

```

We might expect this value to be `FALSE`, but the return value is actually `NULL`.

To visualize these `NULL`s a little better, let's set how `psql` displays `NULL` values using the `\pset` option:

```sql
fcc=# \pset null 'NULL'
Null display is "NULL".

```

Now if we run that query again we'll see the `NULL` output we expect:

```sql
SELECT 1 = NULL;

 ?column?
----------
 NULL
(1 row)

```

So `1` is not equal to `NULL`, what about `NULL = NULL`?

```sql
SELECT NULL = NULL;

 ?column?
----------
 NULL
(1 row)

```

Oddly enough, `NULL` is not equal to `NULL`.

It helps to think of `NULL` as an unknown value. Is an unknown value equal to `1`? Well, we don't know — it's unknown. Is an unknown value equal to an unknown value? Again, it's unknown. In this way `NULL` makes a little more sense.

### Using `IS NULL` and `IS NOT NULL`

We can't use the equality operator with `NULL`, but we can use two operators specifically designed for it: `IS NULL` and `IS NOT NULL`.

```sql
SELECT
  NULL IS NULL,
  NULL IS NOT NULL;

 ?column? | ?column?
----------+----------
 t        | f
(1 row)

```

These values come out as expect: `NULL IS NULL` is true, and `NULL IS NOT NULL` is false.

That's all fine and weird, but how do we use this?

Well first let's get some data in our `first_paid_at` column:

```sql
UPDATE users SET first_paid_at = NOW() WHERE id = 1;
UPDATE 1

UPDATE users SET first_paid_at = (NOW() - INTERVAL '1 month') WHERE id = 2;
UPDATE 1

UPDATE users SET first_paid_at = (NOW() - INTERVAL '1 year') WHERE id = 3;
UPDATE 1

```

In those `UPDATE` statements above we've set three different users `first_paid_at` columns: User ID 1 to the current time (`NOW()`), User ID 2 to one month ago, and User ID 3 to one year ago.

First, let's find users that have paid us and users who haven't:

```sql
SELECT *
FROM users
WHERE first_paid_at IS NULL;

 id | first_name | last_name |        email        | age | first_paid_at
----+------------+-----------+---------------------+-----+---------------
  4 | Bev        | Scott     | bev@bevscott.com    |  16 | NULL
  5 | Bree       | Jensen    | bjensen@corp.net    |  42 | NULL
  6 | John       | Jacobs    | jjacobs@corp.net    |  56 | NULL
  7 | Rick       | Fuller    | fullman@hotmail.com |  16 | NULL
(4 rows)

SELECT *
FROM users
WHERE first_paid_at IS NOT NULL;

 id | first_name | last_name |        email        | age |       first_paid_at
----+------------+-----------+---------------------+-----+----------------------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 | 2020-08-11 20:49:17.230517
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28 | 2020-07-11 20:49:17.233124
  3 | Xavier     | Wills     | xavier@wills.io     |  35 | 2019-08-11 20:49:17.23488
(3 rows)

```

### Comparison operators with dates and times

Now that we have some data, let's use our same comparison operators against this new `TIMESTAMP` field.

Let's try to find users that paid us for the first within the past week. To do this, we can take the current time, `NOW()`, and subtract from it one week using the `INTERVAL` keyword:

```sql
SELECT *
FROM users
WHERE first_paid_at > (NOW() - INTERVAL '1 week');

 id | first_name | last_name |        email        | age |       first_paid_at
----+------------+-----------+---------------------+-----+----------------------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 | 2020-08-11 20:49:17.230517
(1 row)

```

We could also use a different interval, such as three months ago:

```sql
SELECT *
FROM users
WHERE first_paid_at < (NOW() - INTERVAL '3 months');

 id | first_name | last_name |      email      | age |       first_paid_at
----+------------+-----------+-----------------+-----+---------------------------
  3 | Xavier     | Wills     | xavier@wills.io |  35 | 2019-08-11 20:49:17.23488
(1 row)

```

Let's try to find users that first paid us between one to six months ago.

We could combine our conditions again using `AND`, but instead of using _less than_ and _greater than_ operators let's use the `BETWEEN` keyword:

```sql
SELECT *
FROM users
WHERE first_paid_at BETWEEN (NOW() - INTERVAL '6 month')
  AND (NOW() - INTERVAL '1 month');
  
 id | first_name | last_name |       email       | age |       first_paid_at
----+------------+-----------+-------------------+-----+----------------------------
  2 | Jane       | Doe       | janedoe@Gmail.com |  28 | 2020-07-11 20:49:17.233124
(1 row)

```

### Existence using `EXISTS` / `NOT EXISTS`

Another way to check for existence is to use `EXISTS` and `NOT EXISTS`. 

These operators filter out rows by checking for the existence (or non-existence) of a condition. This condition is usually a query against another table.

To set this up, let's create a new table called `posts`. This table will hold posts that a user can make in our system.

```sql
CREATE TABLE posts(
  id SERIAL PRIMARY KEY,
  body TEXT NOT NULL,
  user_id INTEGER REFERENCES users NOT NULL
);

```

It's a simple table. It only contains an ID, a field to store the post text (`body`), and a reference to the user that wrote the post (`user_id`).

Let's insert some data into this new table:

```sql
INSERT INTO posts(body, user_id) VALUES
('Here is post 1', 1),
('Here is post 2', 1),
('Here is post 3', 2),
('Here is post 4', 3);

```

In the data that we inserted into the `posts` table, User ID 1 has two posts, User ID 2 has one post, and User ID 3 also has one post.

To find users that do have posts, we can use `EXISTS`.

The `EXISTS` keyword takes a subquery. If _anything_ is returned from that subquery (even a row with just the value of `NULL`), the database will include that row in the result set.

[From the PostgreSQL docs](https://www.postgresql.org/docs/current/functions-subquery.html#FUNCTIONS-SUBQUERY-EXISTS) on `EXISTS`:

> The argument of EXISTS is an arbitrary SELECT statement, or subquery. The subquery is evaluated to determine whether it returns any rows. If it returns at least one row, the result of EXISTS is “true”; if the subquery returns no rows, the result of EXISTS is “false”.

`EXISTS` is just looking for the _existence_ of a row from the subquery — it doesn't matter what's in it.

Here's an example of users that have posts using `EXISTS`:

```sql
SELECT *
FROM users
WHERE EXISTS (
  SELECT 1
  FROM posts
  WHERE posts.user_id = users.id
);

 id | first_name | last_name |        email        | age |       first_paid_at
----+------------+-----------+---------------------+-----+----------------------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 | 2020-08-11 20:49:17.230517
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28 | 2020-07-11 20:49:17.233124
  3 | Xavier     | Wills     | xavier@wills.io     |  35 | 2019-08-11 20:49:17.23488
(3 rows)

```

As we expected we got back User 1, 2, and 3.

Our `EXISTS` subquery is checking for a `posts` record where the post's `user_id` matches the `id` column on the `users` table. We returned `1` in our `SELECT` because we can return anything here—the database just wants to see that something was in fact returned.

Similarly, we could find users that don't have any posts by changing `EXISTS` to `NOT EXISTS`:

```sql
SELECT *
FROM users
WHERE NOT EXISTS (
  SELECT 1
  FROM posts
  WHERE posts.user_id = users.id
);

 id | first_name | last_name |        email        | age | first_paid_at
----+------------+-----------+---------------------+-----+---------------
  4 | Bev        | Scott     | bev@bevscott.com    |  16 | NULL
  5 | Bree       | Jensen    | bjensen@corp.net    |  42 | NULL
  6 | John       | Jacobs    | jjacobs@corp.net    |  56 | NULL
  7 | Rick       | Fuller    | fullman@hotmail.com |  16 | NULL
(4 rows)

```

Finally, we could also re-write this query to use `IN` or `NOT IN` instead of `EXISTS` or `NOT EXISTS`, like this:

```sql
SELECT *
FROM users
WHERE users.id IN (
  SELECT user_id
  FROM posts
);

```

This technically works, but as a general rule if you are testing for _existence_ of another record it is _generally_ more performant to use `EXISTS`. The `IN` and `NOT IN` operator are generally better used for checking a value against a static list like we did earlier:

```sql
SELECT *
FROM users
WHERE first_name IN ('John', 'Jane', 'Rick');

```

### Bitwise operators

Although in practice the bitwise operators are not often used, for completeness let's look at a simple example.

If we wanted to (for some reason) look at the age of our users in binary and play with flipping those bits around, we could use a variety of bitwise operators.

As an example, let's look at the bitwise "and" operator: `&`.

```sql
SELECT age::bit(8) & '11111111' FROM users;

 ?column?
----------
 00010000
 00101010
 00111000
 00010000
 00011001
 00011100
 00100011
(7 rows)
```

To perform a bitwise calculation we first have to convert our `age` column from an integer to binary — in this example we cast it into an eight-bit binary string using `::bit(8)`.

Next we can "and" the result of our age in binary format with another binary string, `11111111`.  Since a binary `AND` only returns 1 if both bits are 1's, this all 1's string keeps the output interesting.

Almost every other bitwise operator uses the same format:

```sql
SELECT age::bit(8) | '11111111' FROM users;    -- bitwise OR
SELECT age::bit(8) # '11111111' FROM users;    -- bitwise XOR
SELECT age::bit(8) << '00000001' FROM users;   -- bitwise shift left
SELECT age::bit(8) >> '00000001' FROM users;   -- bitwise shift right
```

The bitwise "not" operator (`~`) is a little different in that it is applied to a single term — similar to the regular `NOT` operator:

```sql
SELECT ~age::bit(8) FROM users;

 ?column?
----------
 11101111
 11010101
 11000111
 11101111
 11100110
 11100011
 11011100
(7 rows)
```

And finally, the most useful of the bitwise operators: concatenation.

A common use of this operator is to combine strings of text together. For example if we wanted to build a calculated property of a "full name" for users, we could use concatenation:

```sql
SELECT first_name || ' ' || last_name AS name
FROM users;

     name
--------------
 Bev Scott
 Bree Jensen
 John Jacobs
 Rick Fuller
 John Smith
 Jane Doe
 Xavier Wills
(7 rows)
```

Here we concatenate (or "combine") the `first_name`, a space (`' '`), and the `last_name` property to build a `name` value.

## Conclusion

So that's an overview of basically every query filtering operator you'll ever need to use!

There are a few more operators that we didn't cover here, but those operators are either not used very often or are used in exactly the same way as above—so they shouldn't pose you any trouble.

If you liked this post, I write similar things [on my blog here.](https://johnmosesman.com/)

Thanks for reading!

John

