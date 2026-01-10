---
title: How to Use a Foreign Key in Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-22T14:05:27.872Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-foreign-key-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745330646960/e2fc7f1d-73f9-4e25-b870-e0928833e7a5.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: 'When you''re building something in Django – whether it''s a blog, a to-do
  app, or even something way more complex – at some point, you''ll want to connect
  different pieces of data.

  That’s where ForeignKey comes in. It helps link one model to another, li...'
---

When you're building something in Django – whether it's a blog, a to-do app, or even something way more complex – at some point, you'll want to connect different pieces of data.

That’s where `ForeignKey` comes in. It helps link one model to another, like tying a comment to a post, or an order to a customer.

It’s one of those things in Django that can seem confusing at first, but once it clicks, you’ll wonder how you ever built apps without it.

So let’s break it all down. I’ll walk you through everything from what a ForeignKey is, to how to use it in your Django project.

## Here’s what we’ll cover:

* [What is a Foreign Key in Django?](#heading-what-is-a-foreign-key-in-django)
    
* [Why Use a ForeignKey Instead of Storing IDs Manually?](#heading-why-use-a-foreignkey-instead-of-storing-ids-manually)
    
* [Real-World Example: Blog Posts and Comments](#heading-real-world-example-blog-posts-and-comments)
    
* [What is on\_delete and Why Does It Matter?](#heading-what-is-ondelete-and-why-does-it-matter)
    
* [How to Access Related Objects in Django](#heading-how-to-access-related-objects-in-django)
    
* [How to Create Foreign Key Relationships in Django Admin](#heading-how-to-create-foreign-key-relationships-in-django-admin)
    
    * [What Happens in the Database?](#heading-what-happens-in-the-database)
        
* [How to Query with ForeignKey](#heading-how-to-query-with-foreignkey)
    
    * [Get all comments for a post with id=1:](#heading-get-all-comments-for-a-post-with-id1)
        
    * [Get all posts that have at least one comment by a specific user:](#heading-get-all-posts-that-have-at-least-one-comment-by-a-specific-user)
        
* [FAQs](#heading-faqs)
    
    * [Can a ForeignKey be optional?](#heading-can-a-foreignkey-be-optional)
        
    * [Can a ForeignKey point to the same model (self)?](#heading-can-a-foreignkey-point-to-the-same-model-self)
        
    * [Can a model have more than one ForeignKey?](#heading-can-a-model-have-more-than-one-foreignkey)
        
* [Final Thoughts](#heading-final-thoughts)
    
    * [Further Resources](#heading-further-resources)
        

## What is a Foreign Key in Django?

In the simplest terms, a Foreign Key in Django creates a many-to-one relationship between two models. This means many rows in one table can be related to a single row in another.

For example:

* One blog post can have **many comments**
    
* One customer can have **many orders**
    
* One author can write **many books**
    

If you're coming from a spreadsheet background, think of it like linking two sheets using a shared column. In Django, you do this in your model definitions.

## Why Use a ForeignKey Instead of Storing IDs Manually?

You might be wondering, “Why not just store the ID of the related object in a plain integer field?”

Well, you could – but you'd lose a ton of power. Without a ForeignKey:

* You don’t get automatic validation that the related object exists.
    
* You can't follow relationships easily in queries (for example, `post.comments.all()` wouldn’t be possible).
    
* The Django admin can’t provide dropdowns or inline forms for related data.
    
* You lose out on helpful features like `on_delete` behaviour and related object naming.
    

ForeignKey fields automate and enforce these relationships, making your code cleaner, more secure, and easier to maintain.

## Real-World Example: Blog Posts and Comments

Let’s say you’re building a blog. You’ll probably have a `Post` model and a `Comment` model. Each comment needs to be linked to a specific post.

Here’s how that looks in code:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'
```

Let me explain each part of that:

* `models.ForeignKey(Post, on_delete=models.CASCADE)`: This line creates the connection. It means each comment is linked to one post. The `on_delete=models.CASCADE` part tells Django to delete all related comments if a post is deleted.
    
* `__str__` methods just make it easier to read things in the admin or shell.
    

## What is `on_delete` and Why Does It Matter?

When you create a ForeignKey in Django, you have to include an `on_delete` argument. This controls what happens to the child rows (like comments) if the parent row (like a blog post) is deleted.

Here are the common options:

* `models.CASCADE`: Delete the child rows, too (like deleting all comments when a post is deleted).
    
* `models.PROTECT`: Prevent deletion if there are related objects.
    
* `models.SET_NULL`: Set the ForeignKey to `NULL` instead of deleting.
    
* `models.SET_DEFAULT`: Set a default value.
    
* `models.DO_NOTHING`: Do nothing (not recommended unless you really know what you're doing).
    

I usually go with `CASCADE` for simple apps, but it's worth thinking through depending on the situation.

## How to Access Related Objects in Django

Once you’ve set up the ForeignKey, Django gives you a few nice tools to work with related data.

For example, let’s say you have a post object:

```python
post = Post.objects.get(id=1)
```

You can get all comments for that post like this:

```python
comments = post.comment_set.all()
```

The `comment_set` is automatically created by Django, and you can customize the name with `related_name`:

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
```

Now you can do:

```python
post.comments.all()
```

Much cleaner, right?

## How to Create Foreign Key Relationships in Django Admin

The Django admin handles ForeignKeys well. If you’ve got both `Post` and `Comment` models registered in `admin.py`, you’ll get a dropdown in the comment form to select the post it belongs to.

You can also make inline forms, so you can add comments while editing a post. Here’s a quick example:

```python
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
```

Now when you're editing a post, you can add or edit comments right there on the same page.

### What Happens in the Database?

Django uses a relational database (like PostgreSQL, MySQL, or SQLite), and ForeignKey creates a column in the database table that holds the ID of the related object.

If you run `python manage.py makemigrations` and then `python manage.py migrate`, Django will create the actual database tables with the proper relationships behind the scenes.

## How to Query with ForeignKey

You can also filter or search based on ForeignKey relationships:

### Get all comments for a post with id=1:

```python
Comment.objects.filter(post_id=1)
```

Or, using the post object:

```python
post = Post.objects.get(id=1)
comments = Comment.objects.filter(post=post)
```

### Get all posts that have at least one comment by a specific user:

```python
Post.objects.filter(comments__author='John')
```

That `comments__author` part is thanks to the `related_name='comments'` I added earlier.

## FAQs

### **Can a ForeignKey be optional?**

Yes, just add `null=True, blank=True` like this:

```python
post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
```

You might want this if the related object isn't always required. For example, a `Comment` might *optionally* belong to a `Post`, or a `Task` might optionally have a related `Project`. It’s useful when building drafts, soft deletes, or handling legacy data.

### **Can a ForeignKey point to the same model (self)?**

Absolutely. That’s called a self-referential ForeignKey, often used for things like threaded comments or categories.

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
```

### **Can a model have more than one ForeignKey?**

Totally. For example, an Order model could have one ForeignKey to a Customer, and another to a ShippingAddress.

## Final Thoughts

If you’re building anything in Django that deals with more than one model, understanding ForeignKey is essential. It makes your app more structured, easier to query, and way more powerful.

At first, it might feel like a lot, but once you build one or two relationships and see it all working in the admin and your views, it clicks.

And if something’s still unclear, that’s normal. I had to build a few mini-projects before it started to feel natural.

### Further Resources

* Django Docs on [ForeignKey](https://docs.djangoproject.com/en/stable/ref/models/fields/#foreignkey)
    
* [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)
    
* [Writing Models in Django](https://docs.djangoproject.com/en/stable/topics/db/models/)
    
* [Django Admin Docs](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
