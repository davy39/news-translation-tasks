---
title: Understanding VPC Architecture – How to Secure AWS EC2 Instances
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-02T13:33:22.000Z'
originalURL: https://freecodecamp.org/news/understanding-vpc-architecture-securing-aws-ec2-instances
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-sevenstorm-juhaszimrus-425160.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: computer networking
  slug: computer-networking
seo_title: null
seo_desc: "AWS Virtual Private Clouds (VPCs) are the organizing structure of most\
  \ AWS network operations. Without a clear understanding of how they work, it'll\
  \ be hard to get security and efficiency quite right. \nBut before talking about\
  \ VPCs directly, I'm goin..."
---

AWS Virtual Private Clouds (VPCs) are the organizing structure of most AWS network operations. Without a clear understanding of how they work, it'll be hard to get security and efficiency quite right. 

But before talking about VPCs directly, I'm going to take a minute or two to refresh your memories on the basics of TCP/IP networking architecture and NAT addressing. 

But feel free to skip the next bit if you're already dug in on all that. When that's behind us, though, I'll show you what building VPCs in AWS looks like. 

## A Quick TCP/IP Primer

Ok. So TCP stands for Transmission Control Protocol and IP stands for Internet Protocol. If those sound a bit broad – almost as if they're trying to describe the totality of the internet – it's because just about everything we do on the internet is indeed controlled by these half century-old TCP/IP protocols.

This article comes from my [Securing Your AWS EC2 Instances course](https://www.udemy.com/course/securing-amazon-ec2-instances/?referralCode=E3ACB9DC5E3B77853E63). If you'd like, you can follow the video version here:

%[https://www.youtube.com/watch?v=iCal_Tzvg9g&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

For our purposes, remember that every network-connected device must have a unique IP address. Given that, mathematically, there can be no more than four billion 32-bit IPv4 addresses, and that there are already far more than four billion network-connected devices on the internet, something had to change. 

```
A typical IPv4 address:
192.168.2.45
```

The 128-bit IPv6 protocol was eventually introduced to allow _trillions_ of unique addresses. We'll never run out of those. 

```
A typical IPv6 address:
fd42:e265:3791:64f9:216:3eff:fe54:fcfe/64
```

But before IPv6, another brilliant solution was introduced: NAT networking. 

## What is Network Address Translation (NAT)?

The NAT protocol sets aside three network segments for use in _private_ networks only. Using NAT, your home can have 15 or 20 devices – including laptops, smartphones on WiFi, network printers, routers, and maybe a smart fridge or two – but between them, they'll use up only a single public IP address. 

How does that work? Well, your internet service provider will assign that one public IP to the modem they send you. But that modem will act as a DHCP server and assign each _local_ device a _private_ IP address from one of those three network segments. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-31.png)
_A typical NAT architecture_

The DHCP server will _translate_ all requests moving between your local devices and internet-based services in a way that leaves those internet services thinking that your device's IP is actually the single public one. 

But incoming network packets are actually delivered right to your device using its local NAT address. The system really is brilliant. And it added decades of life to the IPv4 system.

But once we have NAT in place anyway, it can actually do a whole lot more than just translate local addressing. Which brings us to why we're talking about this stuff in the context of EC2 instance security in the first place. 

You see, NAT allows for very sophisticated network segmenting. By carefully configuring addressing and routing rules, you can turn a single local network into a multi-layered, highly-secured environment for mission-critical enterprise deployments. 

Here's an illustration of a replicated environment using public and private subnets from AWS documentation.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/bastion_aws.png)
_How bastion hosts might fit into an AWS VPC_

The only connection with the outside world, such a private subnet, would have flows through a bastion host and a NAT gateway living in an adjacent public subnet. Forcing everything through those two devices lets you precisely control traffic. 

The bastion host provides a jump box allowing admins to safely open remote SSH sessions on instances running in your private subnets. And the NAT gateway allows services running on your private instances outbound access to, for example, pull software updates. Both bastion hosts and NAT gateways will incur regular usage costs, by the way.

## How to Optimize VPC Networks

Now I'll show you how all this works within the AWS ecosystem. From the VPC dashboard I can click Create VPC. Right away I've got a decision to make: do I want to build just a simple VPC where I can host some resources, or something more complicated?

If I go with VPC only, I'll just need to give the VPC a name, select my addressing environments and I'm good to go. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ec2_security8-f007434.png)
_Part of the VPC configuration interface in AWS_

But we're here to test drive the _VPC and more_ option. As you can see, that'll open up an infrastructure preview to the right that shows us exactly what will be created based on the current selections, and what they'll look like. 

Right now, as you can see, we'll get one public and one private subnet in each of two availability zones, and appropriate route tables and network connections to make everything work. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ec2_security8-f007926.png)
_Note how AWS automatically assigns logical names to new subnets_

Note how each object is automatically given a name that properly reflects the naming structure I specified. All this automatically conforms with security and availability best-practices

I can choose to specify a dedicated tenancy for new instances launched into this VPC – although, as I mentioned earlier, that probably won't be relevant for all that many cases.

The number of availability zones you configure will reflect the depth of fault tolerance your application needs. The more zones, the less chance your application goes down. 

Of course, by that same token, the more zones, the more instances you'll need to run and the more you'll spend. You can see that editing this value will have an instance impact on the subnet settings to the right.

You can similarly control the number of public and private subnets. The options available will reflect the number of availability zones you selected above. Basically, the UI makes it pretty much impossible to do something stupid – which is something I appreciate.

Adjusting the subnets within the UI will automatically update the configuration to the right. Selecting a NAT gateway will generate a new object with all the appropriate connectivity built-in. 

One last really nice tool is the fields that let us fine tune the address allocation for our subnets. This could be important if you're planning to deploy, say, large numbers of virtual containers into a couple of public subnets but nothing more than a handful of database servers in your private subnets. You'll probably need a lot more addresses in the former and fewer in the latter.

Once you fire up your VPC, it'll take just a few seconds for all the parts to fall into place. When that's done, you'll be able to navigate to the Your VPCs dashboard to confirm what's now available. 

## Wrapping Up

We covered a lot of ground in this article. You learned how VPCs can be designed to employ sophisticated routing topologies that expose and block resources to efficiently meet your operational and security needs.

Thanks for reading!

