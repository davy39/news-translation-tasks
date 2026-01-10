---
title: How to Use PostgreSQL in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-14T15:16:10.000Z'
originalURL: https://freecodecamp.org/news/postgresql-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/postgresql-in-python.png
tags:
- name: database
  slug: database
- name: postgres
  slug: postgres
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nThere are many different types of databases in use today.\
  \ We have centralized databases, commercial databases, cloud databases, distributed\
  \ databases, end-user databases, NoSQL databases, relational databases, and lots\
  \ more.  \nThis ..."
---

By Shittu Olumide

There are many different types of databases in use today. We have centralized databases, commercial databases, cloud databases, distributed databases, end-user databases, NoSQL databases, relational databases, and lots more.  
  
This article will focus on an example of a relational database (PostgreSQL) and how to query data from it. Other examples of relational databases include MySQL, MariaDB, and SQLite. 

In this tutorial, you will learn how to install, connect, and finally query a PostgreSQL database with Python.

To get started, let's ease into it by learning a bit more about PostgreSQL.

## What is PostgreSQL?

One of the most well-known open-source relational databases is PostgreSQL. It is used by developers and businesses of all sizes worldwide. 

In terms of global popularity, PostgreSQL is [ranked fourth](https://db-engines.com/en/ranking) by DB-Engines, and its popularity is growing. This shouldn't come as a surprise, given that many web and mobile applications, as well as analytical tools, use PostgreSQL databases.

PostgreSQL also has a robust ecosystem with a huge selection of add-ons and extensions that work well with the main database. For these reasons, PostgreSQL is a fantastic option whether you want to create your own custom database solution or need a transactional or analytical database.

Now that you know what PostgreSQL is, let's discuss how to connect to the database using Python.

## Getting Started

We must use a database connector library to connect to a PostgreSQL database instance from our Python script. We can pick from a variety of alternatives in Python, but [Psycopg2](https://www.psycopg.org/docs/) is the most well-known and widely-used one.

There are alternative libraries built entirely in Python, such as [pg8000](https://github.com/tlocke/pg8000) and [py-postgresql](https://github.com/python-postgres/fe), but we'll use Psycopg2 here.

### What is Psycopg2?

The Psycopg2 library uses the C programming language as a wrapper around the [libpq](https://www.postgresql.org/docs/current/libpq.html) PostgreSQL library to support the Python DB API 2.0 standards. The C implementation of Psycopg2 makes it incredibly quick and effective.

Using a SQL query, we can utilize Psycopg2 to get one or more rows from the database. With this library, we can also insert data into the database using a variety of single or batch inserting methods.

The library is like SQL (Structured Query Language) and it performs all the tasks and operations a query language can do. It is both Unicode and Python 3 friendly, and it also has thread safety (the same connection is shared by multiple threads).

It is made to run highly multi-threaded programs, which frequently produce and delete a lot of cursors and do a lot of simultaneous INSERTS or UPDATES. Psycopg2's features include client-side and server-side cursors, asynchronous communication, and notifications.

## How to Install Psycopg2

We must first install Psycopg2 in order to use it. We can install it via the terminal or command prompt using `pip`.

```python
#installation

pip install psycopg2
pip3 install psycopg2
```

If we also decide to install the connector library in a virtual environment, you can do so using this code:

```python
virtualenv env && source env/bin/activate
pip install psycopg2-binary
```

The Psycopg2 library and all of its dependencies will be installed into our Python virtual environment with this code snippet.

We have installed our connector, so let's start typing some queries.

## How to Query PostgreSQL using Python 

First, you'll need to create a new file and name it whatever you want. Then open it up in your IDE and start writing the code. 

The first thing to do is to import the library (this is very important). We will make use of two Psycogp2 objects:

* **Conection object**: The connection to a PostgreSQL database instance is managed by the connection object. It encapsulates a database session, created using the function `connect()`.
* **Cursor object**: The cursor object makes it possible for Python scripts to run PostgreSQL commands within a database session. The connection generates cursors, then the `cursor()` method ties them permanently to the connection. All commands are carried out within the framework of the connection-enclosed database session.

```python
import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_user",
                        password="db_pass",
                        port="db_port")
```

We have to specify those arguments in order to be able to connect to the database. Let's have a quick look into there arguments.

* **database**: the name of the database we wish to access or connect to. Note that we can only connect to one database with one connection object.
* **host**: this most likely refers to the database server's IP address or URL.
* **user**: as the name implies, this refers to the name of the PostgreSQL user.
* **password**: this is the password that matches the PostgreSQL user.
* **port**: the PostgreSQL server's port number on localhost – it is usually 5432.

If our database credentials were entered correctly, we will receive a live database connection object that we can use to build a cursor object. We can go ahead and run any database queries and retrieve data with the aid of a cursor object.

```python
cursor = conn.cursor()
```

 Let's write a simple query:

```python
cursor.execute("SELECT * FROM DB_table WHERE id = 1")
```

We apply the `execute()` function and supply a query string as its parameter. Then the database will be queried using the query that we entered.

After we have successfully achieved this, in order to be able to retrieve data from the database using Pyscopg2, we have to use any of these functions: `fetchone()` `fetchall()`, or `fetchmany()`.

### How to use `fetchone()`:

After running the SQL query, this function will only return the first row. It is the simplest method of getting data out of a database.

```python
#code
print(cursor.fetchone())

#output
(1, 'A-CLASS', '2018', 'Subcompact executive hatchback')
```

The `fetchone()` function returns a single row in the form of a tuple, with the information arranged in the order specified by the query's supplied columns.

When constructing the query string, it's crucial to provide the column orders precisely in order to distinguish which data in the tuple belongs to which.

### How to use `fetchall()`:

The `fetchall()` function works the same way as `fetchone()` except that it returns not just one row but all the rows. So in case we want 20-200 rows or more, we make use of Psycopg2 `fetchall()`.

```python
#code
print(cursor.fetchall())

#output
[(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
 (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
 (3, 'CLA', '2019', 'Subcompact executive fastback sedan'),
 (4, 'CLS', '2018', 'E-segment/executive fastback sedan'),
 (5, 'E-CLASS', '2017', 'E-segment/executive sedan'),
 (6, 'EQE', '2022', 'All-electric E-segment fastback'),
 (7, 'EQS', '2021', 'All-electric full-size luxury liftback'),
 (8, 'S-CLASS', '2020', 'F-segment/full-size luxury sedan.'),
 (9, 'G-CLASS', '2018', 'Mid-size luxury SUV, known as the G-Wagen'),
 (10, 'GLE', '2019', 'Mid-size luxury crossover SUV')]
[...]
```

### How to use `fetchmany()`: 

The `fetchmany()` function allows us to get a number of records out of the database and gives us additional control over the precise number of rows we get.

```python
#code
print(cursor.fetchmany(size=3))

#output
[(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
 (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
 (3, 'CLA', '2019', 'Subcompact executive fastback sedan')]

```

Because we set the argument to 3, we only received three rows. 

When we are done querying our database we need to close the connection with `conn.close()`.

## Conclusion 

That was pretty easy, right? We were able to perform all these tasks from a single Python script and it worked really well.

I hope this article was helpful and you can now work with PostgreSQL using Python. 

For more information, do check out the Psycopg2 [documentation](https://www.psycopg.org/docs/) to learn more.

