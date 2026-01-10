---
title: How to Use TypeScript with GraphQL using TypeGraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-13T00:18:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-typescript-with-graphql
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-reagan-787642.jpg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  In this tutorial, I''ll explain what TypeScript and GraphQL are, and the benefits
  of using them.

  Then I''ll show you how you can use them together using TypeGrapQL, and why you''d
  want to do this.

  What is TypeScript?

  TypeScript is a su...'
---

By Dillion Megida

In this tutorial, I'll explain what TypeScript and GraphQL are, and the benefits of using them.

Then I'll show you how you can use them together using TypeGrapQL, and why you'd want to do this.

## What is TypeScript?

TypeScript is a superset of JavaScript that compiles to JavaScript for production. It's like JavaScript, but with powers – type powers.

TypeScript helps you build typed applications that help you avoid static type errors in those apps and make predictable code. 

Without TypeScript, a function declared to receive a string typed argument may receive a number typed argument during execution, and you may get a runtime error. This can be bad for production code.

With TypeScript, such a function will result in a compile-time error unless the appropriate type is passed.

TypeScript can handle more than primitive types. It can also ensure that correct, expected, structured objects are typed. This means a missing object property can also result in an error.

TypeScript helps us build more predictable JavaScript code during development through type-checking. It is also integrated into editors like VSCode, which makes it easier to spot type errors while writing code.

TypeScript takes an extra step to compile to JavaScript for use. While some libraries like React do this internally for you, you may have to set it up yourself if you're building without such tools. But I'd say it is worth it.

## What is GraphQL?

GraphQL is another method for managing APIs. It's an alternative to Rest APIs that allows you to request "only the data you need". This helps reduce the amount of data that needs to be sent to the client from the server.

For example, with a Rest API, an endpoint may return all users' data when only their email and phone number are needed at that point. This is termed "over-fetching". With GraphQL, the client can request such specific data.

GraphQL also comes with type definitions, which exist in schema objects. GraphQL uses Schema objects to know what properties are query-able, and basically, the type of queries that are accepted. It also throws an error when an unaccepted query is executed.

However, these type definitions to limited to schema objects. They do not give you overall static typing in your application. And that's why TypeScript is an excellent addition, as we'll see in the rest of this article.

## Advantages of Using TypeScript and GraphQL

Using TypeScript and GraphQL ensures that static typing exists all through your application.

Without TypeScript, you can still create query types with GraphQL. But there's a limitation to this.

GraphQL types only exist in the GraphQL schema. The `buildSchema` function from the GraphQL library is used to create the schema object:

```js
const schema = buildSchema(`
    type Query {
        name(firstname: String!, lastname: String!): String
    }
`)
```

We've created the schema object, and now we need a resolver:

```js
const root = {
    name: variables => {
        return `My name is ${firstname} ${lastname}!`
    },
}
```

On executing the query with wrongly typed variables in a GraphQL playground, we would get errors:


![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-4.png)
_GraphQL playground showing error for wrong type provided to query_

But the resolvers are not aware of the type definition in the schema object. As you can see, the resolver is a regular JavaScript function. This means, we don't get static typing in the resolver. 

Say, for example, we provide the wrong argument types to the resolver, or we return a different type from the resolver that the schema did not expect. We may introduce bugs to our code without knowing it.

And this is why TypeScript is beneficial. With TypeScript, we have type definitions in the schema object and in the resolvers, thereby synchronizing both of them and making our code much more predictable.

## How to Use TypeScript and GraphQL

In this section, we'll be using TypeScript and GraphQL to create a simple GraphQL API on an Express server.

### Step 1: Create a project folder

You can name it whatever you want, but we'll be using the `graphql-ts-example` folder for this tutorial:

```bash
mkdir graphql-ts-example
cd graphql-ts-example
npm init -y
```

### Step 2: Install dependencies

We'll use the following dependencies for this tutorial:

