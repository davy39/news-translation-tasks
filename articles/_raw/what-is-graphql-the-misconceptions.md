---
title: What is GraphQL? Common Myths Debunked.
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-01-07T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-graphql-the-misconceptions
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/1_RHQ7lpGDV_M3yWRa9DiR2g-2.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
seo_title: null
seo_desc: "I love talking about GraphQL, especially with people who have been working\
  \ with GraphQL or thinking of adopting GraphQL. One common question people have\
  \ is why someone would want to move to GraphQL from REST. \nThere are a ton of resources\
  \ out there t..."
---

I love talking about GraphQL, especially with people who have been working with GraphQL or thinking of adopting GraphQL. One common question people have is why someone would want to move to GraphQL from REST. 

There are a ton of resources out there that talk about the difference between REST and GraphQL and those are great to check out if you are interested in how those two are different. In this blog post, I want to address some common misconceptions and questions asked about GraphQL.

## How do you benefit from GraphQL on the front end?

As a Front End Engineer, I like working with a GraphQL API for the following reasons:

1. You can instantly test queries and mutations using GraphiQL or playground
2. Less data means lighter state management
3. It offloads heavy lifting to the server through resolvers
4. It has documentation that is up-to-date and interactive

## How is it better than REST?

1. There is one endpoint to fetch all resources.
2. You avoid over fetching of data (getting too many fields when only a few fields are needed).
3. You avoid under fetching of data (having to call multiple APIs because one API doesn't give back all the information needed).

## Myth: GraphQL is used to query graph databases.

GraphQL can be used to query a graph database, but this is not its only use case. The "graph" in GraphQL is used to represent the graph-like structure of data. You model the data in terms of nodes and how they connect to each other. Schema is used to represent this modeling.

There is no limitation in the GraphQL spec that enforces that the data source should be a graph.

## Myth: GraphQL only works with databases or data sources that are graph based.

It's a misconception that you need to rewrite your database to adopt GraphQL. GraphQL can be a wrapper around any data source, including databases. GraphQL is a `query language for your API` - which means it is a syntax of how to ask for data.

## Myth: Data fetching with resolvers, queries and mutations work magically.

You will need to define exactly what each of them needs to do. You will be writing functions that get called when queries are fired, and writing functions for resolvers that send back exactly the data you need and know which API to call. You will be defining what data return through those functions by calling resolvers.

## Myth: GraphQL replaces Redux or any state management library

Redux is a state management library. GraphQL is not a state management library. GraphQL helps to get less data, which in turn leads to less data to manage on the client-side, but it is not a state management solution. 

You will still need to manage state - albeit in a more lightweight way. Client libraries like Apollo and Relay can be used to manage state and they have caching built-in. GraphQL is not a replacement for Redux - it helps to reduce the need for it.

## Myth: GraphQL is a database language.

GraphQL is a programming language - specifically a query language. GraphQL's spec defines how GraphQL runtimes should implement the language and how data should be communicated between client and server. 

GraphQL is used to ask for data and can be used in multiple places in any layer from front end to back end. There are databases such as DGraph that implement the GraphQL spec, allowing clients to use GraphQL to query the database.

## Myth: You can't have REST endpoints in your implementation with GraphQL.

You can plug in multiple REST endpoints or even multiple GraphQL endpoints in your application. Although it is not a best practice to have multiple REST endpoints, it is technically possible.

## Myth: GraphQL is difficult to introduce in an existing project.

GraphQL can be plugged into an existing project. You can start with one component of business logic, plug in a GraphQL endpoint, and start fetching data through GraphQL. You don't need to scrap an entire project to start using GraphQL. 

If switching to GraphQL endpoint is still a daunting task, you can start by masking a REST endpoint into a GraphQL endpoint using resolvers.

## Myth: GraphQL is only for front-end developers

GraphQL is platform agnostic. In my opinion, the beauty of GraphQL's benefits starts from the inside out - back end to front end. 

As a back end developer, you are able to expand the API by adding fields without having to publish a new version of the API. You don't need to write different endpoints for different needs since clients can fetch whatever data they need. 

With GraphQL, you have visibility of what fields clients are using, which provides powerful instrumentation.

## Myth: GraphQL will write database queries itself, I just need to specify schemas and the relation between them

You may need to write the database queries depending on which GraphQL library you are using. However, some libraries like Neo4j and Prisma write database queries too and abstract the logic away from the developer. Everything, including resolvers, queries, and mutations, needs to be defined.

## Myth: GraphQL is used to draw graphs.

Often people new to GraphQL think that it is a graph plotting software such as D3. GraphQL doesn't plot graphs.

## Myth: GraphQL requires complicated clients and is near impossible to do with a simple HTTP fetch

## Myth: It replaces ORMs.

Lately we see a lot of DB and GraphQL integration but GraphQL itself is not that.

I think GraphQL is awesome! There are a multitude of libraries that help a user get started with GraphQL. If you are interested in learning about GraphQL, [start with the documentation](https://graphql.org/learn/) or [check out this Udemy course](https://www.udemy.com/course/graphql-with-react-course/) that I found helpful when I was new to GraphQL.

%[https://twitter.com/shrutikapoor08/status/1205005069223022592]


