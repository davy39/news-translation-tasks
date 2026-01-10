---
title: How to build a photo feed using Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:34:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-photo-feed-using-django-2d81c8519594
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lYy3cb9EF5I8Pz1E.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ogundipe Samuel

  Today, we will make a real-time photo feed framework using Django and Pusher. This
  is like a mini Instagram, but without the comments and filter functionality.


  A basic understanding of Django and jQuery is needed to follow this tu...'
---

By Ogundipe Samuel

Today, we will make a real-time photo feed framework using Django and Pusher. This is like a mini Instagram, but without the comments and filter functionality.

![Image](https://cdn-media-1.freecodecamp.org/images/0*aTITCCoNi8aLM4_G.gif)

A basic understanding of Django and jQuery is needed to follow this tutorial.

### Setting up Django

First, you need to install the Django library (if we don’t have it).

To install Django, we run:

After installing Django, it’s time to create our project. Open up a terminal and create a new project using the following command:

In the above command, we created a new project called `photofeed`. The next step will be to create an app inside our new project. To do that, let’s run the following commands:

Once we’re done setting up the new app, Django needs to know about our new application. To do this, we will go into our `feed\settings.py` and add the message app to our installed apps as seen below:

After doing the above, it’s time to run the application and see if all went well. In our terminal shell, we run:

If we navigate our browser to `http://localhost:8000`, we should see the following:

![Image](https://cdn-media-1.freecodecamp.org/images/0*Bh4MhbFyoq9kt2XQ.png)

### Set up an App on Pusher

At this point, Django is ready and set up. We need to set up Pusher next, as well as grab our app credentials. If you haven’t already, sign up to a free [Pusher](https://pusher.com/signup) account and create a new app, then copy your secret, application key and application id.

![Image](https://cdn-media-1.freecodecamp.org/images/0*lYy3cb9EF5I8Pz1E.png)

The next step is to install the required libraries:

In the above bash command, we installed one package, Pusher. — Pusher: This is the official Pusher library for Python. We will be using this library to trigger and send our messages to the Pusher HTTP API.

### Creating Our Application

First, let us create a model class, which will generate our database structure. Let’s open up `feed\models.py` and replace with the following:

In the above block of code, we defined a model called `Feed`. The Feed table will consist of the following fields:

* A field to store the description of the photo
* A field to store the photo In the above code, while declaring our document field, we have included an `upload_to` attribute, which we set to `static/documents`  
Please note that this path is relative to the path of the `DJANGO MEDIA ROOT`, which we will set now.

While in this article, we will be setting the `MEDIA_ROOT` to the static folder in our `feed` app, so it can get served as a static file. To do that, let us move to our `photofeed/settings.py` and add the code below to our file, immediately after the `STATIC_URL` declaration.

### Running Migrations

We need to make migrations and run them, so our database table can get created. To do that, let us run the following in our terminal:

### Creating Our Views

Our views refer to the file/files that hold up the logic behind the application, often referred to as the `Controller`. Let us open up our `views.py` in our `feed` folder and replace with the following:

In the code above, we have defined three main functions which are:

* index
* pusher_authentication_
* push_feed

In the `index` function, we fetch all the available photos in the database. The photos are then rendered in the view. This enables a new user to see all previous feeds that are available.

In the `pusher_authentication` function, we verify that the current user can access our private channel.

In the `push_feed` function, we check if it is a POST request, then we try validating our form before saving it into the database. (The form used in this method named `DocumentForm` is not available yet. We will be creating it soon.) After the form validation, we then place our call to the Pusher library for real-time interaction.

### Creating The Form Class

A Django Form handles taking user input, validating it, and turning it into Python objects. They also have some handy rendering methods. Let us create a file called `forms.py` in our `feed` folder and add the following content to it:

In the above code block, we have imported our Feed model and used it to create a form. This form will now handle the validation and upload of images to the right folder.

### Populating The URL’s.py

Let us open up our `photofeed\urls.py` file and replace with the following:

What has changed in this file? We have added 3 new routes to the file. We have defined the entry point, and have assigned it to our `index` function. We also defined the push_feed URL and assigned it to our `push_feed` function. This will be responsible for pushing updates to Pusher in real-time. Finally, the `pusher_authentication` endpoint handles the authentication of our private channel.

### Creating the HTML Files

Now we need to create the index.html file which we have referenced as the template for our index function. Let us create a new folder in our `feed` folder called `templates`. Next, we create a file called `index.html` in our `templates` folder and replace it with the code below:

In this HTML snippet, note that we have included some required libraries such as:

* Bootstrap CSS
* jQuery JavaScript library
* Pusher JavaScript library

### Pusher Bindings And jQuery Snippet

That’s it! Now, once a photo gets uploaded, it also gets broadcast and we can listen using our channel to update the feed in real-time. Below is our example jQuery snippet used to handle the file upload as well as Pusher’s real-time updates.

Below is an image of what we have built:

![Image](https://cdn-media-1.freecodecamp.org/images/0*JzA7njPCUC9-ozFM.gif)

### Conclusion

In this article, we have covered how to create a real-time photo feed using Django and Pusher as well as passing CSRF tokens in AJAX request using Django.

The code base to this tutorial is available in a [public Github repository](https://github.com/samuelayo/pusher_django_photo_feed). You can download it for educational purposes.

Have a better way we could have built our application, reservations or comments, let us know in the comments. Remember sharing is learning.

This post was originally published on Pusher’s blog [here](https://blog.pusher.com/build-a-photo-feed-using-django/)