- [graphql](https://www.npmjs.com/package/graphql): the JavaScript library for GraphQL
- [express](https://www.npmjs.com/package/express): a web framework for Node that allows us to create APIs and a backend server
- [express-graphql](https://www.npmjs.com/package/express-graphql): for creating a GraphQL server for the APIs
- [ts-node](https://www.npmjs.com/package/ts-node): for executing TypeScript code in Node
- [typescript](https://www.npmjs.com/package/typescript): for compiling TypeScript code to JavaScript
- [@types/express](https://www.npmjs.com/package/@types/express): for using Express in TypeScript
- [nodemon](https://www.npmjs.com/package/nodemon): for restarting the server when changes are made

In your terminal, run:

```bash
npm install graphql express express-graphql
npm install -D nodemon ts-node @types/express typescript
```

For testing our API, we'll be using the GraphQL playground provided by express-graphql.

### Step 3: Setting up our scripts

In `package.json`, update the `scripts` object to this:

```json
"scripts": {
    "start": "nodemon --exec ts-node src/index.ts",
}
```

Also, add a configuration file for TypeScript, `tsconfig.json`:

```json
{
    "compilerOptions": {
        "target": "es2018",
        "module": "commonjs",
        "jsx": "preserve",
        "strict": true,
        "esModuleInterop": true,
        "lib": ["es2018", "esnext.asynciterable"]
    },
    "exclude": ["node_modules"]
}
```

With this, we can run our server with `npm start`.

### Step 4: Write the code

We'll create an Express server with a GraphQL API that allows us to fetch users, create a user, and update a user's data.

Create a new directory called "src" and add the `index.ts` file into it. We have our imports in the file as follows:

```js
import { buildSchema } from "graphql"
import express from "express"
import { graphqlHTTP } from "express-graphql"
```

Then we need our users list. Ideally, this would come from a database, but we'll hardcode it here:

```js
const users = [
    { id: 1, name: "John Doe", email: "johndoe@gmail.com" },
    { id: 2, name: "Jane Doe", email: "janedoe@gmail.com" },
    { id: 3, name: "Mike Doe", email: "mikedoe@gmail.com" },
]
```

Next, we build the GraphQL schema:

```js
const schema = buildSchema(`
    input UserInput {
        email: String!
        name: String!

    }

    type User {
        id: Int!
        name: String!
        email: String!
    }

    type Mutation {
        createUser(input: UserInput): User
        updateUser(id: Int!, input: UserInput): User
    }

    type Query {
        getUser(id: String): User
        getUsers: [User]
    }
`)
```

From our schema, we've defined:
* a user input with two required properties, which is required when creating a user
* a user type with three required properties
* a GraphQL mutation where we create users and update users
* and a GraphQL query for getting a particular user or all users.

Now, we need to define our TypeScript types for static typing:

```ts

type User = {
    id: number
    name: string
    email: string
}

type UserInput = Pick<User, "email" | "name">
```

Next, our resolvers:

```ts
const getUser = (args: { id: number }): User | undefined =>
    users.find(u => u.id === args.id)

const getUsers = (): User[] => users

const createUser = (args: { input: UserInput }): User => {
    const user = {
        id: users.length + 1,
        ...args.input,
    }
    users.push(user)

    return user
}

const updateUser = (args: { user: User }): User => {
    const index = users.findIndex(u => u.id === args.user.id)
    const targetUser = users[index]

    if (targetUser) users[index] = args.user

    return targetUser
}

const root = {
    getUser,
    getUsers,
    createUser,
    updateUser,
}
```

And finally, our Express route and server:

```ts
const app = express()

app.use(
    "/graphql",
    graphqlHTTP({
        schema: schema,
        rootValue: root,
        graphiql: true,
    })
)

const PORT = 8000

app.listen(PORT)

console.log(`Running a GraphQL API server at http://localhost:${PORT}/graphql`)
```

With what we have above, our resolvers are typed following the schema definition. This way, our resolvers are in sync. On `localhost:4000/graphql`, we can see the GraphQL playground:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-5.png)
_GraphQL playground showing working queries_

Although we can see how beneficial TypeScript is, we also cannot deny the hassle of writing type definitions after creating a schema object. 

This codebase is small, so that can be easier, but imagine something big, with many resolvers and having to create type definitions for each one 😩

We need a better way of doing this. We need something that allows us to create type definitions in one place, as the main source of truth, and then use them in our resolvers and schema objects.

## How to Use TypeGraphQL to Improve Your Typed GraphQL

The goal of [TypeGraphQL](https://typegraphql.com/) is to make it seamless to enjoy static typing in your resolvers and create your schemas from one place. 

It comes with its syntax, which is another learning process. But it's not so steep – it's a step in the right direction.

Let's improve our codebase by using TypeGraphQL.

We'd need a couple of dependencies:

* [class-validator](https://www.npmjs.com/package/class-validator): allows the use of [decorators](https://www.typescriptlang.org/docs/handbook/decorators.html) for validation
* [type-graphql](https://www.npmjs.com/package/type-graphql): the TypeGraphQL library itself, that allows you to create schemas and resolvers with TypeSCript, using classes and decorators
* [reflect-metadata](https://www.npmjs.com/package/reflect-metadata): for runtime reflection of types (learn more about this here: [Metadata reflection in TypeScript](http://blog.wolksoftware.com/decorators-metadata-reflection-in-typescript-from-novice-to-expert-part-4))

In your terminal, run:

```bash
npm install class-validator type-graphql reflect-metadata
```

In your `tsconfig.json`, add the following to the `compilerOptions` object:

```json
"compilerOptions": {
    // ...
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
}
```

These are important so that TypeScript doesn't complain about the use of decorators. They are still in experimental mode.

Now, let's update our codebase using TypeGraphQL. Create a new directory called "users". In it, we'll have the schema and resolvers.

Create a new file in "users" called "users.schema.ts":

```ts
// users.schema.ts

import { Field, ObjectType, InputType } from "type-graphql"

@ObjectType()
export class User {
    @Field()
    id!: number
    @Field()
    name!: string
    @Field()
    email!: string
}

@InputType()
export class UserInput implements Pick<User, "name" | "email"> {
    @Field()
    name!: string
    @Field()
    email!: string
}
```

First, we have the `User` class, which is decorated with the `ObjectType` decorator. This tells GraphQL that this class is a GraphQL type. In GraphQL, this is interpreted as:

```ts
buildSchema(`
    type User {
        id: Int!
        name: String!
        email: String!
    }

    input UserInput {
        name: String!
        email: String!
    }
`)
```

Next, our resolvers. Create a `users.resolvers.ts` file in the "users" directory:

```ts

// users.resolvers.ts

import { Query, Resolver, Mutation, Arg } from "type-graphql"
import { UserInput, User } from "./users.schema"

@Resolver(() => User)
export class UsersResolver {
    private users: User[] = [
        { id: 1, name: "John Doe", email: "johndoe@gmail.com" },
        { id: 2, name: "Jane Doe", email: "janedoe@gmail.com" },
        { id: 3, name: "Mike Doe", email: "mikedoe@gmail.com" },
    ]

    @Query(() => [User])
    async getUsers(): Promise<User[]> {
        return this.users
    }

    @Query(() => User)
    async getUser(@Arg("id") id: number): Promise<User | undefined> {
        const user = this.users.find(u => u.id === id)
        return user
    }

    @Mutation(() => User)
    async createUser(@Arg("input") input: UserInput): Promise<User> {
        const user = {
            id: this.users.length + 1,
            ...input,
        }
        
        this.users.push(user)
        return user
    }

    @Mutation(() => User)
    async updateUser(
        @Arg("id") id: number,
        @Arg("input") input: UserInput
    ): Promise<User> {
        const user = this.users.find(u => u.id === id)
        
        if (!user) {
            throw new Error("User not found")
        }

        const updatedUser = {
            ...user,
            ...input,
        }

        this.users = this.users.map(u => (u.id === id ? updatedUser : u))

        return updatedUser
    }
}
```

There are a few decorators to take note of here:

* there's the `Resolver` decorator, which decorates the class as an object with many query and mutation resolve methods. The beauty here is we're defining the queries and mutations and the resolve methods in the same class.
* there's the `Query` decorator, which tells GraphQL that this is a query and the respective resolve method
* there's the `Mutation` decorator, which tells GraphQL that this is a mutation and the respective resolve method
* there's the `Arg` decorator, which tells GraphQL that this argument is a GraphQL argument for the resolver.

As you'll notice, without creating a type definition for the `User` object, we could simply use the class exported from the schema file.

The above code will be interpreted to GraphQL as:

```ts
buildSchema(`
    type Query {
        getUsers: [User]
        getUser(id: Int!): User
    }

    type Mutation {
        createUser(input: UserInput): User
        updateUser(id: Int!, input: UserInput): User
    }
`)

// resolvers
```

Back in `src/index.ts`, here's what the code looks like:

```ts
import "reflect-metadata"
import { buildSchema } from "type-graphql"
import express from "express"
import { graphqlHTTP } from "express-graphql"

import { UsersResolver } from "./users/users.resolver"

async function main() {
    const schema = await buildSchema({
        resolvers: [UsersResolver],
        emitSchemaFile: true,
    })

    const app = express()

    app.use(
        "/graphql",
        graphqlHTTP({
            schema: schema,
            graphiql: true,
        })
    )

    app.listen(8000)

    console.log("Running a GraphQL API server at http://localhost:8000/graphql")
}

main()
```

The `buildSchema` function comes from the `type-graphql` library this time around. Back in the GraphQL playground, our queries work as expected:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-6.png)
_GraphQL playground showing GraphQL mutation for creating user_

Here's the GitHub repository for this project: [graphql-typescript-example](https://github.com/dillionmegida/graphql-typescript-example)

## Conclusion

In this article, we've learnt what GraphQL and TypeScript are, and seen the limitations of using GraphQL without TypeScript. 

We've also seen a beautiful way to use GraphQL and TypeScript together – TypeGraphQL.

If you found this helpful, kindly share it with others : )


