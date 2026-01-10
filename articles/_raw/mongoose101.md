---
title: 'Mongoose 101: An Introduction to the Basics, Subdocuments, and Population'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2020-01-22T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/mongoose101
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d9f740569d1a4ca38bb.jpg
tags:
- name: mongoose
  slug: mongoose
seo_title: null
seo_desc: "Mongoose is a library that makes MongoDB easier to use. It does two things:\n\
  \nIt gives structure to MongoDB Collections\nIt gives you helpful methods to use\n\
  \nIn this article, we'll go through: \n\nThe basics of using Mongoose \nMongoose\
  \ subdocuments\nMongo..."
---

Mongoose is a library that makes MongoDB easier to use. It does two things:

1. It gives structure to MongoDB Collections
2. It gives you helpful methods to use

In this article, we'll go through: 

1. The basics of using Mongoose 
2. Mongoose subdocuments
3. Mongoose population

By the end of the article, you should be able to use Mongoose without problems.  

## Prerequisites

I assume you have done the following:

1. You have installed MongoDB on your computer
2. You know how to set up a local MongoDB connection
3. You know how to see the data you have in your database
4. You know what "collections" are in MongoDB

If you don't know any of these, please read ["How to set up a local MongoDB connection"](https://zellwk.com/blog/local-mongodb) before you continue.

I also assume you know how to use MongoDB to create a simple CRUD app. If you don't know how to do this, please read ["How to build a CRUD app with Node, Express, and MongoDB"](https://zellwk.com/blog/crud-express-mongodb) before you continue.

## Mongoose Basics

Here, you'll learn how to: 

1. Connect to the database
2. Create a Model
3. Create a Document
4. Find a Document
5. Update a Document
6. Delete a Document

### Connecting to a database

First, you need to download Mongoose.

```bash
npm install mongoose --save
```

You can connect to a database with the `connect` method. Let's say we want to connect to a database called `street-fighters`. Here's the code you need:

```js
const mongoose = require('mongoose')
const url = 'mongodb://127.0.0.1:27017/street-fighters'

mongoose.connect(url, { useNewUrlParser: true })
```

We want to know whether our connection has succeeded or failed. This helps us with debugging.

To check whether the connection has succeeded, we can use the `open` event. To check whether the connection failed, we use the `error` event.

```js
const db = mongoose.connection
db.once('open', _ => {
  console.log('Database connected:', url)
})

db.on('error', err => {
  console.error('connection error:', err)
})
```

Try connecting to the database. You should see a log like this:

<img src="https://zellwk.com/images/2019/mongoose/connect-database.png" alt="Connected to a database.">

### Creating a Model

In Mongoose, you need to **use models to create, read, update, or delete items** from a MongoDB collection.

To create a Model, **you need to create a Schema**. A Schema lets you **define the structure of an entry** in the collection. This entry is also called a document.

Here's how you create a schema:

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const schema = new Schema({
  // ...
})
```

You can use [10 different kinds of values](https://mongoosejs.com/docs/guide.html) in a Schema. Most of the time, you'll use these six:

- String
- Number
- Boolean
- Array
- Date
- ObjectId

Let's put this into practice.

Say we want to create characters for our Street Fighter database.

In Mongoose, it's a normal practice to **put each model in its own file.** So we will create a `Character.js` file first. This `Character.js` file will be placed in the `models` folder.

```bash
project/
    |- models/
        |- Character.js
```

In `Character.js`, we create a `characterSchema`.

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const characterSchema = new Schema({
  // ...
})
```

Let's say we want to save two things into the database:

1. Name of the character
2. Name of their ultimate move

Both can be represented with Strings.

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const characterSchema = new Schema({
  name: String,
  ultimate: String
})
```

Once we've created `characterSchema`, we can use mongoose's `model` method to create the model.

```js
module.exports = mongoose.model('Character', characterSchema)
```

### Creating a document

Let's say you have a file called `index.js`. This is where we'll perform Mongoose operations for this tutorial.

```bash
project/
    |- index.js
    |- models/
        |- Character.js
```

First, you need to load the Character model. You can do this with `require`.

```js
const Character = require('./models/Character')
```

Let's say you want to create a character called Ryu. Ryu has an ultimate move called "Shinku Hadoken".

To create Ryu, you use the `new`, followed by your model. In this case, it's `new Character`.

```js
const ryu = new Character ({
  name: 'Ryu',
  ultimate: 'Shinku Hadoken'
})
```

`new Character` creates the character in memory. It has not been saved to the database yet. **To save to the database, you can run the `save` method**.

```js
ryu.save(function (error, document) {
  if (error) console.error(error)
  console.log(document)
})
```

If you run the code above, you should see this in the console.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/saved.png" alt="Ryu saved to the database."></figure>

#### Promises and Async/await

**Mongoose supports promises.** It lets you write nicer code like this:

```js
// This does the same thing as above
function saveCharacter (character) {
  const c = new Character(character)
  return c.save()
}

