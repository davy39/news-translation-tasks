---
title: How to Get the User Model in Django – A Simple Guide With Examples
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-30T15:19:33.742Z'
originalURL: https://freecodecamp.org/news/how-to-get-user-model-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746026362647/7b47e9e7-6baf-409a-8654-0ad1eb528e31.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: null
seo_desc: 'When I’m working with Django, one of the first things I often need to do
  is work with users – like getting the logged-in user, creating a new one, or extending
  the default user model to add more information.

  Now, Django has a built-in User model, but...'
---

When I’m working with Django, one of the first things I often need to do is work with users – like getting the logged-in user, creating a new one, or extending the default user model to add more information.

Now, Django has a built-in `User` model, but sometimes you might want a custom one. That's where things can get a little confusing if you're just starting.

The good news? Getting the user model in Django is very simple once you understand how Django is set up.

Today, I’ll walk you through exactly how to get the user model in Django, explain why it matters, show you real code you can use, and answer a few common questions people usually have around this topic.

Let's jump right into it.

## Table of Contents

* [Why Getting the User Model Correctly Matters](#heading-why-getting-the-user-model-correctly-matters)
    
* [How to Get the User Model in Django](#heading-how-to-get-the-user-model-in-django)
    
* [Full Example: Using the User Model](#heading-full-example-using-the-user-model)
    
* [When to Use settings.AUTH\_USER\_MODEL](#heading-when-to-use-settingsauthusermodel)
    
* [Quick Summary](#heading-quick-summary)
    
* [Common Mistakes to Avoid](#heading-common-mistakes-to-avoid)
    
* [FAQs](#heading-faqs)
    
    * [1\. Can I access request.user it directly?](#heading-1-can-i-access-requestuser-it-directly)
        
    * [2\. What happens if I call get\_user\_model() Multiple times?](#heading-2-what-happens-if-i-call-getusermodel-multiple-times)
        
    * [3\. How do I know if I’m using a custom user model?](#heading-3-how-do-i-know-if-im-using-a-custom-user-model)
        
    * [4\. When should I create a custom user model?](#heading-4-when-should-i-create-a-custom-user-model)
        
* [Further Resources](#heading-further-resources)
    
* [Conclusion](#heading-conclusion)
    

## Why Getting the User Model Correctly Matters

Before anything else, it’s important to know why this even matters.

Django projects depend heavily on user information – not just for logins, but for permissions, profiles, admin management, and much more.

If you get the user model the wrong way, you can easily run into problems later, especially if you customize your user model.

Django even warns you about this in its [official documentation](https://docs.djangoproject.com/en/stable/topics/auth/customizing/). If you don't use the right way to access the user model, your project could break when you change or extend it.

That’s why it’s super important to always get the user model the *recommended* way, which I’ll show you next.

## How to Get the User Model in Django

Alright, here’s the simplest way to get the user model in Django:

```python
from django.contrib.auth import get_user_model

User = get_user_model()
```

**What’s happening here?**

* `get_user_model()` is a built-in Django function.
    
* It returns the correct User model – whether you're using the default one or a custom one you created.
    

If you’re wondering why not just import `from django.contrib.auth.models import User`, the reason is this: if you ever swap out the default User model for a custom one, directly importing like that will break your code.

By using `get_user_model()`, you stay safe and future-proof your project.

## Full Example: Using the User Model

Let’s look at a full working example, not just a little snippet.

Imagine you want to create a new user inside a Django view:

```python
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_user_view(request):
    User = get_user_model()
    user = User.objects.create_user(username='newuser', password='securepassword123')
    return HttpResponse(f"Created user: {user.username}")
```

In this example:

* First, I get the user model with `get_user_model()`.
    
* Then, I use Django’s built-in `create_user` method to create a user safely.
    
* Finally, I send back a simple HTTP response showing the created username.
    

Notice how clean and flexible it is – no matter what user model you're using under the hood.

## When to Use `settings.AUTH_USER_MODEL`

Another thing you’ll often see in Django projects is something like this:

```python
from django.conf import settings

settings.AUTH_USER_MODEL
```

This doesn’t **get** the user model. Instead, it gives you the **string** path to the user model, like `"auth.User"` (for default) or `"myapp.MyCustomUser"` if you customized it.

You usually use `settings.AUTH_USER_MODEL` inside your **models.py** when you want to link to the User model in a ForeignKey, OneToOneField, or ManyToManyField.

For example:

```python
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
```

Here, the `Profile` model is tied to the correct user model. Again, this keeps your project flexible and future-proof.

## Quick Summary

| Situation | What to Use |
| --- | --- |
| Getting the actual User model in Python code (views, forms, admin, and so on) | `get_user_model()` |
| Referring to the User model in database relationships (ForeignKey, OneToOneField, and so on) | `settings.AUTH_USER_MODEL` |

Remember this table – it saves a lot of headaches later!

## Common Mistakes to Avoid

* **Directly importing** `User`: Never just do `from django.contrib.auth.models import User` unless you are 100% sure you're sticking with the default model forever (not recommended).
    
* **Hardcoding relationships**: If you write something like `ForeignKey('auth.User')` instead of using `settings.AUTH_USER_MODEL`, it will break if you ever switch to a custom user model.
    
* **Not creating custom user models early**: If you think you might ever need a custom user model (like adding phone numbers, extra profile fields), set it up early. Switching later is painful once you have a database full of users.
    

## FAQs

### 1\. Can I access `request.user` directly?

Yes! Inside views, `request.user` gives you the current logged-in user object. Behind the scenes, Django is using the correct user model, whether it’s custom or default.

### 2\. What happens if I call `get_user_model()` multiple times?

No problem at all. Django caches it internally, so it’s efficient. Feel free to call it wherever you need it.

### 3\. How do I know if I’m using a custom user model?

Check your Django settings file (`settings.py`) and look for `AUTH_USER_MODEL`. If it’s set (like `'myapp.MyCustomUser'`, you are using a custom model. If it’s not there, Django is using the default.

### 4\. When should I create a custom user model?

If you even *think* you’ll need fields like phone number, date of birth, profile pictures, and so on, it’s better to set up a custom model early.

Here’s a great guide from Django’s official docs on [customizing user models](https://docs.djangoproject.com/en/stable/topics/auth/customizing/).

## Conclusion

Working with users in Django doesn’t have to be tricky. Once you know to use `get_user_model()` when you need the model and `settings.AUTH_USER_MODEL` for database relationships, your code stays clean, safe, and ready for whatever changes come your way.

Now that you know how to get the user model in Django, what’s one thing you'd love to customize about your users in your project? Shoot me a message on [X](http://x.com/_udemezue/).

If you want me to show you how to **build** a custom user model from scratch, let me know – it’s not hard once you know the steps.

### Further Resources

* [Official Django documentation: Using a custom user model](https://docs.djangoproject.com/en/stable/topics/auth/customizing/)
    
* [Simple explanation on AbstractBaseUser vs AbstractUser](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
    
* [StackOverflow: Best practices for Django user models](https://stackoverflow.com/questions/29725217/django-custom-user-model-best-practice)
