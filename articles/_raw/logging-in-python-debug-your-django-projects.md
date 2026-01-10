---
title: Logging in Python – How to Use Logs to Debug Your Django Projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-31T20:46:24.000Z'
originalURL: https://freecodecamp.org/news/logging-in-python-debug-your-django-projects
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Django-Logger.png
tags:
- name: debugging
  slug: debugging
- name: Django
  slug: django
- name: logging
  slug: logging
- name: Python
  slug: python
seo_title: null
seo_desc: "By Md. Saifur Rahman\nThe only perfect code is code that has never been\
  \ written. As a developer, you are bound to face errors and will be responsible\
  \ for debugging them. \nIf you're coding in Python, you can always look at its error\
  \ messages to figure ..."
---

By Md. Saifur Rahman

The only perfect code is code that has never been written. As a developer, you are bound to face errors and will be responsible for debugging them. 

If you're coding in Python, you can always look at its error messages to figure out what's going on. But what if an error occurs that you have no idea what's breaking your code? 

Something might be strangely wrong in the background, but you are unable to recognize it. You can always turn it off and on again – or even better, you can check the logs.

## What is Logging?

If an error occurs or your app decides to work strangely, your log files will come in handy. You can traverse through them and find out where exactly the application is having problems and how you can replicate those problems.

By reproducing the problem, you can dig deeper and find a reasonable solution for the errors. Something which might otherwise take several hours to detect might just take few minutes to diagnose with the presence of log files.

## How Logging Works in Django

Thankfully, Django has support for logging and most of the hard work has already been done by its developers. Django comes with Python's built-in logging module to leverage system logging. 

The Python logging module has four main parts:

1. [Loggers](#heading-1-loggers)
2. [Handlers](#heading-2-handlers)
3. [Filters](#heading-3-filters)
4. [Formatters](#heading-4-formatters)

Every component is explained meticulously in the [Django Official Documentation](https://docs.djangoproject.com/en/3.2/topics/logging/). I don't want you to be overwhelmed with its complexity, so I'll explain every single part briefly:

<h3 id="loggers">1. Loggers</h3>

Loggers are basically the entry point of the logging system. This is what you'll actually work with as a developers. 

When a message is received by the logger, the log level is compared to the log level of the logger. If it is the same or exceeds the log level of the logger, **the message is sent to the handler for further processing.** The log levels are:

* **DEBUG:** Low-level system information
* **INFO:** General system information
* **WARNING:** Minor problems related information
* **ERROR:** Major problems related information
* **CRITICAL:** Critical problems related information

<h3 id="handlers">2. Handlers</h3>

Handlers basically determine what happens to each message in a logger. It has log levels the same as Loggers. But, we can essentially define what way we want to handle each log level. 

For example: **ERROR** log level messages can be sent in real-time to the developer, while **INFO** log levels can just be stored in a system file.

It essentially tells the system what to do with the message like writing it on the screen, a file, or to a network socket

<h3 id="filters">3. Filters</h3>

A filter can sit between a **Logger** and a **Handler**. It can be used to filter the log record. 

For example: in **CRITICAL** messages, you can set a filter which only allows a particular source to be processed.

<h3 id="formatters">4. Formatters</h3>

As the name suggests, formatters describe the format of the text which will be rendered.

Now that we have covered the basics, let's dig deeper with an actual example. [Click here for the source code](https://github.com/sa1if3/django-logging-tutorial). 

**Please note that this tutorial assumes that you are already familiar with the basics of Django.**

## Project Setup

First, create a virtual environment called **`venv`** inside your project folder `django-logging-tutorial` with the command below and activate it.

``` bash
mkdir django-logging-tutorial
virtualenv venv
source venv/bin/activate

Create a new Django project called `django_logging_tutorial`. Notice that the project folder name is with a dash while the project name is with an underscore (- vs _). We will also run a series of commands quickly to set up our project.

## How to Configure Your Log Files

Let's first set up the `settings.py` file of our project. Heads up – notice my comments in the code which will help you understand this process better. 

This code is also mentioned in the [3rd example of the official documentation](https://docs.djangoproject.com/en/3.2/topics/logging/#examples) and in most of our projects, it will serve just fine. I have slightly modified it to make it more robust.

``` python

LOGGING = {
    'version': 1,
    # The version number of our log
    'disable_existing_loggers': False,
    # django uses some of its own loggers for internal operations. In case you want to disable them just replace the False above with true.
    # A handler for WARNING. It is basically writing the WARNING messages into a file called WARNING.log
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'warning.log',
        },
    },
    # A logger for WARNING which has a handler called 'file'. A logger can have multiple handler
    'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

If you read my comments above, you might have noticed that the logger part was just blank. Which essentially means any logger. 

Be careful with this approach as most of our work can be satisfied with in-built [Django loggers](https://docs.djangoproject.com/en/3.2/topics/logging/#django-s-logging-extensions) like `django.request` or `django.db.backends`. 

Also, for the sake of simplicity, I only used a file for storing the logs. Depending on your use case you might also choose to drop an email when **CRITICAL** or **ERROR** messages are encountered. 

To learn more about this, I would encourage you to read the [handler](https://docs.djangoproject.com/en/3.2/topics/logging/#id4) part of the docs. The docs might feel overwhelming at the start, but the more you get used to reading them the more you might discover other interesting or better approaches. 

Don't worry if it's your first time working with documentation. There is always a first time for everything.

I've explained most of the code in the comments, but we still haven't touched upon `propagate` yet. What is it? 

When `propagate` is set as **True**, a child will propagate all their logging calls to the parent. This means that we can define a handler at the root (parent) of the logger tree and all logging calls in the subtree (child) go to the handler defined in the parent. 

It is also important to note that hierarchy is important here. We can also just set it up as **True** in our project as it won't matter in our case since there is no subtree.

## How to Trigger Logs in Python

Now, we need to create some log messages so we can try out our configuration in **`settings.py`**. 

Let's have a default homepage that just displays '**Hello FreeCodeCamp.org Reader :)'** and every time someone visits the page we note down a **WARNING** message in our `warning.log` file as 'Homepage was accessed at 2021-08-29 22:23:33.551543 hours!'

Go to your app `logging_example`, and in `views.py` include the following code. Make sure you have added `logging_example` in the `INSTALLED_APPS` in `setting.py`.

``` python

from django.http import HttpResponse
import datetime
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def hello_reader(request):
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
    return HttpResponse("<h1>Hello FreeCodeCamp.org Reader :)</h1>")



In the project's `urls.py`, add the following code so that when we access the homepage the right function is called.

``` python
from django.contrib import admin
from django.urls import path
from logging_example import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello_reader, name="hello_reader")
]

## Time for Some Testing

Finally, our simple setup is done. All we need to do now is to fire up our server and test our log.

Run the development server with this command:

``` bash
python manage.py runserver

Now, go to your homepage **127.0.0.1:8000** where you will be greeted with the message we have coded. Now check your `warning.log` file in the path created. Sample output is shown below:

``` txt
Homepage was accessed at 2021-08-29 22:38:29.922510 hours!
Homepage was accessed at 2021-08-29 22:48:35.088296 hours!


That's it! Now you know how to perform logging in Django. If you have any questions, just drop me a message. I promise to help :)

If you found my article helpful and want to read more, please check out some Django tutorials at my blog [Techflow360.com](https://techflow360.com/category/web-development/django/).

