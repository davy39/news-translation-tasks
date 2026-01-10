---
title: Organizing GraphQL Mutations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T17:38:27.000Z'
originalURL: https://freecodecamp.org/news/organizing-graphql-mutations-653306699f3d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OYjAHBzgbgDRDFJeIrzr0Q.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jeff M Lowery

  Cleaning up the CRUD.

  Update (5/7/2018): Anders Ringqvist (comments) spotted an issue report that can
  cause problems when using this approach. Please see my follow up post.

  —

  The Great Divide in GraphQL schemas runs between Queries a...'
---

By Jeff M Lowery

Cleaning up the CRUD.

**_Update (5/7/2018):_** Anders Ringqvist (comments) spotted [an issue report](https://github.com/graphql/graphql-js/issues/221) that **can cause problems** when using this approach. Please see [my follow up post](https://www.freecodecamp.org/news/beware-of-graphql-nested-mutations-9cdb84e062b5/).

—

The Great Divide in GraphQL schemas runs between [Queries and Mutations](http://graphql.org/learn/queries/). A query method reads data from a datasource, such as a SQL database or file system or even a remote service. Whereas queries can be executed concurrently, mutations cannot.

Mutations have to execute sequentially because the next mutation operation may be dependent on data stored or updated by the previous mutation. For instance, a record has to be created before it can be updated. Therefore, mutations have to execute sequentially. This is why queries and mutations have their own namespace in GraphQL.

Queries are the ‘R’ in CRUD (Create, Read, Update, & Delete). The code in this article builds off of a [Launchpad example](https://launchpad.graphql.com/1jzxrj179). In the Launchpad code, there is a query defined that will return an Author’s Posts, given an author ID. I’ve extended this example once already on my post about [testing GraphQL interfaces](https://medium.freecodecamp.org/mocking-graphql-with-graphql-tools-42c2dd9d0364). In that post I added Books to the mix, and here I’ll extend that idea.

### Author Posts

Mutations are the CUD in CRUD. The Launchpad example linked above has an `**upvotePost**` mutation that bumps up the vote count (an update operation) for a Post.

```js
Mutation: {
    upvotePost: (_, { postId }) => {
      const post = find(posts, { id: postId });
      if (!post) {
        throw new Error(`Couldn't find post with id ${postId}`);
      }
      post.votes += 1;
      return post;
    },
  },
```

To implement down vote also, I simply create a similar `**downvotePost**` mutation:

```js
Mutation: {
...

  downvotePost: (_, { postId }) => {
      const post = find(posts, { id: postId });
      if (!post) {
        throw new Error(`Couldn't find post with id ${postId}`);
      }
      post.votes -= 1;
      return post;
    },
  },
```

This is not exactly a [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) way of doing it. The body of the logic could be put into one external function with a parameter to increment the vote up or down.

Also, I would like to get rid of the `upvotePost` and `downvotePost` naming and instead rely on a context, like `**Post.upvote()**` and `**Post.downvote()**`. That can be done by having the Mutation method return a set of operations that affect a given Post.

`PostOps` is a type defined as:

```js
type PostOps {
          upvote(postId: Int!): Post
          downvote(postId: Int!): Post
      }
```

The noun `**Post**` has been eliminated from the verb-noun name of the method as it is redundant. The resolver code operates in a Post context, via `PostOps`:

```js
const voteHandler = (postId, updown) => {
    return new Promise((resolve, reject) => {
        const post = posts.find(p => p.id === postId);
        if (!post) {
            reject(`Couldn't find post with id ${postId}`);
        }
        post.votes += updown;
        resolve(post);
    })
};

const PostOps =
    ({
        upvote: ({
            postId
        }) => voteHandler(postId, 1),
        downvote: ({
            postId
        }) => voteHandler(postId, -1)
    });
```

You’ll notice I use a new Promise in the resolver, though technically it isn’t required for this example. Nonetheless, most applications fetch data asynchronously, so… force of habit?

Now, instead of calling a mutation method directly at the root level, it is called within the context of a `Post`:

```js
mutation upvote {
  Post {
    upvote(postId: 3) {
      votes
    }
  }
}
```

And this returns:

```json
{
  "data": {
    "Post": {
      "upvote": {
        "votes": 2
      }
    }
  }
}
```

So far, so good. The methods could be DRYed up further by moving the `**postId**` argument to the top level:

```js
extend type Mutation {
        Post
(postId: Int!): PostOps
}

