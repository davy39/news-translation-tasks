---
title: Using Kubernetes to deploy a chat gateway (or when technology works like it’s
  supposed to)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T10:40:51.000Z'
originalURL: https://freecodecamp.org/news/using-kubernetes-to-deploy-a-chat-gateway-or-when-technology-works-like-its-supposed-to-a169a8cd69a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZsohwEQHHw_sh0KX37pdeg.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Richard Li

  TL;DR

  This is a story about what happens when cloud technologies work like they’re supposed
  to. In this case, the technologies are Docker and Kubernetes.

  Introduction

  At Datawire, we use Gitter so that users of our open source tools can...'
---

By Richard Li

### TL;DR

This is a story about what happens when cloud technologies work like they’re supposed to. In this case, the technologies are Docker and Kubernetes.

### Introduction

At [Datawire](https://www.datawire.io), we use [Gitter](http://gitter.im) so that users of our open source tools can chat with us (and each other). We like Gitter because it’s low friction to join, especially if you have a GitHub or Twitter account. However, Gitter’s mobile client isn’t great, and the notifications in general don’t work well.

Since migrating a community of users is a fair bit of work, I decided to see if I could deploy a bridge between Slack (what we use internally) and our Gitter chat. A little bit of Googling led me to [Matterbridge](https://github.com/42wim/matterbridge).

In the rest of the article, I’ll walk through how Docker and Kubernetes actually made my life easier, and why. I found the amount of [yak shaving](https://en.wiktionary.org/wiki/yak_shaving) required to be remarkably small … which made me really appreciate how far we’ve come in the cloud world.

### Docker is great

I wanted to run Matterbridge locally to debug the configuration. I followed the general instructions on creating accounts for Slack and Gitter, and then put the necessary authentication tokens into a `matterbridge.toml` file.

I was happy to see how Matterbridge is available as a Docker image, so I was able to just copy my configuration file into the Docker image to test out the configuration. All I needed to do was to specify my configuration file when using `docker run`:

```
docker run -ti -v /tmp/matterbridge.toml:/matterbridge.toml 42wim/matterbridge
```

I had to make a few turns of this to debug my configuration, but it was quick and easy. The Docker image did exactly what it’s supposed to do: provide a tested runtime environment for Matterbridge so I didn’t have to debug it on my laptop.

### Running in the cloud

The next step was to deploy my configuration to the cloud. We already run a production Kubernetes cluster fronted by an [API Gateway](https://www.getambassador.io) powered by [Envoy](https://www.datawire.io/envoyproxy/), so I wanted to deploy the service into its own namespace.

To deploy to Kubernetes, I wrote a simple Dockerfile:

```
FROM 42wim/matterbridge:1.9.0ADD matterbridge.toml .CMD ["/bin/matterbridge"]
```

Then, all I needed was a Kubernetes manifest.

### Kubernetes

In my Kubernetes manifest, I’m able to specify a bunch of key information about the service:

* My update strategy, `RollingUpdate`
* The minimum and maximum amount of CPU and memory to allocate
* The number of replicas of the service

Here is my basic manifest:

```
---apiVersion: apps/v1beta1kind: Deploymentmetadata:  name: {{build.name}}  namespace: {{service.namespace}}spec:  replicas: 1  strategy:    type: RollingUpdate  template:    metadata:      labels:        app: {{build.name}}    spec:      containers:      - name: {{build.name}}        image: {{build.images["Dockerfile"]}}        imagePullPolicy: IfNotPresent        resources:          requests:            memory: 0.1G            cpu: 0.1          limits:            memory: {{service.max_memory}}            cpu: {{service.max_cpu}}    
```

(Note that I’m using [Forge](https://forge.sh) to template and manage the service, so this is a templated Kubernetes manifest).

With this manifest, I was able to get my service up and running in Kubernetes.

### My Matterbridge Service in Git

In summary, my service consists of:

* A Dockerfile
* A (templated) Kubernetes manifest
* A `matterbridge.toml` configuration file

all of which I was able to check into a Git repository.

### The pre-Kubernetes world

The ease with which I was able to get a service reliably made me reflect on how I would have done this in the VM-days. I would’ve had to:

* Provision a VM (and/or create an auto-scaling group)
* Install the necessary runtime dependencies on the VM via some bash script hackery (or use Ansible, or build a custom AMI)
* Copy my configuration to the VM

Moreover, if I wanted to make the above reproducible, I would have had to use Terraform, Ansible, CloudFormation, or one of these types of tools. Here is the example from the Terraform documentation on [how to create an EC2 instance](https://www.terraform.io/docs/providers/aws/r/instance.html):

```
# Create a new instance of the latest Ubuntu 14.04 on an# t2.micro node with an AWS Tag naming it "HelloWorld"provider "aws" {  region = "us-west-2"}data "aws_ami" "ubuntu" {  most_recent = true  filter {    name   = "name"    values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]  }  filter {    name   = "virtualization-type"    values = ["hvm"]  }  owners = ["099720109477"] # Canonical}resource "aws_instance" "web" {  ami           = "${data.aws_ami.ubuntu.id}"  instance_type = "t2.micro"  tags {    Name = "HelloWorld"  }}
```

As a developer, many of the options above (region, instance type) are things that I don’t really care about. Yet, this is the current abstraction if I want to commit infrastructure-as-code.

### Summary

Kubernetes is more than just a container scheduler. It really gives you the primitives you need to control how your service gets run, without bogging you down in the details of deployment. We’re definitely [embracing](http://www.datawire.io/faster/developer-experience/) the mentality of having a small team of ops folks manage the Kubernetes cluster, while the rest of the development team just manages their services via the Kubernetes primitives.

While it’s not always sunshine and roses in Kubernetes-land, in my case of deploying Matterbridge, it was. You’ll have to wait for another article to read about challenges!

