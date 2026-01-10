---
title: What is the OSI Model? Computer Networking for Beginners
subtitle: ''
author: Tamerlan Gudabayev
co_authors: []
series: null
date: '2021-10-04T16:27:49.000Z'
originalURL: https://freecodecamp.org/news/osi-model-computer-networking-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/banner-1.jpg
tags:
- name: computer networking
  slug: computer-networking
seo_title: null
seo_desc: 'In this article, you will learn about the core concepts of the Open Systems
  Interconnections (OSI) model in a simple and easy way.

  As a developer, it''s a good idea to learn how things work "under the hood". That
  way you understand what your code and ...'
---

In this article, you will learn about the core concepts of the Open Systems Interconnections (OSI) model in a simple and easy way.

As a developer, it's a good idea to learn how things work "under the hood". That way you understand what your code and the tools you use are actually doing.

But it might seem easier to rely on black box abstraction and ignore the inner workings.

A popular black box abstraction is the internet. 

Sure, many of us probably know the basics of what the internet is and how it works. There is a client and a server and they simply "communicate" with each other using something called HTTP or HTTPS?

But that's the extent of most people's knowledge.

I'm not saying we shouldn't use abstractions – I'm just saying that we should have some basic idea about how things work.

This is why I'm writing this article: to demystify this black box to help you learn how computers communicate with each other over a network. 

## What is the OSI Model?

