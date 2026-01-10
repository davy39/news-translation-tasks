---
title: What is REST? Rest API Definition for Beginners
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-28T17:21:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/REST-API.png
tags:
- name: api
  slug: api
- name: http
  slug: http
- name: REST API
  slug: rest-api
seo_title: null
seo_desc: "In this article, you will learn what the term REST means and how it lets\
  \ us communicate with the server efficiently.\nBefore we get into REST, let's learn\
  \ what an API is. I believe this will help you understand REST better. \nWhat is\
  \ an API?\nSince we'r..."
---

In this article, you will learn what the term REST means and how it lets us communicate with the server efficiently.

Before we get into REST, let's learn what an API is. I believe this will help you understand REST better. 

## **What is an API?**

Since we're talking about REST APIs, our definition of an API will not go beyond the scope of the web. 

API stands for Application Programming Interface. An API establishes a connection between programs so they can transfer data. 

A program that has an API implies that some parts of its data is exposed for the client to use. The client could be the frontend of the same program or an external program.

In order to get this data, a structured request has to be sent to the API. If the request meets the desired requirements, a response which contains the data gets sent back to where the request was made. This response usually comes in the form of JSON or XML data.

In some cases, you'll need some sort of authorization to gain access to external API data.

Every API has documentation that tells you what data is available and how to structure your request in order to get a valid response.

### API Example

Was that confusing?

Let's use a real life scenario to give an example.

Imagine visiting a new restaurant. You're there to order food, and since you haven't been there before, you don't exactly know what type of food they serve. 

The server then approaches you with a menu so you can pick what you'd like to eat. After making your choice, the server then goes to the kitchen and gets your food.

In this case, the server is the API who is connecting you to the kitchen. The API's documentation is the menu. The request is made when you pick what you'd like to eat, and the response is the food being served.

I hope that helps you understand what an API is and how it works.

## What is REST?

REST stands for REpresentational State Transfer. It is a standard that guides the design and development of processes which enable us interact with data stored on a web servers. 

The above definition may not look as complex or "professional" as the ones you come across on the internet, but the goal here is for you to understand the basic purpose of REST APIs.

An API that complies with some or all of the [six guiding constraints](https://en.wikipedia.org/wiki/Representational_state_transfer#:~:text=The%20REST%20architectural%20style%20defines,visibility%2C%20portability%2C%20and%20reliability.) of REST is considered to be **RESTful.**

We are able to communicate with servers using the HTTP protocol. With these protocols, we can **Create**, **Read**, **Update** and **Delete** data – otherwise known as **CRUD** operations. 

But how can we perform these CRUD operations and communicate with data on the server? 

We can do this by sending HTTP requests, and that is where REST comes in. REST simplifies the communication process by providing various HTTP methods/operations/verbs which we can use to send requests to the server.

## How to communicate with a server using REST APIs

As we discussed in the last section, REST APIs make the communication process with the server easier for us by giving us various HTTP request methods. The most commonly used methods are:

* **GET**: The get method is used to **Read** data on the server.
* **POST**: The post method is used to **Create** data.
* **PATCH/PUT**: The patch method is used to **Update** data.
* **DELETE**: The delete method is used to **Delete** data.

These methods provided by REST allow us perform CRUD operations easily. That is:

Create => POST.  
Read => GET.  
Update => PATCH/PUT.  
Delete => DELETE.

So if we are to make a request to a server, let's say to retrieve data, we are going to make a **GET** request to an endpoint/resource provided by the server. The endpoint is similar to a URL.

If the request made is a valid one, then the server will respond to us with the data we requested. It also sends a status code where 200 is a success and 400 is a client error.

Here is an example of a request made to the JSONPlaceholder API using JavaScript:

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))
```

When making a request using the `fetch` API, the default method is the GET method – so we are not forced to specify it. But we do need to specify when making a request using the other methods. 

In the code example above, the endpoint is [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) and the specific data we are requesting is one todo item. The data will be returned to us in JSON format.

If we were to make a POST request, then we would include the method type which would be POST and a request body which would contain the data we are creating to send to the server. 

Deleting would require that we use the corresponding request method along with the id of the todo item we want to delete. Like this: 

```js
fetch('https://jsonplaceholder.typicode.com/posts/3', {
  method: 'DELETE',
});
```

Updating would require both the id and the request body that would be used to update the data. Here is an example:

```js
fetch('https://jsonplaceholder.typicode.com/posts/5', {
  method: 'PATCH',
  body: JSON.stringify({
    title: 'new todo',
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

## Conclusion

In this tutorial, you learned what REST is and how it helps us communicate with the server efficiently. 

We defined an API and gave an example to help explain its meaning. We also got to know some of the methods provided by REST to create, read, update and delete data stored on the server.

Thank you for reading!

