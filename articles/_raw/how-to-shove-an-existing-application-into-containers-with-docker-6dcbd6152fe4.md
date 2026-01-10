---
title: How to shove an existing application into containers with Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-02T14:38:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-shove-an-existing-application-into-containers-with-docker-6dcbd6152fe4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mxgRaQctGgv6qSSjNrq1JQ.png
tags:
- name: Docker
  slug: docker
- name: Java
  slug: java
- name: MongoDB
  slug: mongodb
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Daniel Newton

  I have finally got round to learning how to use Docker past the level of knowing
  what it is and does without ever using it. This is the first post that I have attempted
  to use Docker in and will probably be what I refer to whenever I...'
---

By Daniel Newton

I have finally got round to learning how to use Docker past the level of knowing what it is and does without ever using it. This is the first post that I have attempted to use Docker in and will probably be what I refer to whenever I start a new project (for Java or Kotlin anyway).

This will be a short post that takes an existing project (from one of my other posts) and alters it so it can run inside of containers. The project is a Spring Boot application with a MongoDB database and ActiveMQ message queue. All these components are prime fodder for containerization.

Completing the steps outlined in this post removes the need to have a local installation of MongoDB and ActiveMQ. Just install Docker and you’re good to go. That itself is already a victory in my books.

Here are links to the [code](https://github.com/lankydan/spring-boot-jms) and the corresponding [blog post](https://lankydanblog.com/2017/06/18/using-jms-in-spring-boot/). The post covers all the information about the code.

One last comment: for the content of this post, I am assuming that you have already installed Docker. If you haven’t, then Docker has already got you covered. Here’s where you can find the [supported platforms](https://docs.docker.com/install/#supported-platforms) which provide further links on how to install Docker for your specific machine. The [orientation and setup](https://docs.docker.com/get-started/) page Docker provides might also be helpful.

### Converting the Spring App

First up, the Spring Boot application.

This is the only part of the project that contains our code. The rest are images downloaded from someone else’s repository. To start moving this application towards running in a container, we need to create a `Dockerfile` that specifies the content of an image:

This takes the base image of `openjdk:8-jdk-alpine`. This is a good starting point for the application. It adds the Jar built from the application code (naming it `app.jar`) and exposes a port for communication between containers. The final line defines the command that executed when the image is run in a container. This is what starts the Spring application.

To build an image from the `Dockerfile` run the command below (assuming you have already built the application code):

```
docker build -t spring-boot-jms-tutorial .
```

There is now an image named `spring-boot-jms-tutorial` (`-t` lets us define the name). This can now be used to create a container that executes the code that is packed into the image’s Jar:

```
docker run --name application -p 4000:8080 spring-boot-jms-tutorial
```

This will create and run a container built from the `spring-boot-jms-tutorial` image. It names the container `application` and the `-p` property allows a port from a local machine to be mapped to a port inside the container. To access port `8080` of the container we simply need to use port `4000` on our own machine.

If we stopped this container and wanted to run it again, we should use the command:

```
docker start application
```

Where `application` is the name of the container we created before. If `docker run` was used again it would create another new container rather than reusing the existing one. Actually, because we provided a name to the container, running the same `run` command from earlier will lead to an error.

Now the Spring application is successfully running in a container, but the logs are not looking very good. Let’s have a quick look so we know what we need to do next.

MongoDB connection failing:

```
Exception in monitor thread while connecting to server mongocontainer:27017 com.mongodb.MongoSocketException: mongocontainer: Name does not resolve at com.mongodb.ServerAddress.getSocketAddress(ServerAddress.java:188) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.SocketStreamHelper.initialize(SocketStreamHelper.java:59) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.SocketStream.open(SocketStream.java:57) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.InternalStreamConnection.open(InternalStreamConnection.java:126) ~[mongodb-driver-core-3.6.4.jar!/:na] at com.mongodb.connection.DefaultServerMonitor$ServerMonitorRunnable.run(DefaultServerMonitor.java:114) ~[mongodb-driver-core-3.6.4.jar!/:na] at java.lang.Thread.run(Thread.java:748) [na:1.8.0_171] Caused by: java.net.UnknownHostException: mongocontainer: Name does not resolve at java.net.Inet4AddressImpl.lookupAllHostAddr(Native Method) ~[na:1.8.0_171] at java.net.InetAddress$2.lookupAllHostAddr(InetAddress.java:928) ~[na:1.8.0_171] at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1323) ~[na:1.8.0_171] at java.net.InetAddress.getAllByName0(InetAddress.java:1276) ~[na:1.8.0_171] at java.net.InetAddress.getAllByName(InetAddress.java:1192) ~[na:1.8.0_171] at java.net.InetAddress.getAllByName(InetAddress.java:1126) ~[na:1.8.0_171] at java.net.InetAddress.getByName(InetAddress.java:1076) ~[na:1.8.0_171] at com.mongodb.ServerAddress.getSocketAddress(ServerAddress.java:186) ~[mongodb-driver-core-3.6.4.jar!/:na] ... 5 common frames omitted
```

ActiveMQ also isn’t there:

```
Could not refresh JMS Connection for destination 'OrderTransactionQueue' - retrying using FixedBackOff{interval=5000, currentAttempts=1, maxAttempts=unlimited}. Cause: Could not connect to broker URL: tcp://activemqcontainer:61616. Reason: java.net.UnknownHostException: activemqcontainer
```

We will sort these out in the next sections so the application can work in its entirety.

One last thing before we move onto looking at Mongo and ActiveMQ.

The `dockerfile-maven-plugin` could also be used to help with the above which builds the container as part of running `mvn install`. I chose not to use it since I couldn’t get it to work properly with `docker-compose`. Below is a quick example of using the plugin:

This then allows us to replace a few of the lines in the `Dockerfile`:

Here one line has been added and one existing line is changed. The `JAR_FILE` argument replaces the original name of the Jar which is injected in by the plugin from the `pom.xml`. Make these changes and run `mvn install` and bam, your container is built with all the required code.

### Using the MongoDB image

There is a MongoDB image ready and waiting for us to use. It is ideally named `mongo`… What else did you expect? All we need to do is `run` the image and give it’s container a name:

```
docker run -d --name mongocontainer mongo
```

Adding `-d` will run the container in the background. The name of the container is not just for convenience as the Spring application will need it later to connect to Mongo.

### Onto the ActiveMQ image

Setting up ActiveMQ is just as simple as Mongo. Run the command below:

```
docker run -d --name activemqcontainer -p 8161:8161 rmohr/activemq
```

Here the `8161` ports are mapped from the container to the machine it’s running on, allowing the admin console to be accessed from outside the container.

### Tying it all together

If you have been running all these commands as you read through the post, you would have noticed that the `application` container hasn’t actually been able to see the `mongocontainer` and `activemqcontainer`. This is because they are not running within the same network. Getting them to communicate is not difficult and takes only a few extra steps.

By default, Docker creates a Bridge network when setting one up without any extra configuration. Below is how to do so:

```
docker network create network
```

Now that the network (named `network`) is created, the commands that were run previously need to be altered to create containers that will connect to the network instead. Below are the 3 commands used to create the containers in the previous sections, each altered to join the network.

```
docker run -d --name mongocontainer --network=network mongodocker run -d --name activemqcontainer -p 8161:8161 --network=network rmohr/activemqdocker run --name application -p 4000:8080 --network=network spring-boot-jms-tutorial
```

Once these are all run, the application as a whole will now work. Each container can see each other. Allowing the `application` container to connect to MongoDB and ActiveMQ in their respective containers.

At this point, everything is working. It runs in the same way that I remember it working when I had everything set up on my own laptop. But, this time around, nothing is set up locally… Except for Docker!

### Docker composing it up

We could have stopped there, but this next section will make running everything even easier. Docker Compose allows us to effectively bring all the commands that we ran earlier together and start all the containers and their network all in a single command. There is some more setup, but in the end, I think the amount of typing actually goes down.

To do this, we need to create a `docker-compose.yml` file:

Use with this version of the `Dockerfile`:

This is pretty much everything that needs to be done.

`appcontainer` is the Spring application container built from the project’s code. The `build` property of the container tells Docker to build the image based on the projects `Dockerfile` found in the project’s root directory. It passes in the `JAR_FILE` argument to the `Dockerfile` moving some of the configurations into this file instead.

The other two containers don’t require much setup. As with the previous commands, the images they are built from are specified and `activemqcontainer` adds configuration around it’s mapped ports.

The last piece of configuration happens in the background. A network is created and all the containers are added to it. This removes the need to create a network manually.

All that is left to do is run the `up` command:

```
docker-compose up
```

This will build and run all the containers. The application code image is built if necessary. Running this exact command will output all the containers logs to the console, to do this in the background add the `-d` flag:

```
docker-compose up -d
```

After doing so, we can have a look at the created containers and network. Running:

```
docker ps -a --format "table {{.Image}}\t{{.Names}}"
```

Shows us:

```
IMAGE                          NAMESmongo                          spring-boot-jms_mongocontainer_1spring-boot-jms_appcontainer   spring-boot-jms_appcontainer_1rmohr/activemq                 spring-boot-jms_activemqcontainer_1
```

And the network:

```
docker network ls
```

Produces:

```
NETWORK ID       NAME                      DRIVER            SCOPE163edcfe5ada     spring-boot-jms_default   bridge            local
```

The names of the containers and network are prepended with the name of the project.

### Conclusion

That is all there is to it…for a simple setup anyway. I’m sure there is much more the Docker gods could do but I am not one of them… Yet.

In conclusion, we took an existing application that I wrote to work locally on a machine and shoved everything into a few containers. This meant we went from a machine that needed to have everything set up (with both MongoDB and ActiveMQ installed) to a machine that could skip all this by using containers and only requiring an installation of Docker. Docker then manages all of the dependencies for us.

We looked at how to move each part of the application into a container and then tied it all together with Docker Compose. Leaving us, at the end of all this, with a single command that can move us from absolutely nothing to everything needed to run the application.

The code used in this post can be found on my [GitHub](https://github.com/lankydan/spring-boot-jms-docker).

If you found this post helpful, you can follow me on Twitter at [@LankyDanDev](http://www.twitter.com/LankyDanDev) to keep up with my new posts.

Opinions and views found in my posts are my own and do not represent Accenture’s views on any subject. [View all posts by Dan Newton](https://lankydanblog.com/author/danknewton/)

_Originally published at [lankydanblog.com](https://lankydanblog.com/2018/09/02/using-docker-to-shove-an-existing-application-into-some-containers/) on September 2, 2018._

