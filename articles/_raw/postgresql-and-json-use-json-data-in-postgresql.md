---
title: PostgreSQL and JSON – How to Use JSON Data in PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-10T20:02:00.000Z'
originalURL: https://freecodecamp.org/news/postgresql-and-json-use-json-data-in-postgresql
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/PostgreSQL-and-JSON-Using-JSON-Data-in-PostgreSQL.jpg
tags:
- name: database
  slug: database
- name: json
  slug: json
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'By Faith Oyama

  PostgreSQL is a powerful open-source relational database management system (RDBMS).
  It was initially created as a successor to the Ingres database system and was later
  named "PostgreSQL" (short for "Post-Ingres SQL").

  PostgreSQL is kno...'
---

By Faith Oyama

PostgreSQL is a powerful open-source relational database management system (RDBMS). It was initially created as a successor to the Ingres database system and was later named "PostgreSQL" (short for "Post-Ingres SQL").

PostgreSQL is known for its robustness, reliability, and scalability, making it a popular choice for large and complex database applications. It offers advanced features such as support for JSON and other non-relational data types as well as support for spatial data.

JSON file support was first introduced in PostgreSQL v9.2, and with every new release, steady improvements are being made.

In this comprehensive guide, you will learn about JSON functions and operators in PostgreSQL. We’ll also go into the basics of storing JSON data in PostgreSQL, how to query JSON data in PostgreSQL to make it readily accessible, and finally, you’ll learn about working with JSON arrays.

## What is JSON?

JSON stands for JavaScript Object Notation. It is a common way to store data, especially in web applications. It is pretty similar to HTML or XML and was made for applications to easily read JSON files.

**Key-Value Pairs**: JSON data is written in key-value pairs surrounded by quotes. Here’s an example of a key-value pair “email”: “[jsonlearning@gmail.com](mailto:jsonlearning@gmail.com)”. “Email” here is the key, while “[jsonlearning@gmail.c](mailto:jsonlearning@gmail.com)om” represents the value. The two are separated by a colon “:”.

**Objects:** An object is a key-value pair or pairs enclosed in curly brackets. Whenever a key-value pair is enclosed in curly brackets it becomes an object and can be treated as a single unit. Multiple key-value pairs can be added in an object, separated with a comma.

Example of a JSON object:

```
{“email” : “jsonlearning@gmail.com”, 
“country” : “United Kingdom”}
```

**Arrays:**  Arrays in JSON are a way to store a collection of values within a single JSON object. An array in JSON is represented by square brackets `[ ]` containing a comma-separated list of values.

Here’s an example of an array in JSON: `[ "apple",  "banana",  "cherry"]`.

Arrays in JSON can also be nested, meaning that an array can contain other arrays or objects as values. Here's an example of a nested array:

```
{ "firstname" : "Claire", 
"location" : "United Kingdom", 
"blog" : [{ "id" : "1", 
"title" : "Welcome to my blog" }, 
{ "id" : "2", 
"title" : "My first programming language" }]}
```

In this example of nested Arrays, you can see, “blog” is contained in an array, and the array also contains several objects. 

## JSONB in PostgreSQL

### What is the JSONB data type? And how is it different from JSON?

JSONB (JSON Binary) is a data type in PostgreSQL that allows you to store and manipulate JSON data in a more effective and efficient way than the regular JSON data type.

JSONB stores JSON data in a binary format, which enables faster indexing and query performance compared to the regular JSON data type. This is because the binary format allows for more efficient storage and retrieval of JSON data, particularly when dealing with large or complex JSON objects.

In addition, JSONB supports additional indexing options, such as the ability to index specific keys within a JSON object, which allows for even faster queries.

The regular JSON data type in PostgreSQL stores JSON data as plain text, without any binary encoding or special indexing support. This makes it simpler to use but can result in slower query performance when dealing with large or complex JSON objects.

### How to create a table with the JSONB data type

You can create a table and give a column a data type of JSON or JSONB, just like you give a column the data type of Int, VARCHAR, or Double. You can just simply give the column a data type of either JSON or JSONB.

Here’s an example of creating a Table Journal and giving the column “diary_information” the data type JSONB. 

```sql
CREATE TABLE journal (
  id Int NOT NULL PRIMARY KEY, day VARCHAR, 
  diary_information JSONB
);

```

Because we specified the data type to be of type JSONB, any data held in that column must be a valid JSON.

### How to insert JSON data into tables

After creating a table and giving our column the data type JSONB, how do we insert values into the column? Remember the data must be in a valid JSON format. 

To insert data to our table, we use this statement:

```sql
INSERT INTO journal (id, day, diary_information) 
VALUES 
  (
    1, “Tuesday”, '{"title": "My first day at work", "Feeling": "Mixed                   feeling"}'
  );

```

If we try to retrieve the information using a select statement `SELECT * FROM journal` we get the following output, meaning the records have been inserted.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/select-from.png)

In the next section, we’ll take a look at some Functions and Operators.

## Overview of JSON Functions and Operators 

Functions and operators allow you to store, manipulate, and query data in JSON format in PostgreSQL.

Here are some commonly used PostgreSQL Functions and operators used in working with JSON files:

* `->`: This operator allows you to extract a specific value from a JSON object, you specify the key as a “child” to the “parent”. 

For example:

To retrieve a specific value from a JSON object using the `->` operator, use it in a SELECT statement as seen below: 

```sql
SELECT 
  Id, 
  day, 
  diary_information -> 'Feeling' AS Feeling 
FROM 
  journal;

```

Something to note here is that this operator extracts the field name, with the quote around it.

* `->>`: This operator allows you to extract a JSON object field as text without the quotes around it from a JSON object.

For example:

```sql
SELECT 
  id, 
  day, 
  dairy_information ->> 'Feeling' as Feeling 
FROM 
  products;

```

This will extract the value of the "material" key as text from the "features" column in the "products" table.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/material-products.png)

* `json_agg`: This function aggregates JSON values into a JSON array.

For example, `SELECT json_agg(my_column) FROM my_table;` will return a JSON array containing the values in the "my_column" column of the "my_table" table.

* `jsonb_set`: This function updates a JSON object field with a new value. For example:

```sql
UPDATE 
  my_table 
SET 
  json_column = jsonb_set(
    json_column, '{field_name}', '"new_value"'
  ) 
WHERE 
  id = 1;
```

To update an existing JSON record, we use the function `jsonb_set() ()` in an update statement. 

For example, to update the record in the table we created earlier, you can run the following code:

```sql
UPDATE 
  journal 
SET 
  diary_information = jsonb_set(
    diary_information, '{Feeling}', '"Excited"'
  ) 
WHERE 
  id = 1;

```

This will update the "Feeling" key in the "diary_information" column of the "journal" table with the new value "Excited".

* `JSONB_BUILD_OBJECT`: Manually inserting JSON values can lead to errors, especially if it’s your first time working with JSON data. But with this function, you can input values without having to worry about curly brackets, colons, and the rest of them.

You can use a `JSONB_BUILD_OBJECT` function to insert a plain text record and this will convert it to JSON data. For example if you run the code:

```sql
JSONB_BUILD_OBJECT('Morning', 'Everybody is annoying today', 'Evening', 'Cannot wait to go home’)
```

This will create a value that looks like this:

```sql
{“Morning”: “Everybody is annoying today”, “Evening”: “Cannot wait to go home”} 
```

Using this function in an insert statement:

```sql
INSERT INTO journal (id, day, feeling) 
VALUES 
  (
    2, 
    'Wednesday', 
    JSONB_BUILD_OBJECT(
      'Tired', 
      'Everybody is annoying today', 
      'Hungry', 
      'Cannot wait to go home’));

```

The new record will be added to the table and because we used the `JSONB_BUILD__OBJECT` function, the values that follow will be in JSON format.

These are the few functions and operators we can cover in this article. You can read more on JSON functions and Operators in PostgreSQL in the official documentation [here](https://www.postgresql.org/docs/9.5/functions-json.html).

## How to Work with JSON Arrays in PostgreSQL

In PostgreSQL, you can store JSON data as a column value in a table, and you can use JSON arrays to store a collection of JSON objects in a single column. 

Working with JSON arrays in PostgreSQL involves various operations, such as inserting, querying, and manipulating JSON data. Let's see how those work.

### How to insert JSON arrays into tables

To insert JSON arrays into a table in PostgreSQL, you can use the INSERT INTO statement along with the VALUES clause to specify the JSON array as a string value.

Here's an example:

Suppose you have a table called employees with columns id, name, and skills. The skills column stores an array of JSON objects representing the skills of each employee.

To insert a new employee record with the following details:

* id: 1
* name: John
* skills: [{"name": "Python", "level": "Intermediate"}, {"name": "JavaScript", "level": "Expert"}]

You can use the following SQL statement:

```sql
INSERT INTO employees (id, name, skills) 
VALUES 
  (
    1, 'John', '[{"name": "Python", "level": "Intermediate"}, {"name":   "JavaScript", "level": "Expert"}]'
  );

```

### How to query JSON arrays using JSON operators

To query JSON arrays in PostgreSQL, you can use the various JSON functions and operators provided by PostgreSQL. These functions allow you to extract specific values or elements from the JSON array and perform various operations on them. Let's look at an example.

#### How to extract values from a JSON array

Suppose you have a table called employees with a skills column that stores an array of JSON objects representing the skills of each employee.

To extract the names of all employees who have "Python" as one of their skills, you can use the `->>` operator to extract the "name" property of each skill object, and the `@>` operator to check if the resulting array contains the value "Python":

```sql
SELECT 
  name 
FROM 
  employees 
WHERE 
  skills @ > '[{"name": "Python"}]' :: jsonb

```

This is just an example of the many ways in which you can query and manipulate JSON arrays using the JSON operators provided by PostgreSQL.

## Conclusion

In conclusion, PostgreSQL support for JSON provides developers with the ability to simplify data models, enhance application performance, and so much more. This also provides a seamless relationship between relational and non-relational data structures. 

You have learned about the JSON and JSONB data types, and what key-value pairs, objects, and arrays are in JSON. You also learned about some operators and functions in PostgreSQL to query data in JSON format.

If you learned a thing or two from this article, please share it with others.

