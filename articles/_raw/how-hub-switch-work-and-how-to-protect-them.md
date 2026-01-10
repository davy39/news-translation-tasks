---
title: Network Devices – How Hubs and Switches Work and How to Secure Them
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2022-10-27T14:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-hub-switch-work-and-how-to-protect-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Computer-Networks-Hub-Switch.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Security
  slug: security
seo_title: null
seo_desc: 'In a previous post I described every bit and byte of the Ethernet protocol.
  In this post you will learn about two network devices, how they work, and how this
  knowledge may be used by hackers.

  How Classic Ethernet Works

  Before describing the network ...'
---

In [a previous post](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/) I described every bit and byte of the Ethernet protocol. In this post you will learn about two network devices, how they work, and how this knowledge may be used by hackers.

# How Classic Ethernet Works

Before describing the network devices, consider a network without special network devices. That is, a network using classic Ethernet where all computers are attached to a single cable.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-168.png)
_Four devices connected using classic Ethernet (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

In this case, if computer A sends a message to another computer, for instance – B, the message is sent over the shared cable, and all devices receive it.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-169.png)
_With classic Ethernet, If A sends a message to B - all devices (except for A) receive this message (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Can you think of some problems with this network structure?

First, **overload –** all network frames are received by all computers. Let’s say A wants to send a frame to B. C also sees this frame, and has to realize that it is not destined to his address, and thus discard it. This process takes time and resources. The same process happens at machine D, of course.

Second, **privacy –** if C sees every message sent from A to B and vice versa, this means that the privacy is violated. We would rather have a network where only A and B see the messages sent between them.

Third, **extensibility –** this network is not really extensible. Assume that up to 10 computers can attach to this cable. What happens when you need to add one more computer? You'd have to replace the entire cable. This is expensive and inconvenient. 

Well, the person who actually has to replace the cable is probably the I.T. person - you know, the one who makes sure that everything runs well in your network and is rarely noticed until something bad happens (at least when you work in an organization large enough to have I.T. people). 

Just to be clear – we LOVE the I.T. person. We want their life to be good, we don’t want them to be running around buying cables all the time.

Fourth, **collisions** – let’s say A wants to send a message to B, and C wants to send a message to D. At the same time, both of them might start their transmission, and the messages will _collide_. 

In this case, we get errors – much like the case where two people start to speak at the same time, and it is impossible to understand either of them.

Fifth, this network structure might lead to **starvation** – let’s say that A is transmitting a frame. If the other stations wish to avoid collisions, they will refrain from sending data. But now, machine A can keep on transmitting forever, thereby taking all the bandwidth to itself and not letting any other station speak. This is called starvation.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-181.png)
_Five major problems with classic Ethernet networks (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Well, this doesn’t seem like the best network, does it?

We'll now get to know network devices that help deal with these issues.

# How Network Devices Solve These Problems

## What is a Hub?

One device that solves only the **extensibility** issue is called a **Hub**. A hub is a device with multiple ports that single Ethernet cables are connected to:  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-182.png)
_An Ethernet hub is a device with multiple ports, each connected to a single Ethernet cable (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

So now, instead of having one cable with multiple ports with many computers attached to it, we have instead a single hub, and each computer is connected to it via a single cable. This makes the I.T. person's life much easier.

The hub simply takes the pulse it receives and multiplies it – that is, sends it to all other ports. For example, if A sends a frame to B, the hub will send this frame to B, C and D – all ports except A’s port.

The hub doesn’t understand Ethernet, and doesn’t know anything about MAC addresses. For the hub, all bits are just bits transmitted over the wire, and these bits should get to all other ends.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-183.png)
_A hub simply takes a bitstream and multiplies it to all ports but the source port (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Now, if you need to add a new computer to the network, you can simply connect it to the hub. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-199.png)
_To add a new device to the network, we simply connect it to the Hub (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

What happens if the hub runs out of ports? No problem, we will connect it to another Hub, like so:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-200.png)
_In case you run out of ports, you can add another Hub (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Nice! This is a lot easier to maintain than classic Ethernet.

Yet, at least with classic hubs, all other issues still remain. Since all computers receive the frame sent from A to B, there is no **privacy**, the network is **overloaded**, **collisions** may occur, and the network is prone to **starvation**. 

What we really want is a device that, when A sends a frame to B, forwards that frame to B and **only** B. This device is called a **switch**.

## What is a Switch?

If all the stations are connected via a **switch**, and A sends a frame to B, only B receives it. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-201.png)
_With a Switch, if A sends a message to B - only B will receive it (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Notice that this means that all issues are indeed solved. The devices won’t be overloaded as every frame will get only to the relevant recipients. There are no privacy issues since, apart from the switch, only A and B see the frame. The network is easily extensible by plugging additional switches if needed.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-202.png)
_Similar to working with Hubs, the network is easily extensible by adding multiple Switches (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

The switch can avoid collisions as every connection between a switch and an endpoint is a single **collision domain** – that is, the switch will refrain from sending more than one frame on a single wire at the same time.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-204.png)
_Every connection between the Switch and another device forms an independent collision domain (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Similarly, there will be no starvation as B and C can communicate with one another while A is sending data. Even if A keeps sending frames destined to the entire network, that is the broadcast address, the switch can allow messages sent by other hosts to be transferred in between.

But, how can this magical switch operate?

Let’s say we have just bought a brand new switch and plugged it into the network. A sends a frame destined to B. How does the switch know where computer B resides?

One option would be to manually configure the switch. That is, have a table mapping between a MAC address and the relevant port, and have someone manually configure that table.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-205.png)
_The Switch may hold a table mapping MAC addresses to physical ports (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

When we say _someone_, we usually mean the I.T. person. And, well, we LOVE I.T. people. We wouldn’t want to make them do this tedious job every time. 

In addition, I don’t know about you, but most people don’t usually have an I.T. person at home for every time they plug a device into their network.

Another option would be to send a special message from the switch to every port, and then the endpoints will reply with their MAC addresses. The major downside here is that we now have to make all devices aware of the switch. We need to change the devices’ behavior so they reply to that special message.

It would be so much better if the switch were just **transparent** – no endpoint would need to know that it’s there, but it would still do the job.

Apparently, this can indeed be achieved!

Consider this network, with a brand new switch that has just been added to the network. The switch stores a table, mapping a MAC address to a physical port. This table is empty.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-206.png)
_When a Switch joins a new network, the table mapping MAC addresses to physical ports is empty (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Now, A sends a frame to B.

The switch understands Ethernet, and can look at the Frame’s header and read the **source address**. Since this source address maps to “A”, and since the message has been sent from physical port number 2, the switch adds the mapping of A’s MAC address and port number 2 to its table.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-207.png)
_When machine A sends a frame, the Switch inspects the frame, reads the source address, and maps it with the corresponding physical port (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

But what will the switch do with the frame? Well, for now, the switch doesn’t know where B resides, so the switch simply multiplies the frame and sends it to all ports, just like a hub would do. So for now, B, C and D all get the frame.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-208.png)
_Since the Switch's table doesn't include a record for B, a frame destined to B is actually sent to all ports but the source port - the same as a Hub would do (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Next, A sends another message to B. The switch looks at it, and already knows that A’s MAC address is plugged to port number 2. It still doesn’t know B, so this frame is sent to all other ports as well.

Now, C sends a frame to A. The switch looks at the **source address**, and adds the mapping between C’s MAC address and port number 5 to its table.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-209.png)
_Upon receiving a frame from C, the Switch parses its header, extracts the source address, and associates it with the corresponding physical port - port number 5 (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

This time, since the frame is destined to A’s MAC address, and since the switch knows that address – the frame can be forwarded to port number 2, and port number 2 only. Yay! 👏🏻👏🏻👏🏻

Now, B sends a message to C. The switch creates a mapping between port number 7 and B’s MAC address, which appears at the **source address** field.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-210.png)
_The Switch keeps on learning the addresses gradually, filling in its internal mappings (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

The switch can also forward the message to C, as it already knows C's address.

So, in general, the switch uses the **source address** field of Ethernet frames to dynamically learn what addresses reside behind every port.

Now, a question for you: Is it possible for two different addresses to map to a single port? For example, to have the address of computer A map to port number 3, and also have the address of computer B map to port number 3? 🤔

Well, the answer is yes. Consider the following network:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-211.png)
_A network diagram with five endpoints and three Switches (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

Now, given that the switches know the network, when A sends a message to D, it will be sent to Switch 1, and then to Switch 2, and finally forwarded by Switch 2 to D. When Switch 2 sees the frame, what address does it see in the **source address** field?

The address of computer A, of course. Notice that switches are transparent, and never modify the MAC addresses. So Switch 2 learns that the MAC address of computer A resides behind port number 3. 

Next, when computer B sends a frame to computer C, this message will also be transferred via switch 1 and then switch 2. So now, switch 2 learns that the MAC address of computer B resides behind port number 3 as well. So, in this case, both the MAC address of A and that of B reside behind port number 3. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-213.png)
_Given this network diagram, switch 2 registers both the MAC address of A as well as that of B - with port number 3 (Source: [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&amp;ab_channel=Brief))_

