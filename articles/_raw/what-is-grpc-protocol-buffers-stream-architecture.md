---
title: What is gRPC? Protocol Buffers, Streaming, and Architecture Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-09T21:33:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa0296d49c47664ed8187bf.jpg
tags:
- name: communication
  slug: communication
- name: performance
  slug: performance
- name: protocol-buffers
  slug: protocol-buffers
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: 'By Pramono Winata

  gRPC is a powerful framework for working with Remote Procedure Calls. RPCs allow
  you to write code as though it will be run on a local computer, even though it may
  be executed on another computer.

  These past few days I have been div...'
---

By Pramono Winata

gRPC is a powerful framework for working with Remote Procedure Calls. RPCs allow you to write code as though it will be run on a local computer, even though it may be executed on another computer.

These past few days I have been diving deep into gRPC. I'm going to share some of my big discoveries here in this article.

Note that I will focus more on concepts than implementation details. You will learn the core architecture of gRPC itself. You'll also learn:

* Why gRPC is so widely used by developers
* How it performs so well
* And how it all works under the hood.

## Let’s go back a bit

Before we rush into gRPC, we should take a look at what **Remote Procedure Calls** are.

A RPC is a form of Client-Server Communication that uses a function call rather than a usual HTTP call.

It uses IDL (Interface Definition Language) as a form of contract on functions to be called and on the data type.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/operating-system-remote-call-procedure-working.png)
_RPC Architecture_

If you all haven’t realized it yet, the RPC in gRPC stands for Remote Procedure Call. And yes, gRPC does replicate this architectural style of client server communication, via function calls.

So gRPC is technically not a new concept. Rather it was adopted from this old technique and improved upon, making it very popular in just the span of 5 years.

## Overview of gRPC

![Image](https://www.freecodecamp.org/news/content/images/2020/11/index.png)

In 2015, Google open sourced their project which eventually would be the one called gRPC. But what does the "g" in gRPC actually stand for?

Lots of people might assume its for Google because Google made it, but it does not.

Google changes the meaning of the "g" for each version to the point where they even made a [README](https://github.com/grpc/grpc/blob/master/doc/g_stands_for.md) to list all the meanings.

Since gRPC has been introduced it has gained quite a bit of popularity and many companies use it.

### What makes gRPC so popular?

There are plenty of reasons why gRPC is so popular:

* Abstraction is easy (it’s a function call)
* It is supported in a lot of languages
* It is very performant
* HTTP calls are often confusing, so this makes it easier

And aside from all of the reasons above, gRPC is popular because microservices are very popular.

Microservices will often be running several services in different programming languages. They'll also often have a lot of service to service interactions. 

This is where gRPC helps out the most by providing the support and capability to solve the typical issues that arise from those situations.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/index.jpeg)
_Microservices_

gRPC is very popular in service to service calls, as often HTTP calls are harder to understand at first glance. 

gRPC functions are much easier to reason about, so developers don't have to worry about writing a lot of documentation because the code itself should explain everything.

Some of the services might also be written in different languages and gRPC comes with multiple libraries to support that.

Performance is the cherry on top – and it’s a big cherry.

## gRPC Architecture

![Image](https://www.freecodecamp.org/news/content/images/2020/11/landing-2.png)
_The rough architecture of gRPC. It's more or less the same as regular RPC._

I have mentioned several times that gRPC's performance is very good, but you might wonder what makes it so good? What makes gRPC so much better than RPC when their designs are pretty similar?

Here are a few key differences that make gRPC so performant.

### HTTP/2

HTTP has been with us for a long time. Now, almost all backend services use this protocol.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/HTTP2-graphic.png)
_History of HTTP_

As the picture above shows, HTTP/1.1 stayed relevant for a long time.

Then in 2015, HTTP/2 came out and essentially replaced HTTP/1.1 as the most popular transport protocol on the internet.

If you remember that 2015 was also the year that gRPC came out, it was not a coincidence at all. HTTP/2 was also created by Google to be used by gRPC in its architecture.

HTTP/2 is one of the big reasons why gRPC can perform so well. And in this next section, you'll see why.

### Request/Response Multiplexing

In a traditional HTTP protocol, is not possible to send multiple requests or get multiple responses together in a single connection. A new connection will need to be created for each of them.

This kind of request/response multiplexing is made possible in HTTP/2 with the introduction of a new HTTP/2 layer called binary framing.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-from-2020-10-03-15-46-01.png)

This binary layer encapsulates and encodes the data. In this layer, the HTTP request/response gets broken down into frames.

