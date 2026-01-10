---
title: How to Simplify Asynchronous JavaScript using the Result-Error Pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T22:08:11.000Z'
originalURL: https://freecodecamp.org/news/simplify-asynchronous-javascript-using-the-result-error-pattern
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/locomotive-gfe169d971_1920-1.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Ken Snyder\nOver the last 18 years of programming, I've had to deal\
  \ with asynchronous behavior in virtually every project. \nSince the adoption of\
  \ async-await in JavaScript, we've learned that async-await makes a lot of code\
  \ more pleasant and easier..."
---

By Ken Snyder

Over the last 18 years of programming, I've had to deal with asynchronous behavior in virtually every project. 

Since the adoption of async-await in JavaScript, we've learned that async-await makes a lot of code more pleasant and easier to reason about.

Recently I noticed that when I work with a resource that needs to asynchronously connect and disconnect, I end up writing code like this:

```js
// NOT MY FAVORITE PATTERN
router.get('/users/:id', async (req, res) => {
  const client = new Client();
  let user;
  try {
    await client.connect();
    user = await client.find('users').where('id', req.path.id);
  } catch(error) {
    res.status(500);
    user = { error };
  } finally {
    await client.close();
  }
  res.json(user);
});
```

It gets verbose because we have to use try/catch to handle errors.

Examples of such resources include databases, ElasticSearch, command lines, and ssh.

In those use cases, I've settled into a code pattern I'm calling the Result-Error Pattern.

Consider rewriting the code above like this:

```js
// I LIKE THIS PATTERN BETTER
router.get('/users/:id', async (req, res) => {
  const { result: user, error } = await withDbClient(client => {
    return client.find('users').where('id', req.path.id);
  });
  if (error) {
    res.status(500);
  }
  res.json({ user, error });
});

```

Notice a few things:

1. The database client gets created for us and our callback can just utilize it.
2. Instead of capturing errors in a try-catch block, we rely on `withDbClient` to return errors.
3. The result is always called `result` because our callback may return any kind of data.
4. We don't have to close the resource.

So what does `withDbClient` do?

1. It handles creating the resource, connecting and closing.
2. It handles try, catch, and finally.
3. It ensures that there will be no uncaught exceptions thrown from `withDbClient`.
4. It ensures that any exceptions thrown in the handler also get caught inside `withDbClient`.
5. It ensures that `{ result, error }` will always be returned.

Here is an example implementation:

```js
// EXAMPLE IMPLEMENTATION
async function withDbClient(handler) {
  const client = new DbClient();
  let result = null;
  let error = null;
  try {
    await client.connect();
    result = await handler(client);
  } catch (e) {
    error = e;
  } finally {
    await client.close();
  }
  return { result, error };
}

```

## A step further

![Image](https://www.freecodecamp.org/news/content/images/2022/01/pexels-tom-fisk-1595104.jpg)
_Photo by [Tom Fisk](https://www.pexels.com/@tomfisk) from Pexels_

What about a resource that does not need to be closed? Well the Result-Error Pattern can still be nice!

Consider the following use of `fetch`:

```js
// THIS IS NICE AND SHORT
const { data, error, response } = await fetchJson('/users/123');

```

Its implementation might be the following:

```js
// EXAMPLE IMPLEMENTATION
async function fetchJson(...args) {
  let data = null;
  let error = null;
  let response = null;
  try {
    const response = await fetch(...args);
    if (response.ok) {
      try {
        data = await response.json();
      } catch (e) {
        // not json
      }
    } else {
      // note that statusText is always "" in HTTP2
      error = `${response.status} ${response.statusText}`;
    }
  } catch(e) {
    error = e;  
  }
  return { data, error, response };
}

```

## Higher-level use

![Image](https://www.freecodecamp.org/news/content/images/2022/01/aerial-g3ccde9887_1920.jpg)
_Photo by [16018388](https://pixabay.com/users/16018388-16018388/) from Pixabay_

We don't have to stop at low-level use. What about other functions that may end with a result or error?

Recently, I wrote an app with a lot of ElasticSearch interactions. I decided to also use the Result-Error pattern on higher-level functions.

For instance, searching for posts produces an array of ElasticSearch documents and returns result and error like this:

```js
const { result, error, details } = await findPosts(query);
```

If you've worked with ElasticSearch, you'll know that responses are verbose and data is nested several layers inside the response. Here, `result` is an object containing:

1. `records` – An Array of documents
2. `total` – The total number of documents if a limit was not applied
3. `aggregations` – ElasticSearch faceted-search information

As you might guess, `error` may be an error message and `details` is the full ElasticSearch response in case you need things like error metadata, highlights, or query time.

My implementation for searching ElasticSearch with a query object reads something like this:

```js
// Fetch from the given index name with the given query
async function query(index, query) {
  // Our Result-Error Pattern at the low level  
  const { result, error } = await withEsClient(client => {
    return client.search({
      index,
      body: query.getQuery(),
    });
  });
  // Returning a similar object also with result-error
  return {
    result: formatRecords(result),
    error,
    details: result || error?.meta,
  };
}
    
// Extract records from responses 
function formatRecords(result) {
  // Notice how deep ElasticSearch buries results?
  if (result?.body?.hits?.hits) {
    const records = [];
    for (const hit of result.body.hits.hits) {
      records.push(hit._source);
    }
    return {
      records,
      total: result.body.hits.total?.value || 0,
      aggregations: result.aggregations,
    };
  } else {
    return { records: [], total: null, aggregations: null };
  }
}    
```

And then the `findPosts` function becomes something simple like this:

```js
function findPosts(query) {
  return query('posts', query);
}
```

## Summary

Here are the key aspects of a function that implements the Result-Error Pattern:

1. Never throw exceptions.
2. Always return an object with the results and the error, where one may be null.
3. Hide away any asynchronous resource creation or cleanup.

And here are the corresponding benefits of calling functions that implement the Result-Error Pattern:

1. You don't need to use try-catch blocks.
2. Handling error cases is as simple as `if (error)`.
3. You don't need to worry about setup or cleanup operations.

Don't take my word for it, try it yourself!

