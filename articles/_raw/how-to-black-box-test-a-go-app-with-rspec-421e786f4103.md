---
title: How to black box test a Go app with RSpec
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T23:06:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-black-box-test-a-go-app-with-rspec-421e786f4103
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3EftyhurldrDfAe0PuBHZQ.jpeg
tags:
- name: Go Language
  slug: go
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Dmitriy Lutsko

  Automated testing is all the rage in web development these days and goes on across
  the whole industry. A well-written test dramatically reduces the risk of accidentally
  breaking an application when you add new features or fix bugs. ...'
---

By Dmitriy Lutsko

Automated testing is all the rage in web development these days and goes on across the whole industry. A well-written test dramatically reduces the risk of accidentally breaking an application when you add new features or fix bugs. When you have a complex system that’s built from several components that interact with each other, it’s incredibly hard to test how each component interacts with other components.

Let’s take a look at how to write good automatic tests for developing components in Go and how to do so using the RSpec library in Ruby on Rails.

### Adding Go to our project’s tech stack

One of the projects that I’m working on at my company, [eTeam](https://eteam.io/), can be divided into an admin panel, user dashboard, report generator and request processor that handles requests from different services integrated into the application.

The part of the project that processes requests is the most important, thus we needed to maximize its reliability and availability.

As part of a monolithic application, there’s a high risk of a bug affecting the request processor, even when there are changes in code in parts of the app not related to it. Likewise, there’s a risk of crashing the request processor when other components are under a heavy load. The number of Ngnix workers for the app is limited, which can cause problems as the load increases. For instance, when a number of resource-intensive pages are opened at once in the admin panel, the processor slows down or even crashes the entire app.

These risks, as well as the maturity of the system in question — we didn’t have to make major changes for months — made this app an ideal candidate for creating a separate service to handle request processing.

We decided to write the separate service in Go, that shared the database access with the Rails application that remained responsible for changes in the table structure. With only two applications, such a scheme with a shared database works fine. Here’s what it looked like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*3dV9gtMm5kAMTzojZ2Y3hQ.jpeg)

We wrote and deployed the service in a separate Rails instance. This way, there was no need to worry that the request processor would be affected whenever the Rails app was deployed. The service directly accepts HTTP requests without Ngnix and doesn’t use a lot of memory. You could call it a minimalist app!

### The problem with unit testing in Go

We created unit tests for the Go application where all database requests were mocked. In addition to other arguments for this solution, the main Rails application was responsible for the database structure, thus the Go application didn’t actually have the information for creating a test database. Half of processing was business logic, while the other half was database queries, all of which were mocked.

Mocked objects are much less readable in Go than in Ruby. Whenever new functions were added for reading data from the database, we had to add mocked objects during many failed tests that had previously worked. In the end, such unit tests didn’t prove very effective and were extremely fragile.

### Our solution

In order to make up for these drawbacks, we decided to cover the service with functional tests in the Rails application and test the service in Go like a black box. White-box testing wouldn’t work in any case, since it was impossible to use Ruby to get inside the service and see whether a method was being called.

That also means that requests sent through the test service were also impossible to mock, thus we needed another application for managing and writing these tests. Something like RequestBin would work, but it had to work locally. We’d already written a utility that’d do the trick, so we decided to try using it.

This was the resulting setup:

1. RSpec compiles and runs the Go binary with the configuration in which access to the test database is specified along with a particular port for receiving HTTP requests, i.e 8082.
2. It also runs the utility, which records HTTP requests coming to port 8083.
3. We write regular tests in RSpec. This creates the necessary data in the database and sends a request to localhost:8082 as if it were an external service such as HTTParty.
4. We parse the response, check changes in the database, receive a list of requests that were recorded by the RequestBin substitute and check them.

### Details of the implementation

Here’s how we implemented this. As a demonstration, let’s call the test service TheService and create a wrapper:

It’s worth mentioning that autoloading files have to be configured in the support folder when using RSpec:

```
Dir[Rails.root.join('spec/support/**/*.rb')].each {|f| require f}
```

The start method:

* Reads the configuration information necessary to start TheService. This information can differ among different developers and therefore is excluded from Git. The configuration contains the necessary settings for starting the program. All of these different configurations are in a single place so you don’t have to create unnecessary files.
* Compiles and runs through `go run <path to main.go> <path t`o config>
* Polls every second and waits until TheService is ready to accept requests.
* Records the identifier of each process in order to not repeat anything and to have the ability to stop a process.

The configuration itself:

The “stop” method simply stops the process. There’s a gotcha though! Ruby runs a “go run” command, which compiles TheService and launches a binary in a child process with an unknown ID. If we just stop the process that’s running in Ruby, the child process doesn’t stop automatically and the port will remain in use. Thus stopping TheService has to go through the Process Group ID:

Next we prepare the “shared_context” where we define the default variables, start TheService if it hasn’t already been launched and temporarily turn off VCR since VCR would see what we’re doing as an external service request, but we don’t want VCR to mock requests at this point:

And now we can look at writing the specs themselves:

TheService can make HTTP requests to external services. We can configure it to redirect requests to the local utility that logs them. For this utility, there’s also a wrapper for starting and stopping it that’s similar to ‘TheServiceControl’, except that this utility can just be started as a binary without compilation.

### Additional highlights

The Go application was written so that all the logs and debugging information would be sent to STDOUT. On production, this output is sent to a file. When launching from RSpec the log is displayed in the console, which really helps with debugging.

If you specifically run the specs that don’t need TheService, then it won’t start.

In order not to waste time on launching TheService each time whenever a spec changes, during the development process you can launch TheService manually in the terminal and simply not turn it off. Whenever it’s necessary, you can even launch it in an IDE debugging mode. Then the specs prepare everything, send the request to the service, it stops and you can easily debug it. This makes the TDD approach really convenient.

### Conclusion

We’ve been using this setup for about a year now and haven’t experienced any failures with it. The specs come out far more readable than unit testing in Go, and they don’t rely on knowing the internal structure of the service. If we, for some reason, need to rewrite the service in another language, then we won’t need to change the specs. Only the wrappers, which are used for launching the test service with a different command would need to be rewritten.

