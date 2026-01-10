---
title: How you can build a Hello World API with Scala and Akka HTTP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T16:27:50.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-build-a-hello-world-api-with-scala-and-akka-http-55e2ff67d70d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9wHrewC1Dyf2Au_qEqwWcg.jpeg
tags:
- name: Akka
  slug: akka
- name: api
  slug: api
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Miguel Lopez

  Yes, it’s still a thing.


  _Photo by [Unsplash](https://unsplash.com/photos/B3l0g6HLxr8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Blake Connally on <a href="https://unsp...'
---

By Miguel Lopez

#### _Yes, it’s still a thing._

![Image](https://cdn-media-1.freecodecamp.org/images/ws5H0lYzh1Kol7Aum0Up1pW9eiDRpXHoKkcT)
_Photo by [Unsplash](https://unsplash.com/photos/B3l0g6HLxr8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Blake Connally</a> on <a href="https://unsplash.com/search/photos/code?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Akka is a popular actor-based toolkit for building concurrent and distributed applications in the JVM. These applications mostly use Scala or Java.

It has several modules that help to build such applications, and Akka HTTP is one of them.

Akka HTTP has both client-side and server-side utilities. We will focus on the server in this tutorial.

You should be familiar with Scala, and you should have SBT and IntelliJ setup and installed. If that’s not the case, check the [official docs](https://docs.scala-lang.org/getting-started-intellij-track/getting-started-with-scala-in-intellij.html).

Without further ado, let’s build a hello world API using Scala and Akka HTTP!

### Project setup

Feel free to clone the [repo](https://github.com/Codemunity/akkahttp-quickstart), make sure you are using the branch `2.1-review-project`.

If not, we’ll be using sbt `1.1.6` and Scala `2.12.6` . Check your `build.properties` and `build.sbt` files to make sure the versions there match these.

Let’s start by adding the required dependencies. Because Akka HTTP depends on actors and streams, we’ll need to add those libraries as well.

Add the following snippet at the end of your `build.sbt` file:

```
libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % "2.5.13",  "com.typesafe.akka" %% "akka-stream" % "2.5.13",  "com.typesafe.akka" %% "akka-http" % "10.1.3",)
```

If you’re prompted to enable auto-import, do it. Otherwise you can open a terminal and `cd` into the root directory of your project. Then run `sbt update` to get the dependencies.

Auto-import will make sure to update your project every time certain files are updated, including the `build.sbt` file.

### Instantiate dependencies

Let’s create a Scala object under “src/main/scala” named `Server`. We will start by instantiating the dependencies required to create a server with Akka HTTP.

First, the object will extend the `App` trait:

```
object Server extends App {}
```

This will allow our `Server` object to be runnable.

We will need a host and a port to bind the server, so let’s add them now:

```
val host = "0.0.0.0"val port = 9000
```

Because Akka HTTP uses Akka actors and streams underneath, we will need to supply their dependencies as well:

```
implicit val system: ActorSystem = ActorSystem("helloworld")implicit val executor: ExecutionContext = system.dispatcherimplicit val materializer: ActorMaterializer = ActorMaterializer()
```

Even though you don’t need to know what they do to start developing Akka HTTP applications, it’s always good to be aware of what they’re for.

An `ActorSystem` is used to manage actors. It is used for creating and looking them up. Actors in the same system typically share the same config.

The `ExecutionContext` is in charge of executing `Future` s. It knows where and how it should execute them, for example in a thread pool.

And finally, an `ActorMaterializer` is in charge of running streams.

With that done, we can create our hello route!

### Create the route

To create our route, we will use Akka HTTP’s routing DSL. It is based on “layers” of what’s called a directive. For an overview, feel free to browse their [official docs](https://doc.akka.io/docs/akka-http/current/routing-dsl/overview.html).

Add the route below the dependencies:

```
def route = path("hello") {  get {    complete("Hello, World!")  }}
```

We have a first layer, where we try to match the incoming request’s path as “/hello”. If it doesn’t match it will be rejected.

If it matches it will try to match inner “[directives](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html)”. In our case we are matching GET requests. We complete the request/response cycle with a “Hello, World” message.

### Start the server

With our route created, all we need to do is start the server:

```
Http().bindAndHandle(route, host, port)
```

We are binding our route to the given host and port using the Akka HTTP `Http` object.

To run our `Server` object, you can right-click it and hit _Run ‘Server’_.

Give it a couple of seconds to compile, then go to a browser. Navigate to `http://localhost:9000/hello` and you should see our “Hello, World!” message.

![Image](https://cdn-media-1.freecodecamp.org/images/EZYjgm5uULRp-qqC1upw4Q8kGcDad7q4BeXN)

Cool, isn’t it?

### Logging

Before wrapping up this tutorial we’ll add basic logging to our server.

You might have noticed that there was no feedback when we ran our `Server` object. We have no clue whether it succeeded or failed.

We can only assume it worked because the application didn’t crash.

Let’s add some logging to it.

If you look into the `bindAndHandle` function from the `Http` object, it returns a future of `ServerBinding` . We can hook some logs into the future’s `onComplete` function.

Let’s do that:

```
val bindingFuture = Http().bindAndHandle(route, host, port)bindingFuture.onComplete {  case Success(serverBinding) =&gt; println(s"listening to ${serverBinding.localAddress}")  case Failure(error) => println(s"error: ${error.getMessage}")}
```

Run the `Server` again, and this time you should see:

```
listening to /0:0:0:0:0:0:0:0:9000
```

### Wrapping up

While using Scala and Akka HTTP is not the fastest way to develop APIs, it allows you to integrate other Akka modules, such as actors, streams, clusters, and more, making it easier to develop resilient and scalable systems.

Having said that, it’s good to keep in mind that developing an application using Scala and/or Akka doesn’t necessarily mean that it will be resilient and scalable. You’ll still need to perform work to accomplish that, but it’s easier than with other technologies.

If you liked Akka HTTP, we’ve got a free course that’ll quickstart your way into developing APIs with it. You’ll build an API for a Todo application, explained step by step. Check it out! ??

[**Akka HTTP Quickstart**](http://link.codemunity.io/hw-akka-http-quickstart-course)  
[_Learn how to create web applications and APIs with Akka HTTP in this free course!_link.codemunity.io](http://link.codemunity.io/hw-akka-http-quickstart-course)

