---
title: An introduction to Reactive Relational Database Access with Spring and R2DBC
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-16T10:28:54.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-reactive-relational-database-access-with-spring-and-r2dbc-1a9447d4b122
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y5vRk0tztWvhhbWrvJrm-g.png
tags:
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: spring data
  slug: spring-data
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Daniel Newton

  Not too long ago, a reactive variant of the JDBC driver was released, known as R2DBC.
  It allows data to be streamed asynchronously to any endpoints that have subscribed
  to it. Using a reactive driver like R2DBC together with Spring, ...'
---

By Daniel Newton

Not too long ago, a reactive variant of the JDBC driver was released, known as R2DBC. It allows data to be streamed asynchronously to any endpoints that have subscribed to it. Using a reactive driver like R2DBC together with Spring, WebFlux allows you to write a full application that handles receiving and sending of data asynchronously.

In this post, we will focus on the database, from connecting to the database and then finally saving and retrieving data. To do this, we will be using Spring Data. As with all Spring Data modules, it provides us with out of the box configuration. This decreases the amount of boilerplate code that we need to write to get our application setup. On top of that, it provides a layer upon the database driver that makes doing the simple tasks easier and the more difficult tasks a little less painful.

For the content of this post, I am making use of a Postgres database. At the time of writing, only Postgres, H2 and Microsoft SQL Server have their own implementations of R2DBC drivers.

