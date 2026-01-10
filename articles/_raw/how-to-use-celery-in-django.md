---
title: How to Use Celery in Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-18T16:37:24.801Z'
originalURL: https://freecodecamp.org/news/how-to-use-celery-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744994231247/63228755-1929-4474-9930-15f8ff1a5631.png
tags:
- name: Python
  slug: python
- name: celery
  slug: celery
- name: Django
  slug: django
seo_title: null
seo_desc: 'You’ve probably noticed that some tasks in your Django app seem to take
  a long time. For example, maybe sending confirmation emails, resizing images, or
  processing large data files slows things down.

  The good news? You don’t have to sit around waitin...'
---

You’ve probably noticed that some tasks in your Django app seem to take a long time. For example, maybe sending confirmation emails, resizing images, or processing large data files slows things down.

The good news? You don’t have to sit around waiting. You can hand those tasks off to something else and let your app keep doing its thing. That "something else" is Celery.

Celery lets you run time-consuming tasks in the background while your app stays fast. And if you're using Django, it's actually not that hard to plug it in – once you understand how the pieces work together.

In this guide, I’ll walk you through what Celery is, why it’s useful, and exactly how to set it up with Django step by step.

## Table Of Contents

1. [What Is Celery and Why Should You Use It in Django?](#heading-what-is-celery-and-why-should-you-use-it-in-django)
    
2. [How Celery Works (The Simple Version)](#heading-how-celery-works-the-simple-version)
    
3. [How to Use Celery in Django](#how-to-use-celery-in-django)
    
    * [1\. Install the right packages](#heading-1-install-the-right-packages)
        
    * [2\. Create a](#heading-2-create-a-celerypy-file-in-your-project-folder) [celery.py](http://celery.py) [file in your project folder](#heading-2-create-a-celerypy-file-in-your-project-folder)
        
    * [3\. Add Celery to](#heading-3-add-celery-to-initpy) [**init**.py](http://init.py)
        
    * [4\. Set the broker URL in your settings](#heading-4-set-the-broker-url-in-your-settings)
        
    * [5\. Write your first task](#heading-5-write-your-first-task)
        
    * [6\. Call the task from your views](#heading-6-call-the-task-from-your-views)
        
    * [7\. Run the Celery worker](#heading-7-run-the-celery-worker)
        
4. [Optional: Using Django Admin to Monitor Tasks](#heading-optional-using-django-admin-to-monitor-tasks)
    
5. [FAQ](#heading-faq)
    
    * [What happens if Redis goes down?](#heading-what-happens-if-redis-goes-down)
        
    * [Can I retry failed tasks?](#heading-can-i-retry-failed-tasks)
        
    * [Is Celery the only option?](#heading-is-celery-the-only-option)
        
6. [Wrapping It Up](#heading-wrapping-it-up)
    
7. [Further Reading and Resources](#heading-further-reading-and-resources)
    

## What Is Celery and Why Should You Use It in Django?

Imagine you’re running an online shop. Someone places an order. You want to:

* Save the order to the database
    
* Send them an invoice by email
    
* Notify your warehouse
    
* Maybe even start printing a shipping label
    

If your app tries to do all this at once, your user is going to be stuck staring at a loading screen. Instead, what if you only saved the order right away – and passed the rest to Celery to handle in the background?

That’s exactly what Celery does.

It’s a task queue — which just means it runs things later, so your main app doesn’t have to wait. It’s especially helpful for:

* Sending emails
    
* Data imports/exports
    
* Running machine learning models
    
* Scraping data
    
* Generating reports
    

And yeah, it works really well with Django.

## How Celery Works (The Simple Version)

Celery is made up of a few parts:

1. **Task producer (your Django app)** – This is where you call a task.
    
2. **Broker (usually Redis)** – This is the middleman. It takes the task and holds it until a worker can grab it.
    
3. **Worker** – This is Celery’s background process that grabs tasks from the broker and runs them.
    

Here’s the flow:

```plaintext
Django app → Redis → Celery Worker → Done ✅
```

Now let’s actually set this up.

## How to Use Celery in Django

### 1\. Install the right packages

You’ll need `celery` and a message broker. Redis is a popular choice.

```bash
pip install celery redis
```

Also make sure you have Redis running. You can install it locally via Homebrew (`brew install redis`) or use a Docker container.

If you’re using Docker:

```bash
docker run -p 6379:6379 redis
```

### 2\. Create a `celery.py` file in your project folder

Let’s say your Django project is called `myproject`. Inside that same folder (where `settings.py` is), create a file called `celery.py`.

```python
# myproject/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

Here’s what’s happening:

* `os.environ...` sets up Django’s settings.
    
* `Celery("myproject")` creates a new Celery app with your project name.
    
* `app.config_from_object(...)` tells Celery to read config from Django’s settings file.
    
* `autodiscover_tasks()` tells Celery to find tasks in your Django apps automatically.
    

### 3\. Add Celery to `__init__.py`

Still in your `myproject/` folder, open `__init__.py` and add:

```python
from .celery import app as celery_app

__all__ = ("celery_app",)
```

This makes sure Celery starts with Django.

### 4\. Set the broker URL in your settings

Open `settings.py` and add:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
```

This tells Celery to use Redis as the broker.

### 5\. Write your first task

Go to one of your Django apps (say you’ve got an app called `shop`), and create a file called `tasks.py`.

```python
# shop/tasks.py
from celery import shared_task

@shared_task
def send_invoice_email(order_id):
    # Imagine this sends an email
    print(f"Sending invoice email for order {order_id}")
```

The `@shared_task` decorator tells Celery this is a background task.

### 6\. Call the task from your views

Here’s how you’d use it in a Django view:

```python
# shop/views.py

from .tasks import send_invoice_email
from django.shortcuts import render

def place_order(request):
    # pretend this saves an order
    order_id = 1234  # this would come from your model

    # run the task in the background
    send_invoice_email.delay(order_id)

    return render(request, "order_complete.html")
```

Notice the `.delay()` – this is what sends the task to Celery.

### 7\. Run the Celery worker

Now open a terminal and start the worker:

```bash
celery -A myproject worker --loglevel=info
```

You should see the worker start and wait for tasks. When you place an order, it’ll print something like:

```css
Sending invoice email for order 1234
```

## Optional: Using Django Admin to Monitor Tasks

If you want to monitor task status in the admin, you can use [django-celery-results](https://github.com/celery/django-celery-results).

```bash
pip install django-celery-results
```

Then update your `settings.py`:

```python
INSTALLED_APPS += ["django_celery_results"]

CELERY_RESULT_BACKEND = "django-db"
```

Run migrations:

```bash
python manage.py migrate
```

Now Celery will save task results in your database, and you can see them in Django admin.

## FAQ

### **What happens if Redis goes down?**

Your tasks won’t be sent or picked up. But once Redis comes back, things should resume.

### **Can I retry failed tasks?**

Yes! Celery supports retries. You can set how many times a task should retry and how often. Example:

```python
@shared_task(bind=True, max_retries=3)

def risky_task(self):
    try:
        # Do something risky
        pass
    except Exception as e:
        raise self.retry(exc=e, countdown=60)
```

### **Is Celery the only option?**

No. There’s also Django Q, Dramatiq, and Huey. But Celery is the most mature and has the biggest community.

## Wrapping It Up

Using Celery in Django doesn’t just speed things up – it also helps improve the experience for your users.

Offloading heavy or slow tasks makes your app feel snappier and more reliable.

Once you get the basics down, you’ll find yourself using it for all kinds of things.

### Further Reading and Resources

* [Celery Documentation](https://docs.celeryq.dev/en/stable/)
    
* [Redis Quickstart](https://redis.io/docs/latest/develop/get-started/)
    
* [django-celery-results](https://github.com/celery/django-celery-results)
    
* [Asynchronous Tasks in Django (Real Python)](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
    
* [Celery Monitoring with Flower](https://flower.readthedocs.io/en/latest/)
