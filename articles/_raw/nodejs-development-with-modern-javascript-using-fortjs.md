---
title: Node.js Development with modern JavaScript using FortJs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T02:37:44.000Z'
originalURL: https://freecodecamp.org/news/nodejs-development-with-modern-javascript-using-fortjs
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-20-36-31-1.png
tags:
- name: dependency injection
  slug: dependency-injection
- name: ES6
  slug: es6
- name: Node.js
  slug: nodejs
- name: REST
  slug: rest
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Ujjwal Gupta

  Introduction

  Nodejs gives you the power to write server side code using JavaScript. In fact,
  it is very easy and fast to create a web server using Nodejs. There are several
  frameworks available on Node package manager which makes the ...'
---

By Ujjwal Gupta

## Introduction

  
Nodejs gives you the power to write server side code using JavaScript. In fact, it is very easy and fast to create a web server using Nodejs. There are several frameworks available on Node package manager which makes the development even easier and faster.

But there are a few challenges in Nodejs development:

* Nodejs is all about callbacks, and with more and more callbacks you end up with a situation called callback hell.
* Writing readable code.
* Writing maintainable code.
* You don't get much intellisense support which makes development slow.

If you are quite experienced and have a good knowledge of Nodejs, you can use different techniques and try to minimize these challenges.

The best way to solve these problems is by using modern JavaScript ES6, ES7 or TypeScript, whatever you feel comfortable with. I recommend TypeScript, because it provides intillisense support for every word of code which makes your development faster.