The headers frame contains typical HTTP headers information, and the data frame contains the payload. Using this mechanism, it's possible to have data from multiple requests in a single connection.

This allows payloads from multiple requests with the same header, thus identifying it as a single request.

### Header Compression

You might have encountered many cases where HTTP headers are even bigger than the payload. And HTTP/2 has a very interesting strategy called HPack to handle that.

For one, everything in HTTP/2 is encoded before it's sent, including the headers. This does help with performance, but that’s not the most important thing about header compression.

HTTP/2 maps the header on both the client and the server side. From that, HTTP/2 is able to know if the header contains the same value and only sends the header value if it is different from the previous header.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-from-2020-11-04-22-32-12-1.png)

As seen in the picture above, Request #2 will only send the path since the other values are exactly the same. And yes, this does cut down a lot on the payload size, and in turn, improves HTTP/2's performance even more.

### Protocol Buffer, a.k.a. Protobuf

![Image](https://www.freecodecamp.org/news/content/images/2020/11/protobuf.png)
_Protocol Buffer_

Protobuf is the most commonly used IDL (Interface Definition Language) for gRPC. It's where you basically store your data and function contracts in the form of a proto file.

```proto
message Person {
    required string name = 1;
    required int32 id = 2;
    optional string email = 3;
}
```

As this is in the form of a contract, both the client and server need to have the same proto file. The proto file acts as the intermediary contract for client to call any available functions from the server.

Protobuf also has it owns mechanisms, unlike a usual REST API that just sends over strings of JSON as bytes. These mechanisms allow the payload to be much smaller and enable faster performance. 

The encoding method Protobuf uses is pretty complicated. If you want to take a deep dive into how it works, check out this [comprehensive documentation](https://developers.google.com/protocol-buffers/docs/encoding).

## What else does gRPC offer?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-257.png)
_Photo by [Unsplash](https://unsplash.com/@kyledevaras?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Kyle Gregory Devaras</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Now you should have a basic understanding of the architecture of gRPC, how it works, and what it's capable of.

But here are a few other interesting things gRPC offers us.

### Metadata

Instead of using a usual HTTP request header, gRPC has something called metadata. Metadata is a type of key-value data that can be set from either the client or server side.

`Header` can be assigned from the client side, while servers can assign `Header` and `Trailers` so long as they're both in the form of metadata.

### Streaming

Streaming is one of the core concepts of gRPC where several things can happen in a single request. This is made possible by the multiplexing capability of HTTP/2 mentioned earlier.

There are several types of streaming:

* **Server Streaming RPC:** Where the client sends a single request and the server can send back multiple responses. For example, when a client sends a request for a homepage that has a list of multiple items, the server can send back responses separately, enabling the client to use lazy loading.
* **Client Streaming RPC:** Where the client sends multiple requests and the server only sends back a single response. For example, a zip/chunk uploaded by the client.
* **Bidirectional Streaming RPC:** Where both the client and server send messages to each other at the same time without waiting for a response.

### Interceptors

gRPC supports the usage of interceptors for its request/response. Interceptors, well, intercept messages and allow you to modify them.

Does this sound familiar? If you have played around with HTTP processes on a REST API, interceptors are very similar to middleware.

gRPC libraries usually support interceptors, and allow for easy implementation. Interceptors are usually used to:

* Modify the request/response before being passed on. It can be used to provide mandatory information before being sent to the client/server.
* Allow you to manipulate each function call such as adding additional logging to track response time.

### Load Balancing

If you aren't already familiar with load balancing, it's a mechanism that allows client requests to be spread out across multiple servers.

But load balancing is usually done at the proxy level (for example, NGINX). So why am I talking about it here?

Turns out that gRPC supports a method of load balancing by the client. It's already implemented in the Golang library, and can be used with ease.

While it might seem like some sort of crazy magic, it's not. There's some sort of DNS resolver to get an IP list, and a load balancing algorithm under the hood.

### Call Cancellation

gRPC clients are able to cancel a gRPC call when it doesn't need a response anymore. Rollback on the server side is not possible, though.

This feature is especially useful for server side streaming where multiple server requests might be coming. The gRPC library comes equipped with an observer method pattern to know if a request is cancelled and allow it to cancel multiple corresponding requests at once.

## Wrapping Up

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-258.png)
_Photo by [Unsplash](https://unsplash.com/@rcrazy?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ricardo Rocha</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Everything I shared today just scratches the surface of what gRPC is, what it's capable of, and roughly how it works.

I truly hope this article helped you understand more about gRPC. But there's still a lot more learn, so don't stop here! Keep digging.

Thanks for reading!

