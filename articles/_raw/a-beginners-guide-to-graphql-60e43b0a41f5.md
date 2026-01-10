---
title: A Guide to GraphQL in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T00:13:12.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-graphql-60e43b0a41f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PpKiiMujrwHszBHWoZDqPQ.jpeg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Luis Aguilar

  All you need to know about the latest buzzword that’s taking the API development
  scene by storm.


  TL;DR

  GraphQL is a query language and runtime that we can use to build and expose APIs
  as a strongly-typed schema instead of hundreds of...'
---

By Luis Aguilar

#### All you need to know about the latest buzzword that’s taking the API development scene by storm.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PpKiiMujrwHszBHWoZDqPQ.jpeg)

### TL;DR

_GraphQL_ is a query language _and_ runtime that we can use to build and expose APIs as a strongly-typed schema instead of hundreds of REST endpoints. Your clients see the schema. They write a query for what they want. They send it over and get back exactly the data they asked for and nothing more.

A schema looks like:

<script src="https://gist.github.com/ldiego08/8492502e3d95a9beaa3415fe53b959c8.js"></script>

So, if a client wants a user with an ID of 2, instead of doing a `GET /api/v1/users/2`, they would rather send a query like this:

<script src="https://gist.github.com/ldiego08/4220bbfff7ce646c906f4c818a742bbf.js"></script>

… and get a response like this:

<script src="https://gist.github.com/ldiego08/cc5294ae03f7876fea2f5b0685ccb613.js"></script>

Why should REST watch its back, and why should _you_ care?

1. **The schema is strongly-typed.** The schema dictates that the `id` parameter must be an integer. If a client sends `user(id: “2”)` instead, the GraphQL engine will reject the whole query.
2. **Clients pick what they need.** See those braces after the query parameters? That’s how our clients tell which fields they want. Fewer fields = leaner and faster responses.
3. **It’s fast.** Fields not picked won’t be processed, meaning less stress on the server.
4. **And most importantly, it’s flexible.** If a client needs fewer fields from an endpoint, we don’t create a new endpoint or version our whole API exclusively for that need. They can pick whichever fields they need, and that’s free for us.

And that’s all there is to it, really. No magic is going on. Just a more convenient, flexible, and natural way of building your API.

But what is life without those juicy core concepts and sweet, sweet code examples?

### The Big Five

Before moving onto the actual fun, there are some concepts we need to have in mind, otherwise everything else won’t make any sense.

Don’t worry—I’ll keep it short.

#### **Query**

A member of the schema that reads data.

<script src="https://gist.github.com/ldiego08/41e5d69e45c31198fb86e210581192e2.js"></script>

#### **Mutation**

A member of the schema that modifies data (as in create, edit, or delete.)

<script src="https://gist.github.com/ldiego08/955d4ab670a88441aa3e9b588b2a32fc.js"></script>

#### **Schema**

A single-rooted tree with two primary nodes: one for queries, and another for mutations.

<script src="https://gist.github.com/ldiego08/50e1b0913d75d5e5a8264a1154c74fe5.js"></script>

#### Type

The shape of everything composing the schema. The data returned by a query, the fields of that data, the parameters taken by a mutation, queries, and mutations themselves—everything has a type.

<script src="https://gist.github.com/ldiego08/44d713c8c41d9314b9bbeb16c444f65d.js"></script>

Types are composed of fields which also have a type.

Both the `query` and `mutation` initial nodes are of type `Query` and `Mutation` respectively. These have more fields, `users` and `user`, and their type can also have more fields! That’s how you structure your API data into a queryable tree.

<script src="https://gist.github.com/ldiego08/d54644fc52f0e7b4cdb903baebe4f6c8.js"></script>

#### Resolver

The actual piece that connects your code to your schema. Resolvers are actual functions that _resolve_ the value of a single field in a type. The following is a very, **very** barebones pseudo example of how it works—don’t mind it too much.

<script src="https://gist.github.com/ldiego08/4d48f724f8cca7bdff607acb7d0da927.js"></script>

Easy, right? Well, that’s it for theory, time for some code!

### A Totally Original and Not Overused Code Example

Tired of the classic user model code example? Me neither! Okay, it might be dull and uninteresting, but it serves well to illustrate the previous concepts, so let’s stick to it. By the end, we’ll have an API clients will be able to query for users, roles, and create new users.

#### 1. Create a Server

As already mentioned, GraphQL is a language, _and_ a runtime—we still have to put it somewhere. For this example, it will live in an Express server.

So let’s get started:

* Create a new folder.
* Open a terminal and `cd` to your folder.
* Run `npm init && touch server.js`
* Run `npm i express --save` to, well, install ExpressJS.
* Throw this into `server.js`:

