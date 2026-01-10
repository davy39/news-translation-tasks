---
title: How to write beautiful Node.js APIs using async/await and the Firebase Database
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-05T03:29:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-beautiful-node-js-apis-using-async-await-and-the-firebase-database-befdf3a5ffee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6wZYofh0czXf3SO8Ubw2xg.png
tags:
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Paul Breslin

  This tutorial will cover the typical use cases you’ll come across when writing RESTful
  API endpoints to read and write to a Firebase Database instance.

  There will be a focus on beautiful asynchronous code, which makes use of the async...'
---

By Paul Breslin

This tutorial will cover the typical use cases you’ll come across when writing RESTful API endpoints to read and write to a Firebase Database instance.

There will be a focus on **beautiful** asynchronous code, which makes use of the `async/await` feature in Node.js (available in v7.6 and above).

(Feel free to smile sweetly as you wave goodbye to callback hell ?)

### Prerequisites

I’ll assume that you already have a Node.js application set up with the Firebase Admin SDK. If not, then check out the [official setup guide](https://firebase.google.com/docs/admin/setup).

### Writing data

First off, let’s create an example `POST` endpoint which will save words to our Firebase Database instance:

This is a very basic endpoint which takes a `userId` and a `word` value, then saves the given word to a `words` collection. Simple enough.

But something’s wrong. We’re missing error handling! In the example above, we return a `201` status code (meaning the resource was created), even if the word wasn’t properly saved to our Firebase Database instance.

So, let’s add some error handling:

Now that the endpoint returns accurate status codes, the client can display a relevant message to the user. For example, “Word saved successfully.” Or “Unable to save word, click here to try again.”

> Note: if some of the ES2015+ syntax looks unfamiliar to you, check out the Babel [ES2015 guide](https://babeljs.io/learn-es2015/).

### Reading data

OK, now that we’ve written some data to our Firebase Database, let’s try reading from it.

First, let’s see what a `GET` endpoint looks like using the original promise-based method:

Again, simple enough. Now let’s compare it with an `async/await` version of the same code:

Note the `async` keyword added before the function parameters `(req, res)` and the `await` keyword which now precedes the `db.ref()` statement.

The `db.ref()` method returns a promise, which means we can use the `await` keyword to “pause” execution of the script. (The `await` keyword can be used with any promise).

The final `res.send()` method will **only run** **after** the `db.ref()` promise is fulfilled.

That’s all well and good, but the true beauty of `async/await` becomes apparent when you need to chain multiple asynchronous requests.

Let’s say you had to run a number of asynchronous functions sequentially:

Not pretty. This is also known as the “pyramid of doom” (and we haven’t even added error handlers yet).

Now take a look at the above snippet rewritten to use `async/await`:

No more pyramid of doom! What’s more, all of the `await` statements can be wrapped in a single `try/catch` block to handle any errors:

### Parallel async/await requests

What about cases where you need to fetch multiple records from your Firebase Database at the same time?

Easy. Just use the `Promise.all()` method to run Firebase Database requests in parallel:

### One more thing

When creating an endpoint to return data retrieved from a Firebase Database instance, be careful not to simply return the entire `snapshot.val()`. This can cause an issue with JSON parsing on the client.

For example, say your client has the following code:

The `snapshot.val()` returned by Firebase can either be a JSON object, or `null` if no record exists. If `null` is returned, the `response.json()` in the above snippet will throw an error, as it’s attempting to parse a non-object type.

To protect yourself from this, you can use `Object.assign()` to always return an object to the client:

Thanks for reading!

_Interested in seeing a real-world project built on top of Firebase and Node.js? Check out [Vocabify](https://vocabifyapp.com), the vocabulary builder that helps you remember the words you come across._

