---
title: How to Use Environment Variables the Right Way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-02T18:27:57.000Z'
originalURL: https://freecodecamp.org/news/using-environment-variables-the-right-way
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/cover.jpg
tags:
- name: Application Security
  slug: application-security
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
seo_title: null
seo_desc: "By Stanley Nguyen\nEnvironment variables are one of the foundational concepts\
  \ for application developers. And they're something we use on a daily basis. \n\
  Environment variables have even claimed a part in the de-facto twelve-factor app.\
  \ They have a lon..."
---

By Stanley Nguyen

Environment variables are one of the foundational concepts for application developers. And they're something we use on a daily basis. 

Environment variables have even claimed a part in [the de-facto twelve-factor app](https://12factor.net/config). They have a long list of benefits that includes application configurability and security, which are covered in many resources like [this one](https://hyperlane.co/blog/the-benefits-of-environment-variables-and-how-to-use-them), or even [this one from StackOverflow](https://serverfault.com/questions/892481/what-are-the-advantages-of-putting-secret-values-of-a-website-as-environment-var).

Environment variables are great and I'm completely behind the idea. However, everything comes at a cost – and environment variables, if wielded carelessly, can have harmful effects on our codebases and applications.

## The curse of environment variables

How could environment variables be a bad thing if they help us write more secure code and more easily configure our applications for different environments? 

Funny enough, environment variables' shortcomings actually derive from their very nature that makes them great: they're global and external, through which application developers are able to inject configurations and manage these secrets somewhere that's more difficult to compromise.

As developers, we all know how bad global states are for our applications. And please don't take my word for it, these evils have been discussed in a lot of places like [here](https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil), [here](https://thevaluable.dev/global-variable-explained/), and [here](https://stackoverflow.com/questions/19209468/why-is-global-state-bad).

For this article, I will be focusing on the 2 main flaws that I mostly encounter when dealing with environment variables:

* Inflexibility / Poor testability
* Code comprehension / readability

## How to use environment variables properly

Similarly to how I deal with global variables or global patterns (like singleton) that are applied in bad locations, my favourite weapon is [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection).

It's not going to be the exact same thing that we do to code dependencies, but the principles are the same. Instead of using environment variables (dependencies) directly, we inject them at callsites (that is, the place they are actually used). This inverts the relationship from "callsites depending" to "callsites requiring". 

Dependency injection solves these issues by:

* allowing developers to inject configurations more easily at test time
* reducing the mental scope for code readers to the package only, eliminating all externalities

## So how do we apply these principles?

I will be using a Node.js example to demonstrate how we can refactor a codebase and eliminate scattered environment variables.

### Hypothetical situation

Let's say we have a simple app with a single endpoint that will query for all TODOs in a PostGres database. Here is our database module with environment variables scattered into it:

```js
const { Client } = require("pg");

function Postgres() {
  const c = new Client({
    connectionString: process.env.POSTGRES_CONNECTION_URL,
  });
  this.client = c;
  return this;
}

Postgres.prototype.init = async function () {
  await c.connect();
  return this;
};

Postgres.prototype.getTodos = async function () {
  return this.client.query("SELECT * FROM todos");
};

module.exports = Postgres;

```

and this module will be injected into our HTTP controller through the application's entrypoint:

```js
const express = require("express");
const TodoController = require("./controller/todo");
const Postgres = require("./pg");

const app = express();

(async function () {
  const db = new Postgres();
  await db.init();
  const controller = new TodoController(db);
  controller.install(app);

  app.listen(process.env.PORT, (err) => {
    if (err) console.error(err);
    console.log(`UP AND RUNNING @ ${process.env.PORT}`);
  });
})();

```

Glancing at the above entry point file, we have no way of telling what the app's requirements for environment variables (or environment config in general) are (minus point for code glanceability 👎 ).

### Refactoring the code

The first step to improve the previously laid-out code is to identify all locations that environment variables are being used directly. 

For our specific case above, it's pretty straightforward as the codebase is small. But for larger codebases, you can use linting tools like [eslint](https://github.com/eslint/eslint) to scan for all locations that use environment variables directly. Just set up a rule, for example, forbidding environment variables (like `node/no-process-env` from [eslint-plugin-node](https://github.com/mysticatea/eslint-plugin-node#readme)).

Now it's time to remove direct uses of environment variables from our app's modules and include these configurations as part of the module's requirements:

```js
...
function Postgres(opts) {
  const { connectionString } = opts;
  const c = new Client({
    connectionString,
  });
  this.client = c;
  return this;
}
...

```

These configurations will then be supplied only from our application's entrypoint:

```js
...
const db = new Postgres({
  connectionString: process.env.POSTGRES_CONNECTION_URL,
});
...

```

It's much clearer what the environment requirements for our application are now, looking at the entrypoint. This prevents potential problems with forgotten-to-be-added environment variables.

The full source code for the above demo can be found [here](https://github.com/stanleynguyen/dispelling-environment-variable-curse-demo).

## Bonus: Frequently-asked-questions

These are some of the questions that **I think** might be asked by those reading this post. Maybe they're not actual frequently asked questionsk, but hey what's the harm in addressing possible alternative opinions?

### Why not use a central config file/module?

I have seen quite a few attempts to solve this problem using a central location for drawing out these values (like a `config.js` file/module for Node projects). 

But this approach is no better than actually using the environment variables provided by the application's runtime (like `process.env`) because everything is still consolidated in a somewhat global state (a single config object used throughout the app). 

In fact, it could be even worse, as now we're introducing another location for code to rot.

### What if I want a zero-config setup for my module?

Yes, who doesn't love zero-config, ready-to-roll modules. Again, I would like to re-iterate that building software is all about making trade-offs, and this comes at the cost of readability as this whole post has been discussing. 

If you would still like a possible zero-config setup, I would suggest having config objects (that is, the `opts` constructor argument in the prior code example) and direct environment variable usage only as a fallback, something like this:

```js
function Postgres(opts) {
  const connectionString =
    opts.connectionString || process.env.POSTGRES_CONNECTION_URL;
  const c = new Client({
    connectionString,
  });
  this.client = c;
  return this;
}

```

This way, readers of our code will still be able to recognise (although with less glanceability, as it's been traded for zero-configurability) the module's requirements.

### Thank you for reading!

Last but not least, if you like my writings, please head over to [my blog](https://blog.stanleynguyen.me/) for similar commentaries and follow [me on Twitter](https://twitter.com/stanley_ngn). 🎉

