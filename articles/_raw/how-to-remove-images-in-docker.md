---
title: How to Remove Images and Containers in Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T21:12:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-images-in-docker
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e04740569d1a4ca3ae5.jpg
tags:
- name: Docker
  slug: docker
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Docker rmi

  docker rmi removes images by their ID.

  To remove the image, you first need to list all the images to get the Image IDs,
  Image name and other details. By running simple command docker images -a or docker
  images.

  After that you make sure whi...'
---

## **Docker rmi**

`docker rmi` removes images by their ID.

To remove the image, you first need to list all the images to get the Image IDs, Image name and other details. By running simple command `docker images -a` or `docker images`.

After that you make sure which image want to remove, to do that executing this simple command `docker rmi <your-image-id>`. Then you can confirm that image has been removed or not by list all the images and check.

### **Remove multiple images**

There is a way to remove more than one images at a time, when you want to remove multiple specific images. So to do that first get Image IDs simply by listing the images then execute simple followed command.

`docker rmi <your-image-id> <your-image-id> ...`

Write Images IDs in the command followed by the spaces between them.

### **Remove all images at once**

To remove all images there is a simple command to do that. `docker rmi $(docker images -q)`

Here in the above command, there are two command the first which execute in the `$()` is shell syntax and returns the results whatever executed in that syntax. So in this `-q- is a option is used to provide to return the unique IDs,`$() returns the results of image IDs and then `docker rmi` removes all those images.

#### **For More Information:**

* [Docker CLI docs: rmi](https://docs.docker.com/engine/reference/commandline/rm/)

## **Docker rm**

`docker rm` removes containers by their name or ID.

When you have Docker containers running, you first need to stop them before deleting them.

* Stop all running containers: `docker stop $(docker ps -a -q)`
* Delete all stopped containers: `docker rm $(docker ps -a -q)`

### **Remove multiple containers**

You can stop and delete multiple containers by passing the commands a list of the containers you want to remove. The shell syntax `$()` returns the results of whatever is executed within the brackets. So you can create your list of containers within this to be passed to the `stop` and `rm` commands.

### Here is a breakdown of docker ps -a -q

* `docker ps` list containers
* `-a` the option to list all containers, even stopped ones. Without this, it defaults to only listing running containers
* `-q` the quiet option to provide only container numeric IDs, rather than a whole table of information about containers

#### **More Information:**

* [Docker CLI docs: rm](https://docs.docker.com/engine/reference/commandline/rm/)

## More info about images in Docker:

* [Docker image guide](https://www.freecodecamp.org/news/docker-image-guide-how-to-remove-and-delete-docker-images-stop-containers-and-remove-all-volumes/)
* [Where are Docker images stored?](https://www.freecodecamp.org/news/where-are-docker-images-stored-docker-container-paths-explained/)

## More info about containers in Docker:

* [How to automate Docker container deployment](https://www.freecodecamp.org/news/automate-docker-container-deployment-via-maven-53a855e26d3e/)
* [How to fix Docker container vulnerabilities](https://www.freecodecamp.org/news/how-to-find-and-fix-docker-container-vulnerabilities-in-2020/)

## More info about Docker:

* [A beginner's guide to Docker](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/)
* [Docker DevOps course (free video course)](https://www.freecodecamp.org/news/docker-devops-course/)
* [Docker 101: from creation to deployment](https://www.freecodecamp.org/news/docker-101-creation-to-deployment/)


