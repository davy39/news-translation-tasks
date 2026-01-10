---
title: How to Use MySQL Common Table Expressions – with Example Queries
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-02-20T17:52:56.000Z'
originalURL: https://freecodecamp.org/news/mysql-common-table-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Common-dining-table-eettafel-Esstisch-04-1280x854.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
seo_title: null
seo_desc: "In your day to day job as a Software Engineer or Database Administrator,\
  \ you'll likely have to write long complex queries, often with some subqueries.\
  \ \nThese queries over time become less performant, difficult to read and understand,\
  \ and even more di..."
---

In your day to day job as a Software Engineer or Database Administrator, you'll likely have to write long complex queries, often with some subqueries. 

These queries over time become less performant, difficult to read and understand, and even more difficult to manage. And no one wants to do the hard job of refactoring them, so they just live on. 

Or you have probably had to fetch similar data based on a set of data or parameters. To achieve this, you write many similar, sometimes exactly identical subqueries and bring them together using the UNION keyword. 

Well, you can make your life easier and solve these problems efficiently using a Common Table Expression.

> A common table expression (CTE) is a named temporary result set that exists within the scope of a single statement and that can be referred to later within that statement, possibly multiple times. – [MySQL.com](https://dev.mysql.com/doc/refman/8.0/en/with.html)

Using a Common Table Expression, you can write more readable and more performant queries very easily. It's actually easier than it is to write multiple subqueries that could make your queries unreadable and less performant.

You'll primarily use a common table expression for two reasons:

* To write queries without using subqueries (or using fewer subqueries)
* To write recursive functions

In this tutorial, I'll show you how to write your own common table expressions.

## How to Create a Common Table Expression

You can create a Common Table Expression (CTE) using the `WITH` keyword. You can specify multiple common table expressions at the same time by comma-separating the queries making up each common table expression.

The general shape of a Common Table Expression is like so:

```sql
WITH cte_name AS (query)

-- Multiple CTEs
WITH
    cte_name1 AS (
        -- Query here
    ),
    cte_name2 AS (
        -- Query here
    )
```

The `WITH` keyword is followed by the CTE name. After the name, you introduce the query to be run in the CTE using the `AS` keyword. You need to enclose the query must in parentheses. The CTE cannot be followed by a semicolon like other SQL queries. Instead it is followed by another query that uses it.

After creating a CTE, you can easily use the result of the queries run in the CTE by referencing the CTE in other queries, other CTEs, or even in itself.

### CTE Example

If you have a table of world_cup players, for example, you can create a CTE like this:

```sql
WITH
    barca_players AS (
        SELECT
            id,
            player_name,
            nationality,
            position,
            TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
        FROM
            wc_players
        WHERE
            club = 'Barcelona'
    )
SELECT
    *
FROM
    barca_players;
```

Here, we've created a CTE named `barca_players`. This CTE will return the name, position, age, and nationality of every Barcelona player that was at the world cup. It contains the subquery:

```sql
SELECT
    id,
    player_name,
    nationality,
    position,
    TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
FROM
    wc_players
WHERE
    club = 'Barcelona';
```

This subquery is what produces the CTE result. Next, it is followed by a query that uses this result. You can see the result of selecting every record in the CTE below.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-17-at-22.59.25.png)

You can also select only specific fields from the CTE, for example:

```sql
WITH
    barca_players AS (
        SELECT
            id,
            player_name,
            nationality,
            position,
            TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
        FROM
            wc_players
        WHERE
            club = 'Barcelona'
    )
SELECT
    player_name,
    position
FROM
    barca_players;
```

This query is almost the same as the first one, except that it selects only the player names and positions from the list.

## How to Use Common Table Expressions With Parameters

You can also pass arguments to the CTE. These are aliases you can use for referencing columns of the query results. The number of parameters passed into the CTE must be the same as the number of columns being selected in its subquery. This is because the columns get matched to the aliases one by one, one after the other.

For example, in the `barca_players` CTE created above, you can decide to refer to the `nationality` column as `country`, and `position` as `role`:

```sql
WITH
    barca_players (id, player_name, country, role, age) AS (
        SELECT
            id,
            player_name,
            nationality,
            position,
            TIMESTAMPDIFF (YEAR, player_dob, CURRENT_DATE) age
        FROM
            wc_players
        WHERE
            club = 'Barcelona'
    )
SELECT
    player_name,
    role
FROM
    barca_players;
```

Notice that in the CTE subquery, you still use the correct column names. But in the outer `SELECT` query, you use the new aliases specified as parameters to the CTE.

## Recursive Common Table Expressions

When you reference a Common Table Expression within itself, it becomes a recursive Common Table Expression. 

A Recursive Common Table Expression, as the name implies, is a common table expression that can run a subquery multiple times, as long as a condition is met. It iterates continuously until it reaches a break point, when the condition stops being true.

To define a recursive CTE, the `RECURSIVE` keyword must be in its name. Without this keyword, MySQL throws an error.

For example, you can write a common table expression that prints numbers 1 to 10 and their squares like this:

```sql
WITH RECURSIVE
    numbers_list (n, square) AS (
        SELECT
            1,
            1
        UNION ALL
        SELECT
            n + 1,
            (n + 1) * (n + 1)
        FROM
            numbers_list
        WHERE
            n < 10
    )
SELECT
    *
FROM
    numbers_list;
```

Let's examine what is happening here:

