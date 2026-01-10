---
title: How to Perform CRUD Operations – JavaScript and SQL Example
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-08-03T20:41:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-js-and-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/5f9ca0b7740569d1a4ca4a58.jpg
tags:
- name: crud
  slug: crud
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: SQL
  slug: sql
seo_title: null
seo_desc: For the most part, interactive website architectures will involve generating
  or dispensing data of one sort or another. You can certainly use HTML forms to collect
  user input. But the kind of web form that's described here will only take you so
  far. ...
---

For the most part, interactive website architectures will involve generating or dispensing data of one sort or another. You can certainly use HTML forms to collect user input. But the kind of web form [that's described here](https://www.freecodecamp.org/news/creating-html-forms/) will only take you so far. 

What we really need is a way to reliably store and manipulate our data within the application environment. 

In this article, I'm going to show you how to connect a back end database to your data collection process. The plan involves tossing some HTML, JavaScript, and the tiny database engine SQLite into a bowl, mixing vigorously, and seeing what comes out. 

This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). If you'd like, you can follow the video version here:

%[https://youtu.be/yf2RJmpMEiI]

As you may already know, the SQL in SQLite stands for _structured query language_. This means that the syntax you'll use for interacting with a SQLite database will closely parallel how you'd do it with databases like MariaDB, Amazon Aurora, Oracle, or Microsoft's SQL Server. If you've got experience with any of those, you'll be right at home here.

Why are we going to use SQLite here? Because it's a very popular choice for the kind of work you're likely to undertake in a web environment. 

You'll need to create a new directory on your machine along with some files with JavaScript code. We'll learn how to create, modify, and delete records in a SQLite database. 

I could incorporate all those actions into a single file, of course, but I think breaking them out into multiple files will make it easier to understand what's going on.

## Connecting to a Database and Creating a Table

Here's what the first file will look like:

```
const sqlite3 = require('sqlite3').verbose();

// Create/connect to the database
const db = new sqlite3.Database('mydatabase.db');

// Create a table
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)`);

// Insert data
const insertQuery = `INSERT INTO users (name, age) VALUES (?, ?)`;
const name = 'Trevor';
const age = 5;
db.run(insertQuery, [name, age], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Inserted data with id ${this.lastID}`);
    }
});

// Close the database connection
db.close();
```

We begin by loading the sqlite3 module as `sqlite3` and then creating the `db` variable to represent our new database instance. The database will be called `mydatabase.db`. 

```
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('mydatabase.db');
```

If there isn't a database using that name in our local directory, the code will create one, otherwise it'll just connect to the one that's there already.

Since this is our first run, I'll create a new table within the `mydatabase.db` database. There will be three keys in our table: `id`, `name`, and `age`. 

```
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)`);
```

As you can see, `id` will be the primary key that we'll use to reference individual records. 

We defined the data type of each key: integer, text and, again, integer. This definition is something we only need to do once. But we do want to get it right, because changing it later, after we've already added data, can be tricky.

## Inserting New Data into a Table

In this section, we'll will add a new record to the table using the SQL `INSERT` command.

```
const insertQuery = `INSERT INTO users (name, age) VALUES (?, ?)`;
const name = 'Trevor';
const age = 5;
db.run(insertQuery, [name, age], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Inserted data with id ${this.lastID}`);
    }
});
```

You'll probably discover that official SQL documentation always capitalizes key syntax terms like `INSERT` and `SELECT`. That's a useful best practice, but it's not actually necessary. As a rule, I'm way too lazy to bother.

The query itself is templated as `insertQuery`, with the `name` and `age` details added as constants in the lines that follow. 

The `db.run` method, using the `insertQuery` constant and those two values (`name` and `age`) as attributes, is then executed. Based on the success or failure of the operation, log messages will be generated.

But hang on for a moment. What's with those question marks after declaring `insertQuery`? And why did we need to break this process into two parts? 

This is actually an important security practice known as an escape variable. With this in place, when the `db.run()` method executes the prepared statement, it'll automatically handle the escaping of the variable value, preventing SQL injection.

Lastly, we close down the connection:

```
db.close();
```

## Modifying Data

Now let's see how the "modify" code works. Like before, we create a SQLite3 constant and then connect to our database. 

This time, however, our table already exists, so we can go straight to the "modify" section.

```
const sqlite3 = require('sqlite3').verbose();

// Create/connect to the database
const db = new sqlite3.Database('mydatabase.db');

// Modify data
const updateQuery = `UPDATE users SET age = ? WHERE name = ?`;
const updatedAge = 30;
const updatedName = 'name2';
db.run(updateQuery, [updatedAge, updatedName], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Modified ${this.changes} row(s)`);
    }
});

// Close the database connection
db.close();
```

The pattern is similar. We define an `updateQuery` method to `UPDATE` a record that we'll define. This operation will change the `age` value for an entry whose name equals `Trevor`. 

You may recall that Trevor's age was earlier listed as 25. We're going to update that to 30. Everything else will work the same as before, including closing the connection when we're done.

This section of code from the third file will delete a record:

```
const deleteQuery = `DELETE FROM users WHERE name = ?`;
const deletedName = 'name1';
db.run(deleteQuery, [deletedName], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Deleted ${this.changes} row(s)`);
    }
});

```

The code above will delete the record where the name equals `Trevor`.

You can run any of those files using the `node`  command. But you should first make sure that you've installed the `sqlite3` module:

```
$ npm install sqlite3
```

Next I'll use `node` to run the first file (that you could choose to call `db.js`). 

```
$ node db.js
Inserted data with id 1
```

We'll see that a new record has been successfully inserted. If you list the directory contents, you'll also see that a new `mydatabase.db` file has been created.

You can always manually log into sqlite3 to see how things might have changed. I'll reference the `mydatabase.db` file so we can open it up right away. 

```
$ sqlite3 mydatabase.db
```

Typing `.tables` within the SQLite interface will list all the existing tables in this database. In our case, it'll be the `users` table we created. 

```
sqlite> .tables
users
sqlite>
```

Now I'll use the SQL `select` command to display a record. Here I'll use the asterisk to represent all records and specify the `users` table. 

```
sqlite> SELECT * FROM users;
1|Trevor|25
sqlite>
```

We can see that record `1` containing `Trevor` who is 25 years old has been created. Great!

Finally, we can run the `delete` code which should remove Trevor altogether:

```
const deleteQuery = `DELETE FROM users WHERE name = ?`;
const deletedName = 'Trevor';
db.run(deleteQuery, [deletedName], function (err) {
    if (err) {
        console.error(err.message);
    } else {
        console.log(`Deleted ${this.changes} row(s)`);
    }
});
```

I should note that the `db.run` and `db.close` format I used for those methods can also be referred to as `Database.run()`, and `database.close()`. It's just a matter of preference - or, in my case, laziness. I'm a Linux admin, after all, and the very best admins are, in principle, lazy.

## Summary

We've seen how use JavaScript to connect to a back end database, create a new table, and then add, modify, and delete records in that table. And we seem to have gotten away with it, too! 

Now try this on your own computer. But play around with the values. Even better: build something practical.

_This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

