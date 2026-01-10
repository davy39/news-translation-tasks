---
title: SQL Joins – LEFT Join, RIGHT Join, and INNER Join Explained
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-01-10T18:23:24.000Z'
originalURL: https://freecodecamp.org/news/understanding-sql-joins
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/JOIN-s.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'SQL is a programming language we use to interact with relational databases.
  SQL databases contain tables, which contain rows of data. These tables usually contain
  similar or related data.

  In an office management web application database, you would ha...'
---

SQL is a programming language we use to interact with relational databases. SQL databases contain tables, which contain rows of data. These tables usually contain similar or related data.

In an office management web application database, you would have tables for `employees`, their `departments`, their `managers`, the `projects` they work on, and so on depending on the structure of your application. 

In the `employees` table, you would find data like the employee ID, name, salary, department ID (used to link the employee to the department), and other fields that match your needs. The other tables would also contain data for their specific entities.

## **What Are Joins?**

If you ever need to bring multiple tables in your database together to access the data, you use a JOIN.

Joins let you fetch data that is scattered across tables. For example, using the database tables that we'll create in a moment, we'll be able to get all the details of an employee, along with their manager name, and department they're working in by using a join. 

A join lets you use a single query to achieve this. You use a join because you can only get this data by bringing data from the `employees` table, `departments` table, and `projects` table together. In simple terms, you would be JOIN-ing these tables together.

 To perform a join, you use the **JOIN** keyword. And we'll see how it works in this tutorial.

### Prerequisites:

To continue with this tutorial, you should know the basics of insertion and retrieval operations with SQL.

Also, you can setup a demo database that we'll use for this article. The database should have tables like this: 

```sql
CREATE TABLE employees (
    id int,
    emp_name varchar(100),
    salary int,
    dept_id int,
    manager_id int
);

INSERT INTO employees 
VALUES (1, 'Idris', 1000, 1, 1), (2, 'Aweda', 2000, 2, 2), (3, 'Zubair', 3000, 3, 2), (4, 'Young', 4000, 3, 3), (5, 'Babu', 5000, 1, 3), (6, 'John', 1000, 8, 1);

CREATE TABLE departments (
    id int,
    dept_name varchar(100)
);

INSERT INTO departments
VALUES (1, 'Engineering'), (2, 'Product'), (3, 'Marketing'), (4, 'Support');

CREATE TABLE managers (
    id int,
    manager_name varchar(100),
    dept_id int
);

INSERT INTO managers
VALUES (1, 'Doe', 1), (2, 'Jane', 2), (3, 'May', 4);

CREATE TABLE projects (
    id int,
    project_name varchar(100),
    emp_id int
);

INSERT INTO projects
VALUES (1, 'Fintech App', 1), (1, 'Fintech App', 5), (1, 'Fintech App', 6), (2, 'Cooking Website', 1), (2, 'Cooking Website', 2);
```

## **How to Use an Inner Join in SQL**

There are many types of joins in SQL, and each one has a different purpose.

The inner join is the most basic type of join. It is so basic that sometimes, you can omit the JOIN keyword and still perform an inner join. 

For example, say you want to fetch the name of all employees in the organanization, along with the name of their departments. In a situation like this, you need data from both the `employees` table and the `departments` table. A simple join like this would do:

```sql
SELECT e.emp_name, d.dept_name 
FROM employees e, departments d 
WHERE e.dept_id = d.id;
```

So how does this actually work? To start with, take a look at the `FROM` part of the query:

```sql
FROM employees e, departments d
```

Here, data is being fetched from more than one table, and each table is aliased. The alias is very useful for scenarios where both tables have similarly named fields,  like the `id` field both tables have in this case. You would be able to access the different fields easily using the short alias created.

Next, in the `SELECT` part of the query, we also specify the columns we want (and we use the alias to tell which table each value comes from):  

```sql
SELECT e.emp_name, d.dept_name
```

And finally, to ensure only correct values are matched to each other, the `WHERE` part of the query specifies the conditions that have to be met for the data to be joined.

```sql
WHERE e.dept_id = d.id;
```

So for the first employee, the `dept_id` is `1`, so we fetch the department with `id = 1`, and it's name is returned. This happens for as many rows as there are in the employees table.

The result of the query looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-15.45.09.png)
_Result of JOIN query_

