---
title: How to Enable Live-reload on Docker-based Applications with Docker Volumes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-25T17:16:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-live-reload-on-docker-based-applications
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a0f740569d1a4ca233c.jpg
tags:
- name: Docker
  slug: docker
- name: Docker compose
  slug: docker-compose
- name: Docker Containers
  slug: docker-containers
- name: node
  slug: node
seo_title: null
seo_desc: 'By Erick Wendel

  In this post you''ll learn how to configure a development environment with live-reload
  enabled. This will allow you to convert a legacy application so it uses Docker,
  Docker volumes, and docker-compose.

  Some developers turn up their no...'
---

By Erick Wendel

In this post you'll learn how to configure a development environment with live-reload enabled. This will allow you to convert a legacy application so it uses Docker, Docker volumes, and docker-compose.

Some developers turn up their noses when talking about using Docker for their development environment. They say that Docker isn't good for development because it always needs to rebuild the entire image to reflect all new modifications. This makes it unproductive and slow. 

In this article, our goal is to tackle this mindset by demonstrating how simple configurations can result in many benefits such as a reliable environment over production and development environments.

By the end of this post you will have learned how to:

* Convert a legacy application to run within a Docker container;
* Enable dependency caching on Node.js modules;
* Enable live-reload by using docker volumes;
* Aggregate all services within docker-compose.

## **Requirements**

In the next steps, you'll clone an existing project to execute all examples in this article. Before starting to code make sure you have the following tools installed on your machine:

