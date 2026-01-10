---
title: JavaScript Get Request – How to Make an HTTP Request in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-15T19:05:24.000Z'
originalURL: https://freecodecamp.org/news/javascript-get-request-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--2-.png
tags:
- name: api
  slug: api
- name: axios
  slug: axios
- name: http
  slug: http
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When building applications, you will have to interact between the backend
  and frontend to get, store, and manipulate data.

  This interaction between your frontend application and the backend server is possible
  through HTTP requests.

  There are five pop...'
---

When building applications, you will have to interact between the backend and frontend to get, store, and manipulate data.

This interaction between your frontend application and the backend server is possible through HTTP requests.

There are five popular HTTP methods you can use to make requests and interact with your servers. One HTTP method is the GET method, which can retrieve data from your server.

This article will teach you how to request data from your servers by making a GET request. You will learn the popular methods that exist currently and some other alternative methods.

For this guide, we'll retrieve posts from the free [JSON Placeholder posts API](https://jsonplaceholder.typicode.com/posts).

There are two popular methods you can easily use to make HTTP requests in JavaScript. These are the Fetch API and Axios.

## How to Make a GET Request with the Fetch API

The Fetch API is a built-in JavaScript method for retrieving resources and interacting with your backend server or an API endpoint. Fetch API is built-in and does not require installation into your project.

Fetch API accepts one mandatory argument: the API endpoint/URL. This method also accepts an **option** argument, which is an optional object when making a GET request **because it is the default request**.

```js
  fetch(url, {
      method: "GET" // default, so we can ignore
  })
```

Let’s create a GET request to get a post from the [JSON Placeholder posts API](https://jsonplaceholder.typicode.com/posts).

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => response.json())
  .then((json) => console.log(json));
```

This will return a single post which you can now store in a variable and use within your project.

> Note: For other methods, such as POST and DELETE, you need to attach the method to the options array.

## How to Make a GET Request with Axios

Axios is an HTTP client library. This library is based on promises that simplify sending asynchronous HTTP requests to REST endpoints. We will send a GET request to the JSONPlaceholder Posts API endpoint.

Axios, unlike the Fetch API, is not built-in. This means you need to install Axios into your JavaScript project.

To install a dependency into your JavaScript project, you will first initialize a new `npm` project by running the following command in your terminal:

```js
$ npm init -y
```

And now you can install Axios to your project by running the following command:

```js
$ npm install axios
```

Once Axios is successfully installed, you can create your GET request. This is quite similar to the Fetch API request. You will pass the API endpoint/URL to the `get()` method, which will return a promise. You can then handle the promise with the `.then()` and `.catch()` methods.

```js
axios.get("https://jsonplaceholder.typicode.com/posts/1")
.then((response) => console.log(response.data))
.catch((error) => console.log(error));
```

> **Note:** The major difference is that, for Fetch API, you first convert the data to JSON, while Axios returns your data directly as JSON data.

At this point, you have learned how to make a GET HTTP request with Fetch API and Axios. But there are some other methods that still exist. Some of these methods are [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and jQuery.

## How to Make a GET Request with `XMLHttpRequest`

You can use the XMLHttpRequest object to interact with servers. This method can request data from a web server’s API endpoint/URL without doing a full page refresh.

> **Note:** All modern browsers have a built-in XMLHttpRequest object to request data from a server.

Let’s perform the same request with the XMLHttpRequest by creating a new XMLHttpRequest object. You will then open a connection by specifying the request type and endpoint (the URL of the server), then you'll send the request, and finally listen to the server’s response.

```js
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://jsonplaceholder.typicode.com/posts/1");
xhr.send();
xhr.responseType = "json";
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 200) {
    console.log(xhr.response);
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};
```

In the above code, a new XMLHttpRequest object is created and stored in a variable called `xhr`. You can now access all its objects using the variable, such as the `.open()` method, when you specify the request type (GET) and the endpoint/URL where you want to request data.

Another method you will use is `.send()`, which sends the request to the server. You can also specify the format in which the data will be returned using the `responseType` method. At this point, the GET request is sent, and all you have to do is listen to its response using the `onload` event listener.

If the client's state is done (**4),** and the status code is successful (**200)**, then the data will be logged to the console. Otherwise, an error message showing the error status will appear.

## How to Make a GET Request with jQuery

Making HTTP requests in jQuery is relatively straightforward and similar to the Fetch API and Axios. To make a GET request, you will first install jQuery or make use of its CDN in your project:

```js
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.2/jquery.min.js" integrity="sha512-tWHlutFnuG0C6nQRlpvrEhE4QpkG1nn2MOUMWmUeRePl4e3Aki0VB6W1v3oLjFtd0hVOtRQ9PHpSfN6u6/QXkQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

With jQuery, you can access the GET method `$.get()`, which takes in two parameters, the API endpoint/URL and a callback function that runs when the request is successful.

```js
$.get("https://jsonplaceholder.typicode.com/posts/1", (data, status) => {
  console.log(data);
});
```

> **Note:** In the callback function, you have access to the request's **data** and the request's **status**.

You can also use the jQuery AJAX Method, which is quite different and can be used to make asynchronous requests:

```js
$.ajax({
  url: "https://jsonplaceholder.typicode.com/posts/1",
  type: "GET",
  success: function (data) {
    console.log(data);
  }
});
```

## Wrapping Up

In this article, you have learned how to make the HTTP GET request in JavaScript. You might now begin to think — which method should I use?

If it’s a new project, you can choose between the Fetch API and Axios. Also, if you want to consume basic APIs for a small project, there is no need to use Axios, which demands installing a library.

Have fun coding!