I have previously written two posts about reactive Spring Data libraries, one on [Mongo](https://lankydanblog.com/2017/07/16/a-quick-look-into-reactive-streams-with-spring-data-and-mongodb/) and another about [Cassandra](https://lankydanblog.com/2017/12/11/reactive-streams-with-spring-data-cassandra/). You might have noticed that neither of these databases are RDBMS databases. Now there are other reactive drivers available for a long time (I wrote the Mongo post nearly 2 years ago) but at the time of writing a reactive driver for a RDBMS database is still a pretty new thing. This post will follow a similar format to those.

Furthermore, I have also written a post about using [Spring WebFlux](https://lankydanblog.com/2018/03/15/doing-stuff-with-spring-webflux/) which I mentioned in the introduction. Feel free to have a look at that if you are interested in producing a fully reactive web application.

### Dependencies

There are a few things to point out here.

The more you use Spring Boot, the more you will get used to importing a single `spring-boot-starter` dependency for the cool thing that you want to do. For example, I hoped that there would have been a `spring-boot-starter-r2dbc` dependency, but unfortunately, there is not one. Yet.

Simply put, this library is on the newer side and at the time of writing, does not have its own Spring Boot module that contains any dependencies it needs along with faster setup via auto-configuration. I am sure these things will come at some point and make setting up a R2DBC driver even easier.

For now, we will need to fill in a few extra dependencies manually.

Furthermore, the R2DBC libraries only have Milestone releases (more proof of them being new) so we need to make sure we bring in the Spring Milestone repository. I will probably need to update this post in the future when it gets a release version.

### Connecting to the database

Thanks to Spring Data doing a lot of the work for us, the only Bean that needs to be created manually is the `ConnectionFactory` that contains the database’s connection details:

The first thing to notice here is the extension of `AbstractR2dbcConfiguration`. This class contains a load of Beans that we no longer need to manually create. Implementing `connectionFactory` is the only requirement of the class as it is required to create the `DatabaseClient` Bean. This sort of structure is typical of Spring Data modules, so it feels quite familiar when trying out a different one. Furthermore, I’d expect this manual configuration to be removed once auto-configuration is available and be solely driven via the `application.properties`.

I have included the `port` property here, but if you have not played around with your Postgres configuration then you can rely on the default value of `5432`.

The four properties: `host`, `database`, `username` and `password` defined by the `PostgresqlConnectionFactory` are the bare minimum to get it working. Any less and you will experience exceptions during startup.

Using this configuration, Spring is able to connect to a running Postgres instance.

The final piece of noteworthy information from this example is the use of `@EnableR2dbcRepositories`. This annotation instructs Spring to find any repository interfaces that extend Spring’s `Repository` interface. This is used as the base interface for instrumenting Spring Data repositories. We will look at this a little closer in the next section. The main piece of information to take away from here is that you need to use the `@EnableR2dbcRepositories` annotation to fully leverage Spring Data’s capabilities.

### Creating a Spring Data Repository

As touched on above, in this section we will look at adding a Spring Data Repository. These repositories are a nice feature of Spring Data, meaning that you don’t need to write out a load of extra code to simply write a query.

Unfortunately, at least for now, Spring R2DBC cannot infer queries in the same way that other Spring Data modules currently do (I am sure this will be added at some point). This means that you will need to use the `@Query` annotation and write the SQL by hand. Let’s take a look:

This interface extends `R2dbcRepository`. This in turn extends `ReactiveCrudRepository` and then down to `Repository`. `ReactiveCrudRepository` provides the standard CRUD functions and from what I understand, `R2dbcRepository` does not provide any extra functions and is instead an interface created for better situational naming.

`R2dbcRepository` takes in two generic parameters, one being the entity class that it takes as input and produces as output. The second being the type of the Primary Key. Therefore in this situation, the `Person` class is being managed by the `PersonRepository` (makes sense) and the Primary Key field inside `Person` is an `Int`.

The return types of functions in this class and the ones provided by `ReactiveCrudRepository` are `Flux` and `Mono` (not seen here). These are Project Reactor types that Spring makes use of as the default Reactive Stream types. `Flux` represents a stream of multiple elements whereas a `Mono` is a single result.

Finally, as I mentioned before the example, each function is annotated with `@Query`. The syntax is quite straight forward, with the SQL being a string inside the annotation. The `$1` (`$2`, `$3`, etc… for more inputs) represents the value input into the function. Once you have done this, Spring will handle the rest and pass the input(s) into their respective input parameter, gather the results and map it to the repository’s designated entity class.

### A very quick look at the entity

Not going to say much here but simply show the `Person` class used by the `PersonRepository`.

Actually, there is one point to make here. `id` has been made nullable and provided a default value of `null` to allow Postgres to generate the next suitable value itself. If this is not nullable and an `id` value is provided, Spring will actually try to run an update instead of an insert upon saving. There are other ways around this, but I think this is good enough.

This entity will map to the `people` table defined below:

### Seeing it all in action

Now let’s have a look at it actually doing something. Below is some code that inserts a few records and retrieves them in a few different ways:

One thing I will mention about this code. There is a very real possibility that it executes without actually inserting or reading some of the records. But, when you think about it, it makes sense. Reactive applications are meant to do things asynchronously and therefore this application has started processing the function calls in different threads. Without blocking the main thread, these asynchronous processes might never fully execute. For this reason, there are some `Thread.sleep` calls in this code, but I removed them from the example to keep everything tidy.

The output for running the code above would look something like the below:

```
[ main] onSubscribe(FluxConcatMap.ConcatMapImmediate)[ main] request(unbounded)[actor-tcp-nio-1] onNext(Person(id=35, name=Dan Newton, age=25))[actor-tcp-nio-1] onNext(Person(id=36, name=Laura So, age=23))[actor-tcp-nio-1] onComplete()[actor-tcp-nio-2] findAll - Person(id=35, name=Dan Newton, age=25)[actor-tcp-nio-2] findAll - Person(id=36, name=Laura So, age=23)[actor-tcp-nio-4] findAllByName - Person(id=36, name=Laura So, age=23)[actor-tcp-nio-5] findAllByAge - Person(id=35, name=Dan Newton, age=25)
```

A few things to take away here:

* `onSubscribe` and `request` occur on the main thread where the `Flux` was called from. Only `saveAll` outputs this since it has included the `log` function. Adding this to the other calls would have lead to the same result of logging to the main thread.
* The execution contained within the subscribe function and the internal steps of the `Flux` are run on separate threads.

This is not anywhere close to a real representation of how you would use Reactive Streams in an actual application but hopefully demonstrates how to use them and gives a bit of insight into how they execute.

### Conclusion

In conclusion, Reactive Streams have come to some RDBMS databases thanks to the R2DBC driver and Spring Data that builds a layer on top to make everything a bit tidier. By using Spring Data R2DBC we are able to create a connection to a database and start querying it without the need of too much code.

Although Spring is already doing a lot for us, it could be doing more. Currently, it does not have Spring Boot auto-configuration support. Which is a bit annoying. But, I am sure that someone will get around to doing it soon and make everything even better than it already is.

The code used in this post can be found on my [GitHub](https://github.com/lankydan/spring-data-r2dbc).

If you found this post helpful, you can follow me on Twitter at [@LankyDanDev](https://twitter.com/LankyDanDev) to keep up with my new posts.

[View all posts by Dan Newton](https://lankydanblog.com/author/danknewton/)

_Originally published at [lankydanblog.com](https://lankydanblog.com/2019/02/16/asynchronous-rdbms-access-with-spring-data-r2dbc/) on February 16, 2019._

