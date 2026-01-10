---
title: Build a Heroku Clone – Provision Infrastructure Programmatically
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-06-02T14:08:55.000Z'
originalURL: https://freecodecamp.org/news/build-a-heroku-clone-provision-infrastructure-programmatically
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/heroku-1.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: youtube
  slug: youtube
seo_title: null
seo_desc: "Heroku is a platform as a service that enables developers to build, run,\
  \ and operate applications entirely in the cloud.\nHeroku makes it simple to do\
  \ things like create virtual machines to host applications and to deploy websites.\
  \  \nSome of the featu..."
---

Heroku is a platform as a service that enables developers to build, run, and operate applications entirely in the cloud.

Heroku makes it simple to do things like create virtual machines to host applications and to deploy websites.  
  
Some of the features that Heroku offers can actually be created easily with other tools. 

In this article, you will learn how to create a very simple web app that allows users to provision virtual machines and deploy static websites at the click of a button, all hosted on Amazon Web Services.

You will learn how to provision infrastructure with code and then you will be able to apply what you learn to your own applications.

This article is a companion to the full course we just posted on the freeCodeCamp.org YouTube channel that will teach you how to provision infrastructure programmatically using Python.

You can watch the course below or on the freeCodeCamp.org YouTube channel (1.5-hour watch).

