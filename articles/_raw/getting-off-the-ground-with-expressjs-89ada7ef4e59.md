---
title: Getting off the ground with Express.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-08T19:49:49.000Z'
originalURL: https://freecodecamp.org/news/getting-off-the-ground-with-expressjs-89ada7ef4e59
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ofMfrqFMfpaTH_RMvI_RQA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Victor Ofoegbu

  Writing web apps with the Node.js framework


  A common moment of truth is when you develop a lot of applications that need the
  same or identical functionality. It’s now obvious that copying and pasting code
  isn’t scalable — you need ...'
---

By Victor Ofoegbu

#### Writing web apps with the Node.js framework

![Image](https://cdn-media-1.freecodecamp.org/images/1*ofMfrqFMfpaTH_RMvI_RQA.jpeg)

A common moment of truth is when you develop a lot of applications that need the same or identical functionality. It’s now obvious that copying and pasting code isn’t scalable — you need a tool that was made for flexibility, minimality, and reusability.

That’s where Express sits in the MERN stack. It’s a Node.js framework for building scalable web applications.

In this post, we’ll go deep into building web apps with the Express framework. We’ll look at Database integration, sessions, and cookies, templating engines to solidify our workflow, and finally production and security concerns.

This tutorial requires you to have Node.js and npm installed, and you should possess a basic understanding of Node.js and JavaScript generally. If you aren’t familiar with Node.js, here’s my last post: [The only NodeJs introduction you’ll ever need](https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219?source=activity---post_recommended_rollup). It’s a great place to start diving into Node.js.

### Let’s do Express!

Express was built by TJ Holowaychuk who got the inspiration from the Ruby on Rails framework Sinatra. The latest version of Express is 4.16.1. Express 4 became lighter by letting go of some of the modules that developers didn’t always use. So they could easily import them only when they needed. Makes sense right?

To get started with Express, you need to install it and `require` it in your program.

1) Create a folder called `express-app`, `cd` into it and hit `npm init`. This creates our `package.json` file.

2) Still on the terminal or command line, hit `npm install --save express`. This will install express to the project. The double-dash `save` flag basically means we’re adding it to our `package.json` file.

3) On the root of our express-app folder, create a `server.js` file and copy this inside.

```js
const express = require('express'),
      app = express();

app.get('/',(request,response)=>{
  response.send(‘Hello world’);
});

//Binding the server to a port(3000)
app.listen(3000,()=>console.log(‘express server started at port 300’));
```

const express = require('express'),      app = express();app.get('/',(request,response)=>{  response.send(‘Hello world’);});//Binding the server to a port(3000)app.listen(3000,()=>console.log(‘express server started at port 300’));

