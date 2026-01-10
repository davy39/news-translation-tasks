---
title: How to Define Relationships Between Django Models
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2023-03-20T16:05:18.000Z'
originalURL: https://freecodecamp.org/news/django-model-relationships
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Blog-Banner-560x315-px-1.png
tags:
- name: database
  slug: database
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: 'Django is a free and open-source web framework written in Python. It helps
  with rapid web development and provides out-of-the-box web security.

  Websites must be able to store and retrieve data from databases. Django makes provisions
  for this. By defa...'
---

[Django](https://www.djangoproject.com/) is a free and open-source web framework written in Python. It helps with rapid web development and provides out-of-the-box web security.

Websites must be able to store and retrieve data from databases. Django makes provisions for this. By default, Django operates a Relational Database Management System.

> A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key. [(Source: Oracle Cloud)](https://www.oracle.com/ng/database/what-is-a-relational-database/#:~:text=The%20software%20used%20to%20store,storage%2C%20access%2C%20and%20performance.)

A major advantage of a Relational Database Management System is being able to define the types of relationships between the different data held in the different tables of your database.

This tutorial shows you how you can define the relationships between your Django [models](https://docs.djangoproject.com/en/3.2/topics/db/models/). To get the most out of this tutorial, you should have a basic understanding of the Django web framework, especially Django file structure and [models](https://docs.djangoproject.com/en/3.2/topics/db/models/).

## **Different Types of Model Relationships in Django**

Each [model](https://docs.djangoproject.com/en/3.2/topics/db/models/) in a [Django](https://www.djangoproject.com/) application represents a database table. This means that you can define the kind of relationship you want between the different models in your Django application.

Django supports three main types of relationships between its models. They're as follows:

### **One-to-One Relationship**

A **one-to-one** relationship means that a record in one table relates to a single record in another table.

An instance of this is if you have a Django model that defines users. This model can then have a one-to-one relationship with another Django model, which defines users' profiles. In this scenario, a user can have only one profile and a profile can be associated with only one user.

The following diagram illustrates a **one-to-one** relationship:

![diagram indicating one-to-one relationship](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-drawing--5--2.png align="left")

*A diagram showing a one-to-one relationship between a User model and a Profile model.*

Django provides you with `OneToOneField`**,** which helps define a one-to-one relationship between two different models.

The following code shows you how you can define a **one-to-one** relationship in Django. Go to your `<app>/models.py` and write the following code:

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    language = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return str(self.email)
```

Let's see what's going on in the above code:

1. Line one imports the sub-module `models` from the `django.db` module.
    
2. Line three defines a Django model named `User`.
    
3. Line four defines a `name` property within the `User` model, and the keyword `CharField` is how you define text with a limited number of characters.
    
4. Line six and seven is a special method within the `User` model and returns a string representation of the `User` model that includes the `name` property.
    
5. Line nine defines a Django model named `Profile`.
    
6. Line ten defines a **one-to-one** relationship between the `Profile` model and the `User` model using the `OneToOneField` keyword.
    
7. Lines eleven and twelve define the properties `language` and `email` within the `Profile` model.
    
8. Line twelve and thirteen is a special method within the `Profile` model and returns a string representation of the `Profile` model that includes the `email` property.
    

### **Many-to-one Relationship**

In a **many-to-one** relationship, a record in one table relates to multiple records in another table. Some resources refer to a **many-to-one** relationship as a *one-to-many* relationship. These two mean the same thing.

An example of a one to many relationship is the relationship between an author and their published books. While an author can have more than one book to their name, it's less common to find a book with more than one author. You can see this kind of relationship as a parent-child relationship.

The following diagram illustrates a **one-to-many** relationship:

![diagram indicating one-to-many relationship](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-drawing-1.png align="left")

*A diagram showing a one-to-many relationship between an Author model and a Book model.*

Django provides you with `ForeignKey`, which helps define a **many-to-one** relationship between two different models.

The following code shows you how you can define a **many-to-one** relationship in Django. Go to your `<app>/models.py` and write the following code:

```python
from django.db import models

class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        blank=False
    )

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

This code is similar to the code in the first example. However, in line ten here, the `ForeignKey` keyword is what you use to define a many-to-one relationship between two Django models. In this case, the current model will have a **many-to-one** relationship with the `Author` model.

### **Many-to-Many Relationship**

In a **many-to-many** relationship, multiple records in one table relate to many records in another table. For instance, you may have a collection model in your application, in which one collection has many books within it. In the same vein, a book may belong to several collections.

The following diagram illustrates a **many-to-many** relationship:

![diagram indicating many-to-many relationship](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-drawing--3-.png align="left")

*A diagram showing a many-to-many relationship between a Collection model and a Book model.*

Django provides you with a [`ManyToManyField`](https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ManyToManyField) which helps define a **many-to-many** relationship between two different models.

The following code shows you how you can define a many-to-many relationship in Django. Go to your `<app>/models.py` and enter the write the following code:

```python
from django.db import models

class Collection(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
        return str(self.name)
    
class Book(models.Model):
  collection = models.ManyToManyField(Collection)
  
  title = models.CharField(max_length=100)
  
  def __str__(self):
        return str(self.title)
```

In this code sample, the `ManyToManyField` keyword in line 10 is what you use to define a **many-to-many** relationship between the `Collection` and `Book` models.

## **Conclusion**

Although this tutorial explains the basics of Django model relationships to help you get a basic understanding, real-life projects can get more complicated.

The complexity of your Django model relationships depends on your application's complexity. So before you build your applications, it's important to plan out your database relationships. Doing this saves you lots of time and effort compared to finding problems and backtracking later.
