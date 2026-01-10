---
title: How to get started with PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-02T16:22:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-postgresql-9d3bc1dd1b11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IJ3HI44YdLzTkMOQpibNGw.png
tags:
- name: learning
  slug: learning
- name: postgres
  slug: postgres
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Akul Tomar

  PostgreSQL is an open source Relational Database Management System (RDBMS). In this
  article, I’ll provide an introduction to getting started with PostgreSQL. Here is
  what we’ll cover:


  Installation

  Administration

  Basic Database Operatio...'
---

By Akul Tomar

PostgreSQL is an open source Relational Database Management System (RDBMS). In this article, I’ll provide an introduction to getting started with PostgreSQL. Here is what we’ll cover:

* [Installation](https://medium.com/p/9d3bc1dd1b11#d220)
* [Administration](https://medium.com/p/9d3bc1dd1b11#d003)
* Basic Database Operations

### Installation

If you have homebrew installed on your system, you can run the command below on your terminal to quickly install PostgreSQL:

```
brew install postgresql
```

Others can download the latest version of PostgreSQL [here](https://www.postgresql.org/download/) and follow the installation steps.

Once downloaded, to verify you’ve got PostgreSQL installed, run the following command to check your PostgreSQL version:

```
postgres --version
```

### Administration

PostgreSQL can be administered from the command line using the `psql` utility, by running the command below:

```
psql postgres
```

This should get your psql utility running. psql is PostgreSQL’s command line tool. While there are many third-party tools available for administering PostgreSQL databases, I haven’t felt the need to install any other tool yet. psql is pretty neat and works just fine.

> To quit from the psql interface, you can type `\q` and you’re out.

If you need help, type `\help` on your psql terminal. This will list all the available help options. You can type in `\help [Command Name]`, in case you need help with a particular command. For example, typing in `\help UPDATE` from within `psql` will show you the syntax of the update option.

```
Description: update rows of a table[ WITH [ RECURSIVE ] with_query [, ...] ]UPDATE [ ONLY ] table_name [ * ] [ [ AS ] alias ]    SET { column_name = { expression | DEFAULT } |          ( column_name [, ...] ) = ( { expression | DEFAULT } [, ...] ) |          ( column_name [, ...] ) = ( sub-SELECT )        } [, ...]    [ FROM from_list ]    [ WHERE condition | WHERE CURRENT OF cursor_name ]    [ RETURNING * | output_expression [ [ AS ] output_name ] [, ...] ]
```

If you’re a beginner, you may still not understand. A quick Google search will provide you examples of its use or you can always search the official [psql documentation](https://www.postgresql.org/docs/current/static/sql-update.html) which will provide many examples.

When you first install PostgreSQL, there are a few common administrative tasks that you’ll frequently perform.

The first thing would be to check for existing users and databases. Run the command below to list all databases:

```
\list or \l
```

![Image](https://cdn-media-1.freecodecamp.org/images/X7JXfDeBJE4FwB8VpGyzcQQeScyrXbkbi0MR)

In the figure above, you can see **three** default databases and a superuser `akultomar` that get created when you install PostgreSQL.

To list all users, use the `\du` command. The attributes of the user tell us that they’re a Superuser.

![Image](https://cdn-media-1.freecodecamp.org/images/ufNwqrWDxIpZPbuVWl73LbCHehsjT3Hp5Tab)

### Basic Database Operations

To perform basic database operations, you use the Structured Query Language (commonly known as SQL).

#### **Create a database**

To create a database, you use the `create database` command. In the example below, we’ll create a database named `riskzone`.

![Image](https://cdn-media-1.freecodecamp.org/images/cDE-hPhNlkyAacTptApc62hoZrDTczpurCPy)

If you forget the semicolon at the end, the `=` sign at the postgres prompt is replaced with a `-` as in the figure below. This is basically an indication that you need to terminate your query. You’ll understand it’s significance when you actually start writing longer queries. For now just put a semi-colon to complete the SQL statement and hit return.

![Image](https://cdn-media-1.freecodecamp.org/images/yLCabIGAb-rU5IrgEr-ziVy9ynjkkcclgG2U)

#### **Create a user**

To create a user, you use the `create user` command. In the example below, we’ll create a user named `no_one`.

![Image](https://cdn-media-1.freecodecamp.org/images/Zo-ux1MpucuEes7-fNdgt1z5jwIoAswSj08n)

When you create a user, the message shown is **CREATE ROLE**. Users are roles with login rights. I have used them interchangeably. You’ll also notice that the Attributes column is empty for the user `no_one`. This means that the user `no_one` has no administrative permissions. They can only read data and cannot create another user or database.

You can set a password for your user. To a set password for an existing user, you need use the `\password` command below:

```
postgres=#\password no_one 
```

To set a password when a user is created, the command below can be used:

```
postgres=#create user no_two with login password 'qwerty';
```

#### **Delete a user or database**

The `drop` command can be used to delete a database or user, as in the commands below.

```
drop database <database_name>drop user <user_name>
```

> This command needs to be used very carefully. Things dropped don’t come back unless you have a backup in place.

If we run the `\du` and `\l` that we learned about earlier to display the list of users and databases respectively, we can see that our newly created `no_one` user and `riskzone` database.

![Image](https://cdn-media-1.freecodecamp.org/images/RHPB-ZGQ4e8vqVY9mmlN-w1Qkieg44phby9Q)

When you specify `psql postgres` (without a username), it logs into the postgres database using the default superuser (`akultomar` in my case). To log into a database using a specific user, you can use the command below:

```
psql [database_name] [user_name]
```

Let’s login to the `riskzone` database with the `no_one` user. Hit `\q` to quit from the earlier postgres database and then run the command below to log into `riskzone` with the user `no_one`.

![Image](https://cdn-media-1.freecodecamp.org/images/MsaHxCUlBMaQ0VEnGj7bNcH9rVjH9XuxGg3v)

I hoped you like the short introduction to PostgreSQL. I’ll be writing another article to help you understand roles better. If you’re new to SQL, my advice would be to practice as much as you can. Get your hands dirty and create your own little tables and practice.

