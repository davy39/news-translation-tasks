---
title: How to Use MySQL Transactions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-10T21:35:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-mysql-transactions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/White-Minimalist-Dental-Clinic-Facebook-Cover--1-.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
seo_title: null
seo_desc: "By Aisha Bukar\nWhat is a Database Transaction and Why is it Important?\n\
  A database transaction is a single area of the database where multiple data operations\
  \ are carried out and written as a whole. \nThese operations can be create, read,\
  \ update, or de..."
---

By Aisha Bukar

## What is a Database Transaction and Why is it Important?

A database transaction is a single area of the database where multiple data operations are carried out and written as a whole. 

These operations can be create, read, update, or delete operations. 

During the process of a transaction, the database is in an inconsistent state because there are ongoing operations that are making changes to the database. The DB returns to a more consistent state when the operations have been committed. 

For a transaction to be successful, it means that every operation carried out has been committed.

Database transactions are very important in ensuring the consistency of your database when multiple operations are being performed at the same time. It also gives you a way to recover changes that may have occurred due to the failure or accidental misuse of an operation.

## Overview of MySQL and its Transaction Support

MySQL databases offer support for database transactions by providing statements to initiate these transactions. It gives us the following in-built queries:

"**START TRANSACTION / BEGIN**": this query triggers the start of a transaction.

"**COMMIT**": this query allows the changes made to the database to become permanent. You can set your database to auto-commit changes by using the following query:

```mysql
SET autocommit = 1;
```

"**SET**": this query allows you to set your commit by enabling the operations to commit automatically or disabling the auto-commit. That is, your operations won't commit automatically until you call the "commit" query.

```mysql
/*Disabling the auto-commit  */
SET autocommit = 0;
/* OR */
SET autocommit = OFF;

/* Enabling the operations to automatically commit every operation*/
SET autocommit = 1;
/* OR */
SET autocommit = ON
```

"**ROLLBACK**": this query allows you to undo the changes you have made to the database, therefore returning the database to its previous (last commit) state.

## ACID Properties of Transactions

ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. Let's go through each term to understand how they relate to transactions.

