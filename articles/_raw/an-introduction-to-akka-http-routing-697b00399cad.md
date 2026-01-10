---
title: An introduction to Akka HTTP routing
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T19:17:41.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-akka-http-routing-697b00399cad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SLnwW0f177L3NOX0V88Z0g.png
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

  Akka HTTP’s routing DSL might seem complicated at first, but once you get the hang
  of it you’ll see how powerful it is.

  In this tutorial we will focus on creating routes and their structure. We won’t
  cover parsing to and from JSON, we...'
---

By Miguel Lopez

Akka HTTP’s routing DSL might seem complicated at first, but once you get the hang of it you’ll see how powerful it is.

In this tutorial we will focus on creating routes and their structure. We won’t cover parsing to and from JSON, we have [other tutorials](https://www.codemunity.io/tutorials/akka-http-json-circe/) that cover that topic.

### What are directives?

One of the first concepts we’ll find when learning server-side Akka HTTP (there’s a client-side library as well) is _directives_.

So, what are they?

You can think of them as building blocks, Lego pieces if you will, that you can use to construct your routes. They are composable, which means we can create directives on top of other directives.

If you want a more in-depth reading, feel free to check out [Akka HTTP’s official documentation](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html).

Before moving on, let’s discuss what we’ll build.

### Blog-like API

We’ll create a sample of a public facing API for a blog, where we will allow users to:

* query a list of tutorials
* query a single tutorial by ID
* query the list of comments in a tutorial
* add comments to a tutorial

The endpoints will be:

```
- List all tutorials GET /tutorials 
```

```
- Create a tutorial GET /tutorials/:id 
```

```
- Get all comments in a tutorial GET /tutorials/:id/comments 
```

```
- Add a comment to a tutorial POST /tutorials/:id/comments
```

We will only implement the endpoints, no logic in them. This way we’ll learn how to create this structure and the common pitfalls when starting with Akka HTTP.

### Project Setup

We’ve created a [repo](https://github.com/Codemunity/akka-http-routing-primer) for this tutorial, in it you’ll find a branch per each section that requires coding. Feel free to clone it and use it as a base project or even just change between branches to look at the differences.

Otherwise, create a new SBT project, and then add the dependencies in the `build.sbt` file:

```
name := "akkahttp-routing-dsl" 
```

```
version := "0.1" 
```

```
scalaVersion := "2.12.7" 
```

```
val akkaVersion = "2.5.17" val akkaHttpVersion = "10.1.5" 
```

```
libraryDependencies ++= Seq(   "com.typesafe.akka" %% "akka-actor" % akkaVersion,   "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,   "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,   "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,   "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,      "org.scalatest" %% "scalatest" % "3.0.5" % Test )
```

We added Akka HTTP and its dependencies, Akka Actor and Streams. And we will also use Scalatest for testing.

### Listing all the tutorials

We’ll take a TDD approach to build our directive hierarchy, creating the tests first to make sure when don’t break our routes when adding others. Taking this approach is quite helpful when starting with Akka HTTP.

Let’s start with our route to listing all the tutorials. Create a new file under `src/test/scala` (if the folders don't exist, create them) named `RouterSpec`:

```
import akka.http.scaladsl.testkit.ScalatestRouteTest import org.scalatest.{Matchers, WordSpec} 
```

```
class RouterSpec extends WordSpec with Matchers with ScalatestRouteTest { 
```

```
}
```

`WordSpec` and `Matchers` are provided by Scalatest, and we'll use them to structure our tests and assertions. `ScalatestRouteTest` is a trait provided by Akka HTTP's test kit, it will allow us to test our routes in a convenient way. Let's see how we can accomplish that.

Because we’re using [Scalatest’s WordSpec](http://www.scalatest.org/at_a_glance/WordSpec), we’ll start by creating a scope for our `Router` object that we will create soon and the first test:

```
"A Router" should {   "list all tutorials" in {   } }
```

Next, we want to make sure can send a GET request to the path `/tutorials` and get the response we expect, let's see how we can accomplish that:

```
Get("/tutorials") ~> Router.route ~> check {   status shouldBe StatusCodes.OK   responseAs[String] shouldBe "all tutorials" }
```

It won’t even compile because we haven’t created our `Router` object. Let's do that now.

Create a new Scala object under `src/main/scala` named `Router`. In it we will create a method that will return a `Route`:

```
import akka.http.scaladsl.server.Route 
```

```
object Router {
```

```
  def route: Route = ???
```

```
}
```

Don’t worry too much about the `???`, it's just a placeholder to avoid compilation errors temporarily. However, if that code is executed, it'll throw a `NotImplementedError` as we'll see soon.

Now that our tests and project are compiling, let’s run the tests (Right-click the spec and “Run ‘RouterSpec’”).

The test failed with the exception we were expecting, we haven’t implemented our routes. Let’s begin!

### Creating the listing route

By looking into the [official documentation](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html#composing-directives) we see that the route begins with the `path` directive. Let's mimic what they're doing and build our route:

```
import akka.http.scaladsl.server.{Directives, Route}
```

```
object Router extends Directives {
```

```
  def route: Route = path("tutorials") {    get {      complete("all tutorials")    }  }}
```

Seems reasonable, let’s run our spec. And it passes, great!

For reference, our entire `RouterSpec` now looks like:

```
import akka.http.scaladsl.model.StatusCodesimport akka.http.scaladsl.testkit.ScalatestRouteTestimport org.scalatest.{Matchers, WordSpec}class RouterSpec extends WordSpec with Matchers with ScalatestRouteTest {  "A Router" should {    "list all tutorials" in {      Get("/tutorials") ~> Router.route ~> check {        status shouldBe StatusCodes.OK        responseAs[String] shouldBe "all tutorials"      }    }  }}
```

### Getting a single tutorial by ID

Next, we will allow our users to retrieve a single tutorial.

Let’s add a test for our new route:

```
"return a single tutorial by id" in {  Get("/tutorials/hello-world") ~> Router.route ~> check {    status shouldBe StatusCodes.OK    responseAs[String] shouldBe "tutorial hello-world"  }}
```

We expect to get back a message that includes the tutorial ID.

The test will fail because we haven’t created our route, let’s do that now.

From the same [resource](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html#composing-directives) we used earlier to base our route on, we can see how we can place multiple directives at the same level in the hierarchy using the `~` directive.

We will have to nest `path` directives because need another segment after the `/tutorials` route for the tutorial ID. In the documentation they use `IntNumber` to extract a number from the path, but we'll use a string and for that we use can `Segment` instead.

Our route looks like:

```
def route: Route = path("tutorials") {  get {    complete("all tutorials")  } ~ path(Segment) { id =>    get {      complete(s"tutorial $id")    }  }}
```

Let’s run the tests. And you should get a similar error:

```
Request was rejectedScalaTestFailureLocation: RouterSpec at (RouterSpec.scala:17)org.scalatest.exceptions.TestFailedException: Request was rejected
```

What’s going on?!

Well, a request is rejected when it doesn’t match our directive hierarchy. This is one of the things that got me when starting.

Now is probably a good time to look into how these directives match the incoming request as it goes through the hierarchy.

Different directives will match different aspects of an incoming request, we’ve seen `path` and `get`, one matches the URL of the request and the other the method. If a request matches a directive it will go inside it, if it doesn't it will continue to the next one. This also tells us that order matters. If it doesn't match any directive the request is rejected.

Now that we now that our request is not matching our directives, let’s start looking into why.

If we look the documentation for the `path` directive (Cmd + Click on Mac) we'll find:

```
/** * Applies the given [[PathMatcher]] to the remaining unmatched path after consuming a leading slash. * The matcher has to match the remaining path completely. * If matched the value extracted by the [[PathMatcher]] is extracted on the directive level. * * @group path */
```

So, the `path` directive has to match exactly the path, meaning our first `path` directive will only match `/tutorials` and never `/tutorials/:id`.

In the same `PathDirectives` trait that contains the `path` directive we can see another directive named `pathPrefix`:

```
/** * Applies the given [[PathMatcher]] to a prefix of the remaining unmatched path after consuming a leading slash. * The matcher has to match a prefix of the remaining path. * If matched the value extracted by the PathMatcher is extracted on the directive level. * * @group path */
```

`pathPrefix` matches only a prefix and removes it. Sounds like this is what we're looking for, let's update our routes:

```
def route: Route = pathPrefix("tutorials") {  get {    complete("all tutorials")  } ~ path(Segment) { id =>    get {      complete(s"tutorial $id")    }  }}
```

Run the tests, and… we get another error. ?

```
"[all tutorials]" was not equal to "[tutorial hello-world]"ScalaTestFailureLocation: RouterSpec at (RouterSpec.scala:18)Expected :"[tutorial hello-world]"Actual   :"[all tutorials]"
```

Looks like our request matched the first `get` directive. It now matches the `pathPrefix`, and because it also is a GET request it will match the first `get` directive. Order matters.

There are a couple of things we can do. The simplest solution would be to move the first `get` request to the end of the hierarchy, however, we would have to remember this or document it. Not ideal.

Personally, I prefer avoiding such solutions and instead make the intend clear through code. If we look in the `PathDirectives` trait from earlier, we'll find a directive called `pathEnd`:

```
/** * Rejects the request if the unmatchedPath of the [[RequestContext]] is non-empty, * or said differently: only passes on the request to its inner route if the request path * has been matched completely. * * @group path */
```

That’s exactly what we want, so let’s wrap our first `get` directive with `pathEnd`:

```
def route: Route = pathPrefix("tutorials") {  pathEnd {    get {      complete("all tutorials")    }  } ~ path(Segment) { id =>    get {      complete(s"tutorial $id")    }  }}
```

Run the tests again, and… finally, the tests are passing! ?

### Listing all comments in a tutorial

Let’s put into practice what we learned about nesting routes by taking it a bit further.

First the test:

```
"list all comments of a given tutorial" in {  Get("/tutorials/hello-world/comments") ~> Router.route ~> check {    status shouldBe StatusCodes.OK    responseAs[String] shouldBe "comments for the hello-world tutorial"  }}
```

It’s a similar case as before: we know we’ll need to place a route next to another one, which means we need to:

* change the `path(Segmenter)` to `pathPrefix(Segmenter)`
* wrap the first `get` with the `pathEnd` directive
* place the new route next to the `pathEnd`

Our routes end up looking like:

```
def route: Route = pathPrefix("tutorials") {  pathEnd {    get {      complete("all tutorials")    }  } ~ pathPrefix(Segment) { id =>    pathEnd {      get {        complete(s"tutorial $id")      }    } ~ path("comments") {      get {        complete(s"comments for the $id tutorial")      }    }  }}
```

Run the tests, and they should pass! ?

### Adding comments to a tutorial

Our last endpoint is similar to the previous, but it will match POST requests. We’ll use this example to see the difference between implementing and testing a GET request versus a POST request.

The test:

```
"add comments to a tutorial" in {  Post("/tutorials/hello-world/comments", "new comment") ~> Router.route ~> check {    status shouldBe StatusCodes.OK    responseAs[String] shouldBe "added the comment 'new comment' to the hello-world tutorial"  }}
```

We’re using the `Post` method instead of the `Get` we've been using, and we're giving it an additional parameter which is the request body. The rest is familiar to us now.

To implement our last route, we can refer to the [documentation](https://doc.akka.io/docs/akka-http/current/routing-dsl/index.html#longer-example) and look at how it’s usually done.

We have a `post` directive just as we have a `get` one. To extract the request body we need two directives, `entity` and `as`, to which we supply the type we expect. In our case it's a string.

Let’s give that a try:

```
post {  entity(as[String]) { comment =>    complete(s"added the comment '$comment' to the $id tutorial")  }}
```

Looks reasonable. We extract the request body as a string and use it in our response. Let’s add it to our `route` method next to the previous route we worked on:

```
def route: Route = pathPrefix("tutorials") {  pathEnd {    get {      complete("all tutorials")    }  } ~ pathPrefix(Segment) { id =>    pathEnd {      get {        complete(s"tutorial $id")      }    } ~ path("comments") {      get {        complete(s"comments for the $id tutorial")      } ~ post {        entity(as[String]) { comment =>          complete(s"added the comment '$comment' to the $id tutorial")        }      }    }  }}
```

_If you’d like to learn how to parse Scala classes to and from JSON [we’ve got tutorials for that as well](https://www.codemunity.io/tutorials/akka-http-json-circe/)._

Run the tests, and they should all pass.

### Conclusion

Akka HTTP’s routing DSL might seem confusing at first, but after overcoming some bumps it just clicks. After a while it’ll come naturally and it can be very powerful.

We learned how to structure our routes, but more importantly, we learned how to create that structure guided by tests which will make sure we don’t break them at some point in the future.

Even though we only worked on four endpoints, we ended up with a somewhat complicated and deep structure. Stay tuned and we’ll explore different ways to simplify our routes and make them more manageable!

[Learn how to build REST APIs with Scala and Akka HTTP with this step-by-step free course!](http://link.codemunity.io/website-akka-http-quickstart)

_Originally published at [www.codemunity.io](https://www.codemunity.io/tutorials/akka-http-routing-primer/)._

