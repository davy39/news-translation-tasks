---
title: How to Use a Foreign Key to Create Many-to-One Relationships in Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-06T20:33:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-one-to-many-relationship-in-django
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Add-a-subheading--5-.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Sampurna Chapagain

  In Django, there are three main types of relationships: one-to-one, many-to-one,
  and many-to-many.

  In this article, I will explain the many-to-one relationship in Django. If you are
  a beginner with some knowledge about Django pr...'
---

By Sampurna Chapagain

In Django, there are three main types of relationships: one-to-one, many-to-one, and many-to-many.

In this article, I will explain the many-to-one relationship in Django. If you are a beginner with some knowledge about Django project setup or even have some decent experience in Django, you can follow along with this article.

Many-to-one relationship are sometimes referred to as one-to-many relationships. As you'll see below, these are related terms.

## What is a Many-to-One Relationship?

A `Many-to-one` relationship is a type of relationship where multiple records in one table are associated to the single record in another table.

Let's assume we have two tables in a database: `Department` and `Employee`. The relationship between `Department` and `Employee` is a `one-to-many` relationship. A `department` can have many `employees` and each `employee` belongs to one `department`.

And, the relationship between the `employees` and `departments` is a `many-to-one` relationship.

This can be illustrated with the diagram below:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Add-a-little-bit-of-body-text.png)
_Diagram to illustrate many-to-one relationship_

For example, an `Account` department can have many `employees` (one-to-many) and those `employees` all belong to the `account` department (many-to-one).

## How to Create Models for Many-to-one Relationships

For this tutorial, the app will have two models: `Department` and `Employee`. 

So let's start adding code for the models.

```python
from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=70)
    address=models.CharField(max_length=90)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

The`Department` model contains only one field, `name`.

The `Employee` model contains `name` and `address` fields, and also a `ForeignKey` field (`department`) which references the `Department` model. That's the reason it's passing `Department` as the first argument. 

The second argument, `on_delete`, specifies the behavior to adopt when the reference object is deleted, which is `Department` in this case.  The `models.CASCADE` option means that if a `Department` object is deleted, all related `Employee` objects will also be deleted.

### What is a Foreign Key in a Django Model?

The foreign key is used to connect two tables and establishes the `many-to-one` relationship. You can define a `foreign key` in a Django model using the `models.ForeignKey` field. And this `ForeignKey` field takes at least two arguments:

```python
department = models.ForeignKey(Department, on_delete=models.CASCADE)
```

We already discussed these two arguments in the above section.

And you can also pass other arguments like `related_name` with a value which lets you access `foreign keys` defined in your Django models backwards. 

### Database Migrations

Now, you can make the migrations using the `makemigrations` command.

```python
manage.py makemigrations
```

And then you can make changes to the database using the `migrate` command.

```python
manage.py migrate
```

## How to Interact with Models

Now, let's play around with shell to understand the primary concepts of `many-to-one` relationships.

First, you need to run the `shell` command:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-26-26.png)

Then import models in the `shell`. Here, the name of the app is `company`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-23-46.png)

And now, let's create few departments.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-23-57.png)

Now, you can make a `Department.objects.all()` query to return a `QuerySet` that contains all `Department` objects in the database.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-24-18.png)

In the next step, let's create a few employees, `emp1`, `emp2`, and `emp3`:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-24-28.png)

Here, you are passing the instance of the `department` object for the `department` field.

If you want to retrieve all `employees` for a specific `department`, which is `programming` in this example, you can use the following query: 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-24-38.png)

You can also use any `employee` object to retrieve record from `department`. Here, it's using `emp1` object.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-03-18-40-45.png)

## Conclusion

Many-to-one relationships are widely used in Django applications.

They help to create relationships between models and make it easier to perform database queries.

I hope you found this article useful.

You can find me on [Twitter](https://twitter.com/saam_codes) for daily content regarding Web development.

Enjoy Coding in Python!




