---
title: How to Use IndexedDB – Database Guide for Beginners
subtitle: ''
author: Victor Yakubu
co_authors: []
series: null
date: '2022-09-08T16:23:00.000Z'
originalURL: https://freecodecamp.org/news/how-indexeddb-works-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Colorful-Minimalist-Shapes-Internal-Pitch-Deck-Talking-Presentation-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: database
  slug: database
seo_title: null
seo_desc: "The modern browser has given us a number of options when it comes to storing\
  \ data on the client-side. Aside from storing data, browser databases allow us to\
  \ retrieve that data. \nBased on your application's needs, you can choose from the\
  \ different bro..."
---

The modern browser has given us a number of options when it comes to storing data on the client-side. Aside from storing data, browser databases allow us to retrieve that data. 

Based on your application's needs, you can choose from the different browser storage options out there to enhance your users' experience when they use your applications. 

One of these browser storage options is IndexedDB. I used IndexedDB for the first time a couple of months ago. Before using it, I went through articles and videos on various implementations of it. So I thought it would be nice to write about it based on my understanding of how it works. 

So basically in this article, I will be talking about what IndexedDB is, its advantages, and how it works.

## What is a Database?

These days, data are everywhere. Data can be any information such as your age, location, what you've recently purchased from an online site, and so on. Data can be in the form of videos, images, files or even text.  

Companies need to be able to store and process that data effectively, and they use databases for this purpose.

Now, a database is simply where you store data – it's that simple. So if you open an excel sheet, for example, and populate it with data, that is considered a database. 

The purpose of storing data in a database is to make it easy to access. This lets you modify it, protect it, and also analyze it to get as many insights as you can.

## Types of Databases

There are mainly two types of database out there. Depending on your needs you'll want to try both out on you journey:

### Relational Databases

In a relational database, data is stored in a collection of tables. These tables are connected to one another. 

Examples of relational databases include Oracle, PostgreSQL, MySQL, Microsoft SQL Server, and so on.

### Non-Relational Databases

In a non-relational database, data is stored in collections. There are no tables, columns, or rows and the data are not connected to one another. 

Under non-relational databases, there are different categories: key-value databases, Document Databases, graph databases, wide column databases, search engine databases, and more.

Examples of non-relational database include Redis, MongoDB, Neo4j, Cassandra, and others, our very own IndexedDB is also a non-relational database.

In this article we won't cover databases themselves in-depth, as it is not the primary purpose. But [Dionysia Lemonaki](https://www.freecodecamp.org/news/author/dionysia/) has a more detailed article on relational and non-relational databases which you can check out [here](https://www.freecodecamp.org/news/relational-vs-nonrelational-databases-difference-between-sql-db-and-nosql-db/) to learn more.

