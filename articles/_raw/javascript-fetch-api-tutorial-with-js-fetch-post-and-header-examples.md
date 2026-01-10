---
title: JavaScript Fetch API Tutorial with JS Fetch Post and Header Examples
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-21T20:26:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-fetch-api-tutorial-with-js-fetch-post-and-header-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/wall-2.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: REST API
  slug: rest-api
seo_title: null
seo_desc: 'If you are writing a web application, chances are you will have to work
  with external data. This can be your own database, third party APIs, and so on.

  When AJAX first appeared in 1999, it showed us a better way to build web applications.
  AJAX was a ...'
---

If you are writing a web application, chances are you will have to work with external data. This can be your own database, third party APIs, and so on.

When [AJAX](https://en.wikipedia.org/wiki/Ajax_%28programming%29) first appeared in 1999, it showed us a better way to build web applications. AJAX was a milestone in web development and is the core concept behind many modern technologies like React.

Before AJAX, you had to re-render an entire web page even for minor updates. But AJAX gave us a way to fetch content from the backend and update selected user interface elements. This helped developers improve user experience and build larger, complicated web platforms.

## Crash Course on REST APIs

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-9.png)

We are now in the age of [RESTful APIs](https://restfulapi.net/). Simply put, a REST API lets you push and pull data from a datastore. This might either be your database or a third party’s server like the [Twitter API](https://developer.twitter.com/en/docs/twitter-api).

There are a few different types of REST APIs. Let’s look at the ones you will use in most cases.

* **GET** — Get data from the API. For example, get a twitter user based on their username.
* **POST** — Push data to the API. For example, create a new user record with name, age, and email address.
* **PUT** — Update an existing record with new data. For example, update a user’s email address.
* **DELETE** — Remove a record. For example, delete a user from the database.

There are three elements in every REST API. The request, response, and headers.

**Request** — This is the data you send to the API, like an order id to fetch the order details.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-6.png)
_Sample Request_

**Response** — Any data you get back from the server after a successful / failed request.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-5.png)
_Sample Response_

**Headers** — Additional metadata passed to the API to help the server understand what type of request it is dealing with, for example “content-type”.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/4-2.png)
_Sample Headers_

The real advantage of using a REST API is that you can build a single API layer for multiple applications to work with. 

If you have a database that you want to manage using a web, mobile, and desktop application, all you need is a single REST API Layer.

Now that you know how REST APIs work, let's look at how we can consume them.

## XMLHttpRequest

Before [JSON](https://www.w3schools.com/js/js_json_intro.asp) took over the world, the primary format of data exchange was XML. XMLHttpRequest() is a JavaScript function that made it possible to fetch data from APIs that returned XML data. 

XMLHttpRequest gave us the option to fetch XML data from the backend without reloading the entire page.

This function has grown from its initial days of being XML only. Now it supports other data formats like JSON and plaintext.

Let's write a simple XMLHttpRequest call to the GitHub API to fetch my profile.

```javascript
// function to handle success
function success() {
    var data = JSON.parse(this.responseText); //parse the string to JSON
    console.log(data);
}

// function to handle error
function error(err) {
    console.log('Request Failed', err); //error details will be in the "err" object
}

var xhr = new XMLHttpRequest(); //invoke a new instance of the XMLHttpRequest
xhr.onload = success; // call success function if request is successful
xhr.onerror = error;  // call error function if request failed
xhr.open('GET', 'https://api.github.com/users/manishmshiva'); // open a GET request
xhr.send(); // send the request to the server.
```

The above code will send a GET request to [https://api.github.com/users/manishmshiva](https://api.github.com/users/manishmshiva) to fetch my GitHub info in JSON. If the response was successful, it will print the following JSON to the console:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-2.png)

If the request failed, it will print this error message to the console:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/8-1.png)

## Fetch API

The Fetch API is a simpler, easy-to-use version of XMLHttpRequest to consume resources asynchronously. Fetch lets you work with REST APIs with additional options like caching data, reading streaming responses, and more.

The major difference is that Fetch works with promises, not callbacks. JavaScript developers have been moving away from callbacks after the introduction of promises.

For a complex application, you might easily get into a habit of writing callbacks leading to [callback hell](http://callbackhell.com/). 

With promises, it is easy to write and handle asynchronous requests. If you are new to promises, [you can learn how they work here](https://javascript.info/promise-basics).

Here is how the function we wrote earlier would look like if you used fetch() instead of XMLHttpRequest:

```javascript
// GET Request.
fetch('https://api.github.com/users/manishmshiva')
    // Handle success
    .then(response => response.json())  // convert to json
    .then(json => console.log(json))    //print data to console
    .catch(err => console.log('Request Failed', err)); // Catch errors
```

The first parameter of the Fetch function should always be the URL. Fetch then takes a second JSON object with options like method, headers, request body, and so on.

There is an important difference between the response object in XMLHttpRequest and Fetch. 

XMLHttpRequest returns the data as a response while the response object from Fetch contains information about the response object itself. This includes headers, status code, etc. We call the “res.json()” function to get the data we need from the response object.

Another important difference is that the Fetch API will not throw an error if the request returns a 400 or 500 status code. It will still be marked as a successful response and passed to the ‘then’ function.

Fetch only throws an error if the request itself is interrupted. To handle 400 and 500 responses, you can write custom logic using ‘response.status’. The ‘status’ property will give you the status code of the returned response.

Great. Now that you understand how the Fetch API works, let's look at a couple more examples like passing data and working with headers.

## Working with Headers

You can pass headers using the “headers” property. You can also use the [headers constructor](https://developer.mozilla.org/en-US/docs/Web/API/Headers) to better structure your code. But passing a JSON object to the “headers” property should work for most cases.

```javascript
fetch('https://api.github.com/users/manishmshiva', {
  method: "GET",
  headers: {"Content-type": "application/json;charset=UTF-8"}
})
.then(response => response.json()) 
.then(json => console.log(json)); 
.catch(err => console.log(err));
```

## Passing Data to a POST Request

For a POST request, you can use the “body” property to pass a JSON string as input. Do note that the request body should be a JSON string while the headers should be a JSON object.

```javascript
// data to be sent to the POST request
let _data = {
  title: "foo",
  body: "bar", 
  userId:1
}

fetch('https://jsonplaceholder.typicode.com/posts', {
  method: "POST",
  body: JSON.stringify(_data),
  headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(response => response.json()) 
.then(json => console.log(json));
.catch(err => console.log(err));
```

The Fetch API is still in active development. We can expect better features in the near future. 

However, most browsers support the use of Fetch in your applications. The chart below should help you figure out which browsers support it on the web and mobile apps.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/6-2.png)

I hope this article helped you understand how to work with the Fetch API. Be sure to try out Fetch for your next web application.

---

_I regularly write about Machine Learning, Cyber Security, and DevOps. You can signup for my_ [_weekly newsletter_](https://www.manishmshiva.com/) _here._

