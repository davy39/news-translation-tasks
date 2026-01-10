---
title: How to Dockerise a Scala and Akka HTTP Application — the easy way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T16:46:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerise-a-scala-and-akka-http-application-the-easy-way-23310fc880fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b7Wr6wXgoBALNMH7veOr2w.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Miguel Lopez

  Using Docker is a given nowadays. In this tutorial we will how to learn to dockerise
  our Scala and Akka HTTP applications without even creating a Dockerfile ourselves.

  For the purposes of this tutorial, we assume Docker is already ins...'
---

By Miguel Lopez

Using Docker is a given nowadays. In this tutorial we will how to learn to dockerise our Scala and Akka HTTP applications **without** even creating a Dockerfile ourselves.

For the purposes of this tutorial, we assume Docker is already installed on the machine. If it isn’t, please follow the [official documentation](https://docs.docker.com/install/).

To automate the creation of the Dockerfile for our project, we will use the [sbt-native-packager](https://sbt-native-packager.readthedocs.io/en/stable/index.html) plugin.

You can use any Scala or Akka HTTP project for this tutorial. We will be using the following [repository](https://github.com/Codemunity/akkahttp-quickstart), feel free to clone it and make sure to checkout the branch `6.5-testing-directives`.

### Adding the plugin

First, we need to add the plugin to our project in the `project/plugins.sbt` file. If the file doesn't exist, we need to create it, and then add the following line:

```
addSbtPlugin("com.typesafe.sbt" % "sbt-native-packager" % "1.3.6")
```

Then we need to enable the plugin in our `build.sbt` file. Add the following line at the top:

```
enablePlugins(JavaAppPackaging)
```

Enabling this plugin also allows us to create an executable for our application. Run `sbt stage` in the project's root directory.

Now we can execute our application by running `./target/universal/stage/bin/akkahttp-quickstart`. You should see a `Success!` message. If you send a GET request to `localhost:9000/todos` you'll get a couple of todos.

![Image](https://cdn-media-1.freecodecamp.org/images/jVniXyVNPfmJU9A2DQStDwnbF8NECz032xsA)

### Dockerising our application

It’s time to start toying around with Docker.

Let’s start by generating the Dockerfile for our application. Run `sbt docker:stage`, then run `cat target/docker/stage/Dockerfile` to see its contents:

```
FROM openjdk:latestWORKDIR /opt/dockerADD --chown=daemon:daemon opt /optUSER daemonENTRYPOINT ["/opt/docker/bin/akkahttp-quickstart"]CMD []
```

It’s quite simple. It ends up running a similar binary to the one we generated and ran earlier.

We can build a Docker image using that Dockerfile manually, but there’s a more convenient way of doing so. Let’s run `sbt docker:publishLocal.` As its name suggests, it will publish a Docker image of our application to our local registry.

Run `docker images` and you should see the following entry:

```
REPOSITORY            TAG     IMAGE ID       CREATED          SIZEakkahttp-quickstart   0.1     d03732dd0854   42 seconds ago   774MB
```

We can now run our application using Docker.

Run `docker run akkahttp-quickstart:0.1`, you should see the `Success!` message once again.

But this time, if we try to query our application we’ll get an error:

![Image](https://cdn-media-1.freecodecamp.org/images/RCytsNfGbtjSz-gywaiAP06joml9gbwl2nOE)

Let’s run `docker ps` to get some information about our running Docker process (output abbreviated):

```
CONTAINER ID     IMAGE                       PORTS            NAMES9746162d4723     akkahttp-quickstart:0.1                      serene_agnesi
```

As we can see, there are no ports exposed, so there’s no way to communicate with our application.

Applications in Docker run in their network by default. There are multiple ways to allow communication between Docker processes and the host machine. The simplest way is to expose a port.

Stop the running application, either by hitting `Ctrl-C` or by running `docker stop $CONTAINER_ID`.

This time when we run it, we’ll expose the respective port as well:

```
docker run -p 9000:9000 akkahttp-quickstart:0.1
```

We’re now able to query our dockerised application:

![Image](https://cdn-media-1.freecodecamp.org/images/3Wtn42GiMc9VPzZqNW1pJrZhzu39mlmFZcqt)

### Customising our setup

There are several things that we might want to do with the current setup we have:

* What if we want a different image name?
* What if we want to use a different port?
* Can we have a lighter image?

Let’s explore these common use cases.

#### Changing the image name

If we look into the [plugin’s official documentation](https://sbt-native-packager.readthedocs.io/en/stable/formats/docker.html), we see that there are a number of options we can change.

Give it a read and see what else you can customise.

To change the image name we can modify the `packageName` property in our `build.sbt` file, add the following line after the `scalaVersion` property:

```
packageName in Docker := "dockerised-akka-http"
```

Let’s publish the image again. Run `sbt docker:publishLocal`. We can check that we have a new image by running `docker images`:

```
REPOSITORY            TAG   IMAGE ID       CREATED          SIZE akkahttp-quickstart   0.1   d03732dd0854   42 minutes ago   774MB dockerised-akka-http  0.1   d03732dd0854   42 minutes ago   774MB
```

Now we have two images, the original one and the new one. Awesome!

#### Changing the port

We can’t change the port that our application is listening to without making code changes. The port is hardcoded in our application. Ideally, we would read it from an environment variable and maybe have one as default.

But that’s okay. Because our application is running in a different network, we can map a different port to the internal 9000 port.

When we specify the flag `-p 9000:9000` we are saying that the port 9000 in the host machine will map to the port 9000 in our process' network. Let's try changing that.

Run `docker run -p 5000:9000 dockerised-akka-http:0.1` to run our new image with a different port.

We can query the `todos` to make sure it works as expected:

![Image](https://cdn-media-1.freecodecamp.org/images/Na3g2v4jd6FRCUrKyR84TR5lHIG6CrjG5BWn)

#### Making our image lighter

For our last experiment, we will try to make our image lighter. At this point it uses over 700MB.

First, let’s increase the version so we get a different tag and can compare them. Then add `dockerBaseImage := "openjdk:8-jre-alpine"` above where we change the `packageName` . Our `build.sbt` now looks like:

```
enablePlugins(JavaAppPackaging)
```

```
name := "akkahttp-quickstart"version := "0.2"scalaVersion := "2.12.6"
```

```
dockerBaseImage := "openjdk:8-jre-alpine"packageName in Docker := "dockerised-akka-http"
```

```
val akkaVersion = "2.5.13"val akkaHttpVersion = "10.1.3"val circeVersion = "0.9.3"
```

```
libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % akkaVersion,  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,  "io.circe" %% "circe-core" % circeVersion,  "io.circe" %% "circe-generic" % circeVersion,  "io.circe" %% "circe-parser" % circeVersion,  "de.heikoseeberger" %% "akka-http-circe" % "1.21.0",  "org.scalatest" %% "scalatest" % "3.0.5" % Test)
```

We are using a different tag of the `openjdk` base image to specify that we want to use `alpine`, which is a lightweight Linux distribution.

Publish the image by running `sbt docker:publishLocal`. Get the images with `docker images` . We can see that the image is lighter now:

```
REPOSITORY             TAG   IMAGE ID       CREATED          SIZE dockerised-akka-http   0.2   4688366e70bb   32 seconds ago   119MB akkahttp-quickstart    0.1   d03732dd0854   2 hours ago      774MBdockerised-akka-http   0.1   d03732dd0854   2 hours ago      774MB
```

Let’s make sure that it still works.

Run `docker run -p 5000:9000 dockerised-akka-http:0.2`, minding the tag number. It's not working, ad we get the following error:

```
env: can't execute 'bash': No such file or directory
```

Apparently, our dockerised application needs **bash** to run. Reading the [plugin’s documentation](https://sbt-native-packager.readthedocs.io/en/stable/archetypes/java_app/index.html?highlight=bash), we can tell that it generates a bash script that executes our application.

So let’s install bash in our image and try again.

Add the following lines below where we change the `packageName` in our `build.sbt` file:

```
import com.typesafe.sbt.packager.docker._dockerCommands ++= Seq(  Cmd("USER", "root"),  ExecCmd("RUN", "apk", "add", "--no-cache", "bash"))
```

We are adding some extra commands to our Dockefile. We are changing the user to `root` to install the package, and then we install bash.

Let’s try running the application again, `docker run -p 5000:9000 dockerised-akka-http:0.2`. And it's working now, great!

If we check the images again, the **alpine**-based one is a bit bigger, like 10MB. That’s nothing compared to the roughly 770MB of the others.

Installing bash in **alpine** isn’t the worst thing in the world. Some people end up adding it anyway due to their preference and for debugging.

### Generating an Ash-compatible executable

Installing bash on our image is a bit of a workaround. Let’s use an additional plugin to generate an executable that is compatible with Alpine. Thanks to [Muki Seller](http://disq.us/p/1vwhg62) for letting us know about this solution!

According to the [official documentation](https://sbt-native-packager.readthedocs.io/en/stable/formats/docker.html#busybox-ash-support), we need to enable the extra plugin `AshScriptPlugin`.

Modify the `build.sbt` file to enable both plugins, and remove the previous workaround:

```
enablePlugins(JavaAppPackaging, AshScriptPlugin)
```

```
name := "akkahttp-quickstart"version := "0.3"scalaVersion := "2.12.6"
```

```
dockerBaseImage := "openjdk:8-jre-alpine"packageName in Docker := "dockerised-akka-http"
```

```
val akkaVersion = "2.5.13"val akkaHttpVersion = "10.1.3"val circeVersion = "0.9.3"
```

```
libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % akkaVersion,  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,
```

```
  "io.circe" %% "circe-core" % circeVersion,  "io.circe" %% "circe-generic" % circeVersion,  "io.circe" %% "circe-parser" % circeVersion,  "de.heikoseeberger" %% "akka-http-circe" % "1.21.0",
```

```
  "org.scalatest" %% "scalatest" % "3.0.5" % Test)
```

We also increased the version so we can compare and avoid overriding the previous one.

Run `sbt docker:publishLocal`, and then `docker run dockerised-akka-http:0.3`.

You should see the success message and, if you query for the todos, you should see them as well. Great!

### Conclusion

In this tutorial we dockerised a Scala and Akka HTTP application. There was nothing done specifically for this application which means that the setup will work pretty much as it is.

Then we looked at how to accomplish some common use cases by customising our Dockerfile through the plugin.

We even managed to reduce the image size by nearly seven times!

Amazing, isn’t it?

If you liked this tutorial and want to learn how to build an API for a todo application, check out our [new **free** course](https://codemunity-courses.thinkific.com/courses/akka-http-quickstart/)! ???

Originally published at [www.codemunity.io](https://www.codemunity.io/tutorials/dockerising-akka-http/).