It's exciting to know that IndexedDB, which we will be talking about here, is a database that is available on all modern browsers. But, IndexedDB is not the only browser storage option available to you. There's also [local storage](https://www.freecodecamp.org/news/how-leverage-local-storage-to-build-lightning-fast-apps-4e8218134e0c/), [session storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage), [cookies](https://www.freecodecamp.org/news/everything-you-need-to-know-about-cookies-for-web-development/), [Web SQL](https://www.w3.org/TR/webdatabase/), and [cache storage](https://www.freecodecamp.org/news/web-caching-explained-by-buying-milk-at-the-supermarket-2ba6133ca4ed/). 

You might already be familiar with these options, but if you are not, I encourage you to read more about them. 

## What is Browser Storage? How is it Different from Server Storage?

Browser storage is also referred to as client-side storage. It simply means storage that's located on a user's browser.

Just like server-side storage (which allows you to store data on a database called the backend) where you are able to communicate with the database using lines of code, client-side storage uses the same principle. 

But keep in mind that client-side storage is not a substitute for server-side storage. Client-side storage a mainly used to enhance the user's experience. 

A simple example is when you log in to a platform for the first time. The server-side storage handles authentication and necessary authorizations, and the client-side storage makes it possible for you to visit that platform after a few hours and continue from your previous state without having to send a request to the backend.

And then, whenever you need to log in after some time, the client-side storage saves your login details, and auto-fills them in. All that will be required from you is to click the login button.

Server-side can be written and accessed using any number of programming languages depending on your preference – like Python, Ruby, C#, PHP and JavaScript (NodeJS). For the client-side, you'll mostly use JavaScript to access and communicate with the browser storage.

Alright, now let's learn about IndexedDB.

## What is IndexedDB?

Above we talked about non-relational databases and their different types. We also mentioned key-value databases as one of these types, right? Well, IndexedDB is an example of a key-value database.

### What is a Key-Value Database?

A key-value database means that all the data stored must be assigned to a key. It is one of the less complicated non-relational databases, at least in my opinion. 

A key value database associates a key to a value. The key serves as a unique identifier for that value, which means that you can keep track of that value using the key.

If your app needs to fetch data constantly, key-value databases use really efficient and compact index structures to quickly and reliably locate values by their keys. Using the key you are able to not only retrieve the value stored, but also delete, update, and replace the value.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/key-value.png)
_[key-value database](https://mdn.github.io/learning-area/javascript/apis/client-side-storage/indexeddb/notes/)_

Okay, I believe you understand what key-value database is all about now? let's continue talking about IndexedDB. 

### **Advantages of IndexedDB**

So we have all these browser storage options available to us, which is a great thing because we can choose one based on our needs. And each option has different capabilities. 

So it's important to know how each works and their capabilities so you can choose the right one for your use case.

That being said, IndexedDB has the following advantages:

1. IndexedDB is asynchronous, meaning it does not stop the user interface from rendering while the data loads.
2. It allows you to categorise your data using object stores.
3. It allows you to store large amounts of data.
4. It supports objects like videos, images, and so on – any object that supports a structured clone algorithm.
5. It supports database transactions and versioning.
6. It has great performance.
7. The database is private to an origin.
8. It is supported on all modern browsers.

### Use Cases of IndexedDB 

Aside from knowing how IndexedDB works, it's also important to know when you should use it.

* **To store user-generated content:** An example of user generated content is filling out an application form. While still in the process of completing the form, a user can leave it and come back some time later to complete the form without losing their initial data inputs.
* **To store application state:** When a user first loads a website or application, you can use IndexedDB to store these initial states. These can be log in authentications, API requests, or any other state needed before the UI is rendered. So when next the user visits the site, the load speed increases because the application has state already stored. This means that it renders the UI faster.
* **For an application that works offline:** Users can edit and add data while the application is offline. IndexedDB will process and empty these operations in a synchronization queue when the application comes online.

## How IndexedDB Works

Now to the main part of this article: learning how IndexedDB works. We will be using the flowchart below, and we will go over the various events and paths one after the other and the associated JavaScript code to properly explain them.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-1.drawio--1-.png)
_IndexedDB event flowchart_

### Path 1: What to do if the database does not exist

When you create a new database in IndexedDB this is the path it will follow. This path is pretty straightforward:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-2.drawio.png)

An important thing to note is that, when creating a Database, you will have to give the database a name and a version (you determine any version to give the database). 

Also, when you create a database for the first time, **version 1** is automatically assigned to it even without you stating a version.

Now, let's explain the flowchart above. When you create a database, it checks if a database with that name (dbname) exists already. 

If it doesn't exist, it will proceed to call the **upgrade** event. When the upgrade event gets called, you can then upgrade the structure of the database. When the upgrade event block runs successfully, it will then call the **success** event.

```
        const request = indexedDB.open('myDatabase', 1);

        //upgrade event
        request.onupgradeneeded = () => {
            alert("upgrade needed")
        }

        //on success
        request.onsuccess = () => {
            alert("success is called")
        }
```

### Path 2: What to do if the database exists but has a new version greater than the previous version

