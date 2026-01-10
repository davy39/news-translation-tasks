---
title: Docker Development WorkFlow — a guide with Flask and Postgres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-08T11:05:40.000Z'
originalURL: https://freecodecamp.org/news/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NlqpTTAM8DbGl4paBmjE_g.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Timothy Ko

  Docker, one of the latest crazes, is an amazing and powerful tool for packing, shipping,
  and running applications. However, understanding and setting up Docker for your
  specific application can take a bit of time. Since the internet is ...'
---

By Timothy Ko

Docker, one of the latest crazes, is an amazing and powerful tool for packing, shipping, and running applications. However, understanding and setting up Docker for your specific application can take a bit of time. Since the internet is filled with conceptual guides, I won’t be going too deep conceptually about Containers. Instead, I’ll be explaining what each line I write means and how you can apply that to your specific application and configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/Qv18K6q0lHj07pm6jZk8lWgCkfib7Zg6xQMP)
_Photo by [Unsplash](https://unsplash.com/photos/m_HRfLhgABo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Christopher Gower</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Why Docker?

I am part of a student-run non-profit called Hack4Impact at UIUC, where we develop technical projects for non-profit organizations to help them further their missions. Each semester, we have multiple project teams of 5–7 student software developers, with a variety of skill levels including students who have only finished their first college-level computer science course.

Since many non-profits often asked for web applications, I curated a Flask Boilerplate to allow teams to quickly get their backend REST API services up and running. Common utility functions, application structure, database wrappers, and connections are all provided along with documentation for setup, best coding practices, and steps for Heroku deployment.

#### Issues with Development Environment and Dependencies

However, since we onboard new student software developers every semester, teams would spend a lot of time configuring and troubleshooting environment issues. We would often have multiple members developing on different Operating Systems and ran into a myriad of problems(Windows, I’m pointing at you). Although many of those problems were trivial, such as starting up the correct PostgreSQL database version with the right user/password, it wasted time that could’ve been put into the product itself.

In addition to that, I only wrote documentation for MacOS users with only bash instructions (I have a Mac), and essentially left Windows and Linux users out to dry. I could’ve spun up some Virtual Machines and documented the setup again for each OS, but why would I do that if there’s Docker?

#### Enter Docker

With Docker, the entire application can be isolated in containers that can be ported from machine to machine. This allows for consistent environments and dependencies. Thus, you can “build once, run anywhere,” and developers will now be able to install just **one** thing — Docker — and run a couple commands to get the application running. Newcomers will be able to rapidly begin developing without worrying about their environment. Nonprofits will also be able to quickly make changes in the future.

Docker also has many other benefits, such as its portable and resource-efficient nature (compared to Virtual Machines), and how you can painlessly set up Continuous Integration and rapidly deploy your application.

### A Brief Overview of Docker Core Components

There are many resources online that will explain Docker better than I can, so I won’t go over them in too much detail. Here’s an [awesome blog post](https://medium.freecodecamp.org/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b) on its concepts, and [another one](https://medium.com/@xenonstack/docker-overview-a-complete-guide-43decd218eca) on Docker specifically. I will, however, go over some of the Core Components of Docker that are required to understand the rest of this blog post.

#### Docker Images

Docker images are read-only templates that describe a Docker Container. They include specific instructions written in a Dockerfile that defines the application and its dependencies. Think of them as a snapshot of your application at a certain time. You will get images when you `docker build`.

#### Docker Containers

Docker Containers are instances of Docker images. They include the operating system, application code, runtime, system tools, system libraries, and so on. You are able to connect multiple Docker Containers together, such as a having a Node.js application in one container that is connected to a Redis database container. You will run a Docker Container with `docker start`.

#### Docker Registries

A Docker Registry is a place for you to store and distribute Docker images. We will be using Docker Images as our base images from DockerHub, a free registry hosted by Docker itself.

#### Docker Compose

Docker Compose is a tool that allows you to build and start multiple Docker Images at once. Instead of running the same multiple commands every time you want to start your application, you can do them all in one command — once you provide a specific configuration.

### Docker example with Flask and Postgres

With all the Docker components in mind, let’s get into setting up a Docker Development environment with Flask Application using Postgres as its data store. For the remainder of this blog post, I will be referencing [Flask Boilerplate](https://github.com/tko22/flask-boilerplate), the repository I mentioned earlier for Hack4Impact.

In this configuration, we will use Docker to build two Images:

* `app` — the Flask Application served in port 5000
* `postgres` — the Postgres Database served in port 5432

When you look at the top directory, there are three files that define this configuration:

* **Dockerfile** — a script composed of instructions to setup the `app` containers. Each command is automatic and is successively performed. This file will be located in the directory where you run the app(`python manage.py runserver` or `python app.py` or `npm start` are some examples). In our case, it is in the top directory(where `manage.py` is located). A Dockerfile accepts [Docker Instructions](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#build-cache).
* **.dockerignore** — specifies which files not to include in the Container. It is just like `.gitignore` but for the Docker Containers. This file is paired with the Dockerfile.
* **docker-compose.yml** — Configuration file for Docker Compose. This will allow us to build both `app` and `postgres` images at once, define volumes and state that `app` depends on `postgres`, and set required environmental variables.

**Note:** There’s only one Dockerfile for two images because we will be taking an official Docker Postgres image from DockerHub! You can include your own Postgres Image by writing your own Dockerfile for it, but there’s no point.

#### Dockerfile

Just to clarify again, this Dockerfile is for the `app` container. As an overview, here is the entire Dockerfile—it essentially gets a base image, copies the application over, installs dependencies, and sets a specific environment variable.

```
FROM python:3.6
```

```
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"
```

```
RUN apt-get update
```

```
RUN mkdir /app
```

```
WORKDIR /app
```

```
COPY . /app
```

```
RUN pip install --no-cache-dir -r requirements.txt
```

```
ENV FLASK_ENV="docker"
```

```
EXPOSE 5000
```

Because this Flask Application uses Python 3.6, we want an environment that supports it and already has it installed. Fortunately, [DockerHub](https://hub.docker.com/) has an official image that’s installed on top of Ubuntu. In one line, we will have a base Ubuntu image with Python 3.6, virtualenv, and pip. There are tons of images on DockerHub, but if you would like to start off with a fresh Ubuntu image and build on top of it, you could do that.

```
FROM python:3.6
```

I then note that I’m the maintainer.

```
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"
```

Now it’s time to add the Flask application to the image. For simplicity, I decided to copy the application under the `/app` directory on our Docker Image.

```
RUN mkdir /app
```

```
COPY . /app
```

```
WORKDIR /app
```

`WORKDIR` is essentially a `cd` in bash, and `COPY` copies a certain directory to the provided directory in an image. `ADD` is another command that does the same thing as `COPY` , but it also allows you to add a repository from a URL. Thus, if you want to clone your git repository instead of copying it from your local repository (for staging and production purposes), you can use that. `COPY`, however, should be used most of the time unless you have a URL. Every time you use `RUN`, `COPY`, `FROM`, or `CMD`, you create a new layer in your docker image, which affects the way Docker stores and caches images. For more information on best practices and layering, see [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

Now that we have our repository copied to the image, we will install all of our dependencies, which is defined in `requirements.txt`

```
RUN pip install --no-cache-dir -r requirements.txt
```

But say you had a Node application instead of Flask — you would instead write `RUN npm install`. The next step is to tell Flask to use Docker Configurations that I hardcoded into `config.py`. In that configuration, Flask will connect to the correct database we will set up later on. Since I had production and regular development configurations, I made it so that Flask would choose the Docker Configuration whenever the `FLASK_ENV` environment variable is set to `docker`. So, we need to set that up in our `app` image.

```
ENV FLASK_ENV="docker"
```

Then, expose the port(5000) the Flask application runs on:

```
EXPOSE 5000
```

And that’s it! So no matter what OS you’re on, or how bad you are at following documentation instructions, your Docker image will be same as your team members’ because of this Dockerfile.

Anytime you build your image, these following commands will be run. You can now build this image with `sudo docker build -t app .`. However, when you run it with `sudo docker run app` to start a Docker Container, the application will run into a database connection error. This is is because you haven’t provisioned a database yet.

#### docker-compose.yml

Docker Compose will allow you to do that and build your `app` image at the same time. The entire file looks like this:

```
version: '2.1'services:  postgres:    restart: always    image: postgres:10    environment:      - POSTGRES_USER=${POSTGRES_USER}      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}      - POSTGRES_DB=${POSTGRES_DB}    volumes:      - ./postgres-data/postgres:/var/lib/postgresql/data    ports:      - "5432:5432"  app:    restart: always    build: .    ports:      - 5000:5000    volumes:      - .:/app
```

For this specific repository, I decided to use version 2.1 since I was more comfortable with it and it had a few more guides and tutorials on it — yeah, that’s my only reasoning for not using version 3. With version 2, you must provide “services” or images you want to include. In our case, it is `app` and `postgres`(these are just names that you can refer to when you use docker-compose commands. You call them `database` and `api` or whatever floats your boat).

#### Postgres Image

Looking at the Postgres Service, I specify that it is a `postgres:10` image, which is another DockerHub Image. This image is an Ubuntu Image that has Postgres installed and will automatically start the Postgres server.

```
postgres:  restart: always  image: postgres:10  environment:    - POSTGRES_USER=${USER}    - POSTGRES_PASSWORD=${PASSWORD}    - POSTGRES_DB=${DB}  volumes:    - ./postgres-data/postgres:/var/lib/postgresql/data  ports:    - "5432:5432"
```

If you want a different version, just change the “10” to something else. To specify what user, password, and database you want inside Postgres, you have to define environment variables beforehand — this is implemented in the official postgres Docker image’s Dockerfile. In this case, the `postgres` image will inject the `$USER`, `$PASSWORD`, and `$DB` environment variables and make them the `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` envrionment variables **inside** the postgres container. Note that `$USER` and the other environment variables injected are environment variables specified in your own computer (more specifically the command line process you are using to run the `docker-compose up` command. By injecting your credentials, this allows you to not commit your credentials into a public repository.

Docker-compose will also automatically inject environment variables if you have a `.env` file in the same directory as your `docker-compose.yml` file. Here’s an example of a .env file for this scenario:

```
USER=testusrPASSWORD=passwordDB=testdb
```

Thus our PostgreSQL database will be named **testdb** with a user called **testusr** with password **password.**

Our Flask application will connect to this specific database, because I wrote down its URL in the Docker Configurations I mentioned earlier.

Every time a container is stopped and removed, the data is deleted. Thus, you must provide a persistent data storage so none of the database data is deleted. There are two ways to do it:

* Docker Volumes
* Local Directory Mounts

I’ve chosen to mount it locally to `./postgres-data/postgres` , but it can be anywhere. The syntax is always`[HOST]:[CONTAINER]`. This means any data from `/var/lib/postgresql/data` is actually stored in `./postgres-data`.

```
volumes:- ./postgres-data/postgres:/var/lib/postgresql/data
```

We will use the same syntax for ports:

```
ports:- "5432:5432"
```

#### app Image

We will then define the `app` image.

```
app:  restart: always  build: .  ports:    - 5000:5000  volumes:     - .:/app  depends_on:    - postgres  entrypoint: ["python", "manage.py","runserver"]
```

We first define it to have `restart: always`. This means that it will restart whenever it fails. This is especially useful when we build and start these containers. `app` will generally start up before `postgres`, meaning that `app` will try to connect to the database and fail, since the `postgres` isn’t up yet. Without this property, `app` would just stop and that’s the end of it.

We then define that we want this build to be the Dockerfile that is in this current directory:

```
build: .
```

This next step is pretty important for the Flask server to restart whenever you change any code in your local repository. This is very helpful so you don’t need to rebuild your image over and over again every time to see your changes. To do this, we do the same thing we did for `postgres` : we state that the `/app` directory inside the container will be whatever is in .(the current directory). Thus, any changes in your local repo will be reflected inside the container.

```
volumes:  - .:/app
```

After this, we need to tell Docker Compose that app depends on the `postgres` container. Note that if you change the name of the image to something else like `database`, you must replace that `postgres` with that name.

```
depends_on:  - postgres
```

Finally, we need to provide the command that is called to start our application. In our case, it’s `python manage.py runserver`.

```
entrypoint: ["python", "manage.py","runserver"]
```

One caveat for Flask is that you must explicitly note which host (port) you want to run it in, and whether you want it to be in debug mode when you run it. So in `manage.py`, I do that with:

```
def runserver():    app.run(debug=True, host=’0.0.0.0', port=5000)
```

Finally, build and start your Flask app and Postgres Database using your Command Line:

```
docker-compose builddocker-compose up -ddocker-compose exec app python manage.py recreate_db
```

The last command essentially creates the database schema defined by my Flask app in Postgres.

And that’s it! You should be able to see the Flask application running on http://localhost:5000!

#### Docker Commands

Remembering and finding Docker commands can be pretty frustrating in the beginning, so [here’s](https://medium.com/statuscode/dockercheatsheet-9730ce03630d) a list of them! I’ve also written a bunch of commonly used ones in my [Flask Boilerplate Docs](https://github.com/tko22/flask-boilerplate) if you want to refer to that.

### Conclusion

Docker truly allows teams to develop much faster with its portability and consistent environments across platforms. Although I’ve only gone through using Docker for development, Docker excels when you use it for Continuous Integration/testing and in Deployment.

I could add a couple more lines and have a full production setup with Nginx and Gunicorn. If I wanted to use Redis for session caching or as a queue, I could do that very quickly and everyone on my team would be able to have the same environment when they rebuilt their Docker Images.

Not only that, I could spin up 20 instances of the Flask Application in seconds if I wanted to. Thanks for reading! :)

_If you have any thoughts and comments, feel free to leave a comment below or email me at tk2@illinois.edu! Also, feel free to use my code or share this with your peers!_

