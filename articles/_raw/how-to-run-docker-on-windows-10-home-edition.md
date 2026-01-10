---
title: How to run Docker on Windows 10 Home edition
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-22T09:38:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-docker-on-windows-10-home-edition
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/head-image-1.jpg
tags:
- name: ArchLinux
  slug: archlinux
- name: Docker
  slug: docker
- name: 'VirtualBox '
  slug: virtualbox
- name: vm
  slug: vm
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "By Mihail Gaberov\nRecently I have been watching a tutorial where, in order\
  \ to follow it, you need to have Docker running on your machine. So far, so good.\
  \ \nBut it turns out that the latest versions of Docker require Windows 10 Pro,\
  \ Enterprise, or Edu..."
---

By Mihail Gaberov

Recently I have been watching a tutorial where, in order to follow it, you need to have [Docker](https://docs.docker.com/docker-for-windows/install/) running on your machine. So far, so good. 

But it turns out that the latest versions of Docker require Windows 10 Pro, Enterprise, or Education. Which means that if you are like me and have just Windows 10 Home edition on your personal laptop, then you cannot use Docker…**or maybe you still can**. 

Read on below to find out how. ?

## Reasoning

First, let's do a short summary of the situation. What do we want to achieve and what do we currently have?

We have Windows 10 OS Home edition on our machine. We would like to have Docker running on the same machine so that we are able to create docker images, run containers, and learn better and grow faster! 

The last one is a bit out of the scope of this article, but we should start from somewhere, no? ?.

## Actions

After defining what we want, let's see how to achieve it. Here are the steps I followed. It worked for me, which make me want to share it with you. And maybe I can save someone a few days of going back and forth to StackOverflow! ?

After some reading, I found this [article](http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows). It explains that it is possible to use Docker in Windows 10 Home by leveraging a Linux virtual machine and having Docker containers running on it. Let's see how it works.

### Step 1: Installations

First you need to install a software called [Oracle VM VirtualBox](https://www.virtualbox.org/). It gives you the ability to have multiple virtual machines installed on your physical one. This way we can have a virtual machine which will be running Linux where our Docker will live.

Then use Windows PowerShall and [Chocolatey](https://chocolatey.org/), your Windows package manager, to install a _docker-machine_ by running the following:

```bash
choco install docker-machine
```

Open your favorite bash terminal app and run this:

```bash
docker-machine create --driver virtualbox default
```

This will create a docker virtual machine called 'default'.

### Step 2: Configurations

Next, we need to configure which ports are exposed when running Docker containers. You can do that by going to Oracle VM VirtualBox -> default virtual machine -> Settings -> Network -> Adapter 1 -> Port Forwarding.

![VirtualBox Port Forwarding](https://mihail-gaberov.eu/static/fb9bdc0bd6814d55c65b8ea7c761c8bd/fcda8/port-forwarding.png)

This was the **most critical** **detail** that I forgot . We need to allow Docker to mount volumes located on your hard drive. By default, you can only mount from the `C://Users/` directory. 

To add a different path, simply go to the **Oracle VM VirtualBox** GUI. Select **default** VM and go to _Settings > Shared Folders_. If you don't mind to use the default settings, do not forget to put your project under the 'Users' directory, e.g. `C:\Users\{your project}`. 

In my case, I forgot about this and had to spend few days of head banging until I figured out why the heck was I getting a "Couldn't find package.json" error when trying to run the [containers](https://github.com/mihailgaberov/microservices), built through this [tutorial](https://www.youtube.com/watch?v=6Yfm5gHQjaQ&list=PLnTRniWXnjf8YC9qJFLSVCrXfS6cyj6x6&index=2).

Start the virtual machine by running the following command in your terminal app:

```bash
docker-machine start default
```

### Step 3: Setting up Environment Variables

Next, we need to set up Docker environment variables:

```bash
docker-machine env default
```

This allows the Docker client and Docker Compose to communicate with the Docker Engine running in the Linux VM that we named "default".

You may also need to run:

```bash
@FOR /f "tokens=*" %i IN ('"C:\ProgramData\chocolatey\lib\docker-machine\bin\docker-machine.exe" env') DO @%i
```

in order to get Docker working properly. _Note: the specified path in the above command may vary depending on your setup_.

If you are going to use things such as `docker-compose up`, you will need to install Docker Tools as well. You may do it by running the following commands in PowerShall:

```bash
choco install docker-cli
choco install docker-compose
```

These will install everything you need to start using Docker on your Windows 10 Home OS.

## **Conclusion**

Now that we have all we need, we may spend our time on actual learning, either by following a docker-related tutorial or reading a book. No matter what you want to do next, you have all the tools you will need. 

I personally will try to [finish](https://github.com/mihailgaberov/microservices) the previously mentioned tutorial and then, who knows, may be I will start using Docker for each project I do.

By the way, during the process of researching, I found a very promising book which is specifically about Docker. It's called _"Docker in Practice" by Ian Miell_. If this interests you, you might want to take a look.

? Thanks for reading! ?

### **References**

* [https://www.virtualbox.org/](https://www.virtualbox.org/)
* [https://www.sitepoint.com/docker-windows-10-home](https://www.sitepoint.com/docker-windows-10-home)
* [https://www.youtube.com/watch?v=6Yfm5gHQjaQ&list=PLnTRniWXnjf8YC9qJFLSVCrXfS6cyj6x6&index=2](https://www.youtube.com/watch?v=6Yfm5gHQjaQ&list=PLnTRniWXnjf8YC9qJFLSVCrXfS6cyj6x6&index=2)
* [https://github.com/mihailgaberov/microservices](https://github.com/mihailgaberov/microservices)
* [http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows](http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows)

