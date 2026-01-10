---
title: How to Create a Rate Limiter using Bucket4J and Redis
subtitle: ''
author: Abhinav Pandey
co_authors: []
series: null
date: '2022-04-01T19:05:04.000Z'
originalURL: https://freecodecamp.org/news/rate-limiting-with-bucket4j-and-redis
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Rate-Limiter-with-Bucket4J-and-Redis.png
tags:
- name: api
  slug: api
- name: Redis
  slug: redis
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'In this tutorial we will learn how to implement rate limiting in a scaled
  service.We will use the Bucket4J library to implement it and we will use Redis as
  a distributed cache.

  Why Use Rate Limiting?

  Let''s get started with some basics to make sure we...'
---

In this tutorial we will learn how to implement rate limiting in a scaled service.  
We will use the [Bucket4J](https://github.com/vladimir-bukhtoyarov/bucket4j) library to implement it and we will use [Redis](https://redis.io/) as a distributed cache.

## Why Use Rate Limiting?

Let's get started with some basics to make sure we understand the need for rate limiting and introduce the tools we'll be using in this tutorial.

### Problem with Unlimited Rates

If a public API like the Twitter API allowed its users to make an unlimited number of requests per hour, it could lead to:

* resource exhaustion
* decreasing quality of the service
* denial of service attacks

This might result in a situation where the **service is unavailable or slow**. It could also lead to more **unexpected costs** being incurred by the service.

### How Rate Limiting Helps

Firstly, rate-limiting can prevent denial of service attacks. When coupled with a deduplication mechanism or API keys, rate limiting can also help prevent distributed denial of service attacks.

Secondly, it helps in estimating traffic. This is very important for public APIs. This can also be coupled with automated scripts to monitor and scale the service.

And thirdly, you can use it to implement tier-based pricing. This type of pricing model means that users can pay for a higher rate of requests. The Twitter API is an example of this.

### The Token Bucket Algorithm

Token Bucket is an algorithm that you can use to implement rate limiting. In short, it works as follows:

1. A bucket is created with a certain capacity (number of tokens).
2. When a request comes in, the bucket is checked. If there is enough capacity, the request is allowed to proceed. Otherwise, the request is denied.
3. When a request is allowed, the capacity is reduced.
4. After a certain amount of time, the capacity is replenished.

### How to Implement Token Bucket in a Distributed System

To implement the token bucket algorithm in a distributed system, we need to use a **distributed cache**.

The cache is a **key-value store** to store the bucket information. We will use a Redis cache to implement this.

Internally, Bucket4j allows us to plug in any implementation of the Java JCache API. The [Redisson](https://redisson.org/) client of Redis is the implementation we will use.

## Project Implementation

We will use the [Spring Boot](https://spring.io/projects/spring-boot) framework to build our service.

Our service will contain the below components:

1. A simple REST API.
2. A Redis cache connected to the service – using the Redisson client.
3. The Bucket4J library wrapped around the REST API.
4. We'll connect Bucket4J to the JCache interface which will use the Redisson client as the implementation in the background.

First, we will learn to rate limit the API for all requests. Then we will learn to implement a more complex rate limiting mechanism per user or per pricing tier.

Let's start with the project setup.

### Install Dependencies

Let's add the below dependencies to our _pom.xml_ (or _build.gradle_) file.

```xml
<dependencies>
    <!-- To build the Rest API -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- Redisson Starter = Spring Data Redis starter(excluding other clients) and Redisson client -->
    <dependency>
        <groupId>org.redisson</groupId>
        <artifactId>redisson-spring-boot-starter</artifactId>
        <version>3.17.0</version>
    </dependency>
    
    <!-- Bucket4J starter = Bucket4J + JCache -->
    <dependency>
        <groupId>com.giffing.bucket4j.spring.boot.starter</groupId>
        <artifactId>bucket4j-spring-boot-starter</artifactId>
        <version>0.5.2</version>
    </dependency>
</dependencies>

```

### Cache Configuration

Firstly, we need to start our Redis server. Let's say we have a Redis server running on port 6379 on our local machine.

We need to perform two steps:

1. Create a connection to this server from our application.
2. Set up JCache to use the Redisson client as the implementation.

[Redisson's documentation](https://github.com/redisson/redisson/wiki/14.-Integration-with-frameworks/#144-jcache-api-jsr-107-implementation) provides concise steps to implement this in a regular Java application. We're going to implement the same steps, but in Spring Boot.

Let's look at the code first. We need to create a Configuration class to create the required beans.

```java
@Configuration
public class RedisConfig  {
    
    @Bean
    public Config config() {
        Config config = new Config();
        config.useSingleServer().setAddress("redis://localhost:6379");
        return config;
    }
    
    @Bean
    public CacheManager cacheManager(Config config) {
        CacheManager manager = Caching.getCachingProvider().getCacheManager();
        cacheManager.createCache("cache", RedissonConfiguration.fromConfig(config));
        return cacheManager;
    }

    @Bean
    ProxyManager<String> proxyManager(CacheManager cacheManager) {
        return new JCacheProxyManager<>(cacheManager.getCache("cache"));
    }
}

```

**What does this do?**

1. Creates a configuration object that we can use to create a connection.
2. Creates a cache manager using the configuration object. This will internally create a connection to the Redis instance and create a hash called "cache" on it.
3. Creates a proxy manager that will be used to access the cache. Whatever our application tries to cache using the JCache API, it will be cached on the Redis instance inside the hash named "cache".

### Build the API

Let's create a simple REST API.

```java
@RestController
public class RateLimitController {
    @GetMapping("/user/{id}")
    public String getInfo(@PathVariable("id") String id) {
        return "Hello " + id;
    }
}

```

If I hit the API with the URL `http://localhost:8080/user/1`, I will get the response `Hello 1`.

### Bucket4J Configuration

To implement the rate limiting, we need to configure Bucket4J. Thankfully, we do not need to write any boilerplate code due to the starter library.

It also **automatically detects the ProxyManager bean** we created in the previous step and uses it to cache the buckets.

What we do need to do is configure this library around the API we created.  
Again there are multiple ways to do this.

We can go for [property-based configuration](https://github.com/MarcGiffing/bucket4j-spring-boot-starter#configuration-via-properties) which is defined in the starter library.  
This is the most convenient way for simple cases like rate-limiting for all users or all guest users.

However, if we want to implement something more complex like a rate limit for each user, it's better to write custom code for it.

We are going to implement rate limiting per user. Let's assume we have the rate limit for each user stored in a database, and we can query it using the user id.

Let's write the code for it step by step.

#### Create a Bucket

Before we start, let's look at how a bucket is created.

```java
Refill refill = Refill.intervally(10, Duration.ofMinutes(1));
Bandwidth limit = Bandwidth.classic(10, refill);
Bucket bucket = Bucket4j.builder()
        .addLimit(limit)
        .build();

```

* **Refill** – After how much time the bucket will be refilled.
* **Bandwidth** – How much bandwidth the bucket has. Basically, requests per refill period.
* **Bucket** – An object configured using these two parameters. Additionally, it maintains a token counter to keep track of how many tokens are available in the bucket.

Using this as the building block, let's change a few things to make it suitable to our use case.

#### Create and Cache Buckets using ProxyManager

We created the proxy manager for the purpose of storing buckets on Redis. Once a bucket is created, it needs to be cached on Redis and does not need to be created again.

To make this happen, we will replace the `Bucket4j.builder()` with `proxyManager.builder()`. ProxyManager will take care of caching the buckets and not creating them again.

ProxyManager's builder takes two parameters – a **key** against which the bucket will be cached and a **configuration object** that it will use to create the bucket.

Let's see how we can implement it:

```java
@Service
public class RateLimiter {
    //autowiring dependencies
    
    public Bucket resolveBucket(String key) {
        Supplier<BucketConfiguration> configSupplier = getConfigSupplierForUser(key);
        
        // Does not always create a new bucket, but instead returns the existing one if it exists.
        return buckets.builder().build(key, configSupplier);
    }

    private Supplier<BucketConfiguration> getConfigSupplierForUser(String key) {
        User user = userRepository.findById(userId);
        Refill refill = Refill.intervally(user.getLimit(), Duration.ofMinutes(1));
        Bandwidth limit = Bandwidth.classic(user.getLimit(), refill);
        return () -> (BucketConfiguration.builder()
                .addLimit(limit)
                .build());
    }
}

```

We have created a method which returns a bucket for a key provided. In the next step, we will see how to use this.

#### How to Consume Tokens and Set Up Rate Limiting

When a request comes in, we will try to consume a token from the relevant bucket.  
We will use the `tryConsume()` method of the bucket to do this.

```java
@GetMapping("/user/{id}")
public String getInfo(@PathVariable("id") String id) {
    // gets the bucket for the user
    Bucket bucket = rateLimiter.resolveBucket(id);
    
    // tries to consume a token from the bucket
    if (bucket.tryConsume(1)) {
        return "Hello " + id;
    } else {
        return "Rate limit exceeded";
    }
}

```

The `tryConsume()` method returns `true` if the token was consumed successfully or `false` if the token was not consumed.

## How to Test our Service

We can test this using any automated testing technique. For example, we can use [JUnit](https://junit.org/). Let's write a test case that calls the `getInfo()` method multiple times and verifies that the response is correct.

Let's assume we have a user with id `1` and a limit of `10` requests per minute. Let's assume we also have a user with id `2` and a limit of `20` requests per minute.

We will hit 11 requests for both users and verify that the request fails for the user with id `1` but succeeds for the user with id `2`.

```java
@Test
public void testGetInfo() {

    // calls the method 10 times for user 1
    for (int i = 0; i < 10; i++) {
        rateLimiter.getInfo(1));
        rateLimiter.getInfo(2));
    }
    
    // verifies that the response is rate limited for user 1
    assertEquals("Rate limit exceeded", rateLimiter.getInfo(1));
    
    // verifies that the response is successful for user 2
    assertEquals("Hello 2", rateLimiter.getInfo(2));
}

```

When we run the test, we will see that the test passes.

## Conclusion

In this tutorial, we have covered how to create a rate limiter using Bucket4j and Redis in a Spring Boot application.We also looked at how to set up a Redisson client with JCache and how to use it to cache buckets.

At the end, we implemented a simple rate limiter which can be used to rate limit requests for specific users.

Hope you enjoyed this tutorial. Thanks for reading!

