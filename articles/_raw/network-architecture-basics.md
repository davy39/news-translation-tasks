---
title: Learn Network Architecture Basics for Beginners
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-04-11T19:05:27.000Z'
originalURL: https://freecodecamp.org/news/network-architecture-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-brett-sayles-2881232.jpg
tags:
- name: architecture
  slug: architecture
- name: computer network
  slug: computer-network
- name: Security
  slug: security
seo_title: null
seo_desc: "Networking is engineering, magic, and skilled trade all rolled into one.\
  \ Getting all the countless pieces to talk nicely – and reliably – to each other\
  \ is complicated. Troubleshooting unexpected outages is worse. \nBut, once you've\
  \ got it all running ..."
---

Networking is engineering, magic, and skilled trade all rolled into one. Getting all the countless pieces to talk nicely – and reliably – to each other is complicated. Troubleshooting unexpected outages is worse. 

But, once you've got it all running nicely, well that's when you should really be worried: because that's exactly when the bad guys start banging away at the door trying to find a way in.

In this article we're going to cover just enough of the most important networking fundamentals so that discussions of network security that you may encounter will make sense. 

This article comes from [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). You can also follow along using this video:

%[https://www.youtube.com/watch?v=tsAEFWVJKsc&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=5]

## Understanding IPv4 and NAT Routing

IP networks (where IP stands for Internet Protocol) are the backbone of the Internet, connecting devices and transmitting data over the network.

IP is responsible for routing data packets from one device to another, and IP version 4 is the most widely used IP address format. IPv4 uses a 32-bit address, and consists of four 8-bit numbers called octets. IPv4 addresses are written in a decimal notation where each octet is separated by a dot.

An example of an IPv4 host address might look something like this:

```
192.168.2.34
```

Network Address Translation is a method used to allow private IPv4 addresses to access the Internet. NAT maps private IP addresses to a single public IP address, which is assigned by an Internet Service Provider (ISP). 

When a device in a private network wants to access the Internet, it sends a request to the NAT gateway. The NAT gateway translates the private IP address of the device into the public IP address assigned by the ISP and forwards the request to the Internet.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-11.png)
_NAT addressing explained in a diagram_

When the response from the Internet is received, the NAT gateway translates the public IP address back into the private IP address of the device and sends the response to the device. 

In this way, NAT enables multiple devices in a private network to share a single public IP address and access the Internet, while hiding their private IP addresses from the public. NAT also provides a basic level of security by hiding the internal network from the Internet.

## Understanding IPv6

IP version 6 is the latest IP address format. IPv6 uses a 128-bit address, and is made up of eight 16-bit hexadecimal segments separated by colons.

Here is an example of what an IPv6 address might look like:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

IPv6 was created because we were running out of IPv4 addresses – since IPv4's 32-bit addresses allow for a maximum of only 4.3 billion unique addresses. 

This was great in the early days of the Internet, but as the number of Internet-connected devices has grown, the demand for unique IP addresses has surpassed the number available in the IPv4 address space.

To address this shortage, IPv6 was developed with its larger address space, allowing for 340 trillion, trillion, trillion unique addresses. This large address space ensures that there will be enough unique IP addresses for all Internet-connected devices forever. Literally.

Additionally, IPv6 addresses overcome some other limitations of IPv4, such as improved security, auto-configuration, and support for hierarchical address allocation and routing.

## Defining Routing Protocols

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the most common transport layer protocols used in IP networks. 

TCP is a reliable connection-oriented protocol that provides error-checking and flow control. UDP is a connectionless protocol that provides fast data transmission but with less reliability.

ICMP (Internet Control Message Protocol) is a network layer protocol used to send error messages, test network connectivity (in particular, through a tool called `ping`), and perform other functions.

DHCP (Dynamic Host Configuration Protocol) is a protocol used to dynamically assign IP addresses to devices on a network. In a home or small business network, DHCP is usually performed by a router or a dedicated DHCP server, which is responsible for dynamically assigning IP addresses to devices on the network.

Here's how the process of DHCP typically works:

* When a device connects to the network, it broadcasts a request for an IP address.
* The DHCP server receives the request and assigns a unique IP address to the device, along with other network information such as the subnet mask, default gateway, and DNS server addresses.
* The device receives the assigned IP address and other network information from the DHCP server and uses it to configure its network settings.
* Finally, the DHCP server maintains a table of assigned IP addresses and the devices that have been assigned them, so it can ensure that each device on the network has a unique IP address.

In a home or small business network, the router or DHCP server is usually configured to automatically assign IP addresses to devices on the network. This eliminates the need for manual IP address configuration and makes it easy for devices to connect to the network.

With those basics, you'll be in a much better position to understand the stuff you hear and read about network security issues. 

This article and the accompanying video are excerpted from [my Complete LPI Security Essentials Exam Study Guide course](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/).

