---
title: Want to understand the MEAN Stack quickly? Here's documentation with useful
  diagrams.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-08T11:01:56.000Z'
originalURL: https://freecodecamp.org/news/cjn-understanding-mean-stack-through-diagrams
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-08-at-3.58.32-AM.png
tags:
- name: documentation
  slug: documentation
- name: full stack
  slug: full-stack
- name: ' Single Page Applications '
  slug: single-page-applications
- name: software architecture
  slug: software-architecture
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Clark Jason Ngo

  This article is based on my capstone for the City University of Seattle. The title
  of my research is "Software Documentation and Architectural Analysis of Full Stack
  Development". The goal of my research was to reduce the learning ...'
---

By Clark Jason Ngo

This article is based on my capstone for the [City University of Seattle](https://www.cityu.edu/). The title of my research is "Software Documentation and Architectural Analysis of Full Stack Development". The goal of my research was to reduce the learning curve in understanding open source projects and full stack development, and I choose the MEAN Stack. 

I have created the following diagrams, using [Lucidchart](https://www.lucidchart.com/), for easier comprehension. These UML diagrams were based on the 4+1 architectural view model:

* Restaurant Analogy
* Process View using Sequence Diagram
* Scenario using Sequence Diagram
* Physical View using Deployment Diagram
* Development View using Package Diagram
* Logical View using Class Diagram

The research was more focused on Deployment and Request and Response Flow.

# MEAN Stack

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/logo1.png)

The MEAN Stack is a full-stack JavaScript open-source solution. It's made up of MongoDB, Express, Angular, and Node.js. 

The idea behind it is to solve the common issues with connecting those frameworks, build a robust framework to support daily development needs, and help developers use better practices while working with popular JavaScript components.

## Back-end with Node.js

Node.js is built for handling asynchronous I/O while JavaScript has an event loop built-in for the client-side. This makes Node.js fast compared to other environments. However, the event-driven/callback approach makes Node.js difficult to learn and debug.

Node.js includes modules such as Mongoose, which is a MongoDB object modeling, and the Express web application framework. Through Node modules, abstraction can be achieved, which reduces the overall complexity of the MEAN stack.

## Back-end with Express Framework

Express is a minimalist and unopinionated application framework for Node.js. It is a layer on top of Node.js that is feature-rich for web and mobile development without hiding any Node.js functionality.

## Front-end with Angular

Angular is a web development platform built in TypeScript that provides developers with robust tools for creating the client side of web applications. 

It allows development of single-page web applications where content changes dynamically based on user behavior and preferences. It features dependency injection to ensure that whenever a component is changed, other components related to it will be changed automatically.

## Database with MongoDB

MongoDB is a NoSQL database which stores data in BJSON (Binary JavaScript Object Notation). 

MongoDB became the de facto standard database for Node.js applications to fulfill the "JavaScript everywhere" paradigm using JSON (JavaScript Object Notation) to transmit data across different tiers (front-end, back-end, and the database).

Now that we've gotten those basics out of the way, let's look at these diagrams.

## Restaurant Analogy

As I wanted to tackle the steep learning curve, I chose a restaurant analogy to let the user understand and retain the process for request and response in a full stack application.

The customer (end-user) requests their order through the waiter (controller), and the waiter hands over the request to the person at the order window (service factory). 

These three components makes up the front-end server. The service factory will be the one to communicate with the cook (controller) in the back-end. The cook will then grab the necessary ingredients (data) in the fridge (database server).

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/analogy_request.png)

The fridge will be able to provide the necessary material (data) to the cook in the back-end. The cook can now process that data and send back to the service factory of the front-end. 

The controller (waiter) will hand-over the prepared meal to the customer (user). The customer will now be able to consume the meal (data).

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/analogy_response.png)

## Process View using Sequence Diagram

Who uses it or what it shows:

* Integrators
* Performance
* Scalability

In the process view, I show the front-end server and back-end server separately at first and then connect them together with the database server. 

In the first example, an Angular application was deployed with hard-coded JSON in a `service.ts` file (located in the Service Factory).

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_frontend.png)

The Angular application can communicate with third-party APIs to obtain data and display it to the user.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_frontend_api.png)

