---
title: How to setup log rotation for a Docker container
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T22:50:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-log-rotation-for-a-docker-container-a508093912b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_q2gpmanaKPIhoScKtgt1Q.png
tags:
- name: debugging
  slug: debugging
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ying Kit Yuen

  We all need logs!

  Sometimes working with Docker makes me feel like I’m working with a black box. Especially
  when I’m playing with Docker images from the community, and it doesn’t go the way
  I expected. In many cases, reading logs tak...'
---

By Ying Kit Yuen

#### We all need logs!

Sometimes working with [Docker](https://www.docker.com/) makes me feel like I’m working with a black box. Especially when I’m playing with Docker images from the community, and it doesn’t go the way I expected. In many cases, reading logs takes up a large portion of time when debugging.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PdclvVxyj07MQ_Fn8nJPYw.jpeg)

This article is about setting up log rotation for Docker containers.

### The default logging driver

We can configure different logging drivers for containers. By default, the **stdout** and **stderr** of the container are written in a JSON file located in _/var/lib/docker/containers/[container-id]/[container-id]-json.log_. If you leave it unattended, it can take up a large amount of disk space, as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2e9iGLyDCm5_WNfxl0_KAQ.jpeg)
_A large log file in json format_

#### Purge the log manually

If this JSON log file takes up a significant amount of the disk, we can purge it using the following command.

We could setup a cronjob to purge these JSON log files regularly. But for the long term, it would be better to setup log rotation.

### Setup the log rotation

#### Configure the default logging driver

This can be done by adding the following values in _/etc/docker/daemon.json_. Create this file if it doesn’t exist.

The _json-file_ logging driver has a few more options, and we can even change to other logging drivers such as _syslog_. For more information, please refer to the [Docker Docs — Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/).

Execute the following commands to reload the updated _daemon.json_. The new configuration will apply to all newly created containers after restart.

#### Configure the logging driver for a container

The configuration can also be done on the container level if you do not want to apply it globally.

**The docker run command**

We can specify the logging driver and options in the _docker run_ command. For example:

**Using docker-compose**

The logging driver and options can also be configured using docker-compose. For example:

Verify if the setup is working.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Pl6ERkWFB4HBZ9fVNvtsw.jpeg)
_The logs are broken down into 1k files_

### Summary

Although the default settings work fine, you never know when the container logs take up all the disk space. This can be avoided by the few steps discussed above. Other than that, logs are an important asset. They are not only useful when something goes wrong, but they also contain a lot of hidden value. So never let the logs go.

If you are looking for a **log management SAAS solution**, consider using [Boatswain](https://boatswain.io/). We will help you manage all the logs and monitor your [Docker](https://www.docker.com/) servers. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*wU51pWBThLTG2ngSYcE7lA.jpeg)
_Insufficient facts always invite danger_

— Originally posted on [Boatswain Blog](https://blog.boatswain.io/post/docker-container-log-rotation/).

