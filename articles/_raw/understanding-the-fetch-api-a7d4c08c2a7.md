---
title: Understanding the Fetch API
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-03-15T02:58:01.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-fetch-api-a7d4c08c2a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2uRk3VpmBwXvnuRtfBReSQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Since IE5 was released in 1998, we’ve had the option to make asynchronous network
  calls in the browser using XMLHttpRequest (XHR).

  Quite a few years after this, Gmail and other rich a...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

Since IE5 was released in 1998, we’ve had the option to make asynchronous network calls in the browser using [XMLHttpRequest (XHR)](https://flaviocopes.com/xhr/).

Quite a few years after this, Gmail and other rich apps made heavy use of it, and made the approach so popular that it had to have a name: **AJAX**.

Working directly with the XMLHttpRequest has always been a pain, and it was almost always abstracted by some library. In particular, jQuery has its own helper functions built around it:

* `jQuery.ajax()`
* `jQuery.get()`
* `jQuery.post()`

and so on.

They had a huge impact on making asynchronous calls more accessible. In particular, they focused on older browsers to make sure everything still worked.

The **Fetch API** has been standardized as a modern approach to asynchronous network requests and uses [**Promises**](https://flaviocopes.com/javascript-promises/) as a building block.

Fetch at the time of writing (Sep 2017) has a good support across the major browsers, except IE.

![Image](https://cdn-media-1.freecodecamp.org/images/ZTZudnYkwsXj7jUrXoEcNRjAyqKBjqoLalmx)

The [polyfill](https://github.com/github/fetch) released by GitHub allows us to use `fetch` on any browser.

### Using Fetch

Starting to use Fetch for `GET` requests is very simple:

```
fetch('/file.json')
```

You’re already using it: fetch is going to make an HTTP request to get the `file.json` resource on the same domain.

As you can see, the `fetch` function is available in the global `window` scope.

Now let’s make this a bit more useful, let’s actually see what the content of the file is:

```
fetch('./file.json') .then(response => response.json()).then(data => console.log(data))
```

Calling `fetch()` returns a promise. We can wait for the promise to resolve by passing a handler with the `then()` method of the promise.

That handler receives the return value of the `fetch` promise, a Response object.

We’ll see this object in more detail in the next section.

### Catching errors

Since `fetch()` returns a promise, we can use the `catch` method of the promise to intercept any error occurring during the execution of the request, and the processing is done in the `then` callbacks:

```
fetch('./file.json').then(response => {  //...}.catch(err => console.error(err))
```

### Response Object

The Response Object returned by a `fetch()` call contains all the information about the request and the response of the network request.

Accessing the `headers` property on the `response` object gives you the ability to look into the HTTP headers returned by the request:

```
fetch('./file.json').then(response => {  console.log(response.headers.get('Content-Type'))  console.log(response.headers.get('Date'))})
```

![Image](https://cdn-media-1.freecodecamp.org/images/OJOg4dW3f2GWea2bcfnwa4MvECpCZ7WbwHxo)

#### status

This property is an integer number representing the HTTP response status.

* `101`, `204`, `205`, or `304` is a `null body` status
* `200` to `299`, inclusive, is an `OK` status (success)
* `301`, `302`, `303`, `307`, or `308` is a `redirect`

```
fetch('./file.json') .then((response) => {   console.log(response.status) })
```

#### statusText

`statusText` is a property representing the status message of the response. If the request is successful, the status is `OK`.

```
fetch('./file.json') .then(response => console.log(response.statusText))
```

#### url

`url` represents the full URL of the property that we fetched.

```
fetch('./file.json') .then(response => console.log(response.url))
```

### Body content

A response has a body, accessible using the `text()` or `json()` methods, which return a promise.

```
fetch('./file.json').then(response => response.text()).then(body => console.log(body))
```

```
fetch('./file.json').then(response => response.json()).then(body => console.log(body))
```

![Image](https://cdn-media-1.freecodecamp.org/images/bUd5fnaOF3fWarIFA7kr5j2cU-Y9LLvnE35F)

The same can be written using the [ES2017](https://flaviocopes.com/ecmascript/) [async functions](https://flaviocopes.com/async-await/):

```
(async () => {  const response = await fetch('./file.json')  const data = await response.json()  console.log(data)})()
```

### Request Object

The Request object represents a resource request, and it’s usually created using the `new Request()` API.

Example:

```
const req = new Request('/api/todos')
```

The Request object offers several read-only properties to inspect the resource request details, including

* `method`: the request’s method (GET, POST, etc.)
* `url`: the URL of the request.
* `headers`: the associated Headers object of the request
* `referrer`: the referrer of the request
* `cache`: the cache mode of the request (e.g., default, reload, no-cache).

And exposes several methods including `json()`, `text()` and `formData()` to process the body of the request.

The full API can be found [here](https://developer.mozilla.org/docs/Web/API/Request).

Being able to set the HTTP request header is essential, and `fetch` gives us the ability to do this using the Headers object:

```
const headers = new Headers()headers.append('Content-Type', 'application/json')
```

or, simpler:

```
const headers = new Headers({   'Content-Type': 'application/json' })
```

To attach the headers to the request, we use the Request object, and pass it to `fetch()` instead of simply passing the URL.

Instead of:

```
fetch('./file.json')
```

we do

```
const request = new Request('./file.json', {   headers: new Headers({ 'Content-Type': 'application/json' }) }) 
```

```
fetch(request)
```

The Headers object is not limited to setting values, but we can also query it:

```
headers.has('Content-Type') headers.get('Content-Type')
```

and we can delete a header that was previously set:

```
headers.delete('X-My-Custom-Header')
```

### POST Requests

Fetch also allows you to use any other HTTP method in your request: POST, PUT, DELETE or OPTIONS.

Specify the method in the method property of the request, and pass additional parameters in the header and in the request body:

Example of a POST request:

```
const options = {   method: 'post',   headers: {     "Content-type": "application/x-www-form-urlencoded; charset=UTF-8" },     body: 'foo=bar&test=1' } 
```

```
fetch(url, options) .catch((err) => {   console.error('Request failed', err) })
```

### **How to cancel a fetch request**

For a few years after `fetch` was introduced, there was no way to abort a request once opened.

Now we can, thanks to the introduction of `AbortController` and `AbortSignal`, a generic API to notify **abort** events

You integrate this API by passing a signal as a fetch parameter:

```
const controller = new AbortController()const signal = controller.signalfetch(‘./file.json’, { signal })
```

You can set a timeout that fires an abort event 5 seconds after the fetch request has started, to cancel it:

```
setTimeout(() => controller.abort(), 5 * 1000)
```

Conveniently, if the fetch already returned, calling `abort()` won’t cause any error.

When an abort signal occurs, fetch will reject the promise with a `DOMException` named `AbortError`:

```
fetch('./file.json', { signal }).then(response => response.text()).then(text => console.log(text)).catch(err => {  if (err.name === 'AbortError') {    console.error('Fetch aborted')  } else {    console.error('Another error', err)  }})
```

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

