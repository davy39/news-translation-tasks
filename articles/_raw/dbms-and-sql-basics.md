---
title: Database Management Systems and SQL – Tutorial for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-12T13:57:35.000Z'
originalURL: https://freecodecamp.org/news/dbms-and-sql-basics
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/FreeCodeCamp.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Bikash Daga (Jain)\nDatabase Management Systems and SQL are two of the\
  \ most important and widely used tools on the internet today. \nYou use a Database\
  \ Management System (DBMS) to store the data you collect from various sources, and\
  \ SQL to manipulat..."
---

By Bikash Daga (Jain)

Database Management Systems and SQL are two of the most important and widely used tools on the internet today. 

You use a Database Management System (DBMS) to store the data you collect from various sources, and SQL to manipulate and access the particular data you want in an efficient way.

Many different businesses use these tools to increase their sales and improve their products. Other institutions like schools and hospitals also use them to improve their administrative services.

In this article, you will learn about:

* The basics of DBMS and SQL
* The most important features of DBMS and SQL
* The reasons you should learn DBMS and SQL.

## What Does a DBMS Do?

DBMS stands for Database Management System, as we mentioned above. [SQL](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/) stands for Structured Query Language.

If you have lots of data that you need to store, you don't just want to keep it anywhere – then there would be no sense of what that huge amount of data means or can tell you. That's why we use a DBMS. 

A database is basically where we store data that are related to one-another – that is, inter-related data. This inter-related data is easy to work with. 

A DBMS is software that manages the database. Some of the commonly used DBMS (software) are MS ACCESS, MySQL, Oracle, and others. 

Suppose you have some data like different names, grades, and ID numbers of students. You'd probably prefer to have that data in a nice table where a particular row consists of students’ names, grades, and ID numbers. And to help you organize and read that data efficiently, you'll want to use a DBMS.

Using a DBMS goes hand in hand with SQL. This is because when you store data and want to access and alter it, you'll use SQL.

A database stores data in various forms like schemas, views, tables, reports, and more.

## Types of DBMS

There are two types of DBMS.

First, you have Relational Databases (RDBMS). In these types of databases, data is stored in the format of tables by the software. In an RDBMS, each row consists of data from a particular entity only.

Some of the RDBMS commonly used are MySQL, MSSQL, Oracle, and others.

Then you have Non-Relational Databases. In these databases, data is stored in the form of key and value pairs.

Some of the Non-Relational DBMSs commonly used are MongoDB, Amazon, Redis, and others.

### Components of a DBMS

There are mainly four components of a DBMS which you can understand by checking out the image below:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-1.54.06-PM.png)

You have your Users. There can be multiple users, like someone who manages the database (the database administrator), system developers, and also those who are just regular users like the customer.

You also have the Database Application. The application of a database can be either departmental or personal or may be for internal use in an organization.

Then you have the DBMS, which we've been discussing. This is software that helps the users create the database and access the data inside it in an efficient manner.

Finally, you have the Database, which is a collection of data stored in the form of a single unit. 

One important feature of a DBMS is that it helps reduce the redundancy in the data stored. Having the same data stored at multiple locations in a database is called redundancy. 

To eliminate and reduce the redundancy in the database, normalization is used.

Normalization is the process of structuring the data in an RDBMS by removing anomalies. It is important to enable easy retrieval of data from the database as well as to add or delete data without losing consistency.   
  
This might be implemented with the help of “Normal Forms” in DBMS. These normal forms help in establishing relations in a relational database instead of having to redefine existing fields again and again. In this way, normalization reduces redundancy.

## What is SQL?

SQL is a database language. SQL is used widely and almost all Relational Database Management Systems can recognize it.

SQL contains a set of commands that enable you to create a database. You can also use it to execute commands in your Relational Database Management System.

SQL has certain advantages which have helped it thrive from the 1970s until now. It is widely accepted by both people and platforms, in part because of the following features:

* SQL is fast
* SQL is a very high-level language
* SQL is a platform-independent language
* SQL is a standardized language
* SQL is a portable language 

Along with all the features mentioned above, you need almost no coding skills to work with SQL.

SQL performs a variety of tasks like creating, altering, maintaining and retrieving data, setting properties, and so on. All the tasks are done based on the commands you write, and these commands are grouped into various categories like DDL commands, DML commands, DCL commands, and so on. 

Let's discuss some of the frequently used commands and their types.

### DDL commands

DDL stands for Data Definition Language. It includes the set of commands that you use to perform various tasks related to data definition. You use these commands to specify the structure of the storage and methods through which you can access the database system.

You use DDL commands to perform the following functions:

* To create, drop, and alter.
* To grant and revoke various roles and privileges.
* Maintenance commands

