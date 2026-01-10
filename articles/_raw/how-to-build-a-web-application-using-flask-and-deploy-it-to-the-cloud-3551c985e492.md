---
title: How to build a web application using Flask and deploy it to the cloud
subtitle: ''
author: Salvador Villalon Jr
co_authors: []
series: null
date: '2018-08-28T15:04:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OrCZB4PxwGqppjkoIMzCaA.png
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Introduction

  In each section, I will show pieces of code for you to follow along. All the code
  used in the tutorial is available in this GitHub Repository.

  What is HTTP and What Does it Have to do with Flask?

  HTTP is the protocol for websites. The in...'
---

### **Introduction**

In each section, I will show pieces of code for you to follow along. All the code used in the tutorial is available in this [GitHub Repository](https://github.com/salvillalon45/SPGISummer2018-FlaskTutorial).

## What is HTTP and What Does it Have to do with Flask?

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is the protocol for websites. The internet uses it to interact and communicate with computers and servers. Let me give you an example of how you use it everyday.

When you type the name of a website in the address bar of your browser and you hit enter. What happens is that an HTTP request has been sent to a server.

For example, when I go to my address bar and type google.com, then hit enter, an HTTP request is sent to a Google Server. The Google Server receives the request and needs to figure how to interpret that request. The Google Server sends back an HTTP response that contains the information that my web browser receives. Then it displays what you asked for on a page in the browser.

### How is Flask involved?

We will write code that will take care of the server side processing. Our code will receive requests. It will figure out what those requests are dealing with and what they are asking. It will also figure out what response to send to the user.

To do all this we will use Flask.

## What is Flask?

![Image](https://cdn-media-1.freecodecamp.org/images/1SnE5y1jhzqsSoFvgFyWc4mRLXX-iuG2DPtm align="left")

\_\[Flask (A Python Microframework)\](http://flask.pocoo.org/" rel="noopener" target="*blank" title=")*

It makes the process of designing a web application simpler. Flask lets us focus on what the **users are requesting and what sort of response to give back.**

Learn more about [micro frameworks](https://en.wikipedia.org/wiki/Microframework).

## How Does a Flask App Work?

The code lets us run a basic web application that we can serve, as if it were a website.

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)
```

This piece of code is stored in our main.py.

**Line 1:** Here we are importing the Flask module and creating a Flask web server from the Flask module.

**Line 3: name means this current file**. In this case, it will be main.py. This current file will represent my web application.

We are creating an instance of the Flask class and calling it app. Here we are creating a new web application.

**Line 5:** It represents the default page. For example, if I go to a website such as “google.com/” with nothing after the slash. Then this will be the default page of Google.

![Image](https://cdn-media-1.freecodecamp.org/images/rl8hovE8cNuaTMh6X8S8y4LLYoAVTJ5uvSMh align="left")

*This is what the @app.route(“/”) will represent*

**Line 6–7**: When the user goes to my website and they go to the default page (nothing after the slash), then the function below will get activated.

**Line 9:** When you run your Python script, Python assigns the name “**main**” to the script when executed.

If we import another script, the **if statement will prevent other scripts from running.** When we run main.py, it will change its name to **main** and only then will that if statement activate.

**Line 10:** This will run the application. Having `debug=True` allows possible Python errors to appear on the web page. This will help us trace the errors.

### **Let’s Try Running main.py**

In your Terminal or Command Prompt go to the folder that contains your main.py. Then do `**py main.py**` or `**python main.py**`**.** In your terminal or command prompt you should see this output.

![Image](https://cdn-media-1.freecodecamp.org/images/QynmMfSb7CoZkeuyC38ZLrTuA5eHtTkSxb6n align="left")

The important part is where it says `Running on http://127.0.0.1:5000/`.

127.0.0.1 means this local computer. If you do not know the meaning of this (like I didn’t when I started — [this article is really helpful](https://whatismyipaddress.com/localhost)), the main idea is that 127.0.0.1 and localhost refer to this local computer.

Go to that address and you should see the following:

![Image](https://cdn-media-1.freecodecamp.org/images/3TazBO699jNj7C88MyFbf-jlqseyWRPL5N4X align="left")

*Congrats! You made a website with Flask!*

#### **More Fun with Flask**

Earlier you saw what happened when we ran main.py with one route which was app.route(“/”).

Let’s add more routes so you can see the difference.

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
```

In **lines 9–11**. we added a new route, this time to **/salvador.**

Now run the main.py again and go to [http://localhost:5000/salvador](http://localhost:5000/salvador).

![Image](https://cdn-media-1.freecodecamp.org/images/63Ib3PYx1He2Y0pRiH9As7OivEc-dBmsVdYE align="left")

So far we have been returning text. Let’s make our website look nicer by adding HTML and CSS.

## HTML, CSS, and Virtual Environments

### HTML and Templates in Flask

First create a new HTML file. I called mine **home.html.**

Here is some code to get you started.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
  </head>
  <body>
    <h1> My First Try Using Flask </h1>
    <p> Flask is Fun </p>
  </body>
</html>
```

#### **Important Point To Remember**

The Flask Framework looks for HTML files in a folder called **templates.** You **need to create a templates** folder and put all your HTML files in there.

![Image](https://cdn-media-1.freecodecamp.org/images/Ggzs2MzQiYmno0hkvLCbdj2-rWl4gzqkjZil align="left")

*Remember to always keep the main.py outside of your templates folder*

Now we need to change our main.py so that we can view the HTML file we created.

```py
from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
  We made two new changes
```

**Line 1:** We imported `render_template()` method from the flask framework. `render_template()` looks for a template (HTML file) in the templates folder. Then it will render the template for which you ask. Learn more about [render\_templates() function](http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates).

**Line 7:** We change the return so that now it returns `render_template(“home.html”)`. This will let us view our HTML file.

Now visit your localhost and see the changes: [http://localhost:5000/](http://localhost:5000/).

![Image](https://cdn-media-1.freecodecamp.org/images/YmVgj3pCcduDB6T5UBabraK-glrVPNGhc4R9 align="left")

### **Let’s add more pages**

Let’s create an **about.html** inside the **templates folder.**

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>About Flask</title>
  </head>
  <body>
    <h1> About Flask </h1>
    <p> Flask is a micro web framework written in Python.</p>
    <p> Applications that use the Flask framework include Pinterest,
      LinkedIn, and the community web page for Flask itself.</p>
  </body>
</html>
```

Let’s make a change similar to what we did before to our main.py.

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about)
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)
```

We made three new changes:

**Line 9:** Change the route to`"/about**"**`**.**

**Line 10:** Change the function so it is now `def about():`

**Line 11:** Change the return so that now it returns `render_template("about.html")`.

Now see the changes: [http://localhost:5000/about](http://localhost:5000/about).

![Image](https://cdn-media-1.freecodecamp.org/images/O1Oo1GXYO2LHnXRiz8-VmKuvpywABTV7MuVn align="left")

### Let’s Connect Both Pages with a Navigation

To connect both pages we can have a navigation menu on the top. We can use Flask to make the process of creating a navigation menu easier.

First, let’s create a **template.html.** This **template.html** will serve as a parent template. Our two child templates will inherit code from it.

```html
 <!DOCTYPE html>
<html lang="en" dir="ltr">
 <head>
   <meta charset="utf-8">
   <title>Flask Parent Template</title>
   <link rel="stylesheet" href="{{ url_for('static',     filename='css/template.css') }}">
 </head>
 <body>
    <header>
      <div class="container">
        <h1 class="logo">First Web App</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>
    
    {% block content %}
    {% endblock %}
    
 </body>
</html>
```

**Line 13–14:** We use the function called `url_for()`**.** It accepts the name of the function as an argument. Right now we gave it the name of the function. More information on [**url\_for() function**](http://flask.pocoo.org/docs/0.12/quickstart/#url-building)**.**

The two lines with the curly brackets will be **replaced by the content of home.html and about.html.** This will depend on the URL in which the user is browsing.

These changes allow the child pages (home.html and about.html) to connect to the parent (template.html). This allows us to not have to **copy the code for the navigation menu in the about.html and home.html.**

Content of about.html:

```javascript
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>About Flask</title>
  </head>
  <body>
    {% extends "template.html" %}
    {% block content %}
    
    <h1> About Flask </h1>
    <p> Flask is a micro web framework written in Python.</p>
    <p> Applications that use the Flask framework include Pinterest,
      LinkedIn, and the community web page for Flask itself.</p>
      
    {% endblock %}
  </body>
</html>
```

Content of home.html:

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
  </head>
  <body>
    {% extends "template.html" %}
    {% block content %}
    
    <h1> My First Try Using Flask </h1>
    <p> Flask is Fun </p>
    
    {% endblock %}
  </body>
</html>
```

Let’s try adding some CSS.

## Adding CSS to Our Website

### An important note to remember

In the same way as we created a folder called **templates** to store all our HTML templates, we need a folder called **static**.

In **static**, we will store our CSS, JavaScript, images, and other necessary files. That is why it is important that you should create a **CSS** **folder to store your stylesheets.** After you do this, your project folder should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/ui4uCQ2KhjEaJ1JQ71XgXwNIs5TkzPuaGU8W align="left")

### Linking our CSS with our HTML file

Our template.html is the one that links all pages. We can insert the code here and it will be applicable to all child pages.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Parent Template</title>
    
    <link rel="stylesheet" href="{{ url_for('static',    filename='css/template.css') }}">
    
</head>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">First Web App</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>
    
{% block content %}
{% endblock %}

 </body>
</html>
```

**Line 7:** Here we are giving the path to where the template.css is located.

Now see the changes: [http://localhost:5000/about](http://localhost:5000/about).

![Image](https://cdn-media-1.freecodecamp.org/images/kvI3GKRQwhuu2O2giyPZBvu2am63So7OLH32 align="left")

## Moving Forward with Flask and virtualenv

Now that you are familiar with using Flask, you may start using it in your future projects. One thing to always do is use virtualenv.

### Why use virtualenv?

You may use Python for others projects besides web-development.

Your projects might have different versions of Python installed, different dependencies and packages.

We use virtualenv to create an isolated environment for your Python project. This means that each project can have its own dependencies regardless of what dependencies every other project has.

### Getting started with virtualenv

First, run this command on your command prompt or terminal:

```bash
pip install virtualenv
```

Second, do the following:

```bash
virtualenv “name of virtual environment”
```

Here you can give a name to the environment. I usually give it a name of virtual. It will look like this: `virtualenv virtual`**.**

After setting up virtual environment, check your project folder. It should look like this. The virtual environment needs to be created in the **same directory where your app files are located.**

![Image](https://cdn-media-1.freecodecamp.org/images/nlsgTQVp9ZrBHudAD4yKWF7tywO5fsaiYvHq align="left")

*How the directory looks like*

### Activating the virtual environment

Now go to your terminal or command prompt. Go to the directory that contains the file called **activate.** The file called **activate** is found inside a folder called **Scripts for Windows** and **bin for OS X and Linux.**

For OS X and Linux Environment:

```bash
$ name of virtual environmnet/bin/activate
```

For Windows Environment:

```bash
name of virtual environment\Scripts\activate
```

Since I am using a Windows machine, when I activate the environment it will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/FnmOzwRngsHOTcuJr4gMBnvyB6VhYGhcdyI2 align="left")

*You should see this at beginning of your command prompt line*

The next step is to install flask on your virtual environment so that we can run the application inside our environment. Run the command:

```bash
pip install flask
```

Run your application and go to [http://localhost:5000/](http://localhost:5000/)

We finally made our web application. Now we want to show the whole world our project.

(More information on virtualenv can be found in the following guides on [virtualenv](https://realpython.com/python-virtual-environments-a-primer/) and [Flask Official Documentation](http://flask.pocoo.org/docs/0.12/installation/#installation))

## Let’s send it to the Cloud

To show others the project we made, we will need to learn how to use Cloud Services.

### Deploy Your Web Application to the Cloud

To deploy our web application to the cloud, we will use [Google App Engine](https://cloud.google.com/appengine/) (Standard Environment). This is an example of a **Platform as a Service (PaaS).**

**PaaS** refers to the **delivery of operating systems and associated services over the internet without downloads or installation**. The approach lets customers create and deploy applications without having to invest in the underlying infrastructure (More info on PaaS check out [TechTarget](https://searchitchannel.techtarget.com/definition/cloud-services)).

> Google App Engine is a platform as a service offering that allows developers and businesses to build and run applications using Google’s advanced infrastructure — [TechOpedia](https://www.techopedia.com/definition/31267/google-app-engine-gae).

#### **Before you Start:**

You will need a [Google Account](https://accounts.google.com/signup/v2?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)**.** Once you create an account, go to the [Google Cloud Platform Console](https://console.cloud.google.com) and create a new project. Also, you need to install the [Google Cloud SDK](https://cloud.google.com/sdk/).

At the end of this tutorial your project structure will look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/Nb7fiERQFkKC5chGteCvWkQCkShVq7a1auUe align="left")

*Project Folder Structure*

We will need to create three new files: app.yaml, appengine\_config.py, and requirements.txt.

Content of app.yaml:

```yml
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /static
  static_dir: static
- url: /.*
  script: main.app
  
libraries:
  - name: ssl
    version: latest
```

If you were to check [Google’s Tutorial](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env) in the part where they **talk about content of the app.yaml**, it does not include the section where I wrote about libraries.

When I first attempted to deploy my simple web app, my deployment never worked. After many attempts, I learned that we needed to include the SSL library.

The SSL Library allows us to [create secure connections between the client and server](https://wiki.python.org/moin/SSL). Every time the user goes to our website they will need to connect to a server run by Google App Engine. We need to create a secure connection for this. (I recently learned this, so if you have a suggestions for this let me know!)

Content of appengine\_config.py:

```py
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
```

Content of requirements.txt:

```javascript
Flask
Werkzeug
```

Now inside our virtual environment **(make sure your virtualenv is activated)**, we are going to install the new dependencies we have in requirements.txt. Run this command:

```bash
pip install -t lib -r requirements.txt
```

**\-t lib:** This flag copies the libraries into a lib folder, which uploads to App Engine during deployment.

**\-r requirements.txt:** Tells pip to install everything from requirements.txt.

### Deploying the Application

To deploy the application to Google App Engine, use this command.

```bash
gcloud app deploy
```

I usually include — **project \[ID of Project\]**

This specifies what project you are deploying. The command will look like this:

```bash
gcloud app deploy --project [ID of Project]
```

### The Application

Now check the URL of your application. The application will be store in the following way:

```bash
"your project id".appspot.com
```

My application is here: [http://sal-flask-tutorial.appspot.com](http://sal-flask-tutorial.appspot.com)

## Conclusion

From this tutorial, you all learned how to:

* Use the framework called Flask to use Python as a Server Side Language.
    
* Learned how to use HTML, CSS, and Flask to make a website.
    
* Learned how to create Virtual Environments using virtualenv.
    
* Use Google App Engine Standard Environment to deploy an application to the cloud.
    

#### **What I learned**

I learned three important things from this small project.

**First, I learned about the difference between a static website and a web application**

**Static Websites:**

* Means that the server is serving HTML, CSS, and JavaScript files to the client. The content of the site does not change when the user interacts with it.
    

**Web Applications:**

* A web application or dynamic website generates content based on retrieved data (most of the time is a database) that changes based on a user’s interaction with the site. In a web application, the server is responsible for querying, retrieving, and updating data. This causes web applications to be slower and more difficult to deploy than static websites for simple applications ([Reddit](https://www.reddit.com/r/Python/comments/1iewqt/deploying_static_flask_sites_for_free_on_github/)).
    

**Server Side and Client Side:**

* I learned that a web application has two sides. The client side and the server side. The client side is what the user interacts with and the server side is where the all the information that the user inputted is processed.
    

**Second, I learned about Cloud Services**

Most of my previous projects were static websites, and to deploy them I used [GitHub Pages](https://pages.github.com/). GitHub Pages is a free static site hosting service designed to host projects from a GitHub Repository.

When working with web applications, I could not use GitHub Pages to host them. GitHub Pages is only meant for static websites not for something dynamic like a web application that requires a server and a database. I had to use Cloud Services such as [Amazon Web Services](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/)

**Third, I learned how to use Python as a Server Side Language**

To create the server side of the web application we had to use a server side language. I learned that I could use the framework called Flask to use Python as the Server Side Language.

#### **Next Steps:**

You can build all sorts of things with Flask. I realized that Flask helps make the code behind the website easier to read. I have made the following applications during this summer of 2018 and I hope to make more.

Personal Projects

* [A Twilio SMS App](http://twilio-pokedex.appspot.com/)
    
* [My Personal Website](http://salvador-villalon.appspot.com/)
    

During my internship

* [Part of a project where I learned about Docker and Containers](http://spgi2018-container-project.appspot.com/)
    

Here is the list of resources that helped me create this tutorial:

* “App Engine — Build Scalable Web & Mobile Backends in Any Language | App Engine | Google Cloud.” *Google*, Google, [cloud.google.com/appengine/](https://cloud.google.com/appengine/).
    
* “Building a Website with Python Flask.” *PythonHow*, [pythonhow.com/building-a-website-with-python-flask/](https://pythonhow.com/building-a-website-with-python-flask/).
    
* “Flask — Lecture 2 — CS50’s Web Programming with Python and JavaScript.” *YouTube*, 6 Feb. 2018, [youtu.be/j5wysXqaIV8](https://youtu.be/j5wysXqaIV8).
    
* “Getting Started with Flask on App Engine Standard Environment | App Engine Standard Environment for Python | Google Cloud.” *Google*, Google, [cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env).
    
* “Installation.” *Welcome | Flask (A Python Microframework)*, [flask.pocoo.org/docs/0.12/installation/](http://flask.pocoo.org/docs/0.12/installation/).
    
* “Python — Deploying Static Flask Sites for Free on Github Pages.” *Reddit*, [www.reddit.com/r/Python/comments/1iewqt/deploying\_static\_flask\_sites\_for\_free\_on\_github/.](http://www.reddit.com/r/Python/comments/1iewqt/deploying_static_flask_sites_for_free_on_github/.)
    
* Real Python. “Python Virtual Environments: A Primer — Real Python.” *Real Python*, Real Python, 7 Aug. 2018, [realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/).
    
* “What Is Cloud Services? — Definition from WhatIs.com.” *SearchITChannel*, [searchitchannel.techtarget.com/definition/cloud-services](https://searchitchannel.techtarget.com/definition/cloud-services).
    
* “What Is Google App Engine (GAE)? — Definition from Techopedia.” *Techopedia.com*, [www.techopedia.com/definition/31267/google-app-engine-gae.](http://www.techopedia.com/definition/31267/google-app-engine-gae.)
    

If you have any suggestions or questions, feel free to leave a comment.
