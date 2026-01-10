---
title: Docker Detached Mode Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T19:55:00.000Z'
originalURL: https://freecodecamp.org/news/docker-detached-mode-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e2d740569d1a4ca3bc1.jpg
tags:
- name: Docker
  slug: docker
seo_title: null
seo_desc: 'Docker detached mode

  Detached mode, shown by the option --detach or -d, means that a Docker container
  runs in the background of your terminal. It does not receive input or display output.

  docker run -d IMAGE


  If you run containers in the background, ...'
---

## **Docker detached mode**

Detached mode, shown by the option `--detach` or `-d`, means that a Docker container runs in the background of your terminal. It does not receive input or display output.

```text
docker run -d IMAGE
```

If you run containers in the background, you can find out their details using `docker ps` and then reattach your terminal to its input and output.

#### **More Information:**

* [Attach to and detach from a running container | Docker Docs](https://docs.docker.com/engine/reference/commandline/attach/#examples)
* [Detached vs foreground | Docker docs](https://docs.docker.com/engine/reference/run/#detached-vs-foreground)

## More info about Docker

Docker is an open platform to build, ship, and run distributed applications. It is written in Go. It was first released in 2013 and is developed by Docker, Inc.

Docker is used to run packages called “containers”. Containers are isolated from each other and from the OS. These are more lightweight than virtual machines as they do not use the host machine to run an operating system.

Containerization, which is a way of deploying and running applications, runs isolated services which run natively on the Linux kernel. Memory can be set manually for each container in Docker.

Docker is used to simplify configurations, and ensure a smooth continuous integration and deployment flow. Specific containers can be specified for development, staging, and production environments. A true implementation of a container in production, according to the Docker manual, is to run it as a service, using the `docker-compose.yml` file for setup. This is a YAML file that defines how Docker containers should behave in production.

One of Docker’s biggest advantages is that it can be used by a team using different operating systems to build projects without needing to worry about software conflicts.

### **Installation**

* Ubuntu: `sudo apt install docker`
* RedHat: `yum install docker-ce`
* Windows / macOS: [Download](https://www.docker.com/get-started)
* Linux:

```text
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

#### **More Information:**

* For download and documentation check the docker official site: [Docker official site](https://www.docker.com/)

