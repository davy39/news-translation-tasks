---
title: How to Get Started with Golang – a Developer Roadmap
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-14T14:01:00.000Z'
originalURL: https://freecodecamp.org/news/golang-developer-roadmap
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/go-roadmap-fcc.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: null
seo_desc: "By Shubham Chadokar\nThe Go programming language – also known as Golang\
  \ – is now almost 15 years old. And it's become a popular choice for web development\
  \ and microservices thanks to its performance and efficient resource utilisation.\
  \ \nGo jobs are als..."
---

By Shubham Chadokar

The Go programming language – also known as Golang – is now almost 15 years old. And it's become a popular choice for web development and microservices thanks to its performance and efficient resource utilisation. 

Go jobs are also quite well-paid. As per the [Glassdoor report](https://www.glassdoor.com/Salaries/golang-developer-salary-SRCH_KO0,16.htm?countryPickerRedirect=true), the average salary of a Go developer is around $103k in the USA, and can be as high as $200k.

Ready to kick off your Go developer journey? This roadmap can be your guide.  
In it, I aimed to outline as many points as I could. For each point, I've included comments and examples to explain it thoroughly. The references provided at the end cover all the points.

Here what we are going to cover:

1. [Why Should You Learn Go?](#heading-why-should-you-learn-go)
2. [How to Install Go](#heading-how-to-install-go)
3. [Basics of Go](#heading-basics-of-go)
4. [Advanced Concepts](#heading-advanced-concepts)
5. [Web Development in Go](#heading-web-development-in-go)
6. [Logging, Testing, Benchmarking, and Debugging](#heading-logging-testing-benchmarking-and-debugging)
7. [How to Build Scalable Microservices](#heading-how-to-build-scalable-microservices)
8. [How to Build Command Line Tools (CLI)](#heading-how-to-build-command-line-tools)
9. [Projects to Sharpen Your Go Skills](#heading-projects-to-sharpen-your-go-skills)
10. [What's Next?](#heading-whats-next)
11. [References](#heading-references)

## 🎯 Why Should You Learn Go?

Go was first introduced in late 2009. It is an open-source, statically typed, compiled high-level programming language designed at Google. It's a popular choice for building secure and scalable systems.

According to the annual [StackOverflow survey](https://survey.stackoverflow.co/2023/), it is one of the most popular and well-loved programming languages. Also, in the [Tiobe Index 2024](https://www.tiobe.com/tiobe-index/), Go currently holds the 11th position, and its position has been improving steadily each year.

Go is a popular choice for building scalable and efficient services and APIs. It is widely used for microservices architecture due to its small memory footprint, fast compilation, and high performance.

Due to its built-in support for concurrency through goroutines and channels, it is a popular choice for blockchain development. For example, Ethereum and Hyperledger Fabric are written in Go.

Your favourite software like Docker, Kubernetes, Hugo, GitHub CLI, Prometheus, Terraform, and many more are also written in Go.

And companies like Google, Meta, Netflix, and Uber all use Go.

You can check out the following resources to learn more:

* [go.dev](https://go.dev/solutions/case-studies)
* [stackshare](https://stackshare.io/golang)

## How to Install Go

You can install Go to your respective OS from [here](https://go.dev/dl/). 

Test the installation using the `go version` command:

```bash
$ go version
go version go1.21.4 darwin/arm64
```

If you get some error, then check the environment variables.

## Basics of Go 

First, let's start with understanding the basic syntax of running a Go program. The program starts from the package `main` and the function `main`. The files are saved with a `.go` extension. 

In Go, a package is a fundamental unit for structuring and managing code. You can use the `import` keyword to import any package. For example, to print you can use the `fmt` or `log` package. 

This is a simple message printing program in Go:

```go
// main.go
package main

import "fmt"

func main() {
	fmt.Println("freecodecamp")
}
```

To run the program use `go run <filename>.go`.

```bash
$ go run main.go
freecodecamp
```

Now, you can start learning about the following topics:

* **Basic Data types:** int, float, bool, string, array
* **Reference Data types:** channel, map, slices
* **Variables and Constants**
* **Conditional Statements:** if, if else, switch
* **Iteration Statement:** for (only "for" is available, no "while")
* **Type Casting and Inference:** there is no implicit type conversion available
* **Export Function:** Exporting a function is done by capitalising its first letter
* **Module:** Initialising the module. Learn commands under `go mod`.
* **Importing third party packages:** Using `go get <gitrepo_url>.git`
* **Basic keywords:** `make`, `new`, `range`, `defer`

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-14-at-9.58.31-PM.png)

Many of these concepts are covered in [this beginner's guide](https://www.freecodecamp.org/news/golang-for-beginners/). And if you want to dive even deeper, [here's a full handbook](https://www.freecodecamp.org/news/learn-golang-handbook/) that covers basic Go concepts in detail.

## Advanced Concepts

To harness the Go's potential to build a scalable and distributed system, it's essential to have a solid understanding of its core features.

These are Go's core features:

* Functions & Packages
* Concurrency and Goroutines
* Channels
* Context Management
* Error Handling
* Pointers and Memory Management
* Garbage Collection (You can tweak default GC to get a performance boost)
* Concurrency Patterns
* Mutexes
* Waitgroups

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-14-at-9.57.15-PM.png)

If you want to go more in-depth into all these important Go concepts, [here's a free 10-hour course for you](https://www.freecodecamp.org/news/go-programming-video-course/).

## Web Development in Go

With a rich standard library, built-in concurrency, and excellent performance, Go is an ideal choice for web development. Beyond its built-in packages, the Go ecosystem offers a variety of web development frameworks and packages to choose from. 

Here are some well-known frameworks and packages:

* net/http (built-in package)
* [gorilla/mux](https://github.com/gorilla/mux)
* [gin](https://github.com/gin-gonic/gin)
* [chi](https://github.com/go-chi/chi)
* [fiber](https://github.com/gofiber/fiber)
* [echo](https://github.com/labstack/echo)

All are well-known frameworks, and you can start with any of them. A few follow the `net/http` pattern and a few are inspired by Express or other frameworks.

## Logging, Testing, Benchmarking, and Debugging

The language provides a comprehensive logging package `log` for effective monitoring, as well as a built-in testing and benchmarking package. You should understand effective debugging techniques for identifying and resolving issues in the code.

### Logging in Go

The standard `log` package is a great starting point. It is easily configurable to include file path, log type, and any custom message in the log message. 

Besides this, there are many loggers available. These loggers follow industry standards of logging and are highly performant compared to standard `log` package.

Here are some of the available loggers: 

* [uber-go/zap](https://github.com/uber-go/zap)
* [logrus](https://github.com/sirupsen/logrus)
* [zerolog](https://github.com/rs/zerolog)
* [apex/log](https://github.com/apex/log)
* [slog (standard package)](https://go.dev/blog/slog)

### Testing and Benchmarking in Go

The built-in testing framework `testing` provides support for writing tests and benchmarks. 

The `go test` command is used to run the tests and the benchmarks. You can add tests and benchmarks in a file ending in `_test.go`. 

To write a test, use `testing.T` and follow the function naming convention `TestXxx`. 

For example, to write a test for `fibonaci` function, its test function name would be `TestFibonaci` where `Test` is the keyword which tells the Go compiler that it is a test function, and `Fibonaci` is the function name. Remember to capitalise the first letter of test function name, `Fibonaci`.

You can read more about [adding tests to you Go code here](https://go.dev/doc/tutorial/add-a-test).

To write a benchmark, use `testing.B` and follow the function naming convention `BenchmarkXxx`. Benchmarking is used to measure the performance of functions or code snippets. 

So to write a benchmark for the `fibonaci` function, its benchmark function name would be `BenchmarkFibonaci`, where `Benchmark` is the keyword which tells the Go compiler that it is a benchmark function, and `Fibonaci` is the function name.

You can [learn more about benchmarking in Go here](https://www.practical-go-lessons.com/chap-34-benchmarks).

If you're accustomed to assertion functions, then you can try the `testify` package. It is an external package which improves the readability of test cases. Internally it is using the built-in `testing` package.

### Debugging in Go

[Delve](https://github.com/go-delve/delve) is a powerful debugger available for the Go. It easily integrates with popular IDEs like Visual Studio Code, Goland by JetBrains, Neovim, Atom, and so on. 

You can use the built-in `pprof` package to analyse and identify performance bottlenecks and memory usage issues. Its path is `net/http/pprof`. 

## How to Build Scalable Microservices

Building scalable microservices requires a combination of thoughtful architecture, efficient coding practices, and robust tooling. 

Go's lightweight concurrency model, efficient runtime, and rich standard library can handle high traffic loads and scale horizontally, which makes it an ideal choice for microservices.

Following are some topics you can start with:

* [Microservice Fundamentals](https://martinfowler.com/tags/microservices.html)
* Communication Protocols ([REST APIs](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/), [gRPC](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/), [WebSockets](https://www.freecodecamp.org/news/beginners-guide-to-websockets/))
* [Service Discovery](https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/)
* [Pub-Sub model](https://cloud.google.com/pubsub/docs/overview)
* [Message Queues](https://www.freecodecamp.org/news/message-queues-in-distributed-systesms/) ([Apache Kafka](https://www.freecodecamp.org/news/apache-kafka-handbook/), [RabbitMQ](https://www.freecodecamp.org/news/message-queues-with-rabbitmq-in-nest-js/))

## How to Build Command Line Tools

When it comes to CLIs, Go is a rockstar. There are packages available in Go to build CLIs very easily. The built-in `flag` can be used to build the basic CLI. 

The [Cobra](https://github.com/spf13/cobra) package is very popular for creating powerful modern CLI applications. Many Go projects like GitHub CLI, Hugo, and Kubernetes use Cobra.

Here are some CLI projects you can build to practice:

* **Task Manager:** Develop a CLI-based task manager that allows CRUD operations. 
* **Notes:** Build a CLI to take notes. 
* **Password Manager:** Create a CLI that securely stores and manages passwords with proper encryption, password generation and retrieval.
* **Universal Conversion Tool:** Build a universal convertor, which can convert all metrics, and currency.

## Projects to Sharpen Your Go Skills

To understand more about Go's capabilities, you can gain practical hands-on experience by building projects.

Here's a list of projects you can build in Go:

* Todo application
* Chat Application
* CLI
* Microservices which communicate using gRPC
* Containerizing a Go application
* Create a blogging website
* Webscraper using `net/http` and `goquery` package
* Rate limiter
* Email Template generator using `template` package

If you'd like more practice building projects with Go, [here's a full free course](https://www.freecodecamp.org/news/learn-go-by-building-11-projects/) that walks you through building 11 Go projects.

## What's Next?

For your next steps, you can follow this amazing **[Go Roadmap](https://roadmap.sh/golang)** created by Kamran. 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/go-roadmap.png)
_Go Roadmap_

### References

* [Go Official Documentation](https://golang.org/doc/)
* [Effective Go](https://github.com/golang/go)
* [Go Tour](https://go.dev/tour/list)
* [Gobyexample](https://gobyexample.com/)
* [PracticeGo](https://www.youtube.com/@practicego)
* [Microservices](https://martinfowler.com/tags/microservices.html)
* [Create a CLI with cobra](https://medium.com/towards-data-science/how-to-create-a-cli-in-golang-with-cobra-d729641c7177)
* [Create a Chat application](https://medium.com/gitconnected/create-a-chat-application-in-golang-with-redis-and-reactjs-c75611717f84)
* [StackOverflow Survey 2023](https://survey.stackoverflow.co/2023/)

😃 I hope you liked this article.

👋 I am Shubham Chadokar, Software Developer and Content Creator. You can follow me on Twitter(X) [@schadokar1](https://twitter.com/schadokar1) and subscribe to my YouTube channel [practicego](https://www.youtube.com/@practicego).