So I created a framework called [FortJs](http://fortjs.info/) which is very easy to learn and use. FortJs enables you to write server-side code using ES6 or TypeScript which is modular, secure, and pretty much just beautiful and readable.

## Features

  
Some of the important features of FortJs are:  

* Based on [Fort](https://github.com/ujjwalguptaofficial/fort) architecture. 
* MVC Framework and follows OOPS approach so everything is class and object.
* Provides components - Wall, Shield and Guard. Components help modularize the application.
* Uses ES6 async/await or promise for executing asychronous code.
* Everything is configurable - you can configure your session store, view engine, websocket etc.
* Dependency Injection.
* Everything can be unit tested, so you can use a [TDD](https://guide.freecodecamp.org/agile/test-driven-development/) approach.

## Let's Code

  
In this article I am going to create a REST API using FortJs and ES6. But you can use the same code and steps to implement using TypeScript too.

### Project Setup

  
FortJs provides a CLI - fort-creator. This helps you set up the project and develop faster. Let's use the CLI to develop.

 Perform the below steps sequentially:

* Open your terminal or command prompt.
* Install **fort-creator** globally - run the command "npm i fort-creator -g". Note: Make sure you have Nodejs installed in your system.
* Create a new project - run the command "fort-creator new my-app". Here “my-app” is the name of the app, so you can choose any name. The CLI will prompt you to choose the language with two options: TypeScript and JavaScript. Choose your language by using the arrow keys and press enter - i have chosen JavaScript. It will take some time to create the project, so please wait until you see "new project my-app created".
* Enter into the project directory - "cd my-app".  
Start the development server with live reloading - run the command "fort-creator start".
* Open the browser and type the URL - [http://localhost:4000/](http://localhost:4000/).  


You should see something like this in the browser.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-20-36-31.png)
_FortJs starter page_

Let's understand how this page is rendered:

* Open the project folder in your favourite code editor. I am going to use VS Code. You will see many folders inside project root such as controllers, views, etc. Every folder is grouped by their use - for example, the controllers folder contains all controllers and the views folder contains all views.
* Open the controllers folder -> Inside the controllers, you will see a file name - default_controller. Let's open it and observe the code. The file contains a class DefaultController - this is a [controller](http://fortjs.info/tutorial/controller/) class and it contains methods which return some http response.
* Inside the class DefaultController, you will see a method 'index' - this is the one which is rendering current output to the browser. The method is known as [worker](http://fortjs.info/tutorial/worker/) in FortJs because they do some kind of work and return the result as an http response. Let's observe the index method code:  
  
```  
const data = {  
    title: title  
}  
const result = await viewResult('default/index.html', data);  
return result;  
```  
It creates a data object and passes that object into the **viewResult** method. The **viewResult** method takes two parameters - the view location and view data. The work of **viewResult** is to render the view and return a response, which we are seeing in the browser.
* Let's find the view code and understand it. Open the views folder - > open default folder - > open index.html. This is our view code. It is simple HTML code along with some mustache syntax. The default view engine for Fortjs is mustache.

I hope you have understood the project architecture. If you are having any difficulties or doubts, please feel free to ask in the comments section.

Now we will move to next part of this article where we will learn how to create a simple rest API.

## REST

We are going to create a REST endpoint for entity user - which will perform CRUD operations for the user such as adding a user, deleting a user, getting a user, and updating a user.

According to REST:

1. Adding user - should be done using the http method "`POST`"
2. Deleting user - should be done using the http method "`REMOVE`"
3. Getting user - should be done using the http method "`GET`"
4. Updating user - should be done using the http method "`PUT`"

For creating an endpoint, we need to create a Controller similar to the default controller explained earlier.

Execute the command  "`fort-creator add`". It will ask you to "Choose the component to add ?" Choose Controller & press **enter**. Enter the controller name "User" and press **enter**.

Now that we have created the user controller we need to inform FortJs by adding it to routes. The route is used to map our controller to a path.

Since our entity is user, "`/user`" will be a good route. Let's add it. Open routes.js inside the root directory of the project and add `UserController` to routes.

After adding UserController, routes.js will look like this:

```javascript
import { DefaultController } from "./controllers/default_controller";
import { UserController } from "./controllers/user_controller";

export const routes = [{
    path: "/*",
    controller: DefaultController
},
{
    path: "/user",
    controller: UserController
}]
```

So when an http request has the path "/user" then UserController will be called. 

Let's open the url - [http://localhost:4000/user](http://localhost:4000/user).

Note: If you have stopped FortJs while adding the controller, please start it again by running the cmd - `fort-creator start`

And you see a white page right?

This is because we are not returning anything from the index method and thus we get a blank response. Let's return a text "Hello World" from the index method. Add the below code inside the index method and save:

```javascript
return textResult('Hello World');
```

Refresh the url - [http://localhost:4000/user](http://localhost:4000/user)

And you see "Hello World" right?

Now, let's convert "UserController" to a REST API. But before writing code for the REST API, let's create a dummy service which will do CRUD operations for users.

### Service

Create a folder called “services” and then a file “user_service.js” inside the folder. Paste the below code inside the file:

```javascript
const store = {
    users: [{
        id: 1,
        name: "ujjwal",
        address: "Bangalore India",
        emailId: "ujjwal@mg.com",
        gender: "male",
        password: "admin"
    }]
}

export class UserService {
    getUsers() {
        return store.users;
    }

    addUser(user) {
        const lastUser = store.users[store.users.length - 1];
        user.id = lastUser == null ? 1 : lastUser.id + 1;
        store.users.push(user);
        return user;
    }

    updateUser(user) {
        const existingUser = store.users.find(qry => qry.id === user.id);
        if (existingUser != null) {
            existingUser.name = user.name;
            existingUser.address = user.address;
            existingUser.gender = user.gender;
            existingUser.emailId = user.emailId;
            return true;
        }
        return false;
    }

    getUser(id) {
        return store.users.find(user => user.id === id);
    }

    removeUser(id) {
        const index = store.users.findIndex(user => user.id === id);
        store.users.splice(index, 1);
    }
}
```

The above code contains a variable store which contains a collection of users. The method inside the service does operations like add, update, delete, and get on that store.

We will use this service in REST API implementation.

### GET

For the route "/user" with the http method "GET", the API should return a list of all users. 

In order to implement this, let's rename the "index" method inside user_controller.js to "getUsers" making it semantically correct. Then paste the below code inside the method:

```javascript
const service = new UserService();
return jsonResult(service.getUsers());
```

Now user_controller.js looks like this:

```javascript

import { Controller, DefaultWorker, Worker, textResult, jsonResult } from "fortjs";
import { UserService } from "../services/user_service";

export class UserController extends Controller {

    @DefaultWorker()
    async getUsers() {
        const service = new UserService();
        return jsonResult(service.getUsers());
    }
}
```

Here, we are using the decorator DefaultWorker. The DefaultWorker does two things: it adds the route "/" & the http method "GET". It's a shortcut for this scenario. In the next part, we will use other decorators to customize the route.

Let's test this by calling the url [http://localhost:4000/user](http://localhost:4000/user). You can open this in the browser or use any http client tools like postman or curl. 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-21-53-59.png)

Ok, so we have successfully created an end point :) .

Let's look again at our code and see if we can make it better: 

1. The service "UserService" is tightly coupled with Controller "UserController" which becomes a problem for unit testing "UserController". So we will use [dependency injection](http://fortjs.info/tutorial/dependency-injection/) by FortJs to inject UserService.
2. We are creating an instance of "UserService" every time the method getUsers is called. But what we need from "UserService" is a single object and then call the "UserService" method from the object. 

So if we can somehow store an object of "UserService" then we can make our code faster (because calling new does some work under the hood). For this we will use the singleton feature of FortJs.

Let's change the user_controller.js code by the below code: 

```javascript

import { Controller, DefaultWorker, Worker, textResult, jsonResult, Singleton } from "fortjs";
import { UserService } from "../services/user_service";

export class UserController extends Controller {

    @DefaultWorker()
    async getUsers(@Singleton(UserService) service) {
        return jsonResult(service.getUsers());
    }
}
```

As you can see, the only change is that we are using the "Singleton" decorator in the method getUsers. This will create a singleton and inject that singleton when getUsers is called. This singleton will be available throughout the application.

Since service is now a parameter, we can manually pass the parameter while calling. This makes getUsers unit testable.

For doing unit testing or E2E testing, please read this test doc - [http://fortjs.info/tutorial/test/](http://fortjs.info/tutorial/test/)

### POST

Let's add a method "addUser" which will extract data from the request body and call service to add a user.

```javascript
async addUser(@Singleton(UserService) service) {
        const user = {
            name: this.body.name,
            gender: this.body.gender,
            address: this.body.address,
            emailId: this.body.emailId,
            password: this.body.password
        };
        const newUser = service.addUser(user);
        return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

> In the above code we are creating the Singleton of the UserService again. So the question is will it create another object?

No it will be same object that was in getUser. FortJs supplies the object as a parameter when it calls the method.

The methods created are by default not visible for an http request. So in order to make this method visible for the http request, we need to mark this as a worker. 

A method is marked as a worker by adding the decorator "Worker". The Worker decorator takes a list of http methods and makes that method available for only those http methods. So let's add the decorator:

```javascript
@Worker([HTTP_METHOD.Post])
async addUser(@Singleton(UserService) service) {
    const user = {
        name: this.body.name,
        gender: this.body.gender,
        address: this.body.address,
        emailId: this.body.emailId,
        password: this.body.password
    };
    const newUser = service.addUser(user);
    return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

Now the route of this method is the same as the name of the method that is "addUser". You can check this by sending a post request to [http://localhost:4000/user/addUser](http://localhost:4000/user/addUser) with user data in the body.

But we want the route to be "/", so that it will be a rest API. The route of the worker is configured by using the decorator "Route". Let's change the route now.

```
@Worker([HTTP_METHOD.Post])
@Route("/")
async addUser(@Singleton(UserService) service) {
    const user = {
        name: this.body.name,
        gender: this.body.gender,
        address: this.body.address,
        emailId: this.body.emailId,
        password: this.body.password
    };
    const newUser = service.addUser(user);
    return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

Now our end point is configured for a post request. Let's test this by sending a post request to [http://localhost:4000/user/](http://localhost:4000/user/) with user data in the body.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-22-43-19.png)

It returns the user created with id which is our logic. So we have created the end point for the post request, but one important thing to do is to validate the data. Validation is an essential part of any app and is very important for a backend application.

So far, our code is clean and readable. But if we add validation code it will become a little dirty. 

Worry not, FortJs provides the component [Guard](http://fortjs.info/tutorial/guard/) for this kind of work. A/c to the FortJs docs:

> Guard is security layer on top of Worker. It controls whether a request should be allowed to call the Worker.

So we are going to use guard for validation of the data. Let's create the guard using fort-creator. Execute the command  `fort-creator add` and choose Guard. Enter the file name "UserValidator". There will be a file "user_validator_guard.js" created inside the guards folder. Open that file.

A guard has access to the body, so you can validate the data inside that. Returning null inside the method `check` means that we're allowing to call the worker. Returning anything else means block the call.

Let's make it clearer by writing code for the validation. Paste the below code inside the file "user_validator_guard.js":

```javascript

import { Guard, textResult, HTTP_STATUS_CODE } from "fortjs";

export class UserValidatorGuard extends Guard {

    async check() {
        const user = {
            name: this.body.name,
            gender: this.body.gender,
            address: this.body.address,
            emailId: this.body.emailId,
            password: this.body.password
        };
        const errMsg = this.validate(user);
        if (errMsg == null) {
            // pass user to worker method, so that they dont need to parse again  
            this.data.user = user;
            // returning null means - guard allows request to pass  
            return null;
        } else {
            return textResult(errMsg, HTTP_STATUS_CODE.BadRequest);
        }
    }
    
    validate(user) {
        let errMessage;
        if (user.name == null || user.name.length < 5) {
            errMessage = "name should be minimum 5 characters"
        } else if (user.password == null || user.password.length < 5) {
            errMessage = "password should be minimum 5 characters";
        } else if (user.gender == null || ["male", "female"].indexOf(user.gender) < 0) {
            errMessage = "gender should be either male or female";
        } else if (user.emailId == null || !this.isValidEmail(user.emailId)) {
            errMessage = "email not valid";
        } else if (user.address == null || user.address.length < 10) {
            errMessage = "address length should be greater than 10";
        }
        return errMessage;
    }
    
    isValidEmail(email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }


}
```

In the above code:

* We have created a method validate which takes the parameter user. It validates the user & returns the error message if there is a validation error, otherwise null.
* We are validating data inside the check method, which is part of guard lifecycle. We are validating the user inside it by calling the method validate.  
If the user is valid, then we are passing the user value by using the "data" property and returning null. Returning null means guard has allowed this request and the worker should be called.
* If a user is not valid, we are returning an error message as a text response with the HTTP code "Bad Request". In this case, execution will stop here and the worker won't be called.

In order to activate this guard for the method addUser, we need to add this on top of addUser. The guard is added by using the decorator "Guards". So let's add the guard:

```javascript
@Worker([HTTP_METHOD.Post])
@Route("/")
@Guards([UserValidatorGuard])
async addUser(@Singleton(UserService) service) {
    const newUser = service.addUser(this.data.user);
    return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

In the above code:

* I have added the guard, “UserValidatorGuard” using the decorator Guards.
* With the guard in the process, we don't need to parse the data from the body anymore inside the worker. Rather, we are reading it from this.data which we are passing from "UserValidatorGuard".
* The method “addUser” will only be called when Guard allows, which means all data is valid.

One thing to note is that the method "addUser" looks very light after using a component, and it's doing validation too. You can add multiple guards to a worker which gives you the ability to modularize your code into multiple guards and use that guard at multiple places.

> Isn't this cool :D?

Let's try adding a user with some invalid data:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-23-21-37.png)

As you can see in the screenshot, I have tried sending a request without a password. The result is - "password should be minimum 5 characters". So it means that guard is activated and working perfectly.

### PUT

Let’s add another method - “updateUser” with route “/” , guard “UserValidatorGuard” (for validation of user) and most important - worker with http method “PUT”.

```javascript
@Worker([HTTP_METHOD.Put])
@Guards([UserValidatorGuard])
@Route("/")
async updateUser(@Singleton(UserService) service) {
    const user = this.data.user;
    const userUpdated = service.updateUser(user);
    if (userUpdated === true) {
        return textResult("user updated");
    } else {
        return textResult("invalid user");
    }
}
```

The updated code is similar to the addUser code except functionality wise it is updating the data. Here, we have reutilized UserValidatorGuard to validate data.

### DELETE

In order to delete data, user needs to pass the id of the user. This can be passed by:

* Sending data in body just like we did for add & update - {id:1}
* Sending data in query string - ?id=1
* Sending data in route - for this, we need to customize our route - "/user/1"

We have already implemented getting data from body. So let's see other two ways:

**Sending Data in Query String**

Let's create a method "removeByQueryString" and paste the below code:

```javascript
@Worker([HTTP_METHOD.Delete])
@Route("/")
async removeByQueryString(@Singleton(UserService) service) {
    // taking id from query string
    const userId = Number(this.query.id);
    const user = service.getUser(userId);
    if (user != null) {
        service.removeUser(userId);
        return textResult("user deleted");
    } else {
        return textResult("invalid user", 404);
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-23-40-34.png)

**Sending Data in Route**

You can parameterise the route by using "{var}" in a route. Let's see how.

Let's create another method "removeByRoute" and paste the below code:

```javascript
@Worker([HTTP_METHOD.Delete])
@Route("/{id}")
async removeByRoute(@Singleton(UserService) service) {
    
    // taking id from route
    const userId = Number(this.param.id);

    const user = service.getUser(userId);
    if (user != null) {
        service.removeUser(userId);
        return textResult("user deleted");
    } else {
        return textResult("invalid user");
    }
}
```

The above code is exactly the same as removeByQueryString except that it is extracting the id from the route and using parameter in route i.e., "/{id}" where id is parameter.

Let's test this:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-23-46-42.png)

So we have finally created a REST API for all the funtionalities except GETting a particular user by id. I will leave that to you for practice.

## POINTS OF INTEREST

Q: How do we add authentication to "UserController", so that any unauthenticated request can't call the "/user" end point.

A: There are multiple approaches for this: 

* We can check in every worker for authentication. (BAD - so much extra work and code repetition)
* Create a Guard component and assign to every worker . (GOOD) 
* Create a [Shield](http://fortjs.info/tutorial/shield/) component and assign to controller. Shield is a security layer similar to guard but works on top of controller, so if shield rejects then controller is not initiated. (BEST)

Take a look at the FortJs authentication docs - [http://fortjs.info/tutorial/authentication/](http://fortjs.info/tutorial/authentication/)

## REFERENCES

* [http://fortjs.info/](http://fortjs.info/)
* [https://medium.com/fortjs](https://medium.com/fortjs)


