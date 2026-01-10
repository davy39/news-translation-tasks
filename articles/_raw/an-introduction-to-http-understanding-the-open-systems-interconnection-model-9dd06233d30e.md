---
title: 'An introduction to HTTP: Exploring Telecommunication in Computer Systems'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T16:29:27.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7pzeTboIfH5UxaFnVnGhnA.jpeg
tags:
- name: https
  slug: https
- name: network
  slug: network
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cher Don

  Get to know the Open Systems Interconnection model


  Overview

  Throughout this series, we will be tackling the basics such as:(Part 1) How does
  DNS work?(Part 2) Network Stack, OSI Model [You are here!](Part 3) HTTP Methods
  and Formats(Part...'
---

By Cher Don

#### Get to know the Open Systems Interconnection model

![Image](https://cdn-media-1.freecodecamp.org/images/AboxQNs-z1kZCMDrUuPqdsHzdyVLBBE5MeFL)

### Overview

Throughout this series, we will be tackling the basics such as:   
[(Part 1) How does DNS work?](https://medium.freecodecamp.org/an-introduction-to-http-domain-name-system-servers-b3e7060eca98)   
(Part 2) Network Stack, OSI Model _[You are here!]_  
(Part 3) HTTP Methods and Formats   
(Part 4) Client Identification   
(Part 5) Basic/Digest Authentication   
(Part 6) HTTPS working with SSL/TLS

### OSI Model

The Open Systems Interconnection (OSI) Model is a standardized model for telecommunication in computer systems. It does not regard the underlying technology, but instead the layers involved in communication. Let us explore the different layers within the OSI Model:

![Image](https://cdn-media-1.freecodecamp.org/images/Yc4ZTugFjR4A1zuGQqAQbN6Ez77yBttblRUI)
_Typical 5-layered OSI Model_

### 1. Application Layer

This layer allows applications to communicate over the network once the connection has been established, such as from the Web Browser (Application) to the Server. Examples of protocols in this layer include HTTP and TELNET.

#### HyperText Transfer Protocol (HTTP)

A set of rules for transferring files over the Internet. For example, when you enter the URL into the browser, the browser sends an HTTP request for the webpage. The host would then return the webpage, together with all the elements that are within, such as images, text, videos, styling fonts, etc.

### 2. Transport Layer

This layer is responsible for the host-to-host communication of messages. Examples of protocols in this layer include TCP and UDP.

#### Transmission Control Protocol (TCP)

The most common connection-oriented protocol. It defines how to establish and maintain a network conversation. It is responsible for establishing a connection (called a _socket_) between the client and the host in a 3-way handshake.

![Image](https://cdn-media-1.freecodecamp.org/images/aZwDUnYpTUmP4-20iIQpxYRqP2PGJRAI52N5)

The user requesting the data will send a SYN data packet to the server, requesting _synchronization_. The server will then respond with a SYN-ACK to the user, indicating that it has _acknowledged_ the data packet, and would like to connect as well. The connection is hence established when the user sends the last ACK to the server.

TCP is the most common due to its elegance, in which it is able to offer the following:

**Connection-oriented communication**  
 Establish a handshake protocol between end-points to ensure connection before data is exchanged, and transmit as a data stream (data packets).

**Reliability**  
Using checksums, it ensures that the data packets transmitted and received are the same. If there are missing/corrupted packets, it will request for re-transmission of the data packets by sending a NACK message to the sender.

**Order**  
The data packets are numbered and transmitted. As such, TCP will ensure that the received packets are re-ordered before delivering the application.

**Flow Control**  
The rate of data transmission is regulated to improve efficiency while preventing buffer overruns/underruns, where data is sent faster than the receiver is able to process it, and vice versa.  
The mechanics behind it are explained below in the [TCP Slow Start](#c804) section.

**Multiplexing**  
Basically, it is able to send over multiple streams of information concurrently over the same socket. These are done through different ports on the socket. We will discuss the differences between [Multiplexing and Pipelining](#8aeb) further along in the article.

#### User Datagram Protocol (UDP)

While similar to TCP, it is a connection-less protocol. It is the complete opposite of TCP, making it unreliable and unordered. Dropped packets will not be re-transmitted, causing gaps in the data.

![Image](https://cdn-media-1.freecodecamp.org/images/-YFU7rjDOESeBDk4iwsJJ3DXbF7kTF4FPKPQ)

However, that makes it best for time-sensitive applications, such as voice calls over the internet (VoIP). This is because it does not require the 3-way handshake before transmitting, making it fast. In addition, dropped data packets are not a problem in VoIP, as the human ear is very good at handling the short gaps that are typical with dropped packets.

### 3. Network Layer

This layer is responsible for providing data routing paths for network connections. Basically, it moves data packets across the network with the most logical path.

#### Internet Protocol (IP)

Defines the structure of the data packets, as well as labeling it with the source and destination information.

The source and destination information are in the form of IP Addresses, in which can be in the form `104.16.121.127`(IPv4), or `2001:db8:0:1234:0:567:8:1`(IPv6).

### 4. Link/ Physical Layer

This layer is the root of the OSI model, where information is transmitted either in the Local Area Network (LAN) for the Link Layer, and a physical signal such as electrical, mechanical medium in the form of code words or symbols in the Physical Layer.

### Visualising Routes

Using `tracert google.com`, the route can be traced from the client-side (your computer) to the host (google.com).

![Image](https://cdn-media-1.freecodecamp.org/images/hcYgb-j6sNT4L3em4eSD-K5DzC798H6zwYDn)

From above, you can see the route starting from my device `192.168.1.254` to the router `10.243.128.1`, before passing through the Internet Service Provider (ISP) located in Portugal, and so forth.

### Complementary Layers

#### TCP/IP Model

![Image](https://cdn-media-1.freecodecamp.org/images/75nPgdIHhsTD5xSIbj1bTjRlNryTU3291Ndo)
_TCP will request for re-transmission of dropped data packets, and re-order them_

IP is only responsible for the structure of the data packet. As such, it will not make amends if the data packet is corrupted, or dropped. This is where TCP comes into play, numbering the data packets before sending over to the client. At the client’s side, TCP will request for re-transmission of lost/corrupted packets, and then rearrange the packets of data.

#### HTTP/TCP Model

As we have mentioned earlier, HTTP can now make requests via the connection made by [TCP Handshake](#259f). But how do they complement each other?

**HTTP Persistent Connections**   
This would allow multiple HTTP request/response on a single TCP connection, as opposed to opening a new connection upon every request/response.

![Image](https://cdn-media-1.freecodecamp.org/images/-F9J9R9grtdhm7aQ1Y1ptqz1xL8Ft8c4x-0T)
_Sample response for Persistent Connection_

This is done through the HTTP Header, where `Connection: Keep-Alive`. On default, the connection will only close upon another response where `Connection: Close` is sent after 30 seconds of idle.

**TCP Slow Start**  
As mentioned before, TCP supports [flow control](#e64e). This is done through TCP Slow Start, which is a form of prevention for network congestion.

![Image](https://cdn-media-1.freecodecamp.org/images/rV1aQqU5LxUsUJaX1-jDTn1VVCpKORoM10lb)

The sender has a congestion window (CWND) and the receiver has a receiver window (RWND). If the data is larger than the congestion/receiver window, there would be a buffer under/overrun respectively.

To prevent that, the sender will begin by sending a data packet with a small congestion window (CWND = 1), to slowly probe the receiver for its receiver window.

The receiver will respond with an acknowledge, prompting the sender to double the data packets each time until no acknowledge is received. At this point, the optimum number of data packets has been discovered, allowing other congestion control algorithms to keep the connection at this speed.

**Working Together**  
Hence, TCP Slow Start is able to figure out the optimum number of data packets to send before the connection is closed. This will allow the amount of data sent from the host to the client to be optimized without the risk of buffer overrun (data is sent faster than it can be received).

### Other HTTP Features

#### HTTP Pipelining

![Image](https://cdn-media-1.freecodecamp.org/images/Lw7lr7o1l1yyIyMDwRugYYE0DR4jjgNoxFuE)

This feature in version HTTP/1.1 allows multiple requests to be sent at once on the same socket, without waiting for a response. However, it has been replaced by TCP Multiplexing in the newer version of HTTP/2.

The key difference is that although both allow for multiple requests all at once on the same socket, Pipelining would still require responses to be sent in order. It means that if the items requested are in the order (A, B, C), the client would not receive item C if item B has not been delivered properly.

In Multiplexing, the order does not matter. This would allow quicker delivery time.

These methods are best used for the idempotent method, which are methods that respond independently of the number of times requested — for example, requesting a web page multiple times will respond to the same web page.

#### Parallel Connections

Ever opened a webpage and seen multiple components of the webpage (video bar, thumbnails, buttons) load simultaneously?

![Image](https://cdn-media-1.freecodecamp.org/images/kSoqraJbI4QgwnlADZzo32d5E2dQb2408ODU)
_Multiple components loading simultaneously | Photo courtesy of [Cloudflare Mobile SDK](https://www.cloudflare.com/products/mobile-sdk/" rel="noopener" target="_blank" title=")_

This is made possible with Parallel Connections, where there is more than one TCP Connection established at the same time, allowing these components to load concurrently instead of one after another.

However, although it might seem to load faster, it might be held back by the client’s limited bandwidth. If all Parallel Connections are competing for the limited bandwidth, each component will load proportionately slower, resulting in zero advantage in total loading speed.

### Conclusion

With the OSI Model, we can easily understand the big picture of networks, and how they interact with each other from hardware to software.

In general, it is a great teaching tool as well as a reference for troubleshooting. The model is also useful for design, as it investigates the functions at every layer, forcing one to ponder over the design layer by layer.

What I have gone through so far is the OSI 5-Layer Model, whereas there is also the [OSI 7-Layer Model](https://www.webopedia.com/quick_ref/OSI_Layers.asp) which also deals with Identification, Authentication and Data Encryption.

This is Part 2 of the HTTP Introductions Series. You can read the first article about the importance of DNS Servers in [Part 1](https://medium.freecodecamp.org/an-introduction-to-http-domain-name-system-servers-b3e7060eca98). Let’s explore the structure of HTTP Requests next in Part 3!

Hi! I’m [Cher Don](https://www.freecodecamp.org/news/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e/undefined), currently pursuing a Major in Data Science. I’m the CTO of [Paralegal Bot](https://www.linkedin.com/company/paralegal-bot/), and you can find my website below. Thanks for reading!

[**Piqued;**](http://www.piqued.co)  
[_Quality Content We offer the best content for difficult to grasp concepts. We've been there, and felt the same you do…_www.piqued.co](http://www.piqued.co)

