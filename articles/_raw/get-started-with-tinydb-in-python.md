---
title: How to Get Started with TinyDB in Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-13T18:46:34.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-tinydb-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/tinydb--1-.png
tags:
- name: database
  slug: database
- name: Python
  slug: python
seo_title: null
seo_desc: "While working on your personal projects, you'll often need to store some\
  \ data. You could use a SQL or NoSQL database with a server, but that would require\
  \ you to do a bit of setup. \nIn this article, we'll learn about TinyDB and how\
  \ to use it to store..."
---

While working on your personal projects, you'll often need to store some data. You could use a SQL or NoSQL database with a server, but that would require you to do a bit of setup. 

In this article, we'll learn about TinyDB and how to use it to store our data in JSON format.

## What is TinyDB?

TinyDB is a document-oriented database written in pure Python with no external dependencies. 

It is designed to be easy and fun to use by providing a simple and clean API. It is quite straightforward to learn and set up, even for a beginner.

### When not to use TinyDB

As mentioned in the TinyDB docs itself, it is not always the right choice for your projects. If you need advanced features like:

* access from multiple processes or threads,
* creating indexes for tables,
* an HTTP server,
* managing relationships between tables or similar,
* [ACID guarantees](https://en.wikipedia.org/wiki/ACID).

TinyDB is the wrong database for you. In those cases, consider using databases like [SQLite](https://www.sqlite.org/), [Buzhug](https://buzhug.sourceforge.net/), [CodernityDB](http://labs.codernity.com/codernitydb/) or [MongoDB](https://mongodb.org/).

## How to Install TinyDB

It is extremely easy to install TinyDB. Just run this command in your terminal:

```bash
pip install tinydb
```

## How to Use TinyDB

Consider an example of a Todo Application where we just need to perform CRUD operations. Now that we have TinyDB installed, let's see how we can store our data using TinyDB. TinyDB does everything using JSON.

The very first thing we'll do is to import the required classes from the `tinydb` module. So, fire up your Python shell to code along.

```bash
$ python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Now we are ready to code.

```repl
>>> from tinydb import TinyDB       
>>> db = TinyDB("todo_db.json")
>>> 
```

We have created an instance of the _TinyDB_ class and passed the filename to it. This will create a JSON file `todo_app.json` where our data will be stored.

### How to Insert Data in TinyDB

As we are dealing with JSON, the data to be added will be nothing but a [Python Dictionary](https://iread.ga/posts/84/everything-you-need-to-know-about-python-dictionaries). So, let's see how we can insert an item:

```repl
>>> new_item = {"name": "Book", "quantity": 5}
>>> db.insert(new_item) 
1
>>> 
```

First of all, we created a new dictionary called `new_item` with `name` and `quantity` set to `Book` and `5`, respectively. Then we used the `insert()` method in the _TinyDB_ class to insert the data into the database. The `insert()` method returns the `id` of the newly created object.

At this stage, a new JSON file called `todo_db.json` will be created and after the data is inserted. It will look like this:

```json
{"_default": {"1": {"name": "Book", "quantity": 5}}}
```

If you take a closer look, `_default` is the name of the table (set by default but can be changed),  `1` is the id of the newly created object, and its value is the data we just inserted. So, basically it is just a nested dictionary.

We can also insert multiple items at a time like this:

```python
>>> items = [
...         {"name": "Cake", "quantity": 1},
...         {"name": "Candles", "quantity": 10},
...         {"name": "Balloons", "quantity": 50}
...     ]
>>> db.insert_multiple(items)   
[2, 3, 4]
```

In this case, we created a list of dictionaries called `items` and used the `insert_multiple()`method to insert the items. This method also returns a list of `id`s of the objects inserted.

The `todo_db.json` file now looks like this:

```json
{
  "_default": {
    "1": { "name": "Book", "quantity": 5 },
    "2": { "name": "Cake", "quantity": 1 },
    "3": { "name": "Candles", "quantity": 10 },
    "4": { "name": "Balloons", "quantity": 50 }
  }
}

```

### How to Retrieve Data from TinyDB

There are several ways to retrieve data from your database. But you will need to create an instance of the _Query_ class first. So, let's do that:

```repl
>>> from tinydb import Query
>>> Todo = Query()
>>> 
```

You can use the `db.search()` method to retrieve data. 

```repl
>>> db.search(Todo.name == 'Book')
[{'name': 'Book', 'quantity': 5}]
>>> db.search(Todo.name == 'Copies') 
[]
>>>
```

The `search()` method returns the list of items matching the query. If no such item is there, it returns an empty list.

We can also use the `get()` method to get an item.

```repl
>>> db.get(Todo.name == 'Book')
{'name': 'Book', 'quantity': 5}
>>> db.get(Todo.name == 'Copies') 
>>> 
```

The `get()` method returns only one matching document. If no document is matched, it returns `None`.

To check whether a document exists in the database or not, we use the `contains()` method.

```repl
>>> db.contains(Todo.name == 'Copies') 
False
>>> db.contains(Todo.name == 'Book')   
True
>>>
```

We can also get the number of documents matching our query using the `count()` method.

```repl
>>> db.insert({"name": "Balloons", "quantity": 500}) 
5
>>> db.count(Todo.name == 'Balloons') 
2
>>> 
```

To get the total number of stored documents in the database, we use the `len()` method.

```repl
>>> len(db)
5
>>>
```

To get all the documents in the database, we can use the `all()` method:

```repl
>>> db.all()
[{'name': 'Book', 'quantity': 5}, {'name': 'Cake', 'quantity': 1}, {'name': 'Candles', 'quantity': 10}, {'name': 'Balloons', 'quantity': 50}, {'name': 'Balloons', 'quantity': 500}]
>>>
```

### How to Update Data in TinyDB

The `update()` method takes the fields that the matching documents will have or a method that will update the documents. It can also take a condition to query an argument optionally.

To update a document matching a query, we can do this:

```repl
>>> db.update({'name': 'Books'}, Todo.name == 'Book')
[1]
>>>
```

Here, we updated the name of the document to `Books` (its name was `Book` above).

Sometimes, we need to update all the documents. In that case, we don't write the query argument.

```repl
>>> db.update({'quantity': 10}) 
[1, 2, 3, 4, 5]
>>> db.all()
[{'name': 'Books', 'quantity': 10}, {'name': 'Cake', 'quantity': 10}, {'name': 'Candles', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}]
>>> 
```

We updated the quantity of all the documents to `10`.

### How to Delete Data in TinyDB

To delete documents from the database, we use the `remove()` method. This method takes an optional condition and an optional list of document ids. If the condition is matched, the document will be deleted.

```repl
>>> db.remove(Todo.name == 'Cake')                              
[2]
>>> db.all()                      
[{'name': 'Books', 'quantity': 10}, {'name': 'Candles', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}, {'name': 'Balloons', 'quantity': 10}]
>>> db.remove(Todo.name == 'Copies')
[]
>>> 
```

To delete documents using the document id, we can write this code:

```repl
>>> db.remove(doc_ids=[4,5]) 
[4, 5]
>>> db.all()
[{'name': 'Books', 'quantity': 10}, {'name': 'Candles', 'quantity': 10}]
>>>
```

To delete everything from the database, we can use the `truncate()` method:

```repl
>>> db.truncate()
>>> db.all()
[]
>>>
```

## Wrapping Up

In this article, we have talked about TinyDB and how to perform CRUD operations on the database. 

This was just a basic tutorial. To learn more about advanced usages of TinyDB, you can go through its [official documentation](https://tinydb.readthedocs.io/en/latest/index.html).

Thanks for reading!

<a class="cta-button" href="https://newsletter.ashutoshkrris.tk" target="_blank">Subscribe to my newsletter</a>