saveCharacter({
  name: 'Ryu',
  ultimate: 'Shinku Hadoken'
})
  .then(doc => { console.log(doc) })
  .catch(error => { console.error(error) })
```

You can also use the `await` keyword if you have an asynchronous function.

If the Promise or Async/Await code looks foreign to you, I recommend reading ["JavaScript async and await"](https://zellwk.com/blog/async-await) before continuing with this tutorial.

```js
async function runCode() {
  const ryu = new Character({
    name: 'Ryu',
    ultimate: 'Shinku Hadoken'
  })

  const doc = await ryu.save()
  console.log(doc)
}

runCode()
  .catch(error => { console.error(error) })
```

Note: I'll use the async/await format for the rest of the tutorial.

#### Uniqueness

Mongoose adds a new character to the database each time you use `new Character` and `save`. If you run the code(s) above three times, you'd expect to see three Ryus in the database.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/three-ryus.png" alt="Three Ryus in the database."></figure>

We don't want to have three Ryus in the database. We want to have **ONE Ryu only**. To do this, we can use the **unique** option.

```js
const characterSchema = new Schema({
  name: { type: String, unique: true },
  ultimate: String
})
```

The `unique` option **creates a unique index**. It ensures that we cannot have two documents with the same value (for `name` in this case).

For `unique` to work properly, you need to **clear the Characters collection**. To clear the Characters collection, you can use this:

```js
await Character.deleteMany({})
```

Try to add two Ryus into the database now. You'll get an `E11000 duplicate key error`. You won't be able to save the second Ryu.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/dup-error.png" alt="Duplicated key error."></figure>

Let's add another character into the database before we continue the rest of the tutorial.

```js
const ken = new Character({
  name: 'Ken',
  ultimate: 'Guren Enjinkyaku'
})

await ken.save()
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/ryu-ken.png" alt="Database contains two characters."></figure>

### Finding a document

Mongoose gives you two methods to find stuff from MongoDB.

1. `findOne`: Gets one document.
2. `find`: Gets an array of documents

#### findOne

`findOne` **returns the first document** it finds. You can specify any property to search for. Let's search for `Ryu`:

```js
const ryu = await Character.findOne({ name: 'Ryu' })
console.log(ryu)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/found-one.png" alt="Found Ryu from the database."></figure>

#### find

`find` **returns an array** of documents. If you specify a property to search for, it'll return documents that match your query.

```js
const chars = await Character.find({ name: 'Ryu' })
console.log(chars)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/found-many-ryu.png" alt="Combed through the database and found one character with the name Ryu."></figure>

If you did not specify any properties to search for, it'll return an array that contains all documents in the collection.

```js
const chars = await Character.find()
console.log(chars)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/found-many.png" alt="Found two characters in the database."></figure>

### Updating a document

Let's say Ryu has three special moves:

1. Hadoken
2. Shoryuken
3. Tatsumaki Senpukyaku

We want to add these special moves into the database. First, we need to update our `CharacterSchema`.

```js
const characterSchema = new Schema({
  name: { type: String, unique: true },
  specials: Array,
  ultimate: String
})
```

Then, we use one of these two ways to update a character:

1. Use `findOne`, then use `save`
2. Use `findOneAndUpdate`

#### findOne and save

First, we use `findOne` to get Ryu.

```js
const ryu = await Character.findOne({ name: 'Ryu' })
console.log(ryu)
```

Then, we update Ryu to include his special moves.

```js
const ryu = await Character.findOne({ name: 'Ryu' })
ryu.specials = [
  'Hadoken',
  'Shoryuken',
  'Tatsumaki Senpukyaku'
]
```

After we modified `ryu`, we run `save`.

```js
const ryu = await Character.findOne({ name: 'Ryu' })
ryu.specials = [
  'Hadoken',
  'Shoryuken',
  'Tatsumaki Senpukyaku'
]

const doc = await ryu.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/ryu-updated.png" alt="Updated Ryu."></figure>

#### findOneAndUpdate

`findOneAndUpdate` is the same as MongoDB's `findOneAndModify` method.

Here, you search for Ryu and pass the fields you want to update at the same time.

```js
// Syntax
await findOneAndUpdate(filter, update)
```