Example DDL commands include `CREATE`, `ALTER`, `DROP`, and `TRUNCATE`.

### DML commands

DML stands for Data Manipulation Language. As the name suggests, it consists of commands which you use to manipulate the data. 

You use these commands for the following actions:

* Deletion
* Insertion
* Retrieval
* Modification

Example DML commands are `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

### TCL commands

TCL stands for Transaction Control Language. As the name says, you use these commands to control and manage transactions.

One complete unit of work that involves various steps is called a transaction.

You use these commands for the following purposes:

* To create savepoints
* To set properties of the transaction going on
* To undo the changes to the database (permanent)
* To make changes in the database (permanent)

Example TCL commands include `COMMIT`, `ROLLBACK`, and `SAVE TRANSACTION`.

## How to Write Basic Queries in SQL

There are various keywords you use in SQL like SELECT, FROM, WHERE, and others. These SQL keywords are not case-sensitive.

To create a table called Student that has a name, roll numbers, and marks in it, you can write: 

```sql
CREATE TABLE student
(Name char(20)  NOT NULL,
Rollno int,
Marks int );
```

Here CREATE, TABLE, and NOT NULL are keywords. You use CREATE and TABLE to create a table and NOT NULL to specify that the column cannot be left blank while making a record.

To make a query from a table, you'll write:  

```sql
SELECT what_to_select FROM table_name WHERE condition_to_satisfy.
```

You use the ‘select’ keyword to pull the information from a table. The ‘From’ keyword selects the table from which the information is to be pulled. The ‘where’ keyword specifies the condition to be specified.

For example, say we want to retrieve the marks from the student table that has data for marks, roll numbers, and names. The command would be as follows:

```sql
SELECT Name FROM student WHERE marks>95
```

If you want to learn more about SQL for beginners, you can [check out this cheatsheet](https://www.freecodecamp.org/news/learn-sql-in-10-minutes/) that'll teach you the basics pretty quickly.

You can also go through this [Relational Database Course for Beginners](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/) to get a more solid understanding of the query language.

## Why Are DBMS and SQL Important?

Being able to work with DBMS and SQL are some of the most critical skills in today’s world. After all, you know what they say - "Data is the new oil." So you should know how to work with it effectively.

Here are a few reasons why you should learn how to use at least one DBMS and SQL.

## Reasons to Learn How to Use a DBMS

### If you're storing an extremely large amount of data

If your organization needs to store a huge amount of data, you'll want to use a DBMS to keep them organized and be able to access them easily. 

DBMS store the data in a very logical manner making it very easy to work with a humongous amount of Data. You can read more about database management 	 systems in [this tutorial by freeCodeCamp](https://www.freecodecamp.org/news/sql-and-databases-full-course/), [in this Wiki](https://en.wikipedia.org/wiki/SQL), [and on Scaler](https://www.scaler.com/topics/dbms/) for a better understanding of data storage in DBMS.

### If you're doing data mining

Data mining is the process of extracting usable data that includes only relevant information from a very large dataset. Using a DBMS, you can perform data mining very efficiently.   
  
For managing the data, you use [CRUD operations](https://www.freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app/) which stands for Create, Read, Update, and Delete. You can perform these operations with a DBMS easily and efficiently.

### Integrity constraint and scalability

The data you store in your database satisfies integrity constraints. Integrity constraints are the set of rules that are already defined and which are responsible for maintaining the quality and consistency of data in that database. The DBMS makes sure that the data is consistent.   
  
Scalability is another important feature of a DBMS. You can insert a lot of data into a database very easily and it will be accessible to the user quickly and with some basic queries.   
  
You do not need to write new code and spend lots of time and money on expanding the same database.

### When you have multiple user interfaces

When you're using a DBMS, you can have multiple users access the system at the same time. Just like in a UNIX operating system two users can log into a single account at the same time. 

### Security

DBMS makes storing data simple. You can also add security permissions on data access to make sure access is restricted and the privacy of the data remains intact.   
  
DBMS protects the confidentiality, availability, integrity, and consistency of the data stored in it.   
  
Along with making the data secure it reduces the time taken to develop an application and makes the process efficient.

### Learning a DBMS is an in-demand skill: 

Most companies out there – big or small – have lots of data to work with. And so they'll need people to analyze it. 

If you know how to use a DBMS, you can use those skills in almost all data-oriented technologies. So once you learn DBMS, it will be easy to work on any data-driven technology.

## Reasons to Learn SQL

Since SQL is a language that is used for database management, some of the above points also apply to learning it (such as data storage, data mining, and so on). 

Here are some of the additional reasons you should learn SQL.

### SQL is relatively easy to learn

SQL is quite easy to learn in the context of database management. SQL queries resemble the simple English we use in our day-to-day life. For example, if we want to make a table named Topics, we just have to use the command: 

```sql
CREATE TABLE Topics;
```

Understanding how a computer works helps you learn other skills related to computers like any programming language, spreadsheet software like MS Excel, and word processing software like MS word. 

You also use SQL to manage data on various platforms like [SQLite](https://www.sqlite.org/). 

### SQL is standardized

SQL was developed in the 1970s and has been extensively used for more than 50 years without many significant changes made to it.  
  
This makes it a standard skill for working with data, so typically when you apply for a job, they will be using SQL for data storage and management purposes.   
  
This general standardization also makes it easier to learn because you don't need to constantly update your knowledge, again and again, to be adept at it.

### SQL is easy to troubleshoot

Any error you get while using SQL will show a clear message about what's going on in very simple English. 

For example, if you are trying to use a table or any database that does not exist, it will show the error that the table or the database you are trying to access does not exist. 

There is the concept of exception handling in SQL also just like any other          	programming language. 

Exception handling is used for handling query runtime errors with the TRY CATCH construct. The TRY block is used to specify the set of statements that need to be checked for an error, while CATCH block executes certain statements in case an error has occurred. Exception handling is crucial for writing bug-free code.

### Easy to manipulate data 

Data manipulation refers to Adding (or inserting), deleting (removing), and modifying (updating) the data in a database.  
  
The data you store in the SQL is dynamic in nature which makes it easy for you to manipulate the data at any point in time. 

You can also retrieve data easily using a single-line SQL command.And if you want to present the data in the form of charts or graphs, then SQL plays a key role in that and makes data visualization easy for you. 

### Client and server data sharing

Whenever an application is used, the data stored in the database management system is retrieved based on the option selected by the user.   
  
To create and manage the servers, SQL is used. SQL is used to navigate through the large amount of data stored in the database management system.   


### Easy to sync data from multiple sources

You'll come across many cases when you have to get data from multiple sources and combine them to get the desired output. This means you'll be dealing with outputs from multiple sources at one time, which can be time-consuming and a tedious job.

But when you use SQL, it is much easier to handle data from multiple sources at the same time and combine them to get the desired output. 

In SQL you can use the UNION operation to combine data, like this:

```sql
SELECT name FROM customers
UNION
SELECT order_id FROM orders;
```

Using this combines the columns “name” and “order_id” from the “customers” and “orders” tables, respectively, and renders the combined table.

### Flexibility, versatility, and data analysis

SQL is a programming language, but the scope of this language is not only limited to programming tasks.   
  
You can use it for various purposes like in the finance sector and in sales and marketing, as well. By executing a few queries you can get the data you need and analyze it for your purposes. 

There are various roles that are specific to SQL like SQL developer, SQL database Administrator, Database Tester, SQL Data analyst DBA, Data Modeler, and more. You can learn more about salary insights [here](https://www.glassdoor.co.in/Salaries/sql-developer-salary-SRCH_KO0,13.htm).

Another important role is that of a data analyst. The process of cleansing, modeling, and transforming data to draw conclusions from it based on certain information is called Data analysis. 

The role of a data analyst is important in any organization as it helps in analyzing trends and making fast and flexible decisions on the basis of the available data. 

SQL and DBMS are two of the most in-demand skills for Data Analysis.

## How DBMS and SQL Work Together

DBMS and SQL are interdependent and cooperate to make the data organized and accessible. Now, let's understand how SQL works in synchronization with a Database Management System.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/How-Does-SQL-Work.png)
_How SQL + DBMS work_

  
SQL is the way you interact with the database management system. You use it to retrieve, insert, update, or delete data (CRUD operations), among other things.

When you execute a SQL command, the DBMS figures out the most efficient way to execute that command. The interpretation of the task to be performed is determined by the SQL engine.

The classic query engine is used to handle all the non-SQL queries, but it will not handle any logical files.

The query processor interprets the queries of the user and translates them into a database-understandable format.

The parser is used for translation purposes (in query processing). It also checks the syntax of the query and looks for errors, if present.

The optimisation engine, as the name suggests, optimises the performance of the database with the help of useful insights.

The DBMS engine is the underlying software component for performing CRUD operations on the database.

The file manager is used for managing the files in the database, one at a time.

And the transaction manager is used for managing the transactions to maintain concurrency while accessing data.

## Conclusion

In this article, we have discussed the basics of DBMS and SQL and why you should learn these skills. 

We have discussed the purpose and importance of DBMS and SQL, what they're used for, and what professionals who work with databases and SQL do.

After reading this article you have a good understanding of where knowledge of DBMS and SQL can take you.  
  
Happy Learning!

