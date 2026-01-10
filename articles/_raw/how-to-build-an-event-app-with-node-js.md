---
title: How to Build an Application With Node.js
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2024-08-05T17:56:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-event-app-with-node-js
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741114813767/a2786471-5a6a-4450-bdb1-f7d1162c2a90.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'Node.js it’s a runtime environment that allows you to run JavaScript code
  on the server side for building server-side applications. It works well for creating
  fast and scalable applications.

  In this article, I will use a simple event management app a...'
---

Node.js it’s a runtime environment that allows you to run JavaScript code on the server side for building server-side applications. It works well for creating fast and scalable applications.

In this article, I will use a simple event management app as an example to show you how to build an application using Node.js, Express.js, and MongoDB.

By the end, you’ll know how to set up a Node.js project, create a server with Express.js, show dynamic pages with embedded JavaScript, and connect to a MongoDB database to handle your data.

### What You'll Learn

* Setting up a Node.js project
    
* Creating a server with Express.js
    
* Rendering dynamic pages with ejs
    
* Connecting to a MongoDB database
    
* Creating models and schemas for your data
    
* Handling HTTP requests and responses
    

## Table of Contents

* [Set Up Your Development Environment](#step-1-set-up-your-development-environment%22)
    
* [Set Up the Server](#heading-step-2-set-up-the-server)
    
* [Install and Set Up Express.js](#heading-step-3-install-and-set-up-expressjs)
    
* [Create a Dynamic Template](#heading-step-4-create-a-dynamic-template)
    
* [Save Your Data to MongoDB](#heading-step-5-save-your-data-to-mongodb)
    
* [Connect to the Database](#heading-step-6-connect-to-the-database)
    
* [Create the Model for the Document Structure](#heading-step-7-create-the-model-for-the-document-structure)
    
* [Create HTML Pages](#heading-step-8-create-html-pages)
    
* [Create Partials](#heading-step-9-create-partials)
    
* [Create an Environment Variable File](#heading-step-10-create-an-environment-variable-file-env)
    
* [Further Steps](#heading-further-steps)
    
* [Conclusion](#heading-conclusion)
    

![Let's get started 🚀](https://www.freecodecamp.org/news/content/images/2024/07/image-56.png align="left")

*Let's get started 🚀*

## Prerequisites

* [Node.js](https://nodejs.org/en) installed on your system.
    
* A good understanding of [MongoDB](https://www.mongodb.com/).
    
* A code editor that you prefer, such as [Visual Studio Code](https://code.visualstudio.com/) or [Sublime Text](https://www.sublimetext.com/download).
    

## Step 1: Set Up Your Development Environment

### Install Node.js and npm

First, you'll need to download and install Node.js from [nodejs.org](https://nodejs.org/). Then you can verify the installation by running: `node -v` and `npm -v`.

### Initialize a New Project

Create a new directory for your project. Then initialize the project with npm: `npm init -y` in your terminal.

```js
mkdir event-app
cd event-app
npm init -y
```

![Initializing the project](https://www.freecodecamp.org/news/content/images/2024/07/ShareX_OnHiLv8GvS-1.gif align="left")

*Initializing the project*

Running `npm init -y` creates the `package.json` file, as shown above. This file is crucial. It stores and tracks all third-party libraries (dependencies) needed for your application.

## Step 2: Set Up the Server

To set up your server, create a file called `server.js` or `app.js`. These are common names. They are used for their descriptive nature. But, you can name the file whatever you prefer.

The `server.js` file will be used to create a server which will be used to manage, control, and route to the necessary page in our application.

## Step 3: Install and Set Up Express.js

Express.js is a popular web application framework for Node.js and a third-party library that we use in our application.

Express simplifies the handling and definition of various routes for HTTP requests. It enables you to manage the application's routing and connect it to the server.

### To use Express:

Install Express.js by running the following command in your terminal:

```javascript
npm install express
```

Require Express in your `server.js` file.

```js
const express = require('express')
```

Initialize Express so you can use it in your application.

```js
const app = express()
```

Create a routing path to get the HTTP request.

```javascript
//routing path
app.get('/', (req, res) => {
  res.send('Hello World!');
});
```

Lastly, we need to ensure that the connection to the server is set up correctly. When we start the server in the terminal, it will open in the browser.

To do this, use the `listen()` method.

```javascript
// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

This method will `listen()` to requests from the server.

**Here's the complete code process:**

```javascript
const express = require('express');


// Next initialize the application
const app = express();

// routing path
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

**Note:** The routing path above was only for testing purposes to confirm that the server is working and connected. We will provide a different file for the event app we are creating.

With Express.js installed in your application, you can now create a server that will handle all your routing and connections.

To start the server, go to your terminal.

Use the keyword `node`, then type `--watch`, a flag to start and automatically restart the server whenever you make changes:

```javascript
node --watch server.js
```

Or you can install `[nodemon](https://www.npmjs.com/package/nodemon)` for the same purpose. `Nodemon` detects changes in the directory and restarts your application.

```javascript
npm install -g nodemon
```

Then run your server with:

```javascript
nodemon server.js
```

## Step 4: Create a Dynamic Template

We need a templating engine to render `HTML` code in the browser using Node.js. We'll use ejs **(Embedded JavaScript)** for this tutorial but there are others such as [Pug (formerly known as Jade)](https://pugjs.org/api/getting-started.html) and [Express Handlebar](https://www.npmjs.com/package/express-handlebars), which also render HTML on the server.

`ejs` allows you to embed JavaScript in HTML to create dynamic web pages.

To install `ejs`, run:

```bash
npm install ejs
```

To set up `ejs` in `server.js`, require and set `ejs` as the templating engine:

![requiring ejs template in our application](https://www.freecodecamp.org/news/content/images/2024/07/image-51.png align="left")

*Requiring* `ejs` template in your application

```javascript
const express = require('express');
const app = express();

app.set('view engine', 'ejs');
```

With this setup, you can now enable dynamic rendering of `HTML` code in your Node.js application.

## Step 5: Save Your Data to MongoDB

To save the data you create for your application, you will use MongoDB.

MongoDB is a "Not Only SQL" (NoSQL) database that's designed for storing document collections. Traditional SQL databases organize data into tables, but MongoDB is optimised for handling large volumes of data.

To read more about this, [check out this article](https://www.mongodb.com/resources/basics/databases/nosql-explained).

## Step 6: Connect to the Database

Now we need to connect to the database which will be MongoDB for this tutorial.

Using MongoDB provides you with a Uniform Resource Locator (URL) to connect to your application. This URL connect you and acts as a communicator between the database and your application.

### How to get the URL

To get the URL, follow these simple steps:

1. **Sign Up/Log In**: Go to the [MongoDB website](https://www.mongodb.com/) and sign up for an account or log in if you already have one.
    
2. **Create a Cluster**: Once logged in, create a new cluster. This will set up your database.
    
3. **Connect to Your Cluster**: After your cluster is created, click the "Connect" button.
    
4. **Choose a Connection Method**: Select "Connect your application".
    
5. **Copy the Connection String**: MongoDB will provide a connection string (URL) like this:
    

```js
mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
```

6. **Replace the Placeholders**: Replace `<username>`, `<password>`, and `<dbname>` with your actual username, password, and database name.
    

Now that you have the URL, you can easily connect to your database.

To make this connection easier, we will use a tool called Mongoose.

### What is Mongoose?

[Mongoose](https://mongoosejs.com/) is a JavaScript library that makes it easier to work with MongoDB in a Node.js environment. It provides a simple way to model your data. You can define schemas, do data validation, and build queries as well.

### How to make a connection

MongoDB has already provided you with a URL for connection. Now you'll use Mongoose to send your documents to the database.

To use Mongoose in your project, follow these steps:

Install Mongoose using npm.

```js
npm i mongoose
```

In your `server.js` file, you need to require Mongoose to use it as a connector to the database.

```js
const mongoose = require('mongoose');
```

After you require Mongoose, you need to define the connection `URl` provided in your `server.js` file.

`server.js`:

```js
const mongoose = require('mongoose');

// Replace <username>, <password>, and <dbname> with your actual credentials
const dbURL = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose
  .connect(process.env.dbURL)
  .then((result) => {
    console.log('Connected to MongoDB');
    app.listen(3000, () => {
      console.log('Server started on port 3000');
    });
  })
  .catch((err) => {
    console.error('Could not connect to MongoDB:', err);
  });
```

This setup ensures that Mongoose acts as the connector. It connects your application to the MongoDB database.

## Step 7: Create the Model for the Document Structure

Next, we need to create a model document called a Schema so that when you post data to your database it will be saved accordingly.

To create this model:

1. Create a folder named `models` to keep your application organized.
    
2. Inside the `model's` folder, create a file called `event.js`.
    

In the`event.js` file, you will use Mongoose to define the schema for the event documents. You'll specify the structure and data types for the documents you will send to your database.

Here's the `event.js` file created inside the `model` folder:

```js
const mongoose = require('mongoose');

// Schema
const EventSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: true,
    },
    date: {
      type: Date,
      required: true,
    },
    organizer: {
      type: String,
      required: true,
    },
    price: {
      type: String,
      required: true,
    },
    time: {
      type: String,
      required: true,
    },
    location: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

const Event = mongoose.model('event', EventSchema);

module.exports = Event;
```

When this is done, export so you can use it in your `server.js` file by simply using the **require keyword**.

With the schema created, it can now be exported to the `server.js` file.

Your `server.js` will look like this:

```js
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');
const Event = require('../models/Events');// the event.js file
```

## Step 8: Create HTML Pages

As we talked about earlier, we're using `ejs` in step 4 to render `HTML` code, allowing us to view the code in the browser.

### Form Page

First, let's create a form page. With the form page created, you'll be able to make POST requests which will enable you to send data to your MongoDB database.

To create a basic form, ensure it includes:

* An `action` attribute which specifies the route to send the data.
    
* A `method` attribute which specifies the HTTP request method – in this case, the POST request.
    

A basic form:

```js
<form action="/submit-event" method="POST">
    <h2>Event Creation Form</h2>
  <label for="title">Title</label>
  <input type="text" id="title" name="title" required>

  <label for="date">Date</label>
  <input type="date" id="date" name="date" required>

  <label for="organizer">Organizer</label>
  <input type="text" id="organizer" name="organizer" required>

  <label for="price">Price</label>
  <input type="text" id="price" name="price" required>

  <label for="time">Time</label>
  <input type="text" id="time" name="time" required>

  <label for="location">Location</label>
  <input type="text" id="location" name="location" required>

  <label for="description">Description</label>
  <textarea id="description" name="description" rows="4" required></textarea>

  <button type="submit">Submit</button>
</form>
```

NB: Make sure to add the **name** attribute to each input, or it won't post.

The form created above will let you post data to the specified route. You will then process and store it in your database.

**Here's the result:**

![The form page](https://www.freecodecamp.org/news/content/images/2024/07/image-53.png align="left")

*The form page*

After creating the form page, we need to go back to the `server.js file` and create a POST request to handle the form submission.

`server.js` file:

```js
// posting a data

app.post('/submit-event', (req, res) => {
  const event = new Event(req.body);
  event.save()
    .then((result) => {
      res.redirect('/');
    })
    .catch((err) => {
      console.error(err);
    });
});
```

### The Homepage

Now that the form can post data to the database, we can create the homepage to display the created events in the browser.

First, in your `server.js` file, you need to create a function. It will fetch all the events posted from the form and stored in the database.

Here’s how to set it up:

This is a function created at `server.js` to fetch all data from the database:

```js
// To get all the event

router.get('/', (req, res) => {
  Event.find()
    .then((result) => {
      res.render('index', { title: 'All event', events: result })
    })
    .catch((err) => {
      console.error(err); 
  })
})
```

Next, we will dynamically loop through each part using a `forEach` loop in the homepage file. Since we are using `ejs`, the `HTML` file extension will be `.ejs`.

```js
<div>
  <h2>All events</h2>
  <div>
    <% if (events.length > 0) { %>
      <% events.forEach(event => { %>
        <div>
          <h3><%= event.title %></h3>
          <p><%= event.description %></p>
          <a href="/event/<%= event.id %>">
            Read More
          </a>
        </div>
      <% }) %>
    <% } else { %>
      <p>No events available at the moment.</p>
    <% } %>
  </div>
</div>
```

Here is an explanation of what each part of the code does:

* **Heading (**`<h2>All events</h2>`): Displays "All events" as a heading.
    
* **Event List (**`<div>`): Container for displaying a list of events.
    
* **Conditional Check (** `<% if (events.length > 0) { %> ... <% } else { %> ... <% } %>`): Checks if there are any events (`events.length > 0`). If events exist, it loops through each event (`events.forEach`) to display its details.
    
* For each event, it creates a `<div>` containing the event's title (`event.title`) in a`<h3>` tag, the event's description (`event.description`) in a `<p>` tag, and a link (`<a>`) to view more details about the event (`Read More`). The link directs to `/event/event.id`, where `event.id` is the unique identifier of the event.
    
* **No Events Message (**`<% } else { %> ... <% } %>`): If no events are present (`events.length <= 0`), it displays a message saying "No events available at the moment."
    

## Step 9: Create Partials

Remember that you installed `ejs` into your application to facilitate more dynamic components. It allows you to break your code down further to be more dynamic.

To further organize your code, you'll use something called **Partials**.

Partials let you break down your code into scalable, modular, and manageable parts, keeping your HTML organized.

First, let's create a partial for the navbar.

### How to Create a Partial:

* Inside your `views` folder, create a new folder named `partials`
    
* Inside the `partials` folder, create a new file called `nav.ejs`.
    
* Cut out the navbar code from your homepage file and paste it into `nav.ejs`.
    

### Example:

First, create the Partials folder and file:

![nav partial](https://www.freecodecamp.org/news/content/images/2024/07/partial.png align="left")

*nav partial*

Use the `<%- include() %>` syntax from `ejs` to include the `nav.ejs` partial across pages in your application where you want the navbar to appear.

![Include ()](https://www.freecodecamp.org/news/content/images/2024/07/include.png align="left")

*Include () syntax*

Here's the code:

```js
<!DOCTYPE html>
<html lang="en">
    <%- include('./partial/head.ejs') %>

<body>
    <%- include('./partial/nav.ejs') %>
    <main>
      hello
    </main>
      <%- include('./partial/footer.ejs') %>
</body>
</html>
```

With this setup, your HTML code will be organized. It will be easy to manage and update components like the navbar across different pages. You can use this approach on other parts of your application. For example, the head tag, footer tag, and other reusable components.

## Step 10: Create an Environment Variable File (.Env)

In this tutorial, we'll upload the project to GitHub. You'll protect your port number and MongoDB URL with secure storage. You'll also use an environment variable file, a configuration file known as .env. This file keeps sensitive information safe. It includes passwords and API URLs and prevents exposure.

Here's how to set it up using Node.js:

First, install the `[dotenv](https://www.npmjs.com/package/dotenv)` package.

```js
npm i dotenv
```

Then create a `.env` file. Inside it, add your PORT number and MongoDB URL. It should look something like this:

```plaintext
PORT=3000
dbURl='mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';
```

Then update your `.gitignore` file:

```plaintext

/node_modules
.env
```

Adding .env to your .gitignore ensures that it is not included in your GitHub repository. This tells Git to ignore the .env file when uploading your code.

Then in your `server.js` file, require the `dotenv` package. Load the variables with this line at the top of the file:

To require it, simply type:

```js
require('dotenv').config();
```

This way, you don't need to hardcode the PORT number and MongoDB URL in your `server.js` file. Instead, you can access them using `process.env.PORT` and `process.env.dbURl`.

So your `server.js` file will be cleaner and not messy 😵‍💫

```js
require('dotenv').config();
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');

mongoose
  .connect(process.env.dbURL)
  .then((result) => {
    console.log('Connected to MongoDB');
    app.listen(3000, () => {
      console.log('Server started on port 3000');
    });
  })
  .catch((err) => {
    console.error('Could not connect to MongoDB:', err);
  });
```

## Further Steps

To expand on this basic application, consider adding features such as:

* User authentication
    
* Event search and filter functionality
    
* Event editing and deletion
    
* Notifications for upcoming events
    

### How to Style the Application

If you want to add some styling to your application, follow these steps:

First, create a `public` folder. Inside this folder, create a `style.css` file where you will write your custom CSS.

Then in your `HTML` file, link the `style.css` file in the `<head>` tag as you normally would:

```js
<link rel="stylesheet" href="/style.css">
```

To ensure your CSS file is served correctly, add the following line to your `server.js` file:

```js
app.use(express.static('public'));
```

This application uses Tailwind CSS for styling. But using Tailwind is optional. You can use any CSS framework or write custom CSS to achieve your desired layout.

### How to Include Images

All images should be stored in the `public` folder and referenced in your HTML files. You should also ensure that the `public` folder is correctly set up in your `server.js` file to serve static files.

Here's an example of how to serve static files in `server.js`:

```js
const express = require('express');
const app = express();


// Serve static files from the 'public' folder
app.use(express.static('public'));
```

## Conclusion

Congratulations! You've built a simple application using Node.js, Express.js, ejs, and MongoDB. With these fundamentals, you can expand and enhance your application to meet more specific needs and features.

Feel free to share your progress or ask questions if you encounter any issues.

If you found this article helpful, share it with others who may also find it interesting.

Stay updated with my projects by following me on [Twitter](https://https//twitter.com/ijaydimples), [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) and [GitHub](https://github.com/ijayhub)

Thank you for reading 💖.

Happy coding!
