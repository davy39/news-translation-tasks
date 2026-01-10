---
title: How to (Un)marshal JSON in Akka HTTP with spray-json
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T00:37:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-un-marshal-json-in-akka-http-with-spray-json-1407876373a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HS08mMqwO6HTlYIA_xtmVw.png
tags:
- name: api
  slug: api
- name: json
  slug: json
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Miguel Lopez

  In the previous post, we added JSON support to our Akka HTTP API using circe.

  This time we’ll do the same but using spray-json. Akka HTTP supports it by providing
  an official library — we don’t need a third-party party one like we did...'
---

By Miguel Lopez

In the [previous post](https://www.codemunity.io/tutorials/akka-http-json-circe), we added JSON support to our Akka HTTP API using circe.

This time we’ll do the same but using spray-json. Akka HTTP supports it by providing an official library — we don’t need a third-party party one like we did with circe.

### Project setup

We’ll go through the same steps as the previous tutorial to set up the project.

Clone the [repo](https://github.com/Codemunity/akkahttp-quickstart), and check out the branch `3.3-repository-implementation`.

We will also do the changes we did in the previous tutorial.

First, we will replace the circe dependencies with the spray-json dependency since we won’t be needing it for this tutorial. Update the `build.sbt` file with the following contents:

```
name := "akkahttp-quickstart"version := "0.1"scalaVersion := "2.12.6"val akkaVersion = "2.5.13"val akkaHttpVersion = "10.1.3"libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % akkaVersion,  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,  "com.typesafe.akka" %% "akka-http-spray-json" % akkaHttpVersion,  "org.scalatest" %% "scalatest" % "3.0.5" % Test)
```

Next, we will add a `save` function to the `TodoRepository` and its implementation:

```
import scala.concurrent.{ExecutionContext, Future}trait TodoRepository {  def all(): Future[Seq[Todo]]  def done(): Future[Seq[Todo]]  def pending(): Future[Seq[Todo]]  def save(todo: Todo): Future[Todo]}class InMemoryTodoRepository(initialTodos: Seq[Todo] = Seq.empty)(implicit ec: ExecutionContext) extends TodoRepository {  private var todos: Vector[Todo] = initialTodos.toVector  override def all(): Future[Seq[Todo]] = Future.successful(todos)  override def done(): Future[Seq[Todo]] = Future.successful(todos.filter(_.done))  override def pending(): Future[Seq[Todo]] = Future.successful(todos.filterNot(_.done))  override def save(todo: Todo): Future[Todo] = Future.successful {    todos = todos :+ todo    todo  }}
```

This will allow us to create a POST request to create new todos.

And finally, update the `Main` object to create a list of todos for testing purposes, and with the appropriate routes:

```
import akka.actor.ActorSystemimport akka.http.scaladsl.Httpimport akka.stream.ActorMaterializerimport scala.concurrent.Awaitimport scala.util.{Failure, Success}object Main extends App {  val host = "0.0.0.0"  val port = 9000  implicit val system: ActorSystem = ActorSystem(name = "todoapi")  implicit val materializer: ActorMaterializer = ActorMaterializer()  import system.dispatcher  val todos = Seq(    Todo("1", "Record amazing gifs for the tutorials", "", done = false),    Todo("2", "Finish the spray-json tutorial", "", done = true),  )  val todoRepository = new InMemoryTodoRepository(todos)  import akka.http.scaladsl.server.Directives._  def route = path("todos") {    get {      complete(todoRepository.all())    } ~ post {      entity(as[Todo]) { todo =>        complete(todoRepository.save(todo))      }    }  }  val binding = Http().bindAndHandle(route, host, port)  binding.onComplete {    case Success(_) => println("Success!")    case Failure(error) => println(s"Failed: ${error.getMessage}")  }  import scala.concurrent.duration._  Await.result(binding, 3.seconds)}
```

With this in place, we can now move to support JSON parsing.

### Creating the format

The project shouldn’t be compiling right now because Akka HTTP doesn’t know how to convert JSON to our models and vice versa.

Adding JSON support with circe was quite simple. It only involved adding a couple of import statements.

Sadly, with spray-json that isn’t the case. The effort isn’t that great either.

So, let’s start.

Because we want to use spray-json with Akka HTTP, we can look at the [Akka HTTP’s official docs](https://doc.akka.io/docs/akka-http/current/common/json-support.html) on how to accomplish what we want.

We need to extend the trait `SprayJsonSupport` to let Akka HTTP know how to parse our models to and from JSON (via the `FromEntityUnmarshaller` and `ToEntityMarshaller` provided by the trait).

And to create the actual _format_, we will use the trait `DefaultJsonProtocol` from spray-json.

Add the following object below the `Todo` model:

```
object TodoFormat extends SprayJsonSupport with DefaultJsonProtocol {  implicit val todoFormat = jsonFormat4(Todo)}
```

This is the extra step we need when using spray-json. It has to be done for every model we have.

To get our project working, we need to import `TodoFormat` in our `Main` object:

```
import TodoFormat._import akka.http.scaladsl.server.Directives._def route = path("todos") {  get {    complete(todoRepository.all())  } ~ post {    entity(as[Todo]) { todo =>      complete(todoRepository.save(todo))    }  }}
```

Run the application and it should be working fine.

Let’s make some tests!

### Testing our API

We need to make sure our API is working as intended. So let’s query it as we did in the previous tutorial to check the functionality is the same.

Sending a GET request to `localhost:9000/todos` should give us the initial todos:

![Image](https://cdn-media-1.freecodecamp.org/images/97TXx4zg12xaNIhdDcxZys0figQgN06hFTdI)

Great, that works the same.

Let’s see if sending invalid JSON gives us something similar:

![Image](https://cdn-media-1.freecodecamp.org/images/SeH1uiH0xzKy12LYxYIglHDS8TmWIlZ8kifl)

It does. The error message is different but we get the same `400 Bad Request` which is the important part.

Let’s create a new todo with valid JSON:

![Image](https://cdn-media-1.freecodecamp.org/images/o3ItlFqvXdih41ioeLPP7p9VI1F3ZpXu23fm)

And to finish off, let’s query the todos again to make sure it was saved:

![Image](https://cdn-media-1.freecodecamp.org/images/q9BNV8IqdeXQ-FMBp1q6rtaD9Ef9M2sZKVbG)

There we go. We have a working application with spray-json.

Cool, isn’t it?

### Wrapping up

Even though working with spray-json involves some extra manual work, you don’t need an additional third-party dependency to get it to work with Akka HTTP.

It’s a matter of preference really.

In the future, we will explore how to accomplish different use cases with both to compare them. So stay tuned!

If you liked this tutorial and wanted to learn how to build an API for a todo application, check out our new **free** course! ???

[**Akka HTTP Quickstart**](http://link.codemunity.io/website-akka-http-quickstart)  
[_Learn how to create web applications and APIs with Akka HTTP in this free course!_link.codemunity.io](http://link.codemunity.io/website-akka-http-quickstart)

_Originally published at [www.codemunity.io](https://www.codemunity.io/tutorials/akka-http-spray-json/)._

