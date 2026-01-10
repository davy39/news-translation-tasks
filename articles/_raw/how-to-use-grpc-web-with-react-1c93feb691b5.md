---
title: How to use gRPC-web with React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T17:48:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-grpc-web-with-react-1c93feb691b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PJce89y7GZdBYsiHzmmUow.jpeg
tags:
- name: Envoy Proxy
  slug: envoy-proxy
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mohak Puri

  For the past few months, my team has been working on a gRPC service. A few weeks
  back a new requirement came in: we needed a web portal to display some information.
  Since we already had a gRPC backend, the server side was sorted. But fo...'
---

By Mohak Puri

For the past few months, my team has been working on a gRPC service. A few weeks back a new requirement came in: we needed a web portal to display some information. Since we already had a gRPC backend, the server side was sorted. But for the front-end, we had a few important choices to make.

```
1. Vue or React (We choose react)2. REST or gRPC from the web portal 
```

If you don’t know what gRPC is you can read about it [here](https://grpc.io/). Here are a few reasons that made us choose gRPC over REST.

1. One major factor for choosing gRPC was the fact that we already had protos that we used in our backend service. We could use the same protos to generate client-side code in javascript**.**
2. Using gRPC would mean that we would not have to write any code for creating the client. Adding new endpoints would mean making changes to the proto and generating client-side code.
3. We needed server-side streaming which is supported by gRPC-web.
4. We already had a setup of envoy for loading balancing our backend service (more on this later).

### Caveats

1. gRPC web-client won’t send HTTP2 requests. Instead, you need a proxy between your web-client and gRPC backend service for converting that HTTP1 request to HTTP2. gRPC web client has built-in support for Envoy as a proxy. You can find more information about this [here](https://grpc.io/blog/state-of-grpc-web#f2).
2. The teams at Google and Improbable both went on to implement the spec in two different repositories. We will be using gRPC web client provided by Google. You can find the implementation by Google [here](https://github.com/grpc/grpc-web) and by Improbable [here](https://github.com/improbable-eng/grpc-web).
3. As of now, client-side streaming is not supported.

![Image](https://cdn-media-1.freecodecamp.org/images/OQ0IsJZIV2TFKQc7ErPHvNc735UGRcIHcWmK)
_Credits: [https://grpc.io/blog/state-of-grpc-web](https://grpc.io/blog/state-of-grpc-web" rel="noopener" target="_blank" title=")_

Now that we have some idea about gRPC web, below is a diagram depicting how the entire communication will take place. We are going to make a react web application that will send a _Ping_ request and get a _Pong_ response for it.

![Image](https://cdn-media-1.freecodecamp.org/images/wZ-PKPpwVBps6i71c37sQ8G2pZRjtlguKsPx)
_Front-end + Proxy + Back-end_

#### Before starting make sure you have the following installed:

```
1. npm (Node package manager) - For generating react project2. Docker - For running envoy locally3. protoc - For generating code using protos
```

There are 3 pieces to this puzzle. We are going to tackle each of them one by one.

### 1. User Interface — Website using react

For creating a react project, we will use the _create-react-app_ command.

```
create-react-app learn-react-grpc
```

Now that we have a sample project in place, let’s create a proto. This is what a ping pong proto looks like.

For subsequent commands to run, make sure that the proto is inside the src/ folder of the react project. For generating client-side code in javascript, run the following command:

```
protoc -I=. src/ping_pong.proto --js_out=import_style=commonjs:. --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.
```

This will generate two new files: **_ping_pong_pb.js_** and **_ping_pong_grpc_web_pb.js,_** with all the generated code in it. We will use this code to make requests to our gRPC service.

First, let’s update our package.json with a few gRPC and protobuf related dependencies and then run **_npm install_**_._

Below is the entire logic for building our website. You can use this code in your App.js file. It is a really simple website which contains a button, clicking on which creates a ping pong request and gets a response.

Now if you run the node server using **npm start,** you are likely to face this compilation issue. This is apparently an issue when using gRPC-web with a project created using _create-react-app_ command line interface_._

![Image](https://cdn-media-1.freecodecamp.org/images/5ZczeglnF24jEX58qfPUxInNybjRcJTZQww6)
_compilation issues when using create-react-app_

However, this issue can be fixed by adding _eslint-disable_ to all of the proto generated files. Make sure that you do this for _all_ the files. Now if you start the server, everything should be working.

![Image](https://cdn-media-1.freecodecamp.org/images/hAk-fyDb6JZ6bq5Vyqsxxoiyxkp5CB5gxueY)
_fixing compile issues_

### 2. Backend — gRPC server in Node

Let’s create a simple node server. We will be using the same proto that we used in our react app. Let’s create a node js application node-ping-pong-server. Here is our sample server.js file.

We can run the node server using the following command:

```
node server.js
```

### 3. Proxy — Envoy

As mentioned above, we will be using Docker for setting up envoy. Here is the docker file. As of writing, the latest tag points to Envoy _version 1.11._ Create a Dockerfile inside src/ folder of your react app.

Before running the Docker container, we need to make sure that we have a config file for envoy. Add this envoy.yml inside the src/ folder of your react app.

Let’s understand what this envoy configuration file does:

9901 is the port where envoy admin portal is running. You can use this portal to check envoy routes, health checks and a lot more.

9090 is the port where envoy is listening for incoming requests. Our website will make a request to envoy on this port.

Any request that matches the above prefix is routed to the ping_pong_service cluster. Since our node server (aka cluster) is running on the host machine (your laptop) and not the docker container, we need to route those request out of the container to the host. **_host.docker.internal_** does exactly this.

Now let’s build our docker image using the following command:

```
docker build -t mohak1712/learn-grpc-web .
```

Now let’s run the docker image:

```
docker run -d -p 9090:9090 mohak1712/learn-grpc-web
```

We need to forward host port 9090 to the containers port 9090 so that any request on port 9090 is forwarded to the docker container where envoy is running.

### Final Output

Now that everything is set up, make sure that the website, node server and envoy container are running. You can run the following set of commands in case you still haven’t.

```
npm start -> start web server
```

```
node server.js -> start node server
```

```
docker run -d -p 9090:9090 mohak1712/learn-grpc-web -> start envoy
```

![Image](https://cdn-media-1.freecodecamp.org/images/ybrDqzwv38XiKDlSZfVpdcjX2pTn2kkYaaOK)

![Image](https://cdn-media-1.freecodecamp.org/images/nfvEXxasFhtEuT9fqkKkXLBGE6DB8Eq4-xSq)

Now when you click on the button, it sends a Ping request and gets a Pong response for it!

That’s about it! Thank you for reading, and I hope you enjoyed the article.

You can follow me on [Medium](https://medium.com/@mohak1712) and [Github](https://github.com/mohak1712) :)

