---
title: I Built a Members' Area on My Website with Python and Django. Here's What I
  Learned.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T15:40:01.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-members-area-on-my-website-with-python-and-django-heres-what-i-learned
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b12740569d1a4ca2983.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: "By Nick McCullum\nI decided it was time to upgrade my personal website\
  \ in order to allow visitors to buy and access my courses through a new portal.\
  \ \nSpecifically, I wanted a place for visitors to sign up for an account, view\
  \ my available courses, and..."
---

By Nick McCullum

I decided it was time to upgrade my personal website in order to allow visitors to buy and access [my courses](https://courses.nickmccullum.com/courses/) through a new portal. 

Specifically, I wanted a place for visitors to sign up for an account, view my available courses, and purchase those courses. Once a user had purchased a course they would be able to access all of the content in the course forever.   
  
This may sound simple in theory. However, without using an ecommerce site such as Shopify, membership sites are surprisingly complex. 

In this article I will walk you through the decisions I made and the technology stack I used to build this new site, including:

1. How to start?
2. Starting a Django Project
3. How to set up Django models
4. Integrating [Stripe](https://stripe.com/en-ca) Payments
5. Deploying my new site on an AWS EC2 instance
6. How to clone CSS from an existing page 

![Image](https://lh5.googleusercontent.com/VcTBavKxXlNR907_Gc8lRLWvXPC_8avJogGeEGw7ykM6d9WwZskU6GPvsZjAepF4glzURlMkeKBjdw5yhAcjupP_9AFZEdWVEJEEGRgJs33VbIY2gME4MOk5imvszBkpxBmPBeXJ)

## How To Start?

When adding a new section to your website with a completely new feature set, it’s logical to organize this site as a subdomain of your original site.  
  
A subdomain is exactly what it sounds like. It's _a domain that is part of another (main) domain._ Subdomains appear as a new section of your domain url _before_ the main domain url.

More specifically:

* My _main_ domain is: [https://nickmccullum.com](http://www.nickmccullum.com)
* My new _courses_ subdomain is: [https://courses.nickmccullum.com](https://courses.nickmccullum.com/courses/)

The main advantage of a subdomain is that they are free! Not to mention, a subdomain tagged on to an already-well-ranked site gets indexed quickly and benefits from its parent’s success.

I knew that I would need a server to host my new site. I would also need to attach that server with an elastic IP address. 

An elastic IP address is a static IP that will never change. This means it can be accessed by the public 24/7.

The fastest way to get a server up and running nowadays is to host it in the cloud. There are many options for cloud computing, including as [Amazon's AWS](https://aws.amazon.com/), [DigitalOcean's Droplets](https://www.digitalocean.com/products/droplets/), or [Azure's Containers](https://azure.microsoft.com/en-ca/). In terms of pricing, the options available are all fairly equal across the board - so that didn’t factor into my decision too much.

I’ve had previous experience with [AWS (Amazon Web Services)](https://aws.amazon.com/) - a cloud based service for hosting infrastructure. Naturally I chose to host my server here. To be more specific, I am hosting the site on an [EC2](https://aws.amazon.com/ec2/) instance. We will talk more about that later.

Okay, so now I knew where I wanted to host my new website, what’s next?   
  
It was time to think about the tech stack for the site. When thinking about what technology to use for building your website, it's important to consider these major topics:  


1. What you are proficient in
2. Choosing frontend and backend technologies that mesh well together
3. The performance of the site

You should answer these questions and try to choose a technology stack that suits your needs and abilities. For me, I am most proficient in Python, so [Django 3.0](https://www.djangoproject.com/) was a natural choice!

I had worked on a Django app before ([Passiv](https://getpassiv.com/)) so I was broadly familiar with the infrastructure. However, I had never built a Django project from scratch. 

Because of this, I had some reading to do. As I learned more about this popular framework I kept comparing it to PHP, the popular web programming tool. I have worked on multiple Wordpress sites in the past, and Wordpress is built on PHP, so this was a natural comparison (at least for me).

According to their documentation and various posts on Stackoverflow, here are the main differences between the Django framework and the major PHP frameworks:

* Django is more focused on security by default and provides built-in security practices to help programmers save time during development.
* Django is focused on speed. It's known as a framework which helps developers get their sits off the ground as quickly as possible.
* Django has marginally lower performance compared to most PHP-based frameworks. 

I’d like to touch on that last point. Python is an interpreted language and is commonly associated with a lower performance than other programming languages. When a new programmer hears something like this they may think that Python is much worse than other language choices because of the importance of performance in computing. 

Though Python does have lower performance standards compared to other languages this is an extremely vague statement. In fact, the difference between Django and Laravel (a popular PHP based framework) is so small it's considered negligible. 

For this performance difference to matter to you, you would need to be writing a highly performance-dependent application with millions of users. I was encouraged to learn that many of the world's largest web applications are built on Django. Said differently, if Django is good enough for [Instagram](https://www.instagram.com/), then it was certainly performant enough for my site.

In the end I decided to build my courses website using Django mainly because I have experience with [Python](https://nickmccullum.com/best-python-libraries-quantitative-finance/). Learning a new web framework was a nice bonus.

Next, I knew I was going to need a database for this site. Having experience with MySQL and [PostgreSQL](https://nickmccullum.com/sql/sql-installation/), I was originally going to resort to using it again here. However, Django ships default with an SQLite3 database service that requires minimal setup. I have never used SQLite so I did some more research.

Based on the performance and data storage needs, the default [SQLite3](https://www.sqlite.org/index.html) database shipped with Django would be more than powerful enough for my site. I was shocked to find that a lighter version of a database service could be so powerful!

For anyone unfamiliar with this technology (like I was), SQLite3 is a relational database with great performance for sites with low to medium levels of traffic (~100K hits per day). SQLite3 can be run on the same server as the website without impacting performance. This means that I did not need to spin up a separate Amazon RDS instance, which saves some money in the deployment stage.

## Starting a Django Project

![Image](https://lh5.googleusercontent.com/d5I_NnBMYltwX71zwpcZJ6Fx54w-AU-WR2GRRzrJgw70jY5Xd3oTAEZnmfnslPwM-EeZ-na8_KHOjrlk-Z9VH9gGKvuF8UXz4fOgewIA8dD1-baCKsEMwRaxIRUszVS1z9Ggdux6)

Django is a high-level python web framework with the main goal of allowing **rapid development** and providing security by default. It takes care of many hassles of web development, reducing repetitive coding practices.

One of the best parts of using Django is that it is absolutely free.

Django is designed to help developers get their websites off the ground quickly (which is one of the main reasons I chose to use it for this project). One of my favourite features of this framework (as with most others) is their frontend templating system.   
  
[Django Templates](https://docs.djangoproject.com/en/3.0/topics/templates/) allow you to write dynamic code which then generates the desired HTML and CSS. This gives you the ability to use structures such as loops and if statements in order to create dynamic HTML code (meaning it renders differently for each user) that can then be served as a static file.   
  
For example:

```html
# course_titles_template.html
{% for course in courses_list %}
<h1>{{ course.course_title }} </h1>
{% endfor %}
```

Would create a heading for every course variable found in the `courses_list` object. This could would render an HTML file with an `<h1>` tag that contains the title of each course, like this:

```html
<h1> Python Fundamentals </h1>
<h1> Advanced Python for Finance and Data Science</h1>
<h1> How to Run Python Scripts </h1>
<h1> How to Make A Python Class </h1>
```

The templating system saves you from a lot of manual labor. Allowing the HTML to render dynamically saves you the headaches of updating your code every time you add a new object.   
  
This templating system also allows the web app to update over time as I add more content. So in this case if I were to add a new course to my database, this template would not need to be changed. It would simply render my new course’s title in a new heading tag.  
  
Django also makes it extremely easy to get started in a project. Once you have Django installed, you are able to use the `django-admin` in order to start a project and even set up your apps.

Hang on a second, apps? Projects? What’s the difference?  
  
An app is a web application that performs some functionality. It can be a blog, _a login system,_ or even a file server. A project is a collection of apps and configurations which together form a website.

### Installing Django:

The simplest way to install is with pip, the Python package manager.

```bash
python -m pip install Django
```

For a full installation guide, check out [Django's Official Documentation](https://docs.djangoproject.com/en/3.0/intro/install/).

### Starting a Project:

Once you have Django installed, you will have access to the `django-admin` tool which helps developers with setting up projects and apps and also provides other handy tools.  
  
Running  `django-admin startproject myproject` will create a new folder in the current directory where your project will live. It will also create many of the necessary files you will need to get going.

Here's what your directory will look like after running this command:

> myproject/  
>     manage.py   
>     myproject/  
>         __init__.py  
>         settings.py  
>         urls.py  
>         asgi.py  
>         wsgi.py

Inside the `myproject` folder you will find a `manage.py` file, which is extremely useful and provides many handy utilities. There will be another folder named `myproject` which will be where you set your configurations for the project.   
  
The outer myproject/ root directory is a container for your project, its name doesn’t actually matter and if you find this confusing you can rename it to anything you like.  
  
The inner myproject/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it.

The important files to note here are the `myproject/settings.py`, where your Django and app specific settings are configured, and the `myproject/urls.py`. 

The `urls.py` file is used to create urls within your website and point them to a location to service the request. This image does a great job explaining how Django handles requests:

![Image](https://lh3.googleusercontent.com/sSrqigM9D-JRg3XQg_sh9WvtehX-UKJnnOmygeIn4u8-Ht2xcv_y0jZ1toPcg8mgoA4BIC_7Y14AG4DKKJ6CIV3IzON06BtmjLp-cTyL8GJ7CvHRr-odmE1Yofo0cGYzhuPbgXQI)

Kudos to [Ryan Nevius](https://www.ryannevius.com/) for creating such a wonderful visualization.

The `myproject/urls.py` file outlines the URL resolution for the entire website. Each app you add to your website will contain its own `urls.py` file which outlines the URL resolution within that specific app.

Now that you have a grasp on what some of those files are used for, let’s dive into getting a project started with the manager script’s commands.

One command to note would be the `startapp` command used for creating an app inside your project the same way you created the app. `python manage.py startapp myapp` will create a new folder and some of the necessary files for creating a new app in your project.

> myapp/     
>     __init__.py  
>     admin.py  
>     apps.py  
>     migrations/  
>         __init__.py  
>     models.py  
>     tests.py  
>     views.py

The main difference here is the presence of the models and views files, which are used to define the database and the frontend functionality of the app, respectively.

Models are classes that define your database tables. We will discuss models in more detail later in this tutorial.

Views control the frontend structure and functionality of the app taking in a web request and returning a web response.   
  
Probably the most important command to remember is the runserver command:   
`python manage.py runserver`. This will run your project on your localhost at the default port, 8000.

That’s it! With three simple steps you will see a welcome landing page showing you that the installation worked.

![Image](https://lh3.googleusercontent.com/przKJhywBTWAxqF7H1D7YbreiryXuAE4k1a_3ZmGQ0zu7ByEFTI-LBW-PsyBJlT7sUSmWXvycmlZcwAkK0QoOe-bi3zmPmF61KbGsUfNtUE1WVlkSnaCjIgE_00Kn0i8osx1Ipb_)

There is an extremely well written tutorial in Django’s Documentation providing a far more in depth walk through of starting a project. It can be found here: [Starting a Project](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

## How to set up models

Like many other web frameworks, Django has an implementation of the object-relational mapping (**ORM**) concept. In Django, this implementation is called models.

Models are a very important topic to understand when developing a project in Django. In there most basic form, models can be thought of as wrappers for database tables.  
  
Said differently, a Django model is used to define your data. It contains the fields and behaviours of the data you store. Each model maps to a single table in your database and fields in your model map to fields in your database.

When writing models you have access to powerful built-in field types that do a lot of the heavy lifting for you. Forget writing SQL code manually to construct your database. You can simply write a model class and run the migration commands to have a fully functional SQL script loaded into your database.   


![Image](https://lh3.googleusercontent.com/CVP_WO8s02EEdmC8_A0w6gbAFmH4AbZ5Z65XatAvx9j31rLjJ1oQMgW4EmBMTlOz0hRWjiybiqnYgadFVX4rlCKLBZGX8pEbhYKbsYwCXwEClo444j6eRt3UeTYurZPg047u5-LH)

Django offers a [User Model](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#user-model) as part of its built in authentication system which allows you to ignore the backend side of all the login/sign-up and password handling. 

When designing the models for my new site I needed the following three models:

* Profile - a wrapper class around the User model to add non-auth related information (often called a [Profile Model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#extending-the-existing-user-model))
* Course - to store all the information about each course
* Document - a model that stores information about which files are attributed to each course. I specifically wanted to upload Markdown documents, as that's [how my public blog is already built](https://nickmccullum.com/blog-like-a-hacker/)

Here's an example of a model:

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    			
    enrolled_courses = models.ManyToManyField(Course)
```

A Profile Model is a useful tool for extending the functionality of the existing user model in order to store information about the user, beyond just authentication data. In my case I created a _profile model_ named Profile to store which courses the user is enrolled in.

Here's my Course Model:

```python
class Course(models.Model):   
    course_title = models.CharField(max_length=200)   
    course_description = models.CharField(max_length=500)   
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
```

My Course model is fairly straightforward. I only needed to store 3 pieces of information about each course for logistics while the actual content of the course is handled by the Document model.

```python
class Document(models.Model):   
    course = models.ForeignKey(Course,on_delete=models.PROTECT)   
    file = models.FileField (
upload_to=markdown_upload_location,
default='default.md'
)
```

Here I take advantage of some built in python functionality, where I’m passing the function `markdown_upload_location` into the `FileField` constructor. 

This function is used to determine where the file being uploaded is to be stored on the file system. Passing the function into the constructor allows the function to be run each time a new file is uploaded instead of only being run once and then the same result being used over again. 

Essentially, when an admin (me) uploads a new course to the site, a new folder is created for that course and all markdown files for that course are stored there. The Document model records link those files to the course record in the database. 

One thing I took away from setting up these models was how easy the process of designing my database became. Gone are the days of MySQL Workbench and ERR diagrams, or writing SQL line-by-line and executing painful updates to schemas.

## Integrating Stripe Payments

[Stripe](https://stripe.com/en-ca) is a platform used by many websites around the world to take payment from customers. It’s secure, easy to use for customers and most importantly, it’s easy for us developers to set up! 

The pricing is also quite fair compared to their competition, currently sitting at 2.9% + 0.30 CAD per transaction. This pricing applies to one time payments as well as their subscription sign ups.

In order to use Stripe as a developer you must make an account and check out their developer pages to review the options. They have prebuilt checkouts, entire libraries and SDKs for building your own custom checkout. Stripe also provides preexisting plugins for web frameworks (Wordpress, Drupal, etc.)

I decided to use their [Checkout](https://stripe.com/docs/payments/checkout) tool which is a secure, Stripe-hosted payment page that allowed me to avoid having to build a payment page. This not only saves the time of developing the frontend page for collecting payment information, but also the hassle of securing the payment in the backend.

Security is a huge topic nowadays and customers are wary of where they hand out their credit card details, so for me, using Stripe was a no brainer. I store none of the users details. Instead, they are sent straight to Stripe where they can be securely handled.

With a few lines of code I was able to import Stripe’s pre-built Javascript checkout module. Here's the script tag:

```javascript
<script 
src="https://checkout.stripe.com/checkout.js"    
class="stripe-button"    
data-key="{{ key }}"    
data-description="Payment: {{ course.course_title }}"    
data-amount="{% multiply course.course_price 100 %}"    
data-locale="auto">
</script>
```

Here the data-key is set to the Stripe public key, similar to any developer API key. The description is what will appear in your Stripe dashboard for the payment received and the amount is the number of cents for the purchase. This simple inclusion imports this payment page as a modal on the website:

![Image](https://lh6.googleusercontent.com/ZoLSCpczDEDUwno0TaWc8jYVl4dTnBxnL1bZBMNjyVJ46UDPbP271hBWancYSPPWA9IDPZHxg6YWSEQEyrcIyNkb4eMpg5iIMHnl0NSJ1oiF4QZluZ8YarjqWStmUc3c0-2hvY3c)

Once a customer fills out the payment information you only need to bundle up the payment information into a request and send it to Stripe. Next, Stripe is able to process the information and approve the payment within seconds. 

```python
# Send the charge to Stripe
charge = stripe.Charge.create(    
amount=amount,
currency=currency,    
description=f"Payment for course: {courseTitle}",    source=self.request.POST['stripeToken']
)
```

## Deploying my new site on an EC2 instance

![Image](https://lh3.googleusercontent.com/uRaS5Pqadp9Z-dGeRfXf12DaLLZLpcfQum70RzmQRNUWfcN9JM3Gc46pjCj8KIReqmP922jI9hWQRYDWG0i8r_eBOb5zNh6a0zrO7PXm4qzPPBVRRAsHsjjok2IyxcmsCG1UofJM)

Once I was finished developing my new site on my localhost, I needed to find a place to deploy it. I’ve had some experience with AWS and already had an account so it made for an easy decision.   
  
Amazon’s Elastic Compute Cloud - usually referred to as EC2 - allows for an abundance of configurations, I simply went with the most straightforward set up. More specifically, a Ubuntu machine running on a T2 Micro server would be ample performance for this site.

Setting up the server was the easiest part of deployment, I set up a server in less than 10 minutes. Next I had to attach an elastic IP address to the instance and update my DNS records in [Route53](https://aws.amazon.com/route53/) (where my domain lives).  
  
After setting up the server I had to figure out how I was going to serve the website to visitors. I’ve had some experience in the past with Apache so that was a natural choice. It turns out that Apache and Django mesh together very well.

Django is served via its WSGI (Web Server Gateway Interface) - a fast CGI interface for Python, this is similar to PHP’s FPM if you are familiar with that. In simple terms, the WSGI is a layer between Django and the web server that acts as an interface to serve the web pages. 

As you may already know, Python is normally run within a `virtualenv`. This creates a virtual environment where the dependencies for a particular project can live without interfering with the system’s version of python. 

If you’d like to learn a bit more about virtualenv check out the [Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/).

Basically this is important only to configure the Apache configurations. To serve the files correctly you need to make a WSGI Daemon for your Django project like so:

```bash
# /etc/apache2/sites-available/mysite.conf:

WSGIProcessGroup courses.nickmccullum.com

WSGIDaemonProcess course python-path=/home/ubuntu/django/courses-website python-home=/home/ubuntu/django/courses-website-venv


WSGIProcessGroup course


WSGIScriptAlias / /home/ubuntu/django/courses-website/courses-website/wsgi.py


<VirtualHost *:80>
        ServerName courses.nickmccullum.com
</VirtualHost>
```

This tells Apache to utilize the WSGI daemon in order to properly serve the files from the Django project. Once this was set up, I needed to restart Apache, wait the 24 hours it took for the DNS records to update, then - voilà:  


![Image](https://lh4.googleusercontent.com/rPc_HYj7M-kwBTan4LUTk4pqkYBYsU4PKksK6gfYo0tV9WzX128fl67Iu0m_xz2-TVmfhRNYvMx4OWzrJP_nr5DE2ECQUXQ6Ym1P1gVFhVpLYH2_3_PE6_JcMLNBZBvWemwNDCuY)

One last step, I needed to secure my site with SSL (Secure Socket Layer). After all, I am asking people to make payments on my site, so customers will expect the site to be secured!

The simplest way to enable SSL on a site, in my opinion, is through [Lets Encrypt](https://letsencrypt.org/). They offer a tool called [Certbot](https://certbot.eff.org/) for free, which can be enabled on your server to auto renew a server certificate and keep your server running with SSL 24/7 all year long.

It’s as simple as the following three steps:  
  
1. Install Certbot:

`sudo apt-get install certbot python3-certbot-apache`

**NOTE**: This script will look at the ServerName setting in your apache configuration file to create the certificate so make sure you’ve set that before running it.

2. Get the certificate and tell certbot to update the apache configuration automatically:

`sudo certbot --apache`

3. Test the auto renewal:

`sudo certbot renew --dry-run`

Once you’ve configured SSL you can test to make sure the certificate was installed correctly by checking this website: [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/).

After securing my site with SSL I opened the EC2 instance’s security rules to allow the site to be public. With my new site up and running on my EC2 instance, I am now able to securely sell my courses to customers who wish to learn about various topics in software development. 

## Final Thoughts

I am grateful for all of the experience I gained throughout this project, from navigating a new web framework to integrating the Stripe API – I certainly learned a lot! 

Learning a new topic like Django can be overwhelming but I felt their documentation was very strong compared to others that I’ve read (erhm, AWS).

If I were to give a single piece of advice I would tell you that the most valuable resource with any tool is the official documentation. This is especially true when it’s well written. But no matter what tool you are using, never be afraid of the docs and get used to reading them in order to find answers to your problems.

This article was written by Nick McCullum, who teaches [Python](https://nickmccullum.com/python-course/), [JavaScript](https://nickmccullum.com/javascript/), and [Data Science](https://nickmccullum.com/advanced-python/) courses on his website.