![ACID properties](https://www.freecodecamp.org/news/content/images/2023/02/Colorful-Villager-Bingo-Card-Instagram-Story.png)

### Atomicity

Atomicity in a database transaction means that all the changes made during that transaction are treated as one "bundle" of changes. This means that when you are trying to modify your database, it's either all of the changes happen at the same time, or none of them happen at all. 

It's like when you and your teammates are building an application. If one person writes a line of code, and then another person takes it off, it's like nothing happened. But if everyone keeps adding different lines of code and nobody takes any off, then the code base keeps getting bigger.

### Consistency

Consistency in databases means that the data stored in the database is always in a valid and consistent state. For example, if the database contains any constraints such as primary keys, foreign keys, and so on, it should always conform to the rules surrounding the constraint.

For example, let's say a table has a rule that says a specific column must be an integer value. Consistency ensures that this rule is always followed and data inserted into the column can only be of the integer value data type.

### Isolation

The ability of multiple transactions to execute without interfering with one another is known as Isolation. The isolation level of a transaction determines how the changes made by that transaction are visible to other transactions.

MYSQL supports the following isolation levels:

**i. READ UNCOMMITTED**: In the READ UNCOMMITTED level, which is also the lowest isolation level, a transaction can read data that is yet to be committed by other transactions. This means that other transactions can alter the data that another transaction is currently reading, but these changes may not be visible until the operation is complete.

**ii. READ COMMITTED**: This is the second-to-the-lowest isolation level. Here, a transaction is only able to read data that has already been committed by other transactions. This means that other transactions can alter the data that a transaction is currently reading but these changes will not be visible until the other transaction has been committed.

**iii. REPEATABLE READ**: This is a higher level of isolation. A transaction at this level is only able to read data that has already been committed by other transactions, and it also restricts other transactions from altering the data that is currently being read. This means that even though other transactions have committed changes, if a transaction executes a SELECT statement again, it will always see the same data.

**iv. SERIALIZABLE**: This is the highest level of isolation. At this level, a transaction is only able to read data that has already been committed by other transactions. It also prevents other transactions from altering the data that the transaction is reading and from adding new rows that would be visible to the current transaction.

MySQL uses the READ COMMITTED isolation level by default. However, it is possible to change the isolation level by using the "SET TRANSACTION ISOLATION LEVEL" statement.

### Durability

Durability ensures that your data remains safe, even in the event of unforeseen circumstances. When a transaction is committed, its changes must remain in the database, even if it experiences a malfunction or a power outage. 

But how does MySQL ensure durability? It makes use of write-ahead logging. This technique involves writing a log of the transaction to disk before making any changes to the database. 

The log acts as a road map for the database and contains information about the changes that will be made in case of an unexpected system failure. In the event of this, the database can be recovered from the log, and the changes made in the transaction will be replayed to make sure that the database is still in a consistent state. 

It's important to keep in mind that while write-ahead logging can have a performance impact, it's a small price to pay for the peace of mind that comes with knowing your data is safe.

## Locking and Concurrency in MySQL Transactions

Locking is a technique that is used to prevent race conditions. A race condition is a process where multiple transactions are trying to access the same data at the same time. 

MySQL uses different types of locks to control access to data in a transaction. These include:

1. **Shared locks**: This allows multiple transactions to read the same data at the same time but restricts any of them from writing or making changes to it.
2. **Exclusive locks**: This prevents different transactions from reading or writing the same data at the same time.
3. **Intent locks**: This is used to specify that a transaction is planning to read or write a certain section of data.
4. **Row-level locks**: This allows transactions to lock only the specific rows they need to access, rather than the entire table.

Concurrency is a method where multiple transactions can run simultaneously without interfering with each other's data.

MySQL uses a multi-version concurrency control (MVCC) mechanism. This allows multiple transactions to read and write to the same data at the same time without conflict. 

I'm sure you are wondering how this can be achieved. Well, each transaction sort of captures the data it is about to modify at the start of the transaction and writes its changes to an entirely different version of the data. This allows other transactions to continue working with the original version of the data without a conflict of interest.

To achieve high concurrency, it's important to keep the transactions as short as possible and avoid long-running transactions that hold locks for extended periods.

## How to Create and Use Transactions in MySQL

The first thing required is to start the transaction using the "START TRANSACTION" statement. Here is an example:

```mysql
START TRANSACTION;
    INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
    UPDATE accounts SET balance = SUM(balance) WHERE name = 'John Doe';
```

In this example, a new transaction is started with the START TRANSACTION statement. The next two statements, an insert and an update, are executed within the transaction.

The next step is to commit the changes to make sure they are permanent. We do this by including the COMMIT statement in the query.

```mysql
START TRANSACTION;
    INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
    UPDATE accounts SET balance = SUM(balance) WHERE name = 'John Doe';
COMMIT;
```

If by any chance there was an error during the transaction and you want to undo the changes, you can use the ROLLBACK statement. Then the transaction will be rolled back and the insert and update statements will not be executed. This means no change will take place in the database.

```mysql
START TRANSACTION;
    INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
    UPDATE accounts SET balance = SUM(balance) WHERE user_id=15;
ROLLBACK;
```

## How to Use the InnoDB Storage Engine for Transactions

InnoDB is a storage engine for MySQL that has many functions that can improve your database performance. Some of these features include the ability to group and execute multiple SQL statements together, encrypt our data, create and drop indexes without affecting the database performance, handle CPU as well as large data, and many more.

To use InnoDB for transactions in MySQL, you will need to make sure that your tables are using the InnoDB storage engine. You can check this by running the following query:

```mysql
SHOW TABLE STATUS FROM your_database_name;
```

This will show you the storage engine used by each table in your database. It is also possible for you to set the default storage engine to InnoDB by modifying the `my.cnf` configuration file, or by running the following command:

```mysql
SET storage_engine=InnoDB;
```

After running this query, your database tables should be using the InnoDB storage engine. We can then begin to perform the functions we listed above.

```mysql
START TRANSACTION;
    UPDATE accounts SET balance = 50 WHERE user_id = 1;
    UPDATE accounts SET balance = 2000 WHERE user_id = 2;
COMMIT;
```

This is a simple example of a transaction that updates two rows in the "accounts" table. If any of the statements fails, the entire transaction will be rolled back, and no changes will be made to the database.

Additionally, InnoDB also provides some additional features like row-level locking, foreign key constraints, and crash recovery which makes it more robust and reliable than other storage engines, particularly for transactional workloads.

## How to Handle Errors and Exceptions in Transactions

Handling errors and exceptions are important, especially when working with transactions. 

A method of handling errors and exceptions in transactions is to use a try-catch block. In MySQL, you can use the SIGNAL and RESIGNAL statements to raise and handle exceptions within a transaction.

Here's an example of how you might use a try-catch block to handle an exception within a transaction:

```mysql
START TRANSACTION;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        START TRANSACTION
            ROLLBACK;
            RESIGNAL;
        END;
    UPDATE accounts SET balance = 5000 WHERE user_id = 1;
    UPDATE accounts SET balance = 1000 WHERE user_id = 2;
    IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance';
    END IF;
COMMIT;
```

The DECLARE EXIT HANDLER FOR SQLEXCEPTION block is used to catch any SQL exceptions that occur within the transaction. 

If an exception is caught, the transaction is rolled back using the ROLLBACK statement. Then the RESIGNAL statement raises the exception again so that it can be handled by an outer try-catch block, if any.

The IF statement checks if the balance of user_id =1 is less than zero. If true, the SIGNAL statement raises an exception with a specific SQLSTATE '45000' and a message "Insufficient balance".

It's worth knowing that if an exception occurs within a transaction, any changes that may have occurred during the transaction will be rolled back, regardless of whether or not the exception is handled.

## How to Use Savepoints in MySQL Transactions

It's good practice to use the SAVEPOINT statement within a transaction to set savepoints. This makes it possible for you to rollback to a specific point in the transaction, rather than rolling back the entire transaction. 

Here is an example of how you might use the SAVEPOINT statement within the previous example:

```mysql
START TRANSACTION;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        START TRANSACTION
            ROLLBACK TO SAVEPOINT my_savepoint;
            RESIGNAL;
        END;
    UPDATE accounts SET balance = 5000 WHERE user_id = 1;
    UPDATE accounts SET balance = 1000 WHERE user_id = 2;
    IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance';
    END IF;
COMMIT;
```

You use the SAVEPOINT statement to set a savepoint named "my_savepoint" before the two updates. If an exception is caught, the ROLLBACK statement rolls back the transaction to the savepoint, using the clause "TO SAVEPOINT my_savepoint", rather than rolling back the entire transaction. 

This will undo only the changes made after the savepoint, and leave the changes made before the savepoint intact.

## Conclusion

Transaction operations are quite important. They help developers ensure that their database remains in a consistent state and makes it easy to reverse changes if necessary. 

MySQL provides features such as commit, rollback, and savepoint to make the process much easier. It also provides robust engines like InnoDB which support these features as well. 

For further information on MySQL transactions, you can check out the official [documentation](https://dev.mysql.com/doc/refman/8.0/en/sql-transactional-statements.html).

