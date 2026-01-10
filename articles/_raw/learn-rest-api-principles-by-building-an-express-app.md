---
title: Learn REST API Principles by Building an Express App
subtitle: ''
author: Ikegah Oliver
co_authors: []
series: null
date: '2025-04-21T15:20:53.838Z'
originalURL: https://freecodecamp.org/news/learn-rest-api-principles-by-building-an-express-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745003938509/442fd99e-d098-4a5a-98d7-94c4af9a5d55.png
tags:
- name: REST API
  slug: rest-api
- name: Express
  slug: express
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: Web development revolves around communication – communication between browsers
  and servers, as well as frontend applications and backends. At the centre of this
  is the API. And the REST architecture has become a popular way to design APIs that
  are cl...
---

Web development revolves around communication – communication between browsers and servers, as well as frontend applications and backends. At the centre of this is the API. And the REST architecture has become a popular way to design APIs that are clean, consistent, and easy to use in web development.

REST works so well because it speaks the web’s native language. It uses familiar HTTP methods like `GET`, `POST`, `PUT`, and `DELETE`, treats data as resources, and follows clear conventions. All this makes it easy to understand, quick to implement, and widely supported, which is why most modern web APIs follow REST principles.

In this article, I will explore REST concepts and core principles while we build a simple Express application step by step. You will learn:

* What is REST architecture, and what are its advantages in web development?
    
* The core REST principles (statelessness, resources, HTTP methods, and so on)
    
* How to implement these principles in a real Express.js app
    
* Best practices for designing clean and consistent APIs
    

### Here’s what we will cover:

