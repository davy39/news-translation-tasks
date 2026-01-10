---
title: 7 Cases When You Should Not Use Docker
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2019-11-19T16:23:17.000Z'
originalURL: https://freecodecamp.org/news/7-cases-when-not-to-use-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Docker-1.png
tags:
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
seo_title: null
seo_desc: 'Docker is a game-changer. But it is not a one-size-fits-all solution.

  There are many good things about Docker. It packs, ships, and runs applications
  as a lightweight, portable, and self-sufficient containerization tool. Docker is
  great for businesse...'
---

## Docker is a game-changer. But it is not a one-size-fits-all solution.

There are many good things about Docker. It packs, ships, and runs applications as a lightweight, portable, and self-sufficient containerization tool. Docker is great for businesses of all sizes. When you are working on a piece of code in a small team, it eliminates the “but it works on my machine” problem. Meanwhile, enterprises can use Docker to build Agile software delivery pipelines to ship new features faster and more securely.

With its built-in containerization system, Docker is an excellent tool for cloud computing. In turn, Docker Swarm advances clusterization and decentralized design. Sounds too good to be true, right? Well, there are still several cases when not to use Docker. Here are seven of them.

![do not use docker](https://images.ctfassets.net/6xhdtf1foerq/2JJ68pTAT6ZhVo05jVwbWI/d79861dd9b194ee83a313ce18f8b624e/Infographics__3_-min.png?fm=png&q=85&w=1000)

Let's go through these one by one.

## **Do Not Use Docker if You Need to Boost Speed**

Docker containers are smaller and require fewer resources than a virtual machine with a server and a database. At the same time, Docker will use as much system resources as the host’s kernel scheduler will allow. You should not expect Docker to speed up an application in any way.

What is more, Docker might even make it slower. If you are working with it, you should set limits on how much memory, CPU, or block IO the container can use. Otherwise, if the kernel detects that the host machine’s memory is running too low to perform important system functions, it could start killing important processes. If the wrong process is killed (including the Docker itself), the system will be unstable.

Unfortunately, Docker’s memory adjustments – the out-of-memory priority on the Docker daemon – do not solve this issue. By contrast, an additional layer between an application and the operating system could also result in speed reduction. Yet, this decrease will be insignificant. Docker containers are not fully isolated and do not contain a complete operating system like any virtual machine.

## **Do Not Use Docker if You Prioritize Security**

The greatest Docker security advantage is that it breaks the app into smaller parts. If the security of one part is compromised, the rest of them will not be affected.

However, while isolated processes in containers promise improved security, all containers share access to a single host operating system. You risk running Docker containers with incomplete isolation. Any malicious code can get access to your computer memory.

There is a popular practice to run a lot of containers in a single environment. This is how you make your app predisposed to the Resource Abuse type of attacks unless you limit the resource container capabilities. For maximum efficiency and isolation, each container should address one specific area of concern.

Another issue is Docker’s default configuration – users are not namespaced. Namespaces let software resources use other resources only if they belong to a specific namespace.

Running applications with Docker implies running the Docker daemon with root privileges. Any processes that break out of Docker container will have the same privileges on the host as it did in the container. Running your processes inside the containers as a non-privileged user cannot guarantee security. It depends on the capabilities you add or remove. To mitigate the risks of Docker container breakout, you should not download ready-to-use containers from untrusted sources.

## **Do Not Use Docker if You Develop a Desktop GUI Application**

Docker does not suit applications that require rich UI. Docker is mainly intended for isolated containers with console-based applications. GUI-based applications are not a priority, their support will rely on the specific case and application. Windows containers are based on either Nano or Core Server – it does not allow users to start up a GUI-based interface or a Docker RDP server in the Docker container.

Yet, you can still [<ins>run GUI-based applications</ins>](https://hub.docker.com/r/tzutalin/py2qt4/) developed with Python and the QT framework in a Linux container. Also, you can use X11 forwarding, but this solution is somewhat awkward.

## **Do Not Use Docker if You Want to Light Up Development and Debugging**

Docker was created by developers and for developers. It provides environment stability: a container on the development machine will work exactly the same on staging, production, or any other environment. This eliminates the problem of various program versioning in different environments.

With Docker’s help, you can easily add a new dependency to your application. No developer on your team will need to repeat this manipulation on their machine. Everything will be up and running in the container and distributed to the entire team.

At the same time, you have to do some extra setup to code your app in Docker. Moreover, with Docker debugging, you have to configure logs output and set up debugging ports. You may also need to map ports for your applications and services in containers. So, if you have a complicated and tedious deployment process, Docker will help you out a lot. If you have a simple app, it just adds unnecessary complexity.

## **Do Not Use Docker if You Need to Use Different Operating Systems or Kernels**

With virtual machines, the hypervisor can abstract an entire device. You can use Microsoft Azure to run both instances of Windows Server and Linux Server at the same time. Docker image, however, requires the same operating system it was created for.

There is a large database of Docker container images –  Docker Hub. Yet, if an image was created on Linux Ubuntu, it will run only on the exact same Ubuntu.

If an app is developed on Windows, but the production runs on Linux, you will not be able to use Docker effectively. Sometimes, it is easier to set up a server if you have several static apps.

## **Do Not Use Docker if You Have a Lot of Valuable Data to Store**

By design, all Docker files are created inside a container and stored on a writable container layer. It may be difficult to retrieve the data out of the container if a different process needs it. Also, the writable layer of a container is connected to the host machine which the container is running on. If you need to move the data elsewhere, you cannot do it easily. More than that, all the data stored inside a container will be lost forever once the container shuts down.

You have to think of ways to save your data somewhere else first. To keep data safe in Docker, you need to employ an additional tool – Docker Data Volumes. Yet, this solution is still quite clumsy and needs to be improved.

## **Do Not Use Docker if You Are Looking for The Easiest Technology to Manage**

Being introduced in 2012, Docker is still a new technology. As a developer, you might have to update Docker versions regularly. Unfortunately, backward compatibility is not guaranteed. Moreover, the documentation is falling behind the advancement of the technology. As a developer, you will have to figure some things out yourself.

In addition, the monitoring options that Docker offers are quite poor. You can get a quick insight into some simple statistics. Yet, if you want to see some advanced monitoring features, Docker has nothing to offer.

Also, in the case of a large and complex application, the implementation of Docker comes at a cost. Building and maintaining communication between numerous containers on numerous servers will take a lot of time and effort. Yet, there is a helpful tool, which makes it easier to work with multi-container Docker apps, – Docker Compose. Docker Compose defines services, networks, and volumes in a single YAML file.

Nonetheless, the Docker ecosystem is quite fractured – not all the supporting container products work well with one another. Each product is backed by a certain company or community. The heated competition between those results in product incompatibility.

## **To Wrap Up**

KeenEthics professionals enjoy working with Docker and often use it for app development. Despite some drawbacks, you can easily use it to run and manage apps side by side in isolated containers. 

Installing an app can be as simple as running a single command – <docker run>. Docker also provides a clean and original isolation environment for each test, making it an important and useful tool for automation testing. 

Docker features offer benefits in terms of dependency management and security. Augmented with such useful tools as Docker Hub, Docker Swarm, and Docker Compose, Docker is a popular and user-friendly solution.

Despite all the benefits of Docker, you should not use it to containerize each and every application you develop.

_Remember: Docker is a game-changer. But it is not a one-size-fits-all solution._

Docker is not the only such a tool in the market either. The alternatives of Docker are [<ins>rkt</ins>](https://coreos.com/rkt/), pronounced as ‘rocket’, [<ins>Linux Containers</ins>](https://linuxcontainers.org/), or [<ins>OpenVZ</ins>](https://openvz.org/). Each of these with its advantages and disadvantages is quite similar to Docker. The growing popularity and use rates of Docker are caused only by the decision of businesses to adopt it.

Before jumping to conclusions as for should you use Docker or not, research the project requirements. Talk to your teammates or peers and let them help you decide when to use Docker, when not to use containers, and whether it is one of those Docker use cases.

Whether you like it or not, this technology has a future. There are some developers and development agencies that hate Docker and try to eliminate it from all their ongoing projects. At the same time, there are specialists who containerize everything they can because they see Docker as a panacea. Perhaps, you should not join either camp. Stay impartial, stay objective, and make a decision depending on a particular situation.

## Do you have an idea for a Docker project?

My company KeenEthics is a team of experienced [web application developers](https://keenethics.com/services-web-development). In case you need a free estimate of a similar project, feel free to [get in touch](https://keenethics.com/contacts?activeForm=estimate)_._

You can read more of similar articles on my Keen Blog. Allow me to suggest you read [Why to Refactor Your Code?](https://keenethics.com/blog/1554572000000-refactoring) or [Software Development Models Explained:  Outsourcing vs Outstaffing,  Fixed Price vs Time & Material?](https://keenethics.com/blog/outsourcing-vs-outstaffing)

## P.S.

Also, I would like to say "thank you" to [Alex Pletnov](https://www.linkedin.com/in/oleksiy-pletnov-212b3764/) for coauthoring this article as well as the readers for making it to the end!

The original article posted on KeenEthics blog can be found here: [7 Cases When Not to Use Docker](https://keenethics.com/blog/1517306255770-docker-5-cases-when-you-should-not-use-it).

