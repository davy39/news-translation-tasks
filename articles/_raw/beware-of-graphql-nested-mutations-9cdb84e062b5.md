---
title: Beware of GraphQL Nested Mutations!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T17:51:21.000Z'
originalURL: https://freecodecamp.org/news/beware-of-graphql-nested-mutations-9cdb84e062b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6bCUDbvVF5Ccaavkye2Tjw.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jeff M Lowery

  “I have a cunning plan…”

  Once upon a time, I hit upon the notion of organizing GraphQL mutations by nesting
  operations in a return type. The idea was that these operations would then mutate
  the parent entity.

  The basic idea was this:...'
---

By Jeff M Lowery

_“I have a cunning plan…”_

Once upon a time, I hit upon the notion of [organizing GraphQL mutations](https://www.freecodecamp.org/news/organizing-graphql-mutations-653306699f3d/) by nesting operations in a return type. The idea was that these operations would then mutate the parent entity.

The basic idea was this:

```
input AddBookInput {
            ISBN: String!
            title: String!
        }
        
input RemoveBookInput {
            bookId: Int!
        }
        
input UpdateBookInput {
          ISBN: String!
          title: String!
      }
      
type AuthorOps {
          addBook(input: AddBookInput!): Int
          removeBook(input: RemoveBookInput! ): Boolean
          updateBook(input: UpdateBookInput!): Book
      }
      
type Mutation {
        Author(id: Int!): AuthorOps
      }
```

And I’ve used this technique a few times without ill effect, but I’ve been lucky. Where’s the problem?

[A reader pointed me](https://medium.com/@anddoutoi/hey-jeff-bca074856669) to [an issue](https://github.com/graphql/graphql-js/issues/221) on the GraphQL GitHub site where it was stated that the execution order of **nested mutations** is not guaranteed. Uh-oh. In the above case, I definitely want the **addBook**() mutation to occur before attempting an **updateBook**() operation on the same book. Alas, only so-called **root** **mutations** are guaranteed to execute in order.

### An illustration of the problem

Say I have a message queue where I want the messages stored in the order in which they were received. Some messages take longer to process, so I use a mutation to guarantee that messages are processed sequentially:

```
type Query {
  noop: String!
}

type Mutation {
  message(id: ID!, wait: Int!): String!
}
```

The resolver logs when the message arrives, then waits a given time before returning the mutation result:

```js
const msg = (id, wait) => new Promise(resolve => {
  setTimeout(() => {
    
console.log({id, wait})
    let message = `response to message ${id}, wait is ${wait} seconds`;
    
resolve(message);
  }, wait)
})

const resolvers = {
  Mutation: {
    message: (_, {id, wait}) => msg(id, wait),
  }
}
```

Now for the trial run. I will want to ensure that the console log messages are in the same order as the mutation requests. Here’s the request:

```js
mutation root {
  message1: message(id: 1, wait: 3000)
  message2: message(id: 2, wait: 1000)
  message3: message(id: 3, wait: 500)
  message4: message(id: 4, wait: 100)
}
```

The response is:

```json
{
  "data": {
    "message1": "response to message 1, wait is 3000 seconds",
    "message2": "response to message 2, wait is 1000 seconds",
    "message3": "response to message 3, wait is 500 seconds",
    "message4": "response to message 4, wait is 100 seconds"
  }
}
```

And the console log says:

```
{ id: '1', wait: 3000 }
{ id: '2', wait: 1000 }
{ id: '3', wait: 500 }
{ id: '4', wait: 100 }
```

Great! The messages are processed in the order in which they are received, even though the second and subsequent messages take less time than the previous. In other words, the mutations are executed sequentially.

#### The fly in the ointment

Now let’s nest these operations and see what happens. First I define a **MessageOps** type, then add a **Nested** mutation:

```
const typeDefs = `
type Query {
  noop: String!
}

type MessageOps {
  message(id: ID!, wait: Int!): String!
}

type Mutation {
  message(id: ID!, wait: Int!): String!
  Nested: MessageOps
}`
```

My mutations now go through the Nested resolver, returning MessageOps, which I then use to execute my message mutation:

```
mutation nested {
  Nested {
    message1: message(id: 1, wait: 3000)
    message2: message(id: 2, wait: 1000)
    message3: message(id: 3, wait: 500)
    message4: message(id: 4, wait: 100)
  }
}
```

Pretty similar to what we had before, and the response to the mutation request looks nearly the same as well:

```
{
  "data": {
    "Nested": {
      "message1": "response to message 1, wait is 3000 seconds",
      "message2": "response to message 2, wait is 1000 seconds",
      "message3": "response to message 3, wait is 500 seconds",
      "message4": "response to message 4, wait is 100 seconds"
    }
  }
}
```

The only difference is the responses are packaged up in a Nested JSON object. Sadly, the console reveals a tale of woe:

```
{ id: '4', wait: 100 }
{ id: '3', wait: 500 }
{ id: '2', wait: 1000 }
{ id: '1', wait: 3000 }
```

It reveals that the messages are processed out-of-sequence: the fastest-processing messages get posted first.

Alright. [In the code](https://github.com/JeffML/graphql-crud2) from my original post, I actually did something more like the following:

```
mutation nested2 {
  Nested {
    message1: message(id: 1, wait: 3000)
  }
  Nested {
    message2: message(id: 2, wait: 1000)
  }
  Nested {
    message3: message(id: 3, wait: 500)
  }
  Nested {
    message4: message(id: 4, wait: 100)
  }
}
```

Maybe this works? Every mutation operation is in it’s own Nested root mutation, so we might expect the Nested mutations to execute sequentially. The response is identical to the one before:

```
{
  "data": {
    "Nested": {
      "message1": "response to message 1, wait is 3000 seconds",
      "message2": "response to message 2, wait is 1000 seconds",
      "message3": "response to message 3, wait is 500 seconds",
      "message4": "response to message 4, wait is 100 seconds"
    }
  }
}
```

But so is the console log:

```
{ id: '4', wait: 100 }
{ id: '3', wait: 500 }
{ id: '2', wait: 1000 }
{ id: '1', wait: 3000 }
```

#### So what’s going on here?

The “problem” is that GraphQL executes a Nested mutation, returning an object with further mutation methods. Unfortunately, once that object is returned, GraphQL is off to the next mutation request, unaware that there are further mutation operations to be performed in the request.

GraphQL is elegantly simple, but simple comes at a cost. It’s conceivable that nested mutations could be supported, say by adding a **mutator** type (its corollary would be the [**input**](https://graphql.org/graphql-js/mutations-and-input-types/) type), which GraphQL would treat as an extension of the mutation operation. As it stands, there’s just not enough information in the mutation request to know that nested operations are mutators, also.

### Organizing GraphQL Mutations, part 2

You can still use the technique for operations that are not sequentially dependent, but that’s an assumption that’s likely to be brittle and hard to debug when violated. Perhaps schema [stitching](https://www.apollographql.com/docs/graphql-tools/schema-stitching.html) or [weaving](https://www.npmjs.com/package/graphql-weaver) offers an answer. I hope to explore these approaches in a future post.

The complete NodeJS application used for this post can be found [here](https://github.com/JeffML/nested_mutations).

