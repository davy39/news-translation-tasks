---
title: What is an API Gateway and Why is it Useful?
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-12-11T21:40:25.000Z'
originalURL: https://freecodecamp.org/news/what-are-api-gateways
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/cover.png
tags:
- name: api
  slug: api
seo_title: null
seo_desc: APIs are often referred to as the front-door for applications to access
  data and business logic from backend services. As explained here, an API is essentially
  the interface that a piece of software presents to other humans or programs, allowing
  them...
---

APIs are often referred to as the front-door for applications to access data and business logic from backend services. As explained [here](https://lightcloud.substack.com/p/api-integration-patterns), an API is essentially the *interface* that a piece of software presents to other humans or programs, allowing them to interact with that software.

When creating an API, you need to choose a programming language (Java, Python, PHP, and so on) in which to write the API logic. You also need to deploy the API to a server, and you need to monitor the API to ensure your infrastructure has enough capacity to deal with a large number of requests.

API gateways abstract these steps away. You don’t have to write much code or worry about managing the underlying infrastructure. You simply create API endpoints which clients can send requests to.

The major cloud providers all have a fully managed API gateway service:

1. [AWS API Gateway](https://aws.amazon.com/api-gateway/)
    
2. [GCP API Gateway](https://cloud.google.com/api-gateway)
    
3. [Azure API Management](https://azure.microsoft.com/en-gb/products/api-management)
    

This article will explain why you should use an API gateway, how they work, and we'll look at a real world example of an API gateway in action.

### What we'll cover:

1. [Why use an API gateway?](#heading-why-use-an-api-gateway)
    
2. [How an API gateway works](#heading-how-an-api-gateway-works)  
    – [Request validation](#heading-request-validation)  
    – [Authorisation and authentication](#heading-authorisation-and-authentication)  
    – [Rate limiting](#heading-rate-limiting)  
    – [Request routing](#heading-request-routing)  
    – [Request and response transformation](#heading-request-and-response-transformation)
    
3. [Real world example](#heading-real-world-example)
    
4. [Bringing it together](#heading-bringing-it-together)
    

## Why Use an API Gateway?

An API gateway is a fully managed service that makes it easier for developers to create, publish, maintain, monitor, and secure APIs at almost any scale.

The term “fully managed” in the context of cloud computing means that the maintenance and management responsibilities of the service are handled by the cloud provider. This means the underlying infrastructure, software updates, security, scalability, availability and disaster recovery are all managed by the cloud provider.

This abstraction mostly makes life easier for developers, as they simply need to focus on developing the service instead of worrying about managing it. This is not always the case, though, as every abstraction comes with a price.

In this case, the price of such an abstraction is a loss of flexibility. Most API gateways offered by cloud providers have a hard limit on the number of requests per second (RPS) they can handle.

There is also the higher cloud cost of using a managed service like an API gateway, which must be weighed against the higher number of developer days (number of developers \* number of days worked) needed to build an API from scratch.

To really understand the benefits of using an API Gateway, let’s have a look at the steps you need to follow to design, write, and deploy a traditional API:

### Step 1: Define Requirements and Scope

* Understand the needs of the target users or systems.
    
* Determine the data and functionality the API will expose.
    

### Step 2: Design the API

* Define the API endpoints and methods (GET, POST, PUT, DELETE).
    
* Design the request and response format (usually JSON or XML).
    
* Specify the data models and resources the API will interact with.
    
* Plan for error handling and status codes.
    

### Step 3: Develop the API

* Choose a programming language and framework.
    
* Implement the API endpoints as defined in the design phase.
    
* Integrate with databases or other services as needed.
    
* Ensure security practices are implemented, like input validation and rate limiting.
    

### Step 4: Deploy the API

* Choose a hosting solution (cloud provider, on-premises servers).
    
* Set up the deployment environment.
    
* Deploy the API to the server.
    

### Step 5: Monitor and Maintain the API

* Monitor the API for uptime, performance, and errors.
    
* Regularly update the API to fix bugs and patch security vulnerabilities
    

With an API gateway, you mainly need to focus on step 1, step 2, and parts of step 3. The other steps are mostly abstracted away and handled by the API gateway.

The main reason for using an API gateway is to simplify the process of developing and maintaining an API.

## How an API Gateway Works

An API gateway does many things at the same time.

To understand how an API gateway works, let's consider a restaurant analogy.

An API gateway is like the maître d’ (French for head waiter, more or less). The maître d' is usually found in upscale restaurants, although it is a slowly dying profession.

The maître d' serves as a liaison between the guests and the restaurant staff, and is responsible for:

1. **Greeting and Seating Guests:** The maître d' is often the first person guests encounter when they arrive at the restaurant. They warmly welcome guests, inquire about reservations, and assist in seating them at their tables, taking into account preferences and special requests.
    
2. **Reservations:** The maître d's is responsible for managing reservations and ensuring that tables are allocated efficiently. They keep track of available tables and reservation times, making adjustments as necessary to accommodate guests.
    
3. **Managing Wait Times:** During busy periods, the maître d' manages wait times for guests by providing estimated wait times and offering alternatives, such as seating at the bar or in a waiting area.
    
4. **Resolving Issues:** If any issues or concerns arise during a guest's meal, the maître d' steps in to address them promptly and ensure that the guest is satisfied.
    
5. **Handling Special Requests:** If guests have special requests or dietary restrictions, the maître d' communicates these to the kitchen and ensures that the guest's needs are met.
    

In short, the maître d’ is a person with multiple talents and responsibilities in a restaurant. From the image below, we can see how the maitre’d serves as a communicator between the customers and whatever they might need.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81489f0d-0f66-4b18-b59b-6debb17341e5_1754x1064.png align="left")

*A maître d' serves as the communicator between customers and whatever they might need.*

An API gateway works in a similar fashion. It acts as the communicator between clients and the many services they may need to access. A simplified view of this is shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c4cf127-4e90-4beb-9987-80998211e7cf_1768x916.png align="left")

*API Gateway serves as the middle-man between clients and the many services they may need to access.*

Let’s examine in more detail what an API gateway can do.

### **Request validation**

This involves checking incoming requests to confirm they meet predefined criteria before forwarding them to the backend services.

This may include checking the structure of the request, validating data types, ensuring required parameters are present, and validating the query parameters, headers, and body of the request against a schema.

By doing so, the API gateway acts as a first line of defense, preventing malformed or malicious requests from reaching backend systems.

Using our restaurant analogy, this is similar to the maître’d waiting at the entrance of the restaurant to greet guests as they arrive. But remember, this is a fancy upscale restaurant. So the maître d’ ensures guests are dressed according to the restaurant's dress code – similar to validating the incoming API request against a predefined schema.

### Authorisation and Authentication

Authentication is the process of verifying the identity of a user or service making a request, often through credentials like a username and password, tokens, or API keys.

Once authenticated, authorisation determines what resources or operations the authenticated entity has permission to access or execute.

API gateways often integrate with identity providers and support various authentication and authorisation mechanisms like [OAuth](https://oauth.net/), [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token), API keys, and so on. They ensure that only legitimate, authorised requests are allowed through to backend services.

Authentication is concerned with the “who” while authorisation is concerned with the “permissions”.

For the maître d’ waiting for guests as they arrive to the restaurant, authentication would involve the guests proving they are who they say they are, usually by showing some form of identification with a picture that can be matched to their faces.

Authorisation will involve checking that they have a reservation, that is that they have the permission to enter the restaurant and order a meal.

### Rate Limiting

Rate limiting involves controlling the number of requests a user or service can make within a specified time frame, usually defined as a limit on the number of requests per second (RPS).

Rate limiting helps to avoid overloading of backend services, ensuring they remain [available](https://lightcloud.substack.com/i/59017006/high-availability). Rate limiting is also used as part of a cost-control strategy, since you will pay for every request sent to the API gateway.

API gateways can enforce different rate limiting policies based on the user, service, or endpoint being accessed.

Drawing on our restaurant analogy, imagine our restaurant with guests inside, who have all been validated, authenticated, and authorised to enter the restaurant. But the guests are particularly hungry and thirsty and keep ordering meal after meal and drink after drink. At a certain point, this becomes unmanageable for the restaurant. The chefs and waiters are overworked and have no capacity to take on any new orders, plates and cutlery are all used up, and food in the kitchen is running out.

The maître d’ can step in and limit the number of orders customer are making. For example, by limiting the number of main courses or bottles of wine that can be ordered every hour. Rate limiting ensures that the restaurant is not overloaded with orders and is still able to serve new customers.

### Request Routing

API gateways manage the routing of incoming requests to the appropriate backend services based on various criteria like the URL path, HTTP method, headers, or query parameters. It's integral for microservice architectures where different services handle different parts of the API.

Back to our restaurant analogy, based on what the guests are there for, the maître d’ directs them to the appropriate person or place – diners to a waiter, guests who only want a drink to the bar, and those inquiring about booking events in the restaurant to the event coordinator.

### Request and Response Transformation

This involves modifying requests and responses as they pass through the API gateway.

For requests, this might mean adding, removing, or modifying headers, rewriting URLs, or even changing the request body. For responses, it might involve changing the status code, modifying headers, or transforming the body.

This capability allows the API gateway to serve as an intermediary that can transform requests and responses to meet the needs of both clients and backend services.

The backend services can also carry out this request and response transformation. The decision on which component (API gateway or a backend service) does the transformation is subjective. But an API gateway is often an ideal place to centralise such transformation with minimal effort, instead of having custom transformations in every backend service.

If a guest in a restaurant is gluten intolerant, for example, their orders have to be transformed to ensure that the their meal does not contain any gluten.

This logic of this order transformation can be handled by the maître d’ explicitly calling out which ingredients should be excluded from the dish before sending the order to the chef. This transformation can also be handled in the kitchen by the maître d’ simply telling the chef that the guest ordered a gluten-free dish and letting him modify the order accordingly.

## Real World Example

A microservice architecture is an approach to developing software that breaks down a large application into smaller, independent components called microservices. Each microservice is a self-contained unit with a specific function or responsibility within the broader application.

The figure below shows a simple microservice architecture for a basic E-commerce application.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62394846-1dc8-4f0f-a4b0-0db079c1ddcd_1794x916.png align="left")

*An API Gateway used in a microservice architecture for an e-commerce site*

* **Clients:** These are different clients that interact with the e-commerce platform. They can be a mobile app, a web browser, or any other third-party application.
    
* **API gateway:** Serves as the single entry point for all types of clients. It routes requests to the appropriate microservices based on the nature of the request (user-related, product-related, order-related).
    
* **Services:** These are examples of microservices specific to an E-commerce site. Each service handles a different aspect of the business logic like user profiles, product catalog, and order processing.
    
* **Databases:** Each microservice has its own dedicated database, ensuring data isolation and service independence.
    

In this example, the API gateway:

1. Ensures every client request is **validated**
    
2. Ensures clients are **authenticated and authorised** before they can carry out some actions like making an order or writing a review for a product
    
3. **Rate limits** requests to ensure services are not taken down by malicious actors sending a high number of requests
    
4. **Routes client requests** to the appropriate backend services based on various criteria like the URL path, HTTP method, headers, or query parameters.
    
5. Handles **request and response transformation**. For example, the response from the Product Service might be in a complex format with extensive details. The API gateway takes this response and transforms it into a format that is more suitable for the mobile app. This might involve simplifying the data, converting it into a lighter format, or extracting only the essential information needed by the mobile app.
    

## Bringing it Together

An API gateway is a fully managed service that makes it easier for developers to create, publish, maintain, monitor, and secure APIs at almost any scale. Being fully managed, it abstracts away the effort needed to manage and maintain the underlying infrastructure – this is handled by the cloud provider offering the service.

The API gateway acts as the middle-man between clients and the many services they may need to access. It handles request validation, authentication and authorisation, rate limiting, request routing, and request/response transformation.

It is especially useful in microservice architectures as the central point of entry for managing, processing, and routing incoming requests to the appropriate microservices. It plays a crucial role in simplifying the client-side interaction and provides a central interface for a group of microservices.
