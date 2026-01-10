---
title: How to Set Up Basic User Authentication in a Flask App
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-01-03T14:57:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-user-authentication-in-flask
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/basic-auth.png
tags:
- name: authentication
  slug: authentication
- name: Flask Framework
  slug: flask
seo_title: null
seo_desc: User authentication is important for protecting sensitive information and
  resources from unauthorized access. It helps ensure that only authorized users can
  access and make changes to data, and helps prevent unauthorized users from gaining
  access to ...
---

User authentication is important for protecting sensitive information and resources from unauthorized access. It helps ensure that only authorized users can access and make changes to data, and helps prevent unauthorized users from gaining access to sensitive information.

There are different methods for implementing user authentication, including password-based authentication, token-based authentication, and so on. 

In this tutorial, you will learn how to set up basic user authentication – that is password-based authentication – in your Flask application.

## Project Demo

Here’s what the final output will look like:

%[https://www.youtube.com/watch?v=XxSESg89xEI]

The link to the GitHub repository is available at the end of the tutorial. Feel free to check it out whenever you're stuck.

## Prerequisites

Before you get started with the tutorial, make sure you have the following requirements satisfied:

* Working knowledge of Python
* Python 3.8+ installed on your system
* Basic knowledge of [Flask](https://ashutoshkrris.hashnode.dev/getting-started-with-flask) and [Flask Blueprints](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps)

## Get Your Tools Ready

You'll need a few external libraries in this project. Let's learn more about them and install them one by one.

But before we install them, let's create a virtual environment and activate it.

First, start with creating the project directory and navigating to it like this:

```bash
mkdir flask-basic-auth
ccd flask-basic-auth
```

We are going to create a virtual environment using `venv`. Python now ships with a pre-installed `venv` library. So, to create a virtual environment, you can use the below command:

```bash
python -m venv env
```

The above command will create a virtual environment named env. Now, we need to activate the environment using this command:

```bash
source env/Scripts/activate
```

To verify if the environment has been activated or not, you can see `(env)` in your terminal. Now, we can install the libraries.

* [Flask](https://flask.palletsprojects.com/en/2.2.x/) is a simple, easy-to-use microframework for Python that helps you build scalable and secure web applications.
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/) is a Flask extension that provides bcrypt hashing utilities for your application.
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) is a simple integration of Flask and WTForms that helps you create forms in Flask.
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface.
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is an extension for Flask that adds support for SQLAlchemy to your application. It helps you simplify things using SQLAlchemy with Flask by giving you useful defaults and extra helpers that make it easier to perform common tasks.
* [Flask-Testing](https://pythonhosted.org/Flask-Testing/) extension provides unit testing utilities for Flask.
* [Python Decouple](https://pypi.org/project/python-decouple/) helps you use environment variables in your Python project.

To install the above-mentioned libraries, run the following command:

```bash
pip install Flask Flask-Login Flask-Bcrypt Flask-WTF FLask-Migrate Flask-SQLAlchemy Flask-Testing python-decouple
```

> This tutorial was verified with Python V3.11, Flask V2.2.2, Flask-Login V0.6.0, Flask-Bcrypt V1.0.1, Flask-WTF V1.0.1, Flask-SQLAlchemy V2.5.1 and, Flask-Testing V0.8.1.

## How to Set Up the Project

Let’s start by creating a `src` directory:

```bash
mkdir src
```

The first file will be the `__init__.py` file for the project:

```python
from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
```

In the above script, we created a Flask app called `app` . We use the `__name__` argument to indicate the app's module or package so that Flask knows where to find other files such as templates. You also set the configuration of the app using an environment variable called `APP_SETTINGS`. You'll export it later.

To use Flask-Bcrypt, Flask-SQLAlchemy, and Flask-Migrate in your application, you just need to create objects of the `Bcrypt`, `SQLAlchemy` and `Migrate` classes from the `flask_bcrypt`, `flask_sqlalchemy` and, `flask_migrate` libraries, respectively.

You've also registered blueprints called `accounts_bp` and `core_bp` in the application. You'll define them later in the tutorial.

In the root directory of the project (that is, outside the `src` directory), create a file called `config.py`. We'll store the configurations for the project in this file. Within the file, add the following content:

```python
from decouple import config

DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default="guess-me")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False

```

In the above script, we have created a `Config` class and defined various attributes inside that. Also, we have created different child classes (as per different stages of development) that inherit the `Config` class.

Notice that we're using a few environment variables like `SECRET_KEY` and `DATABASE_URL`. Create a file named `.env` in the root directory and add the following content there:

```
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
```

Apart from the `SECRET_KEY` and `DATABASE_URL`, we've also exported `APP_SETTINGS`, `DEBUG`, `FLASK_APP`, and `FLASK_DEBUG`. 

The `APP_SETTINGS` refers to one of the classes we created in the `config.py` file. We set it to the current stage of the project. 

The value of `FLASK_APP` is the name of the package we have created. Since the app is in the development stage, you can set the values of `DEBUG` and `FLASK_DEBUG` to `True` and `1`, respectively.

Run the following command to export all the environment variables from the `.env` file:

```bash
source .env
```

Next, you'll create a CLI application of the app so that you can later add custom commands such as `test` and `create_admin` in order to test the application and create admin, respectively. 

Create a `manage.py` file in the root directory of the application and add the following code:

```python
from flask.cli import FlaskGroup

from src import app

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()

```

Now, your basic application is ready. You can run it using the following command:

```bash
python manage.py run
```

## How to Create Blueprints for Accounts and Core

As mentioned earlier, you'll use the concepts of blueprints in the project. Let's create two blueprints – `accounts_bp` and `core_bp` – in this section.

First create a directory called `accounts` like this:

```bash
mkdir accounts
cd accounts
```

Next, add an empty `__init__.py` file to covert it into a Python package. Now, create a `views.py` file inside the package where you'll store all your routes related to user authentication.

```bash
touch __init__.py views.py
```

Add the following code inside the `views.py` file:

```python
from flask import Blueprint

accounts_bp = Blueprint("accounts", __name__)
```

In the above script, you have created a blueprint called `accounts_bp` for the `accounts` package.

Similarly, you can create a `core` package in the root directory, and add a `views.py` file.

```bash
mkdir core
cd core
touch __init__.py views.py
```

Now, add the following code inside the `views.py` file:

```python
from flask import Blueprint

core_bp = Blueprint("core", __name__)
```

Note: If you're new to Flask Blueprints, make sure you go through [this tutorial](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps) to learn more about how it works.

## How to Create a User Model

Let's create a `models.py` file inside the `accounts` package.

```bash
touch src/accounts/models.py
```

Inside the `models.py` file, add the following code:

```python
from datetime import datetime

from src import bcrypt, db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"

```

In the above code, you created a `User` model by inheriting the `db.Model` class. The `User` model consists of the following fields:

* `id`: stores the primary key for the `users` table
* `email`: stores the email of the user
* `password`: stores the hashed password of the user
* `created_on`: stores the timestamp when the user was created
* `is_admin`: stores whether the user is admin or not

In the constructor of the class, you set the fields. Notice the password field where you generate the hash of the password using the `bcrypt` object imported from the app. 

## How to Add Flask-Login

The most important part of Flask-Login is the `LoginManager` class that lets your application and Flask-Login work together. 

In the `src/__init__.py` file, add the following code:

```python
from decouple import config
from flask import Flask
from flask_login import LoginManager # Add this line
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager() # Add this line
login_manager.init_app(app) # Add this line
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
```

In the above script, you created and initialized the login manager in your app.

Next, you need to provide a `user_loader` callback. This callback is used to reload the user object from the user ID stored in the session. It should take the ID of a user, and return the corresponding user object.

```python
from src.accounts.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
```

The `User` model should implement the following properties and methods:

* `is_authenticated`: This property returns True if the user is authenticated.
* `is_active`: This property returns True if this is an active user (the account is activated)
* `is_anonymous`: This property returns True if this is an anonymous user (actual users return False).
* `get_id()`: This method returns a string that uniquely identifies this user, and can be used to load the user from the `user_loader` callback. 

Now, you don't need to implement these explicitly. Instead, the Flask-Login provides a `UserMixin` class that contains the default implementations for all of these properties and methods. You just need to inherit it in the following way:

```python
from datetime import datetime

from flask_login import UserMixin # Add this line

from src import bcrypt, db


class User(UserMixin, db.Model): # Change this line

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"

```

You can also customize the default login process in the `src/__init__.py` file.

The name of the login view can be set as `LoginManager.login_view`. The value refers to the function name that will handle the login process.

```python
login_manager.login_view = "accounts.login"
```

To customize the message category, set `LoginManager.login_message_category`:

```python
login_manager.login_message_category = "danger"
```

## How to Add Templates and Static Files

Let's create a CSS file called `styles.css` inside the `src/static` folder:

```css
.error {
  color: red;
  margin-bottom: 5px;
  text-align: center;
}

a {
  text-decoration: none;
}

```

Let's also create the basic templates inside the `src/templates` folder. Create a `_base.html` file and add the following code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask User Management</title>
    <!-- meta -->
    <meta name="description" content="">
    <meta name="author" content="">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <!-- styles -->
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <link rel="stylesheet" href="{{url_for('static', filename="styles.css")}}">
    {% block css %}{% endblock %}
  </head>
  <body>

    {% include "navigation.html" %}

    <div class="container">

      <br>

      <!-- messages -->
      {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4">
          {% for category, message in messages %}
          <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
           {{message}}
           <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
          {% endfor %}
        </div>
        <div class="col-md-4"></div>
      </div>
      {% endif %}
      {% endwith %}

      <!-- child template -->
      {% block content %}{% endblock %}

    </div>

    <!-- scripts -->
    <script src="https://code.jquery.com/jquery-3.6.1.min.js" type="text/javascript"></script>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    {% block js %}{% endblock %}
  </body>
</html>
```

The `_base.html` is the parent HTML file that will be inherited by the other templates. We have added Bootstrap 5 support in the above file. We are also making use of Flask Flashes to show Bootstrap alerts in the app.

Let's also create a `navigation.html` file that contains the navbar of the app:

```html
<!-- Navigation -->
<header class="p-3 text-bg-dark">
  <div class="container">
    <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
      <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        <li><a href="{{ url_for('core.home') }}" class="nav-link px-2 text-secondary">Home</a></li>
      </ul>

      <div class="text-end">
        {% if current_user.is_authenticated %}
        <a href="{{ url_for('accounts.logout') }}"><button type="button" class="btn btn-danger me-2">Logout</button></a>
        {% else %}
          <a href="{{ url_for('accounts.login') }}"><button type="button" class="btn btn-outline-light me-2">Login</button></a>
          <a href="{{ url_for('accounts.register') }}"><button type="button" class="btn btn-success">Sign up</button></a>
        {% endif %}
          
      </div>
    </div>
  </div>
</header>
```

Note that we have not yet created the views used above.

## How to Create the Homepage

In this section, you'll first create a view function for the homepage inside the `core/views.py` file. Add the following code there:

```python
from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")

```

Notice that we have used the blueprint to add the route. We also added a `@login_required` middleware to prevent access from unauthenticated users. 

Next, let's create an `index.html` file inside the `templates/core` folder, and add the following code:

```html
{% extends "_base.html" %}
{% block content %}

<h1 class="text-center">Welcome {{current_user.email}}!</h1>

{% endblock %}
```

The HTML page will just have a welcome message for authenticated users.

## How to Implement User Registration

First of all, we'll create a registration form using Flask-WTF. Create a `forms.py` file inside the `accounts` package and add the following code:

```python
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User


class RegisterForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True

```

The `RegisterForm` extends the `FlaskForm` class and contains three fields – `email`, `password`, and `confirm`. We have added different validators such as `DataRequired`, `Length`, `Email`, and `EqualTo` to the respective fields.

We also defined a `validate()` method which is automatically called when the form is submitted. 

Inside the method, we first perform the initial validation provided by FlaskForm. If that is successful, we perform our custom validation such as checking whether user is already registered, and matching the password with the confirmed password. If there are any errors, we append the error message in the respective fields.

Let's use this form in the `views.py` to create a function to handle the registration process.

```python
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user

from src import db
from src.accounts.models import User

from .forms import RegisterForm


@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return redirect(url_for("core.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("You registered and are now logged in. Welcome!", "success")

        return redirect(url_for("core.home"))

    return render_template("accounts/register.html", form=form)
```

In the above function, notice that we're using the blueprint to add the route for the function. Initially, we check if a user is already authenticated using the `is_authenticated` property. If it is, we redirect it to the homepage with a message.

If no user is authenticated, we first create an instance of the `RegisterForm` class. If the request method is GET, we render an HTML file with the form. Otherwise, we check if the form has valid inputs using the `validate_on_submit()` method. 

If the inputs are valid, we create an instance of the `User` class with the email and password provided by the user, and add it to the database. 

Next, we login the user using the `login_user()` method that accepts the `user` object. We also flash a success message and redirect the user to the homepage.

Now, let's use this form inside the HTML file. Create an `accounts` directory inside the `templates` folder and add a new file called `register.html` inside it. Add the following code:

```html
{% extends "_base.html" %}

{% block content %}

<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4">
    <main class="form-signin w-100 m-auto">
      <form role="form" method="post" action="">
        {{ form.csrf_token }}
        <h1 class="h3 mb-3 fw-normal text-center">Please register</h1>

        <div class="form-floating">
          {{ form.email(placeholder="email", class="form-control mb-2") }}
          {{ form.email.label }}
            {% if form.email.errors %}
              {% for error in form.email.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.password(placeholder="password", class="form-control mb-2") }}
          {{ form.password.label }}
            {% if form.password.errors %}
              {% for error in form.password.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.confirm(placeholder="Confirm Password", class="form-control mb-2") }}
          {{ form.confirm.label }}
            {% if form.confirm.errors %}
              {% for error in form.confirm.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
        <p class="text-center mt-3">Already registered? <a href="{{ url_for('accounts.login') }}">Login now</a></p>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}
```

In the above code, we created an HTML form where we make use of the `form` instance that contains the form fields with their labels and errors. We have used a `accounts.login` view function which doesn't exist yet.

## How to Implement User Login and Logout

First, let's create a login form in the `accounts/forms.py` file:

```python
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
```

The form is similar to the registration form but it has only two fields – `email` and `password`.

Next, let's create a view function to handle the login process inside the `accounts/views.py` file:

```python
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user

from src import bcrypt, db
from src.accounts.models import User

from .forms import LoginForm, RegisterForm


@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("accounts/login.html", form=form)
    return render_template("accounts/login.html", form=form)

```

Similar to registration view function, we first check if a user is already authenticated using the `is_authenticated` property. If it is, we redirect it to the homepage with a message.

If not authenticated, we create an instance of the login form. If the request method is GET, we simply render a `login.html` file with the form. Otherwise, the form is validated. 

During the validation, we use the `check_password_hash` method from the `Flask-Bcrypt` library to match the hashed passwords. If the passwords match, we login the user using the `login_user()` method and redirect to the homepage. Otherwise, we flash an error message and render the same HTML page.

Now, let's create a `login.html` file inside the `templates/accounts` folder: 

```html
{% extends "_base.html" %}

{% block content %}

<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4">
    <main class="form-signin w-100 m-auto">
      <form role="form" method="post" action="">
        {{ form.csrf_token }}
        <h1 class="h3 mb-3 fw-normal text-center">Please sign in</h1>

        <div class="form-floating">
          {{ form.email(placeholder="email", class="form-control mb-2") }}
          {{ form.email.label }}
            {% if form.email.errors %}
              {% for error in form.email.errors %}
              <div class="alert alert-danger" role="alert">
                {{ error }}
              </div>
              {% endfor %}
            {% endif %}
        </div>
        <div class="form-floating">
          {{ form.password(placeholder="password", class="form-control mb-2") }}
          {{ form.password.label }}
            {% if form.password.errors %}
              {% for error in form.password.errors %}
                <div class="alert alert-danger" role="alert">
                  {{ error }}
                </div>
              {% endfor %}
            {% endif %}
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        <p class="text-center mt-3">New User? <a href="{{ url_for('accounts.register') }}">Register now</a></p>
      </form>
    </main>
  </div>
  <div class="col-md-4"></div>
</div>

{% endblock %}
```

The login form is similar to the registration form but with just two fields for the email and password.

Logging out the user is a very simple process. You just need to create a view function for it inside the `accounts/views.py` file:

```python
from flask_login import login_required, login_user, logout_user


@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login"))

```

The `Flask-Login` library contains a `logout_user` method that removes the user from the session. We used the `@login_required` decorator so that only authenticated users can logout.

## How to Run the Completed App for the First Time

Now that your application is ready (without the tests), you can first migrate the database, and then run the app.

* To initialize the database (create a migration repository), use the command:

```bash
flask db init
```

* To migrate the database changes, use the command:

```bash
flask db migrate
```

* To apply the migrations, use the command:

```bash
flask db upgrade
```

Since this is the first time we're running our app, you'll need to run all the above commands. Later, whenever you make changes to the database, you'll just need to run the last two commands.

After that, you can run your application using the command:

```
python manage.py run
```

## How to Add Unit Tests to the App

Now that we have all the features ready, create a `tests` folder in the root directory and convert it into a package by adding an empty `__init__.py` file.

### How to Create a Base TestCase

Let's create a base testcase that will be extended by the other testcases. Create a `base_test.py` file inside the `tests` package, and add the following code:

```python
import os

from flask_testing import TestCase

from src import app, db
from src.accounts.models import User


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        testdb_path = os.path.join("src", "testdb.sqlite")
        os.remove(testdb_path)

```

The `BaseTestCase` class extends the `TestCase` class and implements the following three methods:

* The `create_app()` method is a required method which should return a Flask instance. If you don’t define `create_app()`,  `NotImplementedError` will be raised. Notice that we're using the `TestingConfig` in this case.
* The `setUp()` method is called before running any test. In this method, we create all the database tables. Additionally, we also create a user so that we can play with it later.
* The `tearDown()` method is called after running all the testcases. So, in this method, we'll clean up all the test data.

### How to Write Tests for Forms

In the above sections, we created two forms – `RegisterForm` and `LoginForm`. Let's test these forms in a new test file named `test_forms.py` inside the `tests` package.

```python
import unittest

from base_test import BaseTestCase

from src.accounts.forms import LoginForm, RegisterForm


class TestRegisterForm(BaseTestCase):
    def test_validate_success_register_form(self):
        # Ensure correct data validates.
        form = RegisterForm(email="new@test.com", password="example", confirm="example")
        self.assertTrue(form.validate())

    def test_validate_invalid_password_format(self):
        # Ensure incorrect data does not validate.
        form = RegisterForm(email="new@test.com", password="example", confirm="")
        self.assertFalse(form.validate())

    def test_validate_email_already_registered(self):
        # Ensure user can't register when a duplicate email is used
        form = RegisterForm(
            email="ad@min.com", password="admin_user", confirm="admin_user"
        )
        self.assertFalse(form.validate())


class TestLoginForm(BaseTestCase):
    def test_validate_success_login_form(self):
        # Ensure correct data validates.
        form = LoginForm(email="ad@min.com", password="admin_user")
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # Ensure invalid email format throws error.
        form = LoginForm(email="unknown", password="example")
        self.assertFalse(form.validate())


if __name__ == "__main__":
    unittest.main()

```

The `TestRegisterForm` class defines three test methods to test the `validate` method of the `RegisterForm` class. 

The first test method tests that the form validates with correct input data. The second test method tests that the form does not validate with an invalid password format. And the third test method tests that the form does not validate when a duplicate email is used to register.

The `TestLoginForm` class defines two test methods to test the `validate` method of the `LoginForm` class. The first test method tests that the form validates with correct input data, and the second test method tests that the form does not validate with an invalid email format.

### How to Test the User Model

Let's now test the `User` model in a new file named `test_models.py` inside the `tests` package.

```py
import datetime
import unittest

from base_test import BaseTestCase
from flask_login import current_user

from src import bcrypt
from src.accounts.models import User


class TestUser(BaseTestCase):
    def test_user_registration(self):
        # Ensure user registration behaves correctly.
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post(
                "/register",
                data=dict(
                    email="test@user.com", password="test_user", confirm="test_user"
                ),
                follow_redirects=True,
            )
            user = User.query.filter_by(email="test@user.com").first()
            self.assertTrue(user.id)
            self.assertTrue(user.email == "test@user.com")
            self.assertFalse(user.is_admin)

    def test_get_by_id(self):
        # Ensure id is correct for the current/logged in user
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            self.assertTrue(current_user.id == 1)

    def test_created_on_defaults_to_datetime(self):
        # Ensure that registered_on is a datetime
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            user = User.query.filter_by(email="ad@min.com").first()
            self.assertIsInstance(user.created_on, datetime.datetime)

    def test_check_password(self):
        # Ensure given password is correct after unhashing
        user = User.query.filter_by(email="ad@min.com").first()
        self.assertTrue(bcrypt.check_password_hash(user.password, "admin_user"))
        self.assertFalse(bcrypt.check_password_hash(user.password, "foobar"))

    def test_validate_invalid_password(self):
        # Ensure user can't login when the pasword is incorrect
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            response = self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="foo_bar"),
                follow_redirects=True,
            )
        self.assertIn(b"Invalid email and/or password.", response.data)


if __name__ == "__main__":
    unittest.main()
```

The `TestUser` class defines four test methods to test various aspects of the `User` model class. 

* The first test method tests the user registration process by posting a registration request to the server with the `client` object, which is a Flask test client. The test verifies that a new user is correctly added to the database and that the user's attributes are correctly set.
* The second test method tests the `get_by_id` method, which is a helper method to get the user object from the database by its id. The test logs in a user and verifies that the current user's id is correct.
* The third test method tests that the `created_on` attribute of the user object is a datetime object.
* The fourth test method tests the `check_password` method, which is a helper method to check the user's password. The test verifies that the method correctly checks a correct and an incorrect password.
* The fifth test method tests the login process by posting a login request to the server with the `client` object and verifies that the server responds with an error message when the password is incorrect.

### How to Test the Routes

Let's now test the routes in a new file named `test_routes.py` inside the `tests` package.

```python
import unittest

from base_test import BaseTestCase
from flask_login import current_user


class TestPublic(BaseTestCase):
    def test_main_route_requires_login(self):
        # Ensure main route requres logged in user.
        response = self.client.get("/", follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        self.assertIn(b"Please log in to access this page", response.data)

    def test_logout_route_requires_login(self):
        # Ensure logout route requres logged in user.
        response = self.client.get("/logout", follow_redirects=True)
        self.assertIn(b"Please log in to access this page", response.data)


class TestLoggingInOut(BaseTestCase):
    def test_correct_login(self):
        # Ensure login behaves correctly with correct credentials
        with self.client:
            response = self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            self.assertTrue(current_user.email == "ad@min.com")
            self.assertTrue(current_user.is_active)
            self.assertTrue(response.status_code == 200)

    def test_logout_behaves_correctly(self):
        # Ensure logout behaves correctly, regarding the session
        with self.client:
            self.client.post(
                "/login",
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True,
            )
            response = self.client.get("/logout", follow_redirects=True)
            self.assertIn(b"You were logged out.", response.data)
            self.assertFalse(current_user.is_active)


if __name__ == "__main__":
    unittest.main()

```

The `TestPublic` class defines two test methods to test the access control of certain routes. 

The first test method tests that the main route requires a logged-in user by attempting to access it with the `client` object, which is a Flask test client. The test verifies that the server responds with a login prompt. The second test method tests that the logout route also requires a logged-in user.

The `TestLoggingInOut` class defines two test methods to test the login and logout functionality. 

The first test method tests the login process by posting a login request to the server with the `client` object and verifies that the server responds with a successful login. The second test method tests the logout process by posting a logout request to the server with the `client` object. It then verifies that the server responds with a logout message and that the user is no longer logged in.

### How to Run the Tests

Now that we have all the tests ready, we are ready to run the testcases. But before that, as mentioned in the beginning, we'll need to add a command in the `manage.py` file to run the tests.

```python
import unittest


@cli.command("test")
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1
```

The command runs the unit tests in the `tests` package and displays the results in the terminal.

You use the `unittest.TestLoader().discover()` method to discover and run all the unit tests in the `tests` package. You use the `unittest.TextTestRunner()` method to run the unit tests and to print the results to the terminal. The `verbosity` argument controls the level of detail in the output.

If all the unit tests pass, the `test` command returns a exit code of 0. If any of the unit tests fail, the command returns a exit code of 1.

Now, you can run all the tests using the command:

```bash
python manage.py test
```

This will give the below output:

```bash
test_validate_invalid_email_format (test_forms.TestLoginForm) ... ok
test_validate_success_login_form (test_forms.TestLoginForm) ... ok
test_validate_email_already_registered (test_forms.TestRegisterForm) ... ok
test_validate_invalid_password_format (test_forms.TestRegisterForm) ... ok
test_validate_success_register_form (test_forms.TestRegisterForm) ... ok
test_check_password (test_models.TestUser) ... ok
test_created_on_defaults_to_datetime (test_models.TestUser) ... ok
test_get_by_id (test_models.TestUser) ... ok
test_user_registration (test_models.TestUser) ... ok
test_validate_invalid_password (test_models.TestUser) ... ok
test_correct_login (test_routes.TestLoggingInOut) ... ok
test_logout_behaves_correctly (test_routes.TestLoggingInOut) ... ok
test_logout_route_requires_login (test_routes.TestPublic) ... ok
test_main_route_requires_login (test_routes.TestPublic) ... ok

----------------------------------------------------------------------
Ran 14 tests in 19.577s

OK
```

## Features to Add to Your Application

Here are some extra things you can add in your application. Note that these are optional.

### How to Create an Admin

Similar to the `test` command, you can add a `create_admin` command to create an admin in your application. Add the following code inside the `manage.py` file:

```python
import getpass


@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    email = input("Enter email address: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords don't match")
        return 1
    try:
        user = User(email=email, password=password, is_admin=True)
        db.session.add(user)
        db.session.commit()
    except Exception:
        print("Couldn't create admin user.")
```

The command prompts the user to enter an email address and a password for the admin user. The password is entered using the `getpass` module, which hides the password input from the terminal. The command then checks if the entered password and the confirmed password match. If the passwords don't match, the command prints an error message and returns a exit code of 1.

If the passwords match, the command creates a new `User` object with the entered email address, password, and the `is_admin` attribute set to `True`. The command then adds the user object to the database session and commits the changes to the database. If an exception is raised during this process, the command prints an error message.

You can run the below command to create one:

```bash
python manage.py create_admin
```

Output:

```bash
> python manage.py create_admin
Enter email address: admin@myapp.com
Enter password: 
Enter password again: 
Admin with email admin@myapp.com created successfully!
```

### How to Create Error Pages

Our application can get errors at any time. The most common errors that we get are Unauthorized (401), Not Found (404) and Server Error (500). 

Let's create an `errors` directory inside the `templates` directory and create three HTML pages as below:

* 401.html

```html
{% extends "_base.html" %}
{% block content %}
<h1>401</h1>
<p>Run along!</p>
<p><em>Return <a href="{{url_for('core.home')}}">Home</a>?</em></p>
{% endblock %}

```

* 404.html

```html
{% extends "_base.html" %}
{% block content %}
<h1>404</h1>
<p>There's nothing here!</p>
<p><em>Return <a href="{{url_for('core.home')}}">Home</a>?</em></p>
{% endblock %}

```

* 500.html

```html
{% extends "_base.html" %}
{% block content %}
<h1>500</h1>
<p>Something's wrong! We are on the job.</p>
<p><em>Return <a href="{{url_for('core.home')}}">Home</a>?</em></p>
{% endblock %}

```

Next, we need to add error handlers for these errors. Open the `src/__init__.py` file and add the following code in the bottom of the file:

```python
@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500

```

This above code snippet registers error handler functions for the HTTP error codes 401, 404, and 500 in a Flask application. An error handler function is a function that is called when an error occurs in the application.

The error handler functions are decorated with the `@app.errorhandler` decorator, which registers them with the Flask application. The decorator takes an error code as an argument, and the function is called when the error code is raised.

Each error handler function returns a rendered template and the error code as a response to the client. The templates are HTML files located in the `errors` folder and contain the content to be displayed to the user for each error. The error code is passed as an argument to the `render_template` function to determine which template to render.

## Wrapping up

In this tutorial, you learned how to set up basic user authentication in your Flask app. You also wrote few testcases in order to test the functionalities.

Here's the link to the [GitHub repository](https://github.com/ashutoshkrris/Flask-User-Authentication). Feel free to check it out whenever you're stuck.

### Recommended next steps

* You can add more security such as email verification, or token-based authentication in the app.
* You can add a "forgot password" feature in the application.
* You can add more testcases in order to test the app more thoroughly.

Thank you for reading. I hope you found this article useful. You can follow me on [Twitter](https://twitter.com/ashutoshkrris).

