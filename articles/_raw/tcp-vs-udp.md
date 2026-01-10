---
title: TCP vs. UDP — What's the Difference and Which Protocol is Faster?
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-06-28T12:06:00.000Z'
originalURL: https://freecodecamp.org/news/tcp-vs-udp
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/ian-battaglia-9drS5E_Rguc-unsplash.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: internet
  slug: internet
- name: network
  slug: network
- name: networking
  slug: networking
seo_title: null
seo_desc: 'If you''re getting into computer networking, or if you''ve dug through
  the network settings of some applications, you''ve likely seen these terms: TCP
  and UDP.

  TCP, which stands for Transmission Control Protocol, and UDP, or User Datagram Protocol,
  are ...'
---

If you're getting into computer networking, or if you've dug through the network settings of some applications, you've likely seen these terms: TCP and UDP.

TCP, which stands for Transmission Control Protocol, and UDP, or User Datagram Protocol, are part of the internet protocol suite. TCP and UDP are different methods to send information across the internet.

But even knowing what they stand for, it's hard to know which protocol you should use, or why you would use one over the other.

In this article, we'll go over computer networking basics, the differences between TCP and UDP, when each is used, and more.

## Computer Networking Basics

Before diving into how TCP and UDP work, it's helpful to know the basics about how the internet works.

Generally speaking, the internet is a network of connecting devices. Each device, whether it's your smartphone or a server, communicate through the internet protocol suite.

The internet protocol suite is a collection of different protocols, or methods, for devices to communicate with each other. Both TCP and UDP are major protocols within the internet protocol suite:

![Basic diagram of the internet protocol suite.](https://www.freecodecamp.org/news/content/images/2021/07/internet-protocol-suite-diagram.gif)
_[Source](https://www.sciencedirect.com/topics/computer-science/internet-protocol-suite)_

Each device that's connected to the internet has a unique IP address. And whenever two devices communicate over the internet, they're likely using either TCP or UDP to do so.

Here's a brief comparison between the two:

![Diagram comparing TCP and UDP](https://www.freecodecamp.org/news/content/images/2021/07/tcp-vs-udp-diagram.png)
_[Source](https://www.wowza.com/blog/udp-vs-tcp)_

For an even higher-level overview of how the internet works, check out this five minute video:

%[https://www.youtube.com/watch?v=7_LPdttKXPc]

## What is TCP?

TCP, or Transmission Control Protocol, is the most common networking protocol online. TCP is extremely reliable, and is used for everything from surfing the web (HTTP), sending emails (SMTP), and transferring files (FTP).

TCP is used in situations where it's necessary that all data being sent by one device is received by another completely intact.

For example, when you visit a website, TCP is used to guarantee that everything from the text, images, and code needed to render the page arrives. Without TCP, images or text could be missing, or arrive in the incorrect order, breaking the page.

TCP is a connection-oriented protocol, meaning that it establishes a connection between two devices before transferring data, and maintains that connection throughout the transfer process.

To establish a connection between two devices, TCP uses a method called a three-way handshake:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/tcp-three-way-handshake-simple.png)
_[Source](https://www.techopedia.com/definition/10339/three-way-handshake)_

For example, to read this article on your device, your device first sent a message to the freeCodeCamp News server called an SYN (Synchronize Sequence Number).

Then the freeCodeCamp News server sends back an acknowledgement message called a SYN-ACK.

When your device receives the SYN-ACK from the server, it sends an ACK acknowledgment message back, which establishes the connection.

Once a TCP connection is established between two devices, the protocol guarantees that all data is transmitted.

Going back to the example of your device and freeCodeCamp News, once the three-way handshake is complete, the News server can start sending all the data your device's web browser needs to render this article.

All devices break up data into small packets before sending them over the internet. Those packets then need to be reassembled on the other end.

So when the freeCodeCamp News server sends the HTML, CSS, images, and other code for this article, it breaks everything into small packets of data before sending them to your device. Your device then reassembles those packets into the files and images it needs to render this article.

TCP ensures that these packets all arrive to your device. If any packets are lost along the way, TCP makes it easy for your device to let the server know it's missing data, and for the server to resend those packets.

Once your device receives all the data it needs to render the article, TCP automatically terminates the connection between the two devices with a method similar to the three-way handshake, this time using FIN and ACK packets.

## What is UDP?

UDP, or User Datagram Protocol, is another one of the major protocols that make up the internet protocol suite. UDP is less reliable than TCP, but is much simpler.

UDP is used for situations where some data loss is acceptable, like live video/audio, or where speed is a critical factor like online gaming.

While UDP is similar to TCP in that it's used to send and receive data online, there are a couple of key differences.

First, UDP is a connectionless protocol, meaning that it does not establish a connection beforehand like TCP does with its three-way handshake.

Next, UDP doesn't guarantee that all data is successfully transferred. With UDP, data is sent to any device that happens to be listening, but it doesn't care if some of it is lost along the way. This is one of the reasons why UDP is also known as the "fire-and-forget" protocol.

A good way to think about these differences is that TCP is like a conversation between two people. Person A asks person B to talk. Person B says sure, that's fine. Person A agrees and they both start speaking.

UDP is more like a protester outside with a megaphone. Everyone who is paying attention to the protester should hear most of what they're saying. But there's no guarantee that everyone in the area will hear what the protester is saying, or that they're even listening.

![A diagram comparing UDP and TCP connections](https://www.freecodecamp.org/news/content/images/2021/07/udp-and-tcp-comparison.jpg)
_UDP vs TCP — [Source](https://www.dpstele.com/snmp/transport-requirements-udp-tcp.php)_

## Which is Faster – TCP or UDP?

In general, UDP is the faster protocol.

UDP is much simpler, and doesn't try to establish a connection between devices before sending data, or verify that all the data even arrived. It simply sends out data to any device that requests it, and keeps doing that until the other device disconnects or there is no more data left to send.

Think drinking from a hose rather than sipping from a bottle. You'll quench your thirst either way, but will probably end up with a damp shirt using the former method.

![A meme showing one person drinking from a water bottle to represent TCP, and another person pouring water from a bottle onto their face to represent UDP.](https://www.freecodecamp.org/news/content/images/2021/07/tcp-vs-udp-meme.png)
_Not a hose, but still pretty accurate. Also imagine that the TCP bottle keeps asking if you received water while you drink from it. [Source](https://www.reddit.com/r/ProgrammerHumor/comments/9gcwgw/tcp_vs_udp/e63axmd/)_

But being faster doesn't mean that UDP is the better protocol overall. It just means that it's better in certain situations.

As mentioned earlier, TCP is necessary in situations where it's vital that all data packets are sent in order, and that all packets arrive. The web just wouldn't function without TCP.

And while TCP is slower because of the way it establishes connections, and due to the checks for missing packets, it can still be blazing fast. Because they're on the web and use HTTP, sites like YouTube or Netflix all use TCP to send data to your devices.

TCP also allows for buffering, so your browser can request and load more data as you watch, allowing for smooth playback and for you to skip ahead to other parts of the video.

UDP is the better choice for live video and audio or online games where speed is more important than potential data loss.

When you make a call over Google Meet or Zoom, your video and audio are being transmitted over UDP. If some packets are lost along the way, it'll just appear as a bit of lag or clipped video/audio.

If you play video games, you might think that the way TCP ensures all data packets arrive at the other device would make it the ideal choice. But in reality, all the checking and resending data that TCP does just adds latency.

Game developers have found other clever ways to ensure that player input and state are as accurate as possible. If you're interested in reading more about why UDP is preferred for online gaming, check out [this article](https://gafferongames.com/post/udp_vs_tcp/).

## FIN

I hope this article helped you understand some of the nuances between TCP and UDP. And if someone asks which is faster, tell 'em what you read here: "UDP is faster, _but_..."

And if you like what you read, let me know over on [Twitter](https://twitter.com/kriskoishigawa).

