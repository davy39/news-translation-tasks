---
title: The Best SQL Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-14T00:29:00.000Z'
originalURL: https://freecodecamp.org/news/sql-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/sql-image.jpeg
tags:
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'SQL stands for Structured Query Language. It''s used with all kinds of
  relational databases.

  Basic SQL Syntax Example

  This guide provides a basic, high level description of the syntax for SQL statements.

  SQL is an international standard (ISO), but you...'
---

SQL stands for Structured Query Language. It's used with all kinds of relational databases.

## Basic SQL Syntax Example

This guide provides a basic, high level description of the syntax for SQL statements.

SQL is an international standard (ISO), but you will find many differences between implementations. This guide uses MySQL as an example. If you use one of the many other Relational Database Managers (DBMS) you’ll need to check the manual for that DBMS if needed.

### What we will cover

* Use (sets what database the statement will use)
* Select and From clauses
* Where Clause (and / or, IN, Between, LIKE)
* Order By (ASC, DESC)
* Group by and Having

### How to use this

This is used to select the database containing the tables for your SQL statements:

```sql
use fcc_sql_guides_database; -- select the guide sample database

```

### Select and From clauses

The Select part is normally used to determine which columns of the data you want to show in the results. There are also options you can use to show data that is not a table column.

This example shows two columns selected from the “student” table, and two calculated columns. The first of the calculated columns is a meaningless number, and the other is the system date.

```sql
select studentID, FullName, sat_score, recordUpdated, 
3+2 as five, now() as currentDate 
from student;

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-198.png)

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax01.JPG)

> Where Clause (and / or, IN, Between and LIKE)

The WHERE clause is used to limit the number of rows returned.

In this case all five of these will be used is a somewhat ridiculous Where clause.

Compare this result to the above SQL statement to follow this logic.

Rows will be presented that:

* Have Student IDs between 1 and 5 (inclusive)
* or studentID = 8
* or have “Maxmimo” in the name

The following example is similar, but it further specifies that if any of the students have certain SAT scores (1000, 1400), they will not be presented:

```sql
select studentID, FullName, sat_score, recordUpdated
from student
where
  (
    studentID between 1 and 5
    or studentID = 8
    or FullName like '%Maximo%'
  )
and sat_score NOT in (1000, 1400);

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax02.JPG)

### Order By (ASC, DESC)

Order By gives us a way to sort the result set by one or more of the items in the SELECT section. Here is the same list as above, but sorted by the students Full Name. The default sort order is ascending (ASC), but to sort in the opposite order (descending) you use DESC, as in the example below:

```sql
select studentID, FullName, sat_score
from student
where 
  (
    studentID between 1 
    and 5 -- inclusive
    or studentID = 8 
    or FullName like '%Maximo%'
  ) 
  and sat_score NOT in (1000, 1400)
order by FullName DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax03.JPG)

### Group By and Having

Group By gives us a way to combine rows and aggregate data. The Having clause is like the above Where clause, except that it acts on the grouped data.

This data is from the campaign contributions data we’ve been using in some of these guides.

This SQL statement answers the question: “which candidates recieved the largest number of contributions (not $ amount, but count (*)) in 2016, but only those who had more than 80 contributions?”

Ordering this data set in a descending (DESC) order places the candidates with the largest number of contributions at the top of the list.

```sql
select Candidate, Election_year, sum(Total_$), count(*)
from combined_party_data
where Election_year = 2016
group by Candidate, Election_year
having count(*) > 80
order by count(*) DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax04.JPG)

_As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide. I hope this at least gives you enough to get started. Please see the manual for your database manager and have fun trying different options yourself._

## Common SQL Interview Questions

### What is an inner join in SQL?

This is the default type of join if no join is specified. It returns all rows in which there is at least one match in both tables.

```sql
SELECT * FROM A x JOIN B y ON y.aId = x.Id

```

### What is a left join in SQL?

A left join returns all rows from the left table, and the matched rows from the right table. Rows in the left table will be returned even if there was no match in the right table. The rows from the left table with no match in the right table will have `null` for right table values.

```sql
SELECT * FROM A x LEFT JOIN B y ON y.aId = x.Id

```

### What is a right join in SQL?

A right join returns all rows from the right table, and the matched rows from the left table. Opposite of a left join, this will return all rows from the right table even where there is no match in the left table. Rows in the right table that have no match in the left table will have `null` values for left table columns.

