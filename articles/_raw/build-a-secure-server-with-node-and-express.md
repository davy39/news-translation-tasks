---
title: How to Build a Secure Server with Node.js and Express and Upload Images with
  Cloudinary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-14T16:51:14.000Z'
originalURL: https://freecodecamp.org/news/build-a-secure-server-with-node-and-express
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-aleksandar-pasaric-325185.jpg
tags:
- name: Express
  slug: express
- name: node js
  slug: node-js
- name: servers
  slug: servers
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'By Njoku Samson Ebere

  In this tutorial, we will learn how to create a server. We will begin without express
  and then strengthen the server using express. After that, we will see how to upload
  images to Cloudinary from the app we have created.

  I assum...'
---

By Njoku Samson Ebere

In this tutorial, we will learn how to create a server. We will begin without `express` and then strengthen the server using `express`. After that, we will see how to upload images to Cloudinary from the app we have created.

I assume that you already understand the basics of `Node.js`, `express` and `nodemon` so we will just go straight to the practical parts.

## Install Node.js and NPM

If you haven't yet done so, you'll need to install Node and npm on your machine.

1. Go to the [Node.js website](https://nodejs.org/en/)
2. Click on the recommended download button

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-13-at-18.52.57.png)
_Nodejs home page_

When the download is complete, install Node using the downloaded `.exe` file (it follows the normal installation process).

### Check if the installation was successful

1. Go to your terminal/command prompt _(run as administrator if possible)_
2. Type in each of the following commands and hit Enter

```javascript
node -v 
npm -v
```

Your output should be similar to the image below:

