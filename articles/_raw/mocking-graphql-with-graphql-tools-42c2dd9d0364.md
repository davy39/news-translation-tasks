---
title: Mocking GraphQL with graphql-tools+
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-03T23:15:48.000Z'
originalURL: https://freecodecamp.org/news/mocking-graphql-with-graphql-tools-42c2dd9d0364
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb38c740569d1a4cac9a0.jpg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Mocking
  slug: mocking
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Jeff M Lowery

  How to mock up your GraphQL API with realistic values

  In my last article, I took the original Apollo LaunchPad Posts and Authors API and
  broke it down into domains and components. I wanted to illustrate how one could
  organize a large...'
---

By Jeff M Lowery

#### How to mock up your GraphQL API with realistic values

In [my last article,](https://medium.com/@jefflowery/declarative-graphql-with-graphql-tools-cd1645f94fc) I took the original Apollo LaunchPad [Posts and Authors API](https://launchpad.graphql.com/1jzxrj179) and broke it down into domains and components. I wanted to illustrate how one could organize a large GraphQL project using [graphql-tools](https://github.com/apollographql/graphql-tools).

Now I’d like the API to return mock data when I query it. How?

### The original source

In the original Apollo Launchpad example, we used static data structures and simple mapping resolvers to provide output for queries.

For instance, given this query:

```graphql
# Welcome to GraphiQL

query PostsForAuthor {
  author(id: 1) {
    firstName
    posts {
      title
      votes
    }
  }
}
```

The output would be:

```json
{
  "data": {
    "author": {
      "firstName": "Tom",
      "posts": [
        {
          "title": "Introduction to GraphQL",
          "votes": 2
        }
      ]
    }
  }
}
```

The resolvers object has functions that take care of mapping authors to posts and visa-versa. It’s not truly a mock, though.

The problem is that the more relationships and the more complex the entities become, the more code needs to go into the resolvers. Then more data needs to be provided.

When it comes to testing, tests are likely to sometimes reveal problems in the data or in the resolvers. You really want focus testing of the API itself.

### Using mocks

There are three Node.js modules that make mocking an API quick and easy. The first is part of the `graphql-tools` module. Using this module, a beginning step is to require or import the method `addMockFunctionsToSchema` from the module into the root `schema.js` file:

```js
import {
    makeExecutableSchema,
    addMockFunctionsToSchema
} from 'graphql-tools';
```

Then, after creating an executable `schema` by calling `createExecutableSchema`, you add your mocks like so:

```js
    addMockFunctionsToSchema({
        schema: executableSchema,
    })
```

Here’s a full listing of the root `schema.js`:

```js
// This example demonstrates a simple server with some relational data: Posts and Authors. You can get the posts for a particular author,
// and vice-versa Read the complete docs for graphql-tools here: http://dev.apollodata.com/tools/graphql-tools/generate-schema.html

import {
    makeExecutableSchema,
    addMockFunctionsToSchema
} from 'graphql-tools';

import {
    schema as authorpostsSchema,
    resolvers as authorpostsResolvers
} from './authorposts';

import {
    schema as myLittleTypoSchema,
    resolvers as myLittleTypeResolvers
} from './myLittleDomain';

import {
    merge
} from 'lodash';

const baseSchema = [
    `
    type Query {
        domain: String
    }
    type Mutation {
        domain: String
    }
    schema {
        query: Query,
        mutation: Mutation
    }`
]

// Put schema together into one array of schema strings and one map of resolvers, like makeExecutableSchema expects
const schema = [...baseSchema, ...authorpostsSchema, ...myLittleTypoSchema]

const options = {
    typeDefs: schema,
    resolvers: merge(authorpostsResolvers, myLittleTypeResolvers)
}

const executableSchema = makeExecutableSchema(options);

addMockFunctionsToSchema({
    schema: executableSchema
})

export default executableSchema;
```

So what’s the output? Executing the same query as before yields:

```json
{
  "data": {
    "author": {
      "firstName": "Hello World",
      "posts": [
        {
          "title": "Hello World",
          "votes": -70
        },
        {
          "title": "Hello World",
          "votes": -77
        }
      ]
    }
  }
}
```

Well, that’s kind of dumb. Every string is “Hello World”, votes are negative, and there will always be exactly two posts per author. We’ll fix that, but first…

#### Why use mocks?

Mocks are often used in unit tests to separate the functionality being tested from the dependencies that those functions rely on. You want to test the function (the unit), not a whole complex of functions.

At this early stage of development, mocks serve another purpose: to test the tests. In a basic test, you want to ensure first that the test is calling the API correctly, and that the results returned have the expected structure, properties, and types. I think the cool kids call this “shape”.

This offers more limited testing than a queryable data structure, because reference semantics are not enforced. `id` is meaningless. Nonetheless, mocks offer something to structure your tests around

### Realistic mocking

There’s a module called [casual](https://github.com/boo1ean/casual) that I really like. It provides reasonable and variable values for a lot of common data types. If you are demonstrating your new API in front of jaded colleagues, it actually looks like you’ve done something special.

Here’s a wish list for mock values to display:

1. Author’s first name should be **first-name-like**
2. Post titles should be variable **lorem ipsum** text of limited length
3. votes should be positive or zero
4. the number of posts should vary between 1 and 7

First thing is to create a folder called `mocks`. Next, we’ll add an `index.js` file to that folder with the mock methods. Finally, the custom mocks will be added to the generated executable schema.

The **casual** library can generate values by data type (`String, ID, Int, …`) or by property name. Also, graphql-tools MockList object will be used to vary the number of items in a list — in this case `posts`. So let’s start.

`Import` both casual and MockList into `/mocks/index.js`:

```js
import casual from 'casual';
import {
    MockList
} from 'graphql-tools';
```

Now let create a default export with the following properties:

```js
export default {
    Int: () => casual.integer(0),
    
    Author: () => ({
        firstName: casual.first_name,
        posts: () => new MockList([1, 7])
    }),
    
    Post: () => ({
        title: casual.title
    })
}
```

The `Int` declaration takes care of all integer types appearing in our schema and it will ensure that `Post.votes` will be positive or zero.

Next, `Author.firstName` will be a reasonable first name. MockList is used to ensure the number of posts associated with each Author will be between 1 and 7. Finally, casual will generate a **lorem ipsum** `title` for each `Post`.

Now the generated output varies each time the query is executed. And it looks credible:

```json
{
  "data": {
    "author": {
      "firstName": "Eldon",
      "posts": [
        {
          "title": "Voluptatum quae laudantium",
          "votes": 581
        },
        {
          "title": "Vero quos",
          "votes": 85
        },
        {
          "title": "Doloribus labore corrupti",
          "votes": 771
        },
        {
          "title": "Qui nulla qui",
          "votes": 285
        }
      ]
    }
  }
}
```

### Generating custom values

I just scratched the surface of what casual can do, but it is well-documented and there’s nothing much to add.

Sometimes, though, there are values that have to conform to a standard format. I would like to introduce one more module: [randexp](https://www.npmjs.com/package/randexp).

randexp allows you to generate values conforming to the regexp expression you provide it. For instance, ISBN numbers have the format:

**/ISBN-\d-\d{3}-\d{5}-\d/**

Now I can add Books to the schema, add books to Author, and generate ISBN and title for each `Book`:

```js
// book.js
export default `
  type Book {
    ISBN: String
    title: String
}
```

mocks.js:

```js
import casual from 'casual';
import RandExp from 'randexp';
import {
    MockList
} from 'graphql-tools';
import {
    startCase
} from 'lodash';

export default {
    Int: () => casual.integer(0),
    
Author: () => ({
        firstName: casual.first_name,
        posts: () => new MockList([1, 7]),
        books: () => new MockList([0, 5])
    }),
    
Post: () => ({
        title: casual.title
    }),
    
Book: () => ({
        ISBN: new RandExp(/ISBN-\d-\d{3}-\d{5}-\d/)
            .gen(),
        title: startCase(casual.title)
    })
}
```

And here’s a new query:

```graphql
query PostsForAuthor {
  author(id: 1) {
    firstName
    posts {
      title
      votes
    }
    books {
      title
      ISBN
    }
  }
}
```

Sample response:

```json
{
  "data": {
    "author": {
      "firstName": "Rosemarie",
      "posts": [
        {
          "title": "Et ipsum quo",
          "votes": 248
        },
        {
          "title": "Deleniti nihil",
          "votes": 789
        },
        {
          "title": "Aut aut reprehenderit",
          "votes": 220
        },
        {
          "title": "Nesciunt debitis mollitia",
          "votes": 181
        }
      ],
      "books": [
        {
          "title": "Consequatur Veniam Voluptas",
          "ISBN": "ISBN-0-843-74186-9"
        },
        {
          "title": "Totam Et Iusto",
          "ISBN": "ISBN-6-532-70557-3"
        },
        {
          "title": "Voluptatem Est Sunt",
          "ISBN": "ISBN-2-323-13918-2"
        }
      ]
    }
  }
}
```

So that’s the basics of mocking using graphql-tools plus a couple of other useful modules .

**Note**: I use snippets throughout this post. If you want to follow along in a broader context, sample code is [here](https://github.com/JeffML/graphql_authors_mock).

The [Full source](https://github.com/JeffML/graphql_authors_mock) is on GitHub for your perusal.

Give me a hand if you found this article informative.