* [Docker](https://docs.docker.com/desktop/) and [Docker compose](https://docs.docker.com/compose/)
* [Node.js 1](https://nodejs.org/en/download/current/)0+
* [Git](https://code.visualstudio.com/download)

## **Why use docker?**

More and more cutting-edge technologies are being released for the internet all the time. They're stable, and they're fun to develop and release, but they're not predictable when working over different environments. So developers created Docker to help reduce the chances of possible errors.

Docker is one of my favorite tools that I work with every day on desktop, web, and IoT apps. It has given me the power to not only move applications through different environments, but also to keep my local environment as clean as possible.  

Developers working with cutting-edge technologies are always working with something new. But what about legacy applications? Should we just rewrite everything with new tech? I know this is not as simple as it seems. We should work on new stuff, but also make improvements to existing applications. 

Let's say you have decided to move from Windows Servers to Unix servers. How would you do it? Do you know every dependency your app requires to work?

## What should a development environment look like?

Developers have always tried to be more productive by adding plugins, boilerplates, and codebases on their editors/IDEs/terminals. The best environment in my opinion should be:

1. Easy to run and test;
2. Environment agnostic;
3. Fast to evaluate modifications;
4. Easy to replicate on any machine.

Following these principles, we'll configure an application over the next sections of this article. Also, if you've never heard about live-reload (or hot reload), it is a feature that watches for changes in your code and restarts the server if needed. So you don't need to go back and forth, restarting your app or even rebuilding the system.

## Getting started

First, you'll need to have an empty folder called `post-docker-livereload` which you'll use as a workspace. Go to the [Github repository](https://github.com/ErickWendel/nodejs-with-mongodb-api-example) and clone it on your post-docker-live-reload folder.

Secondly, let's analyse what the application requires. If you take a look at the README.md file, there are a few instructions demonstrating how to run this app as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-24-at-18.10.43-1.png)

It requires Node.js version 10 or higher and MongoDB. Instead of installing MongoDB on your local environment machine, you'll install it using Docker. You'll also expose it on localhost:27017 so applications that are not running through Docker can access it without knowing the internal Docker IP address. 

Copy the command below and paste it in your terminal:

```bash
docker run --name mongodb -p 27017:27017 -d mongo:4
```

Using the command above, it'll download and run the MongoDB instance. Notice that if you already have an instance with this name it'll throw an error about invalid name. 

If you see the error, run `docker rm mongodb` and it will remove any previous instance so you can run the docker run command again.

## Digging into the application

The README.md file says that you need a MongoDB instance running before starting your app, along with Node.js. 

If you have Node.js installed, go to the `nodejs-with-mongodb-api-example` folder and run the following commands:

```bash
npm i 
npm run build 
npm start
```

After running these commands, you can go to a browser on [http://localhost:3000](http://localhost:3000) and see the application running as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/01-start.gif)

Keep in mind that the app already has a command to enable live reload which is `npm run dev:watch`. The pipeline should reflect the following steps:

1. Developer changes Typescript files;
2. Typescript transpiles files to Javascript;
3. Server notices changes to Javascript and restarts the Node.js server.

So mirroring files to Docker containers will reflect all changes in the container. The `npm run build:watch` from the application will catch the changes and generate output files in the lib folder so the `npm run dev:run` will restart the server every time it has been triggered.

## Dockerizing applications

If Docker is a completely new world to you, don't be afraid! You will configure it from scratch. You'll need to create a few files to start:

1. `Dockerfile` - a receipt file that lists how to install and run your app;
2. `.dockerignore` - a file that lists what file(s) won't go within the Docker container instance.

### Creating the Dockerfile

The Dockerfile is the key concept here. There you specify the steps and dependencies to prepare and run the application. As long as you have read the README.md file, it will be easy to implement the receipt file. 

I'm going to put the whole file below and dig into it later. In your `nodejs-with-mongodb-api-example` folder create a `Dockerfile` file and paste the code below:

```dockerfile
FROM node:14-alpine

WORKDIR /src

ADD package.json /src 

RUN npm i --silent

ADD . /src 

RUN npm run build 

CMD npm start
```

What's happening there?

* On line 1 - It uses as its image base Node.js 14 - alpine version;
* From lines 2 to 4 - It copies and installs Node.js dependencies from host to container. Note that the order there is important. Adding package.json to the src folder before restoring dependencies will cache it and prevent it from installing packages every time you need to build your image;
* From lines 6 to 7 - It runs commands for the compilation process and then for starting the program as mentioned in the README.md file.

### Ignoring unnecessary files with .dockerignore

Also, I'm working on an OSX-based system and the Docker container will run on a Linux Alpine-based system. When you run `npm install` it will restore dependencies for specific environments. 

You will now create a file to ignore the generated code from your local machine such as node_modules and lib_._ So when you copy all files from the current directory to the container it won't get invalid package versions. 

In the `nodejs-with-mongodb-api-example` folder create a `.dockerignore` file and paste the code below:

```txt
node_modules/
lib/
```

### Building the docker image

I prefer running this app from the rootFolder. Go back to the `post-docker-live-reload` folder and run the following commands to prepare an image for further use:

```shell
docker build -t app nodejs-with-mongodb-api-example
```

Notice that the command above uses the `-t` flag to tell you the image name and, right after that, the folder which contains the `Dockerfile` file.

### Working with volumes

Before running the app, let's do a few hacks to improve our experience in the Docker containers.

Docker volumes is a feature to mirror files through your local machine and Docker environment. You can also share volumes over containers and reuse them to cache dependencies.

Your goal is to watch any changes on local `.ts` files and mirror those changes in the container. Even though the files and the `node_modules` folder are in the same path. 

Do you remember when I said that the dependencies in each operating system would be different? To make sure our local environment won't affect the Docker environment when mirroring files, we'll isolate the container's `node_modules` folder on a distinct volume. 

Consequently, when creating the `node_modules` folder on the container, it won't create the folder on local machine environment. Run the command below in your terminal to create it:

```
docker volume create --name nodemodules

```

### Running and enabling live-reload

As you know, the `npm run dev:watch` specified in the README.md shows how to enable live-reload. The problem is that you're coding on a local machine and it must reflect directly your container. 

By running the following commands you will link your local environment with the Docker container so any change in `nodejs-with-mongodb-api-example` will affect the container's `src` folder.

```shell
docker run \
    --name app \
    --link mongodb \
    -e MONGO_URL=mongodb \
    -e PORT=4000 \
    -p 4000:4000 \
    -v `pwd`/nodejs-with-mongodb-api-example:/src \
    -v nodemodules:/src/node_modules \
    app npm run dev:watch
```

Let's dig into what's happening there:

* `--link` is giving permission to the app to access the MongoDB instance;
* `-e` - is the environment variables. As mentioned in the README.md file you can specify the MongoDB connection string you want to connect to by overriding the `MONGO_URL` variable. Override the `PORT` variable if you want to run it on a different port. Note that the value `mongodb` is the same name we used to create our MongoDB instance in the previous sections. This value is also an alias for the internal MongoDB instance's IP;
*  `-v` - maps the current directory to the Docker container by using a virtual volume. Using the `pwd` command you can get the absolute path for your current working directory and then the folder you want to mirror on the Docker container. There's the `:/src`. The `src` path is the `WORKDIR` instruction defined on `Dockerfile` so we mirror the local folder to the Docker container's src;
* `-v` - the second volume there will mirror the individual volume we created on the container's `node_modules` folder;
* `app` - the image name;
*  `npm run dev:watch` - this last command will override the `CMD` instruction from the `Dockerfile`.

After running the command below, you can trigger the browser after changing the local `index.ts` file to see the results. The video below demonstrates these steps in practice:

%[https://youtu.be/O9vEQhU_JEM]

## Wrapping up

You know that working with shell commands works. But is not that common to use them here, and it's not productive for running all those commands, building images, and managing instances by hand. So compose it!

Docker compose is a way to simplify the aggregation and linking of services. You can specify the databases, logs, application, volumes, networks, and so on.

First, you need to remove all active instances to avoid conflict on exposed ports. Run the following commands on your terminal to remove volumes, services and containers:

```bash
docker rm app 
docker volume rm nodemodules
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```

### The docker-compose file

Create a `docker-compose.yml` file on your `post-docker-livereload` folder using the data below:

```yaml
version: '3'
services:
    mongodb:
        image: mongo:4
        ports:
            - 27017:27017
    app:
        build: nodejs-with-mongodb-api-example
        command: npm run dev:watch
        ports:
            - 4000:4000
        environment: 
            MONGO_URL: mongodb
            PORT: 4000
        volumes:
            - ./nodejs-with-mongodb-api-example:/src/
            - nodemodules:/src/node_modules
        links:
            - mongodb
        depends_on: 
            - mongodb

volumes:
    nodemodules: {}
```

The file above specifies resources by sections. Notice that you have `links` and `depends_on` sections there. The links field is the same flag you've used in your shell command. The `depends_on` will make sure that the MongoDB is a dependency for running your app. It'll run the MongoDB before your app like magic! 

Going back to your terminal, to start all services and build the Docker image and create volumes and link services run the following command:

```shell
docker-compose up --build
```

If you need to remove all services created before by that `Dockerfile` you can also run `docker-compose down`.

## Docker is your friend!

That's right, my friend. Docker can help you prevent many possible errors before they happen. You can use it for front and back end applications. Even for IoT when you need to control hardware, you can specify policies for using it.

As your next steps, I highly recommend that you take a look at container orchestrators such as Kubernetes and Docker swarm. They could improve even more your existing applications and help you go to the next level.

## **Thank you for reading**

I really appreciate the time we spent together. I hope this content will be more than just text. I hope it will help make you a better thinker and also a better programmer. Follow me on [Twitter](https://twitter.com/erickwendel_) and check out my [personal blog](https://erickwendel.com/) where I share all my valuable content.

See ya! ?

