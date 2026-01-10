---
title: How to Use PostgreSQL in Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-22T13:43:52.647Z'
originalURL: https://freecodecamp.org/news/how-to-use-postgresql-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745329406033/4d3cb010-d612-4ca8-8039-2d922e8b0337.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: PostgreSQL
  slug: postgresql
seo_title: null
seo_desc: 'If you’re building a Django project and wondering which database to use,
  PostgreSQL is a great choice. It’s reliable, fast, packed with powerful features,
  and works beautifully with Django.

  I’ve used it across multiple projects – from small web apps ...'
---

If you’re building a Django project and wondering which database to use, PostgreSQL is a great choice. It’s reliable, fast, packed with powerful features, and works beautifully with Django.

I’ve used it across multiple projects – from small web apps to large-scale platforms – and it never disappoints.

In this post, I’ll walk you through how to connect PostgreSQL with Django step-by-step.

Let’s get started.

### What we’ll cover:

1. [Why Use PostgreSQL with Django?](#heading-why-use-postgresql-with-django)
    
2. [What You'll Need](#heading-what-youll-need)
    
3. [How to Use PostgreSQL in Django](#heading-how-to-use-postgresql-in-django)
    
    * [Step 1: Install PostgreSQL](#heading-step-1-install-postgresql)
        
    * [Step 2: Install the PostgreSQL Adapter for Python](#heading-step-2-install-the-postgresql-adapter-for-python)
        
    * [Step 3: Create a Django Project (If You Haven’t Yet)](#heading-step-3-create-a-django-project-if-you-havent-yet)
        
    * [Step 4: Create a PostgreSQL Database](#heading-step-4-create-a-postgresql-database)
        
    * [Step 5: Update Django Settings to Use PostgreSQL](#heading-step-5-update-django-settings-to-use-postgresql)
        
    * [Step 6: Run Migrations](#heading-step-6-run-migrations)
        
    * [Step 7: Test the Connection](#heading-step-7-test-the-connection)
        
4. [Common Issues (and Fixes)](#heading-common-issues-and-fixes)
    
5. [Optional: Use dj-database-url for Better Settings](#heading-optional-use-dj-database-url-for-better-settings)
    
6. [Frequently Asked Questions](#heading-frequently-asked-questions)
    
    * [Is PostgreSQL better than SQLite for Django?](#heading-is-postgresql-better-than-sqlite-for-django)
        
    * [Do I need to install PostgreSQL on my production server?](#heading-do-i-need-to-install-postgresql-on-my-production-server)
        
    * [Is psycopg2-binary safe to use in production?](#heading-is-psycopg2-binary-safe-to-use-in-production)
        
    * [Can I switch from SQLite to PostgreSQL mid-project?](#heading-can-i-switch-from-sqlite-to-postgresql-mid-project)
        
7. [Wrapping Up](#heading-wrapping-up)
    
8. [Further Resources](#heading-further-resources)
    

## Why Use PostgreSQL with Django?

PostgreSQL is a popular, open-source relational database that’s known for its performance, flexibility, and powerful features like:

* Advanced data types (JSON, arrays, and so on)
    
* Full-text search
    
* Support for complex queries
    
* Data integrity and reliability
    

Django officially recommends PostgreSQL as the most feature-complete database backend it supports. If you're planning to build a serious web application, PostgreSQL is usually the best database to pair with Django.

## What You’ll Need

Before we begin, make sure you have the following:

* Python installed (3.7 or higher is best)
    
* Django installed (I’ll be using version 4.x)
    
* PostgreSQL installed and running
    
* `psycopg2` or `psycopg2-binary` (This is the adapter that lets Django talk to PostgreSQL)
    

## How to Use PostgreSQL in Django

Here is how to get started:

### Step 1: Install PostgreSQL

If you haven’t installed PostgreSQL yet, you can grab it from the [official PostgreSQL website](https://www.postgresql.org/download/). It works on Windows, macOS, and Linux.

Make sure you remember the username, password, and database name when you set it up – you’ll need those later.

### Step 2: Install the PostgreSQL Adapter for Python

Django needs a little help to connect with PostgreSQL. That’s where `psycopg2` comes in.

You can install it using pip:

```bash
pip install psycopg2-binary
```

Tip: The `-binary` version is easier to install and works for most people. If you run into issues later, you can switch to `psycopg2` (non-binary).

### Step 3: Create a Django Project (If You Haven’t Yet)

If you haven’t created a project yet, start with:

```bash
django-admin startproject myproject
cd myproject
```

This will give you the basic project structure.

### Step 4: Create a PostgreSQL Database

Now, open your PostgreSQL client (like `psql` or pgAdmin), and create a new database:

```sql
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```

This sets up a database and user with the right permissions. Replace `mydatabase`, `myuser`, and `mypassword` with whatever values you prefer.

### Step 5: Update Django Settings to Use PostgreSQL

Now it’s time to tell Django to use your new PostgreSQL database.

Open `myproject/settings.py` and look for the `DATABASES` setting. Replace the default `sqlite3` section with this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

This tells Django to:

* Use PostgreSQL (`django.db.backends.postgresql`)
    
* Connect to a local database called `mydatabase`
    
* Use the user and password you set up earlier
    

### Step 6: Run Migrations

Now that everything’s connected, let’s create the database tables Django needs:

```bash
python manage.py migrate
```

If everything’s working, you’ll see Django creating tables in PostgreSQL. No errors? You’re good to go!

### Step 7: Test the Connection

Let’s test it all by creating a superuser (admin account):

```bash
python manage.py createsuperuser
```

Follow the prompts, then run:

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/admin`. Log in with your superuser account. You’ll be in the Django admin dashboard – and yes, all of this is backed by PostgreSQL now!

## Common Issues (and Fixes)

Here are a few things that might trip you up:

* **Error:** `psycopg2.errors.UndefinedTable`: This usually means you forgot to run `migrate`.
    
* **Can’t connect to database:** Double-check your database name, user, and password. Make sure PostgreSQL is running.
    
* **Role doesn’t exist:** You might’ve forgotten to create the user in PostgreSQL, or you used the wrong name in `settings.py`.
    

## Optional: Use `dj-database-url` for Better Settings

If you’re planning to deploy your app later (especially on services like Heroku), managing your database settings through a URL is cleaner.

Install the helper package:

```bash
pip install dj-database-url
```

Then in your `settings.py`:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgres://myuser:mypassword@localhost:5432/mydatabase')
}
```

This lets you control your database config from an environment variable, which is more secure and flexible.

## Frequently Asked Questions

### **Is PostgreSQL better than SQLite for Django?**

For learning or small projects, SQLite is fine. But for serious apps with lots of users or advanced queries, PostgreSQL is much better.

### **Do I need to install PostgreSQL on my production server?**

Yes – unless you’re using a hosted PostgreSQL solution like [Amazon RDS](https://aws.amazon.com/rds/postgresql/), [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql), or [Supabase](https://supabase.com/).

### **Is psycopg2-binary safe to use in production?**

Yes, for most cases. But some recommend switching to the non-binary version (`psycopg2`) in production for better control.

### **Can I switch from SQLite to PostgreSQL mid-project?**

Yes, but you’ll need to migrate your data. Tools like [Django’s `dumpdata` and `loaddata`](https://docs.djangoproject.com/en/stable/ref/django-admin/#dumpdata) can help with that.

## Wrapping Up

Using PostgreSQL in Django is a great step forward when you want to build real, production-ready apps.

The setup is pretty straightforward once you know the steps, and the performance gains are worth it.

Come say hey on [X.com/\_udemezue](http://X.com/_udemezue) and check out my [blog](https://Tchelete.com) while you're at it!

### Further Resources

If you want to dive deeper, here are a few links I recommend:

* [Django Database Settings Docs](https://docs.djangoproject.com/en/stable/ref/settings/#databases)
    
* [PostgreSQL Official Documentation](https://www.postgresql.org/docs/)
    
* [Using PostgreSQL with Django (Real Python)](https://realpython.com/django-setup/#databases)
