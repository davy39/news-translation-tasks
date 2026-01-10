---
title: SQL INSERT Statement – How to Insert Data into a Table in SQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-01T18:54:21.000Z'
originalURL: https://freecodecamp.org/news/sql-insert-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/SQL-Insert-Statement.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By Karlgusta Annoh

  In this tutorial, you''ll learn how to use the SQL INSERT statement.

  We''ll discuss the syntax of INSERT, and then we''ll use an example to show all
  the different ways you can use INSERT. We''ll also combine it with other helpful
  claus...'
---

By Karlgusta Annoh

In this tutorial, you'll learn how to use the SQL INSERT statement.

We'll discuss the syntax of INSERT, and then we'll use an example to show all the different ways you can use INSERT. We'll also combine it with other helpful clauses to perform more complex operations.

## Prerequisites
* Basic understanding of SQL

## Syntax of SQL `INSERT` statement

You use the SQL INSERT INTO statement to insert new records in a table. The syntax of the SQL INSERT INTO statement is:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

## Example of SQL `INSERT`

Let's say we have a table called `Persons` with the following columns:

* `PersonID`
* `LastName`
* `FirstName`
* `Address`
* `City`

Let's first create the table:

![Create a table in SQL](https://user-images.githubusercontent.com/33565767/204135303-4ce17e6e-9ed9-4083-80e7-32a644cbacd9.png 'Create a table in SQL')

I am using this query to create the table:

```sql
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

On running the query will create the table.

![Empty table we created](https://user-images.githubusercontent.com/33565767/204135389-e4c47686-0232-4d7b-89cd-d94a10a9b7af.png 'Empty table we created')


We can insert a new record into the `Persons` table by using the following SQL statement:

```sql
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) 
VALUES (1, 'Wilson', 'John', '123 Main St.', 'Anytown');
```

![Inserting data into persons table](https://user-images.githubusercontent.com/33565767/204135468-a58b036f-eb22-4da0-9fb8-a42a2ffd31b2.png 'Inserting data into persons table')

Here is the table with the data inserted:

![Table after data has been inserted](https://user-images.githubusercontent.com/33565767/204135554-ffab65c8-5c0b-465c-a5b4-c1913a343eb1.png 'Table after data has been inserted')

## How to Insert Multiple Records with the `INSERT` Statement

We can insert multiple records into a table by using a single SQL statement. The following SQL statement inserts three new records into the `Persons` table:

```sql
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (2, 'Smith', 'Mary', '456 Maple St.', 'Anytown'),
       (3, 'Jones', 'David', '789 Elm St.', 'Anytown'),
       (4, 'John', 'David', '789 Elm St.', 'Meru');
```

When running the query on TablePlus, it will look like this:

![Insert multiple records](https://user-images.githubusercontent.com/33565767/204137155-1b131742-5765-46e6-8f34-44dd9accd55d.png 'Insert multiple records')

Here is the table with the data inserted:

![The table with the records inserted](https://user-images.githubusercontent.com/33565767/204135891-0868ec8d-6278-43b3-95e2-f143be29b919.png 'The table with the records inserted')


## How to Insert Records from Another Table

We can insert records into a table from another table using the SQL INSERT INTO SELECT statement.

The following SQL statement inserts all records from the `Persons` table into the `PersonsBackup` table:

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons;
```

In order to run this query, we need to create a new table called `PersonsBackup`:

```sql
CREATE TABLE PersonsBackup (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    PRIMARY KEY (PersonID)
);
```

