---
title: How to Use MySQL Stored Procedures to Simplify Database Operations
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-06-12T22:05:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-simplify-database-operations-using-mysql-stored-procedures
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/How-to-use-Mysql-procedure-1.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
seo_title: null
seo_desc: "In the realm of database management, MySQL has emerged as one of the most\
  \ popular and reliable choices. \nMySQL not only offers robust data storage capabilities\
  \ but also provides a powerful feature called \"procedures\" that allows developers\
  \ to streaml..."
---

In the realm of database management, MySQL has emerged as one of the most popular and reliable choices. 

MySQL not only offers robust data storage capabilities but also provides a powerful feature called "procedures" that allows developers to streamline complex database operations. 

In this tutorial, we will delve into the concept of MySQL procedures and explore their benefits. Then I'll provide a step-by-step guide on how to use them effectively.

## What are SQL Procedures?

SQL procedures are a set of SQL statements grouped together to form a logical unit of work. They are similar to functions or methods in programming languages, enabling you to encapsulate complex queries and operations into a single reusable entity. 

Procedures enhance code modularity, readability, and maintainability, making it easier to manage and execute repetitive or intricate database tasks.

## When to Use Stored Procedures

Let's consider an e-commerce website, where we have the functionality to generate sales reporting. We have a table called `sales` that we'll be working with for this example.

Generating sales reports in real time can be resource-intensive, especially when dealing with large datasets. By creating stored procedures that aggregate and summarize sales data, we can optimize the reporting process. 

These procedures can calculate metrics like total sales, top-selling products, or revenue by category, making it easier to retrieve valuable insights quickly and efficiently.

Here's the schema of sales table:

<table class=""><thead><tr><th role="textbox" aria-multiline="true" aria-label="Header cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Column</th><th role="textbox" aria-multiline="true" aria-label="Header cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Type</th></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">sale_id</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">int</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">customer_id</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">int</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">saled_date</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">datetime</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">total_amount</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">decimal</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">status</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">varchar(50)</td></tr></thead></table>

To illustrate a simple example, let's consider `sales` table is populated with 1 million rows of mock data.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-108.png)
_Mock data for sales table_

```
select count(*) from sales;
```

The goal is to get sales reports for a particular period of time.

```
CREATE PROCEDURE GenerateSalesReport (
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
    SELECT DATE_FORMAT(order_date, '%Y-%m-%d') AS Date,
           COUNT(order_id) AS TotalOrders,
           SUM(total_amount) AS TotalSales
    FROM orders
    WHERE order_date BETWEEN start_date AND end_date
    GROUP BY DATE_FORMAT(order_date, '%Y-%m-%d');
END
```

The example stored procedure `GenerateSalesReport` takes two input parameters: `start_date` and `end_date`. These define the date range for the sales report. 

The procedure selects the order date, counts the number of orders, and calculates the total sales amount within the specified date range. The result is grouped by the date, using the `DATE_FORMAT` function to display it in the desired format.

Now, you might have a question:

> "Can't we achieve the same outcome using a simple query instead of creating a stored procedure?"

Well. It's true that using a simple query is a viable option. But there are several compelling reasons to consider utilizing a stored procedure.

Here are few reasons that feels promising to use stored procedures at some places. 

1. A stored procedure offers the advantage of code reusability. By encapsulating the query logic within a stored procedure, we can reuse it multiple times without duplicating the code.
2. Instead of rewriting the same query in different parts of the application, we can simply call the stored procedure whenever needed, streamlining the codebase and making it easier to manage and update.
3. Using a stored procedure can lead to improved performance in certain scenarios. When a stored procedure is executed, the database server can optimize the execution plan and cache it for subsequent invocations. This optimization can result in faster execution times, as the database engine leverages the cached plan.
4. Furthermore, stored procedures can minimize network round trips by combining multiple queries into a single call, reducing the overhead associated with individual query executions. This optimization can significantly enhance overall performance, especially when dealing with complex operations or large datasets.
5. Another significant advantage of stored procedures is enhanced security. By granting execution privileges only to the stored procedure and not directly to underlying tables, you can enforce access control and protect sensitive data.

In summary, while a simple query can achieve the desired outcome, utilizing a stored procedure offers distinct benefits such as code reusability, improved performance through query optimization, reduced network overhead, and enhanced security.

## Building Blocks of Stored Procedures

Let's break down the stored procedure and examine each component individually. We will understand creating and running the stored procedure in MySQL. 

There are several MySQL IDEs available, and I recommend using MySQL Workbench. But you are free to choose any IDE that suits your preferences and needs.

### Procedure Name

Every stored procedure has a unique name that identifies it within the database. The name should be descriptive and relevant to the procedure's purpose.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-107.png)
_Define a procedure_

```
CREATE PROCEDURE `GenerateSalesReport`()
BEGIN
END
```

### Parameters

