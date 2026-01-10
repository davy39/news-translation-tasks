---
title: What is a REST API? API Endpoint Request Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-10T16:39:44.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-life-of-pix-42408.jpg
tags:
- name: api
  slug: api
- name: REST API
  slug: rest-api
seo_title: null
seo_desc: 'An API (short for Application Programming Interface) allows for two or
  more applications to communicate with one another and send data back and forth.

  APIs operated based on a standardized set of rules and they''re an integral component
  of modern-day ...'
---

An API (short for Application Programming Interface) allows for two or more applications to communicate with one another and send data back and forth.

APIs operated based on a standardized set of rules and they're an integral component of modern-day software development.

There are different API styles, and each one has its unique architecture. One of the most common styles is REST.

In this article, you will learn the basics of REST APIs. You will see an overview of what they are and how they work. You will also learn what makes an API RESTful.

Let's get into it!

## What Is A REST API?

REST (short for REpresentational State Transfer) is a software architectural style created by computer scientist Roy Fielding in 2000. 

With REST APIs, a client requests a resource. Then the server responds to the client with a representation of the current state of that resource and all relevant information about it in a standardized format, such as JSON or XML.

## An Overview of REST API Concepts

In the previous section, I mentioned the terms client, resource, and server. What do they mean?

A **client** is a program running on a user's computer. 

This program could be a web browser, which initiates communication and makes requests to the API.

The role of the client is only to retrieve or modify information within the application.

A **resource** is any information the API can provide – a document, a text file, an image, a video, or any other object.

Each resource has a unique identifier, known as the Universal Resource Identifier (or URI), which is a string that refers to that specific resource.

A **server** is a system that stores the resource the client is requesting.

A server's role is to listen for and receive client requests for its resources and respond to them with the requested information.

The server sends back a representation of the resource's state and does not grant full access to the client.

## How Does A REST API Work?

A client sends an HTTP request to the server to perform a CRUD operation. CRUD is an acronym for `Create`, `Read`, `Update`, and `Delete`.

The server responds with a resource in a standardized format such as JSON (JavaScript Object Notation) or XML, with JSON being the most popular format used today.

### An Overview of REST API Requests

A REST API request needs to include the following:

- An operation
- An endpoint
- The parameters/body
- HTTP headers

Firstly, each request needs to include the **operation/action** you want the server to perform on the resource. 

In the section above, I mentioned that the client sends a request to the server to perform a CRUD operation.

Each CRUD operation is equivalent to an HTTP method/verb that defines the operation:

- The `Create` operation's equivalent is a `POST` request which indicates that you want to create a new resource.
- The `Read` operation's equivalent is a `GET` request which indicates that you want to retrieve a resource.
- The `Update` operation's equivalent is a `PUT` request which indicates that you want to edit or update a specific existing resource.
- The `Delete` operation's equivalent is a `DELETE` request which indicates that you want to delete a specific resource.

Then, the request must also include an **endpoint**.

An endpoint is a URL (short for Uniform Resource Locator) that contains the URI (Uniform Resource Identifier), which is the location where the API can find and interact with the specific resource.

You can view a list of endpoints in the documentation for the specific API you are using.

For example, when using [Spotify's API](https://developer.spotify.com/documentation/web-api/), the endpoint to get a [specific artist's album](https://developer.spotify.com/console/get-artist-albums/) looks something like the following:

```
https://api.spotify.com/v1/artists/{id}/albums
```

The request also optionally includes the **parameters/body**, which is any additional data and messages you might send to the server.

Lastly, the request also includes HTTP headers, which are authentication data such as an API key.
 
### An Overview of REST API Responses

After receiving the request, the server will return information about the requested resource.

The response is a representation of the state of the requested resource – not the resource itself.

Typically, the response is in the form of JSON data – a readable format for the client that made the request.

There is also an appropriate HTTP status code sent back in the response header to let the client know if the operation was successful or not.

Some of the most commonly used status codes are the following:

- `200 OK` means the request was successful
- `201 Created` means the request was successful, and a resource got created
- `204 No Content` means the request was successful, but there is no need to return a message body
- `400 Bad Request` means the server cannot process the request due to an error from the client's side
- `401 Unauthorized` means the server cannot process the request due to a lack of authentication credentials
- `403 Forbidden` means the client doesn't have permission to access the resource
- `404 Not Found` means the server cannot find the resource (this may be because it got deleted)
- `500 Internal Server Error` means the server encountered an unexpected error

## What Makes An API RESTful?

For an API to be considered RESTful, it should follow certain best practices, also known as architectural constraints.

The six constraints of the REST architecture are:

- Client-server separation
- A uniform interface
- Stateless
- Layered system
- Cacheable
- Executable code

Let's see each one in a bit more detail in the following sections.


### Client-Server separation

In REST API architecture, the client and server must work independently.

A client only initiates communication and sends a request to the server, and a server waits for requests from a client and responds appropriately.

This separation of concerns ensures system reliability and scalability.

When you separate the client from the server, you can change the client-side code without affecting the server. And you can modify the resources stored in the server without affecting the client.

### A Uniform Interface

All requests and responses must follow a format and protocol – there needs to be a standardized common language. 

This common language is HTTP (short for HyperText Transfer Protocol).

Note that HTTP was not designed for REST APIs – REST adopted the communication protocol.


###  Stateless

REST APIs are stateless, meaning the API treats each request from a client independently, and the request needs to include all the necessary information.

The server interprets each request as brand new – that is, it does not remember past information about the client. For example, it doesn't remember if the client has requested the same resource before.

This constraint enhances performance, scalability, and reliability.

### Layered System

The RESTful architecture has a layered structure, and each layer works independently – requests and responses go through separate hierarchical layers.

The client and server don't know whether they are communicating with an intermediary. There can be several other servers in the middle sitting between them that don't affect client-server interactions.

These layers can add security and manage and distribute traffic, which improves system security and scalability.

### Cacheable

REST APIs are designed with caching in mind. The response from the server should indicate whether a resource is cacheable or not.

If the resource is cacheable, the client can store and reuse frequently accessed data instead of requesting it again and again from the server.

When a resource is cacheable, it lowers a page's load time since the client fetches data from local storage and makes fewer calls to the server. The server, in turn, has less latency.


### Executable Code 

The final constraint is optional.

Instead of sending a representation of a static resource in JSON, the server may return some computer code in the form of a script that the client can execute.

That said, an API is RESTful even if it doesn't provide executable code.

## Conclusion

Hopefully, this article was helpful and gave you insight into what a REST API is, how it works, and what makes an API RESTful.

If you want to dive in more deeply to using REST APIs, here's a [guide to help you get started](https://www.freecodecamp.org/news/how-to-use-rest-api/).

And then if you want to try designing your own REST API, this [full handbook will walk you through the process](https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/).

Thank you for reading, and happy coding!


