---
title: How to set up an internal team forum in half a day using Discourse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-12T15:34:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-an-internal-team-forum-in-half-a-day-using-discourse-b13588d907fe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*chgxuE38EYBS5anj2E49LQ.png
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ben Cheng

  TL;DR: I’ve deployed Discourse on Kubernetes (K8s) for my company’s internal discussion
  platform. Because I couldn’t find a simple tutorial, I documented my steps to help
  other developers do it too.

  Why would I want to deploy Discourse o...'
---

By Ben Cheng

**TL;DR:** I’ve deployed [Discourse](https://www.discourse.org/) on [Kubernetes (K8s)](https://kubernetes.io/) for [my company](http://oursky.com)’s internal discussion platform. Because I couldn’t find a simple tutorial, I documented my steps to help other developers do it too.

### Why would I want to deploy Discourse on Kubernetes?

1. Our company already has a Kubernetes cluster for random tools and staging deployment, so it is cheaper to deploy on the existing cluster for an internal Discourse usage.
2. As a founder, I don’t get many chances to code anymore. I wanted to learn how to use Kubernetes because my team has been using it a lot lately.

### A quick overview of this tutorial

The tutorial and the sample config below **shows how to deploy a single Discourse web-server**. This server needs to connect to a **PostgreSQL** and **Redis server**. We are using **Google Cloud Registry** and `[gcePersistentDisk](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)` for storage.  
   
So let's begin:

#### Create Discourse app Docker image

We will “misuse” the launcher provided by `discourse_docker` to create the docker image for the Discourse web server. And by “misuse” I mean that we have over-used the launcher script to create docker images for production use.

1. Clone from [https://github.com/discourse/discourse_docker](https://github.com/discourse/discourse_docker) to your local environment.

2. Setup a temporary [Redis server](https://redis.io/topics/quickstart) and [PostgresSQL database](https://www.postgresql.org/download/) in the local environment.

3. Create a `containers/web_only.yml` (as shown below)

* The env var is not relevant to K8s. It’s just for building the local image, so let’s fill in something that works for your local environment.
* Determine the plugins you want to install with your Discourse setting here.

4. **Tip**_:_ The local Redis instances might be in protected-mode, and won’t allow a Docker guest to host the connection. For this case, you should start your Redis server with the protected-mode turned off: `redis-server --protected-mode no`

5. Create the Docker images and upload the images to your K8s Docker registry. In this case, we are using Google Cloud Registry:

* Create Docker image with Discourse’s launcher: `./launcher bootstrap web_only`
* Verify that the image is created: `docker images`. You should see the Discourse image in the list if successful.
* Upload the image to the registry with this command:

Sample config in `web_only.yml` :

#### Now we’re ready to deploy to K8s

**1. Prepare a persistent volume**

We will need a persistent volume as the database to store the user info and the discussion items. We are using [GCEPersistentDisk](https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk) for the persistent disk on the K8s cluster. Now, let’s create two 10GB disks for the app and database respectively. You may consider your Discourse usage to adjust the disk size configuration.

**2. Deploy to Kubernetes**

Next, we will configure the deployment settings of the K8s cloud. Customize the sample K8s file. Here are some variables you probably want to tweak:

`volumes.yaml`

* For both persistent volumes:   
- metadata.name   
- spec.capacity.storage   
- spec.gcePersistentDisk.pdName (for the persistent disk name above)   
- spec.claimRef.namespace (for the namespace you’re using in K8s)
* The sample file here assumes you are using `gcePersistentDisk`. volumes.yaml needs to change heavily depending on what type of persistent disk you plan to use.

`redis.yaml`

* Redis Deployment:  
- spec.template.spec.containers.resources.* (CPU and Memory resources for cache server)

`pgsql.yaml`

* PersistentVolumeClaim (`pgsql-pv-claim`):  
- `spec.resources.requests.storage` (storage of DB server)

`discourse.yaml`

* PersistentVolumeClaim (`discourse-pv-claim`)  
- spec.resources.requests.storage (storage of web-server disk for logs and backups)
* Deployment (`web-server`)  
-`spec.template.spec.containers.image` (Set the URL to point to your Docker image)   
-`spec.template.spec.containers.env`

> `DISCOURSE_DEVELOPER_EMAILS`  
> `DISCOURSE_HOSTNAME`  
> `DISCOURSE_SMTP_ADDRESS`  
> `DISCOURSE_SMTP_PORT`

- spec.template.spec.containers.resources.* (CPU and Memory resources for your web-server)

`ingress.yaml`

* `spec.rules.host`
* `spec.tls.hosts`

**Recommended:** From there, you might want to create your own namespace for the deployment. Also assume you have set the right context to run the `kubectl` command in the namespace. (For details, read [Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/namespaces-walkthrough/)). Otherwise, you should rename most of the names in the config files above to unique names and add some labels.  
   
Apply secrets. `dbUsername` and `dbPassword` can be anything you want. Please set the right `smtpUsername` and `smtpPassword` for the mail delivery services you use.  
   
Another note on HTTPS for Ingress: you should read [this document](https://kubernetes.io/docs/concepts/services-networking/ingress/#tls) and the Ingress controllers specific to your cluster and update `ingress.yaml` accordingly.

Apply all config files:

Before starting the app, run the following on PostgreSQL instance to initialize the database properly. You can find your pod name by running `kubectl get pods`.

Create Discourse deployment and Ingress with these commands:

From here, your Discourse instance should be up and running. Below are some useful commands in case things don't work and require debugging:

#### Setup S3 backup and file upload

Discourse can use AWS S3 for backup and file upload. Here are the steps to enable it:

1. Create two S3 buckets: one for backup and one for file upload. Set them as private.

2. Create an IAM user with API access only and attach the AWS inline policy below:

3. Fill in the Access Key and Key ID in **Discourse Setting**.

Then Discourse can upload files to the S3 bucket you’ve specified, so you can attach image and file attachments in each post.

### That’s it!

I hope this piece is helpful for you to set up your own Discourse platform. It’s also a practical exercise for me to try deploying an app on K8s.

### Potential improvement and scaling up:

* It’s possible to run multiple replicas for Discourse web-server for scaling up. It should work, but I haven’t tried yet.
* We could also deploy Primary-Replica PostgreSQL for scaling up. We’re using [Bitnami](https://bitnami.com/)’s PostgreSQL docker image and you can read the relevant instructions [here](https://github.com/bitnami/bitnami-docker-postgresql).

_Building an app? Our free [developer tools](https://oursky.com/products/) and [open source backend](http://skygear.io) will make your job easier._

