---
title: 'Django in the wild: tips for deployment survival'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-24T22:21:00.000Z'
originalURL: https://freecodecamp.org/news/django-in-the-wild-tips-for-deployment-survival-9b491081c2e4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5w9DNocznYRp8ndO
tags:
- name: Django
  slug: django
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ali Alavi

  Before deploying your Django web app in the real world, you need to make sure your
  project is production-ready. Better to start implementing them earlier. It saves
  you and your team a lot of time and headache. Here are some points I lear...'
---

By Ali Alavi

Before deploying your Django web app in the real world, you need to make sure your project is production-ready. Better to start implementing them earlier. It saves you and your team a lot of time and headache. Here are some points I learned along the way:

1. Use pipenv (or requirements.txt + venv). Commit Pipefile and Pipefile.lock (or requirements.txt). Name your venv.
2. Have a quickstart script.
3. Write tests. Use the [Django test framework](https://docs.djangoproject.com/en/2.0/topics/testing/overview/) and [Hypothesis](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python).
4. Use [environ](https://github.com/joke2k/django-environ) and [direnv](https://direnv.net/) to manage your settings and automatically load your environment variables.
5. Make sure all developers commit their migrations. Squash migrations from time to time. Reset them if necessary. Architect your project for smoother migrations. Read about migrations.
6. Use continuous integration. Protect your master branch.
7. Go through [Django’s official deployment checklist.](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/)
8. Don’t manage your own server, but if you must, use a proper directory structure, and use Supervisord, Gunicorn and NGINX.

This list grew organically as I was going through the release our first Django app, and is not exhaustive. But I think these are some of the most important points you need to be aware of.

Read along for a discussion on each of the points.

## Manage your dependencies and virtual environments the right way

You and your team should agree on a way to manage your dependencies and virtual environments. I recommend either using [pipenv](https://github.com/pypa/pipenv), which is the new way of managing both your virtual environments and dependencies, or using the good old approach of creating a venv and tracking your dependencies with a `requirements.txt` file.

Using the `requirements.txt` approach is prone to human error, since developers tend to forget about updating the package list. This is not an issue with **pipenv,** since it automatically updates **Pipefile.** The drawback of **pipenv** is that it hasn’t been around long enough. Even though it is [officially recommended](https://packaging.python.org/tutorials/managing-dependencies/) by the Python Software Foundation, you might have issues getting it to run on some machines. Personally, I still use the old approach, but I will use **pipenv** for my next project.

### Using venv and requirements.txt

If you are using Python ≥ 3.6 (you should be), you can simply create one with `python -m venv ENV` . Make sure you name your virtual environment (instead of using `.` ). Sometimes you need to delete your virtual environment and create it anew. It makes it easier. Also, you should add `ENV` directory to your .`gitignore` file (I prefer the **ENV** name instead of **venv**, **.env**, … since it stands out when I **ls** the project folder).

To manage the dependencies, every developer runs `pip freeze > requirements.txt` whenever they install a new package, and add and commit it to the repo. They will use `pip install -r requirements.txt` whenever they pull from the remote repository.

### Using pipenv

If using **pipenv**, you just need to add [Pipfile and Pipfile.lock](https://github.com/pypa/pipenv/issues/598) to your repo.

## Have a quickstart script

This helps make sure your developers spend as little time as possible working on things not directly related to their job.

Not only does this save time and money, but also makes sure that they are all working on similar environments (same versions of Python and pip, for example).

So, try to automate as many setup tasks as possible.

Moreover, having a single step build script is very much what [Joel Test’s 2nd step](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/) is about.

Here is a small script I use, which saves my developers quite a few key strokes:

```bash
#!/bin/bash
python3.6 -m venv ENV
source ENV/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
source .envrc
python ./manage.py migrate
python ./manage.py loaddata example-django/fixtures/quickstart.json
python ./manage.py runserver
```

## Write tests

Everyone knows writing tests is a good practice. But many overlook it, for the sake of, they think, faster development. DON’T. Tests are an absolute necessity when it comes to writing software used in production, especially when you work in a team. The only way you can know that the latest update did not break something is to have well-written tests. Also, you absolutely need tests for continuous integration and delivery of your product.

Django has a decent [test framework](https://docs.djangoproject.com/en/2.0/topics/testing/overview/). You can also use property-based testing frameworks such as [Hypothesis](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python), which help you write shorter, mathematically rigorous tests for your code. For many cases, writing property-based tests is faster. In practice, you might end up using both these frameworks for writing comprehensive, easy-to-read-and-write tests.

## Use environment variables for settings

Your **settings.py** file is where you store all important project settings: your database URL, paths to media and static folders, and so on. These will have different values on your development machine and your production server. The best way to address this is to use environment variables. The first step is to update your [settings.py](https://gist.github.com/alialavia/da1c82a9f5194257d1de868decec933c) to read from the environment variables, using [environ](https://github.com/joke2k/django-environ)**:**

```py
import environ
import os
root = environ.Path(__file__) - 2 # two folders back (/a/b/ - 2 = /)
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
GOOGLE_ANALYTICS_ID=env('GOOGLE_ANALYTICS_ID')

SITE_DOMAIN = env('SITE_DOMAIN') 
SITE_ROOT = root()

DEBUG = env('DEBUG') # False if not in os.environ

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

public_root = root.path('./public/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = '/media/'

STATIC_ROOT = public_root('static')
STATIC_URL = '/static/'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

..
```

To avoid loading your envvars manually, set up [direnv](https://direnv.net/) on your development machines, and store the envvars in a `.envrc` file in your project directory. Now, whenever you `cd` into your projects folder, the environment variables are automatically loaded. Add `.envrc` to your repository (if all developers use the same settings), and make sure you run `direnv allow` whenever there is a change in `.envrc` file.

Don’t use `direnv` on your production server. Instead, create a file called **.server.envrc**, add it to the `.gitignore`, and put the production settings there. Now, create a script,`runinenv.sh`, to automatically source the environment variables from `.server.envrc`, activate the virtual environment, and run the provided command. You will see how it is used in the next section. Here is how `runinenv.sh` should look ([link to GitHub](https://gist.github.com/alialavia/7a29ea149870e151b4a27d53993d5d17)).

```bash
#!/bin/bash
WORKING_DIR=/home/myuser/example.com/example-django
cd ${WORKING_DIR}
source .server.envrc
source ENV/bin/activate
exec $@
```

## Handle your migrations properly

Django migrations are great, but working with them, especially in a team, is far from hassle-free.

First, you should make sure that all developers commit the migration files. Yes, you might (will) end up having conflicts, especially if you work with a large team, but it’s better than having an inconsistent schema.

In general, dealing with migrations is not that easy. You need to know what you are doing, and you need to follow some best practices to ensure a smooth workflow.

One thing that I figured is that it usually helps if you squash the migrations from time to time (e.g. on a weekly basis). This helps with reducing the number of files and the size of the dependency graph, which in turn leads to faster build time, and usually fewer (or easier to handle) conflicts.

Sometimes it’s easier to reset your migrations and make them anew, and sometimes you need to manually fix the conflicting migrations or merge them together. In general, dealing with migrations is a topic which deserves its own post, and there are some good reads on this topic:

* [Django migrations and how to manage conflicts](https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/)
* [How to Reset Migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

Moreover, how your project’s migrations end up depends on your project architecture, your models, and so on. This is especially important when your code-base grows, when you have multiple apps, or when you have complicated relations between models.

I highly recommend you to [read this great post about scaling Django apps](https://blog.doordash.com/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5), which covers the topic pretty well. It also has a tiny, useful migration script.

## Use Continuous Integration

The idea behind CI is simple: run tests as soon as new code is pushed.

Use a solution which integrates well with your version controlling platform. I ended up using [CircleCI](https://circleci.com/). CI is especially helpful when you work with multiple developers, since you can be sure their code passes all the tests before they send a pull request. Again, as you can see, it’s very important to have well covered tests in place. Moreover, make sure your master branch is protected.

## Deployment checklist

Django’s official website provides a [handy deployment checklist](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/). It helps you ensure your project’s security and performance. Make sure you follow through those guidelines.

## If you must manage your own server…

There are many good reasons to not manage your own server. Docker gives you more portability and security, and serverless architectures, such as AWS Lambda, can provide you with even more benefits for less money.

But there are cases where you need more control over your server (if you need more flexibility, if you have services cannot work with containerized apps — such as security monitoring agents, and so on).

### Use a proper directory structure

The first thing to do is to use a proper folder structure. If all you want to serve on your server is the Django app, you can simple clone your repository and use that as your main directory. But that’s rarely the case: usually you also need to have some static pages (home page, contacts, …). They should be separate from your Django code base.

A good way to go about it is to create a parent repository, which has different parts of your project as submodules. Your Django developers work on a django repository, your designers work on the homepage repository, … and you integrate all of them in a repository:

```
example.com/
   example-django/
   homepage/
```

### Use Supervisord, NGINX, and Gunicorn

Sure, `manage runserver` works, but only for a quick test. For anything serious, you need to use a proper application server. [Gunicorn](http://gunicorn.org/) is the way to go.

Keep in mind that any application server is a long-running process. And you need to make sure that it keeps running, is automatically restarted after a server failure, logs errors properly, and so on. For this purpose, we use `[supervisord](http://supervisord.org/).`

Supervisord needs a configuration file, in which we tell how we want our processes to run. And it is not limited to our application server. If we have other long-running processes (e.g. celery), we should defined them in `/etc/supervisor/supervisord.conf`. Here is an example ([also on GitHub](https://gist.github.com/alialavia/c3b5ec16823a1278833c66cfd3a638ca)):

```
[supervisord]
nodaemon=true
logfile=supervisord.log

[supervisorctl]

[inet_http_server]
port = 127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[program:web-1]
command=/home/myuser/example.com/example-django/runinenv.sh gunicorn example.wsgi --workers 3 --reload --log-level debug --log-file gunicorn.log --bind=0.0.0.0:8000
autostart=true
autorestart=true
stopsignal=QUIT
stdout_logfile=/var/log/example-django/web-1.log
stderr_logfile=/var/log/example-django/web-1.error.log
user=myuser
directory=/home/myuser/example.com/example-django

[program:celery-1]
command=/home/myuser/example.com/example-django/runinenv.sh celery worker --app=example --loglevel=info
autostart=true
autorestart=true
stopsignal=QUIT
stdout_logfile=/var/log/example-django/celery-1.log
stderr_logfile=/var/log/example-django/celery-1.error.log
user=myuser
directory=/home/myuser/example.com/example-django

[program:beat-1]
command=/home/myuser/example.com/example-django/runinenv.sh celery beat --app=example --loglevel=info
autostart=true
autorestart=true
stopsignal=QUIT
stdout_logfile=/var/log/example-django/beat-1.log
stderr_logfile=/var/log/example-django/beat-1.error.log
user=myuser
directory=/home/myuser/example.com/example-django

[group:example-django]
programs=web-1,celery-1,beat-1
```

Note how we use `runinenv.sh` here (lines 14, 24 and 34). Also, pay attention to line 14, where we tell **gunicorn** to dispatch 3 workers. This number depends on the number of cores your server has. [The recommended number of workers is: 2*number_of_cores + 1.](http://docs.gunicorn.org/en/stable/design.html#how-many-workers)

You also need a reverse proxy to connect your application server to the outside world. Just use [NGINX](https://www.nginx.com/), since it has a wide user base, and it’s very easy to configure ([you can also find this code on GitHub](https://gist.github.com/alialavia/63805a95cb821c19c553d0c21a8da938)):

```nginx
server {
    server_name www.example.com;
    access_log  /var/log/nginx/example.com.log;
    error_log    /var/log/nginx/example.com.error.log debug;
    root  /home/myuser/example.com/homepage;
    sendfile on;
    
# if the uri is not found, look for index.html, else pass everthing to gunicorn
    location / {
 index index.html;
 try_files $uri $uri/
     @gunicorn;
    }
    
# Django media
    location /media  {
        alias /home/myuser/example.com/example-django/public/media;      # your Django project's media files
    }
    
# Django static files
    location /static {
        alias /home/myuser/example.com/example-django/public/static;   # your Django project's static files
    }
    
location @gunicorn {

proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
 #proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_redirect off;
 
proxy_pass http://0.0.0.0:8000;
    }
    
client_max_body_size 100M;

listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.example.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.example.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    
}

server {
    server_name example.com;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/www.example.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.example.com/privkey.pem; # managed by Certbot
    return 301 https://www.example.com$request_uri;
    
}

server {
    if ($host = www.example.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
    
if ($host = example.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
    
listen 80 default_server;
    listen [::]:80 default_server;
    server_name example.com www.example.com;
    return 301 https://$server_name$request_uri;
}
```

Store the configuration file in `/etc/nginx/sites-available`, and create a symbolic link to it in `/etc/nginx/sites-enabled`.

I hope you’ve found this post helpful. Please let me know what you think about it, and show it some ❤ if you will.