![Image](https://www.freecodecamp.org/news/content/images/2021/12/termial-1.jpeg)
_Terminal showing the versions of node and npm_

The version may be different but that's OK.

## How to Create a Node Server without Express

For the rest of this tutorial, I will be using VS code as my editor. You can use whatever editor you choose.

Let's start by creating a project directory. Open a terminal and type the following to create a directory and open it:

```javascript

mkdir server-tutorial cd server-tutorial

```

I named my project directory `server-tutorial`, but you can name yours as you please.

In the terminal, type `npm init`. Hit the `Enter` button for all prompts. When completed, you should have a `package.json` file seated in your project directory.

The `package.json` file is just a file with all the details of your project. You don't have to open it.

Create a file called `index.js`.

In the file, require the `HTTP` module like so:

```javascript
  const http = require('http');

```

Call the `createServer()` method on it and assign it to a constant like this:

```javascript
  const server = http.createServer();

```

Call the `listen()` method on the server constant like this:

```javascript
  server.listen();

```

Give it a port to listen to. Now this could be any free port, but we will be using port `3000` which is the conventional port. So we have this:

```javascript
  const http = require('http');

  const server = http.createServer();

  server.listen(3000);

```

Basically, that is all you need do to create a server.

### How to Test the Server

In your terminal (should be in the project directory), type `node index.js` and hit the `Enter` button.

Open a new tab in [`postman`](https://www.getpostman.com/) or any web `browser` and in the address bar, type `http://localhost:3000/`, and hit the `Enter` button. (I will be using postman because of its extended functionality outside the box.)

You will notice that your browser or postman keeps loading indefinitely like so:

![Postman Loading Indefinitely](https://dev-to-uploads.s3.amazonaws.com/i/fp7k6pcfctn0548n0rmx.JPG)

Yay! That is fine. Our Server is up and running.

But it's boring already. We need to make the server talk to us.

Let's get to it immediately.

### How to Send Back a Response from the Server

Back in the code, add the following to `const server = http.createServer();`:

```javascript
 (request, response) => {
    response.end('Hey! This is your server response!');
 }

```

So we now have:

```javascript
  const http = require('http');

  const server = http.createServer((request, response) => {
    response.end('Hey! This is your server response!');
  });

server.listen(3000);

```

In basic terms, the `request` object tells the `server` that we want something, the `response` object tells us what the `server` has to say about our `request`, and the `end()` method terminates the communication with the `server` `response`.

Hopefully, that makes sense!

Now, test the server again following the steps we outlined above and your server should be talking to you. This is my output:

![Postman returning a response](https://dev-to-uploads.s3.amazonaws.com/i/b0189qzrdkppbvr57uo8.JPG)

Feel free to change the string as you wish.

Use `Control/Command + C` to terminate the server and run `node index` to start the server again.

Looking Sharp! Right? All good...

## How to Create a Node Server With Express

In this section, we want to make our lives easier by using `Express` and `Nodemon` (node-mon or no-demon, pronounce it as you wish).

In the terminal, install the following:

```
npm install express --save 
npm install nodemon --save-dev
```

Create a new file named `app.js` or whatever suits you

In the file,

1. Require express like so:

`const express = require('express');`

2.   Assign the express method to a constant like this:

`const app = express();`

3.   Export the app constant to make it available for use in other files within the directory like so:

`module.exports = app;`

So we have:

```javascript
const express = require('express');

const app = express();



module.exports = app;

```

In the `index.js` file, require the `app` we exported a while ago:

`const app = require('./app');`

Next, set the port using the app like so:

`app.set('port', 3000);`

And replace the code in the `http.createServer()` method with just `app` like this:

`const server = http.createServer(app);`

This directs all API management to the `app.js` file helping with separation of concerns.

So our `index.js` file now looks like this:

```javascript
const http = require('http');
const app = require('./app');

app.set('port', 3000);
const server = http.createServer(app);

server.listen(3000);

```

Back in our `app.js` file, since we have directed all API management to it, let's create an endpoint to speak to us like before.

So before the `module.exports = app`, add the following code:

```javascript
app.use((request, response) => {
   response.json({ message: 'Hey! This is your server response!' }); 
});

```

We now have:

```javascript
const express = require('express');

const app = express();

app.use((request, response) => {
   response.json({ message: 'Hey! This is your server response!' }); 
});

module.exports = app;

```

Ahaaa... It's time to test our app.

To test our app, we now type `nodemon index` in our terminal and hit the `Enter` button. This is my terminal:

![Terminal running nodemon](https://dev-to-uploads.s3.amazonaws.com/i/1gy6psmeylb6onbbt18i.JPG)

Do you notice that nodemon gives us details of execution in the terminal unlike Node? That's the beauty of nodemon.

You can now go to `postman` or any `browser` and in the address bar, type `http://localhost:3000/` and hit `Enter`. See my output:

![Postman returning response from express app](https://dev-to-uploads.s3.amazonaws.com/i/m4yrqaf3d235xo7hjqae.JPG)

**Walah! It's working.**

Now more reasons to use nodemon. Go to the `app.js` file and change the `message` string to any string on your choice, save, and watch the `terminal`.

![nodemon restarting after changes](https://dev-to-uploads.s3.amazonaws.com/i/qcslu7vqa746nq5hvjwk.JPG)

Wow... It automatically restarts the server. This was impossible with Node. We had to restart the server ourselves.

## How to Secure the Server and Make it Future-Proof

In the `index.js` file, replace all the code with the following:

```javascript
const http = require('http');
const app = require('./app');

const normalizePort = val => {
  const port = parseInt(val, 10);

  if (isNaN(port)) {
    return val;
  }
  if (port >= 0) {
    return port;
  }
  return false;
};
const port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

const errorHandler = error => {
  if (error.syscall !== 'listen') {
    throw error;
  }
  const address = server.address();
  const bind = typeof address === 'string' ? 'pipe ' + address : 'port: ' + port;
  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges.');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use.');
      process.exit(1);
      break;
    default:
      throw error;
  }
};

const server = http.createServer(app);

server.on('error', errorHandler);
server.on('listening', () => {
  const address = server.address();
  const bind = typeof address === 'string' ? 'pipe ' + address : 'port ' + port;
  console.log('Listening on ' + bind);
});

server.listen(port);

```

`process.env.PORT` makes the app dynamic so that it can run any port assigned to it in the future when hosted on a live server.

The `normalizePort` function returns a valid port, whether it is provided as a number or a string.

The `errorHandler` function checks for various errors and handles them appropriately — it is then registered to the server.

A `listening` event listener is also registered, logging the port or named pipe on which the server is running to the console.

YooH! Our server is more secure and robust right now. Notice that nodemon also displays the port we are listening on.

There you have it, a simple, secure and robust Node.js server.

## How to Upload Images to Cloudinary 

Now that we have a cool server running, let's learn how we can save our images on Cloudinary. This will just be a basic introduction so it should be fun 😊.

[Cloudinary](https://cloudinary.com/) helps developers across the world manage images with minimal effort.

### How to Create a Cloudinary Account

To create an account, go to the [Cloudinary Website](https://cloudinary.com/).

1. Click the `sign up` button on the `top right`.
2. Fill the form that shows up accordingly.
3. Submit the form using the `Create Account` button.
4. Check your email to finish up by validating your email

You should be able to access your dashboard which looks like mine below:

![Cloudinary Dashboard](https://dev-to-uploads.s3.amazonaws.com/i/qfiw7cobdp7pv3c0fb65.JPG)

Notice the `Account details`. You **shouldn't reveal this information to anyone**. I am showing it to you here because this is a temporary account that I'm using only for the purposes of this tutorial.

Checkout the `Media Library` tab too. This is where the uploaded images will appear.

If you have all these showing, then let's rock and roll...

### How to Install Cloudinary in Our Project

Open your terminal and navigate into the project directory.

Execute the following command to install `Cloudinary`:

```javascript
  npm install cloudinary --save

```

### How to Setup Cloudinary in Our Project

In the app.js file, require `cloudinary` below the `const app = express();` like so:

```javascript
  const cloudinary = require('cloudinary').v2

```

Next, add the configuration details from the account details on your dashboard like this:

```javascript
    cloud_name: 'place your cloud_name here',
    api_key: 'place your api_key here',
    api_secret: 'place your api_secret here',

```

This is what I have:

```javascript
  // cloudinary configuration
  cloudinary.config({
    cloud_name: "dunksyqjj",
    api_key: "173989938887513",
    api_secret: "ZPLqvCzRu55MaM1rt-wxJCmkxqU"
  });

```

### How to Create an EndPoint to Upload an Image

To avoid bugs in our code, first replace the existing API with the following code:

```javascript
  app.get("/", (request, response) => {
    response.json({ message: "Hey! This is your server response!" });
  });

```

It is basically the same but this time, we are using the `get` verb in place of the `use` verb and we added a root end-point (`/`).

Next, just before the `module.exports = app;` line, we will be creating our `image-upload` API.

Let's start by placing this code there:

```javascript
// image upload API
app.post("/upload-image", (request, response) => {});

```

Basically, this is how we set up an API. The API makes a `POST` `request` to the `server` telling the `server` that the `request` should be handled with a degree of security. It uses two parameters to make this request: an `end-point` (/upload-image) and a `callback function` ((request, response) => {}).

Let's breathe life into the API by building out the `callback function`.

### How to Build the Callback Function

#### Install [body-parser](https://www.npmjs.com/package/body-parser)

This npm package enables us to handle incoming requests using `req.body` or `request.body` as the case may be. We will be installing `body-parser` using the following code:

```javascript
  npm install --save body-parser

```

#### Configure body-paser for our project

Require body-parse in the app.js like so:

```javascript
const bodyParser = require('body-parser');

```

Next, add the following code to set its `json` function as global middleware for our app like so:

```javascript
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

```

We can now handle our request body appropriately.

### Back to Building Our Function

In the function, add the following code to collect any data (images) entered by a user:

```javascript
    // collected image from a user
    const data = {
        image: request.body.image,
    };

```

Next, upload the image to `cloudinary` using the following code:

```javascript
cloudinary.uploader.upload(data.image);

```

Basically, this is all we need to upload our image. So our `app.js` looks like this:

```javascript
const express = require("express");
const app = express();
const cloudinary = require("cloudinary").v2;
const bodyParser = require('body-parser');

// body parser configuration
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// cloudinary configuration
cloudinary.config({
  cloud_name: "dunksyqjj",
  api_key: "173989938887513",
  api_secret: "ZPLqvCzRu55MaM1rt-wxJCmkxqU"
});

app.get("/", (request, response) => {
  response.json({ message: "Hey! This is your server response!" });
});

// image upload API
app.post("/image-upload", (request, response) => {
    // collected image from a user
    const data = {
      image: request.body.image,
    }

    // upload image here
    cloudinary.uploader.upload(data.image);
    
});

module.exports = app;

```

Now this looks good and it works perfectly. You can test it out using `postman`. But it's would be awesome if our app could give us feedback when it's done handling our requests, right?

To make this happen, we will add the following `then...catch...` block to the cloudinary upload like so:

```javascript
    // upload image here
    cloudinary.uploader.upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    }).catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });

```

So our final code will be:

```javascript
const express = require("express");
const app = express();
const cloudinary = require("cloudinary").v2;
const bodyParser = require('body-parser');

// body parser configuration
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// cloudinary configuration
cloudinary.config({
  cloud_name: "dunksyqjj",
  api_key: "173989938887513",
  api_secret: "ZPLqvCzRu55MaM1rt-wxJCmkxqU"
});

app.get("/", (request, response) => {
  response.json({ message: "Hey! This is your server response!" });
});

// image upload API
app.post("/image-upload", (request, response) => {
    // collected image from a user
    const data = {
      image: request.body.image,
    }

    // upload image here
    cloudinary.uploader.upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    }).catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });
    
});

module.exports = app;

```

### How to Test our API

Create a folder/directory in the root directory and name it `images` like so:

```javascript
  mkdir images

```

Copy an image of your choice to this folder. (Now, the path to your image relative to the app.js file should look like this: `"images/<your-image.jpg">`.)

Now let's proceed to `postman`.

1. In the address bar, enter this: `http://localhost:3000/image-upload`
2. Set the `Header` Key to `Content-Type` and value to `application/json`
3. Set the `body` to the `json` data we declared in our code like so:

```javascript
       {
	   "image": "images/oskar-yildiz-gy08FXeM2L4-unsplash.jpg"
       }

```

Hit the `Send` button and wait for the upload to complete and get your response:

![Postman setup to upload image](https://dev-to-uploads.s3.amazonaws.com/i/ate77jhmka2agj3nxip2.JPG)

Now, this is the result. The image now has a unique `public_id` which is randomly generated by Cloudinary and a `secure_url` which is globally accessible (you can load it in your browser to see).

![Postman showing result of upload](https://dev-to-uploads.s3.amazonaws.com/i/wys21hgc58nl4rfmq63i.JPG)

Finally, checking the `Media Library` tab on your Cloudinary dashboard, you should have a new image with a `new` badge on it. This will have a unique id that matches the `public_id` we saw in the postman result above just like in the image below:

![Cloudinary Media Files](https://dev-to-uploads.s3.amazonaws.com/i/vkvevngtumyfdd105suu.JPG)

Walah! We are persisting images without stress...That feels good.

Well, one more thing – SECURITY!

Our Cloudinary configuration details rea exposed in our app.js file. If we push our project to GitHub, it becomes publicly available to anyone who cares to check it out. And that becomes a problem if it gets into the wrong hands.

But don't worry about a thing here, there is a fix for almost everything in this space. We will be using the `dotenv` npm package to hid our configurations from the public.

## How to Secure Our Configurations with `dotenv`

First, you'll need to install [dotenv](https://www.npmjs.com/package/dotenv) if you haven't already:

```javascript
npm install dotenv --save

```

Then require `dotenv` in `app.js` like so:

```javascript
  require('dotenv').config()

```

Create a new file in the root directory and name it `.env`.

In the file, enter your Cloudinary configuration details like so:

```javascript
  CLOUD_NAME=dunksyqjj
  API_KEY=173989938887513
  API_SECRET=ZPLqvCzRu55MaM1rt-wxJCmkxqU

```

In the app.js file, we will access the configurations in the `.env` file via the `process.env` property like so:

```javascript
// cloudinary configuration
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET
});

```

This is my `app.js` code at the moment:

```javascript
const express = require("express");
const app = express();
const cloudinary = require("cloudinary").v2;
const bodyParser = require('body-parser');
require('dotenv').config()

// body parser configuration
app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

// cloudinary configuration
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET
});

app.get("/", (request, response, next) => {
  response.json({ message: "Hey! This is your server response!" });
  next();
});

// image upload API
app.post("/image-upload", (request, response) => {
    // collected image from a user
    const data = {
      image: request.body.image,
    }

    // upload image here
    cloudinary.uploader.upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    }).catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });
});

module.exports = app;

```

Let's test our app again to make sure that nothing is broken. Here is my result:

![Cloudinary media library](https://dev-to-uploads.s3.amazonaws.com/i/d3a2b47shxlmext6o40j.JPG)

I now have two of the same image but with different `public_id`s.

And that is it!

Yeeeh! Our application is more secure than it was when we started.

## Conclusion

In this tutorial, we went through the steps involved in creating a server using just Node.js. And after that, we improved our server using Express and nodemon.

Finally, we saw how to upload an image to Cloudinary through our Express application and how our configuration details are secured using the `dotenv` package.

This is just an introduction. You can do a whole lot more if you play around with this application.

You can find the server creation code [here](https://github.com/EBEREGIT/server-tutorial/tree/create-server).

And the image upload codes are available [here](https://github.com/EBEREGIT/server-tutorial/tree/cloudinary-upload).

Thank you for your time. 😊

