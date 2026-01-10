---
title: How to set up Vertx in Spring
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T01:43:36.000Z'
originalURL: https://freecodecamp.org/news/vertx-in-spring-39c2dd7bc2a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zOLXCXhrX_NgyWJf3KGmrQ.jpeg
tags:
- name: Java
  slug: java
- name: MySQL
  slug: mysql
- name: spring-boot
  slug: spring-boot
- name: 'tech '
  slug: tech
- name: vertx
  slug: vertx
seo_title: null
seo_desc: 'By Rick Lee

  Spring is probably the most popular framework in the Java space. We all love its
  dependency injection and all that autowired/configuration magic. It makes unit testing
  a piece of cake.

  On the other hand, Vertx.io, which is a newer toolkit...'
---

By Rick Lee

[Spring](https://spring.io/) is probably the most popular framework in the Java space. We all love its dependency injection and all that autowired/configuration magic. It makes unit testing a piece of cake.

On the other hand, [Vertx.io](https://vertx.io/), which is a newer toolkit/framework, is gaining traction in recent years. It is light-weight and supports fully asynchronous programming via event loop like Node.js and eventbus messaging like Akka. Also, the community has made quite a lot of asynchronous tools/db clients like [Async MySQL / PostgreSQL Client](https://vertx.io/docs/vertx-mysql-postgresql-client/java/), which make it another trendy choice besides Spring.

It seems that it’s tough to choose between Vertx and Spring for new projects, but the good news is they are indeed not mutually exclusive! The following is a simple example to illustrate the setup.

This example project is about deploying a Vertical in a Springboot application. The Vertical provides a function for querying MySQL using an Async MySQL client. The function can be called directly or via vertx.eventbus.

First of all, create a simple maven Springboot application. You can create it through [Spring Initializer](https://start.spring.io/). Then add the following to the pom.xml:

As we’re going to query mysql using [Async MySQL / PostgreSQL Client](https://vertx.io/docs/vertx-mysql-postgresql-client/java/), a very primitive MysqlClient.java is created and the MySQL configuration is put on the application.yaml.

Create a dummy user table with 2 fields and insert some data:

Optionally, create a repository class for accessing the user table:

Now we can create the vertical, which has a single method for handling MySQL queries.

Finally, create the Spring application and add a deployVerticle method with the @PostConstruct annotation.

If you run the Spring application, you will see the following System printout of “dbVerticle deployed” and it means the Verticle is running on the Spring application.

```
2019-02-11 08:56:27.110  INFO 29444 --- [ntloop-thread-0] i.v.ext.asyncsql.impl.MYSQLClientImpl    : Creating configuration for localhost:33062019-02-11 08:56:27.442  INFO 29444 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'dbVerticle deployed2019-02-11 08:56:27.848  INFO 29444 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''2019-02-11 08:56:27.853  INFO 29444 --- [           main] n.r.s.SpringVertxExampleApplication      : Started SpringVertxExampleApplication in 5.393 seconds (JVM running for 6.671)
```

To test it, we can simply add a db query request right after the Verticle was deployed.

The console prints out the following:

```
dbVerticle deployedsuccess[{"id":10466,"username":"ricklee"}][{"id":10468,"username":"maryjohnson"}]
```

This example illustrated how you can enjoy the facilities from both the Spring and Vertx world with a simple setup.

Source code here: [https://github.com/rickcodetalk/spring-vertx-example](https://github.com/rickcodetalk/spring-vertx-example)

