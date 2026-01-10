---
title: How to Start Using MongoDB – Database Setup for Beginners
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-07-25T21:42:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-using-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-tom-fisk-3285715.jpg
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
- name: NoSQL
  slug: nosql
seo_title: null
seo_desc: "MongoDB is an increasingly popular open source NoSQL database. And it has\
  \ many advantages over traditional SQL databases. \nIt offers high scalability,\
  \ reliability, and performance even with a huge amount of data. \nThis article covers\
  \ the basics that ..."
---

MongoDB is an increasingly popular open source NoSQL database. And it has many advantages over traditional SQL databases. 

It offers high scalability, reliability, and performance even with a huge amount of data. 

This article covers the basics that you need to know to get started with MongoDB and how to use it properly.

### Prerequisites

* A suitable IDE such as VS Code
* A terminal

### What You'll Learn

* What is MongoDB?
* What is NoSQL?
* How to install MongoDB
* Hoe to setup MongoDB
* How to run MongoDB

## What is a NoSQL Database?

A NoSQL database is a non-relational database that does not use the traditional table-based schema of a relational database. 

NoSQL databases are often used for big data and real-time web applications. MongoDB is one of the most popular NoSQL databases. It's fast, scalable, and uses JSON documents to store data. 

## Why Should I Use No-SQL?

No-SQL databases are powerful tools that can help you work with large amounts of data. They're especially good at handling unstructured data, so they can be a good choice if you're dealing with a lot of data that doesn't fit into a traditional relational database. 

No-SQL databases can also be more scalable than relational databases, which is important if you're expecting your data to grow over time.

## How to Get Started with MongoDB – Install Guide

Install MongoDB using [this link](https://www.mongodb.com/docs/manual/administration/install-community/) or use the instructions below if you are using Ubuntu: 

* Import the public key

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

```

* Create a list file for Ubuntu 

```bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

```

* Run the following command to update:

```bash
sudo apt-get update

```

* Install the latest package

```bash
sudo apt-get install -y mongodb-org

```

* Then run:

```bash
sudo service mongod start

```

## How to Create and Populate the MongoDB Database

Once you have MongoDB installed, create a data directory where MongoDB will store its data files. By default, this is `/data/db`, but you can specify a different location if you prefer. Finally, start the MongoDB server by running `mongod` from the command line.

Make a directory for `dbPath` with the following command: 

```bash
sudo mkdir -p /data/db 
sudo chown -R `id -un` /data/db
```

Then run `sudo mongod --port 27017`or `mongod` in a different terminal:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-214.png)

Your output format (also known as `structured logging`) for server logs in MongoDB 4.4+ should look like the above. Although the JSON format may initially seem intimidating, it is made to be used with common JSON tools and frameworks.

Enter the MongoDB shell using this command: 

```bash
mongo

```

You will get the output shown below after running the following command:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-from-2022-07-24-18-37-20.png)

## How to Create a New MongoDB Database

The first step in using MongoDB is creating a new database with the command `use mydatabase`. You can then create collections inside this database. Finally, you can populate your new collection.

```
 use record
 db.users.insert({username: "myname", password: "mypassword"})

```

The  `use record` command switches the database to `record database`. The `db.users.insert(...)` command adds an input to the `users` table within the  `record` database.

Below is the output of the commands above:

```
WriteResult({ "nInserted" : 1 })
```

Run the following command to view the record you created in the previous step:

```
 db.users.find()

```

The `db.users.find()` command searches the `users` table for all entries.  
Your output yields the following result:

```
{ "_id" : ObjectId("62dd6ab4a7d1ab0948574778"), "username" : "myname", "password" : "mypassword" }
```

## How to Add New Records to Your Database

To add new records, do the following:

```
 use record
 db.commerce.save({scriptname: "dygraph.min.js", version: "2.1.0"})
 db.commerce.save({scriptname: "sortable.min.js", version: "0.8.0"})
```

We've added two records to the `commerce` table, each with data specified by the `scriptname` and `version` attributes.

You should get something like this:

```
WriteResult({ "nInserted" : 1 })
```

To view all the tables stored in your MongoDB database, run the following commands:

```
 use record
 show collections

```

You should see a similar output to the below:

```
commerce
users
```

## Conclusion

MongoDB is a powerful database system you can use for a variety of applications. It is easy to set up and use, and its scalability makes it a good choice for large-scale projects. 

If you are new to database systems, MongoDB is a good place to start.

