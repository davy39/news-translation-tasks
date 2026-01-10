---
title: How to build a serverless NodeJS microservice on AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-18T17:12:29.000Z'
originalURL: https://freecodecamp.org/news/building-a-nodejs-microservice-on-aws-lambda-6adb6da53cbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*foHs8AleRqNMimdXsK9hAA.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Paul Matthew Jaworski\nDEPRECATED\nUnfortunately, since I wrote this\
  \ article, v1.0 of the Serverless Framework has been released, along with some breaking\
  \ changes. I believe that you can migrate to the new version simply by adding:\n\
  \ integration: lam..."
---

By Paul Matthew Jaworski

### **DEPRECATED**

Unfortunately, since I wrote this article, v1.0 of the [Serverless Framework](https://serverless.com/) has been released, along with some breaking changes. I believe that you can migrate to the new version simply by adding:

```
 integration: lambda
```

to each of your resources. For example:

```
createPet:    handler: handler.create    events:      - http:          path: pets          method: POST          cors: true          integration: lambda
```

However, I have decided to move on from Serverless for now, mainly due to issues with authentication, authorization, and frustrations with DynamoDB, so I won’t be updating this post. I will explore these issues and my decision to switch back to a “traditional” REST API in a later story.

For now, I would recommend referencing [the official Serverless docs on API Gateway](https://serverless.com/framework/docs/providers/aws/events/apigateway/#api-gateway) to get started, and possibly using the rest of this post as a reference, bearing in mind that any information in the Serverless docs takes precedence over anything written here.

### Proceed from here with caution:

In this article, I’ll share my experience going “serverless” and building a CRUD API “microservice” using AWS Lambda, API Gateway, and DynamoDB. This will function as a guide for you to make your own microservices with these tools.

### **Getting Started**

I’m going to assume you have an AWS account and NodeJS installed. If not, handle that now.

Next you’ll need to install the Serverless npm package, which provides a way to easily create, edit, and deploy microservices as AWS Lambda functions:

```
npm install -g serverless
```

Then follow Amazon’s [instructions on creating an IAM user and configuring Serverless](https://github.com/serverless/serverless/blob/master/docs/02-providers/aws/01-setup.md) to use those credentials.

Navigate to the directory where you want to store your new project and run:

```
serverless create --template aws-nodejs --path pets-service
```

Now’s a good time to set up linting in your project. Since this is not an intro to ESLint, I won’t go into full detail, but I’d recommend installing that now and setting up your **.eslintrc** like this:

```
{  “plugins”: [“node”],  “extends”: [“eslint:recommended”, “plugin:node/recommended”],  “env”: {    “node”: true,    “mocha”: true  },  “rules”: {    “no-console”: 0,    “node/no-unsupported-features”: [2, {“version”: 4}]  }}
```

The important thing to note here is the “no-unsupported-features” rule from the node plugin. AWS Lambda uses Node v4.3, and knowing which ES6 features are available can be a pain in the ass. This makes it easy.

### **Creating the Handler**

Install the aws-sdk and lodash with npm:

```
npm i -S aws-sdk lodash
```

Now head over to **handler.js** and add those dependencies to the top of your file:

```
const aws = require(‘aws-sdk’);const _ = require(‘lodash/fp’);
```

Note that we’re using the “functional programming” variant of lodash because its merge function won’t mutate the original object.

Below that, set up your document client for communicating with DynamoDB:

```
const dynamo = new aws.DynamoDB.DocumentClient();
```

Now let’s make our **create()** function to make a new Pet in the database:

```
exports.create = function(event, context) {  const payload = {    TableName: 'Pets',    Item: event.body  };
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail(‘Error creating pet’);    } else {      console.log(data);      context.succeed(data);    }  }
```

```
  dynamo.put(payload, cb);};
```

It’s pretty easy to see what’s going on here for the most part:

We get an **event** object passed in with a key **body** that contains the data we want to store. The DocumentClient requires at minimum an object with the keys **TableName** and **Item** to be passed into put().

We also provide a callback that does two important things:

If there is an error, we run **context.fail()**, which is basically just an onError callback provided by AWS.

If the item creation is successful, we run **context.succeed()**, passing in the data to be returned as the result of our Lambda function.

An important caveat with DynamoDB is that we must provide the primary key ourselves on creation. In this case, we have to include **petId** as a key in our event.body object.

Why is such a basic feature missing from DynamoDB? Your guess is as good as mine.

I’m fortunate enough in my application to have a unique ID generated for me by Auth0, which I’m using for my auth/user management. You’ll have to solve this problem some other way if you’re not.

We’ll follow this same basic pattern for the rest of our CRUD operations:

```
exports.show = function(event, context) {  const payload = {    TableName: 'Pets',    Key: {      petId: event.params.path.petId    }  }
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error retrieving pet');    } else {      console.log(data);      context.done(null, data);    }  }
```

```
  dynamo.get(payload, cb);};
```

```
exports.list = function(event, context) { const payload = {  TableName: 'Pets' }
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error getting pets');    } else {      console.log(data);      context.done(null, data);    }  }
```

```
  dynamo.scan(payload, cb);}
```

```
exports.update = function(event, context) {  const payload = {    TableName: 'Pets',    Key: {      petId: event.params.path.petId    }  };
```

```
  dynamo.get(payload, (err, data) => {    if (err) {      console.log(err);      context.fail('No pet with that id exists.');    } else {      const item = _.merge(data.Item, event.body);      payload.Item = item;
```

```
      dynamo.put(payload, (putErr, putData) => {        if (putErr) {          console.log('Error updating pet.');          console.log(putErr);          context.fail('Error updating pet.');        } else {          console.log('Success!');          console.log(putData);          context.done(null, item);        }      });    }  });}
```

```
exports.delete = function(event, context) {  const payload = {    TableName: 'Pets',    Key: {      petId: event.params.path.petId    }  };
```

```
  const cb = (err, data) => {    if (err) {      console.log(err);      context.fail('Error retrieving pet');    } else {      console.log(data);      context.done(null, data);    }  }
```

```
  dynamo.delete(payload, cb);}
```

There are just a couple things to note here:

We want to be able to do partial updates, meaning you don’t need to send the entire Pet object with its changes, you can just send the changes. To accomplish this, we’re calling a **get** first in the **update()** function, then merging our changes into the result of that operation.

Our **petId** is passed in as a parameter to API Gateway and then provided to us in Lambda via event.params.path.petId. You could also use query strings if you prefer.

### **Configuring Serverless**

We’re almost done here, so now let’s get our Serverless config files set up. Open up **serverless.yml** and edit it to look like this:

```
service: pets-service
```

```
provider:  name: aws  runtime: nodejs4.3
```

```
defaults:  stage: dev  region: us-west-2
```

```
functions:  createPet:    handler: handler.create    events:      - http:          path: pets          method: POST  showPet:    handler: handler.show    events:      - http:          path: pets/{petId}          method: GET  listPets:    handler: handler.list    events:      - http:          path: pets          method: GET  updatePet:    handler: handler.update    events:      - http:          path: pets/{petId}          method: PUT  deletePet:    handler: handler.delete    events:      - http:          path: pets/{petId}          method: DELETE
```

This is pretty easy to understand, I think. We’re just specifying the names of our Lambda functions, then mapping them to our **handler.js** functions and the HTTP methods and paths we want them to respond to.

I’ve changed defaults to use ‘us-west-2’ as my region, and kept ‘dev’ as my stage. Setting up different stages with Serverless is not something I have fully explored.

The documentation is _very_ lacking right now, but this configuration will result in an API Gateway named “dev-pets-service” being created, even though that’s not really what we want.

API Gateways shouldn’t have the environment referenced in their name at all, since they can hold multiple environments or “stages.”

Hopefully I’ll find a fix for this and publish it in a future edit ;)

### **Deploying and Testing Our Service**

Now we’re ready to deploy! All it takes is running:

```
serverless deploy
```

In a minute or so, your Lambda functions should be deployed, and your API Gateway created.

Create a DynamoDB table named ‘Pets’ (or whatever you’re calling your resource). Then head to API Gateway. Find your ‘dev-pets-service’, and navigate to the POST method.

Test your API by clicking on the “TEST” button with the lightning bolt and using the following data:

```
{ petId: "029340", name: "Fido", type: "dog" }
```

You should have successfully created a new item in your database!

### **What’s Next?**

Your next steps might be enabling CORS for your resources, using a custom domain name for your API, and setting up your front end app to talk to these endpoints.

This is all beyond the scope of the article, and should be pretty simple, but let me know in the comments if you have questions.

**EDIT**

User jcready on Reddit has suggested an improvement to our update method:

```
exports.update = function(event, context) {  const payload = _.reduce(event.body, (memo, value, key) => {    memo.ExpressionAttributeNames[`#${key}`] = key    memo.ExpressionAttributeValues[`:${key}`] = value    memo.UpdateExpression.push(`#${key} = :${key}`)    return memo  }, {    TableName: 'Pets',    Key: { petId: event.params.path.petId },    UpdateExpression: [],    ExpressionAttributeNames: {},    ExpressionAttributeValues: {}  })  payload.UpdateExpression = 'SET ' + payload.UpdateExpression.join(', ')  dynamo.update(payload, context.done)}
```

The issue with our current implementation is that a user could overwrite another’s changes if two update requests are sent at once.

DocumentClient provides us with an **update** method that allows us to specify the fields we want to update, but the syntax is a little odd and requires generating an “UpdateExpression” to achieve these changes.

This code builds that expression based on the keys passed in and solves the problem of overwriting updates in an application where resources are shared between users.

