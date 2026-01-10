---
title: How to Perform Load Testing in Spring Boot with Gatling
subtitle: ''
author: Mario Casari
co_authors: []
series: null
date: '2024-07-08T19:46:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-spring-boot-with-gatling
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/pexels-markusspiske-177598.jpg
tags:
- name: Gatling
  slug: gatling
- name: Java
  slug: java
- name: spring-boot
  slug: spring-boot
seo_title: null
seo_desc: "To evaluate the performance of a system, you need a tool that can simulate\
  \ its behavior in production. \nFor this purpose, you can use a software tool based\
  \ on Scala called Gatling. This article will teach you how to integrate it into\
  \ a Spring Boot ap..."
---

To evaluate the performance of a system, you need a tool that can simulate its behavior in production. 

For this purpose, you can use a software tool based on [Scala](https://www.scala-lang.org/) called [Gatling](https://gatling.io/). This article will teach you how to integrate it into a [Spring Boot](https://spring.io/projects/spring-boot) application and perform a load test.

## Main Concepts

Gatling is a tool you can use to execute load and performance tests. It can be used as a standalone application or integrated into a Maven or Gradle-based project.

Gatling is based on Scala, the [Netty](https://en.wikipedia.org/wiki/Netty_(software)) framework, and the [Akka](https://doc.akka.io/docs/akka/current/typed/guide/index.html) toolkit. It has an asynchronous, non-blocking architecture, which allows for high performance with minimum wasting of resources.

You can define tests by Gatling's flexible domain-specific language. You can also use its recorder function with a Graphical User Interface to capture user interactions in the browser and generate Scala scripts that can be modified and launched to perform a simulation.

In this article, you will learn how to integrate Gatling in a Spring Boot web application based on Maven. You will define a load test by its DSL, and then run it using the Gatling Maven plugin.

With Gatling, you can perform performance tests in a variety of ways. For instance, you can implement:

<ul><li><b>Load Testing</b>: to see how a system performs under a specific load</li><li><b>Stress Testing</b>: to find the breaking point of a system, raising the load progressively</li><li><b>Soak Testing</b>: running the system with a steady load for a long time to find its pitfalls</li><li><b>Spike Testing</b>: to see how the system performs when swiftly raising the load to a peak and then going down</li></ul>

The basic components by which Gatling implements the features described above are:

<ul><li><b>Scenarios</b>: a series of steps performed by a virtual user</li><li><b>Feeders</b>: how data is provided to feed the scenarios</li><li><b>Injection</b>: a sort of a blueprint that states how the test is performed, in terms of number of virtual users, how they change in time, and so on</li></ul>

## Spring Boot Gatling Integration

In this article, you will start with a simple Spring Boot web application and implement and run a load test over it. You can find the source code of this sample application on [GitHub](https://github.com/mcasari/codingstrain/tree/main/spring-cloud-sample-libraryapp/libraryapp-testing-gatling-test).

Imagine you have a library and want to insert new books by their title. You can implement this minimal requirement using JPA by defining a Book entity, a repository class, a service class, and a controller with a [REST](https://codingstrain.com/spring-boot-for-cloud-rest-api-development/) service mapping.

The REST service is defined as a POST call to a /book endpoint that saves a new book object. You can see the implementation in the code below:

```java
@RestController
@RequestMapping("/library")
public class BookController {

    Logger logger = LoggerFactory.getLogger(BookController.class);

    @Autowired
    BookService bookService;

    @PostMapping(value = "/book", consumes = "application/json", produces = "application/json")
    public Book createPerson(@RequestBody Book book) {
        return bookService.save(book);
    }

}
```

To perform a load test on the above REST endpoint, you need to integrate Gatling. You can do this by setting some Maven dependencies first:

```xml
<dependency>
    <groupId>io.gatling</groupId>
    <artifactId>gatling-app</artifactId>
    <version>3.7.2</version>
</dependency>

			
<dependency>
    <groupId>io.gatling.highcharts</groupId>
    <artifactId>gatling-charts-highcharts</artifactId>
    <version>3.7.2</version>
</dependency>	

<dependency>
    <groupId>com.github.javafaker</groupId>
    <artifactId>javafaker</artifactId>
    <version>0.15</version>
</dependency>	
```

Then you also need a Maven plugin to execute the test:

```xml
<plugin>
    <groupId>io.gatling</groupId>
    <artifactId>gatling-maven-plugin</artifactId>
    <version>4.2.9</version>
    <configuration>
<simulationClass>com.codingstrain.springcloud.sample.libraryapp.books.BookSaveSimulation</simulationClass>
    </configuration>
</plugin>
```

## Load Test Implementation

To implement a test, you need to extend the `io.gatling.javaapi.core.Simulation` class, as in the `BookSaveSimulation` class below:

```java
import static io.gatling.javaapi.core.CoreDsl.StringBody;
import static io.gatling.javaapi.core.CoreDsl.global;
import static io.gatling.javaapi.core.CoreDsl.rampUsersPerSec;
import static io.gatling.javaapi.http.HttpDsl.http;

import java.time.Duration;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.stream.Stream;

import com.github.javafaker.Faker;

import io.gatling.javaapi.core.CoreDsl;
import io.gatling.javaapi.core.OpenInjectionStep.RampRate.RampRateOpenInjectionStep;
import io.gatling.javaapi.core.ScenarioBuilder;
import io.gatling.javaapi.core.Simulation;
import io.gatling.javaapi.http.HttpDsl;
import io.gatling.javaapi.http.HttpProtocolBuilder;


public class BookSaveSimulation extends Simulation {


    public BookSaveSimulation() {

        setUp(buildPostScenario()
            .injectOpen(injection())
            .protocols(setupProtocol())).assertions(global().responseTime()
          .max()
          .lte(10000), global().successfulRequests()
          .percent()
          .gt(90d));
    }

    private static ScenarioBuilder buildPostScenario() {
        return CoreDsl.scenario("Load POST Test")
            .feed(feedData())
            .exec(http("create-book").post("/library/book")
            .header("Content-Type", "application/json")
                .body(StringBody("{ \"title\": \"${title}\" }")));
    }

    private static Iterator &lt;Map&lt;String, Object&gt;&gt; feedData() {
        Faker faker = new Faker();
        Iterator&lt;Map&lt;String, Object&gt;&gt; iterator;
        iterator = Stream.generate(() -&gt; {
              Map&lt;String, Objectglt; stringObjectMap = new HashMap<>();
            stringObjectMap.put("title", faker.book()
                .title());
              return stringObjectMap;
          })
          .iterator();
        return iterator;
    }

    private static HttpProtocolBuilder setupProtocol() {
        return HttpDsl.http.baseUrl("http://localhost:8080")
          .acceptHeader("application/json")
          .maxConnectionsPerHost(10)
            .userAgentHeader("Performance Test");
    }

    private RampRateOpenInjectionStep injection() {
        int totalUsers = 100;
        double userRampUpPerInterval = 10;
        double rampUpIntervalInSeconds = 30;

        int rampUptimeSeconds = 300;
        int duration = 300;
        return rampUsersPerSec(userRampUpPerInterval / (rampUpIntervalInSeconds)).to(totalUsers)
            .during(Duration.ofSeconds(rampUptimeSeconds + duration));
    }
}
```

The `BoookSaveSimulation` class uses its constructor to do all the settings using the parent class `setUp` method. It first implements a scenario. Since the test's purpose is to simulate a real situation in production, the scenario represents the steps performed by a configured number of virtual users interacting with the system.

The scenario in the example executes a POST call to the /library/book endpoint, sending a single title parameter in the payload. The invoked service will save a new book by the passed title value. A class named `com.github.javafaker.Faker` produces title values automatically and implements the feeder component described earlier in the `Main Concepts` section.

Then the `injectOpen` method defines how the virtual users are added to the simulation. The injectOpen method implements the injection part using the so-called open mode. There are two different models of injection, `open` and `closed`.

The open model simulates a scenario in which new users can be added constantly and independently from the execution state of the others. This is the model used in this article's example. On the other hand, in the closed model, new users can be added only when all the others have terminated their tasks. This helps simulate a steady load on the system.

The open injection configuration in the example sets a total number of 100 users that are added progressively 10 at a time, every 30 seconds. Once all users have been added, the execution continues for 300 seconds.

The protocols method sets up the base URL, the data type expected in the response, the maximum number of connections per host, and the User-Agent header.

The last part of this set-up phase defines a couple of assertions to consider the test passed: a maximum response time lower than 10 seconds and a percentage of successful requests greater than 90%.

## How to Run the Test

To run the test, you first have to start the Spring Boot web application. You can do this, for instance, by going to the project base directory and execute the following command: `mvn spring-boot:run`. 

Once the application is started, you can run the Gatling simulation by executing `mvn gatling:test`.

## How to See the Results

Once the test is terminated, you will find an index.html in the /target/gatling directory with all the measurements and several graphs.

The figure below displays all the results. It shows a list of the assertions and their outcome. Then, you can see the total number of requests, and how many requests have a positive or negative result. You have useful information about the response time: minimum, maximum, average, and standard deviation, and you also have the 50th, 75th, 95th, and 99th percentiles.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Summary.png)
_Summary of the test results_

A chart shows the number of requests, with positive and negative outcomes, in a particular response time range, as in the following figure.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/GlobalInfo.png)
_Number of requests in particular response time ranges_

Another graph shows the number of requests per second and how it changes depending on the number of active users.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/RequestsPerSecond.png)
_Number of request per second and active users over time_

You can also see in the next figure how the percentiles change over time, and with the number of active users at each point in time.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Percentiles.png)

## Conclusion

Evaluating the performance of a system is a complex task. Gatling makes things easy enough to integrate this kind of task with continuous integration. It gives you a comprehensive view and allows you to tweak the tests to find weaknesses and suggest solutions.

  

