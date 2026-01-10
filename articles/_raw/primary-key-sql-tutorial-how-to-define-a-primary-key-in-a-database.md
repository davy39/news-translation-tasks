---
title: Primary Key SQL Tutorial – How to Define a Primary Key in a Database
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-10T08:20:23.000Z'
originalURL: https://freecodecamp.org/news/primary-key-sql-tutorial-how-to-define-a-primary-key-in-a-database
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a60740569d1a4ca253e.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Neil Kakkar

  Every great story starts with an identity crisis. Luke, the great Jedi Master, begins
  unsure - "Who am I?" - and how could I be anyone important? It takes Yoda, the one
  with the Force, to teach him how to harness his powers.

  Today, let...'
---

By Neil Kakkar

Every great story starts with an identity crisis. Luke, the great Jedi Master, begins unsure - _"Who am I?"_ - and how could I be anyone important? It takes Yoda, the one with the Force, to teach him how to harness his powers.

Today, let me be your Yoda.

We'll start with how to choose a Primary Key, fight an identity crisis, and then finish with code samples for creating a Primary Key in a database.

## How to Choose a Primary Key

You may think Luke is the only one with an identity crisis, but that's not true. When creating a database, everything is in an identity crisis. And that's exactly why we need primary keys: they resolve the crisis. They tell us how to find everyone.

Imagine you're the government, and you want to identify each one of your citizens digitally. So, you create this database with everything about them:

```
First Name
Last Name
Passport Number
```

You choose the passport Number as the Primary Key - the identity for everyone. You figure that's all you need since the passport has the address and everything else. You know passport numbers are unique, so you feel good and implement this system.

Then, a few years later, you find out an ugly truth: the entire country is facing an identity crisis.

Whenever someone's passport expires, they get a new one. Their identity changes. Other systems keep using the old passport numbers, so they now point to ghost people.

> Uniqueness isn't enough. The value must not change throughout the row's lifetime.

And then, you find there are some people who don't even have passports. You can't enter them into your system, since Primary Keys can't be `NULL`.  How can you identify someone with a `NULL` key?

> Every row must have an identifier. NULLs not allowed.

The next iteration means finding an identifier that doesn't change over time, and one that everyone has. In India, this is turning out to be the Adhaar Card. In the USA, the Social Security Number.

If you're creating a database, make those your primary keys.

Sometimes, you don't have any such key. Consider a country that doesn't have a Social Security Number yet, and they want to create a digital record of every citizen. They could create a new SSN, or they could just leverage the power of databases, and use a surrogate key.

A surrogate key has no real world equivalent. It's just a number inside a database. So, you have this table in the new country:

```
userID
First Name
Last Name
Passport Number
```

Passport Numbers are unique. Whenever you want to get the identifier for a user, you can get it via the Passport Number.

The userID never changes. The Passport Number can change - but it's always unique, so you always get the right user. The userID is a _surrogate_ for a non-existing Social Security Number in this country.

> Fun fact: The Passport Number here is also a Candidate Key. It could've been the Primary Key, if it never changed. This is a business logic distinction.

The main takeaway is this: **Whenever you're choosing a Primary Key, think of an identity crisis**. Is it possible that someone might change their identifier in the future? Can we get into a state with multiple people having the same identifier?

I use people as an example, because it makes identity clearer - we know every person is supposed to have an identity. Transfer this thinking to your databases. Everything has an identity, which is exactly why you need Primary Keys.

> Note: Sometimes, it's possible, and desirable to use multiple columns together as the Primary Key. This is a Composite Key.

Now let's try defining Primary Keys with real code examples. There's two things to do here: first, you'll identify the Primary Key. Then, you'll learn the syntax for defining it in a database.

## A real world example

Let's say you run a shipping startup, much like Flexport. You have packages that need to get from one place to another, and ships that transport them. Further, you have customers who are ordering these packages.

You figure you'll need one table for the customers, one for the packages, and one for transportation, showing which package is where right now.

Think through what columns you'll need, and what should be the Primary Key. If you were an engineer at Flexport, this is an actual question you would have to figure out. Nothing is given, everything is discovered in the real world.

Given this information, I'd design these tables like so:

