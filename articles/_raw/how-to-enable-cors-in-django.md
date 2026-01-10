---
title: How to Enable CORS in Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-28T15:51:42.800Z'
originalURL: https://freecodecamp.org/news/how-to-enable-cors-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745855234567/f09d3338-c824-4cd8-a26f-93bb485f925a.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: CORS
  slug: cors
seo_title: null
seo_desc: 'If you''ve ever tried to connect your frontend app to your Django backend
  and suddenly hit an error that looks something like "has been blocked by CORS policy",
  you''re not alone. It’s frustrating, especially when your code seems fine.

  So what’s going ...'
---

If you've ever tried to connect your frontend app to your Django backend and suddenly hit an error that looks something like **"has been blocked by CORS policy"**, you're not alone. It’s frustrating, especially when your code seems fine.

So what’s going on?

This is where **CORS** (Cross-Origin Resource Sharing) comes in. It's a browser security feature that blocks web pages from making requests to a different domain than the one that served the web page.

It’s there to protect users, but if it’s not configured correctly, it can stop your app from working the way you want.

Let’s fix that.

In this article, I’ll walk you through everything you need to know to enable CORS in Django without headaches.

### Here’s what we’ll cover:

* [What is CORS and Why Should You Care?](#heading-what-is-cors-and-why-should-you-care)
    
* [How to Enable CORS in Django](#heading-how-to-enable-cors-in-django)
    
    * [1\. Install django-cors-headers](#heading-1-install-django-cors-headers)
        
    * [2\. Add It to INSTALLED\_APPS](#heading-2-add-it-to-installedapps)
        
    * [3\. Add Middleware](#heading-3-add-middleware)
        
    * [4\. Set the Allowed Origins](#heading-4-set-the-allowed-origins)
        
* [Optional Settings You Might Need](#heading-optional-settings-you-might-need)
    
    * [Allow All Origins (Not Recommended for Production)](#heading-allow-all-origins-not-recommended-for-production)
        
    * [Allow Credentials (Cookies, Auth)](#heading-allow-credentials-cookies-auth)
        
    * [Allow Specific Headers](#heading-allow-specific-headers)
        
* [Example: Full Settings File Snippet](#heading-example-full-settings-file-snippet)
    
* [Common Errors (And How to Fix Them)](#heading-common-errors-and-how-to-fix-them)
    
    * [1\. CORS Not Working At All?](#heading-1-cors-not-working-at-all)
        
    * [2\. Preflight Request Fails (OPTIONS method)](#heading-2-preflight-request-fails-options-method)
        
    * [3\. Using Django Rest Framework?](#heading-3-using-django-rest-framework)
        
* [FAQs](#heading-faqs)
    
    * [Can I allow multiple frontend URLs?](#heading-can-i-allow-multiple-frontend-urls)
        
    * [Does CORS affect local development only?](#heading-does-cors-affect-local-development-only)
        
    * [Is it secure to allow all origins?](#heading-is-it-secure-to-allow-all-origins)
        
    * [Do I need to change anything on the frontend?](#heading-do-i-need-to-change-anything-on-the-frontend)
        
* [Further Resources](#heading-further-resources)
    
* [Final Thoughts](#heading-final-thoughts)
    

## What is CORS and Why Should You Care?

Before you start changing settings, it’s important to understand what CORS is.

Imagine you have a frontend built with React running on `http://localhost:3000` and a Django API running on `http://localhost:8000`.

When the frontend tries to talk to the backend, your browser sees that they’re not the same origin (they have different ports), and it blocks the request.

That’s CORS doing its job. It assumes you might be trying to do something unsafe – like stealing cookies or user data – so it steps in.

Now, as a developer, if you trust the frontend and you own both ends, then it’s safe to let those requests through. You just need to tell Django it’s okay.

## How to Enable CORS in Django

You’re going to need a third-party package called `django-cors-headers`. It’s widely used and actively maintained. Here’s how to set it up:

### 1\. Install `django-cors-headers`

Run this in your terminal:

```bash
pip install django-cors-headers
```

This adds the package to your environment so Django can use it.

### 2\. Add It to `INSTALLED_APPS`

Open your `settings.py` file and find the `INSTALLED_APPS` section. Add this line:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]
```

This registers the app with Django.

### 3\. Add Middleware

Now scroll down to the `MIDDLEWARE` section in `settings.py`. Add this **at the top of the list**:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

**Why at the top?** Because middleware in Django runs in order. If you don’t place it at the top, the CORS headers might not be added correctly, and your browser will still block your requests.

### 4\. Set the Allowed Origins

This is where you tell Django which origins are allowed to talk to your backend.

Still in `settings.py`, add:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

Replace `localhost:3000` with whatever domain or port your frontend is using. If you're using HTTPS or deploying, make sure to include the correct URL, like `https://yourfrontend.com`.

And that’s it! You’re now allowing your frontend to access your backend.

## Optional Settings You Might Need

Depending on your project, you might run into other issues. Here are some extra settings you might find useful:

### Allow All Origins (Not Recommended for Production)

If you’re just testing and want to allow everything (be careful with this), you can use:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

Again, don’t use this in production unless you understand the risks. It can open up your API to abuse.

### Allow Credentials (Cookies, Auth)

If your frontend is sending authentication credentials like cookies or tokens, you also need this:

```python
CORS_ALLOW_CREDENTIALS = True
```

And make sure you **don’t** use `CORS_ALLOW_ALL_ORIGINS` with this setting – it won’t work due to security rules. Stick to `CORS_ALLOWED_ORIGINS`.

### Allow Specific Headers

By default, common headers are allowed, but if you’re sending custom ones (like `X-Auth-Token`), you can add:

```python
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-auth-token",
    ...
]
```

## Example: Full Settings File Snippet

Here’s a mini version of what your `settings.py` might look like after setup:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True
```

You can tweak this based on your needs, but that’s the basic structure.

## Common Errors (And How to Fix Them)

### 1\. CORS Not Working At All?

Double check:

* You added `corsheaders.middleware.CorsMiddleware` it **at the top** of the middleware list.
    
* Your frontend origin matches exactly, including port and protocol.
    
* You restarted your server after changing the settings.
    

### 2\. Preflight Request Fails (OPTIONS method)

Sometimes your browser sends an `OPTIONS` request first to check if the server will allow the real request. Make sure your views or Django setup allow that method, or Django will return a 405 error.

You don’t usually need to do anything here unless you’re using a custom middleware or view decorator that blocks it.

### 3\. Using Django Rest Framework?

No problem – `django-cors-headers` works out of the box. Just make sure it’s installed and the middleware is set up correctly.

## FAQs

### **Can I allow multiple frontend URLs?**

Yes! Just add more items to the list:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://myfrontend.com",
]
```

### **Does CORS affect local development only?**

No, it applies in production too. Any time your frontend and backend are on different origins (different domain or port), you need to handle CORS.

### **Is it secure to allow all origins?**

No. Only do that temporarily during development. Always restrict access in production to just the domains you trust.

### **Do I need to change anything on the frontend?**

Sometimes. If you're sending credentials (like cookies), you’ll need to set `credentials: "include"` in your fetch or Axios requests.

Example with fetch:

```js
fetch("http://localhost:8000/api/data", {
  method: "GET",
  credentials: "include",
})
```

## Final Thoughts

CORS can feel like a wall you keep running into when building web apps. But once you get the hang of how it works – and how to set it up in Django – it becomes a small thing you configure and move on.

Just remember:

* Be specific in production
    
* Always restart the server after changes
    
* Don’t ignore warnings in your browser console – they’re your friends
    

Now you know how to enable CORS in Django the right way.

### Further Resources

* [django-cors-headers GitHub page](https://github.com/adamchainz/django-cors-headers) – for full documentation.
    
* [MDN CORS Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) – to understand how CORS works under the hood.
    
* [Official Django Middleware Docs](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