type PostOps {
          upvote: Post
          downvote: Post
      }
```

The `PostOp` resolvers would remain unchanged: they still take a `postId` parameter, but that parameter is passed from `Post` to `PostOps`. The next example will explain how this works in detail.

### Authors and Books

The Authors in my application not only author Posts, but some have authored Books as well. I want to perform classical Create, Update, and Delete operations on the list of books authored. The `AuthorOps` are then:

```js
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
```

In GraphQL, [Mutations take their own Input types](http://graphql.org/graphql-js/mutations-and-input-types/) as parameters. This is commonly necessary for entities that have autogenerated IDs. In the Query type, Author ID may be required, but in the AuthorInput type, it isn’t nor can it be (the ID is generated).

In this case, ISBN is the non-generated Book ID, so is included in `CreateBookInput`. Books also have an Author. Where is that going to come from? It turns out that `authorId` gets passed to the `addBook` resolver from the context from which the create operation is called, namely `AuthorOps`:

```js
extend type Mutation {
        Post: PostOps
        Author(id: Int!): AuthorOps
      }
```

The resolver for `AuthorOps` looks like:

```js
const addBook = (book, authorId) => {
    console.log("addBook", book, authorId)
    return new Promise((resolve, reject) => {
        book.authorId = authorId
        books.push(book)
        resolve(books.length)
    })
}

const removeBook = (book, authorId) => {
    return new Promise((resolve, reject) => {
        books = books.filter(b => b.ISBN !== book.ISBN && b.authorId === authorId);
        resolve(books.length)
    })
}

const updateBook = (book, authorId) => {
    return new Promise((resolve, reject) => {
        let old = books.find(b => b.ISBN === book.ISBN && b.authorId === authorId);
        if (!old) {
            reject(`Book with ISBN = ${book.ISBN} not found`)
            return
        }
        resolve(Object.assign(old, book))
    })
}

const AuthorOps = (authorId) => ({
    addBook: ({
        input
    }) => addBook(input, authorId),
    removeBook: ({
        input
    }) => removeBook(input, authorId),
    updateBook: ({
        input
    }) => updateBook(input, authorId)
})
```

Now let’s create a book and update it:

```js
mutation addAndUpdateBook {
  Author(id: 4) {
    
addBook(input: {ISBN: "922-12312455", title: "Flimwitz the Magnificent"})
  }
  Author(id: 4) {
    
updateBook(input: {ISBN: "922-12312455", title: "Flumwitz the Magnificent"}) {
      authorId
      title
    }
  }
}
```

The response is:

```json
{
  "data": {
    "Author": {
      "addBook": 4,
      "updateBook": {
        "authorId": 4,
        "title": "Flumwitz the Magnificent"
      }
    }
  }
}
```

#### What about “Book”?

You may notice that there is actually a subcontext at play. Notice that we have mutations named `**addBook**`, `**updateBook**`, `**removeBook**`. I could reflect this in the schema:

```js
type AuthorOps {
     Book: BookOps
}

type BookOps {
     add(input: AddBookInput!): Int
     remove(input: RemoveBookInput! ): Boolean
     update(input: UpdateBookInput!): Book
}
```

Nothing stops you from adding contexts as deep as you like, but be aware that the returned results are nested deeper each time this technique is used:

```json
>>> RESPONSE >>>
{
  "data": {
    "Author": {
       "Book": {

          "add": 4,
          "update": {
             "authorId": 4,
             "title": "Flumwitz the Magnificent"
          }
        }
     }
  }
}
```

This is quite similar to the structure GraphQL queries return, but for mutation operations deep hierarchies can get in the way: you have to “dig deep” to figure out if your mutation operation was successful. In some cases, a flatter response may be better. Still, a shallow organization of mutations in a few high-level contexts seems better than none.

Working source code for this post can be found [on my Github account](https://github.com/JeffML/graphql-crud2).

