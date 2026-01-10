---
title: 'Understanding the basics of Ruby on Rails: SQL Databases and how they work'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-02T16:53:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-basics-of-ruby-on-rails-sql-databases-and-how-they-work-7a628cd42073
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iIiiKaJKg8k9aRU8iWxCxA.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By TK

  After learning about Ruby, the first step we took was to understand how the web
  and the Ruby on Rails request-response cycle work.

  Now it’s time to learn about databases and how they connect with Ruby on Rails.
  Basically, the answer is the Mode...'
---

By TK

After [learning about Ruby](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d), the first step we took was to understand how the [web and the Ruby on Rails request-response cycle](https://medium.com/the-renaissance-developer/ruby-on-rails-http-mvc-and-routes-f02215a46a84) work.

Now it’s time to learn about databases and how they connect with Ruby on Rails. Basically, the answer is the Model: the `M` from `MVC` , as we learned [here](https://medium.com/the-renaissance-developer/ruby-on-rails-http-mvc-and-routes-f02215a46a84).

Before learning web development with Rails, I really recommend learning about [**Ruby first**](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d).

Let’s begin!

### What is a database?

Hmmm… The first thought that comes to my mind is something that stores data.

But this definition is quite imprecise! An array, a hash, a linked list, or any data structure can be something that is able to store data.

When you turn off the computer, you lose all data values that were stored in that array (the same as all data structures). So it’s not a good idea to store all my `precious data`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p1Yw2imC4HhUPaEfssliXw.gif)
_MY PRECIOUS DATA_

We need to solve two problems here:

1. Store data and get it anytime we want.
2. Store data in an organized and structured way, so we can get it easily.

Should I store all the data in a notepad? Just put all the information inside it separated by commas, save the `txt file`, and done. Now I can open it and get all the data I want. We can store data and get it anytime… problem solved!

We solved this problem, but we missed the other. Now all the data is stored and we won’t lose it. But it’s not well-structured in the file. We need the rule to store and get data in an organized and well-structured form.

Let’s think about how can we organize the data in a well-structured way.

**What about organizing all the data in tables?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QzMTJf39jdsi_alIWlGxig.jpeg)

So, here’s we have: the table’s header (_columns name: First Name, Last Name, Address, etc_) containing values that we’ll store. For example, if we want to store the **_string “Mickey”_** _(the value)_, it’ll be stored in the **_“First Name”_** _column_.

* **Table**: let’s say **_People_**
* **Columns**: **_First name_**_, **Last Name**, **Address**, etc_
* **Rows**: in this case, we can say that a row can be a **_person_** with, for example, first name “_Mickey_” and last name “_Mouse,_” address “123 _Fantasy Way,_” etc.
* **Fields**: all data stored in the database.

And now we have a well-structured way to store data**: in a Table!**

### How about get, delete, insert, and update data?

We’ll use SQL language (_I’ll not mention NoSQL world!_) to manipulate the data. Let’s get the basics.

1. **GET:** if we want to get all data (**_person_**) from **People** table, we need to select it from that table.

The (***)** symbol means that it will select all columns from **People** table. If we can get all columns, we can specify which columns we need for this select.

2. **DELETE:** we want to delete all data from our **People** table.

But it’s not common to delete all data from a table. We usually use a condition to delete, like “I want to delete all people under 21 years old.” We will learn how later in this post!

3. **INSERT:** we will insert/store data into the table.

or we can specify into which columns we want to insert data.

4. **UPDATE:** we have stored the data, but we want to update it.

### Using conditions in our queries

Now we can use SQL language to query (select, delete, insert, update) data.

* But what if we want to delete just records with the last name **_Kinoshita_**?
* Or if we want to update a specific person with first name **_Leandro_** and last name **_Kinoshita_**?
* Or just select all data from the people table and sort it by age from younger to older?

Yeah, we use conditions like **where** and **order by,** and operators like **or** and **and**. Let’s see some examples:

* Deleting all records from the people table with last name **_Kinoshita_**.

* Updating all records from the people table with first name **_Leandro_** and last name **_Kinoshita_**.

* Selecting all records from the people table but ordering them by age (in ascending order → ASC).

#### Relationship between tables

We know how to execute queries (with or without conditions). Let’s understand how the tables’ relationships work.

