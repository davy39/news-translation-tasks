---
title: How to Test Your Microservices to Make Sure They Are Production Ready
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-20T07:54:00.000Z'
originalURL: https://freecodecamp.org/news/testing-microservices-are-they-production-ready-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/UiqRDTTd.png
tags:
- name: Microservices
  slug: microservices
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'By Anton Lawrence

  Microservices architecture describes the practice of breaking up an application
  into a series of smaller and more problem-solution oriented components. Then each
  of these components communicates with one another across common protoc...'
---

By Anton Lawrence

Microservices architecture describes the practice of breaking up an application into a series of smaller and more problem-solution oriented components. Then each of these components communicates with one another across common protocols like HTTP or the more lightweight TCP.

## **You might be wondering - are tests important for me?**

**Long story short - YES.**  
  
Software testing is important for a number of reasons, but most importantly:

* It saves money and a lot of time
* Security
* Product quality (fewer bugs and errors)
* Customer satisfaction
* It lets you sleep peacefully at night

No one likes an application that has bugs and stops working for no reason. And there is no need to talk about the hazards of poor security, which allows hackers to steal credentials and even money.  
  
As long as you develop an application that will be used by users and has some complexity, tests should not be an option – they should be mandatory.

## **What test should I write?**

There are various types of software testing.  
  
**Functional Testing types include:**

* Unit Testing
* Integration Testing
* Smoke Testing
* Regression Testing
* Sanity Testing
* Beta/Acceptance Testing
* End to End (e2e) Testing

**Non-functional Testing types include:**

* Performance Testing
* Load Testing
* Stress Testing
* Security Testing
* Compliance Testing
* Usability Testing

The more complex the app gets the more types of tests you will use.

**The basic tests that you should always use are the following:**

* Unit Testing
* Integration Testing
* E2E Testing combined with Regression testing and Security Testing

The process goes like this: first you write tests to check if your app behaves as expected in almost all aspects, including corner cases. Second, if your app is already live, you write tests to check if any new changes to the code break the current functionality.  
  
_Side note: besides these basic tests that you should use at any type of software, there are additional tests you should write for microservices. Don't forget load tests, for example, to check your system's behavior under both normal and anticipated peak load conditions._

## **Less talk, more code**

In the following examples, we will see how we can implement those basic types of software testing from above in a microservice. The microservice uses the TCP protocol for communication and is written in Node.js using the [Nest Framework](https://nestjs.com/).  
  
If NestJS sounds new to you, don't worry – all you need to know is the following:

> "**Nest** is a framework for building efficient, scalable **Node.js** server-side applications.  
>   
> It uses modern JavaScript, is built with TypeScript (preserves compatibility with pure JavaScript) and combines elements of OOP (Object Oriented Programming), FP (Functional Programming), and FRP (Functional Reactive Programming).   
>   
> Under the hood, Nest makes use of [Express](https://expressjs.com/), but also, provides compatibility with a wide range of other libraries, like e.g.   
>   
> [Fastify](https://github.com/fastify/fastify), allowing for easy use of the myriad third-party plugins which are available." – _Official Github repo description_

For this example we will use a simple module, name: **user**, with a simple function **createUser**, that will create a new user in our database.  
  
The folder structure for the module looks like this:

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583005463519_folder-structure.PNG)

  
We have a controller that listens for a message **create_user**. After it does the validation with the ValidationPipe it will call a function with the same name inside its service.

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162403293_controller.png)

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162684122_validation.png)

Inside the service, we hash the user password. Then using TypeORM we save a new user inside our database.

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162552215_service.png)

  
For this module we use TypeORM as the ORM linked to the table User, and another module named **UtilsModule** in which we have some helper function:

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583162768022_module.png)

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583163527010_entity.png)

## Unit testing

A **unit** is the smallest testable part of an application like functions, classes or procedures. **Unit Testing** is a software testing method by which individual units of source code are tested to determine whether they are good for us. 

Basically, unit tests are written to make sure that each simple implementation of different code forms (functions, classes, and so on) meets their design and requirements and behaves as expected.  
  
