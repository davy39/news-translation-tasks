---
title: How to Use the Traceroute and Ping Commands to Troubleshoot Network Connectivity
  Issues
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-04T23:46:48.000Z'
originalURL: https://freecodecamp.org/news/traceroute-and-ping
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-pixabay-163064--1-.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Network Engineering
  slug: network-engineering
seo_title: null
seo_desc: "By Megan Kaczanowski\nPing and traceroute are common commands you can use\
  \ to troubleshoot network problems. \nPing is a simple command that can test the\
  \ reachability of a device on the network. \nTraceroute is a command you use to\
  \ 'trace' the route that..."
---

By Megan Kaczanowski

Ping and traceroute are common commands you can use to troubleshoot network problems. 

Ping is a simple command that can test the reachability of a device on the network. 

Traceroute is a command you use to 'trace' the route that a packet takes when traveling to its destination. It's useful for tracing network problems, discovering where connections fail, and tracking down latency problems. 

## How does ping work? 

Ping uses ICMP (Internet Control Message Protocol) Echo messages to see if a remote host is active or inactive, how long a round trip message takes to reach the target host and return, and any packet loss. 

It sends a request and waits for a reply (which it receives if the destination responds back within the timeout period). 

It's basically a quick, easy way to verify that you can reach a destination on the internet. If you can, great! If not, you can use traceroute to investigate what's happening at every step between your device and the destination.

### Example ping command and results:

hostname ~ % ping -c 5 www.google.com

PING www.google.com (216.58.212.228): 56 data bytes

_The ping command, set to send 5 packets to google.com._

64 bytes from 216.58.212.228: icmp_seq=0 ttl=113 time=42.262 ms

64 bytes from 216.58.212.228: icmp_seq=1 ttl=113 time=34.796 ms

64 bytes from 216.58.212.228: icmp_seq=2 ttl=113 time=35.805 ms

64 bytes from 216.58.212.228: icmp_seq=3 ttl=113 time=45.299 ms

64 bytes from 216.58.212.228: icmp_seq=4 ttl=113 time=150.292 ms

_This shows the results from each individual ping, with their round trip time in milliseconds._

--- www.google.com ping statistics ---

5 packets transmitted, 5 packets received, 0.0% packet loss

round-trip min/avg/max/stddev = 34.796/61.691/150.292/44.474 ms

_The stats from the entire test - the minimum time it took to reach the destination, the average, the maximum, and the standard deviation._

## How does traceroute work?

By default, traceroute sends three packets of data to test each 'hop' (when a packet is passed between routers it is called a 'hop'). 

It will first send 3 packets to an unreachable port on the target host, each with a Time-To-Live (TTL) value of 1. This means that as soon as it hits the first router in the path (within your network), it will timeout. The first router will respond with an ICMP Time Exceeded Message (TEM), as the datagram has expired. 

Then another 3 datagrams are sent, with the TTL set to 2, causing the second router (your ISP) in the path to respond with an ICMP TEM. 

This continues until the datagrams eventually have a TTL long enough to reach the destination. When it does, as the messages are being sent to an invalid port, an ICMP port unreachable message is returned, signaling that the traceroute is finished. 

In this case, an error message is actually expected behavior, not a sign that something has gone wrong.

The most important part of a traceroute is usually the round trip times. Ideally you're looking for consistent times over the course of the trace. 

If you see times suddenly increase (elevated latency) on a specific hop, and continue to increase as the trace approaches the target, this may indicate a problem starting with the sudden increase. 

However, if there is elevated latency in the middle, but it remains consistent toward the end, or if the elevated latency decreases toward the end, that doesn't necessarily indicate a problem.

If you see high latency at the beginning of the trace, it may indicate a problem with your local network. You should work with your local admin (or yourself, if you are your own local admin) to fix it. By default, Windows uses ICMP to transmit the data while Linux uses UDP.

### Example traceroute command and result:

hostname ~ % traceroute www.google.com 

traceroute to www.google.com (216.58.212.228), 64 hops max, 52 byte packets

_The command to traceroute to google._

1  homerouter.cpe (192.168.8.1)  10.129 ms  1.528 ms  1.373 ms

_The first hop is within a local network. Here, we have the hop number (1), the domain name/IP address (in this case a home router), then RTT1, RTT2, and RTT3 (Round Trip Time - the time it takes for a packet to get to the hop and back to the computer, in milliseconds). This is the latency of the hop._ 

_There are three numbers because, by default, the command sends three data packets. In general, times over 150ms are unusual for a trip within the continental US, though signals crossing an ocean may exceed this time._

2  * * *

_Hop 2: There are two possibilities for stars like this - either ICMP/UDP were not configured on the receiving device and it did not respond, or the packets were dropped due to a network issue (such as a firewall or packet timeouts)._ 

_In this case, as it's very close to the beginning of the trace, it's likely that this is due to the device not being configured to send responses to a traceroute._

3  192.168.213.21 (192.168.213.21)  26.641 ms  31.671 ms  26.824 ms

4  192.168.213.22 (192.168.213.22)  20.294 ms  22.496 ms  19.922 ms

5  * * *

6  * * *

_These stars, further along in the trace, are more likely to be due to a target's firewall  blocking requests (though HTTP requests should still be able to be processed in most cases), a possible connection problem, or a return path issue (that is, the signal is reaching the router, but isn't getting a response)._

_The trace will then continue until it reaches the target._

## Wrapping Up

In summary, ping is a (very) fast way to tell if a host is reachable over a network, while traceroute can help you diagnose connectivity problems. 

They're both useful commands to know, as understanding how they work, and what the output means, can be very helpful when troubleshooting network connectivity.

You should also know how to use them for networking or security interviews, where questions like 'what port does ping work over (it's a trick question as ping uses ICMP)?' are commonly asked.  