```js
// Usage
const doc = await Character.findOneAndUpdate(
  { name: 'Ryu' },
  {
    specials: [
      'Hadoken',
      'Shoryuken',
      'Tatsumaki Senpukyaku'
    ]
  })

console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose/ryu-updated.png" alt="Updated Ryu."></figure>

#### Difference between findOne + save vs findOneAndUpdate

Two major differences.

First, the **syntax for ``findOne` + `save`` is easier to read** than `findOneAndUpdate`.

Second, `findOneAndUpdate` does not trigger the `save` middleware.

**I'll choose `findOne` + `save`** over `findOneAndUpdate` anytime because of these two differences.

### Deleting a document

There are two ways to delete a character:

1. `findOne` + `remove`
2. `findOneAndDelete`

#### Using findOne + remove

```js
const ryu = await Character.findOne({ name: 'Ryu' })
const deleted = await ryu.remove()
```

#### Using findOneAndDelete

```js
const deleted = await Character.findOneAndDelete({ name: 'Ken' })
```

## Subdocuments 

In Mongoose, **subdocuments** are documents that are **nested in other documents**. You can spot a subdocument when a schema is nested in another schema.

Note: MongoDB calls subdocuments **embedded documents**.

```js
const childSchema = new Schema({
  name: String
});

const parentSchema = new Schema({
  // Single subdocument
  child: childSchema,

  // Array of subdocuments
  children: [ childSchema ]
});
```

In practice, you don't have to create a separate `childSchema` like the example above. Mongoose helps you create nested schemas when you nest an object in another object.

```js
// This code is the same as above
const parentSchema = new Schema({
  // Single subdocument
  child: { name: String },

  // Array of subdocuments
  children: [{name: String }]
});
```

In this section, you will learn to: 

1. Create a schema that includes a subdocument
2. Create documents that contain subdocuments
3. Update subdocuments that are arrays
4. Update a single subdocument

### Updating characterSchema

Let's say we want to create a character called Ryu. Ryu has three special moves.

1. Hadoken
2. Shinryuken
3. Tatsumaki Senpukyaku

Ryu also has one ultimate move called:

1. Shinku Hadoken

We want to save the names of each move. We also want to save the keys required to execute that move.

Here, each move is a subdocument.

```js
const characterSchema = new Schema({
  name: { type: String, unique: true },
  // Array of subdocuments
  specials: [{
    name: String,
    keys: String
  }]
  // Single subdocument
  ultimate: {
    name: String,
    keys: String
  }
})
```

You can also use the childSchema syntax if you wish to. It makes the Character schema easier to understand.

```js
const moveSchema = new Schema({
  name: String,
  keys: String
})

const characterSchema = new Schema({
  name: { type: String, unique: true },
  // Array of subdocuments
  specials: [moveSchema],
  // Single subdocument
  ultimate: moveSchema
})
```

### Creating documents that contain subdocuments

There are two ways to create documents that contain subdocuments:

1. Pass a nested object into `new Model`
2. Add properties into the created document.

#### Method 1: Passing the entire object

For this method, we construct a nested object that contains both Ryu's name and his moves.

```js
const ryu = {
  name: 'Ryu',
  specials: [{
    name: 'Hadoken',
    keys: 'â†“ â†˜ â†’ P'
  }, {
    name: 'Shoryuken',
    keys: 'â†’ â†“ â†˜ â†’ P'
  }, {
    name: 'Tatsumaki Senpukyaku',
    keys: 'â†“ â†™ â† K'
  }],
  ultimate: {
    name: 'Shinku Hadoken',
    keys: 'â†“ â†˜ â†’ â†“ â†˜ â†’ P'
  }
}
```

Then, we pass this object into `new Character`.

```js
const char = new Character(ryu)
const doc = await char.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu.png" alt="Image of Ryu's document."></figure>

#### Method 2: Adding subdocuments later

For this method, we create a character with `new Character` first.

```js
const ryu = new Character({ name: 'Ryu' })
```

Then, we edit the character to add special moves:

```js
const ryu = new Character({ name: 'Ryu' })
const ryu.specials = [{
  name: 'Hadoken',
  keys: 'â†“ â†˜ â†’ P'
}, {
  name: 'Shoryuken',
  keys: 'â†’ â†“ â†˜ â†’ P'
}, {
  name: 'Tatsumaki Senpukyaku',
  keys: 'â†“ â†™ â† K'
}]
```

Then, we edit the character to add the ultimate move:

