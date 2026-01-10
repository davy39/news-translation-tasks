---
title: How to write powerful schemas in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-21T04:53:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-powerful-schemas-in-javascript-490da6233d37
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u_gVBtCyIcrWbOBv3xDCWg.png
tags:
- name: JavaScript
  slug: javascript
- name: mongoose
  slug: mongoose
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Diego Haz

  Introducing schm, a functional and highly composable library for creating schemas
  in JavaScript and Node.js


  _Background photo by [Willi Heidelbach](https://www.flickr.com/photos/wilhei/" rel="noopener"
  target="blank" title="Vá para a ga...'
---

By Diego Haz

#### Introducing [schm](https://github.com/diegohaz/schm), a functional and highly composable library for creating schemas in JavaScript and Node.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*u_gVBtCyIcrWbOBv3xDCWg.png)
_Background photo by [Willi Heidelbach](https://www.flickr.com/photos/wilhei/" rel="noopener" target="_blank" title="Vá para a galeria de Willi Heidelbach)_

I’ve been working with HTML, CSS, and JavaScript since 2002. The first time I needed some sort of schema in JavaScript was just a few years ago.

After using many different libraries and even authoring [one](https://github.com/diegohaz/querymen) and [another](https://github.com/diegohaz/bodymen), I decided to create [schm](https://github.com/diegohaz/schm). That’s the result of all my experience with schemas in JavaScript.

### What is [schm](https://github.com/diegohaz/schm)?

`schm` is a group of npm packages to help developers deal with schemas in JavaScript and Node.js.

It’s highly inspired by [Mongoose Schemas](http://mongoosejs.com/docs/guide.html). Actually, they’re so similar that you can use `schm` parameters within Mongoose Schemas and vice-versa. It's not MongoDB specific, though. You can use it for everything in JavaScript.

### What kind of problems does [schm](https://github.com/diegohaz/schm) solve?

#### ? Parsing and validation of form values

On the client, you can use schemas to define models for HTML forms. It makes it easier to transform and validate values. Also, if you’re using Node.js on the server, you can use the same schema. The result is a consistent behavior between client and server validations.

#### ? Parsing and validation of query string

Consider the following query string: `/?term=John&page=2&limit=10` . By combining packages such as [schm-koa](https://github.com/diegohaz/schm/tree/master/packages/schm-koa), [schm-express](https://github.com/diegohaz/schm/tree/master/packages/schm-express) and/or [schm-mongo](https://github.com/diegohaz/schm/tree/master/packages/schm-mongo), you will be able to parse and validate query strings with search terms and pagination with ease.

#### ☊ Communication between client and server

If you have an app that consumes resources from a REST API, for example, you can use schemas to define, on the client, the object structure your client expects to receive from the server. If something changes on the server (properties have been renamed, for example), you can just update your schema so your entire application will continue to work.

### Creating a schema

A simple schema is just a map of keys and types:

That’s the same as using a `type` property:

A schema can also be a map between keys and default values. Types will be automatically inferred:

That’s equivalent to doing the following:

To learn more about how to write schemas, take a look at [Mongoose Schemas](http://mongoosejs.com/docs/guide.html).

### Parsing values

After defining the schema, you can use it to parse values. This process will convert values to the proper types, as well as applying other parsers defined in the schema. These are the available parsers: `type`, `default` , `set` , `get` , `trim`, `uppercase` , `lowercase` .

The output will be something like this:

```
{  name: "HAZ",  birthdate: Tue Apr 10 1990 00:00:00 GMT,}
```

### Validating values

Just like in [Mongoose Schemas](http://mongoosejs.com/docs/guide.html), you can define validation rules within your schemas. These are the available validators: `validate` , `required` , `match` , `enum` , `max` , `min` , `maxlength` , `minlength` .

You can also create custom parsers and validators by extending the schema. We’ll talk about it later in this article.

The validation error will be, by default, an array of objects describing the errors.

```
[  {    message: "age must be greater than or equal 18",    min: 18,    param: "age",    validator: "min",    value: 17,  }]
```

If the validation passes, it will return the parsed values, just like `parse()`.

### Composing multiple schemas

Say you have separate schemas describing a `body`, `identity` and other things, and want to compose them to build a `human` schema. That's as easy as it sounds:

Another way to compose schemas is through nesting. A schema can be used as a `type` within another schema:

### Extending schemas

This is the part where `schm` really shines. You can add custom parsers and validators or even replace the default behavior of `parse` and `validate` methods by creating schema groups.

A **schema group** is a function that receives the previous schema as the only argument. Besides previous `params` , `parsers` and `validators` , the schema object has a `merge` method, which is useful for schema group functions to merge new functionality into the previous schemas.

The output of the above snippet will be something like this:

```
{  name: "Haz!!!",  age: 27,}
```

If you want to go further and learn more about how to create custom parsers, take a look at how parsers are written inside the core library [here](https://github.com/diegohaz/schm/blob/master/packages/schm/src/parsers.js).

By extending schemas, we can create many kinds of things. That’s how most of the `schm` satellite libraries, such as [schm-translate](https://github.com/diegohaz/schm/tree/master/packages/schm-translate), [schm-computed](https://github.com/diegohaz/schm/tree/master/packages/schm-computed) and [schm-mongo](https://github.com/diegohaz/schm/tree/master/packages/schm-mongo), are written.

We’re going to talk about one of them now.

### Renaming values keys

[schm-translate](https://github.com/diegohaz/schm/tree/master/packages/schm-translate) is one of the simplest, yet powerful, satellite libraries of `schm` . It's a few more than [10 lines of code](https://github.com/diegohaz/schm/blob/master/packages/schm-translate/src/index.js) compressed into one function which lets you translate values keys to your schema keys.

Say you’re working on a webapp that consumes resources from a REST API. Suddenly, developers change things on the API, which makes the response body return a slightly different model than the one the client expected. Instead of an `email` property, it returns now an array of `emails` .

This will probably make your app to break. If you don’t have a schema or any other centralized way to handle that object, you will need to update every part of the application to conform to the server changes.

With `schm` and `schm-translate` , it can be solved by changing a few lines of code in just one place:

The output will be exactly the one your app expected before the change:

```
{  name: "Haz",  email: "hazdiego@gmail.com",}
```

[Click here to see the list of all packages](https://github.com/diegohaz/schm#packages)

### How is this different from other schema libraries?

A common question is the difference between `schm` and other libraries, such as [Joi](https://github.com/hapijs/joi) and [ajv](https://github.com/epoberezkin/ajv) (which follows [JSON Schema](http://json-schema.org/) spec).

Comparing to `ajv`, `schm` doesn't follow any particular spec. Instead, it tries to mimic the Mongoose Schema API. Also, even though `ajv` has some parsing features, they're limited to [default values](https://github.com/epoberezkin/ajv#assigning-defaults) and [type coercion](https://github.com/epoberezkin/ajv#coercing-data-types).

In `schm`, the ability to parse values based on the schema is what makes it possible to transform a query string into a MongoDB query, for example.

That said, both `Joi` and `ajv` can be combined with `schm` . You can easily extend it to use a different validation method:

### Thank you for reading this!

If you like it and find it useful, here are some things you can do to show your support:

* Hit the clap ? button on this article a few times (up to 50)
* Give a star ⭐️ on GitHub: [https://github.com/diegohaz/schm](https://github.com/diegohaz/schm)
* Follow me on GitHub: [https://github.com/diegohaz](https://github.com/diegohaz)
* Follow me on Twitter: [https://twitter.com/diegohaz](https://twitter.com/diegohaz)