NOTE that a switch is **not** an additional _hop_! We are not talking about routing here. As we’ve said earlier, a switch is a **transparent** device. From the endpoints’ perspective, there is no switch – A “feels” as if it were directly connected to B, C and D.

All devices that are connected via one **hop** are said to be in the same **network segment**. So here, all computers and switches – A, B, C, D, switch 1 and switch 2 – all reside within the same segment.

In the resources section below, I’ve added a link to an exercise about hubs and switches. You are welcome to solve it in order to make sure everything is clear. If you have any questions, feel free to reach out 😊

## Interim Summary

So far you learned about two network devices. First, a hub, which is basically a first layer device. That is, it only transmits bits from one port to other ports, without understanding any protocols. 

Second, you got to know a second layer network device, namely a switch, which already "understands" the Ethernet protocol and MAC addresses. It uses that knowledge in order to transfer frames only to relevant ports, at least once it knows the network.

# Security Twist 😈

Now that you understand how hubs and switches work under the hood, it's time to consider their security implications.

Assume that I am connected to a certain Ethernet segment, and you run on computer A. B sends a message to C. Is it possible for you to see that message?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-214.png)
_Four PCs, B is sending a frame to C (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

In case the computers are connected via a hub, you certainly will see the message, as the hub simply forwards the frame to all ports (except for the source port) regardless of the destination address.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-215.png)
_A hub would simply multiply the frame and send it to A, C and D (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

Furthermore, if the computers are connected via a switch, but the switch has not yet learned the address of the destination, this message will also be sent to your port – and, in general to all ports other than the source port, just like a hub would act.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-216.png)
_A new switch acts just like a hub until it learns the destination address (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

So, in these cases, your network card will receive the frames, but will it handle them?

As I covered in [a previous tutorial](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/), the first field of an Ethernet frame is the destination address. By default, the network card will discard frames that are not destined to its address, or to a group which its system belongs to, such as the broadcast address. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-217.png)
_Ethernet frame structure - the devices first consider the destination address (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

So, by default, if your network card happens to receive a frame that was not destined to it, the frame will be discarded. This is exactly where **promiscuous mode** comes in handy. When the network card is in promiscuous mode, it will not discard frames based on their destination MAC addresses.

Now, consider a network with a switch, and that switch has already learned all addresses of the network, thereby achieving privacy.

Let’s say that a malicious person works from computer C, and wants to see the communication being sent to computer B, even though the switch forwards those frames to B only.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-218.png)
_A network with a switch that has already learned the MAC addresses and their corresponding ports. Can a malicious person see private communication? (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

Can the malicious person do something in order to steal the data?

Well, the malicious person can pretend that they have B’s address. That is, the malicious person will send a frame with the source address of B. It doesn’t really matter what the destination address of that frame would be.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-219.png)
_The malicious person sends a frame and impersonates B by specifying B's MAC address as the source address of the frame (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

