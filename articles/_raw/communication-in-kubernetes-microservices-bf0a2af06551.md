---
title: A quick look at communication in Kubernetes microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T15:31:03.000Z'
originalURL: https://freecodecamp.org/news/communication-in-kubernetes-microservices-bf0a2af06551
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JsNkOMxwSlxFNW44eFBdqg.jpeg
tags:
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adam Henson

  The “service” concept and a Node.js example


  Chico Hailing a Cab

  Based on complexity, a layer of microservices can require a variety of communication.
  Kubernetes provides a rich set of features in managing services, load balancing,
  and...'
---

By Adam Henson

#### The “service” concept and a Node.js example

![Image](https://cdn-media-1.freecodecamp.org/images/1*JsNkOMxwSlxFNW44eFBdqg.jpeg)
_Chico Hailing a Cab_

Based on complexity, a layer of microservices can require a variety of communication. Kubernetes provides a rich set of features in managing services, load balancing, and networking.

This post is intended to provide a simple example. For an in-depth overview — see [the official documentation about Services](https://kubernetes.io/docs/concepts/services-networking/service/).

### Services

> A Kubernetes `Service` is an abstraction which defines a logical set of `Pods` and a policy by which to access them - sometimes called a micro-service. ~ [Kubernetes Docs](https://kubernetes.io/docs/concepts/services-networking/service/)

As documented, we have a number of options in exposing and communicating with services. Let’s take a look at Kubernetes DNS. Details about DNS naming can be found [here](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#what-things-get-dns-names).

### A Simple Example

Consider a set of microservices that need to communicate with each other through the HTTP protocol. As an example, let’s say we need to create a cron job to ping a health check endpoint from another pod and log the response status code.

We have a Node.js Express app.

Fair enough, this app can receive HTTP GET requests to “/healthcheck” and respond with JSON.

Okay, now let’s create a little cron job app to execute requests to this endpoint at 8:00am every day.

Very good, very good… nothing out of the ordinary here. Well, wait a minute — let’s take a closer look at the line below which defines the endpoint to fetch.

```
const apiUrl = 'http://api:3000/healthcheck';
```

In utilizing Kubernetes DNS, communicating with other pods is that simple! Our service configuration for our first app above (the Express app) could be as simple as the below.

Our cron app could look very similar to the above. Configuring pods is out of scope of this post, but you can read about how you could do so utilizing [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

### Conclusion

Kubernetes offers a plethora of features and documentation supporting various means of communication internally and exposure to the outside world. We can get significant mileage simply from DNS.

