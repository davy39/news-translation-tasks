---
title: Learn Node.js and Express in Spanish – Course for Beginners
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2022-08-08T04:35:40.000Z'
originalURL: https://freecodecamp.org/news/learn-node-js-and-express-in-spanish-course-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/thumbnail.png
tags:
- name: Express
  slug: express
- name: node
  slug: node
seo_title: null
seo_desc: "Hi! If you speak Spanish and you want to learn Node.js, and Express, you\
  \ are in the right place. \nIn this article, you will find a brief introduction\
  \ to back-end web development, Node.js, and Express. You will learn why they are\
  \ very powerful tools f..."
---

Hi! If you speak Spanish and you want to learn Node.js, and Express, you are in the right place. 

In this article, you will find a brief introduction to back-end web development, Node.js, and Express. You will learn why they are very powerful tools for developing web servers and why you should learn them if your goal is to be a back-end web developer. 

Then, you will find [an **8.5 hour** Node.js and Express course](https://www.youtube.com/watch?v=1hpc70_OoAg) on freeCodeCamp's Spanish YouTube channel where you can learn the fundamentals in Spanish and build a project step by step.

If you have Spanish-speaking friends, you are welcome to share the **[Spanish version of this article](https://www.freecodecamp.org/espanol/news/aprende-node-js-y-express-curso-desde-cero/)** with them.

Let's begin! ✨

## **🔸 What is Back-End Web Development?**

Web development has transformed our modern world. Every day we access the internet to find information, learn, buy products, share our thoughts, and connect with family and friends. 

Basically, our lives would never be the same without websites and web applications. Do you agree? 🙂 

If you do, then learning web development can lead you down a very rewarding career path because you can have a tremendous impact in the lives of thousands or even millions of users. 

Let's talk a little bit about the different areas of web development. 

### ◼️ Front-End vs. Back-End Web Development

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-174.png)

The developers who create amazing web applications are called **web developers**. They can specialize to develop different parts of a web application:

* **Font-End Web Developers** implement the part of the web application that users interact with directly. They develop the visible part of the amazing platforms we use and love every day. In the store analogy that you can see above, the front-end would be represented by the part of the store that clients can see. 
* **Back-End Web Developers** implement all the functionality that users don't see, such as servers, databases, and their interactions with the font-end part of the applications. In our store analogy, the back-end would be represented by the warehouse, the part of the store that supports everything that clients do see. 
* **Full-stack Web Developers** are in charge of both areas. They have thorough knowledge of front-end and back-end web development. 

Interesting, right? ✨

Now let's dive deeper into back-end web development because that is one of the main applications of Node.js and Express.  

### The Client-Server Model

The internet is based on the **client-server model**, in which two devices (the client and the server) communicate with each other. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-173.png)
_Illustration of the client-server model._

### What is a Client?

When you try to access a website in your browser, the browser (**client**) sends an HTTP request for that website to the server. 

### What is a Server?

The **server** is a program that listens for requests and generates appropriate responses. These responses often include:

* Sending data to the client.
* Running some task.
* Working with or updating a database. 

For example, we may send a request to the server to add a new user to the database of a web application. The server should make the necessary updates in the database and notify the client that this change was successful. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-175.png)
_Client (left) - Server (center) - Database (right)_

Developing and maintaining servers is one of the main tasks of back-end web developers, and that is precisely what **Node.js and Express** are used for. 

## 🔹 What is Node.js? 

**Node.js** is an asynchronous event-driven JavaScript runtime built on Chrome's V8 JavaScript engine. It gives us all the tools we need to run JavaScript in the terminal without a web browser. 

💡 **Tip:** Before Node.js, we could not run JavaScript programs without a browser. Only browsers were designed for this task since JavaScript is one of the main programming languages of the web. 

The awesome thing about Node.js is that it lets us build scalable network applications with high performance. 

According to its [official documentation](https://nodejs.org/en/about/):

> Users of Node.js are free from worries of dead-locking the process, since there are no locks. Almost no function in Node.js directly performs I/O, so the process never blocks except when the I/O is performed using synchronous methods of Node.js standard library. **Because nothing blocks, scalable systems are very reasonable to develop in Node.js.**

🚩 It is important to note that **Node.js is not** a:

* Programming language.
* Framework.
* Library.

It is a **JavaScript runtime** developed to run JavaScript code. 

### **Why should you learn Node.js?**

Now that you know what Node.js is, let's see **why** you should learn it. 

**Node.js** is one of the most popular web technologies among developers, including beginners who are learning how to code, as well as professionals.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/node-logo.png)
_Node.js Logo_

**Node.js** is extremely popular. According to the [2022 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe), it is one of the most popular web technologies used by professional developers and by those who are learning to code. 

Node.js got **47.12%** of the votes when respondents were asked which web frameworks and web technologies they had done extensive development work in over the past year, and which they wanted to work in over the next year. 

**💡 Tip:** that is almost half of the 58,743 responses!

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-171.png)
_The results of the Web Frameworks and technologies category in the [2022 Stack Overflow Developer](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe) Survey. **Node**.js leads with 4**7.12**%********of the responses.****_

That percentage was even higher among respondents who were learning how to code: **52.86%**. Awesome, right? 😁

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-172.png)
_The results of the Web Frameworks and technologies category in the [2022 Stack Overflow Developer](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe) Survey when Learning to Code was selected. **Node**.js leads with** 52.86**%of the responses.****_

