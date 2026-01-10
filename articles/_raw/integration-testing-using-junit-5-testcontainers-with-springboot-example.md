---
title: How to Perform Integration Testing using JUnit 5 and TestContainers with SpringBoot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-26T15:46:39.000Z'
originalURL: https://freecodecamp.org/news/integration-testing-using-junit-5-testcontainers-with-springboot-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/testcontainers-logo.png
tags:
- name: Docker
  slug: docker
- name: Software Testing
  slug: software-testing
- name: spring-boot
  slug: spring-boot
- name: Testing
  slug: testing
seo_title: null
seo_desc: "By Sameer Shukla\nTestContainers is a library that helps you run module-specific\
  \ Docker containers to simplify Integration Testing. \nThese Docker containers are\
  \ lightweight, and once the tests are finished the containers get destroyed.\nIn\
  \ the article ..."
---

By Sameer Shukla

TestContainers is a library that helps you run module-specific Docker containers to simplify Integration Testing. 

These Docker containers are lightweight, and once the tests are finished the containers get destroyed.

In the article we are going to understand what the TestContainers is and how it helps you write more reliable Tests. 

We are also going to understand the important components (Annotations and Methods) of the library which help you write the Tests. 

Finally, we will also learn to write a proper Integration Test in SpringBoot using the TestContainers library and its components. 

## Limitations of Testing with an H2 In-Memory Database

The most common approach to Integration Testing today is to use an H2 in-memory database. But there are certain limitations to this method.

First of all, say we are using version 8.0 of MySQL in production, but our integration tests are using H2. We can never execute our tests for the database version running on Production.       

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-303.png)
_SpringBoot app with MySQL DB and H2_

‌Secondly, the test cases are less reliable because in production we are using an altogether different database and the tests are pointing to H2. The application may run into issues in production, but the integration tests may succeed. 

I was trying to access my RESTful service on local and faced this error: 

“**Caused by: org.postgresql.util.PSQLException: FATAL: database "example_db" does not exist**”. 

It happened because of a permission issue, but the tests on local worked fine.

And finally, as documented [here](http://h2database.com/html/features.html#compatibility), H2 is compatible with other databases only up to a certain point. There are few areas where H2 is incompatible. If you need to use “nativeQueries” in a SpringBoot application, for example, then using H2 may cause problems.

## Enter the TestContainers Library

By using TestContainers we can overcome the limitations of H2.

* Integration tests will point to the same version of the database as it’s in production. So we can tie our TestContainer Database Image to the same version running on production.
* Integration tests are lot more reliable because both application and tests are using the same database type and version and there won't be any compatibility issues in Testcases.

## What is TestContainers?

The TestContainers library is a wrapper API over Docker. When we write code to create a container behind the scenes it may be translated to some Docker command, for example‌:                                    

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-283.png)
_MySQLContainer Creation_

This code may be translated to something like the following:

```docker 
docker run -d --env MYSQL_DATABASE=example_db --env MYSQL_USER=test --env MYSQL_PASSWORD=test ‘mysql:latest’ 
```

TestContainers has a method name “withCommand”. You use it to set the command that should be run inside the Docker container which confirms that TestContainers is a wrapper API over Docker.

TestContainers downloads the MySQL, Postgres, Kafka, Redis images and runs in a container. The MySQLContainer will run a MySQL Database in a container and the Testcases can connect to it on the local machine. Once the execution is over the Database will be gone – it just deletes it from the machine. In the Testcases we can start as many container images as we want.

TestContainers supports JUnit 4, JUnit 5 and Spock. If you go to the TestContainers.org website, just visit the QuickStart section that explains how to use it:                    

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-284.png)
_TestContainers.org how to start with Test Framework_

TestContainers supports almost every Database from MySQL and Postgres to CockroachDB. You can find more info about this on the TestContainers.org website under the Modules section:‌                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-285.png)
_TestContainers support for Database Modules_

‌TestContainers also supports Cloud Modules like GCloud Module and Azure Module as well. If your application is running on Google Cloud, then TestContainers has support for Cloud Spanner, Firestore, Datastore and so on.‌ 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-286.png)
_TestContainers support for GCloud Module_

In the article so far, we have discussed only about Databases, but TestContainers supports various other components like Kafka, SOLR, Redis, and more.

## How to Use the TestContainers Library