Stored procedures can have input parameters that allow you to pass values into the procedure at runtime. We define `start_date` and `end_date` as our input parameters. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-106.png)
_Sample parameters in stored procedure_

```
CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
END
```

### Variables

Variables are used to store and manipulate data within the stored procedure. They can be declared and assigned values as needed. 

There are two types of variables in SQL. We'll look at each of them now.

#### Session Variables

Session variables in MySQL are prefixed with the `@` symbol (for example `@variable_name`). These variables are associated with the current session or connection and retain their values throughout the session until they are explicitly changed or the session ends.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-102.png)
_Define Session variable in stored procedure_

```

CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
   SELECT @totalSales := 0;
   SELECT SUM(sales_amount) INTO @totalSales FROM sales;
   SELECT @totalSales As total_sales;
END
```

#### Regular Variables

Regular variables, also known as local variables, are declared using the `DECLARE` keyword within the scope of a stored procedure. Unlike session variables, regular variables do not have the `@` prefix (for example `variable_name`). They are temporary and exist only within the block of code where they are declared.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-104.png)
_Define Normal variable in stored procedure_

```
CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
   DECLARE totalSales INT;
   SELECT SUM(sales_amount) INTO totalSales FROM sales;
END
```

### SQL Statements

The core functionality of a stored procedure is defined by SQL statements. These statements can include SELECT, INSERT, UPDATE, DELETE, and other SQL commands to interact with the database.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-105.png)
_SQL statements in stored procedure_

```
CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
    SELECT DATE_FORMAT(saled_date, '%d-%m-%Y') AS Date,
           COUNT(sale_id) AS TotalOrders,
           SUM(total_amount) AS TotalSales
    FROM sales
    WHERE saled_date BETWEEN start_date AND end_date
    GROUP BY DATE_FORMAT(saled_date, '%d-%m-%Y');
END
```

### Procedure Call

To execute the stored procedure and generate a detailed sales report for a specific date range, we can use the following syntax:

```sql
CALL <procedure_name>(<parameter1>, ...);
```

```
CALL GenerateSalesReport('2021-01-01', '2023-12-31');
```

The below screenshot shows the result of the stored procedure. The interesting part is that this query has processed around 1 million data in a second. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-109.png)
_Result of sample procedure call to generate saled report_

## Importance of Using MySQL Stored Procedures

### Improved Performance

Stored procedures offer a significant performance advantage over ad-hoc SQL queries. Once a stored procedure is created, it is compiled and stored in a pre-optimized form. 

This compilation process eliminates the need for repetitive query parsing and optimization, resulting in faster execution times. By reducing the overhead associated with query processing, stored procedures enhance the overall performance of database operations.

### Enhanced Security

Security is a critical aspect of database management. Stored procedures allow database administrators to define access rights and permissions for executing specific procedures. This fine-grained control ensures that only authorized users can interact with the database through the procedures, minimizing the risk of unauthorized data access or modifications. 

By encapsulating sensitive operations within stored procedures, security vulnerabilities are reduced, strengthening the overall database security posture.

### Code Reusability and Maintainability

Stored procedures promote code reusability, modularity, and maintainability. By encapsulating frequently used SQL statements and operations within a single procedure, you can avoid code duplication and ensure consistent execution across multiple instances. 

This modularity makes it easier to maintain and update the database logic. Additionally, when modifications are required, changes can be made in a single location (the stored procedure) rather than in multiple places, simplifying the maintenance process.

### Transaction Control

Stored procedures enable transaction control within the database. Transactions ensure data integrity by grouping multiple database operations into a single logical unit. By executing a series of operations within a transaction, you can ensure that either all the operations are successfully completed, or none of them are applied. 

This atomicity ensures data consistency and protects against data corruption. Stored procedures allow you to define transaction boundaries, ensuring that complex operations are handled reliably and consistently.

### Performance Optimization and Query Plan Caching

Another advantage of using stored procedures is the ability to optimize query execution plans. 

Since stored procedures are compiled and stored, the database engine can generate optimized execution plans based on the stored procedure's statistics and data distribution. These optimized plans can significantly improve query performance. 

Furthermore, the query execution plans for stored procedures are cached, which further reduces the overhead of plan generation for subsequent executions.

## Conclusion

Stored procedures are a valuable tool in database management, and you'll want to use them in specific scenarios. When dealing with complex business logic, aiming for performance optimization, enhancing security and access control, promoting code reusability and maintainability, handling complex transactions, or integrating with legacy systems, stored procedures can provide significant benefits. 

By leveraging their power effectively, you can streamline your database operations, improve application performance, and simplify code maintenance, leading to a more efficient and scalable database environment.

If you wish to learn more about SQL and Stored Procedures, subscribe to my [email newsletter](https://5minslearn.gogosoon.com/?ref=fcc_sql_stored_procedure) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_sql_stored_procedure)) and follow me on social media.


