---
title: How to make input validation simple and clean in your Express.js app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T22:08:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e0mCbx2PuNysG54g0B1gRg.jpeg
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Shailesh Shekhawat


  This tutorial requires prior knowledge of using the expressjs framework


  Why do we need server-side validation?


  Your client side validation is not enough and it may be subverted

  More prone to Man in middle attacks, and the ser...'
---

By Shailesh Shekhawat

> This tutorial requires prior knowledge of using the [expressjs](http://expressjs.com) framework

#### Why do we need server-side validation?

* Your client side validation is not enough and it may be subverted
* More prone to [Man in middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), and the server should never trust the client-side
* A user can turn off client-side JavaScript validation and manipulate the data

If you have been building web applications using an Express framework or any other Node.js framework, validation plays a crucial role in any web app which requires you to validate the request `body` `param` `query`.

Writing your own middleware function can be cumbersome if

* you want to move fast while maintaining the quality of code or
* you want to avoid using `**if** (**req**.body.head)` or `**if** (**req**.params.isCool)` in your main controller function where you define business logic

In this tutorial, you’ll learn how to validate input in an Express.js app using an open source and popular module called [express-validator](https://github.com/ctavan/express-validator).

### Introduction to express-validator

The definition on Github says:

> express-validator is a set of [express.js](http://expressjs.com/) middlewares that wraps [validator.js](https://github.com/chriso/validator.js) validator and sanitizer functions.

The module implements five important API’s:

* Check API
* Filter API
* Sanitization chain API
* Validation chain API
* Validation Result API

Let's take a look at a basic user `route` without any validation module to create a user: `/route/user.js`

```js
/**
* @api {post} /api/user Create user
* @apiName Create new user
* @apiPermission admin
* @apiGroup User
*
* @apiParam  {String} [userName] username
* @apiParam  {String} [email] Email
* @apiParam  {String} [phone] Phone number
* @apiParam  {String} [status] Status
*
* @apiSuccess (200) {Object} mixed `User` object
*/

router.post('/', userController.createUser)
```

Now in user controller `/controllers/user.js`

```js
const User = require('./models/user')

exports.createUser = (req, res, next) => {
  /** Here you need to validate user input. 
   Let's say only Name and email are required field
 */
  
  const { userName, email, phone, status } = req.body
  if (userName && email &&  isValidEmail(email)) { 
    
    // isValidEmail is some custom email function to validate email which you might need write on your own or use npm module
    User.create({
      userName,
      email,
      phone,
      status,   
    })
    .then(user => res.json(user))
    .catch(next)
  }
}
```

The above code is just a basic example of validating fields on your own.

You can handle some validations in your user model using Mongoose. For best practices, we want to make sure validation happens before business logic.

[express-validator](https://github.com/ctavan/express-validator) will take care of all these validations and the [sanitization](https://www.quora.com/What-does-it-mean-to-sanitize-a-field-How-is-that-related-to-escaping-as-in-entering-in-malicious-input-that-escapes-or-something) of inputs as well.

#### **Installation**

```bash
npm install --save express-validator
```

Include **module** in your main `server.js` file:

```js
const express = require('express')
const bodyParser = require('body-parser')
const expressValidator = require('express-validator')
const app = express()
const router = express.Router()

app.use(bodyParser.json())

app.use(expressValidator())

app.use('/api', router)
```

Now using [express-validator](https://github.com/ctavan/express-validator), your `/routes/user.js` will be like this:

```js
router.post(
  '/', 
  userController.validate('createUser'), 
  userController.createUser,
)
```

Here `userController.validate` is a middleware function which is explained below. It accepts the `method` name for which the validation will be used.

Let’s create a middleware function `validate()`in our`/controllers/user.js`:

```js
const { body } = require('express-validator/check')

exports.validate = (method) => {
  switch (method) {
    case 'createUser': {
     return [ 
        body('userName', 'userName doesn't exists').exists(),
        body('email', 'Invalid email').exists().isEmail(),
        body('phone').optional().isInt(),
        body('status').optional().isIn(['enabled', 'disabled'])
       ]   
    }
  }
}
```

Please refer to [this article](https://express-validator.github.io/docs/check-api.html) to know more about function definition and its use.

The `body` function will only validate `req.body` and takes two arguments. First is the `property name`. Second is your custom `message` that will be shown if validation fails. If you don’t provide a custom message, then the default message will be used.

As you can see, for a `required` field we are using the `.exists()` method. We are using `.optional()`for an `optional` field. Similarly `isEmail()` `isInt()` is used to validate `email` and `integer`.

If you want an input field to include only certain values, then you can use `.isIn([])`. This takes an `array` of values, and if you receive values other than the above, then an error will be thrown.

For example, the status field in the above code snippet can only have an `enabled` or `disabled` value. If you provide any value other than that, an error will be thrown.

In `/controllers/user.js` let’s write a`**createUser**` function where you can write business logic. It will be called after `**validate()**` with the result of the validations.

```js
const { validationResult } = require('express-validator/check');

exports.createUser = async (req, res, next) => {
   try {
      const errors = validationResult(req); // Finds the validation errors in this request and wraps them in an object with handy functions

      if (!errors.isEmpty()) {
        res.status(422).json({ errors: errors.array() });
        return;
      }

      const { userName, email, phone, status } = req.body
      
      const user = await User.create({

        userName,

        email,

        phone,

        status,   
      })

      res.json(user)
   } catch(err) {
     return next(err)
   }
}
```

#### If you are wondering what is validationResult(req)?

**This function** **finds the validation errors in this request and wraps them in an object with handy functions**

Now whenever request includes invalid body params or `userName` field is missing in `req.body`, your server will respond like this:

```js
{
  "errors": [{
    "location": "body",
    "msg": "userName is required",
    "param": "userName"
  }]
}
```

So if `userName` or `email` failed to satisfy the validation then each error returned by `.array()`method has the following format by default:

```js
{   
  "msg": "The error message",
   
  "param": "param name", 
  
  "value": "param value",   
  // Location of the param that generated this error.   
  // It's either body, query, params, cookies or headers.   
  "location": "body",    
  
  // nestedErrors only exist when using the oneOf function
  "nestedErrors": [{ ... }] 
}
```

As you can see, this module really helps us take care of most of the validations on its own. It maintains code quality as well, and focuses mainly on business logic.

This was the introduction to input validation using the **express-validator** module and check out how to validate an array of the item and make your own custom validation in [Part 2](https://www.freecodecamp.org/news/how-to-perform-custom-validation-in-your-express-js-app-432eb423510f/) of this series.

I have tried my best and hope I covered enough to explain it in detail so that you can get started.

If you encounter any problems, feel free to _get in [touch](https://101node.io) or comment below._  
I would be happy to help :)

Follow [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) to get notified whenever I publish a new post.

_Don’t hesitate to clap if you considered this a worthwhile read!_

_Originally published at [101node.io](https://101node.io/blog/how-to-validate-inputs-in-express-js-app/) on September 2, 2018._