4) Go back to the terminal, still in the same folder, and hit `node server.js`. Head to your browser and visit [localhost](http://localhost:3000).

We’re requiring our Express module. If you were quite observant, you must have noticed we didn’t need the `http` module like we do in pure Node.js apps. That’s because Express requires it, so we don’t need to do that again.

When we `require ('express’)`, what gets exported to us is a function, so we can basically call it directly and assign it to the `app` variable. At this point, nothing’s gonna work till we actually handle the request. This is called `routing` and it means giving the client what they are asking for.

Express gives us some basic verbs to do HTTP operations (such as GET, POST, PUT and DELETE). In our example here, we do an `app.get()` method which handles get requests to the server. It takes two arguments: the `path` of the request and a callback to handle the request.

If you didn’t get this, I’ll explain more.

A **path** is an address to a resource on a computer. **A callback is a function passed to another function as an argument that is called when certain conditions happen.**

You might remember this:

```
$('p').click(function(){
   console.log('You clicked me')
});
```

Here, we add a callback to fire when p is clicked. See? It’s easy.

On the last line of `server.js`, we listen at port 3000 and console.log when we start the server.

I bet you can’t write apps with that. Let’s get meaty.

### Routing in Express

Routing means assigning functions to respond to users’ requests. Express routers are basically middleware (meaning they have access to the `request` and `response` objects and do some heavy lifting for us).

Routing in Express follows this basic format:

```
app.VERB(‘path’, callback…);
```

**Where `VERB` is any of the `GET`, `POST`, `PUT`, and `DELETE` verbs.**

We can add as many callbacks as we desire. See an example here:

```js
const express = require('express'),
      app = express();
      
function sayHello(request,response,next){
  console.log(‘I must be called’);
  next();
}

app.get('/', sayHello, (request, response)=>{
  response.send('sayHello');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Head to your terminal or command prompt and hit `node server.js`. You’ll see that the `sayHello` function fires before the response is sent to the browser.

The `sayHello` function takes three arguments (`request`, `response`, and `next`).

The `next()`function, when called, moves control to the next middleware or route.

#### The request and response objects

The `request` object contains information about the incoming request. Here are the most useful properties and methods:

The `**request.params**` variable stores an object of named GET request parameters. For example, clear your `server.js` file and paste this inside:

```js
const express = require('express'),
      app = express();
      
app.get('/:name/:age', (request, response)=>{
   response.send(request.params);
});

app.listen(3000,()=>console.log(‘Express server started at port 3000’));
```

Run this with `node server.js`, then head to your browser and run: `[https://localhost:3000/john/5](https://localhost:3000/john/5)`

In the code above, we’re getting variables from the URL and sending them to the browser. The point is that the `request.params` is an object holding all those GET parameters. Notice the colon before the parameters. They differentiate route parameters from normal routes paths.

The `**request.body**` property stores POST form parameters.

The `**request.query**` property is used to extract the GET form data. Here’s an example of that:

1) Create another folder called `express-query`, and then create two files: `server.js`and `form.html`. Paste this into `server.js` :

```js
const express = require('express'),
      app = express();
      
//route serves both the form page and processes form data
app.get('/', (request, response)=>{
  console.log(request.query);
  response.sendFile(__dirname +'/form.html');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

2) Copy this to the `form.html` file:

```js
<!--action specifies that form be handled on the same page-->
<form action='/' method='GET'>
  <input type='text' name='name'/>
  <input type='email' name='email'/>
  <input type='submit'/>
</form>
```

Run the code with `node server.js`, hit `[localhost:3000](http://localhost:3000)`, and fill and submit the form in your browser. After submitting the form, the data you filled out gets logged to the console.

`**request.headers**` hold key/pair values of the request received by the server. Servers and clients make use of headers to communicate their compatibility and constraints.

`**request.accepts([‘json’,’html’])**`holds an array of data formats and returns the format the browser prefers to collect data in. We’ll also see this when dealing with Ajax forms.

`**request.url**` stores data about the URL of the request.

`**request.ip:**` holds the IP (Internet protocol) address of the browser requesting for information.

The `response` object also ships with some convenient methods to get useful information about the outgoing request.

`**response.send(message)**` sends its argument to the browser.

`**response.json()**` sends its argument as data to the browser in JSON format.

`**response.cookie(name,value,duration)**` provides an interface to set cookies on browsers. We’ll talk about cookies too.

`**response.redirect([redirect status], url)**` redirects the browser to the specified URL with the optional status.

`**response.render(‘file’,{routeData: routedata})**` renders a view to the browser and takes an object containing data the router might need. You’ll understand it better when we see views.

`**response.set(name,value)**` sets header values. But you don’t want to do that, as it gets in the way of the browser’s job.

`**response.status(status)**`sets the status of a particular response (404, 200, 401 and so forth).

You don’t have to memorize all these. As we use them, you’ll subconsciously master them.

### Express Router

With Express Router, we can break our application into fragments that can have their own instances of express to work with. We can them bring them together in a very clean and modular way.

Let’s take for example. These four random URLs:

localhost:3000/users/john

localhost:3000/users/mark

localhost:3000/posts/newpost

localhost:3000/api

Our normal approach of doing this with Express would be:

```js
const express = require('express'),
      app = express();

//Different routes
app.get('/users/john',(request,response)=>{
    response.send(`John’s page`);
});

app.get('/users/mark',(request,response)=>{
    response.send(`John’s page`);
});

app.get('/posts/newpost',(request,response)=>{
  response.send(`This is a new post`);
});

app.get('/api',(request,response)=>{
  response.send(‘Api endpoint’);
});

app.listen(3000,()=>console.log(‘Server started at port 3000’));
```

There’s nothing wrong with this pattern at this point. But it has potential for errors. When our routes are basically just five, there isn’t much of a problem. But when things grow and lots of functionality is required, putting all that code in our `server.js` isn’t something we want to do.

#### **We should let Router do this for us**

Create a folder called `react-router` in the root of our project, create a file inside it, and call it `basic_router.js`. Copy this right in:

```js
const express = require('express'),
      router = express.Router();

//making use of normal routes
router.get('/john',(request,response)=>{
  response.send('Home of user');
});

router.get('/mark',(request,response)=>{
  response.send('Home of user');
});

//exporting thee router to other modules
module.exports = router;
```

We’re basically creating another instance of Express. This time, we’re calling the `Router()` function of Express. It’s possible to directly call `express()` as a function (as in our `**server.js**`) and call `express.Router()` also. This is because Express is exported as a function, and in JavaScript, functions are objects too.

We add routes to it as a normal Express app. But we don’t bind it to any port. The `router` object contains all the routes we’ve defined, so we export only that object so other parts of our program can make use of it too.

We create our main `server.js`, and add it as a middleware. Yes middlewares make work easier, remember?

```js
const express = require('express'),
      app = express();

//requiring the basic_router.js
app.use('/users',require('.react-router/basic_router'));

//routes
app.get('/posts/newpost',(request,response)=>{
  response.send('new post');
});

app.get('/api',(request,response)=>{
  response.send('API route');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

Now run this. Navigate to `localhost:3000/user/john` and `localhost:3000/user/mark`. See? things are quite easy to group at this point.

We can do this for every other route. Create another file for our APIs. We’ll call it `api_route.js`. Copy this right in:

```js
const express = require('express'),
      router = express.Router();

router.get('/',(request,response)=>{
  response.send('Home of user');
});

//some other endpoints to submit data
module.exports = router;
```

Now, go back to our `**server.js**` and change the code to this:

```js
const express = require('express'),
      app = express();

app.use('/users',require('./basic_router'));
                         
app.use('/api',require('./api_route'));

app.get('/posts/newpost',(request,response)=>{
   response.send('new post');
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

This is quite enough information to build basic web app routes.

### Template engines

![Image](https://cdn-media-1.freecodecamp.org/images/1*2jgQ7PxyWZKsORaDoWe6_w.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/JaWmkrSFR2Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Michael Mroczek</a> on <a href="https://unsplash.com/search/photos/engines?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Most of the time, you aren’t definitive about the number of pages you want your website to have. This means you’d want to keep things flexible, reusable, and clean.

Imagine you have a footer that you might want to use on every page. Wouldn’t it be cool if you just put it in a file and embed it with a line of code on every page? Or how would like to lose the `.html` on your URL?

These are just a few things template engines can do for us.

There are a lot of template engines at the moment. But we’ll be using Handlebars to see how template works. Luckily enough, the same principles apply to pretty much all template engines — there are just syntax changes.

To make use of Handlebars, we install it.

```
npm install --save express-handlebars
```

`require` it in your file and configure your app to use it like so:

```js
const express = require('express'),
      hbs = require('express-handlebars').create({defaultLayout:'main.hbs'}),
      app = express();

app.engine('hbs', hbs.engine);
app.set('view engine','hbs');
```

So let’s do a basic rendering with Handlebars:

1. Create a folder called `express-handlebars`, create a `views` folder, and inside the `views` folder create another folder called `layouts`.

2) Create a `server.js` file and paste this inside:

```js
const express = require('express'),
      hbs = require('express-handlebars').create({defaultLayout:'main.hbs'}),
      app = express();

//setting our app engine to handlebars
app.engine('hbs', hbs.engine);
app.set('view engine', 'hbs');
app.get('/',(request,response)=>{
  response.render('home',{title: 'Home'});
});

app.get('/about',(request,response)=>{
  response.render(‘about’,{title: ‘About’});
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

3) Inside the `layouts` folder, create a file `main.hbs`. Paste this inside:

```
<!-- The main.hbs file will act as a default template for every view on the site -->

<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>

<!-- The title variable will be replaced with the title of every page -->

<title>{{title}}</title>
</head>

<body>
<!-- Content of other pages will replace the body variable -->
{{{body}}}
</body>
</html>
```

4) Next, we’re going to create the separate views. Inside of the `views` folder, create two files — `home.hbs`and `about.hbs`. Paste the following inside `home.hbs` :

```
//home.hbs
<!-- This is the Home view and will render into the main.hbs layout -->

<div>
  Hello, I’m the Home page and you’re welcome
</div>
```

and in our `about.hbs` :

```
//about.hbs
<!-- This is the About view and will also render into the main.hbs layout -->

<div>
  Hello, I’m the about page, what do you want to know about
</div>
```

Do a `node server.js` in your terminal and hit `[http://localhost:3000](http://localhost:3000)` on your browser.

What’s happening up here?

We first require `express-handlebars`and create a `defaultLayout`, assigning it to `main.hbs`. This means that all our views will render into the `main.hbs` layout.

Take a look at the `server.js`. Just a few things changed right? Let’s start with these two lines:

```js
app.engine('hbs', hbs.engine);
app.set(‘view engine’,’hbs’);
```

The first line sets the app engine to `hbs.engine` and the second line sets the view engine property to handlebars. Quite straightforward right?

The routes in our `server.js` are also a little different. Here’s the culprit:

```js
response.render('home',{title: 'Home'});
```

While `.send()`sends plain text to the browser, `render()` looks for the first parameter in the `views` folder and renders it to the browser. Most of the time, we might want to pass dynamic content to the view too. We give the render method an object as the second parameter. The object contains keys and values of data to be passed inside the view.

Take this line in our `main.hbs` file in our layout folder.

```
//main.hbs
<title>{{title}}</title>
```

The `{{title}}` is replaced with whatever is passed with the view. In our case, the `{title: 'Home'}`. We can pass as many values as we want to the view. Just add it as a property of the object.

When we do a `response.render()`, Express knows where to get the files we ask for. Let’s look into the `about.hbs`.

```
<!-- This is the About view and will render into the main.handlebars layout -->
<div>
  Hello, I’m the about page, what do you want to know about
</div>
```

The content of this file replaces the body variable in our `layout.handlebars`:

```
{{{body}}}
```

If you’re asking why we’re using two braces for {{title}} and three for the {{{body}}} , you’re on the right track.

When we use two braces, we spit out everything, even the HTML tags (unescaped). Here’s what I mean.

If the content we want to send to the browser is `<b>Hello wor`ld</b>, with two braces, Express will r`ender it as <b&g`t;Hello world</b>. If we make use of three braces, Express will understand that we want a bol**d text and** render it as Hello world (bolded).

This is basically how template engines work in Express. [Handlebars](http://handlebarsjs.com/) provides a one page documentation. I consider it a good place to start.

### Rendering static content in express

Have you ever thought of where we’ll store our CSS, JavaScript files, and images? Well, Express provides a middleware to make the server know where to find static content.

Here’s how to make use of it:

```js
app.use(express.static(__dirname +'public'));
```

Put this at the top of your `server.js`, right after the require statements. `__dirname` holds the path where the program is being run from.

If you didn’t get that, try this.

Delete everything on your `server.js`, and put this inside:

`console.log(__dirname);`

Head to your command line, and run `node server.js`. It shows you the path to the file node that is running.

Where we store our static content is up to us. We might want to name it `assets`or whatever, but you have to make sure you append it to the `dirname` like so:

```js
express.static(__dirname + ‘static_folder_name’).
```

### Express Middleware

Middleware are functions that encapsulate functionality. They perform operations on HTTP requests and give us a high-level interface to customize them. Most middleware take three arguments: **request**, **response** objects, and a **next** function. In error handling middleware, there’s an additional parameter: the **err** object, which can tell us about the error and let us pass it to other middleware.

We add middleware to our server by using `**app.use(name_of_middleware)**`. It’s also important to note that middleware are used in the same order they were added. I’ll show you an example later if you don’t understand.

With this definition, we can also see route functions like `app.get()`, `app.post()` and so on, as middleware, except that they are applied to particular HTTP verb requests. You might also find it interesting to know that there’s an `app.all()`route that is applied to all HTTP requests not considering if they were a GET, POST, or other request.

```js
//This middleware will be called for every request. GET or POST
app.all((request,response)=>{
  console.log('Hello world');
})
```

Route handlers take two parameters, the path to match and the middleware to execute.

```js
app.get('/',(request,,response)=>{
  response.send(‘Hello world’);
});
```

If the path is left out, the middleware applies to every GET request.

```js
//Every GET request will call this middleware
app.get((request,response)=>{
  response.send(‘Hello world’);
});
```

In our example above, once we send a `GET`request, our server responds to the browser by sending a `‘Hello world’` message and then terminates until there’s another request.

But we might want more than one middleware to be called. There’s a way to do this. Remember our `next` function? We could make use of it to push control to another middleware.

Let’s see how this works. Copy and paste this code into our `server.js:`

```js
const express = require('express'),
      app = express();
      
//setting the port
app.set(‘port’, process.env.PORT || 3000);

//first middleware
app.use((request,respone,next)=>{
  console.log(`processing for data for ${request.url}`);
  next();
});

//second middleware
app.use((request,response,next)=>{
  console.log(`The response.send will terminate the request`);
response.send(`Hello world`);
});

//third middleware
app.use((request,respone,next)=>{
  console.log(`I’ll never get called`);
});

app.listen(3000,()=>console.log('Express server started at port 3000'));
```

From the terminal, hit `node server.js` and take a look at the terminal. Head to your browser and open up `localhost:3000`. Look at your console again, and you’ll see something similar.

```
Express server started at port 3000
processing for data for /
The response.send will terminate the request
```

Our first middleware executes every time a request is received. It writes something to the console and calls the `next()`function. Calling the `next()` function tells Express to not terminate the `request` object but sends control to the **next** middleware. Anytime we write a middleware without calling the `next` function, Express terminates the `request`object.

In the second middleware, we pass the `next()` function as an argument but we never call it. This terminates the `request` object and the third middleware never gets called. Note that if we never sent anything to the browser in the second middleware, the client will eventually timeout.

Here are some useful middleware in Express.js:

* [Morgan](https://github.com/expressjs/morgan) — log each request
* [CORS](https://github.com/expressjs/cors) — enables Cross Origin Request Sharing
* [body-parser](https://github.com/expressjs/body-parser) — a middleware to parse the `request.body` in Express apps
* [Multer](https://github.com/expressjs/multer) — Node.js middleware for handling `multipart/form-data`
* [session](https://github.com/expressjs/session) — simple session middleware for Express.js
* [errorhandler](https://github.com/expressjs/errorhandler) — development-only error handler middleware
* [serve-favicon](https://github.com/expressjs/serve-favicon) — favicon serving middleware
* [csurf](https://github.com/expressjs/csurf) — Node.js CSRF protection middleware
* [Passport](http://www.passportjs.org/) — Simple, unobtrusive authentication
* [Merror](https://github.com/mamsoudi/merror) — A RESTful-friendly Express Middleware for HTTP error handling and error responses
* [Expressa](https://github.com/thomas4019/expressa) — express middleware for easily making REST APIs

### Handling form data in Express

The web’s main function is communication. Express provides us with tools to understand what clients request and how to respond properly.

Express basically has two places to store client data. The **request.querystring(for GET request)** and the **request.body (for POST requests)**. On the client side, it’s ideal to use the POST method for form submission because most browsers place limits on the length of the `querystring` and additional data is lost. If you don’t know what a query string is, it’s the part after your URL that contains data and does not fit properly into your routing path system. In case you don’t quite understand what a query string is, here’s an example:

```
facebook.com/users?name=Victor&age=100&occupation=whatever
```

From the point where the question mark begins is called the query string. It passes data to the server but exposes it in the URL.

It’s also good practice to keep the query string as clean as possible. Sending large data with GET requests makes the query string messy.

Let’s see a demo. We’ll take some data from our client via GET and send it back to them.

Create a folder, call it `form-data` , and create two files inside: `server.js` and `form.html`. Paste this into the `server.js` file and `form.html` files respectively:

```js
//server.js file

const express = require('express'),
      app = express();

//setting the port 
app.set('port', process.env.PORT || 3000);

//
app.get('/',(request,response)=>{
  response.sendFile(__dirname +'/form.html');
});

app.get('/process',(request,response)=>{
  console.log(request.query);
  response.send(`${request.query.name} said ${request.query.message}`);
});

app.listen(3000,()=>{
  console.log('Express server started at port 3000');
});
```

```html
//form.html

<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>Form page</title>
    <style>
      *{
        margin:0;
        padding:0;
        box-sizing: border-box;
        font-size: 20px;
      }
      input{
        margin:20px;
        padding:10px;
      }
      input[type=”text”],
      textarea {
        width:200px;
        margin:20px;
        padding:5px;
        height:30px;
        display: block;
      }
      textarea{
        resize:none;
        height:60px;
      }
    </style>
  </head>
<body>
  <form action='/process' method='GET'>
    <input type='text' name='name' placeholder='name'/>
    <textarea name='message' placeholder='message'></textarea>
    <input type='submit'/>
  </form>
</body>
</html>
```

Run `node server.js`, head to `localhost:3000`, fill the form and submit it.

Here’s what the result would look like.

In our `server.js` file here, we have to two GET routes. One for `localhost:3000` and `localhost:3000/process`.

```js
app.get(‘/’,(request,response)=>{
   response.sendFile(__dirname + ‘/form.html’);
});
```

And

```js
app.get(‘/process’,(request,response)=>{
  response.send(`${request.query.name} said ${request.query.message}`);
});
```

Head to your your console. You’ll see an object. This proves that our `request.query` is an object that contains all queries and their values.

```js
{
  name: 'victor',
  message: 'Hello world'
}
```

If you take a look at our form in the `form.html`page, you’ll notice our form has `action` and `method`attributes. The `action`attribute specifies the page or route that should handle the form’s data (‘process’ in this case). When the form gets submitted, it sends a GET request to the `process`route with the content of our form as `querystring`data.

Our `server.js` file also handles the request for the process path and sends data passed from our `form.html` to the browser and console.

Let’s see how we would handle this with the POST method. It’s time to clear our `server.js`file. Copy and paste this code into `server.js`:

```js
//server.js

const express = require('express'),
      app = express(),
      
//You must require the body-parser middleware to access request.body in express
bodyParser = require('body-parser');

//configuring bodyparser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//setting our port
app.set('port', process.env.PORT || 3000);

//Get route for localhost:3000
app.get('/',(request,response)=>{
  response.sendFile(__dirname +'/form.html');
});

//POST route for form handling
app.post('/',(request,response)=>{
  console.log(request.body);  
  response.send(`${request.body.name} said ${request.body.message}`);
});

app.listen(3000,()=>{
  console.log('Express server started at port 3000');
});
```

```js
//form.html file

<!DOCTYPE html>
<html>
  <head>
  <meta charset='UTF-8'>
  <title>Form page</title>
    <style>
      *{
        margin:0;
        padding:0;
        box-sizing: border-box;
        font-size: 20px;
      }
      input{
        margin:20px;
        padding:10px;
      }
      input[type='text'],
      textarea {
        width:200px;
        margin:20px;
        padding:5px;
        height:30px;
        display: block;
      }
      textarea{
        resize:none;
        height:60px;
      }
    </style>
  </head>
<body>
  <form action='/' method='POST'>
    <input type='text' name='name' placeholder='name'/>
    <textarea name='message' placeholder='message'></textarea>
    <input type='submit'/>
  </form>
</body>
</html>
```

If you look closely, the first different thing we’re doing is requiring and using `body-parser`. Body-parser is a middleware that makes POST data available in our `request.body`. Bear in mind that the `request.body` won’t work without the body-parser middleware.

You might also notice we have both GET and POST route handlers. The GET middleware shows the form and the POST middleware processes it. It’s possible for both of them to use one route path because they have different methods.

We couldn’t do this for our first example because our form method was GET. Obviously, you can’t have two GET requests for the same route and have both of them send data to the browser. That’s why our first example processed the form on the `/process` path.

### Handling AJAX forms

Handling Ajax forms with Express is quite straightforward. Express provides us with a `request.xhr`property to tell us if a request is sent via AJAX. We can couple that with the `request.accepts()`method we talked about earlier. It helps us determine what format the browser wants the data in. If the client will like JSON, well, we’ll just give it JSON.

Let’s modify our `form.html` to use AJAX and our `server.js` to accept AJAX and send JSON.

```html
<!DOCTYPE html>
<html>
  <head>
  <meta charset='UTF-8'>
  <title>Form page</title>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js'></script>
  <style>
    *{
      margin:0;
      padding:0;
      box-sizing: border-box;
      font-size: 20px;
    }
    input{
      margin:20px;
      padding:10px;
    }
    input[type=”text”],
    textarea {
      width:200px;
      margin:20px;
      padding:5px;
      height:30px;
      display: block;
    }
    textarea{
      resize:none;
      height:60px;
    }
  </style>
  </head>
<body>
  <div></div>
                       
  <form action='/' method='POST'>
    <input type='text' name='name' placeholder='name'/>
    <textarea name='message' placeholder='message'></textarea>
    <input type='submit'/>
  </form>
                       
  <script>
    $('form').on('submit',makeRequest);
      function makeRequest(e){
        e.preventDefault();
        $.ajax({
          url:'/',
          type : 'POST',
          success: function(data){
            if(data.message){
              $('div').html(data.message);
            } else {
              $('div').html('Sorry, an error occured');
            }
          },
          error: function(){
            $('div').html('Sorry, an error occurred');
          }
      });
    }
  </script>
  </body>
</html>
```

```js
//server.js

const express = require('express'),
      app = express(),
      bodyParser = require('body-parser');

//configuring the body-parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//setting our app port
app.set('port', process.env.PORT || 3000);

//Route for  get requests.
app.get('/',(request,response)=>{
  response.sendFile(__dirname +'/form.html');
});

//Route to handle POST form requests.
app.post('/',(request,response)=>{
//we check if the request is an AJAX one and if accepts JSON
  if(request.xhr || request.accepts('json, html')==='json'){
    response.send({message:'Just wanted to tell you. It worked'});
   } else {
    //Do something else by reloading the page.
   }
});

app.listen(3000,()=>{
  console.log('Express server started at port 3000');
});
```

#### **Here’s how this works**

Not much changes here — we just added a way to vet if the request was made with AJAX.

So here’s what we’re doing. We made the request an AJAX one with the POST method. We linked to jQuery CDN. In the script tag, we attach an event handler for the submit event. When we do this, we prevent the default behavior of reloading the page.

We then use the jQuery `$.ajax()` method to make an AJAX request. The server responds with an object with a `message`property, which we then append to the empty div.

If you aren’t familiar with AJAX, I once wrote some articles on AJAX. Check them out: [A gentle introduction to AJAX](https://codeburst.io/a-gentle-introduction-to-ajax-1e88e3db4e79) and [Easier asynchronous requests with jQuery.](https://codeburst.io/easier-asynchronous-requests-with-jquery-80507b502e62)

### Databases in Node.js apps

MongoDB and CouchDB are some database systems that are suitable for Node.js applications. This doesn’t completely rule out the possibility of using other databases. We’ll look at MongoDB, but you can choose any one you like.

Documents replace rows in a relational database like MySQL. In MongoDB and other document-based databases, data is stored and retrieved in an object format. This means we can have deeply nested structures.

If you consider objects in JavaScript, there’s no way to validate that the value of an object property is a particular type. Here’s what I mean:

`const obj = { text : 1234}`

There’s no way to make sure the value of `text`is a string.

Fortunately, there’s Mongoose. Mongoose allows you define schemas that strongly validate data and ensure they match objects or documents in a MongoDB. Mongoose is an Object Document Mapper (ODM).

[An introduction to Mongoose](https://code.tutsplus.com/articles/an-introduction-to-mongoose-for-mongodb-and-nodejs--cms-29527) is a nice place to start exploring and working with Mongoose.

### Sessions and Cookies in Express

HTTP is stateless. Meaning any request or response sent by the browser or server respectively maintains no information (state) about the previous or future requests and responses. Every single request has all it takes to evoke a new server response.

But there has to be a way for servers to remember clients as they browse through the site so they don’t have to enter passwords on every page.

The web has been innovative enough to make use of cookies and sessions. Cookies are basically small files stored on the client’s machine. When clients send requests, the server uses it to identify them. More like a passport, the server then knows it’s them and applies all their preferences.

So the idea would be to store files on the client’s machine. While this is not a bad idea, we want to make sure we don’t abuse the user’s storage by storing huge amounts of data. On the other side of things, we understand that if we want to make things harder to guess and more secure, we make it longer and more complex. How can we achieve these two concurrently?

People came up with sessions. So the idea of sessions is that instead of storing all the information on the client’s cookie, the server stores an identifier in the cookie (a small string). When the client sends requests, the server takes that unique string and matches it to the user’s data on the server. This way, we get to store any amount of data and still remember users.

To make use of cookies in Express, we need to require the `cookie-parser` middleware. Remember our middleware?

I’m not in the best position to explain this in depth. But someone did it better here: [Express sessions](https://glebbahmutov.com/blog/express-sessions/).

### Security in Express apps

The web is not secured by default. Packets are the way data is sent over the web. These packets are unencrypted by default. When we think about web security, the first place to start is to secure those packets.

**HTTPS**: That’s no new word! Like you might have guessed, the difference between HTTP and HTTPS is the S (Security). HTTPS encrypts packets traveling through the web so people don’t do malicious things with it.

#### So how do I go about getting HTTPS?

Chill, let’s take it slow. To get HTTPS, you need to approach a Certificate Authority (CA). HTTPS is based on the server having a public key certificate, sometimes called an SSL. CAs assign certificates to qualified servers. You have to also understand that CAs make root certificates that get installed when you install your browser. So browsers can easily communicate with servers with certificates too.

**Good news**: Anybody can make their own certificates.

**Bad news**: The browsers can’t recognize those certificates because they weren’t installed as root certificates.

**Impossible**: You can’t configure all the browsers in the world during installation to recognize your certificate.

I can tell what you’re thinking now. You’re thinking that you can create your own certificate for testing and development and get one in production. Well, that’s smart and possible.

The browser will give you warnings, but you are aware of the problem so it won’t be much of an issue. Here’s a [post](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/) that walks you through creating your own certificate.

[**How to Set Up HTTPS Locally Without Getting Annoying Browser Privacy Errors**](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/)  
[_Setting up HTTPS locally can be tricky business. Even if you do manage to wrestle self-signed certificates into…_](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/)  
[deliciousbrains.com](https://deliciousbrains.com/https-locally-without-browser-privacy-errors/)

Enough talking. Let’s assume you now have the SSL certificate. Here’s how to make it work with your Express app.

#### Enabling HTTPS in your Node app

We need to make use of the `https` module for HTTPS. After obtaining our credentials from a Certificate Authority, we’ll include it as an argument to the `**createServer()**` method.

```js
//server.js

const express = require('express'),
	  https = require('https'),
	  http = require('http'),
	  fs = require('fs'),
	  app = express();

//credentials obtained from a Certificate Authority
var options = {
  key: fs.readFileSync('/path/to/key.pem'),
  cert: fs.readFileSync('/path/to/cert.pem')
};

//Binding the app on different ports so the app can be assessed bt HTTP and HTTPS
http.createServer(app).listen(80);
https.createServer(options, app).listen(443);
```

Notice we’re requiring `http`and `https.` This is because we want to respond to both. In our program, we’re making use of the `fs` module (file-system).

We basically provide the path to where our SSL key and certificate is stored. A module or something. Observe that we’re making use of the `**readFileSync**` method instead of the `**readFile**`. If you understand Node.js architecture, you’ll infer that we want to read the file synchronously before running any other lines of code.

Running this code asynchronously might lead to situations where aspects of our code that require the content of the file don’t get them on time.

The last two lines bind the HTTP and HTTPS to two different ports and take different arguments. Why are we doing this?

At most times, we want our server to still listen to requests with HTTP and maybe redirect them to HTTPS.

**Note**: the default port for HTTPS is 443.

To do this basic redirect, we’ll install and require a module `express-force-ssl` at the top of our program like so:

```
npm install express-force-ssl
```

And configure like so:

```js
const express_force_ssl = require('express-force-ssl');
app.use(express_force_ssl);
```

Now, our server can take care of both HTTP and HTTPS requests effectively.

#### Cross-Site Request Forgery (CSRF)

This is the other big thing you’d want to protect yourself from. It happens when requests come to your server but not directly from your user. For example, you have an active session on Facebook.com and you have another tab open. Malicious scripts can run on the other site and make requests to Facebook’s server.

A way to handle this is to ensure that requests come only from your website. That’s quite easy. We assign an ID to users and attach it to forms, so when they submit, we can match up the ID and deny access if it doesn’t match.

Luckily, there’s a middleware that handles this — `csurf`middleware. Here’s how to use it:

```
npm install csurf
```

To use it in our program:

```js
const express = require('express'),
	  body_parser = require('body-parser'),
	  hbs = require('express-handlebars').create({defaultLayout: 'main',extname:'hbs'});
	  session = require('express-session'),
	  csurf = require('csurf'),

	  app = express();

//setting the app port
app.set('port', process.env.PORT || 3000);

//configuring the app for handlebars
app.engine('hbs', hbs.engine);
app.set('view engine', 'hbs');


//setting up a session csrf
app.use(session({
	name: 'My session csrf',
	secret: 'My super session secret',
	  cookie: {
	  	maxAge: null,
	    httpOnly: true,
	    secure: true
	  }
	})
  );

app.use(csurf());

//configuring the body parser middleware
app.use(body_parser.urlencoded());

//Route to login
app.get('/login', (request,response)=>{
	console.log(request.csrfToken());
	response.render('login',{
		csrfToken : request.csrfToken(),
		title: 'Login'
	});
});

app.listen(3000,()=>console.log('Express app started at port 3000'));
```

```html
<b>Here's the generated csrf token</b> ({{csrfToken}})<br><br>

<form method='POST' action='/process'>
  <!-- We pass the _csrf token as a hidden input -->
  <input type='hidden' name='_csrf' csurf={{csrfToken}}/>
  <input type='text' name='name'/>
  <input type='submit'/>
</form>
```

Run `node server.js` , head to your browser `localhost:3000`, fill the form and submit. Also check in your command line and see the token logged.

What we’re doing is generating and passing the `csrfToken` to our login view.

**Note:** The `csurf` module requires `express-session` module to work. We configure our session CSRF and pass it to the view via the `response.render()` method.

Our view can now append it to the form or any other sensitive request.

So what happens when the browser doesn’t get the CSRF token from the browser forms? It spits an error. Make sure you have an error handling route in your Express application, or else your application might misbehave.

#### Authentication

One step to reduce authentication problems is to let people sign up and sign in with third-party apps (Facebook, Twitter, Google,+ and so on). A whole lot of people have these accounts, and you can also have access to some of their data like emails and usernames. Modules like `passport.js` provide a very elegant interface to handle such authentications.

Here’s the [official passport.js documentation](http://www.passportjs.org/docs/). I think it’s a nice place to start.

Another step to reduce authentication problems is to always encrypt all passwords and decrypt them back when showing them to the users.

One more thing. I see this on a lot of websites. They set crazy criteria for users’ password on the site. I understand that they’re trying to make passwords more secure, but think about it. Whose job is it? The developer or the user?

The user should be least bothered about security issues. When criteria like these are set on passwords, users have no other option than to use passwords they’ll never remember. I know the web is getting better and we’ll figure out a way to make authentication better.

Till then I think we can end this here.

This is a lot of information. But you need more than this to build scalable web applications. Here are some insightful books for learning more about Express.

If this was useful, you should follow me on [Twitter](https://twitter.com/vick_OnRails) for more useful stuff.

1. [Express in action](https://www.amazon.com/Express-Action-Writing-building-applications/dp/1617292427) by [Evan Hahn](https://www.freecodecamp.org/news/getting-off-the-ground-with-expressjs-89ada7ef4e59/undefined).
2. [Getting MEAN with Express, Mongo, Angular and Node](https://www.amazon.com/Getting-MEAN-Mongo-Express-Angular/dp/1617294756) by [Simon Holmes](https://www.freecodecamp.org/news/getting-off-the-ground-with-expressjs-89ada7ef4e59/undefined).

