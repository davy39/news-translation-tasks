---
title: How to Dockerize a React Application – A Step by Step Tutorial
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-07-18T14:54:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-a-react-application
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-pixabay-39656--1-.jpg
tags:
- name: Docker
  slug: docker
- name: React
  slug: react
seo_title: null
seo_desc: 'Picture this: you have developed an application that is ready to be deployed.
  You have worked really hard on it, so you want to make sure it gets deployed seamlessly
  and the final product is both fast and reliable. Enter images and containers.

  Images...'
---

Picture this: you have developed an application that is ready to be deployed. You have worked really hard on it, so you want to make sure it gets deployed seamlessly and the final product is both fast and reliable. Enter images and containers.

Images and containers help you package your application and run it in a lightweight and isolated environment. Containers make it possible to make faster and scalable deployments. And it's not that hard to start using them. All you have to do is write some scripts and run a few commands to have a container up and running. How cool is that?

In this tutorial, I am going to take a React application and show you, step by step, how to build an image, push it to a remote registry, and use that image to run your application in a container.

To follow along with this tutorial, I am assuming you are already familiar with the basics of images and containers. I'll start by explaining what Docker is and then dive into the process.

## What is Docker?

Docker is an open-source platform developer by [Docker, Inc.](https://www.docker.com/company/) It enables you to package your application and its dependencies and run it all in an isolated environment, called the container. With just a small set of instructions, you can easily build images and run them as containers.

Docker containers are extremely lightweight and efficient. Due to isolation, each container runs differently and the container processes do not interfere with each other. Docker also has its own version control system, Docker Hub, which we'll discuss later on in the tutorial.

Docker is widely used by enterprise technologies and cloud services that have chosen to adopt containerization for faster deployments. Lastly, Docker has a vast community and an ever-expanding ecosystem of tools and services. For more info, you can go through the [docs](https://docs.docker.com/get-started/).

Okay, enough about Docker (actually, not). You are here to get some hands-on practice and that's what we'll do here. Before we get started, you first need to install Docker on your system. Refer to [this](https://docs.docker.com/get-docker/) for a guide on installing Docker on different operating systems.

Run the command `docker --version` to check if Docker is installed.

## How to Create a Simple React Application

Use the following command to set up a simple React application.

```bash
create-react-app react-docker-example
```

You do not need to add any more dependencies to the project. All you need is a working application. Run `npm start` to see if the app is running properly.

Once the application is running and ready to deploy, we are ready to start Dockerizing it!

## How to Write a Dockerfile

To build an image of your application, you need to specify instructions for the same in a Dockerfile. The instructions from this file will be executed one after the other. You'll find a reference to all the instructions [here](https://docs.docker.com/engine/reference/builder/).

A Docker image consists of different layers stacked on top of each other. Each instruction in the Dockerfile adds a new layer on top of the existing ones. Each layer in the image is stored as a SHA-256 hash.

Note that not all instructions create new layers. Certain instructions like `LABEL`, `ENV`, and `ARG` are only set to provide some metadata for the image. Read [this](https://kodekloud.com/blog/docker-image-layers/) to learn more about image layers.

Let's go over the instructions we'll need, one by one.

```python
FROM node:18-alpine
```

This instruction pushes the base image from a remote repository (in this case, the Docker Hub) and defines the starting point for the image layers. The syntax for specifying the image is

![](undefined align="left")

: where tag represents the version of the image.

Since React is a Node-based application, we'll pull a Node image from the repository. Specify the version of the image you want to pull. You can get a list of versions [here](https://hub.docker.com/_/node/tags).

If you specify *latest,* it will pull the latest version – that is whenever the image is upgraded, it will always fetch the latest one. But this is not a good practice for applications deployed in production.

```python
WORKDIR /react-docker-example/
```

This command sets the working directory for any commands you add in the Dockerfile. So, while building the image, the commands will be executed in this directory.

```python
COPY public/ /react-docker-example/public
COPY src/ /react-docker-example/src
COPY package.json /react-docker-example/
```

These instructions will copy the files we need into the working directory. We only need the public and src folders (where your code resides), and the package.json file to run the application.

```python
RUN npm install
```

The `RUN` instruction executes any command by adding a new layer on top of the current ones, thus modifying the image. This modified image will be used for the next steps.

In this case, it installs all the dependencies specified in the `package.json` file. This is why we did not copy the `node_modules` folder into the working directory. The folder will be created after this command gets executed.

```python
CMD ["npm", "start"]
```

This instruction defines the command that will be executed when starting a container from the image. There can only be one `CMD` instruction in the Dockerfile. If there are more than one, then only the last one will be considered.

Since `npm start` is the command used for starting a React app, we'll specify the same for running the container.

## How to Build the Image

Now that we have written the Dockerfile, it's time to build the image. Open your terminal (or cmd in Windows) and execute the following command.

```python
docker image build -t <image_name>:<tag> <path>
```

`-t` option specifies the name and tag for the image. `<path>` represents the path in which you want to run the command.

We'll name the image react-docker-example and give it a tag `latest`. Make sure you change into the project's root directory using `cd react-docker-example` before executing the command.

```python
docker image build -t react-example-image:latest .
```

The `.` at the end represents the current directory.

Once you hit enter, this command will execute each instruction in the Dockerfile one by one.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-6.08.46-PM.png align="left")

*Output of the docker build command*

In the above image, you can see that each instruction in the Dockerfile is getting executed in a new layer on top of the previous ones. In the end, the image is represented by a single sha256 hash which is the image id.

Now, run `docker images` to see a list of images in your system. You'll see the details of the image you just created.

That's all it takes to build a Docker image: a few instructions in a Dockerfile and one command.

## How to Push the Image to Docker Hub

Now, the image that you created resides in your local system. But what if you want to make it accessible to your team members? Similar to Git, you would need to push the image to a remote repository.

Docker Hub is a repository (or registry) where you can push your image as well as access other open source images. Similar to Node, there are other base images such as Ubuntu, Python, Redis, and so on. Check them out [here](https://hub.docker.com/search).

To start using [Docker Hub](https://hub.docker.com/signup), you first need to create an account.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.26.02-PM.png align="left")

*Register into Docker Hub*

Then, go to repositories and click on Create repository.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.25.24-PM.png align="left")

*Repositories*

Specify a repository name and mark it public or private. In the community edition, you are only allowed to have 1 private repository. Click on Create.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.37.41-PM.png align="left")

*Create Repository*

Now, this is how your repository looks. You can push your image into this repository. Since this is a public repository, anyone can pull your images. But only you have the permission to push.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.39.30-PM.png align="left")

Now that you have created your remote repository, it's time to push your image. First, you need to login using your credentials.

```python
docker login
```

After this, tag the image with your username.

```python
docker image tag react-example-image <username>/react-example-image
```

Now, run this command to push the image.

```python
docker push kunalmac25/react-example-image
```

Since you have not specified an image tag (that is, a version), it will use the default one – the latest. Unlike the version tag, it is necessary to tag the image name with your username. This gives you the complete ownership of the image and prevents any potential naming conflicts.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.49.48-PM.png align="left")

*Image pushed to the repository*

The latest version of your image has been pushed into the repository. Let's say, in the future, you have made changes to your application. You can create an upgraded version of the same image, tag it with the new version name and then, push it.

```python
docker image build -t react-example-image:upgrade .
```

```python
docker image tag react-example-image:upgrade <username>/react-example-image:upgrade
```

```python
docker push kunalmac25/react-example-image:upgrade
```

Now, open your repository and check the images.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-10.58.50-PM.png align="left")