<script src="https://gist.github.com/ldiego08/4d48f724f8cca7bdff607acb7d0da927.js"></script>

* Run the server with `node server.js`

And so we have a home for our GraphQL API.

#### 2. Add a Pinch of GraphQL

As simple as:

* Run `npm i graphql graphql-express --save`
* Edit `server.js` like this:

<script src="https://gist.github.com/ldiego08/f5d94ce7b4b6db44f6cbb7e578172337.js"></script>

And this is why it was essential to review the concepts before moving onto the code. This simple Hello World app already has a **lot** going on, but we can at least get an idea.

Don’t worry, here’s the annotated version:

<script src="https://gist.github.com/ldiego08/bb627e0f0dd0e4fbc46e3c950564681d.js"></script>

> _Wait, are we hardcoding our schema using a huge magic string? Don’t panic— we’ll get to that later._

Okay, time to fire up Postman and send some queries to our GraphQL API!

Heh, just kidding…

At line `46` we enabled GraphiQL (pronounced _“graphical,”_) a built-in fully-featured IDE for writing queries. Now, close Postman and go to `localhost:4000/graphql` in your browser of preference.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kilXLXH_EGVuMulfFfiYPg.png)
_GraphiQL: the best thing since the [IE7 tax](https://www.wired.com/2012/06/retailer-taxes-customers-still-using-internet-explorer-7/" rel="noopener" target="_blank" title=")._

What can you do with this? Well, here are some things you can try:

* **View schema.** To the right, select the `Query` root type to see its fields, return types, documentation, etc.
* **Write queries.** To the left, type the following query, and notice how the editor shows autocompletion and documentation as you go:

<script src="https://gist.github.com/ldiego08/50bb8897229d3de0121f3a8a8c58cdee.js"></script>

* **Test queries.** If your query is valid, hit that play button at the top and see the results in the middle pane.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DnfYdpMnUbIGAwshyLL5yw.gif)
_GraphiQL: Everybody’s New Best Friend_

But what about clients? They can use Graph_i_QL (or a similar tool—there are tons) to build and test their queries. Then send them over using a GraphQL client like Apollo Boost—as easy as copying and pasting!

#### 3. Add a Query to List Users

All right, Hello World is fine and all, but we want to do more than greeting people. Let’s add a new `User` type, and replace `hello` with `users` which will return all users from a dummy repository.

* Edit `server.js` like this:

<script src="https://gist.github.com/ldiego08/768a065d0a65973fa708fe82b86d5cdd.js"></script>

* Grab the `user-repository.js` file from [here](https://github.com/ldiego08/workshops-graphql/blob/2-with-repository/user-repository.js) and put it in your local directory.
* Restart your server and refresh the Graph_i_QL editor.
* In your query, replace `hello` for `users { id, login }` and hit play.
* **Profit.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*i6jTWR6tXLF_7ypl9hoK_g.gif)
_Building a Query: As Easy as 1–2–3._

Annotated:

<script src="https://gist.github.com/ldiego08/a9705fa26ee350d7d94c2981acf95782.js"></script>

#### 4. Add a Query to Get a Single User By ID

By now, you might be asking: if queries are also fields of a type, why not call them fields? What makes them different?

**Queries can take parameters and use a resolver.**

The easiest way to see it is to compare it to OOP classes. While classes have fields and functions, GraphQL types have fields and queries.

* Edit `server.js` with:

<script src="https://gist.github.com/ldiego08/434191e901d3b79a77a2c9d990718d72.js"></script>

Again, no magic.

We’re saying the `user` query takes an `id` parameter, and that’s what its resolver function will take. Oh, also notice the `!` sign meaning the parameter is required—GraphQL will make sure it is provided.

#### 5. Replace Schema Builder with Manual Definitions

Remember how we called out that huge magic string we used to define our schema? Well, it’s time to fix that.

