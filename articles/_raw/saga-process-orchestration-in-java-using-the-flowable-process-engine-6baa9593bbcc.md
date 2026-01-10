---
title: Saga Process Orchestration in Java Using the Flowable Process Engine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T22:05:19.000Z'
originalURL: https://freecodecamp.org/news/saga-process-orchestration-in-java-using-the-flowable-process-engine-6baa9593bbcc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Hcv7JuT-UuVxnTO2TkRoUg.jpeg
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'By Felix Kuestahler

  Define a Saga Process Controller in Flowable by using the Camel Task for system
  integration

  Introduction

  In this tutorial, I did an assessment of the capability of Flowable to act as a
  Saga Process Controller.


  _Photo by [Unsplash...'
---

By Felix Kuestahler

#### Define a Saga Process Controller in Flowable by using the Camel Task for system integration

### Introduction

In this tutorial, I did an assessment of the capability of Flowable to act as a Saga Process Controller.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hcv7JuT-UuVxnTO2TkRoUg.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/uYkdJEYNwSM?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Geran de Klerk</a> on <a href="https://unsplash.com/collections/1988198/integrous?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Flowable provides a core set of open source business process engines that are compact and highly efficient. They provide a workflow and Business Process Management (BPM) platform for developers, system admins and business users. At its heart is a lightning fast, tried and tested dynamic BPMN process engine, with accompanying DMN decision tables and CMMN case management engines, all written in Java. They are Apache 2.0 licensed open source, with a committed community. ([Link](https://www.flowable.org/))

As one can see, Flowable is positioned as a Workflow and Business Process Management Platform. What we want to understand is the feasibility of Flowable in context of low-level service orchestration, defined as Saga Orchestration.

Refer to the following excellent article by Bernd Rücker in order to get an overview of how to tackle “[Business Transactions without two-phase commit](https://blog.bernd-ruecker.com/saga-how-to-implement-complex-business-transactions-without-two-phase-commit-e00aa41a1b1b)”

> The Saga pattern describes how to solve distributed (business) transactions without two-phase-commit as this does not scale in distributed systems. The basic idea is to break the overall transaction into multiple steps or activities. Only the steps internally can be performed in atomic transactions but the overall consistency is taken care of by the Saga. The Saga has the responsibility to either get the overall business transaction completed or to leave the system in a known termination state. ([Link](https://blog.bernd-ruecker.com/saga-how-to-implement-complex-business-transactions-without-two-phase-commit-e00aa41a1b1b))

In this article, I don’t address compensating transaction. I will concentrate on the basic skeleton necessary to execute Saga process orchestration. It’s mainly a combination of the workflow capability provided by Flowable combined with the power of Apache Camel (a Java integration framework based on the [EIP pattern](https://www.enterpriseintegrationpatterns.com/)). Apache Camel is a first-citizen in Flowable via the so-called “Camel Task”.

### Spring Boot Application Framework

Flowable in its nature is a Spring Boot based application. It benefits from all the features provided by Spring Boot.

> Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run".

> We take an opinionated view of the Spring platform and third-party libraries so you can get started with minimum fuss. Most Spring Boot applications need very little Spring configuration.([Link](https://spring.io/projects/spring-boot))

Spring Boot is all about convention over configuration. Our _build.gradle_ looks as follows:

The gradle build file is quite compact and consists of the following dependencies:

* Spring Boot framework dependencies
* Flowable Spring Boot integrated framework dependencies
* Camel Boot integrated framework dependencies
* As well as H2, an in-memory database required for the Flowable stateful processing engine

That’s it, rather straightforward.

#### Spring Boot and Flowable

By introducing the above Flowable dependencies (refer to the [Flowable Spring Boot App Documentation](https://www.flowable.org/docs/userguide/index.html#springSpringBoot)) and using the _@SpringBootAplication_ annotation, a lot has happened behind the scenes:

* An in-memory datasource is created automatically (because the H2 driver is on the classpath). It is passed to the Flowable process engine configuration
* A Flowable ProcessEngine, CMMNEngine, DMNEngine, FormEngine, ContentEngine, and IdmEngine beans have been created and exposed
* All the Flowable services are exposed as Spring beans
* The Spring Job Executor is created

You may fine-tune the Flowable App — i.e. in case you only need a subset of the provided engines, refer to the following [Flowable Starter List](https://www.flowable.org/docs/userguide/index.html#springBootFlowableStarter).

#### SpringBoot and Camel

The Apache Camel Integration Framework is included via the following two dependencies:

```
implementation 'org.apache.camel:camel-spring-boot-starter:2.23.0'implementation 'org.flowable:flowable-camel:6.4.1'
```

* The first dependency ties Camel into the Spring Boot App framework,
* The second dependency ties Camel into the Flowable Process Engine, via the so-called Camel Task, which enables the delegation of any third party system integration into a Flowable Process Model to a Camel Route (more on that later)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gXYo1XbpKyBN8UNIvYOD-w.png)

### Bootstrapping Flowable Boot App

To get a barebones Flowable Spring App running, follow these steps:

Introduce an application.properties with the following properties.

```
management.endpoints.web.exposure.include=*management.endpoint.health.show-details=when_authorizedflowable.idm.password-encoder=spring_delegating
```

Provide a SecurityConfiguration class.

And load three test users at startup.

Finally, we provide a REST controller, to do an initial check of our core Flowable Spring Boot App.

Start the Flowable App, via the command

```
gradle bootApp
```

And open the browser with [http://localhost:8080](http://localhost:8080). You will be prompted for a user and password. Provide `flowfest` and password `test`. You should now be logged in and the greeting message should be displayed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7bxOg44MynsRr-IJXanD3A.png)

Ok well done, our powerful Spring App is ready and we can move on.

### Flowable Modeller

Our Saga Process will be modeled in the Flowable Modeler by using the BPM model feature. A quick introduction is given in this [Flowable Tutorial](https://paulhh.wordpress.com/2017/01/31/flowable-6-instant-gratification/).

Via the [Flowable Home Page](https://www.flowable.org/), download the latest version (actual Flowable version v4.6.1) which is a zip file containing a war directory with 5 WAR files.

Deploy these 5 war files for example on a Tomcat test server and run:

[http://localhost:8080/flowable-modeler](http://cloudburo2:8080/flowable-modeler/#/processes)/ you will be asked to log in, provide `admin` with password `test`

![Image](https://cdn-media-1.freecodecamp.org/images/1*S7UF3czTzNRQv_anLYkjQQ.png)
_Flowable Login Page_

After a successful login, you will be directed to the Business Process Models Dashboard (which would be empty initially).

![Image](https://cdn-media-1.freecodecamp.org/images/1*c6uVzhNkBfCqr8Othmb4QQ.png)

You are ready to test it out. The Flowable default configuration introduces a persistent DB. This ensures that your model artifacts will be stored and are available after rebooting the Application server.

One minor manual modification was necessary on an Ubuntu Standard Tomcat Application Server in order for the loading of the Flowable Modeler to be successful. In the tomcat artifact directory ( /var/lib/tomcat8) I had to create a `flowable-db` directory with user/group right `tomcat8:tomcat8`, otherwise the application startup failed (due to the fact that tomcat8 apt packages are installed by root).

![Image](https://cdn-media-1.freecodecamp.org/images/1*L8s7nstYSmTa_Eqi88fTHw.png)

### Flowable Saga: Hello World Process

In Flowable we model our hello world process, which consists of 4 steps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hrwfgxuel0FA_xOl329uqQ.png)
_The open source Flowable Modeler (BPMN, CMN, DMN and UI Forms)_

* _Initialize Variables_ Task sets an input variable which we want to process in our Camel Task
* _Async Camel_ Task will delegate the process to a Camel Route, which processes the input variable. We will use Camel Routes for any kind of external system integration. This task is called in an asynchronous manner, i.e. after delegating the processing to the Came Route the task is terminated and moved forward to the…
* _Receive Process Response_ Task is an asynchronous Receiver Task, which waits to the completion of the Camel Route processing. After event triggering the processed data will be handed over to the…
* _Save Variable_ Task, which extracts the process result.

As you will see later by using the power of Camel for the Integration, we can elegantly introduce an asynchronous behavior in our Saga process flow with just one line of code.

The Project structure is straightforward. We need three classes to get this process flow implemented, as well as the BPMN process model:

![Image](https://cdn-media-1.freecodecamp.org/images/1*WN4qRXB1JLaw5G9trAzBQg.png)

Taken into consideration that we may have multiple Saga process flows in a Flowable Spring App we strive for clear packaging rule:

* Each BPMN process model has a unique id, in our case the id is `saga1Process`. Therefore
* any kind of tasks referenced in the process model is within a package `task.saga1`
* any kind of Camel route referenced in the process model is within a package `route.saga1`

### InitVariablesTask

We simulate here the retrieval of some input data provided by a calling application. We set the variable `name` to `Hello World`. This variable is now part of the process context.

Within the model, we associate our class with our Service Task:

![Image](https://cdn-media-1.freecodecamp.org/images/1*tIfsbnYIFpsI1_y-QAjbeA.png)

### Camel Route

Let’s switch now to the Camel Task which is a Camel Service Task, which we configure as Asynchronous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MMTOI93toIg528lJ9UTJUA.png)

As one can see the only thing we configure in our a Camel Task is the Service Task Id and we set the Asynchronous flag.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uzQyWtOi9haOaNVfNdY2Gg.png)

The wiring of the Service Task to the Camel route is done within the route class, via naming conventions. The overall process id is `saga1Process` and the task id `camelAsyncTask`, so let’s look at the Camel Route class. We establish the inbound route on line 17 to our Camel Service Task

```
from("flowable:saga1Process:camelAsyncTask")
```

and will put the message received into the Camel seda component (line 18), which will decouple the Camel Service Task from the processing in an asynchronous manner (as said by just one line of code)

```
.to("seda:continueAsync")
```

#### A short intro to the SEDA component

We will use the **seda:** Camel component. This provides asynchronous [SEDA](https://en.wikipedia.org/wiki/Staged_event-driven_architecture) behavior. Messages are exchanged on a [BlockingQueue](http://java.sun.com/j2se/1.5.0/docs/api/java/util/concurrent/BlockingQueue.html) and consumers are invoked in a separate thread from the producer.

> The **staged event-driven architecture** (**SEDA**) refers to an approach to [software architecture](https://en.wikipedia.org/wiki/Software_architecture) that decomposes a complex, event-driven [application](https://en.wikipedia.org/wiki/Computer_program) into a set of stages connected by queues. It avoids the high overhead associated with [thread](https://en.wikipedia.org/wiki/Thread_(computer_science))-based [concurrency models](https://en.wikipedia.org/wiki/Concurrency_(computer_science)) (i.e. locking, unlocking, and polling for locks), and decouples event and thread scheduling from application logic.

As we can see after the retrieval of the message, we simulate some processing

```
.log(LoggingLevel.INFO, logger, "External System Processing...").transform().simple("Processed: ${property.input}, { Result: OK }");
```

Finally, we return the result back to our Saga process

```
from("seda:continueAsync")        .to("flowable:saga1Process:receiveAsyncTask");
```

That’s it. So any kind of external system integration we can delegate to Camel routes, which are providing powerful integration concepts. As for the example, instead of implementing a retry mechanism as part of the Saga process, one can use an exception handler with a re-delivery policy (also known as the `RedeliveryErrorHandler` in Camel). This error handler will allow you to set the number of retries and also set things like the delay between retries etc.

```
public void configure()  {    // ExceptionHandler with RedliveryPolicy    errorHandler(defaultErrorHandler()            .maximumRedeliveries(3)            .backOffMultiplier(4)            .retryAttemptedLogLevel(LoggingLevel.WARN));
```

### Receive Async Response Task

This Service Receiver Task will serve as the bridge back from Camel as explained above.

### Save Output Task

Finally, we print out the produced Camel message which was passed over.

### Spring Boot App

Within the `_SpringBootApplication_` we introduce a `CommandLineRunner` which will trigger our process model.

If we restart our application:

```
gradle bootApp
```

we can see on the console the processing output of our Saga process.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q0AWYjlWCTdhWr2gV6zH5A.png)

Last but not least you may also run unit tests via

```
gradle test
```

To wrap it up: As one can see, Flowable allows, with the concept of Camel Task, a powerful integration of third-party systems into a BPMN process flow. This approach will ensure that the orchestration flow will not be overloaded by enterprise integration logic which is offloaded to Camel Routes.

You can check out the code here:

[**talfco/tutorial-flowable-saga**](https://github.com/talfco/tutorial-flowable-saga)  
[_A tutorial which describes the approach how to use Flowable and Camel for a Saga Process Manager …_github.com](https://github.com/talfco/tutorial-flowable-saga)

Happy coding then.

