---
title: How to Get Started with MongoDB in Rust
subtitle: ''
author: Oduah Chigozie
co_authors: []
series: null
date: '2023-02-20T20:41:19.000Z'
originalURL: https://freecodecamp.org/news/mongodb-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-ulucas-dube-cantin-10325707.jpg
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
- name: Rust
  slug: rust
seo_title: null
seo_desc: "MongoDB is a popular NoSQL database that has been gaining increasing popularity\
  \ in recent years. It offers developers a flexible, scalable, and high-performance\
  \ database solution, which can be used for a wide range of applications. \nFor Rust\
  \ programm..."
---

MongoDB is a popular NoSQL database that has been gaining increasing popularity in recent years. It offers developers a flexible, scalable, and high-performance database solution, which can be used for a wide range of applications. 

For Rust programmers, MongoDB provides an excellent option for storing and retrieving data in a fast, efficient, and reliable way.

Rust is a modern, high-performance systems programming language that was designed for speed, safety, and concurrency. It is well suited for building high-performance, low-level software, and is becoming increasingly popular among developers.

In this article, we will explore how Rust programmers can leverage MongoDB to build high-performance, scalable applications. I will explain how to set up a MongoDB database, and show you how to interact with MongoDB from Rust using the official MongoDB Rust driver. 

Whether you are new to MongoDB or an experienced Rust programmer looking to leverage this powerful database technology, this article will provide you with the knowledge and skills you need to get started.

## Prerequisites

To follow along with the article, you only need the following:

* Knowledge of Rust.
* A system to work with.
* Rust installed on your system.

## Getting Started

To get started with MongoDB, you will need to install the MongoDB Community Edition database software. The following steps will guide you through the installation process.

### Download MongoDB Community Edition.

The first step is to download the MongoDB Community Edition package for your operating system. 

You can download the package from the official MongoDB website at [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community).

### Install MongoDB Community Edition.

After downloading the package, run the installer and follow the prompts to install MongoDB Community Edition on your system.

### Start the MongoDB server.

Once the installation is complete, start the MongoDB server by running the following command:

```bash
mongod

```

This will start the MongoDB server and it will be listening on port 27017 by default.

### Install MongoDB Compass

MongoDB Compass is a graphical user interface (GUI) for working with MongoDB. It provides a simple and intuitive way to interact with MongoDB databases, collections, and documents. 

To install MongoDB Compass, follow these steps:

