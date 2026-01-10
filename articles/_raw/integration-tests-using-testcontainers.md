---
title: How to Emulate Real Dependencies in Integration Tests using Testcontainers
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-08-14T19:55:12.123Z'
originalURL: https://freecodecamp.org/news/integration-tests-using-testcontainers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723631770942/c82aabb6-a9b4-4085-8b06-b4ba1b1cdbd3.png
tags:
- name: Testing
  slug: testing
- name: Go Language
  slug: go
- name: Docker
  slug: docker
- name: containers
  slug: containers
seo_title: null
seo_desc: 'What is Integration Testing?

  The purpose of integration tests is to validate that different software components,
  subsystems, or applications work well together combined as a group.

  It’s an important step in the testing pyramid that can help you ident...'
---

## What is Integration Testing?

The purpose of integration tests is to validate that different software components, subsystems, or applications work well together combined as a group.

It’s an important step in the testing pyramid that can help you identify any issues that arise when components are combined – for example compatibility issues, data inconsistence, or communication issues.

This article is a hands-on guide to integration Tests in Go using Testcontainers. We'll define integrations tests as tests of communication between a backend application and external components such as the database and cache.

## Table of Contents

* [Different Ways to Run Integration Tests](#heading-different-ways-to-run-integration-tests)
    
* [Our Guinea Pig Service: a Simple URL Shortener](#heading-our-guinea-pig-service-a-simple-url-shortener)
    
* [Unit Tests with Mocked Dependencies](#heading-unit-tests-with-mocked-dependencies)
    
* [Integration Tests with Real Dependencies](#heading-integration-tests-with-real-dependencies)
    
* [Integration Tests with Testcontainers](#heading-integration-tests-with-testcontainers)
    
* [How Testcontainers Work](#heading-how-testcontainers-work)
    
* [Conclusion](#heading-conclusion)
    
* [Resources](#heading-resources)
    

## Different Ways to Run Integration Tests

![Testing pyramid](https://miro.medium.com/v2/resize:fit:700/0*AbYCn0k0XzRIk3wR.png align="left")

This diagram shows only 3 types of tests – but there are other kinds as well: components tests, system tests, load testing, and so on.

While unit tests are easy to run (you just execute tests as you would execute your code), integration tests usually require some scaffolding (spin up temporary testing environment with databases and other dependencies). In the companies where I've worked, I’ve seen the following approaches to address the integration testing environment problem.

**Option 1:** Using throwaway databases and other dependencies, which must be provisioned before the integration tests start and destroyed afterwards.

Depending on your application complexity, the effort involved in this option can be quite high, as you must ensure that the infrastructure is up and running and data is pre-configured in a specific desired state.

**Option 2:** Using the existing shared databases and other dependencies. You may create a separate environment for integration tests or even use the existing one (staging for example) that integration tests can use.

But there are many disadvantages here, and I would not recommend it. Because it is a shared environment, multiple tests can run in parallel and modify the data simultaneously. So you may end up with inconsistent data state for multiple reasons.

**Option 3:** Using in-memory or embedded variations of the required services for integration testing. While this is a good approach, not all dependencies have in-memory variations, and even if they do, these implementations may not have the same features as your production database.

**Option 4:** Using [Testcontainers](https://testcontainers.com/) to bootstrap and manage your testing dependencies right inside your testing code. This ensures a full isolation between test runs, reproducibility and better CI experience. We will dive into that in a second.

## Our Guinea Pig Service: a Simple URL Shortener

To demonstrate the tests, we'll use a super simple URL shortener API written in Go. It uses MongoDB for data storage and Redis as a [read-through cache](https://www.enjoyalgorithms.com/blog/read-through-caching-strategy). It has two endpoints which we’ll be testing in our tests:

* `/create?url=` generates the hash for a given URL and stores it in the database.
    
* `/get?key=` returns the original URL for a given key.
    

We won’t delve into the details of the endpoints much, but you can find the full code in [this Github repository](https://github.com/plutov/packagemain/blob/master/testcontainers-demo/main.go). Still, let’s see how we define our “server“ struct:

```go
type server struct {
  DB    DB
  Cache Cache
}

func NewServer(db DB, cache Cache) (*server, error) {
  if err := db.Init(); err != nil {
    return nil, err
  }
  if err := cache.Init(); err != nil {
    return nil, err
  }
  return &server{DB: db, Cache: cache}, nil
}
```

The **NewServer** function allows us to initialize a server with the database and cache instances that implement DB and Cache interfaces.

```go
type DB interface {
  Init() error
  StoreURL(url string, key string) error
  GetURL(key string) (string, error)
}

type Cache interface {
  Init() error
  Set(key string, val string) error
  Get(key string) (string, bool)
}
```

## Unit Tests with Mocked Dependencies

Because we had all dependencies defined as interfaces, we can easily generate mocks for them using [mockery](https://github.com/vektra/mockery) and use them in our unit tests.

```bash
mockery --all --with-expecter
go test -v ./...
```

With the help of unit tests, we can cover quite well the low level components of our application: endpoints, hash key logic, and so on. All we need is to mock the function calls of database and cache dependencies.

unit\_test.go:

```go
func TestServerWithMocks(t *testing.T) {
  mockDB := mocks.NewDB(t)
  mockCache := mocks.NewCache(t)

  mockDB.EXPECT().Init().Return(nil)
  mockDB.EXPECT().StoreURL(mock.Anything, mock.Anything).Return(nil)
  mockDB.EXPECT().GetURL(mock.Anything).Return("url", nil)

  mockCache.EXPECT().Init().Return(nil)
  mockCache.EXPECT().Get(mock.Anything).Return("url", true)
  mockCache.EXPECT().Set(mock.Anything, mock.Anything).Return(nil)

  s, err := NewServer(mockDB, mockCache)
  assert.NoError(t, err)

  srv := httptest.NewServer(s)
  defer srv.Close()

  // actual tests happen here, see the code in the repository
  testServer(srv, t)
}
```

`mocks.NewDB(t)` and `mocks.NewCache(t)` have been auto-generated by mockery and we use `EXPECT()` to mock the functions. Notice that we created a separate function `testServer(srv, t)` that we will use later in other tests as well, but providing a different server struct.

As you may already understand, these unit tests are not testing the communications between our application and our database/cache, and we may easily miss some very critical bugs.

To be more confident with our application, we should write integration tests along with unit tests to ensure that our application is fully functional.

## Integration Tests with Real Dependencies

As Option 1 and 2 mention above, we can provision our dependencies beforehand and run our tests against these instances. One option would be to have a Docker Compose configuration with MongoDB and Redis, which we start before the tests and shutdown after. The seed data could be a part of this configuration, or done separately.

compose.yaml:

```go
services:
  mongodb:
    image: mongodb/mongodb-community-server:7.0-ubi8
    restart: always
    ports:
      - "27017:27017"

  redis:
    image: redis:7.4-alpine
    restart: always
    ports:
      - "6379:6379"
```

realdeps\_test.go:

```go
//go:build realdeps
// +build realdeps

package main

func TestServerWithRealDependencies(t *testing.T) {
  os.Setenv("MONGO_URI", "mongodb://localhost:27017")
  os.Setenv("REDIS_URI", "redis://localhost:6379")

  s, err := NewServer(&MongoDB{}, &Redis{})
  assert.NoError(t, err)

  srv := httptest.NewServer(s)
  defer srv.Close()

  testServer(srv, t)
}
```

Now these tests don’t use mocks, but simply connect to the already provisioned database and cache. Note: we added a “realdeps“ build tag so these tests should be executed by specifying this tag explicitly.

```bash
docker-compose up -d
go test -tags=realdeps -v ./...
docker-compose down
```

## Integration Tests with Testcontainers

However, creating reliable service dependencies using Docker Compose requires good knowledge of Docker internals and how to best run specific technologies in a container. For example, creating a dynamic integration testing environment may result in port conflicts, containers not being fully running and available, and so on.

With Testcontainers, we can now do the same – but inside our test suite, using our language API. This means we can control our throwaway dependencies better and make sure they’re isolated per each test run. You can run pretty much anything in Testcontainers, as long as it has a Docker-API compatible container runtime.

integration\_test.go:

```go
//go:build integration
// +build integration

package main

import (
  "context"
  "net/http/httptest"
  "os"
  "testing"
  "github.com/stretchr/testify/assert"
  "github.com/testcontainers/testcontainers-go/modules/mongodb"
  "github.com/testcontainers/testcontainers-go/modules/redis"
)

func TestServerWithTestcontainers(t *testing.T) {
  ctx := context.Background()

  mongodbContainer, err := mongodb.Run(ctx, "docker.io/mongodb/mongodb-community-server:7.0-ubi8")
  assert.NoError(t, err)
  defer mongodbContainer.Terminate(ctx)

  redisContainer, err := redis.Run(ctx, "docker.io/redis:7.4-alpine")
  assert.NoError(t, err)
  defer redisContainer.Terminate(ctx)

  mongodbEndpoint, _ := mongodbContainer.Endpoint(ctx, "")
  redisEndpoint, _ := redisContainer.Endpoint(ctx, "")

  os.Setenv("MONGO_URI", "mongodb://"+mongodbEndpoint)
  os.Setenv("REDIS_URI", "redis://"+redisEndpoint)

  s, err := NewServer(&MongoDB{}, &Redis{})
  assert.NoError(t, err)

  srv := httptest.NewServer(s)
  defer srv.Close()

  testServer(srv, t)
}
```

This is very similar to the previous test: we just initialized two containers at the top of our test.

The first run may take a while to download the images. But the subsequent runs are almost instant.

![Test run output using Testcontainers](https://miro.medium.com/v2/resize:fit:700/0*A3NirSvt1jkADZjq.png align="left")

## How Testcontainers Work

To run tests with Testcontainers, you need a Docker-API compatible container runtime or to install Docker locally. Try stopping your Docker engine and it won’t work.

But this should not be an issue for most developers, because having a Docker runtime in your CI/CD or locally is a very common practice nowadays. You can easily have this environment in Github Actions, for example.

When it comes to supported languages, Testcontainers support a big list of popular languages and platforms including Java, .NET, Go, NodeJS, Python, Rust, Haskell, and others.

There is also a growing list of preconfigured implementations (called modules) which you can find [here](https://testcontainers.com/modules/). But as I mentioned earlier, you can run any Docker image.

In Go, you could use the following code to provision Redis instead of using a preconfigured module:

```go
// Using available module
redisContainer, err := redis.Run(ctx, "redis:latest")

// Or using GenericContainer
req := testcontainers.ContainerRequest{
  Image:        "redis:latest",
  ExposedPorts: []string{"6379/tcp"},
  WaitingFor:   wait.ForLog("Ready to accept connections"),
}

redisC, err := testcontainers.GenericContainer(ctx, testcontainers.GenericContainerRequest{
  ContainerRequest: req,
  Started:          true,
})
```

## Conclusion

While the development and maintenance of integration tests require significant effort, they are crucial part of the SDLC ensuring that components, subsystems, or applications work well together combined as a group.

Using Testcontainers, we can simplify the provisioning and de-provisioning of throwaway dependencies for testing, making the test runs fully isolated and more predicatble.

## Resources

* [Github repository](https://github.com/plutov/packagemain/blob/master/testcontainers-demo)
    
* [Testcontainers](https://testcontainers.com/)
    
* [Discover more articles from packagemain.tech](https://packagemain.tech)