```sql
SELECT * FROM A x RIGHT JOIN B y ON y.aId = x.Id

```

### What is a full join in SQL?

A full join returns all rows for which there is a match in either of the tables. So if there are rows in the left table that do not have matches in the right table, those will be included. As well as if there are rows in the right table that do not have matches in the left table, those will be included.

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName

```

### What is the result of the following command?

```sql
DROP VIEW view_name

```

Here it’ll be an error because we can’t perform a DML operation on a view.

### Can we perform a rollback after using ALTER command?

No, because ALTER is a DDL command and Oracle server performs an automatic COMMIT when the DDL statements are executed.

### Which is the only constraint that enforces rules at column level?

NOT NULL is the only constraint that works at the column level.

### What are the pseudocolumns in SQL? Give some examples?

A pseudocolumn is a function which returns a system generated value. The reason it is known as so because a pseudocolumn is an Oracle assigned value used in the same context as an Oracle database column but not stored on disk.

```
ROWNUM, ROWID, USER, CURRVAL, NEXTVAL etc.

```

Create a user my723acct with password kmd26pt. Use the user data and temporary data tablespaces provided by PO8 and provide to this user 10M of storage space in user data and 5M of storage space in temporary_data.

```sql
CREATE USER my723acct IDENTIFIED BY kmd26pt
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temporary_data
QUOTA 10M on user_data QUOTA 5M on temporary_data

```

### Create the role role _tables_ and_views.

```sql
CREATE ROLE role_tables_and_views

```

Grant to the role of the previous question the privileges to connect to the database and the privileges to create tables and views.

The privilege to connect to the database is CREATE SESSION The privilege to create table is CREATE TABLE The privilege to create view is CREATE VIEW

```sql
GRANT Create session, create table, create view TO role_tables_and_views

```

### Grant the previous role in the question to the users anny and rita

```sql
GRANT role_tables_and_views TO anny, rita

```

Create a user my723acct with password kmd26pt. Use the user data and temporary data tablespaces provided by PO8 and provide to this user 10M of storage space in user data and 5M of storage space in temporary_data.

```sql
CREATE USER my723acct IDENTIFIED BY kmd26pt
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temporary_data
QUOTA 10M on user_data QUOTA 5M on temporary_data

```

### Create the role role _tables_ and_views.

```sql
CREATE ROLE role_tables_and_views

```

Grant to the role of the previous question the privileges to connect to the database and the privileges to create tables and views.

The privilege to connect to the database is CREATE SESSION The privilege to create table is CREATE TABLE The privilege to create view is CREATE VIEW.

```sql
GRANT Create session, create table, create view TO role_tables_and_views

```

Grant the previous role in the question to the users anny and rita

```sql
GRANT role_tables_and_views TO anny, rita

```

Write a command to change the password of the user rita from abcd to dfgh

```sql
ALTER USER rita IDENTIFIED BY dfgh

```

The users rita and anny do not have SELECT privileges on the table INVENTORY that was created by SCOTT. Write a command to allow SCOTT to grant the users SELECT priviliges on these tables.

```sql
GRANT select ON inventory TO rita, anny

```

User rita has been transferred and no longer needs the privilege that was granted to her through the role role tables and_views. Write a command to remove her from her previous given priviliges except that she still could connect to the database.

```sql
REVOKE select ON scott.inventory FROM rita
REVOKE create table, create view FROM rita

```

The user rita who was transferred is now moving to another company. Since the objects that she created is of no longer use, write a commmand to remove this user and all her objects.

Here CASCADE option is necessary to remove all the objects of the user in the database.

```sql
DROP USER rita CASCADE

/* User rita has been transferred and no longer needs the privilege
that was granted to her through the role role_tables_and_views. Write
a command to remove her from her previous given priviliges except that
she still could connect to the database. */
    
REVOKE select ON scott.inventory FROM rita
REVOKE create table, create view FROM rita

```

The user rita who was transferred is now moving to another company. Since the objects that she created is of no longer use, write a command to remove this user and all her objects.

Here CASCADE option is necessary to remove all the objects of the user in the database.

```sql
DROP USER rita CASCADE

