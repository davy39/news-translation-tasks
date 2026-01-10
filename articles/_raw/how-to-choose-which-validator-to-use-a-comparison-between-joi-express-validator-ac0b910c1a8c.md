---
title: 'How to choose which validator to use: a comparison between Joi & express-validator'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T16:28:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-which-validator-to-use-a-comparison-between-joi-express-validator-ac0b910c1a8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s3Fzn57ud8r82T56w9biWg.png
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shailesh Shekhawat

  Imagine you have an e-commerce website and you’re allowing users to create accounts
  using their name and email. You want to make sure they sign up with real names,
  not something like cool_dud3.

  That''s where we use validation to ...'
---

By Shailesh Shekhawat

Imagine you have an e-commerce website and you’re allowing users to create accounts using their name and email. You want to make sure they sign up with real names, not something like cool_dud3.

That's where we use validation to validate inputs and make sure input data follows certain rules.

In the market, we already have a bunch of validation libraries, but I will compare two important validation libraries: [Joi](https://github.com/hapijs/joi) and [express-validator](https://github.com/express-validator/express-validator) for **express.js based applications**.

This comparison is useful when you have decided to use external input validation library for your application built on **expressjs** and are somewhat not sure which one to use.

### Who is what?

#### Joi

Joi allows you to create _blueprints_ or _schemas_ for JavaScript objects (an object that stores information) to ensure _validation_ of key information.

#### Express-validator

_express-validator_ is a set of [express.js](http://expressjs.com/) middlewares that wraps [validator.js](https://github.com/chriso/validator.js) validator and sanitizer functions.

So by definition, we can say that:

* Joi can be used for creating schemas (just like we use mongoose for creating NoSQL schemas) and you can use it with plain Javascript objects. It's like a plug n play library and is easy to use.
* On the other hand, _express-validator_ uses [validator.js](https://github.com/chriso/validator.js) to validate expressjs routes, and it's mainly built for express.js applications. This makes this library more niche and provides out of box custom validation and sanitization. Also, I find it easy to understand personally :)

Too many methods and API's for doing certain validation in Joi might make you feel overwhelmed so you might end up closing the tab.

But I may be wrong — so let’s keep opinions aside and compare both libraries.

### Instantiation

#### Joi

In Joi_,_ you need to use `**Joi.object()**` to instantiate a Joi schema object to work with.

All schemas require `Joi.object()`to process validation and other Joi features.

You need to separately read `req.body` , `req.params` , `req.query` to request body, params, and query.

```js
const Joi = require('joi');

const schema = Joi.object().keys({
   // validate fields here
})
```

#### Express-validator

You can just require _express-validator_ and start using its methods. You don't need to read values from `req.body` , `req.params` , and `req.query` separately.

You just need to use the `param, query, body` methods below to validate inputs respectively as you can see here:

```js
const {
  param, query, cookies, header 
  body, validationResult } = require('express-validator/check')

app.post('/user', [   
    
// validate fields here
 
], (req, res) => {
const errors = validationResult(req);
   
  if (!errors.isEmpty()) {     
    return res.status(422).json({ errors: errors.array() });   
  }
}
```

#### Field is required

Let’s take a very basic example where we want to make sure that a `username` should be required `string` and is `alphaNumeric` with `min` and `max` characters.

* **Joi:**

```js
const Joi = require('joi');
const schema = Joi.object().keys({
    username: Joi.string().alphanum().min(3).max(30).required()
})

app.post('/user', (req, res, next) => {   
  const result = Joi.validate(req.body, schema)
  if (result.error) {
    return res.status(400).json({ error: result.error });
  }
});
```

* **Express-validator**

```js
const { body, validationResult } = require('express-validator/check')

app.post('/user', [   
 body('username')
  .isString()
  .isAlphanumeric()
  .isLength({min: 3, max: 30})
  .exists(), 
], (req, res) => {
  const errors = validationResult(req);
   
  if (!errors.isEmpty()) {     
    return res.status(422).json({ errors: errors.array() });   
  }
}
```

### Sanitization

Sanitization is basically checking input to make sure it's free of noise, for example, we all have used `.trim()` on string to remove spaces.

Or if you have faced a situation where a number is coming in as `"1"` so in those cases, we want to sanitize and convert the type during runtime.

Sadly, Joi doesn’t provide sanitization out of the box but _express-validator_ does.

#### Example: converting to MongoDB’s ObjectID

```js
const { sanitizeParam } = require('express-validator/filter');  

app.post('/object/:id',  
   sanitizeParam('id')
  .customSanitizer(value => {
     return ObjectId(value); 
}), (req, res) => {   // Handle the request });
```

### Custom Validation

#### Joi: **.extend(**`extension`**)**

This creates a new Joi instance customized with the extension(s) you provide included.

The extension makes use of some common structures that need to be described first:

* `value` - the value being processed by Joi.
* `state` - an object containing the current context of validation.
* `key` - the key of the current value.
* `path` - the full path of the current value.
* `parent` - the potential parent of the current value.
* `options` - options object provided through `[any().options()](https://github.com/hapijs/joi/blob/master/API.md#anyoptionsoptions)` or `[Joi.validate()](https://github.com/hapijs/joi/blob/master/API.md#validatevalue-schema-options-callback)`.

#### Extension

`extension` can be:

* a single extension object
* a factory function generating an extension object
* or an array of those

Extension objects use the following parameters:

* `name` - name of the new type you are defining, this can be an existing type. Required.
* `base` - an existing Joi schema to base your type on. Defaults to `Joi.any()`.
* `coerce` - an optional function that runs before the base, usually serves when you want to coerce values of a different type than your base. It takes 3 arguments `value`, `state` and `options`.
* `pre` - an optional function that runs first in the validation chain, usually serves when you need to cast values. It takes 3 arguments `value`, `state` and `options`.
* `language` - an optional object to add error definitions. Every key will be prefixed by the type name.
* `describe` - an optional function taking the fully formed description to post-process it.
* `rules` - an optional array of rules to add.
* `name` - name of the new rule. Required.
* `params` - an optional object containing Joi schemas of each parameter ordered. You can also pass a single Joi schema as long as it is a `Joi.object()`. Of course some methods such as `pattern` or `rename` won't be useful or won't work at all in this given context.
* `setup` - an optional function that takes an object with the provided parameters to allow for internal manipulation of the schema when a rule is set. You can optionally return a new Joi schema that will be taken as the new schema instance. At least one of either `setup` or `validate` must be provided.
* `validate` - an optional function to validate values that takes 4 parameters `params`, `value`, `state` and `options`. At least one of `setup` or `validate` must be provided.
* `description` - an optional string or function taking the parameters as an argument to describe what the rule is doing.

**Example**:

```js
joi.extend((joi) => ({
    base: joi.object().keys({
        name: joi.string(),
        age: joi.number(),
        adult: joi.bool().optional(),
    }),
    name: 'person',
    language: {
        adult: 'needs to be an adult',
    },
rules: [
        {
            name: 'adult',
            validate(params, value, state, options) {

                if (!value.adult) {
                    // Generate an error, state and options need to be passed
                    return this.createError('person.adult', {}, state, options);
                }

                return value; // Everything is OK
            }
        }
    ]
})
```

#### Express-validator

A custom validator may be implemented by using the chain method `[.custom()](https://express-validator.github.io/docs/validation-chain-api.html#customvalidator)`. It takes a validator function.

Custom validators may return Promises to indicate an async validation (which will be awaited upon), or `throw` any value/reject a promise to [use a custom error message](https://express-validator.github.io/docs/custom-error-messages.html#custom-validator-level).

```js
const {
  param, query, cookies, header 
  body, validationResult } = require('express-validator/check')

app.get('/user/:userId', [   
 param('userId')
  .exists()
  .isMongoId()
  .custom(val => UserSchema.isValidUser(val)), 
], (req, res) => {
    
const errors = validationResult(req);
   
  if (!errors.isEmpty()) {     
    return res.status(422).json({ errors: errors.array() });   
  }
}
```

### Conditional Validation

_express-validator_ does not support conditional validation as of now, but there is a PR for that already you can check [https://github.com/express-validator/express-validator/pull/658](https://github.com/express-validator/express-validator/pull/658)

Let’s see how it works in Joi:

#### `any.when(condition, options)`

`**any:**` Generates a schema object that matches any data type.

```js
const schema = Joi.object({
    a: Joi.any().valid('x'),
    b: Joi.any()
}).when(
    Joi.object({ b: Joi.exist() })
    .unknown(), {
    then: Joi.object({
        a: Joi.valid('y')
    }),
    otherwise: Joi.object({
        a: Joi.valid('z')
    })
});
```

#### `alternatives.when(condition, options)`

Adds a conditional alternative schema type, either based on another key (not the same as `any.when()`) value, or a schema peeking into the current value, where:

* `condition` - the key name or [reference](https://github.com/hapijs/joi/blob/master/API.md#refkey-options), or a schema.
* `options` - an object with:
* `is` - the required condition joi type. Forbidden when `condition` is a schema.
* `then` - the alternative schema type to try if the condition is true. Required if `otherwise` is missing.
* `otherwise` - the alternative schema type to try if the condition is false. Required if `then` is missing.

```js
const schema = Joi
     .alternatives()
     .when(Joi.object({ b: 5 }).unknown(), {
        then: Joi.object({
           a: Joi.string(),
           b: Joi.any()
      }),
      otherwise: Joi.object({
        a: Joi.number(),
        b: Joi.any()
      })
});
```

### Nested Validation

When you want to validate an array of objects/items or just object keys

Both libraries support nested validation

Now what about express-validator?

#### Wildcards

Wildcards allow you to iterate over an array of items or object keys and validate each item or its properties.

The `*` character is also known as a wildcard.

```js
const express = require('express'); 
const { check } = require('express-validator/check'); 
const { sanitize } = require('express-validator/filter');  
const app = express(); 

app.use(express.json());  
app.post('/addresses', [   
    check('addresses.*.postalCode').isPostalCode(),
    sanitize('addresses.*.number').toInt() 
], 
(req, res) => {   // Handle the request });
```

**Joi**

```js
const schema = Joi.object().keys({
    addresses: Joi.array().items(
        Joi.object().keys({
            postalCode: Joi.string().required(),
        }),
    )
});
```

### Custom Error Messages

#### Joi

#### `any.error(err, [options])`

Overrides the default joi error with a custom error

```js
let schema = Joi.string().error(new Error('Was REALLY expecting a string'));
```

#### Express-validator

```js
const { check } = require('express-validator/check'); 

app.post('/user', [   
   // ...some other validations...   
   check('password')     
   .isLength({ min: 5 }).withMessage('must be at 5 chars long')
   .matches(/\d/).withMessage('must contain a number') 
], 
(req, res) => {   // Handle the request somehow });
```

### Conclusion

I covered the most important parts of both libraries and you can decide yourself which one you want to use. Please let me know in the comments below if I left out anything important in the comparison.

I hope you find it helpful when deciding the next input validation module for your express.js application.

I wrote an in-depth article on it here: [how to validate inputs](https://medium.freecodecamp.org/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7). Do check it out.

_Don’t hesitate to clap if you considered this a worthwhile read!_

_Originally published at [101node.io](https://101node.io/blog/javascript-validators-comparison-using-joi-vs-express-validator/) on March 31, 2019._

