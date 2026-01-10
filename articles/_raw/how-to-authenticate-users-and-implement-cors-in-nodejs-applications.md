---
title: How to Authenticate Users and Implement CORS in Node.js Apps
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2021-07-06T16:02:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-authenticate-users-and-implement-cors-in-nodejs-applications
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-27-at-00.10.45.png
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: CORS
  slug: cors
- name: node
  slug: node
seo_title: null
seo_desc: 'In this tutorial, you will learn how to authenticate users and secure endpoints
  in Node.js. You''ll also see how to implement Cross-Origin Resource Sharing (CORS)
  in Node. So let''s get started.

  Prerequisites

  You''ll need the following to follow along w...'
---

In this tutorial, you will learn how to authenticate users and secure endpoints in Node.js. You'll also see how to implement Cross-Origin Resource Sharing (CORS) in Node. So let's get started.

### Prerequisites

You'll need the following to follow along with this tutorial: 
- A working understanding of JavaScript.
- A good understanding of Node.js.
- A working knowledge of MongoDB or another database of your choice.
- [Postman](https://www.postman.com/) and a basic understanding of how it works.

Before we jump into the main part of the article, let's define some terms so we're all on the same page.

## What is Authentication?

Authentication and authorization may seem like the same thing. But there's a big difference between getting into a house (authentication) and what you can do once you're there (authorization).

Authentication is the process of confirming a user's identity by obtaining credentials and using those credentials to validate their identity. If the certificates are valid, the authorization procedure begins.

You are probably already familiar with the authentication process, because we all go through it daily – whether at work (logging onto your computer) or at home (passwords or logging into a website). In fact, most "things" connected to the Internet require you to provide credentials to prove your identity.

## What is Authorization?

Authorization is the process of granting authenticated users access to resources by verifying whether they have system access permissions or not. It also allows you to restrict access privileges by granting or denying specific licenses to authenticated users.

After the system authenticates your identity, authorization occurs, providing you full access to resources such as information, files, databases, finances, locations, and anything else. 

This approval impacts your ability to access the system and the extent to which you can do so.

## What is Cross-Origin Resource Sharing (CORS)?

>[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is an HTTP header-based system that allows a server to specify any other origins (domain, scheme, or port) from which a browser should enable resources to be loaded other than its own. 

CORS also uses a system in which browsers send a "preflight" request to the server hosting the cross-origin help to ensure that it will allow the actual request.

We will be using the JSON web token standard to represent claims between two parties

## What are JSON Web Tokens (JWT)?

> JSON Web Tokens (JWT) are an open industry standard defined by RFC 7519 used to represent claims between two parties. [jwt.io](https://jwt.io/introduction) 

You can use [jwt.io](https://jwt.io) to decode, verify, and create JWTs, for example.

JWT defines a concise and self-contained way of exchanging information between two parties as a JSON object. You can review and trust this information because it is signed. 

JWTs can be signed with a secret (using the HMAC algorithm) or a public/private key pair from RSA or ECDSA. We'll see some examples of how to use them in a bit.

Let's get started.

## How to Use a Token for Authentication in Node.js Development 

To get started, first we'll need to set up our project.

Navigate to a directory of your choice on your machine and open it in the terminal to launch Visual Studio Code.

Then execute:

```bash
code.
```

> **Note**: If you don't have Visual Studio Code installed on your computer, `code .`  won't work. Just make sure you have it installed before trying this command.


### How to Create a Directory and Set it Up with `npm`

Create a directory and initialize `npm` by typing the following command:

- In Windows power shell:

```bash
mkdir cors-auth-project

cd cors-auth-project

npm init -y
```

- In Linux:

```bash
mkdir cors-auth-project

cd cors-auth-project

npm init -y
```

### How to Create Files and Directories

In the previous step, we initialized npm with the command `npm init -y`, which automatically created a package.json file.

We will create the `model`, `middleware`, and `config` directories and their files, for example, `user.js`, `auth.js`, `database.js` using the commands below.

```bash
mkdir model middleware config

touch config/database.js middleware/auth.js model/user.js
```

We can now create the `index.js` and `app.js` files in the root directory of our project with this command:

```bash
touch app.js index.js
```

This will give us a folder structure like the one you see below:

![folder structure](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-19.43.15.png)


### How to Install Dependencies

We'll install several dependencies like `mongoose`, `jsonwebtoken`, `express`, `dotenv`, `bcryptjs`, `cors` and development dependencies like `nodemon` to restart the server as we make changes automatically.

Because I'll be using MongoDB in this project, we'll install Mongoose, and the user credentials will be checked against what we have in our database. As a result, the entire authentication process isn't limited to the database we'll use in this tutorial.

```bash
npm install  cors mongoose express jsonwebtoken dotenv bcryptjs 

npm install nodemon -D
```

### How to Create a Node.js Server and Connect your Database

Now, add the following snippets to your `app.js`, `index.js`, `database.js`, and `.env` files in that order to establish our Node.js server and connect our database.

In our `database.js.`:

`config/database.js`:
```javascript
const mongoose = require("mongoose");

const { MONGO_URI } = process.env;

exports.connect = () => {
  // Connecting to the database
  mongoose
    .connect(MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      useCreateIndex: true,
      useFindAndModify: false,
    })
    .then(() => {
      console.log("Successfully connected to database");
    })
    .catch((error) => {
      console.log("database connection failed. exiting now...");
      console.error(error);
      process.exit(1);
    });
};
```

In our `app.js`:

`auth-cors-project/app.js`
```javascript
require("dotenv").config();
require("./config/database").connect();
const express = require("express");

const app = express();

app.use(express.json());

// Logic goes here

module.exports = app;
```

In our `index.js`:

`auth-cors-project/index.js`
```javascript
const http = require("http");
const app = require("./app");
const server = http.createServer(app);

const { API_PORT } = process.env;
const port = process.env.PORT || API_PORT;

// server listening 
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

Our file, as you can see, requires various environment variables. If you haven't already, create a new `.env` file and add your variables before running the application.

In our `.env.`:

```javascript
API_PORT=4001

MONGO_URI= // Your database URI
```

Edit the scripts object in our `package.json` to look like the one below to start our server.

```javascript
"scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  }
```

We successfully inserted the above snippet into the files `app.js`, `index.js`, and `database.js`. So, we started by creating our Node.js server in `index.js` and then imported the `app.js` file, which already had routes configured.

Then, in database.js, we used Mongoose to build a database connection.

`npm run dev` is the command to start our application.

As long as they haven't crashed, both the server and the database should be up and running.

### How to Create a User Model and Route

After registering for the first time, we'll establish our schema for the user details. Then, when logging in, we'll check them against the remembered credentials.

In the model folder, add the following snippet to `user.js`:

`model/user.js`

```javascript
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  first_name: { type: String, default: null },
  last_name: { type: String, default: null },
  email: { type: String, unique: true },
  password: { type: String },
  token: { type: String },
});

module.exports = mongoose.model("user", userSchema);
```

Now let's create the routes for `register` and `login`, respectively.

In `app.js` in the root directory, add the following snippet for the registration and login.

`app.js`
```javascript
// importing user context
const User = require("./model/user");

// Register
app.post("/register", (req, res) => {
// our register logic goes here...
});

// Login
app.post("/login", (req, res) => {
// our login logic goes here
});
```

### How to Implement Register and Login Functionality

We'll implement these two routes in our application. Before storing the credentials in our database, we'll use JWT to sign them and `bycrypt` to encrypt them.

We will: 
- Get user input from the `/register` route.
- Verify the user's input.
- Check to see if the user has already been created.
- Protect the user's password by encrypting it.
- Make a user account in our database.
- Finally, construct a JWT token that is signed.

Modify the `/register` route structure we created earlier to look as shown below:

`app.js`
```javascript
// ...

app.post("/register", async (req, res) => {

  // Our register logic starts here
   try {
    // Get user input
    const { firstName, lastName, email, password } = req.body;

    // Validate user input
    if (!(email && password && firstName && lastName)) {
      res.status(400).send("All input is required");
    }

    // check if user already exist
    // Validate if user exist in our database
    const oldUser = await User.findOne({ email });

    if (oldUser) {
      return res.status(409).send("User Already Exist. Please Login");
    }

    //Encrypt user password
    encryptedUserPassword = await bcrypt.hash(password, 10);

    // Create user in our database
    const user = await User.create({
      first_name: firstName,
      last_name: lastName,
      email: email.toLowerCase(), // sanitize
      password: encryptedUserPassword,
    });

    // Create token
    const token = jwt.sign(
      { user_id: user._id, email },
      process.env.TOKEN_KEY,
      {
        expiresIn: "5h",
      }
    );
    // save user token
    user.token = token;

    // return new user
    res.status(201).json(user);
  } catch (err) {
    console.log(err);
  }
  // Our register logic ends here
});

// ...
```

> **Note:** Update your `.env` file with a `TOKEN_KEY`, which can be a random string.

Using Postman to test the endpoint, we'll get the response shown below after successful registration.

![user registration](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-22.57.16.png)

We will: 
- Get user input for the `/login` route.
- Verify the user's input.
- Check to see if the user is genuine.
- Compare the user's password to the one we saved earlier in our database.
- Finally, construct a JWT token that is signed.

Make the `/login` route structure that we defined earlier look like this:

```javascript
// ...

app.post("/login", async (req, res) => {

  // Our login logic starts here
   try {
    // Get user input
    const { email, password } = req.body;

    // Validate user input
    if (!(email && password)) {
      res.status(400).send("All input is required");
    }
    // Validate if user exist in our database
    const user = await User.findOne({ email });

    if (user && (await bcrypt.compare(password, user.password))) {
      // Create token
      const token = jwt.sign(
        { user_id: user._id, email },
        process.env.TOKEN_KEY,
        {
          expiresIn: "5h",
        }
      );

      // save user token
      user.token = token;

      // user
      return res.status(200).json(user);
    }
    return res.status(400).send("Invalid Credentials");
    
  // Our login logic ends here
});

// ...
```

Using Postman to test, we'll get the response shown below after a successful login.

![user login](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-23.00.45.png)

### How to Create Middleware for Authentication

We can now create and login a user successfully. Now, we'll establish a route that requires a user token in the header, which will be the JWT token we created before.

Add the following snippet inside `auth.js`:

`middleware/auth.js`
```javascript
const jwt = require("jsonwebtoken");

const config = process.env;

const verifyToken = (req, res, next) => {
  const token =
    req.body.token || req.query.token || req.headers["x-access-token"];

  if (!token) {
    return res.status(403).send("A token is required for authentication");
  }
  try {
    const decoded = jwt.verify(token, config.TOKEN_KEY);
    req.user = decoded;
  } catch (err) {
    return res.status(401).send("Invalid Token");
  }
  return next();
};

module.exports = verifyToken;
```

To test the middleware, create the `/welcome` route and edit app.js with the following code:

`app.js`
```javascript
const auth = require("./middleware/auth");

app.post("/welcome", auth, (req, res) => {
  res.status(200).send("Welcome to FreeCodeCamp 🙌");
});
```

When we try to access the /welcome route we just built without sending a token in the header with the x-access-token key, we get the following response:

![failed response](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-23.09.13.png)

We can now re-test by adding a token in the header with the key x-access-token.

This is the response you'll get:

![success response](https://www.freecodecamp.org/news/content/images/2021/06/success-response.png)

## How to Implement Cross-Origin Resource Sharing (CORS)

[CORS](https://www.npmjs.com/package/cors) is a Node.js package that provides a Connect/Express middleware that you can. use to enable CORS with a variety of parameters.

1. It's easy to use (Enable All CORS Requests)

Adding the following snippet to `app.js` allows us to add CORS to our application and enable all CORS requests.

```
// ...

const cors = require("cors") //Newly added
const app = express();

app.use(cors()) // Newly added


app.use(express.json({ limit: "50mb" }));

// ...
```

2. You can enable CORS for a single route

Using the `/welcome` route as an example, you can activate CORS for a single route in your application by adding the following snippet in `app.js.`:

```
app.get('/welcome', cors(), auth, (req, res) => {
  res.status(200).send("Welcome to FreeCodeCamp 🙌 ");
});
```

3. How to configure CORS

We can set options in the CORS package by adding parameters to configure it, as shown below:

```
// ...

const corsOptions = {
  origin: 'http://example.com',
  optionsSuccessStatus: 200 // for some legacy browsers
}

app.get('/welcome', cors(corsOptions), auth, (req, res) => {
  res.status(200).send("Welcome to FreeCodeCamp 🙌 ");
});

// ...
```

You can check out [NPM CORS PACKAGE](https://www.npmjs.com/package/cors) to read more about Cross-Origin Resource Sharing.

You can [click here](https://github.com/Olanetsoft/auth-cors-demo) to check out the complete code on GitHub.

## Conclusion
In this article, we learned about JWT, authentication, authorization, and CORS. We also learned how to create an API in Node.js that uses a JWT token for authentication.

Thank you for reading!


