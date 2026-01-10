---
title: 'Docker Image Guide: How to Delete Docker Images, Stop Containers, and Remove
  all Volumes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T01:00:00.000Z'
originalURL: https://freecodecamp.org/news/docker-image-guide-how-to-remove-and-delete-docker-images-stop-containers-and-remove-all-volumes
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/docker-container-volumes-images.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: containerization
  slug: containerization
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: 'By Sebastian Sigl

  Docker has been widely adopted and is a great vehicle to deploy an application to
  the cloud (or some other Docker-ready infrastructure). It is also useful for local
  development. You can start complex applications quickly, develop in...'
---

By Sebastian Sigl

Docker has been widely adopted and is a great vehicle to deploy an application to the cloud (or some other Docker-ready infrastructure). It is also useful for local development. You can start complex applications quickly, develop in isolation, and still have a very good performance.

Here are the most important commands to use Docker in your daily business efficiently.

## List All Docker Images

```shell
docker images

```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-52.png)

In my case, I have 3 images installed:

* MySQL, version 8.0.19, one tagged as latest version
* and Cassandra with the latest version.

To get more information about an image, you can inspect it:

```shell
docker inspect mysql:latest
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-51.png)

This will return a list of information. Alternatively, you can also use the image ID to get the information:

```shell
docker inspect 3a5e53f63281
```

The output can be overwhelming. Therefore, there is a handy option to filter certain information:

```shell
docker inspect --format='{{.RepoTags}}  {{.Config.Image}}' 3a5e53f63281
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-50.png)

## Remove Docker Images

A single image can be removed by:

```shell
docker rm mysql:latest
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-48.png)

In my case, the image is still tagged with _mysql:8.0.19_. Therefore, to remove it completely, I need to also remove another version tag:

```shell
docker rm mysql:8.0.19
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-45.png)

To remove the image directly, it is easier to delete the image by image id:

```shell
docker image rm 3a5e53f63281 -f
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-46.png)

The option **-f** forces the execution, because otherwise you would get an error if the image is referenced by more than 1 tag.

## Start a Docker Image

An image can be started in the foreground by:

```shell
docker run cassandra
```

If the image does not exist, then it will be downloaded. You can stop the execution by pressing **CTRL+C**. You can also run it in the background by adding the **-d** option:

```shell
docker run -d mysql
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-54.png)

If the container is started in the background, then you receive the container ID.

By default, the container runs in isolation. Therefore, you won't be able do any communication with it, and no files are stored in your current directory.

## Forward ports of a container

You can forward ports by using the **-p** option to, for example, a page that is exposed from your container:

```shelll
docker run -p 8080:80 nginx
```

This NGINX container exposes a webserver on port 80. By using the -p 8080:80, the local port 8080 is forwarded to the container port 80.

## Log into a container

Sometimes it is helpful to log into a container. This is only possible if the container has a shell installed. You will get an error if this is not the case.

First, start the container detached and give it a name:

```shell
docker run -d --name my_container nginx
```

This will return a container ID. Now you can execute a shell in the container and attach your input and output to it by using the options **-i** and **-t**:

```shell
docker exec -it my_container bash
```

Instead of the container name, you can also use the returned container ID for all following operations. Sometimes, bash is not available. Therefore, you can also try to launch a basic shell:

```shell
docker exec -it my_container sh
```

## List running containers

After you’ve started a container, you can see all running containers executing:

```shell
docker ps
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-56.png)

By appending **-a**, exited containers will also be listed:

```shell
docker ps -a
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-57.png)

## Share a local folder with a container

Sometimes it is useful to sync files between the container and the local filesystem. You can do it by running a container and using the **-v** option. On Linux and macOS, you can share a local temporary folder with a container by:

```shell
docker run --name=my_container -d -v $(pwd)/tmp:/var/log/nginx -p 8080:80 nginx
```

On windows you can run:

```shell
docker run --name=my_container -d -v %cd%/tmp:/var/log/nginx -p 8080:80 nginx
```

## Stop running containers

It is possible to stop a running container by:

```shell
docker stop my_container
```

Stopping a container stops all processes but keeps changes within the filesystem.

## Start a stopped container

A stopped container can be started by:

```shell
docker start my_container
```

## Remove a container

To remove a stopped container, you can execute:

```shell
docker rm my_container
```

To stop and remove the container in one command, you can add the force option **-f**.

```shell
docker rm -f my_container
```

## Create a volume and share it with multiple containers

An independent volume named **SharedData** can be created by:

```shell
docker volume create --name SharedData

docker run --name=my_container -d -v SharedData:/var/log/nginx -p 8080:80 nginx

docker run --name=my_container_2 -d -v SharedData:/var/log/nginx -p 8080:80 nginx
```

Both containers will have a shared folder, and files will be synced between both containers.

## Remove a volume

To remove a volume, all containers that use the volume need to be removed.

```shell
docker rm -f my_container
docker rm -f my_container_2
docker volume rm SharedData
```

## Remove stopped containers and unused images

A safe tidy-up command is:

```shell
docker system prune -a
```

## Remove all unused volumes

All unmounted volumes can be removed by:

```shell
docker volume prune
```

## Conclusion 

Creating containers, logging into containers, forwarding ports, and sharing volumes are the most important commands of your Docker command line interface. They build the foundation of systems like Kubernetes and enable us to create and run applications in isolation.

I hope you enjoyed the article. If you like it and feel the need for a round of applause, [follow me on Twitter](https://twitter.com/sesigl).

I am a co-founder of our revolutionary journey platform called [Explore The World](https://www.urlaubsbaron.de). We are a young startup located in Dresden, Germany and will target the German market first. Reach out to me if you have feedback and questions about any topic.

Happy Docker exploring :)

References

* Docker command line documentation  
[https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)