```js
const ryu = new Character({ name: 'Ryu' })

// Adds specials
const ryu.specials = [{
  name: 'Hadoken',
  keys: 'â†“ â†˜ â†’ P'
}, {
  name: 'Shoryuken',
  keys: 'â†’ â†“ â†˜ â†’ P'
}, {
  name: 'Tatsumaki Senpukyaku',
  keys: 'â†“ â†™ â† K'
}]

// Adds ultimate
ryu.ultimate = {
  name: 'Shinku Hadoken',
  keys: 'â†“ â†˜ â†’ â†“ â†˜ â†’ P'
}
```

Once we're satisfied with `ryu`, we run `save`.

```js
const ryu = new Character({ name: 'Ryu' })

// Adds specials
const ryu.specials = [{
  name: 'Hadoken',
  keys: 'â†“ â†˜ â†’ P'
}, {
  name: 'Shoryuken',
  keys: 'â†’ â†“ â†˜ â†’ P'
}, {
  name: 'Tatsumaki Senpukyaku',
  keys: 'â†“ â†™ â† K'
}]

// Adds ultimate
ryu.ultimate = {
  name: 'Shinku Hadoken',
  keys: 'â†“ â†˜ â†’ â†“ â†˜ â†’ P'
}

const doc = await ryu.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu.png" alt="Image of Ryu's document."></figure>

### Updating array subdocuments

The easiest way to update subdocuments is:

1. Use `findOne` to find the document
2. Get the array
3. Change the array
4. Run `save`

For example, let's say we want to add `Jodan Sokutou Geri` to Ryu's special moves. The keys for `Jodan Sokutou Geri` are `â†“ â†˜ â†’ K`.

First, we find Ryu with `findOne`.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
```

Mongoose documents behave like regular JavaScript objects. We can get the `specials` array by writing `ryu.specials`.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
const specials = ryu.specials
console.log(specials)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/specials.png" alt="Log of specials."></figure>

This `specials` array is a normal JavaScript array.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
const specials = ryu.specials
console.log(Array.isArray(specials)) // true
```

We can use the `push` method to add a new item into `specials`,

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
ryu.specials.push({
  name: 'Jodan Sokutou Geri',
  keys: 'â†“ â†˜ â†’ K'
})
```

After updating `specials`, we run `save` to save Ryu to the database.

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
ryu.specials.push({
  name: 'Jodan Sokutou Geri',
  keys: 'â†“ â†˜ â†’ K'
})

const updated = await ryu.save()
console.log(updated)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu-updated.png" alt="Ryu updated with Jodan Sokutou Geri"></figure>

### Updating a single subdocument

It's even easier to update single subdocuments. You can edit the document directly like a normal object.

Let's say we want to change Ryu's ultimate name from Shinku Hadoken to Dejin Hadoken. What we do is:

1. Use `findOne` to get Ryu.
2. Change the `name` in `ultimate`
3. Run `save`

```js
const ryu = await Characters.findOne({ name: 'Ryu' })
ryu.ultimate.name = 'Dejin Hadoken'

const updated = await ryu.save()
console.log(updated)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-subdocuments/ryu-3.png" alt="Ryu document with Dejin Hadoken."></figure>

## Population

MongoDB documents have a size limit of 16MB. This means you can use subdocuments (or embedded documents) if they are small in number.

For example, Street Fighter characters have a limited number of moves. Ryu only has 4 special moves. In this case, it's okay to use embed moves directly into Ryu's character document.

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/ryu.png" alt="Ryu's document."></figure>

But if you have data that can contain an unlimited number of subdocuments, you need to design your database differently.

One way is to create two separate models and combine them with populate.

### Creating the models

Let's say you want to create a blog. And you want to store the blog content with MongoDB. Each blog has a title, content, and comments.

Your first schema might look like this:

```js
const blogPostSchema = new Schema({
  title: String,
  content: String,
  comments: [{
    comment: String
  }]
})

module.exports = mongoose.model('BlogPost', blogPostSchema)
```

There's a problem with this schema.

A blog post can have an unlimited number of comments. If a blog post explodes in popularity and comments swell up, the document might exceed the 16MB limit imposed by MongoDB.

This means we should not embed comments in blog posts. We should create a separate collection for comments.

```js
const comments = new Schema({
  comment: String
})

module.exports = mongoose.model('Comment', commentSchema)
```

In Mongoose, we can link up the two models with Population.

To use Population, we need to:

1. Set `type` of a property to `Schema.Types.ObjectId`
2. Set `ref` to the model we want to link too.

Here, we want `comments` in `blogPostSchema` to link to the Comment collection. This is the schema we'll use:

```js
const blogPostSchema = new Schema({
  title: String,
  content: String,
  comments: [{ type: Schema.Types.ObjectId, ref: 'Comment' }]
})

