---
title: A crash course on securing Serverless APIs with JSON web tokens
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T22:56:20.000Z'
originalURL: https://freecodecamp.org/news/a-crash-course-on-securing-serverless-apis-with-json-web-tokens-ff657ab2f5a5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AxeOW_M6gdCts83RVl2aaQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Adnan Rahić

  What a mouthful of a title. Wouldn’t you agree? In this walkthrough you’ll learn
  about securing your Serverless endpoints with JSON web tokens.

  This will include a basic setup of a Serverless REST API with a few endpoints, and
  of cours...'
---

By Adnan Rahić

What a mouthful of a title. Wouldn’t you agree? In this walkthrough you’ll learn about securing your Serverless endpoints with JSON web tokens.

This will include a basic setup of a Serverless REST API with a few endpoints, and of course an **authorizer** function. This **authorizer** will act as the middleware for authorizing access to your resources.

During the creation process, we’ll use the [Serverless framework](https://serverless.com/) for simulating a development environment just like you’re used to. Wrapping up the guide we’ll also set up a monitoring tool called [Dashbird](https://dashbird.io/). It will allow us to simulate the debugging capabilities and overview of a regular Node.js application in a way that’s natural and easy to comprehend. It also has a [free tier](https://dashbird.io/pricing/) and doesn’t require a credit card to set up.

If anything I just mentioned above is new to you, don’t worry. I’ll explain it all below. Otherwise you can freshen up your knowledge by taking a look at these tutorials:

* [Securing Node.js RESTful APIs with JWT](https://medium.freecodecamp.org/securing-node-js-restful-apis-with-json-web-tokens-9f811a92bb52) — Authentication and Authorization explained.
* [A crash course on Serverless with Node.js](https://hackernoon.com/a-crash-course-on-serverless-with-node-js-632b37d58b44)— Serverless basics explained.
* [Building a Serverless REST API with Node.js and MongoDB](https://hackernoon.com/building-a-serverless-rest-api-with-node-js-and-mongodb-2e0ed0638f47) — Serverless REST APIs explained.

### TL;DR

Before jumping in head first, you can severely hurt my feelings and only read this TL;DR. Or, continue reading the whole article. ❤

* [**Creating the API**](https://medium.com/p/ff657ab2f5a5#2aa5)  
- [Adding a database](https://medium.com/p/ff657ab2f5a5#8132)  
- [Adding the functions](https://medium.com/p/ff657ab2f5a5#e344)  
- [Adding business logic for the users](https://medium.com/p/ff657ab2f5a5#5845)  
- [Adding the authentication](https://medium.com/p/ff657ab2f5a5#5663)  
- [Adding the authorization](https://medium.com/p/ff657ab2f5a5#40d6)
* [**Deployment**](https://medium.com/p/ff657ab2f5a5#52e1)
* [**Testing**](https://medium.com/p/ff657ab2f5a5#2e10)
* [**Monitoring**](https://medium.com/p/ff657ab2f5a5#6e91)

Ready? Let’s jump in!

### Creating the API

First of all, we need to set up the Serverless framework for our local development environment. This framework is the _de facto_ framework for all things related to Serverless architectures. Jump over to [their site](https://serverless.com/) and follow the instructions to set it up, or reference back to [the article I linked above](https://hackernoon.com/a-crash-course-on-serverless-with-node-js-632b37d58b44).

The installation process is incredibly simple. You set up an AWS management role in your AWS account, and link it to your installation of the Serverless framework. The actual installation process is just running one simple command.

Fire up a terminal window and run the command below.

```
$ npm install -g serverless
```

Moving on, once you have it installed, there’s only one more command to run in the terminal to get a boilerplate Serverless service on your local development machine.

```
$ sls create -t aws-nodejs -p api-with-auth
```

The command above will generate the boilerplate code you need.

Change to the newly created directory called `api-with-auth` and open it up with your code editor of choice.

```
$ cd api-with-auth
```

Once open, you’ll see two main files. A `handler.js` and a `serverless.yml` file. The `handler.js` contains our app logic while the `serverless.yml` defines our resources.

Now it’s time to install some dependencies in order to set up our needed authentication/authorization methods, password encryption and ORM for the database interaction.

```
$ npm init -y$ npm install --save bcryptjs bcryptjs-then jsonwebtoken mongoose
```

There’s what we need for production, but for development we’ll grab the Serverless Offline plugin.

```
$ npm install --save-dev serverless-offline
```

Lovely!

#### Adding a database

For the persistent data store, we’ll just grab a hosted MongoDB instance on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). [Here’s](https://hackernoon.com/building-a-serverless-rest-api-with-node-js-and-mongodb-2e0ed0638f47) a reference for an article where I explained it in detail.

In the root of the service folder let’s create a `db.js` file to keep our logic for the database connection. Go ahead and paste in this snippet of code.

This is a rather simple implementation of establishing a database connection if no connection exists. But, if it exists, I’ll use the already established connection. You see the `process.env.DB`? We'll use a custom `secrets.json` file to keep our private keys out of GitHub by adding it to the `.gitignore`. This file will then be loaded in the `serverless.yml`. Actually, let's do that now.

Add your MongoDB connection string to the `db` field.

With this file created, let’s move on to the `serverless.yml`. Open it up and delete all the boilerplate code so we can start fresh. Then, go ahead and paste this in.

As you can see, it’s just a simple setup configuration. The `custom` section tells the main configuration to grab values from a `secrets.json` file. We'll add that file to the `.gitignore` because pushing private keys to GitHub is a mortal sin punishable by death! Not really, but still, don't push keys to GitHub. Seriously, please don't.

#### Adding the functions

Just a tiny bit of configuring left to do before jumping into the business logic! We need to add the function definitions in the `serverless.yml` right below the providers section we added above.

There are a total of five functions.

* The `VerifyToken.js` will contain an `.auth` method for checking the validity of the JWT passed along with the request to the server. This will be our **authorizer** function. The concept of how an authorizer works is much like how a middleware works in plain old basic Express.js. Just a step between the server receiving the request and handling data to be sent back to the client.
* The `login` and `register` functions will do the basic user authentication. We'll add business logic for those in the `AuthHandler.js` file.
* However, the `me` function will respond with the current authenticated user based on the provided JWT token. Here's where we'll use the **authorizer** function.
* The `getUsers` function is just a generic public API for fetching registered users from the database.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OkT0fGBzGM7Ig6ZkAkdwSw.png)

From the `serverless.yml` file above you can make out a rough project structure. To make it clearer, take a look at the image above.

Makes a bit more sense now? Moving on, let’s add the logic for fetching users.

#### Adding business logic for the users

Back in your code editor, delete the `handler.js` file and create a new folder, naming it `user`. Here you'll add a `User.js` file for the model, and a `UserHandler.js` for the actual logic.

Pretty straightforward if you’ve written a Node app before. We require Mongoose, create the schema, add it to Mongoose as a model, finally exporting it for use in the rest of the app.

Once the model is done, it’s time to add basic logic.

This is a bit tricky to figure out when you see it for the first time. But let’s start from the top.

By requiring the `db.js` we have access to the database connection on MongoDB Atlas. With our custom logic for checking the connection, we've made sure not to create a new connection once one has been established.

The `getUsers` helper function will only fetch all the users, while the `module.exports.getUsers` Lambda function will connect to the database, run the helper function, and return the response back to the client. This is more than enough for the `UserHandler.js`. The real fun starts with the `AuthProvider.js`.

#### Adding the authentication

In the root of your service, create a new folder called `auth`. Add a new file called `AuthHandler.js`. This handler will contain the core authentication logic for our API. Without wasting any more time, go ahead and paste this snippet into the file. This logic will enable user registration, saving the user to the database and returning a JWT token to the client for storing in future requests.

First we require the dependencies, and add the `module.exports.register` function. It's pretty straightforward. We're once again connecting to the database, registering the user and sending back a session object which will contain a JWT token. Take a closer look at the local `register()` function, because we haven't declared it yet. Bare with me a few more seconds, we’ll get to it in a moment.

With the core structure set up properly, let’s begin with adding the helpers. In the same `AuthHandler.js` file go ahead and paste this in as well.

We’ve created three helper functions for signing a JWT token, validating user input, and creating a user if they do not already exist in our database. Lovely!

With the `register()` function completed, we still have to add the `login()`. Add the `module.exports.login` just below the functions comment.

Once again we have a local function, this time named `login()`. Let's add that as well under the helpers comment.

Awesome! We’ve added the helpers as well. With that, we’ve added **authentication** to our API. As easy as that. Now we have a token-based authentication model with the possibility of adding authorization. That’ll be our next step. Hang on!

#### Adding the authorization

With the addition of a `VerifyToken.js` file, we can house all the authorization logic as a separate middleware. Very handy if we want to keep separation of concerns. Go ahead and create a new file called `VerifyToken.js` in the `auth` folder.

We have a single function exported out of the file, called `module.exporst.auth` with the usual three parameters. This function will act as a **middleware**. If you're familiar with Node.js you'll know what a middleware is, otherwise, check [this](https://medium.freecodecamp.org/securing-node-js-restful-apis-with-json-web-tokens-9f811a92bb52) out for a more detailed explanation.

The `authorizationToken`, our JWT, will be passed to the middleware through the event. We're just assigning it to a local constant for easier access.

All the logic here is just to check whether the token is valid and send back a generated policy by calling the `generatePolicy` function. This function is required by AWS, and you can grab it from various docs on AWS and from the Serverless Framework [examples GitHub page](https://github.com/serverless/examples/blob/master/aws-node-auth0-custom-authorizers-api/handler.js).

It’s important because we pass along the `decoded.id` along in the `callback`. Meaning, the next Lambda Function which sits behind our `VerifyToken.auth` **authorizer** function will have access to the `decoded.id` in its `event` parameter. Awesome, right!?

Once we have the token verification completed, all that’s left if to add a route to sit behind the **authorizer** function. For the sake of simplicity, let’s add a `/me` route to grab the currently logged user based on the JWT passed along the `GET` request.

Jump back to the `AuthHandler.js` file and paste this in.

Awesome! The last Lambda Function we’ll add in this tutorial will be `module.exports.me`. It'll just grab the `userId` passed from the **authorizer** and call the `me` helper function while passing in the `userId`. The `me` function will grab the user from the database and return it back. All the `module.exports.me` Lambda does is just retrieves the currently authenticated user. But, the endpoint is protected, meaning only a valid token can access it.

Great work following along so far, let’s deploy it so we can do some testing.

### Deployment

Hopefully, you’ve configured your AWS account to work with the Serverless Framework. If you have, there’s only one command to run, and you’re set.

```
$ sls deploy
```

Voila! Wait for it to deploy, and start enjoying your Serverless API with JWT authentication and authorization.

You’ll get a set of endpoints sent back to you in the terminal once the functions have been deployed. We’ll be needing those in the next section.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hexa4mq9xD91AfZCelMbVw.png)

### Testing

The last step in any development process should ideally be making sure it all works like it should. This is no exception. One of the two tools I use for testing my endpoints is [Insomnia](https://insomnia.rest/). So, I’ll go ahead and open it up. But, you can use [Postman](https://www.getpostman.com/), or any other tool you like.

**_Note_**_: If you want to start by testing everything locally, be my guest. You can always use [serverless-offline](https://www.freecodecamp.org/news/a-crash-course-on-securing-serverless-apis-with-json-web-tokens-ff657ab2f5a5/%20add%20link)._

In your terminal, run a simple command:

```
$ sls offline start --skipCacheInvalidation
```

But I like to go hardcore! Let’s test directly on the deployed endpoints.

Starting slow, first hit the `/register` endpoint with a `POST` request. Make sure to send the payload as JSON. Hit **Send** and you'll get a token back! Nice, just what we wanted.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zbCWN9qyIt0_8kWXwjszGQ.png)

Copy the token and now hit the `/me` endpoint with a `GET` request. Don't forget to add the token in the headers with the `Authorization` key.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n5QxngulaY-QFfGNUtgm8g.png)

You’ll get the current user sent back to you. And there it is. Lovely.

Just to make sure the other endpoints work as well, go ahead and hit the `/login` endpoint with the same credentials as with the `/register` endpoint you hit just recently.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vcc8I4KgAPw-O015G7_ySw.png)

Does it work? Of course it does. There we have it, a fully functional authentication and authorization system implemented in a Serverless environment with **JWT** and **Authorizers**. All that’s left is to add a way to monitor everything.

### Monitoring

I usually monitor my Lambdas with [Dashbird](https://www.dashbird.io/). It’s been working great for me so far. My point for showing you this is for you too see the console logs from the Lambda Function invocations. They’ll show you when the Lambda is using a new or existing database connection. Here’s what the main dashboard looks like, where I see all my Lambdas and their stats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pMkJIIgerPBAeq9sf8T0Tg.png)

Pressing on one of the Lambda Functions, let’s say **register**, you’ll see the logs for that particular function. The bottom will show a list of invocations for the function. You can even see which were crashes and cold starts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-yTb5eKa_Uj-X7nfPieLMw.png)

Pressing on the cold start invocation will take you to the invocation page and you’ll see a nice log which says `=> using new database connect`ion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*unMBkIOwUIOv0EZvVYWr-Q.png)

Now backtrack a bit, and pick one of the invocations which is not a cold start. Checking the logs for this invocation will show you `=> using existing database connect`ion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p5WdW_FEKohXcAtKEVfXcA.png)

Nice! You have proper insight into your system!

### Wrapping up

Amazing what you can do with a few nice tools. Creating a REST API with authentication and authorization is made simple with [Serverless](# runtime: nodejs6.10), JWT, MongoDB, and [Dashbird](https://dashbird.io). Much of the approach to this tutorial was inspired by some of my previous tutorials. Feel free to check them out below.

[**Adnan Rahić - Medium**](https://medium.com/@adnanrahic)  
[_Read writing from Adnan Rahić on Medium. Co-founder @bookvar_co. Teacher @ACADEMY387. Author @PacktPub. Campsite leader…_medium.com](https://medium.com/@adnanrahic)

The approach of using **authorizers** to simulate middleware functions is incredibly powerful for securing your Serverless APIs. It’s a technique I use on a daily basis. Hopefully you’ll find it of use in your future endeavors as well!

If you want to take a look at all the code we wrote above, [here’s the repository](https://github.com/adnanrahic/a-crash-course-on-serverless-auth). Or if you want to dig deeper into the lovely world of Serverless, have a look at all the tools I mentioned above, or check out [a course I authored](https://www.packtpub.com/web-development/serverless-javascript-example-video).

_Hope you guys and girls enjoyed reading this as much as I enjoyed writing it._ _Do you think this tutorial will be of help to someone? Do not hesitate to share. If you liked it, smash the_ **clap** _below so other people will see this here on Medium._

