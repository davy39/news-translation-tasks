---
title: Docker 101 - how to get from creation to deployment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-31T07:31:53.000Z'
originalURL: https://freecodecamp.org/news/docker-101-creation-to-deployment
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca090740569d1a4ca496f.jpg
tags:
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: Tutorial
  slug: tutorial
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: 'By Usheninte Dangana

  Docker is a game-changer, and has very much altered the world of application development.
  Learn the vital skills needed to work with this container technology today.

  What is Docker?

  In simple terms, Docker is a tool that lets dev...'
---

By Usheninte Dangana

Docker is a game-changer, and has very much altered the world of application development. Learn the vital skills needed to work with this container technology today.

## What is Docker?

In simple terms, **Docker** is a tool that lets developers to create, deploy, and run applications in containers. **_Containerization_** is the use of Linux containers to deploy applications.

So why is Docker so great, and why should we as developers even bother learning it?

| Reason | Explanation |
|:---:|---|
| Flexible | Even the most complex applications can be containerized. |
| Lightweight | Containers leverage and share the host kernel. |
| Interchangeable | You can deploy updates and upgrades on-the-fly.
| Portable | You can build locally, deploy to the cloud, and run anywhere. |
| Scalable | You can increase and automatically distribute container replicas. |
| Stackable | You can stack services vertically and on-the-fly. |

Now that we know why Docker is such a big deal, let's have it installed on our local machine.

Sign up for an account on [Docker Hub](https://hub.docker.com/signup) and download the free Docker Desktop application.

## How is Docker different from traditional Virtual Machines?

A container runs natively on Linux and shares the kernel of the host machine with other containers. It runs as a discrete process, taking no more memory than any other executable meaning it's very lightweight.

By contrast, a virtual machine (VM) runs a full-blown “guest” operating system with virtual access to host resources through a hypervisor. In general, VMs provide an environment with more resources than most applications need.

When working with Docker, a `Dockerfile` defines what goes on in the environment inside your container. Access to resources like networking interfaces and disk drives are virtualized inside this environment, which is isolated from the rest of your system. This means that you need to map ports to the outside world, and be specific about what files you want to “copy in” to that environment. However, after doing that, you can expect that the build of your app defined in this `Dockerfile` behaves exactly the same wherever it runs.

## Docker Commands

To test that you have a running version of Docker, run the following command:

`docker --version`

To test that your installation is working perfectly, try running the simple Docker **hello-world** image:

`docker run hello-world`

If all is set up properly, you should see output similar to the following:

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

To see the **hello-world** Docker image that was downloaded to your computer, use the Docker image listing command:

`docker image ls`

Awesome! You've already started developing containerized applications with Docker. Here are some helpful basic Docker commands:

```
## List Docker CLI commands
docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world

## List Docker images
docker image ls

## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq
```

<blockquote>
Containerization makes CI/CD seamless. For example:

- applications have no system dependencies
- updates can be pushed to any part of a distributed application
- resource density can be optimized.
- With Docker, scaling your application is a matter of spinning up new executables, not running heavy VM hosts.
</blockquote>

## Let's build a Node.js web app using Docker

The first thing we do is create a `package.json` file. We can do this quickly by simply running the following command:

```
npm init -y
```

This creates the file above with certain essential fields already filled in or left blank.

Your file should look something like this:

```json
{
  "name": "app-name",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Next, we install `express.js`, which according to the [official website](http://expressjs.com/), is a "**Fast, unopinionated, minimalist web framework for Node.js**".

We do this by running the following command in a terminal:

```
npm install express --save
```

The command above adds the `express.js` framework to our application, with the **--save** flag acting as an instruction to the application to use `express.js` as a dependency.

Now, go into your `package.json`, and change the `"main": "index.js"` key-value pair to the following:

```
"main": "app.js"
```

Next, create a `.gitignore` file using the following command:

```
touch .gitignore
```

Then add the following line:

```
node_modules/
```

> This prevents the **node_modules** folder which is essential to `node.js` development from being tracked by `git`.

Now add the following code to the `app.js` file:

```js
const express = require('express');

const app = express();

const PORT = 8080;
const HOST = '0.0.0.0';

app.get('/', (req, res) => {
  res.send(
    `
    <h1>Home</h1>
    <p>Docker is awesome!</p>
    <a href="/more" alt="Next Page">Next Page</a>
    `
  )
});

app.get('/more', (req, res) => {
  res.send(
    `
    <h1>Page Two</h1>
    <p>Node.js is pretty great too!!</p>
    <a href="/" alt="Back Home">Back Home</a>
    `
  )
});

app.listen(PORT, HOST);
console.log(`Running on https://${HOST}:${PORT}`);
```

To have this run on your local machine, run the following command in the application folder:

```
npm start
```

> You will find the application running at `http://0.0.0.0:8080/`

### Awesome!

![Congratulations](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif)
_Congratulations on making it this far_

---

## Into the Dockerverse

Now create a `Dockerfile` with the following command:

```
touch Dockerfile
```

Then add in the following code:

```
# An official Docker image for Node.js
FROM node:10-alpine

# Working directory for the containerised application
WORKDIR /src/app

# This copies significant package.json files to the current directory
COPY package*.json ./
# Install essential Node.js dependencies
RUN npm install

COPY . .

# Opens up this port on the Docker container
EXPOSE 8080

# This starts the Docker application
CMD [ "npm", "start" ]
```

The comments above attempt to explain what each `Dockerfile` command does.

Also, add a `dockerignore` file to prevent the containerisation of certain components of the application.

Place this inside of the `dockerignore` file:

```
node_modules
npm-debug.log
Dockerfile*
docker-compose*
.dockerignore
.git
.gitignore
README.md
LICENSE
```

## How to Deploy

The `<image-name>` is the name you assign to your Docker app, and `<tag>` is essentially just a version indicator for your Docker image.
* `docker build -t image-name:tag .`

Run this to access your Docker account from your terminal.
* `docker login`

Create a repository on Docker Hub.

Tag `<image>` for upload to registry.
* `docker tag <image-name> username/repository:tag`

Upload the tagged image to the registry.
* `docker push username/repository:tag`

Run the deployed Docker container on your local machine by connecting its PORTS. Target the exposed 8080 port, and assign it to port 10203 on your machine.
* `docker run -p 10203:8080 username/repository:tag`

---

#### That's it! You have built and deployed a containerised Node.js web application.

All the code above can be found in [this Github repository](https://github.com/Usheninte/docker-101).

> Originally posted [here](https://blog.ninte.dev/docker-101-creation-to-deployment-cjzylgqnc0019eus1s10lg39r) on [**blog.ninte.dev**](https://blog.ninte.dev)


