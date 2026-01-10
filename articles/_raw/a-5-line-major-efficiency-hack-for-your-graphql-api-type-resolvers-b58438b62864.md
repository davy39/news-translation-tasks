---
title: A major 5 line efficiency hack for your GraphQL API Type resolvers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T14:16:56.000Z'
originalURL: https://freecodecamp.org/news/a-5-line-major-efficiency-hack-for-your-graphql-api-type-resolvers-b58438b62864
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_5uB_PojUyPvVW0UkpMDUw.jpeg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: efficiency
  slug: efficiency
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Vampiire

  Using Apollo Server and Postgres — Sequelize, we’ll create a proof of concept exploiting
  the info parameter of the resolver function for a 94% reduction in database load
  on Type queries*.

  If you are already familiar with the Apollo Server...'
---

By Vampiire

Using Apollo Server and Postgres — Sequelize, we’ll create a proof of concept exploiting the info parameter of the resolver function for a 94% reduction in database load on Type queries*.

If you are already familiar with the Apollo Server resolver signature and its `info` parameter and want to [**skip to the hack, click here**](https://medium.com/@vampiire/a-5-line-major-efficiency-hack-for-your-graphql-api-type-resolvers-b58438b62864#a693). Thanks to my inquisitive friend [Sloan Brantley Gwaltney](https://www.freecodecamp.org/news/a-5-line-major-efficiency-hack-for-your-graphql-api-type-resolvers-b58438b62864/undefined) for tipping me off to the `info` parameter’s potential.

### Background — The resolver function signature

Apollo Server provides the following resolver function signature [from their docs](https://www.apollographql.com/docs/graphql-tools/resolvers#Resolver-function-signature):

```
fieldName(obj, args, context, info) { result }
```

Back in April, I wrote some notes on the signature to teach to some teammates who were new to GraphQL / Apollo Server. Below is my (slightly) modified version of the signature:

```
(instance, arguments, context, info) { ...returning data... }
```

#### `**instance**`

> _obj / root / instance_  
>  _— GraphQL Type associated with the resolver_  
>  _— only used in Type custom field resolvers (for other Types / renamed fields)_  
>  _— exists as an **instance** of the Type’s corresponding **database Model**_

> `ex:`  
>  `Type: User`  
>  `Model: User, instance is ‘user’`  
>  `Type custom field resolver:`   
>  `user => user.property/.relationshipGette`r()

#### `**arguments**`

> _arguments / Input object_  
>  _— arguments to the Query or Mutation_  
>  _— typically in the form of an Input Type object [defined in the Schema]_  
>  _— Inputs are reusable objects that may contain many fields, a subset of which are appropriate for each resolver_  
>  _— flexible inputs that can be used for both Query and Mutation resolvers_  
>  _— destructuring in the resolver allows selectivity of the Input object fields_

> `ex:`  
>  `UserInput: { id, username, avatar, githubID }`   
>  `resolver: (root, { id }) => User.findById(id);`  
>  `// destructures 1 of 4 UserInput fie`lds

#### `**context**`

> _context / ctx_  
>  _— the context object is injected at runtime in the Apollo middleware declaration of app.js_  
>  _— it is the most versatile of the resolver parameters_  
>  _— allows you to pass in things like utility functions, database models, authenticated User, and so on_  
>  _— by passing these in the context, you no longer need ‘require’ statements for models and helpers. They are accessible directly from the resolver._  
>  _— typically defined as a nesting object with each subcontext having its own object_

#### `**info**`

> _no idea?_

…That was until a serendipitous conversation with Sloan led to discussing this **useless** parameter. Sloan mentioned that it contained information about the incoming Query. This got my gears turning on improving resolver efficiency.

### The info parameter

The `info` object holds details about your entire API Schema and other bits that I assume Apollo Server uses for processing. In particular, it holds information about the Query itself — specifically the set of Type fields requested.

#### Sequelize and the Tale of Gross Inefficiency

As it turns out, when Sequelize (and I believe every other OR/DM*) resolves rows or documents, it does so in their entirety. On the front / receiving end the data is indeed trimmed to specifications. But on the back end, the process appears to be:

`DB query for **entire** row/doc` → `map / custom resolver requested fields` → `filter data and resolve requested fields`

This was proven with a Postgres echo I ran from Sequelize on a User query:

```
SELECT "id", "role", "email", ...wtf Sequelize..., "timezone", "country_id", "city_id", "created_at", "updated_at" FROM "users" AS "User" WHERE "User"."github_username" = 'the-vampiire' LIMIT 1;
```

The Postgres query **selects** **all 17 fields** while the API Query itself only requests 1:

`user(username:”the-vampiire”) { id }`

#### Digging Into the info Object

With a bit of digging into the `info` object, I was able to get to my target: the requested fields. My theory was that if I knew the fields, I could pass them in as the `attributes` property of the Sequelize query object to reduce the load on the Postgres server.

`info.fieldNodes[].selectionSet.selections[].name.value`

#### notes

* `fieldNodes` is an array with the `0th` element is the first query. My guess is that it’s an array to support batch queries.
* `selections` is an array with objects for each requested field of the Type
* the field name itself is buried under `selections.name.value`

### The Hack

So what does all of this mean? Well with a couple of lines of code, a Model (from the context of course!), and the `info` argument, I wrote the following utility and proof of concept. It uses the Sequelize `attributes` property of the query object to get data only from the requested columns.

Using this utility resulted in a **94% decrease in the size of the query**. This, of course, scales with the number of fields requested.

One of the major known benefits of using a GraphQL API is that it allows the front end to request a payload of the exact shape and size needed.

Using my utility allows the back end to reflect the same benefits by similarly reducing the load on the database server.

The first and last lines of the `mapAttributes` function ensure only directly mapped Model fields are passed as `attributes` to the query object.

This prevents errors that arise from requesting fields that do not exist as columns on the Model.

These would arise from fields that require custom Type field resolvers (like Type relationships or custom Type field names).

#### Proof of Concept

`User Type query: user(username:”the-vampiire”) { id }`

`before` → all 17 fields of the User table are queried

```
SELECT "id", "role", "email", ...wtf Sequelize..., "timezone", "country_id", "city_id", "created_at", "updated_at" FROM "users" AS "User" WHERE "User"."github_username" = 'the-vampiire' LIMIT 1;
```

`after` → only the single requested field is queried

```
Executing (default): SELECT "status", "id" FROM "users" AS "User" WHERE "User"."github_username" = 'the-vampiire' LIMIT 1;
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*uY5yPukkf28oxZUtcQVXFw.jpeg)
_This hack is officially abided by The Dude_

### Caveats*

* I have not tested this with Mongoose or other popular OR/DMs, but in principle, the effect should be the same. The `mapAttributes` function and query object would just need a few customizations.
* I have not tested this with batch queries with different fields being requested (it may affect the `fieldNodes` property of `info`).
* Does not work with custom Type field resolvers for renamed fields
* The benefits will scale by the ratio of requested Type fields to total fields on the corresponding Model.

— Vamp

