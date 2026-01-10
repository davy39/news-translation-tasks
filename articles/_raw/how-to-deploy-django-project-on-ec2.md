---
title: How to Deploy Your Django Project on an EC2 Machine using GitHub Actions
subtitle: ''
author: Muhammad Haseeb
co_authors: []
series: null
date: '2024-01-30T15:40:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-django-project-on-ec2
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Deploying-Django-Project-on-EC2-Machine-using-GitHub-Actions.png
tags:
- name: Django
  slug: django
- name: ec2
  slug: ec2
- name: GitHub Actions
  slug: github-actions
seo_title: null
seo_desc: 'Deploying a Django application can be streamlined and automated using GitHub
  Actions.

  This article provides a comprehensive guide on how to set up a continuous deployment
  pipeline for a Django project hosted on an AWS EC2 instance.

  By leveraging GitH...'
---

Deploying a Django application can be streamlined and automated using GitHub Actions.

This article provides a comprehensive guide on how to set up a continuous deployment pipeline for a Django project hosted on an AWS EC2 instance.

By leveraging GitHub Actions, developers can automate their deployment process, making it more efficient and error-free.

## Prerequisites

* A Django project hosted in a GitHub repository.
* An AWS EC2 instance set up for hosting a Django application.
* Basic familiarity with YAML and GitHub workflows.

## How to Set up the EC2 Instance

Before diving into GitHub Actions, ensure your EC2 instance is ready to host your Django application. 

Use the command below to connect to your EC2 instance:

```
ssh -i /path/to/your-key.pem ec2-user@your-ec2-instance-public-dns
```

You can update your system packages using these:

```
sudo apt-get update
sudo apt-get upgrade
```

Next, if you haven't already, install Python and Pip:

```
sudo apt-get install python3
sudo apt-get install python3-pip
```

Then install Django using this command:

```
pip3 install django

```

## How to Configure a Web Server

In this section, you'll see how to configure your web server.

First, install Nginx:

```
sudo apt-get install nginx

```

Then configure Nginx for Django. Start by creating a new configuration file for your Django project.

```
sudo nano /etc/nginx/sites-available/mydjangoapp

```

Then add the following server block:

```
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/django/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/gunicorn.sock;
    }
}

```

Lastly, enable the Nginx configuration:

```
sudo ln -s /etc/nginx/sites-available/mydjangoapp /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

```

## How to Setup a Database

You can install PostgreSQL using this:

```
sudo apt-get install postgresql postgresql-contrib

```

After the installation, create a database and user using this command:

```
sudo -u postgres psql

```

Run this SQL query to create a new database and add a new user:

```sql
CREATE DATABASE mydjangodb;
CREATE USER mydjangouser WITH PASSWORD 'password';
ALTER ROLE mydjangouser SET client_encoding TO 'utf8';
ALTER ROLE mydjangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydjangouser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydjangodb TO mydjangouser;
\q

```

Then configure Django to use PostgreSQL. In your Django `settings.py` file, update the `DATABASES` setting:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydjangodb',
        'USER': 'mydjangouser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

The GitHub Actions workflow for deploying a Django project involves several key steps:

### Step #1 - Checkout and Preparation

The first step in your workflow is to check out the latest code from your GitHub repository and set up the environment for the deployment.

```yaml
name: Deploy Django to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

```

### Step #2 - Deployment Script

The deployment script involves pulling the latest code, installing dependencies, running migrations, and restarting the web and WSGI servers. 

Create a new file `deploy_script.sh` on your EC2 machine and add the code below:

```bash
#!/bin/bash

DRY_RUN=$1

echo "Pulling latest code from repository..."
# Skip actual git pull in dry run
[ "$DRY_RUN" != "true" ] && git pull origin main

echo "Installing dependencies..."
# Skip actual installation in dry run
[ "$DRY_RUN" != "true" ] && pip install -r requirements.txt

echo "Running migrations..."
# Skip actual migrations in dry run
[ "$DRY_RUN" != "true" ] && python manage.py migrate

echo "Restarting the server..."
# Skip actual restart in dry run
[ "$DRY_RUN" != "true" ] && sudo systemctl restart myapp

echo "Deployment complete."

```

### Step #3 - Create a Step to Run the Deployment Script

Use GitHub Actions to SSH into your EC2 instance. You'll need to store your EC2 instance's SSH key as a GitHub secret.

```yaml
- name: Run Deployment
  run: |
    ssh -i ${{ secrets.EC2_SSH_KEY }} ec2-user@your-ec2-instance 'bash -s' < deploy_script.sh
  env:
    ACTIONS_RUNNER_DEBUG: false
```

## Security Considerations

Here are some security considerations to keep in mind:

* **SSH Keys**: Store your SSH private keys securely in GitHub Secrets.
* **Minimal Permissions**: Ensure the EC2 instance's IAM role has minimal permissions necessary for deployment.

## Testing and Validation

Before fully implementing this workflow, test it with a development or staging environment to ensure that the deployment process works as expected.

**Dry Run Deployment**: Implement a step in your GitHub Actions workflow that does a 'dry run' of the deployment process. This can help validate the deployment scripts without affecting the live EC2 instance. Add the step below to pass `dry_run = true` in deployment script.

```yaml
- name: Dry Run Deployment
  run: |
    ssh -i ${{ secrets.EC2_SSH_KEY }} ec2-user@your-ec2-instance 'bash -s' < deploy_script.sh true
  env:
    ACTIONS_RUNNER_DEBUG: true
```

**Logging and Monitoring**: You can see current action capture logs of the deployment process from `deploy_script.sh`, which can be reviewed if any issues arise.

## Conclusion

Automating Django deployments using GitHub Actions offers a streamlined and reliable way to manage application delivery. 

By following the steps outlined above, developers can set up a robust deployment pipeline that pushes their latest Django code to an EC2 instance seamlessly upon every push to the main branch.

