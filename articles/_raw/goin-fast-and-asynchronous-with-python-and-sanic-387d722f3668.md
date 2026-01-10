---
title: How to make your code fast and asynchronous with Python and Sanic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T08:57:06.000Z'
originalURL: https://freecodecamp.org/news/goin-fast-and-asynchronous-with-python-and-sanic-387d722f3668
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vJxAS5gEDCUgnTntr5eSRg.jpeg
tags:
- name: Sanic
  slug: sanic
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Davit Tovmasyan

  Hello everybody. In this article I’ll talk about building simple asynchronous projects
  with the Sanic framework.


  Goin’ Fast

  Introduction

  Sanic is a very flask-like open-source Python web server and web framework with
  more than 10K...'
---

By Davit Tovmasyan

Hello everybody. In this article I’ll talk about building simple asynchronous projects with the Sanic framework.

![Image](https://cdn-media-1.freecodecamp.org/images/F0Jro1PM0OTKI0on7Hz0sEIFNlIb9JWZ58JO)
_Goin’ Fast_

### Introduction

[Sanic](https://sanicframework.org/) is a very flask-like open-source Python web server and web framework with more than [10K stars](https://github.com/huge-success/sanic) that’s written to go fast. It allows the usage of `async/await` syntax added in Python 3.5 ([read more](https://docs.python.org/3/library/asyncio-task.html)), which makes your code [non-blocking](https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b) and speedy.

Sanic has pretty good [documentation](https://sanic.readthedocs.io/en/latest/) and it’s maintained by the community, for the community.

> The goal of the project is to provide a simple way to get a highly performant HTTP server up and running that is easy to build, to expand, and ultimately to scale.

### Requirements

Before we start, let’s install some packages and make sure that we have everything ready for the development of this project.

_Note: Source code is available in my [github.com](https://github.com/davitovmasyan/sanic-project) repository. For each step there is a corresponding commit._

#### Prerequisites:

* Python3.6+
* [pipenv](https://github.com/pypa/pipenv) (you can use any other package installer)
* [PostgreSQL](https://www.postgresql.org/) (for database, can also be MySQL or SQLite)

#### Packages:

* [secure](https://pypi.org/project/secure/) is a lightweight package that adds optional security headers and cookie attributes for Python web frameworks.
* [environs](https://pypi.org/project/environs/) is a Python library for parsing environment variables. It allows you to store configuration separate from your code, as per [The Twelve-Factor App](https://12factor.net/config) methodology.
* [sanic-envconfig](https://github.com/jamesstidard/sanic-envconfig) is and extension that helps you bring command line & environment variables into your Sanic config.
* [databases](https://pypi.org/project/databases/) is a Python package that allows you to make queries using the powerful [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/) expression language, and provides support for PostgreSQL, MySQL, and SQLite.

Let’s create an empty directory and initialize an empty `Pipfile` there.

```
pipenv  -- python python3.6
```

Install all necessary packages using **pipenv** commands below.

```
pipenv install sanic secure environs sanic-envconfig
```

For database:

```
pipenv install databases[postgresql]
```

Choices are **postgresql, mysql, sqlite.**

### Structure

Now let’s create some files and folders where we will write our actual code.

```
├── .env├── Pipfile├── Pipfile.lock├── setup.py└── project    ├── __init__.py    ├── __main__.py    ├── main.py    ├── middlewares.py    ├── routes.py    ├── settings.py    └── tables.py
```

We will use the `setup.py` file to make the `project` folder available as a package in our code.

```
from setuptools import setupsetup(    name='project',)
```

_Installing…_

```
pipenv install -e .
```

In the `.env` file, we’ll store some global variables like the database connection URL.

`__main__.py` is created for making our `project` package executable from the command-line.

```
pipenv run python -m project
```

### Initialization

Let’s do our first call in **__main__.py** file.

```
from project.main import initinit()
```

This is the beginning of our application. Now we need to create the `init` function inside of **main.py** file.

```
from sanic import Sanicapp = Sanic(__name__)def init():    app.run(host='0.0.0.0', port=8000, debug=True)
```

Simply creating the app from the _Sanic_ class we can run it specifying **host**, **port** and optional **debug** keyword argument.

_Running…_

```
pipenv run python -m project
```

![Image](https://cdn-media-1.freecodecamp.org/images/7GwhssZorNRLRt-O9V-Dlm0E9VCqTFqNeOE0)
_Sanic console output_

This is how a successful output should look in your Sanic app. If you open [http://0.0.0.0:8000](http://0.0.0.0:8000) on your browser you’ll see

> Error: Requested URL / not found

We haven’t created any **routes** yet, so it’s fine for now. We will add some routes below.

### Settings

Now we can modify the environment and settings. We need to add some variables in the **.env** file, read them, and pass to Sanic app config.

**_.env_** _file._

```
DEBUG=TrueHOST=0.0.0.0POST=8000
```

_Configuration…_

```
from sanic import Sanic
```

```
from environs import Envfrom project.settings import Settings
```

```
app = Sanic(__name__)
```

```
def init():    env = Env()    env.read_env()        app.config.from_object(Settings)    app.run(        host=app.config.HOST,         port=app.config.PORT,         debug=app.config.DEBUG,        auto_reload=app.config.DEBUG,        )
```

**_settings.py_** _file._

```
from sanic_envconfig import EnvConfigclass Settings(EnvConfig):    DEBUG: bool = True    HOST: str = '0.0.0.0'    PORT: int = 8000
```

Please note that I’ve added an optional **auto_reload** argument which will activate or deactivate the Automatic Reloader.

### Database

Now it’s time to setup a database.

One little note about the **databases** package before we go ahead:

> **databases** package uses [asyncpg](https://github.com/MagicStack/asyncpg) which is an asynchronous interface library for PostgreSQL. It’s pretty fast. See results below.

![Image](https://cdn-media-1.freecodecamp.org/images/RvldCRR3gSuI4UKswmylnrJYrIDQhQ9wetEd)

We will use two of Sanic’s [listeners](https://sanic.readthedocs.io/en/latest/sanic/middleware.html#listeners) where we will specify database connect and disconnect operations. Here are the listeners that we are going to use:

* **after_server_start**
* **after_server_stop**

**_main.py_** _file._

```
from sanic import Sanic
```

```
from databases import Database
```

```
from environs import Envfrom project.settings import Settings
```

```
app = Sanic(__name__)
```

```
def setup_database():    app.db = Database(app.config.DB_URL)    @app.listener('after_server_start')    async def connect_to_db(*args, **kwargs):        await app.db.connect()    @app.listener('after_server_stop')    async def disconnect_from_db(*args, **kwargs):        await app.db.disconnect()
```

```
def init():    env = Env()    env.read_env()        app.config.from_object(Settings)
```

```
    setup_database()
```

```
    app.run(        host=app.config.HOST,         port=app.config.PORT,         debug=app.config.DEBUG,        auto_reload=app.config.DEBUG,        )
```

Once more thing. We need to specify **DB_URL** in project settings and environment.

**_.env_** _file._

```
DEBUG=TrueHOST=0.0.0.0POST=8000DB_URL=postgresql://postgres:postgres@localhost/postgres
```

_And **settings.py** file._

```
from sanic_envconfig import EnvConfigclass Settings(EnvConfig):    DEBUG: bool = True    HOST: str = '0.0.0.0'    PORT: int = 8000    DB_URL: str = ''
```

Make sure that **DB_URL** is correct and your database is running. Now you can access to database using **app.db.** See more detailed information in the next section.

### Tables

Now we have a connection to our database and we can try to do some SQL queries.

Let’s declare a table in **tables.py** file using SQLAlchemy.

```
import sqlalchemymetadata = sqlalchemy.MetaData()books = sqlalchemy.Table(    'books',    metadata,    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),    sqlalchemy.Column('title', sqlalchemy.String(length=100)),    sqlalchemy.Column('author', sqlalchemy.String(length=60)),)
```

Here I assume that you already have a **migrated** database with a **books** table in it. For creating database migrations, I recommend that you use [Alembic](https://alembic.sqlalchemy.org/) which is a lightweight and easy-to-use tool that you can use with the SQLAlchemy Database Toolkit for Python.

Now we can use any [SQLAlchemy core](https://docs.sqlalchemy.org/en/latest/core/) queries. Check out some examples below.

```
# Executing manyquery = books.insert()values = [    {"title": "No Highway", "author": "Nevil Shute"},    {"title": "The Daffodil", "author": "SkyH. E. Bates"},]await app.db.execute_many(query, values)# Fetching multiple rowsquery = books.select()rows = await app.db.fetch_all(query)# Fetch single rowquery = books.select()row = await app.db.fetch_one(query)
```

### Routes

Now we need to setup routes. Let’s go to **routes.py** and add a new route for books.

```
from sanic.response import json
```

```
from project.tables import books
```

```
def setup_routes(app):    @app.route("/books")    async def book_list(request):        query = books.select()        rows = await request.app.db.fetch_all(query)        return json({            'books': [{row['title']: row['author']} for row in rows]        })
```

Of course we need to call **setup_routes** in **init** to make it work.

```
from project.routes import setup_routes
```

```
app = Sanic(__name__)
```

```
def init():    ...    app.config.from_object(Settings)    setup_database()    setup_routes(app)    ...
```

_Requesting…_

```
$ curl localhost:8000/books{"books":[{"No Highway":"Nevil Shute"},{"The Daffodil":"SkyH. E. Bates"}]}
```

### Middlewares

What about checking the **response** headers and seeing what we can add or fix there?

```
$ curl -I localhost:8000Connection: keep-aliveKeep-Alive: 5Content-Length: 32Content-Type: text/plain; charset=utf-8
```

As you can see we need some security improvements. There are some missing headers such as **X-XSS-Protection, Strict-Transport-Security**… so let’s take care of them using a combination of [middlewares](https://sanic.readthedocs.io/en/latest/sanic/middleware.html#middleware) and **secure** packages.

**_middlewares.py_** _file._

```
from secure import SecureHeaderssecure_headers = SecureHeaders()def setup_middlewares(app):    @app.middleware('response')    async def set_secure_headers(request, response):        secure_headers.sanic(response)
```

_Setting up middlewares in **main.py** file._

```
from project.middlewares import setup_middlewares
```

```
app = Sanic(__name__)
```

```
def init():    ...    app.config.from_object(Settings)    setup_database()    setup_routes(app)    setup_middlewares(app)    ...
```

_The result is:_

```
$ curl -I localhost:8000/booksConnection: keep-aliveKeep-Alive: 5Strict-Transport-Security: max-age=63072000; includeSubdomainsX-Frame-Options: SAMEORIGINX-XSS-Protection: 1; mode=blockX-Content-Type-Options: nosniffReferrer-Policy: no-referrer, strict-origin-when-cross-originPragma: no-cacheExpires: 0Cache-control: no-cache, no-store, must-revalidate, max-age=0Content-Length: 32Content-Type: text/plain; charset=utf-8
```

As I promised at the beginning, there is a [github repository](https://github.com/davitovmasyan/sanic-project) for each [section](https://github.com/davitovmasyan/sanic-project/tags) in this article. Hope this small tutorial helped you to get started with Sanic. There are still many unexplored features in the Sanic framework that you can find and check out in the [documentation](https://sanic.readthedocs.io/en/latest/).

[**davitovmasyan/sanic-project**](https://github.com/davitovmasyan/sanic-project)  
[_Goin' Fast and asynchronous with Python and Sanic! - davitovmasyan/sanic-project_github.com](https://github.com/davitovmasyan/sanic-project)

If you have thoughts on this, be sure to leave a comment.

If you found this article helpful, give me some claps ?

Thanks for reading. Go Fast with Sanic and good luck!!!