Here, notice that the number of employees returned is smaller than the number of employees that actually exist. This is because when you use an INNER JOIN, _you only get records that exist in both tables_. 

That is, the employee with `id = 6` that was not returned has a `dept_it = 8`. Now, this department isn't in the `departments` table, so it wasn't returned.

Another way to achieve this same result would be to actually spell out the JOIN like this:

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON (e.dept_id = d.id);
```

Or use the INNER JOIN like this:

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d
ON (e.dept_id = d.id);
```

These queries return exactly the same result as the first one. But they are more readable as they're explicit. 

In these queries, you're selecting from the `employees` table, then joining the `departments` table to the result. The ON in the query is used to specify the conditions on which to JOIN. It's the same as the WHERE condition in the first query.

### INNER JOIN Use Case

In real applications, you use an INNER JOIN when only records that exist in both tables matter. 

For example, in an inventory management application, you could have a table for `sales`, and another for `products`. Now, the `sales` table will contain `product_id` (a reference to the sold product), along with other details like `sold_at` (when the product was sold) and maybe customer details. 

The `products` table, on the other hand, will have the `name`, `price`, and maybe the `quantity` of every product. 

Now say it's end of the week and you need to do a sales report. You would need to fetch all `sales` records, along with the product name and price to display on a dashboard or export as a CSV of some sort. 

To do this, you would use an INNER JOIN of the `products` table on the `sales` table, because you do not care about products that were not sold – you only want to see every sale that was made, and the name and price of the product that was sold. Every other product will be exempted from this report.

## **How to Use a Left Join in SQL**

In another scenario, you might want to fetch all the employee names and their department names, but this time without leaving any employee or department name out. Here, you'd you use a LEFT JOIN. 

In a LEFT JOIN, _every record from the table on the left, the base table, will be returned_. Then values from the right table, the table being joined, will be added where they exist.

The LEFT JOIN is also known as LEFT OUTER JOIN and you can use them interchangeably.

So to fetch all employee and department names, you can modify the previous query to use LEFT JOIN, like this:

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON (e.dept_id = d.id);
```

The result of this query looks like this now:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-15.55.10.png)
_Result of LEFT JOIN_

Now, employee with `id = 6` and `dept_id = 8` is returned, with the department name being set as NULL because there is no department with `id = 8`.

### LEFT JOIN Use Case

In real applications, you use a LEFT JOIN when there's a primary, always existing entity that can be related to another entity that doesn't always exist. 

An easy use case would be in a multi-vendor ecommerce application where after a user signs up, they can set up a store and add products to the store. 

A user, on signing up, doesn't automatically have a store until they create it. So if you try to view all users, with their store details, you would use a LEFT JOIN of the `stores` table on the `users` table. This is because every record in the `users` table is important, store or no store. 

When the user has a store set up, the store details are returned, and if otherwise, NULL is returned. But, you wouldn't be losing any existing data.

## **How to Use a Right Join in SQL**

The RIGHT JOIN works like the opposite of the LEFT JOIN. In a RIGHT JOIN, every record from the table on the right, the table being joined, will be returned. Then values from the left table, the base table, will be added where they exist.

The RIGHT JOIN is also known as the RIGHT OUTER JOIN and you can use them interchangeably.

An example would be to modify the previous query to use a RIGHT JOIN instead of a LEFT JOIN, like this:

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
RIGHT JOIN departments d
ON (e.dept_id = d.id);
```

Now, your result looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-16.02.08.png)
_Result of RIGHT JOIN_

Now, every department in the `departments` table was returned. And employees in those departments were returned too. For the last row, there is no employee with `dept_id = 4`, which is why the NULL value gets returned.

### RIGHT JOIN Use Case

The RIGHT JOIN works exactly as the LEFT JOIN works in real applications. The difference between them comes from the level of importance of the tables to be joined. 

The LEFT JOIN is more commonly used because you very likely will write your query from left to right, listing tables in that order of importance too. Otherwise, the RIGHT JOIN works exactly as the LEFT JOIN.

### How to Combine JOINS in SQL

So far, we've only joined one table to another. But, you can actually join as many tables as you like by using any or all of these joins together as you like. 

For example, say you want to fetch the names of all employees, with their department names, manager names, and projects names. You would have to join the `employees` table to the `departments` table, the `managers` table, and the `projects` table. You can achieve this using this query:

```sql
SELECT e.emp_name, d.dept_name, m.manager_name, p.project_name
FROM employees e
LEFT JOIN departments d
ON (e.dept_id = d.id)
LEFT JOIN managers m
ON (e.manager_id = m.id)
LEFT JOIN projects p
ON (e.id = p.emp_id);
```

In this query, start from the `employees` table as a base table. Then you LEFT JOIN the `departments` table. You also LEFT JOIN the `managers` table, and finally, the `projects` table.

The result of this query will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-19.30.29.png)
_Result of general JOIN query_

The reason for using a LEFT JOIN here is because you have to fetch ALL employees. You could use an INNER JOIN in place of the LEFT JOIN in the `managers` table because all employees have a `manager_id` that actually exists in the `managers` table. But to be safe, you can just use the LEFT JOIN.

## **How to Use a Cross Join in SQL**

This is also known as a CARTESIAN JOIN. It returns every record from both tables in a multiplication-like manner. It returns every possible combination of rows from both tables. It doesn't need a JOIN condition like the other JOINs. 

For example, if you do a CROSS JOIN between tables `employees` and `departments`, your result will look like this:

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
CROSS JOIN departments d;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-20.19.24.png)
_CROSS JOIN of `employees` and `departments` tables._

Here you have 24 rows, which is a product of the number of rows in the `employees` table, 6, and the number of rows in the `departments` table, 4. The records were returned so that for every record in the `employees` table, it is mapped to a record in the `departments` table.

### CROSS JOIN Use Case

A common use case of CROSS JOIN would be in an ecommerce application where it is possible to have size or color variations of all products. If you ever need to fetch a list of all products in different sizes, like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-10-at-13.13.55.png)
_Result of a basic CROSS JOIN_

This result was gotten from CROSS JOINing a `sizes` table that contains an `id` for each size, a string `size` that can be either 'Small', 'Medium', or 'Large' and another field called `ratio` to affect how this size affects the product price. So, for every product, it is mapped to a size, and the price is calculated.

```sql
SELECT 
  p.product_name, 
  ROUND(p.price * s.ratio, 2) as price, 
  s.size 
FROM products p 
CROSS JOIN sizes s;
```

## **How to Use a Self Join in SQL**

As the name implies, is when you try _to join a table to itself._ There is no self JOIN keyword.

Take this new `categories` table, for example. This table contains both main categories and sub-categories. If you ever have to fetch the categories and their sub-categories, you can use a SELF JOIN.

```sql
CREATE TABLE categories (
    id int,
    cat_name varchar(100),
    parent_category_id int DEFAULT NULL
);

INSERT INTO categories 
VALUES (1, 'Ladies', NULL), (2, 'Mens', NULL), (3, 'Lingeries', 1), (4, 'Shoes', 2);
```

```sql
SELECT cat.cat_name, parent_cat.cat_name AS parent 
FROM categories cat
JOIN categories parent_cat 
ON cat.parent_category_id = parent_cat.id;
```

Here, see how the table was referenced twice. Be careful with the alias as it's important in differentiating both instances. The result of this query looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-07-at-21.40.25.png)
_Result of simple Self JOIN on `categories` table_

### SELF JOIN Use Case

In many applications, you find hierarchical data stored in a single table. Like the category and sub-category as shown in the previous example. Or as in employee and manager, because they're both employees of the company. 

In case of the latter, the table will have fields such as `id`, `name`, `manager_id` (this is basically the `id` of another employee). Let's say you want to write a query where you have to fetch a list of managers and the number of their employees. Given that these managers are also employees, you only have one table to fetch from, the `employees` table. To do this fetch, do a SELF JOIN of the `employees` table on the `employees` table like this:

```sql
SELECT e2.name AS supervisor, COUNT(e1.name) AS number_of_employees
FROM employee e1
JOIN employee e2
ON e1.manager_id = e2.id
GROUP BY e2.name;
```

This would correctly return the managers and the number of employees working under them.

## **Summary**

I hope you now understand SQL JOINs, the different types, and when to use them so you can write better queries. 

All the JOINs here work with MySQL. There are other JOINs like FULL OUTER JOIN and NATURAL JOIN that we didn't discuss, but you can look into them yourself if you like.

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

