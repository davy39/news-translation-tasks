---
title: How to Read and Write Data to a SQL Database Using Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-08T19:27:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-and-write-data-to-a-sql-database-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/SQL-Queries.JPG
tags:
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Databases are a crucial component of modern-day software systems. And SQL
  databases are one of the most widely used types of databases.

  They are ideal for managing data in a structured and organized way, and they are
  widely used in various applicatio...'
---

Databases are a crucial component of modern-day software systems. And SQL databases are one of the most widely used types of databases.

They are ideal for managing data in a structured and organized way, and they are widely used in various applications, including e-commerce, healthcare, finance, and more.

In this article, we will discuss how to read and write data to a SQL database using Python. We will provide examples of how to connect to a SQL database using Python and how to execute SQL commands to perform basic database operations such as insert, update, delete, and select.

### Prerequisites

Before we dive into the code examples, make sure that you have the following prerequisites installed on your system:

* Python 3.x
    
* A SQL database management system (for example, MySQL, PostgreSQL, SQLite, and so on)
    
* A SQL database client (for example, MySQL Workbench, pgAdmin, DB Browser for SQLite, and so on)
    

## How to Connect to a SQL Database using Python

Python has several libraries for connecting to SQL databases, including `pymysql`, `psycopg2`, and `sqlite3`. In this section, we will discuss how to connect to a MySQL database using `pymysql`.

First, we need to install the `pymysql` library using pip:

```python
pip install pymysql
```

Next, we need to import the `pymysql` library and connect to the MySQL database using the following code:

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
```

In the code above, we first import the `pymysql` library. Then, we use the `connect()` function to establish a connection to the MySQL database. We need to provide the following parameters to the `connect()` function:

* `host`: the hostname or IP address of the MySQL server
    
* `user`: the username used to authenticate with the MySQL server
    
* `password`: the password used to authenticate with the MySQL server
    
* `db`: the name of the database to connect to
    
* `charset`: the character set to use for the connection
    
* `cursorclass`: the type of cursor to use for the connection (in this case, we use the `DictCursor` cursor, which returns rows as dictionaries)
    

Once we have established a connection to the MySQL database, we can execute SQL commands to perform various operations on the database.

## How to Insert Data into a SQL Database using Python

To insert data into a SQL database using Python, we need to execute an SQL `INSERT` command. In the following example, we will insert a new record into a MySQL database:

```python
try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Commit changes
    conn.commit()

    print("Record inserted successfully")
finally:
    conn.close()
```

In the code above, we use a `try`/`finally` block to ensure that the database connection is closed properly. Within the `try` block, we use the `cursor()` function to create a new cursor object. We then execute the `INSERT` command using the `execute()` function and pass in the values that we want to insert into the database.

Once the `execute()` function has been called, we use the `commit()` function to commit the changes to the database. Finally, we close the database connection using the `close()` function.

## How to Update Data in a SQL Database using Python

To update data in a SQL database using Python, we need to execute an SQL `UPDATE` command. In the following example, we will update an existing record in a MySQL database:

```python
try:
    with conn.cursor() as cursor:
        # Update a record
        sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
        cursor.execute(sql, ('newpassword', 'john@example.com'))

    # Commit changes
    conn.commit()

    print("Record updated successfully")
finally:
    conn.close()
```

In the code above, we use a `try`/`finally` block to ensure that the database connection is closed properly. Within the `try` block, we use the `cursor()` function to create a new cursor object. We then execute the `UPDATE` command using the `execute()` function and pass in the new value that we want to update and the condition that specifies which record to update.

Once the `execute()` function has been called, we use the `commit()` function to commit the changes to the database. Finally, we close the database connection using the `close()` function.

## How to Delete Data from a SQL Database using Python

To delete data from a SQL database using Python, we need to execute an SQL `DELETE` command. In the following example, we will delete a record from a MySQL database:

```python
try:
    with conn.cursor() as cursor:
        # Delete a record
        sql = "DELETE FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('john@example.com',))

    # Commit changes
    conn.commit()

    print("Record deleted successfully")
finally:
    conn.close()
```

In the code above, we use a `try`/`finally` block to ensure that the database connection is closed properly. Within the `try` block, we use the `cursor()` function to create a new cursor object. We then execute the `DELETE` command using the `execute()` function and pass in the condition that specifies which record to delete.

Once the `execute()` function has been called, we use the `commit()` function to commit the changes to the database. Finally, we close the database connection using the `close()` function.

## How to Read Data from a SQL Database using Python

To read data from a SQL database using Python, we need to execute an SQL `SELECT` command. In the following example, we will read data from a MySQL database and print the results:

```python
try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)
finally:
    conn.close()
```

In the code above, we use a `try`/`finally` block to ensure that the database connection is closed properly. Within the `try` block, we use the `cursor()` function to create a new cursor object. We then execute the `SELECT` command using the `execute()` function.

Once the `execute()` function has been called, we use the `fetchall()` function to retrieve all rows returned by the query. We then loop through the rows and print the results.

## Conclusion

In this article, we discussed how to read and write data to a SQL database using Python.

We provided examples of how to connect to a MySQL database using `pymysql`, and how to execute SQL commands to perform basic database operations such as insert, update, delete, and select.

By following the code examples provided in this article, you can quickly and easily read and write data to a SQL database using Python.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
