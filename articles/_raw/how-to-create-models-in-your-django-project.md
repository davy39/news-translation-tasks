---
title: How to Create Models in Your Django Project
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-25T19:47:47.633Z'
originalURL: https://freecodecamp.org/news/how-to-create-models-in-your-django-project
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745610452559/e009644b-bfef-4e43-9f1b-5f2e4deebdfa.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: null
seo_desc: 'If you''re building something with Django, there''s one thing you can''t
  skip: creating models. Models are the heart of any Django app. They define how your
  data is structured, how it''s stored in the database, and how Django can interact
  with it.

  Now, i...'
---

If you're building something with Django, there's one thing you can't skip: creating models. Models are the heart of any Django app. They define how your data is structured, how it's stored in the database, and how Django can interact with it.

Now, if you're new to Django or still wrapping your head around the basics, don’t worry. I’ve been there too. Models might sound a bit intimidating at first, but they’re pretty straightforward once you see how they work.

I’ll walk you through it all – step by step – so by the end of this post, you’ll not only know how to create models, but also how to use them in real projects.

Let’s get into it.

### Here’s what we’ll cover:

1. [What is a Model in Django?](#heading-what-is-a-model-in-django)
    
2. [How to Create Models in Django](#heading-how-to-create-models-in-django)
    
    * [Step 1: Start a Django Project (if you haven’t already)](#heading-step-1-start-a-django-project-if-you-havent-already)
        
    * [Step 2: Define Your Model](#heading-step-2-define-your-model)
        
    * [Step 3: Register the App and Create the Database](#heading-step-3-register-the-app-and-create-the-database)
        
    * [Step 4: Create and Use Objects](#heading-step-4-create-and-use-objects)
        
3. [Extra Model Features That You’ll Use](#heading-extra-model-features-that-youll-use)
    
    * [1\. Default Values](#heading-1-default-values)
        
    * [2\. Auto Timestamps](#heading-2-auto-timestamps)
        
    * [3\. Model Meta Options](#heading-3-model-meta-options)
        
4. [Using Models in Django Admin](#heading-using-models-in-django-admin)
    
5. [FAQs](#heading-faqs)
    
6. [Final Thoughts](#heading-final-thoughts)
    

## What is a Model in Django?

A model in Django is just a Python class that tells Django how you want your data to look. Django takes care of the hard part (talking to the database), so you can focus on describing your data in simple Python code.

Here’s a quick example of a basic model:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

Let me break it down:

* `title` and `author` are just short pieces of text, so I’m using `CharField`.
    
* `published_date` is a date – easy enough, that’s what `DateField` is for.
    
* `price` is a number with decimals, so `DecimalField` does the job.
    

Each line describes one piece of data I want to store for every book. Simple, right?

## How to Create Models in Django

### Step 1: Start a Django Project (if you haven’t already)

If you’re brand new, first you need a Django project:

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp books
```

Now you’ve got a Django app called `books` where you can put your models.

### Step 2: Define Your Model

Inside your app folder (`books`), open `models.py`. That’s where you’ll define your model.

Here’s a slightly more real-world example:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
```

What’s happening here:

* I’ve created two models: `Author` and `Book`.
    
* `Book` has a relationship with `Author` using `ForeignKey`. That means one author can have many books.
    
* I’m using `__str__()` to return a nice name when I look at objects in the Django admin.
    

### Step 3: Register the App and Create the Database

Before Django can use your models, make sure your app is added to the project settings.

Open `mysite/settings.py` and find the `INSTALLED_APPS` list. Add `'books',` to it:

```python
INSTALLED_APPS = [
    # other apps
    'books',
]
```

Now, run migrations to create the database tables for your models:

```bash
python manage.py makemigrations
python manage.py migrate
```

This is how Django turns your Python code into actual database tables. The first command makes a migration file (basically, instructions for the database), and the second applies it.

### Step 4: Create and Use Objects

Now you can use these models in your code. Open the Django shell:

```bash
python manage.py shell
```

Then try this out:

```python
from books.models import Author, Book
from datetime import date

# Create an author
jane = Author.objects.create(name="Jane Austen", birthdate=date(1775, 12, 16))

# Create a book
book = Book.objects.create(
    title="Pride and Prejudice",
    author=jane,
    summary="A novel about manners and marriage in early 19th-century England.",
    isbn="1234567890123",
    published=date(1813, 1, 28),
    price=9.99
)

print(book)
```

Django will save these to your database automatically.

## Extra Model Features That You’ll Use

### 1\. Default Values

You can give a field a default value:

```python
is_published = models.BooleanField(default=False)
```

### 2\. Auto Timestamps

These are super useful when tracking created or updated times:

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

### 3\. Model Meta Options

You can add class Meta to customize things like the default ordering:

```python
class Book(models.Model):
    # fields...

    class Meta:
        ordering = ['published']
```

## Using Models in Django Admin

Django’s built-in admin panel is one of the best parts of the framework. But your models won’t show up there unless you register them.

In `books/admin.py`, add:

```python
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```

Now run:

```bash
python manage.py createsuperuser
```

Then go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), log in, and boom – your models are there, with a full interface.

## FAQs

### **Can I change a model after I’ve made it?**

Yes, but you’ll need to make a new migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

### **What databases work with Django?**

Django works with PostgreSQL, MySQL, SQLite (default), and more. Most people start with SQLite when learning because it's easy and works out of the box.

### **What’s the difference between CharField and TextField?**

Use `CharField` for short text with a max length (like a name or title). Use `TextField` for longer text (like a blog post or summary).

## Final Thoughts

Once you understand models, the rest of Django starts to click into place. Everything – forms, views, templates – eventually connects back to the model. It's how your app stores and works with real data.

The best way to learn is by building something. Start small, maybe a book catalog, a task manager, or a personal blog. Add models one at a time and play with them in the admin.

### Further Resources

* [Official Django Docs – Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
    
* [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)
    
* [Simple Django Tutorial – Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
