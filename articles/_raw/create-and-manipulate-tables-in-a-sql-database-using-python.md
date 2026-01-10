---
title: How to Create and Manipulate Tables in a SQL Database Using Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-14T16:28:25.000Z'
originalURL: https://freecodecamp.org/news/create-and-manipulate-tables-in-a-sql-database-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/tables.JPG
tags:
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Python is a powerful programming language that you can use to interact
  with SQL databases. With the help of Python, you can create, manipulate, and interact
  with the tables in the SQL database.

  In this tutorial, we will be discussing how to create an...'
---

Python is a powerful programming language that you can use to interact with SQL databases. With the help of Python, you can create, manipulate, and interact with the tables in the SQL database.

In this tutorial, we will be discussing how to create and manipulate tables in a SQL database using Python.

### Prerequisites:

To follow along with this tutorial, you will need the following:

* A working knowledge of Python.
    
* A SQL database. For this tutorial, we will be using SQLite.
    

## How to Create a Table in a SQL Database Using Python

To create a table in a SQL database using Python, we first need to establish a connection to the database. For this tutorial, we will be using the SQLite database. SQLite is a lightweight, serverless database that is ideal for small projects.

To connect to the SQLite database, we will be using the built-in SQLite3 module in Python.

Here is the code to create a table in our SQLite database using Python:

```python
import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# create a table
c.execute('''CREATE TABLE employees
             (id INT PRIMARY KEY NOT NULL,
              name TEXT NOT NULL,
              age INT NOT NULL)''')

# save the changes
conn.commit()

# close the connection
conn.close()
```

In the above code, we first established a connection to the SQLite database using the `connect` method of the `sqlite3` module. We then created a cursor object using the `cursor` method.

Next, we executed a SQL query to create a table named `employees` with three columns: `id`, `name`, and `age`. The `id` column is set as the primary key, which means that each record in the table will have a unique `id` value. The `name` and `age` columns are set as `NOT NULL`, which means that they cannot be empty.

Finally, we saved the changes using the `commit` method and closed the connection using the `close` method.

## How to Insert Data into a Table

Now that we have created a table, we can insert data into it. Here is the code to insert data into the `employees` table:

```python
import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# insert data into the table
c.execute("INSERT INTO employees (id, name, age) VALUES (1, 'John Doe', 30)")
c.execute("INSERT INTO employees (id, name, age) VALUES (2, 'Jane Doe', 25)")

# save the changes
conn.commit()

# close the connection
conn.close()
```

In the above code, we inserted two records into the `employees` table using the `execute` method. We passed in two SQL queries, one for each record.

## How to Select Data from a Table

Now that we have inserted data into the `employees` table, we can retrieve it using the `SELECT` statement. Here is the code to select data from the `employees` table:

```python
import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# select data from the table
c.execute("SELECT * FROM employees")

# fetch all the records
records = c.fetchall()

# print the records
for record in records:
    print(record)

# close the connection
conn.close()
```

In the above code, we selected all the records from the `employees` table using the `SELECT` statement. We then fetched all the records using the `fetchall` method and printed them using a for a loop.

## How to Update Data in a Table

To update data in a table, we use the `UPDATE` statement. Here is the code to update data in the `employees` table:

```python
import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# update data in the table
c.execute("UPDATE employees SET age = 35 WHERE name = 'John Doe'")

# save the changes
conn.commit()

# select data from the table
c.execute("SELECT * FROM employees")

# fetch all the records
records = c.fetchall()

# print the records
for record in records:
    print(record)

# close the connection
conn.close()
```

In the above code, we updated the age of the record with the name 'John Doe' to 35 using the `UPDATE` statement. We then saved the changes using the `commit` method.

## How to Delete Data from a Table

To delete data from a table, we use the `DELETE` statement. Here is the code to delete data from the `employees` table:

```python
import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# delete data from the table
c.execute("DELETE FROM employees WHERE name = 'Jane Doe'")

# save the changes
conn.commit()

# select data from the table
c.execute("SELECT * FROM employees")

# fetch all the records
records = c.fetchall()

# print the records
for record in records:
    print(record)

# close the connection
conn.close()
```

In the above code, we deleted the record with the name 'Jane Doe' from the `employees` table using the `DELETE` statement. We then saved the changes using the `commit` method.

## Conclusion

In this article, we discussed how to create and manipulate tables in a SQL database using Python.

We covered how to create a table, insert data into it, select data from it, update data in it, and delete data from it. We also provided the necessary code to accomplish these tasks.

By following the steps outlined in this tutorial, you can create and manipulate tables in any SQL database using Python.

Let’s connect on [Twitter](https://twitter.com/Olujerry19) and [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
