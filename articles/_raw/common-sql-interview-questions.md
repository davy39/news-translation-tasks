---
title: Common SQL Interview Questions for Amazon, Apple, Google
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-02T16:57:00.000Z'
originalURL: https://freecodecamp.org/news/common-sql-interview-questions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9faf740569d1a4ca43fc.jpg
tags:
- name: interview
  slug: interview
- name: SQL
  slug: sql
seo_title: null
seo_desc: SQL is used in a wide variety of programming jobs. It's important to be
  familiar with SQL if you are going to be interviewing soon for a software position.
  This is especially true if you are going to interview at a top tech company such
  as Amazon, Ap...
---

SQL is used in a wide variety of programming jobs. It's important to be familiar with SQL if you are going to be interviewing soon for a software position. This is especially true if you are going to interview at a top tech company such as Amazon, Apple, or Google. 

This guide will cover basic SQL syntax as a refresher and then list some common SQL interview questions. The answers for all questions are given and you can use this information to study for your programming interview.

## **Basic SQL Syntax Example**

SQL is an international standard (ISO), but you will find some differences between implementations. This guide uses MySQL as an example because it's the most popular implementation of SQL. 

### **How to use a specific database**

Here is the SQL command used to select the database containing the tables for your SQL statements:

```sql
USE fcc_sql_guides_database; 

```

### **SELECT and FROM clauses**

Use SELECT to determine which columns of the data you want to show in the results. There are also options you can use to show data that is not a table column.

The following example shows two columns selected from the “student” table, and two calculated columns. The first of the calculated columns is a meaningless number, and the other is the system date.

```sql
SELECT studentID, FullName, 3+2 AS five, now() AS currentDate FROM student;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax01.JPG)

### **WHERE clause**

The WHERE clause specifies a condition while getting data. The WHERE clause is used to limit the number of rows returned. It's often used in a SELECT statement but can also be used in other statements such as UPDATE and DELETE.

Here is the basic syntax of the WHERE clause:

```sql
SELECT column1, column2
FROM table_name
WHERE [condition]
```

The condition in a WHERE clause can include logical operators like >, <, =, LIKE, NOT, AND, OR.

Here is an example of a SQL statment using the WHERE clause. It specifies that if any of the students have certain SAT scores (1000, 1400), they will not be presented:

```
SELECT studentID, FullName, sat_score, recordUpdated
FROM student
WHERE (studentID BETWEEN 1 AND 5
    OR studentID = 8
    OR FullName LIKE '%Maximo%')
    AND sat_score NOT IN (1000, 1400);

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax02.JPG)

### **ORDER BY (ASC, DESC)**

ORDER BY gives us a way to sort the result set by one or more of the items in the SELECT section.

Here is the same list as above, but sorted by the student's Full Name. The default sort order is ascending (ASC), but to sort in the opposite order (descending) you use DESC, as in the example below:

```sql
SELECT studentID, FullName, sat_score
FROM student
WHERE (studentID BETWEEN 1 AND 5
    OR studentID = 8
    OR FullName LIKE '%Maximo%')
    AND sat_score NOT IN (1000, 1400)
ORDER BY FullName DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax03.JPG)

### **GROUP BY and HAVING**

GROUP BY gives us a way to combine rows and aggregate data. The HAVING clause is like the above WHERE clause, except that it acts on the grouped data.

The SQL statement below answers the question: “Which candidates received the largest number of contributions (ordered by count (*)) in 2016, but only those who had more than 80 contributions?”

Ordering this data set in a descending (DESC) order places the candidates with the largest number of contributions at the top of the list.

```
SELECT Candidate, Election_year, SUM(Total_$), COUNT(*)
FROM combined_party_data
WHERE Election_year = 2016
GROUP BY Candidate, Election_year
HAVING count(*) > 80
ORDER BY count(*) DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax04.JPG)

## Common SQL Interview Questions

### **What is an inner join in SQL?**

This is the default type of join if no join is specified. It returns all rows in which there is at least one match in both tables.

```sql
SELECT * FROM A x JOIN B y ON y.aId = x.Id
```

