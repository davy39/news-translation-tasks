---
title: What is a LAN? The Local Area Network Explained in Plain English
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-07-20T20:24:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-lan-local-area-network-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/server-311338_640.png
tags:
- name: computer networking
  slug: computer-networking
- name: network
  slug: network
seo_title: null
seo_desc: 'A local area network (LAN) is really nothing more than a structure for
  organizing and protecting network communications for all the devices running within
  a single home or office.

  Let me break that down a bit. When I say, within a single home or offi...'
---

A local area network (LAN) is really nothing more than a structure for organizing and protecting network communications for all the devices running within a single home or office.

Let me break that down a bit. When I say, _within a single home or office_, I mean all the devices that are connected through either a physical or wireless connection to a network router. That router might be a WiFi access point or the modem your internet service provider (ISP) gave you. 

By _organizing_ I mean each device is given an identifying address, and its access to the internet beyond your local network is defined. 

And by _protecting_ I mean that, generally, traffic requests directed at your devices from external networks will be scanned and filtered to help prevent unauthorized and potentially dangerous access. 

Based in part on [content from my Linux in Action book](https://www.amazon.com/gp/product/1617294934/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1617294934&linkCode=as2&tag=projemun-20&linkId=1a460c0cd9a39e01821133b90632cba8), I'll try to explain how all that works.

# IPv4 addressing

Here's how that might look. The Router in this image has a _public_ IP address of 183.23.100.34 to which all incoming and outgoing traffic is associated. 

At the same time, the router acts as a Dynamic Host Configuration Protocol (DHCP) server, assigning _private_ IP addresses to all the PCs, laptops, smartphones, and servers in the house. The devices will use those addresses whenever they talk to each other.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/lan-figure1.png)
_A typical local area network (LAN) topography_

Notice how all the local devices are described as using something called "NAT IP addresses." NAT stands for Network Address Translation, and it's the method used for organizing devices within a private LAN. 

But why? What's wrong with giving all devices the same kind of public IP address the router has?

In the beginning, there was IPv4. IPv4 addresses are 32-bit numbers made up of four 8-bit octets separated by dots. Here's what that might look like:

```
192.168.1.10

```

# Subnet notation

Because it’s critically important to make sure systems know what kind of subnet a network address is on, we need a standard notation that can accurately communicate which octets are part of the network and which are available for devices. 

There are two commonly used standards: Classless Inter-Domain Routing (CIDR) notation and netmask. 

Using CIDR, one network might be represented as 192.168.1.0/24. The /24 tells you that the first three octets (8×3=24) make up the network portion, leaving only the fourth octet for device addresses. The second network (or subnet), in CIDR, would be described as 192.168.2.0/24.

These same two networks could also be described through a netmask of 255.255.255.0. That means all 8 bits of each of the first three octets are used by the network, but none of the fourth.

# Understanding private networks

In theory, the IPv4 protocol allows for around four billion unique addresses, ranging from 1.0.0.0 to 255.255.255.255. 

But even if all four billion of those addresses were practically available, it still wouldn't come close to covering each of the billions of cell phones, billions of laptop and desktop computers, and billions more network-connected cars, appliances, and Internet of Things devices that are already out there. To say nothing of the billions more that're coming soon.

So network engineers set aside three ranges of IPv4 addresses to be used exclusively in private networks. Devices using any address from those ranges will not be directly reachable from the public internet and will not be able to access internet resources. These are the three ranges:

```
Between 10.0.0.0 and 10.255.255.255
Between 172.16.0.0 and 172.31.255.255
Between 192.168.0.0 and 192.168.255.255

```

Remember what the "T" in NAT stood for? It was "Translation." What that means is that a NAT-enabled router will take the private IP addresses used in traffic requests between the LAN and the internet and _translate_ them to the router's own public address. The router, true to its name, will then _route_ those requests to their appropriate destinations.

This simple redesign of network addressing saved many billions of addresses for use with devices - like cell phones - that weren't part of a private network. All those laptops, PCs, and so on running in all those homes and offices would conveniently (and seamlessly) share their routers' public IPs.

Problem solved? Well, not quite. You see, even with all that efficient use of addresses, there still won't be enough for the explosion of public-facing devices coming online. To manage that problem, more network engineers came up with the _IPv6_ protocol. Here's what an IPv6 address might look like:

```
2002:0df6:0001:004b:0100:6c2e:0370:7234

```

That looks nasty, doesn't it? And it looks like it's a much bigger number than that wimpy IPv4 example from before.

Yup and yup. I've gotten pretty good at remembering some kinds of IPv4 addresses, but I've never even tried to "download" one of these monsters. 

For one thing, it's hexadecimal, meaning it uses the numbers between 0 and 9 _and_ the first six letters of the alphabet (a-f)! Besides that, there are eight octets rather than four, and the address is 128-bit rather than 32-bit.

All of which means that, once the protocol is fully implemented, we won't be at risk of running out of addresses for a very, very long time (meaning: forever). And what _that_ means is that, from the perspective of address allocation, there's no longer any need for private NAT networks. 

Although, for security considerations, you'll still want to give your devices some protection within your LAN.

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com/)._

