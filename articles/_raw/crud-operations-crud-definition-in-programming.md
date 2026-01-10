---
title: CRUD Operations – Crud Definition in Programming
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-20T21:54:52.000Z'
originalURL: https://freecodecamp.org/news/crud-operations-crud-definition-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--16-.png
tags:
- name: crud
  slug: crud
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'When interacting with a database or working with an API, you''ll often
  encounter the term CRUD. It is a popular acronym for the four basic operations or
  functions that a model (in the case of an API) or a database management system uses.

  This is an ac...'
---

When interacting with a database or working with an API, you'll often encounter the term CRUD. It is a popular acronym for the four basic operations or functions that a model (in the case of an API) or a database management system uses.

This is an acronym everyone learning computer programming will come across, and it's good to get familiar with what it means.

In this article, you will learn what each part of the acronym means, what the CRUD operators do, and how they relate to databases and API.

## What is CRUD?

CRUD is an acronym for **C**reate, **R**ead, **U**pdate and **D**elete. Each of these performs different operations, but they all aim to track and manage data, from a database, API, or whatever.

When creating a database or building APIs, you will want users to be able to manipulate any data available either by fetching these data, updating the data, deleting them, or adding more data. These operations are made possible through CRUD operations.

These operations have functions in Databases, as you can map them to a standard Structured Query Language (SQL) statement. Also, these operations can be mapped to a Hypertext Transfer Protocol (HTTP) method when working with RESTful APIs.

In SQL, the Create operation can be mapped to the INSERT function the same as the POST method in an HTTP request. Here is a table to summarize what each CRUD operation can be mapped to an HTTP request and SQL function:

| Letter | Operation | HTTP request | SQL function |
| --- | --- | --- | --- |
| C | Create | POST | INSERT |
| R | Read | GET | SELECT |
| U | Update | PATCH/ PUT (if you have `id` or `uuid`) | UPDATE |
| D | Delete | DELETE | DELETE |

With some examples, let's now understand how these acronyms work with SQL and HTTP requests.

## How the Create Operation Works

Just as its name suggests, you use the create operation to create a new record or entry. This record can be a user's data, a new item, information, or a new row to be added to your database.

For example, let's say you have a database or an array of users which consists of each user's name, age, username, password, and unique ID. You can add a new user to the database or list of users (this is referred to as a new record or entry).

When working with SQL, this is mapped to the INSERT function. A simple UPDATE function will look like this:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
```

In the above, you match the new values to their respective column via their name using the **INSERT** function. You can also tweak this, but the emphasis is the INSERT function.

When working with RESTful APIs, you will use the POST HTTP methods. For example, let's use the JavaScript Fetch API:

```js
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  body: JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

In the above example, a new object containing the `title`, `body` and `userId` of the new `post` is added to the `[posts](https://jsonplaceholder.typicode.com/posts)` [API](https://jsonplaceholder.typicode.com/posts). The server should return a header with the HTTP response code 201 (CREATED).

## How the Read Operation Works

You use the Read operation to read an entire database or search for one or more entries based on certain parameters.

For example, if you have a database of users, you can retrieve the entire list of users or get a particular user...or anything you want. The idea of retrieving can be referred to as READing.

When working with SQL, this is mapped to the SELECT function. A simple SELECT function will look like this:

```sql
SELECT * FROM menu;
```

In the above, you are selecting all the data in the menu table. You can also request specific values via their column names:

```sql
SELECT CustomerID, FirstName, LastName, Email, PhoneNumber
    FROM   Customer
```

You can also use parameters and lots more, but the emphasis is that you will always use the SELECT function.

When working with RESTful APIs, you will use the GET HTTP method. Although most times, you don't need to specify the method as it is the default method, for example, when using the JavaScript Fetch API:

```js
fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((json) => console.log(json));
```

When there are no errors, this will return the JSON data from the API, along with a 200 response code representing OK. If there is an error, it will often return a 404 response code (NOT FOUND).

## How the Update Operation Works

You use the Update operation to modify existing data. This is just like editing the data. Maybe you want to correct the spelling of a name from Jon Doe to John Doe.

When working with SQL, this is mapped to the UPDATE function. A simple UPDATE function will look like this:

```sql
UPDATE user
  SET user_name = 'John Doe', age = 62
  WHERE item_id = 1;
```

The request above will change the name and age of the specified user `id`.

When working with RESTful APIs, you will use either the PUT or PATCH HTTP methods.

```js
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  body: JSON.stringify({
    id: 1,
    title: 'foo',
    body: 'bar',
    userId: 1,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

This will return a response with a Status Code of 200 (OK) if the operation is successful.

## How the Delete Operation Works

As you must have guessed, you use this operation to delete a specified entry or record. This is the direct opposite of the Create operation, but for this, you will specify the ID (unique value) you wish to remove.

When working with SQL, this is mapped to the DELETE function. A simple DELETE function will look like this:

```sql
DELETE FROM user WHERE user_name='John Doe';
```

This will remove the row with the name "John Doe" from the table. If you want to delete all the records from the table, you can use the following:

```sql
DELETE FROM user;
```

When working with RESTful APIs, then you will make use of the DELETE method:

```js
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE',
});
```

If successful, this should return a response code of 204 (NO CONTENT).

## Wrapping Up

In this tutorial, you have learned what each operation in the CRUD acronym means, what they do, and how they work with SQL and HTTP requests.

In summary, C represents Create and is used to create a new entry. R represents Read and is used to read and retrieve entries. U represents Update and updates an entry. D represents Delete and is used to delete an entry.

You can learn more about [CRUD operation in JavaScript by building a Todo application in this article](https://www.freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app/) written by [Joy Shaheb](https://www.freecodecamp.org/news/author/joy/).

Thanks for reading, and have fun coding!
