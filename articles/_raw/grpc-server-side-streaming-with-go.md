---
title: How to Set Up gRPC Server-Side Streaming with Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T00:21:08.000Z'
originalURL: https://freecodecamp.org/news/grpc-server-side-streaming-with-go
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fb5449249c47664ed8226c5.jpg
tags:
- name: Go Language
  slug: go
seo_title: null
seo_desc: "By Pramono Winata\nHave you ever thought about returning multiple server\
  \ responses using only a single connection? Yes, that’s what this article is about.\
  \ \nToday I will be showing you how to implement gRPC server-side streaming with\
  \ Go.\n\nIt's okay, he..."
---

By Pramono Winata

Have you ever thought about returning multiple server responses using only a single connection? Yes, that’s what this article is about. 

Today I will be showing you how to implement gRPC server-side streaming with Go.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/7f6189eec678dc80b34e16ec51aa6133dcab12e3-1-.png)
_It's okay, he won't bite_

Before we go straight to the implementation, let's cover what we'll learn. If you clicked on this article, you might already know about gRPC. But if you just clicked out of curiosity, fret not – I will give you a brief introduction to gRPC in a bit.

And if you don't know much about server-side streaming either, that's ok. I'll also cover that below.

Finally, if you are wondering what Go is, the quick answer is that it's a programming language. I won't cover that here, but you can read more about Go  in [its official docs here](https://golang.org/) before proceeding.

In this article, I'll start out by describing gRPC and server-side streaming.  
If you already have an idea of what both of those are, feel free to skip the first two sections below.

## What is gRPC?

![Image](https://www.freecodecamp.org/news/content/images/2020/11/index-1.png)

Have you ever dreamed about calling a server request with a function call? Instead of using an HTTP call with some URL? Well, that has already existed for quite some time – and we call it a [Remote Procedure Call](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/).

And in 2015, Google introduced something called gRPC, which is basically a Remote Procedure Call on steroids. 

It works almost the same as a traditional Remote Procedure Call. But Google introduced the usage of HTTP/2 as the communication protocol and protobuf as the communication contract between server and client.

HTTP/2 was also created by Google, and allows communication to be much more performant. It also allows multiplexing, which I will talk about later on.

Protobuf is basically the contract used to enable communication between the server and the client side via a function call.

Alright, that's a basic overview of gRPC. If you are still interested and want to dive deeper, you can read more in detail about it [here](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/).

## What is server-side streaming?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-269.png)
_Photo by [Unsplash](https://unsplash.com/@jonflobrant?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Jon Flobrant</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

And now, what about server-side streaming?

By design, gRPC uses HTTP/2 and supports something called multiplexing. I won't go into a ton of detail here, but it allows a single request to have multiple responses, and vice versa. 

This mechanism is implemented in gRPC and it is called streaming.

There are 3 types of streaming:

* Client-side streaming: Where the client will have multiple requests and the server will only return one response.
* Bidirectional streaming: Where both client and server can have multiple requests and responses together within a single connection.
* Server-side streaming: Where the client sends a single request and the server can return several responses together. This is the one I will be showing you how to implement today.

## How to Implement Server-side Streaming

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-270.png)
_Photo by [Unsplash](https://unsplash.com/@camadams?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Cam Adams</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

It’s implementation time! If you are reading this section, I assume you already know about this 3 things:

* gRPC
* Server-side streaming
* Go

Server-side streaming is especially useful if your server needs to return a bulky payload. 

By using streaming, you can split up those responses and return them one by one. The client will be able to cut off unused responses if it already has sufficient responses, or if it has been waiting too long for some responses.

Okay now let’s jump straight into the code.

### Create the Proto File

For starters, we will need to define our protobuf file that'll be used by the client and the server side. Let’s just make a simple one here, like this:

```proto
syntax = "proto3";

package protobuf;

service StreamService {
  rpc FetchResponse (Request) returns (stream Response) {}
}

message Request {
  int32 id = 1;
}

message Response {
  string result = 1;
}
```

This proto file basically contains a single function call with a parameter `Request` and returns a stream of `Response` .

Before we proceed, we also need to generate our `pb` file that'll be used by our Go Program. Each programming language will have a different way of generating the protocol buffer file. In Go we will be using the `protoc` library. 

If you haven’t installed it yet, Google provides the [installation guide for that here](https://developers.google.com/protocol-buffers/docs/reference/go-generated).

Let’s generate the protocol buffer file by running the following command:  
`protoc --go_out=plugins=grpc:. *.proto`   

And now we have `data.pb.go` ready to be used.

### Create the Client File

For the next step, you can create either the client file or the server file, in any order. But in this example I will be making the client file first.

```go
package main

import (
	"context"
	"io"
	"log"

	pb "github.com/pramonow/go-grpc-server-streaming-example/src/proto"

	"google.golang.org/grpc"
)

func main() {
	// dial server
	conn, err := grpc.Dial(":50005", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("can not connect with server %v", err)
	}

	// create stream
	client := pb.NewStreamServiceClient(conn)
	in := &pb.Request{Id: 1}
	stream, err := client.FetchResponse(context.Background(), in)
	if err != nil {
		log.Fatalf("open stream error %v", err)
	}

	done := make(chan bool)

	go func() {
		for {
			resp, err := stream.Recv()
			if err == io.EOF {
				done <- true //means stream is finished
				return
			}
			if err != nil {
				log.Fatalf("cannot receive %v", err)
			}
			log.Printf("Resp received: %s", resp.Result)
		}
	}()

	<-done //we will wait until all response is received
	log.Printf("finished")
}
```

The client will basically be the one sending the request. It will also be the one receiving multiple responses.

The client will call the gRPC method `FetchResponse` and wait for all the responses. I am using a `goroutine` here to show the possibility of concurrency. And I'm using `channel` in order to wait until all the processes are finished before exiting the program.

### Create the Server File

For the third and final file, we will be making the server file. This file will receive the response from client and in turn will send a stream of responses back to the client.

```go
package main

import (
	"fmt"
	"log"
	"net"
	"sync"
	"time"

	pb "github.com/pramonow/go-grpc-server-streaming-example/src/proto"

	"google.golang.org/grpc"
)

type server struct{}

func (s server) FetchResponse(in *pb.Request, srv pb.StreamService_FetchResponseServer) error {

	log.Printf("fetch response for id : %d", in.Id)

  	//use wait group to allow process to be concurrent
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(count int64) {
			defer wg.Done()
      
      			//time sleep to simulate server process time
			time.Sleep(time.Duration(count) * time.Second)
			resp := pb.Response{Result: fmt.Sprintf("Request #%d For Id:%d", count, in.Id)}
			if err := srv.Send(&resp); err != nil {
				log.Printf("send error %v", err)
			}
			log.Printf("finishing request number : %d", count)
		}(int64(i))
	}

	wg.Wait()
	return nil
}

func main() {
	// create listiner
	lis, err := net.Listen("tcp", ":50005")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	// create grpc server
	s := grpc.NewServer()
	pb.RegisterStreamServiceServer(s, server{})

	log.Println("start server")
	// and start...
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}

}
```

In the server file, I am also using a `goroutine` to simulate a concurrent process.  
For each of the requests, I will be streaming five requests back to the client side. Each will also have a different process time in order to simulate the different processing times you'd have in a real-life scenario.

### The Output

Now comes the exciting part. Let’s build both our client and server file with `go build` to get our binary file. Then we'll open up two separate console commands to run it.

**Just a quick note**: you should turn on the server first before the client since the client will directly invoke the server method.

So let’s go inside the directory of each of our binary files and run both of them with `/.server` and `./client` .

Your client will output this:

```
2020/11/10 22:26:11 Resp received: Request #0 For Id:1
2020/11/10 22:26:12 Resp received: Request #1 For Id:1
2020/11/10 22:26:13 Resp received: Request #2 For Id:1
2020/11/10 22:26:14 Resp received: Request #3 For Id:1
2020/11/10 22:26:15 Resp received: Request #4 For Id:1
2020/11/10 22:26:15 finished
```

And the server will output this:

```
2020/11/10 22:26:09 start server
2020/11/10 22:26:11 fetch response for id : 1
2020/11/10 22:26:11 finishing request number : 0
2020/11/10 22:26:12 finishing request number : 1
2020/11/10 22:26:13 finishing request number : 2
2020/11/10 22:26:14 finishing request number : 3
2020/11/10 22:26:15 finishing request number : 4
```

If all is well, you have successfully built yourself a gRPC server side streaming service with Go! If you need the GitHub code for the whole example, you can find it [here](https://github.com/pramonow/go-grpc-server-streaming-example).

## Wrapping Up

I hope this example of how to implement gRPC server side streaming with Go helped you understand the process. 

This implementation might not be very common, and you might not even need this kind of complex implementation in your project. But think of it as a tool to elevate your project even more.

If you want to learn more, check out these other cool concepts such as client side streaming or even bidirectional streaming. I found the example [here](https://github.com/pahanini/go-grpc-bidirectional-streaming-example) to be quite good.

Thanks for reading my article through to the end! I truly hope you learned something new and useful today. As I have said, you might not truly need it, but why not try it out?

> Don’t wait for the change, take the initiative and be the catalyst for change.

