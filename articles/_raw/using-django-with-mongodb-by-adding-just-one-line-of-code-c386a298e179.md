---
title: How to use Django with MongoDB by adding just one line of code.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-04T10:40:40.000Z'
originalURL: https://freecodecamp.org/news/using-django-with-mongodb-by-adding-just-one-line-of-code-c386a298e179
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eu9UNWEULdOQb9K1XvDmhg.png
tags:
- name: Django
  slug: django
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Siddy Zen

  To use MongoDB as your backend database in your Django project, just add this one
  line into your settings.py file:

  DATABASES = {   ‘default’: {      ‘ENGINE’: ‘djongo’,      ‘NAME’: ‘your-db-name’,   }}

  It’s that simple!

  Next, login to y...'
---

By Siddy Zen

To use [MongoDB as your backend database in your Django project](http://nesdis.github.io/djongo/), just add **this one line** into your settings.py file:

```
DATABASES = {   ‘default’: {      ‘ENGINE’: ‘djongo’,      ‘NAME’: ‘your-db-name’,   }}
```

It’s that simple!

Next, login to your admin home (localhost:8000/admin/) and start adding “embedded documents” into MongoDB using the Admin GUI:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZkPNUvkWB5VoMn6bEoKxPA.jpeg)

In October, 2017 MongoDB finished up the final step in going public, [pricing its IPO at $24](https://www.mongodb.com/press/mongodb-inc-announces-pricing-of-initial-public-offering) and raising $192 million in the process. The company's finances have been growing steadily:

MongoDB provides open-sourced database software. This is very helpful to early-stage startups looking to launch while being constrained by tight budgets. A review of Google search trends for MongoDB revealed a steady increase in interest.

![Image](https://cdn-media-1.freecodecamp.org/images/1*76GlEAQiLFt4eGsFaiJIIw.jpeg)
_Google Trends — Search Term: MongoDB_

MongoDB has increasingly becoming a popular database software to work with. Databases and Database management systems (DBMS) have existed for more than five decades. They emerged in the early 1960s, and the most popular flavor was the relational database system.

But MongoDB goes around calling itself a “non-relational” database system, and has been making tall claims about its approach to store data. So, what exactly is the BIG deal here?

#### MongoDB vs SQL

Pretty much all relational database systems use the Structured Query Language (SQL) (or a tweaked version of it) to communicate with the data management software. Several university courses are solely dedicated to the understanding and mastery of the SQL syntax.

SQL had become the de-facto language for working with any database (DB) software, proprietary or open source. Then MongoDB came along and decided to show utter disregard to this ancient language of power and introduced query syntax of its own.

> The language is that of Mordor which I will not utter here. In the common tongue, it says, “One ring to rule them all. One ring to find them. One ring to bring them all and in the darkness bind them.”

> -Gandalf (_from_ The lord of the rings_)_

**MongoDB Schemaless vs SQL Schema:** In an SQL database, it’s impossible to add data until you define tables and field types in what’s referred to as a schema. In a MongoDB database, data can be added anywhere, at any time. There’s no need to specify a document design or even a collection up-front.

**MongoDB Documents vs SQL Tables:** SQL databases provide a store of related data tables. Every row is a different record. The design is rigid: you cannot use the same table to store different information or insert a string where a number is expected.

The MongoDB database stores JSON-like field-value pair documents. Similar documents can be stored in a collection, which is analogous to an SQL table. However, you can store any data you like in any document — MongoDB won’t complain. SQL tables create a strict data template, so it’s difficult to make mistakes. MongoDB is more flexible and forgiving, but being able to store any data anywhere can lead to consistency issues.

There is a plethora of online content available that argues that MongoDB is not a superset of SQL. Applications that run on SQL cannot be ported to MongoDB. I am going out on a limb here to claim that, in the context of Django, **MongoDB is a superset of SQL**.

So why does the popular belief, that MongoDB is not a superset of SQL, exist to begin with?

**MongoDB requires Denormalization of data:** In MongoDb there is no JOIN support. This means we will have to denormalize our documents. Denormalized documents leads to faster queries, but updating the document field information in multiple denormalized documents will be significantly slower.

**There are no JOINs**: SQL queries offer a powerful JOIN clause. We can obtain related data in multiple tables using a single SQL statement. In non-relational databases like MongoDB, there are no JOINs like there would be in relational databases. This means you need to perform multiple queries and join the data manually within your code.

**No Transactions:** In SQL databases, two or more updates can be executed in a transaction — an all-or-nothing wrapper that guarantees success or failure. If we execute two updates individually, one could succeed and the other fail — thus leaving our figures out of sync. Placing the same updates within a transaction ensures either both succeed or both fail.

**No foreign key constraints:** Most SQL databases allow you to enforce data integrity rules using foreign key constraints. This ensure all rows have a valid foreign key for code that matches one entry in the join table, and makes sure that a record from the join table is not removed if one or more rows still refer to them.

The schema enforces these rules for the database to follow. It’s impossible for developers or users to add, edit, or remove records, which could result in invalid data or orphan records. The same data integrity options are not available in MongoDB. You can store what you want regardless of any other documents. Ideally, a single document would be the sole source of all information about an item.

#### The need for a Database Model

Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. While objects are a good way to represent data, a problem arises when we want to **make the data persistent.** The amount of data could be huge, and it must be retrieved from the persistent memory quickly and efficiently. This database software must be used to store the objects. A possible database software is a relational, SQL-based database software.

An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into Python objects that are used in Python code. ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL syntax to create, read, update and delete data and schemas in their database. Developers can use the Python programming language with which they are comfortable instead of writing SQL statements or stored procedures.

An example of an ORM framework for Python is SQLAlchemy. The SQLAlchemy ORM presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. It includes a system that transparently synchronizes all changes in state between objects and their related rows. Web frameworks like flask use SQLAlchemy for storing data persistently.

**Django ORM:** Django comes with its own ORM or model for short. The model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table. The Django Model also make it possible to switch between various relational databases such as Oracle SQL, MySQL, or MSSQL.

#### Using Django ORM to add documents into MongoDB

Let’s say you want to create a blogging platform using Django with MongoDB as your backend.

In your Blog `app/models.py` file define the `BlogContent` model:

```
from djongo import modelsfrom djongo.models import forms
```

```
class BlogContent(models.Model):    comment = models.CharField(max_length=100)    author = models.CharField(max_length=100)    class Meta:        abstract = True
```

To access the model using Django Admin, you will need a Form definition for the above model. Define it as shown below:

```
class BlogContentForm(forms.ModelForm):    class Meta:        model = BlogContent        fields = (            'comment', 'author'        )
```

Now “embed” your `BlogContent` inside a `BlogPost` using the `EmbeddedModelField` as below:

```
class BlogPost(models.Model):    h1 = models.CharField(max_length=100)    content = models.EmbeddedModelField(        model_container=BlogContent,        model_form=BlogContentForm    )   
```

That’s it you are set! Fire up Django Admin on localhost:8000/admin/ and this is what you get:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZkPNUvkWB5VoMn6bEoKxPA.jpeg)

Next, assume you want to “extend” the author field to contain more than just the name. You need both a name and email. Simply make the author field an “embedded” field instead of a “char” field:

```
class Author(models.Model):    name = models.CharField(max_length=100)    email = models.CharField(max_length=100)    class Meta:        abstract = Trueclass AuthorForm(forms.ModelForm):    class Meta:        model = Author        fields = (            'name', 'email'        )
```

```
class BlogContent(models.Model):    comment = models.CharField(max_length=100)    author = models.EmbeddedModelField(        model_container=Author,        model_form=AuthorForm    )    class Meta:        abstract = True
```

If a blog post has multiple content from multiple authors, define a new model:

```
class MultipleBlogPosts(models.Model):    h1 = models.CharField(max_length=100)    content = models.ArrayModelField(        model_container=BlogContent,        model_form=BlogContentForm    )
```

Fire up Django Admin with the new changes and you have:

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ckp5M7dit8F_U9A78FrMA.jpeg)

