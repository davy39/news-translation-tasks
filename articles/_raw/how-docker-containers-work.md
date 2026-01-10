---
title: How Docker Containers Work – Explained for Beginners
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-10-23T16:45:13.000Z'
originalURL: https://freecodecamp.org/news/how-docker-containers-work
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/cover-final.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
- name: virtual machine
  slug: virtual-machine
- name: virtualization
  slug: virtualization
seo_title: null
seo_desc: 'A container is a lightweight, standalone, and executable software package
  that includes everything needed to run a piece of software.

  And one of the most popular tools for working with containers is Docker.

  Docker is both the name of the company (Doc...'
---

A container is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software.

And one of the most popular tools for working with containers is Docker.

Docker is both the name of the company (Docker Inc) and the software they have created which packages software into containers.

To understand how containers work and why they are incredibly useful for software development, you need to understand two seemingly unrelated topics – shipping containers and virtual machines.

## A Brief History of Shipping Containers

"The Box: How the Shipping Container Made the World Smaller and the World Economy Bigger" is a book by [Marc Levinson](https://www.amazon.co.uk/Box-Shipping-Container-Smaller-Economy/dp/0691170819/ref=sr_1_1?crid=14VL4VEQHDVNL&keywords=the+box+book&qid=1694037660&sprefix=the+box+book%2Caps%2C97&sr=8-1). It explores the profound impact of the shipping container on global trade and the world economy.

While the history of the shipping container may seem irrelevant in a discussion about Docker containers, they have more in common than you would expect.

Before shipping containers, cargo handling was labor-intensive and time-consuming, leading to inefficiencies and delays in global trade. Cargo arrived in various shapes and sizes, and the lack of standardised packaging made it challenging to stack and secure items efficiently.

Without standardised containers, cargo was often stored haphazardly in the holds of ships or in dockyards. This inefficient use of space meant that ships were not carrying as much cargo as they could potentially hold, leading to higher transportation costs.

The adoption of uniform container dimensions and handling procedures allowed for seamless transfer of cargo between different modes of transportation – ships, trucks, trains, and the cranes used to move the containers around.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ac7826e-ebd0-4062-8f49-d48a6f9ef9ce_1886x946.png align="left")

*Image showing how standardised container sizes allow them to be easily moved between ships, trains and trucks.*

This standardisation was the key to the success of shipping containers. After all, if one company’s containers didn't fit on another company's ship, truck, or freight train, they couldn't be properly transported. Every company would need its own fleet of containers to be able to send things to each of their customers – which would be an operational nightmare.

Standardisation of shipping containers makes them portable, that is easy to move from one place to another. This portability is a key feature of Docker containers as well, which we'll discuss shortly.

## What are Virtual Machines?

Virtual machines (VMs) are created through a process called virtualisation.

Virtualisation is a technology that allows you to create multiple simulated environments or virtual versions of something, such as an operating system, a server, storage, or a network, on a single physical machine.

These virtual environments behave as if they are independent, separate entities, even though they share the resources of the underlying physical system.

Virtualisation is like having a magician's hat that can conjure up multiple hats within it. Just as the magician's hat creates the illusion of many hats appearing from just a single physical hat, virtualisation allows a single physical computer or server to appear as multiple virtual machines (VMs), each with its own operating system and resources.

VMs virtualise the hardware. This simply means that a VM takes a single piece of hardware – a server – and creates virtual versions of other servers running their own operating systems. Physically, it is just a single piece of hardware.

Logically, multiple virtual machines can run on top of a single piece of hardware. This is essentially one or more computers running within a computer, as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9733d44-d0c7-49e6-8978-da253cf9c3a9_1650x966.png align="left")

*Image showing how virtualisation creates several virtual machines (VMs) from a single physical server*

### How does virtualisation work?

So you might be wondering – how exactly does virtualisation work? Have a look at the image below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cd74b32-e3d1-430f-bbd6-e0daf2150b82_1084x576.png align="left")

*Image showing how virtualisation works by virtualising a single piece of hardware to create multiple virtual machines*

At the base, you have the host hardware and OS. This is the physical machine that is used to create the virtual machines. On top of this, you have the hypervisor. This allows multiple virtual machines, each with their own operating systems (OS), to run on a single physical server.

VMs have a few downsides, though, which containers address. Two downsides particularly stand out:

1. VMs consume more resources: VMs have a higher resource overhead due to the need to run a full OS instance for each VM. This can lead to larger memory and storage consumption. This in turn can have a negative effect on performance and startup times of the virtual machine.
    
2. Portability: VMs are typically less portable due to differences in underlying OS environments. Moving VMs between different hypervisors or cloud providers can be more complex.
    

The major cloud providers all have VMs. For AWS, it's EC2, GCP has Compute Engine, and Azure has Azure Virtual Machines.

## What are Containers?

A container is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, system tools, and libraries.

Containers are designed to isolate applications and their dependencies, ensuring that they can run consistently across different environments. Whether the application is running from your computer or in the cloud, the application behaviour remains the same.

