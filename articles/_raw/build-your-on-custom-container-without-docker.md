---
title: How to Build a Docker Engine-like Custom Container without Any Software
subtitle: ''
author: Gursimar Singh
co_authors: []
series: null
date: '2022-08-10T16:45:36.000Z'
originalURL: https://freecodecamp.org/news/build-your-on-custom-container-without-docker
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/image-12-1.png
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: 'This article will discuss every aspect of containers, including how they
  operate in the background and their various component elements. We will also discover
  why Docker is so lightning-fast.

  By the end, you''ll be able to create your own custom conta...'
---

This article will discuss every aspect of containers, including how they operate in the background and their various component elements. We will also discover why Docker is so lightning-fast.

By the end, you'll be able to create your own custom container. We'll also examine why Kubernetes deprecated Docker and embraced CRI-O, as well as how to configure a multi-node Kubernetes cluster using CRI-O.

In the end, we will look at the list of available container runtimes.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-11.png)

## Table of Contents

1. [What are containers](#heading-what-are-containers)?
2. [Why do we need containers](#heading-why-do-we-need-containers)?
3. [What's the difference between containers and virtualization](#heading-whats-the-difference-between-containers-and-virtualization)?
4. [Is there a standard format for containers](#heading-is-there-a-standard-format-for-containers)?
5. [Types of container platforms](#heading-types-of-container-platforms)
6. [How to launch a container](#heading-how-to-launch-a-container)
7. [Why did Kubernetes deprecate Docker](#heading-why-did-kubernetes-depreciate-docker)?
8. [Challenges of using Docker](#heading-challenges-of-using-docker)
9. [What is a CRI (Container Runtime Interface)](#heading-what-is-a-cri-container-runtime-interface)?
10. [How to build a multi-node cluster using CRI-O](#heading-how-to-build-a-multi-node-cluster-using-cri-o)

Alright, let's dive in.

## What Are Containers?

Containers allow you to reliably move software from one computing environment to another.  

The technology behind containers is nearly as old as that behind virtual machines. But the information technology industry didn't begin using containers until around 2013–14, when Docker, Kubernetes, and other innovations that disrupted the sector became popular. 

Containers have emerged as a critical tool in the process of developing software. They can serve either as a replacement for Virtual Machines or as a supplement to them. 

Containerisation helps developers construct apps more rapidly and securely while also deploying them more easily.

## Why Do We Need Containers?

As we learned above, containers provide a solution to the problem of transporting software from one computer environment to another in a reliable manner. This can be just from a developer's workstation to a test environment, from a staging environment to production, or even from a real system in a data center to a private or public cloud virtual machine. 

Containerization makes possible all of these transformations. And these are just some of the viewpoint alterations that can happen.

This quote gives a little perspective on why containers are helpful:

> "You’re going to test using Python 2.7, and then it’s going to run on Python 3 in production and something weird will happen.   
>   
> Or you’ll rely on the behavior of a certain version of an SSL library and another one will be installed.   
>   
> You’ll run your tests on Debian and production is on Red Hat and all sorts of weird things happen.   
>   
> The network topology might be different, or the security policies and storage might be different but the software has to run on it." – Solomon Hykes

## How Do Containers Solve This Issue?

A more straightforward interpretation is that a container is an all-encompassing runtime environment. 

This means that a piece of software, together with all of its dependencies, libraries, other binaries, and configuration files, is packed and distributed to customers as a single package. 

The application platform and its dependencies can be protected from the consequences of changes in operating system distribution and underlying infrastructure if they are bundled within containers.

## What’s the Difference Between Containers and Virtualization?

A virtual machine is a package that may be shared when employing virtualization technology. This package includes both the program and the operating system being used. 

On top of a physical server running three virtual machines, you'd have an installation of a hypervisor, as well as three distinct operating systems.

On the other hand, a Docker server that hosts three containerized programs only needs to run a single operating system because all of the containers share the same kernel. The standard components of the operating system can only be read, but each container has its own mount or access mechanism, which allows it to store and retrieve data. 

This hints that containers are far lighter than virtual machines and make considerably less use of their resources.

## Is There a Standard Format for Containers?

When CoreOS published its own App Container Image (ACI) specification in 2015, some people worried that the rapidly growing container movement might splinter into different Linux container formats. This was because ACI stood for "App Container Image."

In contrast, the Open Container Project, which would subsequently become the Open Container Initiative (OCI), was not made public until the latter half of the same year.

The [Open Container Initiative](https://opencontainers.org/), which the Linux Foundation leads, aims to establish an industry standard for container formats as well as container runtime software that is compatible with all operating systems (OCI).

Docker technology was used to develop the Open Container Project (OCP) guidelines, and Docker gave around 5 percent of their software to help get the effort off the ground.

### What is Open Container Initiative?

The Open Container Initiative (OCI) is an organization whose mission is to ensure that the fundamental aspects of container technology, such as the container's format, are standardized so that anyone can use them.

As a result, companies can concentrate their efforts on developing the supplementary software they need in order to use standardized containers in an enterprise or cloud environment (instead of developing competing technologies for containers). 

Software components called container orchestration and management solutions, as well as container security systems, are essential components.

## Types of Container Platforms

As a result of the development and expansion of container technology, a number of different choices are currently available. 

Docker is, without a doubt, the most common and widely used container platform available. 

On the other hand, the landscape of container technologies includes other technologies, each of which has its own use cases and benefits.

We will look at the two most famous ones, i.e., Docker and Podman.

### Docker

Docker is the container platform that's currently the most popular and is used the most widely. It allows you to develop and use Linux containers. 

Docker is a piece of software that, by using containers, simplifies the processes of creating, deploying, and operating software applications. It does this by minimising the number of steps in each process. 

Docker has gained support not just from the most major Linux distributions, such as Red Hat and Canonical, but also from large organisations, such as Microsoft, Amazon, and Oracle. 

Virtually all businesses concerned with information technology and cloud computing use Docker.

##### Docker Architecture and Components

Docker is built on a client-server architecture. The Docker daemon enables the creation, operation, and distribution of Docker containers. 

The Docker client and Docker daemon can interact through a REST application programming interface (API), UNIX sockets, or network interface.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-34.png)
_Source: docs.docker.com_

Docker's architecture is comprised of the following five primary components:

1. **Docker Daemon** manages Docker objects like images, containers, networks, and volumes. It also responds to Docker API inquiries.
2. **Docker Clients** enables users to interact with Docker by allowing the user to connect with Docker. Docker client supplies a CLI interface that allows users to send application commands to a Docker daemon and start and halt such operations.
3. **Docker Host** provides a complete software program execution and operation environment. This system comprises the Docker daemon, Images, Containers, Networks, and Storage components.
4. **Docker Registry** maintains Docker Images. Docker Hub is a public registry, and by default, Docker is configured to use images saved on Docker Hub. You can use it to administer your own register.
5. **Docker Images** are templates that can only be read and produced by following a Dockerfile's set of instructions. Images specify the appearance we want for our packaged program, its dependencies, and the processes that should run when the application is launched.

#### Resource Isolation components in Docker

##### Namespaces:

* PID namespace for process isolation.
* NET namespace for managing network interfaces.
* IPC namespace for managing access to IPC resources.
* MNT namespace for managing filesystem mount points.
* UTS namespace for isolating kernel and version identifiers.

##### Control groups

* Memory cgroup that oversees accounting as well as restrictions and alerts
* HugeTBL is a cgroup that keeps track of each process group's use of huge pages.
* CPU group is responsible for regulating the time users and the system spend using CPU.
* CPUSet cgroup lets you associate a group with a certain CPU. Utilized for real-time workloads and NUMA systems with localised memory for each CPU.
* BlkIO cgroup for measuring and limiting the amount of blkIO each group produces.
* the net cls and net prio cgroups are utilised for traffic control tagging.
* Devices cgroup for accessing devices that can both read and write data.
* Cgroup for the freezing of a group referred to as the freezer. It is useful for scheduling cluster batches, relocating processes, and troubleshooting.

##### Union Filesystem

* Docker images are composed of layered filesystems, allowing them to be extremely lightweight and speedy. Union file systems are layering-based file systems.
* Docker Engine has the ability to use several different versions of UnionFS, such as AUFS, btrfs, vfs, and devicemapper.
* For executing five 250MB image containers, we would require 1.25GB of disc space if we didn't have UnionFS.

The Docker interface may appear to be a mysterious black box holding a variety of unknown technologies when seen from the outside. Despite their relative obscurity, these technologies are both highly intriguing and useful.  
  
Despite the fact that we do not need to grasp these technologies in order to utilise Docker effectively, it is still beneficial to learn about and have an awareness of these technologies.   
  
If we have a deeper understanding of the instrument, it will be much easier for us to make the proper decisions, such as those regarding performance optimization or security implications.   
  
In addition, this facilitates the discovery of innovative new technologies, which may have many more uses for the organisation than initially thought.

### Just a note:

Docker does not require cgroupfs as the control group driver. The cgroup can be changed to systemd. 

Docker's own control group manager is cgroupfs. Nevertheless, for most Linux distributions, systemd is the default init system, and systemd has tight interaction with Linux control groups. 

For Kubernetes, it is recommended to use systemd, as utilising cgroupfs in conjunction with systemd appears to be suboptimal.

So systemd is preferable for cgroup management. kubelet is set to utilise systemd by default. Therefore, Docker should be modified to utilise the systemd driver. 

##### Docker Engine Sparked the Containerization Movement

The Docker Engine is the de-facto container runtime for Linux and Windows Server platforms. 

Docker develops simple tools and a uniform packaging strategy that encapsulates all application requirements into a container, which is then executed by Docker Engine. 

The Docker Engine enables containerized apps to operate anywhere reliably on any infrastructure, resolving "dependency hell" for developers and operations teams and removing the "it works on my laptop!" issue.

### Podman

Podman is RedHat's product. Docker and Podman are fairly comparable to one another in many ways. 

Podman provides a Docker-compatible command-line interface that you can alias to the Docker command-line interface with the `$ alias docker = podman`. Also, Podman provides a socket-activated REST API service that makes it possible for remote apps to launch containers whenever they want. 

Users of docker-py and docker-compose are able to connect with Podman as a service because this REST API also supports the Docker API.

By using the libpod library, Podman is able to handle the entirety of the container ecosystem, which includes pods, containers, container images, and container volumes. 

Podman is distinct from Docker in that it does not require a server and has a lightweight and Daemon-less design. This means that it makes direct contact with runC to start containers, which eliminates the need for an overhead server.

Containers managed by Podman can either be operated by the root user or by a user with fewer privileges than root. 

While working with Docker, the Docker Command Line Interface is how we interface with the daemon that Docker runs in the background. The daemon, which operates on containers and produces pictures, is where the majority of the program's functionality can be found. 

This daemon runs with the permissions of the root user. This also suggests that a Docker container may have access to the file system of the host computer if the configuration is not done appropriately. 

In contrast, the architecture of Podman makes it possible for us to collaborate with the user who is responsible for running the container, and this user does not need to have root access in order to execute the application. 

When compared to containers that run with root capabilities, non-privileged containers provide a substantial advantage. This is because if an intruder breaks into a non-privileged container and flees, the intruder will still be an unprivileged host user. Using this approach provides an additional safeguard for our data.

Just replace Docker with Podman in the instructions to use it. It has the same commands as Docker.

```
$ alias docker=podman
```

##### What other advantages does Podman have? 

* Integrated support for systemd makes it possible to run container processes in the background without the need for a separate daemon process.
* Provides us with the ability to build and manage Podami, a collection consisting of one or more functional containers. Because of this, future workload migration to Kubernetes and the orchestration of Podman containers is now possible.
* It is possible to implement UID separation using namespaces, providing an additional layer of security isolation while containers are being executed.
* Can create a YAML file for Kubernetes from a container that is currently operating (with the command `$ podman generate kube`).

## How to Launch a Container

To launch any container we need two things: Image and RunTime.

Container engines such as Docker and Podman are only an additional software layer that sits on top of the runtimes. They are not responsible for actually launching the containers themselves. 

They also initiate interaction with the runtimes in the background to start the container processes.

A Container Runtime is a software that runs and manages the components required to run containers.

Runtime is actually a program/software which launches, deletes, and removes containers.

runC is a very famous Runtime, but we have many other Runtimes like gvisor and kata.

Docker connects to this runtime behind the scenes.

The runtime spec file is a configuration file where we give all the important things for the container to be launch like CMD, folder, network, and so on. It is the file that the container runtime uses to launch the container.

We can verify that Docker is using runC as its default runtime engine like this:

```
$ docker info
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-35.png)

### How to use runC – the universal container runtime

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-36.png)

Because "containers" are a collection of complex and occasionally obscure system elements, they are combined into a single low-level component. This is runC.  
As a standalone tool, infrastructure plumbers all around the world utilise runC as plumbing.

runC is a lightweight, portable runtime for containers. It is a command-line tool for creating and running containers according to the Open Container Initiative (OCI) specification. It has libcontainer, which is the original lower-layer library interface that the Docker engine used to set up what we call an operating system container.

runC is designed with the principles of security, usability at large scale, and no dependency on Docker in mind.

Whenever we launch a container, it starts within a second. It looks like a new OS has launched because it has all the things an OS would have (like all the commands, network card, and more). It looks like an independent OS.

#### How can a container be launched in one second?

As you may know, when you run any program, it becomes a process. So even here, every running container is a process in the host system. So whenever we launch a container, it means we have started some process.

It looks like that container is a different OS with its own file system, network, and so on, as I mentioned above. But the kernel runs this entire setup inside a process by using the concept of namespaces. We'll discuss namespaces further in a minute.

So, as the container is a process, it launches quickly.

A container is just a process running in the RAM. This process looks like it is running a full-flash OS inside an OS. Typically, the process (container) runs the bash command, which has an infinite lifetime till someone gives an exit command.

If we inspect the container, we can find the PID of the /bin/bash command running in the base OS. Now, if we kill the process of the /bin/bash, the container will also be terminated.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-37.png)

#### What is a namespace?

Again, running a container is also a process. But with Docker, a container is given with its own principal user, network configuration, mount folders, filesystem, and so on which they get as a common component of the baseOS. As a result, the container now has its own isolated environment, known as a namespace.

```
$ lsns

# To list down all the namespace in the baseOS
```

To launch a container, Docker Creates a Runtime Spec file for runC, and then runC uses that to launch the container. runC creates Namespaces for the container process.

The Image works as a Hard Drive – that is, it contains the entire file system for the container. A Container Image bundles all the data which is mounted on a storage namespace (that is, mount namespace).

The Image creates the entire bundle in the "/" directory of the containers. We have to unbundle it by untaring it.

Note that runC will not download, unzip, or untar the images for us. It can launch the container and mount the files for us to the container. For the images, we need some image management tools.

Also, runC only provides us with a network namespace, but Docker has to manage the network (that is, specify the IP range, provide IPs, and so on).

Docker can download, unzip, or unbundle the images. It can also do the required networking setup. It can also connect to the storage for us, and many such features are provided by Docker. Typically, Docker can do almost all the stuff provided by Kubernetes via its commands.

In Docker, we have a client-server architecture in which we have Docker CLI working as the client program and the container as the server. The server will now connect to the runtime and launch the container for us.

If we want to launch the container directly, we can do so with the help of runC. 

First, we need to install runC using yum.

```
$ runc list 

# This will list the available containers.
```

```
$ runc spec

# To create a runtime spec file in current directory.
```

runC is written in the Go language. So, generally it supports Go programs (images are also written in the Go language).

`$ go build -o name` is the command to compile a Go program.

### runC Commands:

```
$ runc create <cont_name>

# To launch a container (This will take config file from current directory).
```

```
$ runc start <cont_name>

# This command will run and give the output of the program that we’ve specified in container.
```

In the workspace we use the following:

```
$ runc spec

# This will create a config.json file for the runC configuration.
```

In the congif.json file, we must change the parameters-values according to our requirements. 

For example, if we don’t want the terminal, we need to make it false. For that we can give the command to run in the arg, we can set the hostname, and so on.

We can connect to this container namespace by doing the following:

```
$ nsenter -u -t -n <pid_of_container>

# To enter user and network namespace of specific process ID.
```

#### To create a container just by using runC:

1. Install runC.
2. Create config.json by running the runC spec command.
3. Mention all the important things in the above file. We also have to give process by writing its code in the Go language.
4. Create a rootfs folder in the current workspace and move the compiled Go code into this folder.
5. Now, to launch the container:

```
$ start runc create <container_name>
```

To start the container and print on the console whatever is there in the go file, run this command:

```
$ runc start <container_name>
```

### How to generate an example specification with runC:

```
> runc spec
> cat config.json
{
  "ociVersion": "1.0.0",
  "process": {
    "terminal": true,
    "user": { "uid": 0, "gid": 0 },
    "args": ["sh"],
    "env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      "TERM=xterm"
    ],
    "cwd": "/",
    "capabilities": {
      "bounding": ["CAP_AUDIT_WRITE", "CAP_KILL", "CAP_NET_BIND_SERVICE"],
      [...]
    },
    "rlimits": [ { "type": "RLIMIT_NOFILE", "hard": 1024, "soft": 1024 } ],
    "noNewPrivileges": true
  },
  "root": { "path": "rootfs", "readonly": true },
  "hostname": "runc",
  "mounts": [
    {
      "destination": "/proc",
      "type": "proc",
      "source": "proc"
    },
    [...]
  ],
  "linux": {
    "resources": { "devices": [ { "allow": false, "access": "rwm" } ] },
    "namespaces": [
      { "type": "pid" },
      { "type": "network" },
      { "type": "ipc" },
      { "type": "uts" },
      { "type": "mount" }
    ],
    "maskedPaths": [
      "/proc/kcore",
      [...]
    ],
    "readonlyPaths": [
      "/proc/asound",
      [...]
    ]
  }
}
```

## Why Did Kubernetes Depreciate Docker?

Docker is often the first choice when it comes to managing and creating containers and images. It is extremely fast – so you might be wondering why Kubernetes dropped Docker and went on to use the CRI-O container engine? Let’s explore.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/0_jh4jUOjPPNS-bfU0.png)
_Source: https://www.sumologic.com/blog/kubernetes-vs-docker/_

We can check the Docker container engine like this:

```
$ systemctl status docker
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-41.png)

Here it shows Docker Application Container Engine but conntainerD is the actual engine running.

In Docker, when kubelet needs to connect to the ContainerD it has to go through an API Docker shim to contact runC. This acts as an interface between Docker and Kubernetes. This makes the whole process fairly complex.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-40.png)
_Source: Tutorial Works_

### What is ConatinerD?

ContainerD is an industry standard container runtime that emphasises simplicity, durability, and portability.

You can find a daemon-based implementation of containerD on both Linux and Windows. It is responsible for managing the whole container lifecycle of the system that it is hosted on, which includes image transfer and storage, container execution and monitoring, low-level storage, and network attachments.

#### Features of ContainerD:

* OCI Image Spec support
* Image push and pull support
* Network primitives for creation, modification, and deletion of interfaces
* Multi-tenant supported with CAS storage for global images
* OCI Runtime Spec support (aka runC)
* Container runtime and lifecycle support
* Management of network namespaces containers to join existing namespaces

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-42.png)

### What is dockerd?

Docker's daemon may be kicked off with the help of dockerd (so you can command the daemon to manage images, containers, and so on). Dockerd is a server that runs in the background as a daemon.

To run the Docker daemon we can specify dockerd. After the dockerd keyword, you should supply the daemon parameters you want to use. 

dockerd (Docker Daemon) can listen for Docker Engine API requests via three different types of Sockets: `unix`, `tcp`, and `fd`.

### Challenges of Using Docker

#### Overhead

Docker is a fairly developed platform in the container market. Along with container management, it offers many other capabilities like storage, security, and network infrastructure, among other things.

When compared to Cri-O and Podman, Docker's performance suffers as a direct result of the overhead caused by these additional functionalities. 

But Kubernetes and OpenShift come equipped with all of these functions. Therefore, they want only one thing from the container engine: the ability to launch and manage the containers. In other words, they do not need any other functions.

#### Dockershim

In Kubernetes, the process of launching containers begins when kubelet communicates with containerD, which then contacts runC.

Because separate businesses are responsible for the production of containerD and kubelet, kubelet must have an additional layer in order to contact containerD (an API like layer). And inside the Docker ecosystem, this layer is referred to as Dockershim.

Kubernetes had depreciated dockershim because of the complexities and burden created by Docker updates.

#### What's the issue with dockershim?

Kubernetes suggested a temporary solution to include support for Docker so that it could serve as its container runtime. Dockershim's deprecation just signifies that Dockershim's code will no longer be maintained in the Kubernetes source repository. 

Dockershim has become a significant problem for Kubernetes developers. Following this change, the Kubernetes community will only be permitted to maintain the Kubernetes Container Runtime Interface (CRI). 

Kubernetes supports all CRI-compliant runtimes, such as containerD and CRI-O.

Kubernetes has come up with CRI-O as its interface to contact with runC. Kubelet will now be contacting CRI-O. Further, it will contact the runC, and the container will be launched.

However, like CRI-O and Docker, there are many container engines present. So, the Kubernetes community decided to create an abstraction layer on top of all container engines. So, a client can use any container engine according to their requirements.

This abstraction layer is called CRI (container runtime interface).

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-44.png)
_Kubernetes using Docker vs Kubernetes using CRI-O_

### What is a CRI (Container Runtime Interface)?

The Kubelet program abstracts the underlying container engines. The Container Runtime Interface (CRI) is a plugin interface that lets kubelet use several container runtimes without recompilation. 

In addition to protocol buffers, the gRPC API, and libraries, other specifications and tools are in active development for CRI.

Kubelet establishes a connection with CRI over the gRPC Protocol.

### What is CRI-O?

CRI-OCI is an abbreviation that stands for the Container Runtime Interface and OCI, which stands for the Open Container Initiative.

The term CRI-O was chosen after taking into account references made by members of the CRI and CIO communities.

CRI-O is another container engine, but it is more lightweight than Docker since it does not include the additional capabilities that Docker has, such as networking, storage, and so on.

CRI-O provides a foundation that is more secure, stable, and performant for the execution of runtimes that are compatible with the Open Container Initiative (OCI). Runtimes that are OCI-compliant can be used in conjunction with the CRI-O container engine to launch containers and pods. 

Examples of such runtimes include runC, which is the default OCI runtime, and Kata Containers. But you can use any OCI-conformant runtime in its place. 

The goal of the CRI-O project is to replace Docker as the container engine that implements the Kubernetes Container Runtime Interface (CRI) for OpenShift Container Platform and Kubernetes.

The stability of CRI-O may be attributed to the fact that it is developed, tested, and distributed in tandem with major and minor versions of Kubernetes and complies with OCI standards. 

The O's in CRI-scope are reliant on the Container Runtime Interface (CRI). The actual container engine specifications of a Kubernetes service (kubelet) were compiled and specified by CRI. 

In light of the fact that several container engines were being developed, the CRI team decided to take this measure in order to settle Kubernetes' requirements for container engines.

According to the OpenShift Docs, the tools that help replace and extend what the Docker command and service provided are:

* crictl: For working directly with CRI-O container engines & troubleshooting
* runc: For running container images
* podman: For managing pods and container images (run, stop, start, ps, attach, exec, and so on) outside of the container engine
* buildah: For building, pushing and signing container images
* skopeo: For copying, inspecting, deleting, and signing images

### CRI-O Architecture

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-49.png)
_Source: cri-o.io_

## How to Build a Multi-Node Cluster using CRI-O

Following are the commands you'd use to create a multi-node Kubernetes cluster using CRI-O in Ubuntu 20.04.

Here's the repository that contains the set of commands: 

%[https://github.com/gursimarh/Kubernetes-CRIO/blob/main/commands]

```
OS=xUbuntu_20.04
VERSION=1.20

cat >>/etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list<<EOF
deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/ /
EOF

cat >>/etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.list<<EOF
deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/ /
EOF

curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/Release.key | apt-key --keyring /etc/apt/trusted.gpg.d/libcontainers.gpg add -

curl -L https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable:cri-o:$VERSION/$OS/Release.key | apt-key --keyring /etc/apt/trusted.gpg.d/libcontainers-cri-o.gpg add -

apt update

apt install -qq -y cri-o cri-o-runc cri-tools

systemctl daemon-reload

systemctl enable --now crio

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -


apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"

apt install -qq -y kubeadm=1.20.5-00 kubelet=1.20.5-00 kubectl=1.20.5-00

cat >>/etc/modules-load.d/crio.conf<<EOF
overlay
br_netfilter
EOF

modprobe overlay

modprobe br_netfilter

cat >>/etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
EOF

sysctl --system

cat >>/etc/crio/crio.conf.d/02-cgroup-manager.conf<<EOF
[crio.runtime]
conmon_cgroup = "pod"
cgroup_manager = "cgroupfs"
EOF

systemctl daemon-reload

systemctl enable --now crio

systemctl restart crio

sed -i '/swap/d' /etc/fstab

swapoff -a

systemctl disable --now ufw

kubeadm init --apiserver-advertise-address=172.16.16.100 --pod-network-cidr=192.168.0.0/16

kubectl --kubeconfig=/etc/kubernetes/admin.conf create -f https://docs.projectcalico.org/v3.18/manifests/calico.yaml

kubeadm token create --print-join-command

```

We can use the join command to connect the nodes to the cluster and we're ready with a multi-node cluster of Kubernetes.

### Here's an illustration of how Docker, Kubernetes, CRI-O, containerD and runC work together

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-43.png)

### Container Runtimes

We have seen a lot of details on how containers work, we have defined container runtimes and how we can build our custom container using runC. Now, are there any other tools in hand for us like runC?

Here we will look at landscape of all the container runtimes that are available.

Generally, they fall into two main categories: 

1. Open Container Initiative (OCI) runtimes

The OCI runtimes are further classified in two broader categories: Native Runtimes and Sandboxed & Virtualized Runtimes

2. Container Runtime Interface (CRI)

The CRI consists of containerD and CRI-O.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-47.png)
_1. Open Container Initiative (OCI) runtimes_

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-48.png)
_2. Container Runtime Interface (CRI)_

## Conclusion

Here we saw how we can build our custom images and the various tool available at our disposal. It was a long one but I hope you've enjoyed it and have learned something new.

I'm always open to suggestions and discussions on [LinkedIn](https://www.linkedin.com/in/gursimarh). Hit me up with direct messages.

If you've enjoyed my writing and want to keep me motivated, consider leaving starts on [GitHub](https://github.com/gursimarh) and endorse me for relevant skills on [LinkedIn](https://www.linkedin.com/in/gursimarh).

Till the next one, stay safe and keep learning.