In the first two lines, the recursive common table expression is defined with two parameters, one representing the column for the number, and the other representing the column for the square:

```sql
WITH RECURSIVE
    numbers_list (n, square) AS (
```

Next, the subquery. The subquery is in two parts, joined by the `UNION ALL` keyword to form one. You can also join these subqueries by the `UNION` keyword if you don't need duplicate records. 

The first part of the subquery is a key part of recursive common table expressions. It is the base query, the first result set, the initial iteration. This query is the starting point of all iterations. 

In this example, it is static, as no records are being fetched.

```sql
SELECT
    1,
    1
```

After this first query, the result table has one row, and looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-17-at-23.55.27.png)

The second part of the subquery is where the iteration really happens. 

In this query, the CTE is referenced within itself, and its columns can be used. When a column name is mentioned, the most recent value of that column is taken. 

So at the start of the iteration, `n` is 1 and `square` is also 1. That means, `n + 1` is 2, and `(n + 1) * (n + 1)` is 2 *2 which is 4. 2 and 4 get added to the result table and then become the most recent values in the table. `n` becomes 2, and `square` becomes `4`. 

This continues until the condition in the `WHERE` keyword is stops being true.

The `WHERE` keyword in the query specifies the breakpoint of the CTE. Until the condition specified is met, the query keeps getting run. In this case, after every iteration, the query checks if `n` is less than 10.

If a condition that will always evaluate to true is set, then this creates an endless loop and you get an error like `Recursive query aborted after 1001 iterations. Try increasing @@cte_max_recursion_depth to a larger value.`

```sql
SELECT
    n + 1,
    (n + 1) * (n + 1)
FROM
    numbers_list
WHERE
    n < 10
```

Now you might think, "If the condition checks for `n < 10` , how come 10 is still in the final table?". 

Well, the reason is because in SQL, the `WHERE` keyword part of a query is evaluated first before other parts. So, when `n = 9` is the last row, the query runs once more, and before insertion or anything, it checks if 9 is less than 10. Since 9 is less than 10, it adds `n + 1` which is 10 to the list. Then on the next iteration, 10 is the most recent record and it is not less than itself, so the loop ends. 

Keep in mind that a Recursive Common Table Expression consists of a recursive `SELECT` query, and a non-recursive `SELECT` query.

### Simple Recursive Common Table Expression Rules

* You can't use the `GROUP BY` keyword. This is because you can only group a collection, but in a recursive common table expression, records are handled and evaluated individually. Other keywords like `ORDER BY`, `DISTINCT`, and aggregate functions like `SUM` cannot be used either.
* You can't use window functions.

These rules apply to the recursive part of a recursive common table expression.

### Use Cases for Recursive CTEs

#### Fibonacci Sequence

> The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1, although some authors start the sequence from 1 and 1 or sometimes from 1 and 2. ([source](https://en.wikipedia.org/wiki/Fibonacci_number))

You can easily generate a Fibonacci sequence of any length using a recursive common table expression. For example, here's a query that will get the first 20 numbers of a Fibonacci sequence starting from 0 and 1.

```sql
WITH RECURSIVE
    fibonacci (n, fib_n, next_fib_n) AS (
        /*
        * n - Number of iterations
        * fib_n - Currennt Fibonnaci number. Starts at 0
        * next_fib_n - Next Fibonnaci number. Starts at 1
        */
        SELECT
            1,
            0,
            1
        UNION ALL
        SELECT
            n + 1,
            next_fib_n,
            fib_n + next_fib_n
        FROM
            fibonacci
        WHERE
            n < 20
    )
SELECT
    *
FROM
    fibonacci;
```

#### Hierarchical Data Traversal

In many application databases, you will find that hierarchical data is stored in the same table.

For example, a `categories` table will usually contain main categories and sub-categories referencing their parent category. An `employees` table will contain regular employees with their `manager_id`, as well as their managers or supervisors, because they are also employees.

If you had a `categories` table like this, with 4 records, 1 main category, and a chain of  sub-categories:

```sql
CREATE TABLE
    categories (
        id int,
        cat_name varchar(100),
        parent_category_id int DEFAULT NULL
    );

INSERT INTO
    categories
VALUES
    (1, 'Mens', NULL),
    (2, 'Tops', 1),
    (3, 'Jerseys', 2),
    (4, 'England', 3);
```

You can fetch each category, with its parent category attached easily like this:

```sql
WITH RECURSIVE
    category_tree AS (
        SELECT
            id,
            cat_name,
            parent_category_id,
            cat_name AS full_name
        FROM
            categories
        WHERE
            parent_category_id IS NULL
        UNION ALL
        SELECT
            c.id,
            c.cat_name,
            c.parent_category_id,
            CONCAT (ct.full_name, ' > ', c.cat_name)
        FROM
            categories c
            JOIN category_tree ct ON c.parent_category_id = ct.id
    )
SELECT
    full_name
FROM
    category_tree;
```

In this example, the base query selects the root category, where `parent_category_id IS NULL`. Then it goes on to look for a category where the `parent_category_id` is the `id` of the current category by using a `JOIN`. It repeats this until it gets to the final category. The result of this query is the following:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-18-at-01.19.10.png)

## **Summary**

I hope you now understand how to use MySQL Common Table Expressions, their variations (regular and recursive), and when to use them so you can write better queries. You can find more about common table expressions in the docs [here](https://dev.mysql.com/doc/refman/8.0/en/with.html).

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

