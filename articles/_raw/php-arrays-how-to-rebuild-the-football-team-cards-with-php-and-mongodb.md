---
title: 'PHP Arrays in Practice: How to Rebuild the Football Team Cards Project with
  PHP and MongoDB'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2024-06-18T20:58:07.000Z'
originalURL: https://freecodecamp.org/news/php-arrays-how-to-rebuild-the-football-team-cards-with-php-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/PHP-Arrays-in-Practice-Cover.png
tags:
- name: arrays
  slug: arrays
- name: handbook
  slug: handbook
- name: MongoDB
  slug: mongodb
- name: PHP
  slug: php
seo_title: null
seo_desc: 'This is the second part of my PHP array handbook. You can find the first
  part here, where I cover array basics.

  In the first part, you learned about arrays, how to create arrays, array functions,
  and how to loop through arrays.

  This second part will ...'
---

This is the second part of my PHP array handbook. You can [find the first part here](https://www.freecodecamp.org/news/php-array-handbook/), where I cover array basics.

In the first part, you learned about arrays, how to create arrays, array functions, and how to loop through arrays.

This second part will teach you how to use PHP and MongoDB to rebuild the football team cards project of freeCodeCamp's updated JavaScript curriculum.

The football team data will live in a MongDB Atlas database. We will fetch it as an array, and display it based on the players selected (goalkeepers, defenders, midfielders, and forwards).

This will help you build on top of what you learned about looping through arrays. After all, on many occassions, you'll be looping through what you get from a database or an API, not necessarily some hard-coded arrays.

In order not to shock you by jumping straight into databases from arrays, we'll start with what data and databases are, and then go on to learn about:

* Relational vs non-relational databases
    
* How to use MongoDB Atlas
    
* How to Install MongoDB for PHP on a Mac
    
* How to set up MongoDB Atlas
    
* How to build a CRUD app with PHP and MongoDB Atlas
    
* And finally, how to rebuild the football team cards project with PHP and MongoDB Atlas
    

## Pre-requisites

To get the best put of this guide, I suggest you have a basic knowledge of the following:

* PHP fundamentals (variables, arrays, functions, loops)
    
* HTML and CSS
    
* JavaScript events
    
* Command line
    
* Composer
    
* How to set up a PHP development environment with VS Code
    
* Databases
    
* MongoDB Atlas
    
* Git and GitHub
    

## Table of Contents

* [What are Data and Databases?](#heading-what-are-data-and-databases)
    
* [Relational vs Non-relational Databases](#heading-relational-vs-non-relational-databases)
    
    * [MongoDB Atlas – An Example of a Non-relational Database](#heading-mongodb-atlas-an-example-of-a-non-relational-database)
        
* [How to Install MongoDB for PHP](#heading-how-to-install-mongodb-for-php)
    
    * [Step 1: Install the MongoDB Extension with PECL (PHP Extension Community Library)](#heading-step-1-install-the-mongodb-extension-with-pecl-php-extension-community-library)
        
    * [Step 2: Modify the `php.ini` File to Include the MongoDB Extension](#heading-step-2-modify-the-phpini-file-to-include-the-mongodb-extension)
        
    * [Step 3: Verify the Installation of the MongoDB Extension](#heading-step-3-verify-the-installation-of-the-mongodb-extension)
        
    * [Step 4: Set Up a MongoDB Atlas Cluster](#heading-step-4-set-up-a-mongodb-atlas-cluster)
        
    * [Step 5: Install the MongoDB PHP Library](#heading-step-5-install-the-mongodb-php-library)
        
* [CRUD Operations Using PHP and MongoDB](#heading-crud-operations-using-php-and-mongodb)
    
    * [Step 1: Install MongoDB Library and Dotenv Package](#heading-step-1-install-mongodb-library-and-dotenv-package)
        
    * [Step 2: Create a `.env` File for your MongoDB Atlas URI Credential](#heading-step-2-create-a-env-file-for-your-mongodb-atlas-uri-credential)
        
    * [Step 3: Create a Database Connection File](#heading-step-3-create-a-database-connection-file)
        
    * [Step 4: The `READ` Part of the CRUD](#heading-step-4-the-read-part-of-the-crud)
        
    * [Step 5: The `CREATE` Part of the CRUD](#heading-step-5-the-create-part-of-the-crud)
        
    * [Step 6: The `UPDATE` Part of the CRUD](#heading-step-6-the-update-part-of-the-crud)
        
    * [Step 7: The `DELETE` Part of the CRUD](#heading-step-7-the-delete-part-of-the-crud)
        
* [Project: How to Use PHP to Rebuild the Football Team Cards Project of the Updated JavaScript Curriculum](#heading-project-how-to-use-php-to-rebuild-the-football-team-cards-project-of-the-updated-javascript-curriculum)
    
    * [Step 1: Set up MongoDB Atlas](#heading-step-1-set-up-mongodb-atlas)
        
    * [Step 2: Install the Project Dependencies with Composer](#heading-step-2-install-the-project-dependencies-with-composer)
        
    * [Step 3: Create Project Files](#heading-step-3-create-project-files)
        
    * [Step 4: Wrap the `select` tag in a `form` Element](#heading-step-4-wrap-the-select-tag-in-a-form-element)
        
    * [Step 5: Create the Logic for Fetching the Footballers from the `footballers` Collection](#heading-step-5-create-the-logic-for-fetching-the-footballers-from-the-footballers-collection)
        
    * [Step 6: Create the Logic for Filtering the Footballers Based on Position](#heading-step-6-create-the-logic-for-filtering-the-footballers-based-on-position)
        
    * [Step 7: Display the Players on the Page Based on the Selected Position](#heading-step-7-display-the-players-on-the-page-based-on-the-selected-position)
        
* [Wrapping Up](#heading-wrapping-up)
    

## What are Data and Databases?

Data is central to pretty much everything in the modern world. The people you see on social media and other websites, the content they post, the comments they add to posts, and many other online activities all produce a lot of data. Even patient files in a hospital or a company's payroll hosted on a local server are data. Data does not have to be on the Internet.

To effectively manage and utilize data for growth, you need a **database**. A **Database** is a structured collection of data that helps you efficiently store, retrieve, and manipulate that data.

Databases come in two primary types – relational and non-relational databases. We'll discuss the differences between them next.

Both relational and non-relational databases are managed with what is called database management systems (DBMS). A DBMS is an interface between the user and the database that allows you to create, read, update, and delete data in the database.

## Relational vs Non-relational Databases

### What are Relational Databases?

**Relational databases** organize data into tables consisting of rows and columns. Each table represents a specific entity, such as customers or products. The columns define the attributes of these entities, like the customer name or product name.

The relational model uses structured query language (SQL) for querying and managing data. Relationships between tables are established through primary and foreign keys to ensure data integrity and reduce redundancy.

Relational databases are known for their robustness, consistency, and support for complex queries. They are well-suited for applications that require multi-row transactions, such as financial systems, enterprise resource planning (ERP) software, and customer relationship management (CRM) systems.

Examples of relational databases are MySQL, PostgreSQL, and Microsoft SQL Server.

### What are Non-Relational Databases?

**Non-relational** databases store and manage data in flexible, schema-less formats like key-value pairs, documents, wide-columns, or graphs. They are also known as NoSQL databases because they don't use SQL like relational databases.

Non-relational databases are designed to scale horizontally, making them ideal for large-scale data processing and real-time web applications.

Non-relational databases are easy to use, scalable, and high-performing at the same time. Due to that, they often sacrifice some degree of consistency in favor of availability and partition tolerance.

Common use cases include real-time analytics, real-time web apps, and applications requiring high-speed data ingestion.

### MongoDB Atlas – An Example of a Non-relational Database

MongoDB Atlas is a non-relational database that stores data in a document-oriented JSON-like format called BSON (Binary JSON). BSON extends the JSON model to provide additional data types and to be efficient for encoding and decoding within various programming languages.

MongoDB Atlas offers the flexibility and scalability of MongoDB, with the benefits of automated deployment, backups, and monitoring. It allows developers to focus on building applications without bothering about database management

MongoDB Atlas also supports advanced features such as data partitioning, replication, and global distribution. This makes it a powerful choice for modern applications requiring flexibility and performance.

## How to Install MongoDB for PHP

Before you can install MongoDB for PHP, make sure you have PHP itself installed correctly.

On a Mac, you can install PHP with homebrew by running `brew install PHP`. In addition to that, make sure you have Apache installed by running `brew install httpd` and starting it by running `brew services start httpd`.

You can follow the steps below to install MongoDB for PHP on a Mac.

### Step 1: Install the MongoDB Extension with PECL (PHP Extension Community Library)

Install the MongoDB extension for PHP by running `pecl install mongodb`.

### Step 2: Modify the `php.ini` File to Include the MongoDB Extension

Installing the MongoDB extension should automatically add the necessary configurations to the `php.ini` file. But of it doesnt do that, locate the `php.ini` file by running the command below:

```bash
$ php --ini
Configuration File (php.ini) Path: /usr/local/etc/php/8.3
```

After that, paste the following at the end of the `php.ini` file and save it:

```bash
extension=mongodb.so
```

After doing that, restart Apache by running `brew services restart httpd`.

### Step 3: Verify the Installation of the MongoDB Extension

Run the command below to see whether the PHP extension has been successflly installed:

```bash
php -i | grep mongo
```

You should see something like this in the terminal:

![Screenshot-2024-05-24-at-09.21.50](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.21.50.png align="left")

Check out [the MongoDB PHP docs](https://www.mongodb.com/docs/languages/php/) for more information on how to use MongoDB with PHP and frameworks like Laravel and Symfony.

### Step 4: Set Up a MongoDB Atlas Cluster

To test out the PHP extension you just installed, you need a MongoDB database. Atlas makes this easy for you because the heavy lifting is handled on the cloud.

#### 1\. Login to your MongoDB Account

Head over to https://cloud.mongodb.com/ and log in to your account. If you don't have an account, **you can create one for free**.

#### 2\. Create a Project

If you have existing projects, create a new project by clicking on the arrow right beside the currently opened project and selecting "New Project".

![Screenshot-2024-05-24-at-09.34.05](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.34.05.png align="left")

Give your project a name and click the "Next" button.

![Screenshot-2024-05-24-at-09.37.13](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.37.13.png align="left")

Click "Create Project" to finally create the project.

![Screenshot-2024-05-24-at-09.38.29](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.38.29.png align="left")

#### 3\. Create a Cluster

After creating a project, you should be prompted to create a cluster. If you're not, make sure you're in the Overview tab. From there, click the big "Create" button:

![create-giant-1](https://www.freecodecamp.org/news/content/images/2024/06/create-giant-1.png align="left")

Select the "MO" free tier, give your cluster a name, and click the "Create Deployment" button.

![Screenshot-2024-05-24-at-09.44.11](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.44.11.png align="left")

I have given the cluster the name `movie-list`.

Just keep in mind that as your database grows, you might need to upgrade to one of the paid tiers.

#### 4\. Create a Database User

Immediately after you create your cluster, you'll be prompted to create a database user. Fill in your database user username and password and click the "Create Database User" button. Then click "Choose a connection method".

![Screenshot-2024-05-24-at-09.50.54](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.50.54.png align="left")

Make sure you enter a password you can remember or save it in a password manager.

#### 5\. Choose a Connection Method

You'll see several methods you can use to connect to the cluster once you click the "Choose a connection method" button.

![Screenshot-2024-05-24-at-09.56.37](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.56.37.png align="left")

Select Drivers from the list.

![Screenshot-2024-05-24-at-09.58.02](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.58.02.png align="left")

Choose PHP from the list and select PHP Lib 1.9 + MongoDB 1.10 or later as the version to use. Then copy the connection string and click the "Done" button.

![Screenshot-2024-05-24-at-10.02.55](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.02.55.png align="left")

#### 6\. Choose Network Access

Head over to the "Network Access" tab and select "Add IP ADDRESS", click "ALLOW ACCESS FROM ANYWHERE", and then click the "Confirm" button. You can change this later depending on where your app is deployed.

![Screenshot-2024-05-24-at-10.05.03](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.05.03.png align="left")

Go back to the "Database" tab and click the "Browse Collections" button.

![Screenshot-2024-05-24-at-10.07.48](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.07.48.png align="left")

Select "Load a Sample Dataset" so you don't have to add your own data – at least for now.

![Screenshot-2024-05-24-at-10.24.54](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.24.54.png align="left")

Now you should see the following databases:

![Screenshot-2024-05-24-at-10.28.04](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.28.04.png align="left")

To test that your MongoDB extension for PHP is running, you can query any of the data in those databases. But first, you need to install the MongoDB PHP library with `composer`. `composer` lets you manage dependencies for your PHP project.

### Step 5: Install the MongoDB PHP Library

If you don't have `composer` installed, install it with homebrew by running `brew install composer`.

After that, create a folder and open it with your Text Editor. If your Text Editor has an integrated terminal, open it and run the command below:

```bash
composer require mongodb/mongodb
```

If the installation is successful, you'll see a `vendor` folder, along with `composer.json` and `composer.lock` files in the root of your project. You'll also see the following in the terminal:

![Screenshot-2024-05-24-at-10.36.29](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.36.29.png align="left")

Now you need to query any data in your atlas database and display them.

Create an `index.php` file and paste the following inside it:

```php
<?php

require_once __DIR__ . '/vendor/autoload.php';

// Your connection string
$client = new MongoDB\Client(
 'mongodb+srv://username:<password>@movie-list.s6r7qkr.mongodb.net/?retryWrites=true&w=majority&appName=movie-list'
);

$movies = $client->selectCollection('sample_mflix', 'movies');
$document = $movies->findOne(['title' => 'Wild and Woolly']);

echo '<pre>';
print_r($document);
```

The code above lets you connect to the `movies` database in the `sample_mflix` collection with the `selectCollection()` function and query a movie titled "Wild and Bolly" in it.

**Note**: Make sure you replace the existing connection string with your own. You copied this in item 5 of step 4. Also, make sure you replace `<password>` with your database user password.

After that, run your PHP app (with `php -S localhost:8000` on Mac in the terminal). If you have everything set up correctly, you should see the following in the browser:

![Screenshot-2024-05-24-at-10.54.05](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.54.05.png align="left")

**Note**: I have the data formatted nicely because I installed the PHP View Chrome extension. It prints everything you have inside the `print_r()` function like that.

## CRUD Operations Using PHP and MongoDB

With MongoDB Atlas for database management and UI persistence, and PHP for server-side logic, you can build an application that implements full CRUD operations – create, read, update, and delete.

The particular CRUD app we are building is a movie list. So make sure you set up an Atlas database for it, as we already covered in this guide.

Now let's look at how you can build a movie list CRUD app.

### Step 1: Install MongoDB Library and Dotenv Package

Make sure you have a MongoDB extension and a Dotenv package to help manage your `.env` variables by running the following commands:

```bash
composer require mongodb/mongodb
composer require vlucas/phpdotenv
```

### Step 2: Create a `.env` File for your MongoDB Atlas URI Credential

Create a `.env` file and add the following in it:

```md
MDB_URI="Your MongoDB Atlas connection string"
```

### Step 3: Create a Database Connection File

Create a `mongo_atlas_setup.php` file for the database connection in the root and paste the following in it:

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$client = new MongoDB\Client($_ENV['MDB_URI']);

function getMongoClient()
{
 global $client;
 return $client;
}

function getMongoCollection($database, $collection)
{
 $client = getMongoClient();
 return $client->selectCollection($database, $collection);
}
```

With the code above, we are:

* loading the dependencies required for the project
    
* loading the environment variable
    
* using a function to get the database and the collection we want within it
    

Importing the file and calling the `getMongoCollection` in it with the database and the collection in it will let you connect to the database and the collection.

### Step 4: The `READ` Part of the CRUD

In the root again, create an `index.php` file that will take care of the READ part of the CRUD. Paste the following in the file:

```php
<?php

require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/mongo_atlas_setup.php';

$movies_list = getMongoCollection('movie_list', 'movies');
$movies = $movies_list->find([], ['sort' => ['_id' => -1]]);
?>

<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Movie List CRUD App</title>
 <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 p-10">

 <div class="max-w-4xl mx-auto bg-white p-6 rounded shadow">
   <h1 class="text-3xl font-bold mb-4 text-center">Movie List CRUD App</h1>

   <?php include 'create.php' ?>

   <div class="space-y-4">
     <?php foreach ($movies as $movie) : ?>
       <div class="p-4 border rounded shadow-sm bg-gray-50">
         <h2 class="text-2xl font-semibold"><?= $movie['movie_title'] ?></h2>
         <p class="text-gray-700">Year: <?= $movie['movie_year'] ?></p>
         <div class="mt-2">
           <a href="update.php?id=<?= $movie['_id'] ?>" class="bg-yellow-500 text-white py-1 px-3 rounded">Update</a>
           <a href="delete.php?id=<?= $movie['_id'] ?>" onclick="return confirm('Are you sure you want to delete this movie?')" class="bg-red-500 text-white py-1 px-3 rounded">Delete</a>
         </div>
       </div>
     <?php endforeach ?>
   </div>
 </div>

</body>

</html>
```

Notice that there are the Update and Delete linking to an `update.php` and a `delete.php` files with the id of the movie clicked. That way, we will know which movie is clicked in order to update or delete it. There's also an include statement for a `create.php` file.

For now, you can go ahead and create the `create.php`, `update.php`, and `delete.php` files in the root.

At this point, you won't see anything in the UI yet because you need to handle the creation functionality.

### Step 5: The `CREATE` Part of the CRUD

Create a `create.php` file in the root (if you haven't already) and paste in the following:

```php
<?php
require_once __DIR__ . '/mongo_atlas_setup.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 $movies = getMongoCollection('movie_list', 'movies');
 $newMovie = [
   'movie_title' => $_POST['movie-title'],
   'movie_year' => (int)$_POST['movie-year'],
 ];
 $result = $movies->insertOne($newMovie);
 if ($result->getInsertedCount() === 1) {
   // echo "Movie created successfully!";
   header('Location: ' . '/');
 } else {
   echo "Failed to create movie";
 }
}
?>

<form method="POST" action="create.php" class="space-y-4 mb-6">
 <div>
   <label class="block text-gray-700">Movie Title</label>
   <input type="text" name="movie-title" required class="w-full p-2 border rounded max-w-md">
 </div>
 <div>
   <label class="block text-gray-700">Movie Year</label>
   <input type="text" name="movie-year" required class="w-full p-2 border rounded max-w-md">
 </div>
 <button type="submit" class="bg-green-500 text-white py-2 px-4 rounded">Create</button>
</form>
```

The code above contains the form and input elements for creating a movie. We are then using the name attributes in those input elements to create the `POST` request that will let us create a movie and save it in the `movies` collection of a `movie_list` database.

### Step 6: The `UPDATE` Part of the CRUD

To handle the updating, we need to create a separate file and do something similar to how the movie creation worked. The exeception is that we are going to use the id (`_id`) field to determine whether the movie exists and then update it instead of creating a fresh one.

To do that, create an `update.php` file (if you haven't already) in the root and paste in the following:

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/mongo_atlas_setup.php';

use MongoDB\BSON\ObjectId;

$movies_list = getMongoCollection('movie_list', 'movies');
$title = '';
$year = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 $filter = ['_id' => new ObjectId($_POST['id'])];
 
 $update = ['$set' => [
   'movie_title' => $_POST['movie-title'],
   'movie_year' => (int)$_POST['movie-year'],
 ]];
 
 $result = $movies_list->updateOne($filter, $update);
 
 if ($result->getModifiedCount() === 1) {
   // echo "Movie updated successfully!";
   header('Location: ' . '/');
 } else {
   echo "Failed to update movie.";
 }
} else {
 if (isset($_GET['id'])) {
   $id = $_GET['id'];
   $movie = $movies_list->findOne(['_id' => new ObjectId($id)]);
   if ($movie) {
     $title = $movie['movie_title'];
     $year = $movie['movie_year'];
   } else {
     echo "Movie not found.";
     exit;
   }
 } else {
   echo "No movie ID provided.";
   exit;
 }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <script src="https://cdn.tailwindcss.com"></script>
 <title>Update Movie </title>
</head>

<body class="bg-gray-100 p-10">

 <div class="max-w-4xl mx-auto bg-white p-6 rounded shadow">
   <h1 class="text-3xl font-bold mb-4">Update <?= $title ?> </h1>

   <form method="POST" action="update.php" class="space-y-4">
     <input type="hidden" name="id" value="<?php echo $id; ?>">

     <div>
       <label class="block text-gray-700">Title</label>
       <input type="text" name="movie-title" value="<?= htmlspecialchars($title); ?>" required class="w-full p-2 border rounded" />
     </div>

     <div>
       <label class="block text-gray-700">Release Year</label>
       <input type="number" name="movie-year" value="<?= htmlspecialchars($year); ?>" required class="w-full p-2 border rounded" />
     </div>

     <button class=" bg-green-500 text-white py-2 px-4 rounded" type="submit">Update</button>
   </form>

   <div class="mt-4">
     <a href="index.php" class="bg-gray-500 text-white py-2 px-4 rounded">Back to List</a>
   </div>
 </div>

</body>

</html>
```

### Step 7: The `DELETE` Part of the CRUD

To handle the delete functionality, we can get the movie and use the `deleteOne` function provided by MongoDB to delete it. Once the deleting is done, we will then use the `header()` function again to redirect to the home page.

Paste the following code in your `delete.php` file:

```php
<?php
require_once __DIR__ . '/mongo_atlas_setup.php';

use MongoDB\BSON\ObjectId;

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id'])) {
 $movies = getMongoCollection('movie_list', 'movies');
 $filter = ['_id' => new ObjectId($_GET['id'])];
 $result = $movies->deleteOne($filter);
 if ($result->getDeletedCount() === 1) {
   // echo "Movie deleted successfully!";
   header('Location: ' . '/');
 } else {
   echo "Failed to delete movie.";
 }
} else {
 echo "No movie provided.";
}
?>
```

This is what the CRUD app should look like now:

![CRUD-gif](https://www.freecodecamp.org/news/content/images/2024/06/CRUD-gif.gif align="left")

All the code is in this [GitHub repo](https://github.com/Ksound22/crud-app-for-php-fcc-article)

## Project: How to Use PHP to Rebuild the Football Team Cards Project of the Updated JavaScript Curriculum

Before you start going through the steps to build the project, grab the starter code for the project in [the starter branch of this GitHub repo](https://github.com/Ksound22/football-team-cards-php-rebuild).

You can also take a look at [the football team cards project](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-modern-javascript-methods-by-building-football-team-cards/step-1) to know what we are trying to achieve.

### Step 1: Set up MongoDB Atlas

Log in to your MongoDB Atlas account and create a `football-team-cards` database. Feel free to create it in an existing project or a new one if you want. In the `football-team-cards` database, create a `footballers` collection.

In the `footballers` collection, click the "INSERT DOCUMENT" button.

![Screenshot-2024-06-09-at-14.33.15](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-14.33.15.png align="left")

Then paste in the content of the `footballers.json` file in the starter branch of the project GitHub repo and click "Done".

![Screenshot-2024-06-09-at-14.42.47](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-14.42.47.png align="left")

After that, your `footballers` collection should look like this:

![Screenshot-2024-06-09-at-14.44.59](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-14.44.59.png align="left")

### Step 2: Install the Project Dependencies with Composer

Create a `football-team-cards-php` folder on your computer and open it with your favorite text editor. Open the same folder in your terminal and run the following commands:

```bash
composer require vlucas/phpdotenv 
composer require mongodb/mongodb
```

### Step 3: Create Project Files

Inside the `football-team-cards-php` folder, create the following files:

* `.env`
    
* `mongo_atlas_php_setup.php`
    
* `index.php`
    
* `styles.css`
    

In the `.env` file, you should have the MongoDB Atlas URI:

```bash
MDB_URI="Your MongoDB Atlas connection string"
```

In the `mongo_atlas_php_setup.php` file, you should connect to the database with this code:

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


function getMongoClient()
{
 return new MongoDB\Client($_ENV['MDB_URI']);
}


function getMongoCollection($database, $collection)
{
 $client = getMongoClient();
 return $client->selectCollection($database, $collection);
}
```

In the code above, we are loading the environment variables and using a `getMongCollection` function to connect the database. Make sure you replace the connection string with your own.

Now, anytime you want to connect to a database, require the file, then pass the database and the collection names to the `getMongoCollection` function.

Copy the content of the `index.html` and `styles.css` files in the starter branch of the project GitHub repo and paste them into your `index.php` and `styles.css` files.

### Step 4: Wrap the `select` tag in a `form` Element

Replace the existing `select` tag with the following:

```html
<form method="POST" action="">
     <label class="options-label" for="players">Filter Teammates:</label>
     <select name="position" id="players" onchange="this.form.submit()">
       <option value="all">All Players</option>
       <option value="nickname">Nicknames</option>
       <option value="forward">Position Forward</option>
       <option value="midfielder">Position Midfielder</option>
       <option value="defender">Position Defender</option>
       <option value="goalkeeper">Position Goalkeeper</option>
     </select>
</form>
```

This will let you make a `POST` request with the `name` attribute set to `position`. And with the `onchange` attribute of `this.form.submit()`, you'll be able to fetch footballers based on any of the options selected. More on this later.

### Step 5: Create the Logic for Fetching the Footballers from the `footballers` Collection

```php
require_once __DIR__ . '/mongo_atlas_php_setup.php';

$position = isset($_POST['position']) ? $_POST['position'] : 'all';

$collection = getMongoCollection('football-team-cards', 'footballers');
$team = $collection->findOne(['team' => 'Argentina']);
$players = $team['players']->getArrayCopy();
```

With the code above, we are:

* importing the database connection file
    
* checking for `POST` data with the name on the `select` tag and setting a default value of `all` (the first option in the select element)
    
* getting the database and collection in it
    
* using the `findOne` method from MongoDB to get the team
    
* and fetching the data as an array with `getArraCopy()` so we can loop through it
    

At this point, you can print the `$players` variable with `print_r()` or `var_dump()` to see what it looks like. On my end, it looks like this when I ran the app with `php -S localhost:4000`:

![Screenshot-2024-06-09-at-16.24.47](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-16.24.47.png align="left")

### Step 6: Create the Logic for Filtering the Footballers Based on Position

Remember we have to display the players based on whether they are goakeepers, defenders, midfielders, or forwards. To do that, we can utilize the code below:

```php
$filteredPlayers = $players;


if ($position !== 'all') {
 if ($position === 'nickname') {
   $filteredPlayers = array_filter($players, function ($player) {
     return !empty($player['nickname']);
   });
 } else {
   $filteredPlayers = array_filter($players, function ($player) use ($position) {
     return $player['position'] === $position;
   });
 }
}
```

At first, we are initializing `$filteredPlayers` to all the players. If the selected position is not `all`, we filter the players based on `nickname`. And if the selected position is not `nickname`, we filter the players to include only those whose position matches the selected `position`.

### Step 7: Display the Players on the Page Based on the Selected Position

Now, all we need to do is set each option's value (all players, goalkeepers, defenders, midfielders, forwards) to `selected` if that option is matched. After that, we need to use `foreach` loop to do the proper display.

Here's one way you can set the value of each `option` to `selected`:

```php
<option value="all" <?= $position === 'all' ? 'selected' : '' ?>>All Players</option>
       <option value="nickname" <?= $position === 'nickname' ? 'selected' : '' ?>>Nicknames</option>
       <option value="forward" <?= $position === 'forward' ? 'selected' : '' ?>>Forwards</option>
       <option value="midfielder" <?= $position === 'midfielder' ? 'selected' : '' ?>>Midfielders</option>
       <option value="defender" <?= $position === 'defender' ? 'selected' : '' ?>>Defenders</option>
       <option value="goalkeeper" <?= $position === 'goalkeeper' ? 'selected' : '' ?>>Goalkeepers</option>
```

And here's how you can use the `foreach` loop to finally display the players selected:

```php
<div class="cards" id="player-cards">
     <?php if (empty($filteredPlayers)) : ?>
       <p>No players found for the selected position.</p>
     <?php else : ?>
       <?php foreach ($filteredPlayers as $players) : ?>
         <div class="player-card">
           <h2><?= $players['name'] . ($players['isCaptain'] ? ' (Captain)' : '') ?></h2>
           <p>Position: <?= $players['position'] ?></p>
           <p>Number: <?= $players['number'] ?></p>
           <p>Nickname: <?= !empty($players['nickname']) ? $players['nickname'] : 'N/A' ?></p>
         </div>
       <?php endforeach ?>
     <?php endif ?>
   </div>
```

Now, everything works as expected:

![football-team-cards](https://www.freecodecamp.org/news/content/images/2024/06/football-team-cards.gif align="left")

You can grab the final code of the project in the main branch of this [GitHub repo](https://github.com/Ksound22/football-team-cards-php-rebuild).

## Wrapping Up

Rebuilding the football team cards project with PHP and MongoDB Atlas shows just how powerful and flexible it can be to combine server-side scripting with a cloud-based NoSQL database.

The project not only highlights how smoothly PHP and MongoDB Atlas work together, but it also shows the advantages of using a cloud-based database like Atlas. Atlas offers scalability, high availability, and easy management, making it a great choice for modern web applications.

Whichever data-driven application you're making, these techniques that we used here to build the project and the initial CRUD app can help you out.

Happy coding!
