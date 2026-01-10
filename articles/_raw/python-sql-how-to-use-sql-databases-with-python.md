---
title: Python SQL – How to use the SQLite, MySQL, and PostgreSQL Databases with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-25T19:38:59.000Z'
originalURL: https://freecodecamp.org/news/python-sql-how-to-use-sql-databases-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/max-duzij-qAjJk-un3BI-unsplash-1.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: Python
  slug: python
- name: SQL
  slug: sql
- name: SQLite
  slug: sqlite
seo_title: null
seo_desc: "By Daniel Chae\nOne of my greatest joys as a developer is learning how\
  \ different technologies intersect. \nOver the years I've had the opportunity to\
  \ work with different types of software and tools. Of the many tools I've used,\
  \ Python and Structured Qu..."
---

By Daniel Chae

One of my greatest joys as a developer is learning how different technologies intersect. 

Over the years I've had the opportunity to work with different types of software and tools. Of the many tools I've used, Python and Structured Query Language (SQL) are two of my favorites. 

In this article I'm going to share with you how Python and the different SQL databases interact. 

I'll talk about the most popular databases, SQLite, MySQL, and PostgreSQL. I'll explain the key differences of each database and the corresponding use cases. And I'll end the article with some Python code. 

The code will show you how to write a SQL query to pull data from a PostgreSQL database and store the data in a pandas data frame.

_If you aren't familiar with relational databases (RDBMS), I suggest you check out Sameer's article on basic RDBMS terminology [here](https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/). The rest of the article will use terms referenced in Sameer's article._ 

## Popular SQL Databases

### SQLite

SQLite is best known for being an integrated database. This means that you don't have to install an extra application or use a separate server to run the database. 

If you're creating an MVP or don't need a ton of data storage space, you'll want to go with a SQLite database. 

The pros are that you can move faster with a SQLite database relative to MySQL and PostgreSQL. That said, you'll be stuck with limited functionality. You won't be able to customize features or add a ton of multi-user functionality.

### MySQL/PostgreSQL

There are distinct differences between MySQL and PostgreSQL. That said, given the context of the article, they fit into a similar category. 

Both database types are great for enterprise solutions. If you need to scale fast, MySQL and PostgreSQL are your best bet. They'll provide long-term infrastructure and bolster your security. 

Another reason they're great for enterprises is that they can handle high performance activities. Longer insert, update, and select statements need a lot of computing power. You'll be able to write those statements with less latency than what a SQLite database would give you.

## Why Connect Python and a SQL Database?

You might be wondering, "why should I care about connecting Python and a SQL database?"

There are many use cases for when someone would want to connect Python to a SQL database. As I mentioned earlier, you might be working on a web application. In this case, you'd need to connect a SQL database so you can store the data coming from the web application. 

Perhaps you work in data engineering and you need to build an automated ETL pipeline. Connecting Python to a SQL database will allow you to use Python for its automation capabilities. You'll also be able to communicate between different data sources. You won't have to switch between different programming languages. 

Connecting Python and a SQL database will also make your data science work more convenient. You'll be able to use your Python skills to manipulate data from a SQL database. You won't need a CSV file.

## How Python and SQL Databases Connect

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-design-1-.png)

Python and SQL databases connect through custom Python libraries. You can import these libraries into your Python script. 

Database-specific Python libraries serve as supplemental instructions. These instructions guide your computer on how it can interact with your SQL database. Otherwise, your Python code will be a foreign language to the database you're trying to connect to.

### How to Setup the Project

Let's take a PostgreSQL database, AWS Redshift, for example. First, you'll want to import the psycopg library. It's a universal Python library for PostgreSQL databases. 

```setup
#Library for connecting to AWS Redshift
import psycopg

#Library for reading the config file, which is in JSON
import json

#Data manipulation library
import pandas as pd
```

You'll notice we also imported the JSON and pandas libraries. We imported JSON because creating a JSON config file is a secure way to store your database credentials. We don't want anyone else eyeing those! 

The pandas library will enable you to use all of pandas' statistical capabilities for your Python script. In this instance, the library will enable Python to store the data your SQL query returns into a data frame. 

Next, you'll want to access your config file. The `json.load()` function reads the JSON file so you can access your database credentials in the next step.

```setup (continued)
config_file = open(r"C:\Users\yourname\config.json")
config = json.load(config_file)


```

Now that your Python script can access your JSON config file, you'll want to create a database connection. You'll need to read and use the credentials from your config file:

```
con = psycopg2.connect(dbname= "db_name", host=config[hostname], port = config["port"],user=config["user_id"], password=config["password_key"])
cur = con.cursor()
```

You just created a database connection! When you imported the psycopg library, you translated the Python code you wrote above to speak to the PostgreSQL database (AWS Redshift). 

In it of itself, AWS Redshift would not understand the above code. But because you imported the psycopg library, you now speak a language AWS Redshift can understand. 

The nice thing about Python is that it has libraries for SQLite, MySQL, and PostgreSQL. You'll be able to integrate the technologies with ease.

### How to Write a SQL Query

_Feel free to download the [European Soccer Data](https://www.kaggle.com/hugomathien/soccer) to your PostgreSQL database. I'll be using its data for this example._  

The database connection you created in the last step lets you write SQL to then store the data in a Python-friendly data structure. Now that you've established a database connection, you can write a SQL query to start pulling data:

```sql query
query = "SELECT *
         FROM League
         JOIN Country ON Country.id = League.country_id;"
```

The work is not done yet, though. You need to write some additional Python code that executes the SQL query:

```
#Runs your SQL query
execute1 = cur.execute(query)
result = cur.fetchall()
```

Then you need to store the returned data in a pandas data frame:

```
#Create initial dataframe from SQL data
raw_initial_df = pd.read_sql_query(query, con)
print(raw_initial_df)
```

You should get a pandas data frame (raw_initial_df) that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-108.png)

## There's a Database for Everybody

![Image](https://www.freecodecamp.org/news/content/images/2021/03/nastya-dulhiier-0Oppqi4r394-unsplash.jpg)

SQLite, MySQL, and PostgreSQL all have their pros and cons. The one you select should depend on your project or company's needs. You should also consider what you need now versus several years down the road. 

The important thing to remember is that Python can integrate with each database type. 

This article scratches the surface for what's possible with connecting Python to a SQL database. I love seeing the ways software intersect and combine to add incredible value. 

If you want more of this type of content, you can find me at [Course to Hire](https://coursetohire.com/)! I want to help more people learn how to code and land a job in tech. Please reach out for any questions or if you just want to say hi :)

