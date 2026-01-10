---
title: 'Kubernetes VS Docker: What''s the Difference? Explained With Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-10T18:03:22.000Z'
originalURL: https://freecodecamp.org/news/kubernetes-vs-docker-whats-the-difference-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/docker-vs-kubernetes-2.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: "By Sebastian Sigl\nNowadays, two of the essential tools in a developer's\
  \ toolbox are Docker and Kubernetes. Both let developers to package applications\
  \ into containers to run them in different environments. \nAlthough you can achieve\
  \ similar things usi..."
---

By Sebastian Sigl

Nowadays, two of the essential tools in a developer's toolbox are Docker and Kubernetes. Both let developers to package applications into containers to run them in different environments. 

Although you can achieve similar things using both, in practice they differ in their usage.

In this article, you will get an explanation of Docker and Kubernetes, and you will build an example NodeJS web application and deploy it using both technologies.

## What is Docker?

Here's how people define Docker on Wikipedia:

> "Docker can package an application and its dependencies in a virtual container that runs on any Linux server. This enables applications to run in a variety of locations, such as on-premises, in a public cloud, and/or in a private cloud. Docker uses the resource isolation features of the Linux kernel (such as cgroups and kernel namespaces) and a union-capable file system (such as OverlayFS) to allow containers to run within a single Linux instance, avoiding the overhead of starting and maintaining virtual machines." — Wikipedia

In short, Docker is a platform to run immutable containers encapsulated with close to native performance on a desired machine. 

There are alternatives to Docker that have similar properties like LC, rkt or containerd. Docker is just the most popular one.

## What is Kubernetes?

Here's how people define Kubernetes on Wikipedia:

> Kubernetes defines a set of building blocks ("primitives"), which collectively provide mechanisms that deploy, maintain and scale applications based on CPU, memory or custom metrics. Kubernetes is loosely coupled and extensible to meet different workloads. This extensibility is provided in large part by the Kubernetes API, which is used by internal components as well as extensions and containers that run on Kubernetes. The platform exerts its control over compute and storage resources by defining resources as Objects, which can then be managed as such. — Wikipedia

In short, Kubernetes manages multiple hosts and deploys containers to them. The most used container technology to run containers on these hosts is Docker.

Enough said, let's get our hands dirty and experience the differences ourselves.

## How to Build and deploy a NodeJS web application using Docker and Kubernetes.

If you have not installed Docker yet, you should do so. Check out and install Docker from [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).

```shell
$ docker --version

Docker version 19.03.13, build 4484c46d9d
```