```

### Write SQL query to find the nth highest salary from table.

```sql
SELECT TOP 1 Salary
FROM
  (
    SELECT DISTINCT TOP N Salary
    FROM Employee
    ORDER BY Salary DESC
  )
ORDER BY Salary ASC
```

## SQL Create View Statement

### What is a View?

A View is a database object that presents data existing in one or more tables. Views are used in a similar way to tables, but they don’t contain any data. They just “point” to the data that exists elsewhere (tables or views, for example).

### Why do we like them?

* Views are a way to limit the data presented. For example, the human resources department data filtered to only present non-sensitive information. Sensitive information in this case could be social security numbers, sex of employee, payrate, home address, etc.
* Complex data across more than one table can be combined into a single “view.” This can make life easier for your business analysts and programmers.

### Important Safety Tips

* Views are managed by the system. When data in the related tables are changed, added, or updated, the View is updated by the system. We want to use these only when needed to manage use of system resources.
* In MySQL, changes to the table design (that is, new or dropped columns) made AFTER a view is created are not updated in the view itself. The view would have to be updated or recreated.
* Views are one of the four standard database object types. The others are tables, stored procedures, and functions.
* Views can usually be treated as you would a table, but updates are limited or not available when the view contains more than one table.
* There are many other details about views that are beyond the scope of this introductory guide. Spend time with your database managers manual and have fun with this powerful SQL object.

### Syntax of the Create View Statement (MySQL)

```
CREATE
    [OR REPLACE]
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { user | CURRENT_USER }]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
	[WITH [CASCADED | LOCAL] CHECK OPTION]

```

_This guide will cover this part of of the statement…_

```sql
CREATE VIEW view_name [(column_list) ] AS select_statement

```

### Sample View creation from the student tables

Notes:

* The name of the view has a “v” at the end. It’s recommended that the view name indicate that it’s a view in some way to make life easier for programmers and database administrators. Your IT shop should have its own rules on naming objects.
* The columns in the view are limited by the SELECT and the rows of data by the WHERE clause.
* the ”`” character around the view names is required because of the ”-” in the names. MySQL reports an error without them.

```sql
create view `programming-students-v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';

select * from `programming-students-v`;

```

### Sample of using a View to combine data from more than one table

A Student demographics table was added to the database to demonstrate this usage. This view will combine these tables.

Notes:

* To “join” tables, the tables must have fields in common (usually primary keys) that uniquely identity each row. In this case it’s the student ID. (More on this in the [SQL Joins](https://guide.freecodecamp.org/sql/sql-joins/index.md) guide.)
* Notice the “alias” given to each table (“s” for student and “sc” for student contact). This is a tool to shorten the table names and make it easier to identify which table is being used. It’s easier than typing long table names repeatedly. In this example, it was required because studentID is the same column name in both tables, and the system would present an “ambiguous column name error” without specifying which table to use.

## Guide to the SQL Between Operator

The BETWEEN Operator is useful because of the SQL Query Optimizer. Although BETWEEN is functionally the same as: x <= element <= y, the SQL Query Optimizer will recognize this command faster, and has optimized code for running it.

This operator is used in a WHERE clause or in a GROUP BY HAVING clause.

Rows are selected that have a value greater than the minimum value and less than the maximum value.

It’s important to keep in mind that the values entered in the command are **excluded** from the result. We get just what is between them.

Here is the syntax for using the function in a WHERE Clause:

```sql
select field1, testField
from table1
where testField between min and max

```

Here is an example using the student table and the WHERE clause:

```sql
-- no WHERE clause
select studentID, FullName, studentID
from student;
    
-- WHERE clause with between
select studentID, FullName, studentID
from student
where studentID between 2 and 7;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/between01.JPG?raw=true)

Here is an example using the campaign funds table and the having clause. This will return rows where the sum of the donations for a candidate are between $3 Million and $18 Million based on the HAVING clause in the GROUP BY part of the statement. More on aggregation in that guide.

```sql
select Candidate, Office_Sought, Election_Year, format(sum(Total_$),2)
from combined_party_data
where Election_Year = 2016
group by Candidate, Office_Sought, Election_Year
having sum(Total_$) between 3000000 and 18000000
order by sum(Total_$) desc; 

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/between02.JPG?raw=true)

# SQL Create Table Statement Example

A table is a group of data stored in a database.

To create a table in a database you use the `CREATE TABLE` statement. You give a name to the table and a list of columns with its datatypes.

```sql
CREATE TABLE TABLENAME(Attribute1 Datatype, Attribute2 Datatype, ...);

