---
title: How to Monitor Python APIs using Pyctuator and SpringBootAdmin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-02T15:02:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-monitor-python-apis-using-pyctuator-and-springbootadmin
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-01-at-12.18.52-AM.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
- name: spring-boot
  slug: spring-boot
seo_title: null
seo_desc: "By Sameer Shukla\nActuator endpoints help us monitor our services. By using\
  \ actuators, we can gain a lot of information about what’s going on. \nSpringBoot\
  \ has a number of in-built actuators, and it also allows us to create our own Actuator\
  \ Endpoint. \n..."
---

By Sameer Shukla

Actuator endpoints help us monitor our services. By using actuators, we can gain a lot of information about what’s going on. 

SpringBoot has a number of in-built actuators, and it also allows us to create our own Actuator Endpoint. 

For frameworks written in Python like Flask or FastAPI, we can incorporate actuators by integrating a library called Pyctuator. 

In this article I am going to explain how to monitor applications written in FastAPI using the Pyctuator library. I'll also show you how to manage the actuator endpoints using the SpringBootAdmin server.

## What are Actuators?

We use actuators for monitoring and managing application usage in production. This usage information gets exposed to us via REST endpoints. 

For example, we can access the application logs in production, environment details, and HTTP traces. And if something has gone wrong within the application, we can even access the applications “threaddump” for debugging purposes.

Here are some examples of few important actuator endpoints:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-16.png)
_Actuators_

## What is Pyctuator?

Actuators become popular because of SpringBoot, but you can implement them in frameworks like FastAPI or Flask by integrating a module called Pyctuator.

Pyctuator is a Python Module, which is a partial implementation of SpringBoot Actuators. Pyctuator is managed by SolarEdge.

Some of the actuators supported by Pyctuators are:

* /health: This endpoint in Pyctuator has built-in monitoring for Redis and MySQL
* /env
* /metrics 
* /logfile
* /threaddump 
* /httptrace 
* /loggers

## What is SpringBootAdmin?

Imagine a service having all these actuators for checking metrics, httptrace, threaddump and so on. It would be pretty tedious to invoke each one of them individually to check what’s going on within the service. And if we have many services and each one of them has its own actuator endpoints, this makes monitoring even more difficult.

That’s where you can use SpringBootAdmin to manage and monitor applications.

In a nutshell, SpringBootAdmin provides a nice dashboard for all the actuator endpoints in one place.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-30.png)
_Admin Dashboard_

## Use-Case for Pyctuator

The use-case is straightforward: we are going to develop a RESTful service using FastAPI framework and configure the actuators in the service using the Pyctuator module. 

The service has 3 endpoints as shown in the API-Docs (Swagger) below

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-31.png)
_API-Docs_

* GET /users: Return all the users that exists in the system. 
* POST /users: Create user
* GET /users/{id}: Return a user with a given id

You can find the code [here](https://github.com/sameershukla/fastapi-pyctuator).

In the User-Service we are going to enable the actuators using Pyctuator and monitor them using SpringBootAdmin dashboard. We are also going to explore how we can enhance the /health actuator for monitoring Redis.

For configuring the Actuators, first we need to install “pyctuator”. You can do that using the command “pip install pyctuator”. 

After installation, simply instantiating the Pyctuator object is the entry point for seeing in-built actuators within a web-framework. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-47.png)
_Pyctuator Constructor_

Before instantiating Pyctuator, if you access the /pyctuator endpoint you will get the “Not Found” message:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-91.png)
_Without Pyctuator Configuration_

After instantiation, on accessing the /pyctuator endpoint you will see all the actuators enabled by default. This is because we have defined "pyactuator_endpoint_url" within Pyctuator. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-93.png)
_After Pyctuator Configuration_

I strongly recommend going through the Pyctuator object as it explains what the mandatory and optional arguments are that we need to provide.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-114.png)
_Understanding Constructor parameters_

The mandatory parameters are:

* app – instance of FastAPI or Flask 
* the application name – displayed in the info section in SpringBootAdmin 
* “pyctuator_endpoint_url” – what we have seen which returns all the actuator endpoints   
* “registration_url” – you will understand this one shortly.

## How to Enhance the /health Endpoint

You can enhance the /health endpoint in Pyctuator to monitor Redis or MySQL databases. Say you are using Redis in your application – then we need to use RedisHealthProvider and pass the redis instance to it.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-174.png)
_Redis Health_

## How to Start the SpringBootAdmin Server

To run the SpringBootAdmin server on local, we have two options: first, we can do it by creating SpringBootAdmin manually by going to start.spring.io and adding libraries.

Spring Web & Spring Boot Admin (Server):

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-175.png)
_Creating SpringBootAdmin_

The second option is to run a Docker image:

```docker 
docker run --rm --name spring-boot-admin -p 8080:8080 michayaak/spring-boot-admin:2.2.3-1
 

```

Once the admin server is up, we need to provide the “registration_url” to the Pyctuator Constructor as discussed earlier.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-178.png)
_URL registration in SpringBootAdmin_

The Admin Server is running on localhost:8080 and this should register our application to SpringBootAdmin. We can access all the actuator endpoints in one place:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-181.png)
_Dashboard_

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-182.png)
_All Configured Actuator Endpoints_

I executed the /users endpoint few times and now HTTP Traces on the Admin side showcases all the Request-Response exchange details.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-191.png)
_HTTP Traces_

## Wrapping Up

Actuators are extremely helpful in monitoring and debugging applications in production. By accessing endpoints we can get details on thread dumps, heap dumps, HTTP Traces and so on.

Pyctuator simplifies having actuators in Python APIs to a great extent. By simply importing the library and defining an object, all the actuators are ready for us within our application.  