1. Go to the official MongoDB website at [https://www.mongodb.com/products/compass](https://www.mongodb.com/products/compass) and download the appropriate version for your operating system.
2. Run the installer and follow the prompts to install MongoDB Compass on your system.
3. Once the installation is complete, launch MongoDB Compass and connect to your MongoDB server by entering the connection string in the connection dialog.

Congratulations, you have now installed the MongoDB Community Edition and MongoDB Compass. You can now start working with MongoDB databases, collections, and documents. 

In the next section, we will cover how to set up a project so that you can interact with the database from Rust.

## How to Set Up Your Project

Now that you have MongoDB installed on your system, it's time to set up your Rust project to use the official MongoDB Rust driver. Follow these steps to get started:

### Create a new Rust project.

Open your terminal and create a new Rust project by running the following command:

```bash
cargo new myproject

```

This will create a new Rust project with the name "myproject".

### Add the MongoDB Rust driver dependency.

Open the _Cargo.toml_ file in your project directory and add the following dependency to it:

```toml
[dependencies]
mongodb = "2.3.1"

```

This will add the MongoDB Rust driver dependency to your project.

### Import the necessary libraries.

Open the _src/main.rs_ file in your project directory and import the necessary libraries by adding the following lines to the top of the file:

```rust
extern crate mongodb;
use mongodb::bson::doc;
use mongodb::{Client, options::ClientOptions};

```

This will import the `doc` macro, and the `Client` and `ClientOptions` types from the MongoDB Rust driver.

### Connect to your MongoDB server.

Add the following code to your `main` function to connect to your MongoDB server:

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

```

This will create a new `ClientOptions` object with the connection string to your MongoDB server. Then create a new `Client` object with the `ClientOptions` object.

Congratulations, you have now set up your Rust project to use the official MongoDB Rust driver. 

In the next sections, we will cover how to create a database using MongoDB compass.

## How to Create a Database in MongoDB

Before you can create a collection in MongoDB, you need to have a database to store it in. In this section, I will show you how to create a new database in MongoDB using MongoDB Compass.

1. Open MongoDB Compass and click the **Connect** button in the top left corner of the screen.
2. In the **New Connection** window, enter the connection details for your MongoDB instance. This includes the hostname, port number, and authentication details if necessary.
3. Click **Connect** to establish a connection to your MongoDB instance.
4. In the left-hand navigation pane, click **Databases** to view a list of existing databases.
5. Click the **Create Database** button in the top left corner of the **Databases** window.
6. Enter a name for your new database (e.g “mydatabase”) and click **Create**.

Congratulations, you have created a new database in MongoDB Compass! You can now begin creating collections and adding documents to your database.

## How to Create a Collection in MongoDB

In MongoDB, a database collection is equivalent to a table in a relational database. A collection is a group of MongoDB documents that share a set of common characteristics. 

In this section, I will show you how to create a new collection in MongoDB using Rust.

### Create a new Rust function.

Open the _src/main.rs_ file in your project directory and create a new function called `create_collection`. This function will create a new collection in your MongoDB database. Add the following code to your _main.rs_ file:

```rust
async fn create_collection(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    db.create_collection(coll_name, None).await.unwrap();
}

```

This function takes a `Client` object, a database name, and a collection name as arguments. Then it creates a new collection in the specified database.

### Call the `create_collection` function.

In your main function, add the following code to call the `create_collection` function and create a new collection in your MongoDB database:

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

create_collection(&client, db_name, coll_name).await;

```

This code will create a new `Client` object and call the `create_collection` function to create a new collection called “mycollection” in the `mydatabase` database.

Congratulations, you have now created a new collection in your MongoDB database using Rust. 

In the next four sections, we will cover how to perform CRUD operations on your data, starting with inserting a document.

## How to Insert a Document into a Collection in MongoDB

In MongoDB, a row is equivalent to a document in a collection. In this section, I will show you how to insert a new document into a collection in MongoDB using Rust.

### Create a new Rust function.

Open the _src/main.rs_ file in your project directory and create a new function called `insert_document`. This function will insert a new document into the specified collection in your MongoDB database. Add the following code to your _main.rs_ file:

```rust
async fn insert_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let doc = doc! { "name": "John", "age": 30 };

    coll.insert_one(doc, None).await.unwrap();
}

```

This function takes a `Client` object, a database name, and a collection name as arguments. It then creates a new `Collection` object for the specified collection and inserts a new document into it.

### Call the `insert_document` function.

In your main function, add the following code to call the `insert_document` function and insert a new document into your MongoDB collection:

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

insert_document(&client, db_name, coll_name).await;

```

This code will create a new `Client` object and call its `insert_one` method to insert a new document with the fields `name` and `age` into the collection.

Congratulations, you have now inserted a new document into your MongoDB collection using Rust. 

In the next section, I will cover how to retrieve a document from the collection and perform other CRUD operations on your data.

## How to Retrieve a Document from a Collection in MongoDB

In MongoDB, you can retrieve a document from a collection by querying the collection with specific filter criteria. 

In this section, I will show you how to retrieve a document from a collection in MongoDB using Rust.

### Create a new Rust function.

Open the _src/main.rs_ file in your project directory and create a new function called `get_document`. This function will retrieve a document from the specified collection in your MongoDB database. Add the following code to your _main.rs_ file:

```rust
fn get_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let filter = doc! {"name": "John"};

    let result = coll.find_one(Some(filter), None).await.unwrap();
    match result {
        Some(doc) => println!("{}", doc),
        None => println!("No document found"),
    }
}