![Create Table PersonsBackup](https://user-images.githubusercontent.com/33565767/204136076-03bc5e9b-dc54-4e07-92b5-16ed695f6d58.png 'Create Table PersonsBackup')

Now we can run the query to insert the records from the `Persons` table into `PersonsBackup` table:

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons;
```

![Inserting from PersonsBackup from Persons table](https://user-images.githubusercontent.com/33565767/204136180-97a0266a-c753-4f68-8f62-c418906a487a.png 'Inserting from PersonsBackup from Persons table')

Here is the table with the data inserted:

![Records inserted from PersonsBackup from Persons table](https://user-images.githubusercontent.com/33565767/204136259-7abff786-659a-4b78-9077-2d3462496dcd.png 'Records inserted from PersonsBackup from Persons table')


## How to Insert Records from a SELECT Statement

We can insert records from a SELECT statement into a table by using the SQL INSERT INTO SELECT statement. The following SQL statement inserts all records from the `Persons` table into the `PersonsBackup` table:

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons;
```

![Inserting from PersonsBackup from Persons table](https://user-images.githubusercontent.com/33565767/204136180-97a0266a-c753-4f68-8f62-c418906a487a.png 'Inserting from PersonsBackup from Persons table')

Here is the table with the data inserted:

![Records inserted from PersonsBackup from Persons table](https://user-images.githubusercontent.com/33565767/204136259-7abff786-659a-4b78-9077-2d3462496dcd.png 'Records inserted from PersonsBackup from Persons table')

## How to Insert Records from a SELECT Statement with a WHERE Clause

We can insert records into a table from a SELECT statement with a WHERE clause by using the SQL INSERT INTO SELECT statement. 

The following SQL statement inserts all records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`:

Let's first delete the records from the `PersonsBackup` table:

```sql
DELETE FROM PersonsBackup;
```

![Deleting records from PersonsBackup](https://user-images.githubusercontent.com/33565767/204136584-667bcd37-f9b6-4103-a0a8-e140b11bd11a.png 'Deleting records from PersonsBackup')

Now that the records have been deleted, we can insert the records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`:

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown';
```

Inserting records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`:

![Record inserted from Persons table into PersonsBackup table where the City id Anytown](https://user-images.githubusercontent.com/33565767/204136655-7a104a0b-088a-4b15-8c39-0f735d706a67.png 'Record inserted from Persons table into PersonsBackup table where the City id Anytown')


Here is the table with the data inserted:

![Table where the data has been inserted](https://user-images.githubusercontent.com/33565767/204136695-b7bad680-5620-4558-8846-94b057ddb14d.png 'Table where the data has been inserted')


## How to Insert Records from a SELECT Statement with a WHERE Clause and a LIMIT Clause

We can insert records into a table from a SELECT statement with a WHERE clause and a LIMIT clause by using the SQL INSERT INTO SELECT statement. 

The following SQL statement inserts the first 10 records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`:

Let's first create at least 10 records in the `Persons` table where the `City` is `Anytown`:

```sql
INSERT INTO Persons(PersonID, LastName, FirstName, Address, City) 
VALUES (5, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (6, 'Smith', 'Mary', '456 Maple St.', 'Anytown'),
       (7, 'Jones', 'David', '789 Elm St.', 'Anytown'),
       (8, 'John', 'David', '789 Elm St.', 'Anytown'),
       (9, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (10, 'Smith', 'Mary', '456 Maple St.', 'Anytown'),
       (11, 'Jones', 'David', '789 Elm St.', 'Anytown'),
       (12, 'John', 'David', '789 Elm St.', 'Anytown'),
       (13, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (14, 'Smith', 'Mary', '456 Maple St.', 'Anytown');
```

The values have been inserted into the `Persons` table:

![Insert into Persons table](https://user-images.githubusercontent.com/33565767/204225226-f1a52566-78bd-46fb-af84-8b8e5e5ce49e.png 'Insert into Persons table')

The table now has 14 records:

![The data inserted into Persons table](https://user-images.githubusercontent.com/33565767/204225456-754695bb-68de-4194-93d1-3c1a5a6c9732.png 'The data inserted into Persons table')

We can also add records with the city name being anything other than `Anytown`:

```sql
INSERT INTO Persons(PersonID, LastName, FirstName, Address, City)
VALUES (15, 'Jones', 'David', '789 Elm St.', 'New York'),
       (16, 'John', 'David', '789 Elm St.', 'New York'),
       (17, 'Wilson', 'John', '123 Main St.', 'New York'),
       (18, 'Smith', 'Mary', '456 Maple St.', 'New York');
```

The values have been inserted into the `Persons` table:

![The values inserted into the Persons table](https://user-images.githubusercontent.com/33565767/204225867-02987894-f103-45be-a6b6-2ce8d0adcc81.png 'The values inserted into the Persons table')

The data with different cities has been inserted into the `Persons` table:

![The records with different cities has been inserted into the Persons table](https://user-images.githubusercontent.com/33565767/204226482-49f01867-b989-4234-8669-401dc99d820f.png 'The records with different cities has been inserted into the Persons table')


Now that we have at least 10 records in the `Persons` table where the `City` is `Anytown`, we can insert the first 10 records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`:

We will first delete the records from the `PersonsBackup` table:

```sql
DELETE FROM PersonsBackup;
```

![Deleting from PersonsBackup table](https://user-images.githubusercontent.com/33565767/204227157-4c2a54c2-8f5c-4dd5-a917-e7bb2aeb4878.png 'Deleting from PersonsBackup table')

The `PersonsBackup` table is now empty:

![The PersonsBackup table is now empty](https://user-images.githubusercontent.com/33565767/204227440-a776129c-ee5a-4eed-8c52-c16642d149c8.png 'The PersonsBackup table is now empty')

We can now insert the first 10 records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`:

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' LIMIT 10;
```

You use the limit clause to limit the number of records to be inserted into the `PersonsBackup` table. In this case, we are inserting the first 10 records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`.

You use the where clause to specify the condition that must be met for the records to be inserted into the `PersonsBackup` table. In this case, the `City` must be `Anytown` for the records to be inserted into the `PersonsBackup` table.

When we run the above query, the first 10 records from the e`Persons` table where the `City` is `Anytown` will be inserted into the `PersonsBackup` table:

Running the above query:

![Running the above query, the first 10 records from Persons table where the City is Anytown will be inserted into PersonsBackup table](https://user-images.githubusercontent.com/33565767/204228608-464fb97f-1c24-452b-ae9e-17d02ffaa912.png 'Running the above query, the first 10 records from Persons table where the City is Anytown will be inserted into PersonsBackup table')


The records have been inserted into the `PersonsBackup` table:

![The 10 records inserted from Persons table](https://user-images.githubusercontent.com/33565767/204228789-407882d8-9e6e-4b47-a08b-bfe0da268204.png)


## How to Insert Records from a SELECT Statement with a WHERE Clause and an ORDER BY Clause

We can insert records from a SELECT statement with a WHERE clause and an ORDER BY clause into a table by using the SQL INSERT INTO SELECT statement. 

The following SQL statement inserts all records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown` and orders the records by `LastName`.

Let's first delete the records from `PersonsBackup` table:

```sql
DELETE FROM PersonsBackup;
```

![Delete from PersonsBackup](https://user-images.githubusercontent.com/33565767/204490301-d3a4a651-8b0b-4ace-8ddc-6c049a5170bd.png 'Delete from PersonsBackup')

The `PersonsBackup` table is now empty.

Now, we can insert all records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown` and order the records by `LastName`:

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' ORDER BY LastName;
```

![Inserting into PersonsBackup table from Persons table where city is Anytown and ordering by lastname](https://user-images.githubusercontent.com/33565767/204491737-1ca6933c-6f09-4085-908c-b54f34440aa4.png 'Inserting into PersonsBackup table from Persons table where city is Anytown and ordering by lastname')

Here is the `Persons` table before the query is run:

![The Persons table before the query is run](https://user-images.githubusercontent.com/33565767/204492282-fb2e2e81-ccf6-44df-94f5-15291fbce90c.png 'The Persons table before the query is run')

Here is the `PersonsBackup` table after the records have been inserted:

![The PersonsBackup table after the records have been inserted](https://user-images.githubusercontent.com/33565767/204492653-6a893c30-2446-4a06-b1ca-e2a44ded0f0a.png 'The PersonsBackup table after the records have been inserted')


## How to Insert Records from a SELECT Statement with a WHERE Clause, an ORDER BY Clause, and a LIMIT Clause

We can insert records into a table from a SELECT statement with a WHERE clause and an ORDER BY clause and a LIMIT clause by using the SQL INSERT INTO SELECT statement. 

The following SQL statement inserts the first 10 records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown` and orders the records by `LastName`.

First, let's delete the records from `PersonsBackup` table:

```sql
DELETE FROM PersonsBackup;
```

Run the query above on your database management tool. I am using TablePlus.

After running the delete query, here is the result:

![Delete from PersonsBackup table](https://user-images.githubusercontent.com/33565767/204725197-abb4114e-d4bf-44dd-9931-f8e91e4f8b17.png 'Delete from PersonsBackup table')

The `PersonsBackup` table is now empty.

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' ORDER BY LastName LIMIT 10;
```

Running the above query on TablePlus:

![image](https://user-images.githubusercontent.com/33565767/204727587-e6bde08d-e2a4-4ea5-8496-a30ac3fc9341.png)

Here is the `PersonsBackup` table after the records have been inserted:

![Inserting into PersonsBackup table after selecting from Persons table where city is Anytown, being ordered by lastname and the limit is 10](https://user-images.githubusercontent.com/33565767/204727939-a4519f59-b30e-45ed-b95c-f6840effb87e.png 'Inserting into PersonsBackup table after selecting from Persons table where city is Anytown, being ordered by lastname and the limit is 10')


## How to Insert Records from a SELECT Statement with a WHERE Clause, an ORDER BY Clause, a LIMIT Clause, and an OFFSET Clause

We can insert records from a SELECT statement with a WHERE clause, an ORDER BY clause, a LIMIT clause, and an OFFSET clause by using the SQL INSERT INTO SELECT statement. 

The following SQL statement inserts the records from the `Persons` table into the `PersonsBackup` table where the `City` is `Anytown`. It orders the records by `LastName`, limits the records to 10, and skips the first 5 records.

We'll start with the `OFFSET` clause. The `OFFSET` clause is used to skip the first `n` records. In this case, we are skipping the first 5 records.

First, let's delete the records from the `PersonsBackup` table:

```sql
DELETE FROM PersonsBackup;
```

Run the query above on your database management tool.

After running the delete query, here is the result.

![Delete from PersonsBackup table](https://user-images.githubusercontent.com/33565767/204725197-abb4114e-d4bf-44dd-9931-f8e91e4f8b17.png 'Delete from PersonsBackup table')


```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' ORDER BY LastName LIMIT 10 OFFSET 5;
```

![Inserting into PersonsBackup table, selecting from PersonsTable where city is Anytown and ordering by lastname, while limiting to 10 and skipping the first 5 items](https://user-images.githubusercontent.com/33565767/204733392-3a08eb1d-6d42-45e2-8372-1ccd02eddcc3.png 'Inserting into PersonsBackup table, selecting from PersonsTable where city is Anytown and ordering by lastname, while limiting to 10 and skipping the first 5 items')

Since we have skipped the first 5 records, the first 5 records in the `Persons` table are not inserted into the `PersonsBackup` table. This means only 8 records out of 13 records are inserted into the `PersonsBackup` table, where City is equal to Anytown.

## Conclusion

In this tutorial, you have learned how to insert records into a table by using the SQL INSERT INTO statement. 

You have also learned how to insert records into a table with a SELECT statement by using the SQL INSERT INTO SELECT statement. 

If you want to learn more about SQL, check out this course: [SQL Tutorial - Full Database Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY&t=5s). It's free on freeCodeCamp's YouTube channel.