* **One to One (1–1)**: it’s about a relationship between two tables in which one can only belong with the other. **e.g.** A person has one passport and that passport belongs to that specific person. So in this example, we have table People, table Passports and a 1–1 relationship.
* **One to Many (1-n)**: it’s about a relationship between two tables in which a record from one table can reference many records from another. **e.g.** Imagine an e-commerce platform: users, orders, products, payments, etc. A user can have many orders, and each order belongs to that specific user. So in this example, we have table Users, table Orders, and a 1-n relationship.
* **Many to Many (n-n)**: it’s about a relationship between two tables in which a record from one table can reference many records from another. And a record from another can also reference many records from the one. **e.g.** We have again the e-commerce platform: we divide products into categories. A category has many products (category Technology has many products like cell phones, notebooks, etc) and a product can belong to many categories (product Cellphone belongs to the Technology and Electronics Categories). So in this example, we have table Products, table Categories, and an n-n relationship.

### Rails Mode ON

We now understand the meaning of databases, we’ve tried some basic queries, and have talked about the relationship between tables. But how can we use that knowledge in the **_Ruby on Rails and web development World_**?

First of all: **Rails** _is_ **Rails**. The **Database** _is_ **Database**. Is it obvious? But people usually get confused about that.

A _User_ model **can** represent a _Users_ table. But the model isn’t the table.

* In the **_database_**, we have _tables_ and _rows._
* On **_rails_**, we have _models (classes)_ and _objects._

Imagine a blog site. The blog needs an author for each post. So we create an **Authors** table with some columns (first_name, last_name, etc):

In the migration, we add columns `first_name`, `last_name`, `email`, `birthday`, `created_at`, and `updated_at`. (`created_at` and `updated_at` are created by the `t.timestamps` code).

So we create a migration (Ruby code), run the `rake db:migrate` command in the terminal, and it generates a table `**Authors**` with `first_name`, `last_name`, `email`, `birthday`, `created_at`, and `updated_at` columns.

Back to Rails — we can create an `**Author**` model:

So now we have an `Authors` table with some columns and an `Author` model.

#### Using the Rails Console

Open the terminal and type `bundle exec rails c`. Remember, we are in the **RAILS** console, so we have classes, objects, attributes, etc.

### Relationships on Rails

We created an `Authors` table/model. What we need now is a `Posts` table/model. An author has many posts and a post belongs to a specific author. The relationship here is **one to many** (**1-n**). Remember?

So when we create a `Posts` table, we need to store a reference to the post’s author (column **author_id** in the **Posts** table). It’s known as the `Foreign Key`.

And how do we relate the models?

#### author `has_many` posts

#### post belongs_to an author

#### Using the Rails Console

* Quick explanation about `has_many` and `belongs_to`. Both `codes` are methods defined on `ActiveRecord` class. You can see that we create our models inheriting from `ActiveRecord::Base`.

Remember in my [Ruby Foundation](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d) article that we learned about Object Oriented Programming, the Inheritance part? This is why we can use `has_many` and `belongs_to` methods without defining it anywhere on our application. Rails handles it for us.

If you want to understand this concept deeply, clone the [Rails repo](https://github.com/rails/rails) or check out the [Behind the Scenes of the ‘Has Many’ Active Record Association](http://callahan.io/blog/2014/10/08/behind-the-scenes-of-the-has-many-active-record-association/).

### Queries on Rails

We can query using ActiveRecord methods:

* **all**: Get all objects from a specific model.

Behind the scenes, it is executing the `SELECT * FROM posts` query.

* **find**: Using find we can get the object by the _id_ (primary key).

Behind the scenes, it is executing `SELECT * FROM posts WHERE id = 1` query.

* **where**: Get the objects that pass the conditions.

Behind the scenes, it is executing `SELECT * FROM posts WHERE title = 'Database & Rails'`query.

* **order**: Sort all objects based on a column.

Behind the scenes, it is executing `SELECT * FROM posts ORDER BY created_at DESC` query.

### That’s all!

We learned a lot here. I hope you guys appreciate the content and learn more about how the Databases and Rails models work.

This is one more step forward in my journey to learning and mastering Rails and web development. You can see the documentation of my complete journey here on my [**Renaissance Developer publication**](https://medium.com/the-renaissance-developer).

If you want a complete [Ruby](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1) and [Rails](https://onemonth.com/courses/rails?mbsy=lG6tz&mbsy_source=d2442db6-e764-401a-a394-a9c081468830&discount_code=TKRuby1&campaignid=33448) course, learn real-world coding skills and build projects, try [**_One Month Ruby Bootcamp_**](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1) and [**_Rails Bootcamp_**](https://onemonth.com/courses/rails?mbsy=lG6tz&mbsy_source=d2442db6-e764-401a-a394-a9c081468830&discount_code=TKRuby1&campaignid=33448). See you there ☺

Have fun, and keep learning and coding.

My [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺

