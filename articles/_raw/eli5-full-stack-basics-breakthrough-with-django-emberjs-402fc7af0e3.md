---
title: 'ELI5 Full Stack Basics: breakthrough with Django & EmberJS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T23:04:23.000Z'
originalURL: https://freecodecamp.org/news/eli5-full-stack-basics-breakthrough-with-django-emberjs-402fc7af0e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-YXdpMxaFFkY2QKdxgIsFQ.png
tags:
- name: Django
  slug: django
- name: ember
  slug: ember
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Michael Xavier

  Welcome to ELI5 Full Stack: Breakthrough with Django & EmberJS. This is an introduction
  to full stack development for everyone, especially beginners. We’ll go step-by-step
  through the development of a basic web application. A librar...'
---

By Michael Xavier

Welcome to **_ELI5 Full Stack: Breakthrough with Django & EmberJS_**. This is an introduction to full stack development for everyone, especially **beginners**. We’ll go step-by-step through the development of a basic web application. A library of sorts. Together we’ll build a back-end to store data and a RESTful API to manage it. Then we’ll construct a front-end user interface for users to view, add, edit, and delete the data.

This isn’t meant to be a deep dive into either **Django** or **EmberJS**. I don’t want us to get bogged down with too much complexity. **Rather its purpose is to show the critical elements of basic full stack development**. How to stitch together the back end and front end into a working application. I’ll go into detail about the software, frameworks, and tools used in the process. Every terminal command run and line of code in the final application is present in this tutorial.

I’ve kept each section short and to the point so that no one’s head explodes. There are also indicators to mark points for reflection so you can go back and look at what we’ve done and save state. If you don’t know what something means click through to the linked articles which will explain in detail. Remember, this is as an introduction to everyone including **beginners**. If you don’t need the hand holding push on through to the sections relevant to you.

If you’re a beginner, I that suggest you write every line of code and run each terminal command yourself. Don’t copy and paste. It won’t sink in. Take your time and think about what you’re doing. This is a critical trait of an effective and self-sufficient programmer. You will develop this over time if you write your own code and think about what you’re writing. If you mess up (look at my commit history, I definitely did) don’t sweat it. Go back. This isn’t a race. You’ll be fine if you take your time.

