---
title: How to log a Node.js API in an Express.js app with Mongoose plugins
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T21:46:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-log-a-node-js-api-in-an-express-js-app-with-mongoose-plugins-efe32717b59
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLsF0BLHtCPk5voPS1yFhw.jpeg
tags:
- name: debugging
  slug: debugging
- name: Developer
  slug: developer
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Node.js
  slug: nodejs
seo_title: null
seo_desc: 'By Shailesh Shekhawat


  This tutorial will require prior knowledge of the mongoose Object Relational Mapping
  (ORM) technique


  Introduction

  As your application grows, logging becomes a crucial part to keep track of everything.
  It is especially importan...'
---

By Shailesh Shekhawat

> This tutorial will require prior knowledge of the [mongoose](https://mongoosejs.com/) Object Relational Mapping (ORM) technique

#### Introduction

As your application grows, logging becomes a crucial part to keep track of everything. It is especially important for debugging purposes.

Nowadays there are already logging modules available at npm. These modules can store logs in a file in different formats, or levels. We are going to discuss the API logging in your Node.js Express app using the popular ORM Mongoose.

So how you would create a **Mongoose plugin** that will do logging for you in a cleaner way and make API logging easy?

#### What is a plugin in Mongoose?

In Mongoose, schemas are pluggable. A plugin is like a function that you can use in your schema and reuse again and again over schema instances.

Mongoose also provides **global plugins** which you can use for all schemas. For example, we are going to write a plugin that will create a `**diff**` of two `**jsons**` and write to `**mongodb**`**.**

### Step 1: Creating a Basic Log Schema Model

Let’s create a basic log schema with the following six properties:

* **Action:** As per its name, this will be a course of action of the API whether it is `create` `update` `delete` or something else.
* **Category:** API category. For example doctors and patients. It is more like a class.
* **CreatedBy:** User who is using the API or invoked it.
* **Message:** Here you can include any kind of message you want to show that will make sense or help during debugging.
* **Diff:** This is the main property which will have the _diff_ of two _JSONs_

You can add more fields if you want that make sense for your own application. A schema can be changed and upgraded according to requirements.

Here is our model: `models/log.js`

```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema
const { ObjectId } = Schema

const LogSchema = new Schema({
  action: { type: String, required: true },
  category: { type: String, required: true },
  createdBy: { type: ObjectId, ref: 'Account', required: true },
  message: { type: String, required: true },
  diff: { type: Schema.Types.Mixed },
},{
  timestamps: { createdAt: 'createdAt', updatedAt: 'updatedAt' },
})

LogSchema.index({ action: 1, category: 1 })

module.exports = mongoose.model('Log', LogSchema)
```

### Step 2: Write a function to get the difference between 2 JSONs

So the next step is that you need a reusable function that will create a `diff` of two JSONs on the fly.

Let's call it `diff.js`

```js
const _ = require('lodash')

exports.getDiff = (curr, prev) => {
  function changes(object, base) {
    return _.transform(object, (result, value, key) => {
      if (!_.isEqual(value, base[key]))
        result[key] = (_.isObject(value) && _.isObject(base[key])) ?                 changes(value, base[key]) : value
    })
 }
 return changes(curr, prev)
}
```

I have used `[**lodash**](https://lodash.com/docs/4.17.10)`**,** which is a popular library, to provide the same functionality.

Let's break down the above function and see what's going on:

* **_.transform:** It’s an alternative to `.reduce` for arrays. Basically, it will iterate over your object `keys` and `values`. It provides an `accumulator` which is the first argument. `result` is the accumulator and it is mutable.
* **_.isEqual:** Performs a deep comparison between two values to determine if they are equivalent.

> **_isEqual_**_: This method supports comparing arrays, array buffers, booleans, date objects, error objects, maps, numbers, `Object` objects, regexes, sets, strings, symbols, and typed arrays. `Object` objects are compared by their own, not inherited, enumerable properties. Functions and DOM nodes are compared by strict equality, i.e. `===`._

Here we are iterating over each object property and value and comparing it with our old/prev object.

If the `value` of the current object is not equal to a value of the same property in the previous object: `base[key]` and if that value is the object itself, we call the function `changes` **recursively** until it gets a value which will be finally stored in `result` as `result[key] = value`.

### Step3: Create a plugin to use diff and save it to database

Now we need to keep track of the previous `document` in the database and create a `diff` before saving to `mongodb`.

```js
const _ = require('lodash')
const LogSchema = require('../models/log')
const { getDiff } = require('../utils/diff')

const plugin = function (schema) {
  schema.post('init', doc => {
    doc._original = doc.toObject({transform: false})
  })
  schema.pre('save', function (next) {
    if (this.isNew) {
      next()
    }else {
      this._diff = getDiff(this, this._original)
      next()
    }
})

  schema.methods.log = function (data)  {
    data.diff = {
      before: this._original,
      after: this._diff,
    }
    return LogSchema.create(data)
  }
}

module.exports = plugin
```

In Mongoose, there are different hooks available. For now, we need to use the `[init](https://mongoosejs.com/docs/api.html#document_Document-init)` and `[save](https://mongoosejs.com/docs/api.html#document_Document-save)` methods available on the schema.

`this.isNew()` : If you are creating the new document then just return `next()` middleware.

In `schema.post('init')` `[toObject()](https://mongoosejs.com/docs/api.html#document_Document-toObject)`:

```js
doc._original = doc.toObject({transform: false})
```

Mongoose `Model`s inherit from `Document`s, which have a `toObject()` method. It will convert a `document` into an `Object()` and `transform:false` is for not allowing to transform the return object.

### Step 4: Usage — How to use in express.js API

In your main `server.js` or `app.js` :

Initialise a global [plugin](https://mongoosejs.com/docs/plugins.html) so that it will be available for all schemas. You can also use it for a particular schema by initializing it in the schema model.

```js
const mongoose = require('mongoose')

mongoose.plugin(require('./app/utils/diff-plugin'))
```

Here is a basic example of `user` update API:

```js
const User = require('../models/user')

exports.updateUser = (req, res, next) => {
  return User.findById(req.params.id)
    .then(user => {
        if (!user)
           throw new Error('Target user does not exist. Failed to update.')
       const { name } = req.body
       if (name) user.name = name
       return user.save()
     })
     .then(result => {
       res.json(result)
       return result
     })
     .catch(next)
     .then(user => {
         if (user && typeof user.log === 'function') { 
            const data = {
              action: 'update-user',
              category: 'users',
              createdBy: req.user.id,
              message: 'Updated user name',
         }
         return user.log(data)
     }
     }).catch(err => {
         console.log('Caught error while logging: ', err)
       })
}
```

### Conclusion

In this tutorial, you learned how to create a Mongoose plugin and use it to log the `changes` in your API. You can do a lot more with plugins to build a robust node application.

Here are resources to learn more about Mongoose and plugin usage:

* 80/20 Guide to mongoose plugins: [http://thecodebarbarian.com/2015/03/06/guide-to-mongoose-plugins](http://thecodebarbarian.com/2015/03/06/guide-to-mongoose-plugins)
* [https://mongoosejs.com/docs/plugins.html](https://mongoosejs.com/docs/plugins.html)

I hope you find this tutorial useful, feel free to reach [out](https://101node.io) if you have any questions.

Follow [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) to get notified whenever I publish a new post.

_Don’t hesitate to clap if you considered this a worthwhile read!_

_Originally published at [101node.io](https://101node.io/blog/better-logging-with-mongoose-plugins-in-node-js-express-app/) on September 2, 2018._

