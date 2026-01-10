---
title: How to Set Up Email Verification in a Flask App
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-01-09T17:56:18.000Z'
originalURL: https://freecodecamp.org/news/setup-email-verification-in-flask-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-maksim-goncharenok-5605061.jpg
tags:
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
seo_title: null
seo_desc: 'Email verification is a crucial aspect of creating a new user account or
  signing up for a service. It helps confirm that the email address provided is valid
  and belongs to the intended user.

  In this article, we will explore the process of handling em...'
---

Email verification is a crucial aspect of creating a new user account or signing up for a service. It helps confirm that the email address provided is valid and belongs to the intended user.

In this article, we will explore the process of handling email verification in Flask. The topic will include setting up a route to handle the email verification process, and storing the verification status in a database. 

By the end of this article, you will have a thorough understanding of how to implement email verification in your own Flask application.

Before getting started, make sure you have a good understanding of basic user authentication in Flask. You can go through [this tutorial](https://ashutoshkrris.hashnode.dev/how-to-set-up-basic-user-authentication-in-a-flask-app) to learn more.

## **Project Demo**

Here’s what you're going to build in this tutorial:

%[https://www.youtube.com/watch?v=7o-wY65gHD8]

The link to the GitHub repository is available at the end of the tutorial. Feel free to check it out whenever you're stuck.

## Flask Basic User Authentication

To begin, you will use a Flask boilerplate that includes basic user authentication. You can get the code from [this repository](https://github.com/ashutoshkrris/Flask-User-Authentication). After creating and activating a virtual environment, run the following command to install all the dependencies:

```bash
$ pip install -r requirements.txt
```

Create a file named `.env` in the root directory and add the following content there:

```
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
```

Run the following command to export all the environment variables from the `.env` file:

```bash
source .env
```

Run the following commands to set up the database:

```bash
flask db init
flask db upgrade
```

Run the following command to run the Flask server:

```bash
python manage.py run
```

Once the app is running, go to [http://localhost:5000/register](http://localhost:5000/register) to register a new user. You will notice that after completing the registration, the app will automatically log you in and redirect you to the main page.

Before proceeding, I'd recommend exploring the app and then reviewing the code, particularly the **accounts** blueprint. This will give you a better understanding of how the user authentication is implemented.

## How to Modify the Current Implementation

In this section, you will modify the existing implementation of user authentication in our Flask app.

### Models

First of all, you'll need to add two new fields – `is_confirmed` and `confirmed_on` in the `User` model of your app.

Open the `src/accounts/models.py` file and update the `User` class with the following:

```python
class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(
        self, email, password, is_admin=False, is_confirmed=False, confirmed_on=None
    ):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed_on = confirmed_on

    def __repr__(self):
        return f"<email {self.email}>"
```

The `is_confirmed` is a boolean field to indicate whether the user's email address has been confirmed, set as not nullable and defaulting to `False`. The `confirmed_on` is a `datetime` field for the time when the user's email was confirmed, set as nullable.

To migrate and apply these changes in the database, run the following commands:

```bash
flask db migrate
flask db upgrade
```

### How to create the admin

Next, in the `manage.py` file, update the `create_admin` command to take the new database fields into account:

```python
@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    email = input("Enter email address: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords don't match")
    else:
        try:
            user = User(
                email=email,
                password=password,
                is_admin=True,
                is_confirmed=True,
                confirmed_on=datetime.now(),
            )
            db.session.add(user)
            db.session.commit()
            print(f"Admin with email {email} created successfully!")
        except Exception:
            print("Couldn't create admin user.")
```

Notice that the `is_confirmed` field is set to `True` in this case because you don't want the admin to verify their account.

### How to add a new decorator to check if the user is logged out

If you notice the `register()` and `login()` function in `src/accounts/views.py`, you'll find the below code in both of them:

```python
if current_user.is_authenticated:
    flash("You are already registered.", "info")
    return redirect(url_for("core.home"))
```

The code checks whether a user is already logged in. If the user is authenticated, a message is displayed using the `flash` function and the user is redirected to the home page using the `redirect` function from Flask. 

If the user is not authenticated, they will be allowed to continue with the process they were trying to complete. This essentially means you require the user to be logged out to continue the flow.

Instead of repeating the code at two places, you can create a decorator to check if the user is logged out.

Create a new `utils` folder in the `src` folder, and a `decorators.py` file in the `utils` folder with the following content:

```python
from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user


def logout_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            flash("You are already authenticated.", "info")
            return redirect(url_for("core.home"))
        return func(*args, **kwargs)

    return decorated_function
```

The above code defines a decorator called `logout_required` which is used to wrap routes in a Flask app. 

If the user is authenticated, a message is displayed using the `flash` function and the user is redirected to the home page using the `redirect` function from Flask. If the user is not authenticated, they will be allowed to continue and the decorated route function will be executed.

Now, you can use this decorator in the `register()` and `login()` function as below:

```python
from src.utils.decorators import logout_required


@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
	...
    
    
@accounts_bp.route("/login", methods=["GET", "POST"])
@logout_required
def login():
	...
```

## How to Add Email Verification to Your Flask App

In this section, you will learn how to add email verification to your Flask app.

### Confirmation token

The email confirmation should contain a unique URL that the user can click to confirm their account. The URL should be in the following format: `http://localhost:5000/confirm/<id>`. 

The `<id>` portion of the URL is a unique identifier that is generated using the user's email address and a timestamp. We can use the [itsdangerous](http://pythonhosted.org/itsdangerous/) package to encode this information in the `<id>`. When the user clicks the link, the app can decode the `<id>` to retrieve the user's email address and verify their account.

To provide an additional layer of security to the token, the `itsdangerours` package requires a password salt. You can set an environment variable for the same in the `.env` file:

```
other env vars...
export SECURITY_PASSWORD_SALT=fkslkfsdlkfnsdfnsfd
```

Run the following command to export the environment variable from the `.env` file:

```bash
source .env
```

Add the `SECURITY_PASSWORD_SALT` to your app’s config (`Config`) in the `config.py` file:

```python
class Config:
	...other configs
    SECURITY_PASSWORD_SALT = config("SECURITY_PASSWORD_SALT", default="very-important")
```

Create a `src/accounts/token.py` file and add the following code:

```python
from itsdangerous import URLSafeTimedSerializer

from src import app


def generate_token(email):
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=app.config["SECURITY_PASSWORD_SALT"])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=expiration
        )
        return email
    except Exception:
        return False

```

This code defines two functions for generating and confirming tokens for email verification in a Flask app:

The `generate_token` function takes an email address as an argument and returns a token that is generated using the `URLSafeTimedSerializer` class from the `itsdangerous` package. 

The `URLSafeTimedSerializer` class is initialized with the app's secret key, which is stored in the `SECRET_KEY` configuration variable. The `dumps` method of the `URLSafeTimedSerializer` instance is called with the email address and a password salt as arguments. As mentioned earlier, the password salt is stored in the `SECURITY_PASSWORD_SALT` configuration variable.

The `confirm_token` function takes a token and an optional expiration time as arguments and returns the email address that was used to generate the token. 

The `URLSafeTimedSerializer` instance is initialized with the app's secret key, and the `loads` method is called with the token, password salt, and expiration time as arguments. 

If the token is valid and has not expired, the email address is returned. If the token is invalid or has expired, an exception is raised and caught by the `except` block, causing the function to return `False`.

### How to update the `register()` function

When the user registers, you need to generate a token using the email address of the user.

```python
from src.accounts.token import confirm_token, generate_token


@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        token = generate_token(user.email)
        
        ...
```

The `token` variable will be used while sending an email to the user with the token included in the email's URL.

### How to handle email confirmation

To confirm the email, create a new view function in the `src/accounts/views.py` file:

```python
@accounts_bp.route("/confirm/<token>")
@login_required
def confirm_email(token):
    if current_user.is_confirmed:
        flash("Account already confirmed.", "success")
        return redirect(url_for("core.home"))
    email = confirm_token(token)
    user = User.query.filter_by(email=current_user.email).first_or_404()
    if user.email == email:
        user.is_confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash("You have confirmed your account. Thanks!", "success")
    else:
        flash("The confirmation link is invalid or has expired.", "danger")
    return redirect(url_for("core.home"))
```

The above code defines a route for the `confirm_email` view function in a Flask app. The route is decorated with the `@login_required` decorator, which requires the user to be logged in to access the view. The route takes a `token` argument, which is included in the URL of the route.

The view function first checks if the user's account is already confirmed. If the account is already confirmed, a message is displayed using the `flash` function from the Flask-Babel library and the user is redirected to the home page using the `redirect` function from Flask.

If the account is not confirmed, the `confirm_token` function is called with the `token` as an argument to confirm the token and retrieve the email address that was used to generate the token. If the token is invalid or has expired, the `confirm_token` function returns `False`, and a message is displayed indicating that the confirmation link is invalid or has expired.

If the token is valid, the user's account is confirmed by setting the `is_confirmed` field to `True` and the `confirmed_on` field to the current time. The changes are then committed to the database. A message is displayed indicating that the account has been confirmed, and the user is redirected to the home page.

### How to send email confirmation

Let's first create a basic email template that will be used while sending the email. Create a `templates/accounts/confirm_email.html` file and add the following code:

```html
<p>
  Welcome! Thanks for signing up. Please follow this link to activate your
  account:
</p>
<p><a href="{{ confirm_url }}">{{ confirm_url }}</a></p>
<br />
<p>Cheers!</p>

```

The `confirm_url` placeholder is used to insert a URL into the email message. When the template is rendered, the `confirm_url` placeholder is replaced with the actual URL that the user should visit to confirm their account.

#### How to set up Flask-Mail

Next, you'll need a library called `Flask-Mail` to send out emails using Flask.

Install the library using the pip command:

```bash
pip install Flask-Mail
```

Initialize the `Flask-Mail` library inside the `src/__init__.py` file as:

```python
...other imports...
from flask_mail import Mail

...other initializations...
mail = Mail(app)
...
```

You can set environment variables for your email and password that will be used to send emails in the `.env` file:

```
export EMAIL_USER=your-email
export EMAIL_PASSWORD=your-password
```

Run the following command to export the environment variables from the `.env` file:

```bash
source .env
```

Update the `Config` class in the `config.py` file:

```python
class Config(object):
    ...other configs

    # Mail Settings
    MAIL_DEFAULT_SENDER = "noreply@flask.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = config("EMAIL_USER")
    MAIL_PASSWORD = config("EMAIL_PASSWORD")
```

> Note: If your Gmail account has [2-step authentication](https://support.google.com/accounts/topic/28786?hl=en&ref_topic=3382253), Google will block the attempt. Use an [app password](https://support.google.com/accounts/answer/185833?hl=en) to sign in.

#### How to create a function to send email

Next, create a `email.py` file in the `src/utils` folder and add the following code:

```python
from flask_mail import Message

from src import app, mail


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config["MAIL_DEFAULT_SENDER"],
    )
    mail.send(msg)

```

The function takes three arguments: the recipient's email address (`to`), the subject of the email (`subject`), and the body of the email (`template`). 

The `Message` class from the Flask-Mail library is used to create a new email message with the specified subject and recipient. The `html` argument is used to set the body of the email to the provided `template`, which is expected to be an HTML string. The `sender` argument is used to specify the default sender for the email, which is stored in the `MAIL_DEFAULT_SENDER` configuration variable.

The `send` method of the `mail` object is then called with the message object as an argument to send the email. 

#### How to send the email (finally)

Let's finally send the confirmation email from the `register()` function:

```python
from src.utils.email import send_email


@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = generate_token(user.email)
        confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
        html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)

        flash("A confirmation email has been sent via email.", "success")
        return redirect(url_for("accounts.inactive"))

    return render_template("accounts/register.html", form=form)
```

The `url_for` function is then called to generate a URL for the `confirm_email` route with the `token` as an argument. The `_external` argument is set to `True` to generate an absolute URL with the full domain name. The `render_template` function is called to render an HTML template for the email message, using the `confirm_url` as a placeholder in the template.

The `send_email` function is then called to send the email with the rendered template as the body, using the user's email address as the recipient and a subject of "Please confirm your email".

Finally, the user is logged in using the `login_user` function from the Flask-Login library and a message is displayed indicating that a confirmation email has been sent. The user is then redirected to the `inactive` view. You'll create it later.

A sample email looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-05-234354.png)

## How to Handle Inactive Accounts

Whenever you create a new account, you're redirected to a view called `inactive` where you're asked to confirm your account.

Let's create a view function in the `src/accounts/views.py` file:

```python
@accounts_bp.route("/inactive")
@login_required
def inactive():
    if current_user.is_confirmed:
        return redirect(url_for("core.home"))
    return render_template("accounts/inactive.html")
```

The view function checks if the user's account is confirmed. If the account is confirmed, the user is redirected to the home page using the `redirect` function from Flask. If the account is not confirmed, the `inactive.html` template is rendered using the `render_template` function from Flask.

Let's create the `inactive.html` file in `templates/accounts` folder:

```html
{% extends "_base.html" %} {% block content %}

<div class="text-center">
  <h1>Welcome!</h1>
  <br />
  <p>
    You have not confirmed your account. Please check your inbox (and your spam
    folder) - you should have received an email with a confirmation link.
  </p>
  <p>
    Didn't get the email?
    <a href="{{ url_for('accounts.resend_confirmation') }}">Resend</a>.
  </p>
</div>

{% endblock %}

```

The template includes a link to the `resend_confirmation` route.

### How to resend the email

Consider a case where the user was not able to confirm the account before the expiration time of the token. As a user, you'll want to have an option to resend the email, right?

Create a new view function in the `src/accounts/views.py`:

```python
@accounts_bp.route("/resend")
@login_required
def resend_confirmation():
    if current_user.is_confirmed:
        flash("Your account has already been confirmed.", "success")
        return redirect(url_for("core.home"))
    token = generate_token(current_user.email)
    confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
    html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash("A new confirmation email has been sent.", "success")
    return redirect(url_for("accounts.inactive"))
```

This code defines a route for the `resend_confirmation` view function in a Flask app. The route is decorated with the `login_required` decorator, which requires the user to be logged in to access the view.

The view function first checks if the user's account is already confirmed. If the account is confirmed, a message is displayed indicating that the account has already been confirmed and the user is redirected to the home page.

If the account is not confirmed, a token is generated as earlier. The `url_for` function is then called to generate a URL for the `confirm_email` route with the `token` as an argument. The `send_email` function is then called to send the email with the rendered template as the body, using the user's email address as the recipient and a subject of "Please confirm your email". A message is displayed indicating that a new confirmation email has been sent, and the user is redirected to the `inactive` view.

### How to add middleware for routes

Now that you have the email verification mechanism ready, you want your routes in the `core` package to be accessed by only users with a confirmed account. To do that, you can add a decorator on those routes.

Create a new decorator in the `src/utils/decorators.py` file:

```python
def check_is_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed is False:
            flash("Please confirm your account!", "warning")
            return redirect(url_for("accounts.inactive"))
        return func(*args, **kwargs)

    return decorated_function
```

This code defines a decorator called `check_is_confirmed`. The decorator takes a function as an argument and returns a decorated function.

The decorator works by checking if the user's account is confirmed. If the account is not confirmed, a message is displayed warning the user to confirm their account, and the user is redirected to the `inactive` view. If the account is confirmed, the decorated function is called as usual.

Now, you can use this decorator in the `home` view function in `src/core/views.py` file:

```python
from src.utils.decorators import check_is_confirmed


@core_bp.route("/")
@login_required
@check_is_confirmed
def home():
    return render_template("core/index.html")
```

This is how it looks when you login, and your account is not verified:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-05-234723.png)

## How to Add New Test Cases

Now that you have added the main functionality, it's time to update the test suite.

### How to modify the `setUp()` method in `base_test.py`

Replace the `setUp()` method with the following code:

```python
def setUp(self):
    db.create_all()
    unconfirmed_user = User(email="unconfirmeduser@gmail.com",
                                password="unconfirmeduser")
    db.session.add(unconfirmed_user)
    confirmed_user = User(email="confirmeduser@gmail.com",
                              password="confirmeduser", is_confirmed=True)
    db.session.add(confirmed_user)
    db.session.commit()
```

The method now creates two users – a user with a confirmed account and another user without a confirmed account.

Note that you'll need to replace the usage of the old email address and password with the unconfirmed user's email address and password in all the test files.

### How to add new test cases in `test_routes.py`

Since unauthenticated users cannot access the home page, let's add a test case in the `TestLoggingInOut` class to see if the user is redirected to the login page:

```python
def test_home_route_requires_login(self):
    self.client.get("/logout", follow_redirects=True)
    self.client.get('/', follow_redirects=True)
    self.assertTemplateUsed('accounts/login.html')
```

Create a new `TestEmailConfirmationToken` class in the same file:

```python
class TestEmailConfirmationToken(BaseTestCase):
    def test_confirm_token_route_requires_login(self):
        # Ensure confirm/<token> route requires logged in user.
        self.client.get("/logout", follow_redirects=True)
        self.client.get('/confirm/some-unique-id', follow_redirects=True)
        self.assertTemplateUsed('accounts/login.html')

    def test_confirm_token_route_valid_token(self):
        # Ensure user can confirm account with valid token.
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post('/login', data=dict(
                email='unconfirmeduser@gmail.com', password='unconfirmeduser'
            ), follow_redirects=True)
            token = generate_token('unconfirmeduser@gmail.com')
            response = self.client.get(
                '/confirm/'+token, follow_redirects=True)
            self.assertIn(
                b'You have confirmed your account. Thanks!', response.data)
            self.assertTemplateUsed('core/index.html')
            user = User.query.filter_by(
                email='unconfirmeduser@gmail.com').first_or_404()
            self.assertIsInstance(user.confirmed_on, datetime)
            self.assertTrue(user.is_confirmed)

    def test_confirm_token_route_invalid_token(self):
        # Ensure user cannot confirm account with invalid token.
        token = generate_token('test@test1.com')
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post('/login', data=dict(
                email='unconfirmeduser@gmail.com', password='unconfirmeduser'
            ), follow_redirects=True)
            response = self.client.get('/confirm/'+token,
                                       follow_redirects=True)
            self.assertIn(
                b'The confirmation link is invalid or has expired.',
                response.data
            )

    def test_confirm_token_route_expired_token(self):
        # Ensure user cannot confirm account with expired token.
        user = User(email='test@test1.com', password='test1')
        db.session.add(user)
        db.session.commit()
        token = generate_token('test@test1.com')
        self.assertFalse(confirm_token(token, -1))
```

The above code tests the email verification functionality of the app.

* The `test_confirm_token_route_requires_login` test case tests that when a user tries to access the confirmation route when not logged in, they are redirected to the login page.
* The `test_confirm_token_route_valid_token` test case tests that when a user tries to access the confirmation route with a valid token, their account is confirmed and they are redirected to the index page.
* The `test_confirm_token_route_invalid_token` test case tests that when a user tries to access the confirmation route with an invalid token, an error message is displayed.
* The `test_confirm_token_route_expired_token` test case tests that when a user tries to access the confirmation route with an expired token, an error message is displayed.

## **Wrapping up**

In this tutorial, you learned how to handle email verification in your Flask app. You also wrote few more testcases in order to test the new functionalities.

Here's the link to the [GitHub repository](https://github.com/ashutoshkrris/Flask-User-Authentication-With-Email-Verification). Feel free to check it out whenever you're stuck.

### **Recommended next steps**

* You can add a "forgot password" feature in the application.
* You can allow users to manage their profiles.
* You can add more testcases in order to test the app more thoroughly.

Thank you for reading. I hope you found this article useful. You can follow me on [Twitter](https://twitter.com/ashutoshkrris).

