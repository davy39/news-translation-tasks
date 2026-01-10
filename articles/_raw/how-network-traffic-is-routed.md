---
title: How Network Traffic is Routed
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-04-19T22:23:29.000Z'
originalURL: https://freecodecamp.org/news/how-network-traffic-is-routed
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-barry-tan-7994953.jpg
tags:
- name: computer networking
  slug: computer-networking
seo_title: null
seo_desc: "Moving around the internet – or even over a private local network – requires\
  \ all kinds of magic wand waving and sorcery. \nOr, in sightly more accurate terms,\
  \ it requires the combination of sophisticated engineering and the existence of\
  \ key standards,..."
---

Moving around the internet – or even over a private local network – requires all kinds of magic wand waving and sorcery. 

Or, in sightly more accurate terms, it requires the combination of sophisticated engineering and the existence of key standards, including network ports, the domain Name System (DNS) and routing policies. And we're going to learn how some of that works in this article.

Besides IP addresses (identifiers that could look something like `192.168.2.54` or `e80::1164:3e06:6716:7a0b/64`), network traffic can be routed between devices or even individual services running on a device using TCP and UDP ports. 

This article comes from [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). You can also follow along using this video:

%[https://www.youtube.com/watch?v=GaTTrXcO13I&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=3]

## Routing Network Traffic Using Network Ports

Ports are numbers used to identify specific applications or services running on a device. When data is transmitted over the network, the source and destination ports are included in the data packet to ensure that the data is sent to the correct application or service.

[There are 65,535 TCP and UDP ports in total](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers), each of which can be assigned to a specific application or service for communication over the Internet. 

The first 1024 ports are reserved for well-known services and are typically assigned to specific applications or services by the Internet Assigned Numbers Authority. For example, HTTP (Hypertext Transfer Protocol) uses port 80, while HTTPS (HTTP Secure) uses port 443.

The remaining ports (above 1024) are called ephemeral ports and can be used by any application or service that needs to communicate over the Internet. When a device initiates a connection, it selects an available ephemeral port to use for the duration of the connection.

Devices can also be identified by unique hardware Media Access Control addresses. MAC addresses – assigned at the link-layer of the OSI model – are used to identify devices on a local network segment and to provide a way for data to be transmitted directly to the correct device. Here's a typical MAC address:

```
40:b0:72:d4:29:ab
```

## What is the Domain Name System (DNS)?

The Domain Name System is a system used to translate human-readable domain names into IP addresses. This allows users to access websites and other Internet resources using easy-to-remember domain names instead of IP addresses. 

DNS also provides other important functions, such as mapping IP addresses to multiple domain names and directing traffic to the correct server based on the location of the user.

Forward DNS refers to the process of converting a domain name, such as "www.example.com", into an IP address, such as "192.0.2.1". Forward DNS is used by clients to resolve domain names to IP addresses, so that they can access websites, email servers, and other network services.

Reverse DNS, on the other hand, is the process of converting an IP address into a domain name. Reverse DNS is used to identify the domain name associated with a particular IP address. 

This information can be used for security purposes, such as identifying the source of an incoming network connection, or for tracking the origin of spam or malicious traffic.

Public DNS servers are operated by organizations such as Google, Cloudflare, and OpenDNS, and are available for use by anyone on the Internet. Public DNS servers are often used as an alternative to the DNS servers provided by Internet Service Providers, as they can offer faster resolution times, better security features, and increased privacy.

## Hardware Routing Devices

From a hardware perspective, traffic routing is managed through a loosely related family of networking devices. It should be noted that a single device will sometimes come with features normally identified with more than one category. 

* Switches allow multiple devices on a network to communicate with each other by forwarding data packets to the intended recipient. 
* Routers connect multiple networks together and forward data packets between them. Routers use routing tables to determine the best path for the data to take. 
* Access Points allow wireless devices to connect to a wired network. They act as a bridge between the wireless devices and the network router.

It's useful to bear in mind that a "default router" is the gateway IP address used by devices on a network to communicate with devices on a different network. The default router is typically the IP address of the network router.

## Wrapping Up

Understanding the software and hardware tools used to connect all of our many devices across digital networks can help you troubleshoot when things go wrong. But it's also a critical component for understanding the problems – and solutions – involved with network security.

This article and the accompanying video are excerpted from [my Complete LPI Security Essentials Exam Study Guide course](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/).