### **What is a left join in SQL?**

A left join returns all rows from the left table, and the matched rows from the right table. Rows in the left table will be returned even if there was no match in the right table. The rows from the left table with no match in the right table will have `null` for right table values.

```sql
SELECT * FROM A x LEFT JOIN B y ON y.aId = x.Id
```

### **What is a right join in SQL?**

A right join returns all rows from the right table, and the matched rows from the left table. Opposite of a left join, this will return all rows from the right table even where there is no match in the left table. Rows in the right table that have no match in the left table will have `null` values for left table columns.

```sql
SELECT * FROM A x RIGHT JOIN B y ON y.aId = x.Id
```

### **What is a full join or full outer join in SQL?**

A full outer join and a full join are the same thing. The full outer join or full join returns all rows from both tables, matching up the rows wherever a match can be made and placing NULLs in the places where no matching row exists.

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName
```

### **What is the result of the following command?**

```sql
DROP VIEW view_name
```

This will result in an error because you can’t perform a DML operation on a view. A DML operation is any operation that manipulates the data such as DROP, INSERT, UPDATE, and DELETE.

### **Can we perform a rollback after using ALTER command?**

No, because ALTER is a DDL command and Oracle server performs an automatic COMMIT when the DDL statements are executed. DDL statements define data structures such as `CREATE table` and `ALTER table`.

### **Which is the only constraint that enforces rules at column level?**

NOT NULL is the only constraint that works at the column level.

### **What are the pseudocolumns in SQL? Give some examples?**

A pseudocolumn behaves like a column, but is not actually stored in the table because it is all generated values. The values of a pseudocolumn can be selected but they cannot be inserted, updated, or deleted. 

```
ROWNUM, ROWID, USER, CURRVAL, NEXTVAL etc.
```

### Create a user "my723acct" with password "kmd26pt". Use the "user_data" and temporary data tablespaces provided by PO8 and provide to this user 10M of storage space in "user_data" and 5M of storage space in "temporary_data".

```sql
CREATE USER my723acct IDENTIFIED BY kmd26pt
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temporary_data
QUOTA 10M on user_data QUOTA 5M on temporary_data
```

### **Create the role** _role_tables_and_views_**.**

```sql
CREATE ROLE role_tables_and_views
```

### **Grant to the role of the previous question the privileges to connect to the database and the privileges to create tables and views.**

The privilege to connect to the database is CREATE SESSION The privilege to create table is CREATE TABLE The privilege to create view is CREATE VIEW

```sql
    GRANT CREATE SESSION, CREATE TABLE, CREATE VIEW TO role_tables_and_views
```

### **Grant the previous role in the question to the users _anny_ and _rita_.**

```sql
    GRANT role_tables_and_views TO anny, rita
```

### **Write a command to change the password of the user _rita_ from "abcd" to "dfgh"**

```sql
    ALTER USER rita IDENTIFIED BY dfgh
```

### The users _rita_ and _anny_ do not have SELECT privileges on the table INVENTORY that was created by _scott_. Write a command to allow _scott_ to grant the users SELECT privileges on theses  tables.

```sql
    GRANT select ON inventory TO rita, anny
```

### **User** _**rita**_ **has been transferred and no longer needs the privilege that was granted to her through the role** _role_tables_and_views_. Write a command to remove her from her previously given privileges. She should still be able to connect to the database.

```sql
REVOKE select ON scott.inventory FROM rita
REVOKE create table, create view FROM rita
```

### **The user _rita_ who was transferred is now moving to another company. Since the objects she created are no longer used, write a command to remove this user and all her objects.**

The CASCADE option is necessary to remove all the objects of the user in the database.

```sql
DROP USER rita CASCADE
```

### **Write an SQL query to find the nth highest "Salary" from the "Employee" table.**

```sql
   SELECT TOP 1 Salary
   FROM (
      SELECT DISTINCT TOP N Salary
      FROM Employee
      ORDER BY Salary DESC
      )
    ORDER BY Salary ASC
```

## Conclusion

If you think you can answer all these questions, you may be ready for your interview. Good luck!

