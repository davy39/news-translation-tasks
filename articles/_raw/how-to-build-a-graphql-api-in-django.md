---
title: How to Build a GraphQL API in Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-16T13:22:37.122Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-graphql-api-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744809748866/9a626cc9-4e67-4d63-bdde-1834180db645.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
- name: GraphQL
  slug: graphql
seo_title: null
seo_desc: 'If you''re building an app with Django and thinking about using GraphQL,
  you''re not alone.

  REST has been the go-to for years, but GraphQL is quickly becoming a favourite option
  for developers who want more flexibility and less back-and-forth between f...'
---

If you're building an app with Django and thinking about using GraphQL, you're not alone.

REST has been the go-to for years, but GraphQL is quickly becoming a favourite option for developers who want more flexibility and less back-and-forth between frontend and backend.

I’ve spent a lot of time working with Django and playing around with different ways to make APIS smoother, and I get why people are switching to GraphQL.

You ask for exactly the data you need, and you get just that. No extra fluff, no multiple requests to stitch together data — it’s like ordering off a menu and getting exactly what you wanted, every single time.

So, if you’re curious about how to build a GraphQL API using Django, I’ve got you covered.

I’ll walk you through what GraphQL is, why it might be a better fit than REST in some cases, and how you can get started from scratch — even if you’re not a GraphQL expert (yet).

### Here’s what we’ll cover:

