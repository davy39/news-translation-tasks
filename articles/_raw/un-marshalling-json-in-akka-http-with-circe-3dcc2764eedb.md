---
title: How to (Un)marshal JSON in Akka HTTP with Circe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T08:38:53.000Z'
originalURL: https://freecodecamp.org/news/un-marshalling-json-in-akka-http-with-circe-3dcc2764eedb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RtFazsYIcVhn1w1cr4CyeQ.png
tags:
- name: api
  slug: api
- name: json
  slug: json
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Miguel Lopez

  Even though the usual library to (un)marshal JSON in Akka HTTP applications is spray-json,
  I decided to give circe a try. I use it in the Akka HTTP beginners course I’m working
  on. cough it’s free ? c**_ough_**

  In this post I’d like t...'
---

By Miguel Lopez

Even though the usual library to (un)marshal JSON in Akka HTTP applications is spray-json, I decided to give circe a try. I use it in the Akka HTTP beginners course I’m working on. ***_cough_*** [it’s free](http://link.codemunity.io/circe-akka-http-quickstart-course) ? *c**_ough*_**

In this post I’d like to show you why I tried it out.

To use circe with Akka HTTP — and other JSON libraries for that matter — we have to create the marshalers and unmarshalers manually. Thankfully, there is an [additional library](https://github.com/hseeberger/akka-http-json) that already does that for us.

### Project setup and overview

Clone the [project’s repository](https://github.com/Codemunity/akkahttp-quickstart), and checkout the `branch 3.3-repository-implementation`.

Under `src/main/scala` you'll find the following files:

```
$ tree srcsrc└── main    └── scala        ├── Main.scala        ├── Todo.scala        └── TodoRepository.scala2 directories, 3 files
```

The `Main` object is the application's entry point. So far it has a hello world route and it binds it to a given host and route.

`Todo` is our application’s model. And the `TodoRepository` is in charge of persisting and accessing todos. So far it only has an in-memory implementation to keep things simple and focused.

### Listing all the todos

We’ll change the `Main` object’s route to list all the todos in a repository. We will also add some initial todos for testing:

```
import akka.actor.ActorSystemimport akka.http.scaladsl.Httpimport akka.stream.ActorMaterializerimport scala.concurrent.Awaitimport scala.util.{Failure, Success}object Main extends App {  val host = "0.0.0.0"  val port = 9000  implicit val system: ActorSystem = ActorSystem(name = "todoapi")  implicit val materializer: ActorMaterializer = ActorMaterializer()  import system.dispatcher  val todos = Seq(    Todo("1", "Clean the house", "", done = false),    Todo("2", "Learn Scala", "", done = true),  )  val todoRepository = new InMemoryTodoRepository(todos)  import akka.http.scaladsl.server.Directives._  def route = path("todos") {    get {      complete(todoRepository.all())    }  }  val binding = Http().bindAndHandle(route, host, port)  binding.onComplete {    case Success(_) => println("Success!")    case Failure(error) => println(s"Failed: ${error.getMessage}")  }  import scala.concurrent.duration._  Await.result(binding, 3.seconds)}
```

Now we’re listening to requests under `/todos` and we respond with all the todos we have in our `todoRepository`.

However, if we try to run this it won’t compile:

```
Error:(26, 34) type mismatch; found   : scala.concurrent.Future[Seq[Todo]] required: akka.http.scaladsl.marshalling.ToResponseMarshallable      complete(todoRepository.all())
```

The compilation error is telling us it doesn’t know how to marshal our todos into JSON.

We need to import circe and the support library:

```
import akka.http.scaladsl.server.Directives._import de.heikoseeberger.akkahttpcirce.FailFastCirceSupport._import io.circe.generic.auto._def route = path("todos") {  get {    complete(todoRepository.all())  }}
```

With those two extra lines we can now run our `Main` object and test our new route.

Make a GET request to `http://localhost:9000/todos` :

![Image](https://cdn-media-1.freecodecamp.org/images/xuRxZ8giASz62AEFcSr0SZRIVRlXXOEoMZqL)

And we get our todos back! ?

### Creating todos

Turns out that unmarshaling JSON into our models doesn’t take much effort either. But our `TodoRepository` doesn’t support saving todos at the moment. Let’s add that functionality first:

```
import scala.concurrent.{ExecutionContext, Future}trait TodoRepository {  def all(): Future[Seq[Todo]]  def done(): Future[Seq[Todo]]  def pending(): Future[Seq[Todo]]  def save(todo: Todo): Future[Todo]}class InMemoryTodoRepository(initialTodos: Seq[Todo] = Seq.empty)(implicit ec: ExecutionContext) extends TodoRepository {  private var todos: Vector[Todo] = initialTodos.toVector  override def all(): Future[Seq[Todo]] = Future.successful(todos)  override def done(): Future[Seq[Todo]] = Future.successful(todos.filter(_.done))  override def pending(): Future[Seq[Todo]] = Future.successful(todos.filterNot(_.done))  override def save(todo: Todo): Future[Todo] = Future.successful {    todos = todos :+ todo    todo  }}
```

We added a method `save` to the trait and the implementation. Because we are using a `Vector` our implementation of `save` will store duplicated todos. That’s fine for the purposes of this tutorial.

Let’s add a new route that will listen to POST requests. This route receive a `Todo` as the request’s body and saves it into our repository:

```
def route = path("todos") {  get {    complete(todoRepository.all())  } ~ post {    entity(as[Todo]) { todo =>      complete(todoRepository.save(todo))    }  }}
```

Using the `entity` directive we can build a route that automatically parses incoming JSON to our model. It also rejects requests with invalid JSON:

![Image](https://cdn-media-1.freecodecamp.org/images/ew2sqvGf4H8BuBFuDM5iVG-RQsHTV5DVd9yx)

We sent the `done` field as a string, and it should have been a boolean, which our API responded to with bad request.

Let’s make a valid request to create a new todo:

![Image](https://cdn-media-1.freecodecamp.org/images/qqLEGI-7ia2pcDesaClXCoTW7D21h5DOC7v1)

This time we sent the property as `done := false`, which tells HTTPie to send the value as `Boolean` instead of `String`.

We get our todo back and a 200 status code, which means it went well. We can confirm it worked by querying the todos again:

![Image](https://cdn-media-1.freecodecamp.org/images/bHQixnuljInXUXX7QaKPjX6JfX-9rm-Yxtln)

We get three todos, the hardcoded ones and the new one we created.

### Wrapping up

We added JSON marshaling and unmarshaling to our application by adding the dependencies (it was already done in the project) and by importing both libraries.

Circe figures out how to handle our models without much intervention from us.

In a future post, we will explore how to accomplish the same functionality with spray-json instead.

Stay tuned!

If you liked this tutorial and want to learn how to build an API for a todo application, check out our new **free** course! ???

[**Akka HTTP Quickstart**](http://link.codemunity.io/circe-akka-http-quickstart-course)  
[_Learn how to create web applications and APIs with Akka HTTP in this free course!_link.codemunity.io](http://link.codemunity.io/circe-akka-http-quickstart-course)

_Originally published at [www.codemunity.io](https://www.codemunity.io/tutorials/akka-http-json-circe/)._