%[https://youtu.be/zhJLVFR3pE8]

Provisioning infrastructure is related to platform engineering. A platform engineering team serves an organization by planning, designing, and managing its cloud platforms. And often this can be done programatically.

The tools I teach in this course can be used for much more than just provisioning VMs and deploying websites. They can be used for platform engineering to make it simpler to manage cloud platforms.

### Automation API

This course focusses on the Automation API from Pulumi. Pulumi provided freeCodeCamp a grant that made this course possible. 

Pulumi's open source infrastructure as code SDK enables you to create, deploy, and manage infrastructure on any cloud, using many different programming languages.

Their Automation API makes it possible to provision infrastructure programmatically using the Pulumi engine. Basically, it makes it simple to write a program that automatically creates VMs, databases, VPCs, static websites and more on a variety of different cloud platforms.

I'm going to show you how to create our Heroku-clone web app using Flask and Python on the backend. However, you don't already have to know how to use Flask and Python to follow along. Also, everything I show you could also be done with many other different frameworks and programming languages and many of the steps are the same no matter what web framework you use.

Our app will provision resources on AWS, but Pulumi makes it simple to provision resources on most of the major cloud providers and it wouldn't take that much updating to the code to use a different provider.

Thanks to Komal Ali who created the code that my code in this course is based off of.

## Creating the Heroku Clone

### Pulumi CLI

First, make sure you have the Pulumi CLI installed. The way to install is different depending on your operating system.

If you have MacsOS and [Homebrew](https://brew.sh/), you can use the command `brew install pulumi`.

If you have Windows and [Chocolatey](https://chocolatey.org/), you can use the command `choco install pulumi`.

[This page will give you additional ways of installing Pulumi](https://www.pulumi.com/docs/get-started/install/).

### AWS CLI

This project also uses AWS so you'll have to make sure you have an AWS account and have the CLI set up and authenticated.

You can sign up for a free AWS account here: [https://aws.amazon.com/free/](https://aws.amazon.com/free/)

Learn how to install the AWS CLI for your operating system here: [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

For MacOS, you can use these commands:

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

For Windows there are a few extra steps and you should just [follow the instructions here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html).

Next, you need to get an Access key ID and secret access key from AWS. [Follow the instructions from Amazon to get these](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds).

Now run the following in the command line:

`aws configure`

Enter your Access Key ID and Secret Access Key when prompted. You can keep the "Default region name" and "Default output format" as None.

###   
Setup the Project

A Pulumi project is just a directory with some files in it. It's possible for you to create a new one by hand. The `pulumi new` command, however, automates the process:

`pulumi new`

If this is the first time you have used Pulumi, you will be directed to enter an access code or login. To get an access code, go to [https://app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens)

The `pulumi new` command allows you to choose between many templates. Choose the "aws-python" template. You can select the defaults for the other options.

This command has created all the files we need, initialized a new stack named `dev` (an instance of our project). 

Every Pulumi program is deployed to a _stack_. A stack is an isolated, independently configurable instance of a Pulumi program. Stacks are commonly used to denote different phases of development. In this case, we called it 'dev'.

Now we need to install two more dependencies for our project with

`venv/bin/pip install flask requests`

### Create Flask App

We can now start creating the files for our Flask web app.

Pulumi created a file called "__main__.py". Change the name of that file to "app.py" because this is a Flask app and Flask will look for a file with that name.

There is some code in that file and we will eventually use code similar to that but for now let's just test that flask is working by replacing the code in "app.py" to the following:

```python
from flask import Flask
  
app = Flask(__name__)
  
@app.route('/')
def hello_world():
    return 'Hello World'
  
if __name__ == '__main__':
  
    app.run()
```

This is the most basic Flask web app and we can test it by running the following command in the terminal:

`env/bin/flask run`

Then we can access the running app in the web browser at the URL "[http://127.0.0.1:5000/](http://127.0.0.1:5000/)".

If you go to that URL it should say "Hello World". If so, Flask is working correctly so we can update the "app.py" file to the following:

```python
import os
from flask import Flask, render_template

import pulumi.automation as auto


def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws", "v4.0.0")


def create_app():
    ensure_plugins()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="secret",
        PROJECT_NAME="herocool",
        PULUMI_ORG=os.environ.get("PULUMI_ORG"),
    )

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    from . import sites

    app.register_blueprint(sites.bp)

    from . import virtual_machines

    app.register_blueprint(virtual_machines.bp)

    return app

```

We import Pulumi's automation framework as a variable called `auto`. Then in the `ensure_plugins` function we get access to the `LocalWorkspace`. A `Workspace` is the execution context containing a single Pulumi project. Workspaces are used to manage the execution environment, providing various utilities such as plugin installation, environment configuration, and creation, deletion, and listing of stacks.

Because we are deploying AWS resources in this tutorial, we must install the AWS provider plugin within the `Workspace` so that the Pulumi program will have it available during execution.

The `create_app` function is what Flask will run when we star the flask app. We first run the `ensure_plugins` function and then create the Flask app. The `app.config.from_mapping()` function is used by Flask to set some default configurations that the app will use. This will not be a production ready app but if you ever deploy a Flask app make sure to change secret key. The other variables are used by pulumi.

The rest of the file is common to Flask apps. We set the default route  (`@app.route("/", methods=["GET"])`) to render the template "index.html" (which we still have to create.

Finally, the file imports the sites and virtual_machines files and registers them as a blueprint.

A Blueprint in Flask is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.

Basically, we are using Blueprints so we can define additional routes for our web app in other files that we still have to create.

### Create Templates

And speaking of creating other files, let's create some. Create a director called "templates" and then create a file inside that directory named "index.html".

Add the following code:

```html
{% extends "base.html" %}

{% block content %}
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Static Websites</h5>
          <p class="card-text">Deploy your own static website in seconds!</p>
          <a href="{{ url_for("sites.list_sites") }}" class="btn btn-primary">Get started</a>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Virtual Machines</h5>
          <p class="card-text">Set up a virtual machine for development and testing.</p>
          <a href="{{ url_for("virtual_machines.list_vms") }}" class="btn btn-primary">Get started</a>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
```

I won't go into too much detail about this code. It is basic HTML but anything inside curly braces is an expression that will be output to the final document. Flask uses the Jinja template library to render templates. You will notice that it dynamically renders a list of sites and virtual machines. Soon we will create the Python code that will get those lists using Pulumi. 

But next create a file called "base.html". You will notice that "index.html" extends "base.html". This will basically be the header that all our pages share.

Add this code:

```html
<!DOCTYPE html>
<head>
  <title>Herocool - {% block title %}{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for("static", filename="bootstrap.min.css") }}">
  <script src="{{ url_for("static", filename="bootstrap.min.js") }}"></script>
</head>
<body>
  <div class="container p-2">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="{{ url_for("index") }}" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
        <span class="fs-3">Herocool</span>
      </a>
      {% block nav %}{% endblock %}
    </header>
  </div>
  <section class="container-md px-4">
    <div>
      <header class="row gy-4">
        <span class="fs-4">{% block header %}{% endblock %}</span>
        {% for category, message in get_flashed_messages(with_categories=true) %}
        <div class="alert alert-{{ category }}" role="alert">{{ message }}</div>
        {% endfor %}
      </header>
    </div>
    {% block content %}{% endblock %}
  </section>
</body>

```

Now, we'll quickly create the rest of our HTML templates, then create the Python files that do the real heavy lifting in our app.

Inside our "templates" directory, create two more directories called "sites" and "virtual_machines". Inside each of those directories create the same three files: "index.html", "create.html", and "update.html".

Here is the code to add to each:

**sites/index.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("sites.create_site") }}" class="nav-link active">Create static site</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Site Directory{% endblock %}
{% endblock %}

{% block content %}
  <table class="table">
    <tbody>
      {% if not sites %}
      <div class="container gy-5">
        <div class="row py-4">
          <div class="alert alert-secondary" role="alert">
            <p>No websites are currently deployed. Create one to get started!</p>
            <a href="{{ url_for("sites.create_site") }}" class="btn btn-primary">Create static site</a>
          </div>
        </div>
      </div>
      {%  endif %}
      {% for site in sites %}
        <tr>
          <td class="align-bottom" colspan="4">
            <div class="p-1">
              <a href="{{ site["url"] }}" class="fs-5 align-bottom" target="_blank">{{ site["name"] }}</a>
            </div>
          </td>
          <td>
            <div class="float-end p-1">
              <form action="{{ url_for("sites.delete_site", id=site["name"]) }}" method="post">
                <input class="btn btn-sm btn-danger" type="submit" value="Delete">
              </form>
            </div>
            <div class="float-end p-1">
              <form action="{{ url_for("sites.update_site", id=site["name"]) }}" method="get">
                <input class="btn btn-sm btn-primary" type="submit" value="Edit">
              </form>
            </div>
            <div class="float-end p-1">
              <a href="{{ site["console_url"] }}" class="btn btn-sm btn-outline-primary" target="_blank">View in console</a>
            </div>
          </td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}

```

**sites/create.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("sites.list_sites") }}" class="nav-link">Back to site directory</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Create new static site{% endblock %}
{% endblock %}

{% block content %}
<section class="p-2">
  <form method="post">
    <div class="mb-3">
      <label for="site-id" class="form-label">Name</label>
      <input type="text" class="form-control" name="site-id" id="site-id" aria-describedby="nameHelp" required>
      <div id="nameHelp" class="form-text">Choose a unique name as a label for your website</div>
    </div>
    <div class="mb-3">
      <label for="file-url" class="form-label">File URL</label>
      <input type="text" class="form-control" id="file-url" name="file-url">
    </div>
    <div class="mb-3">
      <strong>OR</strong>
    </div>
    <div class="mb-3">
      <label for="site-content" class="form-label">Content</label>
      <textarea class="form-control" name="site-content" id="site-content" rows="5"></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Create</button>
  </form>
</section>
{% endblock %}

```

**sites/update.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("sites.list_sites") }}" class="nav-link">Back to site directory</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Update site '{{ name }}'{% endblock %}
{% endblock %}

{% block content %}
  <section class="p-2">
    <form method="post">
      <div class="mb-3">
        <label for="file-url" class="form-label">File URL</label>
        <input type="text" class="form-control" name="file-url" id="file-url">
      </div>
      <div class="mb-3">
        <strong>OR</strong>
      </div>
      <div class="mb-3">
        <label for="site-content" class="form-label">Content</label>
        <textarea class="form-control" name="site-content" id="site-content" rows="5">{{ content }}</textarea>
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>
  </section>
{% endblock %}

```

**virtual_machines/index.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("virtual_machines.create_vm") }}" class="nav-link active">Create VM</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Deployed Virtual Machines{% endblock %}
{% endblock %}

{% block content %}
  <table class="table">
    <tbody>
      {% if not vms %}
      <div class="container gy-5">
        <div class="row py-4">
          <div class="alert alert-secondary" role="alert">
            <p>No virtual machines are currently deployed. Create one to get started!</p>
            <a href="{{ url_for("virtual_machines.create_vm") }}" class="btn btn-primary">Create VM</a>
          </div>
        </div>
      </div>
      {%  endif %}
      {% for vm in vms %}
      <tr>
        <td class="align-bottom" colspan="4">
          <div class="p-1">
            <pre> ssh -i ~/.ssh/id_rsa.pem ec2-user@{{ vm["dns_name"] }} </pre>
          </div>
        </td>
        <td>
          <div class="float-end p-1">
            <form action="{{ url_for("virtual_machines.delete_vm", id=vm["name"]) }}" method="post">
              <input class="btn btn-sm btn-danger" type="submit" value="Delete">
            </form>
          </div>
          <div class="float-end p-1">
            <form action="{{ url_for("virtual_machines.update_vm", id=vm["name"]) }}" method="get">
              <input class="btn btn-sm btn-primary" type="submit" value="Edit">
            </form>
          </div>
          <div class="float-end p-1">
            <a href="{{ vm["console_url"] }}" class="btn btn-sm btn-outline-primary" target="_blank">View in console</a>
          </div>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}

```

**virtual_machines/create.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("virtual_machines.list_vms") }}" class="nav-link">Back to Virtual Machines directory</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Create new virtual machine{% endblock %}
{% endblock %}

{% block content %}
<section class="p-2">
  <form method="post">
    <div class="mb-3">
      <label for="vm-id" class="form-label">Name</label>
      <input type="text" class="form-control" name="vm-id" id="vm-id" aria-describedby="nameHelp" required>
      <div id="nameHelp" class="form-text">Choose a unique name as a label for your virtual machine</div>
    </div>
    <div class="mb-3">
      <label for="vm-id" class="form-label">Instance Type</label>
      <select name="instance_type" class="form-control" id="instance_type">
      {% for instance_type in instance_types %}
        <option value="{{ instance_type }}" {% if instance_type == curr_instance_type %} selected {% endif %}>
          {{ instance_type }}
        </option>
      {% endfor %}
      </select>
    </div>
    <div class="mb-3">
      <label for="vm-keypair" class="form-label">Public Key</label>
      <textarea class="form-control" name="vm-keypair" id="vm-keypair-content" rows="5" aria-describedby="keypairHelp"></textarea>
      <div id="keypairHelp" class="form-text">The public key to use to connect to the VM </div>
    </div>
    <button type="submit" class="btn btn-primary">Create</button>
  </form>
</section>
{% endblock %}
```

**virtual_machines/update.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("virtual_machines.list_vms") }}" class="nav-link">Back to Virtual Machines directory</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Update Virtual Machine '{{ name }}'{% endblock %}
{% endblock %}

{% block content %}
  <section class="p-2">
    <form method="post">
      <div class="mb-3">
        <label for="vm-id" class="form-label">Instance Type</label>
        <select name="instance_type" class="form-control" id="instance_type">
          {% for instance_type in instance_types %}
            <option value="{{ instance_type }}" {% if instance_type == curr_instance_type %} selected {% endif %}>
              {{ instance_type }}
            </option>
          {% endfor %}
          </select>
      </div>
      <div class="mb-3">
        <label for="vm-keypair" class="form-label">Public Key</label>
        <textarea class="form-control" name="vm-keypair" id="vm-keypair-content" rows="5">{{ public_key }}</textarea>
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>
  </section>
{% endblock %}

```

### Create Functionality with Python

Now it's time to create the functionality of our Heroku clone using Python. The "app.py" file imports from files we still have to create. In the same directory as "app.py", create "sites.py".

Add the following to "sites.py":

```python
import json
import requests
from flask import (
    current_app,
    Blueprint,
    request,
    flash,
    redirect,
    url_for,
    render_template,
)

import pulumi
import pulumi.automation as auto
from pulumi_aws import s3

bp = Blueprint("sites", __name__, url_prefix="/sites")
```

Those are just the basic imports we need for Flask and Pulumi, including importing the automation framework.

Next, add the the following code to that file. This function defines our Pulumi s3 static website in terms of the content that the caller passes in. This allows us to dynamically deploy websites based on user defined values from the POST body.

```python
def create_pulumi_program(content: str):
    # Create a bucket and expose a website index document
    site_bucket = s3.Bucket(
        "s3-website-bucket", website=s3.BucketWebsiteArgs(index_document="index.html")
    )
    index_content = content

    # Write our index.html into the site bucket
    s3.BucketObject(
        "index",
        bucket=site_bucket.id,
        content=index_content,
        key="index.html",
        content_type="text/html; charset=utf-8",
    )

    # Set the access policy for the bucket so all objects are readable
    s3.BucketPolicy(
        "bucket-policy",
        bucket=site_bucket.id,
        policy=site_bucket.id.apply(
            lambda id: json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        # Policy refers to bucket explicitly
                        "Resource": [f"arn:aws:s3:::{id}/*"],
                    },
                }
            )
        ),
    )

    # Export the website URL
    pulumi.export("website_url", site_bucket.website_endpoint)
    pulumi.export("website_content", index_content)
```

The purpose of `pulumi.export` that you see at the end of the code is to export a named stack output. Exported values are attached to the program’s Stack resource. Later you will see how we can access this data that is being exported.

So far, nothing is calling the function we just created. At this pointe, we will create URL endpoints that can be used to call that function and create websites. 

First, we'll add the code for the /new URL that will create a new site:

```python
@bp.route("/new", methods=["GET", "POST"])
def create_site():
    """creates new sites"""
    if request.method == "POST":
        stack_name = request.form.get("site-id")
        file_url = request.form.get("file-url")
        if file_url:
            site_content = requests.get(file_url).text
        else:
            site_content = request.form.get("site-content")

        def pulumi_program():
            return create_pulumi_program(str(site_content))

        try:
            # create a new stack, generating our pulumi program on the fly from the POST body
            stack = auto.create_stack(
                stack_name=str(stack_name),
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # deploy the stack, tailing the logs to stdout
            stack.up(on_output=print)
            flash(
                f"Successfully created site '{stack_name}'", category="success")
        except auto.StackAlreadyExistsError:
            flash(
                f"Error: Site with name '{stack_name}' already exists, pick a unique name",
                category="danger",
            )

        return redirect(url_for("sites.list_sites"))

    return render_template("sites/create.html")
```

For a GET request, this route renders the "create.html" template. For a POST request, it creates a new site and the redirects to the list of sites at the `/` route.

You will notice that there is a `stack` created. As a reminder, every Pulumi program is deployed to a stack. A stack is an isolated, independently configurable instance of a Pulumi program. In this code, the stack name is based on the id that the user types into the form. There is also a project name, and the program, which is the code block we previously discussed.

Once the stack is created, we can execute commands against the `Stack`, including update, preview, refresh, destroy, import, and export. In this code we use `stack.up()` to `up`date the stack. And we pass in a.callback function to `stack.up()` for standard output.

Next add the code for the root URL that will list the sites:

```python
@bp.route("/", methods=["GET"])
def list_sites():
    """lists all sites"""
    sites = []
    org_name = current_app.config["PULUMI_ORG"]
    project_name = current_app.config["PROJECT_NAME"]
    try:
        ws = auto.LocalWorkspace(
            project_settings=auto.ProjectSettings(
                name=project_name, runtime="python")
        )
        all_stacks = ws.list_stacks()
        for stack in all_stacks:
            stack = auto.select_stack(
                stack_name=stack.name,
                project_name=project_name,
                # no-op program, just to get outputs
                program=lambda: None,
            )
            outs = stack.outputs()
            if 'website_url' in outs:
                sites.append(
                    {
                        "name": stack.name,
                        "url": f"http://{outs['website_url'].value}",
                        "console_url": f"https://app.pulumi.com/{org_name}/{project_name}/{stack.name}",
                    }
                )
    except Exception as exn:
        flash(str(exn), category="danger")

    return render_template("sites/index.html", sites=sites)
```

A `Workspace` is the execution context containing a single Pulumi project, a program, and multiple stacks. So we first get access `ws = auto.LocalWorkspace()`.

Then we `list_stacks()`. This just gives us access to the stack name so we must use `auto.select_stack()` to get access to the stack. We specifically want the `stack.outputs()`. This will be what we exported to the stack, including the `website_url`. 

Then we append information for each site to the `sites` list which is used on the frontend to show the list of sites. 

Now, add the code for the /update route. 

```python
@bp.route("/<string:id>/update", methods=["GET", "POST"])
def update_site(id: str):
    stack_name = id

    if request.method == "POST":
        file_url = request.form.get("file-url")
        if file_url:
            site_content = requests.get(file_url).text
        else:
            site_content = str(request.form.get("site-content"))

        try:

            def pulumi_program():
                create_pulumi_program(str(site_content))

            stack = auto.select_stack(
                stack_name=stack_name,
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # deploy the stack, tailing the logs to stdout
            stack.up(on_output=print)
            flash(f"Site '{stack_name}' successfully updated!",
                  category="success")
        except auto.ConcurrentUpdateError:
            flash(
                f"Error: site '{stack_name}' already has an update in progress",
                category="danger",
            )
        except Exception as exn:
            flash(str(exn), category="danger")
        return redirect(url_for("sites.list_sites"))

    stack = auto.select_stack(
        stack_name=stack_name,
        project_name=current_app.config["PROJECT_NAME"],
        # noop just to get the outputs
        program=lambda: None,
    )
    outs = stack.outputs()
    content_output = outs.get("website_content")
    content = content_output.value if content_output else None
    return render_template("sites/update.html", name=stack_name, content=content)
```

You will notice that the /update route is very similar to the /new route. Since it uses the same `stack_name`, a new site is not created.

A new thing in this function is that the code gets the content of the website to return to the frontend template.

Finally, add the following code for a /delete route.

```
@bp.route("/<string:id>/delete", methods=["POST"])
def delete_site(id: str):
    stack_name = id
    try:
        stack = auto.select_stack(
            stack_name=stack_name,
            project_name=current_app.config["PROJECT_NAME"],
            # noop program for destroy
            program=lambda: None,
        )
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack_name)
        flash(f"Site '{stack_name}' successfully deleted!", category="success")
    except auto.ConcurrentUpdateError:
        flash(
            f"Error: Site '{stack_name}' already has update in progress",
            category="danger",
        )
    except Exception as exn:
        flash(str(exn), category="danger")

    return redirect(url_for("sites.list_sites"))

```

In this delete function we first we get access to the stack then destroy and remove the stack. Just by calling the `stack.destroy()` function will delete the resource on AWS.

Now, in the same directory as "app.py", create "virtual_machines.py".

Add the following to "virtual_machines.py". This time, we'll add it all at once:

```python
from flask import (Blueprint, current_app, request, flash,
                   redirect, url_for, render_template)

import pulumi
import pulumi_aws as aws
import pulumi.automation as auto
import os
from pathlib import Path

bp = Blueprint("virtual_machines", __name__, url_prefix="/vms")
instance_types = ['c5.xlarge', 'p2.xlarge', 'p3.2xlarge']


def create_pulumi_program(keydata: str, instance_type=str):
    # Choose the latest minimal amzn2 Linux AMI.
    # TODO: Make this something the user can choose.
    ami = aws.ec2.get_ami(most_recent=True,
                          owners=["amazon"],
                          filters=[aws.GetAmiFilterArgs(name="name", values=["*amzn2-ami-minimal-hvm*"])])

    group = aws.ec2.SecurityGroup('web-secgrp',
                                  description='Enable SSH access',
                                  ingress=[aws.ec2.SecurityGroupIngressArgs(
                                      protocol='tcp',
                                      from_port=22,
                                      to_port=22,
                                      cidr_blocks=['0.0.0.0/0'],
                                  )])

    public_key = keydata
    if public_key is None or public_key == "":
        home = str(Path.home())
        f = open(os.path.join(home, '.ssh/id_rsa.pub'), 'r')
        public_key = f.read()
        f.close()

    public_key = public_key.strip()

    print(f"Public Key: '{public_key}'\n")

    keypair = aws.ec2.KeyPair("dlami-keypair", public_key=public_key)

    server = aws.ec2.Instance('dlami-server',
                              instance_type=instance_type,
                              vpc_security_group_ids=[group.id],
                              key_name=keypair.id,
                              ami=ami.id)

    pulumi.export('instance_type', server.instance_type)
    pulumi.export('public_key', keypair.public_key)
    pulumi.export('public_ip', server.public_ip)
    pulumi.export('public_dns', server.public_dns)


@bp.route("/new", methods=["GET", "POST"])
def create_vm():
    """creates new VM"""
    if request.method == "POST":
        stack_name = request.form.get("vm-id")
        keydata = request.form.get("vm-keypair")
        instance_type = request.form.get("instance_type")

        def pulumi_program():
            return create_pulumi_program(keydata, instance_type)
        try:
            # create a new stack, generating our pulumi program on the fly from the POST body
            stack = auto.create_stack(
                stack_name=str(stack_name),
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # deploy the stack, tailing the logs to stdout
            stack.up(on_output=print)
            flash(
                f"Successfully created VM '{stack_name}'", category="success")
        except auto.StackAlreadyExistsError:
            flash(
                f"Error: VM with name '{stack_name}' already exists, pick a unique name",
                category="danger",
            )
        return redirect(url_for("virtual_machines.list_vms"))

    current_app.logger.info(f"Instance types: {instance_types}")
    return render_template("virtual_machines/create.html", instance_types=instance_types, curr_instance_type=None)


@bp.route("/", methods=["GET"])
def list_vms():
    """lists all vms"""
    vms = []
    org_name = current_app.config["PULUMI_ORG"]
    project_name = current_app.config["PROJECT_NAME"]
    try:
        ws = auto.LocalWorkspace(
            project_settings=auto.ProjectSettings(
                name=project_name, runtime="python")
        )
        all_stacks = ws.list_stacks()
        for stack in all_stacks:
            stack = auto.select_stack(
                stack_name=stack.name,
                project_name=project_name,
                # no-op program, just to get outputs
                program=lambda: None,
            )
            outs = stack.outputs()
            if 'public_dns' in outs:
                vms.append(
                    {
                        "name": stack.name,
                        "dns_name": f"{outs['public_dns'].value}",
                        "console_url": f"https://app.pulumi.com/{org_name}/{project_name}/{stack.name}",
                    }
                )
    except Exception as exn:
        flash(str(exn), category="danger")

    current_app.logger.info(f"VMS: {vms}")
    return render_template("virtual_machines/index.html", vms=vms)


@bp.route("/<string:id>/update", methods=["GET", "POST"])
def update_vm(id: str):
    stack_name = id
    if request.method == "POST":
        current_app.logger.info(
            f"Updating VM: {stack_name}, form data: {request.form}")
        keydata = request.form.get("vm-keypair")
        current_app.logger.info(f"updating keydata: {keydata}")
        instance_type = request.form.get("instance_type")

        def pulumi_program():
            return create_pulumi_program(keydata, instance_type)
        try:
            stack = auto.select_stack(
                stack_name=stack_name,
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # deploy the stack, tailing the logs to stdout
            stack.up(on_output=print)
            flash(f"VM '{stack_name}' successfully updated!",
                  category="success")
        except auto.ConcurrentUpdateError:
            flash(
                f"Error: VM '{stack_name}' already has an update in progress",
                category="danger",
            )
        except Exception as exn:
            flash(str(exn), category="danger")
        return redirect(url_for("virtual_machines.list_vms"))

    stack = auto.select_stack(
        stack_name=stack_name,
        project_name=current_app.config["PROJECT_NAME"],
        # noop just to get the outputs
        program=lambda: None,
    )
    outs = stack.outputs()
    public_key = outs.get("public_key")
    pk = public_key.value if public_key else None
    instance_type = outs.get("instance_type")
    return render_template("virtual_machines/update.html", name=stack_name, public_key=pk, instance_types=instance_types, curr_instance_type=instance_type.value)


@bp.route("/<string:id>/delete", methods=["POST"])
def delete_vm(id: str):
    stack_name = id
    try:
        stack = auto.select_stack(
            stack_name=stack_name,
            project_name=current_app.config["PROJECT_NAME"],
            # noop program for destroy
            program=lambda: None,
        )
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack_name)
        flash(f"VM '{stack_name}' successfully deleted!", category="success")
    except auto.ConcurrentUpdateError:
        flash(
            f"Error: VM '{stack_name}' already has update in progress",
            category="danger",
        )
    except Exception as exn:
        flash(str(exn), category="danger")

    return redirect(url_for("virtual_machines.list_vms"))
```

There is a lot of similarities between this file and the 'sites.py' file. A virtual machine has quite a few more settings that must be set and Pulumi is able to create the exact type of VM we want. 

We could make it so a user could customize everything from the web interface, but we just give the user the ability to choose the instance type. 

One thing that is required for a VM is a public/private key pair. When creating a VM on AWS, you must give a public key. Then, in order to access the VM you have to have the private key.

You can create keys in your terminal. Run the following command:

`ssh-keygen -m PEM`

Later when testing out the app, you will have to open the public key file so you can copy the key and paste it into the website.

Now switch the directory with the file you just created. The directory should be the same whether you are on MacOS or Windows.

Type in on your terminal:

`cd /Users/[username]/.ssh`

AWS needs the file to be in .pem format and that is why we created it with "PEM" above. Now lets rename the file to have the correct extension. You need to change the name of the file called `id_rsa` to be `id_rsa.pem`.

On macOS, you can rename with this command:

`mv id_rsa id_rsa.pem`

On Windows, use:

`rename id_rsa id_rsa.pem`

When running the Flask app, you may need to enter the public key you just created. You can open the `id_rsa.pub` in any text editor in order to copy the text. If you have vim, you can use this command to open the file:

`vim /Users/beau/.ssh/id_rsa.pub`

### Testing the App

Now it's time to try out the app. On the terminal, run this command:

`FLASK_RUN_PORT=1337 FLASK_ENV=development FLASK_APP=__init__ PULUMI_ORG=[your-org-name] venv/bin/flask run`

Now you can try out the app and create websites and VMs. Make sure to delete them after creation so AWS does not keep charging you for the resources.

## Conclusion

You should now know enough to start provisioning infrastructure in your own applications using Pulumi's automation API. And if you want to see step-by-step how to do the things in this article, check out the video tutorial:

%[https://youtu.be/zhJLVFR3pE8]


