---
title: How to containerise a Spring Data Cassandra application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-08T05:42:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-containerise-a-spring-data-cassandra-application-de4254240511
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3DebQtXUVpccosiYyNJ3HQ.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: spring-boot
  slug: spring-boot
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Daniel Newton

  In this post, I’ll be continuing my journey of learning Docker. I am still keeping
  it simple at this point. This time around, I am going to tackle converting a Spring
  and Cassandra application to use containers instead of running loc...'
---

By Daniel Newton

In this post, I’ll be continuing my journey of learning Docker. I am still keeping it simple at this point. This time around, I am going to tackle converting a Spring and Cassandra application to use containers instead of running locally on the host machine. More precisely, using Spring Data Cassandra to sort out the application.

I wish I looked at doing this a while ago. I have written a fair amount of posts on Cassandra. Each time I had to `cd` to the correct directory or have a shortcut to start it up. I guess it’s not that big of a deal, but there were a few other things involved — such as dropping and recreating keyspaces so I could test my application from scratch. Now, I delete the container and restart it. To me, anyway, this is helpful!

This post will be different from my previous post, [Using Docker to shove an existing application into containers](https://lankydanblog.com/2018/09/02/using-docker-to-shove-an-existing-application-into-some-containers/). Instead, I will focus more here on the application side and remove the intermediate steps of using only Docker. I will jump straight into Docker Compose.

### Containers, containers, containers

I think it’s best to start on the container side of the project. The application depends on the configuration of the Cassandra container.

Let’s go!

There’s not much going on here. This `Dockerfile` builds the Spring application image that will be put into a container in a few moments.

Next up is the `docker-compose` file. This will build both the Spring application and Cassandra containers:

Again, there isn’t too much here. The `app` container builds the Spring application using the `Dockerfile` defined previously. The `cassandra` container instead relies on an existing image, appropriately named `cassandra`.

One thing that stands out is that the `restart` property is set to `always`. This was my lazy attempt to get past how long Cassandra takes to start. Plus all the containers started with `docker-compose` start at the same time. This lead to a situation where the application is trying to connect to Cassandra without it being ready. Unfortunately, this leads to the application dying. I hoped that it would have some retry capability for initial connectivity built in… But it does not.

When we go through the code, we will see how to deal with the initial Cassandra connection programmatically instead of relying on the application dying and restarting multiple times. You will see my version of handling the connection, anyway. I’m not a huge fan of my solution, but everything else I tried caused me much more pain.

### A dash of code

I said this post would focus more on the application code, which it will. We are not going to dive into everything I put into this application and how to use Cassandra. For that sort of information, you can have a look at my older posts, which I’ll link at the end. What we will do, though, is examine the configuration code that creates the beans that connect to Cassandra.

First, let’s go through `ClusterConfig` which sets up the Cassandra cluster:

There isn’t too much there. There would be even less if Spring would retry the initial connection to Cassandra. Anyway, let’s leave that part for a few minutes and focus on the other points in this class.

The original reason I created `ClusterConfig` was to create the keyspace that the application will use. To do this, `getKeyspaceCreations` was overridden. When the application connects it will execute the query defined in this method to create the keyspace.

If this wasn’t needed and the keyspace was created in some other way, for example, a script executed as part of creating the Cassandra container, Spring Boot’s auto-configuration could be relied upon instead. This actually allows the whole application to be configured by the properties defined in `application.properties` and nothing else. Alas, it was not meant to be.

Since we have defined an `AbstractClusterConfiguration`, Spring Boot will disable its configuration in this area. Therefore, we need to define the `contactPoints` (I named the variable `hosts`) manually by overriding the `getContactPoints` method. Originally this was only defined in `application.properties`. I realised I needed to make this change once I started getting the following error:

```
All host(s) tried for query failed (tried: localhost/127.0.0.1:9042 (com.datastax.driver.core.exceptions.TransportException: [localhost/127.0.0.1:9042] Cannot connect))
```

Before I created `ClusterConfig` the address was `cassandra` rather than `localhost`.

No other properties for the cluster need to be configured. Spring’s defaults are good enough for this scenario.

I have mentioned `application.properties` so much at this point, I should probably show you what is in it.

`keyspace-name` and `contact-points` have already popped up since they are related to configuring the cluster. `schema-action` is needed to create tables based on the entities in the project. We don’t need to do anything else here as auto-configuration is still working in this area.

The fact that the `contact-points` value is set to `cassandra` is very important. This domain name originates from the name given to the container, in this case, `cassandra`. Therefore either `cassandra` can be used or the actual IP of the container. The domain name is definitely easier since it will always be static between deployments. To test this theory out, you can change the name of the `cassandra` container to whatever you want. It will still connect, as long as you change it in the `application.properties` as well.

Back to the `ClusterConfig` code. More precisely, the `cluster` bean. I have pasted the code below again so it’s easier to look at:

This code is only needed to allow retries on the initial Cassandra connection. It is annoying, but I could not come up with another simple solution. If you have a nicer one, then please let me know!

What I have done is actually quite simple, but the code itself is not very nice. The `cluster` method is a carbon copy of the overridden version from `AbstractClusterConfiguration`, with the exception of the `RetryingCassandraClusterFactoryBean` (my own class). The original function used a `CassandraClusterFactoryBean` (Spring class) instead.

Below is the `RetryingCassandraClusterFactoryBean`:

The `afterPropertiesSet` method in the original `CassandraClusterFactoryBean` takes its values and creates the representation of a Cassandra cluster by finally delegating to the Datastax Java driver (as I have mentioned throughout the post). If it fails to establish a connection, an exception will be thrown. If the exception is not caught it will cause the application to terminate. That is the whole point of the above code. It wraps the `afterPropertiesSet` in a try-catch block specified for the exceptions that can be thrown.

The `sleep` is added to give Cassandra some time to actually start up. There is no point trying to reconnect straight away when the previous attempt failed.

Using this code the application will eventually connect to Cassandra.

At this point, I would normally show you some meaningless logs to prove that the application works. But in this situation, it does not bring anything to the table. Trust me when I say, if you run the below command:

```
mvn clean install && docker-compose up
```

then the Spring application image is created and both containers are spun up.

### Conclusion

We have had a look at how to put a Spring application that connects to a Cassandra database into containers. One for the application and another for Cassandra.

The application image is built from the project’s code. The Cassandra image is taken from Docker Hub. The image name is `cassandra` just to make sure no one forgets.

In general, connecting the two containers together was relatively simple. The application needed some adjustments to allow retries when connecting to Cassandra running in the other container. This made the code a bit uglier, but it works at least.

Thanks to the code written in this post, I now have another application that I don’t need to set up on my own machine.

The code used in this post can be found on my [GitHub](https://github.com/lankydan/spring-data-cassandra-docker).

If you found this post helpful, you can follow me on Twitter at [@LankyDanDev](http://www.twitter.com/LankyDanDev) to keep up with my new posts.

### Links to my Spring Data Cassandra posts

* [Getting started with Spring Data Cassandra](https://lankydanblog.com/2017/10/12/getting-started-with-spring-data-cassandra/)
* [Separate keyspaces with Spring Data Cassandra](https://lankydanblog.com/2017/10/22/separate-keyspaces-with-spring-data-cassandra/)
* [Multiple keyspaces using a single Spring Data CassandraTemplate](https://lankydanblog.com/2017/11/12/multiple-keyspaces-using-a-single-spring-data-cassandratemplate/)
* [More complex modeling with Spring Data Cassandra](https://lankydanblog.com/2017/11/26/more-complex-modelling-with-spring-data-cassandra/)
* [Startup and shutdown scripts in Spring Data Cassandra](https://lankydanblog.com/2017/12/03/startup-and-shutdown-scripts-in-spring-data-cassandra/)
* [Reactive Streams with Spring Data Cassandra](https://lankydanblog.com/2017/12/11/reactive-streams-with-spring-data-cassandra/)
* [Plumbing included with auto-configuration in Spring Data Cassandra](https://lankydanblog.com/2017/12/16/plumbing-included-with-auto-configuration-in-spring-data-cassandra/)
* [Interacting with Cassandra using the Datastax Java driver](https://lankydanblog.com/2018/04/15/interacting-with-cassandra-using-the-datastax-java-driver/)

Wow, I didn’t realize I’ve written so many Cassandra posts.

Opinions and views found in my posts are my own and do not represent Accenture’s views on any subject. [View all posts by Dan Newton](https://lankydanblog.com/author/danknewton/)

_Originally published at [lankydanblog.com](https://lankydanblog.com/2018/09/08/containerising-a-spring-data-cassandra-application/) on September 8, 2018._

