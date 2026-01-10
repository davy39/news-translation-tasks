---
title: 'Make Your Own Web Server with Go: A Quick Guide'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T19:58:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-own-web-server-with-go
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e35740569d1a4ca3be7.jpg
tags:
- name: Go Language
  slug: go
- name: servers
  slug: servers
seo_title: null
seo_desc: 'The Go programming language is well-known for having a built-in web server.
  In this article you will learn how you can easily make your own web server with
  Go. You won’t need any other packages beside the ones that are already built in!

  First, hop in...'
---

The Go programming language is well-known for having a built-in web server. In this article you will learn how you can easily make your own web server with Go. You won’t need any other packages beside the ones that are already built in!

First, hop in to your text editor. Then create a file called `webserver.go` and enter the following code:

```go
package main

import (
  "net/http"
  "io"
)

func main() {
  http.HandleFunc("/", servePage)
	http.ListenAndServe(":8080", nil)
}

func servePage(writer http.ResponseWriter, reqest *http.Request) {
  io.WriteString(writer, "Hello world!")
}
```

Let’s break down the block of code above. We import the `net/http` package: this package contains the web server itself. Then we also import the `io` package, we will make use of this later to actually serve something to the client.

In the `main` function we do two things. First of all we instruct the server to let the function called `servePage` handle all incoming traffic to `/` - in this case it means that it handles requests to _any_ `URL`. 

The second thing we do is actually activating the server. We do this using a function named `ListenAndServe`. This function requires two parameters: the `port` (as `string`), in this case it’s `8080`, and the `handler` (as `Handler`) - however the last one isn’t important yet. We will just make it `nil` and everything will work just fine.

In the `servePage` we do just one simple thing, for now. Using the `io` package and the `WriteString` function that it contains we can respond to the clients’ request with the text `Hello world!` (or any other string, of course). 

You also might have noticed that the `servePage` function has two arguments: the `writer` and the `request`. With the writer you can actually respond to a `HTTP` request and with the `request` you may get more information about the request itself.

Congratulations! You just created your first web server! If you want to test it: just run `go run webserver.go`, fire up a browser and navigate to `http://localhost:8080`!

