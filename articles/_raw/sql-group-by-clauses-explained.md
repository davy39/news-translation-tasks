---
title: 'SQL Group By Tutorial: Count, Sum, Average, and Having Clauses Explained'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T18:39:37.000Z'
originalURL: https://freecodecamp.org/news/sql-group-by-clauses-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d4740569d1a4ca1c42.jpg
tags:
- name: Productivity
  slug: productivity
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By John Mosesman

  The GROUP BY clause is a powerful but sometimes tricky statement to think about.

  Even eight years later, every time I use a GROUP BY I have to stop and think about
  what it''s actually doing.

  In this article we''ll look at how to constr...'
---

By John Mosesman

The `GROUP BY` clause is a powerful but sometimes tricky statement to think about.

Even eight years later, every time I use a `GROUP BY` I have to stop and think about what it's actually doing.

In this article we'll look at how to construct a `GROUP BY` clause, what it does to your query, and how you can use it to perform aggregations and collect insights about your data.

Here's what we'll cover:

* [Setting up your database](#heading-setting-up-your-database)
* [Setting up example data (creating sales)](#heading-setting-up-the-data-creating-sales)
* [How does a `GROUP BY` work?](#heading-how-does-a-group-by-work)
* [Writing `GROUP BY` clauses](#heading-writing-group-by-clauses)
* [Aggregations ( `COUNT`, `SUM`, `AVG`)](#heading-aggregations-count-sum-avg)
* [Working with multiple groups](#heading-working-with-multiple-groups)
* [Using functions in the `GROUP BY`](#heading-using-functions-in-the-group-by)
* [Filtering groups with `HAVING`](#heading-filtering-groups-with-having)
* [Aggregates with implicit grouping](#heading-aggregates-with-implicit-grouping)

## Setting up your database

Before we can write our queries we need to setup our database.

For these examples we'll be using PostgreSQL, but the queries and concepts shown here will easily translate to any other modern database system (like MySQL, SQL Server, and so on).

To work with our PostgreSQL database, we can use [psql](https://www.postgresql.org/docs/current/app-psql.html)—the interactive PostgreSQL command line program. If you have another database client that you enjoy working with that's fine too.

To begin, let's create our database. With [PostgreSQL](https://www.postgresql.org/download/) already installed, we can run the command `createdb <database-name>` at our terminal to create a new database. I called mine `fcc`:

```
$ createdb fcc

```

Next let's start the interactive console by using the command `psql`, and connect to the database we just made using `\c <database-name>`:

```
$ psql
psql (11.5)
Type "help" for help.

john=# \c fcc
You are now connected to database "fcc" as user "john".
fcc=#

```

> **Note:** I've cleaned up the `psql` output in these examples to make it easier to read, so don't worry if the output shown here isn't exactly what you've seen in your terminal.

I encourage you to follow along with these examples and run these queries for yourself. You will learn and remember far more by working through these examples rather than just reading them.

## Setting up the data (creating sales)

For our examples we'll use a table that stores the sales records of various products across different store locations.

We'll call this table `sales`, and it will be a simple representation of store sales: the location name, product name, price, and the time it was sold.

If we were building this table in a real application we'd set up foreign keys to other tables (like `locations` or `products`). But for illustrating the `GROUP BY` concepts we'll just use simple `TEXT` columns.

Let's create the table and insert some sales data:

```sql
CREATE TABLE sales(
  location TEXT,
  product TEXT,
  price DECIMAL,
  sold_at TIMESTAMP
);

INSERT INTO sales(location, product, price, sold_at) VALUES
('HQ', 'Coffee', 2, NOW()),
('HQ', 'Coffee', 2, NOW() - INTERVAL '1 hour'),
('Downtown', 'Bagel', 3, NOW() - INTERVAL '2 hour'),
('Downtown', 'Coffee', 2, NOW() - INTERVAL '1 day'),
('HQ', 'Bagel', 2, NOW() - INTERVAL '2 day'),
('1st Street', 'Bagel', 3, NOW() - INTERVAL '2 day' - INTERVAL '1 hour'),
('1st Street', 'Coffee', 2, NOW() - INTERVAL '3 day'),
('HQ', 'Bagel', 3, NOW() - INTERVAL '3 day' - INTERVAL '1 hour');

```

We have three locations: _HQ_, _Downtown_, and _1st Street._

We have two products, _Coffee_ and _Bagel_, and we insert these sales with different `sold_at` values to represent the items being sold at different days and times.

There are some sales today, some yesterday, and some from the day before yesterday.

## How does a `GROUP BY` work?

To illustrate how the `GROUP BY` clause works, let's first talk through an example.

Imagine we had a room full of people who were born in different countries.

If we wanted to find the **average height** of the people in the room **per country,** we would first ask these people to separate into groups based on their birth country.

Once they were separated into their groups we could then calculate the average height within that group.

This is how the `GROUP BY` clause works. First we define how we want to group the rows together—then we can perform calculations or aggregations on the groups.

### Multiple groups

We can group the data into as many groups or sub-groups as we want.

For example, after asking people to separate into groups based on their birth countries, we could tell each of those groups of countries to separate _further_ into groups _based on their eye color._

By doing this, we have groups of people based on the combination of their birth country _and_ their eye color.

Now we could find the average height within each of these smaller groups, and we'd have a more specific result: average height _per country per eye color_.

`GROUP BY` clauses are often used for situations where you can use the phrase _**per** something_ or _**for each** something_:

* Average height _per_ birth country
* Total number of people _for each_ eye and hair color combination
* Total sales _per_ product

## Writing `GROUP BY` clauses

A `GROUP BY` clause is very easy to write—we just use the keywords `GROUP BY` and then specify the field(s) we want to group by:

```sql
SELECT ...
FROM sales
GROUP BY location;
```

This simple query groups our `sales` data by the `location` column.

We've done the grouping—but what do we put in our `SELECT`?

The obvious thing to select is our `location`—we're grouping by it so we at least want to see the name of the groups we made:

```sql
SELECT location
FROM sales
GROUP BY location;

```

The result is our three locations:

```
  location
------------
 1st Street
 HQ
 Downtown
(3 rows)

```

If we look at our raw table data (`SELECT * FROM sales;`), we'll see that we have four rows with a location of _HQ_, two rows with a location of _Downtown_, and two rows with a location of _1st Street:_

```
 product |  location  | price |          sold_at
---------+------------+-------+----------------------------
 Coffee  | HQ         |     2 | 2020-09-01 09:42:33.085995
 Coffee  | HQ         |     2 | 2020-09-01 08:42:33.085995
 Bagel   | Downtown   |     3 | 2020-09-01 07:42:33.085995
 Coffee  | Downtown   |     2 | 2020-08-31 09:42:33.085995
 Bagel   | HQ         |     2 | 2020-08-30 09:42:33.085995
 Bagel   | 1st Street |     3 | 2020-08-30 08:42:33.085995
 Coffee  | 1st Street |     2 | 2020-08-29 09:42:33.085995
 Bagel   | HQ         |     3 | 2020-08-29 08:42:33.085995
(8 rows)

```

By grouping on the `location` column, our database takes these inputs rows and identifies the unique locations among them—these unique locations serve as our _"groups."_

But what about the other columns in our table?

If we try to select a column like `product` that we didn't group by...

```sql
SELECT
  location,
  product
FROM sales
GROUP BY location;

```

...we run into this error:

```
ERROR:  column "sales.product" must appear in the GROUP BY clause or be used in an aggregate function

```

The problem here is we've taken _eight_ rows and squished or distilled them down to _three._

We can't just return the rest of the columns like normal—we had eight rows, and now we have three.

What do we do with the remaining five rows of data? Which of the eight rows' data should be displayed on these three distinct location rows? 

There's not a clear and definitive answer here.

To use the rest of our table data, we also have to distill the data from these remaining columns down into our three location groups.

This means that we have to **aggregate** or perform a calculation to produce some kind of summary information about our remaining data.

## Aggregations (`COUNT`, `SUM`, `AVG`)

Once we've decided how to group our data, we can then perform aggregations on the remaining columns.

These are things like counting the number of rows per group, summing a particular value across the group, or averaging information within the group.

To start, let's find the number of sales _per_ location.

Since each record in our `sales` table is one sale, the number of sales per location would be **the number of rows within each location group.**

To do this we'll use the aggregate function `COUNT()` to count the number of rows within each group:

```sql
SELECT
  location,
  COUNT(*) AS number_of_sales
FROM sales
GROUP BY location;

```

We use `COUNT(*)` which counts all of the input rows for a group.

(`COUNT()` also works with expressions, but it has slightly different behavior.)

Here's how the database executes this query:

* `FROM sales` — First, retrieve all of the records from the `sales` table
* `GROUP BY location` — Next, determine the unique `location` groups
* `SELECT ...` — Finally, select the location name and the count of the number of rows in that group

We also give this count of rows an alias using `AS number_of_sales` to make the output more readable. It looks like this:

```
  location  | number_of_sales
------------+-----------------
 1st Street |               2
 HQ         |               4
 Downtown   |               2
(3 rows)

```

The _1st Street_ location has two sales, _HQ_ has four, and _Downtown_ has two.

Here we can see how we've taken the remaining column data from our eight independent rows and distilled them into useful summary information for each location: the number of sales.

### `SUM`

In a similar way, instead of counting the number of rows in a group, we could sum information within the group—like the total amount of money earned from those locations.

To do this we'll use the `SUM()` function:

```sql
SELECT
  location,
  SUM(price) AS total_revenue
FROM sales
GROUP BY location;

```

Instead of counting the number of rows in each group we sum the dollar amount of each sale, and this shows us the total revenue per location:

```
  location  | total_revenue
------------+---------------
 1st Street |             5
 HQ         |             9
 Downtown   |             5
(3 rows)

```

### Average (`AVG`)

Finding the average sale price per location just means swapping out the `SUM()` function for the `AVG()` function:

```sql
SELECT
  location,
  AVG(price) AS average_revenue_per_sale
FROM sales
GROUP BY location;

```

## Working with multiple groups

So far we've been working with just one group: location.

What if we wanted to sub-divide that group even further?

Similar to the _"birth countries and eye color"_ scenario we started with, what if we wanted to find the number of sales **per product per location?**

To do this all we need to do is add the second grouping condition to our `GROUP BY` statement:

```sql
SELECT ...
FROM sales
GROUP BY location, product;
```

By adding a second column in our `GROUP BY` we further sub-divide our location groups into location groups _per product._

Because we're now also grouping by the `product` column, we can now return it in our `SELECT`!

(I'm going to throw some `ORDER BY` clauses on these queries to make the output easier to read.)

```sql
SELECT
  location,
  product
FROM sales
GROUP BY location, product
ORDER BY location, product;

```

Looking at the result of our new grouping, we can see our unique location/product combinations:

```
  location  | product
------------+---------
 1st Street | Bagel
 1st Street | Coffee
 Downtown   | Bagel
 Downtown   | Coffee
 HQ         | Bagel
 HQ         | Coffee
(6 rows)

```

Now that we have our groups, what do we want to do with the rest of our column data?

Well, we can find the number of sales _per product per location_ using the same aggregate functions as before:

```sql
SELECT
  location,
  product,
  COUNT(*) AS number_of_sales
FROM sales
GROUP BY location, product
ORDER BY location, product;

```

```
  location  | product | number_of_sales
------------+---------+-----------------
 1st Street | Bagel   |               1
 1st Street | Coffee  |               1
 Downtown   | Bagel   |               1
 Downtown   | Coffee  |               1
 HQ         | Bagel   |               2
 HQ         | Coffee  |               2
(6 rows)

```

> As an _Exercise For The Reader™:_ find the total revenue (sum) of each product per location.

## Using functions in the `GROUP BY`

Next, let's try to find the total number of sales **per day**.

If we follow a similar pattern as we did with our locations and group by our `sold_at` column...

```sql
SELECT
  sold_at,
  COUNT(*) AS sales_per_day
FROM sales
GROUP BY sold_at
ORDER BY sold_at;

```

...we might expect to have each group be each unique day—but instead we see this:

```
          sold_at           | sales_per_day
----------------------------+---------------
 2020-08-29 08:42:33.085995 |             1
 2020-08-29 09:42:33.085995 |             1
 2020-08-30 08:42:33.085995 |             1
 2020-08-30 09:42:33.085995 |             1
 2020-08-31 09:42:33.085995 |             1
 2020-09-01 07:42:33.085995 |             1
 2020-09-01 08:42:33.085995 |             1
 2020-09-01 09:42:33.085995 |             1
(8 rows)

```

It looks like our data isn't grouped at all—we get each row back individually.

But, our data _is actually grouped!_ The problem is each row's `sold_at` is a unique value—so every row gets its own group!

The `GROUP BY` is working correctly, but this is not the output we want.

The culprit is the unique hour/minute/second information of the timestamp. 

Each of these timestamps differ by hours, minutes, or seconds—so they are each placed in their own group.

We need to convert each of these date and time values into just a date:

* `2020-09-01 08:42:33.085995` => `2020-09-01`
* `2020-09-01 09:42:33.085995` => `2020-09-01`

Converted to a date, all of the timestamps on the same day will return the same date value—and will therefore be placed into the same group.

To do this, we'll cast the `sold_at` timestamp value to a date:

```sql
SELECT
  sold_at::DATE AS date,
  COUNT(*) AS sales_per_day
FROM sales
GROUP BY sold_at::DATE
ORDER BY sold_at::DATE;

```

In our `GROUP BY` clause we use `::DATE` to truncate the timestamp portion down to the "day." This effectively chops off the hours/minutes/seconds of the timestamp and just returns the day.

In our `SELECT`, we also return this same expression and give it an alias to pretty up the output.

For the same reason we couldn't return `product` without grouping by it or performing some kind of aggregation on it, the database won't let us return just `sold_at`—everything in the `SELECT` must either be in the `GROUP BY` or some kind of aggregate on the resulting groups.

The result is the _sales per day_ that we originally wanted to see:

```sql
    date    | sales_per_day
------------+---------------
 2020-08-29 |             2
 2020-08-30 |             2
 2020-08-31 |             1
 2020-09-01 |             3
(4 rows)

```

## Filtering groups with `HAVING`

Next let's look at how to filter our grouped rows.

To do this, let's try to find days where we had _more than one sale._

Without grouping, we would normally filter our rows by using a `WHERE` clause. For example:

```sql
SELECT *
FROM sales
WHERE product = 'Coffee';

```

With our groups, we may want to do something like this to filter our groups based on the count of rows...

```sql
SELECT
  sold_at::DATE AS date,
  COUNT(*) AS sales_per_day
FROM sales
WHERE COUNT(*) > 1      -- filter the groups?
GROUP BY sold_at::DATE;

```

Unfortunately, this doesn't work and we receive this error: 

`ERROR:  aggregate functions are not allowed in WHERE`

Aggregate functions are not allowed in the `WHERE` clause because the `WHERE` clause is evaluated **before** the `GROUP BY` clause—there aren't any groups yet to perform calculations on.

But, there is a type of clause that allows us to filter, perform aggregations, and it is evaluated _after_ the `GROUP BY` clause: the `HAVING` clause.

**The `HAVING` clause is like a `WHERE` clause for your groups.**

To find days where we had more than one sale, we can add a `HAVING` clause that checks the count of rows in the group:

```sql
SELECT
  sold_at::DATE AS date,
  COUNT(*) AS sales_per_day
FROM sales
GROUP BY sold_at::DATE
HAVING COUNT(*) > 1;

```

This `HAVING` clause filters out any rows where the count of rows in that group is not greater than one, and we see that in our result set:

```
    date    | sales_per_day
------------+---------------
 2020-09-01 |             3
 2020-08-29 |             2
 2020-08-30 |             2
(3 rows)

```

Just for the sake of completeness, here's the order of execution for all parts of a SQL statement:

* `FROM` — Retrieve all of the rows from the `FROM` table
* `JOIN` — Perform any joins
* `WHERE` — Filter rows
* `GROUP BY` - Form groups
* `HAVING` - Filter groups
* `SELECT` - Select the data to return
* `ORDER BY` - Order the output rows
* `LIMIT` - Return a certain number of rows

## Aggregates with implicit grouping

The last topic we'll look at is aggregations that can be performed without a `GROUP BY`—or maybe better said they have an _implicit_ _grouping._

These aggregations are useful in scenarios where you want to find one particular aggregate from a table—like the total amount of revenue or the greatest or least value of a column.

For example, we could find the total revenue across _all locations_ by just selecting the sum from the entire table:

```sql
SELECT SUM(price)
FROM sales;

```

```
 sum
-----
  19
(1 row)

```

So far we've done $19 of sales across all locations (_hooray!_).

Another useful thing we could query is the _first_ or _last_ of something.

For example, what is the date of our first sale? 

To find this we just use the `MIN()` function:

```sql
SELECT MIN(sold_at)::DATE AS first_sale
FROM sales;

```

```
 first_sale
------------
 2020-08-29
(1 row)

```

(To find the date of the last sale just substitute `MAX()`for `MIN()`.)

### Using `MIN` / `MAX`

While these simple queries can be useful as a standalone query, they're often parts of filters for larger queries.

For example, let's try to find the total sales for the _last day_ that we had sales.

One way we could write that query would be like this:

```sql
SELECT
  SUM(price)
FROM sales
WHERE sold_at::DATE = '2020-09-01';

```

This query works, but we've obviously hardcoded the date of `2020-09-01`. 

_09/01/2020_ may be the last date we had a sale, but it's not always going to be that date. We need a dynamic solution.

This can be achieved by combining this query with the `MAX()` function in a subquery:

```sql
SELECT
  SUM(price)
FROM sales
WHERE sold_at::DATE = (
  SELECT MAX(sold_at::DATE)
  FROM sales
);

```

In our `WHERE` clause we find the largest date in our table using a subquery: `SELECT MAX(sold_at::DATE) FROM sales`. 

Then, we use this max date as the value we filter the table on, and sum the price of each sale.

### Implicit grouping

I say that these are implicit groupings because if we try to select an aggregate value with a non-aggregated column like this...

```sql
SELECT
  SUM(price),
  location
FROM sales;

```

...we get our familiar error:

```
ERROR:  column "sales.location" must appear in the GROUP BY clause or be used in an aggregate function

```

## `GROUP BY` is a tool

As with many other topics in software development, `GROUP BY` is a tool.

There are many ways to write and re-write these queries using combinations of `GROUP BY`, aggregate functions, or other tools like `DISTINCT`, `ORDER BY`, and `LIMIT`.

Understanding and working with `GROUP BY`'s will take a little bit of practice, but once you have it down you'll find an entirely new batch of problems are now solvable to you! 

If you liked this post, you can [follow me on twitter](https://twitter.com/johnmosesman) where I talk about database things and how to succeed in a career as a developer.

Thanks for reading!

John

