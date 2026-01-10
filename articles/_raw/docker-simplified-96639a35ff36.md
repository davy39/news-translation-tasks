---
title: 'Docker Simplified: A Hands-On Guide for Absolute Beginners'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T16:07:03.000Z'
originalURL: https://freecodecamp.org/news/docker-simplified-96639a35ff36
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8TdTKJ6wtOoX7hZEbNFK-A.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Shahzan

  Whether you are planning to start your career in DevOps, or you are already into
  it, if you do not have Docker listed on your resume, it’s undoubtedly time for you
  to think about it, as Docker is one of the critical skill for anyone who is...'
---

By Shahzan

Whether you are planning to start your career in DevOps, or you are already into it, if you do not have Docker listed on your resume, it’s undoubtedly time for you to think about it, as Docker is one of the critical skill for anyone who is into DevOps arena.

In this post, I will try my best to explain Docker in the simplest way I can.

Before we take a deep dive and start exploring Docker, let’s take a look at what topics we will be covering as part of this beginner’s guide.

* [What is Docker?](https://medium.com/p/96639a35ff36#06d9)
* [The problem Docker solves](https://medium.com/p/96639a35ff36#ba08)
* [Advantages and disadvantages of using Docker](https://medium.com/p/96639a35ff36#dcc3)
* [Core components of Docker](https://medium.com/p/96639a35ff36#5539)
* [Docker Terminology](https://medium.com/p/96639a35ff36#b7d7)
* [What is Docker Hub?](https://medium.com/p/96639a35ff36#a053)
* [Docker Editions](https://medium.com/p/96639a35ff36#965a)
* [Installing Docker](https://medium.com/p/96639a35ff36#d3ff)
* [Some essential Docker commands to get you started](https://medium.com/p/96639a35ff36#d56c)
* [Wrap-Up](https://medium.com/p/96639a35ff36#0ba9)

### Let’s begin by understanding, What is Docker?

In simple terms, Docker is a software platform that simplifies the process of building, running, managing and distributing applications. It does this by virtualizing the operating system of the computer on which it is installed and running.

The first edition of Docker was released in 2013.

Docker is developed using the GO programming language.

![Image](https://cdn-media-1.freecodecamp.org/images/1*waybfdGDf7yb8ZpDfIgEsA.png)

> Looking at the rich set of functionality Docker has got to offer, it’s been widely accepted by some of the world’s leading organizations and universities, such as **Visa, PayPal, Cornell University and Indiana University** (just to name a few) to run and manage their applications using Docker.

### Now let’s try to understand the problem, and the solution Docker has got to offer

#### The Problem

Let’s say you have three different Python-based applications that you plan to host on a single server (which could either be a physical or a virtual machine).

Each of these applications makes use of a different version of Python, as well as the associated libraries and dependencies, differ from one application to another.

Since we cannot have different versions of Python installed on the same machine, this prevents us from hosting all three applications on the same computer.

#### The Solution

Let’s look at how we could solve this problem without making use of Docker. In such a scenario, we could solve this problem either by having three physical machines, or a single physical machine, which is powerful enough to host and run three virtual machines on it.

Both the options would allow us to install different versions of Python on each of these machines, along with their associated dependencies.

Irrespective of which solution we choose, the costs associated with procuring and maintaining the hardware are quite expensive.

Now, let’s check out how Docker could be an efficient and cost-effective solution to this problem.

To understand this, we need to take a look at how exactly Docker functions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MbxLUFB2HRPmLAn60tQKZA.png)

The machine on which Docker is installed and running is usually referred to as a Docker Host or Host in simple terms.

So, whenever you plan to deploy an application on the host, it would create a logical entity on it to host that application. In Docker terminology, we call this logical entity a Container or Docker Container to be more precise.

A Docker Container doesn’t have any operating system installed and running on it. But it would have a virtual copy of the process table, network interface(s), and the file system mount point(s). These have been inherited from the operating system of the host on which the container is hosted and running.

Whereas the kernel of the host’s operating system is shared across all the containers that are running on it.

This allows each container to be isolated from the other present on the same host. Thus it supports multiple containers with different application requirements and dependencies to run on the same host, as long as they have the same operating system requirements.

To understand how Docker has been beneficial in solving this problem, you need to refer to the next section, which discusses the advantages and disadvantages of using Docker.

In short, Docker would virtualize the operating system of the host on which it is installed and running, rather than virtualizing the hardware components.

### The Advantages and Disadvantages of using Docker

#### Advantages of using Docker

Some of the key benefits of using Docker are listed below:

* Docker supports multiple applications with different application requirements and dependencies, to be hosted together on the same host, as long as they have the same operating system requirements.
* Storage Optimized. A large number of applications can be hosted on the same host, as containers are usually few megabytes in size and consume very little disk space.
* Robustness. A container does not have an operating system installed on it. Thus, it consumes very little memory in comparison to a virtual machine (which would have a complete operating system installed and running on it). This also reduces the bootup time to just a few seconds, as compared to a couple of minutes required to boot up a virtual machine.
* Reduces costs. Docker is less demanding when it comes to the hardware required to run it.

#### Disadvantages of using Docker

* Applications with different operating system requirements cannot be hosted together on the same Docker Host. For example, let’s say we have 4 different applications, out of which 3 applications require a Linux-based operating system and the other application requires a Windows-based operating system. In such a scenario, the 3 applications that require Linux-based operating system can be hosted on a single Docker Host, whereas the application that requires a Windows-based operating system needs to be hosted on a different Docker Host.

### Core Components of Docker

**Docker Engine** is one of the core components of Docker. It is responsible for the overall functioning of the Docker platform.

**Docker Engine** is a client-server based application and consists of 3 main components.

1. Server
2. REST API
3. Client

![Image](https://cdn-media-1.freecodecamp.org/images/1*MYX0ClbWoitxS0RNUVvj8A.png)
_Image Source: [https://docs.docker.com](https://docs.docker.com/v17.12/engine/docker-overview/" rel="noopener" target="_blank" title=")_

The **Server** runs a daemon known as **dockerd** **(Docker Daemon)**, which is nothing but a process. It is responsible for creating and managing Docker Images, Containers, Networks and Volumes on the Docker platform.

The **REST API** specifies how the applications can interact with the Server, and instruct it to get their job done.

The **Client** is nothing but a command line interface, that allows users to interact with **Docker** using the commands.

### Docker Terminology

Let us take a quick look at some of the terminology associated with Docker.

**Docker Images** and **Docker Containers** are the two essential things that you will come across daily while working with **Docker**.

In simple terms, a **Docker Image** is a template that contains the application, and all the dependencies required to run that application on Docker.

On the other hand, as stated earlier, a **Docker Container** is a logical entity. In more precise terms, it is a running instance of the Docker Image.

#### What is Docker Hub?

**Docker Hub** is the official online repository where you could find all the Docker Images that are available for us to use.

**Docker Hub** also allows us to store and distribute our custom images as well if we wish to do so. We could also make them either public or private, based on our requirements.

Please Note: Free users are only allowed to keep one Docker Image as private. If we wish to keep more than one Docker Image as private, we need to subscribe to a paid subscription plan.

### Docker Editions

Docker is available in 2 different editions, as listed below:

* **Community Edition (CE)**
* **Enterprise Edition (EE)**

The **Community Edition** is suitable for individual developers and small teams. It offers limited functionality, in comparison to the Enterprise Edition.

The **Enterprise Edition,** on the other hand, is suitable for large teams and for using Docker in production environments.

The Enterprise Edition is further categorized into three different editions, as listed below:

* **Basic Edition**
* **Standard Edition**
* **Advanced Edition**

### Installing Docker

One last thing that we need to know before we go ahead and get our hands dirty with Docker is actually to have Docker installed.

Below are the links to the official Docker CE installation guides. You can follow these guides to install Docker on your machine, as they are simple and straightforward.

* [CentOS Linux](https://docs.docker.com/install/linux/docker-ce/centos/)
* [Debian Linux](https://docs.docker.com/install/linux/docker-ce/debian/)
* [Fedora Linux](https://docs.docker.com/install/linux/docker-ce/fedora/)
* [Ubuntu Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Microsoft Windows](https://docs.docker.com/docker-for-windows/install/)
* [MacOS](https://docs.docker.com/docker-for-mac/install/)

#### Want to skip installation and head off straight to practicing Docker?

Just in case you are feeling too lazy to install Docker, or you don’t have enough resources available on your computer, you need not have to worry — here’s the solution to your problem.

You can head over to [Play with Docker](https://labs.play-with-docker.com/), which is an online playground for Docker. It allows users to practice Docker commands immediately, without having to install anything on your machine. The best part is it’s simple to use and available free of cost.

### Docker Commands

Now it’s time to get our hands dirty with Docker commands, for which we all have been waiting till now.

#### docker create

The first command which we will be looking at is the **docker create** command.

This command allows us to create a new container.

The syntax for this command is as shown below:

```
docker create [options] IMAGE [commands] [arguments]
```

Please Note: Anything enclosed within the square brackets is optional. This is applicable to all the commands that you would see on this guide.

Some of the examples of using this command are shown below:

```
$ docker create fedora
```

```
02576e880a2ccbb4ce5c51032ea3b3bb8316e5b626861fc87d28627c810af03
```

In the above example, the docker create command would create a new container using the latest Fedora image.

Before creating the container, it will check if the latest official image of the Fedora is available on the Docker Host or not. If the latest image isn’t available on the Docker Host, it will then go ahead and download the Fedora image from the Docker Hub before creating the container. If the Fedora image is already present on the Docker Host, it will make use of that image and create the container.

If the container was created successfully, Docker will return the container ID. For instance, in the above example 02576e880a2ccbb4ce5c51032ea3b3bb8316e5b626861fc87d28627c810af03 is the container ID returned by Docker.

Each container has a unique container ID. We refer to the container using its container ID for performing various operations on the container, such as starting, stopping, restarting, and so on.

Now, let us refer to another example of docker create command, which has options and commands being passed to it.

```
$ docker create -t -i ubuntu bash
```

```
30986b73dc0022dbba81648d9e35e6e866b4356f026e75660460c3474f1ca005
```

In the above example, the docker create command creates a container using the Ubuntu image (As stated earlier, if the image isn’t available on the Docker Host, it will go ahead and download the latest image from the Docker Hub before creating the container).

The options -t and -i instruct Docker to allocate a terminal to the container so that the user can interact with the container. It also instructs Docker to execute the bash command whenever the container is started.

#### docker ps

The next command we will look at is the **docker ps** command.

The **docker ps** command allows us to view all the containers that are running on the Docker Host.

```
$ docker ps
```

```
CONTAINER ID IMAGE  COMMAND CREATED        STATUS            PORTS NAMES30986b73dc00 ubuntu "bash"  45 minutes ago Up About a minute                 elated_franklin
```

It only displays the containers that are presently running on the Docker Host.

If you want to view all the containers that were created on this Docker Host, irrespective of their current status, such as whether they are running or exited, then you would need to include the option -a, which in turn would display all the containers that were created on this Docker Host.

```
$ docker ps -a
```

```
CONTAINER ID IMAGE  COMMAND     CREATED           STATUS       PORTS NAMES30986b73dc00 ubuntu “bash”      About an hour ago Up 29 minutes elated_franklin02576e880a2c fedora “/bin/bash” About an hour ago Created hungry_sinoussi
```

Before we proceed further, let’s try to decode and understand the output of the **docker ps** command.

**CONTAINER ID:** A unique string consisting of alpha-numeric characters, associated with each container.

**IMAGE:** Name of the Docker Image used to create this container.

**COMMAND:** Any application specific command(s) that needs to be executed when the container is started.

**CREATED:** This shows the time elapsed since this container has been created.

**STATUS:** This shows the current status of the container, along with the time elapsed, in its present state.

If the container is running, it will display as Up along with the time period elapsed (for example, Up About an hour or Up 3 minutes).

If the container is stopped, then it will display as Exited followed by the exit status code within round brackets, along with the time period elapsed (for example, Exited (0) 3 weeks ago or Exited (137) 15 seconds ago, where 0 and 137 are the exit codes).

**PORTS:** This displays any port mappings defined for the container.

**NAMES:** Apart from the CONTAINER ID, each container is also assigned a unique name. We can refer to a container either using its container ID or its unique name. Docker automatically assigns a unique silly name to each container it creates. But if you want to specify your own name to the container, you can do that by including the `— — name` (double hyphen name) option to the docker create or the docker run (we will look at the docker run command later) command.

I hope this gives you a better understanding of the output of the docker ps command.

#### docker start

The next command we will look at, is the **docker start** command.

This command starts any stopped container(s).

The syntax for this command is as shown below:

```
docker start [options] CONTAINER ID/NAME [CONTAINER ID/NAME…]
```

We can start a container either by specifying the first few unique characters of its container ID or by specifying its name.

Some of the examples of using this command are shown below:

```
$ docker start 30986
```

In the above example, Docker starts the container beginning with the container ID 30986.

```
$ docker start elated_franklin
```

Whereas in this example, Docker starts the container named elated_franklin.

#### docker stop

The next command on the list is the **docker stop** command.

This command stops any running container(s).

The syntax for this command is as shown below:

```
docker stop [options] CONTAINER ID/NAME [CONTAINER ID/NAME…]
```

It is similar to the docker start command.

We can stop the container either by specifying the first few unique characters of its container ID or by specifying its name.

Some of the examples of using this command are shown below:

```
$ docker stop 30986
```

In the above example, Docker will stop the container beginning with the container ID 30986.

```
$ docker stop elated_franklin
```

Whereas in this example, Docker will stop the container named elated_franklin.

#### docker restart

The next command we will look at is the **docker restart** command.

This command restarts any running container(s).

The syntax for this command is as shown below:

```
docker restart [options] CONTAINER ID/NAME [CONTAINER ID/NAME…]
```

We can restart the container either by specifying the first few unique characters of its container ID or by specifying its name.

Some of the examples of using this command are shown below:

```
$ docker restart 30986
```

In the above example, Docker will restart the container beginning with the container ID 30986.

```
$ docker restart elated_franklin
```

Whereas in this example, Docker will restart the container named elated_franklin.

#### docker run

The next command we will be looking at is the **docker run** command.

This command first creates the container, and then it starts the container. In short, this command is a combination of the docker create and the docker start command.

The syntax for this command is as shown below:

```
docker run [options] IMAGE [commands] [arguments]
```

It has a syntax similar to that of the docker create command.

Some of the examples of using this command are shown below:

```
$ docker run ubuntu
```

```
30fa018c72682d78cf168626b5e6138bb3b3ae23015c5ec4bbcc2a088e67520
```

In the above example, Docker will create the container using the latest Ubuntu image and then immediately start the container.

If we execute the above command, it would start the container and immediately stop it — we wouldn’t get any chance to interact with the container at all.

If we want to interact with the container, then we need to specify the options: -it (hyphen followed by i and t) to the docker run command presents us with the terminal, using which we could interact with the container by typing in appropriate commands. Below is an example of the same.

```
$ docker run -it ubuntu
```

```
root@e4e633428474:/#
```

In order to come out of the container, you need to type exit in the terminal.

#### docker rm

Moving on to the next command — if we want to delete a container, we use the **docker rm** command.

The syntax for this command is as shown below:

```
docker rm [options] CONTAINER ID/NAME [CONTAINER ID/NAME...]
```

Some of the examples of using this command are shown below:

```
$ docker rm 30fa elated_franklin
```

In the above example, we are instructing Docker to delete 2 containers within a single command. The first container to be deleted is specified using its container ID, and the second container to be deleted is specified using its name.

Please Note: The containers need to be in a stopped state in order to be deleted.

#### docker images

**docker images** is the next command on the list.

This command lists out all the Docker Images that are present on your Docker Host.

```
$ docker images
```

```
REPOSITORY  TAG      IMAGE          CREATED        SIZEmysql       latest   7bb2586065cd   38 hours ago   477MBhttpd       latest   5eace252f2f2   38 hours ago   132MBubuntu      16.04    9361ce633ff1   2 weeks ago    118MBubuntu      trusty   390582d83ead   2 weeks ago    188MBfedora      latest   d09302f77cfc   2 weeks ago    275MBubuntu      latest   94e814e2efa8   2 weeks ago    88.9MB
```

Let us decode the output of the **docker images** command.

**REPOSITORY:** This represents the unique name of the Docker Image.

**TAG:** Each image is associated with a unique tag. A tag basically represents a version of the image.

A tag is usually represented either using a word or set of numbers or a combination of alphanumeric characters.

**IMAGE ID:** A unique string consisting of alpha-numeric characters, associated with each image.

**CREATED:** This shows the time elapsed since this image has been created.

**SIZE:** This shows the size of the image.

#### docker rmi

The next command on the list is the **docker rmi** command.

The **docker rmi** command allows us to remove an image(s) from the Docker Host.

The syntax for this command is as shown below:

```
docker rmi [options] IMAGE NAME/ID [IMAGE NAME/ID...]
```

Some of the examples of using this command are shown below:

```
docker rmi mysql
```

The above command removes the image named mysql from the Docker Host.

```
docker rmi httpd fedora
```

The above command removes the images named httpd and fedora from the Docker Host.

```
docker rmi 94e81
```

The above command removes the image starting with the image ID 94e81 from the Docker Host.

```
docker rmi ubuntu:trusty
```

The above command removes the image named ubuntu, with the tag trusty from the Docker Host.

These were some of the basic Docker commands you will see. There are many more Docker commands to explore.

### Wrap-Up

Containerization has recently gotten the attention it deserves, although it has been around for a long time. Some of the top tech companies like Google, Amazon Web Services (AWS), Intel, Tesla, and Juniper Networks have their own custom version of container engines. They heavily rely on them to build, run, manage, and distribute their applications.

> **Docker** is an extremely powerful containerization engine, and it has a lot to offer when it comes to building, running, managing and distributing your applications efficiently.

You have just seen Docker at a very high level. There is a lot more to learn about Docker, such as:

* Docker commands (More powerful commands)
* Docker Images (Build your own custom images)
* Docker Networking (Setup and configure networking)
* Docker Services (Grouping containers that use the same image)
* Docker Stack (Grouping services required by an application)
* Docker Compose (Tool for managing and running multiple containers)
* Docker Swarm (Grouping and managing one or more machines on which docker is running)
* And much more…

If you have found Docker to be fascinating, and are interested in learning more about it, then I would recommend that you enroll in the courses which are listed below. I found them to be very informative and straight to the point.

If you are an absolute beginner, then I would suggest you [enroll in this course](http://bit.ly/2YLH23G), which has been designed for beginners.

If you have some good knowledge about Docker, and are pretty much confident with the basic stuff and want to expand your knowledge, then I would suggest you should [enroll into this course](http://bit.ly/2UaTGe8), which is aimed more towards advanced topics related to Docker.

**Docker** is a future-proofed skill and is just picking up momentum.

Investing your time and money into learning Docker wouldn’t be something that you would repent.

> Hope you found this post to be informative. feel free to share it across. This really means a lot to me.

### Before you say goodbye…

Let’s stay in touch, [click here to enter your email address](https://forms.gle/3U1uBNEC4mDkSpMJ7) (Use this link if the above widget doesn’t show up on your screen).

Thank you so much for taking your precious time to read this post.

Disclaimer: All product and company names are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any endorsement by them. There may be affiliate links within this post.