This is clear evidence of the impact that Node.js is having in web development. By learning Node.js, you will be investing your time and resources wisely. You will acquire valuable skills that are highly demanded in this field. 

## 🔸 What is Express? 

If your goal is to develop a server with Node.js, the process can be much easier if you use **Express**. It's a web application framework specifically developed for Node.js. 

According to the [official documentation](https://expressjs.com/) of Express:

> Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.

**💡 Tip:** Express includes many tools that you can use to write more concise, readable, and maintainable code. Trust me. Once you start working with Express, you will never want to stop.

Express has many HTTP utility methods and middleware that you can use to create robust APIs (Application Programming Interfaces), which are fundamental for back-end and full-stack web development.

In the [2022 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe), **Express** was the fourth most used web technology or framework with **22.99%** of all votes:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-177.png)
_The results of the Web Frameworks and technologies category in the [2022 Stack Overflow Developer](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe) Survey. **Express** was fourth with **22.99**%of the responses.****_

Express also got **25.72%** of the votes of the respondents who are learning how to code:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-176.png)
_**Express** had **25.72%** of the votes of the respondents who are learning how to code. It was third in the results of the Web Frameworks and technologies category._

**Awesome!** Now you know why you should learn Node.js and Express. I promise you that it will be totally worth it. ✨

## 🔹 **Node.js and Express Course Content**

Now let's review what you will learn during the course. 

**💡 Tip:** to take the course, you should have previous knowledge of **JavaScript**. If you need to review these topics in Spanish, I recommend watching this [JavaScript course](https://www.youtube.com/watch?v=ivdTnPl1ND0&t=3s) on the freeCodeCamp Spanish YouTube channel.

### Introduction to Node.js and Basic Concepts

* Introduction to Node.js.
* Basic concepts of Back-End Web Development.
* Applications of Node.js.
* APIs and what they are used for.
* Advantages of Node.js.
* How to download and install Node.js.
* How to confirm that Node.js was installed successfully.
* How to check your current version of Node.js.
* The Node.js REPL.

### Your First Node.js Project and Node Modules

* What is a module? Concept and advantages.
* How to export and import modules.
* How to export multiple elements from a JavaScript module. 
* How to run a JavaScript file with the `node` command. 
* Node.js core modules.
* The `console` module.
* The `process` module.
* The `os` module.
* The `fs` module.
* The `timers` module.

### Introduction to npm and JSON

* What is npm? 
* Basic npm concepts.
* How to initialize a package with `npm init`.
* The `package.json` file.
* Introduction to JSON.
* How to install and uninstall packages with npm. 
* The `package-lock.json` file.

### Events and Asynchronous Operations

* What is an event?
* Events in Node.js.
* Asynchronous vs. synchronous events.
* Promises and callback functions in JavaScript.
* Promises, `.then()`, and `.catch()`.
* Asynchronous functions with `async` and `await`.

### Node.js Servers and the HTTP Protocol

* The client-server model.
* The format of HTTP requests and responses. 
* HTTP verbs: GET, POST, PUT, DELETE.
* HTTP state codes. 
* The `http` module in Node.js
* How to create a server in Node.js.
* The `req` and `res` objects. 
* Structure of a URL.
* Routing in Node.js.

### Nodemon

* What is Nodemon?
* How to install Nodemon globally.
* How to use Nodemon to update Node.js applications automatically. 
* Concepts: CRUD, REST, API.

### Express

* How to install Express and how to start a project. 
* Routing in Express.
* Express and Nodemon. 
* How to match multiple routes. 
* Route parameters and dynamic routes. 
* Middleware in Express.
* Handling GET, POST, PUT, PATCH, and DELETE requests. 
* Query parameters. 
* Routers in Express.

💡 **Tip:** We will work with Visual Studio Code during the course and we will install an extension to simulate POST, PUT, and DELETE requests. 

## 🔸 **Node.js and Express Project**

During the course, you will learn through practical examples and you will apply everything you learn step by step.

![Image](https://www.freecodecamp.org/espanol/news/content/images/2022/08/image-3.png)
_Proyect that we will build with Node.js and Express_

You will learn how to work with Promises with a pizza example 🍕, how to work with asynchronous JavaScript, and you will develop a simple server and API with Node.js to send information about programming and mathematics courses to the browser.

Then, we will adapt this simple server to work with Express. You will apply previous and new concepts step by step to create a server that will handle multiple routes, parameters, and different types of HTTP requests. 

## **📌** Node.js and Express **Course** on YouTube

Awesome. Now that you know more about Node.js and Express and what you will learn during the course, you are welcome to start taking the course in **Spanish**:

%[https://www.youtube.com/watch?v=1hpc70_OoAg]

✍️ Course created by **Estefania Cassingena Navone** (Twitter: [@EstefaniaCassN](https://twitter.com/EstefaniaCassN), YouTube: [Coding with Estefania](https://youtube.com/codingwithestefania)).

I really hope you like the course and find it helpful to take your first steps into the world of back-end web development.

You are also welcome to continue learning with our **Spanish** courses:

%[https://www.youtube.com/watch?v=XqFR2lqBYPs]

%[https://www.youtube.com/watch?v=ivdTnPl1ND0]

%[https://www.youtube.com/watch?v=DLikpfc64cA]

%[https://www.youtube.com/watch?v=6Jfk8ic3KVk]


