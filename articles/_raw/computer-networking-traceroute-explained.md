---
title: Computer Networking — Traceroute Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/computer-networking-traceroute-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d32740569d1a4ca366d.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'According to Wikipedia, traceroute is:


  a computer network diagnostic tool for displaying the route (path) and measuring
  transit delays of packets across an Internet Protocol (IP) network. The history
  of the route is recorded as the round-trip times ...'
---

According to Wikipedia, `traceroute` is:

> a computer network diagnostic tool for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network. The history of the route is recorded as the round-trip times of the packets received from each successive host (remote node) in the route (path); the sum of the mean times in each hop is a measure of the total time spent to establish the connection. Traceroute proceeds unless all (three) sent packets are lost more than twice, then the connection is lost and the route cannot be evaluated. Ping, on the other hand, only computes the final round-trip times from the destination point.

`traceroute` can be used to find the fastest source to download data from, and is often used by penetration testers to gather information about a network.

## How data travels across the internet

Each computer on the traceroute is identified by its IP address, or its unique network connection.

```text
- The journey from one computer to another is known as a hop.
- The amount of time it takes to make a hop is measured in milliseconds.
- The information that travels along the traceroute is known as a packet.
```

Here are some important details about a traceroute:

* The path from one computer to another is called a hop
* Hops are measured in milliseconds
* Information that travels along the traceroute is called a packet

If a traceroute cannot access a computer, it will display “Request timed out.” Each hop column for computers that couldn't be accessed will display an asterisk instead of a millisecond count.

## Usage

Most implementations of `traceroute` allow the user to specify the number of queries to send each hop, the time to wait for each response, the port to use, and so on.

Here's a simple example on Linux:

```text
[root@example ~]#  traceroute -w 3 -q 1 -m 16 www.google.com
traceroute to www.google.com (216.58.200.36), 16 hops max, 60 byte packets
 1  192.168.4.2 (192.168.4.2)  0.136 ms
 2  *
 3  *
 4  *
 5  *
 6  *
 7  *
 8  *
 9  *
10  *
11  *
12  *
13  *
14  *
15  *
16  *
```

In the example above, the selected options are to wait for three seconds (instead of five), send out only one query to each hop (instead of three), limit the maximum number of hops to 16 before giving up (instead of 30), with www.google.com as the final host.

This can help identify incorrect routing table definitions or firewalls that may be blocking ICMP traffic, or high port UDP in Unix ping, to a site. Note that a firewall may permit ICMP packets but not permit packets of other protocols.

## IP Subnet Calculator

While not strictly related to traceroutes, an IP subnet calculator is a useful tool when running network diagnostics.

IP Subnet Calculators help to divide IP Networks into subnetworks by calculating appropriate network addresses, subnet masks, broadcast addresses, and host IP ranges. For simple networks (like a home LAN), it may be very easy to identify the appropriate values, but for more complex subnetting, an IP Subnet Calculator is an excellent tool.

Here are a few online IP Subnet Calculators:

* [https://www.calculator.net/ip-subnet-calculator.html](https://www.calculator.net/ip-subnet-calculator.html)
* [https://www.subnetonline.com/pages/subnet-calculators/ip-subnet-calculator.php](https://www.subnetonline.com/pages/subnet-calculators/ip-subnet-calculator.php)
* [https://www.tunnelsup.com/subnet-calculator/](https://www.tunnelsup.com/subnet-calculator/)

