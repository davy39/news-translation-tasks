---
title: Five Common Problems in GraphQL Apps (And How to Fix Them)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-09T08:05:49.000Z'
originalURL: https://freecodecamp.org/news/five-common-problems-in-graphql-apps-and-how-to-fix-them-ac74d37a293c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a5ZZXSCeFVJZ27VXNN8ELQ.png
tags:
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sacha Greif

  Learn to unlock the power of GraphQL without suffering its drawbacks

  GraphQL is all the rage these days, and for good reason: it’s an elegant approach
  that solves many of the problems associated with traditional REST APIs.

  Yet I’d be l...'
---

By Sacha Greif

#### Learn to unlock the power of GraphQL without suffering its drawbacks

[GraphQL](http://graphql.org) is all the rage these days, and for good reason: it’s an elegant approach that solves many of the problems associated with traditional REST APIs.

Yet I’d be lying if I told you that GraphQL doesn’t come with its own set of issues. And if you’re not careful, these issues might not only lead to a bloated codebase, but even to a dramatically slowed-down app.

I’m talking about problems such as:

* **Schema duplication**
* **Server/client data mismatch**
* **Superfluous database calls**
* **Poor performance**
* **Boilerplate overdose**

I’m willing to bet your app suffers from at least one of them. Good news is, none of them are incurable!

For each issue, I’ll describe the problem, and then explain how I’m addressing it inside [Vulcan](http://vulcanjs.org), a React/GraphQL open-source framework I’ve been working on over the past year (you should check it out!). But hopefully, you’ll be able to apply the same strategies to your own codebase whether you use Vulcan or not.

![Image](https://cdn-media-1.freecodecamp.org/images/WzpNm95jVV1teXE08i6UcUQ3UmjxuQrX7d8E)

### Problem: Schema Duplication

One of the first things you realize when coding a GraphQL back-end from scratch is that it involves a lot of similar-but-not-quite-identical code, especially when it comes to schemas.

Namely, you need one schema for your database, and another one for your GraphQL endpoint. Not only is it frustrating to have to write more or less the same thing twice, but you now have two independent sources of truths that you need to constantly keep in sync.

#### Solution: GraphQL Schema Generation

A number of solutions to this problem have emerged in the GraphQL ecosystem. For example, [PostGraphile](https://www.graphile.org/postgraphile/) generates a GraphQL schema from your PostgreSQL database, and [Prisma](https://www.prismagraphql.com/) will also help you generate types for your queries and mutations.

I also remember hearing [Laney Zamore & Adam Kramer from the GraphQL team](https://www.youtube.com/watch?v=XfHOrfTyJJw) describe how they directly generated their GraphQL schema from their PHP type definitions.

For Vulcan, I independently stumbled on a very similar solution. I was using [SimpleSchema](https://github.com/aldeed/simple-schema-js) to describe my schemas as JavaScript objects, and I started simply by converting JavaScript’s `String` type into a GraphQL `String`, `Number` into `Int` or `Float`, and so on.

So this JavaScript field:

```
title: {  type: String}
```

Would become this GraphQL field:

```
title: String
```

But of course, a GraphQL schema can also have custom types: `User`, `Comment`, `Event`, and so on.

I didn’t want to add too much magic to the schema generation step, so I came up with [field resolvers](http://docs.vulcanjs.org/field-resolvers.html), a simple way to let you specify these custom types. So that this JavaScript field:

```
userId{  type: String,  resolveAs: {    fieldName: 'user',    type: 'User',    resolver: document => {      return Users.findOne(document.userId)    }  }}
```

Becomes:

```
user: User
```

As you can see, we’re defining the actual [resolver](http://graphql.org/learn/execution/) function on the field as well, since it’s also directly related to the GraphQL field.

So whether you use something like PostGraphile or write your own schema generation code, I encourage you to avoid schema duplication in your own app.

Or of course, you can also use a hosted service such as [Graphcool](https://www.graph.cool/) to manage your schema using their dashboard and bypass that issue entirely.

![Image](https://cdn-media-1.freecodecamp.org/images/czkjIXuQcTg3x1rNV41WWK8U7BWTiF-UV5xm)

### Problem: Server/Client Data Mismatch

As we’ve just seen, your database and GraphQL API will have different schemas, which translate into different document shapes.

So while a `post` fresh out of the database will have a `userId` property, the same `post` as fetched through your API will instead have a `user` property.

This means that getting a post author’s name on the client will look like:

```
const getPostNameClient = post => {  return post.user.name}
```

But on the server, it’ll be a different story altogether:

```
const getPostNameServer = post => {  const postAuthor = Users.findOne(post.userId)  return postAuthor.name}
```

This can be a problem anytime you’re trying to share code between client and server to simplify your codebase. And even beyond that, it means you’re missing out on GraphQL’s great approach to data querying on the server.

I recently felt that pain when trying to build a system to generate weekly newsletters: each newsletter was composed of multiple posts and comments, along with info about their authors; in other words, a perfect use case for GraphQL. But this newsletter generation was happening on the _server_, meaning I didn’t have a way to query my GraphQL endpoint…

#### Solution: Server-to-Server GraphQL Queries

Or did I? It turns out that you can run server-to-server GraphQL queries just fine! Just [pass your GraphQL executable schema to the `graphql` function](http://graphql.org/graphql-js/graphql/#graphql), along with your GraphQL query:

```
const result = await graphql(executableSchema, query, {}, context, variables);
```

In Vulcan, [I generalized this pattern into a `runQuery` helper](http://docs.vulcanjs.org/server-queries.html), and I also added `queryOne` functions to each collection. These act just like MongoDB’s `findOne` except they return the document as fetched through the GraphQL API:

```
const user = await Users.queryOne(userId, {  fragmentText: `    fragment UserFragment on User {      _id      username      createdAt      posts{        _id        title      }    }  `});
```

Server-to-server GraphQL queries have helped me drastically simplify my code. It let me refactor my newsletter generation call from a mess of successive database calls and loops to a single GraphQL query:

```
query NewsletterQuery($terms: JSON){  SiteData{    title  }  PostsList(terms: $terms){    _id    title    url    pageUrl    linkUrl    domain    htmlBody    thumbnailUrl    commentsCount    postedAtFormatted    user{      pageUrl      displayName    }    comments(limit: 3){      user{        displayName        avatarUrl        pageUrl      }      htmlBody      postedAt    }  }}
```

The takeaway here: don’t see GraphQL as just a pure client-server protocol. GraphQL can be used to query data in any situation, including client-to-client with [Apollo Link State](https://github.com/apollographql/apollo-link-state) or even during a static build process with [Gatsby](https://www.gatsbyjs.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/FuGWs40558hc3tICTQLvg0tjEZC1B3CsngvM)

### Problem: Superfluous Database Calls

Imagine a list of posts, each of which has a user attached to it. You now want to display 10 of these posts, along with the name of their author.

With a typical implementation, this would mean **two** database calls. One to get the 10 posts, and one to get the 10 users corresponding to these posts.

But what about GraphQL? Assuming our posts have a `user` field with its own resolver, we still have one initial database call to get the list of posts. But we now have an extra call to fetch each user _per resolver_, for a total of **11** database calls!

Now imagine that each post also has 5 comments, each of which has an author. Our number of calls has now ballooned to:

* 1 for the list of posts
* 10 for the post authors
* 10 for each sub-list of 5 comments
* 50 for the comment authors

For a grand total of **71** database calls to display _a single view_!

Nobody wants to have to explain to their boss why the homepage is taking 25 seconds to load. Thankfully, there’s a solution: [Dataloader](https://github.com/facebook/dataloader).

#### Solution: Dataloader

Dataloader will let you batch and cache database calls.

* **Batching** means that if Dataloader figures out that you’re hitting the same database table multiple times, it’ll batch all calls together. In our example, the 10 post authors’ and 50 comment authors’ calls would all be batched into a single call.
* **Caching** means that if Dataloader detects that two posts (or a post and a comment) have the same author, it will reuse the user object it already has in memory instead of making a new database call.

In practice you don’t always achieve perfect caching and batching, but Dataloader is still a huge help.

And Vulcan makes using Dataloader extra easy. Out of the box, [every Vulcan model includes Dataloader functions](http://docs.vulcanjs.org/performance.html#Caching-amp-Batching) as alternatives to the “normal” MongoDB query functions.

So in addition to `collection.findOne` and `collection.find`, you can use `collection.loader.load` and `collection.loader.loadMany`.

The one limitation is that Dataloader only works when querying using document IDs. So you can use it to query for a document whose ID is already known, but you’ll still need to hit your database if you want to ask for, say, the most recently created post.

![Image](https://cdn-media-1.freecodecamp.org/images/GxlQow63LtMbXmI1doulB29kJ9Bvpfmg3DbZ)

### Problem: Poor Performance

Even with Dataloader enabled, complex views can still trigger multiple database calls, which in turn can make for slow loading times.

This can be frustrating: on one hand you want to take full advantage of GraphQL’s graph traversal features (“show me the authors of the comments of the author of the post of…” etc.). But on the other hand, you don’t want your app to become slow and unresponsive.

#### Solution: Query Caching

There is a solution though, which is to cache the _entire_ GraphQL query response. Unlike Dataloader, whose scope is limited to the current request (meaning it will only cache documents _within_ the same query), I’m talking here about caching the whole query for a period of time.

[Apollo Engine](https://www.apollographql.com/engine/) is a great way to do just that. It’s a hosted service that provides analytics about your GraphQL queries, but it also has a very useful [caching feature](https://www.apollographql.com/docs/engine/caching.html).

Vulcan comes with a built-in Engine integration, you just need to add your API key to your settings file. You can then add the `enableCache: true` argument to your GraphQL queries to cache them using Engine.

Or, using Vulcan’s built-in [data-loading higher-order components](http://docs.vulcanjs.org/resolvers.html#Higher-Order-Components):

```
withList({  collection: Posts,   enableCache: true})(PostsList)
```

The beauty of this approach is that you can easily control which queries are cached and which aren’t, even for the same resolver. For example, you might want to cache the list of recent posts featured on your frequently-accessed homepage, but not the full list of posts available on your archives page.

A final note: caching might not always be possible. For example, it’s not advisable for data that changes frequently, or for data that depends on the currently logged-in user.

![Image](https://cdn-media-1.freecodecamp.org/images/biuavoAHWIt5n3bDypomKTulQZywt2NZyN0L)

### Problem: Boilerplate Overdose

This is by no means an issue exclusive to GraphQL apps, but it’s true that they generally require you to write a lot of similar boilerplate code.

Typically, adding a new model (e.g. `Comments`) to your app will involve the following steps:

* Writing a resolver to get a list of comments.
* Writing a higher-order component (a.k.a. container) to load that list of comments.
* Optionally, writing a resolver to get a single comment by ID or slug along with the corresponding higher-order component.
* Writing mutations for inserting a new comment, editing a comment, and deleting a comment.
* Adding the corresponding forms and form-handling code.

That’s a whole lot of CRUD!

#### Solution: Generic Resolvers, Mutations, and Higher-Order Components

Vulcan’s approach is to give you smart, easy-to-use generic options for each of these. You’ll get:

* [Default resolvers](http://docs.vulcanjs.org/resolvers.html#Default-Resolvers) for displaying lists of documents and single documents.
* [Pre-made higher-order components](http://docs.vulcanjs.org/resolvers.html#Higher-Order-Components) for loading a list of documents or a single document.
* [Default mutation resolvers](http://docs.vulcanjs.org/mutations.html#Default-Mutations) for inserting, editing, and removing documents.
* [Generated forms](http://docs.vulcanjs.org/forms.html) based on your schema that work with all the above.

These are all written in a generic enough way that they’ll work with any new model out of the box.

To be sure, this “one-size-fits-all” approach is not without its downsides. For example, because queries are generated dynamically by the generic higher-order components, it’s a bit harder to use [static queries](https://dev-blog.apollodata.com/5-benefits-of-static-graphql-queries-b7fa90b0b69a).

But this strategy is still a great way to get started, at least until you have time to refactor each part of your app to a more tailor-made solution.

GraphQL is still relatively new, which means that while everybody is busy extolling its virtues, it’s easy to overlook the very real challenges involved with building GraphQL apps.

Thankfully these challenges all have solutions, and the more we discuss them (the [Vulcan Slack](http://slack.vulcanjs.org) is a great place for that by the way!), the better these solutions will become!