1. [What Is GraphQL, and Why Does It Matter?](#heading-what-is-graphql-and-why-does-it-matter)
    
2. [What You’ll Need Before You Start](#heading-what-youll-need-before-you-start)
    
3. [How to Build a GraphQL API in Django)](#heading-how-to-build-a-graphql-api-in-django)
    
4. [How to Add Mutations (Also Known As Writing Data)](#heading-how-to-add-mutations-also-known-as-writing-data)
    
5. [Code Walkthrough: Creating a Post via Mutation in GraphQL)](#heading-code-walkthrough-creating-a-post-via-mutation-in-graphql)
    
6. [How a Client Would Use This](#heading-how-a-client-would-use-this)
    
7. [Pros and Cons of Using GraphQL in Django](#heading-pros-and-cons-of-using-graphql-in-django)
    
8. [FAQs](#heading-faqs)
    
9. [What's Next?](#heading-whats-next)
    
10. [Final Thoughts](#heading-final-thoughts)
    

## What Is GraphQL, and Why Does It Matter?

GraphQL is a query language for APIs — and more importantly, it’s a runtime for fulfilling those queries with your data.

It was developed by Facebook in 2012 and made public in 2015. Since then, it's been used by companies like GitHub, Shopify, Twitter, and Pinterest.

Unlike REST, where you often have to make multiple requests to get all the data you need, GraphQL lets you fetch all your data in a single request.

This is a big deal, especially for mobile apps or slow networks where fewer requests mean better performance.

Let’s say you want a user’s name, profile picture, and their 3 most recent blog posts. With REST, you might need to hit 2-3 different endpoints. With GraphQL? One request, done.

It’s also great for frontend devs because they can shape the data they get back without waiting for backend devs to create new endpoints.

## What You’ll Need Before You Start

Before jumping in, here’s what you should already have:

* Basic knowledge of Django (models, views, and so on)
    
* Python installed (3.8+ is best)
    
* A Django project set up
    
* pip or pipenv for package management
    

If you're starting fresh, you can spin up a new Django project with:

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

## How to Build a GraphQL API in Django

Let’s get into it.

### 1\. Install Graphene-Django

Graphene is the most popular library for using GraphQL with Python. For Django specifically, there's a package called `graphene-django`.

You can install it like this:

```bash
pip install graphene-django
```

Then, add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'graphene_django',
]
```

### 2\. Add a Simple Model

Here’s a quick model to work with. In `myapp/models.py`:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Then run your migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3\. Create a Schema

In `myapp/schema.py`, start with:

```python
import graphene
from graphene_django.types import DjangoObjectType
from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.all()

schema = graphene.Schema(query=Query)
```

Then, in your Django project settings, add:

```python
GRAPHENE = {
    "SCHEMA": "myapp.schema.schema"
}
```

And finally, in your `urls.py`:

```python
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```

Now, visit `http://localhost:8000/graphql` and try this query:

```graphql
{
  allPosts {
    title
    content
    published
  }
}
```

Boom. You just queried your database using GraphQL.

Here is what your GraphQL playground should look like.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744454293412/8820e7dd-ff86-4c7d-9c8c-ec21dc43b09b.png align="center")

## How to Add Mutations (Also Known As Writing Data)

GraphQL isn’t just for reading data. You can also create, update, and delete. Here’s how to add a mutation for creating a post:

In `myapp/schema.py`:

```python
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
```

Now, in the GraphiQL playground, you can run:

```graphql
mutation {
  createPost(title: "My First Post", content: "Hello GraphQL!") {
    post {
      id
      title
    }
  }
}
```

Pretty clean, right?

## Code Walkthrough: Creating a Post via Mutation in GraphQL

Let me walk you through the code, explain what it does, and how GraphQL makes it work.

### Step 1: The `CreatePost` Mutation Class

```python
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)
```

Here’s what’s going on in this part:

* `graphene.Mutation`: This defines a custom **mutation**, which in GraphQL is how we modify server-side data (similar to POST, PUT, and DELETE in REST).
    
* `class Arguments`: Think of this as the "input" part of the mutation. We're requiring a `title` and `content`, both as strings. These are what the client must provide when calling the mutation.
    
* `post = graphene.Field(PostType)`: This defines the return type of the mutation. In this case, once a post is created, we return it using a custom GraphQL type called `PostType`.
    
* `mutate(self, info, title, content)`: This method is called when the mutation is executed. Inside it:
    
    * We create a new `Post` model instance.
        
    * We save it to the database.
        
    * We return the mutation result as an `CreatePost` object with the new post attached.
        
* This keeps the logic tight, readable, and testable – a great example of clean API design.
    

### Step 2: Wiring the Mutation into the Schema

```python
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
```

This is where we **register** our mutation. In GraphQL, all operations (queries and mutations) must be part of the schema. By adding `create_post` to the `Mutation` class, we expose it to the GraphQL endpoint.

### Step 3: The Final Schema

```python
schema = graphene.Schema(query=Query, mutation=Mutation)
```

In this code,

* We’re creating a new `graphene.Schema`.
    
* We pass in a `Query` class (assumed to be defined elsewhere for read operations) and our `Mutation` class for write operations.
    

This is the GraphQL equivalent of wiring up Django's [`urls.py`](http://urls.py) – it's what gets exposed to clients when they hit your `/graphql/` endpoint.

## How a Client Would Use This

A client (frontend or API testing tool like Insomnia/Postman) would send a mutation like this:

```python
mutation {
  createPost(title: "GraphQL is Awesome", content: "Let's build APIs with it!") {
    post {
      id
      title
      content
    }
  }
}
```

And get a response like:

```python
{
  "data": {
    "createPost": {
      "post": {
        "id": "1",
        "title": "GraphQL is Awesome",
        "content": "Let's build APIs with it!"
      }
    }
  }
}
```

## Bonus: Why This Is Awesome for Developers

* **Frontend teams** can now build forms and instantly see the structure of the response.
    
* **Backend devs** define what’s allowed and handle only necessary logic.
    
* **No more over-fetching or under-fetching data** — GraphQL gives you just what you ask for.
    
* Easy to test, debug, and scale.
    

## Make Sure You Have the Following in Place

* Ensure you have `graphene-django` installed.
    
* Add `'graphene_django'` to your `INSTALLED_APPS`.
    
* Wire up the schema in your Django project’s [`urls.py`](http://urls.py).
    

```python
from django.urls import path
from graphene_django.views import GraphQLView
from myapp.schema import schema

urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
```

## Pros and Cons of Using GraphQL in Django

### Pros:

* Flexible queries
    
* Great for frontend devs
    
* Fewer API calls
    
* Strongly typed schema
    
* Better performance on slower networks
    

### Cons:

* Slightly steeper learning curve
    
* More setup than REST
    
* Can be overkill for simple APIS
    

## FAQs

### Is GraphQL better than REST?

It depends. GraphQL gives you more control and flexibility, but REST is easier to cache and simpler to set up for small projects.

### Is Graphene the only way to use GraphQL with Django?

Nope. You can also use Ariadne or Strawberry. But Graphene is the most mature and widely used right now.

### Does GraphQL work well with Django REST Framework?

They can live side-by-side. If you already have a REST API and want to add GraphQL, you don’t need to throw anything away.

## What’s Next?

Once you’ve got the basics down, you can:

* Add authentication with JWT or sessions
    
* Use Relay if you need pagination and filtering
    
* Connect your GraphQL API to React, Vue, or any frontend
    

## Final Thoughts

If you’ve been using Django for a while and want to give your API a little more power and flexibility, GraphQL is 100% worth checking out.

### Further Resources

* [Graphene-Django Docs](https://docs.graphene-python.org/projects/django/en/latest/)
    
* [Official GraphQL Docs](https://graphql.org/learn/)
    
* [Ariadne – A schema-first GraphQL library for Python](https://ariadnegraphql.org/)
    
* [GraphQL vs REST: Key Differences](https://www.apollographql.com/blog/graphql/basics/graphql-vs-rest/)
