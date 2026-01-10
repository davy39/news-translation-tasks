---
title: A Beginner’s Guide to GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T18:31:55.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-graphql-86f849ce1bec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sbPjm_cUHedMps6Kdy2F-A.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Leonardo Maldonado

  One of the most commonly discussed terms today is the API. A lot of people don’t
  know exactly what an API is. Basically, API stands for Application Programming Interface.
  It is, as the name says, an interface with which people —...'
---

By Leonardo Maldonado

One of the most commonly discussed terms today is the API. A lot of people don’t know exactly what an API is. Basically, API stands for **Application Programming Interface.** It is, as the name says, an interface with which people — developers, users, consumers — can interact with data.

You can think of an API as a bartender. You ask the bartender for a drink, and they give you what you wanted. Simple. So why is that a problem?

Since the start of the modern web, building APIs has not been as hard as it sounds. But learning and understanding APIs was. Developers form the majority of the people that will use your API to build something or just consume data. So your API should be as clean and as intuitive as possible. A well-designed API is very easy to use and learn. It’s also intuitive, a good point to keep in mind when you’re starting to design your API.

We’ve been using REST to build APIs for a long time. Along with that comes some problems. When building an API using REST design, you’ll face some problems like:

1) you’ll have a lot of endpoints

2) it’ll be much harder for developers to learn and understand your API

3) there is over- and under-fetching of information

To solve these problems, Facebook created GraphQL. Today, I think GraphQL is the best way to build APIs. This article will tell you why you should start to learn it today.

In this article, you’re going to learn how GraphQL works. I’m going to show you how to create a very well-designed, efficient, powerful API using GraphQL.

You’ve probably already heard about GraphQL, as a lot of people and companies are using it. Since GraphQL is open-source, its community has grown huge.

Now, it’s time for you start to learn in practice how GraphQL works and all about its magic.

### What is GraphQL?

