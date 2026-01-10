---
title: The best ways to test your serverless applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-15T22:22:18.000Z'
originalURL: https://freecodecamp.org/news/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c3lCL2XzL9qOYV-kj4G2GA.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Slobodan Stojanovic

  Serverless is more than a cloud computing execution model. It changes the way we
  plan, build, and deploy apps. But it also changes the way we test our apps.

  Meet Alex. Alex is an ordinary JavaScript developer, focused on Node.j...'
---

By Slobodan Stojanovic

Serverless is more than a cloud computing execution model. It changes the way we plan, build, and deploy apps. But it also changes the way we test our apps.

Meet Alex. Alex is an ordinary JavaScript developer, focused on Node.js lately.

![Image](https://cdn-media-1.freecodecamp.org/images/MtalllczKaCqHXoYLjhWS-dsCuadSW0CSYJ4)
_This is Alex_

Over the last couple of months, his good friends, Anna and Jeff, are always talking about that serverless thingy. Even through they are annoying from time to time, he likes the idea of serverless apps. He even deployed few simple functions to AWS Lambda and Azure at some point.

![Image](https://cdn-media-1.freecodecamp.org/images/W4arHIFaqZutDUYabYBKCAMZsnyVvctmT4G5)
_Anna and Jeff are always talking about that serverless thingy_

At some point, Alex and his team got a new project. After some analysis, Alex thought that it would be the perfect fit for serverless. He presented the idea to his team. Some of the team members were excited, one of them didn’t like it, but most of them didn’t have a strong opinion. So, they decided to give it a try — the project wasn’t too big, and the risk was low.

![Image](https://cdn-media-1.freecodecamp.org/images/4SH3bquVOC81aS03e6CJcUwGSvaRHI7illvN)
_Alex’s team discussing using serverless on their new project_

The team read about serverless, and they got an idea how to structure their new app. But no one was sure how they should fit serverless into their common development process.

At that moment, their process looks like this:

1. They analyze a new feature.
2. For less complex features, they start with the code, then they run it locally and add some tests in the end.
3. For more complex features, they do their version of TDD: they start with tests, then write the code, and test it locally.
4. When the feature is ready, it goes to the CI tool that deploys it to the testing environment.
5. Then the QA team takes a new feature for another round of manual testing. If everything looks good, the app goes through CI to production.

![Image](https://cdn-media-1.freecodecamp.org/images/3FiH7yO9EWUI6fIo0JG8IQppAbm-a2AvDfCq)
_Alex’s team’s common development process_

They decided to start step by step, and then solve the problems as they encountered them.

They picked a small feature, and as it was simple, they started with the code. When the coding part was ready, they hit the first roadblock: how do you run serverless applications locally?

### Local testing

With serverless apps, you don’t manage the infrastructure. Sounds great, but how do you then run your application locally? Can you even do that?

![Image](https://cdn-media-1.freecodecamp.org/images/nS02sQWyNQjiJZN9R71AMMVYZ04rQSku9fes)
_First roadblock: how do you run serverless application locally?_

Depending on your app and serverless vendor, you can run some parts of your app locally. To do so, you can use some of the following tools and techniques:

* [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools) (for Azure functions)
* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli) (for AWS Lambda apps built using AWS SAM)
* Third-party tools (ie. [localstack](https://localstack.cloud))
* [docker-lambda](https://github.com/lambci/docker-lambda) for AWS Lambda local simulation
* Run Node.js function locally

Of course, the list is not complete — there are more tools, and we see new tools almost every day now.

Most of these tools have certain limitations. They can simulate serverless functions and a few other services, such as API Gateway. But what about permissions, auth layer, and other services?

Local testing helps with quick validations to make sure your function works. But is there a better way to make sure your serverless app is working as intended? Yes there is. The first and most important step is: write tests.

So Alex and his team tried their first function locally, and as it seemed to be working. Then they went to the next step.

### Automated tests

Alex and his team just switched to [Jest](https://facebook.github.io/jest/) for testing their Node.js applications. They still do a lot of front end, so they want to use the same tools for the full stack whenever they can. Can they use Jest for testing serverless apps too? And what should they test?

![Image](https://cdn-media-1.freecodecamp.org/images/fFyCbvZfkRQsbC-Pjse6tUul8djTl6hTstHt)
_Second roadblock: how does serverless affect automated testing?_

After a quick investigation, they realized that they can use their favorite Node.js testing tools. Jest, Jasmine, Mocha and others work fine with serverless.

#### What should you test in a serverless app?

With their Node.js apps, Alex and his team follows the three-tier test automation pyramid. The test pyramid was first mentioned by Mike Cohn in his book “[Succeeding with Agile](https://www.amazon.com/gp/product/0321579364?ie=UTF8&tag=martinfowlerc-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0321579364)”.

As the test pyramid defines, they have:

* A lot of unit tests, because they are the cheapest (fastest to write and run)
* Fewer integration tests, because they are more expensive, and they take more time to run
* A few UI tests, because they are the most expensive (requires some GUI tool) and slowest to run

Besides these, they also have manual session-based testing, done by their QA team.

![Image](https://cdn-media-1.freecodecamp.org/images/4mPvNp-TQMmpeAofZQdp5xnU4vSNZldSlqHn)
_[test pyramid](https://martinfowler.com/bliki/TestPyramid.html" rel="noopener" target="_blank" title=") with manual testing_

How does serverless affect the test automation pyramid?

The answer depends on the tier. But the test pyramid looks less like the [Egyptian pyramids](https://en.wikipedia.org/wiki/Egyptian_pyramids), and more like the [Mayan pyramids](https://en.wikipedia.org/wiki/Mesoamerican_pyramids#Mayan_pyramids).

The unit tests layer is not affected a lot. Unit tests are still the cheapest to write and run, but the units can be smaller.

Integration tests layer becomes more important than ever, because serverless apps relies heavily on integrations. It is also cheaper, because having a serverless database just for testing is cheap. So, in a serverless “test pyramid” you need to have more integration tests.

GUI tests layer is also cheaper and faster, because of cheaper parallelization.

Manual testing layer stays the same. But serverless can help you to improve it slightly. We’ll go into the details on that later.

![Image](https://cdn-media-1.freecodecamp.org/images/j0kvLDW4Tykdab9y8ZQMZ10gBAe81GmDLipn)
_Serverless “test pyramid”_

Alex and his team finally had some idea where to focus. The next problem was how to write a function to test them more easily.

#### How to write a testable serverless functions

You need to think about the following risks while you are writing a serverless function:

* **Configuration risks** Are the database and table correct? Or, do you have access rights?
* **Technical workflow risks** Are you parsing and using the incoming request as you should? Or, are you handling successful responses and errors correctly?
* **Business logic risks** Did you follow all the business logic rules that your application has?
* **Integration risks** Are you reading the incoming request structure correctly? Or are you storing the order to the database correctly?

To confirm that your serverless function is working correctly, you need to test all these risks.

You could test each of these as you did for the integration tests. But setting up and configuring the service each time you want to test for one of these risks isn’t optimal. As my friend [Aleksandar Simovic](https://www.freecodecamp.org/news/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e/undefined) loves to say:

> Imagine if testing automobiles was done that way. That would mean that every time you wanted to test a single screw or even a mirror in a car, you would have to assemble and then disassemble the whole car.

To make the app more testable, the clear solution is to break up your function into several smaller ones.

One of the great ways to do so is applying [Hexagonal Architecture](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjF8vPNsMnbAhXBVywKHSTxAskQFggmMAA&url=http%3A%2F%2Falistair.cockburn.us%2FHexagonal%252Barchitecture&usg=AOvVaw3e6eQDT3ptDvw8FnumhByp) to your serverless functions.

Hexagonal Architecture, or **Ports and Adapters**, is a form of application architecture that promotes the separation of concerns through layers of responsibility. As its creator, [Alistair Cockburn](http://alistair.cockburn.us), explains:

> Allow an application to equally be driven by users, programs, automated test or batch scripts, and to be developed and tested in isolation from its eventual run-time devices and databases.

So, how does that apply to serverless functions?

As Alex and his team use AWS, they ended up with a structure like the following:

* Function business logic exposes few “ports” (or expects few arguments). For example, one for an incoming event, one for permanent storage, and one for notifications.
* They have two adapters for the event that triggers a function, one for the real AWS Lambda trigger and another one for local testing.
* They have several adapters for permanent storage and notifications. For example, DynamoDB table adapter and in-memory adapter.

![Image](https://cdn-media-1.freecodecamp.org/images/chFxK8htCl5K2QOkoBOCnXv18f4xCI47okvJ)
_Hexagonal architecture of AWS Lambda function_

Alex and his team were happy that they were moving forward. But before we move on, let’s see how Hexagonal Architecture affects each tier of the test pyramid.

#### Unit testing

Unit tests stayed the same. But it’s easier to write unit tests because of Hexagonal Architecture. They can simply use a local adapter or mock as an adapter to test the function business layer in isolation.

#### Integration testing

Integration tests benefited a lot from Hexagonal Architecture. They were able to fully test integrations that they own. Third-party integrations are simulated with other adapters.

How does that work in practice?

Each of their serverless functions has _lambda.js_ and _main.js_ files. The main file contains the business logic of a serverless function. And the _lambda.js_ file is in charge of wiring the adapters and invoking the _main.js_ file.

The main file has its own unit and integration tests. But its integration tests don’t test full integration with end services, such as AWS S3, because that would slow them down. Instead, they use an in-memory adapter to test the function with file storage integration.

AWS S3 integration is done through the _FileRepository_, which has its own unit and integration tests. Integration tests checks use AWS S3 to be sure that the end integration actually works.

As opposed to _main.js_, the _lambda.js_ file doesn’t have tests, because most of the time it has just a few lines of code.

![Image](https://cdn-media-1.freecodecamp.org/images/eokIvJ-PIBMhzLPIoNFu7qThfVsmwQjiGtWS)
_Visual representation of single AWS Lambda function with tests_

This approach is like the technique the [MindMup](https://www.mindmup.com) team is using for testing serverless functions. With it, you can easily test integrations of your functions, and still make your integration tests faster.

#### GUI testing

As Alex and his team were building a back end for the app, the GUI tests tier was not relevant. But as they learned more about serverless, they realized that they could use it to improve the GUI tests tier for the other apps they were working on.

UI tests are expensive and slow, because they run in the browser. But, serverless is cheap and it scales fast.

If they could run a browser in AWS Lambda, they would gain cheap parallelization. That would make their UI tests cheaper and faster.

But, can you run a browser, such as Chrome, inside a serverless function?

Yes! And it is easy with the help of a tools such as [Serverless Chrome](https://github.com/adieuadieu/serverless-chrome), [Chromeless](https://github.com/prismagraphql/chromeless), and [Puppeteer](https://github.com/GoogleChrome/puppeteer).

![Image](https://cdn-media-1.freecodecamp.org/images/5eoKemm0zOuNq3KphM3a6exI-WwjZxffmFe6)
_Using AWS Lambda functions for parallelization of UI tests_

A combination of serverless and headless browsers can bring us a new generation of UI testing tools. We can already see and try some of them, such as [Appraise](http://appraise.qa).

### CI / CD

As Alex and his team tested their first serverless function, it was time to deploy the code to the testing environment. That brought up a new question: how can they use CI/CD tools to deploy their serverless app?

![Image](https://cdn-media-1.freecodecamp.org/images/t2czuwldXzmq1WQJyz9z4bcH-zcEHjvtRPAX)

The answer is simple: they can use a CI tool to run the tests and deploy the app. To deploy the app, use any popular tool, such as [Claudia.js](https://claudiajs.com), [AWS SAM](https://github.com/awslabs/serverless-application-model), and [Serverless Framework](https://serverless.com).

You can still use your favorite CI tool (like [Jenkins](https://jenkins.io), [TravisCI](https://travis-ci.org) or [SemaphoreCI](https://semaphoreci.com)), or if you want to stick with AWS, you can try [AWS CodeBuild](https://aws.amazon.com/codebuild/).

### Manual testing

Even through manual testing is not directly affected by serverless, the team found a way to improve their QA process.

![Image](https://cdn-media-1.freecodecamp.org/images/iKbkUkU7K9X0TFyMDArE3df68GjSG-3peTgK)

Stages and deployments of serverless app are cheap and often fast to setup. Also, with serverless, you don’t pay for the app if no one is using it.

This means that having a testing environment has never been cheaper!

Also, with serverless, you can often _promote_ the function from one stage to another. This means that your QA team can test a function, and when they confirm that it works, you can promote the same function to production.

### Beyond testing

Alex and his team shipped their first serverless function to pre-production, and the team was happy that they learned how to test serverless apps.

![Image](https://cdn-media-1.freecodecamp.org/images/5ctT2IR50soRZdzNTojzOv-07ddy6ThSKsS2)

They continued using serverless on the project, and introduce it to few other projects. Alex joined his friends Anna and Jeff, as a third, sometimes annoying, serverless preacher. And they lived happily ever after.

![Image](https://cdn-media-1.freecodecamp.org/images/fkvnvW6w0JSsdN1R6HrDbzkBgviZ12wNHI3e)
_Serverless preachers crew got a new member_

### Post-script

But even though their app was well-tested, something happened overnight.

After an investigation, they found out that one of the integrations changed. They learned that testing is important for serverless apps, but it’s not enough.

As serverless apps heavily depend on integrations, the risk shifts from your code to the integrations. And, to be able to catch integration changes and react fast, your app needs proper monitoring.

Fortunately, there are more and more serverless monitoring tools on the market every day. Some of the good and popular options are [IOpipe](https://www.iopipe.com), [Thundra](https://www.thundra.io), [Dashbird](https://dashbird.io), and [Epsagon](https://www.epsagon.com).

But, serverless apps often have a thick client, which means that back end monitoring is not enough. You need a similar tool for your front end. This market has a lot of nice tools too, such as [Sentry](https://sentry.io) and [Rollbar](https://rollbar.com).

But in the spirit of serverless, we created an open source error-tracking app called [Desole](https://desole.io). It is a serverless app you can install in your AWS account. It enables organisations to track application exceptions and errors without having to choose between the convenience of software-as-a-service and the security of a self-hosted solution. You can check it out here: [https://desole.io](https://desole.io.).

![Image](https://cdn-media-1.freecodecamp.org/images/g874CpDwSRlIUinEuRFszzJVYRxy9G75Ewrp)
_[Desole](https://desole.io" rel="noopener" target="_blank" title="), open source error-tracking, tightly integrated with AWS_

> _All illustrations are created using [SimpleDiagrams4](https://www.simplediagrams.com) app._

If you want to learn more about testing and building serverless apps using Node.js and AWS, check out “Serverless Applications with Node.js”, the book I wrote with [Aleksandar Simovic](https://www.freecodecamp.org/news/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e/undefined) for Manning Publications:

[**Serverless Applications with Node.js**](https://www.manning.com/books/serverless-applications-with-nodejs)  
[_A compelling introduction to serverless deployments using Claudia.js._www.manning.com](https://www.manning.com/books/serverless-applications-with-nodejs)

The book will teach you more about serverless testing, with code examples, but you’ll also learn how to build and debug a real world serverless API (with DB and authentication) using Node and Claudia.js. And you’ll learn how to build chatbots, for Facebook Messenger and SMS (using Twilio), and Alexa skills.