```
Customers: first_name, last_name, email, address (for deliveries to their location)
Packages: weight, content
Transportation: <package_primary_key>, Port, time
```

We're missing the primary keys. Think about them before reading further.

For the package, I'll choose a _surrogate_ PackageID. I could have tried to list all the attributes of the package: weight, volume, density, age. They would uniquely identify the package, but this is very hard to do in practice. People don't care about this, they just care about the package getting from one place to another. 

So, it makes sense to create a random number and use that as the ID. This is exactly why you see FedEx, UPS, and every delivery service use barcodes and IDs. These are surrogate keys generated to track packages.

For the customer, I'll choose a _surrogate_ CustomerID. Here, again, I had an option to choose, say, the Social Security Number of my customers. But, customers don't want to share this with me just so I can ship them something. Thus, we generate a key internally, don't tell our customers about this key, and continue calling them CustomerNo. 345681.

> Fun Story: I know a few companies where they exposed this CustomerNo, and the customers insisted they get No. 1. It was pretty hilarious - the engineers actually had to change their front-end code to: `if (cust == 345681) print(1);`

For Transportation, I'll choose a _composite_ PackageID+Port+time. This is a bit more interesting. I could have created a _surrogate_ here as well, and it would work just as well. 

But, here lies the magic of indexing. The Primary Keys get an index automatically, which means searching is a lot more efficient over Primary Keys. 

When you're searching through this database, most queries will be of the form "where is this package?". In other words, given this PackageID, tell me the Port and Time it is at right now. I would need an extra index over PackageID if I don't have it as part of my Primary Key.

Does this sound good? Final step, let's define these 3 tables in SQL. The syntax varies slightly with the database you're using.

## Defining Primary Keys in MySQL

```sql
CREATE TABLE customers
( customerID  INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  last_name   VARCHAR(30) NOT NULL,
  first_name  VARCHAR(25) NOT NULL,
  email		  VARCHAR(50) NOT NULL,
  address     VARCHAR(300)
);
```

```sql
CREATE TABLE packages
( packageID  INT(15) NOT NULL AUTO_INCREMENT,
  weight     DECIMAL (10, 2) NOT NULL,
  content    VARCHAR(50),
  CONSTRAINT packages_pk PRIMARY KEY (packageID) # An alternative way to above,
  # when you want to name the constraint as well.
);
```

```sql
CREATE TABLE transportation
( package 	INT(15) NOT NULL,
  port  	INT(15) NOT NULL,
  time	 	DATE NOT NULL,
  
  PRIMARY KEY (package, port, time),
  FOREIGN KEY package
  	REFERENCES packages(packageID)
	ON DELETE RESTRICT    # It's good practice to define what should happen on deletion. In this case, I don't want things to get deleted.

);
```

## Defining Primary Keys in PostgreSQL

```sql
CREATE TABLE customers
( customerID  SERIAL NOT NULL PRIMARY KEY, # In PostgreSQL SERIAL is same as AUTO_INCREMENT - it adds 1 to every new row.
  last_name   VARCHAR(30) NOT NULL,
  first_name  VARCHAR(25) NOT NULL,
  address     TEXT,
  email		  VARCHAR(50) NOT NULL
);
```

```sql
CREATE TABLE packages
( packageID  SERIAL NOT NULL,
  weight     NUMERIC NOT NULL,
  content    TEXT,
  CONSTRAINT packages_pk PRIMARY KEY (packageID) # In PostgreSQL, this alternative way works too.
);
```

```sql
CREATE TABLE transportation
( package 	INTEGER NOT NULL,
  port  	INT(15) NOT NULL,
  time	 	DATE NOT NULL,
  
  PRIMARY KEY (package, port, time),
  
  FOREIGN KEY package
  	REFERENCES packages(packageID)
	ON DELETE RESTRICT    # It's good practice to define what should happen on deletion. In this case, I don't want things to get deleted.

);
```

It's not very different, is it? Once you get the basics down, you can apply it to almost any database with just a quick look at the documentation. The key is knowing what to look for!

Good luck, young padawan.

Enjoyed this? You might also like [Things I Learned From a Senior Software Engineer](https://neilkakkar.com/things-I-learnt-from-a-senior-dev.html)