![Image](https://www.freecodecamp.org/news/content/images/2021/10/osi-model-layers.png)
_The Seven Layers of OSI_

The Open Systems Interconnection or OSI model is essentially a reference system that lays out how computers communicate with each other over a network.

It was created in 1983 by representatives of telecom companies and officially standardized in 1984 by the International Organization for Standardization (ISO).

It is divided into seven layers. Each layer has its own domain and receives data from the previous layer, while passing data to the next layer.

The seven layers are:

1. Application Layer
2. Presentation Layer
3. Session Layer
4. Transport Layer
5. Network Layer
6. Data Link Layer
7. Physical Layer

If we think of it in coding terms, each layer is a class with some core functionality, and each class communicates with only the class above or below it. 

Keep in mind that this is a **reference** model, meaning that we don't actually use it in real life. There is another model which is very similar to the OSI model but it encapsulates the first three layers and the last two. 

This "real life" model is called the TCP/IP Model which is what the internet runs on. 

![Image](https://www.freecodecamp.org/news/content/images/2021/10/osi-vs-tcpip-1.png)
_OSI vs TCP/IP Model diagram_

But before we jump in and deal with each layer one by one, let's go over why should you learn the OSI model if it's not even used in real life.

## Why Learn the OSI Model

During the past 20 years or so, the world has dramatically changed.

The internet came, the "web" came, and within the web ecosystem lots of things have changed. We started with simple HTML pages, then came JavaScript, and now we have all these frameworks and it sometimes feels so overwhelming. 

But, you gotta remember this:

> Learn the fundamentals, learn from first principles.

Let's take the web, for example, aside from all these changes we have seen during the past 20 years. 

How the web works hasn't actually change much. 

We still use the HTTP protocol. 

It's true that the HTTP protocol has been updated, but not so much.

Even if we break down HTTP, it's made from TCP which also hasn't changed much.

My point is that you should stop looking at the shiny new things and focus on the fundamentals that these shiny new things are built upon. 

For example, I remember when web sockets was a popular thing.

But if we break it down, they're based on the TCP protocol. 

If you know TCP, you can easily understand how web sockets work and don't have to rely on black box abstractions. 

I hope I've convinced on why you should learn from first principles. This not only applies to software engineering but to many other fields, too.

With that done, let's go over the seven layers of the OSI model.

## The Seven Layers of the OSI Model

### Application Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/3.png)
_This is the layer where the end user exists_

The application layer is where most software engineers work. And this is where your browsers lives. 

But I'm not talking about concrete applications such as Chrome, Skype, or Outlook. 

I'm talking more fundamental things, such as protocols.

For example:

* Your browser makes a request to a web server using the HTTP protocol. 
* Your email app uses the SMTP protocol to send and receive emails.
* Without the DNS protocol, you would have to type 142.250.150.138 instead of google.com. 

In a nutshell, the application layer handles the foundation that almost all end user applications use.

### Presentation Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/4.png)

Once the client makes the HTTP request, the request itself get's passed down to the presentation layer (also called syntax layer).

This layer handles three main functionalities:

#### Encryption and Decryption

You don't want your data out in public, which is why smart people created the Transport Layer Security (TLS). It essentially encrypts your data. 

It's also responsible for decrypting requests coming from other servers to be consumed by the application layer.

#### Serialization and Deserialization

These are some big words, but what they essentially mean is "translation".

We want to "translate" our data to forms that our application understands. 

For example, simple data structures may be translated into "objects" that our JavaScript application understands.

On the other hand, if we want our data to pass down the layer, we would translate our object into simple data structures that could be understood in the lower layers.

#### Compression

This is a no-brainer: the fewer bits there are to send, the faster the request will be. 

This is also one of the main functions of the presentation layer. Keep in mind this is a lossless compression meaning no information will be lost in the process.

Well to be fair, in the real world most of these things are done in the application layer. 

This is why in the TCP/IP model the presentation layer is part of the application layer.

### Session Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/5-1.png)
_The session layer is responsible for opening, closing and maintaining connections between client and server_

This one is a bit confusing. And in fact, I couldn't find many use cases for it. 

The primary function of the session layer is to manage connections between client and server. 

But what does that actually mean?

So let's say you want to go to google.com

To do that you first have to establish a connection with google.com, so you say "Hey server, what's up, I want to connect to google.com".

The server responds back: "Yeah, sure." 

Congratulations, you have just established a connection with google.com's server and can freely send a GET request to fetch the page. 

Long story short, this layer is used for:

* Opening connections 
* Keeping connections alive
* Closing connections.

Now comes the reality check: in real life this pretty much does not exist and is part of the Transport Layer – which we'll discuss next.

### Transport Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Transport-Layer.png)
_TCP and UDP visualized_

This is where the interesting stuff happens.

The transport layer is usually defined based on the protocol that's being used.

The [two most popular ones are](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/):

* Transmission Control Protocol (TCP)
* User Datagram Protocol (UDP)

TCP is one of the main protocols in the internet suite. It is used on top of the IP (internet protocol) to ensure reliable transmission of packets.

TCP fixes many issues that arise when you use IP such as lost packets, out of order packets, duplicate packets, and corrupted packets.

You would use TCP in applications that require all packets to be error-free such as text messaging.

On the other hand UDP is stateless, meaning it doesn't save any state between the client and server It is also very light making it fast. But the downside is that it's not reliable, packets can go missing, get corrupted, and so on.

UDP is mostly used when you don't really care if you lose a few packets here and there, such as video streaming.

Also keep in mind that the data in this layer are called segments.

Long story short, TCP is reliable but slow, while UDP is unreliable but fast.

### Network Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Network-Layer-1.png)
_The network layer is responsible for sending packets from network to network_

I don't really know why this is called the network layer. 

It should be called the internet layer – because the most important protocol here is the Internet Protocol (IP)

What the IP basically does is it takes the segments from the transport protocol, and adds meta-data that helps identify where your client is in a local network.

Another function of the network layer is message forwarding, meaning that it sends your packets from network to network.

Data in this layer are called packets.

### Data-Link Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Data-Link-Layer.png)
_The data link layer is made of two parts: MAC and LLC_

This layer defines how data is transmitted between two systems. 

It takes care of things such as how long two systems talk to each other, how much data can be sent, and what happens if there are any errors. All this is handled in the Data Link layer.

The data link layer is broken up to two sub-layers:

* Logical Link Layer (LLC) – This layer provides flow control, acknowledgment, and error handling in case things go wrong.
* Media Access Control (MAC) – This layer is responsible for assigning a unique id number based on your network card called a MAC address. Meaning no two devices have the same MAC addresses.

Packets are taken from the network layer, and are encapsulated with the addition of new headers for the MAC address of the client and server. 

There is also another subset of data added at the end of the packet which is used for error detection. This is called the tail.

Once these meta-data are added, the data is now called a frame.

### Physical Layer

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Physical-Layer.png)
_Bits can be transferred using electricity, radio waves, or even light_

Finally this is the physical layer.

Don't get confused with the word physical – we are not only talking about wires. 

Data can get transferred in many different ways such as radio waves or even light. 

Unfortunately these ways of transportation do not know "frames", they only know bits. 

The function of this layer is to simply transform frames into bytes (8 bits) and send them over some transport method (electricity, waves, light, and so on).

Finally our request will get transmitted to the server, and the server will go through the same process but in reverse. 

## Conclusion

In this article, you learned:

* That the OSI Model is a reference model on how two systems talk to each other over a network.
* We don't use this model in real life. Instead, we use another similar model called the TCP/IP model.
* The OSI mode is made up of seven parts, each with a specific function.

I hope you learned something today, and would like to thank you for reaching the end. 

I plan to post snippets of content similar to this on Twitter, so if you're interested follow me [@tamerlan_dev](https://twitter.com/tamerlan_dev).




