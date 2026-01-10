---
title: How to perform custom validation in your Express.js app (Part-2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T22:46:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-custom-validation-in-your-express-js-app-432eb423510f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KOwj7MMEgc1V_9t6EQP2ag.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Shailesh Shekhawat

  In the previous post, I showed how to get started with input validation in an express.js
  application. I used the express-validator module and discussed its important features
  with implementation.

  If you haven’t checked that out,...'
---

By Shailesh Shekhawat

In the [previous post](https://medium.freecodecamp.org/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7), I showed how to get started with input validation in an express.js application. I used the [express-validator](https://github.com/ctavan/express-validator) module and discussed its important features with implementation.

If you haven’t checked that out, please go read the first post [here](https://medium.freecodecamp.org/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7).

So now let’s get started. In part 2 of this tutorial, you will learn how to perform custom validation in an Express.js app.

### What you can achieve with custom validation

* It can be used to verify the existence of the entity in your database.
* Also to test if a certain value exists in an array, object, string etc.
* If you want to change the data format itself.

And a lot more…

The [express-validator](https://express-validator.github.io/docs/) library provides a `custom` method which you can use to do all sorts of custom validations

Implementation of a custom validator uses the chain method [.custom()](https://express-validator.github.io/docs/validation-chain-api.html#customvalidator). It takes a validator function.

Custom validators return Promises to show an async validation or `throw` any value/reject a promise to [use a custom error message](https://express-validator.github.io/docs/custom-error-messages.html#custom-validator-level).

Now I will show you examples of the above custom validation use cases.

### Check if the entity exists in your database

An important one which I use on day to day basis — and I guess you will be using to verify an entity against a database

For example, if someone requests to update their name, you’d use it for a basic `PUT` request `/api/users/:userId`.

To make sure that the user should exist in our database, I created a function to check against the DB.

```js
param('userId')
.exists()
.isMongoId()
.custom(val => UserSchema.isValidUser(val))
```

`isValidUser()` is a static function which will make an async call to the database and find if the user exists or not.

Let’s write a static function in mongoose`Schema`:

```js
UserSchema.statics = {
   isValid(id) {
      return this.findById(id)
             .then(result => {
                if (!result) throw new Error('User not found')
      })
   },
}
```

As we cannot trust the `userId` sent by the client based on its format only, we need to make sure it is a real account.

### **Verify against certain values in Array or Object**

For example, if you want to apply a rule on a **username** that it must have a character `@`.

So in your `POST` request of user creation or while updating, you can do something like this:

```js
body('username', 'Invalid Username')
.exists()
.isString().isLowercase()
.custom(val => {   
   
   if (val.indexOf('@') !== -1) return true
    
   return false
}),
```

> _Remember: Always return a boolean value from the callback of `.custom()` function. Otherwise your validation might not work as desired._

As you can see, we can do all these validations including async in middleware itself instead of doing them in a controller

<iframe src="https://giphy.com/embed/TkERwbWzAxvfa" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

### Change input data format

The library has a [Sanitization](https://express-validator.github.io/docs/sanitization.html) feature where custom sanitization is performed using `customerSanitizer()`.

I used it to change the string of comma separated values to an array of strings.

For example, we have a doctor database. Someone wants to get only doctors who are **cardiologists** and **psychiatrists.**

We have stored both of these specializations as a `**type**` in our database.

A simple `GET` request will look like this:

```
GET /api/doctors?type=cardiologists,psychiatrist
```

Now in `mongodb` we can use the `**$in**` operator to search for multiple values of a property.

A basic database query can be like:

```js
Doctors.find({
   type: {
       
     $in: ['cardiologists', 'psychiatrist']
       
   }
})
```

This will give you all cardiologists and psychiatrists.

From `GET` query:

```js
req.query = {

  type: "cardiologists,psychiatrist"
  
}
```

As you can see in `req.query`, you will get a property `type` whose type is a `string`.

With the help of`.customSanitizer()` we are able to convert a string into an array of strings.

At the validation level:

```js
const commaToArray  = (value = '') => value.split(',')

sanitizeQuery('type').customSanitizer(commaToArray),
```

Now we can directly feed it to the database query to the `**$in**` operator.

**What if I want to apply some rules on all items in an array or keys in objects?**

<iframe src="https://giphy.com/embed/a5viI92PAF89q" width="480" height="331" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reaction-a5viI92PAF89q">via GIPHY</a></p>

#### Body:

```js
{
  items:[
    {_id: 'someObjectId', number: '200'},
    ...
  ]
}
```

### Wildcards

Wildcard is one of the great features of this module. It allows you to iterate over an array of items or object keys and validate each item or its properties.

The `*` character is also known as a wildcard.

Imagine I want to validate all the `_id, number`of items.

```js
check('items.*._id')
.exists()
.isMongoId()
.custom(val => ItemSchema.isValid(val)), //similar to isValidUser() 
sanitize('items.*.number').toInt()
```

There you have it — an introduction to input validation using the express-validator module

If you encounter any problems, feel free to _get in [touch](https://101node.io) or comment below._  
I would be happy to help :)

_Don’t hesitate to clap if you considered this a worthwhile read!_

Follow [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) to get notified whenever I publish a new post.

_Originally published at [101node.io](https://101node.io/blog/how-to-make-input-validation-in-express-js-app-part-2/) on September 22, 2018._

