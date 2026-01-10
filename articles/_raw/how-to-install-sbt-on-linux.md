---
title: How to install sbt on Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-15T03:46:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-sbt-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/sbt-1.png
tags:
- name: coding
  slug: coding
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sanjula Madurapperuma

  Introduction

  Hi! I am Sanjula, and in this guide I hope to teach you how to install sbt on Linux.

  Let’s get started!

  What is sbt?

  sbt is an open-source, cross-platform build tool for Scala and Java projects.

  Some of its main ...'
---

By Sanjula Madurapperuma

### Introduction

Hi! I am [Sanjula](https://www.linkedin.com/in/sanjula-madurapperuma/), and in this guide I hope to teach you how to install sbt on Linux.

Let’s get started!

### What is sbt?

sbt is an open-source, cross-platform build tool for Scala and Java projects.

Some of its main features are:

* Support for continuous compilation, testing and deployment.
* Native support for compiling Scala code.
* Dependency management using Ivy.
* Ability to build descriptions written in Scala using a DSL (Domain-Specific Language).

### Steps to install sbt

* First you have to make sure that a JDK is installed. sbt recommends the Oracle JDK 8 or OpenJDK 8.
* Open up a terminal and type in the following command, which will point to the debian distribution of sbt and add sbt to the sources list.

```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*KgNADEh4KyRZf98H4d0T4g.png)
_Figure-2: Adding sbt URL to sources list_

* Next, enter the command below, which adds the key of scala to the key list used by apt to authenticate packages.

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JNJINkN6aWH64wi7aIyBsw.png)
_Figure-3: Adding sbt to key list used by apt_

* Now download the package lists from the repositories to ensure that the list of information on the newest version of packages and their dependencies are updated locally.sudo apt-get update
* Finally run the following command to install sbt.sudo apt-get install sbt

![Image](https://cdn-media-1.freecodecamp.org/images/1*R8eFHroAfiqfwjLTbwB4kQ.png)
_Figure-4: I already have sbt installed :)_

**Congratulations!!!** You have now installed the sbt build tool on your Linux PC! Now you can easily work with Scala and Java projects.

**In the meantime, you** can share **this article if you liked it, or c**ontact me **for any concerns. Also please checkout my profile at** [**LinkedIn**](https://www.linkedin.com/in/sanjula-madurapperuma/) **and follow me on** T**witter****!**