#### Ways to integrate Django and MongoDB.

The Django ORM consists of multiple Abstraction Layers stacked on top of each other.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l41TRyQAGHD5lg0LHXzzag.png)
_The Django ORM stack_

As a web developer, you can take up the challenge of connecting Django to MongoDB in two ways. Take a look at the Django framework stack above to guess the possible entry points.

#### Use a MongoDB compatible model

![Image](https://cdn-media-1.freecodecamp.org/images/1*dGgjMqDl6dzrVHJZdiPbfw.png)
_Switch from Django Models to an ODM_

You can completely avoid using the “batteries included” Django models in your project. Instead, use a third party framework like MongoEngine or Ming in you Django projects.

Choosing a different Model means you miss out on:

* 1500+ core contributors to the project
* [Hourly fixes and ticket resolution](https://dashboard.djangoproject.com)

You’d ramp down on the expertise of existing Django models and ramp up on the new model framework. But perhaps the biggest drawback is that your project can’t use any of Django’s contrib models! Forget about using Admin, Sessions, Users, Auth, and other contrib modules for your project.

Some of these disadvantages are offset by forking a new branch of Django itself. Django-nonrel is an independent branch of Django that adds NoSQL database support to Django. [Django-nonrel](https://github.com/django-nonrel) allows for writing portable Django apps. However, the admin interface does not work fully. There is no active development taking place on the Django-nonrel project.

[Django MongoDB Engine](https://django-mongodb-engine.readthedocs.io/en/latest/) is another MongoDB backend for Django which is a fork off the MongoEngine ODM.

#### Django SQL to MongoDB transpiler — [Djongo](http://nesdis.github.io/djongo/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*QpOq4GaUl_wX4_F6JYkQTA.png)
_Djongo — The SQL to MongoDB transpiler_

Another approach is to translate Django SQL query syntax generated by the Django ORM into pymongo commands. Djongo is one such SQL to MongoDB query compiler. It translates every SQL query string into a mongoDB query document. As a result, all Django models and related modules work as is. With this approach, you gain on:

* **Reuse of Django Models:** Django is a stable framework with continuous development and enhancements. The Django ORM is quite extensive and feature-rich. Defining _a third party_ ORM to work with MongoDB means reproducing the entire Django ORM again. The new ORM needs to constantly align with the Django ORM. Several Django features will never make it into the third party ORM. The idea with Djongo is to **reuse** existing Django ORM features by finally translating SQL queries to MongoDB syntax.
* **SQL syntax will never change** regardless of future additions to Django. By using Djongo, your project is now future proof!

#### Making Django work with MongoDB

**Emulating Schema in MongoDB:** While there is no schema support in MongoDB, this can be emulated. Djongo provides the schema support required in Django by using and defining a combination of MongoDB validator rules and by creating a `__schema__` collection. The `__schema__` collection stores information for supporting features like the SQL AUTOINCREMENT key.

**JOIN support in MongoDB:** In version 3.2, MongoDB introduced the `$lookup` operator. It performs a left outer join to a collection in the same database to filter in documents from the “joined” collection for processing. The `$lookup` stage does an equality match between a field from the input documents with a field from the documents of the “joined” collection.

To each input document, the `$lookup` stage adds a new array field whose elements are the matching documents from the “joined” collection. The `$lookup` stage passes these reshaped documents to the next stage.

Djongo uses the `$lookup` aggregation operator to perform all Django related JOIN queries. This is how it makes admin and other contrib modules work as is.

**Transaction support in MongoDB:** Despite the power of single-document atomic operations, there are cases that require multi-document transactions. When executing a transaction composed of sequential operations, certain issues arise, wherein if one operation fails, the previous operation within the transaction must “rollback” to the previous state — that is, the “all or nothing.”

For situations that require multi-document transactions, Djongo implements the [two-phase commit](https://docs.mongodb.com/manual/tutorial/perform-two-phase-commits/) pattern to provide support for these kinds of multi-document updates. Using two-phase commit ensures that data is consistent and, in case of an error, the state that preceded the transaction is recoverable.

Djongo comes with its own set of compromises, though. So what are the disadvantages of opting to use Djongo for your Django project?

**Performance:** The Django ORM does the heavy lifting of converting complex object manipulations to standard SQL query strings. If your backend database was SQL-based, you could pass this query string directly to it with almost no post-processing. With Djongo, however, the query string will now have to be converted into a MongoDB query document.

This is going to require some CPU cycles. But if extra CPU cycles are really such a problem, you probably shouldn’t be using Python in the first place.

#### Conclusion

I took you through several ways of integrating Django with MongoDB. You will find a multitude of online literature describing the MongoEngine and other variants for doing this.

I focused on [Djongo](http://nesdis.github.io/djongo/) which is a new connector that makes this possible in a different way. It is easy to use and makes the process of migrating from a SQL backend to MongoDB very simple, **by adding just one line of code**.

