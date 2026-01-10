---
title: What is Ansible? A Tool to Automate Parts of Your Job
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2021-10-29T20:42:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-ansible
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/ansble.png
tags:
- name: ansible
  slug: ansible
- name: automation
  slug: automation
seo_title: null
seo_desc: 'Hello everyone, today we will talk about Ansible, a fantastic software
  tool that allows you to automate cross-platform computer support in a simple but
  effective way.

  Table of Contents


  What is Ansible?

  How Does Ansible Work?

  Ansible''s Architecture

  P...'
---

Hello everyone, today we will talk about Ansible, a fantastic software tool that allows you to automate cross-platform computer support in a simple but effective way.

## Table of Contents

- What is Ansible?
- How Does Ansible Work?
- Ansible's Architecture
  - Plugins
  - Modules
  - Inventories
  - Playbook
- Benefits of Using Ansible
- Why is Ansible so important?
- How to Install and Configure Ansible on Ubuntu
- Conclusion
- References


## What is Ansible?

Ansible is a tool that generates written instructions for automating IT professionals' work throughout the entire system infrastructure.

It's designed particularly for IT professionals who use it for application deployment, configuration management, intra-service orchestration, and practically anything else a systems administrator does on a weekly or daily basis. 

Ansible is simple to install because it doesn't require any agent software or other security infrastructure.

While Ansible is at the cutting edge of automation, systems administration, and DevOps, it's also valuable as a tool for devs to use in their daily work. 

Ansible allows you to set up not just one machine but a complete network of them all at once, and it doesn't require any programming knowledge.

## How Does Ansible Work?

Ansible connects to nodes on a network (clients, servers, etc.) and then send a little program called an Ansible module to each node. 

It then runs these modules through SSH and deletes them once they're done. 

Your Ansible control node must have login access to the managed nodes for this interaction to work. 

The most frequent method of authentication is SSH keys, but alternative methods are also allowed.

If you want to see how to install and start using Ansible, we'll cover that below.

## Ansible's Architecture

Now let's take a look at Ansible's architecture and how it manages operations.

### Ansible Plugins

Plugins are supplementary pieces of code that enhance functionality, and you've probably used them in many other tools and platforms. You can use Ansible's built-in plugins or create your own. 

Examples are: 

- Action Plugins
- Become Plugins
- Cache Plugins
- Callback Plugins
- Cliconf Plugins
- Connection Plugins
- HTTP API Plugins
- Inventory Plugins
- Lookup Plugins
- Netconf Plugins
- Tests

### Ansible Modules

Modules are short programs that Ansible distributes to all nodes or remote hosts from a central control workstation. Modules control things like services and packages and can be executed via playbooks. 

Ansible runs all of the modules needed to install updates or complete whatever operation is required and then removes them after they're done.


### Ansible Inventories

Ansible uses an inventory file to track which hosts are part of your infrastructure and then accesses them to perform commands and playbooks.

Ansible works in parallel with various systems in your infrastructure. It accomplishes this by picking methods mentioned in Ansible's inventory file, which is saved in the host location by default.

Once the inventory is registered, you can use a simple text file to assign variables to any of the hosts, and you may retrieve inventory from a variety of sources. 


### Ansible Playbook

IT professionals can use Ansible playbooks to program applications, services, server nodes, and other devices without starting from scratch. Ansible playbooks, along with the conditions, variables, and tasks included within them, can be stored, shared, and reused forever.

Ansible playbooks function similarly to task manuals. They're simple [YAML](https://en.wikipedia.org/wiki/YAML) files, a human-readable data serialization language. 

Playbooks are at the heart of what makes Ansible so popular. They specify activities that can be completed quickly without requiring the user to know or remember any specific syntax.


## Benefits of Using Ansible

-  Ansible is quick and easy to use, as it runs all of its operations over SSH and doesn't require the installation of any agents.
-  Ansible is a free, open-source tool, and it's straightforward to set up and use: Ansible's playbooks don't require any special coding knowledge.
-  Ansible can be used to perform simple tasks such as ensuring that a service is operating or rebooting from the command line without the need for configuration files.

In a more extensive or more uniform system, Ansible may be a better fit. It also provides a set of modules for managing various methods and cloud infrastructure.

## Why is Ansible so important?

Modernization and digital transformation require automation that's both necessary and purposeful. We need a new management solution in today's dynamic contexts to increase speed, scale, and stability throughout IT infrastructure.

Technology is our most potent instrument for product improvement. Previously, accomplishing this required a significant amount of manual labor and intricate coordination. But today, Ansible - a simple yet powerful IT automation engine used by thousands of enterprises to simplify their setups and speed DevOps operations - is available.

## How to Install Ansible on Ubuntu

Run the following commands to configure the PPA on your machine and install Ansible:

Update the repository:

```
sudo apt-get update
```

