---
title: SQL SELECT Statement – How to Select Data from a Database
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-20T16:56:43.000Z'
originalURL: https://freecodecamp.org/news/sql-select-statement-how-to-select-data-from-a-database
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/SQL-SELECT-Statement.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Karlgusta Annoh\nIn this article, you will learn about the SQL SELECT\
  \ statement. We'll discuss its syntax, how to use it, and how to use the SELECT\
  \ statement with the WHERE clause. You will also learn how to use it with the ORDER\
  \ BY clause. \nIntrod..."
---

By Karlgusta Annoh

In this article, you will learn about the SQL SELECT statement. We'll discuss its syntax, how to use it, and how to use the SELECT statement with the WHERE clause. You will also learn how to use it with the ORDER BY clause. 

## Introduction to the SQL SELECT Statement

The SQL Select statement is a statement that you use to select data from a database. 

The result of the SELECT statement is stored in a result table, also known as a result-set. The result-set is a virtual table that has no physical existence. You use the result-set to display the data in a tabular format. 

## Syntax of the SQL SELECT Statement

The syntax of the SQL SELECT statement is as follows:

```sql
    SELECT column_name(s)
    FROM table_name;
```

An example of the SQL SELECT statement is as follows:

```sql
    SELECT * FROM Customers;
```

## How to Use the SQL SELECT Statement in MySQL Workbench

We are going to use a visual database design tool called MySQL Workbench. 

MySQL Workbench enables us to create a database, create a table, insert data into the table, and run the SQL SELECT statement.

In order to use the SQL SELECT statement in MySQL Workbench, we need to follow the following steps:

1. Open the MySQL Workbench.
2. Connect to the MySQL server.
3. Create a database.
4. Create a table. 
5. Insert data into the table.
6. Run the SQL SELECT statement.
7. View the result-set.

## Open the MySQL Workbench

In order to open the MySQL Workbench, we need to follow these steps:

First, install MySQL Workbench on your computer, if you have not already installed it. You can download MySQL Workbench from the following link: https://dev.mysql.com/downloads/workbench/

