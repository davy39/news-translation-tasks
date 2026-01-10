---
title: 'SQL Select Statements: Examples of Select Distinct, Select Into, Insert into,
  and More'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-11T01:07:00.000Z'
originalURL: https://freecodecamp.org/news/sql-select-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ca3740569d1a4ca3358.jpg
tags:
- name: SQL
  slug: sql
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Select and From clauses

  The SELECT part of a query is normally to determine which columns of the data to
  show in the results. There are also options you can apply to show data that is not
  a table column.

  This example shows three columns selected from...'
---

## Select and From clauses

The SELECT part of a query is normally to determine which columns of the data to show in the results. There are also options you can apply to show data that is not a table column.

This example shows three columns selected from the “student” table and one calculated column. The database stores the studentID, FirstName, and LastName of the student. We can combine the First and the Last name columns to create the FullName calculated column.

```sql
select studentID, FirstName, LastName, FirstName + ' ' + LastName as FullName
from student;
```

```text
+-----------+-------------------+------------+------------------------+
| studentID | FirstName         | LastName   | FullName               |
+-----------+-------------------+------------+------------------------+
|         1 | Monique           | Davis      | Monique Davis          |
|         2 | Teri              | Gutierrez  | Teri Gutierrez         |
|         3 | Spencer           | Pautier    | Spencer Pautier        |
|         4 | Louis             | Ramsey     | Louis Ramsey           |
|         5 | Alvin             | Greene     | Alvin Greene           |
|         6 | Sophie            | Freeman    | Sophie Freeman         |
|         7 | Edgar Frank "Ted" | Codd       | Edgar Frank "Ted" Codd |
|         8 | Donald D.         | Chamberlin | Donald D. Chamberlin   |
|         9 | Raymond F.        | Boyce      | Raymond F. Boyce       |
+-----------+-------------------+------------+------------------------+
9 rows in set (0.00 sec)
```

*As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

## **SQL Select Distinct Statement**

### **Introduction**

This keyword allows us to get lists of unique values in a column. This guide will demonstrate that.

### **Full display of the data in the student table**

```sql
USE fcc_sql_guides_database;
SELECT studentID, FullName, sat_score, programOfStudy, rcd_Created, rcd_Updated FROM student;
```

```text
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
| studentID | FullName               | sat_score | programOfStudy   | rcd_Created         | rcd_Updated         |
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
|         1 | Monique Davis          |       400 | Literature       | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
9 rows in set (0.00 sec)
```

### **Get list of fields of study**

```sql
SELECT DISTINCT programOfStudy FROM student;
```

```text
+------------------+
| programOfStudy   |
+------------------+
| Literature       |
| Programming      |
| Computer Science |
+------------------+
3 rows in set (0.00 sec)
```

As with all of these SQL things there is MUCH MORE to them than what’s in this introductory guide.

I hope this at least gives you enough to get started.

Please see the manual for your database manager and have fun trying different options yourself.

## **SQL Select into Statement**

The `SELECT INTO` statement is a query that allows you to create a _new_ table and populate it with the result set of a `SELECT statement`. To add data to an existing table, see the [INSERT INTO](https://guide.freecodecamp.org/sql/sql-select-into-statement/guides/src/pages/sql/sql-insert-into-select-statement/index.md) statement instead.

`SELECT INTO` can be used when you are combining data from several tables or views into a new table.<sup>1</sup> The original table is not affected.

The general syntax is:

```sql
SELECT column-names
  INTO new-table-name
  FROM table-name
 WHERE EXISTS 
      (SELECT column-name
         FROM table-name
        WHERE condition)
```

This example shows a set of a table that was “copied” from the “Supplier” table to a new one called SupplierUSA which holds the set related to the column country of value ‘USA’.

```sql
SELECT * INTO SupplierUSA
  FROM Supplier
 WHERE Country = 'USA';
```

**Results**: 4 rows affected <sup>2</sup>

IDCompanyNameContactNameCityCountryPhone2New Orleans Cajun DelightsShelley BurkeNew OrleansUSA(100) 555-48223Grandma Kelly’s HomesteadRegina MurphyAnn ArborUSA(313) 555-573516Bigfoot BreweriesCheryl SaylorBendUSANULL19New England Seafood CanneryRobb MerchantBostonUSA(617) 555-3267

Please see the manual for your database manager and have fun trying different options yourself.

## **SQL Insert into Statement**

To insert a record in a table you use the `INSERT INTO` statement.

You can do it in two ways, if you want to insert values only in some columns, you have to list their names including all mandatory columns. The syntax is:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

The other way is inserting values to all columns in the table, it is not necessary to specify the columns names. The syntax is:

```sql
INSERT INTO table_name 
VALUES (value1, value2, value3, ...);
```

Here’s an example inserting a record in the table Person in both ways:

```sql
INSERT INTO Person
VALUES (1, ‘John Lennon’, ‘1940-10-09’, ‘M’);
```

And

```sql
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, ‘John Lennon’, ‘1940-10-09’, ‘M’);
```

Some SQL versions (for example, MySQL) support inserting multiple rows at once. For example:

```sql
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, ‘John Lennon’, ‘1940-10-09’, ‘M’), (2, ‘Paul McCartney’, ‘1942-06-18’, ‘M’),
(3, ‘George Harrison’, ‘1943-02-25’, ‘M’), (4, ‘Ringo Starr’, ‘1940-07-07’, ‘M’)
```

Note that the entire original query remains intact - we simple add on data rows encloded by paranthesis and separated by commas.

## **SQL Insert into Select Statement**

You can insert records in a table using data that are already stored in the database. This is only a copy of data and it doesn’t affect the origin table.

The `INSERT INTO SELECT` statement combines `INSERT INTO` and `SELECT` statements and you can use any conditions you want. The syntax is:

```sql
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```

Here is an example that inserts in the table Person all the male students from the table Students.

```sql
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
SELECT Id, Name, DateOfBirth, Gender
FROM Students
WHERE Gender = ‘M’
```

## Other SQL resources:

* [SQL and Databases full video course](https://www.freecodecamp.org/news/sql-and-databases-full-course/)
* [Basic SQL commands you should know](https://www.freecodecamp.org/news/basic-sql-commands/)

