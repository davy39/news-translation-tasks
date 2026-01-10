---
title: Learn how to handle authentication with Node using Passport.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T17:44:27.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-handle-authentication-with-node-using-passport-js-4a56ed18e81e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OUk_mC8ojHhStMEURjbI8g.jpeg
tags: []
seo_title: null
seo_desc: 'By Antonio Erdeljac

  Support me by reading it from its original source: ORIGINAL SOURCE

  In this article you will learn how to handle authentication for your Node server
  using Passport.js. This article does not cover Frontend authentication. Use this
  t...'
---

By Antonio Erdeljac

Support me by reading it from its original source: [**ORIGINAL SOURCE**](https://www.signet.hr/learn-how-to-handle-authentication-with-node-using-passport-js/)

In this article you will learn how to handle **authentication** for your Node server using **Passport.js.** This article **does not cover Frontend authentication.** Use this to configure your **Backend authentication** (Generate token for each user & protect routes).

Keep in mind that **if you get stuck on any step, you can refer to this [GitHub repo](https://github.com/AntonioErdeljac/passport-tutorial)**.

### In this article I will teach you the following:

* Handling protected routes
* Handling JWT tokens
* Handling unauthorised responses
* Creating a basic API
* Creating models & schemas

### Introduction

#### What is Passport.js?

Passport is authentication middleware for [Node.js](https://nodejs.org/). As it’s extremely flexible and modular, Passport can be unobtrusively dropped into any [Express](https://expressjs.com/)-based web application. A comprehensive set of strategies supports authentication using a [username and password](http://www.passportjs.org/docs/username-password/), [Facebook](http://www.passportjs.org/docs/facebook/), [Twitter](http://www.passportjs.org/docs/twitter/), and [more](http://www.passportjs.org/packages/). Find out more about Passport [here](http://www.passportjs.org/).

### Tutorial

#### Creating our node server from scratch

Create a new directory with this “app.js” file inside:

<script src="https://gist.github.com/AntonioErdeljac/3fada52d3c4efa8ef5cd04408bebaee0.js"></script>

We will install [nodemon](https://github.com/JakRowan/nodenom/blob/master/package.json) for easier development.

<script src="https://gist.github.com/AntonioErdeljac/bdfca5e9df272ff71db047d5ed7e3f96.js"></script>

and then we will run our “app.js” with it.

```bash
$ nodemon app.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*6kdVzksHWBymrCL20pNyzA.png)
_Expected result after running the command above_

#### Creating the user model

Create a new folder called “models”, and create the “Users.js” file inside that folder. This is where we will define our “UsersSchema”. We are going to use `JWT` and `Crypto` to generate `hash` and `salt` from the received `password` string. This will later be used to validate the user.

<script src="https://gist.github.com/AntonioErdeljac/d4b1611e8ce92943c067b3a6ab51154b.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*updLloBs1oJyVGplMGG4lQ.png)
_You should now have this structure_

Let’s add our newly created model to “app.js”.

Add the following line to your “app.js” file after configuring `Mongoose`:

```js
require('./models/Users');
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*YDxu9Xcr1SqDjQLzTVI9MA.png)

#### Configure Passport

Create a new folder “config” with the “passport.js” file inside it:

<script src="https://gist.github.com/AntonioErdeljac/3baa23e152bbc068eebd730e05918eca.js"></script>

In this file, we use the method `validatePassword` that we defined in the `User model` . Based on the result, we return a different output from Passport’s `LocalStrategy`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TxTXHZEmeZoEff1TeW9hDA.png)
_You should now have this structure_

Let’s connect “passport.js” to our “app.js” file. Add the following line **below all** `models`:

```js
require('./config/passport');
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Uem3m6YuPSnhx9DZsJ5sA.png)
_The Passport require must be below all models_

#### Routes and authentication options

Create a new folder called “routes” with the file “auth.js” inside it.

In this file we use the function `getTokenFromHeaders` to get a **JWT token** that will be sent from the **client side** in the **request’s headers**. We also create an `auth` object with `optional` and `required` properties. We will use these later in our routes.

<script src="https://gist.github.com/AntonioErdeljac/e78af14bb27bb63ebdd1ab9fb8e29bd5.js"></script>

In the same “routes” folder create an “index.js” file:

<script src="https://gist.github.com/AntonioErdeljac/b83682d7192df9c4ceb7026cedee2610.js"></script>

We now need an “api” folder inside the “routes” folder, with another “index.js” file inside it.

<script src="https://gist.github.com/AntonioErdeljac/158effaaeb527f6d756cf3178a48b5c4.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*xT-bMD4RPNbS0trhqltHQQ.png)
_You should now have this structure_

Now, let’s create the “users.js” file that we require in “api/index.js”.

First, we are going to create an **optional auth** route `‘/’` which will be used for new model creation (register).

```js
router.post('/', auth.optional, (req, res, next) ...
```

After that, we are going to create another **optional auth** route `‘/login’` . This will be used to activate our passport configuration and validate a received password with email.

```js
router.post('/login', auth.optional, (req, res, next) ...
```

Lastly, we will create a **required auth** route, which will be used to return the currently logged in user. Only logged in users (users that have their token successfully sent through request’s headers) have access to this route.

```js
router.get('/current', auth.required, (req, res, next) ...
```

<script src="https://gist.github.com/AntonioErdeljac/c787327eab1c1bb4e216fabe0fb9d8c3.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*FhlHO36q_NTY73Qhw2Vfiw.png)
_You should now have this structure_

Let’s add our “routes” folder to “app.js”. Add the following line **below our passport** `require`:

```js
app.use(require('./routes'));
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*B44dNEd8f0Ii5GDkNJ0fLQ.png)

### Route testing

I will be using [Postman](https://www.getpostman.com/) to send requests to our server.

Our server accepts the following body:

```json
{
  "user": {
    "email": String,
    "password": String
  }
}
```

#### Creating a POST request to create a user

Test body:

![Image](https://cdn-media-1.freecodecamp.org/images/1*e_U1SfVcGty_8XAZ8gWuSQ.png)

Response:

```json
{
    "user": {
        "_id": "5b0f38772c46910f16a058c5",
        "email": "erdeljac.antonio@gmail.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVyZGVsamFjLmFudG9uaW9AZ21haWwuY29tIiwiaWQiOiI1YjBmMzg3NzJjNDY5MTBmMTZhMDU4YzUiLCJleHAiOjE1MzI5MDgxNTEsImlhdCI6MTUyNzcyNDE1MX0.4TWc1TzY6zToHx_O1Dl2I9Hf9krFTqPkNLHI5U9rn8c"
    }
}
```

We will now use this token and add it to our “Headers” in Postman’s configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3TqFAWgy1bULj-ECJRyKKw.png)

And now let’s test our **auth only** route.

#### Creating a **GET request to return the currently logged in user**

Request URL:

```
GET http://localhost:8000/api/users/current
```

Response:

```json
{
    "user": {
        "_id": "5b0f38772c46910f16a058c5",
        "email": "erdeljac.antonio@gmail.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVyZGVsamFjLmFudG9uaW9AZ21haWwuY29tIiwiaWQiOiI1YjBmMzg3NzJjNDY5MTBmMTZhMDU4YzUiLCJleHAiOjE1MzI5MDgzMTgsImlhdCI6MTUyNzcyNDMxOH0.5UnA2mpS-_puPwwxZEb4VxRGFHX6qJ_Fn3pytgGaJT0"
    }
}
```

Let’s try to do it **without token in “Headers”.**

Response:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ggNxOl_DMzg6dklIJAKG3g.png)

### The end

Thank you for going through this tutorial. If you notice any errors please report them to me. **If you got stuck on any step,** please refer to [this GitHub repo](https://github.com/AntonioErdeljac/passport-tutorial).

**You can contact me through:**

* erdeljac DOT antonio AT gmail.com
* [Linkedin](https://www.linkedin.com/in/antonio-erdeljac/)

**Check out my app [SwipeFeed](https://play.google.com/store/apps/details?id=com.swipefeed.android).**

