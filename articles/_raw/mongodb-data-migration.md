---
title: How to Migrate Your Local Data to MongoDB Atlas
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-03-18T14:40:31.000Z'
originalURL: https://freecodecamp.org/news/mongodb-data-migration
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/mongoCloud.jpg
tags:
- name: Cloud
  slug: cloud
- name: MongoDB
  slug: mongodb
seo_title: null
seo_desc: 'Data forms the bedrock of our daily lives, as a lot of day-to-day decision-making
  is hinged on its existence. Just like energy, data can be transformed from one medium
  to another.

  So far, web development has become much more advanced, and data migrat...'
---

Data forms the bedrock of our daily lives, as a lot of day-to-day decision-making is hinged on its existence. Just like energy, data can be transformed from one medium to another.

So far, web development has become much more advanced, and data migration and backup is an essential skill every web developer should have to help ensure continuity of data and preserve user information regardless of any circumstances.

For developers like me who prefer to test all their code features locally in a development environment before final deployment to the cloud, this tutorial would come in handy for you when faced with the challenge of migrating your locally stored MongoDB data to a cloud platform or any other platform.

The inspiration for this article is a result of the need for me to migrate the total JSON data on my local MongoDB Compass server to the cloud (MongoDB Atlas) for an ongoing project. I waded through the endless internet resources and documentation but couldn’t get a suitable, straightforward fix. With multiple trials and errors, I was able to succeed with the migration. This article should serve as the definitive guide you need to save you time and achieve fast results.

In this article, we'll delve into data management in MongoDB, data backup, and efficient data migration tools that ease up the entire process. This article is suited for people with intermediate to advanced knowledge of MongoDB and backend development. 

If you have any difficulty with the terminologies used in this article, I would suggest studying the MongoDB documentation [here](https://www.mongodb.com/docs/). 

Let’s begin.

## Introduction to MongoDB

MongoDB is a non-relational NoSQL-based database that stores data via the document model in a JSON format. It’s quite popular, and ranks top among the most used databases worldwide.

It's also more code-friendly as it's currently the default database used by many JavaScript-based full stack and backend developers.

It has various database options, comprising both local database servers and a cloud-based Database-As-A-Platform. 

A good example of this is the MongoDB Atlas. MongoDB Atlas is a flexible and scalable MongoDB implementation with strong cloud security.

It provides indexing, load balancing, and sharding, among other features. More information regarding it can be found [here](https://www.mongodb.com/features).

## How to Initialize the MongoDB Server

You should have the MongoDB local server already installed. However, if you haven’t installed it, it can be downloaded [here](https://www.mongodb.com/try/download/community).

The MongoDB server can then be easily executable by adding its path to the environmental variables on Windows.

To initialize the MongoDB application, activate the command prompt and type in  
`Mongod`

![Mongo DB server running](https://hackmd.io/_uploads/r1aAf6gCp.jpg)
_MongoDb server running_

To explore the databases on the MongoDB server, open the MongoDB command shell and type `show dbs`  


![The databases in my mongodb server](https://hackmd.io/_uploads/rJY2G6eC6.jpg)
_The databses on the MongoDB server_

This displays all the databases on the MongoDB server.

With this, let's go on to migrate one of these databases to the cloud.

## How to Back Up Data

To efficiently upload the database collections to the cloud, they must first be backed up.

To back up your database, you'll have to install an additional tool. Navigate back to the MongoDB downloads site and download the MongoDB database administration [tools](https://www.mongodb.com/try/download/database-tools).

This package contains a lot of database tools, such as `MongoExport`, `MongoImport`, `MongoDump`, and `MongoRestore`. 

The above settings are applicable for users who have a version of MongoDB above version 4.4. MongoDB decided to release it as a stand-alone tool. For users whose version is less than version 4.4, these tools can be pre-installed in the MongoDB package.

Now, let's go on to the two major tools that would help facilitate the migration process: `MongoDump` and `MongoRestore`.

When `MongoDump` is executed on a database, it helps to create a backup database file in a binary-encoded JSON format (BSON). While the `MongoRestore` helps to return the backed-up database to MongoDB for usage.

Moving on, ensure that their package path is included in the environmental variables so as to guarantee efficient execution.

In order to back up a local database, open the MongoDB shell and then enter this command:

```
Mongodump --db={TheNameOFYourDB} --collection={TheNameOfYourCollection} –out={The name of the folder the backed up JSON files would be located}

```

With this execution, you have successfully backed up your local MongoDB database.

## How to Set Up a MongoDB Atlas

MongoDB Atlas is MongoDB cloud Database-As-A-Service cloud option accessible to its users at all times with little to no disruption.

Also, for most production apps that utilize the power of MongoDB on the server as a database tool, the easiest and most convenient provider of this solution is the MongoDB Atlas.

Hence, it is our choice to back up our MongoDB data to the cloud. I would assume you already have a MongoDB Atlas account, but you can still create one and then create a database that would serve as the recipient of the local database.

To set the account up, kindly navigate to the Atlas home page [here](https://www.mongodb.com/atlas/database). Create an account and you'll be directed to a dashboard where you can create new databases.  


![atllas](https://hackmd.io/_uploads/S15QNeGAp.jpg)
_MongoDb Atlas home page_

You can, however, name it with any name you want. To complete the upload of the local MongoDB data to the cloud, navigate to the settings tab on the MongoDB Atlas database and click on the migrate data option. With this successfully done, let's now go on to complete the migration process.

## How to Migrate Your Data to the Cloud

To migrate your backed-up database to the cloud, `MongoImport` and `MongoExport` will be invoked.

In the command prompt, paste the migration code copied from the Atlas, and then execute it on the command prompt. With that, you should see a success text.

You can then check and refresh your cloud database to see the new files that have been uploaded there. Thereafter, you can connect the new cloud database to your backend application and run it successfully to get the same results on your local computer.

## Conclusion

With this, we have come to the end of the tutorial. We hope you’ve learned about data management and migration in MongoDB, tools involved and all its intricacies. 

Feel free to drop comments and questions, and also check out my other articles [here](https://www.freecodecamp.org/news/author/oluwatobi/). Till next time, keep on coding!

