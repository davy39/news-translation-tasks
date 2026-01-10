---
title: A beginner’s guide to Docker — how to create your first Docker application
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2019-04-02T17:17:11.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5ErAAkV5REH3bE6-xAzzFg.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'You are a developer and you want to start with Docker? This article is
  made for you.

  After a short introduction on what Docker is and why to use it, you will be able
  to create your first application with Docker.

  What is Docker?

  Docker is a free softw...'
---

#### You are a developer and you want to start with Docker? This article is made for you.

After a short introduction on what Docker is and why to use it, you will be able to create your first application with Docker.

#### **What is Docker?**

[Docker](https://www.docker.com/) is a free software developed by Docker Inc. It was presented to the general public on March 13, 2013 and has become since that day a must in the world of IT development.

It allows users to create independent and isolated environments to launch and deploy its applications. These environments are then called containers.

This will let the developer run a container on any machine.

As you can see, with Docker, there are no more dependency or compilation problems. All you have to do is launch your container and your application will launch immediately.

#### **But, is Docker a virtual machine?**

Here is one of the most asked question about Docker. The answer is: actually, not quite.

It may look like a virtual machine at first but the functionality is not the same.

Unlike Docker, a virtual machine will include a complete operating system. It will work independently and act like a computer.

Docker will only share the resources of the host machine in order to run its environments.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Blog.-Are-containers-..VM-Image-1-1024x435.png)
_Docker VS Virtual machines (Copyright to [Docker blog](https://blog.docker.com/2018/08/containers-replacing-virtual-machines/" rel="noopener))_

#### **Why use Docker as a developer?**

This tool can really change a developer’s daily life. In order to best answer this question, I have written a non-exhaustive list of the benefits you will find:

* Docker is fast. Unlike a virtual machine, your application can start in a few seconds and stop just as quickly.
* Docker is multi-platform. You can launch your container on any system.
* Containers can be built and destroyed faster than a virtual machine.
* No more difficulties setting up your working environment. Once your Docker is configured, you will never have to reinstall your dependencies manually again. If you change computers or if an employee joins your company, you only have to give them your configuration.
* You keep your work-space clean, as each of your environments will be isolated and you can delete them at any time without impacting the rest.
* It will be easier to deploy your project on your server in order to put it online.

### Now let’s create your first application

Now that you know what Docker is, it’s time to create your first application!

The purpose of this short tutorial is to create a Python program that displays a sentence. This program will have to be launched through a Dockerfile.

You will see, it’s not very complicated once you understand the process.

> Note: You will not need to install Python on your computer. It will be up to the Docker environment to contain Python in order to execute your code.

#### 1. Install Docker on your machine

_For Ubuntu:_

First, update your packages:

```
$ sudo apt update
```

Next, install docker with apt-get:

```
$ sudo apt install docker.io
```

Finally, verify that Docker is installed correctly:

```
$ sudo docker run hello-world
```

* _For MacOSX:_ you can follow [this link](https://docs.docker.com/docker-for-mac/install/).
* _For Windows:_ you can follow [this link](https://docs.docker.com/docker-for-windows/install/).

#### 2. Create your project

In order to create your first Docker application, I invite you to create a folder on your computer. It must contain the following two files:

* A ‘_main.py_’ file (python file that will contain the code to be executed).
* A ‘_Dockerfile_’ file (Docker file that will contain the necessary instructions to create the environment).

Normally you should have this folder architecture:

```
.
├── Dockerfile
└── main.py
0 directories, 2 files
```

#### 3. Edit the Python file

You can add the following code to the ‘_main.py_’ file:

```python
#!/usr/bin/env python3

print("Docker is magic!")
```

Nothing exceptional, but once you see “_Docker is magic!_” displayed in your terminal you will know that your Docker is working.

#### 3. Edit the Docker file

Some theory: the first thing to do when you want to create your Dockerfile is to ask yourself what you want to do. Our goal here is to launch Python code.

To do this, our Docker must contain all the dependencies necessary to launch Python. A linux (Ubuntu) with Python installed on it should be enough.

The first step to take when you create a Docker file is to access the [DockerHub](https://hub.docker.com/) website. This site contains many pre-designed images to save your time (for example: all images for linux or code languages).

In our case, we will type ‘Python’ in the search bar. The first result is [the official image](https://hub.docker.com/_/python) created to execute Python. Perfect, we’ll use it!

```python
# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:latest

# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.
COPY main.py /

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
CMD [ "python", "./main.py" ]
```

#### 4. Create the Docker image

Once your code is ready and the Dockerfile is written, all you have to do is create your image to contain your application.

```
$ docker build -t python-test . 
```

The ’_-t_’ option allows you to define the name of your image. In our case we have chosen ’_python-test_’ but you can put what you want.

#### 5. Run the Docker image

Once the image is created, your code is ready to be launched.

```
$ docker run python-test
```

You need to put the name of your image after ‘_docker run_’.

There you go, that’s it. You should normally see “Docker is magic!” displayed in your terminal.

### Code is available

If you want to retrieve the complete code to discover it easily or to execute it, I have put it at your disposal on my GitHub.

**->** [GitHub: Docker First Application example](https://github.com/gael-thomas/Docker-First-Application-example)

### Useful commands for Docker

Before I leave you, I have prepared a list of commands that may be useful to you on Docker.

* List your images.

```
$ docker image ls
```

* Delete a specific image.

```
$ docker image rm [image name]
```

* Delete all existing images.

```
$ docker image rm $(docker images -a -q)
```

* List all existing containers (running and not running).

```
$ docker ps -a
```

* Stop a specific container.

```
$ docker stop [container name]
```

* Stop all running containers.

```
$ docker stop $(docker ps -a -q)
```

* Delete a specific container (only if stopped).

```
$ docker rm [container name]
```

* Delete all containers (only if stopped).

```
$ docker rm $(docker ps -a -q)
```

* Display logs of a container.

```
$ docker logs [container name]
```

#### What’s next?

After all your feedback, I decided to write the next part of this beginner’s guide. In this article, you will discover how to use docker-compose to create your first client/server-side application with Docker.

-> [A beginner’s guide to Docker — how to create a client/server side with docker-compose](https://herewecode.io/blog/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose/)

## Conclusion

You can refer to this post every time you need a simple and concrete example on how to create your first Docker application. If you have any questions or feedback, feel free to ask.

If you want more content like this, you can [follow me on Twitter](https://twitter.com/gaelgthomas/), where I tweet about web development, self-improvement, and my journey as a full stack developer!

You can find other articles like this on my website: [herewecode.io](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/herewecode.io).

