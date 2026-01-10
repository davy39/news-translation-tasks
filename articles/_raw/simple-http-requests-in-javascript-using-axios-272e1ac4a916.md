---
title: Simple HTTP requests in JavaScript using Axios
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-04-11T11:27:52.000Z'
originalURL: https://freecodecamp.org/news/simple-http-requests-in-javascript-using-axios-272e1ac4a916
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AIVLX97Nn6e3NfKOkvWTEQ.png
tags:
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Introduction

  Axios is a very popular JavaScript library you can use to perform HTTP requests.
  It works in both Browser and Node.js platforms.

  Is supports all modern browsers, includin...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

### Introduction

Axios is a very popular JavaScript library you can use to perform HTTP requests. It works in both Browser and [Node.js](https://flaviocopes.com/nodejs/) platforms.

Is supports all modern browsers, including IE8 and higher.

It is promise-based, and this lets us write async/await code to perform [XHR](https://flaviocopes.com/xhr/) requests very easily.

Using Axios has quite a few advantages over the native [Fetch API](https://flaviocopes.com/fetch-api/):

* supports older browsers (Fetch needs a polyfill)
* has a way to abort a request
* has a way to set a response timeout
* has built-in CSRF protection
* supports upload progress
* performs automatic JSON data transformation
* works in Node.js

### Installation

Axios can be installed using [npm](https://flaviocopes.com/npm/):

```
npm install axios
```

or [yarn](https://flaviocopes.com/yarn/):

```
yarn add axios
```

or simply include it in your page using unpkg.com:

```
<script src="https://unpkg.com/axios/dist/axios.min.js"><;/script>
```

### The Axios API

You can start an HTTP request from the `axios` object:

```
axios({  url: 'https://dog.ceo/api/breeds/list/all',  method: 'get',  data: {    foo: 'bar'  }})
```

but for convenience, you will generally use

* `axios.get()`
* `axios.post()`

(like in jQuery, you would use `$.get()` and `$.post()` instead of `$.ajax()`)

Axios offers methods for all the HTTP verbs, which are less popular but still used:

* `axios.delete()`
* `axios.put()`
* `axios.patch()`
* `axios.options()`

It also offers a method to get the HTTP headers of a request, discarding the body.

### GET requests

One convenient way to use Axios is to use the modern (ES2017) async/await syntax.

This Node.js example queries the [Dog API](https://dog.ceo/) to retrieve a list of all the dog breeds, using `axios.get()`, and it counts them:

```
const axios = require('axios')const getBreeds = async () => {  try {    return await axios.get('https://dog.ceo/api/breeds/list/all')  } catch (error) {    console.error(error)  }}const countBreeds = async () => {  const breeds = await getBreeds()  if (breeds.data.message) {    console.log(`Got ${Object.entries(breeds.data.message).length} breeds`)  }}countBreeds()
```

If you don’t want to use async/await, you can use the [Promises](https://flaviocopes.com/javascript-promises/) syntax:

```
const axios = require('axios')const getBreeds = () => {  try {    return axios.get('https://dog.ceo/api/breeds/list/all')  } catch (error) {    console.error(error)  }}const countBreeds = async () => {  const breeds = getBreeds()    .then(response => {      if (response.data.message) {        console.log(          `Got ${Object.entries(response.data.message).length} breeds`        )      }    })    .catch(error => {      console.log(error)    })}countBreeds()
```

### Add parameters to GET requests

A GET response can contain parameters in the URL, like this: `[https://site.com/?foo=bar](https://site.com/?foo=bar.)`[.](https://site.com/?foo=bar.)

With Axios you can perform this by simply using that URL:

```
axios.get('https://site.com/?foo=bar')
```

or you can use a `params` property in the options:

```
axios.get('https://site.com/', {  params: {    foo: 'bar'  }})
```

### POST Requests

Performing a POST request is just like doing a GET request, but instead of `axios.get`, you use `axios.post`:

```
axios.post('https://site.com/')
```

An object containing the POST parameters is the second argument:

```
axios.post('https://site.com/', { foo: 'bar' })
```

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