* [What is REST](#heading-what-is-rest)
    
* [Why use REST?](#heading-why-use-rest)
    
* [Core Principles of REST Architecture](#heading-core-principles-of-rest-architecture)
    
* [Build a Simple Express App](#heading-build-a-simple-express-app)
    
    * [What is Express?](#heading-what-is-express)
        
    * [Set Up the Express App](#heading-set-up-the-express-app)
        
    * [Build RESTful Resources](#heading-build-restful-resources)
        
    * [Middlewares](#heading-middlewares)
        
    * [Test your Express App](#heading-test-your-express-app)
        
* [Bad REST Practices to Avoid](#heading-bad-rest-practices-to-avoid)
    
* [Conclusion](#heading-conclusion)
    

## What is REST?

Representational State Transfer (REST) is a style of designing networked applications that emphasises a stateless client-server communication model centred around resources. Think of it like ordering at a restaurant: each time you ask for something, you have to tell the waiter exactly what you want, and they don't remember your previous orders.

RESTful APIs treat data as resources, each accessible through a unique web address (URI). Then, it leverages the standard actions defined by HTTP methods – POST to create new resources, GET to retrieve them, PUT to modify existing ones, and DELETE to remove them – providing a consistent and well-understood way to interact with data over the internet.

## Why Use REST?

REST architectural principles offer a compelling set of advantages that contribute to building robust, scalable, and maintainable web services. Below are some of the key benefits that make REST a preferred choice for modern web development:

* **Simplicity and familiarity:** REST leverages standard HTTP, which is already well-understood by developers and infrastructure.
    
* **Scalability:** The stateless nature of REST allows for easy scaling of both client and server components independently.
    
* **Flexibility and interoperability:** RESTful APIs can be consumed by a wide variety of clients, regardless of the technology stack.
    
* **Cacheability:** REST's design supports caching mechanisms, leading to improved performance and reduced server load.
    
* **Loose coupling:** The client and server are independent, allowing for changes on either side without necessarily affecting the other.
    
* **Visibility and monitoring:** The straightforward nature of HTTP requests and responses makes it easier to monitor and debug interactions.
    

## Core Principles of REST Architecture

REST (Representational State Transfer) is built on a few simple principles that make APIs easy to understand and use. Here’s a quick breakdown of the key ones:

### Statelesness

Every request from the client to the server must contain all the information needed to process it. The server doesn’t store anything about the client between requests – no session, no memory of previous actions.

**Example:** If a user sends `GET /movies/1`, the server returns the movie data without needing to know whether the user is logged in or what they requested before.

This makes APIs easier to scale, since each request can be handled independently.

### Resource and URIs

In REST, everything you work with is considered a resource – users, products, and so on. Each resource should be accessible via a unique, meaningful URL.

**Example:**

* `/movies` – a collection of movie resources
    
* `/movies/42` – a specific movie with ID 42
    

Resources are treated like nouns. Actions are determined by the HTTP method used.

### Standard HTTP Methods

REST takes full advantage of HTTP methods to describe what action you’re taking on a resource:

* `GET` – retrieve data
    
* `POST` – create a new resource
    
* `PUT` – update or replace a resource
    
* `PATCH` – partially update a resource
    
* `DELETE` – remove a resource
    

**Example:** To delete a movie, you’d send a `DELETE` request to `/movies/42`. That’s clear, consistent, and intuitive.

### Uniform Interface

REST enforces a consistent structure for communication between client and server. This means all REST APIs should behave similarly, no matter who built them. It includes:

* Using URIs to identify resources
    
* Using standard HTTP methods
    
* Representing data in formats like JSON or XML
    
* Self-descriptive messages (for example, proper status codes and headers)
    

This consistency makes it easier for developers to understand and integrate with RESTful APIs.

### Cacheability

Servers should label responses as cacheable (stored to be retrieved later) or not, so clients can reuse responses when appropriate. This reduces unnecessary server load and improves performance.

**Example:** A `GET /movies` response can be cached for 5 minutes if the data doesn’t change frequently. That means fewer repeated calls for the same info.

### Client-Server Separation

The client (frontend) and server (backend) operate independently. The client just needs to know how to communicate with the API – it doesn’t care how the server handles data, and vice versa.

This separation allows teams to develop and scale frontend and backend systems separately.

The principles above help create APIs that are scalable, predictable, and easy to work with.

## How to Build a Simple Express App

### What is Express?

Express.js is a lightweight and flexible Node.js web application framework. Built on top of Node.js, it provides a robust set of features for building single-page, multi-page, and hybrid web applications and APIs. Think of it as a helpful toolkit that streamlines the process of setting up and managing web servers and routing requests.

In this exercise, you will be building an Express app that will:

1. Handle a simple in-memory collection of movies as a RESTful resource
    
2. Support basic CRUD operations using the appropriate HTTP methods (GET, POST, PUT, DELETE)
    
3. Parse incoming JSON requests using built-in middleware
    
4. Use a custom middleware function to validate movie input before creating or updating entries
    
5. Send clear and meaningful responses based on the outcome of each request
    

By the end, you’ll have a working API that follows REST principles and can be tested using a tool like Thunder Client or Postman.

### Set Up the Express App

To get the most out of this exercise, there are a few tools and concepts you should already be familiar with. Since we’re focusing on REST principles and how to apply them using Express, we won’t dive deep into the basics of these prerequisites. Make sure you’re comfortable with the following:

* Node.js
    
* Npm
    
* Thunderclient extension
    
* Basic JavaScript
    

With that, let’s get started.

Open your command prompt and create a new directory (folder):

```bash
mkdir express-app
```

Navigate into your new directory:

```bash
cd express-app
```

Initialize an npm project:

```bash
npm init -y
```

Install the Express package in your project:

```bash
npm install express
```

Now, open your directory in your code editor with the following command:

```bash
code .
```

Create a new file, server.js, and set up your Express app in that file:

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.listen(8000, () => console.log('Server running on port 8000'));
```

This snippet above sets up a basic Express server. It starts by importing the Express library you installed, enables JSON parsing for incoming requests (so we can work with request bodies), and listens on port 3000. It’s ready to handle RESTful routes like `GET`, `POST`, `PUT`, and `DELETE` as we build out our API.

To start your server, go back to your command prompt and type in this command:

```bash
node server.js
```

You should see this logged in your command prompt:

![A screenshot of a command prompt or terminal window. The prompt shows the current directory as "C:sersSEResktopest-tutorial>". The command "node server.js" has been executed, and the output below it reads "Server is running on port 8000".](https://cdn.hashnode.com/res/hashnode/image/upload/v1744840192457/818bc1a4-3e96-4494-9895-d02cf816e3f3.png align="left")

### Build RESTful Resources

With our Express app set up, let’s build out the `/movies` resource using RESTful routes. We'll treat each movie as a resource and use HTTP methods to define what we want to do – retrieve, add, update, or delete movies. For simplicity, we'll store the movies in an in-memory array.

Here is the full set of routes. Add it in your server.js file just under your `app.use(express.json());` line:

```javascript
// In-memory database (for demonstration purposes)
// In a real application, you would use a database like MongoDB or PostgreSQL
const movies = [];

// Get all movies
app.get('/movies', (req, res) => {
  res.json(movies);
  console.log(movies);
});

// Get a particular movie by ID
app.get('/movies/:id', (req, res) => {
  const movie = movies.find(m => m.id === parseInt(req.params.id));
  if (!movie) return res.status(404).send('Movie not found');
  res.json(movie);
});

// Add a new movie
app.post('/movies', (req, res) => {
  const movie = {
    id: movies.length + 1,
    title: req.body.title,
    genre: req.body.genre,
    year: req.body.year
  };
  movies.push(movie);
  res.status(201).json(movie);
});

// Update a movie
app.put('/movies/:id', (req, res) => {
  const movie = movies.find(m => m.id === parseInt(req.params.id));
  if (!movie) return res.status(404).send('Movie not found');

  movie.title = req.body.title;
  movie.genre = req.body.genre;
  movie.year = req.body.year;

  res.json(movie);
});

// Delete a movie
app.delete('/movies/:id', (req, res) => {
  const movieIndex = movies.findIndex(m => m.id === parseInt(req.params.id));
  if (movieIndex === -1) return res.status(404).send('Movie not found');

  const deletedMovie = movies.splice(movieIndex, 1);
  res.json(deletedMovie);
});
```

The code above defines a complete set of RESTful routes for managing a movies resource using Express.

It begins with an in-memory array, `movies`, which acts as our temporary data store. The `GET /movies` route returns all books, while `GET /movies/:id` looks up a book by its ID using `Array.find()`, returning a 404 status if it's not found. The `POST /movies` route accepts JSON input, creates a new book with an auto-incremented ID, and adds it to the array, returning the new resource with a `201 Created` status.

The `PUT /movies/:id` route handles full updates. It first finds the book, and if found, updates its `title` , `genre`, and `year` with the new values from the request body. The `DELETE /movies/:id` route removes a movie by finding its index in the array and using `splice()`. If the movie doesn't exist, both PUT and DELETE return a 404 error.

These routes demonstrate idempotency – that is, sending the same PUT or DELETE request multiple times will have the same effect as sending it once, a key REST principle. Each route also returns appropriate HTTP status codes and JSON responses, following REST conventions closely.

Each route follows a REST principle:

* Uses nouns for endpoints (`/movies`)
    
* Uses standard HTTP methods to express actions
    
* Ensure idempotency where appropriate (PUT, DELETE)
    
* Return appropriate status codes and messages
    

This structure keeps your API predictable and easy to use – exactly what REST is all about.

### Middlewares

In RESTful APIs built with frameworks like Express, middleware plays a key role in maintaining clean, modular, and consistent request handling.

Middlewares are functions that sit in the middle of the request-response cycle in an Express app. When a client sends a request, middleware functions have access to the `req` (request), `res` (response), and `next` objects. They can inspect, modify, or act on the request before it reaches the route handler or even terminate the response early.

You have already seen a middleware here: `app.use(express.json());`. This is a global middleware that is used for parsing JSON. We will be creating a custom middleware for validating input for our POST and PUT requests.

Add the following code in your server.js file just before your routes:

```javascript
// Middleware for simple validation
const validateMovie = (req, res, next) => {
  if (!req.body.title || !req.body.genre || !req.body.year) {
      return res.status(400).send('Title, genre, and year are required');
  }
  next();
};
```

This middleware function, `validateMovie`, performs basic validation on incoming requests before they reach the route handler. It checks if the `title`, `genre`, and `year` fields are present in the request body. If any of these fields are missing, it immediately responds with a `400 Bad Request` status and an error message. If all required fields are provided, it calls `next()` to pass control to the next middleware or route. This keeps validation logic separate and reusable, helping maintain clean and RESTful route handlers.

To use this middleware, pass it as an argument in your POST and PUT routes, for example example:

```javascript
app.post('/movies', validateMovie, (req, res) => {
  const movie = {
    id: movies.length + 1,
    title: req.body.title,
    genre: req.body.genre,
    year: req.body.year
  };
  movies.push(movie);
  res.status(201).json(movie);
});
```

### Test Your Express App

To test the changes you have made, you need to restart your server. Go to your command prompt and press CTRL + C (for Windows) or Command + . (for MacOS). Input the start command like before to start the server again.

For this exercise, you will be testing the endpoints with the Thunder Client extension on VSCode. Thunder Client is a lightweight REST API extension for VSCode. With Thunder Client, you can your REST API routes and endpoints directly in VSCode.

To download Thunder Client, click on the Extension icon on the taskbar on your left and search “Thunder Client”. Then click Install:

![A screenshot of the Extensions Marketplace in Visual Studio Code (VS Code). The search bar at the top contains the text "Thunder". Below the search bar, a list of extensions related to "Thunder" is displayed. The first result, "Thunder Client," shows an install button. A red arrow points to the Extensions icon in the VS Code activity bar on the left, which is highlighted to indicate that this is the icon to click.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744234771851/a5d7a3e4-384b-47e9-8b2d-47bc45a2007d.png align="left")

After installation, you'll see the Thunder Client icon appear in your sidebar below the Extensions icon. Click it, then hit New Request to open a new tab. The request tab will open with a clean layout, ready for you to send and test API calls:

![A screenshot of the Thunder Client interface within Visual Studio Code. A new request tab is open, displaying a GET request configured to the URL "https://www.thunderclient.com/welcome". The HTTP method is set to "GET" in a dropdown menu. Below the URL bar, tabs for "Query," "Headers," "Auth," "Body," "Tests," and "Pre Run" are visible, with "Query" currently selected, showing a section for "Query Parameters" with fields for "parameter" and "value". At the bottom, a message indicates "Non-Commercial Use" with a link to view terms. The left sidebar shows "THUNDER CLIENT" with options like "New Request," "Activity," and "Collections.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744282644259/dfe4b735-c465-4993-bc46-cce28966deb3.png align="center")

To start testing your API, set the request method (GET, POST, PUT, or DELETE) from the dropdown and enter the appropriate route, like `http://localhost:3000/movies`. For GET requests, just hit Send and you should see a response, in this case, an empty array `[]`. To get a specific movie, you include an ID (for example, `/movies/1`).

For `POST`, `PUT`, and `DELETE` requests, switch to the Body tab and select the JSON format. Then provide the data you want to send:

* **POST** `/movies`: Add a new movie with `{"title": "Movie Title", "genre": "Genre Name", "year": 0000}`.
    
* **PUT** `/movies/1`: Update an existing movie with the same JSON structure.
    
* **DELETE** `/movies/1`: Remove a movie by its ID — no body is needed.
    

After sending each request, Thunder Client will display the response body, headers, and status code. Example:

![A screenshot of the Thunder Client interface in Visual Studio Code, showing a successful POST request. On the left, the request details are visible: the HTTP method is set to "POST" with the URL "http://localhost:8000/movies". The "Body" tab is selected, displaying JSON content: {"title": "Home Alone", "genre": "Comedy", "year": 1999}. On the right, the response details indicate a "Status: 201 Created", "Size: 58 Bytes", and "Time: 5 ms". The "Response" tab is selected, showing the JSON response: {"id": 1, "title": "Home Alone", "genre": "Comedy", "year": 1999}.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744840699502/4ea83fbc-7b47-4aea-b8ff-a6e351bf54be.png align="left")

## Bad REST Practices to Avoid

When building REST APIs, aside from using the right HTTP methods, you also have to consider avoiding practices that break the core principles of REST. These bad practices can make your API harder to use, less predictable, or even misleading.

Here are some common REST bad practices and how to avoid them:

### **Using verbs in endpoints**

Avoid routes like `/getMovies` or `/createMovie`. RESTful APIs rely on HTTP methods to express actions, so use nouns for endpoints and let methods do the talking — for example, use `GET /movies` to retrieve movies and `POST /movie` to create one.

### **Ignoring HTTP status codes**

Returning `200 OK` for every response, even errors, breaks REST conventions. Use the appropriate status codes: `201 Created` for successful POSTs, `404 Not Found` when a resource doesn’t exist, and `400 Bad Request` for validation issues. This helps clients interpret responses correctly.

### **Overloading a single endpoint**

Avoid writing one endpoint that changes behaviour based on the request body or headers. Each route should clearly map to a resource and method, like `GET /movies/1` to fetch, and `DELETE /movies/1` to remove, making the API predictable and easy to follow.

### **Not being idempotent where expected**

`PUT` and `DELETE` should be idempotent, meaning repeated requests should have the same effect. If calling `DELETE /movies/1` twice causes an error or unexpected behaviour, that’s a red flag. Design your handlers to handle these cases gracefully.

### **Exposing internal logic or database structure**

Don’t leak internal details like database table names or query logic in your route naming (`/api/movie_table_data`). Keep your URIs clean, abstracted, and centred around the actual resource, like `/movies`.

Avoiding these practices not only keeps your API RESTful but also improves developer experience, consistency, and long-term maintainability.

## Conclusion

You have explored the core ideas behind REST and put them into practice by building and testing a real Express API. This hands-on approach should help bridge the gap between theory and real-world application.

Along the way, you learned how REST treats resources, how to write clean and predictable routes, and why these principles matter when designing APIs that are easy to use and maintain.

Here’s a quick recap of what you’ve built and learned:

* Defined what REST is and why it’s widely used in web development
    
* Explored core REST principles like statelessness, resource-based routing, HTTP methods, status codes, and idempotency
    
* Set up a simple Express server to serve as the base for a RESTful API
    
* Built a complete set of routes (GET, POST, PUT, DELETE) for managing a `movies` resource
    
* Used middleware for tasks like JSON parsing and input validation
    
* Tested routes using Thunder Client and learned how to interact with each HTTP method
    
* Identified common REST anti-patterns and how to avoid them for cleaner design
    

To take your API further and follow more advanced RESTful practices, consider:

* Organising routes with Express Router to keep your code modular
    
* Adding robust error handling to return consistent and informative responses
    
* Using logging tools like `morgan` to monitor requests and debug more easily
    
* Securing endpoints with authentication methods like JWT or API keys
    
* Structuring responses consistently, possibly with pagination and filtering for larger datasets
    
* Validating user input thoroughly with libraries like `Joi` or `express-validator`
    

Explore the full project on [GitHub](https://github.com/oliverTwist2/rest-tutorial), review the code, and try extending it with your features. Happy coding!
