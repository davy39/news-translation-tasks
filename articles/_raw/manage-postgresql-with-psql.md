---
title: How to Manage PostgreSQL Databases from the Command Line with psql
subtitle: ''
author: Gerard Hynes
co_authors: []
series: null
date: '2022-06-07T15:29:11.000Z'
originalURL: https://freecodecamp.org/news/manage-postgresql-with-psql
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/manage-postgreSQL-with-psql.png
tags:
- name: command line
  slug: command-line
- name: database
  slug: database
- name: postgres
  slug: postgres
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'Now is a great time to learn relational databases and SQL. From web development
  to data science, they are used everywhere.

  In the Stack Overflow 2021 Survey, 4 out of the top 5 database technologies used
  by professional developers were relational dat...'
---

Now is a great time to learn relational databases and SQL. From web development to data science, they are used everywhere.

In the [Stack Overflow 2021 Survey](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-database-prof), 4 out of the top 5 database technologies used by professional developers were relational database management systems.

PostgreSQL is an excellent choice as a first relational database management system to learn.

1. It’s widely used in industry, including at [Uber, Netflix, Instagram, Spotify, and Twitch](https://stackshare.io/postgresql).
    
2. It’s open source, so you won’t be locked into a particular vendor.
    
3. It's more than 25 years old, and in that time it has earned a reputation for stability and reliability.
    

Whether you’re learning from the freeCodeCamp [Relational Database Certification](https://www.freecodecamp.org/learn/relational-database/) or trying out PostgreSQL on your own computer, you need a way to create and manage databases, insert data into them, and query data from them.

While there are several graphical applications for interacting with PostgreSQL, using psql and the command line is probably the most direct way to communicate with your database.

## What is psql?

psql is a tool that lets you interact with PostgreSQL databases through a terminal interface. When you install PostgreSQL on a machine, psql is automatically included.

psql lets you write SQL queries, send them to PostgreSQL, and view the results. It also lets you use meta-commands (which start with a backslash) for administering the databases. You can even write scripts and automate tasks relating to your databases.

Now, running a database on your local computer and using the command line can seem intimidating at first. I’m here to tell you it’s really not so bad. This guide will teach you the basics of managing PostgreSQL databases from the command line, including how to create, manage, back up, and restore databases.

## Prerequisite – Install PostgreSQL

If you haven’t already installed PostgreSQL on your computer, follow the instructions for your operating system on the [official PostgreSQL documentation](https://www.postgresql.org/download/).

When you install PostgreSQL, you will be asked for a password. Keep this in a safe place as you’ll need it to connect to any databases you create.

## How to Connect to a Database

You have two options when using psql to connect to a database: you can connect via the command line or by using the psql application. Both provide pretty much the same experience.

### Option 1 – Connect to a database with the command line

Open a terminal. You can make sure psql is installed by typing `psql --version`. You should see `psql (PostgreSQL) version_number`, where `version_number` is the version of PostgreSQL that’s installed on your machine. In my case, it's 14.1.

![Checking psql version via the command line](https://www.freecodecamp.org/news/content/images/2022/06/image-4.png align="left")

*Checking psql version via the command line*

The pattern for connecting to a database is:

```python
psql -d database_name -U username
```

The `-d` flag is shorter alternative for `--dbname` while `-U` is an alternative for `--username`.

When you installed PostgreSQL, a default database and user were created, both called `postgres`. So enter `psql -d postgres -U postgres` to connect to the `postgres` database as the `postgres` superuser.

```python
psql -d postgres -U postgres
```

You will be prompted for a password. Enter the password you chose when you installed PostgreSQL on your computer. Your terminal prompt will change to show that you’re now connected to the `postgres` database.

![Connecting to a database from the command line with psql](https://www.freecodecamp.org/news/content/images/2022/06/image-5.png align="left")

*Connecting to a database from the command line with psql*

If you want to directly connect to a database as yourself (rather than as the `postgres` superuser), enter your system username as the username value.

### Option 2 – Connect to a database with the psql application

Launch the psql application – it'll be called "SQL Shell (psql)". You will be prompted for a server, a database, a port and a username. You can just press enter to select the default values, which are `localhost`, `postgres`, `5432`, and `postgres`.

Next, you’ll be prompted for the password you chose when you installed PostgreSQL. Once you enter this, your terminal prompt will change to show that you’re connected to the `postgres` database.

![Connecting to a database with the psql application](https://www.freecodecamp.org/news/content/images/2022/06/image-2.png align="left")

*Connecting to a database with the psql application*

**Note:** If you’re on Windows you might see a warning like “Console code page (850) differs from Windows code page (1252) 8-bit characters might not work correctly. See psql reference page 'Notes for Windows users' for details.” You don’t need to worry about this at this stage. If you want to read more about it, see the [psql documentation](https://www.postgresql.org/docs/current/app-psql.html).

## How to Get Help in psql

To see a list of all psql meta-commands, and a brief summary of what they do, use the `\?` command.

```python
\?
```

![psql's help command](https://www.freecodecamp.org/news/content/images/2022/06/image-6.png align="left")

*psql's help command*

If you want help with a PostgreSQL command, use `\h` or `\help` and the command.

```python
\h COMMAND
```

This will give you a description of the command, its syntax (with optional parts in square brackets), and a URL for the relevant part of the PostgreSQL documentation.

![psql describing the DROP TABLE statement](https://www.freecodecamp.org/news/content/images/2022/06/image-7.png align="left")

*psql describing the DROP TABLE statement*

## How to Quit a Command in psql

If you’ve run a command that’s taking a long time or printing too much information to the console, you can quit it by typing `q`.

```python
q
```

## How to Create a Database

Before you can manage any databases, you’ll need to create one.

**Note:** SQL commands should end with a semicolon, while meta-commands (which start with a backslash) don’t need to.

The SQL command to create a database is:

```sql
CREATE DATABASE database_name;
```

For this guide, we’re going to be working with book data, so let’s create a database called `books_db`.

```sql
CREATE DATABASE books_db;
```

## How to List Databases

You can view a list of all available databases with the list command.

```python
\l
```

![Listing all databases](https://www.freecodecamp.org/news/content/images/2022/06/image-8.png align="left")

*Listing all databases*

You should see `books_db`, as well as `postgres`, `template0`, and `template1`. (The `CREATE DATABASE` command actually works by copying the standard database, called `template1`. You can read more about this in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/manage-ag-templatedbs.html).)

Using `\l+` will display additional information, such as the size of the databases and their tablespaces (the location in the filesystem where the files representing the database will be stored).

```python
\l+
```

![Listing all databases with additional information](https://www.freecodecamp.org/news/content/images/2022/06/image-22.png align="left")

*Listing all databases with additional information*

## How to Switch Databases

You’re currently still connected to the default `postgres` database. To connect to a database or to switch between databases, use the `\c` command.

```python
\c database_name
```

So `\c books_db` will connect you to the `books_db` database. Note that your terminal prompt changes to reflect the database you’re currently connected to.

![Switching databases](https://www.freecodecamp.org/news/content/images/2022/06/image-9.png align="left")

*Switching databases*

## How to Delete a Database

If you want to delete a database, use the `DROP DATABASE` command.

```sql
DROP DATABASE database_name;
```

You will only be allowed to delete a database if you are a superuser, such as `postgres`, or if you are the database’s owner.

If you try to delete a database that doesn’t exist, you will get an error. Use `IF EXISTS` to get a notice instead.

```sql
DROP DATABASE IF EXISTS database_name;
```

![Deleting a database](https://www.freecodecamp.org/news/content/images/2022/06/image-10.png align="left")

*Deleting a database*

You can’t delete a database that has active connections. So if you want to delete the database you are currently connected to, you’ll need to switch to another database.

## How to Create Tables

Before we can manage tables, we need to create a few and populate them with some sample data.

The command to create a table is:

```sql
CREATE TABLE table_name();
```

This will create an empty table. You can also pass column values into the parentheses to create a table with columns. At the very least, a basic table should have a Primary Key (a unique identifier to tell each row apart) and a column with some data in it.

For our `books_db`, we’ll create a table for authors and another for books. For authors, we’ll record their first name and last name. For books, we’ll record the title and the year they were published.

We’ll make sure that the authors’ `first_name` and `last_name` and the books’ `title` aren’t null, since this is pretty vital information to know about them. To do this we include the `NOT NULL` constraint.

```sql
CREATE TABLE authors(
	author_id SERIAL PRIMARY KEY, 
	first_name VARCHAR(100) NOT NULL, 
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE books(
	book_id SERIAL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	published_year INT
);
```

You will see `CREATE TABLE` printed to the terminal if the table was created successfully.

Now let's connect the two tables by adding a Foreign Key to books. Foreign Keys are unique identifiers that reference the Primary Key of another table. Books can, of course, have multiple authors but we’re not going to get into the complexities of many to many relationships right now.

Add a Foreign Key to `books` with the following command:

```sql
ALTER TABLE books ADD COLUMN author_id INT REFERENCES authors(author_id);
```

Next, let’s insert some sample data into the tables. We’ll start with `authors`.

```sql
INSERT INTO authors (first_name, last_name) 
VALUES (‘Tamsyn’, ‘Muir’), (‘Ann’, ‘Leckie’), (‘Zen’, ‘Cho’);
```

Select everything from `authors` to make sure the insert command worked.

```sql
SELECT * FROM authors;
```

![Querying all data from the authors table](https://www.freecodecamp.org/news/content/images/2022/06/image-13.png align="left")

*Querying all data from the authors table*

Next, we’ll insert some books data into `books`.

```sql
INSERT INTO books(title, published_year, author_id) 
VALUES (‘Gideon the Ninth’, 2019, 1), (‘Ancillary Justice’, 2013, 2), (‘Black Water Sister’, 2021, 3);
```

If you run `SELECT * FROM books;` you’ll see the book data.

![Querying all data from the books table](https://www.freecodecamp.org/news/content/images/2022/06/image-14.png align="left")

*Querying all data from the books table*

## How to List All Tables

You can use the `\dt` command to list all the tables in a database.

```python
\dt
```

For `books_db` you will see `books` and `authors`. You'll also see `books_book_id_seq` and `authors_author_id_seq`. These keep track of the sequence of integers used as ids by the tables because we used `SERIAL` to generate their Primary Keys.

![Listing all tables in a database](https://www.freecodecamp.org/news/content/images/2022/06/image-15.png align="left")

*Listing all tables in a database*

## How to Describe a Table

To see more information about a particular table, you can use the describe table command: `\d table_name`. This will list the columns, indexes, and any references to other tables.

```python
\d table_name
```

![Describing the authors table](https://www.freecodecamp.org/news/content/images/2022/06/image-25.png align="left")

*Describing the authors table*

Using `\dt+ table_name` will provide more information, such as about storage and compression.

## How to Rename a Table

If you ever need to change the name of a table, you can rename it with the `ALTER TABLE` command.

```sql
ALTER TABLE table_name RENAME TO new_table_name;
```

## How to Delete a Table

If you want to delete a table, you can use the `DROP TABLE` command.

```sql
DROP TABLE table_name;
```

If you try to delete a table that doesn’t exist, you will get an error. You can avoid this by including the `IF EXISTS` option in the statement. This way you’ll get a notice instead.

```sql
DROP TABLE IF EXISTS table_name;
```

## How to Manage Longer Commands and Queries

If you’re writing longer SQL queries, the command line isn’t the most ergonomic way to do it. It's probably better to write your SQL in a file and then have psql execute it.

If you are working with psql and think your next query will be long, you can open a text editor from psql and write it there. If you have an existing query, or maybe want to run several queries to load sample data, you can execute commands from a file that is already written.

### Option 1 – Open a text editor from psql

If you enter the `\e` command, psql will open a text editor. When you save and close the editor, psql will run the command you just wrote.

```python
\e
```

![Writing commands in a text editor](https://www.freecodecamp.org/news/content/images/2022/06/image-30.png align="left")

*Writing commands in a text editor*

On Windows, the default text editor for psql is Notepad, while on MacOs and Linux it's vi. You can change this to another editor by setting the `EDITOR` value in your computer’s environment variables.

### Option 2 – Execute commands and queries from a file

If you have particularly long commands or multiple commands that you want to run, it would be better to write the SQL in a file ahead of time and have psql execute that file once you’re ready.

The `\i` command lets you read input from a file as if you had typed it into the terminal.

```python
\i path_to_file/file_name.sql
```

**Note:** If you're executing this command on Windows, you still need to use forward slashes in the file path.

If you don’t specify a path, psql will look for the file in the last directory that you were in before you connected to PostgreSQL.

![Executing SQL commands from a file](https://www.freecodecamp.org/news/content/images/2022/06/image-29.png align="left")

*Executing SQL commands from a file*

## How to Time Queries

If you want to see how long your queries are taking, you can turn on query execution timing.

```python
\timing
```

This will display in milliseconds the time that the query took to complete.

If you run the `\timing` command again, it will turn off query execution timing.

![Using query execution timing](https://www.freecodecamp.org/news/content/images/2022/06/image-19.png align="left")

*Using query execution timing*

## How to Import Data from a CSV File

If you have a CSV file with data and you want to load this into a PostgreSQL database, you can do this from the command line with psql.

First, create a CSV file called `films.csv` with the following structure (It doesn’t matter if you use Excel, Google Sheets, Numbers, or any other program).

![A spreadsheet with Pixar film data](https://www.freecodecamp.org/news/content/images/2022/06/image-21.png align="left")

*A spreadsheet with Pixar film data*

Open psql and create a `films_db` database, connect to it, and create a `films` table.

```sql
CREATE DATABASE films_db;

\c films_db

CREATE TABLE films(
	id SERIAL PRIMARY KEY,
	title VARCHAR(100),
	year INT,
	running_time INT
);
```

You can then use the `\copy` command to import the CSV file into `films`. You need to provide an absolute path to where the CSV file is on your computer.

```python
\copy films(title, year, running_time) FROM 'path_to_file' DELIMITER ‘,’ CSV HEADER;
```

The `DELIMITER` option specifies the character that separates the columns in each row of the file being imported, `CSV` specifies that it is a CSV file, and `HEADER` specifies that the file contains a header line with the names of the columns.

**Note:** The column names of the `films` table don't need to match the column names of `films.csv` but they do need to be in the same order.

Use `SELECT * FROM films;` to see if the process was successful.

![Importing data from a .csv file.](https://www.freecodecamp.org/news/content/images/2022/06/image-31.png align="left")

*Importing data from a .csv file*

## How to Back Up a Database with `pg_dump`

If you need to backup a database, `pg_dump` is a utility that lets you extract a database into a SQL script file or other type of archive file.

First, on the command line (not in psql), navigate to the PostgreSQL `bin` folder.

```python
cd "C:\Program Files\PostgreSQL\14\bin"
```

Then run the following command, using `postgres` as the username, and filling in the database and output file that you want to use.

```python
pg_dump -U username database_name > path_to_file/filename.sql
```

Use `postgres` for the username and you will be prompted for the `postgres` superuser's password. `pg_dump` will then create a `.sql` file containing the SQL commands needed to recreate the database.

![Backing up a database to a .sql file.](https://www.freecodecamp.org/news/content/images/2022/06/image-60.png align="left")

*Backing up a database to a .sql file*

If you don’t specify a path for the output file, `pg_dump` will save the file in the last directory that you were in before you connected to PostgreSQL.

![Contents of films.sql backup file](https://www.freecodecamp.org/news/content/images/2022/06/image-45.png align="left")

*Contents of films.sql backup file*

You can pass the `-v` or `--verbose` flag to `pg_dump` to see what `pg_dump` is doing at each step.

![Running pg_dump in verbose mode.](https://www.freecodecamp.org/news/content/images/2022/06/image-61.png align="left")

*Running pg\_dump in verbose mode*

You can also backup a database to other file formats, such as `.tar` (an archive format).

```python
pg_dump -U username -F t database_name > path_to_file/filename.tar
```

Here the `-F` flag tells `pg_dump` that you're going to specify an output format, while `t` tells it it's going to be in the `.tar` format.

## How to Restore a Database

You can restore a database from a backup file using either psql or the `pg_restore` utility. Which one you choose depends on the type of file you are restoring the database from.

1. If you backed up the database to a plaintext format, such as `.sql`, use psql.
    
2. If you backed up the database to an archive format, such as `.tar`, use `pg_restore`.
    

### Option 1 – Restore a database using psql

To restore a database from a `.sql` file, on the command line (so not in psql), use `psql -U username -d database_name -f filename.sql`.

You can use the `films_db` database and `films.sql` file you used earlier, or create a new backup file.

Create an empty database for the file to restore the data into. If you're using `films.sql` to restore `films_db`, the easiest thing might be to delete `films_db` and recreate it.

```python
DROP DATABASE films_db;

CREATE DATABASE films_db;
```

In a separate terminal (not in psql), run the following command, passing in `postgres` as the username, and the names of the database and backup file you are using.

```python
psql -U username -d database_name -f path_to_file/filename.sql
```

The `-d` flag points psql to a specific database, while the `-f` flag tells psql to read from the specified file.

If you don’t specify a path for the backup file, psql will look for the file in the last directory that you were in before you connected to PostgreSQL.

You will be prompted for the `postgres` superuser's password and then will see a series of commands get printed to the command line while psql recreates the database.

![Restoring a database using psql.](https://www.freecodecamp.org/news/content/images/2022/06/image-52.png align="left")

*Restoring a database using psql*

This command ignores any errors that occur during the restore. If you want to stop restoring the database if an error occurs, pass in `--set ON_ERROR_STOP=on`.

```python
psql -U username -d database_name --set ON_ERROR_STOP=on -f filename.sql
```

### Option 2 – Restore a database using `pg_restore`

To restore a database using `pg_restore`, use `pg_restore -U username -d database_name path_to_file/filename.tar`.

Create an empty database for the file to restore the data into. If you're restoring `films_db` from a `films.tar` file, the easiest thing might be to delete `films_db` and recreate it.

```python
DROP DATABASE films_db;

CREATE DATABASE films_db;
```

On the command line (not in psql), run the following command, passing in `postgres` as the username, and the names of the database and backup file you are using.

```python
pg_restore -U username -d database_name path_to_file/filename.tar
```

![Restoring a database using pg_restore](https://www.freecodecamp.org/news/content/images/2022/06/image-54.png align="left")

*Restoring a database using pg\_restore*

You can also pass in the `-v` or `--verbose` flag to see what `pg_restore` is doing at each step.

![Using pg_restore in verbose mode](https://www.freecodecamp.org/news/content/images/2022/06/image-55.png align="left")

*Using pg\_restore in verbose mode*

## How to Quit psql

If you’ve finished with psql and want to exit from it, enter `quit` or `\q`.

```python
\q
```

This will close the psql application if you were using it, or return you to your regular command prompt if you were using psql from the command line.

## Where to Take it from Here

There are lots more things you can do with psql, such as managing schemas, roles, and tablespaces. But this guide should be enough to get you started with managing PostgreSQL databases from the command line.

If you want to learn more about PostgreSQL and psql, you could try out freeCodeCamp’s [Relational Database Certificate](https://www.freecodecamp.org/learn/relational-database/) . The official [PostgreSQL documentation](https://www.postgresql.org/docs/current/) is comprehensive, and [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-administration/psql-commands/) offers several in-depth tutorials.

I hope you find this guide helpful as you continue to learn about PostgreSQL and relational databases.