Okay, in a real-world app, you would put your schema in separate `*.graphql` files. Then you can add syntax highlighting and code completion plugins to your code editor. However, manual definitions offers a better integration with the rest of our code. Check out [this article](https://blog.apollographql.com/three-ways-to-represent-your-graphql-schema-a41f4175100d) for more info.

For this step, we’ll use the specialized classes and helpers provided by GraphQL:

<script src="https://gist.github.com/ldiego08/6d856472fde11ee9b7b6f26a02fe7111.js"></script>

Done? Okay, now annotated:

<script src="https://gist.github.com/ldiego08/fe5e44292438018e8b336950390dabd9.js"></script>

This way we can put our type definitions in separate files to better organize our server code!

As pointed out in the example, in this notation, the resolver function takes the following parameters:

* `**root**`**—**the resolved parent object, in this case the user.
* `**args**`**—**arguments passed by the query.
* `**context**`**, `info`—**out of the scope of this guide.

#### 6. Add a Sub-query for Fetching User Roles

So far, we’ve learned to define basic queries. Time to turn it up a notch! Let’s add a new field to the `User` type for its assigned roles. In a traditional architecture, we’d be tempted to create a new query like `userRoles(userId: Int!): Role` and call it a day. But that’s not how things work in GraphQL!

**We have to think in _graphs_.**

In the language of graphs, to get the roles of a user we’d send a query like this:

<script src="https://gist.github.com/ldiego08/4d4437d1c2f9b94befe1b17010b685c6.js"></script>

… and get a JSON result like this:

<script src="https://gist.github.com/ldiego08/54c1e39b10e094bd3e428f989122003f.js"></script>

Makes sense, right? Let’s go ahead and modify the schema.

* Edit `server.js` with:

<script src="https://gist.github.com/ldiego08/ba3260d390ffe8bf0a2f63105a1dd5a4.js"></script>

There—we can fetch user roles now. Notice how we used the `User` instance passed as the first parameter to the resolver to get the ID from the parent resolved user.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o6VJ8MEkuRgfgPHZEx4hAg.gif)
_Schema Documentation: It’s Got Your Back._

The advantage of subqueries? GraphQL won’t resolve the `roles` field unless it’s selected in the query.

**Did you spot the pitfall with the last bit of code?**

If we query 100 users and their roles, the `roles` resolver function will execute a hundred times. Then, let’s say each user has 10 roles and each role has a sub-query field. That query will execute 100 * 10 times.

This is called [The N + 1 Problem](https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/).

Finding out how to fix that is your homework! But it’s dangerous to go alone, so take this:

[**Avoiding n+1 requests in GraphQL, including within subscriptions**](https://medium.com/slite/avoiding-n-1-requests-in-graphql-including-within-subscriptions-f9d7867a257d)  
[_Note: this article will not make much sense unless you know the basics of GraphQL, an awesome technology we use at…_medium.com](https://medium.com/slite/avoiding-n-1-requests-in-graphql-including-within-subscriptions-f9d7867a257d)

#### 7. Add a Mutation to Create a New User

As mentioned before, _mutations_ are how we change data in our schema. If we want to create, edit, or delete a user account, we’ll need a mutation for that.

Mutations are defined almost exactly the same as a query, and often return the affected data. So the only difference between them is merely logical?

Exactly.

As mentioned before, queries can also take parameters. They only return data.

* Edit `server.js` with:

<script src="https://gist.github.com/ldiego08/ccd363aac96df4440c2ab098102abf9f.js"></script>

* Send the following query from Graph_i_QL:

<script src="https://gist.github.com/ldiego08/f286b4f91e03dabff287ec06536b1903.js"></script>

* **Profit.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*qq5k85ub7aQ3xB-siyUKUw.gif)
_Typos: Screwing Up GIF Recordings Since 1927_

### Conclusion

So, hopefully, the basics of GraphQL are clear: setting up a server, creating a schema (in plain and complex notation) with types, queries, and mutations. I used quite a basic example. Hopefully it served well for illustrating every concept unobtrusively.

From this point onwards, it’s up to you to expand the example with more stuff. Or you can create a completely new codebase for another use case.

To get you going, here are a few things you can try out:

* Solving the N+1 problem by implementing data loaders.
* Create mutations for validating user credentials, managing user roles, and more.
* Add an actual database to feed your resolvers (MySQL, SQLite, etc.)
* Use an authentication backend like OAuth to validate users.
* Create a simple client app that uses the Apollo Boost client to connect to your server.
* Rebuild the example with TypeScript.

Possibilities are endless!

### Get the Source Code

The entire example is hosted in GitHub. Browse through the [tags](https://github.com/ldiego08/workshops-graphql/tags) to see a gradual progression of the code.

[**ldiego08/workshops-graphql**](https://github.com/ldiego08/workshops-graphql)  
[_GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…_github.com](https://github.com/ldiego08/workshops-graphql)

> Got questions, comments, or anything you’d like to share? Find me on Twitter as [@ldiego08](https://twitter.com/ldiego08). Also, don’t forget to ?, share, and follow if this post was helpful!

[**Luis Aguilar (@ldiego08) | Twitter**](https://twitter.com/ldiego08)  
[_San José, Costa Rica — Writer of sci-fi, software dev @skillshare._ twitter.com](https://twitter.com/ldiego08)