In our back-end, the Node.js application example starts with a hard-coded JSON that can be processed and used as a response.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_backend.png)

This back-end can be connected to third-party APIs or a database server to obtain the JSON, process it, and send it back to the requester.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_backend_database.png)

With the front-end server, back-end server, and database server processes explained, I show the combination of these three servers below:

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_mean.png)

When an HTTP request is made, the front-end will be triggered and Angular will pick up the request. The request will be passed internally in Angular with Route sending a request for the view to View/Template. 

View/Template will request the Controller. The Controller will then create an HTTP request to a RESTful (Representational state transfer) endpoint to the Server Side, which is Express/Node.js. The request will then be passed internally with Express/Node.js from its Route to the Controller/Model. 

The Controller/Model will make a request through the Mongoose ODM to interact with the Database Server that has MongoDB. MongoDB will process the request and respond the callback to Express/Node.js. 

Express/Node.js sends a JSON response to the Angular Controller. The Angular Controller would then respond with a view.

## Scenario View using Sequence Diagram

Who uses it or what it shows:

* Describe interactions between objects and between processes

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/sce_book_store.png)

The scenario described above involves a user accessing a book store application. When the user enters the URL, JavaScript will be run and will hit the router of the front-end server, which is the AppRoutingModule. The AppRoutingModule will call the BooksComponent, which will load fetchBooks as its dependency injection. 

fetchBooks will then create an HTTP request to the back-end server that has a router, controller, and model to process the request and query the database server. 

The database server processes the query, and with the back-end server waiting, will grab the data and sent it back to the front-end server as a JSON response. 

The front-end will now have the data and the template view to show to the user.

## Physical View using Deployment Diagram

Who uses it and what it shows:

* System engineer
* Topology
* Communications

The deployment diagram shows 3 servers: front-end, back-end, and database. In the front-end, we require the browser as Angular applications are browser-based web applications.

The back-end server hosts our Node.js with Express on top of Node.js. In Express, we have the application and Mongoose on top of it. Express will handle the communication on both front-end and database. The database server only includes MongoDB. It uses JSON to communicate across servers.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_overview.png)

In our first build of the MEAN Stack, we’ll be deploying locally using our local machine (localhost) to deploy the front-end server, back-end server, and database server. 

We’ll be using the following default ports: Angular - port 4200, Node.js/Express – port 3000, and MongoDB – port 27017.

The diagram below shows the full stack web application in UML notation.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_local_uml.png)

Moving further to actual production, the thing to migrate to the cloud is our database. For MongoDB, I chose MongoDB Atlas as the cloud solution.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_local_cloud_uml.png)

The last step to production deployment is uploading our front-end code to Amazon S3 and uploading the back-end in an EC2 instance with AWS. They would all communicate to each other with HTTP / HTTPS endpoints.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_cloud_uml.png)

Here's another diagram to show our production deployment without using UML notation.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_cloud.png)

## Development View using Package Diagram

Who uses it and what it shows:

* Programmers
* Software Management

The package view of the Angular application shows that every Angular Component is imported in the AppModule. AppModule and AppRoutingModule are dependent on BooksComponent. The BooksComponent is dependent on BookDetailComponentDialog and ApiService.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/dev_angular.png)

The package view of the Node.js application shows that all CRUD operations (controllers) such as fetch all books, fetch a book, update a book, and delete a book are imported by the app. Also, all the CRUD operations logic resides in the model book.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/dev_nodejs.png)

## Logical View using Class Diagram

Who uses it and what it shows:

* End-user
* Functionality

The book store application only showcased a single class called Book. The class members are: title, isbn, author, picture and price. The methods are: addBook, fetchBooks, fetchBook, updateBook, and deleteBook.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/log_book.png)

The model Book’s structure in JSON format.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/log_book_json.png)

**Here are some videos for the diagrams:**

%[https://youtu.be/hPNziXpjf7E?list=PLK4sJSsw4V-fxsMJEC8YV7cPDlYxp7Ib2]

**Documentation available on my GitHub:**

%[https://github.com/clarkngo/cityu_capstone]

Find me on [LinkedIn](https://www.linkedin.com/in/clarkngo/). =)

