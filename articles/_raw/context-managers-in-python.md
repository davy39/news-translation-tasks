---
title: What Are Context Managers in Python?
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2023-10-02T13:49:54.000Z'
originalURL: https://freecodecamp.org/news/context-managers-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/python-context-managers-1.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'One of the most common tasks that you''ll have to perform in your programs
  is working with external resources. These resources can be files on your computer''s
  storage or an open connection to third-party service on the internet.

  For the sake of simpli...'
---

One of the most common tasks that you'll have to perform in your programs is working with external resources. These resources can be files on your computer's storage or an open connection to third-party service on the internet.

For the sake of simplicity, imagine a program that opens a file, writes something to it, and then closes the file.

One way to implement this program in Python would be like this:

```python
def main():
    my_file = open('books.txt', 'w')
    my_file.write('If Tomorrow Comes by Sidney Sheldon')
    my_file.close()


if __name__ == '__main__':
    main()

```

Given that you run this program with the right permissions on your computer, it'll create a file called `books.txt` and write `If Tomorrow Comes by Sidney Sheldon` in it.

The `open()` function is one of the built-in functions in Python. It can open a file from a given path and return a corresponding file object.

A file object or file-like object, as it's often called, is a useful way to encapsulate methods like `read()`, `write()`, or `close()`. 

The `write()` method can be used write/send bytes-like object to an open stream, like a file.

Whenever you open an external resource, you must close it when its no longer needed, and the `close()` method does just that.

This program is functional, but it has a big flaw. If the program fails to close the file, it will remain open until the program itself closes.

You see, every program that you run on your computer gets a finite amount of memory allocated to it. All the variables you create or external resource you open from a program stay within the memory allocated to it by your computer.

If a program like this one, keeps opening new files without closing the previous ones, the allocated memory will keep shrinking.

At one point the program will inevitably run out of memory and crash ungracefully. This problem is referred to as a memory leak.

One way to prevent this from happening in Python is using a `try...except...finally` statement.

```python
def main():
    my_file = open('books.txt', 'w')

    try:
        my_file.write('If Tomorrow Comes by Sidney Sheldon')
    except Exception as e:
        print(f'writing to file failed: {e}')
    finally:
        my_file.close()


if __name__ == '__main__':
    main()

```

The code inside the `finally` block will run no matter what. So even if the program fails on the right action, it'll still be executed.

So, this solves the problem but imagine writing these lines of code every time you want to write something to a file.

It's not very reusable. You will have to repeat yourself a lot and chances of skipping a portion of the `if...except...finally` ladder is also a possibility.

That's where context managers come in.

## What is a Context Manager in Python?

According to the Python glossary, a context manager is —

> An object which controls the environment seen in a `with` statement by defining `__enter__()` and `__exit__()` methods.

That may not be noticeably clear to you. Let me explain the concept with an example.

The `with` statement in Python lets you run a block of code within a runtime context defined by a context manager object.

Once the block of code has finished executing, the context manager object will take care of tearing down any external resources that are no longer needed.

You can rewrite the program by using the `with` statement as follows:

```python
def main():
    with open('books.txt', 'w') as my_file:
        my_file.write('If Tomorrow Comes by Sidney Sheldon')


if __name__ == '__main__':
    main()

```

Since the `open()` function is paired with a `with` statement in this example, the function will create a context manager.

The file object will be accessible within the context of the indented code block, which means the file object doesn't exist outside of that scope.

The `as` keyword is useful when you want to assign a target variable to a returned object. Here, the `my_file` variable is the target and will hold the file object.

You can do whatever you want within the indented block of code and don't have to worry about closing the file.

Because once the block of code has finished executing the context manager will close the file automatically.

So, you have rewritten the entire `try...except...finally` ladder within two lines of code using the `with` statement and a context manager.

But how does that happen? How does a context manager object handle the task of setting up and closing resources?

And where are those `__enter__()` and `__exit__()` methods you read about on the Python documentation glossary?

Well, I'm so glad you asked :-)

## How To Create a Custom Context Manager in Python

The American theoretical physicist, Richard Feynman famously said —

> What I cannot create, I do not understand.

So, to understand the functionalities of a context manager you must create one by yourself and there are two distinct ways of doing that.

The first one is a generator-based approach and the second one is a class-based approach. In this section, I'll teach you both.

But before that, let me you a complex example that does more than merely opening and closing files in Python.

Imagine another Python application that must communicate with an SQLite database for reading and writing data.

You can write that program as follows:

```python
import sqlite3

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


def main():
    database_path = ':memory:'

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    try:
        cursor.execute(create_table_sql_statement)
        connection.commit()

        cursor.execute(insert_into_table_sql_statement)
        connection.commit()

        cursor.execute(select_from_table_sql_statement)

        print(cursor.fetchall())
    except Exception as e:
        print(f'read or write action to the database failed: {e}')
    finally:
        connection.close()


if __name__ == '__main__':
    main()

# [('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]

```

This Python program establishes a connection with an SQLite database. Then it creates a new table called books with two `TEXT` columns named `title` and `author`.

The program then stores information about three books on the table, retrieves them from the database, and prints out the retrieved data on the console.

As evident from the output of the `print()` statement, the program has successfully saved and retrieved the given data from the database.

There are three SQL queries in this program responsible for the database actions I just described.

```python
create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'
```

I've kept these three lines of code at the top of the file to keep the `main()` function to cleaner. The rest of the program sets up the database and executes the queries.

Python comes with excellent support for SQLite databases, thanks to the `sqlite3` module encapsulating useful methods such as the `sqlite3.connect()` method.

This method takes the path to a database as a string, attempts to establish a connection and in case of success, returns a `Connection` object.

