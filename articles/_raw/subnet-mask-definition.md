---
title: Subnet Mask Definition
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-20T08:06:00.000Z'
originalURL: https://freecodecamp.org/news/subnet-mask-definition
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/denny-muller-JyRTi3LoQnc-unsplash-1.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: networking
  slug: networking
- name: Tech Terms
  slug: tech-terms
seo_title: null
seo_desc: 'A subnet mask defines the range of IP addresses that can be used within
  a network or subnet. It also separates an IP address into two parts: network bits
  and host bits.

  Subnet masks are used when subnetting, which is when you break a network up into
  ...'
---

A subnet mask defines the range of IP addresses that can be used within a network or subnet. It also separates an IP address into two parts: network bits and host bits.

Subnet masks are used when subnetting, which is when you break a network up into smaller networks. By adjusting the subnet mask, you can set the number of available IP addresses within a network.

For example, a common subnet mask for simple home networks is `255.255.255.0`. This subnet mask allows up to 254 usable IP addresses within the home network. In other words, up to 254 computers, phones, and other internet connected devices can connect to your router/network and access the internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/home-network-diagram-1.png)
_A simple network / subnet. Source: [What Is My IP Address?](https://www.popularmechanics.com/technology/a32729384/how-to-find-ip-address/)_

Subnet masks break an IP address up into network bits and host bits. When a device sees the network and host bits of another device's IP address, it can figure out if the other device is part of the same network (home, business, etc.), or is somewhere else online

![Image](https://www.freecodecamp.org/news/content/images/2021/04/network-and-host-bits-2.png)
_An IP address and subnet mask. Source: [IPv4](https://support.huawei.com/enterprise/en/doc/EDOC1100145159)_

Check out [this article](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/) for more information about subnets, subnet masks, and how they work.  


## Related Tech Terms:

* [Subnet Definition](https://www.freecodecamp.org/news/subnet-definition/)

