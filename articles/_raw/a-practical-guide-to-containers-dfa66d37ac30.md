---
title: A practical guide to containers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T19:56:47.000Z'
originalURL: https://freecodecamp.org/news/a-practical-guide-to-containers-dfa66d37ac30
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BNdwczuGtUJQLjgi2EaxZg.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Julius Zerwick

  Containers have taken over the software world by storm — and for good reason.

  They’ve proven vital for DevOps and deployment, and have a multitude of uses for
  developers. And this goes not only for large companies, but for independe...'
---

By Julius Zerwick

Containers have taken over the software world by storm — and for good reason.

They’ve proven vital for DevOps and deployment, and have a multitude of uses for developers. And this goes not only for large companies, but for independent developers as well. In fact, containers played a vital role in the development and deployment of our project [SpaceCraft](https://spacecraft-repl.com).

In this article, we’re going to give an introduction to containers and explain their core features. We’ll then showcase their uses in software development and cover some important topics regarding security and resource management. Along the way, we’ll give a peek into [how containers were utilized in SpaceCraft](https://spacecraft-repl.com/whitepaper#5-security--resource-management-with-containers). Let’s dive in!

### What Is A Container?

So what exactly is a container?

At its core, a container can be described as a single unit of encapsulated software. It’s essentially a box in which you can place all of your project dependencies and run a single service or an entire development environment, while keeping everything inside the box isolated from the host system.

![Image](https://cdn-media-1.freecodecamp.org/images/GTyN5psx6tnP8jU-X7MRTTZULVVcq12QmoMe)

As an example, imagine that you need to work on a new project and know all of the needed dependencies. But some of these dependencies may conflict with what you already have installed on your computer, like a language version number.

If you were to work on the project on your computer, you’d have to go through the tedious process of managing your dependencies and deactivating versions while activating the versions that you need.

This issue is compounded when it’s a whole team of developers working on the same project, and no two developers have the same configurations on their computer.

With a container, you can simply put all your needed dependencies inside it and then work on your project from within the container. This saves a ton of a headache by eliminating the dependency management issues and instead providing us with an isolated area to work in.

### How are containers made?

So we now know what a container is. But how exactly do we create them?

Well, to start we need to create an image. This is simply a package that includes all of the dependencies that should exist in our container. It’s a snapshot of everything that should be inside our container when we run it.

![Image](https://cdn-media-1.freecodecamp.org/images/4ONl-2xcwZXUBC3VFRjgGYPUO0SDakgpy1Na)

An easy way to visualize this is to think of an image as a class and a container as an object that is instantiated from that class. So our image will serve as a blueprint for creating our containers, and we can create any number of identical containers from the same image.

### How are images built?

Images are built by [executing a set of commands](https://www.aquasec.com/wiki/display/containers/Docker+Images+101). In Docker, the set of commands are written in a text file called Dockerfile.

When the image build process starts, each command [forms a layer](https://docs.docker.com/storage/storagedriver/#images-and-layers) that comprises the final image. The last layer specifies what command to run within a container when a container is started.

![Image](https://cdn-media-1.freecodecamp.org/images/rfC-aIsKtyAL5VruQcu34TTlATH4FZsqGekJ)
_An example Dockerfile that builds into an image. Each layer represents an instruction from the Dockerfile._

In [SpaceCraft](https://spacecraft-repl.com), we bundled a [modified version of Ubuntu](https://hub.docker.com/r/phusion/baseimage/), our language runtimes, and a copy of our application code into an image to start multiple containers that each run an instance of our application.

Images do not necessarily need to be stored or built on just your local machine. Containers are meant to be deployable anywhere and thus we should be able to access our images from any physical machine. This is accomplished through [registries](https://docs.docker.com/registry/introduction/#understanding-image-naming), which are essentially a place to remotely store and access images.

### Why should we use containers?

Now we can dive into the many use cases of containers.

Remember how we said that containers can provide us with an isolated box to hold a development environment with a specific set of dependencies? Each developer can simply download the needed image from a registry onto their local computer and then create a container from that image.

This way, they can start contributing to existing projects in no time.

#### Ease of deployment

As you can see, one of the biggest advantages of containers is that they are easily deployable on a variety of systems, due to their isolation. This allows developers to uncouple their software from their physical machines and launch a container from anywhere.

#### Run multiple services on one machine

Another use case involves placing a single service in a container and then communicating with that service.

In this situation, you can build a system that houses individual services in separate containers. This allows you to isolate each piece of your system architecture and run multiple services on the same host while making it easy to swap services in and out of your system as needed.

To demonstrate how this works, each service can communicate with each other through [Docker container networking](https://docs.docker.com/v17.09/engine/userguide/networking/) by their IP addresses. With this, containers can, for instance, send HTTP requests with the destination container’s IP address as part of the URL.

![Image](https://cdn-media-1.freecodecamp.org/images/uLp2wy8wRF0OP2ovvggkNzh42OvFbkmdGIwu)
_Containers can communicate with each another via their IP addresses._

In fact, we use this technique in [SpaceCraft](https://spacecraft-repl.com). We’ve built a [reverse proxy server](https://www.incapsula.com/cdn-guide/glossary/reverse-proxy.html) that forwards clients’ requests to the appropriate containers. To enable communication between our reverse proxy server and the containers, we retrieve the containers’ IP addresses during initialization and use them as destinations for proxying.

#### Isolation for Security

Another important use case is that containerized applications are isolated from the host system. This prevents unwanted user access to the host’s file system. This is important, especially for an application like [SpaceCraft](http://repl.space) that gives users the ability to execute code.

We can also add security measures to strengthen the isolation and further prevent malicious activity from reaching our host system. We’ll explore these strategies in the following section.

### Containers versus Virtual Machines

At this point, we want to make clear the distinction between containers and virtual machines, as this can heavily impact your decision on which to use.

Virtual machines came before containers, and were used to address the same pain points as containers. Essentially, they provide an isolated environment for services and development and are deployable on multiple systems.

However, there are some significant differences between them and containers.

#### Containers are more lightweight, and faster to spin up

First, containers are more lightweight in memory requirements than virtual machines. Depending on what you place in a container, they generally run in the tens to hundreds of MBs for memory size.

Virtual machines are far heavier and run into the GBs. This is mainly due to one big inclusion: the operating system kernel.

![Image](https://cdn-media-1.freecodecamp.org/images/binzfjGViQTJIpQs3d9UUIxsgl62HClcJOac)
_Source: [I am a Developer: why should I use Docker?](https://blog.octo.com/en/i-am-a-developer-why-should-i-use-docker" rel="noopener" target="_blank" title=")_

Virtual machines contain not only all of your dependencies for your service or environment, but also a full copy of an operating system kernel to run all of your dependencies. This addition can add a lot of memory to an instance of a virtual machine.

On the other hand, containers don’t contain a kernel and instead make system calls to the host system kernel. This dramatically lowers their memory footprint. It allows for more containers to be created and used on a system, as opposed to the number of virtual machines you can run on the same system.

In addition to a smaller memory footprint, the lack of a kernel in a container makes their startup time a lot faster. Container startup can happen in seconds, whereas virtual machines will take much longer.

#### VMs are more secure by default

However, there are always tradeoffs. When it comes to virtual machines versus containers, the big tradeoff is security.

Because containers need access to the host system kernel to make system calls, they are not as airtight on security as a virtual machine.

In fact, resourceful malicious users can find ways to use this security disadvantage to break out of a container and gain access to the host system.

With virtual machines, this risk is mitigated because each instance of a virtual machine contains a kernel for its system calls. Thus there is stronger isolation between a virtual machine and the host system than with a container.

However, the security risks of containers can be addressed by implementing a few security measures that we incorporated into [SpaceCraft](https://spacecraft-repl.com), which we will look at now.

### Security measures

One huge security issue that you should know about is that users generally run as root users in containers by default.

This means that anyone who works inside a container, whether a developer on your team or a user who is using an application that is housed in a container on the back end, will have privileged access to the container file system.

If you’re concerned about giving this level of control over to the container user, then you should consider ways to limit their privileges.

This issue can be addressed by creating an unprivileged user profile in the container filesystem, and having users run as that user profile while in the container.

This will restrict their ability to access the container filesystem and run commands that could harm your container environment and any services running inside it.

Another security issue that can rear its head is the ability for users to break out of containers and access the file system of the host system.

As we mentioned before, containers make system calls to the host system kernel in order to run processes. This opens the door for malicious users to break out of a container and attach the host system.

![Image](https://cdn-media-1.freecodecamp.org/images/WZ5jhJvKBZOluHlpS9dKrdvRy5THnryb24ts)
_Containerization alone provides weak isolation, where all system calls made by our application are accepted by the host kernel. Source: [gVisor Github](https://github.com/google/gvisor" rel="noopener" target="_blank" title=")_

One of the methods we use to prevent this situation is to use a container runtime sandbox to intercept the system calls made by a container. The sandbox acts as a guest kernel and creates a strong level of isolation between the container and host kernel. This prevents malicious users from attacking our host system.

If you’re interested in using a container runtime sandbox, check out [gVisor](https://github.com/google/gvisor) which is an open-source solution provided by Google that we utilized with [SpaceCraft](https://spacecraft-repl.com).

### Container resource control

One more issue that we want to address pertains to potential abuse of a container’s resources.

Since a container runs on a host system and uses the host kernel, it essentially consumes CPU and memory resources from the host system to complete its processes and tasks.

While this is usually not a problem on an individual level with developers using containers, it does become a bigger problem once we use containers to deploy applications to be used by external users.

Let’s say that your system architecture includes using containers to run separate instances of your application that users can access. And something happens with one of those containerized instances that requires more CPU and memory from the host system than expected.

What this can result in is that one instance hogs system resources away from the other instances which causes their performances to drop and create a poor user experience.

Obviously, this is a situation that we want to avoid if possible. Thankfully we can do so with cgroups, which is short for ‘control groups’.

With cgroups, you can limit the amount of system resources used by a container and thereby prevent the situation we just described.

For example, you can set the cgroups on a container to be a maximum of 100MB of memory and 20% of CPU. With those limits set, that container will never be able to use more than 100MB of memory or utilize more than 20% of CPU from the host system for its lifetime. You can rest easy knowing that the performance of your other containerized application instances will not drop.

In SpaceCraft, we utilized cgroups to limit the maximum amount of memory and CPU that a single session can consume. If a session happens to run an expensive computation and consume all available resource within that container, only that session will be affected.

![Image](https://cdn-media-1.freecodecamp.org/images/GVqFqcXMbtyeqoFz37VjUoH-Ge-keD5nstpE)
_With each session isolated and controlled through cgroups, a single spike in resource consumption will only affect that session, while leaving others unaffected._

### Where can I get started?

There are many container services that you can choose from. We used Docker for [SpaceCraft](https://spacecraft-repl.com) due to its ease of use and excellent documentation. We highly recommend it for your next project.

Other options include:

* Redhat OpenShift
* Amazon EC2 Container Service
* AWS Elastic Container Registry
* Google Cloud Container Registry
* Azure Kubernetes
* HashiCorp
* Quay

#### Integration with Node.js

If you use Node.js primarily for your development, [Dockerode](https://github.com/apocas/dockerode) can help you to interact with Docker from within a Node.js environment. We leveraged Dockerode to help us perform some important container actions, including:

* Starting and destroying a container
* Reading a container’s IP address
* Placing limits on a container’s memory and CPU usage

Those operations are important to help us handle multiple sessions and scale our application.

### Conclusion

Containers are an extremely useful tool in your arsenal as a software developer to simplify and speed up your project deployment.

Whether it’s creating an isolated development environment for building projects, setting up a microservices architecture, or helping to onboard a new team member, the utility of containers continues to grow over time. Give it a try in your next project and see how they can benefit you!

If you enjoyed reading this article, we’ve also written a detailed case study on how we built SpaceCraft and the challenges that we faced. You can [read it here](https://spacecraft-repl.com/whitepaper).

_Co-written by Julius, Gooi, and Nick of the [SpaceCraft Team](https://spacecraft-repl.com/team)._

### References

- [What is a container](https://www.docker.com/resources/what-container)  
- [I am a Developer: why should I use Docker?](https://blog.octo.com/en/i-am-a-developer-why-should-i-use-docker/)  
- [Docker Security Best-Practices](https://dev.to/petermbenjamin/docker-security-best-practices-45ih)  
- [Open-sourcing gVisor, a sandboxed container runtime](https://cloud.google.com/blog/products/gcp/open-sourcing-gvisor-a-sandboxed-container-runtime)  
- [Why it is recommended to run only one process in a container?](https://devops.stackexchange.com/questions/447/why-it-is-recommended-to-run-only-one-process-in-a-container)  
- [Processes In Containers Should Not Run As Root](https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b)  
- [Security and Virtual Machines](https://pubs.vmware.com/vsphere-4-esx-vcenter/index.jsp?topic=/com.vmware.vsphere.server_configclassic.doc_40/esx_server_config/security_for_esx_systems/c_security_and_virtual_machines.html)

