---
title: How to Build a Message Delivery Status in Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:56:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-message-delivery-status-in-django-e8d1eb2e8b6a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iF8r7xsxvctowLcc.gif
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ogundipe Samuel

  Today, we will make a real-time message delivery status framework with Django and
  Pusher.


  A basic understanding of Django and Vue is needed in order to follow this tutorial.

  Setting up Django

  First, we need to install the Python D...'
---

By Ogundipe Samuel

Today, we will make a real-time message delivery status framework with Django and Pusher.

![Image](https://cdn-media-1.freecodecamp.org/images/0*iF8r7xsxvctowLcc.gif)

A basic understanding of Django and Vue is needed in order to follow this tutorial.

### Setting up Django

First, we need to install the Python Django library if we don’t already have it.  
 To install Django, we run:

After installing Django, it’s time to create our project. Open up a terminal and create a new project using the following command:

[https://gist.github.com/4896cf41463ff83e191949a02bbead23](https://gist.github.com/4896cf41463ff83e191949a02bbead23)

In the above command, we created a new project called `pusher_message`. The next step will be to create an app inside our new project. To do that, let’s run the following commands:

Once we are done setting up the new app, we need to tell Django about our new application, so we will go into our `pusher_message\settings.py` and add the message app to our installed apps as seen below:

After doing the above, it’s time for us to run the application and see if all went well.

In our terminal shell, we run:

If we navigate our browser to `http://localhost:8000`, we should see the following:

### Set up an App on Pusher

At this point, Django is ready and set up. We now need to set up Pusher, as well as grab our app credentials.

We need to sign up on [Pusher](https://pusher.com/signup), create a new app, and also copy our secret application key and application id.

The next step is to install the required libraries:

In the above bash command, we installed one package, `pusher`. This is the official Pusher library for Python, which we will be using to trigger and send our messages to Pusher.

### Creating Our Application

First, let us create a model class, which will generate our database structure.  
Let’s open up `message\models.py` and replace the content with the following:

In the above block of code, we defined a model called `Conversation`. The conversation table consists of the following fields:

* A field to link the message to the user who created it
* A field to store the message
* A field to store the status of the message
* A filed to store the date and time the message was created

### Running Migrations

We need to make migrations and also run them so our database table can be created. To do that, let us run the following in our terminal:

### Creating Our Views

In Django, the views do not necessarily refer to the HTML structure of our application. In fact, we can see it as our `Controller`, as referred to in some other frameworks.

Let us open up our `views.py` in our `message` folder and replace the content with the following:

In the code above, we have defined four main functions which are:

* `index`
* `broadcast`
* `conversation`
* `delivered`

In the `index` function, we added the login required decorator, and we also passed the login URL argument which does not exist yet, as we will need to create it in the `urls.py` file. Also, we rendered a default template called `chat.html` that we will also create soon.

In the `broadcast` function, we retrieved the content of the message being sent, saved it into our database, and finally triggered a Pusher request passing in our message dictionary, as well as a channel and event name.  
 In the `conversations` function, we simply grab all conversations and return them as a JSON response.

Finally, we have the `delivered` function, which is the function that takes care of our message delivery status.

In this function, we get the conversation by the ID supplied to us. We then verify that the user who wants to trigger the delivered event isn’t the user who sent the message in the first place. Also, we pass in the `socket_id` so that Pusher does not broadcast the event back to the person who triggered it.

The `socket_id` stands as an identifier for the socket connection that triggered the event.

### Populating The URL’s.py

Let us open up our `pusher_message\urls.py` file and replace with the following:

What has changed in this file? We have added six new routes to the file.  
 We have defined the entry point and assigned it to our `index` function. Next, we defined the login URL, which the `login_required` decorator would try to access to authenticate users.

We have used the default `auth` function to handle it but passed in our own custom template for login, which we will create soon.

Next, we defined the routes for the `conversation` message trigger, all `conversations`, and finally the `delivered` conversation.

### Creating the HTML Files

Now we will need to create two HTML pages so our application can run smoothly. We have referenced two HTML pages in the course of building the application.

Let us create a new folder in our `messages` folder called `templates`.

Next, we create a file called `login.html` in our `templates` folder and replace it with the following:

### Vue Component And Pusher Bindings

That’s it! Now, whenever a new message is delivered, it will be broadcast and we can listen, using our channel, to update the status in real-time. Below is our Example component written using Vue.js.

**Please note:** In the Vue component below, a new function called `**queryParams**` was defined to serialize our POST body so it can be sent as `**x-www-form-urlencoded**` to the server in place of as a `**payload**`. We did this because Django cannot handle requests coming in as `**payload**`.

Below is the image demonstrating what we have built:

![Image](https://cdn-media-1.freecodecamp.org/images/0*iF8r7xsxvctowLcc.gif)

### Conclusion

In this article, we have covered how to create a real-time message delivery status using Django and Pusher. We have gone through exempting certain functions from CSRF checks, as well as exempting the broadcaster from receiving an event they triggered.

The code is hosted on a [public GitHub repository](https://github.com/samuelayo/pusher_django_message_delivery). You can download it for educational purposes.

Have a better way we could have built our application, reservations or comments? Let us know in the comments. Remember, sharing is learning.

This post was originally published by the author in the pusher blog [here](https://blog.pusher.com/how-to-build-a-message-delivery-status-in-django/).

This version has been edited for clarity and may appear different from the original post.

