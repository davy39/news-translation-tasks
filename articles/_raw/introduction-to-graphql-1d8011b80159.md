---
title: 4 Reasons you should try out GraphQL today
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-23T21:30:40.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-graphql-1d8011b80159
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9Lp6ioBWW7wD2EZTZ7Mh9w.png
tags:
- name: api
  slug: api
- name: data
  slug: data
- name: database
  slug: database
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Guido Schmitz

  Even though I’ve been developing (RESTful) APIs for some years now, I’ve started
  to become a big fan of GraphQL.

  In this post I’ll introduce you to GraphQL and what kind of advantages you will
  have over REST. Let’s get started.


  Grap...'
---

By Guido Schmitz

Even though I’ve been developing (RESTful) APIs for some years now, I’ve started to become a big fan of GraphQL.

In this post I’ll introduce you to GraphQL and what kind of advantages you will have over REST. Let’s get started.

> GraphQL is a data query language and runtime designed and used at Facebook to request and deliver data to mobile and web apps since 2012.

#### **Why GraphQL?**

* One endpoint to access your data
* Retrieve only the data your client needs in a single request (flexibility)
* No need to tailor endpoints for your views
* No versioning

Imagine having a mobile application that has a news feed.

Often, your data will change over time, and you’ll need to introduce new versions of your API while maintaining older versions as well. This is necessary because other users still rely on older versions, where those new data changes have not yet been implemented.

One of the advantages of GraphQL is that it enables flexibility in your data model by using the [Type System](http://graphql.org/docs/typesystem/). The Type System is a description of which types of objects your server can return.

Let’s describe a Person type, using the JavaScript implementation of GraphQL:

#### **The Introspection system**

One of the other cool things about GraphQL is its [introspection system](http://graphql.org/docs/introspection/). This allows us to ask our server about which queries it supports. Compare this to built-in documentation. If you don’t know what types are available, you can easily ask GraphQL with this simple query:

```
{  __schema {    types {      name    }  }}
```

So when a new iOS developer comes in that has to retrieve data from your API, you can easily refer to this as documentation. As your schema evolves, this will always be up to date because of the type system. Cool right?

> To make it even better, there is an in-browser IDE library available to explore your API called [**GraphiQL**](https://github.com/graphql/graphiql).

#### **Querying data from the GraphQL server**

After defining your data models using the type system, you can execute queries on your GraphQL server. Before you can execute queries on the server, you’ll have to define a root query type:

Now you can actually execute the query on our server:

```
query PersonQuery {  person {    firstName    lastName    friends {      firstName    }  }}
```

So you ask the server for the Person type and his related friends. No endpoint that returns an array of resources containing all fields and some   
kind of **?include** query parameter. **_Just the data our client needs_**.

Let’s say you also have a News type. In GraphQL, you can retrieve multiple types at once. This means you can get different resources with only one single request:

```
query HomepageQuery {  person {    firstName    lastName  }  news(limit: 10) {    title    excerpt    createdAt    person {      firstName      lastName    }  }}
```

If you want your server to support this query, you have to extend your root query type a bit (Note: If you’re using this code, don’t forget to define the news type ?):

After we’ve created our root query type, we have to add it to our schema:

```
new GraphQLSchema({ query: Query });
```

#### **Mutating data to the GraphQL server**

So with the **query** type, we can retrieve data from the server. We can also add, update or delete data with GraphQL. We can do this by executing a **mutation** on the server and let the server return the values of the mutation we executed. Take a look at this example:

```
mutation addPerson {  createPerson(    firstName: 'John',    lastName: 'Doe'  ) {    firstName    lastName  }}
```

Defining a mutation is just like defining a root query type. The only thing we need to do is to add it to our schema. So, our updated schema looks like below:

```
new GraphQLSchema({ query: Query, mutation: Mutation });
```

> More information on query formatting can be found at the official [documentation](http://graphql.org/docs/queries/).

I hope I gave you a basic understanding of GraphQL. If you have any questions, feel free to tweet me [**@guidsen**](https://twitter.com/guidsen).

I also send out weekly issues to my subscribers about JavaScript & ReactJS.  
[**Subscribe here to gain JavaScript knowledge**](https://www.getrevue.co/profile/guidsen)**.**

Oh, and click the ? below so other people will see this article here on Medium. Thanks for reading.

![Image](https://cdn-media-1.freecodecamp.org/images/1*prif7-04oPf8Dqo1gvSDsQ.gif)