```

This function takes a `Client` object, a database name, and a collection name as arguments. It then creates a new `Collection` object for the specified collection and retrieves a document from it that matches the specified filter criteria.

In this example, we are retrieving a document in the collection that has a field called “name” with the value “John”.

### Call the `get_document` function.

In your main function, add the following code to call the `get_document` function and retrieve a document from your MongoDB collection:

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

get_document(&client, db_name, coll_name).await;

```

This code will create a new `Client` object, and retrieve a document from the `mycollection` collection that matches the filter criteria.

Congratulations, you have now retrieved a document from your MongoDB collection using Rust. In the next section, we will cover how to delete data from the collection.

## How to Delete a Document from a Collection in MongoDB

In MongoDB, you can delete a document from a collection by specifying one or more criteria to match the document. 

In this section, I will show you how to delete a document from a collection in MongoDB using Rust.

### Create a new Rust function.

Open the _src/main.rs_ file in your project directory and create a new function called `delete_document`. This function will delete a document from the specified collection in your MongoDB database. Add the following code to your _main.rs_ file:

```rust
fn delete_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let filter = doc! {"name": "John"};
    coll.delete_one(filter, None).await.unwrap();
}

```

This function takes a `Client` object, a database name, and a collection name as arguments. It then creates a new `Collection` object for the specified collection and deletes a document from it that matches the specified filter criteria.

In this example, we are deleting a document from the collection that has a field called “name” with the value “John”.

### Call the `delete_document` function.

In your main function, add the following code to call the `delete_document` function and delete a document from your MongoDB collection:

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

delete_document(&client, db_name, coll_name).await;

```

This code will create a new `Client` object, and delete a document from the `mycollection` collection that matches the filter criteria.

Congratulations, you have now deleted a document from your MongoDB collection using Rust. 

In the next section, I will cover how to modify documents in your collection.

## How to Modify a Document in a Collection in MongoDB

In MongoDB, you can modify a document in a collection by updating one or more fields in the document. In this section, I will show you how to modify a document in a collection in MongoDB using Rust.

### Create a new Rust function.

Open the _src/main.rs_ file in your project directory and create a new function called `update_document`. This function will update a document in the specified collection in your MongoDB database. Add the following code to your main.rs file:

```rust
fn update_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let filter = doc! {"name": "John"};
    let update = doc! {"$set": {"age": 35}};
    coll.update_one(filter, update, None).await.unwrap();
}

```

This function takes a `Client` object, a database name, and a collection name as arguments. It then creates a new `Collection` object for the specified collection and updates a document in it that matches the specified filter criteria.

In this example, we are updating a document in the collection that has a field called “name” with the value “John”. We are setting the value of the “age” field to “35”.

### Call the `update_document` function.

In your main function, add the following code to call the `update_document` function and update a document in your MongoDB collection:

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

update_document(&client, db_name, coll_name).await;

```

This code will create a new `Client` object, and update a document in the `mycollection` collection that matches the filter criteria.

Congratulations, you have now updated a document in your MongoDB collection using Rust. Now, you have performed all basic CRUD operations on a MongoDB database.

## Conclusion

In this article, I have introduced you to MongoDB and how to use it with Rust. I have covered the basics of setting up a MongoDB server, creating a database, and creating a collection within the database. I have also shown you how to insert, retrieve, modify, and delete data from your MongoDB database using Rust.

By leveraging the Rust programming language and the MongoDB database, you can build robust and scalable applications that can handle large amounts of data. Rust's performance and safety features make it an excellent choice for working with databases like MongoDB.

I hope that this article has provided you with a solid foundation for working with MongoDB in Rust. With the knowledge gained in this article, you should be able to build a wide range of applications that require a database backend.

Thank you for reading, and happy coding!

