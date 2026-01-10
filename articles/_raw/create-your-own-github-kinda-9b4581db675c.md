---
title: Create your own GitHub (kinda)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-24T14:45:18.000Z'
originalURL: https://freecodecamp.org/news/create-your-own-github-kinda-9b4581db675c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BCZkmZR1_YzDZy22Vn4uUw.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Shashank Sharma

  In order to do any collaboration in Git, you’ll need to have a remote Git repository.
  Let’s cover step by step how you can create a Git server on an AWS EC2 instance.

  First, let’s cover some of the basics.

  Bare vs Non-bare reposito...'
---

By Shashank Sharma

In order to do any collaboration in Git, you’ll need to have a remote Git repository. Let’s cover step by step how you can create a Git server on an AWS EC2 instance.

First, let’s cover some of the basics.

#### Bare vs Non-bare repository

A git repository that has no working directory is called a “bare” repository. A “**bare**” **repository** in Git just contains the version control information and no working files (no tree). It doesn’t contain the special .git sub-directory. Instead, it contains all the contents of the .git sub-directory directly in the main directory itself.

```
Create: git init --bare
```

```
Clone: git clone --bare $URL
```

**Non-bare repository** has a checked-out working tree with .git sub-directory.

```
Create: git init
```

```
Clone: git clone $URL
```

You should use a non-bare repository to work locally and a bare repository as a central server/hub to share your changes with other people. For example, when you create a repository on github.com, it is created as a bare repository.

Bare repositories are smaller than non-bare repositories. As bare repository do not have working copy, any changes pushed to them won’t cause conflicts. Bare repository by convention uses names with the .git postfix.

#### The Protocols

Git can use four major protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.

1. _Local Protocol:_ the most basic protocol, where the remote repository can reside on any shared mounted disk. You can clone a local repository like this:

```
git clone /var/local/repository
```

2. _HTTP protocol:_ This runs over standard HTTP/S ports. It can use things like username/password basic authentication rather than having to set up SSH keys. If you use this, you can use the same URL to view or clone the repository, like with Github.

3. _SSH protocol:_ This is the most common transport protocol for Git when self-hosting. This is because SSH access to servers is already set up in most places — and if it isn’t, it’s relatively straight-forward to do.

4. _Git protocol:_ The Git protocol is often the fastest network transfer protocol available. This is a special daemon that comes packaged with Git. It listens on a dedicated port (9418) that provides a service similar to the SSH protocol, but with absolutely no authentication.

In depth explanation of these protocols is beyond the scope of this article. For more details, you can check [https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols](https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols).

#### Setting up Git server on an EC2 instance

Now lets start get started with the reason you’re here — to set up a Git server. If you haven’t already set up an EC2 instance with SSH access, follow [this guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) to create one.

I am using an Ubuntu t2.micro instance for this exercise.

a) Login to your EC2 instance using SSH.

```
-> ssh -i ~/.certs/cert.pem ubuntu@54.254.174.183
```

b) Install Git.

```
-> sudo apt-get install git
```

c) Create a bare repository which will be your remote Git repository.

```
-> mkdir gitserverexcersise.git-> cd gitserverexcersise.git-> git init --bare
```

This will create your bare empty repository. At this point of time you already have a Git repository ready to be cloned. But to clone this from your local system, you need to add your pem file to your ssh config.

d) Open another terminal and add this instance to SSH config. You can find SSH config file in home directory .ssh folder. If you don’t have this folder you can create one. And edit or create config file in preferable text editor.

```
-> vi .ssh/config
```

Add entry for your instance like

```
 Host gitserver HostName 54.254.174.183 User ubuntu IdentityFile ~/.certs/cert.pem
```

And save.

e) Close this terminal and open new terminal. Now you should be able to login to ec2 instance using

```
-> ssh gitserver
```

If you able to login then you can clone your repository to your local system using:

```
-> git clone gitserver:gitserverexcersise.git
```

Congratulations! You have successfully setup a remote Git server and now can push and pull to that server.

#### Setting up GitWeb

Now that you have basic read/write and read-only access to your project, you may want to set up a simple web-based visualizer. Git comes with a CGI script called GitWeb that is sometimes used for this. Follow below steps to setup GitWeb.

a. Login to your EC2 instance

```
-> ssh gitserver
```

b) Install apache2

```
-> sudo apt-get update-> sudo apt-get install apache2
```

c) Install “make” as will be required for next step

```
-> sudo apt-get install make
```

d) We will get the Git source code, which GitWeb comes with, and generate the custom CGI script:

```
-> git clone git://git.kernel.org/pub/scm/git/git.git-> cd git-> make GITWEB_PROJECTROOT=”/home/ubuntu” prefix=/usr gitweb-> sudo cp -Rf gitweb /var/www/
```

GITWEB_PROJECTROOT is the location of your Git repositories.

e) Add VirtualHost for Apache

```
-> cd /etc/apache2/sites-enabled/
```

Update conf (000-default.conf) to

```
<VirtualHost *:80>      DocumentRoot /var/www/gitweb      <Directory /var/www/gitweb>            Options +ExecCGI +FollowSymLinks +SymLinksIfOwnerMatch            AllowOverride All            order allow,deny            Allow from all            AddHandler cgi-script cgi            DirectoryIndex gitweb.cgi      </Directory&gt;</VirtualHost>
```

f) Load the mod_cgi module

```
-> sudo a2enmod cgi
```

g) Restart apache

```
-> sudo service apache2 restart
```

Congratulations! GitWeb is ready. Before you able to access the GitWeb on [http://54.254.174.183](http://54.254.174.183)/ (For you, it would be your instance’s public URL), there’s one last thing you need to do: allow TCP port 80 to open for your instance. You can do this by [changing your security group setting](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html) for your instance.

If all of this seems too complicated for you, you can go with other alternatives like [GitLab](https://about.gitlab.com/). GitLab is a database-backed web application, so its installation is a bit more involved than some other git servers. Fortunately, this process is very well-documented and supported.

_If you liked the article and helped you setting up Git server, hit the heart down there and help others see it. Follow me for other such articles._