Now, the switch sees a frame being sent from B’s address and from C’s port, in our diagram, port 5, and changes the mapping of B’s address to port 5. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-220.png)
_As a result, the Switch changes the port associated with B's address (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

As I mentioned earlier, it is indeed possible to have two different MAC addresses map to the same port number (for instance in case of an additional switch that connects the devices that have these addresses). But it is not possible to have B’s address mapped to two different ports.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-221.png)
_As far as the Switch is concerned, B and C may indeed both be attached to it via port 5, perhaps through another Switch (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

Now, if A sends a message to B, it will actually get to C, but not to B! 😨

This technique is called **MAC SPOOFING**. The malicious entity is said to **spoof** B’s MAC address.

Is this technique very useful for the attacker? 🤔

Well, not really. Once B sends _any_ frame at all to the network, the switch will replace the entry for B’s MAC address to that of the correct port number. So, for the attacker to keep receiving data, they will have to keep sending more frames on B’s behalf, thereby causing the switch to rewrite the table entry again and again.

This way, C will send a frame using B’s address, and the switch will map B’s MAC address to C’s port. Then, B will send a frame, and the switch will map B’s MAC address to B’s port again.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-223.png)
_Once B send any frame, the Switch will overwrite its entry and the original value will be restored (Source: [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&amp;t=3s&amp;ab_channel=Brief))_

Hence, B will receive some of the traffic, and this attack is easily noticeable.

There are many ways to defend a switch from such attacks. One would be to set the port with a maximum number of MAC addresses that are attached to it. For instance, if no other switch is supposed to be connected to a certain port, the maximum number of linked MAC addresses can be set to one.

How cool is that?! By understanding how a switch operates, we are able to estimate security issues that stem from its way of operation, as well as relevant countermeasures. 🤯

# Conclusion

In this post you learned about two important network devices, a hub and a switch. 

You learned that a hub simply multiplies the bitstream it receives to all ports other than the port that received the bitstream, whereas a switch forwards the frame only to the right port (once it has learned the network). You also learned how switches are able to achieve this ability automatically. 

Lastly, you learned about a security problem that arises from the way switches operate, and how it may be mitigated.

## About the Author

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) is [Swimm](https://swimm.io/)’s Chief Technology Officer. He's the author of the Brief [YouTube Channel](https://youtube.com/@BriefVid). He's also a cyber training expert and founder of Checkpoint Security Academy. He's the author of [Computer Networks (in Hebrew)](https://data.cyber.org.il/networks/networks.pdf). You can find him on [Twitter](https://twitter.com/Omer_Ros).

## Additional Resources

* [Computer Networks Playlist - on my Brief channel](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)
* [A DIY exercise about Hubs and Switches](https://drive.google.com/file/d/1WeHTbRNph7mevNLwGeIkys1aP6_Z-Fbk/view)

  

