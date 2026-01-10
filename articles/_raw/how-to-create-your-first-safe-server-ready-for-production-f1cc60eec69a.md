---
title: How to create your first safe server that’s ready for production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-09T12:29:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-first-safe-server-ready-for-production-f1cc60eec69a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rka-cGjoHmoOpLLNz8ANbA.jpeg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Flavio H. Freitas

  In this tutorial, I will present some of the best practices to build your own first
  safe server. I’ll list the steps you’ll need to take to have a fully functional
  server that you can use in production for your app.

  Having a safe...'
---

By Flavio H. Freitas

In this tutorial, I will present some of the best practices to build your own first **safe server**. I’ll list the steps you’ll need to take to have a fully functional server that you can use in **production** for your app.

Having a safe server doesn't just rely on following some steps. It's a constant search for new resources and never-ending improvement. But this article can be a step 0 in building your own infrastructure.

I will use Amazon EC2 to run these tests, but I’ve also used Amazon LightSail, Digital Ocean, Vultr and some others. In all cases, they were the same to configure, so you can use the provider you prefer.

![Image](https://cdn-media-1.freecodecamp.org/images/oc74KOmG7JQiUS3NJ4fHjNM8S6BoKZLeyExz)
_Let's make it safe!_

So let's go:

### Creating public and private SSH keys

Before starting, let's create a pair of keys that some hosts ask for during installation of the server. This step and the next can be omitted if you decide to create a pair of keys while launching a machine instance with Amazon.

Create an SSH key pair using the ssh-keygen tool.

```
$ ssh-keygen -t rsa -b 4096
```

After this step, you will have the following files: id_rsa and id_rsa.pub (private and public keys). **Never** share your private key.

A more detailed document on creating the keys can be found [here](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

### Import the public key on Amazon:

We will import the public key that we just created on the Amazon platform.

1. Access [Amazon Management Console](https://us-west-2.console.aws.amazon.com/console/home)
2. Click on AWS services > Compute > EC2
3. Click on the left menu Network & Security > Key Pairs
4. Click on "Import Key Pair" and upload your public key (id_rsa.pub)

### **Create your machine**

I will install an Ubuntu version on Amazon EC2. You can find a complete setup at this [link](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine). The steps are as follows (but just for simplicity, follow this [link](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine) for more explanation):

1. Access [Amazon Management Console](https://us-west-2.console.aws.amazon.com/console/home)
2. Click on AWS services > Compute > EC2
3. Choose Launch Instance
4. Choose one of the images. I chose Ubuntu Server 16.04 LTS (HVM), SSD Volume Type (but choose accordingly to your needs)
5. Choose the instance (again, according to your needs). Click Review and Launch
6. Open a new tab and import the created public key on Amazon.
7. Here we are asked to "Select an existing key pair or create a new key pair". I chose "Choose an existing key pair". Choose the one you uploaded in the previous step.
8. Click "Launch Instances".
9. Click on the link of the instance you just created.

Attention: Some of the steps bellow could be configured on this initial screen of Amazon. But since I want to create a generic tutorial that can be used for other hosts, I chose the default configurations.

### Connect to the new server

Access the machine with ssh.

Type on your terminal:

```
$ ssh <USER>@<IP-ADDRESS> -p 22 -i <PATH-TO-PRIVATE-KEY>
```

* <USER>: The user on the Linux system. For Amazon use ubuntu, for others, root
* <IP-ADDRESS> : The IP address of the machine you created. It is the field "Public DNS (IPv4)" on the tab "Description" of your instance.
* <PATH-TO-PRIVATE-KEY> : The full path to the private key you generated on the item before (e.g. /Users/flavio/.ssh/id_rsa).
* -i <PATH-TO-PRIVATE-KEY> : this part can be omitted if you added the key to your SSH agent.

### Give your new user access

Create a new user account named “wizard”

```
$ sudo adduser wizard
```

Give “wizard” the permission to sudo. Open the file

```
$ sudo nano /etc/sudoers.d/wizard
```

And set the content:

```
wizard ALL=(ALL) NOPASSWD:ALL
```

Create the following directories:

```
$ mkdir /home/wizard/.ssh# create authorized_keys file and copy your public key here$ nano /home/wizard/.ssh/authorized_keys$ chown wizard /home/wizard/.ssh$ chown wizard /home/wizard/.ssh/authorized_keys
```

Copy the content of the public key (PATH-TO-PUBLIC-KEY) and paste on the remote instance on the /home/wizard/.ssh/authorized_keys . Set the permissions:

```
$ chmod 700 /home/wizard/.ssh$ chmod 600 /home/wizard/.ssh/authorized_keys
```

### Securing the System

Update all currently installed packages.

```
$ sudo apt-get update$ sudo apt-get upgrade
```

Change the SSH port from 22 to 2201. Configure the firewall (ufw, Uncomplicated Firewall, and it is really uncomplicated) to allow it. Open the file /etc/ssh/sshd_config

```
$ sudo nano /etc/ssh/sshd_config
```

and change the following data:

```
Port 2201PermitRootLogin noPasswordAuthentication no
```

```
# add this to avoid problem with multiple sshd processesClientAliveInterval 600ClientAliveCountMax 3
```

Restart the ssh service:

```
$ sudo service ssh restart
```

Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2201), HTTP (port 80), and NTP (port 123).

```
# close all incoming ports$ sudo ufw default deny incoming# open all outgoing ports$ sudo ufw default allow outgoing# open ssh port$ sudo ufw allow 2201/tcp# open http port$ sudo ufw allow 80/tcp# open ntp port : to sync the clock of your machine$ sudo ufw allow 123/udp# turn on firewall$ sudo ufw enable
```

### Configure your server clock

Configure the local timezone to UTC:

```
$ sudo dpkg-reconfigure tzdata
```

Choose the option ‘None of the Above’ and then select UTC.

### Disconnect and Add your key to your SSH agent

Disconnect from your server and make the following on your machine. To disconnect:

```
$ exit
```

### Add Access Port Permission on Amazon

This step is required on Amazon. We will set the ssh port that we want to use on Amazon also.

1. Access [Amazon Management Console](https://us-west-2.console.aws.amazon.com/console/home)
2. Click on AWS services > Compute > EC2
3. Click on the left menu Network & Security >Security Groups
4. Choose the one that is attached to your instance
5. Click on Action > Edit Inbound Rules
6. Click on "Add Rule" and set: Type: Custom TCP, Port Range: 2201, Source: 0.0.0.0/0 and Description: SSH

### Connect with the new credentials

Now you can connect on the machine with the user on the new port.

```
$ ssh wizard@<IP-ADDRESS> -p 2201 -i <PATH-TO-PRIVATE-KEY>
```

You have a server ready to run your application. Soon I will write another tutorial on how to install an environment to run your Meteor application using pm2. I’ll also discuss configuring SSL, a reverse proxy, a load balancer and Nginx. But this article showed how to make a generic safer server that you can run whatever you need.

If you enjoyed this article, be sure to like it give me a lot of claps — it means the world to the writer ? And f[ollow me](https://medium.com/@flaviohfreitas) if you want to read more articles about Culture, Technology, and Startups.

**Flávio H. de Freitas** is an Entrepreneur, Engineer, Tech lover, Dreamer and Traveler. Has worked as **CTO** in **Brazil**, **Silicon Valley and Europe**.

Photo by [Ben White](https://unsplash.com/photos/1MHU3zpTvro?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