```

Here’s an example creating a table named Person:

```sql
CREATE TABLE Person(
  Id int not null, 
  Name varchar not null, 
  DateOfBirth date not null, 
  Gender bit not null, 
  PRIMARY KEY(Id)
);

```

In the example above, each Person has a Name, a Date of Birth and a Gender. The Id column is the key that identifies one person in the table. You use the keyword `PRIMARY KEY` to configure one or more columns as a primary key.

A column can be `not null` or `null` indicating whether it is mandatory or not.

# A guide to the SQL Insert Query

Insert queries are a way to insert data into a table. Let’s say we have created a table using

```sql
CREATE TABLE example_table (
  name varchar(255), 
  age int
)

```

**example_table**

```
Name|Age
--- | --- 
```

Now to add some data to this table , we’ll use  **INSERT**  in the following way:

`INSERT INTO example_table (column1,column2) VALUES ("Andrew",23)`

```sql
INSERT INTO example_table (column1, column2) 
VALUES ("Andrew", 23)

```

**example_table**

```
Name|Age
--- | --- 
Andrew|23
```

Even the following will work, but it’s always a good practice to specify which data is going into which column.

`INSERT INTO table_name VALUES ("John", 28)`

```sql
INSERT INTO table_name 
VALUES ("John", 28)

```

**example_table**

```
Name|Age
--- | --- 
Andrew|23
John|28
```

# A guide to the SQL AND operator

AND is used in a WHERE clause or a GROUP BY HAVING clause to limit the rows returned from the executed statement. Use AND when it’s required to have more than one condition met.

We’ll use the student table to present examples.

Here’s the student table without a WHERE clause:

```sql
select * from student;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator01.JPG?raw=true)

Now the WHERE clause is added to display only programming students:

```sql
select * from student 
where programOfStudy = 'Programming';

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator02.JPG?raw=true)

Now the WHERE clause is updated with AND to show results for programming students that also have a SAT score greater than 800:

```sql
select * from student 
where programOfStudy = 'Programming' 
and sat_score > 800;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator03.JPG?raw=true)

This is a more complex example from the campaign contributions table. This example has a GROUP BY clause with HAVING clause using an AND to restrict the returned records to candidates from 2016 with contributions between $3 Million and $18 Million in total.

```sql
select Candidate, Office_Sought, Election_Year, FORMAT(sum(Total_$),2) from combined_party_data
where Office_Sought = 'PRESIDENT / VICE PRESIDENT'
group by Candidate, Office_Sought, Election_Year
having Election_Year = 2016 and sum(Total_$) between 3000000 and 18000000
order by sum(Total_$) desc;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator06.JPG?raw=true)

## How to use the SQL Order By Keyword

### Order By (ASC, DESC)

ORDER BY gives us a way to SORT the result set by one or more of the items in the SELECT section. Here is an SQL sorting the students by FullName in descending order. The default sort order is ascending (ASC) but to sort in the opposite order (descending) you use DESC.

```sql
SELECT studentID, FullName, sat_score
FROM student
ORDER BY FullName DESC;

```

```
+-----------+------------------------+-----------+
| studentID | FullName               | sat_score |
+-----------+------------------------+-----------+
|         2 | Teri Gutierrez         |       800 |
|         3 | Spencer Pautier        |      1000 |
|         6 | Sophie Freeman         |      1200 |
|         9 | Raymond F. Boyce       |      2400 |
|         1 | Monique Davis          |       400 |
|         4 | Louis Ramsey           |      1200 |
|         7 | Edgar Frank "Ted" Codd |      2400 |
|         8 | Donald D. Chamberlin   |      2400 |
|         5 | Alvin Greene           |      1200 |
+-----------+------------------------+-----------+
9 rows in set (0.00 sec)

```

_Here is the UN-ORDERED, current, full student list to compare to the above._

```sql
SELECT studentID, FullName, sat_score, rcd_updated FROM student;

```

```
+-----------+------------------------+-----------+---------------------+
| studentID | FullName               | sat_score | rcd_updated         |
+-----------+------------------------+-----------+---------------------+
|         1 | Monique Davis          |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+---------------------+
9 rows in set (0.00 sec)

```

As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

