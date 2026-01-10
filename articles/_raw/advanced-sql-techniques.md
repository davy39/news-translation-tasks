---
title: Advanced SQL Techniques for Complex Queries
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-21T17:01:39.000Z'
originalURL: https://freecodecamp.org/news/advanced-sql-techniques
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/GBL.JPG
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Structured Query Language or SQL is an effective tool for managing and
  modifying data that is stored in databases.

  The SELECT, INSERT, UPDATE, and DELETE SQL commands are suitable for many common
  use cases. But sometimes, more sophisticated technique...'
---

Structured Query Language or SQL is an effective tool for managing and modifying data that is stored in databases.

The SELECT, INSERT, UPDATE, and DELETE SQL commands are suitable for many common use cases. But sometimes, more sophisticated techniques can help you perform out more complex queries and analyses with improved accuracy and efficiency.

In this tutorial, we will discuss some of the most popular advanced SQL techniques and provide real-world applications for each.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/tenor.gif align="left")

## Window Functions

You can use window functions to perform calculations on a "window" of data that is defined by a particular subset of rows in a table. This can be helpful when you're doing things like calculating running totals, sorting rows according to a particular criterion, or locating outliers in a dataset.

Let's begin by looking at an interactive example of how to create running totals using window functions. Let's say you want to determine the cumulative sales for each month for a business. You have a table of sales data that shows the total sales for each month.

Here's some example code you can run in the SQL console to perform this calculation:

```sql
SELECT month, sales, SUM(sales) OVER (ORDER BY month) AS cumulative_sales
FROM sales_data;
```

This SQL query is used to analyze sales data over time. It selects three columns from the `sales_data` table: `month`, `sales`, and `cumulative_sales`.

The `month` column contains the month in which the sales were made, while the `sales` column contains the total sales for that month. The `cumulative_sales` column is calculated using the `SUM()` function and the `OVER()` clause, which sums up all the `sales` values up to and including the current month.

So, the `cumulative_sales` column shows how the sales accumulate over time. By looking at this column, you can see the progression of sales from month to month and identify periods of high or low sales.

Overall, this SQL query is useful for identifying sales trends and patterns, which can help businesses make informed decisions about their operations and strategies.

## Common Table Expressions

You can create a temporary named result set that you can use in subsequent queries within the same session using Common Table Expressions (CTEs). This can be helpful for disassembling complicated queries into simpler, easier-to-handle parts.

Let's now try an interactive demonstration of how to utilize common table expressions (CTEs) to divide a challenging query into smaller, easier-to-handle parts.

Consider a scenario in which you want to determine the average age of customers who have bought a particular product. You have a table of customer data including their name, age, and the products they have purchased.

Here's some example code you can run in the SQL console to perform this calculation using a CTE:

```sql
WITH product_customers AS (
  SELECT name, age
  FROM customer_data
  WHERE product = 'widget'
)
SELECT AVG(age) AS avg_age
FROM product_customers;
```

This query uses a Common Table Expression (CTE), which is a temporary named result set that can be referenced within a single query.

The CTE is named `product_customers`. It's created using a `SELECT` statement that retrieves the `name` and `age` columns from the `customer_data` table for customers who have purchased the product 'widget'.

The second part of the query selects the average age of the customers who have purchased the product 'widget', using the `AVG()` function. The `AS` keyword gives the resulting column a name of `avg_age`.

Overall, this query is useful for analyzing the demographic characteristics of customers who have purchased a particular product, in this case, the 'widget'. By calculating the average age of these customers, businesses can gain insights into the preferences and behaviors of their target audience and use this information to inform their marketing and product development strategies.

### Recursive Queries

Recursive queries allow you to perform hierarchical or iterative calculations on data that is structured in a tree-like or graph-like format. This can be useful for tasks like calculating the total cost of a series of interconnected transactions or identifying the shortest path between two nodes in a network.

Now let's try an interactive example of how to use recursive queries to perform hierarchical calculations on data.

Imagine you have a table of employee data that includes each employee's name, job title, and the name of their supervisor. You want to find the total number of employees in each job category.

Here's some example code you can run in the SQL console to perform this calculation using a recursive CTE:

```sql
WITH RECURSIVE job_categories AS (
  SELECT job_title, COUNT(*) AS employee_count
  FROM employee_data
  GROUP BY job_title
  UNION ALL
  SELECT e.job_title, COUNT(*) AS employee_count
  FROM employee_data e
  JOIN job_categories jc ON e.supervisor = jc.job_title
  GROUP BY e.job_title
)
SELECT job_title, SUM(employee_count) AS total_employees
FROM job_categories
GROUP BY job_title;
```

This query uses a Common Table Expression (CTE) with a recursive component, which allows it to traverse hierarchical data structures.

The CTE is named `job_categories` and is created using two `SELECT` statements combined with the `UNION ALL` operator.

The first part of the query selects the `job_title` column and calculates the number of employees in each job category by counting the number of rows in the `employee_data` table that have the same `job_title`.

The second part of the query is where the recursion happens. It selects the `job_title` column and calculates the number of employees in each job category. It does this by joining the `employee_data` table with the `job_categories` CTE on the condition that the employee's supervisor is in the `job_title` column of the CTE. This allows the query to traverse the hierarchy of job categories to calculate the total number of employees in each category.

Finally, the query selects the `job_title` and `employee_count` columns from the `job_categories` CTE and uses the `SUM()` function to calculate the total number of employees in each job category. The `GROUP BY` clause is used to group the results by job title.

Overall, this query is useful for analyzing the hierarchical structure of employee data and calculating aggregate statistics for each level of the hierarchy. By understanding the distribution of employees across job categories, businesses can identify areas for improvement and make data-driven decisions about hiring, promotions, and resource allocation.

## Conclusion

Advanced SQL techniques like window functions, CTEs, and recursive queries can help you perform complex data analyses and manipulations with greater precision and efficiency.

By understanding these techniques and their real-world applications, you can take full advantage of SQL's capabilities and become a more effective data manager.
