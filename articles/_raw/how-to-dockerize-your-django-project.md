---
title: How to Dockerize Your Django Project
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-18T16:37:57.106Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-your-django-project
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744994272728/248cef70-5f8e-46fd-a640-66852ffda7d2.png
tags:
- name: Python
  slug: python
- name: Docker
  slug: docker
seo_title: null
seo_desc: 'If you''re working on a Django project and you want to make your life easier
  – especially when it comes to running your app across different environments – Docker
  is your new best friend.

  Docker makes it possible to package your Django app, along with...'
---

If you're working on a Django project and you want to make your life easier – especially when it comes to running your app across different environments – Docker is your new best friend.

Docker makes it possible to package your Django app, along with all its dependencies, into something called a “container.”

That way, it runs the same on your computer, your teammate’s computer, a testing server, or even in production.

When I first started using Docker, it felt a little overwhelming. But after setting it up for a few Django apps, it all clicked.

The good news? I’m going to walk you through it, step by step, in a way that’s easy to follow, even if you’re brand new to Docker.

## Table of Contents

1. [What You’ll Need](#heading-what-youll-need)
    
2. [How to Dockerize Your Django Project](#how-to-dockerize-your-django-project)
    
    * [Step 1: Start a Django Project](#heading-step-1-start-a-django-project)
        
    * [Step 2: Create a Dockerfile](#heading-step-2-create-a-dockerfile)
        
    * [Step 3: Add a requirements.txt](#heading-step-3-add-a-requirementstxt)
        
    * [Step 4: Create docker-compose.yml](#heading-step-4-create-docker-composeyml)
        
    * [Step 5: Run It!](#heading-step-5-run-it)
        
3. [Common Issues](#heading-common-issues)
    
    * [Port Already in Use?](#heading-port-already-in-use)
        
    * [Database Not Working?](#heading-database-not-working)
        
4. [FAQs](#heading-faqs)
    
    * [Do I need Docker for development?](#heading-do-i-need-docker-for-development)
        
    * [Can I run migrations inside Docker?](#heading-can-i-run-migrations-inside-docker)
        
    * [How do I stop everything?](#heading-how-do-i-stop-everything)
        
5. [Extra Tip: Use .dockerignore](#heading-extra-tip-use-dockerignore)
    
6. [What You’ve Built](#heading-what-youve-built)
    
7. [Want to Go Deeper?](#heading-want-to-go-deeper)
    
8. [Further Reading](#heading-further-reading)
    

## What You’ll Need

Before we begin, make sure you’ve got a few things installed:

* **Python 3** (any version that Django supports)
    
* **Django** (of course)
    
* **Docker and Docker Compose**  
    👉 [Install Docker](https://docs.docker.com/engine/install/)  
    👉 [Install Docker Compose](https://docs.docker.com/compose/install/linux/)
    

You don’t need to be an expert in Docker. I’ll explain what each part does as we build it together.

## How to Dockerize Your Django Project

### Step 1: Start a Django Project

If you already have a Django project, you can skip this part.

Otherwise, open your terminal and run:

```bash
django-admin startproject myproject
cd myproject
```

This will create a new Django project called `myproject`. You’ll see a structure like this:

```markdown
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Let’s say this is your app that you want to run inside Docker.

### Step 2: Create a Dockerfile

In the root of your project (same folder as `manage.py`), create a file called `Dockerfile`. No file extension –just `Dockerfile`.

Here’s what goes inside:

```dockerfile
# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code
COPY . /app/
```

Let me break that down:

* `FROM python:3.10-slim`: This tells Docker to use a lightweight version of Python 3.10.
    
* `ENV`: These just help with cleaner logs and better performance.
    
* `WORKDIR /app`: This sets the default working directory inside the container.
    
* `COPY` and `RUN`: These lines copy your code into the container and install your Python packages.
    

### Step 3: Add a `requirements.txt`

You’ll need a file listing your Python packages.

Create a file called `requirements.txt` in the root folder and add:

```plaintext
Django>=4.0,<5.0
```

You can add more later if your project grows. For now, that’s enough.

To generate a full list of dependencies from your local virtual environment, run:

```bash
pip freeze > requirements.txt
```

### Step 4: Create `docker-compose.yml`

Now let’s create the file that tells Docker how to run everything together.

In your root folder, create `docker-compose.yml`:

```yaml
version: '3.9'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```

Let’s go line-by-line:

* `build: .`: This tells Docker to use the `Dockerfile` in the current folder.
    
* `command`: This runs Django’s development server inside the container.
    
* `volumes`: This mounts your code into the container so changes are reflected live.
    
* `ports`: This maps port 8000 inside Docker to port 8000 on your machine.
    

So if you go to `http://localhost:8000`, you’ll see your app.

### Step 5: Run It!

Now the fun part. From your terminal, run:

```bash
docker-compose up --build
```

This tells Docker to:

* Build the container
    
* Install dependencies
    
* Run the Django server
    

If everything goes well, you’ll see logs from the Django server, and you can open your browser and go to `http://localhost:8000`.

You should see the Django welcome screen.

## Common Issues

### Port Already in Use?

If port 8000 is busy, change this line in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"
```

Then go to `http://localhost:8001`.

### Database Not Working?

If you need a database (like PostgreSQL), you can add another service to `docker-compose.yml`. Here's an example with PostgreSQL:

```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
```

Then, update your `settings.py` in Django to use that database.

## FAQs

### **Do I need Docker for development?**

No, but it helps keep your environment clean and consistent. If it works in Docker, it'll work anywhere.

### **Can I run migrations inside Docker?**

Yes! Just run:

```bash
docker-compose run web python manage.py migrate
```

### **How do I stop everything?**

Press `Ctrl+C` to stop the running server, and if you want to remove containers:

```bash
docker-compose down
```

## Extra Tip: Use `.dockerignore`

Just like `.gitignore`, you can create a `.dockerignore` file to avoid copying unnecessary files into the Docker container. Here’s a simple one:

```nginx
__pycache__
*.pyc
*.pyo
*.pyd
.env
.git
```

## What You’ve Built

By now, you’ve:

* Created a Django project
    
* Built a Docker container for it
    
* Set up `docker-compose` to run everything
    
* Learned how to manage it all easily
    

Once you’re comfortable, you can expand this setup with static files, NGINX, Gunicorn, or even production-ready Docker builds.

## Want to Go Deeper?

If this feels like a lot, that’s ok. It takes a little practice, but once you’ve done it a few times, Docker becomes second nature.

You’ll spend less time debugging setup issues and more time coding your app.

### Further Reading

* [Docker Documentation](https://docs.docker.com/)
    
* [Django Official Docs](https://docs.djangoproject.com/)
    
* [Compose File Reference](https://docs.docker.com/reference/compose-file/)