In this article we are going to explore TestContainers with JUnit 5. To implement TestContainers we need to understand a few important TestContainers annotations, methods, and the libraries that we need to implement in our project.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-288.png)
_TestContainers libraries_

### Annotations in TestContainers

Two important annotations are required in our Tests for TestContainers to work: @TestContainers and @Container.

@TestContainer is JUnit-Jupiter extension which automatically starts and stops the containers that are used in the tests. This annotation finds the fields that are marked with @Container and calls the specific Container life-cycle methods. Here, MySQLContainer life-cycle methods will be invoked.‌                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-289.png)
_MySQLContainer_

The MySQLContainer is declared as static because if we declare Container as static then a single container is started and it will be shared across all the test methods.

If it’s an instance variable, then a new container is created for each test method.

## TestContainers Library Methods

There are few important methods in TestContainers library that you'll use in the tests. They're good to know before using the library.

* **withInitScript**: Using ‘withInitScript’ we can execute the .SQL to define the schema, tables, and plus add the data into the database. In short, this method is used to run the .SQL to populate the database.
* **withReuse** (true): Using “withReuse” method we can enable the reuse of containers. This method works well in conjunction with enabling the “testcontainers.reuse.enable:true” property in the “.testcontainers.properties” file.
* **start**: we use this to start the container.
* **withClasspathResourceMapping**: This maps a resource (file or directory) on the classpath to a path inside the container. This will only work if you are running your tests outside a Docker container.
* **withCommand**: Set the command that should be run inside the Docker container.
* **withExposedPorts**: Used to set the port that the container listens on.
* **withFileSystemBind**: Used to map a file / directory from the local filesystem into the container.

## TestContainers Use Case

In the example we'll look at now, the application will communicate only with the database and write the integration tests for it using TestContainers. Then we'll extend the use-case by implementing Redis in between.

If the data exists in the Redis cache it will be returned, otherwise it'll dip into the database for saving and retrieval based on the Key.              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-308.png)
_Use-Case_

The service is simple. It has 2 endpoints – the first one is to create a user and the second one is to find a user by email. If the user is found it is returned, otherwise we get a 404. The service class code looks something like this:‌

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-291.png)
_Service Component_

We are going to write tests for this class. You can find the entire codebase [here](https://github.com/sameershukla/testcontainers_demo ):‌

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-292.png)
_Test Class_

The test class is marked with @TestContainers annotation which starts/stops the container. We use the @Container annotation to call the specific container's life-cycle methods. 

Also, the “MySQLContainer” is declared as static because then a single container is started. Then it gets shared across all the test methods (we have already discussed the importance of these annotations).                             

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-293.png)
_BeforeAll_

Next we need to write a setup method marked with @BeforeAll, where we have enabled the “withReuse” method. This helps us reuse the existing containers. We are using the “withInitScript” method to execute the “.sql” file and then starting the container.‌                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-294.png)
_Overwriting Properties_

‌@DynamicPropertySource helps us override the properties declared in the properties file. We write this method to allow TestContainers to create the URL, username, and password on its own – otherwise we may face errors. 

For example on removing username and password we may face an ‘Access denied’ error which may confuse us. So it’s better to allow TestContainer to assign these properties dynamically on its own.

That’s it – we are ready to run the Testcases:       

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-295.png)
_Test Cases_

Execute @AfterAll to stop the container, otherwise it may keep running on your local machine if you don't explicitly stop it. ‌                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-296.png)

## How to Use GenericContainer

‌‌GenericContainer is the most flexible container. It makes it easy to run any container images within GenericContainer.

Now we have Redis in place, all we need to do in our Testcase is to spin up a GenericContainer with the Redis image.        

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-297.png)
_GenericContainer for Redis_

Then we start the Generic Redis container in @BeforeAll and stop it with the @AfterAll tear down method.                     

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-298.png)
_Starting Containers_

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-299.png)
_Stopping Containers_

## Wrapping Up

It's extremely easy to use TestContainers in our application to write better tests. The learning curve is not too steep and it has support for various different modules from a variety of databases like Kafka, Redis and others. 

Writing tests using TestContainers makes our tests lot more reliable. The only flip side is that the tests are slow compared to H2. This is because H2 is in memory and TestContainers takes time to download the image, run the container, and execute the entire setup we have discussed in this article.


