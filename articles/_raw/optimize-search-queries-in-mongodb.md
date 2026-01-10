---
title: How to Optimize Search Queries in MongoDB
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-01-10T21:12:23.000Z'
originalURL: https://freecodecamp.org/news/optimize-search-queries-in-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/mongosearch.jpg
tags:
- name: MongoDB
  slug: mongodb
- name: search
  slug: search
seo_title: null
seo_desc: 'Searching through a database to extract relevant data can be quite cumbersome
  if you don''t have – or know how to use – the right tools.

  MongoDB is a non-relational, no-SQL database that differs from relational SQL-based
  databases such as PostgresSQL,...'
---

Searching through a database to extract relevant data can be quite cumbersome if you don't have – or know how to use – the right tools.

MongoDB is a non-relational, no-SQL database that differs from relational SQL-based databases such as PostgresSQL, MySQL.

These SQL-based databases use conventional rows and columns to display data, whereas MongoDB uses collections. Because of this primary distinction, it's important for you to understand certain special terminologies specific to MongoDB.

The inspiration for this tutorial came from working on a personal project. I had to implement a feature which required a complex MongoDB query operation. Scrolling through the MongoDB docs regarding the issue, I got more confused and I couldn’t figure it out.

After consulting several websites and books, I was finally able to get it done. So in this tutorial, my aim is to simplify MongoDB complex search operations for you as a newer MongoDB user.

I hope this article answers your burning questions and helps you navigate through MongoDB query operations.

Before we begin, here are some important prerequisites for this tutorial:

* Basic knowledge of Node.js
* Basic knowledge of MongoDB
* Knowledge of MongoDB commands
* Knowledge of Postman

## What Are MongoDB Queries?

Queries are commands that you use to obtain data from a MongoDB database. They work similarly to the SQL query system, but they operate differently syntax-wise. 

A conventional SQL query looks like this:

```
“SELECT * FROM db.Users”(SQL) vs  “db.collection.find(MONGO DB)”


```

This command lets you get all data stored in the Users database.

Many query operators can be used on a MongoDB database collection to obtain relevant information. But I'll be shedding more light on a few relevant ones in this tutorial.

### MongoDB Query Examples

Now I'll explain some of the query operators available to you in MongoDB. You can run the code samples provided below in the MongoDB command line interface to see how they work.

`Find()`: This operator returns all the documents in a collection. You can test this out by running;

```
Db.collection.find()

```

In this case, replace `collection` with the actual name of the collection you intend to search.

`findOne()`: this query operator returns the first document in a collection that matches the filter attached to the operator.

```
Db.collection.findOne()

```

`Aggregate()`: This operator collates results from various document in a given collection. You can combine it with other query operators to organize the results and group various data efficiently. 

You'll see an example of how to use this operator alongside the limit and sort query operators.

`limit()`: This operator limits the total expected search results to the number specified.

```
db.collection.aggregate([{ $limit: 6 }]);
```

This code above limits the total aggregated data to just 6.

`Sort()`: This operator sorts out the findings from the search query in either ascending or descending order.

```
db.collection.aggregate([
  { $sort: { fieldName: 1 } } // Replace 'fieldName' with the actual field name and use 1 for ascending or -1 for descending order
]);


```

You can test these query operators in a standard web application. There are quite a lot of programming tools available to develop applications, but in this tutorial, we'll be using Node.js because it is less complex to use and easily compatible with the MongoDB database application.

## How to Implement Search Queries in MongoDB using Node.js

Node.js is a JavaScript-based backend language, and it'll be our go to language for MongoDB usage in this tutorial. 

Right now, we'll be writing some code to search documents using the Node.js Express backend framework.

Mongoose will serve as the connection between MongoDB and Node. But before we delve in, what is Mongoose?

### What is Mongoose?

Mongoose is a popular object relational mapping (ORM) tool which helps establish an efficient connection between the database (MongoDB) and the object oriented programming language (Node.js/JavaScript).

It provides extensive features such as data modeling, schema development, model authentication, and data management which simplifies web API and database interactions.

You can also use it to interact with other databases such as Redis, MySQL and Postgres.

Now, let's set up Mongoose.

```
Npm install mongoose

```

To connect it to MongoDB in a Node.js application, use the following code:

```
const mongoose = require("mongoose");

mongoose.connect('mongodb://localhost/location', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  autoIndex: true
})
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.error(err);
  });



```

This code initiates a connection with the MongoDB database and maintains the connection to allow for data exchange with the backend application.

## How to Search Through Documents in MongoDB

In this section, we'll further improve our search query by applying some of the MongoDB operations we learned in the previous sections. We'll get books in a database based on the `findOne` parameter we briefly mentioned earlier.

First, let's use the `Find()` operator like this:

```
router.get("/", async (req, res) => {
  try {
    const books = await Book.find();
    res.status(200).json(books);
  } catch (err) {
    res.status(500).json(err);
  }
});



```

The code above requests all the books in the database. If successfully executed, it returns a status code of 200 with all the books in the collection in JSON format. If unsuccessful, it returns an error code.

How we can apply the `Limit()` operator like this:

```
router.get("/", async (req, res) => {
  try {
    let limitedBooks = await Book.find().limit(6);
    res.status(200).json(limitedBooks);
  } catch (err) {
    res.status(500).json(err);
  }
});


```

This code is quite similar to the code above. But it has an additional limit operator attached which limits the response expected to the first 6 books from the database.

And finally, we'll apply the `FindOne()` operator:

```
router.get("/", async (req, res) => {
  try {
    let myBook = await Book.findOne({ Author: "Man" });
    res.status(200).json(myBook);
  } catch (err) {
    res.status(500).json(err);
  }
});


```

In the code above, we tried finding the first book written by someone called “Man”. If it successfully finds that document it will return a success code 200 and the JSON format of that book collection in the database, else it will return an error code.

## How to Search Between Texts in MongoDB

Searching between texts entails a more complex approach to searching a MongoDB database.

It involves searching texts and phrases in the entire database and then displaying the info of objects containing these texts searched.

It is commonly used in complex search operations in order to include only information which is grouped based on price, authors, address, age or any other relevant common variable.

So now, let's implement a special MongoDB search query operator. We'll use this operator to search between texts and return the results as appropriate.

The code for this is displayed below:

```
let myBook = await Book.find({
  "$or": [
    { Author: { $regex: req.params.key } },
    { Title: { $regex: req.params.key } },
  ]
});



```

This code above utilizes the regex format to help locate phrases in the database and returns it. Regex works on the principle by matching a set of strings with similar patterns. This helps provide a faster response to our search queries and only returns documents that are similar to our search.

## Conclusion

With this, we have come to the end of the tutorial. We hope you’ve learnt essentially about MongoDB search queries and how to harness various search operators to obtain the best possible outcomes from your database.

Feel free to drop comments and questions and also check out my other articles [here](https://www.freecodecamp.org/news/author/oluwatobi/). Until next time, keep on coding.

