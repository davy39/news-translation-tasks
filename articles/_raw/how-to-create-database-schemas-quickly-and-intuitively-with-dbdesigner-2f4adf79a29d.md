---
title: How to create database schemas quickly and intuitively with DBDesigner
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2018-08-06T16:30:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-database-schemas-quickly-and-intuitively-with-dbdesigner-2f4adf79a29d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6Y5Szhl_pNIkjhu0Uo3rEw.png
tags:
- name: coding
  slug: coding
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: One of the most important parts of developing a project is having a clear
  picture in mind of the end goal. We need to know the target audience for the project,
  as well as the features it will include. This means that we need to be as informed
  as poss...
---

One of the most important parts of developing a project is having a clear picture in mind of the end goal. We need to know the target audience for the project, as well as the features it will include. This means that we need to be as informed as possible about the business logic, and then implement all the features as needed.

[DBDesigner](http://dbdesigner.net/) is a great tool when it comes to creating database schemas for your application. It allows you to create any number of tables you want (as far as I am concerned). You can add any data type attribute you want to any table you have created. You can also have certain attributes serve as foreign keys. This way, when you set up primary keys and foreign keys respectively, you can see relations between tables of the database that you are trying to create.

You can use your email and create many projects, and get back to them whenever you want. You can also invite your colleagues via email and have them collaborate with you in the preparation of that schema.

When you have an initial version of your database schema, you can then export it as an SQL script for the following database technologies: PostgreSQL, SQLite, MySQL, MSSql, and Oracle.

### **Demonstration**

Let’s start by creating a new database schema to demonstrate how it works in practice.

We can either start with a new blank template, or use one from the many pre-existing templates that are available.

We will be demonstrating an empty template here, just so that we can see some of the features that are included. Otherwise, you may not notice them using existing templates.

First we need to create a new schema. Our example uses the “Generic” database type, and we will call it “library”.

So, we need to go to *Schema* &g\_t;\_ New and then we will see a new window will pop up:

![Image](https://cdn-media-1.freecodecamp.org/images/dKGQLARUrZNYsvQzfxx65r0lfDNqFe2fTsiu align="left")

This is the image that we should see after that:

![Image](https://cdn-media-1.freecodecamp.org/images/3evdVmxCEoqv6npUjobnLH1v-1RJA7qTrIS5 align="left")

Then we need to add new tables into our schema, which we can do by right clicking anywhere on the grid, and selecting the “Table” option:

![Image](https://cdn-media-1.freecodecamp.org/images/JdF6W8rIb5S1G6s0mItsmb0rRpBhRJaZIGIS align="left")

Now we need to add fields to the table. All we have to do is go to *Add field*, after which a new window will show up. In it you can choose the type, and also set up a few constraints to your new table column:

![Image](https://cdn-media-1.freecodecamp.org/images/SiFU1HH-YjlF8zl2LL3Bo-Lwo-LIqAzImh76 align="left")

Here we can see how it looks like after we have added a few columns:

![Image](https://cdn-media-1.freecodecamp.org/images/8JJt351B9ZkdPyeWdRDBgf3rcykpCz1c8h9R align="left")

Then we can add relations between tables. We will take the example of creating a *many-to-many* relation between two tables: *Authors* and *Books.* For this, we initially need to create a new table called *AuthorBooks,* in which we add foreign keys that reference the *Authors* table and the *Books* table, respectively:

![Image](https://cdn-media-1.freecodecamp.org/images/9QbhYFaIoE9xEMDnINK5-MsqMlMP85NCEOAa align="left")

Here we have the connection with the *Books* table:

![Image](https://cdn-media-1.freecodecamp.org/images/RUzIA5zXMBg8rQufWIb43FIkfiBp8E0HR0H- align="left")

After we are done with that, we should see a schema similar to the following:

![Image](https://cdn-media-1.freecodecamp.org/images/kx7-qxvknuSAt85PbjOU37BP-XiHDSEe9vev align="left")

A really great feature of *dbdesigner* is the flexibility it gives you to move your tables around the grid as you wish:

![Image](https://cdn-media-1.freecodecamp.org/images/EstgpMYYjO7hwLR7ug5pwniVvUV54uif2KQn align="left")

We can also share the schema with up to five collaborators in the free version. We simply need to go to \_Schema &gt; Sha\_re and a new window will pop up, like the following:

![Image](https://cdn-media-1.freecodecamp.org/images/yMNJVmGA6UCGGRUGNFMlAKqxdtG97Vhcb9r1 align="left")

We can save this schema as an image by going to: \_Export &gt; Im\_age.

We can also generate the corresponding SQL script the following way:

![Image](https://cdn-media-1.freecodecamp.org/images/pQz9K1zslWpL3MFBUwCqqmEpmOvU7MVMPEHZ align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/lcpubCJYZNuusWp1YfBjkmUxu7dyMYviPN62 align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/ftc3d8sSxITbljXkA7z4gjJ2Tv-UcuhKkEb9 align="left")

We can also import our own SQL into the schema and see it represented graphically:

![Image](https://cdn-media-1.freecodecamp.org/images/imO4ID01-K3ANkILlUQ-hSNHvIq9R9JYJueT align="left")

### Conclusion

I heard about this tool when I was doing a pair-programming with a colleague, and have found it really helpful. I hope you benefit from it as well.

[DBDesigner](https://www.dbdesigner.net/designer/schema/187386) has other features, and I would definitely recommend that you give them a try.
