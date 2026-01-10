---
title: TCP and UDP Protocols – Explained in Plain English
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2023-08-10T22:19:30.000Z'
originalURL: https://freecodecamp.org/news/tcp-and-udp-protocols
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-159304.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: computer networking
  slug: computer-networking
seo_title: null
seo_desc: 'Did you know that it''s thanks to the TCP and UDP protocols that the internet
  works?

  But what do these acronyms mean?

  Well, TCP stands for Transmission Control Protocol and UDP stands for User Datagram
  Protocol

  Ok, but what are they? Why are they usef...'
---

Did you know that it's thanks to the TCP and UDP protocols that the internet works?

But what do these acronyms mean?

Well, TCP stands for Transmission Control Protocol and UDP stands for User Datagram Protocol

Ok, but what are they? Why are they useful? Why is it thanks to these protocols that the internet works?

In this article, we'll start with a simple analogy to help you understand the ideas behind TCP and UDP. Then I'll explain how they work in plain English. Next we'll discuss why these protocols are important, and we'll understand their key differences.

## What are TCP and UDP? Explained with an Analogy

![Image](https://www.freecodecamp.org/news/content/images/2023/03/letter.jpg)
_Photo by Suzy Hazelwood from Pexels: https://www.pexels.com/photo/shallow-focus-of-letter-paper-1157151/_

You can think about TCP and UDP in a similar way as you think about a mail service.

Just like a **mail service** sends **letters** to **individuals, TCP and UDP** send **packets** to **computers**.

Packets are just formatted units of data in bytes.

TCP works more like a registered mail service. With registered mail, the sender sends a parcel to a recipient, and they're notified when the parcel is delivered. The sender can also track the parcel if it is lost or delayed.

On the other hand, UDP is like a regular mail service. The sender sends a parcel without any confirmation of delivery. There is also no tracking or guarantee that the parcel is going to be delivered.

## How Do TCP and UDP Work?

Both the UDP and TCP are protocols used to ensure that data is reliably and securely transmitted between devices over a network.

TCP creates a connection between the sender and receiver and then data is transmitted between packets.

TCP also ensures that all packets are delivered in order. Additionally, it has mechanisms for resending lost packets and managing flow control. 

Meanwhile, UDP sends packets without establishing a connection. Because of this, packets can be lost or arrive out of order as there is no mechanism to request retransmission.

## TCP vs UDP – What's the Difference?

Both UDP and TCP were developed starting in the 1980s.

TCP is important in programming because it provides a reliable and secure way for devices to communicate with each other over a network.

Without TCP, it would be difficult for devices to communicate securely, and many of the applications that we use today would not exist.

For example email communication, file transfers, and online transactions would all be very difficult without TCP.

TCP is preferred for secure, ordered, and reliable data transmission, as well as for delivering large amounts of data with minimal delay and mitigating network congestion.

UDP is also important for connections that require a lot broadband where security is not an issue.

For example video streaming services, online gaming platforms, and IoT devices can all use UDP to transmit data.

## Conclusion

With these protocols, the internet can operate safely and devices can communicate with each other effectively.

These concepts are key to understand if you're interested in Computer Networking. If you want to learn more about networking, you can [read this tutorial](https://www.freecodecamp.org/news/computer-networking-how-applications-talk-over-the-internet/).

