---
title: How to Use SQLite with Python
subtitle: ''
author: Eesa Zahed
co_authors: []
series: null
date: '2023-02-21T21:41:41.000Z'
originalURL: https://freecodecamp.org/news/sqlite-python-beginners-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/218187404-b5da9bc5-a6aa-446f-a8d5-5805344d091e.jpeg
tags:
- name: Python
  slug: python
- name: SQLite
  slug: sqlite
seo_title: null
seo_desc: 'Databases are a crucial component in software development. After all, we
  need to collect data in a location where we can digitally access it for reading,
  writing, updating, and deleting.

  In this tutorial, you''ll learn how to use SQLite with Python. L...'
---

Databases are a crucial component in software development. After all, we need to collect data in a location where we can digitally access it for reading, writing, updating, and deleting.

In this tutorial, you'll learn how to use SQLite with Python. Learning SQLite is a great way to learn how databases operate and how to perform basic CRUD (create, read, update, delete) operations. 

Many software developer positions involve working with databases, and if you ever consider creating a full-scale application (such as a social media app or an online game), you'll definitely need a database too. 

This tutorial will explain many basic concepts and simple operations, so that you can understand how to work with databases better.

## What is SQLite?

SQLite is an embedded SQL (Structured Query Language) database engine library that works with many languages. 

According to the [official website](https://www.sqlite.org/arch.html), SQL text is compiled into bytecode, which is then run by a virtual machine. Therefore, it is extremely fast and can efficiently handle complex queries.

A SQLite database is stored as a disk file, similar to a CSV (comma-separated values) file. But SQLite has many advantages over using a CSV file:

* It is written using C. C is a statically-typed, compiled language which is much faster than most languages, including Python.
* It’s lightweight, so it performs better and faster than reading from a CSV file.
* It’s easy to set up
* It can handle more complex queries.
* It’s more useful to learn, in case you are ever tasked with using SQL or MySQL in the future.

## How to Setup SQLite

Here is an example of using SQLite with Python. I’m using [Replit’s online IDE](https://replit.com), but you are welcome to follow along on any IDE you like. 

First, I’ll create a Python project with a `main.py` file. I’ll be using CS50’s SQL library, which you can install by running `pip3 install cs50`.

The first step is to create a database.db file in the root directory, which you can do by entering the following command in the terminal:

```
touch database.db

```

At this point, the following code should be added to main.py:

```
from cs50 import SQL

db = SQL("sqlite:///database.db")

```

### How to create a database table

The next step is to create a table in the database. SQL stores data in tables, which are similar to tables found in Excel or Google Sheets. The code for this is:

```
db.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age NUMBER, fav_food STRING)")

```

To break this down, db is the database that the data is written to. Next, a command gets executed. If the table `users` doesn’t exist, create a table with the name users, with the column names `name`, `age`, and `fav_food`, with the data types for each value specified.

### How to write to the database

You can use the INSERT operation to add a user.

```
db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)", "eesa", 14, "pizza")

```

The value “eesa” gets inserted into the name column, the value 14 is inserted into the age column, and the value “pizza” is inserted into the fav_food column.

The code for adding another user (in this case, Bob), would be this:

```
db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)", "bob", 20, "burgers")
```

### How to read from the database

After this, we can attempt to read all the users from the database. You can do this by running the following code.

```
people = db.execute("SELECT * FROM users")
print(people) # [{'name': 'eesa', 'age': 14, 'fav_food': 'pizza'}]

```

The code above is fairly straightforward. The * in the SELECT statement selects everything that’s in the database.

To only select specific values, you can use the DISTINCT statement. Say for example, you only want the favorite food of each user. You can do this by running the following code:

```
people = db.execute("SELECT DISTINCT fav_food FROM users")
print(people)

```

You can also separate values using commas in a SELECT DISTINCT query:

```
people = db.execute("SELECT DISTINCT age, fav_food FROM users")
print(people)

```

What if we wanted to just read the data for Bob, and ignore everyone else? You can do this by using the SQL WHERE Clause:

```
people = db.execute("SELECT * FROM users WHERE name='bob'")
print(people)

```

How about for more complex queries? You can do this using the AND, OR and NOT syntax. You can separate WHERE clauses with these keywords for more complex queries.

```
people = db.execute("SELECT * FROM users WHERE name='bob' AND age=20")
print(people)
```

This will print out the data for Bob, because Bob is 20. 

### How to update a row in the database

To update a row, you can use the UPDATE statement like this:

```
db.execute("UPDATE users SET fav_food='shawarma' WHERE name='eesa'")

```

### How to delete a row in the database

To delete a row, use the DELETE Syntax (as you might’ve guessed). It looks like this:

```
db.execute("DELETE FROM users WHERE name='bob'") # goodbye bob

people = db.execute("SELECT * FROM users")
print(people) # [{'name': 'eesa', 'age': 14, 'fav_food': 'shawarma'}]

```

To delete all the rows in the table, just remove the WHERE clause:

```
db.execute("DELETE FROM users") # :(

people = db.execute("SELECT * FROM users")
print(people) # []

```

## Conclusion

And that’s it for now. For more information on SQLite, I'd recommend checking out the [official documentation](https://docs.python.org/3/library/sqlite3.html). I wish you the best in creating amazing things!

Feel free to check out my [GitHub](https://github.com/eesazahed) and [Replit](https://replit.com/@eesazahed) to view my projects.

If you'd like to reach out, my email address is eszhd1 (at) gmail.com