Unlike VMs which virtualise the hardware, [containers virtualise the operating system](https://aws.amazon.com/compare/the-difference-between-containers-and-virtual-machines/#:~:text=Containers%20virtualize%20the%20operating%20system,use%20your%20hardware%20resources%20efficiently.). This simply means that a container uses a single OS to create a virtual application and its libraries. Containers run on top of a shared OS provided by the host system.

This is illustrated below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55e6ff35-1917-4374-8006-80aa8668a772_1160x470.png align="left")

*Image showing how containers works by virtualising the OS*

The container engine allows you to spin up containers. It provides the tools and services necessary for building, running, and deploying containerised applications.

Containers have several benefits:

1. **Portability**: Containers are designed to be platform-independent. They can run on any system that supports the container runtime, such as Docker, regardless of the underlying operating system. This makes it easier to move applications between different environments, including local development machines, testing servers, and different cloud platforms.
    
2. **Efficiency**: Containers share the host system's operating system, which reduces the overhead of running a virtual machine with multiple operating systems. This leads to more efficient resource utilization and allows for a higher density of applications that can run on a single host.
    
3. **Consistency**: Containers package all the necessary components, including the application code, runtime, libraries, and dependencies, into a single unit. This eliminates the "it works on my machine" problem and ensures that the application runs consistently across different environments, from development to production.
    
4. **Isolation**: Containers provide a lightweight and isolated environment for running applications. Each container encapsulates the application and its dependencies, ensuring that they do not interfere with each other. This isolation helps prevent conflicts and ensures consistent behaviour across different environments.
    
5. **Fast Deployment**: Containers can be created and started quickly, often in a matter of seconds. This rapid deployment speed is particularly beneficial for applications that need to rapidly scale up or down based on demand.
    

## What is Docker?

Now that we have covered VMs and containers, what exactly is Docker? Docker is simply a tool for creating and managing containers.

At its core, Docker has two concepts that are useful to understand: the Dockerfile and Docker Images.

A Dockerfile contains the set of instructions for building a Docker Image.

A Docker Image serves as a template for creating Docker containers. It contains all the necessary code, runtime, system tools, libraries, and settings required to run a software application.

So, a Dockerfile is used to build a Docker Image which is then used as the template for creating one or more Docker containers. This is illustrated below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f5a703a-0a08-48a0-be54-46ca4a29a9dc_1974x534.png align="left")

*Image showing the steps to create a docker container. First you create the Dockerfile which is used to build the Docker Image which is finally used to run a Docker container*

If this explanation still causes you to scratch your head, consider the following analogy using shipping containers.

Imagine you need to build multiple shipping containers to transport items all over the world. You start with a document listing out the requirements for your shipping container. This will contain information like the container dimensions, type of seals, door locking mechanisms, ventilation and refrigeration requirements (if you are shipping food that needs a temperature controlled environment, for example), and so on.

This requirement document will then be used to create a detailed template for the container which will include engineering drawings showing the dimensions and other specifications.

From this template, the physical containers will then be built. This single template can be used to build one or many physical containers which will all be identical and match the specifications in the container template.

This is illustrated below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa1ac249-4fd1-49f2-8b7b-e52914017f89_1944x830.png align="left")

*Image showing a shipping container analogue for docker containers*

The Dockerfile is analogous to the requirements document, which simply has a set of instructions for building the container template.

The Docker Image is analogous to the container template, which details all the instructions needed for building the physical container.

Once created, Docker images are immutable, meaning they cannot be changed. If you need to make changes to an application, you need to modify the Dockerfile and create a new image. This immutability ensures consistency and reproducibility in application deployment.

And finally, the Docker container is analogous to the physical shipping container.

## Bringing it Together

In summary, containers provide a **portable** and **efficient** way to package applications and their dependencies, ensuring consistency across various environments. The benefits they bring to software development is similar to the benefits brought to the global economy by the humble shipping container.

### Portability

Shipping containers, through standardisation, ensure that any container, anywhere in the world, can be seamlessly used to move items across various modes of transportation – ships, trucks, trains and the cranes used to load them on and off different forms of transport.

Similarly, Docker containers allow for portability. They ensure that applications can run consistently across different environments, from development laptops to production servers, and across different cloud providers.

### Increased Efficiency

With standard container sizes, the packing density of goods you can move increases. Now, you can squeeze more things into a single shipping container, compared to the days before the shipping container existed where you had cargo in non standard shapes and sizes stored haphazardly in the holds of ships or on dockyards. So, every ship, freight train or truck can carry more goods during every trip, making it cheaper to move goods around the world.

With Docker containers, better efficiency comes from the fact that containers share the host operating system, making them lightweight compared to VMs. This leads to rapid container startup times and less CPU, memory, and storage use.

Less resource utilisation also means that containers can increase the application density when compared to VMs. With containers, you can run more applications on the same hardware without a significant drop in performance.

To conclude, the shipping container by itself is not magical. After all, it is just a metal box. It is the standardisation of shipping containers which made them portable and a cheap and efficient way to move goods around the world.

In application development, containers benefit from standardisation in the same way. Containers provide a portable and efficient way to package applications and their dependencies, ensuring consistency across various environments.
