---
title: Why You Should Start Using Docker Right Now
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-11-17T20:42:19.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-start-using-docker-now
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/why-use-docker-image.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: null
seo_desc: 'About a year back, I was just about ready to release Caer, a Computer Vision
  library in Python that would be publicly available on PyPi. But first, I decided
  to send it to a friend in Alberta to tinker around with it.

  A few days later, I found that h...'
---

About a year back, I was just about ready to release [Caer](https://github.com/jasmcaus/caer), a Computer Vision library in Python that would be publicly available on PyPi. But first, I decided to send it to a friend in Alberta to tinker around with it.

A few days later, I found that he was still trying to figure out how to get it to work on his machine.

After dozens of hours, I finally found out why — Caer implemented code from the previous versions of other Python packages that simply wasn't available in their newer releases.

And so despite having those packages installed, my friend wasn’t able to run Caer.

Issues like this aren’t specific to Python packages. You might face something similar when moving locally-built code into production and not have it work because of different operating systems.

But what if there was a way to mitigate this issue of portability?

> Well, there is – Docker!

Before we talk about Docker, you need to understand the intuition behind a *container.*

## What is a Container?

A container is an entire runtime environment: an application with all its dependencies, libraries, binaries, and configuration files needed to run it, bundled up into one package.

![Very Blue Sky](https://images.unsplash.com/photo-1504383633899-a17806f7e9ad?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDZ8fGNvbnRhaW5lcnxlbnwwfHx8fDE2MzY3NDEwMzM&ixlib=rb-1.2.1&q=80&w=2000 align="left")

*Photo by \[Unsplash\](https://unsplash.com/@victoire\_jonch?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit"&gt;Victoire Joncheray / &lt;a href="https://unsplash.com/?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit)*

*Containerization* abstracts away differences in OS distributions, application dependencies, and underlying infrastructure.

## Containers are like VMs, but way smaller

With virtualization, these containers are called *Virtual Machines.* These include the operating system in addition to the application. A server running three virtual machines may have three different operating systems running on top of it.

Imagine how bulky this can get.

In contrast, you can have the same server run 3 containerized applications with Docker that all run the *same* operating system. The parts of the operating system that are shared are *read-only*, while a container has a mount (a way to access the container) for writing.

While VMs may be several gigabytes in size, a container may be just a few megabytes in size.

## The magic of containers

When applications are containerized, only the *operating system* is virtualized, as opposed to hardware (as is the case with VMs). Instead of provisioning hardware, a virtual OS is provisioned to the application, enabling you to run multiple applications and set resource-limitations as you please.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-42.png align="left")

[*Source*](https://containerjournal.com/topics/container-ecosystems/kubernetes-vs-docker-a-primer/)*: Container Journal*

## How to Use Docker

Docker is a containerization tool used that developers use to spin up isolated, reproducible environments for their applications.

It has a fast development process, it is easy to use, it works the same on local machines, dev, staging, and production servers, and it is extremely scalable.

Docker, in fact, drove the shift to the containerization of applications, and is, to no one's surprise, the most powerful player in the market today.

#### How to install Docker

* Windows or MacOS: Install [Docker Desktop](https://www.docker.com/get-started)
    
* Linux: Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
    

If you are on Linux, you’ll need to run your commands as *root* or add the user to the Docker group:

```bash
sudo usermod -aG docker $(thatsme)
```

## How to Create a Dockerfile

In Python, to containerize an application, you will need to pack it as a Docker Image. To generate one, you need to define a Dockerfile. This name of the file is simply **DOCKERFILE** (no extension).

```dockerfile
# Defining a base image (Python 3 in our case)
FROM python:3# Adding a Python script to be run

ADD hello_world_script.py /

# If our script uses the Caer package, we'll have to pip install it:RUN pip install caer

# To execute the Python script:
CMD [ "python", "./hello_world_script.py" ]
```

* `FROM` instructs Docker what image the application is based on (a mouthful, I know)
    
* `RUN` executes any additional commands (such as a pip install)
    
* `CMD` executes the commands when the image is loaded
    

For this demonstration, I have used the `caer` package that you can install with a simple `pip install caer` .

Suppose, our `hello_world_script.py` script looks like this:

```python

import caer

print(caer.__version__)

img = caer.imread('./img1.png')

print(img.shape) # image shape
print(img) # image tensor
```

To build the image from the Dockerfile, go ahead and run the following:

```bash
docker build -t caer-readimg .
```

Once the image has been built, you’ll be able to run it as a container.

You’ll also notice a ‘caer-readimg’ image (you can view all your Docker image by running the `docker images` command).

To run this image,

```bash
docker run caer-readimg
```

## How to delete a Docker Image

```bash
# The image_id can be found when you run `docker images`

docker rmi <image_id>
```

## How to delete a Docker Container

```bash
# Retrieve the container ID:
docker ps -a 

# Deleting the container
docker rm <container_id>
```

# Wrapping Up

That’s how easy it is to get started with Docker. Of course, you probably don't need to build a Docker image if your application is as simple as the code discussed above – but it makes sense especially if you’re working on the same project with multiple people.

Be sure to [follow me on Twitter](http://twitter.com/jasmcaus) for updates on future articles. Happy learning!
