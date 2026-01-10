---
title: Docker Exec - How to Run a Command Inside a Docker Image or Container
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-04T14:49:12.000Z'
originalURL: https://freecodecamp.org/news/docker-exec-how-to-run-a-command-inside-a-docker-image-or-container
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/antoine-petitteville-hHntcuiLbOg-unsplash.jpg
tags:
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
- name: docker image
  slug: docker-image
seo_title: null
seo_desc: 'By Jillian Rowe

  I''m going to let you in on a DevOps secret here: The thing all DevOpsy people love
  to do is build a super fancy and complex system, then find a way to deal with it
  like a regular shell. Or connect to it with SSH and then treat it like...'
---

By Jillian Rowe

I'm going to let you in on a DevOps secret here: The thing all DevOpsy people love to do is build a super fancy and complex system, then find a way to deal with it like a regular shell. Or connect to it with SSH and then treat it like a regular shell.

Docker is no different! You are running a computer inside some other computer. Maybe that computer is an EC2 instance or a laptop. You can even get really crazy and run a VM that is then running Docker.

Most of the time when I use Docker I am using it to package and distribute an application. Sometimes I'm using it for something cooler like a distributed computing project. But a lot of times I'm throwing a Dockerfile in a GitHub repo so that I don't have to install CLIs that I just know will eventually conflict on my laptop.

Long story short, you can tell Docker to run the command `bash`, which drops you into a shell:

```bash
docker run -it name-of-image bash
# docker run -it continuumio/miniconda3:latest bash
# docker run -it node:latest bash
```

But keep reading for more. ;-)

## Try it out

Google your favorite programming language's Docker up. For me this is Python, and specifically I like conda. Then run a few commands to make sure that you are in fact in that shell.

```bash
# From Host
echo $(pwd)
# Drop into docker shell
docker run -it continuumio/miniconda3:latest bash
# Now you are in the docker shell!
echo $(pwd)
echo $USER
```

Cool, huh? This is perfect for debugging a container that absolutely should be working properly. It's also great for my most common "I don't want to install this to my computer" use case. 

## Debug a Docker Build with Docker Run

Treating your Docker image like a regular shell will come in handy when trying to debug Docker builds. 

Let's say you have a Dockerfile for an image you are trying to build. Normally what happens is that when running `docker build -t my-image .` (-t is for tag) Docker will run through each of your RUN steps, and stop when it gets to a command that does not exit properly. 

In a UNIX shell, the exit code 0 means that all is well with a command. So to illustrate this point I have made our Dockerfile have a RUN command that exits with 1. 

```bash
FROM continuumio/miniconda3:latest

RUN apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y \
    vim-tiny vim-athena build-essential

RUN  conda update conda \
    && conda clean --all --yes

RUN exit 1
```

```bash
docker build -t my-image .
```

This will get you an output that looks like: 

```bash
(base) ➜  my-image docker build -t my-image .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM continuumio/miniconda3:latest
 ---> 406f2b43ea59
Step 2/4 : RUN apt-get update -y;     apt-get upgrade -y;     apt-get install -y     vim-tiny vim-athena build-essential
 ---> Using cache
 ---> 726af29a48a0
Step 3/4 : RUN  conda update conda     && conda clean --all --yes
 ---> Using cache
 ---> 19478bb3ce67
Step 4/4 : RUN exit 1
 ---> Running in 7c98aab6b52c
The command '/bin/sh -c exit 1' returned a non-zero code: 1
```

You can confirm that your Docker image wasn't built by running `docker images` and checking for `my-image`. It won't be there because it wasn't successfully built. 

Now what we can do is to comment out that troublesome Dockerfile RUN command.

```bash
FROM continuumio/miniconda3:latest

RUN apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y \
    vim-tiny vim-athena build-essential

RUN  conda update conda \
    && conda clean --all --yes

#RUN exit 1
```

Then what you will see is:

```bash
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM continuumio/miniconda3:latest
 ---> 406f2b43ea59
Step 2/3 : RUN apt-get update -y;     apt-get upgrade -y;     apt-get install -y     vim-tiny vim-athena build-essential
 ---> Using cache
 ---> 726af29a48a0
Step 3/3 : RUN  conda update conda     && conda clean --all --yes
 ---> Using cache
 ---> 19478bb3ce67
Successfully built 19478bb3ce67
Successfully tagged my-image:latest

```

You can now drop into your Docker image and start interactively running commands!

```bash
docker run -it my-image bash
# you can also run
# docker run -it my-image:latest bash
```

From here, one by one, you can start debugging your RUN commands to see what went wrong. If you're not sure if a command exited properly or not, run `$?`:

```
# First run docker run -it my-image bash to get to the shell
# Print the string hello
echo "hello"
# hello
echo $?
# 0

# Run a non existant command hello
$(hello)
# bash: hello: command not found
echo $?
# 127
```

You can keep running these steps, commenting out your Dockerfile, dropping into a shell, and figuring out problematic commands, until your Docker images builds perfectly.

## Wrap Up

Hopefully I have shown you that using a Docker image is no different from the terminal on your computer. Using Docker images is an awesome way to distribute applications. 

Try to take your favorite CLI application or next GitHub project, and instead of creating an install script, package it up with Docker. ;-)