module.exports = mongoose.model('BlogPost', blogPostSchema)
```

### Creating a blog post

Let's say you want to create a blog post. To create the blog post, you use `new BlogPost`.

```js
const blogPost = new BlogPost({
  title: 'Weather',
  content: `How's the weather today?`
})
```

A blog post can have zero comments. We can save this blog post with `save`.

```js
const doc = await blogPost.save()
console.log(doc)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/blog-post-no-comments.png" alt="Created a blog post document without comments."></figure>

### Creating comments

Now let's say we want to create a comment for the blog post. To do this, we create and save the comment.

```js
const comment = new Comment({
  comment: `It's damn hot today`
})

const savedComment = await comment.save()
console.log(savedComment)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/comment.png" alt="Created and saved a comment."></figure>

Notice the saved comment has an `_id` attribute. We need to add this `_id` attribute into the blog post's `comments` array. This creates the link.

```js
// Saves comment to Database
const savedComment = await comment.save()

// Adds comment to blog post
// Then saves blog post to database
const blogPost = await BlogPost.findOne({ title: 'Weather' })
blogPost.comments.push(savedComment._id)
const savedPost = await blogPost.save()
console.log(savedPost)
```

<figure role="figure" aria-label="Blog post with comments."><img src="https://zellwk.com/images/2019/mongoose-population/blog-post-with-comments.png" alt=""><figcaption>Blog post with comments.</figcaption></figure>

### Searching blog posts and their comments

If you tried to search for the blog post, you'll see the blog post has an array of comment IDs.

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })
console.log(blogPost)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/blog-post-with-comments.png" alt="Found blog post contains comment ids."></figure>

There are four ways to get comments.

1. Mongoose population
2. Manual way #1
3. Manual way #2
4. Manual way #3

#### Mongoose Population

Mongoose allows you to fetch linked documents with the `populate` method. What you need to do is call `.populate` when you execute with `findOne`.

When you call populate, you need to pass in the `key` of the property you want to populate. In this case, the `key` is `comments`. (Note: Mongoose calls this `key` a "path").

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })
  .populate('comments')
console.log(blogPost)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/populated.png" alt="Comments populated by Mongoose."></figure>

#### Manual way (method 1)

Without Mongoose Populate, you need to find the comments manually. First, you need to get the array of comments.

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })
  .populate('comments')
const commentIDs = blogPost.comments
```

Then, you loop through `commentIDs` to find each comment. If you go with this method, it's slightly faster to use `Promise.all`.

```js
const commentPromises = commentIDs.map(_id => {
  return Comment.findOne({ _id })
})
const comments = await Promise.all(commentPromises)
console.log(comments)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/found-comments.png" alt="Comments found."></figure>


#### Manual way (method 2)

Mongoose gives you an `$in` operator. You can use this `$in` operator to find all comments within an array. This syntax takes a little effort to get used to.

If I had to do the manual way, I'd prefer Manual #1 over this.

```js
const commentIDs = blogPost.comments
const comments = await Comment.find({
    '_id': { $in: commentIDs }
})

console.log(comments)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/found-comments.png" alt="Comments found."></figure>

#### Manual way (method 3)

For the third method, we need to change the schema. When we save a comment, we link the comment to the blog post.

```js
// Linking comments to blog post
const commentSchema = new Schema({
  comment: String
  blogPost: [{ type: Schema.Types.ObjectId, ref: 'BlogPost' }]
})

module.exports = mongoose.model('Comment', commentSchema)
```

You need to save the comment into the blog post, and the blog post id into the comment.

```js
const blogPost = await BlogPost.findOne({ title: 'Weather' })

// Saves comment
const comment = new Comment({
  comment: `It's damn hot today`,
  blogPost: blogPost._id
})
const savedComment = comment.save()

// Links blog post to comment
blogPost.comments.push(savedComment._id)
await blogPost.save()
```

Once you do this, you can search the Comments collection for comments that match your blog post's id.

```js
// Searches for comments
const blogPost = await BlogPost.findOne({ title: 'Weather' })
const comments = await Comment.find({ _id: blogPost._id })
console.log(comments)
```

<figure role="figure"><img src="https://zellwk.com/images/2019/mongoose-population/found-comments.png" alt="Comments found."></figure>

I'd prefer Manual #3 over Manual #1 and Manual #2.

And Population beats all three manual methods.

## Quick Summary 

You learned to use Mongoose on three different levels in this article: 

1. Basic Mongoose 
2. Mongoose subdocuments
3. Mongoose population 

That's it!


<hr>

Thanks for reading. This article was originally posted on [my blog](https://zellwk.com/blog/mongoose
).  Sign up for my newsletter if you want more articles to help you become a better frontend developer. 