Now we'll look at the second path. When a new database is created, it first checks to see if the database already exists. 

If a database with the same name exists, it then checks the version to see if the version is greater than the previous version. If it is, it then calls the **upgrade** event where you can modify the structure of the database. And after that is done, it calls the **success** event.



![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-3.drawio.png)

Following the explanation above, now let's look at the code below.

Let's assume we had already created a database with the name "myDatabase". Since the database name is the same as the one we previously created, it then moves to check the version. The previous version was "version 1". Since we changed the version to "version 2" and since version 2 > version 1, it will then execute the modification inside the **onupgradeneeded** function.

```
    const request = indexedDB.open('myDatabase', 2);

        //upgrade event
        request.onupgradeneeded = () => {
            alert("upgrade needed")
        }

        //on success
        request.onsuccess = () => {
            alert("success is called")
        }
```

### Path 3: What to do if the database exists, but the version is less than the current version

Following the flowchart below, if the database already exists, and the version is less than the current version, it then moves to check if the version is the same as the current version. 

There are two possible outcome here: first, if the version is the same as the current version it calls the **success** event, i.e. no update will be made, the database stays the same, no error is thrown. Second, if the version is less that the current version, it fails and throws an error.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-4.drawio--3-.png)

### How to create an Object Store and Transaction in IndexedDB

* [**Object Store**](https://developer.mozilla.org/en-US/docs/Web/API/IDBObjectStore): Is a collection of objects inside a database, a database can have different object stores. considering the code below, myDatabase is the database created, while myDatabaseStore is the object store created inside the database. The object store can be used to store any form of data. I used the code below to explain how to create an object store.

```
let db;

const openRequest = indexedDB.open('myDatabase', 1);

openRequest.onupgradeneeded = function (e) {
    db = e.target.result;
    console.log('running onupgradeneeded');
    const storeOS = db.createObjectStore('myDatabaseStore',  {keyPath: "name"});
                
 };
openRequest.onsuccess = function (e) {
    console.log('running onsuccess');
    db = e.target.result;
};
openRequest.onerror = function (e) {
    console.log('onerror! doesnt work');
};

```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/key-value-1.png)
_Creating object store_

* [**Transaction**](https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction): A transaction is a sequence of task wrapper together. For a transaction to be successful, all the task wrapped into it must pass, if one fails, none will pass. If that happens, no update will be made to the database. Transaction has methods, properties and events you can explore. In the code below, I was able to add item to the object store by wrapping it in a transaction.

```
let db;

const openRequest = indexedDB.open('myDatabase', 2);

openRequest.onupgradeneeded = function (e) {
    db = e.target.result;
    console.log('running onupgradeneeded');
    const storeOS = db.createObjectStore('myDatabaseStore',  {keyPath: "name"});
                
};
openRequest.onsuccess = function (e) {
    console.log('running onsuccess');
    db = e.target.result;
    addItem();
};
openRequest.onerror = function (e) {
    console.log('onerror! doesnt work');
    console.dir(e);
};

function addItem() {
    const item = {
        name: 'banana',
        price: '$2.99',
        description: 'It is a purple banana!',
        created: new Date().getTime(),
    };
    const tx = db.transaction("myDatabaseStore", "readwrite");
    const store = tx.objectStore('myDatabaseStore');
    store.add(item);
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/key-value-2.png)
_Adding item to the store_

## Conclusion

IndexedDB is a very powerful client-side storage option that developers can use to provide a better user experience for their websites or applications. It helps you reduce the time it takes to load data from a website or application that your users visit frequently.

If you haven't built something with IndexedDB, I encourage you to try it out. This article did not cover how to do that, but there I materials online that will guide you. Building stuff will help you appreciate IndexeDB more.

I hope you enjoyed reading it as I enjoyed writing it.

**Relevant Documentation on IndexedDB:**

* [www.w3.org/IndexedDB](https://www.w3.org/TR/IndexedDB/#introduction)
* [developer.mozilla.org/IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)

