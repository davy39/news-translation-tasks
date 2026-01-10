---
title: JavaScript POST Request – How to Send an HTTP POST Request in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-06T23:40:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-post-request-how-to-send-an-http-post-request-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--7-.png
tags:
- name: http
  slug: http
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'HTTP requests allow your front-end application to interact successfully
  with a back-end server or database.

  One of the five popular HTTP methods for making requests and interacting with your
  servers is the POST method, which you can use to send data ...'
---

HTTP requests allow your front-end application to interact successfully with a back-end server or database.

One of the five popular HTTP methods for making requests and interacting with your servers is the POST method, which you can use to send data to a server.

In this article, you will learn the various methods that you can use to send an HTTP POST request to your back-end server in JavaScript. We'll send GET requests to the [free JSON Placeholder todos API](https://jsonplaceholder.typicode.com/todos) for this guide.

There are two built-in JavaScript methods for making an HTTP POST request that don't require the installation of a library or the use of a CDN. These methods are the FetchAPI, based on JavaScript promises, and XMLHttpRequest, based on callbacks.

There are other methods, such as Axios and jQuery, that you will also learn how to use.

## How to Send a POST Request with the Fetch API

The FetchAPI is a built-in method that takes in one compulsory parameter: the endpoint (API URL). While the other parameters may not be necessary when making a GET request, they are very useful for the POST HTTP request.

The second parameter is used to define the body (data to be sent) and type of request to be sent, while the third parameter is the header that specifies the type of data you will send, for example JSON.

```js
fetch("https://jsonplaceholder.typicode.com/todos", {
  method: "POST",
  body: JSON.stringify({
    userId: 1,
    title: "Fix my bugs",
    completed: false
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});
```

In the code above, the body holds the data to be sent to the server and added to the JSONPlaceholder todos API. Also, the headers hold the type of content you want to send to the server, which in this case is JSON data.

**Note:** It is always best to serialize your data before sending it to a web server or API using the **JSON.stringify()** method. This will help convert and ensure your JSON data is in string format.

The Fetch API is based on JavaScript promises, so you need to use the .then method to access the promise or response returned.

```js
fetch("https://jsonplaceholder.typicode.com/todos", {
  method: "POST",
  body: JSON.stringify({
    userId: 1,
    title: "Fix my bugs",
    completed: false
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

If this is successful, it will return the new JSON data you send to the server.

## How to Send a POST Request with `XMLHttpRequest`

Like the Fetch API, `XMLHttpRequest` is also in-built and has existed much longer than the Fetch API. This means that almost all modern browsers have a built-in XMLHttpRequest object to request data from a server.

You will start by creating a new XMLHttpRequest object stored in a variable called `xhr`. This is important as it gives you access to all its objects using the variable.

For example, you can then open a connection with `.open()`, which is used to specify the request type and endpoint (the URL of the server). As you did for the FetchAPI, you will specify the type of data using the `setRequestHeader` method.

```js
const xhr = new XMLHttpRequest();
xhr.open("POST", "https://jsonplaceholder.typicode.com/todos");
xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8")
```

The next step is to create the data to be sent to the server. Make sure you serialize the data and then store it in a variable that you'll send with the `.send()` method after making some checks with the `.onload` method.

```js
const body = JSON.stringify({
  userId: 1,
  title: "Fix my bugs",
  completed: false
});
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 201) {
    console.log(JSON.parse(xhr.responseText));
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};
xhr.send(body);
```

When you put the code together, it will look like this and return the JSON data you send to the server:

```js
const xhr = new XMLHttpRequest();
xhr.open("POST", "https://jsonplaceholder.typicode.com/todos");
xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
const body = JSON.stringify({
  userId: 1,
  title: "Fix my bugs",
  completed: false
});
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 201) {
    console.log(JSON.parse(xhr.responseText));
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};
xhr.send(body);
```

The major difference between the Fetch API and `XMLHttpRequest` method is that the Fetch API has a better syntax that is easier to read and understand.

At this point, you have learned how to use the two JavaScript inbuilt methods to send POST HTTP requests. Let’s now learn how to use Axios and jQuery.

## How to Send a POST Request with Axios

Axios is an HTTP client library. This library is based on promises that simplify sending asynchronous HTTP requests to REST endpoints. We will send a GET request to the JSONPlaceholder Posts API endpoint.

Unlike the Fetch API and `XMLHttpRequest`, Axios is not built-in. This means you need to install Axios in your JavaScript project.

To install a dependency into your JavaScript project, you will first initialize a new `npm` project by running the following command in your terminal:

```bash
$ npm init -y
```

And now, you can install Axios in your project by running the following command:

```bash
$ npm install axios
```

Once Axios is successfully installed, you can send your POST request. This is quite similar to the Fetch API request.

You will pass the API endpoint/URL to the `post()` method, which will return a promise. You can then handle the promise with the `.then()` and `.catch()` methods.

```js
axios.post("https://jsonplaceholder.typicode.com/todos", {
    userId: 1,
    title: "Fix my bugs",
    completed: false
  })
  .then((response) => console.log(response.data))
  .then((error) => console.log(error));
```

**Note:** Axios will automatically serialize the object to JSON and set the Content-Type header to 'application/json' for you.

This will return the new data sent to the server.

## How to Send a POST Request with jQuery

Making an HTTP request in jQuery is similar to the Fetch API and Axios, but jQuery is not in-built. So you will first have to install or use its CDN in your project:

```js
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.2/jquery.min.js" integrity="sha512-tWHlutFnuG0C6nQRlpvrEhE4QpkG1nn2MOUMWmUeRePl4e3Aki0VB6W1v3oLjFtd0hVOtRQ9PHpSfN6u6/QXkQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

With jQuery, you can access the POST method `$.post()`, which takes in three parameters: the API endpoint/URL, the data to be sent to the server, and a callback function that runs when the request is successful.

```js
const body = {
  userId: 1,
  title: "Fix my bugs",
  completed: false
};
$.post("https://jsonplaceholder.typicode.com/todos", body, (data, status) => {
  console.log(data);
});
```

**Note:** You can access the request's data and status in the callback function.

You can check [this similar article on how to make an HTTP GET request in JavaScript](https://www.freecodecamp.org/news/javascript-get-request-tutorial/).

## Wrapping Up

In this article, you have learned how to send an HTTP POST request in JavaScript. You might now begin to think — which method should I use?

You can choose between the Fetch API and Axios if it's a new project. Also, if you want to consume basic APIs for a small project, Axios is optional because it demands installing a library.

Have fun coding!

You can access over 150 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.