Let’s create a NodeJS package file and add a single webserver dependency called [Express](https://expressjs.com).

```javascript
// file: package.json

{
  "name": "docker-vs-k8s",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

Additionally, we need to start the webserver and define a single endpoint.

```javascript
// file: server.js

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
```

_FYI: It’s fine to skip the next step if you don't have NodeJS installed. The step after the next will utilize a Docker image that comes with a ready to use Node environment._

If you have NodeJS installed on your local pc, then you can try to run the application with plain NodeJS. 

```shell
$ npm install
$ node server.js 

Running on http://0.0.0.0:8080
```

Open [http://localhost:8080](http://localhost:8080/), and you'll see your hello world response.

### Let's find a base Docker image to run our application

The public [Docker Hub](https://hub.docker.com/) is a great source. If you search for 'node' you will quickly find an i[mage that has been used more than 1 billion times](https://hub.docker.com/_/node).

A container needs to be assembled from its foundation. We start from a base image that contains a ready to use NodeJS environment. It usually builds on a simple Linux image. We copy all the required files in the container. 

Afterwards, we execute commands, for example, fetch all required dependencies. The last step is to tell the container what command to run when the container starts. 

```dockerfile
# file: 'Dockerfile'

# lts-alpine means long term support and alpine is a very small Linux 
# distribution that is a lot smaller than the default one (node:lts).
# smaller images mean faster builds and startup time that is very handy 
# when it comes to scaling containers for production up and down
FROM node:lts-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./

# Install all dependencies
RUN npm install

# Copy sources
COPY server.js server.js

CMD [ "node", "server.js" ]
```

Now, let's build the image: 

```shell
docker build -t node-web-app .
```

We can run the Docker container by:

```shell
$ docker run --name my_container -p 8080:8080 node-web-app

Running on http://0.0.0.0:8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser and you will see the hello world page. This time, it runs isolated in a container. 

You do not even need NodeJS or anything else to build and run this container. Everything is encapsulated, and due to the nature of Docker, it runs with native performance.

Let’s stop this container that might still run in the background:

```shell
$ docker rm -f my_container
```

_FYI: Close to 100% native performance is only true for Linux hosts. For Mac OS and windows, there is some translation and virtualization required that comes with some performance degradations. For development, it should be ok. Most importantly, production servers usually run a native Linux that plays nicely with Docker._

Next, let's use our previously built container in a Kubernetes cluster. In this tutorial, we will focus on a local cluster. If you go remote, it's very similar. 

In a remote setup, you also need to push your image to a publicly available registry, which allows your remote cluster to access the image. 

I might write another blog post about that in the future if people request it.

### Run your web app in Kubernetes

Your Docker comes already with a Kubernetes integration. Open the Docker app, go to _Settings -> Kubernetes_ and enable Kubernetes. 

Applying the change might take a while. You are ready as soon as the status of your Kubernetes in the bottom bar of your Docker application is green. 

If you have any issues, go to troubleshooting (the little bug icon in the top right corner), and press reset to factory defaults. Afterwards, Docker should restart and you need to activate Kubernetes again.

Let's install kubectl, one of the most important tools to interact with your Kubernetes cluster. Follow this guide to install it: [https://kubernetes.io/docs/tasks/tools/install-kubectl/](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

Now, we can check if everything is set up properly:

```shell
$ kubectl get services

NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
kubernetes ClusterIP 10.96.0.1 <none> 443/TCP 3m14s
```

Let's deploy our Docker container in our cluster:

```yaml
# file 'application/deployment.yaml'

apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-web-app
spec:
  selector:
    matchLabels:
      app: node-web-app
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: node-web-app
    spec:
      containers:
        - name: node-web-app
          image: node-web-app
          
          # only use this to for local development
          # we never pushed our image to a remote registry
          # and by default Kubernetes pulls images
          # this property forces kubernetes to always use 
          # the local image that is not a good practice in production
          imagePullPolicy: Never
          ports:
            - containerPort: 8080

```

The deployment.yaml is a file that describes what deployment to do. We can execute it by:

```shell
$ kubectl apply -f application/deployment.yaml

deployment.apps/node-web-app created
```

and check if containers are running:

```shell
$ kubectl get pods

NAME READY STATUS RESTARTS AGE
node-web-app-6788cfd6cc-bcbb2 1/1 Running 0 3s
node-web-app-6788cfd6cc-t5t6w 1/1 Running 0 3s

```

Our Kubernetes manages a cluster that contains a single host, which is our local machine. On a remote cluster, there might be hundreds of nodes that host different deployments. 

It deployed two containers to our environment. These containers run in an isolated network. Otherwise, it would not be possible to expose the same port two times. 

So how do we access the actual container? You can access a deployed container by defining a so-called service. Every public application needs a service in front that defines the exposed public port.

```yaml
# file 'application/service.yaml'

apiVersion: v1
kind: Service
metadata:
  name: my-service-for-my-webapp
spec:
  type: LoadBalancer
  selector:
    app: my-example-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080

```

We map the container port 8080 to a publicly available port 80. The service acts as a load balancer. It distributes requests among the containers.

Let's deploy our service:

```shell
$ kubectl apply -f ./application/service.yaml 

service/my-service-for-my-webapp created
```

we can check if our service is running:

```shell
$ kubectl describe svc my-service-for-my-webapp

Name: my-service-for-my-webapp
Namespace: default
Labels: <none>
Annotations: Selector: app=my-example-app
Type: LoadBalancer
IP: 10.104.18.24
LoadBalancer Ingress: localhost
Port: <unset> 80/TCP
TargetPort: 8080/TCP
NodePort: <unset> 32114/TCP
Endpoints: 10.1.0.17:8080,10.1.0.18:8080
Session Affinity: None
External Traffic Policy: Cluster
Events: <none>

```

The output is very descriptive and confirms what we want to achieve. It uses endpoints from two deployed containers (so-called pods in Kubernetes).

Now, you can open [http://localhost:80](http://localhost:80)

That's it! You created a Docker container and used it in your Kubernetes cluster. This setup is powerful and is the foundation for many scalable products and businesses nowadays.

## Finishing up

Let's tidy up our experimentation space:

```shell
$ kubectl delete -f ./application/service.yaml 

service "my-service-for-my-webapp" deleted

$ kubectl delete -f application/deployment.yaml

deployment.apps "node-web-app" deleted
```

To keep our device's resources free, we should also stop the Kubernetes feature of Docker.

I hope you enjoyed this hands-on example. Motivate yourself to Google around, check out other examples, deploy containers, connect them, and use them. 

You will learn many cool features in the future that enable you to ship your application to production in an effortless, reusable, and scalable way.

As always, I appreciate any feedback and comments. 

I hope you enjoyed the article. If you like it and feel the need for a round of applause, [follow me on Twitter](https://twitter.com/sesigl).  I work at eBay Kleinanzeigen, one of the biggest classified companies globally. By the way, [we are hiring](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen)!

Happy Dockering!

## References:

* [https://en.wikipedia.org/wiki/Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
* [https://en.wikipedia.org/wiki/Docker_(software)](https://en.wikipedia.org/wiki/Docker_(software))
* [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)
* [https://labs.play-with-k8s.com/](https://labs.play-with-k8s.com/)
* [https://nodejs.org/en/docs/guides/nodejs-docker-webapp/](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)

