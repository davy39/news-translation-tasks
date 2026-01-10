---
title: Call vs Put vs Post – HTTP Request Methods Explained
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-13T14:59:18.000Z'
originalURL: https://freecodecamp.org/news/call-vs-put-vs-post-http-request-methods-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--7-.png
tags:
- name: http
  slug: http
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The HTTP (Hypertext Transfer Protocol) is the foundation of communication
  between clients (such as web browsers) and servers (such as web servers) on the
  World Wide Web.

  One crucial aspect of HTTP is the request method, which indicates the type of op...'
---

The HTTP (Hypertext Transfer Protocol) is the foundation of communication between clients (such as web browsers) and servers (such as web servers) on the World Wide Web.

One crucial aspect of HTTP is the request method, which indicates the type of operation the client wants to perform on a resource.

This article will explore three common HTTP request methods — Call, Put, and Post — and their applications in JavaScript web development.

## How HTTP Works

HTTP (Hypertext Transfer Protocol) is the foundation of communication on the World Wide Web. It is a protocol that governs how data is transmitted and received between clients (web browsers) and servers (web servers) over the internet.

When you enter a URL (Uniform Resource Locator) in your web browser and hit enter, your browser sends an HTTP request to the server hosting the website associated with that URL. The server then processes the request and sends back an HTTP response containing the requested data, such as a webpage, an image, or other resources.

HTTP uses a client-server model, where the client (typically a web browser) sends requests to the server, and the server responds with the requested data. One important aspect of HTTP is the concept of request methods, also known as HTTP verbs or methods.

Request methods are used to indicate the type of operation the client wants to perform on a resource on the server. HTTP defines several request methods, including Call, Put, Post, Delete, and more, each with its specific purpose and behavior.

These request methods are used to communicate the client's intention to the server and determine how the server should handle the request. Let's focus on three common request methods: Call, Put, and Post.

## How to Use the Call Method

In the context of an HTTP Request, the call method is called the [GET method](https://www.freecodecamp.org/news/javascript-get-request-tutorial/). It is used to retrieve data from a resource on the server. When you make a Call request, you ask the server to provide you with the data of a particular resource.

The Call method is considered "safe" and "idempotent." This means it should not have any side effects on the server and can be repeated multiple times without changing the outcome. In other words, making the same Call request multiple times should not result in any changes on the server.

In JavaScript web development, you often use the Call method to fetch data from APIs or retrieve resources from the server.

For example, you may use the Fetch API in JavaScript to request a Call to an API and retrieve data in JSON format:

```js
fetch("https://jsonplaceholder.typicode.com/posts?_limit=5")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

In this example, the Call request is made to the URL ‘https://jsonplaceholder.typicode.com/posts’ to fetch data from the server (`?_limit=5` is added to reduce the data fetched from 100 to 5). The response from the server is then parsed as JSON, and the retrieved data is logged to the console. You can now make use of the data within your application.

## How to Use the Put Method

The Put method is used to update data on the server or create a new resource if it does not already exist.

When you make a Put request, you ask the server to update the data of a particular resource or create a new resource with the provided data.

The Put method is considered "idempotent" but not "safe." This means that making the same Put request multiple times will not result in different outcomes but may have side effects on the server.

In JavaScript, you can use the Put method to send data to the server to update resources. For example, you may use the Fetch API to make a Put request with updated data to update a user's profile information on the server:

```js
const dataToUpdate = {
  id: 1,
  title: "Hello freeCodeCamp",
  body: "Welcome to freeCodeCamp",
  userId: 1
};

fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "PUT",
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  },
  body: JSON.stringify(dataToUpdate)
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

In this example, the Put request is made to the URL ‘https://jsonplaceholder.typicode.com/posts/1’ with the updated data in the request body. The server will then update the resource's data with ID 1 based on the provided data in the request body.

The response from the server, containing the updated data, is then parsed as JSON and logged to the console.

```js
{
  "id": 1,
  "title": "Hello freeCodeCamp",
  "body": "Welcome to freeCodeCamp",
  "userId": 1
}
```

**Note:** The PUT method is used to update data. The post of id 1 was updated.

## How to Use the Post Method

The [POST method](https://www.freecodecamp.org/news/javascript-post-request-how-to-send-an-http-post-request-in-js/) is used to submit data to the server to create a new resource.

When you make a Post request, you ask the server to create a new resource with the data provided in the request body. The Post method is not considered "idempotent" or "safe," as making the same Post request multiple times may create multiple resources with different outcomes.

In JavaScript, you can use the Post method to send data to the server to create new resources. For example, you may use the Fetch API to make a Post request with new data to create a new user account on the server:

```js
const newData = {
  title: "Hello freeCodeCamp",
  body: "Welcome to freeCodeCamp",
  userId: 1
};

fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  },
  body: JSON.stringify(newData)
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

In this example, the Post request is made to the URL ‘https://jsonplaceholder.typicode.com/posts’ with the new data in the request body. The server will then create a new resource with the provided data, and the response from the server, containing the newly created resource data, is parsed as JSON and logged to the console.

```js
{
  "title": "Hello freeCodeCamp",
  "body": "Welcome to freeCodeCamp",
  "userId": 1,
  "id": 101
}
```

**Note:** A new `id` of 101 is created because this is new data that does not exist before, so a unique ID is assigned to it.

## Best Practices and Considerations

1. **Use appropriate request methods:** It's important to choose the appropriate one based on the intended operation on the server-side resource. Use Call for custom actions or functions, Put for updating existing resources, and Post for creating new ones.
    
2. **Follow RESTful principles:** If you're building a RESTful API, it's important to follow the principles of Representational State Transfer (REST), which includes using standard HTTP request methods for CRUD operations. Use Get for retrieving resource data, Put for updating, Post for creating new resources, and Delete for deleting resources.
    
3. **Consider idempotency and safety:** Put requests are idempotent, meaning making the same request multiple times will have the same outcome as making it once. Post requests are not idempotent, and making the same request multiple times may create multiple resources with different outcomes. Consider your operation's idempotency and safety requirements when choosing the appropriate request method.
    

## Wrapping Up

HTTP is a crucial protocol that governs how data is transmitted and received between clients and servers on the World Wide Web. Request methods in HTTP, such as Call, Put, and Post, indicate the type of operation the client wants to perform on a resource on the server.

Understanding how these request methods work is essential in web development, as they determine how the server will handle the requests and what actions will be taken on the resources.

By utilizing the appropriate request methods in your web applications, you can effectively communicate with servers and manage resources reliably and efficiently.

Have fun coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Search 'request' for a deep dive into POST, GET, and making HTTP requests with React and JavaScript. Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