![Where to download the MySQL Workbench](https://user-images.githubusercontent.com/33565767/206399335-81d0642c-4d9a-4f0d-a949-90a1836b6280.png 'Where to download the MySQL Workbench')

Then install MySQL server on your computer, if you have not already installed it. You can download MySQL server from the following link: https://dev.mysql.com/downloads/mysql/

![Where to download the MySQL Server](https://user-images.githubusercontent.com/33565767/206399804-7db0adb6-190a-44ce-8ad8-5380b1a74db2.png 'Where to download the MySQL Server')

Now you'll open MySQL Workbench. To do so, click on the Start button and then click on the MySQL Workbench icon.

![Open the MySQL Workbench](https://user-images.githubusercontent.com/33565767/206399997-e991c3ab-89aa-489a-ab9a-20be8aafe55d.png 'Open the MySQL Workbench')

Connect to the MySQL server by clicking on the MySQL Connections icon and then click on the Local instance 3306 icon.

![Connect to the MySQL Server](https://user-images.githubusercontent.com/33565767/206400391-f4dc143e-06e7-4aac-9e7b-32f1e5138d40.png 'Connect to the MySQL Server')

Enter the password for MySQL server in the Password field and then click on the OK button. 

![Enter the password for the MySQL Server](https://user-images.githubusercontent.com/33565767/206400694-eba711dc-79b2-48df-a8d5-9cbb6ca6bb86.png 'Enter the password for the MySQL Server')

Next, you'll need to create the database by clicking on the New Schema icon and then entering the name of the database in the Name field. 

![Create a database in MySQL Workbench](https://user-images.githubusercontent.com/33565767/206401624-b98fdf11-cc19-4dd5-8ef0-487c38d23fb1.png 'Create a database in MySQL Workbench')

Then click on the Apply button and click on the Close button.

![Here is the Database created](https://user-images.githubusercontent.com/33565767/206402352-a24a4e80-3770-4c63-a011-48896f455169.png 'Here is the Database created')

Now you'll create a table. To do this, enter the following SQL statement in the SQL Editor and then click on the Execute button:

```sql
   CREATE TABLE Customers (
    CustomerID int NOT NULL,
    CustomerName varchar(255) NOT NULL,
    ContactName varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    Country varchar(255) NOT NULL
   );
```

Make sure that you have selected the database in the Database Navigator. To get to the SQL Editor, click on the SQL Editor icon.

![SQL Editor tab](https://user-images.githubusercontent.com/33565767/206403845-8ca3f459-cda2-4292-8f71-57eecd09bc23.png 'SQL Editor tab')


Let's now create the table Customers. To do this, enter the following SQL statement in the SQL Editor and then click on the Execute button:

```sql
   CREATE TABLE Customers (
    CustomerID int NOT NULL,
    CustomerName varchar(255) NOT NULL,
    ContactName varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    Country varchar(255) NOT NULL
   );
```

![Create the table Customers](https://user-images.githubusercontent.com/33565767/206403200-94b39cc3-a785-455d-b72d-236d0f876af7.png 'Create the table Customers')

Now you'll execute the SQL statement. After you have entered the SQL statement, click on the Execute button.

![image](https://user-images.githubusercontent.com/33565767/206404552-87efc906-ac16-457e-acaf-d4261c8fff88.png)


To insert data into the table, enter the following SQL statement in the SQL Editor and then click on the Execute button:

```sql
   INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (1, 'Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany');
```

![Insert into Customers table](https://user-images.githubusercontent.com/33565767/206649495-65f45f7e-9b4b-4b12-961f-fb5200fc2ddf.png 'Insert into Customers table')


Now run the SQL SELECT statement by entering the following SQL statement in the SQL Editor and then clicking on the Execute button:

```sql
   SELECT * FROM Customers;
```

![Select from Customers](https://user-images.githubusercontent.com/33565767/206650409-71ebd314-8c97-4b4b-83c1-9ec3fa37992f.png 'Select from Customers')

## How to Use the SQL SELECT Statement with the WHERE Clause

You can use the SQL SELECT statement with the WHERE clause. You use the WHERE clause to filter records. The WHERE clause extracts only those records that fulfill a specified condition. 

The syntax of the SQL SELECT statement with the WHERE clause is as follows:

```sql
   SELECT column_name(s)
   FROM table_name
   WHERE condition;
```

An example of using the SQL SELECT statement with the WHERE clause is as follows:

```sql
   SELECT * FROM Customers
   WHERE Country='Germany';
```

Let's insert another record with a different country and test out the SQL SELECT statement with the WHERE clause. 

To insert another record, enter the following SQL statement in the SQL Editor and then click on the Execute button:

```sql
   INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (2, 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitucion 2222', 'Mexico D.F.', '05021', 'Mexico');
```

![Insert into Customers in MySQL Workbench](https://user-images.githubusercontent.com/33565767/206651983-753b9b6d-ec67-4070-ba85-855fec07fedb.png 'Insert into Customers in MySQL Workbench')

Now let's run the SQL SELECT statement with the WHERE clause. Enter the following SQL statement in the SQL Editor and then click on the Execute button:

```sql
   SELECT * FROM Customers
   WHERE Country='Germany';
```

![Select from Customers in MySQL Workbench](https://user-images.githubusercontent.com/33565767/206653156-c6f4a814-6ff7-4414-9217-b94b1d83f442.png 'Select from Customers in MySQL Workbench')


## How to Use the SQL SELECT Statement with the ORDER BY Clause

You can also use the SQL SELECT statement with the ORDER BY clause. The ORDER BY clause sorts the result-set in ascending or descending order. It sorts the records in ascending order by default. If you want to sort the records in descending order, you can use the DESC keyword. 

The syntax of the SQL SELECT statement with the ORDER BY clause is as follows:

```sql
   SELECT column_name(s)
   FROM table_name
   ORDER BY column_name(s) ASC/DESC;
```

An example of using the SQL SELECT statement with the ORDER BY clause is as follows:

```sql
   SELECT * FROM Customers
   ORDER BY Country DESC;
```

![Select from Customers, order in Descending Order by Country name](https://user-images.githubusercontent.com/33565767/206653974-affc64b0-5f01-4700-9f81-7609588e95f0.png 'Select from Customers, order in Descending Order by Country name')


## Conclusion

In this article, we learned about the SQL SELECT statement. We learned about the syntax of the SELECT statement, how to use it, and how it works with the WHERE clause. We also learned about the SQL SELECT statement with the ORDER BY clause.