[GraphQL](https://graphql.org) is an open-source query language developed by Facebook. It provides us with a more efficient way design, create, and consume our APIs. Basically, it’s the replacement for REST.

GraphQL has a lot of features, like:

1. You write the data that you want, and you get exactly the data that you want. **No more over-fetching of information** as we are used to with REST.
2. It gives us a **single endpoint**, no more version 2 or version 3 for the same API.
3. GraphQL is **strongly-typed**, and with that you can validate a query within the GraphQL type system before execution. It helps us build more powerful APIs.

This is a basic introduction to GraphQL — why it’s so powerful and why it’s gaining a lot of popularity these days. If you want to learn more about it, I recommend you to go the [GraphQL website](https://graphql.org/) and check it out.

### Getting started

The main objective in this article is not to learn how to set up a GraphQL server, so we’re not getting deep into that for now. The objective is to learn how GraphQL works in practice, so we’re gonna use a zero-configuration GraphQL server called ☄️ [Graphpack](https://github.com/glennreyes/graphpack).

To start our project, we’re going to create a new folder and you can name it whatever you want. I’m going to name it `graphql-server`:

Open your terminal and type:

```
mkdir graphql-server
```

Now, you should have _npm_ or _yarn_ installed in your machine. If you don’t know what these are, _npm_ and _yarn_ are package managers for the JavaScript programming language. For Node.js, the default package manager is _npm_.

Inside your created folder type the following command:

```
npm init -y
```

Or if you use yarn:

```
yarn init 
```

npm will create a `package.json` file for you, and all the dependencies that you installed and your commands will be there.

So now, we’re going to install **the only dependency** that we’re going to use.

☄️[Graphpack](https://github.com/glennreyes/graphpack) lets you create a GraphQL server **with zero configuration**. Since we’re just starting with GraphQL, this will help us a lot to go on and learn more without getting worried about a server configuration.

In your terminal, inside your root folder, install it like this:

```
npm install --save-dev graphpack
```

Or, if you use yarn, you should go like this:

```
yarn add --dev graphpack
```

After Graphpack is installed, go to our scripts in `package.json` file, and put the following code there:

```js
"scripts": {
    "dev": "graphpack",
    "build": "graphpack build"
}
```

We’re going to create a folder called `src`, and it’s going to be the only folder in our entire server.

Create a folder called `src`, after that, inside our folder, we’re going to create three files only.

Inside our `src` folder create a file called `schema.graphql`. Inside this first file, put the following code:

```js
type Query {
  hello: String
}
```

In this `schema.graphql` file is going to be our entire GraphQL schema. If you don’t know what it is, I’ll explain later — don't worry.

Now, inside our `src` folder, create a second file. Call it `resolvers.js` and, inside this second file, put the following code:

```js
import { users } from "./db";

const resolvers = {
  Query: {
    hello: () => "Hello World!"
  }
};

export default resolvers;
```

This `resolvers.js` file is going to be the way we provide the instructions for turning a GraphQL operation into data.

And finally, inside your `src` folder, create a third file. Call this `db.js` and, inside this third file, put the following code:

```js
export let users = [
  { id: 1, name: "John Doe", email: "john@gmail.com", age: 22 },
  { id: 2, name: "Jane Doe", email: "jane@gmail.com", age: 23 }
];
```

In this tutorial we’re not using a real-world database. So this `db.js` file is going to simulate a database, just for learning purposes.

Now our `src` folder should look like this:

```
src
  |--db.js
  |--resolvers.js
  |--schema.graphql
```

Now, if you run the command `npm run dev` or, if you’re using yarn, `yarn dev`, you should see this output in your terminal:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FKJYY9qqg4PLBvziWPlhVg.png)

You can now go to `localhost:4000` . This means that we’re ready to go and start writing our first queries, mutations, and subscriptions in GraphQL.

You see the GraphQL Playground, a powerful GraphQL IDE for better development workflows. If you want to learn more about GraphQL Playground, [click here](https://www.prisma.io/blog/introducing-graphql-playground-f1e0a018f05d/).

### Schema

GraphQL has its own type of language that’s used to write schemas. This is a human-readable schema syntax called Schema Definition Language (SDL). The SDL will be the same, no matter what technology you’re using — you can use this with any language or framework that you want.

This schema language its very helpful because it’s simple to understand what types your API is going to have. You can understand it just by looking right it.

### Types

Types are one of the most important features of GraphQL. Types are custom objects that represent how your API is going to look. For example, if you’re building a social media application, your API should have types such as `Posts`, `Users`, `Likes`, `Groups`.

Types have fields, and these fields return a specific type of data. For example, we’re going to create a User type, we should have some `name`, `email`, and `age` fields. Type fields can be anything, and always return a type of data as Int, Float, String, Boolean, ID, a List of Object Types, or Custom Objects Types_._

So now to write our first Type, go to your `schema.graphql` file and replace the type Query that is already there with the following:

```js
type User {
  id: ID!
  name: String!
  email: String!
  age: Int
}
```

Each `User` is going to have an `ID`, so we gave it an `ID` type. `User` is also going to have a `name` and `email`, so we gave it a `String` type, and an `age`, which we gave an `Int` type. Pretty simple, right?

But, what about those `!` at the end of every line? The exclamation point means that the fields are **non-nullable**, which means that every field must return some data in each query. The only **nullable** field that we’re going to have in our `User` type will be `age`.

In GraphQL, you will deal with three main concepts:

1. **queries** — the way you’re going to get data from the server.
2. **mutations** — the way you’re going to modify data on the server and get updated data back (create, update, delete).
3. **subscriptions** — the way you’re going to maintain a real-time connection with the server.

I’m going to explain all of them to you. Let’s start with Queries.

### Queries

To explain this in a simple way, queries in GraphQL are how you’re going to get data. One of the most beautiful things about queries in GraphQL is that you are just going to get the exact data that you want. No more, no less. This has a huge positive impact in our API — no more over-fetching or under-fetching information as we had with REST APIs.

We’re going to create our first type Query in GraphQL. All our queries will end up inside this type. So to start, we’ll go to our `schema.graphql` and write a new type called `Query`:

```js
type Query {
  users: [User!]!
}
```

It’s very simple: the `users` query will return to us an array of one or more `Users`**_._** It will not return null, because we put in the `!` , which means it’s a non-nullable query. It should always return something.

But we could also return a specific user. For that we’re going to create a new query called `user`. Inside our `Query` type, put the following code:

```js
user(id: ID!): User!

```

Now our `Query` type should look like this:

```js
type Query {
  users: [User!]!
  user(id: ID!): User!
}
```

As you see, with queries in GraphQL we can also pass arguments. In this case, to query for a specific `user`, we’re going to pass its `ID`.

But, you may be wondering: how does GraphQL know where get the data? That’s why we should have a `resolvers.js` file. That file tells GraphQL how and where it's going to fetch the data.

First, go to our `resolvers.js` file and import the `db.js` that we just created a few moments ago. Your `resolvers.js` file should look like this:

```js
import { users } from "./db";

const resolvers = {
  Query: {
    hello: () => "Hello World!"
  }
};

export default resolvers;
```

Now, we’re going to create our first Query. Go to your `resolvers.js` file and replace the `hello` function. Now your Query type should look like this:

```js
import { users } from "./db";

const resolvers = {
  Query: {
    user: (parent, { id }, context, info) => {
      return users.find(user => user.id == id);
    },
    users: (parent, args, context, info) => {
      return users;
    }
  }
};

export default resolvers;
```

Now, to explain how is it going to work:

Each query resolver has four arguments. In the `user` function, we’re going to pass `id` as an argument, and then return the specific `user` that matches the passed `id`. Pretty simple.

In the `users` function, we’re just going to return the `users` array that already exists. It’ll always return to us all of our users.

Now, we’re going to test if our queries are working fine. Go to `localhost:4000` and put in the following code:

```js
query {
  users {
    id
    name
    email
    age
  }
}
```

It should return to you all of our users.

Or, if you want to return a specific user:

```js
query {
  user(id: 1) {
    id
    name
    email
    age
  }
}
```

Now, we’re going to start learning about **mutations**, one of the most important features in GraphQL.

### Mutations

In GraphQL, mutations are the way you’re going to modify data on the server and get updated data back. You can think like the CUD (Create, Update, Delete) of REST.

We’re going to create our first type mutation in GraphQL, and all our mutations will end up inside this type. So, to start, go to our `schema.graphql` and write a new type called `mutation`:

```js
type Mutation {
  createUser(id: ID!, name: String!, email: String!, age: Int): User!
  updateUser(id: ID!, name: String, email: String, age: Int): User!
  deleteUser(id: ID!): User!
}
```

As you can see, we’re going to have three mutations:

`createUser`: we should pass an `ID`, `name`, `email`, and `age`. It should return a new user to us.

`updateUser`: we should pass an `ID`, and a new `name`, `email`, or `age`. It should return a new user to us.

**deleteUser**: we should pass an `ID.` It should return a new user to us.

Now, go to our `resolvers.js` file and **below** the `Query` object, create a new `mutation` object like this:

```js
Mutation: {
    createUser: (parent, { id, name, email, age }, context, info) => {
      const newUser = { id, name, email, age };

      users.push(newUser);

      return newUser;
    },
    updateUser: (parent, { id, name, email, age }, context, info) => {
      let newUser = users.find(user => user.id === id);

      newUser.name = name;
      newUser.email = email;
      newUser.age = age;

      return newUser;
    },
    deleteUser: (parent, { id }, context, info) => {
      const userIndex = users.findIndex(user => user.id === id);

      if (userIndex === -1) throw new Error("User not found.");

      const deletedUsers = users.splice(userIndex, 1);

      return deletedUsers[0];
    }
  }
```

Now, our `resolvers.js` file should look like this:

```js
import { users } from "./db";

const resolvers = {
  Query: {
    user: (parent, { id }, context, info) => {
      return users.find(user => user.id == id);
    },
    users: (parent, args, context, info) => {
      return users;
    }
  },
  Mutation: {
    createUser: (parent, { id, name, email, age }, context, info) => {
      const newUser = { id, name, email, age };

      users.push(newUser);

      return newUser;
    },
    updateUser: (parent, { id, name, email, age }, context, info) => {
      let newUser = users.find(user => user.id === id);

      newUser.name = name;
      newUser.email = email;
      newUser.age = age;

      return newUser;
    },
    deleteUser: (parent, { id }, context, info) => {
      const userIndex = users.findIndex(user => user.id === id);

      if (userIndex === -1) throw new Error("User not found.");

      const deletedUsers = users.splice(userIndex, 1);

      return deletedUsers[0];
    }
  }
};

export default resolvers;
```

Now, we’re going to test if our mutations are working fine. Go to `localhost:4000` and put in the following code:

```js
mutation {
  createUser(id: 3, name: "Robert", email: "robert@gmail.com", age: 21) {
    id
    name
    email
    age
  }
}
```

It should return a new user to you. If you want to try making new mutations, I recommend you to try for yourself! Try to delete this same user that you created to see if it’s working fine.

Finally, we’re going to start learning about **subscriptions**, and why they are so powerful.

### Subscriptions

As I said before, subscriptions are the way you’re going to maintain a real-time connection with a server. That means that whenever an event occurs in the server and whenever that event is called, the server will send the corresponding data to the client.

By working with subscriptions, you can keep your app updated to the latest changes between different users.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NaIPy126r9Ie5NwjS3g-rg.png)

A basic subscription is like this:

```js
subscription {
  users {
    id
    name
    email
    age
  }
}
```

You will say it’s very similar to a query, and yes it is. But it works differently.

When something is updated in the server, the server will run the GraphQL query specified in the subscription, and send a newly updated result to the client.

We’re not going to work with subscriptions in this specific article, but if you want to read more about them [click here](https://hackernoon.com/from-zero-to-graphql-subscriptions-416b9e0284f3).

### Conclusion

As you have seen, GraphQL is a new technology that is really powerful. It gives us real power to build better and well-designed APIs. That’s why I recommend you start to learn it now. For me, it will eventually replace REST.

Thanks for reading the article.

[**Follow me on Twitter!**](https://twitter.com/leonardomso)   
[**Follow me on GitHub!**](https://github.com/leonardomso)

I’m looking for a remote opportunity, so if have any I’d love to hear about it, so please contact me at my [**Twitter**](https://twitter.com/leonardomso)!

