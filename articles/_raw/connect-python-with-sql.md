---
title: How to Create and Manipulate SQL Databases with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T19:24:57.000Z'
originalURL: https://freecodecamp.org/news/connect-python-with-sql
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Untitled-design-1-.png
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Craig Dickson\nPython and SQL are two of the most important languages\
  \ for Data Analysts. \nIn this article I will walk you through everything you need\
  \ to know to connect Python and SQL.\nYou'll learn how to pull data from relational\
  \ databases straigh..."
---

By Craig Dickson

[Python](https://www.python.org/) and [SQL](https://en.wikipedia.org/wiki/SQL) are two of the most important languages for Data Analysts. 

In this article I will walk you through everything you need to know to connect Python and SQL.

You'll learn how to pull data from relational databases straight into your machine learning pipelines, store data from your Python application in a database of your own, or whatever other use case you might come up with.

Together we will cover:
* Why learn how to use Python and SQL together?
* How to set up your Python environment and MySQL Server
* Connecting to MySQL Server in Python
* Creating a new Database
* Creating Tables and Table Relationships
* Populating Tables with Data
* Reading Data
* Updating Records
* Deleting Records
* Creating Records from Python Lists
* Creating re-usable functions to do all of this for us in the future

That is a lot of very useful and very cool stuff. Let's get into it!

A quick note before we start: there is a Jupyter Notebook containing all the code used in this tutorial available in [this GitHub repository](https://github.com/thecraigd/Python_SQL). Coding along is highly recommended!

The database and SQL code used here is all from my previous [Introduction to SQL](https://towardsdatascience.com/tagged/sql-series) series posted on [Towards Data Science](https://towardsdatascience.com/) ([contact me](https://www.craigdoesdata.de/contact.html) if you have any problems viewing the articles and I can send you a link to see them for free). 

If you are not familiar with SQL and the concepts behind relational databases, I would point you towards [that series](https://towardsdatascience.com/tagged/sql-series) (plus there is of course a huge amount of great stuff available here on [freeCodeCamp](https://www.freecodecamp.org/news/search/?query=sql)!)

## Why Python with SQL?

For Data Analysts and Data Scientists, Python has many advantages. A huge range of open-source libraries make it an incredibly useful tool for any Data Analyst. 

We have [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and [Vaex](https://vaex.readthedocs.io/en/latest/) for data analysis, [Matplotlib](https://matplotlib.org/), s[eaborn](https://seaborn.pydata.org/) and [Bokeh](https://bokeh.org/) for visualisation, and [TensorFlow](https://www.freecodecamp.org/news/p/5fe3a414-f0df-488b-9402-44d8edc12652/www.tensorflow.org), [scikit-learn](https://scikit-learn.org/stable/) and [PyTorch](https://pytorch.org/) for machine learning applications (plus many, many more).

With its (relatively) easy learning curve and versatility, it's no wonder that Python is one of the [fastest-growing programming languages](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) out there.

So if we're using Python for data analysis, it's worth asking - where does all this data come from? 

While there is a massive variety of sources for datasets, in many cases - particularly in enterprise businesses - data is going to be stored in a relational database. Relational databases are an extremely efficient, powerful and widely-used way to [create, read, update and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) data of all kinds. 

The most widely used relational database management systems (RDBMSs) - [Oracle](https://www.oracle.com/database/), [MySQL](https://www.mysql.com/), [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server), [PostgreSQL](https://www.oracle.com/database/what-is-a-relational-database/), [IBM DB2](https://en.wikipedia.org/wiki/IBM_DB2) - all use the [Structured Query Language](https://en.wikipedia.org/wiki/SQL) (SQL) to access and make changes to the data. 

Note that each RDBMS uses a slightly different [flavour](https://towardsdatascience.com/the-many-flavours-of-sql-7b7da5d56c1e) of SQL, so SQL code written for one will usually not work in another without (normally fairly minor) modifications. But the concepts, structures and operations are largely identical.

This means for a working Data Analyst, a strong understanding of SQL is hugely important. Knowing how to use Python and SQL together will give you even more of an advantage when it comes to working with your data.

The rest of this article will be devoted to showing you exactly how we can do that.

## Getting Started

### Requirements & Installation

To code along with this tutorial, you will need your own [Python environment](https://www.python.org/downloads/) set up.

I use [Anaconda](https://www.anaconda.com/), but there are lots of ways to do this. Just google "how to install Python" if you need further help. You can also use [Binder](https://mybinder.org/) to code along with the associated [Jupyter Notebook](https://github.com/thecraigd/Python_SQL). 

We will be using [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) as it is free and widely used in the industry. If you are using Windows, [this guide](https://www.youtube.com/watch?v=2HQC94la6go) will help you get set up. Here are guides for [Mac](https://www.youtube.com/watch?v=5BQ5GvjiAR4) and [Linux](https://www.youtube.com/watch?v=0o0tSaVQfV4) users too (although it may vary by Linux distribution).

Once you have those set up, we will need to get them to communicate with each other. 

For that, we need to install the [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) Python library. To do this, follow [the instructions](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html), or just use pip:

```terminal
pip install mysql-connector-python
```

We are also going to be using [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html), so make sure that you have that installed as well.

```terminal
pip install pandas
```

### Importing Libraries

As with every project in Python, the very first thing we want to do is import our libraries. 

It is best practice to import all the libraries we are going to use at the beginning of the project, so people reading or reviewing our code know roughly what is coming up so there are no surprises.

For this tutorial, we are only going to use two libraries - [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) and [pandas](https://pandas.pydata.org/).

```python
import mysql.connector
from mysql.connector import Error
import pandas as pd
```

We import the Error function separately so that we have easy access to it for our functions.

## Connecting to MySQL Server

By this point we should have [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) set up on our system. Now we need to write some code in Python that lets us establish a connection to that server.

```python
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
```

Creating a re-usable function for code like this is best practice, so that we can use this again and again with minimum effort. Once this is written once you can re-use it in all of your projects in the future too, so future-you will be grateful!

Let's go through this line by line so we understand what's happening here:

The first line is us naming the function (create_server_connection) and naming the arguments that that function will take (host_name, user_name and user_password). 

The next line closes any existing connections so that the server doesn't become confused with multiple open connections.

Next we use a Python [try-except block](https://www.w3schools.com/python/python_try_except.asp) to handle any potential errors. The first part tries to create a connection to the server using the [mysql.connector.connect() method](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysql-connector-connect.html) using the details specified by the user in the arguments. If this works, the function prints a happy little success message. 

The except part of the block prints the error which MySQL Server returns, in the unfortunate circumstance that there is an error. 

Finally, if the connection is successful, the function returns a [connection object](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html). 

We use this in practice by assigning the output of the function to a variable, which then becomes our connection object. We can then apply other methods (such as [cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)) to it and create other useful objects.

```python
connection = create_server_connection("localhost", "root", pw)
```

This should produce a success message:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-146.png)
_Hooray!_

### Creating a New Database

Now that we have established a connection, our next step is to create a new database on our server. 

In this tutorial we will do this only once, but again we will write this as a re-usable function so we have a nice useful function we can re-use for future projects.

```python
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
```

This function takes two arguments, connection (our connection object) and query (a SQL query which we will write in the next step). It executes the query in the server via the connection.

We use the [cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html) method on our connection object to create a cursor object (MySQL Connector uses an [object-oriented programming paradigm](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/), so there are lots of objects inheriting properties from parent objects). 

This cursor object has methods such as [execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html), [executemany](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html) (which we will use in this tutorial) along with several other useful methods. 

If it helps, we can think of the cursor object as providing us access to the blinking cursor in a MySQL Server terminal window.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-148.png)
_You know, this one._

Next we define a query to create the database and call the function:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-149.png)

All the SQL queries used in this tutorial are explained in my [Introduction to SQL tutorial series](https://towardsdatascience.com/tagged/sql-series), and the full code can be found in the associated Jupyter Notebook in [this GitHub repository](https://github.com/thecraigd/Python_SQL), so I will not be providing explanations of what the SQL code does in this tutorial.

This is perhaps the simplest SQL query possible, though. If you can read English you can probably work out what it does! 

Running the create_database function with the arguments as above results in a database called 'school' being created in our server.

Why is our database called 'school'? Perhaps now would be a good time to look in more detail at exactly what we are going to implement in this tutorial.

### Our Database

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ERD.png)
_The Entity Relationship Diagram for our database._

Following the example in my [previous series](https://towardsdatascience.com/tagged/sql-series), we are going to be implementing the database for the International Language School - a fictional language training school which provides professional language lessons to corporate clients. 

This [Entity Relationship Diagram](https://www.lucidchart.com/pages/er-diagrams) (ERD) lays out our entities (Teacher, Client, Course and Participant) and defines the relationships between them.

All the information regarding what an ERD is and what to consider when creating one and designing a database can be found in [this article](https://towardsdatascience.com/designing-a-relational-database-and-creating-an-entity-relationship-diagram-89c1c19320b2). 

The raw SQL code, database requirements, and data to go into the database is all contained in [this GitHub repository](https://github.com/thecraigd/SQL_School_Tutorial), but you'll see it all as we go through this tutorial too.

### Connecting to the Database

Now that we have created a database in MySQL Server, we can modify our create_server_connection function to connect directly to this database. 

Note that it's possible - common, in fact - to have multiple databases on one MySQL Server, so we want to always and automatically connect to the database we're interested in. 

We can do this like so:

```python
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
```

This is the exact same function, but now we take one more argument - the database name - and pass that as an argument to the connect() method.

### Creating a Query Execution Function

The final function we're going to create (for now) is an extremely vital one - a query execution function. This is going to take our SQL queries, stored in Python as strings, and pass them to the [cursor.execute()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html) method to execute them on the server. 

```python
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
```

This function is exactly the same as our create_database function from earlier, except that it uses the [connection.commit()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html) method to make sure that the commands detailed in our SQL queries are implemented. 

This is going to be our workhorse function, which we will use (alongside create_db_connection) to create tables, establish relationships between those tables, populate the tables with data, and update and delete records in our database.

If you're a SQL expert, this function will let you execute any and all of the complex commands and queries you might have lying around, directly from a Python script. This can be a very powerful tool for managing your data.

## Creating Tables

Now we're all set to start running SQL commands into our Server and to start building our database. The first thing we want to do is to create the necessary tables. 

Let's start with our Teacher table:

```python
create_teacher_table = """
CREATE TABLE teacher (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """

connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
execute_query(connection, create_teacher_table) # Execute our defined query
```

First of all we assign our SQL command (explained in detail [here](https://towardsdatascience.com/coding-and-implementing-a-relational-database-using-mysql-d9bc69be90f5)) to a variable with an appropriate name. 

In this case we use Python's [triple quote notation for multi-line strings](https://developers.google.com/edu/python/strings) to store our SQL query, then we feed it into our execute_query function to implement it.

Note that this multi-line formatting is purely for the benefit of humans reading our code. Neither SQL nor Python 'care' if the SQL command is spread out like this. So long as the syntax is correct, both languages will accept it. 

For the benefit of humans who will read your code, however, (even if that will only be future-you!) it is very useful to do this to make the code more readable and understandable. 

The same is true for the CAPITALISATION of operators in SQL. This is a widely-used convention that is strongly recommended, but the actual software that runs the code is case-insensitive and will treat 'CREATE TABLE teacher' and 'create table teacher' as identical commands. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-151.png)

Running this code gives us our success messages. We can also verify this in the MySQL Server Command Line Client:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-152.png)

Great! Now let's create the remaining tables. 

```python
create_client_table = """
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40) NOT NULL,
  address VARCHAR(60) NOT NULL,
  industry VARCHAR(20)
);
 """

create_participant_table = """
CREATE TABLE participant (
  participant_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  client INT
);
"""

create_course_table = """
CREATE TABLE course (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(40) NOT NULL,
  language VARCHAR(3) NOT NULL,
  level VARCHAR(2),
  course_length_weeks INT,
  start_date DATE,
  in_school BOOLEAN,
  teacher INT,
  client INT
);
"""


connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_client_table)
execute_query(connection, create_participant_table)
execute_query(connection, create_course_table)
```

This creates the four tables necessary for our four entities. 

Now we want to define the relationships between them and create one more table to handle the many-to-many relationship between the participant and course tables (see [here](https://towardsdatascience.com/designing-a-relational-database-and-creating-an-entity-relationship-diagram-89c1c19320b2) for more details). 

We do this in exactly the same way:

```python
alter_participant = """
ALTER TABLE participant
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

alter_course = """
ALTER TABLE course
ADD FOREIGN KEY(teacher)
REFERENCES teacher(teacher_id)
ON DELETE SET NULL;
"""

alter_course_again = """
ALTER TABLE course
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

create_takescourse_table = """
CREATE TABLE takes_course (
  participant_id INT,
  course_id INT,
  PRIMARY KEY(participant_id, course_id),
  FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
  FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, alter_participant)
execute_query(connection, alter_course)
execute_query(connection, alter_course_again)
execute_query(connection, create_takescourse_table)
```

Now our tables are created, along with the appropriate constraints, primary key, and foreign key relations.

### Populating the Tables

The next step is to add some records to the tables. Again we use execute_query to feed our existing SQL commands into the Server. Let's again start with the Teacher table.

```python
pop_teacher = """
INSERT INTO teacher VALUES
(1,  'James', 'Smith', 'ENG', NULL, '1985-04-20', 12345, '+491774553676'),
(2, 'Stefanie',  'Martin',  'FRA', NULL,  '1970-02-17', 23456, '+491234567890'), 
(3, 'Steve', 'Wang',  'MAN', 'ENG', '1990-11-12', 34567, '+447840921333'),
(4, 'Friederike',  'Müller-Rossi', 'DEU', 'ITA', '1987-07-07',  45678, '+492345678901'),
(5, 'Isobel', 'Ivanova', 'RUS', 'ENG', '1963-05-30',  56789, '+491772635467'),
(6, 'Niamh', 'Murphy', 'ENG', 'IRI', '1995-09-08',  67890, '+491231231232');
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, pop_teacher)
```

Does this work? We can check again in our MySQL Command Line Client:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-153.png)
_Looks good!_

Now to populate the remaining tables.

```python
pop_client = """
INSERT INTO client VALUES
(101, 'Big Business Federation', '123 Falschungstraße, 10999 Berlin', 'NGO'),
(102, 'eCommerce GmbH', '27 Ersatz Allee, 10317 Berlin', 'Retail'),
(103, 'AutoMaker AG',  '20 Künstlichstraße, 10023 Berlin', 'Auto'),
(104, 'Banko Bank',  '12 Betrugstraße, 12345 Berlin', 'Banking'),
(105, 'WeMoveIt GmbH', '138 Arglistweg, 10065 Berlin', 'Logistics');
"""

pop_participant = """
INSERT INTO participant VALUES
(101, 'Marina', 'Berg','491635558182', 101),
(102, 'Andrea', 'Duerr', '49159555740', 101),
(103, 'Philipp', 'Probst',  '49155555692', 102),
(104, 'René',  'Brandt',  '4916355546',  102),
(105, 'Susanne', 'Shuster', '49155555779', 102),
(106, 'Christian', 'Schreiner', '49162555375', 101),
(107, 'Harry', 'Kim', '49177555633', 101),
(108, 'Jan', 'Nowak', '49151555824', 101),
(109, 'Pablo', 'Garcia',  '49162555176', 101),
(110, 'Melanie', 'Dreschler', '49151555527', 103),
(111, 'Dieter', 'Durr',  '49178555311', 103),
(112, 'Max', 'Mustermann', '49152555195', 104),
(113, 'Maxine', 'Mustermann', '49177555355', 104),
(114, 'Heiko', 'Fleischer', '49155555581', 105);
"""

pop_course = """
INSERT INTO course VALUES
(12, 'English for Logistics', 'ENG', 'A1', 10, '2020-02-01', TRUE,  1, 105),
(13, 'Beginner English', 'ENG', 'A2', 40, '2019-11-12',  FALSE, 6, 101),
(14, 'Intermediate English', 'ENG', 'B2', 40, '2019-11-12', FALSE, 6, 101),
(15, 'Advanced English', 'ENG', 'C1', 40, '2019-11-12', FALSE, 6, 101),
(16, 'Mandarin für Autoindustrie', 'MAN', 'B1', 15, '2020-01-15', TRUE, 3, 103),
(17, 'Français intermédiaire', 'FRA', 'B1',  18, '2020-04-03', FALSE, 2, 101),
(18, 'Deutsch für Anfänger', 'DEU', 'A2', 8, '2020-02-14', TRUE, 4, 102),
(19, 'Intermediate English', 'ENG', 'B2', 10, '2020-03-29', FALSE, 1, 104),
(20, 'Fortgeschrittenes Russisch', 'RUS', 'C1',  4, '2020-04-08',  FALSE, 5, 103);
"""

pop_takescourse = """
INSERT INTO takes_course VALUES
(101, 15),
(101, 17),
(102, 17),
(103, 18),
(104, 18),
(105, 18),
(106, 13),
(107, 13),
(108, 13),
(109, 14),
(109, 15),
(110, 16),
(110, 20),
(111, 16),
(114, 12),
(112, 19),
(113, 19);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, pop_client)
execute_query(connection, pop_participant)
execute_query(connection, pop_course)
execute_query(connection, pop_takescourse)
```

Amazing! Now we have created a database complete with relations, constraints and records in MySQL, using nothing but Python commands. 

We have gone through this step by step to keep it understandable. But by this point you can see that this could all very easily be written into one Python script and executed in one command in the terminal. Powerful stuff.

## Reading Data 

Now we have a functional database to work with. As a Data Analyst, you are likely to come into contact with existing databases in the organisations where you work. It will be very useful to know how to pull data out of those databases so it can then be fed into your python data pipeline. This is what we are going to work on next.

For this, we will need one more function, this time using [cursor.fetchall()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html) instead of [cursor.commit()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html). With this function, we are reading data from the database and will not be making any changes.

```python
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
```

Again, we are going to implement this in a very similar way to execute_query. Let's try it out with a simple query to see how it works.

```python
q1 = """
SELECT *
FROM teacher;
"""

connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q1)

for result in results:
  print(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-154.png)

Exactly what we are expecting. The function also works with more complex queries, such as this one involving a [JOIN](https://www.w3schools.com/sql/sql_join.asp) on the course and client tables.

```python
q5 = """
SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course
JOIN client
ON course.client = client.client_id
WHERE course.in_school = FALSE;
"""

connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q5)

for result in results:
  print(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-155.png)

Very nice. 

For our data pipelines and workflows in Python, we might want to get these results in different formats to make them more useful or ready for us to manipulate. 

Let's go through a couple of examples to see how we can do that.

### Formatting Output into a List

```python
#Initialise empty list
from_db = []

# Loop over the results and append them into our list

# Returns a list of tuples
for result in results:
  result = result
  from_db.append(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-156.png)

### Formatting Output into a List of Lists

```python
# Returns a list of lists
from_db = []

for result in results:
  result = list(result)
  from_db.append(result)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-157.png)

### Formatting Output into a [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

For Data Analysts using Python, [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) is our beautiful and trusted old friend. It's very simple to convert the output from our database into a DataFrame, and from there the possibilities are endless!

```python
# Returns a list of lists and then creates a pandas DataFrame
from_db = []

for result in results:
  result = list(result)
  from_db.append(result)


columns = ["course_id", "course_name", "language", "client_name", "address"]
df = pd.DataFrame(from_db, columns=columns)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-158.png)

Hopefully you can see the possibilities unfolding in front of you here. With just a few lines of code, we can easily extract all the data we can handle from the relational databases where it lives, and pull it into our state-of-the-art data analytics pipelines. This is really helpful stuff.

## Updating Records

When we are maintaining a database, we will sometimes need to make changes to existing records. In this section we are going to look at how to do that.

Let's say the ILS is notified that one of its existing clients, the Big Business Federation, is moving offices to 23 Fingiertweg, 14534 Berlin. In this case, the database administrator (that's us!) will need to make some changes. 

Thankfully, we can do this with our execute_query function alongside the SQL [UPDATE](https://dev.mysql.com/doc/refman/8.0/en/update.html) statement.

```python
update = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, update)
```

Note that the WHERE clause is very important here. If we run this query without the WHERE clause, then all addresses for all records in our Client table would be updated to 23 Fingiertweg. That is very much not what we are looking to do.

Also note that we used "WHERE client_id = 101" in the UPDATE query. It would also have been possible to use "WHERE client_name = 'Big Business Federation'" or "WHERE address = '123 Falschungstraße, 10999 Berlin'" or even "WHERE address LIKE '%Falschung%'". 

The important thing is that the WHERE clause allows us to uniquely identify the record (or records) we want to update.

## Deleting Records

It is also possible use our execute_query function to delete records, by using [DELETE](https://dev.mysql.com/doc/refman/8.0/en/delete.html). 

When using SQL with relational databases, we need to be careful using the DELETE operator. This isn't Windows, there is no 'Are you sure you want to delete this?' warning pop-up, and there is no recycling bin. Once we delete something, it's really gone.

With that said, we do really need to delete things sometimes. So let's take a look at that by deleting a course from our Course table. 

First of all let's remind ourselves what courses we have.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-174.png)

Let's say course 20, 'Fortgeschrittenes Russisch' (that's 'Advanced Russian' to you and me), is coming to an end, so we need to remove it from our database.

By this stage, you will not be at all surprised with how we do this - save the SQL command as a string, then feed it into our workhorse execute_query function.

```python
delete_course = """
DELETE FROM course 
WHERE course_id = 20;
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, delete_course)
```

Let's check to confirm that had the intended effect:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-175.png)

'Advanced Russian' is gone, as we expected. 

This also works with deleting entire columns using [DROP COLUMN](https://www.w3schools.com/sql/sql_ref_drop_column.asp) and whole tables using [DROP TABLE](https://www.w3schools.com/sql/sql_ref_drop_table.asp) commands, but we will not cover those in this tutorial. 

Go ahead and experiment with them, however - it doesn't matter if you delete a column or table from a database for a fictional school, and it's a good idea to become comfortable with these commands before moving into a production environment.

### Oh [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

By this point, we are now able to complete the four major operations for persistent data storage.

We have learned how to:
* Create - entirely new databases, tables and records
* Read - extract data from a database, and store that data in multiple formats
* Update - make changes to existing records in the database
* Delete - remove records which are no longer needed

These are fantastically useful things to be able to do. 

Before we finish things up here, we have one more very handy skill to learn.

## Creating Records from Lists

We saw when populating our tables that we can use the SQL [INSERT](https://dev.mysql.com/doc/refman/8.0/en/insert.html) command in our execute_query function to insert records into our database. 

Given that we're using Python to manipulate our SQL database, it would be useful to be able to take a Python data structure (such as a [list](https://www.w3schools.com/python/python_lists.asp)) and insert that directly into our database.

This could be useful when we want to store logs of user activity on a social media app we have written in Python, or input from users into a Wiki we have built, for example. There are as many possible uses for this as you can think of.  

This method is also more secure if our database is open to our users at any point, as it helps to prevent against [SQL Injection](https://en.wikipedia.org/wiki/SQL_injection) attacks, which can [damage or even destroy](https://www.lucidchart.com/pages/er-diagrams) our whole database.

To do this, we will write a function using the [executemany()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html) method, instead of the simpler [execute()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html) method we have been using thus far.

```python
def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
```

Now we have the function, we need to define an SQL command ('sql') and a list containing the values we wish to enter into the database ('val'). The values must be stored as a [list](https://www.w3schools.com/python/python_lists.asp) of [tuples](https://www.w3schools.com/python/python_tuples.asp), which is a fairly common way to store data in Python.

To add two new teachers to the database, we can write some code like this:

```python
sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
]
```

Notice here that in the 'sql' code we use the '%s' as a placeholder for our value. The resemblance to the ['%s' placeholder](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/48660475) for a string in python is just coincidental (and frankly, very confusing), we want to use '%s' for all data types (strings, ints, dates, etc) with the MySQL Python Connector. 

You can see a number of questions on [Stackoverflow](https://stackoverflow.com/questions/20818155/not-all-parameters-were-used-in-the-sql-statement-python-mysql/20818201) where someone has become confused and tried to use ['%d' placeholders](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/48660475) for integers because they're used to doing this in Python. This won't work here - we need to use a '%s' for each column we want to add a value to.

The executemany function then takes each tuple in our 'val' list and inserts the relevant value for that column in place of the placeholder and executes the SQL command for each tuple contained in the list.

This can be performed for multiple rows of data, so long as they are formatted correctly. In our example we will just add two new teachers, for illustrative purposes, but in principle we can add as many as we would like. 

Let's go ahead and execute this query and add the teachers to our database.

```python
connection = create_db_connection("localhost", "root", pw, db)
execute_list_query(connection, sql, val)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-177.png)

Welcome to the ILS, Hank and Sue!

This is yet another deeply useful function, allowing us to take data generated in our Python scripts and applications, and enter them directly into our database. 

## Conclusion

We have covered a lot of ground in this tutorial. 

We have learned how to use Python and MySQL Connector to create an entirely new database in MySQL Server, create tables within that database, define the relationships between those tables, and populate them with data. 

We have covered how to [Create, Read, Update and Delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) data in our database.

We have looked at how to extract data from existing databases and load them into pandas DataFrames, ready for analysis and further work taking advantage of all the possibilities offered by the [PyData stack](https://www.pluralsight.com/guides/a-lap-around-the-pydata-stack). 

Going in the other direction, we have also learned how to take data generated by our Python scripts and applications, and write those into a database where they can be safely stored for later retrieval and manipulation.

I hope this tutorial has helped you to see how we can use Python and SQL together to be able to manipulate data even more effectively!

_If you'd like to see more of my projects and work, please visit my website at [craigdoesdata.de](https://www.craigdoesdata.de/). If you have any feedback on this tutorial, please [contact me](https://www.craigdoesdata.de/contact.html) directly - all feedback is warmly received!_

![Image](https://www.freecodecamp.org/news/content/images/2020/08/logo.png)


