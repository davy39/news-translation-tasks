---
title: How to Use Blueprints to Organize Your Flask Apps
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-09-01T15:25:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-blueprints-to-organize-flask-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/blueprints.png
tags:
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
seo_title: null
seo_desc: "Flask is a simple, easy-to-use microframework for Python that can help\
  \ you build scalable and secure web applications. \nSometimes you'll find developers\
  \ dumping all of their logic into a single file called app.py. You will find a lot\
  \ of tutorials tha..."
---

Flask is a simple, easy-to-use microframework for Python that can help you build scalable and secure web applications. 

Sometimes you'll find developers dumping all of their logic into a single file called app.py. You will find a lot of tutorials that follow the same pattern. But it's not a good practice for a large-scale app. 

By doing this, you are clearly violating the _Single Responsibility Principle_, where each piece of your application should handle just one responsibility. 

If you have worked with Django, you might have found your project divided into different modules. In Flask, also, you can organize your applications using **Blueprints**, a built-in concept in Flask similar to Python modules. 

## What Does a Flask Application Look Like?

If you follow the Flask documentation to create a minimal application, your project structure will look similar to this:

```md
/myapp
├── /templates
├── /static
└── app.py
```

Doesn't the folder look so clean? All you have is an `app.py` file where you have all your logic for the application, a `templates` folder to store your HTML files, and a `static` folder to store your static files. 

Let's look at the app.py file:

```py
from flask import Flask


app = Flask(__name__)

# Some Models Here


# Routes related to core functionalities


# Routes related to Profile Page


# Routes related to Products Page


# Routes related to Blog Page


# Routes related to Admin Page

if __name__ == '__main__':
    app.run(debug=True)
```

Doesn't that look messy (imagining that you've built a large-scale app)? You have all your models and different routes inside the same file spread around here and there.

## How Does Blueprints Solve the Problem?

Now, this is where Flask Blueprints come into picture. Blueprints help you structure your application by organizing the logic into subdirectories. In addition to that, you can store your templates and static files along with the logic in the same subdirectory.

So, with Blueprints now your same application will look like this:

```md
/blueprint-tutorial
├── /myapp_with_blueprints
│   ├── __init__.py
│   ├── /admin
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /core
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /products
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   └── /profile
|       ├── /templates
|       ├── /static
|       └── routes.py		
├── app.py
├── /static
└── /templates
```

Now you can see that you have clear separation of concerns. The logic related to admin resides inside the `admin` folder, the logic related to products resides inside the `products` folder and so on. 

Additionally, we also separated the templates and static files in the subdirectories where they are required, so that irrelevant files don't load when going to a page that doesn't require them.

## How to Use Blueprints

Now that you understand what problems Blueprints solves, let's see how we can use Blueprints in our applications.

### How to Define a Blueprint

Let's define our very first blueprint for the **admin** functionality inside the `admin/routes.py` file:

```py
from flask import Blueprint


# Defining a blueprint
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

```

Since Blueprint is a Flask built-in concept, you can import it from the Flask library. While creating the object of the `Blueprint` class, the first parameter is the name you want to give to your Blueprint. This name will later be used for internal routing (we'll see below). 

The second parameter is the name of the Blueprint package, generally `__name__`. This helps locate the `root_path` for the blueprint. 

The third and fourth parameters passed are optional [keyword arguments](https://ashutoshkrris.hashnode.dev/what-are-args-and-kwargs-in-python). By defining the `template_folder` and `static_folder` parameters, you specify that you'll be using blueprint-specific templates and static files. 

### How to Define Routes with Blueprints

Now that you have created a blueprint for the admin related functionality, you can use it while creating routes for the admins.

```py
from flask import Blueprint


# Defining a blueprint
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@admin_bp.route('/admin')   # Focus here
def admin_home():
    return "Hello Admin!"
```

In the above snippet, focus on the line where the route is defined. Instead of the usual `@app.route('...')`, we have used `@admin_bp.route('...')`. This is how you bind a route to a particular blueprint.

### How to Register Your Blueprints

Now you have a blueprint and a route registered to it. But, will your app automatically know about this blueprint? 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-112849.png)
_No. You do it._

So, let's do it. In the `__init__.py` file, we will create a Flask app and register our blueprints there:

```py
from flask import Flask


app = Flask(__name__)

from .admin import routes

# Registering blueprints
app.register_blueprint(admin.admin_bp)

```

To register the blueprint, we use the `register_blueprint()` method and pass the name of the blueprint. Additionally, you can pass other parameters to the method for more customization. One such is `url_prefix` that you may require.

```py
app.register_blueprint(admin.admin_bp, url_prefix='/admin')
```

Similarly, you can register rest of your blueprints if you have more.

## Template Routing with Blueprints

Without Blueprints, in order to create links in your templates, you would use something similar to the below:

```html
<a href="{{ url_for('admin_home') }}">My Link</a>
```

But with blueprints in place, now you can define your links as:

```html
<a href="{{ url_for('admin_bp.admin_home') }}">My Link</a>
```

The `admin_bp` that we used above is the name we gave to our blueprint for internal routing while creating the object. 

To print the blueprint name of the Jinja2 template that the current page belongs to, you can use `{{request.blueprint}}`.

Note: To use Blueprint-specific assets, you can use the <a href="https://flask-assets.readthedocs.io/en/latest/">Flask-Assets</a> library.

## Wrapping Up

Blueprint is an amazing tool to organize and structure your Flask applications. 

In this article, you've learned what blueprints have to offer and how to use them in your Flask applications.

Thanks for reading!

You can follow me on [Twitter](https://twitter.com/ashutoshkrris)[.](https://ireadblog.com/)

