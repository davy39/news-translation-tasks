---
title: How to Use MongoDB + Mongoose with Node.js – Best Practices for Back End Devs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-27T00:17:19.000Z'
originalURL: https://freecodecamp.org/news/mongodb-mongoose-node-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/node-mongodb-fundamentals.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: mongoose
  slug: mongoose
- name: node js
  slug: node-js
seo_title: null
seo_desc: "By Mehul Mohan\nMongoDB is undoubtedly one of the most popular NoSQL database\
  \ choices today. And it has a great community and ecosystem. \nIn this article,\
  \ we'll review some of the best practices to follow when you're setting up MongoDB\
  \ and Mongoose wi..."
---

By Mehul Mohan

MongoDB is undoubtedly one of the most popular NoSQL database choices today. And it has a great community and ecosystem. 

In this article, we'll review some of the best practices to follow when you're setting up MongoDB and Mongoose with Node.js.

## Pre-requisites for this article

This article is one of the part codedamn's [backend learning path](https://codedamn.com/learning-paths/backend), where we start from backend basics and cover them in detail. Therefore I assume you have some experience with JavaScript (and Node.js) already. 

Currently we are here:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-20-at-9.29.47-PM.png)

If you have very little experience with Node.js/JavaScript or the back end in general, [this is probably a good place to start](https://codedamn.com/learning-paths/backend). You can also find a [free course on Mongoose + MongoDB + Node.js here](https://codedamn.com/learn/node-mongodb-fundamentals). Let's dive in.

## Why do you need Mongoose?

To understand why we need Mongoose, let's understand how MongoDB (and a database) works on the architecture level.

* You have a database server (MongoDB community server, for example)
* You have a Node.js script running (as a process)

MongoDB server listens on a TCP socket (usually), and your Node.js process can connect to it using a TCP connection. 

But on the top of TCP, MongoDB also has its own protocol for understanding what exactly the client (our Node.js process) wants the database to do.

For this communication, instead of learning the messages we have to send on the TCP layer, we abstract that away with the help of a "driver" software, called MongoDB driver in this case. MongoDB driver is available as an [npm package here](https://www.npmjs.com/package/mongodb).

Now remember, the MongoDB driver is responsible for connecting and abstracting the low level communication request/responses from you – but this only gets you so far as a developer. 

Because MongoDB is a schemaless database, it gives you way more power than you need as a beginner. More power means more surface area to get things wrong. You need to reduce your surface area of bugs and screw-ups you can make in your code. You need something more.

Meet Mongoose. Mongoose is an abstraction over the native MongoDB driver (the npm package I mentioned above). 

The general rule of thumb with abstractions (the way I understand) is that with every abstraction you lose some low-level operation power. But that doesn't necessarily mean it is bad. Sometimes it boosts productivity 1000x+ because you never really need to have full access to the underlying API anyway.

A good way to think about it is you technically create a realtime chat app both in C and in Python. 

The Python example would be much easier and faster for you as a developer to implement with higher productivity. 

C _might_ be more efficient, but it'll come at a huge cost in productivity/speed of development/bugs/crashes. Plus, for the most part you don't need to have the power C gives you to implement websockets.

Similarly, with Mongoose, you can limit your surface area of lower level API access, but unlock a lot of potential gains and good DX.

## How to connect Mongoose + MongoDB

Firstly, let's quickly see how you should connect to your MongoDB database in 2020 with Mongoose:

```js
mongoose.connect(DB_CONNECTION_STRING, {
	useNewUrlParser: true,
	useUnifiedTopology: true,
	useCreateIndex: true,
	useFindAndModify: false
})
```

This connection format makes sure that you're using the new URL Parser from Mongoose, and that you are not using any deprecated practices. You can read in depth about all these deprecation messages [here](https://mongoosejs.com/docs/deprecations.html) if you like.

## How to perform Mongoose operations

Let's now go ahead and quickly discuss operations with Mongoose, and how you should perform them.

Mongoose gives you options for two things:

1. Cursor-based querying
2. Full fetching query

### Cursor-based querying

Cursor-based querying means that you work with a single record at a time while you fetch a single or a batch of documents at a time from the database. This is an efficient way of working with huge amounts of data in a limited memory environment. 

Imagine that you have to parse documents of 10GB in total size on a 1GB/1core cloud server. You cannot fetch the whole collection because that will not fit on your system. Cursor is a good (and the only?) option here.

### Full fetching querying

This is the type of query where you get the full response of your query all at once. For the most part, this is what you'll be using. Therefore, we'll be focusing mostly on this method here.

## How to use Mongoose Models

Models are the superpower of Mongoose. They help you enforce "schema" rules and provide a seamless integration of your Node code into database calls. 

The very first step is to define a good model:

```
import mongoose from 'mongoose'

const CompletedSchema = new mongoose.Schema(
	{
		type: { type: String, enum: ['course', 'classroom'], required: true },
		parentslug: { type: String, required: true },
		slug: { type: String, required: true },
		userid: { type: String, required: true }
	},
	{ collection: 'completed' }
)

CompletedSchema.index({ slug: 1, userid: 1 }, { unique: true })

const model = mongoose.model('Completed', CompletedSchema)
export default model

```

This is one trimmed down example directly from codedamn's codebase. A few interesting things you should note here:

1. Try to keep `required: true` on all fields which are required. This can be a huge pain saver for you if you don't use a static type checking system like TypeScript to assist you with correct property names while creating an object. Plus the free validation is super cool, too.
2. Define indexes and unique fields. `unique` property can also be added within a schema. Indexes are a broad topic, so I will not go into depth here. But on a large scale they can really help you to speed up your queries a lot.
3. Define a collection name explicitly. Although Mongoose can automatically give a collection name based on the name of model (`Completed` here, for example), this is way too much abstraction in my opinion. You should at least know about your database names and collections in your codebase.
4. Restrict values if you can, using enums.

## How to perform CRUD Operations

CRUD means **C**reate, **R**ead, **U**pdate and **D**elete. These are the four fundamental options with which you can perform any sort of data manipulation in a database. Let's quickly see some examples of these operations.

### The Create Operation

This simply means creating a new record in a database. Let's use the model we defined above to create a record:

```js
try {
    const res = await CompletedSchema.create(record)
} catch(error) {
	console.error(error)
    // handle the error
}
```

Again, a few pointers here:

1. Use async-await instead of callbacks (nice on the eyes, no ground breaking performance benefit as such)
2. Use try-catch blocks around queries because your query _can_ fail for a number of reasons (duplicate record, incorrect value, and so on)

### The Read Operation

This means reading existing values from the database. it's simple just like it sounds, but there are a couple of gotchas you should know with Mongoose:

```
const res = await CompletedSchema.find(info).lean()
```

1. Can you see the `lean()` function call there? It is super useful for performance. By default, Mongoose processes the returned document(s) from the database and adds its _magical_ methods on it (for example `.save`)
2. When you use `.lean()`, Mongoose returns plain JSON objects instead of memory and resource heavy documents. Makes queries faster and less expensive on your CPU, too.
3. However, you can omit `.lean()` if you are actually thinking of updating data (we'll see that next)

### The Update Operation

If you already have a Mongoose document with you (without firing with `.lean()`), you can simply go ahead and modify the object property, and save it using `object.save()`:

```
const doc = await CompletedSchema.findOne(info)
doc.slug = 'something-else'
await doc.save()
```

Remember that here, there are two database calls made. The first one is on `findOne` and the second one is on `doc.save`. 

If you can, you should always reduce the number of requests hitting the database (because if you're comparing memory, network, and disk, network is almost always the slowest).

In the other case, you can use a query like this:

```
const res = await CompletedSchema.updateOne(<condition>, <query>).lean()
```

and it will only make a single call to the database.

### The Delete Operation

Delete is also straightforward with Mongoose. Let's see how you can delete a single document:

```js
const res = await CompletedSchema.deleteOne(<condition>)
```

Just like `updateOne`, `deleteOne` also accepts the first argument as the matching condition for the document. 

There is also another method called `deleteMany` which should be used only when you know you want to delete multiple documents. 

In any other case, always use `deleteOne` to avoid accidental multiple deletes, especially when you're trying to execute queries yourself. 

## Conclusion

This article was a simple introduction to the Mongoose and MongoDB world for Node.js developers. 

If you enjoyed this article, you can step up your game even more as a developer by following the [codedamn backend learning path](https://codedamn.com/learning-paths/backend). Please feel free to reach out to me on [Twitter](https://twitter.com/mehulmpt) for any feedback!