If you pass `:memory:` instead of a file path, the program will create a temporary database on your computer's memory.

Once you have a connection, you'll need a `Cursor` object. A cursor object is a layer of abstraction required for executing SQL queries.

The `cursor()` method encapsulated within the `Connection` object returns a new cursor to the connected database.

Inside a `try` block, you can attempt to execute whatever query you want using the `execute()` or `executemany()` methods.

```python
    try:
        cursor.execute(create_table_sql_statement)
        connection.commit()

        cursor.execute(insert_into_table_sql_statement)
        connection.commit()

        cursor.execute(select_from_table_sql_statement)

        print(cursor.fetchall())
```

You need to call the `connection.commit()` method every time you write something to the database. Otherwise, the changes will be lost.

Data returned from a database remains within the `cursor` object and you can access them using the `cursor.fetchone()` or `cursor.fetchall()` methods.

In case of a failure, the `except` block will be triggered. The `finally` block will run unconditionally and close the database connection in the end.

This is fine and functional but like I've already said, it's not very reusable and is error prone.

Unfortunately, or in our case fortunately Python doesn't come with a built-in context manager for handling connections with SQLite databases.

So, let's try and see if we can produce one ourselves.

### How to Create a Class Based Context Manager in Python

To write a class-based context manager in Python, you need to create an empty class with three specific methods:

```python
class Database:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

The first one is obviously the class constructor that doesn't accept any parameter yet. It'll be responsible for accepting a database path:

```python
import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

The `__enter__()` method handles the task of setting up the resource. This is where you establish the connection and instantiate the cursor:

```python
import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

However you can not return two objects at once so you have to return the instance of the class itself.

Finally, the `__exit__()` method handles the task of closing the external resource in question.

```python
import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    	if exc_type is not None:
            print(f'an error occurred: {exc_val}')

        self.connection.close()
```

You can use this context manager in conjunction with the `with` statement in your code as follows:

```python
import sqlite3

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    	if exc_type is not None:
            print(f'an error occurred: {exc_val}')


def main():
    with Database(':memory:') as db:
        db.cursor.execute(create_table_sql_statement)
        db.connection.commit()

        db.cursor.execute(insert_into_table_sql_statement)
        db.connection.commit()
        
        db.cursor.execute(select_from_table_sql_statement)
        
        print(db.cursor.fetchall())


if __name__ == '__main__':
    main()

# [('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]

```

Evident from the output of the `print()` function call, the program has successfully stored and retrieved the given data from the database.

Without the `with` statement, `Database` is just a plain old class. However, the moment you put `with` infront of it, the three methods hop into action.

The `__init__()` method is the initializer and works identically to any other plain Python class's initializer method. It takes the path to the database.

The `__enter__()` method sets up the connection to the database and returns the instance of the context manager class to the target variable, `db` in this case.

This target variable is now encapsulating both the connection and the cursor objects. You can access them as `db.connection` and `db.cursor` respectively.

Once the code inside the `with` block finishes running, the `__exit__()` method will execute and close the active connection to the database.

You can handle any exception that may occur during the execution inside the `__exit__()` method. If there is an exception, `exc_type` holds the type of the exception, `exc_val` holds the value of the exception, `exc_tb` holds the traceback.

If there is no exception, the three variables will have a value of `None`. I'll not get into the details of exception handling in this article since that can take on many forms depending on what you're dealing with.

To make this custom context manager accessible from anywhere in the program, you can put it into its own separate module or even package.

This is far better solution than the `try...except...finally` ladder you saw earlier. You don't have to repeat yourself and chances of a human error is lower.

### How to Create a Generator Based Context Manager in Python

Evident from the title of this section, this approach uses a generator instead of a class to implement a context manager.

Syntactically, generators are almost the same as normal functions, except that you need to use `yield` instead of `return` in a generator.

Writing a generator-based context manager requires less code but it also loses some of its readability.

You can write the generator-based equivalent of the class-based `Database` context manager as follows:

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'an error occurred: {e}') 
    finally:
        connection.close()
```

Instead of a class, you have a generator function here so there is no initializer. Instead, the function itself can accept the path to the database as a parameter.

Within a `try` block, you can establish a connection to the database, instantiate the cursor, and return both objects to the user.

You can write `yield connection, cursor` to return the two objects but in that case the generator will return them as a tuple.

I prefer to use strings over numbers as accessors and that's why I have put the two objects inside a dictionary with descriptive keys.

The `except` block will run in case of an exception. Feel free to implement any exception handling strategy that you see fit.

The `finally` block will run unconditionally and close the open connection at the end of the `with` block.

Since there are no `__enter__()` or `__exit__()` methods either, you need to decorate the generator with the `@contextmanager` decorator.

This decorator defines a factory function for `with` statement context managers, without needing to create a class or separate `__enter__()` and `__exit__()` methods.

Usage of this context manager is identical to its class-based conterpart except the capitalization of its name.

```python
import sqlite3
from contextlib import contextmanager

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'an error occurred: {e}') 
    finally:
        connection.close()


def main():
    database_path = ':memory:'

    with database(database_path) as db:
        db.get('cursor').execute(create_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(insert_into_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(select_from_table_sql_statement)

        print(db.get('cursor').fetchall())


if __name__ == '__main__':
    main()

# [('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]

```

Since `db` is a dictionary instead of an object in this case, you will need to use square braces or the `get()` method to access the connection or cursor object.

## Conclusion

Context managers in Python is one of those topics that a lot of programmers have used but do not understand clearly.

I hope this article has cleared up some of your confusions.

If you'd like to connect to me, I am always available on [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Feel free to shoot a message and I'd be happy to respond. Also, if you think this was helpful, consider endorsing my relevant skills on the platform.

Until the next one, take care and keep exploring.