Install the software properties:

```
sudo apt-get install software-properties-common
```

And then install Ansible like this:

```
sudo apt-add-repository --yes --update ppa:ansible/ansible
```

Then run this:

```
sudo apt-get install ansible
```

You should have something similar to what is shown below:

![ansible_installation](https://www.freecodecamp.org/news/content/images/2021/10/ansible_installation.png)

Now that you have successfully installed Ansible, let's test if it's working by using the command below:

```
ansible --version
```

![ansible_check](https://www.freecodecamp.org/news/content/images/2021/10/ansible_check.png)


We'll use the command below to instruct Ansible to target all systems for the inventory host localhost, and we'll run the module ping from your local console (rather than ssh).

```
ansible all -i localhost, --connection=local -m ping
```

You should get a response similar to what you can see below:

![ansible_ping](https://www.freecodecamp.org/news/content/images/2021/10/ansible_ping.png)

### How to modify the hosts that Ansible targets

We'll make changes to the host's file in `/etc/ansible/hosts`. This is the default file where Ansible searches for any defined hosts (and groups) where the given commands should be executed remotely.

```
sudo nano /etc/ansible/hosts
```

Add the lines below to the file and save the modifications:

```
[local]
localhost
```

Execute this command with your adjusted inventory file:

```
ansible all --connection=local -m ping
```

The response should look similar to what we have below:

![ansible_pong](https://www.freecodecamp.org/news/content/images/2021/10/ansible_pong.png)

### How to configure a remote server

We deploy our Ansible test program to our remote server using a Digital Ocean droplet.

Use the command below to ssh into the server:

```
ssh username@IP_Address
```

> Note: we have already configured an ssh key in our profile, which was selected when creating the droplet.

![ansible_server](https://www.freecodecamp.org/news/content/images/2021/10/ansible_server.png)

### How to configure Ansible for a remote server

We will edit our hosts file in /etc/ansible/hosts using the command below:

```
sudo nano /etc/ansible/hosts
```

Add the lines below to the file and save the modifications:

```
[remote]
remote_test

[remote:vars]
ansible_host=IP_ADDRESS_OF_VIRTUAL_MACHINE
ansible_user=USERNAME
```

To see if Ansible can connect to your remote compute instance over SSH, let's type the following command:

```
ansible remote -m ping
```

![asnible_result](https://www.freecodecamp.org/news/content/images/2021/10/asnible_result.png)

We'll make an Ansible playbook using the command below, which is the typical way of telling Ansible which commands to run on the remote server and in what order. The playbook is written in .yml and follows a strict format. 

In the official [Ansible documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html), you can learn more about playbooks.

```
nano my-playbook.yml
```

Add the following code, which tells Ansible to install Docker in several steps:

```
---
- name: install docker
hosts: remote
become_method: sudo
become_user: root
vars: #local variables
docker_packages:
- apt-transport-https
- ca-certificates
- curl
- software-properties-common

tasks:
- name: Update apt packages
become: true #make sure you execute the task with sudo privileges
apt: #use apt module
update_cache: yes #equivalent of apt-get update

- name: Install packages needed for Docker
become: true
apt:
name: "{{ docker_packages }}" #uses our declared variable docker_packages
state: present #indicates the desired package state
force_apt_get: yes #forces to use apt-get

- name: Add official GPG key of Docker
shell: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

- name: Save the current Ubuntu release version into a variable
shell: lsb_release -cs
register: ubuntu_version #Output gets stored in this variable

- name: Set right Docker directory
become: true
shell: add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ubuntu_version.stdout }} stable"

- name: Update apt packages
become: true
apt:
update_cache: yes

- name: Install Docker
become: true
apt:
name: docker-ce
state: present
force_apt_get: yes

- name: Test Docker with hello world example
become: true
shell: docker run hello-world
register: hello_world_output

- name: Show output of hello word example
debug: #use debug module
msg: "Container Output: {{hello_world_output.stdout}}"
```

We can now execute it with the command below:

```
ansible-playbook my-playbook.yml -l remote
```

After that, we'll see some magic happen (it might take a while), and somewhere in the last debug message in our terminal, we should see "Hello from Docker!"

## Conclusion

In this article, we had a detailed look into Ansible, its benefits, how it works and what it can do, its architecture, plugins, playbook, inventory, and how to configure and deploy Docker with Ansible on a remote server.

Thank you for reading!


## Resources

[Ansible docs](https://docs.ansible.com/)
[Setting up Ansible Inventories](https://www.digitalocean.com/community/tutorials/how-to-set-up-ansible-inventories)
[Ansible installation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)


I'd love to connect with you on [Twitter](https://twitter.com/olanetsoft) | [LinkedIn](https://www.linkedin.com/in/olubisi-idris-ayinde-05727b17a/) | [GitHub](https://github.com/Olanetsoft)



