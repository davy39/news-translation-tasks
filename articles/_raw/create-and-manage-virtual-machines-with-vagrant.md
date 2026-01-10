---
title: How to Create and Manage Virtual Machines with the Vagrant Command Line Tool
subtitle: ''
author: Eti Ijeoma
co_authors: []
series: null
date: '2023-04-03T20:15:11.000Z'
originalURL: https://freecodecamp.org/news/create-and-manage-virtual-machines-with-vagrant
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-01-at-23.42.01-1.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: virtual machine
  slug: virtual-machine
seo_title: null
seo_desc: 'Creating and managing virtual machines used to be a tedious and time-consuming
  process. Replicating the VM on a different server can also be challenging, and it
  gets harder if you have to replicate multiple VMs.

  But then Vagrant came along, a command...'
---

Creating and managing virtual machines used to be a tedious and time-consuming process. Replicating the VM on a different server can also be challenging, and it gets harder if you have to replicate multiple VMs.

But then Vagrant came along, a command-line or shell tool that generally works with [Type 2 hypervisors](https://en.wikipedia.org/wiki/Hypervisor#:~:text=Type%2D2%20or%20hosted%20hypervisors). You use it to create and manage virtual machines. It is a powerful tool that can help simplify the setup and management of your development environment.

Vagrant can be really helpful if you work on a team or with multiple people. This is because it guarantees consistency in your development environment by ensuring that everyone utilizes the same environment, preventing compatibility issues.

This tutorial will guide you through the process of setting up a single Ubuntu Linux virtual machine with Vagrant and configuring a web server inside it.

### Prerequisites for this tutorial include:

* A computer with at least 8GB of RAM
    
* Basic knowledge of the Linux operating system
    

### Required Tools and Installation

* **Oracle VirtualBox:** Go to the [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads) website, find the version of VirtualBox that is compatible with your operating system, and follow the instructions to download and install it. Virtual Box will provide the virtual environment, while Vagrant will set it up and manage it.
    
* **Vagrant:** Visit the [Vagrant website](https://www.vagrantup.com/) and follow the instructions to download and install the binary that is suitable for your operating system. In this tutorial, we'll be utilizing the open-source Vagrant binary.
    

To check if the installation was successful, launch your preferred command line tool and enter the following command to output the installed version number:

```bash
$ vagrant --version
```

## How to Create a Development Environment with Vagrant

To create a Vagrant project, start by creating a new project directory in your preferred location for Vagrant configuration and related files.

```bash
$ mkdir vagrant-project && cd vagrant-project
```

Within this directory, create a new Vagrantfile. Vagrant uses the configuration in the Vagrantfile to build the VM. By default, Vagrant syncs the project directory where the Vagrantfile is initialized to /vagrant. This eliminates the need to worry about volumes for persisting data.

Vagrant uses the concept of boxes. Boxes are a complete base image of an operating system. The public [vagrant box repository](https://app.vagrantup.com/boxes/search) contains a list of possible boxes. Choosing a box that matches the operating system used in your production environment is good practice.

A Vagrant box has the name of the user or organization that created it and the box name `user/boxname`. To initialize the Vagrant configuration file with an Ubuntu box, run the command:

```bash
$ vagrant init ubuntu/trusty64
```

This generates a Vagrantfile with a Ubuntu/trusty64 box in the current directory. The Vagrantfile, which is written in Ruby, contains the kind of VM to be used and various additional commented options such as network, port forwarding, disc capacity, and so on to assist in configuring the development environment.

You can add the `--minimal` flag to the initialization command of the Vagrantfile to generate a Vagrantfile without any additional settings.

Open the Vagrantfile with any editor of your choice. I will use the Vim editor in this tutorial.

```bash
 $ vim Vagrantfile
```

Removing the informational comments and some advanced configurations will leave the file like this:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.provider "virtualbox" do |vb| vb.memory = "1024"
 end
  config.vm.provision :shell, path: "simple-node-project.sh", privileged: false
end
```

The `simple-node-project.sh` is a bash script that installs Node.js and Git, clones a project that creates a simple Node.js web server, and starts the server.

```bash
#!/bin/bash

 sudo apt-get update -y

 ## Git ##
 echo '###Installing Git..'
 sudo apt-get install git -y

 git clone https://github.com/Aijeyomah/simple-node-app.git

# Installing latest Node and npm version
 sudo apt-get install -y curl software-properties-common

# Add Node.js PPA
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

# Install Node.js and npm
sudo apt-get install -y nodejs

# Verify installation
node -v
npm -v

echo "Node.js has been installed successfully."

# navigate to app directory and start app
cd simple-node-app
node index.js &
```

This Vagrant configuration sets up the following:

* `ubuntu/trusty64` is specified as the virtual box base image
    
* Forwards port 8000 of the VM to port 8000 of the host machine.
    
* Allocates 1GB of memory to the VM
    
* Runs `simple-node-project` to provision the VM
    
* For the shell provisioner to run the script as a non-root user in a login shell, `privileged` is set to `false`
    

Save the `Vagrantfile` and start the virtual machine by running the following command:

```bash
$ vagrant up
```

The first time this command is run, it will download the latest version of the specified box, and it will configure and start the VM. This process might take some time, but when the Ubuntu box exists in the local machine the VM will start immediately.

Once the VM is running, you can access the web page by opening a web browser and navigating to [`http://localhost:8000`](http://localhost:8080). You should see the `Hello World` message page if everything was set up correctly.

## How to Manage Vagrant

You can use Vagrant to manage the running virtual machine. Here are some useful Vagrant commands:

`vagrant up`: Launches the virtual machine and provisions it according to the settings in the Vagrantfile. This command will simply connect to the virtual machine if it is already running.

`vagrant halt`: Stops the virtual machine by delivering a shutdown signal to the guest operating system. This command is similar to shutting down a real computer.

`vagrant reload`: Restarts the virtual machine and re-provisions it depending on any changes in the Vagrantfile.

`vagrant ssh`: Connects to the virtual machine via SSH. This command is useful for accessing the command line interface of the virtual machine.

`vagrant status`: Shows the current status of the virtual machine, including whether it's running, stopped, or suspended.

`vagrant destroy`: Deletes the virtual machine and all associated resources. This command is useful for cleaning up your development environment.

## Conclusion

In this article, we have learned how to utilize Vagrant to set up a reproducible and consistent development environment.

Using Vagrant can help you set up a virtual development environment that closely mimics your production environment. This allows you to test and develop your code in a consistent and isolated environment.
