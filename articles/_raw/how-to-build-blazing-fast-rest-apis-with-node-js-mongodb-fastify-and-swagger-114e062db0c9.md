---
title: How to build blazing fast REST APIs with Node.js, MongoDB, Fastify and Swagger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T22:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-blazing-fast-rest-apis-with-node-js-mongodb-fastify-and-swagger-114e062db0c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B8yGyadpWiDJtyXGVtNO-Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: REST API
  slug: rest-api
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Siegfried Grimbeek

  Presumably no web developer is a stranger to REST APIs and the challenges that architecting
  an effective and efficient API solution brings.

  These challenges include:


  Speed (API Response Times)

  Documentation (Clear concise docum...'
---

By Siegfried Grimbeek

Presumably no web developer is a stranger to **REST APIs** and the challenges that architecting an effective and efficient **API** solution brings.

These challenges include:

* Speed (API Response Times)
* Documentation (Clear concise documents, describing the API)
* Architecture and Sustainability (Maintainable and expandable codebase)

In this tutorial we are going to address all of the above using a combination of **Node.js**, **MongoDB**, **Fastify** and **Swagger**.

The source code for the project is available on [GitHub](https://github.com/siegfriedgrimbeek/fastify-api).

### Before we begin…

You should have some beginner/intermediate **JavaScript knowledge**, have heard of **Node.js** and **MongoDB,** and know what **REST APIs** are.

Below are some links to get you updated:

* [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
* [Node.js](https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219)
* [MongoDB](https://docs.mongodb.com/manual/introduction/)
* [REST APIs](https://restful.io/an-introduction-to-api-s-cee90581ca1b)

#### The Technology we will be using:

* [Fastify](https://www.fastify.io/)
* [Mongoose](https://mongoosejs.com/)
* [Swagger](https://swagger.io/)

It is a good idea to open the above pages in new tabs, for easy reference.

#### You will need to have the following installed:

* [NodeJS/NPM](https://nodejs.org/en/)
* [MongoDB](https://docs.mongodb.com/manual/installation/)
* [Postman](https://www.getpostman.com/)

You will also need an [**IDE**](https://ourcodeworld.com/articles/read/200/top-7-best-free-web-development-ide-for-javascript-html-and-css) and a **terminal,** I use [iTerm2](https://www.iterm2.com/) for Mac and [Hyper](https://hyper.is/) for Windows.

### Let’s get started!

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jw9V__6jYhm2amP74D_0lw.png)

Initialise a new project by opening your **terminal,** executing each of the following lines of code:

```bash
mkdir fastify-api
cd fastify-api
mkdir src
cd src
touch index.js
npm init
```

In the above code, we created two new directories, navigated into them, created an `index.js` file and initialed our project via [npm](https://www.npmjs.com/).

You will be prompted to enter several values when initialising a new project, these you can leave blank and update at a later stage.

Once completed, a [package.json](https://alligator.io/nodejs/package-json/) file is generated in the `src` directory. In this file you can change the values entered when the project was initialised.

Next we install all the **dependancies** that we will need:

```bash
npm i nodemon mongoose fastify fastify-swagger boom
```

Below is a brief description of what each package does, quoted from their respective websites:

[**nodemon**](https://github.com/remy/nodemon)

> nodemon is a tool that helps develop node.js based applications by automatically restarting the node application when file changes in the directory are detected.  
>   
> nodemon does not require _any_ additional changes to your code or method of development. nodemon is a replacement wrapper for `node`, to use `nodemon` replace the word `node` on the command line when executing your script.

To set up **nodemon**, we need to add the following line of code to our `package.json` file, in the scripts object:

```json
“start”: “./node_modules/nodemon/bin/nodemon.js ./src/index.js”,
```

Our `package.json` file should now look as follows:

```json
{
  "name": "fastify-api",
  "version": "1.0.0",
  "description": "A blazing fast REST APIs with Node.js, MongoDB, Fastify and Swagger.",
  "main": "index.js",
  "scripts": {
  "start": "./node_modules/nodemon/bin/nodemon.js ./src/index.js",
  "test": "echo \"Error: no test specified\" && exit 1"
},
  "author": "Siegfried Grimbeek <siegfried.grimbeek@gmail.com> (www.siegfriedgrimbeek.co.za)",
  "license": "ISC",
  "dependencies": {
  "boom": "^7.2.2",
  "fastify": "^1.13.0",
  "fastify-swagger": "^0.15.3",
  "mongoose": "^5.3.14",
  "nodemon": "^1.18.7"
  }
}
```

[**mongoose**](https://mongoosejs.com/)

> Mongoose provides a straight-forward, schema-based solution to model your application data. It includes built-in type casting, validation, query building, business logic hooks and more, out of the box.

[**fastify**](https://www.fastify.io/)

> Fastify is a web framework highly focused on providing the best developer experience with the least overhead and a powerful plugin architecture. It is inspired by Hapi and Express and as far as we know, it is one of the fastest web frameworks in town.

[**fastify-swagger**](https://github.com/fastify/fastify-swagger)

> [Swagger](https://swagger.io/) documentation generator for Fastify. It uses the schemas you declare in your routes to generate a swagger compliant doc.

[**boom**](https://github.com/hapijs/boom)

> boom provides a set of utilities for returning HTTP errors.

### Setup up the server and create the first route!

![Image](https://cdn-media-1.freecodecamp.org/images/1*rocnESJrNWsRGXMygLfDCQ.png)

Add the following code to your `index.js` file:

```js
// Require the framework and instantiate it
const fastify = require('fastify')({
  logger: true
})

// Declare a route
fastify.get('/', async (request, reply) => {
  return { hello: 'world' }
})

// Run the server!
const start = async () => {
  try {
    await fastify.listen(3000)
    fastify.log.info(`server listening on ${fastify.server.address().port}`)
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}
start()
```

We require the **Fastify** framework, declare our first route and initialise the server on `port 3000`, the code is pretty self explanatory but take note of the options object passed when initialising **Fastify**:

```js
// Require the fastify framework and instantiate it
const fastify = require('fastify')({
  logger: true
})
```

The above code enables **Fastify’s** built in logger which is disabled by default.

You can now run the follow code in your `src` directory in your **terminal**:

```bash
npm start
```

Now when you navigate to [http://localhost:3000/](http://localhost:3000/) you should see the `{hello:world}` object returned.

We will get back to the `index.js` file but for now let’s move on to setting up our database.

### Start MongoDB and create the model!

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ce0gUe0LbnhL7ebnDGTp5w.png)

Once **MongoDB** has been successfully installed, you can open a new terminal window and start up a **MongoDB** instance by running the following:

```
mongod
```

With **MongoDB**, we do not need to create a database. We can just specify a name in the setup and as soon as we store data, **MongoDB** will create this database for us.

Add the following to your `index.js` file:

```js
...

// Require external modules
const mongoose = require('mongoose')

// Connect to DB
mongoose.connect(‘mongodb://localhost/mycargarage’)
 .then(() => console.log(‘MongoDB connected…’))
 .catch(err => console.log(err))
 
...
```

In the above code we require **Mongoose** and connect to our **MongoDB** database. The database is called `mycargarage` and if all went well, you will now see `MongoDB connected...` in your terminal.

_Notice that you did not have to restart the app, thanks to the `Nodemon` package that we added earlier._

Now that our database is up and running, we can create our first Model. Create a new folder within the `src` directory called `models`, and within it create a new file called `Car.js` and add the following code:

```js
// External Dependancies
const mongoose = require('mongoose')

const carSchema = new mongoose.Schema({
  title: String,
  brand: String,
  price: String,
  age: Number,
  services: {
    type: Map,
    of: String
  }
})

module.exports = mongoose.model('Car', carSchema)
```

The above code declares our `carSchema` that contains all the information related to our cars. Apart from the two obvious data types: `String` and `Number`. We also make use of a `Map` which is relatively new to **Mongoose** and you can read more about it [here](https://thecodebarbarian.com/whats-new-in-mongoose-5.1-map-support.html). We then export our `carSchema` to be used within our app.

We could proceed with setting up our routes, controllers and config in the `index.js` file, but part of this tutorial is demonstrating a sustainable codebase. Therefore each component will have its own folder.

### Create the car controller

To get started with creating the controllers, we create a folder in the `src` directory called `controllers`, and within the folder, we create a `carController.js` file:

```js
// External Dependancies
const boom = require('boom')

// Get Data Models
const Car = require('../models/Car')

// Get all cars
exports.getCars = async (req, reply) => {
  try {
    const cars = await Car.find()
    return cars
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Get single car by ID
exports.getSingleCar = async (req, reply) => {
  try {
    const id = req.params.id
    const car = await Car.findById(id)
    return car
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Add a new car
exports.addCar = async (req, reply) => {
  try {
    const car = new Car(req.body)
    return car.save()
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Update an existing car
exports.updateCar = async (req, reply) => {
  try {
    const id = req.params.id
    const car = req.body
    const { ...updateData } = car
    const update = await Car.findByIdAndUpdate(id, updateData, { new: true })
    return update
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Delete a car
exports.deleteCar = async (req, reply) => {
  try {
    const id = req.params.id
    const car = await Car.findByIdAndRemove(id)
    return car
  } catch (err) {
    throw boom.boomify(err)
  }
}
```

The above may seem like a little much to take in, but it is actually really simple.

* We require **boom** to handle our errors: `boom.boomify(err)`.
* We export each of our functions which we will use in our route.
* Each function is an **async** function that can contain an **await** expression that pauses the execution of the **async function** and waits for the passed Promise’s resolution, and then resumes the **async function’s** execution and returns the resolved value. [Learn more here.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
* Each function is wrapped in a try / catch statement. [Learn more here.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
* Each function takes two parameters: `req` (the request) and `reply` (the reply). In our tutorial we only make use of the request parameter. We will use it to access the request body and the request parameters, allowing us to process the data. [Learn more here.](https://www.fastify.io/docs/latest/Reply/)
* Take note of the code on line 31:  
`const car = new Car({ …req.body })`   
This makes use of the **JavaScript** spread operator. [Learn more here.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
* Take note of the code on line 42:  
`const { …updateData } = car`  
This makes use of the **JavaScript** destructuring in conjunction with the spread operator. [Learn more here.](https://codeburst.io/use-es2015-object-rest-operator-to-omit-properties-38a3ecffe90)

Other than that, we make use of some standard **Mongoose** features used to manipulate our database.

You are probably burning to fire up your API and do a sanity check, but before we do this, we just need to connect the **controller** to the **routes** and then lastly connect the **routes** to the app.

#### Create and import the routes

Once again, we can start by creating a folder in the root directory of our project, but this time, it is called `routes`. Within the folder, we create an `index.js` file with the following code:

```js
// Import our Controllers
const carController = require('../controllers/carController')

const routes = [
  {
    method: 'GET',
    url: '/api/cars',
    handler: carController.getCars
  },
  {
    method: 'GET',
    url: '/api/cars/:id',
    handler: carController.getSingleCar
  },
  {
    method: 'POST',
    url: '/api/cars',
    handler: carController.addCar,
    schema: documentation.addCarSchema
  },
  {
    method: 'PUT',
    url: '/api/cars/:id',
    handler: carController.updateCar
  },
  {
    method: 'DELETE',
    url: '/api/cars/:id',
    handler: carController.deleteCar
  }
]

module.exports = routes
```

Here we are requiring our **controller** and assigning each of the functions that we created in our controller to our routes.

As you can see, each route consists out of a method, a url and a handler, instructing the app on which function to use when one of the routes is accessed.

The `:id` following some of the routes is a common way to pass parameters to the routes, and this will allow us to access the **id** as follows:

`[http://127.0.0.1:3000/api/cars/5bfe30b46fe410e1cfff2323](http://127.0.0.1:3000/api/cars/5bfe30b46fe410e1cfff2323)`

#### Putting it all together and testing our API

Now that we have most of our parts constructed, we just need to connect them all together to start serving data via our **API**. Firstly we need to import our **routes** that we created by adding the following line of code to our main `index.js` file:

```js
const routes = require(‘./routes’)
```

We then need to loop over our routes array to initialise them with **Fastify.** We can do this with the following code, which also needs to be added to the main `index.js` file:

```js
routes.forEach((route, index) => {
 fastify.route(route)
})
```

Now we are ready to start testing!

The best tool for the job is [Postman](https://www.getpostman.com/), which we will use to test all of our routes. We will be sending our data as raw objects in the body of the request and as parameters.

Finding all cars:

![Image](https://cdn-media-1.freecodecamp.org/images/1*YoxRE054Q7qgrAxaCgrzLw.png)

Finding a single car:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1T4C1-LmgWv0S5W-bgk4wQ.png)

Adding a new car**:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYqA6GVUv_dcKArTRJ_NPA.png)

** The services appear to be empty, but the information does in fact persist to the database.

Updating a car:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BcZdrz0X3dyfDfOhkDFwFg.png)

Deleting a car:

![Image](https://cdn-media-1.freecodecamp.org/images/1*9PwntcmeC1wfYMqo3raXdQ.png)

We now have a fully functional API — but what about the documentation? This is where **Swagger** is really handy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7iaXjYojG6kWxLTZaW1x4Q.png)

#### Adding Swagger and wrapping up.

Now we will create our final folder called **config.** Inside we will create a file called `swagger.js` with the following code:

```js
exports.options = {
  routePrefix: '/documentation',
  exposeRoute: true,
  swagger: {
    info: {
      title: 'Fastify API',
      description: 'Building a blazing fast REST API with Node.js, MongoDB, Fastify and Swagger',
      version: '1.0.0'
    },
    externalDocs: {
      url: 'https://swagger.io',
      description: 'Find more info here'
    },
    host: 'localhost',
    schemes: ['http'],
    consumes: ['application/json'],
    produces: ['application/json']
  }
}
```

The above code is an object with the options which we will pass into our **fastify-swagger** plugin. To do this, we need to add the following to our `index.js` file:

```js
// Import Swagger Options
const swagger = require(‘./config/swagger’)

// Register Swagger
fastify.register(require(‘fastify-swagger’), swagger.options)
```

And then we need to add the following line after we have initialised our **Fastify** server:

```js
...
await fastify.listen(3000)
fastify.swagger()
fastify.log.info(`listening on ${fastify.server.address().port}`)
...
```

And that is it! If you now navigate to [http://localhost:3000/documentation](http://localhost:3000/documentation), you should see the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HV-5eImCMs7LtiLodTz7CQ.png)

As simple as that! You now have self updating API documentation that will evolve with your API. You can easily add additional information to your routes, see more [here](https://github.com/fastify/fastify-swagger).

#### Whats Next?

Now that we have a basic API in place, the possibilities are limitless. It can be used as the base for any app imaginable.

In the next tutorial, we will integrate **GraphQL** and eventually integrate the frontend with **Vue.js** too!

