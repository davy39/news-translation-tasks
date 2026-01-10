---
title: How to Use Django Signals in Your Projects
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-14T13:39:38.052Z'
originalURL: https://freecodecamp.org/news/how-to-use-django-signals-in-your-projects
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744637958755/939ee783-cb11-4f8c-b509-c68c28092248.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: null
seo_desc: 'Django signals can be a lifesaver if you''re building anything with Django
  and want your code to stay clean and organized.

  They help you connect different parts of your app without everything getting tangled
  together. Think of them like walkie-talkies...'
---

Django signals can be a lifesaver if you're building anything with Django and want your code to stay clean and organized.

They help you connect different parts of your app without everything getting tangled together. Think of them like walkie-talkies — when one part of your code finishes something, it can "signal" another part to take action without needing to know all the details. Pretty handy, right?

I know, it can sound a little abstract at first. But once you get the hang of it, you'll start to see how signals can make your Django projects more flexible and easier to manage — especially when you’re dealing with events like user logins, profile creation, or sending emails after specific actions.

So, if you're curious about how Django signals work, why they matter, and how to use them in your code, you’re in the right place. Let’s break it all down together, step by step.

## What Are Django Signals?

In simple terms, Django signals let certain parts of your app talk to each other when something happens. For example, when a new user signs up, you want to create a user profile automatically.

Instead of adding that logic to the user creation code, you can use a signal that listens for the event and handles it separately.

Django has a built-in system for this — and it’s called the **signals framework**.

Here’s the basic idea:

* One part of your app sends a signal when something happens.
    
* Another part listens for that signal and responds with some action.
    

This helps you separate your logic and avoid cluttering your main codebase with extra tasks.

## Real-Life Examples of When to Use Django Signals

To make it easier to understand, here are some situations where signals shine:

* When a user registers, you want to create a profile automatically.
    
* When someone updates their email, and you want to send a confirmation message.
    
* When a blog post is saved, and you want to update a search index or clear a cache.
    
* When an order is placed, and you want to send a notification to the admin.
    

You could put all this logic inside your views or models, but using signals keeps things clean and modular.

## How Does Django Signals Work?

Here’s the basic setup to use Django signals:

1. Import the signal you want to use (like `post_save` or `pre_delete`).
    
2. Write a function (called a *receiver*) that should run when the signal is triggered.
    
3. Connect your function to the signal using a decorator or `connect()` method.
    

Let me show you a basic example.

### Example: Creating a Profile Automatically When a User Signs Up

```python
# accounts/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

Here’s what’s happening:

* `post_save` is a built-in Django signal. It gets triggered after a model is saved.
    
* The function `create_user_profile` is our *receiver*. It listens for the signal.
    
* It checks if the user was just created (`if created:`) and then makes a profile.
    

To make this work, you also need to import the signal somewhere it gets loaded, like in your app’s `apps.py`:

```python
# accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
```

Without this, Django won’t know to load your signals.

### Built-In Signals You Can Use

Django gives you a few built-in signals that are super useful:

| **Signal** | **When It Triggers** |
| --- | --- |
| `pre_save` | Right before a model is saved |
| `post_save` | Right after a model is saved |
| `pre_delete` | Right before a model is deleted |
| `post_delete` | Right after a model is deleted |
| `m2m_changed` | When a many-to-many field changes |
| `request_finished` | When an HTTP request ends |
| `user_logged_in` | When a user logs in |
| `user_logged_out` | When a user logs out |

You can [find the full list here](https://docs.djangoproject.com/en/stable/ref/signals/).

### Custom Signals (Yes, You Can Make Your Own)

Sometimes, the built-in signals aren’t enough. No problem — Django lets you create your own. Here’s an example:

```python
# myapp/signals.py
from django.dispatch import Signal

order_placed = Signal()

# In your views or logic
order_placed.send(sender=None)
```

Then, write a receiver to listen for `order_placed`, just like with built-in signals. This gives you full control over when and how things trigger.

## When Not to Use Signals

Okay, I love Django signals, but they’re not always the right tool. Here are a few times to skip them:

* If the logic is simple and tightly tied to a view or model, just put it there.
    
* If you need things to happen in a specific order — signals run asynchronously and can make things hard to debug.
    
* If you want everything to be super transparent. Signals can be a little “invisible,” which makes it tough for someone else reading your code to figure out what’s going on.
    

In short: Signals are great for keeping your code modular, but don’t overuse them. Use them when they make things cleaner.

## FAQs

### **Are Django signals synchronous or asynchronous?**

Signals are synchronous by default, meaning they run right away. But you can trigger async tasks (like sending emails) inside them using tools like [Celery](https://docs.celeryq.dev/).

### **Do signals slow down my app?**

Not really, unless the work inside the signal is heavy (like sending emails or writing big files). For that, you should move the task to a background worker.

### **Can signals fail silently?**

Yes, if your receiver has a bug, Django doesn’t always shout about it. You can log errors or wrap your receiver in a try/except block to catch issues.

## Final Thoughts

Django signals are like quiet helpers that keep things running behind the scenes. They’re powerful, flexible, and can clean up your code — as long as you don’t go overboard.

They’re one of those tools that feel a bit magical at first, but once you understand how they work, they just make sense.

So, what’s a part of your Django project that could use a little behind-the-scenes automation with signals?

### Further Resources

If you want to dive deeper into Django signals and best practices, here are a few good places to check out:

* [Official Django Signals Docs](https://docs.djangoproject.com/en/stable/topics/signals/)
    
* [Real Python’s Guide to Django Signals](https://realpython.com/django-signals/)
    
* [Understanding Django Signals (YouTube - Simple Is Better Than Complex)](https://www.youtube.com/watch?v=rTz5sGZ7A1Y)
    
* [Celery for Background Tasks](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) (for heavy signal tasks)