![Image](https://cdn-media-1.freecodecamp.org/images/A4ayt-UmztcellrLe6SvphBGHrsHz1u1IXMk)
_Sometimes I get whiplash_

**Note**: I developed this tutorial on a MacBook Pro running [macOS High Sierra (10.3.6)](https://www.macrumors.com/roundup/macos-10-13/). I’m using [iTerm2](https://www.iterm2.com/) for the terminal and [Sublime Text 3](https://www.sublimetext.com/3) as my text editor. All testing uses the [Chrome](https://www.google.com/chrome/) browser and its built-in tools. The actual code shouldn’t have any differences. You can [**download the final project files from the Github repository**](https://github.com/lookininward/my_library).

### Table of Contents

#### **Section 1: The Whats, Hows, and Whys**

1.1 Why I Wrote This Tutorial  
1.2 Back End, Front End. What’s the Difference?  
1.3 The Concept: A Basic Library Application  
1.4 Project Directory Structure  
1.5 Project Directory Setup  
1.6 Conclusion

#### Section 2: Diving into the Back End

2.1 Install Required Software  
2.2 Start a Django Project: server  
2.3 Start a Django App: books  
2.4 Describe the Book model  
2.5 Register the Book model with the admin  
2.6 Conclusion

#### Section 3: Build a Server, then REST

3.1 Django REST Framework  
3.2 Create the books API folder  
3.3 Create a book serializer  
3.4 Create a view to GET and POST books data  
3.5 Create URLs to access books data  
3.6 Conclusion

#### Section 4: Laying Down Front-end Foundations

4.1 Install Required Software  
4.2 Start an Ember Project: client  
4.3 Displaying books data   
4.4 The books route  
4.5 Displaying real data in the books route  
4.6 Conclusion

#### **Section 5: Correct data formats, deal with individual records**

5.1 Install the Django REST Framework JSON API  
5.2 Working with individual book records  
5.3 The book route  
5.4 Conclusion

#### Section 6: Functional Front end

6.1 Adding a new book to the database  
 6.2 Deleting a book from the database  
6.3 Editing a book in the database  
6.4 Conclusion

#### Section 7: Moving On

7.1 What’s Next?  
7.2 Further Reading

### Section 1: The Whats, Hows, and Whys

### 1.1 Why I Wrote This Tutorial

Imagine that you’ve recently joined a new company. They’ve been in business for some time, and their major products are already out in production. Think of the application you see today as cake. The process of picking the ingredients, recipe, and putting it all together… well that’s long over. You’ll be working on pieces of that finished cake.

The developers at the start of a project have laid down certain configurations. These change and conventions are also developed over time as developers come and go. By the time you arrive it may be difficult to comprehend how we’ve gotten to where we are. This was my situation. I felt that dipping into the whole stack would be the only way for me to feel comfortable. It would help me understand where we came from and how to move forward with the software we’re building.

This tutorial is the culmination of my experiences as a junior software developer. I’ve been learning a lot at my time with [Closing Folders](http://we%27re%20hiring%20now%20so%20feel%20free%20to%20get%20in%20touch%21/). It represents a shift in my thinking as I take steps towards more complex full stack development. It also serves as an entry point for developers at the stage where they’re wondering how the cake gets baked. I hope this tutorial is as useful for you as it was instructive for me to create.

![Image](https://cdn-media-1.freecodecamp.org/images/ReFm2Fb6XzpWqD5x8fDDWipgkDicy7WfarFg)
_That wholesome feeling_

**Note**: In a typical workflow a developer would start on the back end to set up the database, and create a REST API. Then, they would work on the front end and build the user interface. Things aren’t so simple though. We make mistakes and often have to go back and forth to resolve them. The jumping back and forth will help build more connections in your mind. and help you better understand how all the pieces fit together. Embrace your mistakes. You’ll be making a lot of them!

**Note2**: Attention Senior Devs, Junior Devs, and Designers! [Closing Folders](http://We're hiring now so feel free to get in touch!) is hiring now so feel free to get in touch.

### 1.2 Back End, Front End. What’s the Difference?

Back-end development. Front-end development. Full-stack development. So much development... What’s the difference anyway?

Think of front-end development as the part of the application that you see and interact with. For example, the user interface is part of the front end. That’s where the user views data and interacts with it.

Back-end development is everything that stores and serves data. Think about what happens when you login to Medium. None of your user profile data or stories exists on the front end. It’s stored and served from the back end.

The front end and back end work together to form the application. The back end has the instructions for how to store and serve the data. The front end has the instructions to capture the data, and how to display it.

![Image](https://cdn-media-1.freecodecamp.org/images/qD5LLIeEVVXSlKjIuqV2OJspW-Sxlu-YSNX4)
_Basic front-end and back-end communication._

Find out more about the differences in [this article](http://blog.teamtreehouse.com/i-dont-speak-your-language-frontend-vs-backend).

![Image](https://cdn-media-1.freecodecamp.org/images/kysaEsRUJ593f1PnOYBlVm1W2UOjl9UX4CnJ)
_MFW I realized development never actually ends_

### 1.3 The Concept: A Basic Library Application

Before we start building anything, let’s outline our plans and what we’re trying to achieve. We want to build a [web application](https://stackoverflow.com/a/8694944/5513243) called **my_library** that runs in the browser. The application is exactly what it sounds like, a digital library of books. We won’t be dealing with actual book content though. The books will only have title, author, and description information. Keeping it simple.

The application will have the following functionality:

* View all books as a single list on the home page, ordered by title
* View each book in detail, displaying its title, author, and description
* Add a new book with the fields title, author, and description
* Edit an existing book’s title, author, and description fields
* Delete an existing book

#### 1.3.1 my_library’s final design and functionality

Take a look at the screenshots below. They depict the application’s final look and functionality:

![Image](https://cdn-media-1.freecodecamp.org/images/OfA6C6cfPUhNSjp6GhZy3N2gXD6UyRhOm5GZ)
_View all the books in our database as a single list ordered by title._

![Image](https://cdn-media-1.freecodecamp.org/images/E0AxS4kV57E1jZegwU599JK3Mre18RUt2C0Z)
_Click on a book to see a detailed view with author and description information._

![Image](https://cdn-media-1.freecodecamp.org/images/ris6Kqmw0lMqDzocS3T72WpXJpBxovfoV0Jy)
_Add a new book to the database with the fields title, author, and description._

![Image](https://cdn-media-1.freecodecamp.org/images/8Vx8NrPBH7ae-u0LG8tzT8QZGSHmmaU8MN0R)
_Edit an existing book’s title, author, and description fields._

![Image](https://cdn-media-1.freecodecamp.org/images/XOuou7IuqqxrlNSU5DdADIxx-gISjjnyn42l)
_Confirm deletion of an existing book._

### 1.4 Project Directory Structure

There are innumerable ways to structure a given project. I’ll keep everything under one `my_library` folder for simplicity’s sake like so:

```
my_library
  - server
    - server
    - books
      - api
    - db.sqlite3
    - manage.py
  - client
    - app
      - adapters
      - controllers
      - models
      - routes
      - templates
      - styles
      router.js
```

These aren’t all the folders and files that the project will contain, though they’re the main ones. You’ll notice quite a few autogenerated files that you can ignore. Though it would be useful for you to read documentation that explains their purpose.

The `my_library` directory contains folders for the back end and front end sub-projects. `server` refers to the Django back end, and `client` refers to the EmberJS front end.

#### 1.4.1 Back End

* `server` contains another folder called `server`. Inside are the top level configurations and settings for the back end.
* The `books` folder will contain all the models, views, and other configuration for the book data.
* Inside the `books/api` folder we’ll create the serializers, URLs, and views that make up our REST API.

#### 1.4.2 Front End

* `client` is our EmberJS front end. It contains routes, templates, models, controllers, adapters, and styles. `router.js` describes all the application routes.

Let’s go ahead and set up the main project directory `my_library`.

### 1.5 Project Directory Setup

#### 1.5.1 Create the main project folder: my_library

Now that we know what we’re going to build, let’s take a few minutes to set up the main project directory `my_library`:

```
# cd into desktop and create the main project folder
  cd ~/desktop && mkdir my_library
```

Create a basic `README.md` file inside the folder with the following content:

```
# my_library
This is a basic full stack library application built. Check out the tutorial: 'ELI5 Full Stack: Breakthrough with Django & EmberJS'.
```

Now let’s commit this project to a new Git repository as the project start point.

#### 1.5.2 Install Git for version control

Git is version control software. We’ll use it to keep track of our project and save our state step-by-step so we can always go back if we make breaking errors. I’m sure most of you’re already familiar with it.

For the uninitiated, you can find out more [here](https://git-scm.com/about). If you don’t have Git installed, you can download it [here](https://git-scm.com/download/mac).

Check that it installed with:

```
$ git --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/KApRH2jTbtKv40ejPFGjr54s8hGPoH9YefFD)

#### 1.5.3 Create a new project repository

I have an account with [Github](https://github.com/). It’s popular and works well so that’s what I’ll be using. Feel free to use other solutions if they suit you better.

Create a new repository and get the remote URL which should look like this:

```
git@github.com:username/repo_name.git
```

![Image](https://cdn-media-1.freecodecamp.org/images/qbjGYbQ9czlLwNvoMw5JwaOmU9jRFD3dDyn7)

#### 1.5.4 Commit and push your changes to the project repository

Inside the `my_library` folder initialize the empty repository:

```
git init
```

Now [add the remote URL](https://help.github.com/articles/adding-a-remote/) so Git knows where we’re pushing our files to:

```
git remote add origin git@github.com:username/repo_name.git
# check that it's been set, should display the origin
  git remote -v
```

Time to push our code to Github:

```
# check the status of our repo
# should show the new file README.md, no previous commits
  git status
# add all changes
  git add .
# create a commit with a message
  git commit -m "[BASE] Project Start"
# push changes to the repo's master branch
  git push origin master
```

The remote Git repository updates with the changes we’ve pushed:

![Image](https://cdn-media-1.freecodecamp.org/images/jNsMz7ixvdfL8iXHX-g5D8Q7Ov0OptROPTVW)

Now that we have a main project directory and a repository we can finally start working on our back end!

**NOTE**: From this point onward I won’t be going into any more detail about commits. The **review and commit indicator below** will let you know when it’s a good time to do so:

![Image](https://cdn-media-1.freecodecamp.org/images/o4SwOn9IR02bwppfcmoKRBV2iujutkGXN8e4)

### 1.6 Conclusion

We’ve come to the end of **Section 1** with the following steps completed:

* Got a feel for what we’re building and how it will work
* Created the `my_library` main project directory
* Installed `git` and created a remote project repository on Github
* Initialized the local repository and set the remote URL
* Created a`README.md` file, then committed and pushed all changes

![Image](https://cdn-media-1.freecodecamp.org/images/oMqTTVH075JVrjgb8mj56cKWDPBEfogE5Pea)
_Puppy is proud of you_

### Section 2: Diving into the Back End

This section is all about back-end development with Django. We’ll begin with the installation of the required software.

Next, we’ll move onto the creation of a new Django project called `server` and create a new app called `books`. In the `books` app we describe the `Book` model and register the model with the admin.

Once we create a `Superuser` account we can login to the Django Admin site. We’ll use the Django Admin site to administrate the database and start seeding it with book data.

### 2.1 Install Required Software

Before we begin our back end project we’ll need to install some software:

* [Python](https://www.python.org/doc/essays/blurb/)
* [pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py)
* [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Django](https://docs.djangoproject.com/en/1.11/topics/install/)

#### 2.1.1 Python

If your MacOS is up-to-date it likely already has `Python 2.7` installed. Feel free to use either `2.7` or `3.x`. They’re the same for the purposes of this tutorial.

Installation is simple. [Download the installer](https://www.python.org/downloads/) and install as you would a typical MacOS application. Open up the terminal and check that it’s installed:

```
python --version 
```

![Image](https://cdn-media-1.freecodecamp.org/images/KN6ZDc46wNzVcEH1yPRUr3ty4fL8wuh6loJV)

#### 2.1.2 pip

In simple terms, pip (Pip Installs Packages) is a package management system. It’s used to install and manage software packages written in Python. In the terminal:

```
# cd into the desktop
  cd ~/desktop
 
# download the pip Python script
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 
# run the script
  python get-pip.py
# once installation completes, verify that it's installed
  pip —-version
```

Full installation documentation is available [here](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py).

#### 2.1.3 virtualenv

virtualenv is a ‘_tool to create isolated Python environments’._ These environments have their own installation directories. They don’t share libraries with others. Such silos protect the globally installed libraries from unwanted changes.

With it we can play with Python libraries without messing up the global environment. For example, you install `exampleSoftware 1.0` on your computer. With a virtual environment activated you can upgrade to `exampleSoftware 1.2` and use it. This won’t affect the global install of `exampleSoftware 1.0` at all.

For the development of a particular app you may want to use `1.2` and for other contexts `1.0` will be appropriate. Virtual environments give us the ability to separate these contexts. Full installation documentation is available [here](https://virtualenv.pypa.io/en/stable/installation/).

Now, open up the terminal to install virtualenv:

```
# use pip to install virtualenv
  pip install virtualenv
# verify that it's installed
  virtualenv —-version
```

Let’s create a directory to house our virtual environments:

```
# cd into the root directory
  cd ~/
# create a hidden folder called .envs for virtual environments
  mkdir .envs
# cd into the virtual environments directory
  cd .envs
```

We can now create a virtual environment for our project:

```
# create a virtual environment folder: my_library
  virtualenv my_library
# activate the virtual environment from anywhere using
  source ~/.envs/my_library/bin/activate
```

Now that we’ve created a virtual environment called `my_library` there are a few rules to keep in mind. **Make sure the environment is always activated before installing, or updating any packages.**

Finally, take a moment to upgrade pip inside this virtual environment:

```
pip install -U pip
```

#### 2.1.4 Django 1.11 (LTS)

Django is a web framework that ‘_encourages rapid development and clean, pragmatic design…’_

It provides us with a set of common components so we don’t have to reinvent everything from scratch.

Examples include:

* a management panel
* a way to handle user authentication

Checkout out [this DjangoGirls article](https://tutorial.djangogirls.org/en/django/) to learn more about Django and why it’s used.

![Image](https://cdn-media-1.freecodecamp.org/images/xTQRhumtGS8zEEkoz6pjawMTmfHTJBYDzmJd)

In this project we’ll be using Django to handle the back end. Along with its add-ons, Django provides the basic tools to develop a REST API.

```
# inside my_library with virtualenv activated
  pip install Django==1.11
# verify that it's installed, open up the Python shell
  python
# access the django library and get the version (should be 1.11)
  import django
  print(django.get_version())
# exit using keyboard shortcut ctrl+D or:
  exit()
```

Full installation documentation is available [here](https://docs.djangoproject.com/en/1.11/topics/install/).

### 2.2 Start a Django Project: server

Let’s use the [django-admin](https://docs.djangoproject.com/en/2.1/ref/django-admin/) to generate a new Django project. This is Django’s ‘_command-line utility for administrative tasks_’:

```
# cd into the project folder
  cd ~/desktop/my_library
# initialize the virtual environment
  source ~/.envs/my_library/bin/activate
# use Django to create a project: server
  django-admin startproject server
# cd into the new Django project
  cd server
# synchronize the database
  python manage.py migrate
# run the Django server
  python manage.py runserver
```

Now visit `http://localhost:8000` in your browser and confirm that the Django project is working:

![Image](https://cdn-media-1.freecodecamp.org/images/7i6tTqE67PlSVFaTr9cp64isfajFSzMzFehh)
_Server running. Success!_

You can shut down the server with `cmd+ctrl`.

#### 2.2.1 Create the Superuser account

We’ll have to create a [superuser](https://docs.djangoproject.com/en/1.11/ref/django-admin/#createsuperuser) to login to the admin site and handle database data. Inside `my_library/server` we run:

```
# create superuser
  python manage.py createsuperuser
```

Fill in the fields `Username`, `Email Address` (optional), and `Password`. You should receive a success message.

Now run the server with `python manage.py runserver` and go to `localhost:8000/admin` to see the admin login page. Enter your superuser account details to login.

![Image](https://cdn-media-1.freecodecamp.org/images/o1Gki-a2KqtXWP15qNmcEomH8Zo8lpMzxkk-)
_Logged into the Django Admin site_

Nice! We have access to the Django admin site. Once we create the `books` model and do the appropriate setup we’ll be able to add, edit, delete, and view book data.

Logout and shut down the server with `cmd+ctrl`.

#### 2.2.2 Protecting Our Secrets

Before moving on, we’ll want to update the settings.py file. It contains authentication credentials that we don’t want to expose to the public. We’ll want to keep these credentials out of our remote repository. There are many [ways of protecting ourselves.](https://medium.freecodecamp.org/how-to-securely-store-api-keys-4ff3ea19ebda) This is my approach to it:

```
# create a config.json file to hold our configuration values
  my_library/server/server/config.json
```

Inside we’ll store our `SECRET_KEY` value from `settings.py` under `API_KEY`:

```
{
  "API_KEY" : "abcdefghijklmopqrstuvwxyz123456789"
}
```

In `settings.py` import the `json` library and load the config variables:

```py
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(BASE_DIR + '/server/config.json', 'r') as config:
    obj = json.load(config)
SECRET_KEY = obj["API_KEY"]
...
```

So that `config.json` (with the secret key) isn’t pushed to the repository, create a `.gitignore` file in `my_library`. This ignores it (along with some other autogenerated files and the database):

```
### Django ###
config.json
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
media
```

![Image](https://cdn-media-1.freecodecamp.org/images/gdH03DpyBNSsAOwSThZDMwnkkM8LFI0DIoyQ)

Now when you commit the changes the files and folders listed above aren’t added. Our secrets are safe and our repo won’t contain unnecessary extra files!

![Image](https://cdn-media-1.freecodecamp.org/images/unF2nV9ydWZI5ueW1dOY5nrSbkGBObGUe48x)

### 2.3 Start a Django App: books

Think of Django apps as modules that plugin into your project. We’ll create an app called `books` containing the models, views, and other settings. This is how we interact with the books data in the database.

What are the differences between projects and apps in Django? Check out [this thread](https://stackoverflow.com/questions/19350785/what-s-the-difference-between-a-project-and-an-app-in-django-world).

```
# create new app: books
  python manage.py startapp books
# creates directory: my_library/server/books
```

Now we’ll install the `books` app into the `server` project. Open the settings file: `my_library/server/server/settings.py`.

Scroll to the `INSTALLED_APPS` array. Django has installed it's own core apps by default. Install the `books` app at the end of the array:

```
INSTALLED_APPS = [
  ...
  'books'
]
```

### 2.4 Describe the Book model

Next we describe the `Book` model in the books app. Open the models file `my_library/server/books/models.py`.

Describe a `Book` model which tells Django that every book in the database will have:

* a `title` field up to 500 characters in length
* an `author` field up to 100 characters
* a `description` field with an open-ended number of characters

```py
from django.db import models

class Book(models.Model):
  title       = models.CharField(max_length=500)
  author      = models.CharField(max_length=100)
  description = models.TextField()
```

### 2.5 Register the Book model with the admin

Now we register the `Book` model with the admin for our `books` app. This lets us view it in the admin site and manipulate the books data from there. Open the admin file `my_library/server/books/admin.py` and add:

```py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'description']
```

With a new model created we’ll have to make and run [migrations](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-makemigrations) so that the database synchronizes:

```
python manage.py makemigrations
python manage.py migrate
```

Run the server and go to `localhost:8000/admin` to login. Notice that the Book model registered with the admin displays:

![Image](https://cdn-media-1.freecodecamp.org/images/BByc9ryhPWVpc6U4SWpaz3E6JTrOeFcQcwFB)
_With the ‘Book’ model registered with the admin_

Clicking on ‘Books’ displays an empty list because there are no books in the database. Click ‘Add’ to begin creating a new book to add to the database. Go ahead and create a few books.

![Image](https://cdn-media-1.freecodecamp.org/images/g24EmlIIvatYfhwIRgzXi3yakh8MzCJnnxfo)
_Add a new book to the database_

Save and go back to the list to view the new data. Now it displays the title, author, and description (`list_display array`) fields.

![Image](https://cdn-media-1.freecodecamp.org/images/jnqaPh1DSeqpT2wrzeA9bppZRhWcVM3Z4O21)
_List of all the books we’ve added to the database_

This is great. We can now view our database books in the admin site. Create, edit, and delete functions are also available.

**Note**: For simplicity’s sake we’ll use the [SQLite database.](https://www.sqlite.org/about.html) It comes preinstalled with the creation of every Django project. No need to do any extra work with databases for the purposes of this tutorial.

![Image](https://cdn-media-1.freecodecamp.org/images/vMyJyhv4xHSQNKh3IkRdoJvFKtO5Olet5iQz)

### 2.6 Conclusion

Congrats, we made it to the end of **Section 2**! This is what we’ve done so far:

* Installed `python`
* Used `python` to install the `pip` package manager
* Used `pip` to install `virtualenv` to create virtual environments
* Created a virtual environment in `~/.envs` called `my_library`
* Activated the `my_library` environment and upgraded `pip`
* Installed `Django 1.11 LTS` within the `my_library` environment
* Created our project directory `my_library`
* Created the Django project `server`
* Created a `Superuser` account to access the Django admin site
* Protected our secrets by moving our `SECRET_KEY` into `config.json`
* Ignored autogenerated and/or sensitive files with `.gitignore`
* Created a new app called `books`
* Described the `Book` model
* Registered the `Book` model with the admin
* Added books data into the database

![Image](https://cdn-media-1.freecodecamp.org/images/-CPsLneURbcGROamQjKRjILkxEgEv5-DNq3o)
_That which holds the internet together_

### Section 3: Build a Server, then REST

In this section we use the Django REST Framework to build our `books` API. It has serializers, views, and URLs that query, structure, and deliver the book data. The data and methods are accessible through API endpoints.

These endpoints are one end of a communication channel. Touchpoints of the communication between the API and another system. The other system in this context is our Ember front end client. The Ember client will interact with the database through the API endpoints. We create these endpoints with Django and the Django REST Framework.

We used Django to set up the `book` model and the admin site that lets us interact with the database. Django REST Framework will help us build the REST API that the front end will use to interact with the back end.

![Image](https://cdn-media-1.freecodecamp.org/images/DRBFIYTjAoZWDNDv9VOK1bWvOIIJej8x5xOP)
_Application layers stacked one by one._

### 3.1 Django REST Framework

[Django REST Framework](http://www.django-rest-framework.org/) (DRF) builds on top of Django. It simplifies the creation of [RESTful Web APIs](http://rest.elkstein.org/). It comes with tools to make the process straightforward.

The developers of DRF have identified common patterns for serializers and views. Since our data and what users can do with it are simple, we’ll use the built-in serializers and views. Remember, our book data only has three fields `title`, `author`, and `description`. Users are able create new records of books, edit, and delete existing records. This functionality is well within the range of basic common patterns. They’re well supported by the built-in serializers and views. We won’t have to build these from scratch.

For more complex projects you’ll want to overwrite defaults or make your own. Again, for the purposes of simplicity we’ll use what comes out of the box without undue modification.

![Image](https://cdn-media-1.freecodecamp.org/images/e6SmOCOMO13g05h-y06mLtBMqtAn2is3WxwX)

#### 3.1.1 Install Django REST Framework

Enter the `my_library` directory and activate the virtual environment. To start working with DRF, install it with `pip`:

```
# enter my_library
  cd ~/desktop/my_library

# activate the virtual environment
  source ~/.envs/my_library/bin/activate

# install Django REST Framework
  pip install djangorestframework
# install Markdown support for the browsable API
  pip install markdown
```

Now open up `my_library/server/server/settings.py`. Install DRF right above the `books` app in the `INSTALLED_APPS` array:

```
INSTALLED_APPS = [
  ...
  'rest_framework',
  'books'
]
```

Add the default settings at the bottom of the file as an object called `REST_FRAMEWORK`:

```
REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': [      
   'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
  ]
}
```

The settings object contains a `DEFAULT_PERMISSION_CLASSES` key with an array. The only item in the array is a permission class. This ‘_allows unauthenticated users to have read-only access to the API’_. Find out more about permissions [here](http://www.django-rest-framework.org/api-guide/permissions/#permissions).

### 3.2 Create the books API folder

With DRF installed let’s start building the `books` API. Create a new folder called `api` inside the `books` app. Then create an empty `__init__.py` file within: `my_library/server/books/api/__init__.py`.

The empty file tells Python that this folder is a Python module. The `api` folder will contain the serializers, views, and URLs for our books data. I’ll get into the meanings of these terms in their respective sections below.

![Image](https://cdn-media-1.freecodecamp.org/images/teuNGFUsjk6LLyFuKtD-pcN1IwvWwP8o0oh6)

### 3.3 Create a book serializer

In simple terms, [serializers](http://www.django-rest-framework.org/api-guide/serializers/) take database data and restructure it. This structure is a blueprint for the data to alternate between application layers. It gets the front end and backend to speak to each other in a common language.

For example, the front end we’ll create expects the response returned to it from a request to be in the JSON format. Serializing the data to be in JSON ensures the front end will be able to read and write it.

```py
from rest_framework import serializers
from books.models import Book
class bookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = (
      'id',
      'title',
      'author',
      'description',
    )
```

This serializer takes the data and transforms it into the JSON format. This ensures that it’s understandable to the front end.

#### **Imports**

We import built-in `serializers` from DRF, and the `Book` model from our `books` app.

```
from rest_framework import serializers
from books.models import Book
```

#### **The bookSerializer Class**

For this project we want a `Serializer` class that ‘_corresponds to the Model fields_’. The serializer should map to the model fields `title`, `author`, and `description`. We can do this with the `[ModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer)`. According to the documentation:

The `ModelSerializer` class is the same as a regular `Serializer` class, except that:

* It will generate a set of fields for you, based on the model.
* It will generate validators for the serializer, such as unique_together validators.
* It includes simple default implementations of `.create()` and `.update()`.

The built-in tools are more than capable of handling our basic needs.

```py
class bookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = (
      'id',
      'title',
      'author',
      'description',
    )
```

### 3.4 Create a view to GET and POST books data

View functions take in a web request and return web responses. A web request to `localhost:8000/api/books` for example elicits a response from the server.

This response can be ‘_HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything…_’ In our case we expect to get back books data structured in the JSON format.

Create the views file in `my_library/server/books/api/views.py`:

```py
from rest_framework import generics, mixins
from books.models import Book
from .serializers import  bookSerializer
class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'books'
  serializer_class = bookSerializer
  def get_queryset(self):
    return Book.objects.all()
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
```

#### **Imports**

First we import `[generics](http://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)` and `[mixins](http://www.django-rest-framework.org/api-guide/generic-views/#mixins)` from DRF. Then the `Book` model from our `books` app and the `bookSerializer` that we created.

`generics` refers to API views that ‘_map to your database models_’. These are ‘_pre-built views that provide for common patterns_’. `mixins` are classes that ‘_provide the actions that used to provide the basic view behavior_’. Our book model is simplistic. It only has `title`, `author`, and `description` attributes so these provide us with the basics we need.

```py
from rest_framework import generics, mixins
from books.models import Book
from .serializers import  bookSerializer
```

#### **The bookAPI View**

We then create a `bookAPIView` which takes in the `[CreateModelMixin](http://www.django-rest-framework.org/api-guide/generic-views/#createmodelmixin)` and `[ListAPIView](http://www.django-rest-framework.org/api-guide/generic-views/#listapiview)`.

`CreateModelMixin` provides a `.create(request, *args, **kwargs)` method_._ This implements the creation and persistence of a new model instance. When successful it returns a `201 Create` response. This comes with a serialized representation of the object that it created.

For example, we would make a POST request to create a new book record for the Steve Jobs book by Walter Isaacson. If successful we get back a response with the code `201`. The serialized representation of the book record like so:

```py
{
  "data": {
    "type": "books",
    "id":"10",
    "attributes": {
      "title": "Steve Jobs",
      "author": "Walter Isaacson",
      "description": "Based on more than forty interviews with Jobs conducted over two years—as..."
    }
  }
}
```

When unsuccessful, we’ll get back a `400 Bad Request` response with errors details. For example, if we try to create a new book record but don’t provide any `title` information:

```json
{
  "errors":[
    {
      "status": "400",
      "source": {
        "pointer": "/data/attributes/title"
      },
      "detail": "This field may not be blank."
    }
  ]
}
```

`ListAPIView` serves our read-only endpoints (GET). It represents ‘_a collection of model instances_’. We use it when we want to get all or many books.

`bookAPIView` also takes in the recently created `bookSerializer` for its `serializer_class`.

We set the `resource_name` to ‘books’ to ‘_specify the_ _type_ _key in the json output_’. The front end client data store layer will have a `book` model that is case sensitive. We don’t want to `book` model in Ember and the `Book` model in Django to clash. Setting the `resource_name` here nips that issue in the bud.

```py
class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'books'
  serializer_class = bookSerializer
```

#### **Functions**

The function `get_queryset` returns all the book objects in the database. `post` takes in the request and arguments and creates a new database record of a book if the request is valid.

```py
def get_queryset(self):
    return Book.objects.all()
def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
```

### 3.5 Create URLs to access books data

URL patterns map a URL to views. For example, visiting `localhost:8000/api/books` should map to a URL pattern. That then returns the results of a query to that view.

Create the URLs file in `my_library/server/books/api/urls.py`:

```py
from .views import bookAPIView
from django.conf.urls import url
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]
```

#### **Imports**

We import our view `bookAPIView` and `url`. We’ll use `url` to create a list of url instances.

```py
from .views import bookAPIView
from django.conf.urls import url
```

#### **booksAPI URL patterns**

In the `urlpatterns` array we create a URL pattern with the following structure:

* the pattern `r'^$'`
* the Python path to the view `bookAPIView.as_view()`
* the name `name='book-create'`

The pattern `r’^$’`is a regular expression that ‘[_matches an empty line/string_](https://stackoverflow.com/a/31057541/5513243)’. This means it matches to `localhost:8000`. It matches to anything that comes after the base URL.

We call `[.as_view()](https://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#django.views.generic.base.View.as_view)` on `bookAPIView` because to connect the view to the url. It ‘[_is the function(class method) which will connect [the] class with its url_](https://stackoverflow.com/a/31491074/5513243)’. Visit a particular URL and the server attempts to match it to the URL pattern. That pattern will then return the `bookAPI` view results that we’ve told it to respond with.

The `name=’book-create’` attribute provides us with a `name` attribute. We use it to refer to our URL throughout the project. Let’s say you want to change the URL or the view it refers to. Change it here. Without `name` we would have to go through the entire project to update every reference. Check out [this thread](https://stackoverflow.com/a/11241936/5513243) to find out more.

```
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]
```

#### **server URL patterns**

Now let’s open up `server`’s URLs file `my_library/server/server/urls.py`:

```py
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^api/books', include('books.api.urls', 
                              namespace='api-books'))
]
```

Here we import `include` and create the `r’^api/books’` pattern which takes in any URLs we created in the `api` folder. Now the base URL for our `books` API URLs becomes `localhost:8000/api/books`. Visiting this URL will match to our `r’^/api/books’` pattern. This matches to the `r’^$’` pattern we constructed in the `books` API.

We use `namespace=’api-books’` so that the URLs don’t collide with each other. This would happen if they’re named the same in another app we create. Learn more about why we use `namespaces` in [this thread](https://stackoverflow.com/a/19171674/5513243).

#### 3.5.1 Demonstration: Browsing the books API

Now that we have the base REST framework setup let’s check out the data the back end is returning. With the server running, visit `localhost:8000/api/books`. The [browsable API](http://www.django-rest-framework.org/topics/browsable-api/) should return something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/vRQH7EEhJl7Dt0M8tqtXezjE48ESk1PF4Urv)
_Django REST Framework returning book data from the database_

![Image](https://cdn-media-1.freecodecamp.org/images/nhkde41r7VxTDjRtIB0qc-ry3jugObDiqfWE)

### 3.6 Conclusion

Awesome, we’re getting going now. By the end of **Section 3** we’ve completed the following steps:

* Installed Django REST Framework into our project
* Started building the `books` API
* Created a `serializer` for books
* Created a `view` for books
* Created `URLs` for books
* Browsed the books API that returns book data from the back end

![Image](https://cdn-media-1.freecodecamp.org/images/QeaabxrQLyzXfW30akDR1qeTrjxVyXUZ4dez)
_Gift from the gods_

### Section 4: Laying Down Front-end Foundations

In this section we shift our attention to the front end and begin working with the Ember framework. We’ll install the required software, set up a basic DOM, styles, create the `book` model, and the `books` route. We’ll also load up fake book data for demonstration purposes before we go on to access real data from the back end.

### 4.1 Install Required Software

To begin front-end development we need to install some software:

* [Node.js, NPM](https://nodejs.org/en/)
* [Ember CLI](https://ember-cli.com/)

#### 4.1.1 NodeJS and NPM

NodeJS is an open source server environment. We don’t need to get into the details right now. NPM is a package manager for Node.js packages. We use it to install packages like the Ember CLI.

Install NodeJS and NPM using the [installation file from the official site](http://nodejs.org/en/download/).

Once installation is complete check that everything installed:

```
node --version
npm --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/hEqfcvp-GnAp2OUfgwCUCBON6UN0fDoovaJu)

#### 4.1.2 Ember CLI

Let’s use NPM to install the Ember CLI. That’s the ‘_official command line utility used to create, build, serve, and test [Ember.js](https://emberjs.com/) apps and addons_’. Ember CLI comes with all the tools we need to build the front end of our application.

```
# install Ember CLI
  npm install -g ember-cli
# check that it's installed
  ember --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/6hklopSfXA8qI9ssI6yPxWmES2K2oF40a-Xm)

### 4.2 Start an Ember Project: client

Let’s create a front end client called `client` using Ember CLI:

```
# cd into the main project folder
  cd ~/desktop/my_library
# create a new app: client
  ember new client
# cd into the directory
  cd client
# run the server
  ember s
```

Head over to `http://localhost:4200` and you should see this screen:

![Image](https://cdn-media-1.freecodecamp.org/images/9CdYwMxZs608uCFDtckD2hupL4IKrcfI1Ehz)
_Up and running_

The base Ember client project is running as expected. You can shut down the server with `ctrl+C`.

#### 4.2.1 Update .gitignore with Ember exclusions

Before we make any new commits, let’s update the `.gitignore` file. We want to exclude unwanted files from from the repo. Add on to the file below the Django section:

```
...
### Ember ###
/client/dist
/client/tmp
# dependencies
/client/node_modules
/client/bower_components
# misc
/client/.sass-cache
/client/connect.lock
/client/coverage/*
/client/libpeerconnection.log
/client/npm-debug.log
/client/testem.log
# ember-try
/client/.node_modules.ember-try/
/client/bower.json.ember-try
/client/package.json.ember-try
```

### 4.3 Displaying books data

#### 4.3.1 Setup the DOM

Now that we’ve generated a base project, let’s set up a basic DOM and styles. I’m not doing anything fancy here. It’s the least necessary to have our data displaying in a readable format.

Locate the file `client/app/templates/application.hbs`. Get rid of `{{welcome-page}}` and the comments .

Next, create a `div` with the class `.nav`. Use Ember’s built-in `[{{#link-to}}](https://guides.emberjs.com/release/templates/links/)` helper to create a link to the route `books`(we’ll create it later):

```html
<div class="nav">
  {{#link-to 'books' class="nav-item"}}Home{{/link-to}}
</div>
```

Wrap everything including the`[{{outlet}}](https://guides.emberjs.com/release/routing/rendering-a-template/)` in a `div` with the `.container` class. Each route template will render inside `{{outlet}}`:

```html
<div class="container">
  <div class="nav">
    {{#link-to 'books' class="nav-item"}}Home{{/link-to}}
  </div>
{{outlet}}
</div>
```

This is the template for the parent level `application` route. any sub-routes like `books` will render inside the `{{outlet}}`. This means that the `nav` will always be visible on screen.

#### 4.3.2 Create styles

I’m not going to get into the nitty-gritty of the CSS. It’s pretty simple to figure out. Locate the file `client/app/styles/app.css` and add the following styles:

**Variables and Utilities**

```css
:root {
  --color-white:  #fff;
  --color-black:  #000;
  --color-grey:   #d2d2d2;
  --color-purple: #6e6a85;
  --color-red:    #ff0000;
  --font-size-st: 16px;
  --font-size-lg: 24px;
  --box-shadow: 0 10px 20px -12px rgba(0, 0, 0, 0.42),
                0 3px  20px  0px  rgba(0, 0, 0, 0.12),
                0 8px  10px -5px  rgba(0, 0, 0, 0.2);
}
.u-justify-space-between {
  justify-content: space-between !important;
}
.u-text-danger {
  color: var(--color-red) !important;
}
```

**General**

```css
body {
  margin: 0;
  padding: 0;
  font-family: Arial;
}
.container {
  display: grid;
  grid-template-rows: 40px calc(100vh - 80px) 40px;
  height: 100vh;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/5XDkBqqpQcV7KXyA9HFpXOMED7ISf-wTnlhR)

**Navigation**

```css
.nav {
  display: flex;
  padding: 0 10px;
  background-color: var(--color-purple);
  box-shadow: var(--box-shadow);
  z-index: 10;
}
.nav-item {
  padding: 10px;
  font-size: var(--font-size-st);
  color: var(--color-white);
  text-decoration: none;
}
.nav-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/vNzYqMngN91hTgUYcAqWpW01vkaJDBGTWGJ7)

**Headings**

```css
.header {
  padding: 10px 0;
  font-size: var(--font-size-lg);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/UKbiWepf0IEUTAjL-9JuR8MUa6zO3HxkCpvU)

**Books List**

```css
.book-list {
  padding: 10px;
  overflow-y: scroll;
}
.book {
  display: flex;
  justify-content: space-between;
  padding: 15px 10px;
  font-size: var(--font-size-st);
  color: var(--color-black);
  text-decoration: none;
  cursor: pointer;
}
.book:hover {
  background: var(--color-grey);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/rcfJhkZZS1D0wxCyxIC9X9jc6BkLnsVAMlWJ)

**Buttons**

```
button {
  cursor: pointer;
}
```

**Book Detail**

```css
.book.book--detail {
  flex-direction: column;
  justify-content: flex-start;
  max-width: 500px;
  background: var(--color-white);
  cursor: default;
}
.book-title {
  font-size: var(--font-size-lg);
}
.book-title,
.book-author,
.book-description {
  padding: 10px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/-8Ss5ml2SZVM6ZLhROuRXIFeMeMVOxER164L)

**Add/Edit Book Form**

```css
.form {
  display: flex;
  flex-direction: column;
  padding: 10px 20px;
  background: var(--color-white);
}
input[type='text'],
textarea {
  margin: 10px 0;
  padding: 10px;
  max-width: 500px;
  font-size: var(--font-size-st);
  border: none;
  border-bottom: 1px solid var(--color-grey);
  outline: 0;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/pdj99DtnkIaB4-7xbtKk1AIbxBUiWt2LOSr-)

**Actions**

```css
.actions {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding: 10px 20px;
  background-color: var(--color-white);;
  box-shadow: var(--box-shadow)
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/KpvfySOayj7YVPKjEmFUV5uZIOTC1Z3YUTmO)

### 4.4 The books route

#### **4.4.1 Create the books route**

Now we have our styles and container DOM in place. Let’s generate a new route that will display all the books in our database:

```
ember g route books
```

The router file `client/app/router.js` updates with:

```js
import EmberRouter from '@ember/routing/router';
import config from './config/environment';
const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});
Router.map(function() {
  this.route('books');
});
export default Router;
```

#### **4.4.2 Load fake data in the model hook**

Let’s edit the books route `client/app/routes/books.js` to load all books from the database.

```js
import Route from '@ember/routing/route';
export default Route.extend({
  model() {
    return [
      {title: 'Monkey Adventure'},
      {title: 'Island Strife'},
      {title: 'The Ball'},
      {title: 'Simple Pleasures of the South'},
      {title: 'Big City Monkey'}
    ]
  }
});
```

The model hook is returning an array of objects. This is fake data for demonstration purposes. We’ll come back here later and load the actual data from the database using Ember Data when we’re ready.

#### **4.4.3 Update the books route template**

Let’s edit the books route template `client/app/templates/books.hbs`. We want to display the books returned in the model.

```html
<div class="book-list">
  {{#each model as |book|}}
    <div class="book">
      {{book.title}}
    </div>
  {{/each}}
</div>
```

Ember uses the [Handlebars Template Library](https://guides.emberjs.com/release/templates/handlebars-basics/). Here we use the `each` helper to iterate through our array of books data in `model`. We wrap each of the items in the array in a `div` with the class `.book`. Access and display it’s title information with `{{book.title}}`.

#### 4.4.4 Demonstration: books route loading and displaying fake data

Now that we have the DOM, `book` model, and `books` route setup with some fake data we can see this running in the browser. Take a look at `localhost:4200/books`:

![Image](https://cdn-media-1.freecodecamp.org/images/Q9NHnr2xZN1Sv556vGJrBaaH-zmpHo8-qFpn)
_Mouse over a book title to highlight_

#### 4.4.5 Create application route for redirect

It’s kind of annoying to have to put a `/books` to visit the `books` route. Let’s generate the `application` route. We can use the `redirect` hook to redirect to the `books` route when we enter the base route `/`.

```
ember g route application
```

If prompted to overwrite the `application.hbs` template, say no. We don’t want to overwrite the template we already set up.

In `client/app/routes/application.js` create the `redirect` hook:

```js
import Route from '@ember/routing/route';
export default Route.extend({
  redirect() {
    this.transitionTo('books');
  }
});
```

Now, if you visit `localhost:4200` it will redirect to `localhost:4200/books`.

![Image](https://cdn-media-1.freecodecamp.org/images/Tkc46qrVylMjB6TuKWMePLOGYLaYPB7TUKc2)

### 4.5 Displaying real data in the books route

#### 4.5.1 Create an application adapter

We don’t want to use fake data forever. Let’s connect to the back end using an [adapter](https://www.emberjs.com/api/ember-data/release/classes/DS.Adapter) and start pulling the books data into the client. Think of the adapter as an “_object that receives requests from a store’._ It _‘translates them into the appropriate action to take against your persistence layer…’_

Generate a new application adapter:

```
ember g adapter application
```

Locate the file `client/app/adapters/application.js` and update it:

```js
import DS from 'ember-data';
import { computed } from '@ember/object';
export default DS.JSONAPIAdapter.extend({
  host: computed(function(){
    return 'http://localhost:8000';
  }),
  namespace: 'api'
});
```

The JSONAPIAdapter is the ‘_default adapter used by Ember Data_’. It transforms the store’s requests into HTTP requests that follow the [JSON API](http://jsonapi.org/format/) format. It plugs into the data management library called [Ember Data](https://github.com/emberjs/data). We use Ember Data to interface with the back end in a more efficient way. It can store and manage data in the front end and make requests to the back end when required. This means minor page updates don’t need constant requests to the back end. This helps the user experience feel more fluid with generally faster loading times

We’ll use its `store` service to access `server` data without writing more complex `ajax` requests. These are still necessary for more complex use cases though.

Here the adapter is telling Ember Data that its `host` is at `localhost:8000`, namespaced to `api`. This means that any requests to the server start with `http://localhost:8000/api/`.

![Image](https://cdn-media-1.freecodecamp.org/images/4lhfnmvPDvGNC0229Z2VqfVVNyn4W5hd4YVs)
_The full stack_

#### 4.5.2 Create the book model

Ember Data has particular requirements for mapping its data to what comes from the back end. We’ll generate a `book` model so it understands what the data coming from the back end should map to:

```
ember g model book
```

Locate the file in `client/models/book.js` and define the `book` model:

```js
import DS from 'ember-data';
export default DS.Model.extend({
  title: DS.attr(),
  author: DS.attr(),
  description: DS.attr()
});
```

The attributes are the same as those we’ve defined in the back end. We define them again so that Ember Data knows what to expect from the structured data.

#### 4.5.3 Update the `books` route

Let’s update the books route by importing the `store` service and using it to request data.

```js
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
export default Route.extend({
  store: service(),
  model() {
    const store = this.get('store');
    return store.findAll('book');
  }
});
```

#### 4.5.4 Demonstration: books has a CORS issue

So far we’ve created an application adapter and updated the `books` route to query for all books in the database. Let’s see what we’re getting back.

Run both the Django and Ember servers. Then visit `localhost:4200/books` and you should see this in the console:

![Image](https://cdn-media-1.freecodecamp.org/images/YofsmuPXJQOamQVnPvs-0dJnGEvCl8LfWure)

There seems to be a problem with CORS.

#### 4.5.5 Resolve the Cross-Origin Resource Sharing (CORS) issue

CORS defines a way in which browser and server interact to determine whether it’s safe to allow a request. We’re making a cross-origin request from `localhost:4200` to `localhost:8000/api/books`. From the client to the server with the purpose of accessing our books data.

Currently, the front end isn’t an allowed origin to request data from our back-end endpoints. This block is causing our error. We can resolve this issue by allowing requests to pass through.

Begin by installing an app that adds CORS headers to responses:

```
pip install django-cors-headers
```

Install it into `server`'s `settings.py` file under the `INSTALLED_APPS` array:

```
INSTALLED_APPS = [
...
    'books',
    'corsheaders'
]
```

Add it to the top of the `MIDDLEWARE` array:

```
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
...
]
```

Finally, allow all requests to get through during development:

```
CORS_ORIGIN_ALLOW_ALL = DEBUG
```

#### 4.5.6 Demonstration: CORS issue resolved, incompatible data format

Visit `localhost:4200` and you should see this in the console:

![Image](https://cdn-media-1.freecodecamp.org/images/0klx5kEzDhADK2vxluljOK1uArhWk4PuuPF9)

Looks like we solved the CORS issue and we’re receiving a response from `server` with the data that we expect:

```json
[
    {
        "id": 1,
        "title": "Conquistador",
        "author": "Buddy Levy",
        "description": "It was a moment unique in ..."
    },
    {
        "id": 2,
        "title": "East of Eden",
        "author": "John Steinbeck",
        "description": "In his journal, Nobel Prize ..."
    }
]
```

Although get an array of objects in JSON format, it’s still not in the format we want it to be. This is what Ember Data expects:

```json
{
  data: [
    {
      id: "1",
      type: "book",
      attributes: {
        title: "Conquistador",
        author: "Buddy Levy",
        description: "It was a moment unique in ..."
      }
    },
    {
      id: "2",
      type: "book",
      attributes: {
        title: "East of Eden",
        author: "John Steinbeck",
        description: "In his journal, Nobel Prize ..."
      }
    }
  ]
}
```

Close but not quite there yet.

![Image](https://cdn-media-1.freecodecamp.org/images/pBr8ZzZtGrBW-ubnBWvlfwv-7tEkxpIxlrV3)

### 4.6 Conclusion

We’ve completed the following steps in **Section 4**:

* Installed NodeJS and NPM
* Installed the Ember CLI and created a new client project
* Basic DOM setup
* Created a `books` route and template to load and display books
* Demonstrated the app running with fake data
* Created an application adapter to connect to the back end and receive data
* Created a `book` model and updated the `books` route to capture back-end data
* Demonstrated that the back-end data isn’t structured in the way that Ember Data expects it to be

![Image](https://cdn-media-1.freecodecamp.org/images/zRshD6WOw8j2R4PwhMmm4eBJ650PkDGWI9lP)
_This one’s mine_

### Section 5: Correct data formats, deal with individual records

In this section we’ll use the Django REST Framework JSON API to structure the data in a way that Ember Data can work with. We’ll also update the `books` API to return book a single instance of a book record. We’ll also add the functionality to add, edit, and create books. Then we’re done with our application!

### 5.1 Install the Django REST Framework JSON API

First we use pip to install the [Django REST Framework JSON API](https://github.com/django-json-api/django-rest-framework-json-api) (DRF). It will transform regular DRF responses into an `identity` model in [JSON API format](http://jsonapi.org/format/#document-resource-object-identification).

With the virtual environment enabled:

```
# install the Django REST Framework JSON API
  pip install djangorestframework-jsonapi
```

Next, update DRF settings in `server/server/settings.py`:

```
REST_FRAMEWORK = {
  'PAGE_SIZE': 100,
  
  'EXCEPTION_HANDLER': 
    'rest_framework_json_api.exceptions.exception_handler',
  
  'DEFAULT_PAGINATION_CLASS':    'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
'DEFAULT_PARSER_CLASSES': (
    'rest_framework_json_api.parsers.JSONParser',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser'
  ),
'DEFAULT_RENDERER_CLASSES': (
    'rest_framework_json_api.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
   ),
'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
'DEFAULT_FILTER_BACKENDS': (
     'rest_framework.filters.OrderingFilter',
    ),
'ORDERING_PARAM': 'sort',
   
   'TEST_REQUEST_RENDERER_CLASSES': (
     'rest_framework_json_api.renderers.JSONRenderer',
    ),
   
   'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}
```

These override the default settings for DRF with defaults from the JSON API. I increased the `PAGE_SIZE` so we can get up to 100 books back in a response.

### 5.2 Working with individual book records

#### 5.2.1 Create a view

Let’s also update our `books` API so that we can retrieve single instances of a book record.

Create a new view called`bookRudView` in `server/books/api/views.py`:

```py
class bookRudView(generics.RetrieveUpdateDestroyAPIView):
  resource_name       = 'books'
  lookup_field        = 'id'
  serializer_class    = bookSerializer
  def get_queryset(self):
    return Book.objects.all()
```

This view uses the `id` `lookup_field` to retrieve an individual book record. The [RetrieveUpdateDestroyAPIView](http://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview) provides basic `GET`, `PUT`, `PATCH` and `DELETE` method handlers. As you might imagine these let us create, update, and delete individual book data.

#### 5.2.2 Update the book API URLs

We’ll need to create a new URL pattern that delivers data through the `bookRudView`.

```py
from .views import bookAPIView, bookRudView
from django.conf.urls import url
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
  url(r'^(?P<id>\d+)', bookRudView.as_view(), name='book-rud')
]
```

Import `bookRudView`, match it to the pattern `r'^(?P<id>`;\d+)', and give it the name `book-rud`.

#### 5.2.3 Update the server URLs

Finally, update the `books` API URL pattern in `server/server/urls.py`. We want to match to patterns which begin after `books/`:

```
...
urlpatterns = [
  ...
  url(r'^api/books/?', include('books.api.urls', namespace='api-books')),
]
```

#### 5.2.4 Demonstration: Access a single book record

Now if you visit `localhost:8000/api/books/1` it should display a single book record that matches to a book’s `id`:

![Image](https://cdn-media-1.freecodecamp.org/images/CUK0sNAqhaAp-aYXHTN0o-gCCToOtM4gUg3z)

Notice that we have access to the `DELETE`, `PUT`, `PATCH` and other methods. These come with `RetrieveUpdateDestroyAPIView`.

#### 5.2.5 Demonstration: Capturing and displaying data from the back end in the correct format

With the `JSONAPI` installed the back end should be sending back responses Ember can work with. Run both servers and visit `localhost:4200/books`. We should get back real data from the back end and have the route display it. Success!

![Image](https://cdn-media-1.freecodecamp.org/images/9RQ7BOzrDZuruIw65IraJFmkz9DlN0WJ0bw5)
_Capturing and displaying data from the back end_

Take a look at the response coming through. It’s in the valid `JSONAPI` format that Ember Data works with.

![Image](https://cdn-media-1.freecodecamp.org/images/Hz-SsH8c5UYq6InAy1jeCxwgNlHnMQ4AJ58L)

![Image](https://cdn-media-1.freecodecamp.org/images/PIGhJY1TrhBHlHDRfzeKcev5qvR1XX9aP62C)

### 5.3 The book Route

We can now view the list of books from our database in the `books` route. Next, let’s create a new route in the front-end `client`. It will display individual books in detail with `title`, `author`, and `description` data.

#### 5.3.1 Create the `book` route

Generate a new route for the individual book page:

```
ember g route book
```

In `router.js` update the new route with the path `‘books/:book_id’`. This overrides the default path and takes in a `book_id` parameter.

```
...
Router.map(function() {
  this.route('books');
  this.route('book', { path: 'books/:book_id' });
});
...
```

Next update the `book` route `client/app/routes/book.js` to retrieve a single book record from the database:

```
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
export default Route.extend({
  store: service(),
model(book) {
    return this.get('store').peekRecord('book', book.book_id);
  }
});
```

As outlined in `router.js` the `book` route takes in the `book_id` parameter. The parameter goes into the route’s `model` hook and we use it to retrieve the book with the Ember Data `store`.

#### 5.3.2 Update the `book` template

Our `client/app/templates/book.hbs` template should display the book data we get back from the `store`. Get rid of `{{outlet}}` and update it:

```html
<div class="book book--detail">
  <div class="book-title">
    {{model.title}}
  </div>
  <div class="book-author">
    {{model.author}}
  </div>
  <div class="book-description">
    {{model.description}}
  </div>
</div>
```

Like in the `books` template we access the `model` attributes using [dot notation](https://codeburst.io/javascript-quickie-dot-notation-vs-bracket-notation-333641c0f781).

#### 5.3.3 Update the `books` template

Finally, let’s update the `books` template. We want to link to each individual book page as displayed in the `book` route we created:

```html
<div class="book-list">
  {{#each model as |book|}}
    {{#link-to 'book' book.id class="book"}}
      {{book.title}}
    {{/link-to}}
  {{/each}}
</div>
```

Wrap the `book.title` with the `link-to` helper. It works like this:

* creates a link to the `book` route
* takes in the `book.id` as a parameter
* takes a `class` to style the `<`;a> tag generated in the DOM.

#### 5.3.4 Demonstration: Select book to view detailed information

Now check out `localhost:4200/books`. We can click on our books to get a detailed view. Sweet!

![Image](https://cdn-media-1.freecodecamp.org/images/hyC6r85lGgPWSydWXWcCppI10y0v0yo4-1sC)

![Image](https://cdn-media-1.freecodecamp.org/images/kfuloJ1VtO6CV09r3CsY-2Gcl9Dd3ts8kt3G)

### 5.4 Conclusion

We’ve come to the end of **Section 5** with the following steps completed:

* Identified the problem with the data coming from Django
* Installed the Django REST Framework JSON API
* Updated the `books` route template
* Created the `book` route and template

![Image](https://cdn-media-1.freecodecamp.org/images/MLAvJIJz8ChUSLcFJi4DFuVyMVcnlnzoMU87)
_Getting into the details now_

### Section 6: Functional Front end

In this section we’ll add the following functionality to the front-end experience:

* Add a new book with the fields title, author, and description
* Edit an existing book’s title, author, and description fields
* Delete an existing book

That’s all we have to do to complete the rest of our application. We come a long way. Let’s push on to the end!

### 6.1 Adding a new book to the database

We can now view all the books from the database and view individual book records in detail. It’s time to build the functionality to add a new book to the database. These are the steps we’ll take to make that happen:

* The `create-book` route handles the process of creating a new book and adding it to the database
* The `create-book` template will have a form with two inputs and a text area to take in a `title`, `author`, and `description`
* The `create-book` controller handles the data entered into the form

#### 6.1.1 Create the create-book route and controller

Generate the `create-book` route to handle new book creation:

```
ember g route create-book
```

Create a controller of the same name to hold form data:

```
ember g controller create-book
```

#### 6.1.2 Setup the `create-book` controller

In `client/app/controllers/create-book.js` create a computed property called `form`. It will return an object with our book data attributes. This is where we capture the new book data entered in by the user. It’s empty by default.

```js
import Controller from '@ember/controller';
import { computed } from '@ember/object';
export default Controller.extend({
  form: computed(function() {
    return {
      title: '',
      author: '',
      description: ''
    }
  })
});
```

#### 6.1.3 Setup the `create-book` route

In `client/app/routes/create-book.js` we do the following:

* create actions to confirm creation of a new book
* cancel the creation process
* use a route hook to clear the form data upon entering the route:

```js
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
export default Route.extend({
  store: service(),
  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.title', '');
    this.controller.set('form.author', '');
    this.controller.set('form.description', '');
  },
  actions: {
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');
      const newBook = store.createRecord('book', {
        title: form.title,
        author: form.author,
        description: form.description
      });
      newBook.save()
        .then(() => {
          this.transitionTo('books');
        });
     },
     cancel() {
       this.transitionTo('books');
     }
  }
});
```

The `setupController` hook allows us to reset the form’s values. This is so that they don’t persist when we go back and forth through pages. We don’t want to click away to another page without having completed the create book process. If we do, we’ll come back to see the unused data still sitting in our form.

The `create()` action will take the form data and create a new record with the Ember Data `store`. It then persists it to the Django back end. Once complete it will transition the user back to the `books` route.

The `cancel` button transitions the user back to the `books` route.

#### 6.1.4 Setup the `create-book` template

Next, in `client/app/template/create-book.hbs` we build the form:

```html
<form class="form">
  <div class="header">
    Add a new book
  </div>
  {{input
    value=form.title
    name="title"
    placeholder="Title"
    autocomplete='off'
  }}
  {{input
    value=form.author
    name="author"
    placeholder="Author"
    autocomplete='off'
  }}
  {{textarea
    value=form.description
    name="description"
    placeholder="Description"
    rows=10
  }}
</form>
<div class="actions">
  <div>
    <button {{action 'create'}}>
      Create
    </button>
    <button {{action 'cancel'}}>
      Cancel
    </button>
  </div>
</div>
```

The `form` uses the built-in `{{input}}` helpers to:

* take in values
* display placeholders
* turn autocomplete off.

The `{{text}}` area helper works in a similar way, with the addition of the number of rows.

The actions `div` contains the two buttons to create and cancel. Each button ties to its namesake action using the `{{action}}` helper.

#### 6.1.5 Update the `books` route template

The final piece of the create book puzzle is to add a button in the `books` route. It will get us into the `create-book` route and begin creating a new book.

Add on to the bottom of `client/app/templates/books.hbs`:

```
...
{{#link-to 'create-book' class='btn btn-addBook'}}
  Add Book
{{/link-to}}
```

#### 6.1.6 Demonstration: Can add a new book

Now if we go back and try to create a new book again we’ll find success. Click into the book to see a more detailed view:

![Image](https://cdn-media-1.freecodecamp.org/images/8ktkFGXqUnl-f3OtzVczYW5Oa4JlfrhEv7Ev)
_Adding a new book to the library_

![Image](https://cdn-media-1.freecodecamp.org/images/7JlRVM4oznuSb0K7FKRdCInNKKVeGOFcy0VS)
_New book created and displayed_

![Image](https://cdn-media-1.freecodecamp.org/images/BUdQmE0HUaMn9xhRvWXR7GI0jU-NlXu8SmzW)

### 6.2 Deleting a book from the database

Now that we can add books to the database we should be able to delete them too.

#### 6.2.1 Update the `book` route template

First update the `book` route’s template. Add on under `book book--detail`:

```html
...
<div class="actions {{if confirmingDelete
                         'u-justify-space-between'}}">
  {{#if confirmingDelete}}
    <div class="u-text-danger">
      Are you sure you want to delete this book?
    </div>
    <div>
      <button {{action 'delete' model}}>Delete</button>
      <button {{action (mut confirmingDelete)false}}>
        Cancel
      </button>
    </div>
  {{else}}
    <div>
      <button {{action (mut confirmingDelete) true}}>Delete</button>
    </div>
  {{/if}}
</div>
```

The `actions` `div` contains the buttons and text for the book deletion process.

We have a `bool` called `confirmingDelete` which will be set on the route’s `controller`. `confirmingDelete` adds the `.u-justify-space-between` utility class on `actions` when it’s `true`.

When it’s true, it also displays a prompt with the utility class `.u-text-danger`. This prompts the user to confirm deletion of the book. Two buttons show up. One to run `delete` action in our route. The other uses the `mut` helper to flip `confirmingDelete` to `false`.

When `confirmingDelete` is `false` (the default state) a single `delete` button display. Clicking it flips `confirmingDelete` to `true`. This then displays the prompt and the other two buttons.

#### 6.2.2 Update the `book` route

Next update the `book` route. Under the `model` hook add:

```
setupController(controller, model) {
  this._super(controller, model);
  this.controller.set('confirmingDelete', false);
},
```

In `setupController` we call `this._super()`. This is so the controller goes through its usual motions before we do our business. Then we set `confirmingDelete` to `false`.

Why do we do this? Let’s say we start to delete a book, but leave the page without either cancelling the action or deleting the book. When we go to any book page `confirmingDelete` would be set to `true` as a leftover.

Next let’s create an `actions` object that will hold our route actions:

```
actions: {
  delete(book) {
    book.deleteRecord();
    book.save().then(() => {
      this.transitionTo('books');
    });
  }
}
```

The `delete` action as referenced in our template takes in a `book`. We run `deleteRecord` on the `book` and then `save` to persist the change. Once that promise completes `transitionTo` transitions to the `books` route (our list view).

#### 6.2.3 Demonstration: Can delete an existing book

Let’s check this out in action. Run the servers and select a book you want to delete.

![Image](https://cdn-media-1.freecodecamp.org/images/X3g8JcJt5Gh7OfgE4G3JPvszzlEE902n8BJK)
_Delete button visible when confirmingDelete is false_

![Image](https://cdn-media-1.freecodecamp.org/images/VsfnqMVBFAce2azSvhDa1kIkBKYSzZ68RhIk)
_Prompt to confirm deletion of book when confirmingDelete is true_

When you delete the book it redirects to the `books` route.

![Image](https://cdn-media-1.freecodecamp.org/images/9OqjwQPyAxDXv9JCgoYGYpF8ARv6WZd-DK4h)

### 6.3 Editing a book in the database

Last but not least we’ll add the functionality to edit an existing books information.

#### 6.3.1 Update the `book` route template

Open up the `book` template and add a form to update book data:

```html
{{#if isEditing}}
  <form class="form">
    <div class="header">Edit</div>
    {{input
      value=form.title
      placeholder="Title"
      autocomplete='off'
    }}
    {{input
      value=form.author
      placeholder="Author"
      autocomplete='off'
    }}
    {{textarea
      value=form.description
      placeholder="Description"
      rows=10
    }}
  </form>
  <div class="actions">
    <div>
      <button {{action 'update' model}}>Update</button>
      <button {{action (mut isEditing) false}}>Cancel</button>
    </div>
  </div>
{{else}}
  ...
  <div>
    <button {{action (mut isEditing) true}}>Edit</button>
    <button {{action (mut confirmingDelete) true}}>Delete</button>
  </div>
  ...
{{/if}}
```

First let’s wrap the entire template in an `if` statement. This corresponds to the `isEditing` property which by default will be `false`.

Notice that the form is very almost identical to our create book form. The only real difference is that the actions `update` runs the `update` action in the `book` route. The `cancel` button also flips the `isEditing` property to `false`.

Everything we had before gets nested inside the `else`. We add the `Edit` button to flip `isEditing` to true and display the form.

#### 6.3.2 Create a `book` controller to handle form values

Remember the `create-book` controller? We used it to hold the values that’s later sent to the server to create a new book record.

We’ll use a similar method to get and display the book data in our `isEditing` form. It will pre-populate the form with the current book’s data.

Generate a book controller:

```
ember g controller book
```

Open `client/app/controllers/book.js` and create a `form` computed property like before. Unlike before we’ll use the `model` to pre-populate our form with the current `book` data:

```js
import Controller from '@ember/controller';
import { computed } from '@ember/object';
export default Controller.extend({
  form: computed(function() {
    const model = this.get('model');
    return {
      title: model.get('title'),
      author: model.get('author'),
      description: model.get('description')
    }
  })
});
```

#### 6.3.3 Update the `book` route

We’ll have to update our route again:

```js
setupController(controller, model) {
  ...
  this.controller.set('isEditing', false);
  this.controller.set('form.title', model.get('title'));
  this.controller.set('form.author', model.get('author'));
  this.controller.set('form.description', model.get('description'));
},
```

Let’s add on to the `setupController` hook. Set `isEditing` to `false` and reset all the form values to their defaults.

Next let’s create the `update` action:

```js
actions: {
  ...
  update(book) {
    const form = this.controller.get('form');
    book.set('title', form.title);
    book.set('author', form.author);
    book.set('description', form.description);
    book.save().then(() => {
      this.controller.set('isEditing', false);
    });
  }
}
```

It’s pretty straightforward. We get the form values, set those values on the `book` and persist with `save`. Once successful we flip `isEditing` back to `false`.

#### 6.3.4 Demonstration: Can edit information of an existing book

![Image](https://cdn-media-1.freecodecamp.org/images/xMgtmxnN122AZPurNoIFRX3QyQ6WVR909YOc)
_Edit button to toggle the isEditing controller property_

![Image](https://cdn-media-1.freecodecamp.org/images/XBlE7hYhZIyRzAhbtDVBPMUFy3ZNJseyVU6p)
_Form pre-populated with book’s current information_

![Image](https://cdn-media-1.freecodecamp.org/images/r5A-y2Xi4sDOwQrza0ClHizr5VNmXbloXM58)
_Book updated with new information_

![Image](https://cdn-media-1.freecodecamp.org/images/jHXRFAZRrJLz3vqbqdsmxPCYsYVOrxu2qogA)

### 6.4 Conclusion

We’ve completed the following steps by the end of **Section 6**:

* Identified the problem with the data coming from Django
* Installed JSON API into Django
* Updated the Books Route Template
* Created the book detail route and template
* Can view, add, edit, and delete database records from the EmberJS client

**That’s it. We’ve done it! We built a very basic full stack application using Django and Ember.**

Let’s step back and think about what we’ve built for a minute. We have an application called `my_library` that:

* lists books from a database
* allows users to view each book in more detail
* add a new book
* edit an existing book
* delete a book

As we built the application we learned about Django and how it’s used to administer the database. We created models, serializers, views, and URL patterns to work with the data. We used Ember to create a user interface to access and change the data through the API endpoints.

![Image](https://cdn-media-1.freecodecamp.org/images/KTyH3U0QWUOf8LUEIgKEXovuO8gabreUhKHN)
_Phew_

### Section 7: Moving On

### 7.1 What’s Next

If you’ve gotten this far, you’ve finished the tutorial! The application is running with all the intended functionality. That’s a lot to be proud of. Software development, complicated? That’s an understatement. It can feel downright inaccessible even with all the resources available to us. I get that feeling all the time.

What works for me is to take frequent breaks. Get up and walk away from what you’re doing. Do something else. Then get back and break down your problems step by step into the smallest units. Fix and refactor until you get to where you want to be. There are no shortcuts to building your knowledge.

Anyways, we’ve might have done a lot here for an introduction but we’re only scratching the surface. There is plenty more for you to learn about full stack development. Here are some examples to think about:

* user accounts with authentication
* testing functionality of the application
* deploying the application to the web
* writing the REST API from scratch

When I have time I’ll look into writing more on these topics myself.

I hope you found this tutorial useful. It’s intended to serve as a jump-off point for you to learn more about Django, Ember and full stack development. It was definitely a learning experience for me. **Shoutout to my [Closing Folders](http://closingfolders.com/) team for the support and encouragement. We’re hiring now so feel free to get in touch!**

If you’d like to reach out you can contact me through the following channels:

* [email](mailto:michael.xavier@closingfolders.com)
* [linkedIn](https://www.linkedin.com/in/vinothmichaelxavier/)
* [medium](https://medium.com/@sunskyearthwind)
* [personal website](https://lookininward.github.io/)

### 7.2 Further Reading

Writing this tutorial forced me confront the edges of my knowledge. Here are the resources that helped with my comprehension of the topics covered:

[What is a full stack programmer?](http://qr.ae/TUIx4x)  
[What is a web application?](https://stackoverflow.com/a/8694944/5513243)  
[What is Django?](https://tutorial.djangogirls.org/en/django/)  
[What is EmberJS?](https://hacks.mozilla.org/2014/02/ember-js-what-it-is-and-why-we-need-to-care-about-it/)  
[What is version control?](https://www.atlassian.com/git/tutorials/what-is-version-control)  
[What is Git?](https://medium.com/swlh/git-as-the-newbies-learning-steroid-963a2146220b)  
[How do I use Git with Github?](http://rogerdudler.github.io/git-guide/)  
[How do I create a Git repository?](https://help.github.com/articles/create-a-repo/)  
[How do I add a Git remote?](https://help.github.com/articles/adding-a-remote/)  
[What is a model?](https://docs.djangoproject.com/en/1.11/topics/db/models/)  
[What is a view?](https://docs.djangoproject.com/en/1.11/topics/http/views/)  
[What is a superuser?](https://docs.djangoproject.com/en/1.11/ref/django-admin/#createsuperuser)  
[What is making a migration?](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-makemigrations)  
[What is migrating?](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)  
[What is SQLite?](https://www.sqlite.org/about.html)  
[JSON Python Parsing: A Simple Guide](https://www.makeuseof.com/tag/json-python-parsing-simple-guide/)  
[How to secure API keys](https://medium.freecodecamp.org/how-to-securely-store-api-keys-4ff3ea19ebda)  
[What is Python?](https://www.python.org/doc/essays/blurb/)  
[What is pip?](https://en.wikipedia.org/wiki/Pip_(package_manager))  
[What is virtualenv?](https://virtualenv.pypa.io/en/stable/)  
[Best practices for virtualenv and git repo](http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html)  
[What is an API?](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82)  
[What are API endpoints?](https://smartbear.com/learn/performance-monitoring/api-endpoints/)  
[What is the Django REST Framework?](http://www.django-rest-framework.org/)  
[What is __init__.py?](https://stackoverflow.com/a/448279/5513243)  
[What is a serializer?](http://www.django-rest-framework.org/api-guide/serializers/)  
[What are views?](https://docs.djangoproject.com/en/1.11/topics/http/views/)  
[What are URLS?](https://tutorial.djangogirls.org/en/django_urls/)  
[What is JSON?](https://www.w3schools.com/js/js_json_intro.asp)  
[What are regular expressions?](https://www.tutorialspoint.com/python/python_reg_expressions.htm)  
[What does __init__.py do?](https://stackoverflow.com/questions/448271/what-is-init-py-for/448279#448279)  
[What is REST?](http://rest.elkstein.org/)  
[What is Node.js?](https://www.w3schools.com/nodejs/nodejs_intro.asp)  
[What is NPM?](https://www.w3schools.com/nodejs/nodejs_npm.asp)  
[What is EmberJS?](https://hacks.mozilla.org/2014/02/ember-js-what-it-is-and-why-we-need-to-care-about-it/)  
[What is Ember CLI?](https://ember-cli.com/)  
[What is Ember-Data?](https://github.com/emberjs/data)  
[What is a model?](https://guides.emberjs.com/release/models/)  
[What is a route?](https://guides.emberjs.com/release/routing/)  
[What is a router?](https://guides.emberjs.com/release/routing/defining-your-routes/)  
[What is a template?](https://guides.emberjs.com/release/templates/handlebars-basics/)  
[What is an adapter?](https://www.emberjs.com/api/ember-data/release/classes/DS.Adapter)  
[What is the Django REST Framework JSON API?](https://github.com/django-json-api/django-rest-framework-json-api)  
[What is the JSON API format?](http://jsonapi.org/format/#document-resource-object-identification)  
[What is dot notation?](https://codeburst.io/javascript-quickie-dot-notation-vs-bracket-notation-333641c0f781)