*List of Images*

You can see a list of all versions of your images.

## How to Create a Container from the Image

At this point, we have bundled package including everything needed to run the React application. Now, we need to create a container to run your application. Run the following command.

```python
docker run -dp 8000:3000 --name react-example-container react-docker-example:latest
```

* `-d` runs the container in detached mode – that is, it will run in the background and not display the running process on your terminal.
    
* `-p` maps the port in the form `<host_port>:<container_port>`. The host port represents the port on the host machine that is mapped to the port inside the container. Since a React app is exposed through port 3000, we will map it to the port 8000 on your host machine.
    
* The `--name` flag specifies the name for the container.
    
* After these, you specify the image name and tag.
    

If the image does not exist on your local system, it will try to find the image in the Docker registry.

To check this, delete your local image using `docker image rm react-example-image` and run the above command. Since there is an image with the same name on Docker Hub (the one you just pushed), it will download the image and create a container out of it.

Now, run `docker ps` or `docker container ps` to show a list of all the running containers.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-14-at-9.14.41-PM.png align="left")

*Running Containers*

Now, open your browser and go to `http://localhost:8000`. You'll be able to access your application.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-15-at-8.27.46-PM.png align="left")

*Application Running in a Container*

To stop a running container, use the `docker stop` command with the container id or name.

```python
docker stop <container_id>
```

Now, if you run `docker ps`, it won't show the container as it only shows the running ones. If you want to see all the containers, including the non-running ones, use `docker ps -a`.

Also, navigate to the same URL and you won't be able to see anything since the container is not running. To restart the container, run `docker start <container_id>`.

To remove the container, use the `docker rm` command followed by the container id or name.

```python
docker rm <container_id>
```

Congratulations! You have just run the application in an isolated environment where no other process is going to interfere with it. This makes your application faster and more reliable. Containers are extremely lightweight, so you can easily scale up the application.

Also, you do not need to worry about missing dependencies or conflicting versions. All the dependencies that your application needs are bundled inside the container. That's the beauty of containers!

## Next Steps

![Image](https://images.unsplash.com/photo-1505909487039-08022c92a8ab?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDEzfHxuZXh0JTIwc3RlcHN8ZW58MHx8fHwxNjg5NTgxMTUyfDA&ixlib=rb-4.0.3&q=80&w=2000 align="left")

*Photo by \[Unsplash\](https://unsplash.com/@createandbloom?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit"&gt;Photo Boards / &lt;a href="https://unsplash.com/?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit)*

At this point, you have a packaged application running in its own isolated environment. But we are just halfway there. The container is still running on your local machine. Once your application is tested and ready to go, you'll need to ship that container.

There are several orchestration platforms like Kubernetes and Docker Swarm and cloud provides like Google, AWS, Azure, and others that make it possible. These are very useful when you want to deploy your application in different environments (dev, test, or production). We'll discuss container orchestration in a future post. That's it for today.

## Conclusion

In this article, I explained what Docker is and why you should use it. Then, I showed you how to build an image by writing a Dockerfile, which is just a set of instructions to build a Docker image. After building an image in your local system, you can push that image to a remote registry, Docker Hub.

Once your application is all packaged up, it is time to run the application in a container, an isolated environment with everything that your application needs. You can start, stop and remove the containers using Docker commands. After that, I showed you a glimpse of what you could do next.

Containers provide a very lightweight and a faster solution for all your deployments and Docker makes it very easy and convenient. Containers have a really promising future with more and more enterprises adopting containerization.

I have explained all the steps in simple words and a straightforward example. I hope you were able to get a good grasp of the process.

If you are unable to understand the content or find the explanation unsatisfactory, let me know. New ideas are always appreciated! Feel free to connect with me on Twitter. Till then, Goodbye!
