---
title: How to Use an Email Validation Service for Flask User Authentication
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-03-30T22:22:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-email-validation-api-for-flask-user-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/email-validation-1.png
tags:
- name: authentication
  slug: authentication
- name: email
  slug: email
- name: Flask Framework
  slug: flask
seo_title: null
seo_desc: "In today's digital world, online security is really important, and user\
  \ authentication is a key aspect of it. \nEmail-based authentication is one of the\
  \ most popular and widely used methods for user registration and login. But it's\
  \ not always reliable..."
---

In today's digital world, online security is really important, and user authentication is a key aspect of it. 

[Email-based authentication](https://ashutoshkrris.hashnode.dev/how-to-set-up-email-verification-in-a-flask-app) is one of the most popular and widely used methods for user registration and login. But it's not always reliable, as users can enter fake or invalid email addresses during registration. This can lead to security risks and fraud. This is where Email Validation Services come in handy.

In this tutorial, you'll use the [Email Validation Service](https://emailvalidation.io/) to help you automate your email validation process during user registration by validating contact information. 

The API checks the syntax, domain, and mailbox of an email address, and can even detect disposable and risky emails. 

By integrating this API with your application, you can ensure that only valid and genuine email addresses are used for user registration, which will enhance the security of your application.

## Prerequisites

Before you get started with the tutorial, make sure you have satisfied the following requirements:

* Working knowledge of Python
* Python 3.8+ installed on your system
* Basic knowledge of [Flask](https://ashutoshkrris.hashnode.dev/getting-started-with-flask), [Flask Blueprints](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps) and [Requests](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python).

## How to Set Up the Virtual Environment

Before you start coding, you'll need to make sure you have all the necessary tools and libraries installed. To ensure that you have a clean and isolated environment, you'll create a virtual environment using `venv`.

Create a project directory and navigate to it in the terminal:

```bash
mkdir email-validation
cd email-validation

```

Create a virtual environment named `env` using the following command:

```bash
python -m venv env
```

Python now ships with pre-installed `venv` library to create virtual environments.

Activate the virtual environment like this:

```bash
source env/bin/activate
```

Note: If you're on Windows, you'll need to use `source env/Scripts/activate` to activate the environment.

You should see `(env)` in your terminal prompt, indicating that the virtual environment has been activated.

## How Email Validation Service Works

Email validation is an essential process for any web application that requires user authentication, and there are various ways to perform it. 

One way is to use an email validation service such as [emailvalidation.io](https://emailvalidation.io/). This API allows developers to validate email addresses by checking whether they are syntactically correct, whether the domain exists, and whether the mailbox can receive messages.

The API offers a range of [pricing plans](https://emailvalidation.io/pricing/) to suit different needs. The free plan allows developers to validate up to 100 emails, which should be sufficient for our testing purposes. The paid plans start at $9.99 per month and offer more requests, more features, and faster response times.

In this section, you'll write a Python function that sends a GET request to the API's endpoint and passes the email address to be validated as a parameter. 

To authenticate the API request, you will also need to pass the API key with the request. Before proceeding, you must create an account on emailvalidation.io to obtain an API key. Once you've created your account, you will be redirected to a dashboard, similar to the one shown below. The API key is located in the black highlighted area.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-29-112311.png)

To make a GET request, you'll need to install the `requests` library in your virtual environment:

```bash
pip install requests
```

Next, create a `test.py` file and add the following code there:

```python
import requests
from requests.structures import CaseInsensitiveDict


def is_valid(email: str):
    url = f"https://api.emailvalidation.io/v1/info?email={email}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = "your-api-key-here"

    response = requests.get(url, headers=headers)

    return response.json()

    
print(is_valid("support@emailvalidation.io"))
print(is_valid("venip42579@jdsdhak.com"))

```

The `is_valid` function takes an email address as an argument and constructs a URL with the email address to call the emailvalidation.io API. The `CaseInsensitiveDict` class from the `requests.structures` module is used to create a dictionary with case-insensitive keys to set the API key in the header of the request. You then return the JSON response from the function.

Finally, you call the `is_valid` function twice with different email addresses to demonstrate how the function can validate both a valid email address (`support@emailvalidation.io`) and an invalid email address (`venip42579@jdsdhak.com`).

Output:

```bash
{
   "email":"support@emailvalidation.io",
   "user":"support",
   "tag":"",
   "domain":"emailvalidation.io",
   "smtp_check":true,
   "mx_found":true,
   "did_you_mean":"",
   "role":true,
   "disposable":false,
   "score":0.64,
   "state":"deliverable",
   "reason":"valid_mailbox",
   "free":false,
   "format_valid":true,
   "catch_all":"None"
}
{
   "email":"venip42579@jdsdhak.com",
   "user":"venip42579",
   "tag":"",
   "domain":"jdsdhak.com",
   "smtp_check":false,
   "mx_found":false,
   "did_you_mean":"",
   "role":false,
   "disposable":false,
   "score":0.64,
   "state":"undeliverable",
   "reason":"invalid_mx",
   "free":false,
   "format_valid":true,
   "catch_all":"None"
}
```

You can learn about the different keys in the response [here](https://emailvalidation.io/docs/info#sample-response). To determine if an email address is valid or invalid based on the JSON response from emailvalidation.io, you should check the following fields:

1. `format_valid`: If `true`, the email address is properly formatted. If `false`, the email address is not valid.
2. `mx_found`: If `true`, at least one MX record was found for the domain. If `false`, the domain is not valid.
3. `smtp_check`: If `true`, the email address has a valid mailbox. If `false`, the mailbox is not valid.
4. `state`: The current state of the email address. The values can be "deliverable" or "undeliverable".

Thus, you can modify the `is_valid` function to return a Boolean response instead of a JSON object as below:

```python
import requests
from requests.structures import CaseInsensitiveDict


def is_valid(email: str):
    url = f"https://api.emailvalidation.io/v1/info?email={email}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = "nUH1hmV24lEwX1TIXmsgRPRRZw0L0NuOeHrdMp78"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_resp = response.json()
        format_valid = json_resp["format_valid"]
        mx_found = json_resp["mx_found"]
        smtp_check = json_resp["smtp_check"]
        state = json_resp["state"]

        return format_valid and mx_found and smtp_check and state == "deliverable"

    return False


print(is_valid("support@emailvalidation.io"))
print(is_valid("venip42579@jdsdhak.com"))

```

Output:

```bash
True
False
```

In the upcoming section, you'll use this function to validate emails during user registration.

## How to Set Up Basic User Authentication in Flask

In this section, you will go through the steps to set up basic user authentication in Flask. You will be using the code from [one of my previous articles](https://blog.ashutoshkrris.in/how-to-set-up-basic-user-authentication-in-a-flask-app) where I had explained how to implement basic user authentication. 

You can start by pulling the code from the GitHub repository to the `email-validation` folder:

```bash
git init
git remote add origin https://github.com/ashutoshkrris/Flask-User-Authentication.git
git pull origin main
```

Note: The command `git clone [https://github.com/ashutoshkrris/Flask-User-Authentication.git](https://github.com/ashutoshkrris/Flask-User-Authentication.git) .` won't run in this case because your directory is not empty.

Next, you'll see a `requirements.txt` file that contains the dependencies to run the the application in your system. Install the dependencies using the command:

```bash
pip install -r requirements.txt
```

Once all the dependencies are installed, you'll need to add the environment variables required for the project. The project contains a `.env` file which has all the environment variables. Run the following command to export all the environment variables from the `.env` file:

```bash
source .env
```

Next, you have to create the database. Since the project uses Flask-Migrate, creating the database is a fairly simple task using the following commands:

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Now, you can run the application using the command:

```bash
python manage.py run
```

The application will start running and you can go to `http://localhost:5000/login` in your web browser to see the application.

Here's a demo video that shows the application:

%[https://www.youtube.com/watch?v=XxSESg89xEI]

Inside your project `flask-validation`, you'll have a `src` folder containing your source code and a `tests` folder containing the unit tests. 

In addition to these, you'll also have a `config.py` file that contains the configuration settings for your application and a `manage.py` file that uses Flask-CLI to add different commands for running and testing your application. You'll also find other files such as `.env` and `requirements.txt` which you already know about.

The `src` folder contains four subfolders – `accounts`, `core`, `templates`, and `static`. The `templates` and `static` folders contain the HTML files and static files such as CSS, images, and JavaScript files, respectively. The other two folders, `accounts` and `core`, use the concept of [Flask Blueprints](https://blog.ashutoshkrris.in/how-to-use-blueprints-to-organize-your-flask-apps) and contain the respective codes for different parts of the application.

If you want to learn more about the implementation of your Flask application, you can refer to [this tutorial](https://blog.ashutoshkrris.in/how-to-set-up-basic-user-authentication-in-a-flask-app).

## How to Integrate the Email Validation Service in Your Flask App

Up until this point, it is possible to successfully register in the application using any email address, regardless of whether it is valid or not. 

But it's not desirable to have random or incorrect email addresses cluttering up your database. So it's a good idea to validate the email address before registering the user. If the email address is valid, you can proceed with registering the user successfully.

Add your Email Validation API Key in the `.env` file to so that you can read it without exposing to the public:

```
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
export API_KEY=your-api-key-here
```

Replace the `your-api-key-here` with your correct API key. Next, you'll again need to run the following command to export the environment variables:

```bash
source .env
```

Now, create a `utils.py` file inside the `accounts` subfolder in the `src` folder. The file will contain the utility function to validate the email. Add the following code in the file:

```python
import requests
from requests.structures import CaseInsensitiveDict
from decouple import config


def is_valid(email: str):
    url = f"https://api.emailvalidation.io/v1/info?email={email}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = config("API_KEY")

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_resp = response.json()
        format_valid = json_resp["format_valid"]
        mx_found = json_resp["mx_found"]
        smtp_check = json_resp["smtp_check"]
        state = json_resp["state"]

        return format_valid and mx_found and smtp_check and state == "deliverable"

    return False

```

As previously mentioned, the `is_valid()` function returns a Boolean value indicating whether an email address is valid or not. It's important to note that the function doesn't hardcode the API key value, instead it retrieves it from the environment variables.

Next, in the `RegisterForm` class in the `forms.py` file, you have a `validate` method. This method is responsible for validating the input data submitted by the user during the registration process. 

Previously, this method only checked if the email was already registered and if the passwords matched. But you can now add an additional validation to check if the email is valid. Thus the modified `validate` method looks like this:

```python
...

from src.accounts.utils import is_valid

...

class RegisterForm(FlaskForm):
	...

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        if not is_valid(self.email.data):
            self.email.errors.append("Email is invalid")
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

In the `validate` method, if the `self.email.data` (that is the user's email address) is not valid, you append an error message to the `self.email.errors` list and return `False` which means the user data is not valid.

Now, when you run the application and try to register, you can see it live. Here's a demo showing both valid and invalid cases.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Validation-Demo-Made-with-Clipchamp.gif)

## Other Use Cases of an Email Validation Service

Apart from validating a user's email during registration, there are several other use cases for Email Validation Services. Some of these are:

1. Cleaning Email Lists: you can use email validation services to clean email lists by removing invalid, non-existent or risky email addresses. This can help to improve email deliverability and ensure that your emails reach the intended recipients.
2. Preventing Fraudulent Activities: you can also use email validation services to detect fraudulent activities such as fake account creation or fraudulent orders. By validating the email addresses associated with these activities, you can prevent such activities from happening.
3. Enhancing marketing campaigns: these services can also help improve the accuracy and effectiveness of email marketing campaigns. By ensuring that email addresses are valid and active, businesses can increase their email deliverability rates and improve their overall campaign performance.

Overall, email validation services can be a powerful tool in ensuring the accuracy and validity of user data, preventing fraud, and improving the user experience.

## Conclusion

Email validation services are a powerful tool for any application that requires verifying user email addresses. It is essential to ensure that email addresses are valid to prevent errors and to ensure that the user input data is correct. 

In this article, you saw how to use the [emailvalidation.io](https://emailvalidation.io/) API to validate an email address in Python. You also learned other potential use cases for email validation services, such as fraud detection and email marketing. 

By implementing email validation services in your application, you can improve your user experience and ensure that your data is accurate and up-to-date.

### Additional Resources

* [How to Use Blueprints to Organize Your Flask Apps](https://blog.ashutoshkrris.in/how-to-use-blueprints-to-organize-your-flask-apps)
* [How to Set Up Email Verification in a Flask App](https://blog.ashutoshkrris.in/how-to-set-up-email-verification-in-a-flask-app)
* [emailvalidation.io Documentation](https://emailvalidation.io/docs/)

