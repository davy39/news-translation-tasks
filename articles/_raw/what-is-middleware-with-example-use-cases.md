---
title: What is Middleware? Definition and Example Use Cases
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T17:10:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-middleware-with-example-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/edgar-chaparro-DPo30-zDO5g-unsplash.jpg
tags:
- name: Application Security
  slug: application-security
- name: Middleware
  slug: middleware
seo_title: null
seo_desc: 'By Yiğit Kemal Erinç

  Middleware is a commonly used term in web development. It can mean many things depending
  on the context, which makes the term a bit confusing.

  In this article, we will start by defining the term and then continue with a discussio...'
---

By Yiğit Kemal Erinç

Middleware is a commonly used term in web development. It can mean many things depending on the context, which makes the term a bit confusing.

In this article, we will start by defining the term and then continue with a discussion on some different use cases. 

After reading this article, you will be able to get more involved in technical and architectural conversations with your peers. You will also be more capable in terms of designing secure and reliable APIs and data flows.

## Definition of Middleware

Middleware is a software that acts as an intermediary between two applications or services to facilitate their communication. 

You can think of it as a proxy that can act as a data accumulator, translator, or just a proxy that forwards requests.

## Common Use Cases for Middleware

### 1) Translator

There are many data-interchange formats, such as JSON, XML and Protobuf. Even though we mostly use JSON nowadays, each of them have their own use cases. 

For example, Protobuffers are known to be more performant than JSON but they are not human readable. So you might be using Protobuffers for internal services and you might use JSON when the API consumer is a browser. 

You can also check out my [article](https://erinc.io/2020/08/09/what-is-protobuf-and-when-to-use-it/) on Protobuffers if you are interested in learning more about them.

Now let's say we need these two services, which speak different protocols, to communicate with each other.

We can create a middleware that makes use of a data conversion library and translates the requests to a format that the receiving service can understand.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/0.png)

### 2) Accumulating-Duplicating Data

Microservice architecture is a popular architectural pattern that is commonly applied in modern applications. 

If you're not familiar with microservices architecture, it basically means that your application consists of many small apps or services that are independent of each other and operate together by communicating over the internet.

For example, in an e-commerce project, you may have a microservice for storing and retrieving products, another microservice for searching, and another one for authentication and storing users. And each has its own database.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-10.png)

Now let's say that we want to implement our search in a way that it searches for both users and products. 

If this was a monolithic application we could simply write a query to search each table and join the results. But now our databases are running on different servers. 

This problem has multiple solutions, and we will look at two of them.

#### Accumulating Data

We can use a middleware to send requests to both servers, and ask them to search their databases for usernames and products that match the searched word. 

Then we can accumulate the results from both servers and return them to the client. Note that the number of requests increases linearly as we increase the number of servers (and we also need to merge those data).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/4-3.png)

#### Duplicating Data

We can store duplicate data in our search server so it can directly search them instead of requesting from product and user servers. This is less efficient in terms of memory but much faster – and speed is critical for search services.

If the tables we need are Product and User, we can create those tables in our search server as well. Then, whenever we save a new user to our user database, we will also save one copy in the search server.

We have a couple options: first, we can call the Search server's save methods from the User and Product servers' save methods to duplicate the data. Or we can create a middleware for saving, which will do the following: 

* Whenever a save request arrives, call Product/User server's save and Search server's save. 
* If the first save fails, do not call the save on other one (this keeps the databases consistent).

Let's look at the design diagrams without and with a middleware. First, this is how it looks without:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-7.png)

Looks ugly, right? Indeed, it is ugly and it will make your code more complicated and tightly coupled.

Here is the same solution with a middleware:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-6.png)

In this scenario, the client-side just calls the middleware to save a product or user and it handles the rest. 

There is no code related to duplicating the data either in the Product or User servers or the client-side. Middleware takes care of that stuff.

### 3) API Security

For any front end client-side code, we can view the outgoing requests, either in the browser's console or via a proxy. 

We talked about a User server that takes care of the login and sign-up. If our front end code directly sends the requests to that server, the address of our authentication server is exposed. After learning the IP address of our backend, attackers can use tools to find our endpoints and scan our server for vulnerabilities.

We can use middleware as a proxy to conceal our authentication server's URL. Our front end communicates with middleware and it will forward the request to the authentication server, and return the response back. 

This approach also allows us to block all requests to our authentication server, except the requests from our middleware's URL. This makes our authentication server much more secure. 

This was not possible previously, because our front end was communicating with the authentication server. Since the front end means the client's computer, we couldn't apply an IP filter.

### 4) Exposing Public APIs

In the previous part, we learned that middlewares can be used to restrict access to our API. 

Now let's look at the other side of the equation: what if we want to give restricted access to our API? Maybe we are a Software Engineer at a bank and the bank is planning a hackathon. We would need to provide access to our API, right? 

But since we are a bank, of course we can't provide access to the whole API and allow every operation. This means that we need to find a way to provide restricted access.

For this purpose, we can implement a middleware that only exposes some of the endpoints and redirects the requests to our actual API. Then we provide this API to the developers at the hackathon.

## Conclusion

In this post, we started off by defining what middleware is and tried to categorize the use-cases of middlewares in web development. 

Keep in mind that this is not a complete list of use-cases, but still I hope it was helpful to you. 

Thank you for reading. If you liked the article, I invite you to check out my [blog](https://erinc.io/). You can also subscribe to my mailing list to get notified when I publish a new post :)