The goal of [unit testing](https://codepad.co/blog/test-driven-development-writing-efficient-code-for-your-unit-tests/) is to segregate each part of the program and test that the individual parts are working correctly.   
  
This means that the other parts of the code that are not directly from the testing unit (but are linked with it) will be mocked.  
  
In our case, the function we want to test (**createUser**) is our unit we want to test. This means that we have to isolate it from the other components. So we have to mock our **user repository** class which represents the link with the database using **TypeORM**.  
  
If we analyze the function (the one in the service), we see that all it does is hash a password and then to save a User object inside our database. Given this fact we write the following test suite:

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583007348914_unit_test.png)

First, we write a **beforeAll** function which creates our testing module. Then we replace the original repository with our mock class, which will only return the object we want to save in the database.

In our function we had one requirement with one corner case:

* create a new user object with some given properties (email, password), but with a hashed password

We mocked the function **save(),** since it’s from TypeORM, outside of our unit, and we overrode it with a simple function that returns the object we passed.   
  
So all we had to do was to check if we were sending the object with the right email property and with the correct hash.

## Integration testing

**Integration** **Testing** is a software testing method by which units of source code are tested to verify the combined functionality.   
  
Unit tests are basically written to make sure that code meets its design and requirements and behaves as expected. The goal of unit testing is to blend together different modules and test if they interact properly.  
  
So now, for our example, we combine our **UserModule** with the TypeORM module (dependency) to check if the user is saved in the database.  
  
Again we have the same function from above, but this time with the following test:

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583008813487_integration_test.png)

This time, in our **beforeAll** function we don’t mock the **userRepository**. Instead we use the original one, plus we add our **databaseModule** which creates the connection to our database.  
  
At the same time, because we use a real database now, we have to write several functions that will prepare our database for tests.   
  
We need to empty the database before and after our tests, just to be sure that it is completely empty.   
  
In the same time we have to manually close the connection to it, so that we do not remain with any open handlers after we finish the tests.  
  
With Unit Testing, we checked to see if our function was working as designed. So here all we have to do is to test if our function blends with the **save()** method from TypeORM and our user is stored inside the database.  
  
We write a helper function name **getOneUserFromDb,** which does what it says it does. Then we check if the email is correct as well as the property **accountConfimed**, which was set in entity class with the default value **false**.

## End-to-End Testing

**[End-to-End Testing](https://itnext.io/end-to-end-testing-78033fb768a8)** is a software testing technique used to test whether the flow of an application is performing as designed from start to finish.   
  
We do this type of testing to ensure that the application will work as expected in a real-world situation.  
  
Up to this point we've tested whether the user password was hashed accordingly and if the password and email were saved inside the database.   
  
Now we need to test our validations at the request level. In our controller, we have a validation pipe which tests the incoming payload to check if the object matches with **CreateUserDto .**

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583163595607_validation.png)

And the tests:

![Image](https://paper-attachments.dropbox.com/s_FDCC4A0956EFA11FA95EB05EAD0F9699A27E3C40529F74A5327263B861F7621B_1583155804389_e2e.png)

Here we tested to see what would happen if we tried to create a user but didn't send the entire object or sent properties in an incorrect format.  
  
These are some examples of the corner cases from our function that we tested using just 3 types of software testing.

## Manual vs Automated Tests

So far, we've written our tests manually – and for this case that was just perfect. But the more code you have, the more complex and larger your test suits will become.  
  
For example, if you are going to test an authentication system, you will have to replicate the entire behavior of a real user. And you will have to mock the requests and responses, including cookies and many more things, just to build the environment for your tests. A long test suite can take a lot of time to run.  
  
Luckily you have one more option when it comes to testing: automated tools. These tools have built-in functionalities for you to mock the entire environment for your tests, which makes the test process way easier.   
  
You can go even further and use [automated API testing tools](https://www.loadmill.io/) for your application. These are tools that come with extra options which makes them great for load testing, regression testing, and data reports for real situations.   
  
Plus they have a good UI that makes it way easier to write tests.

## Conclusion

Building software that's ready for production requires tests. And sometimes, depending on the complexity of the app, those tests can become a bottleneck for you or your team.   
  
In this case, be sure to separate your test suites by their type, just like we did earlier. And only to test the functionality that belongs to the current test type.   
  
If this is not enough for your use case, or tests are too hard to write and take too much time, then you can use automated tools and platforms to make things easier.

